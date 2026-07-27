"""Gen-2 Kidney 18x18: nestled lobes, no barbell.

Key change: satisfy the >=95% largest-component rule by letting the two lobes
touch at the notch lips (8-connected) instead of welding them with a centered
bar. Also uses a shallower notch so each lobe reads as a bean, not a "C".
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(r"C:\Users\Shuha\projects\medicalemoji")
OUT = Path(__file__).parent / "cand2"
OUT.mkdir(exist_ok=True)

spec = importlib.util.spec_from_file_location(
    "kv", REPO / "scripts" / "validate_kidney_artwork.py"
)
kv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kv)

S, N = 36, 18
W = N * S
MAROON = (150, 42, 46, 255)
MAROON_LIGHT = (190, 80, 78, 255)

_CACHE: dict[str, list] = {}


def cmask(cp, sha):
    if cp not in _CACHE:
        img, _ = kv.download_comparator(cp, sha)
        _CACHE[cp] = kv.normalize_mask(img)
    return _CACHE[cp]


def bean(w, h, notch_depth, notch_ry, notch_cy, flip):
    pad = S * 2
    img = Image.new("L", (w + 2 * pad, h + 2 * pad), 0)
    d = ImageDraw.Draw(img)
    d.ellipse([pad, pad, pad + w, pad + h], fill=255)
    nd = int(w * notch_depth)
    nh = int(h * notch_ry)
    cy = pad + int(h * notch_cy)
    d.ellipse([pad + w - nd, cy - nh // 2, pad + w + nd, cy + nh // 2], fill=0)
    if flip:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img


def compose(bw, gap, offset, nd, nry, ncy, bwf, bhf, tilt, ureter):
    layer = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    bwpx, bhpx = int(W * bwf), int(W * bhf)
    gappx = int(W * gap)          # may be negative -> overlap
    offpx = int(W * offset)
    pad = S * 2

    L = bean(bwpx, bhpx, nd, nry, ncy, False)
    R = bean(bwpx, bhpx, nd, nry, ncy, True)
    if tilt:
        L = L.rotate(-tilt, resample=Image.BICUBIC, expand=False)
        R = R.rotate(tilt, resample=Image.BICUBIC, expand=False)

    total_w = 2 * bwpx + gappx
    x0 = (W - total_w) // 2
    y_top = (W - bhpx - abs(offpx)) // 2

    fill = (0, 0, 0, 255) if bw else MAROON
    for msk, xo, yo in (
        (L, x0 - pad, y_top - pad),
        (R, x0 + bwpx + gappx - pad, y_top + offpx - pad),
    ):
        tint = Image.new("RGBA", msk.size, fill)
        layer.paste(tint, (xo, yo), msk)

    if ureter:
        # Short descending stub from the medial gap: anatomical, breaks barbell read.
        d = ImageDraw.Draw(layer)
        cx = x0 + bwpx + gappx // 2
        cy = y_top + int(bhpx * ncy) + offpx // 2
        t = max(int(W * 0.045), S // 2)
        d.rectangle([cx - t, cy - t, cx + t, cy + int(bhpx * 0.42)], fill=fill)

    if not bw:
        sh = ImageDraw.Draw(layer)
        for xo, yo in ((x0, y_top), (x0 + bwpx + gappx, y_top + offpx)):
            sh.ellipse(
                [
                    xo + int(bwpx * 0.20), yo + int(bhpx * 0.14),
                    xo + int(bwpx * 0.52), yo + int(bhpx * 0.34),
                ],
                fill=MAROON_LIGHT,
            )
    return layer


def to18(img, bw):
    small = img.resize((N, N), Image.Resampling.LANCZOS)
    px, out = small.load(), Image.new("RGBA", (N, N), (0, 0, 0, 0))
    op = out.load()
    for y in range(N):
        for x in range(N):
            r, g, b, a = px[x, y]
            op[x, y] = (0, 0, 0, 0) if a < 110 else ((0, 0, 0, 255) if bw else (r, g, b, 255))
    return out


def score(img):
    m = kv.normalize_mask(img)
    dh = kv.difference_hash(m)
    r = {}
    for name, (cp, sha) in kv.COMPARATORS.items():
        cm = cmask(cp, sha)
        r[name] = {
            "iou": round(kv.intersection_over_union(m, cm), 3),
            "dhash": kv.hamming_distance(dh, kv.difference_hash(cm)),
        }
    r["_components"] = kv.connected_components(kv.foreground_mask(img))[:3]
    return r


VARIANTS = {
    # name: gap, offset, notch_d, notch_ry, notch_cy, bean_w, bean_h, tilt, ureter
    "N1_kiss":      (0.005, 0.05, 0.34, 0.40, 0.50, 0.40, 0.66, 0, False),
    "N2_kiss_tilt": (0.005, 0.05, 0.34, 0.40, 0.50, 0.40, 0.66, 8, False),
    "N3_overlap":   (-0.02, 0.05, 0.36, 0.42, 0.50, 0.41, 0.68, 0, False),
    "N4_ureter":    (0.010, 0.05, 0.34, 0.40, 0.46, 0.40, 0.66, 0, True),
    "N5_shallow":   (0.005, 0.06, 0.28, 0.36, 0.50, 0.40, 0.68, 0, False),
    "N6_tilt_ur":   (0.005, 0.06, 0.32, 0.40, 0.46, 0.40, 0.68, 10, True),
    "N7_level":     (0.005, 0.00, 0.34, 0.40, 0.50, 0.40, 0.66, 0, False),
    "N8_tall_kiss": (0.005, 0.07, 0.32, 0.38, 0.50, 0.37, 0.74, 0, False),
    "N9_ov_tilt":   (-0.02, 0.06, 0.34, 0.40, 0.48, 0.41, 0.70, 8, False),
}
CUR = {"color": 0.698, "bw": 0.582}

if __name__ == "__main__":
    rep = {}
    for name, p in VARIANTS.items():
        for bw in (False, True):
            tag = f"{name}_{'bw' if bw else 'color'}"
            img = to18(compose(bw, *p), bw)
            img.save(OUT / f"{tag}_18x18.png")
            rep[tag] = score(img)
    (OUT / "scores.json").write_text(json.dumps(rep, indent=2))

    hdr = f"{'candidate':18s} {'lungs':>6s} {'beans':>6s} {'dh_lg':>6s} {'comps':>12s} {'share':>6s} {'GATE':>5s}"
    print(hdr); print("-" * len(hdr))
    for tag, r in rep.items():
        c = r["_components"]; share = c[0] / sum(c)
        ok = (len(c) <= 2 and share >= 0.95
              and all(r[k]["iou"] <= 0.72 and r[k]["dhash"] >= 16 for k in kv.COMPARATORS)
              and r["lungs"]["iou"] < CUR["bw" if tag.endswith("bw") else "color"])
        print(f"{tag:18s} {r['lungs']['iou']:6.3f} {r['beans']['iou']:6.3f} "
              f"{r['lungs']['dhash']:6d} {str(c):>12s} {share:6.2f} {'PASS' if ok else 'fail':>5s}")
