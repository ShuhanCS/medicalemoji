# White Blood Cell Frequency Evidence Log

Capture dates: Search and Video 2026-07-27; Trends and Books 2026-07-26

All captures use the term `white blood cell`. Google Trends and Google Books use `elephant`, Unicode's required
comparison term. The proposal embeds the readable screenshots; the two Trends CSV files preserve the
underlying values exported by Google.

## Correction to the 2026-07-26 Search capture

The 2026-07-26 Google Search capture recorded **About 125 results** for `white-blood-cell`. That figure is
wrong. Re-measured on 2026-07-27 under the same documented settings, the query returns about 880,000,000
results, and `elephant` reproduces exactly at 491,000,000, which confirms the settings match.

The cause is not the hyphen grouping Unicode requires. `scripts/probe_google_hyphen_artifact.mjs` ran each
term in both the grouped and unhyphenated form and found no meaningful gap for any of them, including
`black-swan`, the example Unicode prints in its own instructions:

| Concept | grouped | plain |
| --- | --- | --- |
| white blood cell | 880,000,000 | 881,000,000 |
| black swan | 258,000,000 | 258,000,000 |
| first aid kit | 377,000,000 | 376,000,000 |
| elephant | 491,000,000 | 491,000,000 |

Google prints result totals as estimates and a single load will occasionally return a collapsed figure. The
2026-07-26 capture recorded one of those loads.

`scripts/recapture_google_search_evidence.mjs` now loads each query three times and refuses to write a
screenshot unless every reading lands in the same order of magnitude.

Raw data: `frequency/google_hyphen_artifact_probe.json`,
`frequency/white-blood-cell_google_recapture_log_2026-07-27.json`.

## Google Search

URL:

https://www.google.com/search?q=white-blood-cell&hl=en&num=10&pws=0

Settings: Firefox Private Browsing, English interface, personalized results disabled, 10 results per page,
Google.com default location with no region override.

Result: About 880,000,000 results, confirmed on three independent loads. Official-form nearest-million value:
880 million.

Comparator URL:

https://www.google.com/search?q=elephant&hl=en&num=10&pws=0

Comparator result: About 491,000,000 results, confirmed on three independent loads.

Files:

- `frequency/white-blood-cell_google_search_2026-07-27_SUBMIT.png`
- `frequency/white-blood-cell_google_search_elephant_2026-07-27_SUBMIT.png`

Superseded: `frequency/white-blood-cell_google_search_2026-07-26_SUBMIT.png` and its elephant comparator are
retained for the record and are not referenced by the proposal.

## Google Video Search

URL:

https://www.google.com/search?tbm=vid&q=white-blood-cell&hl=en&num=10&pws=0

Settings: Firefox Private Browsing, English interface, personalized results disabled, video results,
Google.com default location with no region override.

Result: About 13,900,000 results, confirmed on three independent loads. Official-form nearest-million value:
14 million.

Comparator URL:

https://www.google.com/search?tbm=vid&q=elephant&hl=en&num=10&pws=0

Comparator result: About 84,700,000 results, confirmed on three independent loads.

Files:

- `frequency/white-blood-cell_google_video_search_2026-07-27_SUBMIT.png`
- `frequency/white-blood-cell_google_video_search_elephant_2026-07-27_SUBMIT.png`

## Google Trends - Web Search

URL:

https://trends.google.com/trends/explore?date=all&q=elephant%2Cwhite%20blood%20cell

Settings: Worldwide, 2004-present, all categories, Web Search.

Result: Average indexed interest was 72 for `elephant` and 3 for `white blood cell`. The white-blood-cell
series is sustained across the full period and reaches 4 in each of 2024, 2025, and 2026.

Files:

- `frequency/white-blood-cell_google_trends_web_elephant_2026-07-26_SUBMIT.png`
- `frequency/white-blood-cell_google_trends_web_elephant_2026-07-26_DATA.csv`

## Google Trends - Image Search

URL:

https://trends.google.com/trends/explore?date=all_2008&gprop=images&q=elephant%2Cwhite%20blood%20cell

Settings: Worldwide, 2008-present, all categories, Image Search.

Result: Average indexed interest was 53 for `elephant` and 1 for `white blood cell`. The white-blood-cell
series records recurring image-search interest throughout the available period.

Files:

- `frequency/white-blood-cell_google_trends_image_elephant_2026-07-26_SUBMIT.png`
- `frequency/white-blood-cell_google_trends_image_elephant_2026-07-26_DATA.csv`

## Google Books Ngram Viewer

URL:

https://books.google.com/ngrams/graph?content=elephant%2Cwhite%20blood%20cell&year_start=1500&year_end=2022&corpus=en&smoothing=3

Data URL:

https://books.google.com/ngrams/json?content=elephant%2Cwhite%20blood%20cell&year_start=1500&year_end=2022&corpus=en&smoothing=3

Settings: English corpus, 1500-2022, case-insensitive, smoothing 3.

Result: In 2022, `white blood cell` measured 4.2974917136007207e-7 and `elephant` measured
4.241088959133776e-6, a ratio of approximately 0.1013. The white-blood-cell series rises through the modern
period and reaches its maximum in the final years of the chart.

File:

- `frequency/white-blood-cell_google_books_ngram_elephant_2026-07-26_SUBMIT.png`

## Interpretation

The five sources measure different behavior: indexed relative interest in Trends, phrase frequency in books,
and estimated result inventory in Search and Video. They are presented as complementary evidence of durable,
cross-format usage rather than as directly comparable absolute quantities.

They also do not all point the same way, and the proposal says so. Against `elephant`, the term is larger on
Google Search (about 1.8x), smaller on Google Video Search (about 0.17x), well below on both Trends
properties (3 against 72 on Web, 1 against 53 on Image), and about a tenth in Google Books for 2022.
