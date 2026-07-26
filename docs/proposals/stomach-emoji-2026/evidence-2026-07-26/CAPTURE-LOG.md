# Stomach Evidence Capture Log

Capture date: 2026-07-26

Browser: Playwright CLI with Firefox, persistent profile after interactive Google verification

Viewport: 1440x1100

Locale requested: English

## Results

| Source | Result | Technical evidence |
| --- | --- | --- |
| Google Search | PASS | Exact query loaded after interactive verification; Tools panel shows about 353,000,000 results. |
| Google Video Search | PASS | Exact query loaded; Tools panel shows about 139,000,000 results. |
| Google Trends - Web Search | PASS | Both terms loaded with Worldwide, 2004-present, All categories, and Web Search visible; graph and regional breakdown rendered. |
| Google Trends - Image Search | PASS | Both terms loaded with Worldwide, 2008-present, All categories, and Image Search visible; graph and regional breakdown rendered. |
| Google Books Ngram Viewer | PASS | Page loaded with `elephant,stomach`, 1500-2022, English, case-insensitive, smoothing 3; screenshot visually inspected. |

## Accepted artifacts

- `stomach_google_search_2026-07-26_CANDIDATE.png` — `f29d1d2a3a6157d49143ed149b79deb9bf4069d21e6a31971621225dc4363c08`
- `stomach_google_video_search_2026-07-26_CANDIDATE.png` — `365bdd213219dddb712ec43a1670f5874f142b03adf426773db2394b4c2a3708`
- `stomach_google_trends_web_elephant_2026-07-26_CANDIDATE.png` — `c939e23b61b874c8f0acff8a2d6c9730eddeaa9d2f9840c482231f37d19c752d`
- `stomach_google_trends_image_elephant_2026-07-26_CANDIDATE.png` — `61b4ac92b52a9b68736f09e78f2e36be44e92ff74d033e3e60a439c5c3ce1d2e`
- `stomach_google_books_ngram_elephant_2026-07-26_CANDIDATE.png` — `2e79d604ad5a9361f67d820fc762090c53ce2bc3e0df1cdaed5fe7da0242c8cb`

## Capture notes

1. Google initially returned a CAPTCHA and Trends HTTP 429 in an isolated session.
2. The final artifacts were taken only after interactive verification in a persistent Firefox profile.
3. Search used `filter=0` so the visible result estimate did not silently omit similar results.
4. Every screenshot preserves the query, source mode or settings, and the visible limitation or comparison.
5. Search-result counts are estimates and may change when the query is reproduced.
