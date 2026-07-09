"""Add a case-study slide on how Apple's L2/18-080 was actually argued.

Every quote is verbatim from https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf
Inserted ahead of the Request slide; touches nothing else.
"""
from pptx.enum.text import PP_ALIGN

from deck_kit import AMBER, BLUE, GREEN, HEAD, INK, LIGHT, MID, SLATE, WHITE, Deck, run

SRC = "Emoji-2026-Brief-v4.pptx"
OUT = "Emoji-2026-Brief-v5.pptx"
TITLE = "How Apple did it"
S = "apple"

deck = Deck(SRC)
s = deck.base(TITLE, S)
deck.move_slide(s, 8)  # 0-indexed: becomes slide 9, ahead of "Request"

tf = deck.txbox(s, S, "sub", 0.62, 1.04, 8.66, 0.30)
p = tf.paragraphs[0]
run(p, "L2/18-080 answered Unicode's selection factors one by one, under a heading titled ", size=10.5, color=SLATE)
run(p, "“Counterarguments to Factors for Exclusion.”", size=10.5, bold=True, color=INK)

# ---------------------------------------------------------------- factor rows
ROWS = [
    ("Frequency", None,
     "“the most compelling factor for this proposal is not frequency of use of each character, "
     "but the desire to be inclusive in representation.”",
     "Then filed the Google Trends data anyway, reproducibly: “each data item was obtained using a new private browser window.”"),
    ("Breaking new\nground", None,
     "“Other than the wheelchair symbol, there are currently no emoji that can be used to depict "
     "various forms of disability.”",
     None),
    ("Image\ndistinctiveness", None,
     "“the image of a hearing aid would not be sufficiently distinctive at emoji scale; it needs to be "
     "shown with an ear in order to establish its identity.”",
     "Argued manual and motorized wheelchairs must be separate characters, not one."),
    ("Open-ended", AMBER,
     "“we don't expect such discussion to lead to proposals for a large number of additions beyond "
     "the current proposal.”",
     "The exclusion factor that a fourteen-organ set trips. Apple answered it before it was asked."),
    # Not a Unicode selection factor -- labelled "Partners" so the column doesn't imply it is.
    ("Partners", None,
     "“Developed in collaboration with … American Council of the Blind, the Cerebral Palsy Foundation "
     "and the National Association of the Deaf.”",
     None),
]

RY, RH = 1.60, 0.50
LABX, LABW = 0.62, 1.86
QX = 2.60
QW = 6.78

for i, (label, accent, quote, gloss) in enumerate(ROWS):
    y = RY + i * RH
    if accent:
        deck.card(s, S, f"cardRow{i}", 0.56, y - 0.02, 8.88, RH - 0.02, fill=LIGHT, line=LIGHT, radius=0.04)
    else:
        deck.rule(s, LABX, y - 0.02, 8.76, 0.008, color=MID)

    ltf = deck.txbox(s, S, f"lab{i}", LABX, y + 0.09, LABW, 0.32)
    for j, line in enumerate(label.split("\n")):
        para = ltf.paragraphs[0] if j == 0 else ltf.add_paragraph()
        run(para, line, font=HEAD, size=9, bold=True, color=accent or INK)

    qtf = deck.txbox(s, S, f"q{i}", QX, y + 0.05, QW, 0.27)
    run(qtf.paragraphs[0], quote, size=7.6, italic=True, color=INK)
    if gloss:
        gtf = deck.txbox(s, S, f"g{i}", QX, y + 0.32, QW, 0.15)
        run(gtf.paragraphs[0], gloss, size=7.2, color=SLATE)

# ---------------------------------------------------------------- callout
CO_Y, CO_H = 4.26, 0.70
deck.card(s, S, "cardCallout", 0.62, CO_Y, 8.76, CO_H, fill=WHITE, line=BLUE, width_pt=1.75)
t1 = deck.txbox(s, S, "co1", 0.82, CO_Y + 0.11, 8.36, 0.24)
run(t1.paragraphs[0], "Apple argued Unicode's factors, in Unicode's order, in Unicode's words.",
    font=HEAD, size=11, bold=True, color=BLUE)
t2 = deck.txbox(s, S, "co2", 0.82, CO_Y + 0.38, 8.36, 0.24)
p2 = t2.paragraphs[0]
run(p2, "Our packets led with medical importance and supporter credibility. ", size=7.8, color=INK)
run(p2, "Unicode lists neither as a selection factor. Nine of Apple's concepts shipped in Emoji 12.0 (2019).",
    size=7.8, color=SLATE)

deck.sources(s, S, "All quotes verbatim: unicode.org/L2/L2018/18080-accessibility-emoji.pdf  ·  factors: unicode.org/emoji/proposals.html")

deck.save(OUT)
print(f"saved {OUT} | slides: {len(deck.slides)}")
print("\n--- geometry QA ---")
deck.qa(containers=("card",))
