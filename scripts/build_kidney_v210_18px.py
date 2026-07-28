#!/usr/bin/env python3
"""Build the native-grid Kidney 18x18 proposal assets and their SVG sources."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


SIZE = 18
TRANSPARENT = (0, 0, 0, 0)

OUTLINE = (92, 22, 40, 255)
MAROON = (177, 54, 67, 255)
HIGHLIGHT = (209, 88, 91, 255)
RED_VESSEL = (220, 52, 57, 255)
BLUE_VESSEL = (45, 95, 174, 255)
URETER = (207, 159, 91, 255)

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


# Hand-authored, inclusive x ranges for each scanline. The bodies deliberately face
# inward: their medial edges recede at the center, making a notch that survives at 18px.
LEFT_OUTER = {
    2: (4, 6),
    3: (3, 7),
    4: (2, 7),
    5: (2, 6),
    6: (2, 6),
    7: (2, 5),
    8: (2, 5),
    9: (2, 5),
    10: (3, 6),
    11: (3, 6),
    12: (4, 6),
}

LEFT_INNER = {
    3: (4, 6),
    4: (3, 6),
    5: (3, 5),
    6: (3, 5),
    7: (3, 4),
    8: (3, 4),
    9: (3, 4),
    10: (4, 5),
    11: (4, 5),
}

RIGHT_OUTER = {
    3: (11, 13),
    4: (10, 14),
    5: (10, 15),
    6: (11, 15),
    7: (12, 15),
    8: (12, 15),
    9: (12, 15),
    10: (11, 14),
    11: (11, 14),
    12: (12, 13),
}

RIGHT_INNER = {
    4: (11, 13),
    5: (11, 14),
    6: (12, 14),
    7: (13, 14),
    8: (13, 14),
    9: (13, 14),
    10: (12, 13),
    11: (12, 13),
}


def paint_rows(image: Image.Image, rows: dict[int, tuple[int, int]], color: tuple[int, int, int, int]) -> None:
    pixels = image.load()
    for y, (start, end) in rows.items():
        for x in range(start, end + 1):
            pixels[x, y] = color


def build_color() -> Image.Image:
    image = Image.new("RGBA", (SIZE, SIZE), TRANSPARENT)
    paint_rows(image, LEFT_OUTER, OUTLINE)
    paint_rows(image, RIGHT_OUTER, OUTLINE)
    paint_rows(image, LEFT_INNER, MAROON)
    paint_rows(image, RIGHT_INNER, MAROON)

    pixels = image.load()
    # Minimal highlights keep the two bodies readable without introducing 72px detail.
    pixels[4, 3] = HIGHLIGHT
    pixels[5, 3] = HIGHLIGHT
    pixels[12, 4] = HIGHLIGHT
    pixels[13, 5] = HIGHLIGHT

    # Central red/blue connectors visually bind the organs and echo the large example.
    for x in range(6, 12):
        pixels[x, 6] = RED_VESSEL
        pixels[x, 7] = BLUE_VESSEL
    pixels[6, 5] = RED_VESSEL
    pixels[11, 5] = RED_VESSEL

    # Two short ureters descend from the hilum without crowding the native grid.
    for y in range(8, 14):
        pixels[7, y] = URETER
        pixels[10, y] = URETER
    pixels[8, 8] = URETER
    pixels[9, 8] = URETER
    return image


def build_bw() -> Image.Image:
    image = Image.new("RGBA", (SIZE, SIZE), TRANSPARENT)
    paint_rows(image, LEFT_OUTER, BLACK)
    paint_rows(image, RIGHT_OUTER, BLACK)
    paint_rows(image, LEFT_INNER, WHITE)
    paint_rows(image, RIGHT_INNER, WHITE)

    pixels = image.load()
    for x in range(6, 12):
        pixels[x, 7] = BLACK
    for y in range(8, 14):
        pixels[7, y] = BLACK
        pixels[10, y] = BLACK
    return image


def pixel_svg(image: Image.Image, title: str) -> str:
    rectangles: list[str] = []
    for y in range(SIZE):
        for x in range(SIZE):
            r, g, b, a = image.getpixel((x, y))
            if a:
                rectangles.append(f'  <rect x="{x}" y="{y}" width="1" height="1" fill="#{r:02x}{g:02x}{b:02x}"/>')
    body = "\n".join(rectangles)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" '
        'shape-rendering="crispEdges">\n'
        f"  <title>{title}</title>\n"
        f"{body}\n"
        "</svg>\n"
    )


def make_preview(color: Image.Image, bw: Image.Image, destination: Path) -> None:
    canvas = Image.new("RGB", (720, 360), (245, 246, 248))
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 18), "Native 18x18 Kidney proposal artwork", fill=(20, 24, 32))

    for index, (label, asset) in enumerate((("COLOR", color), ("BLACK AND WHITE", bw))):
        x = 24 + index * 348
        draw.text((x, 54), label, fill=(20, 24, 32))
        light = Image.new("RGB", (270, 220), (255, 255, 255))
        enlarged = asset.resize((180, 180), Image.Resampling.NEAREST)
        light.paste(enlarged, (45, 20), enlarged)
        canvas.paste(light, (x, 78))

        # Actual-size sample is boxed only in the review board, never in the asset.
        draw.rectangle((x, 314, x + 28, 342), fill=(255, 255, 255), outline=(170, 174, 182))
        canvas.paste(asset, (x + 5, 319), asset)
        draw.text((x + 40, 321), "actual 18px", fill=(65, 70, 80))
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--prefix", default="v2.10.0")
    parser.add_argument("--preview", type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    color = build_color()
    bw = build_bw()

    color_png = args.output_dir / f"{args.prefix}_kidney_color_18x18_SUBMIT.png"
    bw_png = args.output_dir / f"{args.prefix}_kidney_bw_18x18_SUBMIT.png"
    color_svg = args.output_dir / f"{args.prefix}_kidney_color_18_SOURCE.svg"
    bw_svg = args.output_dir / f"{args.prefix}_kidney_bw_18_SOURCE.svg"

    color.save(color_png, optimize=True)
    bw.save(bw_png, optimize=True)
    color_svg.write_text(pixel_svg(color, "Kidney color native 18-pixel source"), encoding="utf-8")
    bw_svg.write_text(pixel_svg(bw, "Kidney black-and-white native 18-pixel source"), encoding="utf-8")

    if args.preview:
        make_preview(color, bw, args.preview)

    print(color_png)
    print(bw_png)
    print(color_svg)
    print(bw_svg)


if __name__ == "__main__":
    main()
