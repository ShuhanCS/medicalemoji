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

- `stomach_google_search_2026-07-26_CANDIDATE.png` — `c2c4ef08dafa59a6b07014dd1172f8d0dd71d1dd92dfe2dc4525cc4cd0a6f6b5`
- `stomach_google_video_search_2026-07-26_CANDIDATE.png` — `99b9ffb9facdee2c221bde83be0f063e77d17345d43baec928c3920cca0113a9`
- `stomach_google_trends_web_elephant_2026-07-26_CANDIDATE.png` — `4d6ee031ac1a03656c85b711ba1f399e375ea521d87ad319ae4c8386d72d5387`
- `stomach_google_trends_image_elephant_2026-07-26_CANDIDATE.png` — `2c0a6977df088b357c16eed3ae8641fc5ba50ff5bc43fd21e6438ed865f471be`
- `stomach_google_books_ngram_elephant_2026-07-26_CANDIDATE.png` — `7f3b174662547b54dca6bce4f9fc4a3f08d64df4d8f7f6a1fa470424734dd3a1`

## Capture notes

1. Google initially returned a CAPTCHA and Trends HTTP 429 in an isolated session.
2. The final artifacts were taken only after interactive verification in a persistent Firefox profile.
3. Search used `filter=0` so the visible result estimate did not silently omit similar results.
4. Every screenshot preserves the query, source mode or settings, and the visible limitation or comparison.
5. Search-result counts are estimates and may change when the query is reproduced.
