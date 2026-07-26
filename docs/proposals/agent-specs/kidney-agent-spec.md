# Kidney Proposal Agent Specification

Version: 1.1.0

Status: Ready to assign

## Mission

Produce a complete, reviewable Kidney proposal prerelease package that corrects the known v1.9.0 weaknesses
without altering any canonical or shared files. The result must be suitable for coordinator promotion to the
next canonical release, expected to be `v1.10.0`.

Do not publish or submit the proposal.

## Git and SemVer assignment

- Receive the exact `BASE_COMMIT` from the coordinator.
- Create or use an isolated worktree on branch `agent/kidney-2026` from that exact commit.
- Confirm `git status --short --branch` is clean before editing.
- Copy the complete `submissions/v1.9.0/` directory byte for byte to
  `submissions/v1.10.0-kidney.1/`.
- Set the copied package `VERSION` to `1.10.0-kidney.1` and update only its package `manifest.md` and
  `CHANGELOG.md` plus files inside its `kidney/` folder.
- Never edit `v1.9.0`. Every later Kidney update creates a complete new immutable package named
  `v1.10.0-kidney.2`, `.3`, and so on.
- Do not edit root release metadata or another proposal lane. Commit only this lane's files.

## Required reading before editing

Read all of the following completely:

- `docs/proposals/2026-submission-slate-spec.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- `docs/proposals/2026-organ-submission-audit.md`, especially the Kidney audit
- `submissions/v1.9.0/manifest.md`
- `submissions/v1.9.0/BEST-IN-CLASS-RUBRIC.md`
- `submissions/v1.9.0/IDEAL-EMOJI-PROPOSAL-TEMPLATE.md`
- `submissions/v1.9.0/kidney/kidney_emoji_proposal_SUBMIT.md`
- The entire rendered v1.9.0 Kidney PDF

Verify the current official requirements against:

https://www.unicode.org/emoji/proposals.html

Use primary or authoritative sources for factual claims. Use the repository-preferred gstack browse workflow
for browser research and evidence capture; use raw Playwright only if gstack cannot complete the task.

## Fixed identity and rights

Preserve this exact author order, separated by semicolons:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk; David Rhew; Heena Purohit.

Shuhan He remains the main point of contact. Do not add credentials or affiliations unless they are verified
and improve the filing. Archive or clearly identify the eligibility confirmation and author consent status;
do not invent missing records. Confirm that the artwork rights statement and CC0 record cover every final asset.

## Work required

1. Audit every proposal claim against the current rubric. Remove cause, prestige, burden, or deservingness
   language that substitutes for expected use.
2. Strengthen the independent semantic case against Beans, Droplet, Anatomical Heart, Lungs, and generic
   medical sequences. Do not argue that Unicode should complete an organ set.
3. Verify every 2026 Search, Video, Web Trends, Image Trends, and Ngram capture for readability, query settings,
   widest range, worldwide scope where supported, `elephant` comparator, capture date, and reproducibility.
   Recapture only evidence that fails current requirements.
4. Cite durable sources for literal and metaphorical uses, transplant/donation contexts, dialysis, hydration,
   laboratory or medication claims. Remove plausible but unsupported use sequences.
5. Build a nearest-emoji comparison board at actual 18x18 and 72x72 sizes in color and black-and-white.
6. Prepare and document an unprompted recognition protocol. The intended internal target is at least 80% correct
   at 18x18 with no wrong concept above 10%. Do not fabricate participants or substitute AI guesses for human
   recognition data. If human results are unavailable, mark the gate unresolved.
7. If the art fails, revise the source so the medial notch, hilum, and short attachment survive in both small
   paradigms without turning the image into a bean, bulb, balloon, or food icon.
8. Rebuild the PDF whenever source text or embedded assets change using
   `python scripts/make_submission_pdf.py <proposal-markdown-path>`.
9. Add `kidney/READINESS.md` with the must-pass gate table, updated internal score, findings by severity,
   exact changes, unresolved blockers, and one permitted status.

## Required verification

- Confirm all four PNGs are exactly 18x18 or 72x72 and black-and-white assets use no gray or color pixels.
- Confirm every Markdown image/link resolves locally and the proposal contains no placeholder, stale draft
  note, contradictory status, broken image, or unverified factual assertion.
- Compare copied files outside `kidney/` and package controls with v1.9.0 by hash; they must be byte-identical.
- Run `git diff --check`.
- Inspect PDF page count, encryption, fonts, text extraction, hyperlinks, and file size.
- Render every PDF page to images and inspect at normal zoom for clipping, unreadable evidence, blank pages,
  awkward breaks, and incorrect page numbers.
- Run repository lint/build only if dependencies are installed; report unavailable checks honestly.

## Completion and handoff

Commit the complete prerelease snapshot with a Kidney-specific commit message. Do not push, merge, publish, or
submit unless explicitly authorized. Report:

- branch and starting commit;
- prerelease version and commit hash;
- files changed and files intentionally carried forward;
- evidence recaptured and sources cited;
- art/recognition result, including participant count or an explicit unresolved-human-test gate;
- verification performed;
- readiness score and status;
- blockers and exact coordinator promotion notes.

Allowed status: `REVISION REQUIRED`, `BLOCKED`, or `READY TO PUBLISH`. Never claim `READY TO SUBMIT` without the
public URL, form reconciliation, author confirmation, and Shuhan He's authorization.
