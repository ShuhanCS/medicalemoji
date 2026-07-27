"""Build exact-size Stomach proposal assets from the approved GPT Image 2 artwork.

The full-size source is the approved 1024x1024 project artwork. Color assets are
direct Lanczos reductions. Black-and-white assets use the source's non-white
silhouette, downsampled and thresholded back to a strict two-color palette.

Run from the repository root:

    python scripts/build_stomach_concept_assets.py
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "docs/design/stomach-emoji-2026-07/stomach-gpt-image-2-concept.png"
OUTPUT_DIR = REPO_ROOT / "docs/proposals/stomach-emoji-2026/candidate-v1.12/images"
EXPECTED_SOURCE_SHA256 = "250389e208e3d71488e1895b49c7d4fd69e95507eb3d06f73060db7b34767d7a"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> None:
    actual_source_hash = sha256(SOURCE)
    if actual_source_hash != EXPECTED_SOURCE_SHA256:
        raise ValueError(
            "Approved Stomach source hash changed: "
            f"expected {EXPECTED_SOURCE_SHA256}, got {actual_source_hash}"
        )

    source = Image.open(SOURCE).convert("RGB")
    if source.size != (1024, 1024):
        raise ValueError(f"Expected a 1024x1024 source, got {source.size}")

    # The approved source has a pure-white background and a fully connected,
    # saturated foreground. Preserve that exact outer silhouette for B&W.
    source_pixels = source.load()
    silhouette = Image.new("1", source.size, 1)
    silhouette_pixels = silhouette.load()
    for y in range(source.height):
        for x in range(source.width):
            silhouette_pixels[x, y] = 1 if source_pixels[x, y] == (255, 255, 255) else 0


    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for size in (18, 72):
        color = source.resize((size, size), Image.Resampling.LANCZOS)
        color_path = OUTPUT_DIR / f"stomach_color_{size}x{size}_SUBMIT.png"
        color.save(color_path, optimize=True)

        antialiased_mask = silhouette.convert("L").resize((size, size), Image.Resampling.LANCZOS)
        black_and_white = antialiased_mask.point(
            lambda value: 255 if value >= 128 else 0,
            mode="1",
        )
        bw_path = OUTPUT_DIR / f"stomach_bw_{size}x{size}_SUBMIT.png"
        black_and_white.save(bw_path, optimize=True)

        print(f"{color_path.relative_to(REPO_ROOT)} {sha256(color_path)}")
        print(f"{bw_path.relative_to(REPO_ROOT)} {sha256(bw_path)}")


if __name__ == "__main__":
    build()
