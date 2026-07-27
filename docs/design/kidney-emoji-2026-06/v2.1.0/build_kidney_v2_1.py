#!/usr/bin/env python3
"""Build the native-size v2.1.0 Kidney proposal artwork.

The color artwork is a restrained flat vector-like rendering. The black-and-
white artwork is intentionally quantized to black, white, and transparency so
it cannot contain opaque grayscale pixels.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
OUT = HERE / "final"
REFERENCE = HERE / "reference_only"
OUT.mkdir(exist_ok=True)
REFERENCE.mkdir(exist_ok=True)

SCALE = 4
TRANSPARENT = (0, 0, 0, 0)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
DARK = (83, 19, 18, 255)
MAROON = (163, 54, 48, 255)
LIGHT_MAROON = (184, 72, 65, 255)
TAN_DARK = (137, 103, 53, 255)
TAN = (228, 202, 137, 255)


def cubic(start, first, second, end, steps=10):
    points = []
    for i in range(steps):
        t = i / steps
        mt = 1 - t
        x = mt**3 * start[0] + 3 * mt**2 * t * first[0] + 3 * mt * t**2 * second[0] + t**3 * end[0]
        y = mt**3 * start[1] + 3 * mt**2 * t * first[1] + 3 * mt * t**2 * second[1] + t**3 * end[1]
        points.append((x, y))
    return points


def kidney_path_72():
    """Single renal outline; the medial concavity is on the viewer's right."""
    segments = [
        ((30, 7), (40, 7), (49, 14), (51, 23)),
        ((51, 23), (53, 29), (47, 33), (42, 35)),
        ((42, 35), (39, 38), (41, 41), (45, 44)),
        ((45, 44), (50, 50), (48, 58), (41, 63)),
        ((41, 63), (32, 68), (22, 64), (16, 57)),
        ((16, 57), (9, 48), (8, 36), (11, 26)),
        ((11, 26), (14, 15), (22, 7), (30, 7)),
    ]
    points = []
    for segment in segments:
        points.extend(cubic(*segment))
    return points


def scaled(points, factor, anchor=(30, 36)):
    return [
        (anchor[0] + (x - anchor[0]) * factor, anchor[1] + (y - anchor[1]) * factor)
        for x, y in points
    ]


def at_scale(points):
    return [(round(x * SCALE), round(y * SCALE)) for x, y in points]


def render_72(color=True, variant="a"):
    canvas = Image.new("RGBA", (72 * SCALE, 72 * SCALE), TRANSPARENT)
    draw = ImageDraw.Draw(canvas)
    outer = at_scale(kidney_path_72())
    inner = at_scale(scaled(kidney_path_72(), 0.92))
    ureter = at_scale([(42, 37), (47, 44), (51, 54), (54, 62)])

    if color:
        draw.polygon(outer, fill=DARK)
        draw.polygon(inner, fill=MAROON)
        # One restrained, flat upper-left body plane; no gradient or gloss.
        draw.polygon(at_scale([(18, 22), (27, 13), (37, 15), (31, 32), (19, 38), (14, 31)]), fill=LIGHT_MAROON)
        draw.line(ureter, fill=TAN_DARK, width=6 * SCALE, joint="curve")
        draw.line(ureter, fill=TAN, width=3 * SCALE, joint="curve")
    elif variant == "a":
        # Selected B&W option: solid black body maximizes native-size contrast on white.
        # A small white hilum landmark and the white ureter rim retain a cue on dark fields.
        draw.polygon(outer, fill=BLACK)
        draw.line(at_scale([(46, 31), (41, 36), (45, 42)]), fill=WHITE, width=2 * SCALE, joint="curve")
        draw.line(ureter, fill=WHITE, width=7 * SCALE, joint="curve")
        draw.line(ureter, fill=BLACK, width=3 * SCALE, joint="curve")
    else:
        # Reference-only alternate: white body with heavy black outline.
        draw.polygon(outer, fill=BLACK)
        draw.polygon(inner, fill=WHITE)
        draw.line(ureter, fill=BLACK, width=6 * SCALE, joint="curve")
        draw.line(ureter, fill=WHITE, width=2 * SCALE, joint="curve")

    image = canvas.resize((72, 72), Image.Resampling.LANCZOS)
    return image if color else binary_black_white(image)


def binary_black_white(image):
    """Keep antialiased edges through alpha, never opaque grayscale RGB."""
    result = Image.new("RGBA", image.size, TRANSPARENT)
    source = image.load()
    target = result.load()
    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, alpha = source[x, y]
            if alpha < 12:
                continue
            target[x, y] = WHITE if (red + green + blue) >= 384 else BLACK
            if alpha < 255:
                target[x, y] = (*target[x, y][:3], alpha)
    return result


# Purpose-built 18px geometry. It is not a resize of the 72px art.
OUTER_18 = [
    (7, 1), (10, 1), (12, 3), (13, 5), (12, 7), (10, 8),
    (10, 10), (12, 12), (12, 14), (10, 16), (7, 16), (4, 15),
    (2, 13), (1, 10), (1, 7), (2, 5), (4, 2),
]
INNER_18 = [
    (7, 2), (9, 2), (11, 4), (11, 6), (9, 8), (9, 10),
    (11, 12), (10, 14), (8, 15), (5, 14), (3, 12), (2, 9),
    (2, 6), (4, 3),
]
URETER_18 = [(10, 9), (12, 12), (13, 15)]


def render_18(color=True, variant="a"):
    image = Image.new("RGBA", (18, 18), TRANSPARENT)
    draw = ImageDraw.Draw(image)
    if color:
        draw.polygon(OUTER_18, fill=DARK)
        draw.polygon(INNER_18, fill=MAROON)
        draw.polygon([(4, 4), (7, 2), (9, 3), (7, 6), (4, 7), (3, 6)], fill=LIGHT_MAROON)
        draw.line(URETER_18, fill=TAN_DARK, width=3)
        draw.line(URETER_18, fill=TAN, width=1)
    elif variant == "a":
        draw.polygon(OUTER_18, fill=BLACK)
        draw.line([(11, 8), (9, 9), (11, 11)], fill=WHITE, width=1)
        draw.line(URETER_18, fill=WHITE, width=3)
        draw.line(URETER_18, fill=BLACK, width=1)
    else:
        draw.polygon(OUTER_18, fill=BLACK)
        draw.polygon(INNER_18, fill=WHITE)
        draw.line(URETER_18, fill=BLACK, width=3)
        draw.line(URETER_18, fill=WHITE, width=1)
    return image if color else binary_black_white(image)


def svg(color=True, variant="a"):
    body = "M30 7 C40 7 49 14 51 23 C53 29 47 33 42 35 C39 38 41 41 45 44 C50 50 48 58 41 63 C32 68 22 64 16 57 C9 48 8 36 11 26 C14 15 22 7 30 7 Z"
    ureter = "M42 37 C47 44 51 54 54 62"
    if color:
        return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 72 72'><path d='{body}' fill='#531312'/><path d='{body}' fill='#a33630' transform='translate(2.4 2.9) scale(.92)'/><path d='{ureter}' fill='none' stroke='#896735' stroke-width='6' stroke-linecap='round'/><path d='{ureter}' fill='none' stroke='#e4ca89' stroke-width='3' stroke-linecap='round'/></svg>\n"""
    if variant == "a":
        return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 72 72'><path d='{body}' fill='#000'/><path d='M46 31 C41 36 41 38 45 42' fill='none' stroke='#fff' stroke-width='2' stroke-linecap='round'/><path d='{ureter}' fill='none' stroke='#fff' stroke-width='7' stroke-linecap='round'/><path d='{ureter}' fill='none' stroke='#000' stroke-width='3' stroke-linecap='round'/></svg>\n"""
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 72 72'><path d='{body}' fill='#000'/><path d='{body}' fill='#fff' transform='translate(2.4 2.9) scale(.92)'/><path d='{ureter}' fill='none' stroke='#000' stroke-width='6' stroke-linecap='round'/><path d='{ureter}' fill='none' stroke='#fff' stroke-width='2' stroke-linecap='round'/></svg>\n"""


def main():
    color_72 = render_72(color=True)
    color_18 = render_18(color=True)
    bw_72 = render_72(color=False, variant="a")
    bw_18 = render_18(color=False, variant="a")
    color_72.save(OUT / "kidney_color_72x72.png")
    color_18.save(OUT / "kidney_color_18x18.png")
    bw_72.save(OUT / "kidney_bw_72x72.png")
    bw_18.save(OUT / "kidney_bw_18x18.png")
    render_72(color=False, variant="b").save(REFERENCE / "kidney_bw_variant_b_72x72_REFERENCE_ONLY.png")
    render_18(color=False, variant="b").save(REFERENCE / "kidney_bw_variant_b_18x18_REFERENCE_ONLY.png")
    (OUT / "kidney_color.svg").write_text(svg(color=True), encoding="utf-8")
    (OUT / "kidney_bw.svg").write_text(svg(color=False, variant="a"), encoding="utf-8")
    (REFERENCE / "kidney_bw_variant_b_REFERENCE_ONLY.svg").write_text(svg(color=False, variant="b"), encoding="utf-8")
    print("built kidney v2.1.0 artwork")


if __name__ == "__main__":
    main()
