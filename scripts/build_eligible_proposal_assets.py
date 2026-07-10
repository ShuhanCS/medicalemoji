"""Build vector reference artwork for the clearly re-eligible 2026 slate.

The script writes editable SVG sources plus color and true black-and-white
18x18 and 72x72 PNGs for nine Medical Emoji portfolio concepts.

Usage:
    python scripts/build_eligible_proposal_assets.py
"""

from pathlib import Path

from PIL import Image
from reportlab.graphics import renderPM, renderSVG
from reportlab.graphics.shapes import Circle, Drawing, Ellipse, Line, Path as VectorPath, Rect
from reportlab.lib import colors


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "submissions" / "v1.3.0"


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


def white_blood_cell(color: bool) -> Drawing:
    drawing = base_drawing()
    membrane = colors.HexColor("#DDE7EA") if color else colors.white
    membrane_stroke = colors.HexColor("#8EA3AB") if color else colors.black
    nucleus = colors.HexColor("#6C4A9A") if color else colors.black
    drawing.add(Ellipse(36, 36, 26, 26, fillColor=membrane, strokeColor=membrane_stroke, strokeWidth=2.5))
    for x, y in ((15, 25), (19, 45), (34, 55), (50, 46), (55, 27), (41, 14), (25, 14)):
        drawing.add(Circle(x, y, 4, fillColor=membrane, strokeColor=membrane_stroke, strokeWidth=1.2))
    drawing.add(Ellipse(29.5, 37.5, 9.5, 8.5, fillColor=nucleus, strokeColor=nucleus, strokeWidth=1.5))
    drawing.add(Ellipse(43, 33, 9, 9, fillColor=nucleus, strokeColor=nucleus, strokeWidth=1.5))
    drawing.add(Ellipse(40.5, 45.5, 8.5, 7.5, fillColor=nucleus, strokeColor=nucleus, strokeWidth=1.5))
    return drawing


def hanging_bag(color: bool, *, blood: bool) -> Drawing:
    drawing = base_drawing()
    outline = colors.HexColor("#63727B") if color else colors.black
    shell = colors.HexColor("#F2F6F7") if color else colors.white
    fluid = colors.HexColor("#B52635") if blood else colors.HexColor("#6BBCEB")
    if not color:
        fluid = colors.black
    drawing.add(Circle(36, 65, 3, fillColor=colors.white, strokeColor=outline, strokeWidth=2))
    bag = [
        ("M", 18, 59), ("C", 17, 52, 17, 39, 19, 24),
        ("C", 20, 16, 25, 12, 36, 12), ("C", 47, 12, 52, 16, 53, 24),
        ("C", 55, 39, 55, 52, 54, 59), ("Z",),
    ]
    drawing.add(path(bag, fill=shell, stroke=outline, width=2.5))
    fluid_body = [
        ("M", 20, 41), ("C", 29, 45, 43, 38, 52, 42),
        ("L", 51, 24), ("C", 50, 18, 46, 15, 36, 15),
        ("C", 26, 15, 22, 18, 21, 24), ("Z",),
    ]
    drawing.add(path(fluid_body, fill=fluid, stroke=None, width=0))
    drawing.add(Rect(30, 8, 12, 5, fillColor=shell, strokeColor=outline, strokeWidth=1.5))
    drawing.add(Line(36, 8, 36, 1, strokeColor=outline, strokeWidth=2.5))
    if blood:
        drop = [
            ("M", 36, 35), ("C", 33, 31, 31, 28, 31, 25),
            ("C", 31, 20, 41, 20, 41, 25), ("C", 41, 28, 39, 31, 36, 35), ("Z",),
        ]
        drawing.add(path(drop, fill=colors.white, stroke=colors.white, width=0.8))
    return drawing


def blood_bag(color: bool) -> Drawing:
    return hanging_bag(color, blood=True)


def iv_bag(color: bool) -> Drawing:
    return hanging_bag(color, blood=False)


def pill_pack(color: bool) -> Drawing:
    drawing = base_drawing()
    shell = colors.HexColor("#D8E0E5") if color else colors.white
    stroke = colors.HexColor("#6F7A83") if color else colors.black
    pill = colors.HexColor("#F7FAFC") if color else colors.white
    drawing.add(Rect(17, 8, 38, 56, rx=7, ry=7, fillColor=shell, strokeColor=stroke, strokeWidth=2.5))
    for x in (27, 45):
        for y in (18, 32, 46, 58):
            drawing.add(Circle(x, y, 5, fillColor=pill, strokeColor=stroke, strokeWidth=1.5))
            if color:
                drawing.add(Line(x - 3, y + 2, x + 2, y + 4, strokeColor=colors.white, strokeWidth=1))
    return drawing


def weight_scale(color: bool) -> Drawing:
    drawing = base_drawing()
    body = colors.HexColor("#3D5967") if color else colors.white
    stroke = colors.HexColor("#22333B") if color else colors.black
    gauge = colors.HexColor("#EAF1F4") if color else colors.white
    drawing.add(Rect(8, 9, 56, 54, rx=11, ry=11, fillColor=body, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Ellipse(36, 48, 12, 10, fillColor=gauge, strokeColor=stroke, strokeWidth=2))
    drawing.add(Line(36, 47, 42, 52, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Circle(36, 47, 2.5, fillColor=stroke, strokeColor=None))
    if color:
        drawing.add(Line(15, 22, 57, 22, strokeColor=colors.HexColor("#7892A0"), strokeWidth=2))
    return drawing


def leg_cast(color: bool) -> Drawing:
    drawing = base_drawing()
    skin = colors.HexColor("#C9825B") if color else colors.white
    cast = colors.HexColor("#F4F5F5") if color else colors.white
    outline = colors.HexColor("#5E4A42") if color else colors.black
    cast_line = colors.HexColor("#9DA8AD") if color else colors.black
    upper = [
        ("M", 21, 65), ("C", 31, 66, 39, 59, 38, 50),
        ("C", 37, 43, 31, 39, 29, 33), ("L", 17, 36),
        ("C", 19, 43, 24, 47, 25, 52), ("C", 26, 57, 23, 61, 21, 65), ("Z",),
    ]
    drawing.add(path(upper, fill=skin, stroke=outline, width=2.5))
    lower = [
        ("M", 16, 38), ("L", 31, 34), ("C", 33, 27, 35, 21, 39, 17),
        ("C", 44, 12, 53, 14, 59, 11), ("C", 64, 8, 62, 4, 55, 4),
        ("L", 38, 6), ("C", 31, 7, 25, 12, 22, 18), ("Z",),
    ]
    drawing.add(path(lower, fill=cast, stroke=outline, width=2.5))
    for x1, y1, x2, y2 in ((20, 31, 31, 28), (23, 23, 34, 20), (28, 15, 40, 12)):
        drawing.add(Line(x1, y1, x2, y2, strokeColor=cast_line, strokeWidth=1.5))
    return drawing


def ct_scan(color: bool) -> Drawing:
    drawing = base_drawing()
    outer = colors.HexColor("#D9E0E4") if color else colors.white
    stroke = colors.HexColor("#66757D") if color else colors.black
    inner = colors.white
    table = colors.HexColor("#7BA6B8") if color else colors.white
    drawing.add(Ellipse(36, 42, 28, 26, fillColor=outer, strokeColor=stroke, strokeWidth=2.5))
    drawing.add(Ellipse(36, 42, 16, 15, fillColor=inner, strokeColor=stroke, strokeWidth=2))
    drawing.add(Rect(24, 5, 24, 31, rx=5, ry=5, fillColor=table, strokeColor=stroke, strokeWidth=2))
    drawing.add(Rect(28, 57, 16, 7, rx=2, ry=2, fillColor=stroke, strokeColor=None))
    return drawing


def pill_box(color: bool) -> Drawing:
    drawing = base_drawing()
    shell = colors.HexColor("#DDE5E9") if color else colors.white
    stroke = colors.HexColor("#687780") if color else colors.black
    drawing.add(Rect(5, 19, 62, 35, rx=7, ry=7, fillColor=shell, strokeColor=stroke, strokeWidth=2.5))
    fills = ["#F36C6C", "#F2A65A", "#F4D35E", "#75C98F", "#5FB7D3", "#7C83D8", "#B77AD8"]
    for index in range(7):
        x = 8 + index * 8.5
        fill = colors.HexColor(fills[index]) if color else colors.white
        drawing.add(Rect(x, 23, 7.5, 27, rx=2, ry=2, fillColor=fill, strokeColor=stroke, strokeWidth=1.2))
    drawing.add(Line(10, 58, 62, 58, strokeColor=stroke, strokeWidth=2))
    return drawing


def inhaler(color: bool) -> Drawing:
    drawing = base_drawing()
    stroke = colors.HexColor("#344A56") if color else colors.black
    body = colors.HexColor("#3D9CC2") if color else colors.white
    canister = colors.HexColor("#D9E0E4") if color else colors.white
    highlight = colors.HexColor("#87C8DF") if color else colors.white
    drawing.add(Rect(25, 46, 20, 20, rx=4, ry=4, fillColor=canister, strokeColor=stroke, strokeWidth=2.2))
    housing = [
        ("M", 18, 56), ("L", 50, 56), ("L", 50, 31),
        ("C", 50, 26, 54, 23, 59, 22), ("L", 64, 20),
        ("L", 63, 8), ("L", 50, 6), ("L", 36, 14), ("L", 20, 14), ("Z",),
    ]
    drawing.add(path(housing, fill=body, stroke=stroke, width=2.5))
    drawing.add(Rect(51, 10, 11, 8, rx=3, ry=3, fillColor=colors.white, strokeColor=stroke, strokeWidth=1.5))
    drawing.add(Line(24, 52, 46, 52, strokeColor=highlight, strokeWidth=2))
    drawing.add(Line(46, 18, 57, 18, strokeColor=highlight, strokeWidth=1.5))
    return drawing


DRAWINGS = {
    "white-blood-cell": white_blood_cell,
    "blood-bag": blood_bag,
    "pill-pack": pill_pack,
    "weight-scale": weight_scale,
    "leg-cast": leg_cast,
    "iv-bag": iv_bag,
    "ct-scan": ct_scan,
    "pill-box": pill_box,
    "inhaler": inhaler,
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


def main() -> None:
    for concept in DRAWINGS:
        build_concept(concept)
    print(f"Built eligible proposal artwork under {RELEASE}")


if __name__ == "__main__":
    main()
