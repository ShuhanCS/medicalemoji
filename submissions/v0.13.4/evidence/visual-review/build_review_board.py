"""Regenerate the 18x18 visual review board for the SINGLE-kidney design.

Shows the proposed image at 72x72 and 18x18 (actual size + zoom), in color
and black-and-white, to evidence that the organ stays legible at emoji size.
Pulls the final art from the design folder.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ART = HERE.parents[3] / "docs" / "design" / "kidney-emoji-2026-06" / "final"
OUT = HERE / "v0.13.4_18x18_visual_review_board_SUBMIT.png"


def font(sz, bold=False):
    try:
        return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", sz)
    except OSError:
        return ImageFont.load_default()


def on_white(im):
    b = Image.new("RGBA", im.size, (255, 255, 255, 255))
    b.alpha_composite(im.convert("RGBA"))
    return b.convert("RGBA")


def main():
    c72 = Image.open(ART / "kidney_color_72x72.png").convert("RGBA")
    c18 = Image.open(ART / "kidney_color_18x18.png").convert("RGBA")
    b72 = Image.open(ART / "kidney_bw_72x72.png").convert("RGBA")
    b18 = Image.open(ART / "kidney_bw_18x18.png").convert("RGBA")

    W, H = 1120, 760
    bd = Image.new("RGBA", (W, H), (247, 247, 249, 255))
    d = ImageDraw.Draw(bd)
    ink, sub = (24, 24, 28), (108, 110, 118)
    d.text((44, 34), "Kidney emoji - 18x18 visual review", font=font(34, True), fill=ink)
    d.text((44, 84),
           "Proposed single-kidney image at 72x72 and 18x18, color and "
           "black-and-white. The 18px tiles are the legibility test.",
           font=font(18), fill=sub)

    def row(c, lab, y, dark=False):
        d.text((44, y - 30), lab, font=font(20, True), fill=ink)
        bd.alpha_composite(on_white(c[1]), (60, y))          # 72 white
        d.rectangle([60, y, 131, y + 71], outline=(218, 218, 224))
        d.text((60, y + 78), "72x72", font=font(13), fill=sub)
        if dark:
            chip = Image.new("RGBA", (72, 72), (43, 45, 52, 255))
            chip.alpha_composite(c[1])
            bd.alpha_composite(chip, (174, y))
            d.text((174, y + 78), "72x72 on dark", font=font(13), fill=sub)
        # 18 actual size
        bd.alpha_composite(on_white(c[0]), (330, y + 27))
        d.rectangle([330, y + 27, 347, y + 44], outline=(218, 218, 224))
        d.text((330, y + 78), "18x18 actual", font=font(13), fill=sub)
        # 18 zoom 12x
        z = c[0].resize((216, 216), Image.NEAREST)
        bd.alpha_composite(on_white(z), (430, y - 72))
        d.rectangle([430, y - 72, 646, y + 144], outline=(218, 218, 224))
        d.text((430, y + 150), "18x18 at 12x zoom", font=font(13), fill=sub)

    row((c18, c72), "Color", 200, dark=True)
    row((b18, b72), "Black-and-white", 480)

    d.line([0, 690, W, 690], fill=(228, 228, 233), width=1)
    d.text((44, 706),
           "At 18x18 the single kidney holds a bold organ silhouette with the "
           "hilum notch and the vessel and ureter cues, so it reads as a kidney "
           "rather than a food bean.", font=font(15), fill=sub)
    bd.convert("RGB").save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
