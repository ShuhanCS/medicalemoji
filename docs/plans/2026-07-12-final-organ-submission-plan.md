# Final organ proposal submission plan

Date: 2026-07-12

## Audience and outcome

The three proposal PDFs are written for Unicode's Emoji Standard & Research Working Group. The outcome is a
new synchronized `submissions/v1.6.0/` release containing final Kidney, Stomach, and Liver proposal sources,
embedded frequency screenshots, example artwork, rights documentation, and rendered PDFs.

The older `submissions/v1.2.0/` packet remains unchanged as the historical July 9 release.

## Governing requirement

Unicode's live 2026 guidance requires the proposal itself to include screenshots for all five frequency
methods: Google Search, Google Video Search, Google Trends Web Search, Google Trends Image Search, and Google
Books Ngram Viewer. Reproducible links supplement those screenshots; they do not replace them.

Official guidance:

https://www.unicode.org/emoji/proposals.html

## Scope

1. Copy the complete `v1.2.0` organ packet into a new `v1.6.0` release.
2. Update proposal dates and public packet/license links to the current branch and release.
3. Keep all five evidence screenshots embedded in each proposal under `E. Expected usage level`.
4. Preserve the true capture date and geographic scope of every historical screenshot.
5. Rebuild each final PDF and confirm its embedded raster-image inventory.
6. Render and visually inspect every PDF page for clipping, broken images, unreadable evidence, and bad page
   breaks.
7. Scan sources and extracted PDF text for placeholders, internal planning language, stale packet links, and
   unsupported claims.
8. Update the repository version, changelog, README/handoff status where needed, then commit and push.

## Eligibility boundary

The proposal documents will be finalized on their technical merits. The release manifest will retain a
separate filing gate: Unicode's public guidance says emoji declined within the last four years are not
eligible for re-review, while the recorded organ decline notices are dated 2022-11-04 and the current intake
closes 2026-07-31. The proposal text will not argue eligibility, but the manifest will not conceal this
external procedural risk.

## Quality gates

- Four example images appear at the top of page one: color and true black-and-white at 18x18 and 72x72.
- All five frequency screenshots are visibly embedded in each PDF.
- Every evidence row states its capture date and reproducible full URL.
- The artwork license and public asset URLs resolve to `codex/eligible-2026-slate/submissions/v1.6.0/`.
- PDFs contain no TODO, TBD, placeholder, draft, or internal-only language.
- All rendered pages pass visual inspection.
- `git diff --check`, Python compilation, lint, and build succeed.

## Semantic version decision

This is a substantive proposal release because it republishes the three organ packets as the current final
submission candidates and updates their public evidence packaging. Advance the proposal release from
`v1.5.0` to `v1.6.0` and the project version from `0.23.0` to `0.24.0`.
