"""Export exact Kidney proposal assets from the approved GPT Image 2 masters.

The two high-resolution masters are preserved under docs/design. This script
normalizes their white backgrounds, applies a shared square crop, and writes
the exact 72x72 and 18x18 color and true black-and-white PNGs required by the
Unicode proposal packet.

Usage:
    python scripts/export_kidney_gpt2_assets.py
    python scripts/export_kidney_gpt2_assets.py --release v1.12.0-kidney.6
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE = "v1.12.0-kidney.6"
DESIGN_DIR = ROOT / "docs" / "design" / "kidney-emoji-2026-07"
COLOR_MASTER = DESIGN_DIR / "kidney-paired-gpt-image-2-submission-master.png"
BW_MASTER = DESIGN_DIR / "kidney-paired-gpt-image-2-bw-master.png"
SMALL_SOURCE_DIR = ROOT / "submissions" / "v1.12.0-kidney.5" / "kidney" / "images"


def subject_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    rgb = image.convert("RGB")
    mask = Image.new("1", rgb.size)
    mask.putdata(
        [
            1 if min(pixel) < 232 or max(pixel) - min(pixel) > 18 else 0
            for pixel in rgb.getdata()
        ]
    )
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("Master image has no detectable foreground")
    return bbox


def shared_square_crop(color: Image.Image, bw: Image.Image) -> tuple[int, int, int, int]:
    boxes = [subject_bbox(color), subject_bbox(bw)]
    left = min(box[0] for box in boxes)
    top = min(box[1] for box in boxes)
    right = max(box[2] for box in boxes)
    bottom = max(box[3] for box in boxes)

    width = right - left
    height = bottom - top
    side = int(max(width, height) * 1.14)
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2
    crop_left = max(0, center_x - side // 2)
    crop_top = max(0, center_y - side // 2)
    crop_right = min(color.width, crop_left + side)
    crop_bottom = min(color.height, crop_top + side)
    crop_left = crop_right - side
    crop_top = crop_bottom - side
    return crop_left, crop_top, crop_right, crop_bottom


def normalize_color(image: Image.Image) -> Image.Image:
    rgb = image.convert("RGB")
    pixels = []
    for red, green, blue in rgb.getdata():
        if min(red, green, blue) >= 242 and max(red, green, blue) - min(red, green, blue) <= 14:
            pixels.append((255, 255, 255))
        else:
            pixels.append((red, green, blue))
    rgb.putdata(pixels)
    return rgb


def export_color(master: Image.Image, crop: tuple[int, int, int, int], size: int) -> Image.Image:
    resized = master.crop(crop).resize((size, size), Image.Resampling.LANCZOS)
    return normalize_color(resized)


def export_bw(master: Image.Image, crop: tuple[int, int, int, int], size: int) -> Image.Image:
    grayscale = master.crop(crop).convert("L")
    grayscale = grayscale.resize((size, size), Image.Resampling.LANCZOS)
    return grayscale.point(lambda value: 0 if value < 178 else 255, mode="1").convert("L")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", default=DEFAULT_RELEASE)
    args = parser.parse_args()

    destination = ROOT / "submissions" / args.release / "kidney" / "images"
    if not destination.is_dir():
        raise FileNotFoundError(f"Kidney image directory does not exist: {destination}")

    color = Image.open(COLOR_MASTER).convert("RGB")
    bw = Image.open(BW_MASTER).convert("RGB")
    if color.size != bw.size:
        raise ValueError(f"Master dimensions differ: color={color.size}, bw={bw.size}")

    crop = shared_square_crop(color, bw)
    color.save(destination / "kidney_color_MASTER.png", optimize=True)
    bw.save(destination / "kidney_bw_MASTER.png", optimize=True)

    export_color(color, crop, 72).save(destination / "kidney_color_72x72_SUBMIT.png", optimize=True)
    export_bw(bw, crop, 72).save(destination / "kidney_bw_72x72_SUBMIT.png", optimize=True)

    # The polished master loses its identifying asymmetry when reduced mechanically.
    # Preserve the purpose-built .5 keyboard-size assets, which already pass the
    # fixed Lungs and Beans comparisons, rather than weakening the 72px artwork.
    for filename in ("kidney_color_18x18_SUBMIT.png", "kidney_bw_18x18_SUBMIT.png"):
        shutil.copy2(SMALL_SOURCE_DIR / filename, destination / filename)

    print(f"Exported GPT Image 2 Kidney assets to {destination}")
    print(f"Shared crop: {crop}")


if __name__ == "__main__":
    main()
