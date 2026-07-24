# Liver Emoji Evidence Refresh Plan

Date: 2026-07-23
Scope: new immutable revision `submissions/v1.9.0-liver.2/liver/`, copied from `v1.9.0-liver.1`

## Objective

Promote the confirmed Liver eligibility decision into a new immutable prerelease revision and replace the two historical Google visible-count captures with current, reproducible evidence.

## Steps

1. Copy the complete frozen `v1.9.0-liver.1` package to `v1.9.0-liver.2`, then record eligibility as confirmed and remove it from the submission-blocking gates.
2. Capture current Google Search and Google Video Search result pages for `liver`, preserving the complete query URLs and visible result counts.
3. Update the evidence inventory, proposal narrative, readiness report, and package changelog without overstating any data that cannot be observed.
4. Rebuild the submission PDF and verify linked evidence, image dimensions, and PDF integrity.
5. Commit and push the focused packet and plan updates on `codex/liver-evidence`.

## Acceptance Criteria

- Eligibility is recorded as confirmed, with no remaining eligibility-date gate.
- Search and Video evidence files are current, dated, and referenced consistently.
- The proposal and readiness report describe the fresh captures accurately.
- The rebuilt PDF passes the packet's existing structural checks.

## Completion

- Completed 2026-07-24: created immutable packet `v1.9.0-liver.2` from `v1.9.0-liver.1`.
- Completed: recorded the project owner's eligibility confirmation and removed eligibility as a must-pass gate.
- Completed: captured current Google Web and Video result-stat values and documented Google's zero-layout display
  behavior in the packet's evidence notes.
- Completed: rebuilt the PDF and verified local links, page size, tagging, fonts, image assets, and changed
  evidence pages.
