# 2026 Emoji Submission Slate and Serial Agent Execution Specification

Version: 1.4.0

Date: 2026-07-21

Deadline: End of day 2026-07-31

Official guidelines:

https://www.unicode.org/emoji/proposals.html

## Decision

Work through five proposal workstreams in this strict order:

1. Kidney
2. White Blood Cell
3. Stomach
4. Liver
5. Pill Pack, as a provisional new workstream that must pass a go/no-go gate before it joins the filing slate

Kidney is first in the canonical promotion order. Separate agents may work on all five concepts concurrently,
but only in their assigned prerelease lanes. Canonical packages are promoted one by one so every final version
contains all earlier accepted work. Each concept that advances will have a separate proposal PDF and a separate
submission-form entry. The organs are not presented as an anatomy set, and no proposal may depend on another
candidate for its selection case.

Kidney, White Blood Cell, Stomach, and Liver remain the filing slate. Pill Pack is an explicit new evaluation
workstream, but it does not become a filing commitment until it demonstrates a strong independent case against
Pill, resolves its overlap with Pill Box, avoids confusion with the PillPack brand, and passes the same evidence
and recognition gates as the other proposals. No other Medical Emoji concept is in scope for this intake.

## Review order

| Order | Proposal | Baseline packet | Prior internal baseline | Why this order |
| ---: | --- | --- | ---: | --- |
| 1 | Kidney | [v1.8.0 Kidney](../../submissions/v1.8.0/kidney/) | 79/100 | Active proposal. It has the strongest current frequency package; remaining risk is concentrated in art recognition, citations, and final filing controls. |
| 2 | White Blood Cell | [v1.8.0 White Blood Cell](../../submissions/v1.8.0/white-blood-cell/) | Not yet rescored | Determine whether its cell paradigm is recognizable and independently selective before investing in the full filing packet. |
| 3 | Stomach | [v1.8.0 Stomach](../../submissions/v1.8.0/stomach/) | 77/100 | Strong semantic and silhouette case; four frequency captures must be refreshed and enlarged. |
| 4 | Liver | [v1.8.0 Liver](../../submissions/v1.8.0/liver/) | 64/100 | Requires the most work: current worldwide evidence, stronger small-size art, and better support for usage claims. |
| 5 | Pill Pack | [v1.3.0 Pill Pack](../../submissions/v1.3.0/pill-pack/) | Not yet rescored | Provisional go/no-go evaluation. The existing draft lacks compliant Trends evidence and must overcome Pill/Pill Box substitution, name confusion, and small-size recognition risk. |

The baseline scores came from the earlier readiness audit. They are not Unicode scores or approval
probabilities, and each proposal must be rescored after correction under the current proposal-level rubric.

## Fixed authorship

### White Blood Cell

Submitter and main point of contact: Shuhan He only.

### Kidney

List all authors in this order, separated by semicolons:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk.

Main point of contact: Shuhan He.

### Stomach

Submitter and main point of contact: Shuhan He only.

### Liver

Submitter and main point of contact: Shuhan He only.

### Pill Pack

Provisional submitter and main point of contact: Shuhan He only, matching the current v1.3.0 draft. Reconfirm
this before revising the proposal; do not restore names from the 2020 Emojination draft without each person's
explicit current consent.

Do not copy the Kidney author list into White Blood Cell, Stomach, Liver, or Pill Pack. Credentials and
affiliations are optional; names must match the proposal PDF and submission form exactly.

## Source and release policy

- The complete consolidated starting snapshot is [`submissions/v1.8.0/`](../../submissions/v1.8.0/). Treat it
  as immutable after commit.
- Its White Blood Cell files were copied byte for byte from `submissions/v1.3.0/`; its Kidney, Stomach, and
  Liver files were copied byte for byte from `submissions/v1.7.0/`.
- Every update creates a new complete semver folder. Copy every untouched file byte for byte into the new
  folder and change only the reviewed proposal plus package control files.
- The first substantive proposal correction will create `submissions/v1.9.0/` from v1.8.0.
- Parallel agents use the unique prerelease lanes assigned in
  [`agent-specs/README.md`](agent-specs/README.md). They do not claim canonical version numbers.
- Use `MINOR` for proposal prose, citations, evidence, artwork, generated PDF, rubric/template changes, or
  adding a pre-filing candidate. Use `PATCH` only for a non-substantive packaging or metadata correction that
  changes no claim, evidence interpretation, artwork paradigm, rights statement, or decision.
- A research note may be committed without a new submission snapshot only when it changes nothing under
  `submissions/`. Any committed change to a proposal, its evidence, artwork, PDF, or package controls requires
  a new complete semver snapshot.
- When Pill Pack reaches its turn, copy its full v1.3.0 baseline into the then-current complete package and
  revise it there. Do not edit v1.3.0 or add Pill Pack retroactively to v1.8.0.
- Keep editable Markdown, exact-size PNGs, source artwork, evidence screenshots, and the generated PDF together
  for each concept.
- Do not publish or submit a mixed packet whose source, PDF, public URL, and form answers refer to different
  revisions.
- A proposal can be corrected one at a time, but no proposal will be filed until the cross-slate consistency
  pass covers every proposal still intended for filing. If one proposal remains blocked, removing it from this
  cycle requires an explicit slate decision; it does not automatically hold the ready proposals past the
  deadline.

## One-by-one review protocol

Multiple concept agents may work at once in isolated prerelease lanes. Canonical promotion remains one by one:
finish and integrate Kidney first, then White Blood Cell, Stomach, Liver, and finally the Pill Pack go/no-go
decision if it advances.

## Agent isolation, release lock, and handoff

Each proposal agent works in a dedicated Git worktree and branch. The coordinator owns the integration branch
and the canonical package sequence.

1. Fetch the remote and start the agent branch from the coordinator's exact handoff commit, not from `master`
   and not from an older proposal branch.
2. Confirm a clean worktree and record the starting commit, highest committed submission-package version, and
   active concept before editing.
3. Read this specification, the current package manifest, the best-in-class rubric, the concept's current
   source/PDF, and every relevant prior audit.
4. Copy the entire frozen baseline package into the assigned prerelease semver folder. Verify that untouched
   files are byte-identical.
5. Change only the active concept and the new package's `VERSION`, `manifest.md`, and `CHANGELOG.md`. Update root
   release metadata when required by repository policy.
6. Rebuild only PDFs whose source or embedded assets changed. Keep all evidence, artwork sources, exact-size
   PNGs, editable proposal source, and the generated PDF together.
7. Run content, image, link, and PDF checks; render every changed PDF page and inspect it visually.
8. Commit the complete snapshot and report the commit, package version, files changed, checks run, readiness
   score, and open blockers. Do not push, publish a PDF, file the Unicode form, or merge without coordinator
   authorization.
9. The coordinator verifies each lane, then promotes accepted concept deltas into cumulative canonical packages
   in the declared order. Do not merge an agent branch wholesale into the integration branch.

Every agent may perform writable work only inside its unique prerelease folder and concept-specific branch.
Agents must not edit shared root release metadata or another lane. If two agents accidentally create the same
version folder, neither package is integrated until the collision is resolved.

### Step 1: Freeze identity, eligibility, and rights

- Record the confirmed 2026 eligibility evidence in the filing record.
- Verify the exact author list and main point of contact.
- Verify image ownership or qualifying open-license evidence.
- Confirm that the proposed concept and strongest semantic alternative have not changed.
- Confirm that no duplicate proposal is Under Consideration or Prioritization Pending.

### Step 2: Audit the proposal argument

Review the actual proposal text against the
[best-in-class specification](emoji-proposal-approval-rubric.md).

The review must answer:

1. What ordinary messages require this concept?
2. What is the nearest existing emoji or sequence, and what can it not express?
3. Does the concept represent a broad building block rather than a disease, specialty, subtype, or campaign?
4. Why is this candidate independently useful despite its nearest related concepts?
5. Which inclusion factors are genuinely supported, and which should be `N/A`?
6. Does every factual or metaphorical claim have a durable citation?
7. Would the proposal remain persuasive if all burden, awareness, prestige, and deservingness language were
   removed?

Rewrite weak sections; do not merely annotate them.

### Step 3: Audit and refresh evidence

Require readable, reproducible screenshots for:

1. Google Search with visible result count.
2. Google Video Search with visible result count.
3. Google Trends Web Search versus `elephant`, worldwide, widest range.
4. Google Trends Image Search versus `elephant`, worldwide, widest range.
5. Google Books Ngram Viewer versus `elephant`, widest range.

For each source, preserve the capture date, full query URL, location, time range, search mode, category filter,
and any ambiguity or limitation. Petitions and social-media calls for the emoji are not evidence. Cause-related
use may be described when established and cited, but cannot be the reason for encoding.

### Step 4: Audit the artwork at actual size

- Verify color and true black-and-white PNGs at exactly 18x18 and 72x72 pixels.
- Compare the 18x18 art against the nearest existing emoji and against other active proposals where visual
  confusion is plausible.
- Test unprompted recognition with reviewers who were not told the intended answer.
- Target at least 80% correct unprompted identification at 18x18, with no wrong concept dominating more than
  10% of responses. This is an internal gate, not a Unicode rule.
- If the silhouette fails, revise the art and repeat the test; do not solve recognition through explanatory
  prose.

### Step 5: Correct and rebuild the proposal

- Put title, authors, date, identification, four required images, and rights statement at the top of page 1.
- Follow the current inclusion and exclusion order.
- Use `N/A` wherever a positive factor lacks compelling evidence.
- Put the conclusion first in every factor.
- Keep screenshots readable at 100% zoom.
- Remove stale dates, placeholders, draft notes, unsupported claims, campaign history, and set-completion
  arguments.
- Generate a fresh PDF from the corrected source.

### Step 6: Render and inspect every page

- Visually inspect every rendered page, not only extracted text.
- Reject broken images, clipped text, unreadable screenshots, empty pages, stranded headings, or inconsistent
  page numbers.
- Verify PDF text extraction, fonts, links, encryption status, file size, and page count.
- Confirm that the PDF visually matches the source assets and contains the final revision date.

### Step 7: Issue a readiness decision

Create a concept-specific review report containing:

- A must-pass gate table.
- Updated 100-point internal score.
- Findings ordered by severity.
- Exact corrections made.
- Remaining blockers, if any.
- Final status from the vocabulary below.

Do not promote the next concept into a canonical package until the preceding canonical promotion is complete.

## Proposal-specific review focus

### White Blood Cell

- Preserve Shuhan He as the sole submitter and main point of contact.
- Refresh the 2020 Google Search and Video captures; replace the noncompliant Web Trends comparison and add
  Image Trends, both worldwide against `elephant`.
- Test the 18x18 color and black-and-white art against Microbe, Drop of Blood, Soap, Bubbles, and a generic
  cell. The lobed nucleus must remain visible without making the image look like a face or cartoon germ.
- Decide whether unprompted viewers recognize `white blood cell`, the broader `blood cell`, or only `cell`.
  Revise the paradigm if Microbe or generic cell dominates.
- Cite or remove claims about immunity, infection, inflammation, white-cell counts, laboratory results,
  chemotherapy monitoring, education, and research.
- Keep the concept at the broad leukocyte category. Do not imply that Unicode should add every blood cell,
  immune-cell subtype, laboratory value, or disease marker.
- Directly rebut Microbe, Drop of Blood, Test Tube, Microscope, and Shield as substitutes.
- Keep Completeness and Compatibility as `N/A`; retain Multiple meanings or sequences only where the examples
  are independently useful and not merely clinical labels.

### Kidney

- This is the active agent. Expected first release: `v1.9.0`, provided no intervening package is committed.
- Preserve the complete eight-person author list.
- Test recognition against Beans, Anatomical Heart, Lungs, Droplet, and food-like kidney shapes.
- Strengthen the explanation of the semantic gap without relying on the existence of other organ emoji.
- Verify citations for ordinary use, metaphorical meanings, donation/transplant contexts, and medical claims.
- Remove sequences that do not strengthen the organ's independent communicative case.

### Stomach

- Replace the 2020 Search, Video, Web Trends, and Image Trends captures with current reproducible evidence.
- Preserve only established meanings such as intuition, appetite, nausea, and courage when properly cited.
- Test the J-shaped silhouette against Liver, Anatomical Heart, food, and generic internal-organ shapes.
- Make the Open-ended answer explain why Stomach is independently useful, not why an anatomy set is incomplete.

### Liver

- Replace every 2020 frequency capture, especially U.S.-only Trends, with current worldwide evidence.
- Rework the 18x18 color and black-and-white silhouettes until unprompted reviewers identify Liver reliably.
- Compare against Stomach, Anatomical Heart, meat/food imagery, and generic organ shapes.
- Cite or remove medical, cultural, culinary, and metaphorical usage claims.
- Treat Multiple meanings, Completeness, and Compatibility as `N/A` unless compelling evidence survives review.

### Pill Pack

- Treat the v1.3.0 folder as historical source material, not as a filing-ready packet.
- Begin with a go/no-go memo that tests the generic name `Blister Pack` against `Pill Pack`, including the risk
  of confusion with the PillPack pharmacy brand. Do not use brand evidence as a compatibility argument.
- Reconfirm current eligibility, the public status record, duplicate-proposal status, sole authorship, artwork
  ownership, and whether Pill Box is being held or advanced. Pill Pack and Pill Box must not both be filed in
  the same intake without an explicit overlap decision.
- Build the independent-use case around sealed doses, remaining supply, dispensing, and finite medication
  courses only if evidence shows that the existing Pill emoji and ordinary sequences cannot communicate the
  same ideas clearly.
- Recapture all five required frequency sources from scratch. The archived draft is missing Web Trends, uses
  the wrong Image Trends comparator, and contains stale 2020 Search and Video evidence.
- Test color and black-and-white art at 18x18 against Pill, Pill Box, keypad, remote control, calendar grid, and
  generic packaging. Revise or stop if unprompted reviewers do not identify a blister medication pack.
- Remove burden, opioid-crisis, adherence-advocacy, and professional-importance language unless a narrowly
  relevant factual statement is durably cited and does not substitute for expected usage.
- Exit with either `ADVANCE TO FILING SLATE` and a complete corrected semver package, or `DO NOT ADVANCE` with a
  documented evidence-based reason. A no-go decision must not be disguised as a high readiness score.

## Standalone proposal agent specifications

Each file below is a complete prompt for a separate agent and may be started concurrently from the same frozen
base commit:

- [`agent-specs/kidney-agent-spec.md`](agent-specs/kidney-agent-spec.md)
- [`agent-specs/white-blood-cell-agent-spec.md`](agent-specs/white-blood-cell-agent-spec.md)
- [`agent-specs/stomach-agent-spec.md`](agent-specs/stomach-agent-spec.md)
- [`agent-specs/liver-agent-spec.md`](agent-specs/liver-agent-spec.md)
- [`agent-specs/pill-pack-agent-spec.md`](agent-specs/pill-pack-agent-spec.md)

The coordination and canonical-promotion protocol is in
[`agent-specs/README.md`](agent-specs/README.md).

## Cross-slate consistency pass

After every proposal still intended for filing completes individual review:

1. Confirm the author lists and main contact one final time.
2. Confirm that each proposal has a distinct independent-use case and no set-completion argument.
3. Compare every intended filing glyph side by side in color and black-and-white.
4. Harmonize shared terminology without duplicating unsupported claims.
5. Confirm that dates, category names, rights statements, evidence methods, and file naming are consistent.
6. Re-render and inspect every final PDF.
7. Verify that every proposal independently meets every must-pass gate.

## Status vocabulary

- `IN REVIEW`: The one-by-one audit is active.
- `REVISION REQUIRED`: The concept remains in the slate, but one or more correctable gates are open.
- `BLOCKED`: Required evidence, rights, authorship consent, or recognizability cannot currently be established.
- `READY TO PUBLISH`: The corrected source and PDF pass all content, evidence, art, and technical gates.
- `READY TO SUBMIT`: The public logged-out PDF URL, final form answers, author confirmation, and filing record are
  also complete.
- `SUBMITTED`: The form was sent and its confirmation was archived.

No score can override an unresolved must-pass gate.

## Definition of done for each proposal

A proposal is finished only when:

- It has no unresolved must-pass gate.
- It scores at least 90/100, with a project target of 100/100 before filing.
- Its author list, art rights, four exact-size images, five frequency sources, selection factors, exclusion
  factors, and citations are independently verifiable.
- Every PDF page has passed visual and technical inspection.
- The final PDF has a stable public HTTPS URL that works without login.
- The form data matches the PDF exactly.
- Shuhan He has reviewed the exact filing copy and authorized the external submission.
- The submission confirmation is archived after filing.

## Working schedule

| Target date | Deliverable |
| --- | --- |
| 2026-07-23 | Kidney corrected packet and readiness decision |
| 2026-07-25 | White Blood Cell corrected packet and readiness decision |
| 2026-07-26 | Stomach corrected packet and readiness decision |
| 2026-07-28 | Liver corrected packet and readiness decision |
| 2026-07-29 | Pill Pack go/no-go decision and, only if advanced, corrected packet |
| 2026-07-30 | Cross-slate consistency, final PDF inspection, public URLs, and final authorization |
| 2026-07-31 | Contingency only; official window closes at end of day |

## Execution ledger

- [ ] Kidney reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] White Blood Cell reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Stomach reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Liver reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Pill Pack evaluated and marked either `ADVANCE TO FILING SLATE` or `DO NOT ADVANCE`.
- [ ] Every proposal-package update has its own immutable semver snapshot and committed handoff.
- [ ] Cross-slate consistency pass complete.
- [ ] Public URLs verified without login.
- [ ] Final filing authorization recorded.
- [ ] One submission confirmation archived for every proposal actually filed.
