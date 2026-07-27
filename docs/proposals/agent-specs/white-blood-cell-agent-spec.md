# White Blood Cell Proposal Agent Specification

Version: 1.4.0

Status: Ready to assign

## Mission

Turn the evidence-gated White Blood Cell draft into a rigorously audited prerelease package, or document the
specific blockers that prevent it from advancing. Work independently in the assigned prerelease lane and do
not alter canonical or shared files.

Do not publish or submit the proposal.

## Git and SemVer assignment

- Receive `BASE_COMMIT` from the coordinator and start branch `agent/white-blood-cell-2026` in an isolated
  worktree from that exact commit.
- Confirm a clean worktree before editing.
- Copy all of `submissions/v1.8.0/` byte for byte to
  `submissions/v1.9.0-white-blood-cell.1/`.
- Set `VERSION` to `1.9.0-white-blood-cell.1`. Change only package `manifest.md`, package `CHANGELOG.md`, and
  files inside `white-blood-cell/`.
- Never edit an existing snapshot. A later lane update becomes `v1.9.0-white-blood-cell.2`, then `.3`.
- Do not edit root release metadata, shared specifications, or another proposal lane.

## Required reading before editing

Read completely:

- `docs/proposals/2026-submission-slate-spec.md`
- `docs/proposals/CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- `submissions/v1.8.0/manifest.md`
- `submissions/v1.8.0/white-blood-cell/white-blood-cell_emoji_proposal_DRAFT.md`
- The entire rendered v1.8.0 White Blood Cell PDF
- `docs/proposals/archive-2020-emojination-drafts/white-blood-cell-organ.md`

Verify current requirements at:

https://www.unicode.org/emoji/proposals.html

Use primary sources and the repository-preferred gstack browse workflow for web research and evidence capture.

## Fixed identity and scope

The current v1.8.0 draft lists Shuhan He as submitter and main point of contact, but the latest
concept-specific consent/source record controls. Reconfirm it before revision and preserve every confirmed
coauthor. Do not restore historical names without current consent. Keep the concept at the broad
leukocyte/white-blood-cell level; do not imply
that Unicode should encode every immune-cell subtype, laboratory result, or disease marker. Verify eligibility,
duplicate status, artwork ownership, and the CC0 rights statement without inventing missing evidence.

## Work required

Use the shared proposal-building guidance to study the historical record and develop a compelling
candidate-specific case before polishing the prose. It does not require a separate case brief, claim ledger,
or gate status. Do not draft from the rubric's example sentence patterns.

1. Recapture Google Search and Google Video Search; the archived 2020 captures are stale.
2. Replace Web Trends with a worldwide widest-range comparison against `elephant` and add the missing Image
   Trends comparison using the same standard.
3. Verify or recapture the Ngram comparison against `elephant`, including the widest available range and a
   reproducible query record.
4. Preserve full URLs and operational capture details in an internal record. In the PDF, show only the query,
   date, comparator, settings, result, and limitation needed to understand each exhibit.
5. Explain White Blood Cell's relevant semantic and visual distinctions from Microbe, Drop of Blood, Test Tube,
   Microscope, Shield, and generic-cell imagery without turning the section into a catalog of objections.
6. Cite the material claims about immunity, infection, inflammation, white-cell counts, laboratory testing,
   treatment monitoring, education, and research on which the selection case depends. Combine citations where
   practical. Disease burden cannot be the encoding case.
7. Use actual-size comparison boards only if they help resolve or explain the artwork.
8. Present the exact four final assets at actual size, with useful alternatives when needed, to Shuhan He.
   Record his dated `APPROVE` or `REVISE` decision; no participant panel, sample size, or recognition percentage
   is required.
9. Revise the paradigm if the lobed nucleus disappears or the image reads as a face, germ, bubble, or generic
   cell. Re-run technical checks and obtain fresh Shuhan approval after any art change.
10. Rewrite the proposal under the current factor order, using `N/A` for unsupported factors and directly
    answering Already representable, Overly specific, Open-ended, Transient, and Faulty comparison.
11. Rebuild the PDF with `python scripts/make_submission_pdf.py <proposal-markdown-path>`. If
    `white-blood-cell/READINESS.md` is maintained, keep it to unresolved official filing conditions and handoff
    status.

## Required verification

- Validate exact PNG dimensions and true black-and-white pixels.
- Validate all local links, image paths, evidence captions, dates, and full source URLs.
- Scan for placeholders, stale draft language, unsupported claims, and inconsistent proposal status.
- Hash-compare every carried-forward file outside the active folder and package controls with v1.8.0.
- Run `git diff --check`.
- Check PDF pages, fonts, encryption, text extraction, hyperlinks, and file size.
- Render and visually inspect every PDF page for evidence readability, clipping, blank pages, broken images, and
  layout defects.
- Report any browser/CAPTCHA, dependency, or human-testing limitation rather than working around it silently.

## Optional editorial panel

Use the repeatable [`ESR/UTC-readiness panel`](../review-panel/README.md) only when another editorial perspective
would help. Its feedback is advisory and does not require an action ledger, numeric verdict, or automatic
rerun. Treat it as internal editorial input, never named-person or Unicode feedback.

## Completion and handoff

Commit only the complete White Blood Cell prerelease lane. Do not push, merge, publish, or submit unless
explicitly authorized. Report the branch, base commit, prerelease version, commit hash, changed files, evidence
captures, citations, Shuhan's visual-approval result, verification, status, blockers, and coordinator
promotion notes.

Allowed status: `REVISION REQUIRED`, `BLOCKED`, or `READY TO PUBLISH`. `READY TO SUBMIT` is forbidden until the
exact PDF has a verified logged-out URL, matching form data, confirmed authorship, and Shuhan He's authorization.
