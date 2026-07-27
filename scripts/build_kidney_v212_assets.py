"""Build v2.1.2 Kidney example images from vector sources.

The v2.1.1 black-and-white assets lost the hilum: the medial concavity was
carried only by a 2px white stroke, which does not survive rasterization at
72x72 and disappears entirely at 18x18, leaving a featureless blob. This
script deepens the hilum into real path geometry so the concavity is
background rather than a hairline, and exports exact 18x18 and 72x72 in
color and true black-and-white.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import cairosvg
from PIL import Image

# Geometry is size-specific. At 72x72 there is room for a long curved ureter.
# At 18x18 a long thin tube fragments into loose pixels, so the ureter becomes
# a short thick stub and the hilum is rounded rather than wedge-shaped.
# In both cases the hilum is real path geometry, not a hairline stroke.
GEOM = {
    72: {
        "body": (
            "M30 7 C40 7 49 14 51 23 "
            "C53 30 44 33 37 36 "
            "C43 40 45 42 46 46 "
            "C50 51 48 58 41 63 "
            "C32 68 22 64 16 57 "
            "C9 48 8 36 11 26 "
            "C14 15 22 7 30 7 Z"
        ),
        "ureter": "M36 36 C44 44 50 54 53 62",
        "gap_path": "M44 45 C48 50 51 56 53 62",
        "gap_w": 8,
        "tube_w": 4,
        # Tan reads fine at 72px against white.
        "tube_color": "#e6cd8c",
    },
    18: {
        # Wider notch mouth and a stubbier body so the concavity reads at 1px steps.
        "body": (
            "M30 6 C41 6 50 13 52 23 "
            "C54 31 43 34 35 37 "
            "C43 41 46 43 47 47 "
            "C51 52 48 60 40 65 "
            "C30 69 20 65 14 57 "
            "C7 48 6 35 10 25 "
            "C14 14 22 6 30 6 Z"
        ),
        # Short stub: reaches only to y=54 so it survives as a solid mark.
        "ureter": "M35 37 C44 43 49 49 51 54",
        "gap_path": "M45 45 C48 49 50 52 51 54",
        "gap_w": 11,
        "tube_w": 6,
        # Darker tan: #e6cd8c washes out against white at 18px.
        "tube_color": "#c08f3c",
    },
}

SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 72 72'>"
    "<path d='{body}' fill='{body_fill}'{body_stroke}/>"
    "<path d='{ureter}' fill='none' stroke='{gap}' stroke-width='{gap_w}' stroke-linecap='round'/>"
    "<path d='{ureter}' fill='none' stroke='{tube}' stroke-width='{tube_w}' stroke-linecap='round'/>"
    "</svg>"
)


def svg_for(bw: bool, size: int) -> str:
    g = GEOM[size]
    if bw:
        return SVG.format(
            body=g["body"], body_fill="#000", body_stroke="",
            ureter=g["ureter"], gap="#fff", tube="#000",
            gap_w=g["gap_w"], tube_w=g["tube_w"],
        )
    return SVG.format(
        body=g["body"],
        body_fill="#a3362f",
        body_stroke=" stroke='#56110f' stroke-width='2'",
        ureter=g["ureter"],
        gap="#ffffff",
        tube=g["tube_color"],
        gap_w=g["gap_w"],
        tube_w=g["tube_w"],
    )


def _raster(path_d: str, stroke: str | None, width: int, fill: str, size: int, scale: int):
    """Rasterize one path at working resolution and return its alpha channel."""
    if stroke:
        body = f"<path d='{path_d}' fill='none' stroke='{stroke}' stroke-width='{width}' stroke-linecap='round'/>"
    else:
        body = f"<path d='{path_d}' fill='{fill}'/>"
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 72 72'>{body}</svg>"
    png = cairosvg.svg2png(
        bytestring=svg.encode(), output_width=size * scale, output_height=size * scale
    )
    import io

    return Image.open(io.BytesIO(png)).convert("RGBA").split()[3]


def export(bw: bool, size: int, out: Path, prefix: str) -> Path:
    """Composite body, transparent gap, and tube, then downsample to exact size.

    The gap is punched out as transparency rather than painted white. Opaque
    white would halo on dark backgrounds and would also be counted as part of
    the silhouette. The tube path starts inside the body while the gap path
    starts lower, so the tube stays attached and the artwork remains one
    connected component.
    """
    g = GEOM[size]
    scale = 16 if size == 18 else 4
    W = size * scale

    a_body = _raster(g["body"], None, 0, "#000", size, scale)
    a_gap = _raster(g["gap_path"], "#000", g["gap_w"], "", size, scale)
    a_tube = _raster(g["ureter"], "#000", g["tube_w"], "", size, scale)

    body_col = (0, 0, 0) if bw else (0xA3, 0x36, 0x2F)
    tube_col = (0, 0, 0) if bw else tuple(int(g["tube_color"][i : i + 2], 16) for i in (1, 3, 5))

    canvas = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    cp, bp, gp, tp = canvas.load(), a_body.load(), a_gap.load(), a_tube.load()
    for y in range(W):
        for x in range(W):
            if tp[x, y] > 128:
                cp[x, y] = tube_col + (255,)
            elif bp[x, y] > 128 and gp[x, y] <= 128:
                cp[x, y] = body_col + (255,)

    img = canvas.resize((size, size), Image.Resampling.LANCZOS)
    px = img.load()
    res = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    rp = res.load()
    for y in range(size):
        for x in range(size):
            r, gg, b, a = px[x, y]
            if a < 110:
                rp[x, y] = (0, 0, 0, 0)
            elif bw:
                rp[x, y] = (0, 0, 0, 255)
            else:
                rp[x, y] = (r, gg, b, 255)
    tag = "bw" if bw else "color"
    path = out / f"{prefix}_{tag}_{size}x{size}_SUBMIT.png"
    res.save(path)
    return path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--prefix", default="v2.1.2_kidney")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for bw in (False, True):
        for size in (18, 72):
            (out / f"{a.prefix}_{'bw' if bw else 'color'}_{size}_vector_SOURCE_REFERENCE_ONLY.svg").write_text(
                svg_for(bw, size), encoding="utf-8"
            )
            p = export(bw, size, out, a.prefix)
            print("wrote", p.name)
