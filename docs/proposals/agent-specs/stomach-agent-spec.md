# Stomach Proposal Agent Specification

Version: 1.2.0

Status: Ready to assign

## Mission

Produce a complete Stomach prerelease package with current evidence, defensible usage claims, and tested
small-size artwork. Work only in the assigned prerelease lane so other concept agents can run concurrently.

Do not publish or submit the proposal.

## Git and SemVer assignment

- Receive `BASE_COMMIT` and create branch `agent/stomach-2026` in a dedicated worktree from that commit.
- Confirm a clean worktree before editing.
- Copy the complete `submissions/v1.8.0/` package to `submissions/v1.9.0-stomach.1/` byte for byte.
- Set `VERSION` to `1.9.0-stomach.1`. Change only package `manifest.md`, package `CHANGELOG.md`, and files inside
  `stomach/`.
- Never edit a committed package. Further Stomach revisions use `.2`, `.3`, and so on.
- Do not edit root release metadata, shared specifications, or another lane.

## Required reading before editing

Read completely:

- `docs/proposals/2026-submission-slate-spec.md`
- `docs/proposals/CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- The Stomach audit in `docs/proposals/2026-organ-submission-audit.md`
- `submissions/v1.8.0/manifest.md`
- `submissions/v1.8.0/BEST-IN-CLASS-RUBRIC.md`
- `submissions/v1.8.0/IDEAL-EMOJI-PROPOSAL-TEMPLATE.md`
- `submissions/v1.8.0/stomach/stomach_emoji_proposal_SUBMIT.md`
- The entire rendered v1.8.0 Stomach PDF
- Relevant files in `docs/proposals/stomach-emoji-2026/`

Verify current requirements at:

https://www.unicode.org/emoji/proposals.html

Use primary sources and gstack browse for browser research/evidence capture unless it cannot complete the task.

## Fixed identity and scope

The current confirmed submitters are Shuhan He, David Rhew, and Heena Purohit; Shuhan He is the main point of
contact. Preserve the latest concept-specific consent/source record if it changes. Keep the proposal
independently about Stomach; do not use anatomy-set completeness or the existence of other organ emoji as
justification. Verify eligibility, duplicate status, artwork ownership, and rights. Do not infer or fabricate
confirmation records.

## Work required

Before editing proposal prose, create `stomach/CASE-BRIEF.md` and `stomach/CLAIM-LEDGER.md` under the active
package and pass every gate in the shared case-building instructions. Do not draft from the rubric's example
sentence patterns. If the result is `CASE BLOCKED`, repair the evidence or case and report the blocker instead
of polishing generic text.

1. Replace the 2020 Google Search and Video captures with current, readable captures showing result counts.
2. Replace the 2020 Web and Image Trends captures with worldwide, widest-range comparisons against `elephant`.
3. Validate the existing Ngram comparison, query, range, date, and readability; recapture it if noncompliant.
4. Preserve complete query URLs, dates, settings, filters, and limitations for all five required sources.
5. Cite or remove claims about appetite, hunger, nausea, digestion, intuition, courage, stress, and emotional
   expression. Keep only established meanings that support ordinary communication.
6. Red-team Face Vomiting, Nauseated Face, food emoji, Anatomical Heart, Liver, and generic organ imagery as
   substitutes. Explain the remaining semantic gap without overclaiming clinical importance.
7. Build color and black-and-white comparison boards at 18x18 and 72x72 against Liver, Anatomical Heart, food,
   and generic internal-organ shapes.
8. Present the exact four final assets at actual size beside the declared alternatives to Shuhan He and record
   his dated `APPROVE` or `REVISE` decision. No participant panel, sample size, or recognition percentage is
   required.
9. Revise the J-shaped silhouette if it reads as liver, meat, bean, hook, or generic organ. Recheck both color
   and monochrome assets after revision.
10. Rewrite selection and exclusion factors where needed, especially Open-ended, Already representable, and
    Faulty comparison. Use `N/A` instead of speculative positive factors.
11. Rebuild the PDF with `python scripts/make_submission_pdf.py <proposal-markdown-path>` and add
    `stomach/READINESS.md`.

## Required verification

- Validate the four exact PNG dimensions and confirm black-and-white files contain only black/white pixels.
- Validate every local link, evidence caption, date, setting, and source URL.
- Scan for placeholders, old dates presented as current, draft notes, unsupported claims, and layout artifacts.
- Hash-compare all carried-forward files outside `stomach/` and package controls with v1.8.0.
- Run `git diff --check`.
- Check the PDF's pages, fonts, encryption, text extraction, hyperlinks, and file size.
- Render every PDF page and visually inspect it at normal zoom for readability, clipping, broken images, blank
  pages, stranded headings, and incorrect pagination.
- Report missing dependencies, blocked Google captures, or unavailable human testing explicitly.

## Panel feedback loop

Submit the exact final artifact hash to the repeatable [`ESR/UTC-readiness panel`](../review-panel/README.md).
Answer every written action with `ACCEPT`, `REJECT WITH REASON`, or `DEFER WITH OWNER AND DATE`. Material
changes require a new hash and panel rerun. Treat the panel as an internal red team, never named-person or
Unicode feedback.

## Completion and handoff

Commit only the complete Stomach prerelease lane. Do not push, merge, publish, or submit unless explicitly
authorized. Report branch, base commit, prerelease version, commit hash, files changed, evidence and citations,
Shuhan's visual-approval result, verification, readiness score/status, blockers, and coordinator promotion
notes.

Allowed status: `REVISION REQUIRED`, `BLOCKED`, or `READY TO PUBLISH`. Do not use `READY TO SUBMIT` before a
verified public URL, form reconciliation, author confirmation, and Shuhan He's approval exist.
