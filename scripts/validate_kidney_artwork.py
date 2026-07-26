"""Deterministically validate Kidney submission artwork at emoji scale.

The validator checks the four required proposal assets and compares both 18x18
silhouettes with a pinned set of Noto Emoji references. It is intentionally a
technical separability test, not a claim about human semantic recognition.

Usage:
    python scripts/validate_kidney_artwork.py \
        --proposal-dir submissions/v1.10.0/kidney \
        --json-output submissions/v1.10.0/kidney/validation/computer-validation.json \
        --markdown-output submissions/v1.10.0/kidney/validation/computer-validation.md
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import urllib.request
from collections import deque
from datetime import date
from pathlib import Path
from typing import Any

from PIL import Image


NOTO_COMMIT = "8998f5dd683424a73e2314a8c1f1e359c19e8742"
NOTO_LICENSE_URL = "https://github.com/googlefonts/noto-emoji/blob/master/LICENSE"
COMPARATORS = {
    "anatomical_heart": ("1fac0", "d085a08da7477258c7c9d97b336c1cd9890b2759da3212455d641cb88bb49673"),
    "balloon": ("1f388", "7efbfa64b59cbee4a61a17b1d5af8887cb70dda9b94e9e8463a557fe6e01cd11"),
    "beans": ("1fad8", "e37d8c68eb71eb2eb9845e1bc57d92ebd566f01fba48c33117c9fc55a4b3d8d9"),
    "droplet": ("1f4a7", "f523b07e40891a9765bac75766fc426c4cbcf405eaf9bde95a2657971755a463"),
    "light_bulb": ("1f4a1", "3b57447c18ca9a6bd2df7f17fdf22fb5ee1135bd07fda592e2a34c705060c1c2"),
    "lungs": ("1fac1", "61dc72e8d34d51870196ae3a2fd0644a44e283781fe2ef9d9456a0d8eeec8e32"),
}
EXPECTED_ASSETS = {
    "kidney_color_18x18_SUBMIT.png": (18, 18, False),
    "kidney_color_72x72_SUBMIT.png": (72, 72, False),
    "kidney_bw_18x18_SUBMIT.png": (18, 18, True),
    "kidney_bw_72x72_SUBMIT.png": (72, 72, True),
}
MAX_NORMALIZED_IOU = 0.72
MIN_DHASH_DISTANCE = 16


def download_comparator(codepoint: str, expected_sha256: str) -> tuple[Image.Image, str]:
    url = (
        "https://raw.githubusercontent.com/googlefonts/noto-emoji/"
        f"{NOTO_COMMIT}/png/128/emoji_u{codepoint}.png"
    )
    request = urllib.request.Request(url, headers={"User-Agent": "medicalemoji-validator/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        raise ValueError(
            f"Comparator hash mismatch for U+{codepoint.upper()}: "
            f"expected {expected_sha256}, got {actual_sha256}"
        )
    return Image.open(io.BytesIO(data)).convert("RGBA"), url


def alpha_mask(image: Image.Image, threshold: int = 32) -> list[list[bool]]:
    rgba = image.convert("RGBA")
    return [
        [rgba.getpixel((x, y))[3] > threshold for x in range(rgba.width)]
        for y in range(rgba.height)
    ]


def normalize_mask(image: Image.Image) -> list[list[bool]]:
    alpha = image.convert("RGBA").getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 32 else 0).getbbox()
    if bbox is None:
        raise ValueError("Image has no visible foreground")
    crop = alpha.crop(bbox)
    crop.thumbnail((16, 16), Image.Resampling.LANCZOS)
    canvas = Image.new("L", (18, 18), 0)
    canvas.paste(crop, ((18 - crop.width) // 2, (18 - crop.height) // 2))
    return [
        [canvas.getpixel((x, y)) > 32 for x in range(18)]
        for y in range(18)
    ]


def mask_image(mask: list[list[bool]]) -> Image.Image:
    image = Image.new("L", (len(mask[0]), len(mask)), 0)
    for y, row in enumerate(mask):
        for x, value in enumerate(row):
            if value:
                image.putpixel((x, y), 255)
    return image


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
    image = Image.open(path).convert("RGBA")
    visible_pixels = [pixel for pixel in image.get_flattened_data() if pixel[3] > 0]
    visible_rgb = sorted({pixel[:3] for pixel in visible_pixels})
    mask = alpha_mask(image)
    components = connected_components(mask)
    visible_count = sum(components)
    largest_share = components[0] / visible_count if visible_count else 0.0
    dimensions_pass = image.size == (expected_width, expected_height)
    palette_pass = not must_be_black_and_white or set(visible_rgb).issubset(
        {(0, 0, 0), (255, 255, 255)}
    )
    connectedness_pass = len(components) <= 2 and largest_share >= 0.95
    return {
        "file": path.name,
        "dimensions": list(image.size),
        "expected_dimensions": [expected_width, expected_height],
        "dimensions_pass": dimensions_pass,
        "black_and_white_required": must_be_black_and_white,
        "visible_rgb_count": len(visible_rgb),
        "visible_rgb_values": (
            [list(color) for color in visible_rgb]
            if must_be_black_and_white
            else None
        ),
        "palette_pass": palette_pass,
        "connected_components": len(components),
        "largest_component_share": round(largest_share, 4),
        "connectedness_pass": connectedness_pass,
        "pass": dimensions_pass and palette_pass and connectedness_pass,
    }


def build_report(proposal_dir: Path) -> dict[str, Any]:
    images_dir = proposal_dir / "images"
    asset_results = [
        validate_asset(images_dir / filename, expected)
        for filename, expected in EXPECTED_ASSETS.items()
    ]

    comparator_images: dict[str, tuple[Image.Image, str, str]] = {}
    for name, (codepoint, expected_hash) in COMPARATORS.items():
        image, url = download_comparator(codepoint, expected_hash)
        comparator_images[name] = (image, url, expected_hash)

    silhouette_results: list[dict[str, Any]] = []
    for proposal_name in (
        "kidney_color_18x18_SUBMIT.png",
        "kidney_bw_18x18_SUBMIT.png",
    ):
        proposal_image = Image.open(images_dir / proposal_name).convert("RGBA")
        proposal_mask = normalize_mask(proposal_image)
        proposal_hash = difference_hash(proposal_mask)
        for comparator_name, (comparator_image, url, expected_hash) in comparator_images.items():
            comparator_mask = normalize_mask(comparator_image)
            iou = intersection_over_union(proposal_mask, comparator_mask)
            distance = hamming_distance(proposal_hash, difference_hash(comparator_mask))
            passed = iou <= MAX_NORMALIZED_IOU and distance >= MIN_DHASH_DISTANCE
            silhouette_results.append(
                {
                    "proposal_asset": proposal_name,
                    "comparator": comparator_name,
                    "normalized_iou": round(iou, 3),
                    "dhash_distance_64": distance,
                    "max_iou": MAX_NORMALIZED_IOU,
                    "min_dhash_distance": MIN_DHASH_DISTANCE,
                    "source_url": url,
                    "source_sha256": expected_hash,
                    "pass": passed,
                }
            )

    overall_pass = all(result["pass"] for result in asset_results) and all(
        result["pass"] for result in silhouette_results
    )
    return {
        "schema_version": "1.0.0",
        "validation_date": date.today().isoformat(),
        "proposal_dir": proposal_dir.as_posix(),
        "method": (
            "Deterministic technical validation of dimensions, black-and-white palette, foreground "
            "connectedness, normalized alpha-mask intersection-over-union, and 64-bit difference hash. "
            "This measures machine-visible separation, not human semantic recognition."
        ),
        "thresholds": {
            "max_normalized_iou": MAX_NORMALIZED_IOU,
            "min_dhash_distance_64": MIN_DHASH_DISTANCE,
            "max_connected_components": 2,
            "min_largest_component_share": 0.95,
        },
        "noto_commit": NOTO_COMMIT,
        "noto_license_url": NOTO_LICENSE_URL,
        "assets": asset_results,
        "silhouette_comparisons": silhouette_results,
        "overall_pass": overall_pass,
    }


def markdown_report(report: dict[str, Any]) -> str:
    asset_rows = "\n".join(
        "| {file} | {dimensions} | {palette} | {components} | {result} |".format(
            file=item["file"],
            dimensions="x".join(str(value) for value in item["dimensions"]),
            palette=(
                "pass"
                if item["black_and_white_required"] and item["palette_pass"]
                else "fail"
                if item["black_and_white_required"]
                else "n/a"
            ),
            components=item["connected_components"],
            result="PASS" if item["pass"] else "FAIL",
        )
        for item in report["assets"]
    )
    comparison_rows = "\n".join(
        "| {asset} | {comparator} | {iou:.3f} | {distance} | {result} |".format(
            asset=item["proposal_asset"].replace("kidney_", "").replace("_SUBMIT.png", ""),
            comparator=item["comparator"].replace("_", " "),
            iou=item["normalized_iou"],
            distance=item["dhash_distance_64"],
            result="PASS" if item["pass"] else "FAIL",
        )
        for item in report["silhouette_comparisons"]
    )
    source_lines = "\n".join(
        f"- {name.replace('_', ' ')}: "
        f"https://raw.githubusercontent.com/googlefonts/noto-emoji/{NOTO_COMMIT}/png/128/emoji_u{codepoint}.png "
        f"(SHA-256 `{expected_hash}`)"
        for name, (codepoint, expected_hash) in COMPARATORS.items()
    )
    status = "PASS" if report["overall_pass"] else "FAIL"
    return f"""# Kidney Artwork Computer Validation

Validation date: {report['validation_date']}

Status: **{status}**

## Scope

This is a deterministic technical separability test. It validates exact image dimensions, a true
black-and-white palette, foreground connectedness, and machine-visible silhouette distance from six nearby or
plausible-confusion emoji. It does not claim to measure human semantic recognition.

Thresholds were fixed before the release run: normalized silhouette IoU must be at most
`{MAX_NORMALIZED_IOU:.2f}`, 64-bit difference-hash distance must be at least `{MIN_DHASH_DISTANCE}`, foreground
components must not exceed two, and the largest component must contain at least 95% of visible pixels.

## Required assets

| Asset | Dimensions | B&W palette | Components | Result |
| --- | ---: | --- | ---: | --- |
{asset_rows}

## 18x18 silhouette comparisons

| Proposal asset | Comparator | Normalized IoU | dHash distance | Result |
| --- | --- | ---: | ---: | --- |
{comparison_rows}

## Comparator provenance

All comparators are pinned to Noto Emoji commit `{NOTO_COMMIT}`:

{source_lines}

Noto Emoji license:

{NOTO_LICENSE_URL}

Reproduce with:

```powershell
python scripts/validate_kidney_artwork.py `
  --proposal-dir submissions/v1.10.0/kidney `
  --json-output submissions/v1.10.0/kidney/validation/computer-validation.json `
  --markdown-output submissions/v1.10.0/kidney/validation/computer-validation.md
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
    args.markdown_output.write_text(markdown_report(report), encoding="utf-8")
    print(f"Kidney artwork computer validation: {'PASS' if report['overall_pass'] else 'FAIL'}")
    print(args.markdown_output)
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
