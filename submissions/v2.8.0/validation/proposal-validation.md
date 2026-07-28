# Kidney v2.8.0 Proposal Validation

Validation date: 2026-07-28

Status: **PASS**

## PDF

- Eight letter-size pages (612 x 792 points).
- All eight pages rendered to PNG and visually inspected.
- No clipped headings, overlapping text, broken tables, black squares, or unreadable proposal artwork or
  evidence.
- Page numbering runs from 1 of 8 through 8 of 8.
- The PDF contains 38 link annotations resolving to 25 unique HTTPS URLs; wrapping creates the duplicate
  annotations, and no local `file:` link is present.
- The PDF embeds eleven images: four required proposal images and seven frequency screenshots covering five
  methods.
- SHA-256: `3e1c6555cbab5874dd10b93979143f59e462242f5c4dd553a949d28964feb293`.

## First-page requirements

- Title, exact ten-person submitter order, main point of contact, and date are present.
- Suggested name, keywords, category, and sort location are present.
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

- Google Search: Kidney approximately 211,000,000; Elephant approximately 483,000,000.
- Google Video Search: Kidney approximately 66,000,000; Elephant approximately 85,300,000.
- Both Elephant screenshots visibly show the query, search mode, Tools menu, approximate count, and result
  context.
- Google Trends Web Search, Google Trends Image Search, and Google Books Ngram display Kidney and Elephant in
  the same exhibit.
- The CAPTCHA page and count-free result layouts are absent.

## Assets

- All four proposal PNGs have the required exact dimensions.
- Both black-and-white PNGs use only black and white visible pixels.
- Artwork, Kidney Search and Video, both Trends exhibits, and Books Ngram are byte-identical to the
  corresponding v2.7.0 assets; only the packet filename prefix changed.
- The two new Elephant screenshots are Google viewport crops captured in Firefox on 2026-07-28. Browser chrome
  and unused lower-page space were removed without altering the visible query, count, or result context.

## Commands

```powershell
python -m py_compile scripts/make_submission_pdf.py
python scripts/make_submission_pdf.py submissions/v2.8.0/v2.8.0_kidney_emoji_proposal_SUBMIT.md
pdftoppm -png -r 130 submissions/v2.8.0/v2.8.0_kidney_emoji_proposal_SUBMIT.pdf tmp/pdfs/kidney-v2.8.0/page
```
