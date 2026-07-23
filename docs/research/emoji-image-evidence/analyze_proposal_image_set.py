#!/usr/bin/env python3
"""Deterministically inspect the four Unicode emoji proposal image samples.

This tool records file-level evidence for any Unicode emoji proposal candidate.
It does not substitute for the blinded human recognition test specified in
proposal-image-rubric.v1.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path

from PIL import Image

SAMPLE_LABELS = ("color_18", "color_72", "bw_18", "bw_72")


def luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (channel / 255 for channel in rgb)
    channels = []
    for channel in (r, g, b):
        channels.append(channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast_ratio(first: tuple[int, int, int], second: tuple[int, int, int]) -> float:
    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def connected_components(mask: list[list[bool]]) -> int:
    height, width = len(mask), len(mask[0])
    seen = [[False] * width for _ in range(height)]
    count = 0
    for y in range(height):
        for x in range(width):
            if not mask[y][x] or seen[y][x]:
                continue
            count += 1
            queue = deque([(x, y)])
            seen[y][x] = True
            while queue:
                cx, cy = queue.popleft()
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                    if 0 <= nx < width and 0 <= ny < height and mask[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        queue.append((nx, ny))
    return count


def visible_pixels_on_background(pixels, background: tuple[int, int, int], threshold: int = 30) -> int:
    visible = 0
    for red, green, blue, alpha in pixels:
        composite = tuple(round((channel * alpha + bg * (255 - alpha)) / 255) for channel, bg in zip((red, green, blue), background))
        if max(abs(channel - bg) for channel, bg in zip(composite, background)) >= threshold:
            visible += 1
    return visible


def analyze(path: Path) -> dict:
    raw = path.read_bytes()
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    pixels = list(image.getdata())
    mask = [[pixels[y * width + x][3] >= 32 for x in range(width)] for y in range(height)]
    points = [(x, y) for y in range(height) for x in range(width) if mask[y][x]]
    bbox = None
    if points:
        xs, ys = zip(*points)
        bbox = [min(xs), min(ys), max(xs) + 1, max(ys) + 1]
    opaque_rgb = {pixel[:3] for pixel in pixels if pixel[3] >= 250}
    grayscale_opaque = all(red == green == blue for red, green, blue in opaque_rgb)
    strict_binary_opaque = opaque_rgb.issubset({(0, 0, 0), (255, 255, 255)})
    contrast = {}
    for label, background in (("white", (255, 255, 255)), ("near_black", (15, 15, 15))):
        visible = visible_pixels_on_background(pixels, background)
        opaque_contrasts = [contrast_ratio(rgb, background) for rgb in opaque_rgb]
        contrast[label] = {
            "visible_canvas_fraction": round(visible / (width * height), 4),
            "opaque_palette_min_contrast_ratio": round(min(opaque_contrasts), 2) if opaque_contrasts else None,
            "opaque_palette_max_contrast_ratio": round(max(opaque_contrasts), 2) if opaque_contrasts else None,
        }
    result = {
        "file": path.name,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_px": [width, height],
        "rgba_mode": "RGBA",
        "alpha_foreground_pixels_at_or_above_32": len(points),
        "alpha_foreground_fraction": round(len(points) / (width * height), 4),
        "alpha_bbox_xyxy": bbox,
        "alpha_bbox_fraction_of_canvas": (
            [round((bbox[2] - bbox[0]) / width, 4), round((bbox[3] - bbox[1]) / height, 4)] if bbox else None
        ),
        "alpha_components_4_connected": connected_components(mask),
        "opaque_rgb_count": len(opaque_rgb),
        "opaque_pixels_are_grayscale": grayscale_opaque,
        "opaque_palette_is_strict_black_and_white": strict_binary_opaque,
        "background_visibility": contrast,
    }
    return result


def alpha_mask(path: Path, size: tuple[int, int]):
    image = Image.open(path).convert("RGBA")
    if image.size != size:
        image = image.resize(size, Image.Resampling.LANCZOS)
    return [alpha >= 32 for alpha in image.getchannel("A").getdata()]


def mask_iou(first: list[bool], second: list[bool]) -> float:
    union = sum(a or b for a, b in zip(first, second))
    return round(sum(a and b for a, b in zip(first, second)) / union, 4) if union else 1.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--asset-set", required=True, help="Human-readable candidate and package version, for example 'Stomach proposal v1.0.0'.")
    parser.add_argument("--color-18", required=True, help="Filename of the color 18x18 PNG inside --input-dir.")
    parser.add_argument("--color-72", required=True, help="Filename of the color 72x72 PNG inside --input-dir.")
    parser.add_argument("--bw-18", required=True, help="Filename of the black-and-white 18x18 PNG inside --input-dir.")
    parser.add_argument("--bw-72", required=True, help="Filename of the black-and-white 72x72 PNG inside --input-dir.")
    args = parser.parse_args()

    filenames = {label: getattr(args, label) for label in SAMPLE_LABELS}
    paths = {label: args.input_dir / filename for label, filename in filenames.items()}
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise SystemExit("Missing expected image files:\n" + "\n".join(missing))

    analysis = {label: analyze(path) for label, path in paths.items()}
    for label, expected_size in (("color_18", [18, 18]), ("bw_18", [18, 18]), ("color_72", [72, 72]), ("bw_72", [72, 72])):
        analysis[label]["matches_required_dimensions"] = analysis[label]["size_px"] == expected_size
    for resolution, size in (("18", (18, 18)), ("72", (72, 72))):
        analysis[f"color_bw_alpha_mask_iou_{resolution}px"] = mask_iou(
            alpha_mask(paths[f"color_{resolution}"], size),
            alpha_mask(paths[f"bw_{resolution}"], size),
        )

    output = {
        "schema_version": "1.1.0",
        "dataset_version": "1.1.0",
        "asset_set": args.asset_set,
        "input_files": filenames,
        "method": "Deterministic file inspection; visual recognition must be tested separately with blinded participants.",
        "unicode_format_gate": {
            "all_required_dimensions_match": all(
                analysis[label]["matches_required_dimensions"]
                for label in ("color_18", "bw_18", "color_72", "bw_72")
            ),
            "black_and_white_samples_have_neutral_opaque_pixels": all(
                analysis[label]["opaque_pixels_are_grayscale"] for label in ("bw_18", "bw_72")
            ),
            "black_and_white_samples_have_strict_binary_opaque_palette": all(
                analysis[label]["opaque_palette_is_strict_black_and_white"] for label in ("bw_18", "bw_72")
            ),
            "note": "Unicode requires black-and-white rather than grayscale. A neutral-RGB palette can still contain many gray values, so the strict-binary field is the conservative automated check. A human must also verify that semi-transparent edge treatment does not create the appearance of shaded grayscale."
        },
        "analysis": analysis,
        "interpretation_limits": [
            "Pixel geometry and contrast cannot establish the Unicode requirement that most people recognize the intended entity without foreknowledge.",
            "A high alpha-mask overlap between color and black-and-white assets supports silhouette consistency but does not prove semantic recognition."
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
