"""Validate Stomach submission artwork and build actual-size confuser boards.

This is a deterministic technical-separability check, not a human recognition
test. It validates the four required proposal assets, pins every comparator by
SHA-256, compares both 18-pixel silhouettes, and generates four actual-size
comparison boards for the recognition-test packet.

Usage:
    python scripts/validate_stomach_artwork.py \
        --proposal-dir submissions/v1.11.0/stomach \
        --output-dir docs/proposals/stomach-emoji-2026/validation-v1.12
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

from PIL import Image, ImageDraw, ImageFont


NOTO_COMMIT = "8998f5dd683424a73e2314a8c1f1e359c19e8742"
NOTO_LICENSE_URL = "https://github.com/googlefonts/noto-emoji/blob/master/LICENSE"
NOTO_COMPARATORS = {
    "anatomical_heart": (
        "1fac0",
        "d085a08da7477258c7c9d97b336c1cd9890b2759da3212455d641cb88bb49673",
    ),
    "beans": (
        "1fad8",
        "e37d8c68eb71eb2eb9845e1bc57d92ebd566f01fba48c33117c9fc55a4b3d8d9",
    ),
    "meat_on_bone": (
        "1f356",
        "c35bb6b51f8abed799d429a01a90d6d82eda8c9f129a62061eec4f99ea254c35",
    ),
}
LOCAL_COMPARATORS = {
    "kidney": (
        Path("submissions/v1.11.0/kidney/images/kidney_color_18x18_SUBMIT.png"),
        Path("submissions/v1.11.0/kidney/images/kidney_color_72x72_SUBMIT.png"),
        "86da05075456926c625272323423467b1cbfc6f985791ef82e2244cc1eafbdfE".lower(),
    ),
    "liver": (
        Path("submissions/v1.11.0/liver/images/liver_color_18x18_SUBMIT.png"),
        Path("submissions/v1.11.0/liver/images/liver_color_72x72_SUBMIT.png"),
        "682cbe299bb1944c4fbe632a851655ebe78820a0be158878bc1720486a83d29f",
    ),
}
EXPECTED_ASSETS = {
    "stomach_color_18x18_SUBMIT.png": (18, 18, False),
    "stomach_color_72x72_SUBMIT.png": (72, 72, False),
    "stomach_bw_18x18_SUBMIT.png": (18, 18, True),
    "stomach_bw_72x72_SUBMIT.png": (72, 72, True),
}
MAX_NORMALIZED_IOU = 0.72
MIN_DHASH_DISTANCE = 16


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def download_noto(codepoint: str, expected_sha256: str) -> tuple[Image.Image, str]:
    url = (
        "https://raw.githubusercontent.com/googlefonts/noto-emoji/"
        f"{NOTO_COMMIT}/png/128/emoji_u{codepoint}.png"
    )
    request = urllib.request.Request(url, headers={"User-Agent": "medicalemoji-validator/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    actual_sha256 = sha256_bytes(data)
    if actual_sha256 != expected_sha256:
        raise ValueError(
            f"Comparator hash mismatch for U+{codepoint.upper()}: "
            f"expected {expected_sha256}, got {actual_sha256}"
        )
    return Image.open(io.BytesIO(data)).convert("RGBA"), url


def generic_blob(size: int) -> Image.Image:
    scale = size / 72
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    points = [
        (round(13 * scale), round(39 * scale)),
        (round(17 * scale), round(22 * scale)),
        (round(31 * scale), round(12 * scale)),
        (round(50 * scale), round(16 * scale)),
        (round(61 * scale), round(31 * scale)),
        (round(58 * scale), round(51 * scale)),
        (round(43 * scale), round(62 * scale)),
        (round(24 * scale), round(58 * scale)),
    ]
    draw.polygon(points, fill=(190, 62, 76, 255))
    return image


def foreground_mask(image: Image.Image, threshold: int = 32) -> list[list[bool]]:
    rgba = image.convert("RGBA")
    return [
        [
            rgba.getpixel((x, y))[3] > threshold
            and not all(channel >= 248 for channel in rgba.getpixel((x, y))[:3])
            for x in range(rgba.width)
        ]
        for y in range(rgba.height)
    ]


def normalize_mask(image: Image.Image) -> list[list[bool]]:
    source_mask = foreground_mask(image)
    alpha = mask_image(source_mask)
    bbox = alpha.getbbox()
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


def visible_palette(image: Image.Image) -> list[tuple[int, int, int]]:
    return sorted(
        {
            pixel[:3]
            for pixel in image.convert("RGBA").get_flattened_data()
            if pixel[3] > 0
        }
    )


def validate_asset(path: Path, expected: tuple[int, int, bool]) -> dict[str, Any]:
    expected_width, expected_height, must_be_black_and_white = expected
    image = Image.open(path).convert("RGBA")
    palette = visible_palette(image)
    components = connected_components(foreground_mask(image))
    visible_count = sum(components)
    largest_share = components[0] / visible_count if visible_count else 0.0
    dimensions_pass = image.size == (expected_width, expected_height)
    palette_pass = not must_be_black_and_white or set(palette).issubset(
        {(0, 0, 0), (255, 255, 255)}
    )
    connectedness_pass = len(components) <= 2 and largest_share >= 0.95
    return {
        "file": path.name,
        "sha256": sha256_path(path),
        "dimensions": list(image.size),
        "expected_dimensions": [expected_width, expected_height],
        "dimensions_pass": dimensions_pass,
        "black_and_white_required": must_be_black_and_white,
        "visible_rgb_count": len(palette),
        "visible_rgb_values": [list(color) for color in palette] if must_be_black_and_white else None,
        "palette_pass": palette_pass,
        "connected_components": len(components),
        "largest_component_share": round(largest_share, 4),
        "connectedness_pass": connectedness_pass,
        "pass": dimensions_pass and palette_pass and connectedness_pass,
    }


def monochrome(image: Image.Image, size: int) -> Image.Image:
    rgba = image.convert("RGBA")
    rgba.thumbnail((size, size), Image.Resampling.LANCZOS)
    mask = foreground_mask(rgba)
    alpha = mask_image(mask)
    result = Image.new("RGBA", rgba.size, (0, 0, 0, 0))
    result.paste((0, 0, 0, 255), (0, 0, rgba.width, rgba.height), alpha)
    return result


def make_board(
    output_path: Path,
    title: str,
    items: list[tuple[str, Image.Image]],
    glyph_size: int,
    black_and_white: bool,
) -> None:
    font = ImageFont.load_default()
    cell_width = 132 if glyph_size == 18 else 142
    canvas = Image.new("RGB", (cell_width * len(items), 180 if glyph_size == 18 else 245), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text((12, 10), title, fill="black", font=font)
    top = 70 if glyph_size == 18 else 62
    for index, (label, source) in enumerate(items):
        x0 = index * cell_width
        draw.rectangle(
            (x0 + 8, 38, x0 + cell_width - 8, canvas.height - 12),
            outline=(205, 209, 216),
            fill=(247, 248, 250),
        )
        glyph = monochrome(source, glyph_size) if black_and_white else source.convert("RGBA")
        if glyph.size != (glyph_size, glyph_size):
            glyph = glyph.resize((glyph_size, glyph_size), Image.Resampling.LANCZOS)
        glyph_x = x0 + (cell_width - glyph_size) // 2
        canvas.paste(glyph, (glyph_x, top), glyph)
        text_box = draw.textbbox((0, 0), label, font=font)
        text_width = text_box[2] - text_box[0]
        draw.text((x0 + (cell_width - text_width) // 2, canvas.height - 34), label, fill="black", font=font)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)


def load_comparators(repo_root: Path) -> tuple[dict[str, dict[int, Image.Image]], list[dict[str, Any]]]:
    comparators: dict[str, dict[int, Image.Image]] = {}
    manifest: list[dict[str, Any]] = []
    for name, (codepoint, expected_hash) in NOTO_COMPARATORS.items():
        image, url = download_noto(codepoint, expected_hash)
        comparators[name] = {
            18: image.resize((18, 18), Image.Resampling.LANCZOS),
            72: image.resize((72, 72), Image.Resampling.LANCZOS),
        }
        manifest.append(
            {
                "name": name,
                "kind": "Noto Emoji",
                "source_url": url,
                "source_sha256": expected_hash,
                "license_url": NOTO_LICENSE_URL,
            }
        )
    for name, (path_18, path_72, expected_hash_18) in LOCAL_COMPARATORS.items():
        absolute_18 = repo_root / path_18
        absolute_72 = repo_root / path_72
        actual_hash = sha256_path(absolute_18)
        if actual_hash != expected_hash_18:
            raise ValueError(
                f"Local comparator hash mismatch for {name}: expected {expected_hash_18}, got {actual_hash}"
            )
        comparators[name] = {
            18: Image.open(absolute_18).convert("RGBA"),
            72: Image.open(absolute_72).convert("RGBA"),
        }
        manifest.append(
            {
                "name": name,
                "kind": "Medical Emoji project proposal asset",
                "source_path_18": path_18.as_posix(),
                "source_path_72": path_72.as_posix(),
                "source_sha256_18": actual_hash,
                "source_sha256_72": sha256_path(absolute_72),
                "license": "Medical Emoji project artwork; see submissions/v1.11.0/ARTWORK-LICENSE.md",
            }
        )
    generic_18 = generic_blob(18)
    generic_72 = generic_blob(72)
    buffer = io.BytesIO()
    generic_18.save(buffer, format="PNG")
    comparators["generic_organ"] = {18: generic_18, 72: generic_72}
    manifest.append(
        {
            "name": "generic_organ",
            "kind": "deterministic test control",
            "source": "scripts/validate_stomach_artwork.py:generic_blob",
            "source_sha256_18": sha256_bytes(buffer.getvalue()),
            "license": "Original Medical Emoji project test asset",
        }
    )
    return comparators, manifest


def build_report(proposal_dir: Path, output_dir: Path, repo_root: Path) -> dict[str, Any]:
    images_dir = proposal_dir / "images"
    asset_results = [
        validate_asset(images_dir / filename, expected)
        for filename, expected in EXPECTED_ASSETS.items()
    ]
    comparators, manifest = load_comparators(repo_root)
    proposal_assets = {
        "color": {
            18: Image.open(images_dir / "stomach_color_18x18_SUBMIT.png").convert("RGBA"),
            72: Image.open(images_dir / "stomach_color_72x72_SUBMIT.png").convert("RGBA"),
        },
        "black_and_white": {
            18: Image.open(images_dir / "stomach_bw_18x18_SUBMIT.png").convert("RGBA"),
            72: Image.open(images_dir / "stomach_bw_72x72_SUBMIT.png").convert("RGBA"),
        },
    }

    silhouette_results: list[dict[str, Any]] = []
    for mode in ("color", "black_and_white"):
        proposal_mask = normalize_mask(proposal_assets[mode][18])
        proposal_hash = difference_hash(proposal_mask)
        for comparator_name, sizes in comparators.items():
            comparator_mask = normalize_mask(sizes[18])
            iou = intersection_over_union(proposal_mask, comparator_mask)
            distance = hamming_distance(proposal_hash, difference_hash(comparator_mask))
            passed = iou <= MAX_NORMALIZED_IOU and distance >= MIN_DHASH_DISTANCE
            silhouette_results.append(
                {
                    "proposal_asset": f"stomach_{mode}_18x18",
                    "comparator": comparator_name,
                    "normalized_iou": round(iou, 3),
                    "dhash_distance_64": distance,
                    "max_iou": MAX_NORMALIZED_IOU,
                    "min_dhash_distance": MIN_DHASH_DISTANCE,
                    "pass": passed,
                }
            )

    labels = [("Stomach", proposal_assets["color"][18])] + [
        (name.replace("_", " ").title(), comparators[name][18]) for name in comparators
    ]
    labels_72 = [("Stomach", proposal_assets["color"][72])] + [
        (name.replace("_", " ").title(), comparators[name][72]) for name in comparators
    ]
    make_board(output_dir / "comparison-color-18.png", "Color, actual 18x18", labels, 18, False)
    make_board(output_dir / "comparison-bw-18.png", "Black and white, actual 18x18", labels, 18, True)
    make_board(output_dir / "comparison-color-72.png", "Color, actual 72x72", labels_72, 72, False)
    make_board(output_dir / "comparison-bw-72.png", "Black and white, actual 72x72", labels_72, 72, True)

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
        "assets": asset_results,
        "comparator_manifest": manifest,
        "silhouette_comparisons": silhouette_results,
        "comparison_boards": [
            "comparison-color-18.png",
            "comparison-bw-18.png",
            "comparison-color-72.png",
            "comparison-bw-72.png",
        ],
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
            asset=item["proposal_asset"].replace("stomach_", ""),
            comparator=item["comparator"].replace("_", " "),
            iou=item["normalized_iou"],
            distance=item["dhash_distance_64"],
            result="PASS" if item["pass"] else "FAIL",
        )
        for item in report["silhouette_comparisons"]
    )
    comparator_lines = "\n".join(
        f"- {item['name'].replace('_', ' ')}: `{item.get('source_sha256', item.get('source_sha256_18'))}`"
        for item in report["comparator_manifest"]
    )
    status = "PASS" if report["overall_pass"] else "FAIL"
    return f"""# Stomach Artwork Computer Validation

Validation date: {report['validation_date']}

Status: **{status}**

## Scope

This deterministic test validates exact dimensions, a true black-and-white palette, foreground connectedness,
and machine-visible silhouette separation from six declared confusers. It does not measure or replace human
semantic recognition.

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

## Comparator hashes

{comparator_lines}

Complete provenance and licenses are in `comparator-manifest.json`.

## Comparison boards

- `comparison-color-18.png`
- `comparison-bw-18.png`
- `comparison-color-72.png`
- `comparison-bw-72.png`

Reproduce with:

```powershell
python scripts/validate_stomach_artwork.py `
  --proposal-dir submissions/v1.11.0/stomach `
  --output-dir docs/proposals/stomach-emoji-2026/validation-v1.12
```
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    proposal_dir = args.proposal_dir.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(proposal_dir, output_dir, repo_root)
    (output_dir / "computer-validation.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "comparator-manifest.json").write_text(
        json.dumps(report["comparator_manifest"], indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "computer-validation.md").write_text(markdown_report(report), encoding="utf-8")
    print(f"Stomach artwork computer validation: {'PASS' if report['overall_pass'] else 'FAIL'}")
    print(output_dir / "computer-validation.md")
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
