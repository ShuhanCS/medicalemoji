"""Deterministically validate White Blood Cell submission artwork.

The validator checks the four required assets, hashes the editable SVG sources,
and compares the two 18x18 proposal images with pinned OpenMoji controls and a
generated generic-cell control. It measures technical separation, not human
semantic recognition.

Usage:
    python scripts/validate_white_blood_cell_artwork.py \
        --proposal-dir submissions/v1.19.0/white-blood-cell \
        --json-output submissions/v1.19.0/white-blood-cell/validation/computer-validation.json \
        --markdown-output submissions/v1.19.0/white-blood-cell/validation/computer-validation.md
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from collections import deque
from datetime import date
from pathlib import Path
from typing import Any

import cairosvg
from PIL import Image, ImageDraw


OPENMOJI_COMMIT = "d05930b34516a0a3ff00aad0288ee05364cebd8b"
OPENMOJI_LICENSE_URL = "https://github.com/hfg-gmuend/openmoji/blob/master/LICENSE"
COMPARATORS = {
    "microbe": "1F9A0",
    "drop_of_blood": "1FA78",
    "soap": "1F9FC",
    "bubbles": "1FAE7",
    "generic_cell": None,
}
EXPECTED_ASSETS = {
    "white-blood-cell_color_18x18_SUBMIT.png": (18, 18, False),
    "white-blood-cell_color_72x72_SUBMIT.png": (72, 72, False),
    "white-blood-cell_bw_18x18_SUBMIT.png": (18, 18, True),
    "white-blood-cell_bw_72x72_SUBMIT.png": (72, 72, True),
}
SOURCE_FILES = (
    "white-blood-cell_color_18_SOURCE.svg",
    "white-blood-cell_color_SOURCE.svg",
    "white-blood-cell_bw_18_SOURCE.svg",
    "white-blood-cell_bw_SOURCE.svg",
)
MAX_SILHOUETTE_IOU = 0.87
MIN_SILHOUETTE_DHASH_DISTANCE = 16
MAX_FEATURE_IOU = 0.65
MIN_FEATURE_DHASH_DISTANCE = 12


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def white_background(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    canvas = Image.new("RGBA", rgba.size, "white")
    canvas.alpha_composite(rgba)
    return canvas.convert("RGB")


def render_svg(path: Path, size: int = 18) -> Image.Image:
    data = cairosvg.svg2png(bytestring=path.read_bytes(), output_width=size, output_height=size)
    return white_background(Image.open(io.BytesIO(data)))


def generic_cell(size: int, black_and_white: bool) -> Image.Image:
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    scale = size / 72
    outer = tuple(round(value * scale) for value in (9, 9, 63, 63))
    nucleus = tuple(round(value * scale) for value in (26, 26, 46, 46))
    width = max(1, round(3 * scale))
    draw.ellipse(
        outer,
        fill="white" if black_and_white else "#dbe6e8",
        outline="black" if black_and_white else "#8ca0a6",
        width=width,
    )
    draw.ellipse(nucleus, fill="black" if black_and_white else "#6b4a99")
    return image


def binary_mask(image: Image.Image, feature_only: bool) -> list[list[bool]]:
    rgb = image.convert("RGB")
    result: list[list[bool]] = []
    for y in range(rgb.height):
        row: list[bool] = []
        for x in range(rgb.width):
            red, green, blue = rgb.getpixel((x, y))
            if feature_only:
                luminance = 0.299 * red + 0.587 * green + 0.114 * blue
                row.append(luminance < 180)
            else:
                row.append(max(abs(255 - red), abs(255 - green), abs(255 - blue)) > 12)
        result.append(row)
    return result


def mask_image(mask: list[list[bool]]) -> Image.Image:
    image = Image.new("L", (len(mask[0]), len(mask)), 0)
    for y, row in enumerate(mask):
        for x, value in enumerate(row):
            if value:
                image.putpixel((x, y), 255)
    return image


def normalize_mask(mask: list[list[bool]]) -> list[list[bool]]:
    image = mask_image(mask)
    bbox = image.getbbox()
    if bbox is None:
        raise ValueError("Image has no visible foreground")
    crop = image.crop(bbox)
    crop.thumbnail((16, 16), Image.Resampling.LANCZOS)
    canvas = Image.new("L", (18, 18), 0)
    canvas.paste(crop, ((18 - crop.width) // 2, (18 - crop.height) // 2))
    return [[canvas.getpixel((x, y)) > 32 for x in range(18)] for y in range(18)]


def difference_hash(mask: list[list[bool]]) -> list[bool]:
    resized = mask_image(mask).resize((9, 8), Image.Resampling.LANCZOS)
    return [
        resized.getpixel((x + 1, y)) > resized.getpixel((x, y))
        for y in range(8)
        for x in range(8)
    ]


def intersection_over_union(left: list[list[bool]], right: list[list[bool]]) -> float:
    intersection = 0
    union = 0
    for y in range(len(left)):
        for x in range(len(left[0])):
            intersection += left[y][x] and right[y][x]
            union += left[y][x] or right[y][x]
    return intersection / union if union else 1.0


def hamming_distance(left: list[bool], right: list[bool]) -> int:
    return sum(a != b for a, b in zip(left, right, strict=True))


def connected_components(mask: list[list[bool]]) -> list[int]:
    height = len(mask)
    width = len(mask[0])
    seen: set[tuple[int, int]] = set()
    sizes: list[int] = []
    for y in range(height):
        for x in range(width):
            if not mask[y][x] or (x, y) in seen:
                continue
            queue = deque([(x, y)])
            seen.add((x, y))
            size = 0
            while queue:
                current_x, current_y = queue.popleft()
                size += 1
                for delta_y in (-1, 0, 1):
                    for delta_x in (-1, 0, 1):
                        if delta_x == 0 and delta_y == 0:
                            continue
                        next_x = current_x + delta_x
                        next_y = current_y + delta_y
                        point = (next_x, next_y)
                        if (
                            0 <= next_x < width
                            and 0 <= next_y < height
                            and mask[next_y][next_x]
                            and point not in seen
                        ):
                            seen.add(point)
                            queue.append(point)
            sizes.append(size)
    return sorted(sizes, reverse=True)


def validate_asset(path: Path, expected: tuple[int, int, bool]) -> dict[str, Any]:
    expected_width, expected_height, must_be_black_and_white = expected
    image = Image.open(path).convert("RGB")
    visible_rgb = sorted(set(image.get_flattened_data()))
    foreground = binary_mask(image, feature_only=False)
    components = connected_components(foreground)
    visible_count = sum(components)
    largest_share = components[0] / visible_count if visible_count else 0.0
    dimensions_pass = image.size == (expected_width, expected_height)
    palette_pass = not must_be_black_and_white or set(visible_rgb).issubset(
        {(0, 0, 0), (255, 255, 255)}
    )
    # A true black-and-white cell intentionally has two substantial components:
    # the outer membrane and the connected nucleus. Reject fragmentation while
    # allowing that two-part paradigm.
    connectedness_pass = len(components) <= 2 and largest_share >= 0.50
    return {
        "file": path.name,
        "sha256": sha256(path),
        "dimensions": list(image.size),
        "expected_dimensions": [expected_width, expected_height],
        "dimensions_pass": dimensions_pass,
        "black_and_white_required": must_be_black_and_white,
        "visible_rgb_count": len(visible_rgb),
        "visible_rgb_values": [list(color) for color in visible_rgb] if must_be_black_and_white else None,
        "palette_pass": palette_pass,
        "foreground_components": len(components),
        "largest_component_share": round(largest_share, 4),
        "connectedness_pass": connectedness_pass,
        "pass": dimensions_pass and palette_pass and connectedness_pass,
    }


def comparator_image(proposal_dir: Path, name: str, variant: str) -> tuple[Image.Image, str]:
    codepoint = COMPARATORS[name]
    if codepoint is None:
        return generic_cell(18, variant == "black"), "generated by validator"
    path = proposal_dir / "comparisons" / "source" / "openmoji" / variant / f"{codepoint}.svg"
    return render_svg(path), sha256(path)


def comparison_result(proposal: Image.Image, comparator: Image.Image) -> dict[str, Any]:
    proposal_silhouette = normalize_mask(binary_mask(proposal, feature_only=False))
    comparator_silhouette = normalize_mask(binary_mask(comparator, feature_only=False))
    proposal_features = normalize_mask(binary_mask(proposal, feature_only=True))
    comparator_features = normalize_mask(binary_mask(comparator, feature_only=True))
    silhouette_iou = intersection_over_union(proposal_silhouette, comparator_silhouette)
    silhouette_distance = hamming_distance(
        difference_hash(proposal_silhouette), difference_hash(comparator_silhouette)
    )
    feature_iou = intersection_over_union(proposal_features, comparator_features)
    feature_distance = hamming_distance(difference_hash(proposal_features), difference_hash(comparator_features))
    passed = (
        silhouette_iou <= MAX_SILHOUETTE_IOU
        and silhouette_distance >= MIN_SILHOUETTE_DHASH_DISTANCE
        and feature_iou <= MAX_FEATURE_IOU
        and feature_distance >= MIN_FEATURE_DHASH_DISTANCE
    )
    return {
        "silhouette_iou": round(silhouette_iou, 3),
        "silhouette_dhash_distance_64": silhouette_distance,
        "feature_iou": round(feature_iou, 3),
        "feature_dhash_distance_64": feature_distance,
        "pass": passed,
    }


def build_report(proposal_dir: Path) -> dict[str, Any]:
    images_dir = proposal_dir / "images"
    asset_results = [
        validate_asset(images_dir / filename, expected)
        for filename, expected in EXPECTED_ASSETS.items()
    ]
    source_hashes = {filename: sha256(images_dir / filename) for filename in SOURCE_FILES}
    comparison_results: list[dict[str, Any]] = []
    for variant, marker in (("color", "color"), ("black", "bw")):
        proposal = Image.open(images_dir / f"white-blood-cell_{marker}_18x18_SUBMIT.png").convert("RGB")
        for name in COMPARATORS:
            comparator, provenance = comparator_image(proposal_dir, name, variant)
            result = comparison_result(proposal, comparator)
            comparison_results.append(
                {
                    "proposal_variant": variant,
                    "comparator": name,
                    "comparator_sha256_or_method": provenance,
                    **result,
                }
            )
    overall_pass = all(result["pass"] for result in asset_results) and all(
        result["pass"] for result in comparison_results
    )
    return {
        "schema_version": "1.0.0",
        "validation_date": date.today().isoformat(),
        "proposal_dir": proposal_dir.as_posix(),
        "method": (
            "Deterministic validation of dimensions, true black-and-white palette, foreground connectedness, "
            "source/export hashes, and silhouette plus dark-feature separation from declared confusers. "
            "This does not measure human semantic recognition."
        ),
        "thresholds": {
            "max_silhouette_iou": MAX_SILHOUETTE_IOU,
            "min_silhouette_dhash_distance_64": MIN_SILHOUETTE_DHASH_DISTANCE,
            "max_feature_iou": MAX_FEATURE_IOU,
            "min_feature_dhash_distance_64": MIN_FEATURE_DHASH_DISTANCE,
            "max_foreground_components": 2,
            "min_largest_component_share": 0.50,
        },
        "openmoji_commit": OPENMOJI_COMMIT,
        "openmoji_license_url": OPENMOJI_LICENSE_URL,
        "source_hashes": source_hashes,
        "assets": asset_results,
        "comparisons": comparison_results,
        "overall_pass": overall_pass,
    }


def markdown_report(report: dict[str, Any], proposal_dir: Path) -> str:
    asset_rows = "\n".join(
        "| {file} | {dimensions} | {palette} | {components} | {result} |".format(
            file=item["file"],
            dimensions="x".join(str(value) for value in item["dimensions"]),
            palette=("pass" if item["black_and_white_required"] else "n/a"),
            components=item["foreground_components"],
            result="PASS" if item["pass"] else "FAIL",
        )
        for item in report["assets"]
    )
    comparison_rows = "\n".join(
        "| {variant} | {comparator} | {siou:.3f} | {sdist} | {fiou:.3f} | {fdist} | {result} |".format(
            variant=item["proposal_variant"],
            comparator=item["comparator"].replace("_", " "),
            siou=item["silhouette_iou"],
            sdist=item["silhouette_dhash_distance_64"],
            fiou=item["feature_iou"],
            fdist=item["feature_dhash_distance_64"],
            result="PASS" if item["pass"] else "FAIL",
        )
        for item in report["comparisons"]
    )
    source_lines = "\n".join(f"- `{name}`: `{digest}`" for name, digest in report["source_hashes"].items())
    status = "PASS" if report["overall_pass"] else "FAIL"
    return f"""# White Blood Cell artwork computer validation

Validation date: {report['validation_date']}

Status: **{status}**

## Scope

This reproducible technical test validates the four exact assets, editable-source hashes, true
black-and-white palette, foreground connectedness, and machine-visible separation from Microbe, Drop of Blood,
Soap, Bubbles, and a generic-cell control. Actual-size comparison boards are recorded separately.

## Required assets

| Asset | Dimensions | B&W palette | Components | Result |
| --- | ---: | --- | ---: | --- |
{asset_rows}

## 18x18 comparisons

| Variant | Comparator | Silhouette IoU | Silhouette dHash | Feature IoU | Feature dHash | Result |
| --- | --- | ---: | ---: | ---: | ---: | --- |
{comparison_rows}

## Editable-source hashes

{source_lines}

OpenMoji comparators are pinned to commit `{OPENMOJI_COMMIT}`. Provenance and full URLs are in
`../comparisons/SOURCES.md`.

Reproduce with:

```powershell
python scripts/validate_white_blood_cell_artwork.py `
  --proposal-dir {proposal_dir.as_posix()} `
  --json-output {proposal_dir.as_posix()}/validation/computer-validation.json `
  --markdown-output {proposal_dir.as_posix()}/validation/computer-validation.md
```
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-dir", required=True, type=Path)
    parser.add_argument("--json-output", required=True, type=Path)
    parser.add_argument("--markdown-output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.proposal_dir)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(markdown_report(report, args.proposal_dir), encoding="utf-8")
    print(f"White Blood Cell artwork computer validation: {'PASS' if report['overall_pass'] else 'FAIL'}")
    print(args.markdown_output)
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
