# Kidney v2.10.0 Proposal Validation

Validation date: 2026-07-28

Status: **PASS**

## PDF

- Eight letter-size pages (612 x 792 points).
- All eight pages rendered to PNG and visually inspected.
- No clipped headings, overlapping text, broken tables, black squares, malformed proposal artwork, or
  unreadable evidence.
- Page numbering runs from 1 of 8 through 8 of 8.
- The PDF contains 35 link annotations resolving to 25 unique HTTPS URLs; wrapping creates duplicate
  annotations, and no local `file:` link is present.
- The PDF embeds eleven unique images: four required proposal images and seven frequency screenshots covering
  five methods.
- SHA-256: `6f5d5e4d9f703d912b4ea29b86002b2c01b66ade55ab777a2ac358a2865fc145`.

## First-page requirements

- Title, exact ten-person submitter order, main point of contact, and date are present.
- Suggested name, five suggested keywords, category, and sort location are present.
- The five keywords are `renal`, `dialysis`, `transplant`, `donation`, and `stone`.
- 18x18 and 72x72 color and black-and-white examples are present.
- The 18x18 examples visibly show two kidney bodies, inward-facing notches, a central connector, and short
  ureter cues at their rendered size.
- Image ownership, CC0 dedication, and Unicode agreement language are present.

## Structure and content

- All seven inclusion factors are present in order.
- All five exclusion factors are present in order.
- Other Information is present.
- Compatibility remains `Not applicable`; no unsupported popular-system or high-frequency-use claim appears.
- Expected usage states accurately that all five required methods compare Kidney with Elephant.
- Search and Video identify raw result totals as volatile approximate index estimates used only for the form's
  requested relative comparison.
- The Open-ended answer uses four independent evidence filters and does not claim entitlement from other organs.
- Jarone Lee is absent.

## Frequency evidence

- Google Search: Kidney approximately 211,000,000; Elephant approximately 487,000,000.
- Google Video Search: Kidney approximately 53,600,000; Elephant approximately 85,900,000.
- All four Search and Video screenshots were captured 2026-07-28 in one signed-out Firefox Private Browsing
  session with exact terms and matched settings.
- All four screenshots visibly show the query, search mode, Tools menu, approximate count, signed-out state,
  and result context.
- Google Trends Web Search, Google Trends Image Search, and Google Books Ngram display Kidney and Elephant in
  the same exhibit.
- CAPTCHA, count-free, blocked, and rate-limit layouts are absent.

## Assets

- All four proposal PNGs have the required exact dimensions.
- Both black-and-white PNGs use only black and white visible pixels.
- The new 18x18 assets are hand-authored on a native 18-pixel grid with fully opaque foreground, transparent
  margin, and no fractional alpha.
- Both 18x18 SVG sources declare an 18x18 canvas and crisp-edge rendering.
- The 72x72 PNGs, master PNGs, 72x72 source SVGs, and all seven frequency exhibits are byte-identical to v2.9.0.

## Commands

```powershell
python -m py_compile scripts/build_kidney_v210_18px.py scripts/make_submission_pdf.py
python scripts/build_kidney_v210_18px.py submissions/v2.10.0/images --prefix v2.10.0
python scripts/make_submission_pdf.py submissions/v2.10.0/v2.10.0_kidney_emoji_proposal_SUBMIT.md
pdftoppm -png -r 130 submissions/v2.10.0/v2.10.0_kidney_emoji_proposal_SUBMIT.pdf tmp/kidney-v2.10-pdf/page
npm run lint
```
