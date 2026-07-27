# Kidney Proposal Agent Specification

Version: 1.6.0

Status: Completed in canonical package v1.10.0; retain for audit only

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
- `docs/proposals/CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- `docs/proposals/2026-organ-submission-audit.md`, especially the Kidney audit
- `submissions/v1.9.0/manifest.md`
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

Use the shared proposal-building guidance to study the historical record and develop a compelling
candidate-specific case before polishing the prose. It does not require a separate case brief, claim ledger,
or gate status. Do not draft from the rubric's example sentence patterns.

1. Audit every proposal claim against the current rubric. Remove cause, prestige, burden, or deservingness
   language that substitutes for expected use.
2. Strengthen the independent semantic case against Beans, Droplet, Anatomical Heart, Lungs, and generic
   medical sequences. Do not argue that Unicode should complete an organ set.
3. Verify the five required Search, Video, Web Trends, Image Trends, and Ngram captures for readability, query settings,
   widest range, worldwide scope where supported, `elephant` comparator, capture date, and reproducibility.
   Recapture only evidence that fails current requirements.
4. Cite the material literal, metaphorical, and medical-use claims on which the selection case depends. Combine
   citations where one authoritative source supports a paragraph; remove unsupported speculative uses.
5. Use an actual-size nearest-emoji comparison only if it makes the visual case clearer. Present the exact four
   final assets to Shuhan He at actual size and record his dated `APPROVE` or `REVISE` decision. No
   human-recognition panel is required.
6. Use a computer validator only as an optional internal design aid. Do not include its algorithms, hashes,
   thresholds, scores, or pass/fail narrative in the public proposal.
7. If Shuhan's actual-size review or an optional design check finds the image unclear, revise the source so the
   medial notch, hilum, and short attachment survive in both small paradigms without turning the image into a
   bean, bulb, balloon, or food icon.
8. Rebuild the PDF whenever source text or embedded assets change using
   `python scripts/make_submission_pdf.py <proposal-markdown-path>`.
9. If `kidney/READINESS.md` is maintained, keep it to unresolved official filing conditions, exact changes,
   and handoff status. Do not assign a proposal score or reproduce internal QA in the public proposal.

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

## Optional editorial panel

Use the repeatable [`ESR/UTC-readiness panel`](../review-panel/README.md) only when another editorial perspective
would help. Its feedback is advisory and does not require an action ledger, numeric verdict, or automatic
rerun. Treat it as internal editorial input, never named-person or Unicode feedback.

## Completion and handoff

Commit the complete prerelease snapshot with a Kidney-specific commit message. Do not push, merge, publish, or
submit unless explicitly authorized. Report:

- branch and starting commit;
- prerelease version and commit hash;
- files changed and files intentionally carried forward;
- evidence recaptured and sources cited;
- visual or technical checks used when they materially informed the artwork;
- verification performed;
- readiness status;
- blockers and exact coordinator promotion notes.

Allowed status: `REVISION REQUIRED`, `BLOCKED`, or `READY TO PUBLISH`. Never claim `READY TO SUBMIT` without the
public URL, form reconciliation, author confirmation, and Shuhan He's authorization.
