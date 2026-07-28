# Kidney v2.6.0 Proposal Validation

Validation date: 2026-07-28

Status: **PASS**

## PDF

- Nine letter-size pages (612 x 792 points).
- All nine pages rendered to PNG and were visually inspected at original resolution.
- No clipped headings, overlapping text, broken tables, black squares, or unreadable proposal artwork.
- Page numbering runs from 1 of 9 through 9 of 9.
- The PDF contains 34 link annotations resolving to 23 unique HTTPS URLs; wrapping creates the duplicate
  annotations, and no local `file:` link is present.
- The PDF embeds nine images: four required proposal images on page 1 and five frequency exhibits on pages 4-7.

## First-page requirements

- Title, exact ten-person submitter order, main point of contact, and date are present.
- Suggested name, non-repeating keywords, category, and sort location are present.
- 18x18 and 72x72 color and black-and-white examples are present.
- Image ownership, CC0 dedication, and Unicode agreement language are present.

## Structure and content

- All seven inclusion factors are present in order.
- All five exclusion factors are present in order.
- Other Information is present.
- Compatibility remains `Not applicable`; no unsupported popular-system or high-frequency-use claim appears.
- The Expected usage section does not contain the removed `does not guarantee future emoji use` or
  `unfiltered term also captures` disclaimer.
- The Open-ended answer uses four independent evidence filters and does not claim entitlement from other organs.
- Jarone Lee is absent.

## Assets

- All four proposal PNGs have the required exact dimensions.
- Both black-and-white PNGs use only black and white visible pixels.
- All artwork and retained frequency files are byte-identical to the corresponding v2.5.0 assets; only the packet
  filename prefix changed.
- Five required frequency exhibits are embedded. The attempted 2026-07-28 refresh was not substituted because
  Search/Video lacked a visible result count and Trends returned HTTP 429.

## Commands

```powershell
python -m py_compile scripts/make_submission_pdf.py
python scripts/make_submission_pdf.py submissions/v2.6.0/v2.6.0_kidney_emoji_proposal_SUBMIT.md
pdftoppm -png -r 110 submissions/v2.6.0/v2.6.0_kidney_emoji_proposal_SUBMIT.pdf tmp/pdfs/kidney-v2.6.0/page
```
