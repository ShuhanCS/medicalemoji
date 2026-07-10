# Mouse-maze artwork and browser evidence-capture plan

Date: 2026-07-10
Target proposal release: `v1.5.0`
Target project version: `0.23.0`

## Goal

Revise the Maze proposal so its example image is visibly a mouse navigating a maze, while retaining the
general Unicode name `Maze` and preserving broader puzzle, path, navigation, complexity, learning, memory,
choice, and research uses. Establish a legitimate browser workflow for the four missing Google evidence
categories in the v1.5.0 proposals.

## Browser approach

1. Use Playwright Firefox rather than Chrome so Shuhan's normal Chrome sessions are not disturbed.
2. Keep a dedicated persistent Firefox profile for the evidence run.
3. If Google presents a CAPTCHA, require a one-time human completion in the visible browser. Do not attempt to
   bypass or automatically solve the challenge.
4. Reuse the cleared profile and capture each proposal slowly and sequentially.
5. Capture Google Search after opening `Tools` so the visible result count is included.
6. Capture Google Video Search with its result count, plus Worldwide Web and Image Trends against `elephant`.
7. Preserve the exact source URL, capture date, viewport, and filename for every screenshot.
8. If Google continues returning 429 after human verification, retain the drafts and document that the
   blocker is network-level. Unicode permits comparable alternative search data only when Google is not
   accessible, but alternative data must be labeled and justified rather than presented as Google evidence.
9. Capture a reproducible Bing Web/Video/Image supplement so Microsoft has real evidence to review while the
   preferred Google capture is moved to a clean corporate or residential network. Do not claim that the Bing
   supplement supplies the two missing Trends comparisons.

## Deliverables

- [x] Versioned `v1.5.0` packet carrying all three v1.4.0 concepts.
- [x] Original mouse-maze SVG plus 18x18 and 72x72 color/black-and-white PNGs.
- [x] Revised Maze narrative, manifest, ranking, README, HANDOFF, and Microsoft brief.
- [x] Rebuilt proposal PDFs and Microsoft DOCX/PDF with page-by-page visual inspection.
- [x] Reusable Playwright Firefox capture helper and operator instructions.
- [x] Reproducible Bing Web/Video/Image supplemental captures and JSON logs for all three concepts.
- [ ] Required Google screenshots inserted after the capture runs from a network Google accepts, or a
      complete substitute is cleared under Unicode's Google-inaccessibility exception.
- [x] Validation and semver update.
- [x] Commit, rebase, and push.

## Semver decision

The mouse-maze paradigm changes substantive artwork and proposal framing, so the proposal release advances
by a minor version from `v1.4.0` to `v1.5.0`. The project version advances from `0.22.0` to `0.23.0` because
the current proposal release, internal strategy documents, artwork, and evidence workflow all change.
