"""Build the Stomach nearest-emoji distinctiveness comparison board.

Section D of the proposal claims the proposed Stomach art stays distinguishable
from Beans, Anatomical Heart, Lungs, and Meat on Bone at 18x18. This renders
that claim as a figure so a reviewer can check it directly instead of taking
the sentence on trust.

Comparison glyphs come from the open-licensed Noto Emoji project. They are
shown only for visual comparison and are not part of the proposed artwork
covered by the proposal's rights certification.

Usage:
    python scripts/build_stomach_comparison_board.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "docs/proposals/stomach-emoji-2026/candidate-v1.13"
NOTO = ROOT / "docs/proposals/stomach-emoji-2026/comparison-glyphs"
OUT = CANDIDATE / "images/stomach_distinctiveness_comparison.png"

SCALE = 3           # print oversample
CELL = 96           # nominal column width before scaling
TILE = 72           # nominal tile size before scaling

COLUMNS = [
    ("Stomach", CANDIDATE / "images/stomach_color_72x72_SUBMIT.png", True),
    ("Beans", NOTO / "emoji_u1fad8.png", False),
    ("Anatomical Heart", NOTO / "emoji_u1fac0.png", False),
    ("Lungs", NOTO / "emoji_u1fac1.png", False),
    ("Meat on Bone", NOTO / "emoji_u1f356.png", False),
]

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(candidates, size):
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def flatten(path, background):
    """Composite RGBA art onto the cell background so no tile shows a white box."""
    art = Image.open(path).convert("RGBA")
    canvas = Image.new("RGBA", art.size, (*background, 255))
    canvas.alpha_composite(art)
    return canvas.convert("RGB")


def main() -> int:
    label_font = load_font(FONT_CANDIDATES, 11 * SCALE)
    bold_font = load_font(BOLD_CANDIDATES, 11 * SCALE)
    row_font = load_font(BOLD_CANDIDATES, 10 * SCALE)
    note_font = load_font(FONT_CANDIDATES, 9 * SCALE)

    row_label_w = 104 * SCALE
    width = row_label_w + len(COLUMNS) * CELL * SCALE
    header_h = 34 * SCALE
    tile_row_h = (TILE + 16) * SCALE
    note_h = 20 * SCALE
    height = header_h + tile_row_h * 2 + note_h

    board = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(board)

    # The submitted PNGs are opaque with a baked white background, so a tinted
    # column would draw a visible white box around the proposed art. Mark the
    # proposed column with a rule under its header instead.
    backgrounds = [(255, 255, 255)] * len(COLUMNS)
    accent = (52, 82, 255)

    # Column headers.
    for index, (name, _, proposed) in enumerate(COLUMNS):
        x0 = row_label_w + index * CELL * SCALE
        font = bold_font if proposed else label_font
        text = f"{name}\n(proposed)" if proposed else name
        draw.multiline_text(
            (x0 + CELL * SCALE / 2, header_h / 2),
            text,
            font=font,
            fill=accent if proposed else (85, 85, 85),
            anchor="mm",
            align="center",
            spacing=2 * SCALE,
        )
        if proposed:
            rule_y = header_h - 3 * SCALE
            draw.line(
                [(x0 + 14 * SCALE, rule_y), (x0 + (CELL - 14) * SCALE, rule_y)],
                fill=accent,
                width=2 * SCALE,
            )

    rows = [
        ("72 x 72", TILE, Image.LANCZOS, False),
        ("18 x 18\n(enlarged)", 18, Image.LANCZOS, True),
    ]

    y = header_h
    for row_label, nominal, resample, from_small in rows:
        draw.line([(0, y), (width, y)], fill=(200, 200, 200), width=max(1, SCALE // 2))
        draw.multiline_text(
            (row_label_w - 12 * SCALE, y + tile_row_h / 2),
            row_label,
            font=row_font,
            fill=(60, 60, 60),
            anchor="rm",
            align="right",
            spacing=3 * SCALE,
        )
        for index, (_, path, _) in enumerate(COLUMNS):
            art = flatten(path, backgrounds[index])
            if from_small:
                # Downsample to the real 18x18 first, then enlarge with NEAREST so
                # the figure shows the true pixel structure rather than a smooth fake.
                small = art.resize((18, 18), Image.LANCZOS)
                tile = small.resize((TILE * SCALE, TILE * SCALE), Image.NEAREST)
            else:
                tile = art.resize((TILE * SCALE, TILE * SCALE), resample)
            x0 = row_label_w + index * CELL * SCALE + (CELL - TILE) * SCALE // 2
            board.paste(tile, (x0, y + 8 * SCALE))
        y += tile_row_h

    draw.line([(0, y), (width, y)], fill=(200, 200, 200), width=max(1, SCALE // 2))
    draw.text(
        (row_label_w - 12 * SCALE, y + note_h / 2),
        "",
        font=note_font,
        fill=(110, 110, 110),
        anchor="rm",
    )
    draw.text(
        (row_label_w, y + note_h / 2),
        "Comparison glyphs: Noto Emoji (open licensed), shown for visual comparison only.",
        font=note_font,
        fill=(110, 110, 110),
        anchor="lm",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    board.save(OUT)
    print(f"Wrote {OUT} ({board.width}x{board.height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
