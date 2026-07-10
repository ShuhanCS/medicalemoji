# What to file in the 2026 window, and how to pitch it

## The reframe

Not *"help us relitigate the kidney."*

**"Help us land the first medical emoji that Microsoft commits to ship."**

The kidney is a twice-declined concept with a contested eligibility date, artwork that would be
auto-rejected, and a 5% base rate. A never-proposed concept carries no bar, no history, three times the
odds, and needs no answer from Unicode before the deadline. Pair it with a vendor commitment, which answers
one of Unicode's two named decline reasons and which **no proposal in the corpus has ever carried**, and the
eligibility argument stops mattering.

## Why not the kidney, in numbers

| | Advance rate |
|---|---|
| First-time proposals | 273 / 1671 = **16%** |
| Resubmissions | 7 / 129 = **5%** |
| Resubmissions filed inside the bar | 3 / 53 = 6% |

Reproduce with `python evidence/resubmission_analysis.py`.

Add to that: the four-year clock is unresolved (it leans toward the submission date and is not established,
and the bar is not enforced mechanically); five of our fourteen were re-filed *while barred*; the existing
kidney artwork carries no licence; and the screening gate is a working group we have no seat in.

Even in the best case the kidney is a one-in-twenty play, in twenty-two days.

## Concepts that have never been proposed

Checked against all 1,800 rows of Unicode's public status sheet on 2026-07-09.

| Concept | Status in the sheet | Bar |
|---|---|---|
| Hospital bed | never proposed | none |
| Insulin pen | never proposed | none |
| Glucose meter | never proposed | none |
| Nebulizer | never proposed | none |
| Oxygen mask | never proposed | none |
| Walker | never proposed | none |
| Ice pack | never proposed | none |
| Ventilator | never proposed | none |
| Blood pressure cuff | `Blood Pressure`, **Expired**, 2017-09-21 | none. The bar applies to *declined* emoji |
| Inhaler | `Inhaler`, Declined, 2018-07-03 | lapsed. But it is a resubmission, so 5% |
| Defibrillator | Declined, 2024-04-02 | barred until ~2028 |

**Caveat.** The status page states *"Auto-declined proposals are not included in this list."* Absence from
the sheet is therefore not proof a concept was never submitted, only that it was never formally reviewed and
declined. It is still the best available signal.

## Judging them against the factors that actually decide

The existing `medical` subgroup holds syringe, pill, drop of blood, adhesive bandage, stethoscope, x-ray and
crutch. The encoded organs are brain, anatomical heart and lungs. `Breaks new ground` is measured against
those, using Unicode's own test: *"because there is already an emoji for 🧹 broom, an emoji for vacuum
cleaner would not break new ground."*

| Concept | Nearest existing emoji | Breaks new ground? | Reads at 18×18? | Call |
|---|---|---|---|---|
| **Hospital bed** | 🏥 hospital (a building) | Yes. A bed is not a building | Yes, distinctive silhouette | **Lead candidate** |
| **Blood pressure cuff** | 🩺 stethoscope | Yes. Measurement, not auscultation | Cuff and gauge, plausible | **Strong**, and never declined |
| Ice pack | 🩹 adhesive bandage | Yes. Everyday injury, sport, swelling | Weak. A blue rectangle | Medium |
| Glucose meter | none | Yes | Small screen, risky at 18×18 | Medium |
| Ventilator | none | Yes | Hard to render; also risks `Transient`, tied to one pandemic | Medium |
| Insulin pen | 💉 syringe | **Risky.** Reads as a syringe variant | Yes | Weak |
| Walker | 🩼 crutch | **Risky.** Reads as a mobility-aid variant | Yes | Weak |
| Nebulizer | none | Yes, but low usage | Poor | Weak |
| Oxygen mask | 😷 face with medical mask | Risky | Medium | Weak |

**Recommendation: hospital bed, or blood pressure cuff.** Both break new ground against everything encoded,
both are high-frequency everyday terms rather than clinical jargon, and neither is a variant of an existing
glyph. The blood pressure cuff has the additional advantage that its only prior appearance is `Expired`,
not `Declined`, so no bar can be argued at all.

**File one.** Filing several is itself the answer to the `Open-ended` exclusion factor, and the answer is yes.

## What still has to be true before filing

None of this is optional, and none of it is written yet.

1. **Frequency evidence**, captured properly: five mandated Google sources, screenshots, `elephant` in the
   Trends and Ngram charts, hyphenated multiword terms, a private browser window, a qualifying Trends
   category, and a stated capture month. See [`../proposals/TEMPLATE-emoji-proposal.md`](../proposals/TEMPLATE-emoji-proposal.md).
   **Run the searches before committing to a concept.** If `[hospital-bed]` cannot beat `elephant` anywhere,
   pick another.
2. **Artwork**, originated by Microsoft design: 18×18 and 72×72, colour and black and white, no grayscale,
   and **no text, digits or barcodes**, which is an automatic decline.
3. **The licence sentence**, true and on the page.
4. **The vendor commitment** from Microsoft, in `Other information`.
5. **The Open-ended answer**, drafted first, naming the neighbours we will not come back for.

## The pitch to Rhew

Three sentences, in this order.

> Unicode declines a well-formed proposal for two reasons: weak popularity evidence, and *"lack of
> anticipated support by major vendors."* Microsoft ships Segoe UI Emoji on every Windows device, and no
> emoji proposal in Unicode's history has ever carried a vendor commitment. We would like Microsoft to write
> the first one.

Then the two asks that cost nothing: who is Microsoft's UTC delegate, and does Microsoft have anyone on the
Emoji Standard and Research Working Group, which screens every proposal and is where all fourteen of ours
were declined without record.

The Health category document waits. It cannot approve an emoji.
