# Microsoft brief — three added slides (2026-07-09)

Three slides appended to the *Emoji 2026 Brief* deck for a meeting with Microsoft's Global
Chief Medical Officer & VP of Healthcare. Built to match the deck's existing phone-frame
style (Century Gothic 30pt bold titles, `#484E56` ink, `#B7BDC6` frame).

## Current deck — `Emoji-2026-Brief-v3.pptx` (8 slides)

| # | Slide | Purpose |
|---|-------|---------|
| 6 | Every resubmission reset the clock | Submission/decline timeline and 2026 re-eligibility. |
| 7 | Inside the Unicode Consortium | Org chart: where Microsoft sits, and where emoji sits. |
| 8 | Request | The ask (original slide, moved to the end). |

Slides 1–5 are Shuhan's originals. He dropped the "2021 JAMA set" slide from v2 and renamed
the timeline's middle column from "On a knife edge" to "Unclear".

The org chart shows the Board of Directors and the four committees as **peers** under the
Consortium. `consort.html` describes the committees but never says the Board governs them,
so no reporting line is drawn between them. What the sources do establish precisely is that
the five working groups — including Emoji Standard & Research — hang off the **UTC**, which
is where the vote lives. That subtree is drawn in blue for exactly that reason.

## Files

- `Emoji-2026-Brief-v3.pptx` — the current 8-slide deck
- `infographic-unicode-orgchart.png` — slide 7 at 3200×1800, for dropping into any deck
- `deck_kit.py` — shared chrome/card/text helpers and the geometry QA pass
- `build_orgchart.py` — rebuilds slide 7 from the v2 deck; touches no other slide
- `orgchart.png` — 1600×900 proof of slide 7
- `Emoji-2026-Brief-v2.pptx` — Shuhan's edited 9→8 slide deck, the input to the org chart
- `build_slides.py` — **frozen**; produced the original v2 slides. Predates `deck_kit.py`.
- `infographic-unicode-microsoft.png`, `render-6/7/8.png` — v2-era proofs

Source deck: `C:\Users\Shuha\Downloads\Emoiji 2026 Brief.pptx` (not in this repo, too large).
The scripts locate slides by title rather than by index, and print a geometry QA pass
(out-of-bounds and overlap checks) on every run.

**Gotcha:** add a new slide *before* dropping one. A part created after a drop reuses the
freed partname (`slide8.xml`) and silently overwrites the Request slide.

## The finding that matters

**Kidney, stomach, and liver are probably not eligible for the 2026-07-31 deadline.**

Unicode's rule is four years, not two, and it runs from the *decline*:

> "Emoji declined within the last four years are not eligible for re-review."
> — <https://unicode.org/emoji/proposals.html>

> "Emoji that have been declined are not eligible to be re-submitted for four (4) years."
> — Status Key, <https://unicode.org/emoji/emoji-proposals-status.html>

The public status sheet publishes the **submission** date, not the decline date. Three
independent confirmations:

1. Blood drop is document [L2/18-092](https://www.unicode.org/L2/L2018/18092-blood-drop-emoji.pdf),
   submitted 2018 and approved Feb 2019 for Emoji 12.0. The sheet lists `4/3/2018`.
2. Charlotte Buff, Unicode contributor: *"The 'Date' column appears to show proposal
   submission dates based on document IDs."*
3. Our rows cluster on window boundaries: spine/intestines/ECG are `4/4/2024` and
   `4/5/2024`, two days after the 2024 window opened on April 2. Kidney/stomach/liver are
   `7/19`, `7/28`, `7/30` of 2022 — the final days before the July 31, 2022 close.
   Declines would not cluster that way.

Kidney, stomach and liver were therefore submitted in July 2022 and **declined around
November 2022** (the ESC report for UTC #173 is dated 2022-10-31; submitters are notified
at cycle end). Four years from that decline lands ~November 2026, after the 2026 window
shuts. Counted from submission instead, they clear by 12, 3 and 1 day respectively.

Either reading puts them on a knife edge. Confirm with Unicode before filing
`submissions/v1.1.0/v1.1.0_kidney_emoji_proposal_SUBMIT.md`.

### 2026-07-31 eligibility

| Status | Concepts |
|--------|----------|
| Clear to file now | white blood cell, pill pack, pill box, blood bag, leg cast, IV bag, CT scan, weight scale |
| Knife edge | kidney, stomach, liver |
| Barred (~Nov 2028) | spine, intestines, ECG |

## Fact-check notes

Verified against primary sources and safe to present:

- UTC voting: Full member = 1 vote, Supporting = ½, all other tiers none — <https://www.unicode.org/consortium/utc.html>
- Microsoft holds a Board of Directors seat: "Vishal Chowdhary, 2026 to present … Vice President
  of Science at Microsoft where he leads Office AI Science team in Microsoft 365 Copilot" — verified
  2026-07-09 at <https://unicode.org/consortium/directors.html>
- The five UTC working groups: Emoji Standard & Research, Script Encoding, CJK & Unihan,
  Properties & Algorithms, Editorial — <https://www.unicode.org/consortium/utc.html>
- The Consortium has "three technical committees and the editorial committee" (UTC, CLDR TC,
  ICU TC, Editorial Committee) — <https://www.unicode.org/consortium/consort.html>. That page
  does **not** state a Board→committee reporting line; don't draw one.
- The emoji body is now the **Emoji Standard & Research Working Group**, formerly the Emoji
  Subcommittee (ESC). It recommends; the UTC votes. It has no final encoding authority.
- 2026 window: opened April 2, closes July 31; submitters notified by November 30 — <https://unicode.org/emoji/proposals.html>
- Heart and lungs shipped in **Emoji 13.0 (2020)**. The website's "Unicode 14.0 in 2021"
  (`src/app/page.tsx`, `src/components/Timeline.tsx`) contradicts the memos and is wrong.

Deliberately **not** on the slides, because they could not be confirmed from a primary source:

- The exact Full Member roster and count (Wikipedia says six; that conflicts with Google,
  Adobe and Airbnb holding board seats).
- Membership fee figures.
- Any named Microsoft representative on the UTC or the emoji working group. The deck says
  Microsoft votes in the UTC — which follows from Full membership — and does not claim a
  Microsoft seat on the emoji working group.
- Whether the JAMA figure depicted all 14 concepts. Shuhan (an author) confirmed the set.
