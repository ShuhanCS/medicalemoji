"""Validate Liver proposal assets and build a pinned comparator board."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


COMPARATORS = {
    "Anatomical Heart": ("anatomical_heart.png", "1fac0"),
    "Lungs": ("lungs.png", "1fac1"),
    "Brain": ("brain.png", "1f9e0"),
    "Cut of Meat": ("cut_of_meat.png", "1f969"),
    "Beans": ("beans.png", "1fad8"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def two_tone(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    white = Image.new("RGBA", rgba.size, "white")
    white.alpha_composite(rgba)
    return white.convert("L").point(lambda value: 255 if value >= 210 else 0).convert("RGB")


def foreground_mask(image: Image.Image) -> list[int]:
    rgb = image.convert("RGB")
    return [0 if r > 245 and g > 245 and b > 245 else 1 for r, g, b in rgb.get_flattened_data()]


def iou(left: Image.Image, right: Image.Image) -> float:
    a, b = foreground_mask(left), foreground_mask(right)
    intersection = sum(x and y for x, y in zip(a, b, strict=True))
    union = sum(x or y for x, y in zip(a, b, strict=True))
    return intersection / union if union else 1.0


def dhash(image: Image.Image) -> int:
    gray = image.convert("L").resize((9, 8), Image.Resampling.LANCZOS)
    pixels = list(gray.get_flattened_data())
    bits = 0
    for row in range(8):
        for col in range(8):
            bits = (bits << 1) | (pixels[row * 9 + col] > pixels[row * 9 + col + 1])
    return bits


def build_board(proposal_dir: Path, comparators: dict[str, Path], destination: Path) -> None:
    names = ["Liver", *comparators]
    width, height = 1260, 620
    board = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default(size=18)
    small_font = ImageFont.load_default(size=15)
    col_width = width // len(names)
    rows = [("Color 72", 72, False), ("Color 18", 18, False), ("B/W 72", 72, True), ("B/W 18", 18, True)]
    for col, name in enumerate(names):
        x0 = col * col_width
        draw.text((x0 + 12, 18), name, fill="black", font=font)
        source = (proposal_dir / "images/liver_color_72x72_SUBMIT.png") if name == "Liver" else comparators[name]
        for row, (label, size, bw) in enumerate(rows):
            y0 = 74 + row * 132
            if name == "Liver":
                kind = "bw" if bw else "color"
                image = Image.open(proposal_dir / f"images/liver_{kind}_{size}x{size}_SUBMIT.png").convert("RGB")
            else:
                image = Image.open(source).convert("RGBA")
                canvas = Image.new("RGBA", image.size, "white")
                canvas.alpha_composite(image)
                image = canvas.convert("RGB").resize((size, size), Image.Resampling.LANCZOS)
                if bw:
                    image = two_tone(image)
            scale = 1 if size == 72 else 4
            shown = image.resize((size * scale, size * scale), Image.Resampling.NEAREST if size == 18 else Image.Resampling.LANCZOS)
            board.paste(shown, (x0 + 70, y0 + 20))
            if col == 0:
                draw.text((12, y0 + 2), label, fill="#444444", font=small_font)
        draw.line((x0, 0, x0, height), fill="#dddddd", width=1)
    draw.rectangle((0, 0, width - 1, height - 1), outline="#999999", width=2)
    destination.parent.mkdir(parents=True, exist_ok=True)
    board.save(destination, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-dir", required=True, type=Path)
    args = parser.parse_args()
    proposal_dir = args.proposal_dir.resolve()
    validation_dir = proposal_dir / "validation"
    comparator_dir = validation_dir / "comparators/noto-emoji"
    comparators = {name: comparator_dir / filename for name, (filename, _) in COMPARATORS.items()}

    assets = {}
    for kind in ("color", "bw"):
        for size in (18, 72):
            path = proposal_dir / f"images/liver_{kind}_{size}x{size}_SUBMIT.png"
            image = Image.open(path).convert("RGB")
            assert image.size == (size, size)
            colors = image.getcolors(maxcolors=100000) or []
            if kind == "bw":
                assert {color for _, color in colors} <= {(0, 0, 0), (255, 255, 255)}
            assets[path.name] = {"sha256": sha256(path), "dimensions": [size, size], "colors": len(colors)}

    liver_72 = Image.open(proposal_dir / "images/liver_color_72x72_SUBMIT.png").convert("RGB")
    metrics = {}
    comparator_records = {}
    for name, path in comparators.items():
        source = Image.open(path).convert("RGBA")
        canvas = Image.new("RGBA", source.size, "white")
        canvas.alpha_composite(source)
        resized = canvas.convert("RGB").resize((72, 72), Image.Resampling.LANCZOS)
        metrics[name] = {
            "silhouette_iou": round(iou(liver_72, resized), 4),
            "dhash_distance": (dhash(liver_72) ^ dhash(resized)).bit_count(),
        }
        comparator_records[name] = {
            "sha256": sha256(path),
            "source": f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u{COMPARATORS[name][1]}.png",
        }

    board = validation_dir / "liver-comparison-board.png"
    build_board(proposal_dir, comparators, board)
    report = {
        "proposal": "Liver",
        "technical_scope": "Exact dimensions, palette, hashes, and separation against pinned comparators.",
        "assets": assets,
        "comparators": comparator_records,
        "metrics": metrics,
        "comparison_board": {"path": board.name, "sha256": sha256(board)},
    }
    (validation_dir / "computer-validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = ["# Liver Artwork Computer Validation", "", "Reproducible checks cover exact dimensions, palette, hashes, and separation against pinned comparators.", "", "| Comparator | Silhouette IoU | 64-bit dHash distance |", "| --- | ---: | ---: |"]
    lines.extend(f"| {name} | {value['silhouette_iou']:.4f} | {value['dhash_distance']} |" for name, value in metrics.items())
    lines.extend(["", f"Comparison board: `{board.name}`", "", "Pinned assets and hashes are recorded in `computer-validation.json`."])
    (validation_dir / "computer-validation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(validation_dir / "computer-validation.json")


if __name__ == "__main__":
    main()
