"""Add a slide on organizational precedent: whole emoji sets get through when a member
company carries them. Inserted ahead of the Request slide; touches nothing else.
"""
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from deck_kit import BLUE, GREEN, HEAD, INK, LIGHT, MID, SLATE, WHITE, Deck, lines, run

SRC = "Emoji-2026-Brief-v3.pptx"
OUT = "Emoji-2026-Brief-v4.pptx"
TITLE = "Whole sets get through"
S = "sets"

deck = Deck(SRC)
s = deck.base(TITLE, S)
deck.move_slide(s, 7)  # 0-indexed: becomes slide 8, ahead of "Request"

tf = deck.txbox(s, S, "sub", 0.62, 1.06, 8.66, 0.30)
p = tf.paragraphs[0]
run(p, "When a member company carries them. ", size=10.5, color=SLATE)
run(p, "Apple did exactly this for accessibility in 2018.", size=10.5, bold=True, color=INK)

# ---------------------------------------------------------------- left: the anchor case
LX, LY, LW, LH = 0.62, 1.44, 4.70, 2.70
deck.card(s, S, "cardApple", LX, LY, LW, LH, fill=WHITE, line=GREEN, width_pt=1.75)
deck.topbar(s, LX, LY, LW, GREEN)

htf = deck.txbox(s, S, "ah", LX + 0.18, LY + 0.20, LW - 0.36, 0.26)
run(htf.paragraphs[0], "Apple's accessibility set", font=HEAD, size=12.5, bold=True, color=GREEN)

mtf = deck.txbox(s, S, "am", LX + 0.18, LY + 0.50, LW - 0.36, 0.20)
run(mtf.paragraphs[0], "L2/18-080  ·  Submitter: Apple Inc.  ·  March 2018", size=8, color=SLATE)

BULLETS = [
    ("One curated set", " across four categories, built with the American Council of the Blind, "
                        "the Cerebral Palsy Foundation and the National Association of the Deaf."),
    ("Nine concepts shipped", " in Emoji 12.0 (2019): guide dog, service dog, probing cane, "
                              "both wheelchairs, ear with hearing aid, deaf person, mechanical arm and leg."),
]
by = LY + 0.80
for i, (bold, rest) in enumerate(BULLETS):
    btf = deck.txbox(s, S, f"ab{i}", LX + 0.20, by, LW - 0.40, 0.52)
    bp = btf.paragraphs[0]
    run(bp, "—  ", size=9, color=GREEN)
    run(bp, bold, size=9, bold=True, color=INK)
    run(bp, rest, size=9, color=SLATE)
    by += 0.58

# Apple's own disclaimer -- the move that disarmed the "open-ended" exclusion factor
QY = LY + 1.98
deck.card(s, S, "cardQuote", LX + 0.18, QY, LW - 0.36, 0.56, fill=LIGHT, line=LIGHT)
qtf = deck.txbox(s, S, "aq", LX + 0.30, QY + 0.08, LW - 0.60, 0.40)
qp = qtf.paragraphs[0]
run(qp, "“This is not meant to be a comprehensive list of all possible depictions of "
        "disabilities, but to provide an initial starting point.”", size=8, italic=True, color=INK)

# ---------------------------------------------------------------- right: other precedents
RX, RW, RH, RGAP = 5.48, 3.90, 0.82, 0.12
OTHERS = [
    ("Plan International UK + NHS Blood and Transplant",
     "Drop of blood, Emoji 12.0 (2019). Their narrower\n“period pants” proposal was declined first."),
    ("Tinder + Emojination",
     "71 holding-hands combinations, Emoji 12.1 (2019).\nEmojination's founder later vice-chaired the subcommittee."),
    ("Google",
     "Gender-inclusive designs across ~53 human emoji.\nL2/19-078 (2019)."),
]
ry = LY
for i, (who, what) in enumerate(OTHERS):
    deck.card(s, S, f"cardO{i}", RX, ry, RW, RH, fill=WHITE, line=MID)
    wtf = deck.txbox(s, S, f"ow{i}", RX + 0.16, ry + 0.13, RW - 0.32, 0.20)
    run(wtf.paragraphs[0], who, font=HEAD, size=8.5, bold=True, color=INK)
    dtf = deck.txbox(s, S, f"od{i}", RX + 0.16, ry + 0.37, RW - 0.32, 0.36)
    lines(dtf, what, size=7.8, color=SLATE)
    ry += RH + RGAP

# ---------------------------------------------------------------- callout
CO_Y, CO_H = 4.24, 0.74
deck.card(s, S, "cardCallout", 0.62, CO_Y, 8.76, CO_H, fill=WHITE, line=BLUE, width_pt=1.75)
t1 = deck.txbox(s, S, "co1", 0.82, CO_Y + 0.12, 8.36, 0.24)
run(t1.paragraphs[0], "Unicode declines taxonomies, not sets.", font=HEAD, size=11, bold=True, color=BLUE)
t2 = deck.txbox(s, S, "co2", 0.82, CO_Y + 0.40, 8.36, 0.28)
p2 = t2.paragraphs[0]
run(p2, "“The goal is iconic representation of large categories, not completeness in the sense of filling out "
        "the categories of a scientific or taxonomic classification system.”  ", size=8, italic=True, color=SLATE)
run(p2, "Fourteen organs read as a taxonomy. A curated set, carried by a member, reads as Apple 2018.",
    size=8, color=INK)

deck.sources(s, S, "unicode.org/L2/L2018/18080-accessibility-emoji.pdf  ·  unicode.org/emoji/proposals.html")

deck.save(OUT)
print(f"saved {OUT} | slides: {len(deck.slides)}")
print("\n--- geometry QA ---")
deck.qa(containers=("card",))
