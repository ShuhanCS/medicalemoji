"""Build kidney emoji candidate art (single + paired, color + BW) as SVG,
rasterize with Chrome headless, downscale honestly to 72px and 18px, and
assemble a true-size comparison board.

Emoji house-style targets (from approved organ emoji heart/lungs/brain):
  - one bold silhouette filling ~80% of the frame
  - dark keyline around the whole shape (darkened fill color)
  - soft directional gradient: highlight upper-left, shadow lower-right
  - 2-3 hue palette, chunky simplified vessels (never thin lines)
  - a small specular highlight
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = Path(__file__).resolve().parent
OUT = HERE / "candidates"
OUT.mkdir(exist_ok=True)
MASTER = 360  # 5x of 72; render big, downscale clean

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------
KID_LIGHT = "#c75b54"   # upper-left highlight maroon
KID_MID = "#a23730"     # body
KID_DARK = "#7d251f"    # lower-right shadow
KID_LINE = "#5c1813"    # keyline
ART_RED = "#cf4036"     # renal artery stub
URETER = "#e7d4a4"      # ureter (tan/cream) -> the non-red "organ" cue
URETER_LINE = "#b59b63"
BW_LINE = "#1a1a1a"
BW_FILL = "#ffffff"
BW_SHADE = "#d9d9d9"

# One kidney path in LOCAL coords, centered ~origin.
# Convex (fat) side on the left; hilum notch faces RIGHT at (-5,0)->(local +x).
# Spans roughly x:-27..10, y:-26..27.
KIDNEY_PATH = (
    "M 2 -25 "
    "C 9 -23 11 -14 7 -6 "
    "C 5 -3 -1 -3 -1 0 "       # hilum notch (right/medial) - softer, shallower
    "C -1 3 5 3 7 9 "
    "C 10 17 9 23 2 25 "
    "C -10 27 -22 19 -25 7 "
    "C -27 1 -27 -7 -24 -13 "
    "C -20 -21 -8 -26 2 -25 Z"
)


def defs():
    return f"""
  <defs>
    <linearGradient id='kid' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='{KID_LIGHT}'/>
      <stop offset='0.55' stop-color='{KID_MID}'/>
      <stop offset='1' stop-color='{KID_DARK}'/>
    </linearGradient>
    <radialGradient id='gloss' cx='0.5' cy='0.5' r='0.5'>
      <stop offset='0' stop-color='#ffffff' stop-opacity='0.55'/>
      <stop offset='1' stop-color='#ffffff' stop-opacity='0'/>
    </radialGradient>
    <linearGradient id='ureter' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='#f2e6c4'/>
      <stop offset='1' stop-color='#d8bf86'/>
    </linearGradient>
  </defs>
"""


def kidney_group(tx, ty, scale, rot, mirror, color=True):
    """One kidney + its hilum vessels, transformed into place."""
    m = -1 if mirror else 1
    line = KID_LINE if color else BW_LINE
    fill = "url(#kid)" if color else BW_FILL
    sw = 2.4 / scale  # keep keyline ~constant px after scaling
    # vessel stubs in LOCAL coords emerging from hilum (-5,0) toward +x
    art = ART_RED if color else BW_FILL
    art_line = KID_DARK if color else BW_LINE
    ur = "url(#ureter)" if color else BW_SHADE
    ur_line = URETER_LINE if color else BW_LINE
    vsw = 2.2 / scale
    # gloss ellipse upper-left of body (local ~ (-12,-10))
    gloss = (
        f"<ellipse cx='-11' cy='-9' rx='9' ry='6' transform='rotate(-25 -11 -9)' "
        f"fill='url(#gloss)'/>" if color else ""
    )
    return f"""
  <g transform='translate({tx} {ty}) scale({scale*m} {scale}) rotate({rot})'>
    <!-- renal artery stub: fat rounded tube from hilum -->
    <path d='M -1 -1 C 7 -4 14 -6 20 -9' fill='none' stroke='{art_line}'
          stroke-width='{vsw+2.0}' stroke-linecap='round'/>
    <path d='M -1 -1 C 7 -4 14 -6 20 -9' fill='none' stroke='{art}'
          stroke-width='{vsw+0.4}' stroke-linecap='round'/>
    <!-- ureter stub: tan tube curving down from hilum (kept fat for 18px) -->
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='{ur_line}'
          stroke-width='{vsw+2.6}' stroke-linecap='round'/>
    <path d='M -1 3 C 5 10 11 17 17 26' fill='none' stroke='{ur}'
          stroke-width='{vsw+1.2}' stroke-linecap='round'/>
    <!-- kidney body -->
    <path d='{KIDNEY_PATH}' fill='{fill}' stroke='{line}' stroke-width='{sw}'
          stroke-linejoin='round'/>
    {gloss}
  </g>
"""


def svg_wrap(inner):
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{MASTER}' "
        f"height='{MASTER}' viewBox='0 0 72 72'>{defs()}{inner}</svg>"
    )


def single(color=True):
    # one big kidney, tilted -12, hilum facing right toward viewer
    return svg_wrap(kidney_group(34, 37, 1.18, -12, mirror=False, color=color))


def paired(color=True):
    # two smaller kidneys, hila facing inward, fat sides out; slight top toe-in
    left = kidney_group(26, 38, 0.74, 8, mirror=False, color=color)
    right = kidney_group(46, 38, 0.74, -8, mirror=True, color=color)
    # one short shared vessel between the two hila at center-top
    line = KID_DARK if color else BW_LINE
    fill = ART_RED if color else BW_FILL
    bridge = f"""
  <path d='M 30 30 C 36 26 36 26 42 30' fill='none' stroke='{line}'
        stroke-width='5.4' stroke-linecap='round'/>
  <path d='M 30 30 C 36 26 36 26 42 30' fill='none' stroke='{fill}'
        stroke-width='3.0' stroke-linecap='round'/>
"""
    return svg_wrap(left + right + bridge)


def rasterize(svg, name):
    """Render SVG -> MASTER px PNG via Chrome, return Pillow image."""
    html = (
        "<!DOCTYPE html><html><head><style>"
        "*{margin:0;padding:0}html,body{width:%dpx;height:%dpx;overflow:hidden}"
        "</style></head><body>%s</body></html>" % (MASTER, MASTER, svg)
    )
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", dir=OUT, delete=False, encoding="utf-8"
    ) as f:
        f.write(html)
        hp = Path(f.name)
    png = OUT / f"_raw_{name}.png"
    try:
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1",
             "--default-background-color=00000000",
             f"--screenshot={png}", f"--window-size={MASTER},{MASTER}",
             hp.as_uri()],
            check=True, capture_output=True, timeout=60,
        )
    finally:
        hp.unlink(missing_ok=True)
    im = Image.open(png).convert("RGBA").resize((MASTER, MASTER))
    png.unlink(missing_ok=True)
    return im


def down(im, size):
    return im.resize((size, size), Image.LANCZOS)


def on_bg(im, bg):
    base = Image.new("RGBA", im.size, bg)
    base.alpha_composite(im)
    return base.convert("RGB")


def main():
    variants = {
        "single_color": single(True),
        "single_bw": single(False),
        "paired_color": paired(True),
        "paired_bw": paired(False),
    }
    masters = {}
    for name, svg in variants.items():
        (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
        im = rasterize(svg, name)
        masters[name] = im
        for sz in (72, 18):
            d = down(im, sz)
            d.save(OUT / f"{name}_{sz}.png")
        print(f"built {name}")

    build_board(masters)
    print("built comparison_board.png")


def _font(size, bold=False):
    from PIL import ImageFont
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def build_board(masters):
    from PIL import ImageDraw
    bg = (246, 246, 248, 255)
    W, H = 1240, 880
    board = Image.new("RGBA", (W, H), bg)
    d = ImageDraw.Draw(board)
    white = (255, 255, 255, 255)
    chip = (43, 45, 52, 255)
    ink = (24, 24, 28)
    sub = (110, 112, 120)
    green = (22, 132, 60)
    red = (190, 40, 40)

    d.text((40, 28), "Kidney emoji - candidate comparison at true Unicode sizes",
           font=_font(30, True), fill=ink)
    d.text((40, 70), "72x72 and 18x18, color + black-and-white. 18px shown "
           "actual size and 8x zoom (the real legibility test).",
           font=_font(17), fill=sub)

    col_x = {"single": 70, "paired": 660}
    d.text((col_x["single"], 116), "SINGLE  (recommended)",
           font=_font(22, True), fill=green)
    d.text((col_x["paired"], 116), "PAIRED  (alt - loses at 18px)",
           font=_font(22, True), fill=red)

    def cell(form, kind, gx, gy, label):
        m = masters[f"{form}_{kind}"]
        # 72 on white
        board.alpha_composite(on_bg(down(m, 72), white).convert("RGBA"), (gx, gy))
        d.rectangle([gx, gy, gx + 71, gy + 71], outline=(220, 220, 224))
        if kind == "color":  # also a dark chip for 72 color
            ci = Image.new("RGBA", (72, 72), chip)
            ci.alpha_composite(down(m, 72))
            board.alpha_composite(ci, (gx + 84, gy))
        # 18 actual size
        board.alpha_composite(on_bg(down(m, 18), white).convert("RGBA"),
                              (gx + 188, gy + 27))
        d.rectangle([gx + 188, gy + 27, gx + 188 + 17, gy + 27 + 17],
                    outline=(220, 220, 224))
        # 18 zoomed 8x
        z = down(m, 18).resize((144, 144), Image.NEAREST)
        board.alpha_composite(on_bg(z, white).convert("RGBA"), (gx + 230, gy - 36))
        d.rectangle([gx + 230, gy - 36, gx + 230 + 143, gy - 36 + 143],
                    outline=(220, 220, 224))
        d.text((gx, gy + 78), label, font=_font(15), fill=sub)
        d.text((gx + 188, gy + 48), "18px", font=_font(12), fill=sub)
        d.text((gx + 230, gy + 110), "18px @8x", font=_font(13), fill=sub)
        if kind == "color":
            d.text((gx + 84, gy + 78), "on dark", font=_font(12), fill=sub)

    for form in ("single", "paired"):
        gx = col_x[form]
        cell(form, "color", gx, 200, "72px color")
        cell(form, "bw", gx, 420, "72px b&w")

    d.line([0, 590, W, 590], fill=(225, 225, 230), width=1)
    d.text((40, 612), "Read at 18px (actual size, left chips):",
           font=_font(18, True), fill=ink)
    d.text((40, 644),
           "SINGLE -> bold red organ, vessel + tan ureter cue survive; clearly "
           "not a flat bean.", font=_font(16), fill=green)
    d.text((40, 670),
           "PAIRED -> collapses to a red two-lobe blob (reads heart/peach); BW "
           "pair tangles in the middle.", font=_font(16), fill=red)
    d.text((40, 706),
           "Differentiation from beans emoji: organ color (maroon, not tan) + "
           "renal vessel + ureter at the hilum notch.", font=_font(16), fill=sub)
    d.text((40, 732),
           "All art is candidate-grade (vector built to house style). Final "
           "submission art needs a designer hinting pass at 18px.",
           font=_font(15), fill=sub)

    board.convert("RGB").save(OUT / "comparison_board.png")


if __name__ == "__main__":
    sys.exit(main())
