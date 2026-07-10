"""Build v1.5.0 artwork with the revised mouse-maze paradigm.

Ultrasound and First Aid Kit retain the original v1.4.0 drawings. Maze is
redrawn as a broad labyrinth with a small mouse navigating its center.

Usage:
    python scripts/build_v1_5_proposal_assets.py
"""

from pathlib import Path

from PIL import Image
from reportlab.graphics import renderPM, renderSVG
from reportlab.graphics.shapes import Circle, Drawing, Ellipse, Line, Rect
from reportlab.lib import colors

from build_v1_4_proposal_assets import (
    base_drawing,
    first_aid_kit,
    force_two_tone,
    path,
    ultrasound,
    wall,
)


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "submissions" / "v1.5.0"


def mouse_maze(color: bool) -> Drawing:
    drawing = base_drawing()
    board = colors.HexColor("#F3C84B") if color else colors.white
    ink = colors.HexColor("#233747") if color else colors.black
    mouse_fill = colors.HexColor("#AEB8BC") if color else colors.black
    ear_fill = colors.HexColor("#E9A5AA") if color else colors.black

    drawing.add(Rect(5, 5, 62, 62, rx=9, ry=9, fillColor=board, strokeColor=None))

    # An entrance on the left and exit on the right frame a small central
    # chamber. The corridors remain broad enough for the mouse to survive at 18px.
    wall(drawing, 8, 8, 64, 8, ink)
    wall(drawing, 8, 64, 64, 64, ink)
    wall(drawing, 8, 8, 8, 25, ink)
    wall(drawing, 8, 39, 8, 64, ink)
    wall(drawing, 64, 8, 64, 45, ink)
    wall(drawing, 64, 57, 64, 64, ink)

    for coords in (
        (18, 8, 18, 29),
        (18, 40, 18, 54),
        (18, 54, 38, 54),
        (8, 40, 18, 40),
        (29, 18, 29, 35),
        (29, 18, 51, 18),
        (40, 8, 40, 18),
        (40, 29, 56, 29),
        (51, 40, 51, 64),
        (51, 40, 64, 40),
        (56, 29, 56, 40),
    ):
        wall(drawing, *coords, ink)

    # Side-on mouse silhouette: long tail, body, round head, ears, nose, eye.
    # A compact silhouette reads more reliably than anatomical top-down detail.
    tail = [("M", 29, 43), ("C", 23, 42, 20, 38, 23, 34), ("C", 25, 32, 28, 33, 29, 35)]
    drawing.add(path(tail, fill=None, stroke=ink, width=2.0))
    drawing.add(Ellipse(34, 43, 7, 4.5, fillColor=mouse_fill, strokeColor=ink, strokeWidth=1.4))
    drawing.add(Circle(41, 43, 4.3, fillColor=mouse_fill, strokeColor=ink, strokeWidth=1.3))
    drawing.add(Circle(39, 47, 2.6, fillColor=ear_fill, strokeColor=ink, strokeWidth=1.2))
    drawing.add(Circle(43, 46.5, 2.4, fillColor=ear_fill, strokeColor=ink, strokeWidth=1.2))
    drawing.add(Circle(45.5, 42, 1.4, fillColor=ink, strokeColor=None))
    drawing.add(Circle(42, 44, 0.9, fillColor=colors.white if not color else ink, strokeColor=None))
    drawing.add(Line(44, 41, 48, 39, strokeColor=ink, strokeWidth=0.8))
    drawing.add(Line(44, 42, 49, 42, strokeColor=ink, strokeWidth=0.8))
    return drawing


DRAWINGS = {
    "maze": mouse_maze,
    "ultrasound": ultrasound,
    "first-aid-kit": first_aid_kit,
}


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
    print(f"Built v1.5.0 proposal artwork under {RELEASE}")


if __name__ == "__main__":
    main()
