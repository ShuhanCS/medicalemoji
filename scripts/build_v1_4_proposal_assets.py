"""Build original reference artwork for the v1.4.0 proposal release.

The script writes editable SVG sources plus color and true black-and-white
18x18 and 72x72 PNGs for Maze, Ultrasound, and First Aid Kit.

Usage:
    python scripts/build_v1_4_proposal_assets.py
"""

from pathlib import Path

from PIL import Image
from reportlab.graphics import renderPM, renderSVG
from reportlab.graphics.shapes import Circle, Drawing, Line, Path as VectorPath, Rect
from reportlab.lib import colors


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "submissions" / "v1.4.0"


def path(commands: list[tuple], *, fill, stroke, width: float) -> VectorPath:
    item = VectorPath()
    for command in commands:
        op, *values = command
        if op == "M":
            item.moveTo(*values)
        elif op == "L":
            item.lineTo(*values)
        elif op == "C":
            item.curveTo(*values)
        elif op == "Z":
            item.closePath()
        else:
            raise ValueError(f"Unsupported path command: {op}")
    item.fillColor = fill
    item.strokeColor = stroke
    item.strokeWidth = width
    item.strokeLineJoin = 1
    item.strokeLineCap = 1
    return item


def base_drawing() -> Drawing:
    drawing = Drawing(72, 72)
    drawing.add(Rect(0, 0, 72, 72, fillColor=colors.white, strokeColor=None))
    return drawing


def wall(drawing: Drawing, x1: float, y1: float, x2: float, y2: float, color) -> None:
    line = Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=4.5)
    line.strokeLineCap = 1
    drawing.add(line)


def maze(color: bool) -> Drawing:
    drawing = base_drawing()
    board = colors.HexColor("#F3C84B") if color else colors.white
    ink = colors.HexColor("#233747") if color else colors.black
    drawing.add(Rect(5, 5, 62, 62, rx=9, ry=9, fillColor=board, strokeColor=None))

    # The outer wall leaves a left entrance and right exit. Internal walls use
    # broad, uneven corridors so the paradigm reads as a maze rather than a QR code.
    wall(drawing, 8, 8, 64, 8, ink)
    wall(drawing, 8, 64, 64, 64, ink)
    wall(drawing, 8, 8, 8, 25, ink)
    wall(drawing, 8, 39, 8, 64, ink)
    wall(drawing, 64, 8, 64, 45, ink)
    wall(drawing, 64, 57, 64, 64, ink)

    for coords in (
        (18, 8, 18, 29),
        (18, 40, 18, 54),
        (18, 54, 40, 54),
        (8, 40, 18, 40),
        (29, 18, 29, 43),
        (29, 18, 51, 18),
        (40, 29, 40, 54),
        (40, 29, 56, 29),
        (40, 8, 40, 18),
        (51, 40, 51, 64),
        (51, 40, 64, 40),
        (56, 29, 56, 40),
    ):
        wall(drawing, *coords, ink)
    return drawing


def ultrasound(color: bool) -> Drawing:
    drawing = base_drawing()
    stroke = colors.HexColor("#304A59") if color else colors.black
    shell = colors.HexColor("#DDE7EB") if color else colors.white
    screen = colors.HexColor("#163D52") if color else colors.black
    scan = colors.HexColor("#65C8D0") if color else colors.white

    drawing.add(Rect(7, 27, 44, 38, rx=5, ry=5, fillColor=shell, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Rect(12, 34, 34, 25, rx=2, ry=2, fillColor=screen, strokeColor=stroke, strokeWidth=1.5))
    scan_wedge = [
        ("M", 29, 36),
        ("C", 22, 41, 18, 48, 17, 55),
        ("C", 25, 58, 34, 58, 42, 55),
        ("C", 40, 48, 36, 41, 29, 36),
        ("Z",),
    ]
    drawing.add(path(scan_wedge, fill=scan, stroke=None, width=0))
    scan_line = screen if color else colors.black
    drawing.add(Line(21, 53, 37, 53, strokeColor=scan_line, strokeWidth=1.4))
    drawing.add(Line(24, 48, 34, 48, strokeColor=scan_line, strokeWidth=1.4))

    drawing.add(Line(29, 27, 29, 16, strokeColor=stroke, strokeWidth=3))
    drawing.add(Line(18, 14, 40, 14, strokeColor=stroke, strokeWidth=3.5))
    drawing.add(Line(20, 14, 16, 8, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Line(38, 14, 42, 8, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Circle(15, 7, 2.5, fillColor=stroke, strokeColor=None))
    drawing.add(Circle(43, 7, 2.5, fillColor=stroke, strokeColor=None))

    cable = [("M", 50, 31), ("C", 61, 28, 62, 16, 52, 13)]
    drawing.add(path(cable, fill=None, stroke=stroke, width=2.2))
    probe = [
        ("M", 51, 42),
        ("L", 59, 38),
        ("L", 55, 29),
        ("C", 54, 27, 50, 28, 49, 31),
        ("L", 46, 38),
        ("Z",),
    ]
    drawing.add(path(probe, fill=shell, stroke=stroke, width=2.2))
    drawing.add(Line(48, 39, 58, 35, strokeColor=stroke, strokeWidth=3))
    return drawing


def first_aid_kit(color: bool) -> Drawing:
    drawing = base_drawing()
    case = colors.HexColor("#2E9C72") if color else colors.white
    dark = colors.HexColor("#176B50") if color else colors.black
    cross = colors.white if color else colors.black

    drawing.add(Rect(25, 55, 22, 11, rx=4, ry=4, fillColor=colors.white, strokeColor=dark, strokeWidth=3))
    drawing.add(Rect(6, 10, 60, 49, rx=9, ry=9, fillColor=case, strokeColor=dark, strokeWidth=3))
    drawing.add(Line(9, 47, 63, 47, strokeColor=dark, strokeWidth=2))
    drawing.add(Rect(30, 22, 12, 26, rx=2, ry=2, fillColor=cross, strokeColor=None))
    drawing.add(Rect(23, 29, 26, 12, rx=2, ry=2, fillColor=cross, strokeColor=None))
    drawing.add(Rect(13, 44, 7, 6, rx=1, ry=1, fillColor=colors.white if color else colors.black, strokeColor=dark, strokeWidth=1))
    drawing.add(Rect(52, 44, 7, 6, rx=1, ry=1, fillColor=colors.white if color else colors.black, strokeColor=dark, strokeWidth=1))
    return drawing


DRAWINGS = {
    "maze": maze,
    "ultrasound": ultrasound,
    "first-aid-kit": first_aid_kit,
}


def force_two_tone(destination: Path) -> None:
    with Image.open(destination) as source:
        grayscale = source.convert("L")
        thresholded = grayscale.point(lambda value: 255 if value >= 180 else 0, mode="1")
        thresholded.convert("RGB").save(destination, optimize=True)


def build_concept(name: str) -> None:
    output = RELEASE / name / "images"
    output.mkdir(parents=True, exist_ok=True)
    for variant, is_color in (("color", True), ("bw", False)):
        drawing = DRAWINGS[name](is_color)
        renderSVG.drawToFile(drawing, str(output / f"{name}_{variant}_SOURCE.svg"), showBoundary=False)
        for size in (18, 72):
            destination = output / f"{name}_{variant}_{size}x{size}_SUBMIT.png"
            renderPM.drawToFile(drawing, str(destination), fmt="PNG", dpi=size, bg=colors.white)
            if not is_color:
                force_two_tone(destination)
            with Image.open(destination) as rendered:
                if rendered.size != (size, size):
                    raise RuntimeError(f"{destination} rendered at {rendered.size}, expected {(size, size)}")
                if not is_color:
                    values = set(rendered.convert("L").getdata())
                    if not values.issubset({0, 255}):
                        raise RuntimeError(f"{destination} is not true black-and-white: {sorted(values)}")


def main() -> None:
    for concept in DRAWINGS:
        build_concept(concept)
    print(f"Built v1.4.0 proposal artwork under {RELEASE}")


if __name__ == "__main__":
    main()
