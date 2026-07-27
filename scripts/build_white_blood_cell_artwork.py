"""Export and compare the White Blood Cell proposal artwork.

This script renders the purpose-built 18x18 and 72x72 SVG masters, forces the
black-and-white exports to a true two-color palette, and builds actual-size
comparison boards against pinned OpenMoji controls.

Usage:
    python scripts/build_white_blood_cell_artwork.py \
        --proposal-dir submissions/v1.15.0/white-blood-cell \
        --board-date 2026-07-26
"""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path
import textwrap

import cairosvg
from PIL import Image, ImageDraw, ImageFont


OPENMOJI_COMMIT = "d05930b34516a0a3ff00aad0288ee05364cebd8b"
OPENMOJI = {
    "Microbe": "1F9A0",
    "Drop of Blood": "1FA78",
    "Soap": "1F9FC",
    "Bubbles": "1FAE7",
}
ROWS = ["White Blood Cell", *OPENMOJI.keys(), "Generic cell control"]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)


def white_background(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    canvas = Image.new("RGBA", rgba.size, "white")
    canvas.alpha_composite(rgba)
    return canvas.convert("RGB")


def render_svg(path: Path, size: int) -> Image.Image:
    data = cairosvg.svg2png(
        bytestring=path.read_bytes(),
        output_width=size,
        output_height=size,
    )
    return white_background(Image.open(BytesIO(data)))


def force_black_and_white(image: Image.Image) -> Image.Image:
    return image.convert("L").point(lambda value: 255 if value >= 128 else 0).convert("RGB")


def export_assets(proposal_dir: Path) -> list[Path]:
    images = proposal_dir / "images"
    exports = [
        ("white-blood-cell_color_18_SOURCE.svg", "white-blood-cell_color_18x18_SUBMIT.png", 18, False),
        ("white-blood-cell_color_SOURCE.svg", "white-blood-cell_color_72x72_SUBMIT.png", 72, False),
        ("white-blood-cell_bw_18_SOURCE.svg", "white-blood-cell_bw_18x18_SUBMIT.png", 18, True),
        ("white-blood-cell_bw_SOURCE.svg", "white-blood-cell_bw_72x72_SUBMIT.png", 72, True),
    ]
    written: list[Path] = []
    for source_name, output_name, size, black_and_white in exports:
        image = render_svg(images / source_name, size)
        if black_and_white:
            image = force_black_and_white(image)
        output = images / output_name
        image.save(output, optimize=True)
        written.append(output)
    return written


def generic_cell(size: int, variant: str) -> Image.Image:
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    scale = size / 72
    outer = tuple(round(value * scale) for value in (9, 9, 63, 63))
    nucleus = tuple(round(value * scale) for value in (26, 26, 46, 46))
    width = max(1, round(3 * scale))
    if variant == "color":
        draw.ellipse(outer, fill="#dbe6e8", outline="#8ca0a6", width=width)
        draw.ellipse(nucleus, fill="#6b4a99")
    else:
        draw.ellipse(outer, fill="white", outline="black", width=width)
        draw.ellipse(nucleus, fill="black")
    return image


def proposed_cell(proposal_dir: Path, size: int, variant: str) -> Image.Image:
    marker = "color" if variant == "color" else "bw"
    path = proposal_dir / "images" / f"white-blood-cell_{marker}_{size}x{size}_SUBMIT.png"
    return white_background(Image.open(path))


def control_cell(proposal_dir: Path, label: str, size: int, variant: str) -> Image.Image:
    if label == "White Blood Cell":
        return proposed_cell(proposal_dir, size, variant)
    if label == "Generic cell control":
        return generic_cell(size, variant)
    codepoint = OPENMOJI[label]
    path = proposal_dir / "comparisons" / "source" / "openmoji" / variant / f"{codepoint}.svg"
    return render_svg(path, size)


def centered_paste(board: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> None:
    left, top, right, bottom = box
    x = left + (right - left - image.width) // 2
    y = top + (bottom - top - image.height) // 2
    board.paste(image, (x, y))


def build_board(proposal_dir: Path, variant: str, board_date: str) -> Path:
    width = 1340
    title_height = 108
    header_height = 62
    row_height = 190
    footer_height = 86
    height = title_height + header_height + row_height * len(ROWS) + footer_height
    board = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(board)
    columns = [0, 290, 405, 620, 735, 950, 1340]
    headers = ["Concept", "18x18 actual", "18x18 at 8x", "72x72 actual", "72x72 at 2x", "Notes"]

    draw.text((32, 24), f"White Blood Cell comparison board - {variant}", fill="black", font=font(32, True))
    draw.text(
        (32, 67),
        "Actual-size and enlarged views of the proposed image and nearest visual alternatives.",
        fill="#444444",
        font=font(18),
    )

    y = title_height
    draw.rectangle((0, y, width, y + header_height), fill="#eceff1")
    for index, header in enumerate(headers):
        draw.text((columns[index] + 12, y + 20), header, fill="black", font=font(17, True))

    notes = {
        "White Blood Cell": "Representative neutrophil paradigm for the broad White Blood Cell category",
        "Microbe": "Nearest microorganism alternative",
        "Drop of Blood": "Nearest blood-related alternative",
        "Soap": "Pale rounded visual alternative",
        "Bubbles": "Separate round-shape alternative",
        "Generic cell control": "Generic cell with one round nucleus",
    }

    for row_index, label in enumerate(ROWS):
        top = title_height + header_height + row_index * row_height
        bottom = top + row_height
        if row_index % 2:
            draw.rectangle((0, top, width, bottom), fill="#fafafa")
        display_label = "Generic cell diagram" if label == "Generic cell control" else label
        draw.text(
            (24, top + 72),
            display_label,
            fill="black",
            font=font(20, label == "White Blood Cell"),
        )
        image18 = control_cell(proposal_dir, label, 18, variant)
        image72 = control_cell(proposal_dir, label, 72, variant)
        centered_paste(board, image18, (columns[1], top, columns[2], bottom))
        centered_paste(
            board,
            image18.resize((144, 144), Image.Resampling.NEAREST),
            (columns[2], top, columns[3], bottom),
        )
        centered_paste(board, image72, (columns[3], top, columns[4], bottom))
        centered_paste(
            board,
            image72.resize((144, 144), Image.Resampling.NEAREST),
            (columns[4], top, columns[5], bottom),
        )
        draw.multiline_text(
            (columns[5] + 12, top + 56),
            textwrap.fill(notes[label], width=38),
            fill="#222222",
            font=font(16),
            spacing=5,
        )

    grid_top = title_height
    grid_bottom = title_height + header_height + row_height * len(ROWS)
    for x in columns:
        draw.line((x, grid_top, x, grid_bottom), fill="#aab0b3", width=1)
    for yline in [title_height, title_height + header_height] + [
        title_height + header_height + index * row_height for index in range(1, len(ROWS) + 1)
    ]:
        draw.line((0, yline, width, yline), fill="#aab0b3", width=1)

    footer_y = grid_bottom + 18
    draw.text(
        (24, footer_y),
        "Comparator emoji: OpenMoji, CC BY-SA 4.0.",
        fill="#333333",
        font=font(15),
    )
    draw.text(
        (24, footer_y + 28),
        f"Generic cell illustration is original to this proposal. Board date: {board_date}.",
        fill="#333333",
        font=font(15),
    )

    output = proposal_dir / "comparisons" / f"white-blood-cell_comparison-board_{variant}_{board_date}.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    board.save(output, optimize=True)
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-dir", required=True, type=Path)
    parser.add_argument("--board-date", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for path in export_assets(args.proposal_dir):
        print(path)
    for variant in ("color", "black"):
        print(build_board(args.proposal_dir, variant, args.board_date))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
