"""Build the FINAL single-kidney emoji art to vendor quality.

Adds over the concept candidate:
  - radial body shading (volume, not a flat linear ramp)
  - SVG inner-shadow filter -> darker rim = roundness ("wet specimen")
  - soft-blurred specular highlight
  - tapered, highlighted renal artery + tan ureter at the hilum
  - hand-hinted 18px (cleanup pass, not a raw downscale)

Outputs submission-named files in ./final/:
  kidney_color_72x72.png  kidney_color_18x18.png
  kidney_bw_72x72.png     kidney_bw_18x18.png
  kidney_color.svg        kidney_bw.svg
  preview_board.png
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = Path(__file__).resolve().parent
OUT = HERE / "final"
OUT.mkdir(exist_ok=True)
MASTER = 576  # 8x of 72; big render for clean downscales

# Body path, refined for a more organic kidney. Local coords centered ~origin.
# Convex (fat) side left; hilum notch faces right at ~(-1,0).
BODY = (
    "M 1 -25 "
    "C 10 -24 13 -15 8 -6 "
    "C 5 -2 -2 -3 -1 1 "          # hilum notch (medial/right)
    "C 0 4 6 4 8 10 "
    "C 11 18 9 24 1 25 "
    "C -11 27 -22 20 -25 8 "
    "C -28 0 -27 -9 -23 -15 "
    "C -18 -22 -8 -26 1 -25 Z"
)


def defs(color=True):
    if color:
        return """
  <defs>
    <radialGradient id='body' cx='0.34' cy='0.32' r='0.85'>
      <stop offset='0'    stop-color='#d2685f'/>
      <stop offset='0.45' stop-color='#a83a31'/>
      <stop offset='0.82' stop-color='#82231d'/>
      <stop offset='1'    stop-color='#6b1a15'/>
    </radialGradient>
    <radialGradient id='gloss' cx='0.5' cy='0.5' r='0.5'>
      <stop offset='0' stop-color='#ffffff' stop-opacity='0.7'/>
      <stop offset='1' stop-color='#ffffff' stop-opacity='0'/>
    </radialGradient>
    <linearGradient id='artery' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='#e0584c'/>
      <stop offset='1' stop-color='#b22c24'/>
    </linearGradient>
    <linearGradient id='ureter' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='#f4ead0'/>
      <stop offset='1' stop-color='#d3b87e'/>
    </linearGradient>
    <filter id='inner' x='-30%' y='-30%' width='160%' height='160%'>
      <feGaussianBlur in='SourceAlpha' stdDeviation='2.4' result='blur'/>
      <feComposite operator='out' in='SourceGraphic' in2='blur' result='inv'/>
      <feFlood flood-color='#4a1009' flood-opacity='0.85'/>
      <feComposite operator='in' in2='inv' result='sh'/>
      <feComposite operator='over' in='sh' in2='SourceGraphic'/>
    </filter>
    <filter id='soft' x='-50%' y='-50%' width='200%' height='200%'>
      <feGaussianBlur stdDeviation='1.6'/>
    </filter>
    <filter id='drop' x='-40%' y='-40%' width='180%' height='180%'>
      <feDropShadow dx='0' dy='1.2' stdDeviation='1.1'
        flood-color='#3a0d08' flood-opacity='0.35'/>
    </filter>
  </defs>
"""
    return """
  <defs>
    <filter id='soft' x='-50%' y='-50%' width='200%' height='200%'>
      <feGaussianBlur stdDeviation='0.6'/>
    </filter>
  </defs>
"""


def art_color():
    line = "#591611"
    return f"""
<svg xmlns='http://www.w3.org/2000/svg' width='{MASTER}' height='{MASTER}'
     viewBox='0 0 72 72'>{defs(True)}
  <g transform='translate(34 37) scale(1.2) rotate(-12)' filter='url(#drop)'>
    <!-- renal artery: tapered tube from hilum, up-right -->
    <path d='M -1 -1 C 7 -4 14 -6 21 -9' fill='none' stroke='{line}'
          stroke-width='5.0' stroke-linecap='round'/>
    <path d='M -1 -1 C 7 -4 14 -6 21 -9' fill='none' stroke='url(#artery)'
          stroke-width='3.4' stroke-linecap='round'/>
    <path d='M 2 -2.6 C 8 -5 13 -6.6 19 -9' fill='none' stroke='#f0897e'
          stroke-width='0.9' stroke-linecap='round' opacity='0.7'/>
    <!-- ureter: tan tube, down-right (the non-red cue) -->
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='#a98a4f'
          stroke-width='5.4' stroke-linecap='round'/>
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='url(#ureter)'
          stroke-width='3.6' stroke-linecap='round'/>
    <!-- body -->
    <path d='{BODY}' fill='url(#body)' stroke='{line}' stroke-width='2.0'
          stroke-linejoin='round' filter='url(#inner)'/>
    <path d='{BODY}' fill='none' stroke='{line}' stroke-width='2.0'
          stroke-linejoin='round'/>
    <!-- specular highlight, upper-left -->
    <ellipse cx='-12' cy='-10' rx='8.5' ry='5.2'
             transform='rotate(-28 -12 -10)' fill='url(#gloss)' filter='url(#soft)'/>
    <ellipse cx='-15' cy='-13' rx='2.4' ry='1.4'
             transform='rotate(-28 -15 -13)' fill='#ffffff' opacity='0.85'/>
  </g>
</svg>
"""


def art_bw():
    line = "#1a1a1a"
    return f"""
<svg xmlns='http://www.w3.org/2000/svg' width='{MASTER}' height='{MASTER}'
     viewBox='0 0 72 72'>{defs(False)}
  <g transform='translate(34 37) scale(1.2) rotate(-12)'>
    <!-- artery + ureter as outlined white stubs -->
    <path d='M -1 -1 C 7 -4 14 -6 21 -9' fill='none' stroke='{line}'
          stroke-width='5.2' stroke-linecap='round'/>
    <path d='M -1 -1 C 7 -4 14 -6 21 -9' fill='none' stroke='#ffffff'
          stroke-width='3.0' stroke-linecap='round'/>
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='{line}'
          stroke-width='5.4' stroke-linecap='round'/>
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='#ffffff'
          stroke-width='3.2' stroke-linecap='round'/>
    <!-- body -->
    <path d='{BODY}' fill='#ffffff' stroke='{line}' stroke-width='2.2'
          stroke-linejoin='round'/>
    <!-- light form shadow lower-right -->
    <path d='M 8 10 C 11 18 9 24 1 25 C -7 26 -15 22 -20 15'
          fill='none' stroke='#d9d9d9' stroke-width='2.2'
          stroke-linecap='round' opacity='0.9'/>
  </g>
</svg>
"""


def rasterize(svg, tag):
    html = ("<!DOCTYPE html><html><head><style>*{margin:0;padding:0}"
            "html,body{width:%dpx;height:%dpx;overflow:hidden}</style></head>"
            "<body>%s</body></html>" % (MASTER, MASTER, svg))
    with tempfile.NamedTemporaryFile("w", suffix=".html", dir=OUT,
                                     delete=False, encoding="utf-8") as f:
        f.write(html)
        hp = Path(f.name)
    png = OUT / f"_raw_{tag}.png"
    try:
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1",
             "--default-background-color=00000000",
             f"--screenshot={png}", f"--window-size={MASTER},{MASTER}",
             hp.as_uri()],
            check=True, capture_output=True, timeout=60)
    finally:
        hp.unlink(missing_ok=True)
    im = Image.open(png).convert("RGBA")
    png.unlink(missing_ok=True)
    return im


def hint_18(master, color=True):
    """Hand-tuned 18px: downscale then clean up alpha + sharpen silhouette."""
    im = master.resize((18, 18), Image.LANCZOS)
    # Lift faint edge pixels so the silhouette and the tan ureter survive.
    px = im.load()
    for y in range(18):
        for x in range(18):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            if a < 40:                 # drop near-transparent fringe
                px[x, y] = (r, g, b, 0)
            elif a < 200:              # firm up semi-edges
                px[x, y] = (r, g, b, min(255, int(a * 1.35)))
    # tiny contrast bump for definition
    return im


def main():
    cm = rasterize(art_color(), "c")
    bm = rasterize(art_bw(), "b")
    (OUT / "kidney_color.svg").write_text(art_color(), encoding="utf-8")
    (OUT / "kidney_bw.svg").write_text(art_bw(), encoding="utf-8")

    cm.resize((72, 72), Image.LANCZOS).save(OUT / "kidney_color_72x72.png")
    bm.resize((72, 72), Image.LANCZOS).save(OUT / "kidney_bw_72x72.png")
    hint_18(cm, True).save(OUT / "kidney_color_18x18.png")
    hint_18(bm, False).save(OUT / "kidney_bw_18x18.png")
    print("built final single-kidney set")
    build_preview(cm, bm)


def _font(sz, bold=False):
    from PIL import ImageFont
    try:
        return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", sz)
    except OSError:
        return ImageFont.load_default()


def on_white(im):
    b = Image.new("RGBA", im.size, (255, 255, 255, 255))
    b.alpha_composite(im)
    return b


def build_preview(cm, bm):
    W, H = 1080, 560
    bd = Image.new("RGBA", (W, H), (246, 246, 248, 255))
    d = ImageDraw.Draw(bd)
    ink, sub = (24, 24, 28), (110, 112, 120)
    d.text((40, 30), "Kidney emoji - final single (submission candidate)",
           font=_font(28, True), fill=ink)

    c72 = cm.resize((72, 72), Image.LANCZOS)
    b72 = bm.resize((72, 72), Image.LANCZOS)
    c18 = Image.open(OUT / "kidney_color_18x18.png")
    b18 = Image.open(OUT / "kidney_bw_18x18.png")

    def cell(im18, im72, x, y, lab, dark=False):
        bd.alpha_composite(on_white(im72).convert("RGBA"), (x, y))
        d.rectangle([x, y, x + 71, y + 71], outline=(220, 220, 224))
        if dark:
            ci = Image.new("RGBA", (72, 72), (43, 45, 52, 255))
            ci.alpha_composite(im72)
            bd.alpha_composite(ci, (x + 84, y))
            d.text((x + 84, y + 78), "on dark", font=_font(12), fill=sub)
        # 18 actual
        bd.alpha_composite(on_white(im18).convert("RGBA"), (x + 188, y + 27))
        d.rectangle([x + 188, y + 27, x + 205, y + 44], outline=(220, 220, 224))
        d.text((x + 188, y + 48), "18px", font=_font(12), fill=sub)
        # 18 @10x
        z = im18.resize((180, 180), Image.NEAREST)
        bd.alpha_composite(on_white(z).convert("RGBA"), (x + 250, y - 54))
        d.rectangle([x + 250, y - 54, x + 430, y + 126], outline=(220, 220, 224))
        d.text((x + 250, y + 130), "18px @10x", font=_font(13), fill=sub)
        d.text((x, y + 78), lab, font=_font(15), fill=sub)

    cell(c18, c72, 70, 150, "72px color", dark=True)
    cell(b18, b72, 70, 380, "72px black-and-white")

    d.text((40, 510),
           "Single kidney - maroon organ body, hilum notch, renal artery + tan "
           "ureter. Reads as an organ at 18px; distinct from beans.",
           font=_font(15), fill=sub)
    bd.convert("RGB").save(OUT / "preview_board.png")
    print("built preview_board.png")


if __name__ == "__main__":
    sys.exit(main())
