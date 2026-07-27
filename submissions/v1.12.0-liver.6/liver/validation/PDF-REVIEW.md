# Liver PDF Review

Review record version: 1.1.0

Reviewed: 2026-07-26

Artifact: `liver_emoji_proposal_SUBMIT.pdf`

SHA-256: `dd7b9810b204112de662240fb87d92a3d7683eb0f42f7590cc58a2268a55ed49`

Size: 1,482,030 bytes

## Technical result

- Pages: 9, US Letter, no rotation.
- Tagged: yes.
- Encrypted: no.
- Extractable text: 6,203 characters.
- Fonts: embedded subset Arial, Arial Bold, and Consolas; Unicode mapping present.
- Clickable external links: 11. The exact CC0, institutional, Unicode, Google Search, Google Video, Worldwide
  Trends Web, Worldwide Trends Image, Ngram, and official-guidance targets are present.
- Required names appear once in the extracted page-one byline: Shuhan He, MD; David Rhew, MD; Heena Purohit;
  Adrienne Balk.
- David Rhew's and Heena Purohit's Microsoft affiliations are present.
- The PDF contains `Breaks new ground`, the direct `Yes.`, both ordinary message examples, and three concise
  `Not applicable` answers.
- The PDF contains no `Stomach`, `Kidney`, `TODO`, `BLOCKED`, or `DRAFT` text.

## Visual inspection

All nine pages were rendered at 120 DPI under `tmp/pdfs/liver-v1.12.0-liver.6-review-3` and inspected in full.

| Page | Result |
| ---: | --- |
| 1 | Pass. Four-author metadata, both Microsoft affiliations, all four required images, plain-language design description, rights statement, and license link are clear and inside margins. |
| 2 | Pass. Multiple meanings, two ordinary sequences, `Breaks new ground = Yes`, and both descriptive links are unclipped and easy to scan. |
| 3 | Pass. The actual-size comparison board is legible; Expected usage distinguishes search/word frequency from emoji demand. |
| 4 | Pass. Google Search settings and displayed result count remain readable at normal zoom. |
| 5 | Pass. Google Video Search settings and displayed result count remain readable at normal zoom. |
| 6 | Pass. Worldwide, 2004-present, Web Search settings and comparison graph are visible. |
| 7 | Pass. Worldwide, 2008-present, Image Search settings and comparison graph are visible. |
| 8 | Pass. The Ngram heading, complete capture sentence, descriptive link, full graph, Completeness, Compatibility, and the opening exclusion factors are all visible and unclipped. |
| 9 | Pass. Open-ended, Transient, Faulty comparison, compact Other Information, and the guidance link fit cleanly with no stranded heading. |

## Decision

**PASS.** The PDF has no broken image, clipping, overlap, unreadable required exhibit, empty page, split label,
raw-URL overflow, stale date, or contradictory internal status. Removing the forced post-Ngram page break reduced
the document from ten pages to nine without shrinking an evidence figure.
