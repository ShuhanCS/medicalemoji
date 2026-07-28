# Kidney v2.7.0 Proposal Validation

Validation date: 2026-07-28

Status: **PASS**

## PDF

- Seven letter-size pages (612 x 792 points), reduced from nine pages in v2.6.0.
- All seven pages rendered to PNG and visually inspected.
- No clipped headings, overlapping text, broken tables, black squares, or unreadable proposal artwork or
  evidence.
- Page numbering runs from 1 of 7 through 7 of 7.
- The PDF contains 34 link annotations resolving to 23 unique HTTPS URLs; wrapping creates the duplicate
  annotations, and no local `file:` link is present.
- The PDF embeds nine images: four required proposal images on page 1 and five frequency exhibits on pages 3-5.

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
- The Unicode-facing Markdown text is substantively identical to v2.6.0 apart from synchronized packet paths.
- The Expected usage section does not contain the removed `does not guarantee future emoji use` or
  `unfiltered term also captures` disclaimer.
- The Open-ended answer uses four independent evidence filters and does not claim entitlement from other organs.
- Jarone Lee is absent.

## Assets

- All four proposal PNGs have the required exact dimensions.
- Both black-and-white PNGs use only black and white visible pixels.
- All artwork, both Trends exhibits, and Books Ngram are byte-identical to the corresponding v2.6.0 assets;
  only the packet filename prefix changed.
- Search and Video are top-edge crops of their v2.6.0 images. The retained pixels are identical, and the query,
  search type, Tools menu, visible count, and result context remain legible.
- Five required frequency exhibits are embedded. The attempted 2026-07-28 refresh was not substituted because
  Search/Video lacked a visible result count and Trends returned HTTP 429.

## Commands

```powershell
python -m py_compile scripts/make_submission_pdf.py
python scripts/make_submission_pdf.py submissions/v2.7.0/v2.7.0_kidney_emoji_proposal_SUBMIT.md
pdftoppm -png -r 130 submissions/v2.7.0/v2.7.0_kidney_emoji_proposal_SUBMIT.pdf tmp/pdfs/kidney-v2.7.0/page
```
