"""Build original vector reference artwork for the 2026 organ proposals.

The script writes editable SVG sources plus the four PNG examples required by
Unicode for Kidney, Stomach, and Liver: color and black-and-white at 18x18 and
72x72 pixels.

Usage:
    python scripts/build_organ_proposal_assets.py
"""

from pathlib import Path

from PIL import Image
from reportlab.graphics import renderPM, renderSVG
from reportlab.graphics.shapes import Drawing, Ellipse, Line, Path as VectorPath, Rect
from reportlab.lib import colors


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "submissions" / "v1.2.0"


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


def kidney(color: bool) -> Drawing:
    drawing = base_drawing()
    fill = colors.HexColor("#B33A4A") if color else colors.white
    stroke = colors.HexColor("#70202D") if color else colors.black
    left = [
        ("M", 27, 11),
        ("C", 18, 8, 10, 15, 9, 29),
        ("C", 8, 42, 13, 53, 22, 55),
        ("C", 29, 56, 33, 49, 29, 42),
        ("C", 27, 38, 23, 37, 23, 32),
        ("C", 23, 28, 25, 26, 29, 25),
        ("C", 34, 23, 34, 15, 27, 11),
        ("Z",),
    ]
    right = [
        ("M", 45, 11),
        ("C", 54, 8, 62, 15, 63, 29),
        ("C", 64, 42, 59, 53, 50, 55),
        ("C", 43, 56, 39, 49, 43, 42),
        ("C", 45, 38, 49, 37, 49, 32),
        ("C", 49, 28, 47, 26, 43, 25),
        ("C", 38, 23, 38, 15, 45, 11),
        ("Z",),
    ]
    drawing.add(path(left, fill=fill, stroke=stroke, width=2.5))
    drawing.add(path(right, fill=fill, stroke=stroke, width=2.5))

    ureter = colors.HexColor("#D0A47B") if color else colors.black
    if color:
        vessel_red = colors.HexColor("#D64A3A")
        vessel_blue = colors.HexColor("#2C78B8")
        drawing.add(Line(35, 9, 35, 33, strokeColor=vessel_red, strokeWidth=2.5))
        drawing.add(Line(38, 10, 38, 33, strokeColor=vessel_blue, strokeWidth=2.5))
        drawing.add(Line(35, 27, 29, 31, strokeColor=vessel_red, strokeWidth=2))
        drawing.add(Line(38, 27, 43, 31, strokeColor=vessel_blue, strokeWidth=2))
    else:
        drawing.add(Line(36, 10, 36, 29, strokeColor=colors.black, strokeWidth=2))
        drawing.add(Line(36, 27, 29, 32, strokeColor=colors.black, strokeWidth=2))
        drawing.add(Line(36, 27, 43, 32, strokeColor=colors.black, strokeWidth=2))
    drawing.add(Line(28, 37, 31, 63, strokeColor=ureter, strokeWidth=2.5))
    drawing.add(Line(44, 37, 41, 63, strokeColor=ureter, strokeWidth=2.5))
    return drawing


def stomach(color: bool) -> Drawing:
    drawing = base_drawing()
    fill = colors.HexColor("#F04F68") if color else colors.white
    stroke = colors.HexColor("#A62243") if color else colors.black
    inner = colors.HexColor("#D63355") if color else colors.black

    # Esophagus, deliberately textless and simplified for small-size legibility.
    drawing.add(
        Rect(
            22,
            49,
            12,
            20,
            rx=5,
            ry=5,
            fillColor=fill,
            strokeColor=stroke,
            strokeWidth=2.5,
        )
    )
    body = [
        ("M", 26, 56),
        ("C", 24, 50, 25, 45, 30, 41),
        ("C", 34, 38, 40, 39, 46, 38),
        ("C", 57, 36, 64, 29, 63, 20),
        ("C", 62, 11, 52, 7, 43, 10),
        ("C", 35, 12, 31, 20, 27, 24),
        ("C", 23, 28, 18, 27, 16, 21),
        ("C", 14, 16, 9, 13, 6, 17),
        ("C", 3, 21, 6, 29, 12, 32),
        ("C", 19, 36, 23, 40, 22, 45),
        ("C", 21, 50, 20, 53, 22, 57),
        ("Z",),
    ]
    drawing.add(path(body, fill=fill, stroke=stroke, width=2.5))
    drawing.add(Line(27, 55, 27, 47, strokeColor=inner, strokeWidth=2))
    drawing.add(Line(27, 47, 31, 41, strokeColor=inner, strokeWidth=2))
    return drawing


def liver(color: bool) -> Drawing:
    drawing = base_drawing()
    fill = colors.HexColor("#A83B3F") if color else colors.white
    stroke = colors.HexColor("#692327") if color else colors.black
    crease = colors.HexColor("#7F2A30") if color else colors.black
    gall = colors.HexColor("#5B8F3D") if color else colors.white

    body = [
        ("M", 6, 37),
        ("C", 10, 55, 24, 63, 40, 58),
        ("C", 49, 55, 58, 55, 66, 49),
        ("C", 70, 45, 68, 38, 62, 34),
        ("C", 54, 28, 46, 29, 37, 25),
        ("C", 29, 22, 20, 17, 12, 20),
        ("C", 5, 23, 3, 30, 6, 37),
        ("Z",),
    ]
    drawing.add(path(body, fill=fill, stroke=stroke, width=2.5))

    crease_path = [
        ("M", 42, 57),
        ("C", 40, 48, 38, 39, 36, 29),
    ]
    drawing.add(path(crease_path, fill=None, stroke=crease, width=2))
    gall_x, gall_y, gall_w, gall_h = (28, 19, 7, 9) if color else (29, 20, 5, 7)
    drawing.add(
        Ellipse(
            gall_x,
            gall_y,
            gall_w,
            gall_h,
            fillColor=gall if color else colors.black,
            strokeColor=colors.HexColor("#355C28") if color else colors.black,
            strokeWidth=1.5,
        )
    )
    drawing.add(
        Line(
            33,
            25,
            37,
            32,
            strokeColor=colors.black if not color else colors.HexColor("#355C28"),
            strokeWidth=2,
        )
    )
    return drawing


DRAWINGS = {
    "kidney": kidney,
    "stomach": stomach,
    "liver": liver,
}


def force_two_tone(path: Path) -> None:
    with Image.open(path) as source:
        grayscale = source.convert("L")
        thresholded = grayscale.point(lambda value: 255 if value >= 180 else 0, mode="1")
        thresholded.convert("RGB").save(path, optimize=True)


def build_organ(name: str) -> None:
    output = RELEASE / name / "images"
    output.mkdir(parents=True, exist_ok=True)
    for variant, is_color in (("color", True), ("bw", False)):
        drawing = DRAWINGS[name](is_color)
        renderSVG.drawToFile(
            drawing,
            str(output / f"{name}_{variant}_SOURCE.svg"),
            showBoundary=False,
        )
        for size in (18, 72):
            destination = output / f"{name}_{variant}_{size}x{size}_SUBMIT.png"
            renderPM.drawToFile(
                drawing,
                str(destination),
                fmt="PNG",
                dpi=size,
                bg=colors.white,
            )
            if not is_color:
                force_two_tone(destination)
            with Image.open(destination) as rendered:
                if rendered.size != (size, size):
                    raise RuntimeError(
                        f"{destination} rendered at {rendered.size}, expected {(size, size)}"
                    )


def main() -> None:
    for organ in DRAWINGS:
        build_organ(organ)
    print(f"Built organ proposal artwork under {RELEASE}")


if __name__ == "__main__":
    main()
