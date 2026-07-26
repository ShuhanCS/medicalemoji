# Stomach v1.12 Candidate PDF QA

Review date: 2026-07-26

PDF: `stomach_emoji_proposal_CANDIDATE.pdf`

SHA-256: `01821a1eec18b294fd7fa1cc3e24eeba154f9694d1f4b754723ddbe7de20e18f`

Status: **PASS AS CANDIDATE**

## Technical inspection

| Check | Result |
| --- | --- |
| Document title | `Proposal for Emoji: Stomach` |
| Pages | 7 |
| Page size | US Letter, 612x792 points |
| Encryption | None |
| File size | 523,239 bytes |
| Text extraction | Pass; 7,725 extracted characters |
| Blank text pages | None |
| Link annotations | 11 |
| Fonts | Arial, Arial Bold, and Consolas embedded, subset, and Unicode-enabled |
| Embedded image counts by page | 4, 0, 2, 1, 1, 1, 0 |
| Broken local images | None |
| TODO, placeholder, or draft markers | None in reviewer-facing content |

## Page-by-page visual inspection

| Page | Content | Result |
| ---: | --- | --- |
| 1 | Three submitters, contact, category, four required images, design guidance, and rights | Pass. All required fields are easy to find; 18x18 and 72x72 samples render cleanly. |
| 2 | Multiple meanings, sequences, Breaks new ground, and Distinctiveness | Pass. Clear hierarchy, readable citations, no clipping or stranded heading. |
| 3 | Expected usage, current Google Search, and current Google Video Search | Pass. Each screenshot is tightly cropped to its query, active source, visible count, and representative result. |
| 4 | Current Trends Web Search | Pass. Terms, Worldwide setting, full range, mode, and complete graph are readable. |
| 5 | Current Trends Image Search | Pass. Terms, Worldwide setting, full range, mode, and complete graph are readable. |
| 6 | Current Ngram, Completeness, Compatibility, and Already represented | Pass. Query settings and graph are readable; no clipping or overlap. |
| 7 | Remaining exclusion factors and vendor guidance | Pass. The document closes cleanly with no clipping, stranded heading, or blank page. |

## Final-promotion condition

This QA record applies only to the candidate hash above. All five frequency exhibits are current and pass PDF
inspection. After the human-recognition gate passes, record the aggregate result, rebuild the final packet,
and repeat technical and page-by-page visual inspection. Do not reuse this result for a PDF with a different
hash.
