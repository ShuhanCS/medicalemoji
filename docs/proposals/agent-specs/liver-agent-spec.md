# Liver Proposal Agent Specification

Version: 1.2.0

Status: Ready to assign

## Mission

Correct the Liver proposal's stale evidence, weak small-size recognition, and unsupported usage claims in a
complete prerelease package. Work only in the assigned lane and do not modify shared or canonical files.

Do not publish or submit the proposal.

## Git and SemVer assignment

- Receive `BASE_COMMIT` and create branch `agent/liver-2026` in an isolated worktree from that exact commit.
- Confirm a clean worktree before editing.
- Copy all of `submissions/v1.8.0/` byte for byte to `submissions/v1.9.0-liver.1/`.
- Set `VERSION` to `1.9.0-liver.1`. Change only package `manifest.md`, package `CHANGELOG.md`, and files inside
  `liver/`.
- Every later Liver update creates `.2`, `.3`, and so on. Never edit an earlier snapshot.
- Do not edit root release metadata, shared specifications, or another lane.

## Required reading before editing

Read completely:

- `docs/proposals/2026-submission-slate-spec.md`
- `docs/proposals/CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- The Liver audit in `docs/proposals/2026-organ-submission-audit.md`
- `submissions/v1.8.0/manifest.md`
- `submissions/v1.8.0/BEST-IN-CLASS-RUBRIC.md`
- `submissions/v1.8.0/IDEAL-EMOJI-PROPOSAL-TEMPLATE.md`
- `submissions/v1.8.0/liver/liver_emoji_proposal_SUBMIT.md`
- The entire rendered v1.8.0 Liver PDF
- Relevant files in `docs/proposals/liver-emoji-2026/`

Verify current requirements at:

https://www.unicode.org/emoji/proposals.html

Use authoritative sources and gstack browse for browser research/evidence capture unless it cannot complete the
task.

## Fixed identity and scope

The current confirmed submitters are Shuhan He, David Rhew, and Heena Purohit; Shuhan He is the main point of
contact. Preserve the latest concept-specific consent/source record if it changes. Keep Liver independent of an
anatomy-set argument. Verify eligibility, duplicate status, artwork ownership, and rights. Do not invent missing
confirmation or review records.

## Work required

Before editing proposal prose, create `liver/CASE-BRIEF.md` and `liver/CLAIM-LEDGER.md` under the active
package and pass every gate in the shared case-building instructions. Do not draft from the rubric's example
sentence patterns. If the result is `CASE BLOCKED`, repair the evidence or case and report the blocker instead
of polishing generic text.

1. Replace the 2020 Google Search and Video captures with current, readable evidence.
2. Replace the old Web and Image Trends captures, especially U.S.-only charts, with worldwide widest-range
   comparisons against `elephant`.
3. Validate or recapture the Ngram comparison against `elephant` with the widest available range.
4. Preserve full query URLs, dates, ranges, locations, modes, filters, visible results, and limitations.
5. Cite or remove claims about metabolism, detoxification, disease, donation/transplant, food/cuisine, courage,
   temperament, or other metaphorical and cultural meanings. Medical importance is not expected-use evidence.
6. Red-team Stomach, Anatomical Heart, meat/food emoji, Beans, and generic organ imagery as substitutes or
   confusion targets.
7. Build comparison boards at 18x18 and 72x72 in color and black-and-white.
8. Present the exact four final assets at actual size beside the declared alternatives to Shuhan He and record
   his dated `APPROVE` or `REVISE` decision. No participant panel, sample size, or recognition percentage is
   required.
9. Rework both small silhouettes until the liver reads reliably without depending on internal details that
   disappear at emoji size. Retest after each art revision.
10. Keep Multiple meanings, Completeness, and Compatibility as `N/A` unless strong cited evidence survives
    review. Rewrite Already representable, Overly specific, Open-ended, Transient, and Faulty comparison.
11. Rebuild the PDF using `python scripts/make_submission_pdf.py <proposal-markdown-path>` and add
    `liver/READINESS.md`.

## Required verification

- Confirm exact dimensions for all four PNGs and true black/white pixels in monochrome assets.
- Validate local links, evidence settings, captions, dates, and source URLs.
- Scan for stale dates, placeholders, unsupported assertions, draft notes, and contradictory readiness labels.
- Hash-compare all carried-forward files outside `liver/` and package controls with v1.8.0.
- Run `git diff --check`.
- Inspect PDF pages, fonts, encryption, extractable text, hyperlinks, and file size.
- Render and visually inspect every page for evidence readability, clipping, broken images, empty pages, poor
  page breaks, and pagination errors.
- State any missing dependency, blocked capture, or unavailable human-testing gate honestly.

## Panel feedback loop

Submit the exact final artifact hash to the repeatable [`ESR/UTC-readiness panel`](../review-panel/README.md).
Answer every written action with `ACCEPT`, `REJECT WITH REASON`, or `DEFER WITH OWNER AND DATE`. Material
changes require a new hash and panel rerun. Treat the panel as an internal red team, never named-person or
Unicode feedback.

## Completion and handoff

Commit only the complete Liver prerelease lane. Do not push, merge, publish, or submit unless explicitly
authorized. Report branch, base commit, prerelease version, commit hash, files changed, evidence/citations,
Shuhan's visual-approval result, verification, readiness score/status, blockers, and coordinator promotion
notes.

Allowed status: `REVISION REQUIRED`, `BLOCKED`, or `READY TO PUBLISH`. Never claim `READY TO SUBMIT` without a
verified public PDF URL, reconciled form data, author confirmation, and Shuhan He's approval.
