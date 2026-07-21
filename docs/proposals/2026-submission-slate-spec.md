# 2026 Emoji Submission Slate and One-by-One Review Specification

Version: 1.0.0

Date: 2026-07-21

Deadline: End of day 2026-07-31

Official guidelines:

https://www.unicode.org/emoji/proposals.html

## Decision

Prepare exactly three emoji proposals for the 2026 intake:

1. Kidney
2. Stomach
3. Liver

Each concept will be a separate proposal PDF and a separate submission-form entry. They are not presented as
an anatomy set, and no proposal may depend on the other two for its selection case.

No other Medical Emoji concept is in scope for this intake. A concept can be added only by an explicit new
slate decision, not because related files already exist in the repository.

## Review order

| Order | Proposal | Baseline packet | Prior internal baseline | Why this order |
| ---: | --- | --- | ---: | --- |
| 1 | Kidney | [v1.7.0 Kidney](../../submissions/v1.7.0/kidney/) | 79/100 | Strongest current frequency package; remaining risk is concentrated in art recognition, citations, and final filing controls. |
| 2 | Stomach | [v1.7.0 Stomach](../../submissions/v1.7.0/stomach/) | 77/100 | Strong semantic and silhouette case; four frequency captures must be refreshed and enlarged. |
| 3 | Liver | [v1.7.0 Liver](../../submissions/v1.7.0/liver/) | 64/100 | Requires the most work: current worldwide evidence, stronger small-size art, and better support for usage claims. |

The baseline scores came from the earlier readiness audit. They are not Unicode scores or approval
probabilities, and each proposal must be rescored after correction under the current proposal-level rubric.

## Fixed authorship

### Kidney

List all authors in this order, separated by semicolons:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk.

Main point of contact: Shuhan He.

### Stomach

Submitter and main point of contact: Shuhan He only.

### Liver

Submitter and main point of contact: Shuhan He only.

Do not copy the Kidney author list into Stomach or Liver. Credentials and affiliations are optional; names must
match the proposal PDF and submission form exactly.

## Source and release policy

- Treat `submissions/v1.7.0/` as the immutable reviewed baseline.
- Build substantive corrected proposals into the next versioned packet, expected to be
  `submissions/v1.8.0/`.
- Keep editable Markdown, exact-size PNGs, source artwork, evidence screenshots, and the generated PDF together
  for each concept.
- Do not publish or submit a mixed packet whose source, PDF, public URL, and form answers refer to different
  revisions.
- A proposal can be corrected one at a time, but no proposal will be filed until the cross-slate consistency
  pass covers every proposal still intended for filing. If one proposal remains blocked, removing it from this
  cycle requires an explicit slate decision; it does not automatically hold the ready proposals past the
  deadline.

## One-by-one review protocol

Only one proposal is active at a time. Finish its review report and corrected packet before starting the next.

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
4. Why is this candidate independently selective among other organs?
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
- Compare the 18x18 art against the nearest existing emoji and against the other two proposed organs.
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

Do not begin the next concept until this report and the corrected files are complete.

## Proposal-specific review focus

### Kidney

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

## Cross-slate consistency pass

After the three individual reviews:

1. Confirm the author lists and main contact one final time.
2. Confirm that each proposal has a distinct independent-use case and no set-completion argument.
3. Compare all three 18x18 glyphs side by side in color and black-and-white.
4. Harmonize shared terminology without duplicating unsupported claims.
5. Confirm that dates, category names, rights statements, evidence methods, and file naming are consistent.
6. Re-render and inspect all three final PDFs.
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
| 2026-07-25 | Stomach corrected packet and readiness decision |
| 2026-07-28 | Liver corrected packet and readiness decision |
| 2026-07-29 | Cross-slate consistency and final PDF inspection |
| 2026-07-30 | Public URLs, final authorization, and intended filing day |
| 2026-07-31 | Contingency only; official window closes at end of day |

## Execution ledger

- [ ] Kidney reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Stomach reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Liver reviewed, corrected, and marked `READY TO PUBLISH`.
- [ ] Cross-slate consistency pass complete.
- [ ] Public URLs verified without login.
- [ ] Final filing authorization recorded.
- [ ] Three submission confirmations archived.
