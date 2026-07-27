"""Generate and measure 18x18 Kidney candidates.

Renders kidney-pair designs at high resolution, downsamples to an exact 18x18
grid, and scores each against the same pinned Noto comparators and the same
IoU / dHash functions the repo validator uses.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(r"C:\Users\Shuha\projects\medicalemoji")
OUT = Path(__file__).parent / "cand"
OUT.mkdir(exist_ok=True)

# Reuse the repo validator's exact metric implementations.
spec = importlib.util.spec_from_file_location(
    "kv", REPO / "scripts" / "validate_kidney_artwork.py"
)
kv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kv)

S = 36  # supersample factor -> 648x648 working canvas
N = 18
W = N * S

MAROON = (150, 42, 46)
MAROON_DARK = (104, 26, 30)
MAROON_LIGHT = (186, 74, 74)


def bean_mask(w: int, h: int, notch_depth: float, notch_ry: float, flip: bool) -> Image.Image:
    """One kidney bean: rounded body with a notch carved from the medial edge."""
    pad = S
    img = Image.new("L", (w + 2 * pad, h + 2 * pad), 0)
    d = ImageDraw.Draw(img)
    d.ellipse([pad, pad, pad + w, pad + h], fill=255)

    # Carve the medial notch (right edge by default).
    nd = int(w * notch_depth)
    nh = int(h * notch_ry)
    cy = (h + 2 * pad) // 2
    d.ellipse(
        [pad + w - nd, cy - nh // 2, pad + w + nd, cy + nh // 2],
        fill=0,
    )
    if flip:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img


def compose(
    bw: bool,
    gap: float,
    offset: float,
    notch_depth: float,
    notch_ry: float,
    bean_w: float,
    bean_h: float,
    connector: bool,
    solid: bool,
) -> Image.Image:
    canvas = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    bwpx, bhpx = int(W * bean_w), int(W * bean_h)
    gappx = int(W * gap)
    offpx = int(W * offset)

    left = bean_mask(bwpx, bhpx, notch_depth, notch_ry, flip=False)
    right = bean_mask(bwpx, bhpx, notch_depth, notch_ry, flip=True)

    total_w = 2 * bwpx + gappx
    x0 = (W - total_w) // 2
    y_top = (W - bhpx - offpx) // 2

    fill = (0, 0, 0, 255) if bw else MAROON
    layer = Image.new("RGBA", (W, W), (0, 0, 0, 0))

    for msk, xoff, yoff in (
        (left, x0 - S, y_top - S),
        (right, x0 + bwpx + gappx - S, y_top + offpx - S),
    ):
        tint = Image.new("RGBA", msk.size, fill if bw else MAROON + (255,))
        layer.paste(tint, (xoff, yoff), msk)

    if connector:
        d = ImageDraw.Draw(layer)
        cy = y_top + bhpx // 2 + offpx // 2
        bar_h = int(W * connector)  # connector = fractional bar thickness
        # Push the bar deep into both lobes so it survives downsampling as one blob.
        d.rectangle(
            [
                x0 + int(bwpx * 0.55),
                cy - bar_h // 2,
                x0 + bwpx + gappx + int(bwpx * 0.45),
                cy + bar_h // 2,
            ],
            fill=fill if bw else MAROON_DARK + (255,),
        )

    canvas = Image.alpha_composite(canvas, layer)

    if not bw and solid:
        # Restrained shading: darker medial edge, one soft highlight per lobe.
        sh = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        ds = ImageDraw.Draw(sh)
        for xoff, yoff in ((x0, y_top), (x0 + bwpx + gappx, y_top + offpx)):
            ds.ellipse(
                [
                    xoff + int(bwpx * 0.18),
                    yoff + int(bhpx * 0.12),
                    xoff + int(bwpx * 0.48),
                    yoff + int(bhpx * 0.36),
                ],
                fill=MAROON_LIGHT + (255,),
            )
        alpha = canvas.split()[3]
        sh.putalpha(Image.eval(sh.split()[3], lambda v: v))
        tmp = Image.alpha_composite(canvas, sh)
        tmp.putalpha(alpha)
        canvas = tmp

    return canvas


def to18(img: Image.Image, bw: bool) -> Image.Image:
    small = img.resize((N, N), Image.Resampling.LANCZOS)
    px = small.load()
    out = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    op = out.load()
    for y in range(N):
        for x in range(N):
            r, g, b, a = px[x, y]
            if a < 110:
                op[x, y] = (0, 0, 0, 0)
            elif bw:
                op[x, y] = (0, 0, 0, 255)
            else:
                op[x, y] = (r, g, b, 255)
    return out


def score(img: Image.Image) -> dict:
    mask = kv.normalize_mask(img)
    dh = kv.difference_hash(mask)
    res = {}
    for name, (cp, sha) in kv.COMPARATORS.items():
        cimg, _ = kv.download_comparator(cp, sha)
        cmask = kv.normalize_mask(cimg)
        res[name] = {
            "iou": round(kv.intersection_over_union(mask, cmask), 3),
            "dhash": kv.hamming_distance(dh, kv.difference_hash(cmask)),
        }
    comps = kv.connected_components(kv.foreground_mask(img))
    res["_components"] = comps[:3]
    return res


def ascii_art(img: Image.Image) -> str:
    px = img.convert("RGBA").load()
    return "\n".join(
        "".join("#" if px[x, y][3] > 0 else "." for x in range(N)) for y in range(N)
    )


VARIANTS = {
    # name: (gap, offset, notch_depth, notch_ry, bean_w, bean_h, connector_thickness)
    "A_tight":     (0.09, 0.06, 0.42, 0.46, 0.38, 0.64, 0.10),
    "B_wide":      (0.14, 0.06, 0.44, 0.48, 0.36, 0.62, 0.12),
    "C_nooffset":  (0.11, 0.00, 0.44, 0.48, 0.38, 0.64, 0.10),
    "D_deepnotch": (0.11, 0.07, 0.52, 0.54, 0.39, 0.66, 0.11),
    "E_thinbar":   (0.11, 0.07, 0.46, 0.50, 0.38, 0.64, 0.08),
    "F_stout":     (0.10, 0.08, 0.46, 0.52, 0.41, 0.58, 0.11),
    "G_tall":      (0.12, 0.09, 0.44, 0.46, 0.35, 0.70, 0.12),
    "H_bigoffset": (0.10, 0.14, 0.46, 0.50, 0.38, 0.62, 0.11),
    "I_narrowgap": (0.07, 0.07, 0.48, 0.52, 0.40, 0.64, 0.09),
    "J_fatbar":    (0.11, 0.07, 0.48, 0.52, 0.38, 0.64, 0.15),
}

CUR = {"color": 0.698, "bw": 0.582}  # current v1.12.0-kidney.6 lungs IoU

if __name__ == "__main__":
    report = {}
    for name, (gap, off, nd, nry, bwd, bht, conn) in VARIANTS.items():
        for bw in (False, True):
            tag = f"{name}_{'bw' if bw else 'color'}"
            big = compose(bw, gap, off, nd, nry, bwd, bht, conn, solid=True)
            small = to18(big, bw)
            small.save(OUT / f"{tag}_18x18.png")
            prev = small.resize((N * 20, N * 20), Image.Resampling.NEAREST)
            bgim = Image.new("RGBA", prev.size, (255, 255, 255, 255))
            bgim.alpha_composite(prev)
            bgim.convert("RGB").save(OUT / f"{tag}_preview.png")
            report[tag] = score(small)
            report[tag]["ascii"] = ascii_art(small)
    (OUT / "scores.json").write_text(json.dumps(report, indent=2))

    hdr = f"{'candidate':20s} {'lungs':>6s} {'beans':>6s} {'dh_lg':>6s} {'comps':>14s} {'share':>6s} {'GATE':>6s}"
    print(hdr)
    print("-" * len(hdr))
    for tag, r in report.items():
        comps = r["_components"]
        share = comps[0] / sum(comps)
        conn_ok = len(comps) <= 2 and share >= 0.95
        iou_ok = all(
            r[c]["iou"] <= 0.72 and r[c]["dhash"] >= 16
            for c in kv.COMPARATORS
        )
        beats = r["lungs"]["iou"] < CUR["bw" if tag.endswith("bw") else "color"]
        gate = "PASS" if (conn_ok and iou_ok and beats) else "fail"
        print(
            f"{tag:20s} {r['lungs']['iou']:6.3f} {r['beans']['iou']:6.3f} "
            f"{r['lungs']['dhash']:6d} {str(comps):>14s} {share:6.2f} {gate:>6s}"
        )
