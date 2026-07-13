# Submission Quality and Artwork Refresh Plan

Date: 2026-07-12

## Objective

Produce a reviewer-ready Microsoft internal packet and a cleaner versioned Unicode proposal release for Kidney, Stomach, and Liver. Improve the organ artwork, simplify the expected-usage presentation, restore the verified Kidney co-author list, and rebuild every affected document with visual quality checks.

## Audience

- Microsoft materials: David Rhew, Microsoft medical leadership, standards delegates, product/design owners, and Legal.
- Unicode proposals: Emoji Standard & Research Working Group reviewers evaluating the current proposal criteria.

## Decisions

- Preserve `submissions/v1.6.0` as a historical release and create `submissions/v1.7.0`.
- Replace the Section E summary tables with five concise evidence blocks. Each block will include the source, capture date, quantitative takeaway, reproducible URL, and screenshot.
- Use original vector-native artwork rather than generated raster illustration. The deliverables must remain editable SVG and render cleanly at 18x18 and 72x72.
- Keep black-and-white submission images strictly two-tone: black and white only, with no grayscale.
- Restore the verified Kidney submitter names without affiliations: Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller; Timur Erk. Shuhan He remains the main point of contact.
- Keep the four-year eligibility issue explicit. Content and design quality do not override Unicode's re-review rule.

## Work Plan

- [x] Audit the Microsoft internal memo, decision brief, routing briefing, and their rendered artifacts for decision clarity, consistency, dates, claims, and submission links.
- [x] Audit the three `v1.6.0` proposals and PDFs against the live 2026 Unicode requirements.
- [x] Create a coherent organ-art system with stronger silhouettes, fewer fragile details, consistent stroke weight, and improved 18x18 recognition.
- [x] Create `v1.7.0`, update the proposal copy and Kidney submitter list, remove the Section E tables, and rebuild the PDFs.
- [x] Update the Microsoft internal materials to point to the reviewed release and describe the proposal status accurately.
- [x] Render and inspect every page of each affected PDF/DOCX plus the 18x18 and 72x72 artwork; fix all visible defects.
- [x] Run repository checks, commit only task files, and push the current branch.

## Quality Gates

- Every proposal includes the four required example images at the top of page 1.
- Every proposal embeds all five required frequency screenshots directly in Section E.
- Evidence screenshots are legible at ordinary PDF zoom and have clear captions.
- Artwork remains recognizable without color at 18x18.
- No proposal contains affiliations in the Kidney submitter line.
- No stale release links, placeholders, draft labels, clipped text, broken tables, or malformed PDF metadata remain.
- Microsoft documents distinguish content readiness from procedural eligibility and do not imply Microsoft endorsement before approval.

## Versioning

This is a meaningful proposal and artwork revision. The project version is `0.25.0`, with proposal release `v1.7.0`.

## Remaining filing gates

- Kidney, Stomach, and Liver remain future-cycle assets unless Unicode confirms eligibility during the 2026 intake.
- Stomach and Liver still use historical 2020 evidence; Liver's Trends captures are United States-only.
- A current Google refresh requires a manual session on an approved network because Trends returns HTTP 429 and Search presents a CAPTCHA here.
