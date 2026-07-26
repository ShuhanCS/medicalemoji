"""Build original vector artwork for the organ emoji proposals.

The artwork is designed as an emoji glyph rather than an anatomy diagram:
one dominant silhouette, a dark keyline, restrained depth, and purpose-built
18x18 variants. The script writes editable SVG masters plus the four PNG
examples required by Unicode for Kidney, Stomach, and Liver.

Usage:
    python scripts/build_organ_proposal_assets.py
    python scripts/build_organ_proposal_assets.py --release v1.7.0
"""

import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE = "v1.7.0"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
MASTER_SIZE = 576


def svg_document(title: str, description: str, definitions: str, artwork: str) -> str:
    clean_definitions = "\n".join(line.rstrip() for line in definitions.strip().splitlines())
    clean_artwork = "\n".join(line.rstrip() for line in artwork.strip().splitlines())
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 72 72">
  <title>{title}</title>
  <desc>{description}</desc>
  <rect width="72" height="72" fill="#ffffff"/>
  <defs>{clean_definitions}</defs>
{clean_artwork}
</svg>
"""


def kidney_svg(color: bool, small: bool = False) -> str:
    body = (
        "M 1 -25 C 10 -24 13 -15 8 -6 C 6 -2 3 -2 3 1 "
        "C 3 4 6 5 8 10 C 11 18 9 24 1 25 C -11 27 -22 20 -25 8 "
        "C -28 0 -27 -9 -23 -15 C -18 -22 -8 -26 1 -25 Z"
    )
    small_body = (
        "M 2 -23 C 13 -23 17 -11 12 -1 C 12 4 12 7 11 11 "
        "C 13 17 10 24 1 25 C -12 27 -23 19 -26 7 "
        "C -29 -1 -27 -10 -23 -16 C -18 -23 -8 -24 2 -23 Z"
    )
    if color:
        definitions = """
    <radialGradient id="kidney-body" cx="34%" cy="30%" r="82%">
      <stop offset="0" stop-color="#D96D68"/>
      <stop offset="0.48" stop-color="#B44748"/>
      <stop offset="0.82" stop-color="#842A31"/>
      <stop offset="1" stop-color="#6B1B24"/>
    </radialGradient>
    <linearGradient id="ureter" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F1D8AC"/>
      <stop offset="1" stop-color="#D6AC72"/>
    </linearGradient>
    <linearGradient id="vessel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0645B"/>
      <stop offset="1" stop-color="#C93635"/>
    </linearGradient>
    <radialGradient id="shine" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.85"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
        """
        if small:
            artwork = f"""
  <g transform="translate(33 37) scale(1.22) rotate(-12)">
    <path d="{small_body}" fill="url(#kidney-body)" stroke="#5E1D26" stroke-width="2.4" stroke-linejoin="round"/>
    <path d="M 9 9 C 12 13 13 16 15 21" fill="none" stroke="#A9824E" stroke-width="6" stroke-linecap="round"/>
    <path d="M 9 9 C 12 13 13 16 15 21" fill="none" stroke="url(#ureter)" stroke-width="3.9" stroke-linecap="round"/>
    <ellipse cx="-12" cy="-9" rx="7.5" ry="4.5" transform="rotate(-28 -12 -9)" fill="url(#shine)"/>
  </g>"""
        else:
            artwork = f"""
  <g transform="translate(34 37) scale(1.2) rotate(-12)">
    <path d="{body}" fill="url(#kidney-body)" stroke="#5E1D26" stroke-width="2.3" stroke-linejoin="round"/>
    <ellipse cx="5" cy="0" rx="4.2" ry="5.1" fill="#8A3037" stroke="#5E1D26" stroke-width="1.7"/>
    <path d="M 4 -2 C 9 3 12 9 14 16" fill="none" stroke="#5E1D26" stroke-width="5.4" stroke-linecap="round"/>
    <path d="M 4 -2 C 9 3 12 9 14 16" fill="none" stroke="url(#vessel)" stroke-width="3.3" stroke-linecap="round"/>
    <path d="M 6 2 C 11 7 15 15 18 25" fill="none" stroke="#A9824E" stroke-width="5.8" stroke-linecap="round"/>
    <path d="M 6 2 C 11 7 15 15 18 25" fill="none" stroke="url(#ureter)" stroke-width="3.6" stroke-linecap="round"/>
    <ellipse cx="-12" cy="-10" rx="8" ry="4.8" transform="rotate(-28 -12 -10)" fill="url(#shine)"/>
    <ellipse cx="-15" cy="-13" rx="2.1" ry="1.25" transform="rotate(-28 -15 -13)" fill="#FFFFFF" opacity="0.86"/>
  </g>"""
        return svg_document(
            "Kidney emoji color reference artwork",
            "Original textless single-kidney paradigm with a hilum, vessel, and ureter.",
            definitions,
            artwork,
        )

    shape = small_body if small else body
    scale = "1.22" if small else "1.2"
    transform_x = "33" if small else "34"
    nub = "M 9 9 C 12 13 13 16 15 21" if small else "M 6 2 C 11 7 15 15 18 25"
    if small:
        artwork = f"""
  <g transform="translate({transform_x} 37) scale({scale}) rotate(-12)">
    <path d="{shape}" fill="#000000" stroke="#000000" stroke-width="2.2" stroke-linejoin="round"/>
    <path d="{nub}" fill="none" stroke="#000000" stroke-width="5.4" stroke-linecap="round"/>
    <ellipse cx="8" cy="7" rx="2.2" ry="2.5" fill="#FFFFFF" stroke="#000000" stroke-width="1.2"/>
  </g>"""
        return svg_document(
            "Kidney emoji black-and-white 18-pixel reference artwork",
            "Original textless black silhouette for the 18-pixel kidney paradigm.",
            "",
            artwork,
        )
    artwork = f"""
  <g transform="translate({transform_x} 37) scale({scale}) rotate(-12)">
    <path d="{shape}" fill="#FFFFFF" stroke="#000000" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="{nub}" fill="none" stroke="#000000" stroke-width="5.8" stroke-linecap="round"/>
    <path d="{nub}" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round"/>
    <ellipse cx="7" cy="6" rx="2.9" ry="3.2" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  </g>"""
    return svg_document(
        "Kidney emoji black-and-white reference artwork",
        "Original textless black-and-white single-kidney paradigm with a plumbing cue.",
        "",
        artwork,
    )


def stomach_svg(color: bool, small: bool = False) -> str:
    body = (
        "M 29 4 C 33 4 35 6 35 9 L 35 13 C 35 17 38 19 43 20 "
        "C 47 18 52 20 56 23 C 64 29 66 39 63 48 C 60 58 52 65 43 67 "
        "C 34 69 27 65 22 59 C 19 55 17 51 14 50 C 11 49 9 52 8 56 "
        "C 7 60 8 65 7 67 C 7 69 5 70 3 69 C 1 69 1 67 1 65 "
        "C 0 57 2 50 8 46 C 12 43 18 42 23 45 C 28 47 33 47 37 43 "
        "C 42 39 43 33 40 28 C 39 26 37 24 34 23 C 28 21 24 17 23 12 "
        "L 22 8 C 22 5 25 4 29 4 Z"
    )
    if color:
        definitions = """
    <linearGradient id="stomach-body" x1="0" y1="0" x2="0.55" y2="1">
      <stop offset="0" stop-color="#FF6A63"/>
      <stop offset="0.62" stop-color="#F04B46"/>
      <stop offset="1" stop-color="#E33133"/>
    </linearGradient>
    <radialGradient id="stomach-shine" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.72"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
        """
        stroke_width = "2.8" if small else "2.6"
        highlight = (
            '<ellipse cx="47" cy="25" rx="4.1" ry="2.5" transform="rotate(-50 47 25)" fill="url(#stomach-shine)"/>'
            if small
            else '<ellipse cx="47" cy="24" rx="6.2" ry="3.4" transform="rotate(-50 47 24)" fill="url(#stomach-shine)"/>'
        )
        artwork = f"""
  <path d="{body}" fill="url(#stomach-body)" stroke="#78122C" stroke-width="{stroke_width}" stroke-linejoin="round"/>
  {highlight}"""
        return svg_document(
            "Stomach emoji color reference artwork",
            "Original textless J-shaped stomach paradigm with a long inlet, deep inner concavity, and distinct short outlet.",
            definitions,
            artwork,
        )

    if small:
        artwork = f"""
  <path d="{body}" fill="#000000" stroke="#000000" stroke-width="2.8" stroke-linejoin="round"/>"""
        return svg_document(
            "Stomach emoji black-and-white 18-pixel reference artwork",
            "Original textless black silhouette with a long inlet, deep inner concavity, and distinct outlet.",
            "",
            artwork,
        )
    artwork = f"""
  <path d="{body}" fill="#FFFFFF" stroke="#000000" stroke-width="2.9" stroke-linejoin="round"/>"""
    return svg_document(
        "Stomach emoji black-and-white reference artwork",
        "Original textless black-and-white J-shaped stomach paradigm with a long inlet and distinct outlet.",
        "",
        artwork,
    )


def liver_svg(color: bool, small: bool = False) -> str:
    body = (
        "M 6 29 C 9 17 21 10 35 10 C 48 10 61 15 67 22 "
        "C 71 27 69 34 63 38 C 56 43 48 44 41 48 "
        "C 34 52 29 59 20 60 C 12 61 6 56 4 49 C 2 41 3 34 6 29 Z"
    )
    if color:
        definitions = """
    <radialGradient id="liver-body" cx="37%" cy="27%" r="88%">
      <stop offset="0" stop-color="#D46461"/>
      <stop offset="0.48" stop-color="#A83C43"/>
      <stop offset="0.84" stop-color="#7F2732"/>
      <stop offset="1" stop-color="#641C29"/>
    </radialGradient>
    <linearGradient id="gall" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#84AD58"/>
      <stop offset="1" stop-color="#4F7C37"/>
    </linearGradient>
    <radialGradient id="liver-shine" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.7"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
        """
        seam = "" if small else '<path d="M 43 13 C 42 25 40 36 38 47" fill="none" stroke="#76242F" stroke-width="2.1" stroke-linecap="round" opacity="0.82"/>'
        gall_size = ("M 41 45 C 45 44 48 47 47 52 C 46 57 43 60 40 58 C 37 56 37 52 38 49 C 39 47 40 46 41 45 Z" if not small else "M 42 46 C 46 46 47 50 45 54 C 43 57 39 55 39 52 C 39 49 40 47 42 46 Z")
        artwork = f"""
  <g transform="rotate(4 36 35)">
    <path d="{body}" fill="url(#liver-body)" stroke="#5E1D26" stroke-width="2.7" stroke-linejoin="round"/>
    {seam}
    <path d="{gall_size}" fill="url(#gall)" stroke="#355C2D" stroke-width="1.8" stroke-linejoin="round"/>
    <ellipse cx="23" cy="20" rx="9" ry="4.5" transform="rotate(-16 23 20)" fill="url(#liver-shine)"/>
    <ellipse cx="18" cy="18" rx="2" ry="1.1" transform="rotate(-16 18 18)" fill="#FFFFFF" opacity="0.78"/>
  </g>"""
        return svg_document(
            "Liver emoji color reference artwork",
            "Original textless asymmetric liver paradigm with a tucked gallbladder cue.",
            definitions,
            artwork,
        )

    if small:
        artwork = f"""
  <g transform="rotate(4 36 35)">
    <path d="{body}" fill="#000000" stroke="#000000" stroke-width="2.5" stroke-linejoin="round"/>
  </g>"""
        return svg_document(
            "Liver emoji black-and-white 18-pixel reference artwork",
            "Original textless black silhouette for the 18-pixel asymmetric liver paradigm.",
            "",
            artwork,
        )
    seam = '<path d="M 43 13 C 42 25 40 36 38 47" fill="none" stroke="#000000" stroke-width="2.2" stroke-linecap="round"/>'
    gall = "M 41 45 C 45 44 48 47 47 52 C 46 57 43 60 40 58 C 37 56 37 52 38 49 C 39 47 40 46 41 45 Z"
    artwork = f"""
  <g transform="rotate(4 36 35)">
    <path d="{body}" fill="#FFFFFF" stroke="#000000" stroke-width="2.9" stroke-linejoin="round"/>
    {seam}
    <path d="{gall}" fill="#000000" stroke="#000000" stroke-width="1.4" stroke-linejoin="round"/>
  </g>"""
    return svg_document(
        "Liver emoji black-and-white reference artwork",
        "Original textless black-and-white asymmetric liver paradigm.",
        "",
        artwork,
    )


BUILDERS = {
    "kidney": kidney_svg,
    "stomach": stomach_svg,
    "liver": liver_svg,
}


def force_two_tone(image: Image.Image) -> Image.Image:
    grayscale = image.convert("L")
    thresholded = grayscale.point(lambda value: 255 if value >= 180 else 0, mode="1")
    return thresholded.convert("RGB")


def render(svg: str, destination: Path, size: int, black_and_white: bool) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html, body {{ margin: 0; width: {MASTER_SIZE}px; height: {MASTER_SIZE}px; overflow: hidden; background: #fff; }}
svg {{ display: block; width: {MASTER_SIZE}px; height: {MASTER_SIZE}px; }}
</style></head><body>{svg}</body></html>"""
    with tempfile.TemporaryDirectory(prefix="medicalemoji-organ-art-") as temp_dir:
        temp = Path(temp_dir)
        html_path = temp / "render.html"
        raw_path = temp / "render.png"
        html_path.write_text(html, encoding="utf-8")
        subprocess.run(
            [
                str(CHROME),
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--window-size={MASTER_SIZE},{MASTER_SIZE}",
                f"--screenshot={raw_path}",
                html_path.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=60,
        )
        with Image.open(raw_path) as source:
            rendered = source.convert("RGB").resize((size, size), Image.Resampling.LANCZOS)
            if size == 18 and not black_and_white:
                rendered = rendered.filter(ImageFilter.UnsharpMask(radius=0.55, percent=85, threshold=2))
            if black_and_white:
                rendered = force_two_tone(rendered)
            rendered.save(destination, optimize=True)


def build_organ(name: str, release: Path) -> None:
    output = release / name / "images"
    output.mkdir(parents=True, exist_ok=True)
    builder = BUILDERS[name]
    for variant, is_color in (("color", True), ("bw", False)):
        master = builder(is_color, False)
        small = builder(is_color, True)
        (output / f"{name}_{variant}_SOURCE.svg").write_text(master, encoding="utf-8")
        (output / f"{name}_{variant}_18_SOURCE.svg").write_text(small, encoding="utf-8")
        for size in (18, 72):
            svg = small if size == 18 else master
            destination = output / f"{name}_{variant}_{size}x{size}_SUBMIT.png"
            render(svg, destination, size, black_and_white=not is_color)
            with Image.open(destination) as rendered:
                if rendered.size != (size, size):
                    raise RuntimeError(
                        f"{destination} rendered at {rendered.size}, expected {(size, size)}"
                    )
                if not is_color and len(rendered.convert("RGB").getcolors(maxcolors=256) or []) != 2:
                    raise RuntimeError(f"{destination} is not strict black-and-white artwork")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release",
        default=DEFAULT_RELEASE,
        help=f"Submission release directory name (default: {DEFAULT_RELEASE})",
    )
    args = parser.parse_args()
    release = ROOT / "submissions" / args.release
    for organ in BUILDERS:
        build_organ(organ, release)
    print(f"Built organ proposal artwork under {release}")


if __name__ == "__main__":
    main()
