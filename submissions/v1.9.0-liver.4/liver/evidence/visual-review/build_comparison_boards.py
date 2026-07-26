"""Build Liver recognition comparison boards at actual emoji sizes."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
PACKAGE = HERE.parents[2]
sys.path.insert(0, str(REPO))

from scripts.build_organ_proposal_assets import render  # noqa: E402


LABELS = (
    ("Liver candidate", "liver"),
    ("Stomach candidate", "stomach"),
    ("Anatomical Heart", "1FAC0"),
    ("Cut of Meat", "1F969"),
    ("Beans", "1FAD8"),
    ("Generic organ", "generic"),
)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(Path("C:/Windows/Fonts") / name, size)


def generic_organ(size: int, black_and_white: bool) -> Image.Image:
    master = Image.new("RGB", (72, 72), "white")
    draw = ImageDraw.Draw(master)
    points = [(7, 31), (14, 18), (31, 13), (51, 16), (66, 27), (61, 42), (46, 51), (28, 58), (12, 51)]
    if black_and_white:
        draw.polygon(points, fill="white", outline="black", width=5)
    else:
        draw.polygon(points, fill="#A83C43", outline="#5E1D26", width=3)
    image = master.resize((size, size), Image.Resampling.LANCZOS)
    if black_and_white:
        image = image.convert("L").point(lambda value: 255 if value >= 180 else 0, mode="1").convert("RGB")
    return image


def load_asset(key: str, size: int, variant: str, temp: Path) -> Image.Image:
    if key in {"liver", "stomach"}:
        path = PACKAGE / key / "images" / f"{key}_{variant}_{size}x{size}_SUBMIT.png"
        return Image.open(path).convert("RGB")
    if key == "generic":
        return generic_organ(size, variant == "bw")
    source_variant = "black" if variant == "bw" else "color"
    source = HERE / "sources" / "openmoji" / f"{key}_{source_variant}.svg"
    destination = temp / f"{key}_{variant}_{size}.png"
    render(source.read_text(encoding="utf-8"), destination, size, black_and_white=variant == "bw")
    return Image.open(destination).convert("RGB")


def build_board(size: int, variant: str) -> Path:
    card_width = 220
    columns = 3
    rows = 2
    width = card_width * columns
    scale = 6 if size == 18 else 2
    zoom_size = size * scale
    actual_y = 53
    actual_label_y = actual_y + size + 8
    zoom_y = actual_label_y + 32
    zoom_label_y = zoom_y + zoom_size + 8
    card_height = zoom_label_y + 32
    content_top = 58
    height = content_top + rows * card_height
    board = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(board)
    title_font = font("arialbd.ttf", 20)
    label_font = font("arialbd.ttf", 16)
    small_font = font("arial.ttf", 12)
    mode = "Color" if variant == "color" else "Black and white"
    title = f"Liver visual-confusion board - {mode}, {size}x{size} actual size"
    draw.text((20, 14), title, fill="black", font=title_font)
    with tempfile.TemporaryDirectory(prefix="liver-comparison-") as temp_dir:
        temp = Path(temp_dir)
        for index, (label, key) in enumerate(LABELS):
            column = index % columns
            row = index // columns
            left = column * card_width
            top = content_top + row * card_height
            draw.rectangle((left, top, left + card_width - 1, top + card_height - 1), outline="#B8B8B8", width=1)
            label_box = draw.textbbox((0, 0), label, font=label_font)
            draw.text((left + (card_width - (label_box[2] - label_box[0])) / 2, top + 14), label, fill="black", font=label_font)
            asset = load_asset(key, size, variant, temp)
            actual_x = left + (card_width - size) // 2
            board.paste(asset, (actual_x, top + actual_y))
            actual_label = f"actual {size}px"
            actual_box = draw.textbbox((0, 0), actual_label, font=small_font)
            draw.text((left + (card_width - (actual_box[2] - actual_box[0])) / 2, top + actual_label_y), actual_label, fill="#555", font=small_font)
            zoomed = asset.resize((zoom_size, zoom_size), Image.Resampling.NEAREST)
            board.paste(zoomed, (left + (card_width - zoom_size) // 2, top + zoom_y))
            zoom_label = f"{scale}x nearest-neighbor preview"
            zoom_box = draw.textbbox((0, 0), zoom_label, font=small_font)
            draw.text((left + (card_width - (zoom_box[2] - zoom_box[0])) / 2, top + zoom_label_y), zoom_label, fill="#555", font=small_font)
    output = HERE / f"liver_comparison_{variant}_{size}x{size}.png"
    board.save(output, optimize=True)
    return output


if __name__ == "__main__":
    for artwork_variant in ("color", "bw"):
        for artwork_size in (18, 72):
            print(build_board(artwork_size, artwork_variant))
