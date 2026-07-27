"""Export exact-size Liver Candidate A PNGs from the project-authored SVG masters."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image


ASSETS = (
    ("liver_color_SOURCE.svg", "liver_color_72x72_SUBMIT.png", 72, False),
    ("liver_bw_SOURCE.svg", "liver_bw_72x72_SUBMIT.png", 72, True),
    ("liver_color_18_SOURCE.svg", "liver_color_18x18_SUBMIT.png", 18, False),
    ("liver_bw_18_SOURCE.svg", "liver_bw_18x18_SUBMIT.png", 18, True),
)


def render(source: Path, size: int, bilevel: bool) -> Image.Image:
    png = cairosvg.svg2png(url=str(source), output_width=size, output_height=size)
    image = Image.open(BytesIO(png)).convert("RGB")
    if bilevel:
        image = image.convert("L").point(lambda value: 255 if value >= 210 else 0).convert("RGB")
    return image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-dir", required=True, type=Path)
    args = parser.parse_args()
    image_dir = args.proposal_dir.resolve() / "images"

    for source_name, output_name, size, bilevel in ASSETS:
        destination = image_dir / output_name
        image = render(image_dir / source_name, size, bilevel)
        image.save(destination, optimize=True)
        print(destination)


if __name__ == "__main__":
    main()
