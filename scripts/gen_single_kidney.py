"""Generate matched single-kidney example images for the v2.1.x packet.

Renders one kidney with a medial hilum and a short attached ureter at high
resolution, then downsamples to exact 18x18 and 72x72 in color and true
black-and-white. The black-and-white output keeps the hilum open (background)
so the kidney's defining concavity survives, which the v2.1.1 assets lost by
filling the hilum solid.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

SS = 24  # supersample factor
BODY = (163, 54, 48, 255)      # matches v2.1.1 body red
EDGE = (86, 20, 19, 255)       # matches v2.1.1 outline
HILITE = (184, 72, 65, 255)    # matches v2.1.1 highlight
URETER = (230, 205, 140, 255)  # matches v2.1.1 tan


def render(size: int, bw: bool, hilum: float, ureter_w: float) -> Image.Image:
    W = size * SS
    img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    fill = (0, 0, 0, 255) if bw else BODY
    edge = (0, 0, 0, 255) if bw else EDGE
    ure = (0, 0, 0, 255) if bw else URETER

    # Body: tall rounded bean occupying most of the frame.
    bx0, by0 = int(W * 0.10), int(W * 0.09)
    bx1, by1 = int(W * 0.74), int(W * 0.91)
    d.ellipse([bx0, by0, bx1, by1], fill=fill, outline=edge, width=max(SS // 2, 1))

    # Hilum: carve a concavity out of the medial (right) edge.
    cy = (by0 + by1) // 2
    hw = int((bx1 - bx0) * hilum)
    hh = int((by1 - by0) * 0.42)
    d.ellipse([bx1 - hw, cy - hh // 2, bx1 + hw, cy + hh // 2], fill=(0, 0, 0, 0))

    # Ureter: short tube leaving the hilum downward-right, attached at the top.
    uw = int(W * ureter_w)
    ux = bx1 - hw // 2
    pts = [(ux, cy - hh // 6), (int(W * 0.80), int(W * 0.62)), (int(W * 0.84), int(W * 0.92))]
    d.line(pts, fill=ure, width=uw, joint="curve")
    if not bw:
        d.line(pts, fill=(150, 128, 74, 255), width=max(uw // 4, 1), joint="curve")

    if not bw:
        d.ellipse(
            [int(W * 0.20), int(W * 0.18), int(W * 0.46), int(W * 0.40)], fill=HILITE
        )

    small = img.resize((size, size), Image.Resampling.LANCZOS)
    px = small.load()
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    op = out.load()
    for y in range(size):
        for x in range(size):
            r, g, b, a = px[x, y]
            if a < 110:
                op[x, y] = (0, 0, 0, 0)
            elif bw:
                op[x, y] = (0, 0, 0, 255)
            else:
                op[x, y] = (r, g, b, 255)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--prefix", default="v2.1.2_kidney")
    ap.add_argument("--hilum-72", type=float, default=0.34)
    ap.add_argument("--hilum-18", type=float, default=0.42)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for size, hil, uw in ((72, a.hilum_72, 0.055), (18, a.hilum_18, 0.075)):
        for bw in (False, True):
            im = render(size, bw, hil, uw)
            tag = "bw" if bw else "color"
            im.save(out / f"{a.prefix}_{tag}_{size}x{size}_SUBMIT.png")
            z = max(288 // size, 1)
            big = im.resize((size * z, size * z), Image.Resampling.NEAREST)
            bg = Image.new("RGBA", big.size, (255, 255, 255, 255))
            bg.alpha_composite(big)
            bg.convert("RGB").save(out / f"preview_{tag}_{size}.png")
    print("wrote", out)
