# Pill Pack / Blister Pack Proposal Agent Specification

Version: 1.0.0

Status: Ready to assign as a provisional go/no-go workstream

## Mission

Determine whether the archived Pill Pack concept can become a defensible current proposal, preferably under a
generic name such as `Blister Pack`, and create an immutable decision prerelease package. Advancement is not
assumed. A well-supported `DO NOT ADVANCE` result is valid.

Do not publish or submit the proposal.

## Git and SemVer assignment

- Receive `BASE_COMMIT` and create branch `agent/pill-pack-2026` in an isolated worktree from that commit.
- Confirm a clean worktree before editing.
- Copy all of `submissions/v1.8.0/` byte for byte to `submissions/v1.9.0-pill-pack.1/`.
- Copy the complete historical `submissions/v1.3.0/pill-pack/` folder into that prerelease package, preserving
  it first as source provenance before making changes.
- Set `VERSION` to `1.9.0-pill-pack.1`. Update package `manifest.md`, package `CHANGELOG.md`, artwork licensing
  controls if required, and only the imported `pill-pack/` folder.
- A later decision or proposal update becomes `.2`, `.3`, and so on. Never edit an earlier snapshot.
- Do not edit root release metadata, shared specifications, canonical v1.8.0, historical v1.3.0, or another
  lane.

## Required reading before editing

Read completely:

- `docs/proposals/2026-submission-slate-spec.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- `submissions/v1.3.0/manifest.md`
- `submissions/v1.3.0/ARTWORK-LICENSE.md`
- `submissions/v1.3.0/pill-pack/pill-pack_emoji_proposal_DRAFT.md`
- The entire rendered v1.3.0 Pill Pack PDF
- `docs/proposals/archive-2020-emojination-drafts/pill-pack-object.md`
- `docs/strategy/2026-07-12-microsoft-medical-emoji-decision-brief.md`
- `docs/strategy/2026-07-10-eligible-proposal-ranking.md`
- `docs/research/2026-07-10-eligible-portfolio-status.md`

Verify current requirements and status definitions at:

https://www.unicode.org/emoji/proposals.html

https://www.unicode.org/emoji/emoji-proposals-status.html

Use primary sources and gstack browse for current research/evidence capture unless it cannot complete the task.

## Identity, name, and portfolio gates

The current v1.3.0 draft names Shuhan He as submitter and main point of contact. Reconfirm the complete byline
from the latest concept-specific record and preserve every confirmed individual. Never restore historical
coauthors without explicit current consent. Confirm current eligibility, duplicate
status, artwork ownership, and rights without inventing records.

Evaluate `Blister Pack`, `Medication Blister Pack`, and `Pill Pack` as generic names and search terms. PillPack
is also a pharmacy brand; the proposal and artwork must not encode or imply that brand. Do not use brand usage
as compatibility evidence.

Pill Pack and Pill Box must not both be filed in this intake without an explicit portfolio decision. The agent
must compare them directly and recommend one of: advance Pill Pack/Blister Pack, prefer Pill Box, hold both, or
reject this medication-packaging lane.

## Work required

1. Write `pill-pack/GO-NO-GO.md` before polishing the proposal. Lead with the strongest case that Pill already
   represents the idea and that a blister pack is only a product variant.
2. Define the independent messages, if any: sealed doses, remaining supply, dispensing, finite treatment
   course, travel packaging, or adherence. Reject uses that ordinary Pill, Calendar, Package, or sequences
   already express adequately.
3. Research whether the generic concept has broad, worldwide, durable communication use. Separate medication
   packaging from dose-administration systems and the PillPack brand.
4. Recapture all five required sources from scratch: Google Search, Google Video, worldwide widest-range Web
   Trends versus `elephant`, worldwide widest-range Image Trends versus `elephant`, and widest-range Ngram
   versus `elephant`. Preserve queries, dates, settings, visible results, and limitations.
5. Remove opioid-crisis, adherence advocacy, professional importance, petition, social-media request, and cause
   language unless a narrowly relevant factual statement is cited and does not substitute for expected use.
6. Build comparison boards at 18x18 and 72x72 against Pill, Pill Box, Package, Calendar, keypad, remote control,
   and generic packaging in color and black-and-white.
7. Present the exact four final assets at actual size beside keypad, remote, calendar, pills, and packaging to
   Shuhan He. Record his dated `APPROVE` or `REVISE` decision; no participant panel, sample size, or recognition
   percentage is required.
8. Revise the art only if the concept survives the substitute and evidence gates. Keep it textless, generic,
   vendor-flexible, and recognizable without brand colors, dosage text, logos, or a fixed tablet count.
9. If advancing, rewrite every current inclusion and exclusion factor, rebuild the PDF with
   `python scripts/make_submission_pdf.py <proposal-markdown-path>`, and add `pill-pack/READINESS.md`.
10. If not advancing, keep the historical source clearly labeled, record the evidence-based no-go decision,
    and do not rename a draft to `_SUBMIT` or manufacture a high readiness score.

## Required verification

- Confirm all included PNGs have exact required dimensions and true monochrome assets contain only black/white.
- Verify all local links, full URLs, evidence captions, dates, query settings, and rights statements.
- Scan for brand confusion, stale 2020 claims, unsupported medical assertions, placeholders, and contradictory
  readiness language.
- Hash-compare all carried-forward files outside `pill-pack/` and package controls with v1.8.0.
- Run `git diff --check`.
- If a PDF is rebuilt, inspect pages, fonts, encryption, text extraction, hyperlinks, file size, and every
  rendered page at normal zoom.
- Report blocked Google sessions, missing dependencies, unresolved authorship/rights, and missing Shuhan image
  approval honestly.

## Decision and handoff

The final decision must be exactly one of:

- `ADVANCE TO FILING SLATE`
- `PREFER PILL BOX`
- `HOLD BOTH MEDICATION-PACKAGING CONCEPTS`
- `DO NOT ADVANCE`

Commit only the complete Pill Pack prerelease decision package. Do not push, merge, publish, or submit unless
explicitly authorized. Report branch, base commit, version, commit hash, files changed, evidence, Shuhan's
visual-approval result, decision, readiness score if applicable, blockers, and coordinator promotion notes.
