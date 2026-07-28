# Kidney v2.9.0 Proposal Validation

Validation date: 2026-07-28

Status: **PASS**

## PDF

- Eight letter-size pages (612 x 792 points).
- All eight pages rendered to PNG and visually inspected.
- No clipped headings, overlapping text, broken tables, black squares, or unreadable proposal artwork or
  evidence.
- Page numbering runs from 1 of 8 through 8 of 8.
- The PDF contains 35 link annotations resolving to 25 unique HTTPS URLs; wrapping creates duplicate
  annotations, and no local `file:` link is present.
- The PDF embeds eleven unique images: four required proposal images and seven frequency screenshots covering
  five methods.
- SHA-256: `924f98e28bd4796aa69128b6b70767614b338b9923061fca37fa5120a4a51f84`.

## First-page requirements

- Title, exact ten-person submitter order, main point of contact, and date are present.
- Suggested name, five suggested keywords, category, and sort location are present.
- The five keywords are `renal`, `dialysis`, `transplant`, `donation`, and `stone`.
- 18x18 and 72x72 color and black-and-white examples are present.
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
- All ten artwork files and the three carried Trends/Ngram exhibits are byte-identical to the corresponding
  v2.8.0 assets; only the packet filename prefix changed.
- The four Search and Video exhibits are Google viewport crops from same-day Firefox source captures. Unused
  browser chrome and lower-page space were removed without altering the visible query, mode, count, or context.

## Commands

```powershell
python -m py_compile scripts/make_submission_pdf.py
python scripts/make_submission_pdf.py submissions/v2.9.0/v2.9.0_kidney_emoji_proposal_SUBMIT.md
pdftoppm -png -r 130 submissions/v2.9.0/v2.9.0_kidney_emoji_proposal_SUBMIT.pdf tmp/pdfs/kidney-v2.9.0/page
```
