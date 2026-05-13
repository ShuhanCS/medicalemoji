# Evidence Capture Checklist

Last checked: 2026-05-13

Unicode requires frequency evidence screenshots. Capture these in a private/incognito browser session and save the screenshots under:

`docs/proposals/kidney-emoji-2026/evidence/`

Do not submit with placeholders. This file is a capture plan, not completed evidence.

## Required English Evidence

Use the same capture date for all screenshots when possible.

| Requirement | Query / URL | Capture Notes | Status |
| --- | --- | --- | --- |
| Google Search | https://www.google.com/search?q=kidney | Click Tools so the result count is visible on the right. | Todo |
| Google Video Search | https://www.google.com/search?tbm=vid&q=kidney | Capture result count. | Todo |
| Google Trends Web Search | https://trends.google.com/trends/explore?date=all&q=elephant,kidney | Use widest range; include elephant comparator. | Todo |
| Google Trends Image Search | https://trends.google.com/trends/explore?date=all_2008&gprop=images&q=elephant,kidney | Use Image Search; include elephant comparator. | Todo |
| Google Books Ngram | https://books.google.com/ngrams/graph?content=elephant%2Ckidney&year_start=1500&year_end=2019&corpus=en-2019&smoothing=3 | Include elephant comparator. | Todo |

## Clarifying Queries

The plain term `kidney` is likely clear enough, but the proposal may be stronger if supplemental queries show broad medical and non-medical usage. These are supplemental and should not replace the required plain-term evidence unless Unicode guidance or ESR feedback says otherwise.

| Use Case | Suggested Query | Why |
| --- | --- | --- |
| Organ/anatomy clarity | kidney organ | Reduces recipes/food ambiguity if needed. |
| Disease communication | kidney disease | Shows public health usage. |
| Donation/transplant | kidney transplant | Shows transplant/donation relevance. |
| Acute use case | kidney stone | Shows common patient-facing phrase. |
| Treatment context | dialysis | Useful as sequence/use-case support, not as the emoji name evidence. |

## Non-English Evidence Candidates

Unicode says to supply equivalent searches in appropriate languages when the proposed emoji has high usage in a broad region but relatively low English usage. If coordinating with the Turkish Society of Nephrology, capture Turkish evidence separately.

| Language | Term | Notes |
| --- | --- | --- |
| Turkish | bobrek | ASCII transliteration for `bobrek`; capture actual Turkish spelling in browser if possible. |
| Turkish | bobrek hastaligi | Kidney disease. |
| Turkish | bobrek nakli | Kidney transplant. |
| Spanish | rinon | ASCII transliteration for `rinon`; capture actual Spanish spelling in browser if possible. |
| Arabic | kidney Arabic term | Need native-speaker validation before use. |

Note: final proposal screenshots should preserve the correct native spelling and browser rendering. This checklist uses ASCII transliterations so the repo stays simple and portable.

## Evidence Rules To Respect

- Screenshots must be reproducible snapshots.
- Search result counts may change over time; record date, browser, region, and query.
- Use private/incognito browsing to reduce personalization.
- Do not include petitions or examples of people asking for the emoji.
- Do not count hashtags as evidence.
- Do not rely on social media posts as frequency evidence.

## Suggested File Naming

- `2026-05-xx-google-search-kidney.png`
- `2026-05-xx-google-video-kidney.png`
- `2026-05-xx-google-trends-web-elephant-kidney.png`
- `2026-05-xx-google-trends-image-elephant-kidney.png`
- `2026-05-xx-google-ngram-elephant-kidney.png`

## Submission Readiness Gate

The proposal is not ready until:

- All required frequency screenshots are captured.
- Each screenshot has a visible URL/query and date context.
- The proposal text cites the screenshot filename and source URL.
- Turkish Society/ISN coordination is resolved.
- Re-review eligibility is confirmed.
- Image rights are documented.
