# Microsoft brief — three added slides (2026-07-09)

Three slides appended to the *Emoji 2026 Brief* deck for a meeting with Microsoft's Global
Chief Medical Officer & VP of Healthcare. Built to match the deck's existing phone-frame
style (Century Gothic 30pt bold titles, `#484E56` ink, `#B7BDC6` frame).

| # | Slide | Purpose |
|---|-------|---------|
| 6 | The 2021 JAMA set | The 14 clinical concepts we proposed. All 14 declined. |
| 7 | Every resubmission reset the clock | Submission/decline timeline and 2026 re-eligibility. |
| 8 | Where emoji decisions get made | Unicode governance, where the emoji subcommittee sits, and Microsoft's standing. |

Slide 9 is the original "Request" slide, moved to the end so the governance infographic
lands immediately before the ask.

## Files

- `Emoji-2026-Brief-v2.pptx` — the full 9-slide deck
- `infographic-unicode-microsoft.png` — slide 8 exported at 3200×1800 for dropping into any deck
- `build_slides.py` — regenerates the three slides from the source deck
- `render-6.png`, `render-7.png`, `render-8.png` — 1600×900 proofs

Source deck: `C:\Users\Shuha\Downloads\Emoiji 2026 Brief.pptx` (not in this repo, too large).
`build_slides.py` is self-contained: run `python build_slides.py` and it pulls the phone-frame
chrome off the "Request" slide and the 14 emoji off "Our New Candidates", locating both by
title rather than by index. It prints a geometry QA pass (out-of-bounds and overlap checks)
on every run.

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
- Microsoft holds a Board of Directors seat: Vishal Chowdhary, VP of Science, Microsoft 365 Copilot — <https://unicode.org/consortium/directors.html>
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
