"""Build the ACEP press/social kit: renamed individual emoji PNGs plus a
single labeled grid graphic of the ten concepts named in the ACEP support
letter (June 5, 2026).

Run: python scripts/build-acep-kit.py
Output: public/press/acep/emoji/*.png and public/press/acep/medical-emoji-acep-grid.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public", "images", "emoji")
OUT = os.path.join(ROOT, "public", "press", "acep")
OUT_EMOJI = os.path.join(OUT, "emoji")
os.makedirs(OUT_EMOJI, exist_ok=True)

# slug -> (source file, kit filename, display label) in the letter's order.
CONCEPTS = [
    ("5-liver.png", "liver.png", "Liver"),
    ("kidneysnew2.png", "kidney.png", "Kidney"),
    ("3-stomach.png", "stomach.png", "Stomach"),
    ("1-intestines.png", "intestine.png", "Intestine / Bowel"),
    ("14-white-blood-cell-1.png", "white-blood-cell.png", "White Blood Cell"),
    ("13-ecg-1.png", "ecg.png", "ECG / EKG"),
    ("4-bottom_spine.png", "spine.png", "Spine"),
    ("8-blood-bagcolor.png", "blood-product.png", "Blood Product"),
    ("7-pill-pack.png", "pill-pack.png", "Pill Pack"),
    ("11-scales.png", "weight-scale.png", "Weight Scale"),
]


def load_trimmed(path):
    img = Image.open(path).convert("RGBA")
    bbox = img.split()[3].getbbox()  # trim transparent margins via alpha
    return img.crop(bbox) if bbox else img


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    for p in (os.path.join(r"C:\Windows\Fonts", name), name):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


# Copy individual renamed PNGs (full quality, untrimmed).
for src, dest, _ in CONCEPTS:
    Image.open(os.path.join(SRC, src)).convert("RGBA").save(os.path.join(OUT_EMOJI, dest))

# --- Build the labeled grid ---
COLS, ROWS = 5, 2
CELL_W, ICON_BOX = 340, 230
PAD_X, LABEL_H = 24, 64
TITLE_H, FOOTER_H = 150, 70
CELL_H = ICON_BOX + LABEL_H

W = COLS * CELL_W + PAD_X * 2
H = TITLE_H + ROWS * CELL_H + FOOTER_H

canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Title + subtitle
title_f, sub_f, label_f, foot_f = font(46, True), font(26), font(27, True), font(24)
draw.text((PAD_X + 6, 40), "Medical Emoji endorsed by ACEP", font=title_f, fill=(26, 32, 44))
draw.text(
    (PAD_X + 6, 100),
    "Ten clinical concepts named in the American College of Emergency Physicians support letter",
    font=sub_f,
    fill=(90, 98, 112),
)

for idx, (src, dest, label) in enumerate(CONCEPTS):
    col, row = idx % COLS, idx // COLS
    cx = PAD_X + col * CELL_W + CELL_W // 2
    cy_top = TITLE_H + row * CELL_H

    icon = load_trimmed(os.path.join(SRC, src))
    scale = min(ICON_BOX / icon.width, ICON_BOX / icon.height)
    icon = icon.resize((max(1, int(icon.width * scale)), max(1, int(icon.height * scale))), Image.LANCZOS)
    ix = cx - icon.width // 2
    iy = cy_top + (ICON_BOX - icon.height) // 2
    canvas.alpha_composite(icon, (ix, iy))

    tb = draw.textbbox((0, 0), label, font=label_f)
    draw.text((cx - (tb[2] - tb[0]) // 2, cy_top + ICON_BOX + 14), label, font=label_f, fill=(40, 46, 58))

# Footer
foot = "medicalemoji.org  ·  Advocating for medical representation in the Unicode emoji standard"
tb = draw.textbbox((0, 0), foot, font=foot_f)
draw.text(((W - (tb[2] - tb[0])) // 2, H - FOOTER_H + 22), foot, font=foot_f, fill=(120, 128, 140))

grid_path = os.path.join(OUT, "medical-emoji-acep-grid.png")
canvas.convert("RGB").save(grid_path, "PNG")
print(f"Grid: {grid_path} ({W}x{H})")
print(f"Individual PNGs: {OUT_EMOJI} ({len(CONCEPTS)} files)")
