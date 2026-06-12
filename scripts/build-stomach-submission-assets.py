"""Build submission assets for the Stomach emoji proposal:
  - Required example images at 18x18 and 72x72 (color + black-and-white),
    derived from the project's color stomach artwork.
  - Clearly-labeled placeholder tiles for the five required frequency-evidence
    screenshots. These are NOT real evidence; they mark where the live captures
    must be embedded. Real Google Search / Video / Trends / Ngram screenshots
    must be captured in a browser before filing.

Run: python scripts/build-stomach-submission-assets.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public", "images", "emoji", "3-stomach.png")
WS = os.path.join(ROOT, "docs", "proposals", "stomach-emoji-2026")
IMG = os.path.join(WS, "images")
EVID = os.path.join(WS, "evidence", "frequency")
os.makedirs(IMG, exist_ok=True)
os.makedirs(EVID, exist_ok=True)


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(os.path.join(r"C:\Windows\Fonts", name), size)
    except OSError:
        return ImageFont.load_default()


def trim(im):
    bbox = im.split()[3].getbbox()
    return im.crop(bbox) if bbox else im


# --- Required example images ---
color = trim(Image.open(SRC).convert("RGBA"))


def fit(im, box):
    s = min(box / im.width, box / im.height)
    im2 = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    canvas = Image.new("RGBA", (box, box), (0, 0, 0, 0))
    canvas.alpha_composite(im2, ((box - im2.width) // 2, (box - im2.height) // 2))
    return canvas


# Black-and-white reference: desaturate the color artwork (simplified reference art).
gray = color.copy()
g = gray.convert("LA").convert("RGBA")
g.putalpha(color.split()[3])

for box in (18, 72):
    fit(color, box).save(os.path.join(IMG, f"stomach_color_{box}x{box}_SUBMIT.png"))
    fit(g, box).save(os.path.join(IMG, f"stomach_bw_{box}x{box}_SUBMIT.png"))

# --- Frequency-evidence placeholders (clearly marked CAPTURE PENDING) ---
PLACEHOLDERS = [
    ("google_search", "Google Search", "query: stomach"),
    ("google_video_search", "Google Video Search", "query: stomach"),
    ("google_trends_web", "Google Trends - Web Search", "elephant vs stomach"),
    ("google_trends_image", "Google Trends - Image Search", "elephant vs stomach"),
    ("google_books_ngram", "Google Books Ngram Viewer", "elephant vs stomach"),
]
W, H = 1200, 720
for key, title, sub in PLACEHOLDERS:
    im = Image.new("RGB", (W, H), (244, 245, 248))
    d = ImageDraw.Draw(im)
    d.rectangle([6, 6, W - 7, H - 7], outline=(190, 60, 60), width=4)
    d.text((48, 60), title, font=font(54, True), fill=(40, 46, 58))
    d.text((48, 130), sub, font=font(34), fill=(90, 98, 112))
    d.text((48, 300), "FREQUENCY EVIDENCE — CAPTURE PENDING", font=font(40, True), fill=(190, 60, 60))
    d.text((48, 372), "Replace with a live browser screenshot before filing.", font=font(30), fill=(90, 98, 112))
    d.text((48, 430), "Reproducible URL is listed in Section 3.E.", font=font(30), fill=(90, 98, 112))
    d.text((48, 620), "medicalemoji.org — Stomach emoji proposal", font=font(26), fill=(150, 156, 168))
    im.save(os.path.join(EVID, f"stomach_frequency_{key}_PLACEHOLDER.png"))

print("example images:", sorted(os.listdir(IMG)))
print("placeholders:", sorted(os.listdir(EVID)))
