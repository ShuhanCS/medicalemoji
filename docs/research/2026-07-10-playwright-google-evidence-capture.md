# Playwright workflow for Unicode Google evidence

Verified: 2026-07-10

## Why the prior automated capture failed

Chrome, the gstack browser, and a fresh Playwright Firefox profile all reached the same Google
`unusual traffic` challenge from the current public network address. Changing automation libraries does not
change the network reputation. A compliant workflow therefore needs a one-time human CAPTCHA completion in a
visible browser, followed by slow capture in the same persistent profile.

The workflow does not attempt to bypass, automatically solve, or proxy around Google's controls.

## Setup

Install the Firefox runtime once:

```powershell
npx playwright install firefox
```

The repository includes Playwright as a development dependency and provides:

```text
scripts/capture_unicode_evidence.mjs
```

The script always launches a visible Playwright Firefox window and keeps its profile outside the repository:

```text
%USERPROFILE%\.medicalemoji-google-evidence-firefox
```

Cookies and CAPTCHA-clearance state must never be committed.

The same helper can launch installed Chrome against a dedicated profile supplied by the operator:

```powershell
npm run evidence:capture -- --concept=ultrasound --release=v1.5.0 --browser=chrome --profile=C:\safe\dedicated-profile
```

Do not point this option at an open everyday Chrome profile. Close Chrome and make a dedicated local copy, or
use a fresh profile and complete Google's challenge manually. The copy remains outside the repository.

## Capture one proposal at a time

Start with Ultrasound:

```powershell
npm run evidence:capture -- --concept=ultrasound --release=v1.5.0
```

When the Firefox window shows `I'm not a robot`, complete it manually and wait for the requested results page.
The script polls the visible session and continues automatically after clearance. It will:

1. Open Google Search and click `Tools`.
2. Refuse to save until a result count is visible.
3. Open Google Video Search and require its result count.
4. Open Worldwide Web Trends for 2004-present against `elephant`.
5. Open Worldwide Image Trends for 2008-present against `elephant`.
6. Refuse to save an `Oops`, CAPTCHA, 429, missing-chart, missing-`Worldwide`, or missing-`elephant` state.
7. Write four PNGs plus a JSON capture log with URLs, timestamps, viewport, and the visible result counts.

Run the remaining concepts separately so Google is not hit in a burst:

```powershell
npm run evidence:capture -- --concept=maze --release=v1.5.0
npm run evidence:capture -- --concept=first-aid-kit --release=v1.5.0
```

The grouped multiword Search and Video query for First Aid Kit is `first-aid-kit`, following Unicode's
current guidance.

## Capture everything after the profile is stable

```powershell
npm run evidence:capture -- --concept=all --release=v1.5.0
```

This mode still pauses between pages and concepts. The per-concept mode is safer while the network is being
challenged.

## If Google remains inaccessible

Do not use a CAPTCHA-solving service, rotate proxies, copy another proposal's charts, invent result counts, or
recreate a chart and label it as Google Trends. Keep the proposal in draft status.

Unicode's guidance permits other search engines that display real data when Google is not accessible, but the
substitution must be explained and reproducible. The repository now captures a conservative Bing supplement:

```powershell
npm run evidence:capture:alternate -- --concept=all --release=v1.5.0
```

This command retrieves Bing's HTTPS response with a normal browser user agent, strips response scripts, and
renders that authentic response locally in Playwright Firefox. This avoids turning a bot-challenge page into
evidence while preserving the visible query, result set, and Bing Web count. Each concept receives:

- a Bing Web screenshot with its visible result count;
- a native Bing Video result screenshot;
- a native Bing Image result screenshot; and
- a JSON log containing the exact URLs, queries, timestamps, viewport, and capture method.

The 2026-07-10 Bing Web snapshots reported approximately 105,000 results for `ultrasound`, 46,200 for `maze`,
and 19,900 for the exact phrase `"first aid kit"`. Bing did not expose total counts on its Video or Image
verticals. These are useful supplemental records, but they do not silently replace Google Trends Web and Image
comparisons. The proposals therefore remain labeled DRAFT.

The lowest-risk filing route is to run the Google helper from a Microsoft corporate or ordinary residential
network that Google accepts. If that is still impossible, Microsoft's standards and Bing owners should first
confirm a public, reproducible, comparable substitute for the two Trends categories under Unicode's explicit
Google-inaccessibility exception.

Official Unicode evidence guidance:

https://www.unicode.org/emoji/proposals.html
