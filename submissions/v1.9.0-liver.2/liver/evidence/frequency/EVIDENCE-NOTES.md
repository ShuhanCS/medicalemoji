# Google Result-Stats Evidence Notes

Capture date: 2026-07-24

Google's current result pages expose the native result total in the `#result-stats` DOM element but collapse its
layout to zero pixels, so the text is not ordinarily rendered in the page view. The live values were:

| View | Exact query | Native `#result-stats` value |
| --- | --- | --- |
| Web | https://www.google.com/search?udm=14&q=liver&hl=en&num=10&pws=0 | `About 194,000 results (0.26s)` |
| Video | https://www.google.com/search?udm=7&q=liver&hl=en&num=10&pws=0 | `About 82,000,000 results (0.38s)` |

Each `RESULT_STATS_REVEALED.jpg` screenshot shows the contemporaneous Google page and a labeled overlay that
copies the exact value from the page's own `#result-stats` element. The overlay does not change the query,
result set, timing, or result-stat text. This is a disclosure mechanism for a value Google supplied but did not
render in its current interface.
