# White Blood Cell final-submission improvement specification

Date: 2026-07-26

Status: **APPROVED FOR IMPLEMENTATION**

Target intake deadline: 2026-07-31, end of day

## Fixed decisions

- White Blood Cell is approved for the 2026 filing slate.
- Shuhan He is the sole submitter and main point of contact.
- Eligibility is confirmed.
- Permission to publish and submit is confirmed.
- Shuhan He confirms that he owns or controls the proposed image rights and can make Unicode's required
  warranty and license grant.
- The deliverable is a persuasive final submission, not an internal audit or readiness argument.
- The final PDF will present the strongest accurate case for approval and will not contain internal scores,
  process commentary, abandoned alternatives, or debate about whether to file.

## Outcome

Create and submit a best-in-class White Blood Cell proposal that:

1. establishes a useful semantic building block not expressed by Microbe, Drop of Blood, or a reasonable
   existing sequence;
2. demonstrates strong worldwide, durable expected usage with the five required sources;
3. presents a recognizable White Blood Cell paradigm at actual 18x18 size in color and black-and-white;
4. follows the current Unicode format and the repository's `PROPOSAL-GUIDE.md`;
5. gives reviewers a concise affirmative case with readable evidence and direct exclusion rebuttals; and
6. ships as an immutable, reproducible, publicly accessible PDF with a matching filing record.

Controlling project guide:

`PROPOSAL-GUIDE.md`, version 1.0.1

Controlling external guidance:

https://www.unicode.org/emoji/proposals.html

## Proposal position

### Paradigm

A White Blood Cell emoji represents the broad human leukocyte category: a circulating immune-system cell,
rather than a particular subtype, disease, test result, or pathogen.

### Essential visual cues

1. A compact, softly irregular cell body.
2. One bold connected multi-lobed nucleus.
3. Clear negative space separating the nucleus from the cell boundary.

Color, shading, precise membrane detail, and viewing angle are vendor freedoms. The broad cell body and
connected lobed-nucleus cue carry the identity.

### Semantic gap

Microbe represents germs and microorganisms. Drop of Blood represents blood as a fluid. Neither individually
nor in a short sequence clearly expresses a human white blood cell, immune cell, or white-cell count. White
Blood Cell therefore adds a distinct medical, scientific, educational, and everyday health-communication
building block.

### Required factor posture

- `Multiple meanings`: `N/A`.
- `Use in sequences`: cite concise examples such as immune response and high/low white-cell count.
- `Breaks new ground`: **Yes** — it adds a human immune-cell concept absent from the current emoji vocabulary.
- `Distinctiveness`: demonstrate recognition through actual-size artwork, comparison boards, computer checks,
  and unprompted human results.
- `Usage level`: lead with the five required reproducible sources and numerical observations.
- `Completeness`: `N/A`; White Blood Cell stands independently and does not request every blood component or
  immune-cell subtype.
- `Compatibility`: `N/A`.
- `Already represented`: explain the semantic difference from Microbe, Drop of Blood, and their plausible
  sequences.
- `Overly specific`: define White Blood Cell as the broad leukocyte category.
- `Open-ended`: establish its independent ordinary use and bounded category-level meaning.
- `Transient`: demonstrate durable use over time through current search evidence and Ngram history.
- `Faulty comparison`: rest the case on White Blood Cell's own utility, usage, and recognition.

## Improvement 1: strengthen the 18-pixel image paradigm

Create a dedicated small-size design whose identity survives without color or fine detail.

### Design work

1. Produce at least three silhouette families rather than palette variations of one illustration.
2. Draw dedicated 18x18 color and black-and-white masters.
3. Simplify the outer membrane into a coherent irregular boundary without face-like peripheral marks.
4. Make the connected multi-lobed nucleus bold enough to remain legible at actual size.
5. Design black-and-white independently so outline and negative space carry the paradigm.
6. Keep the art broad enough to represent all white blood cells while using the lobed nucleus as an iconic
   recognition cue.
7. Inspect candidates on light and dark backgrounds at 100% scale.
8. Compare candidates against the declared confuser set:
   - Microbe;
   - Drop of Blood;
   - Bubbles;
   - Soap;
   - a generic cell.

### Final art artifacts

- editable color SVG source;
- editable black-and-white SVG source;
- exact 18x18 color PNG;
- exact 72x72 color PNG;
- exact 18x18 true black-and-white PNG;
- exact 72x72 true black-and-white PNG;
- actual-size color comparison board;
- actual-size black-and-white comparison board.

### Computer validation

Generate reproducible validation output covering:

- exact pixel dimensions;
- color and true two-color black-and-white palettes;
- transparency and background behavior;
- connected components and negative space;
- source and export hashes;
- reproducible export commands;
- technical separation from declared confusers.

Store the results as:

- `validation/computer-validation.json`;
- `validation/computer-validation.md`;
- a committed export and validation script.

Technical metrics support the art record; human recognition establishes semantic clarity.

## Improvement 2: complete unprompted recognition evidence

Use the repository's current recognition standard.

1. Recruit at least 12 adults who have not seen the proposal or intended name.
2. Show the color and black-and-white 18x18 images at actual size on a neutral background in separately
   randomized passes.
3. Ask `What is this?` and record the first free-text answer verbatim before showing choices.
4. Follow with a forced-choice comparison using White Blood Cell, Microbe, Drop of Blood, generic cell, and
   unrelated controls.
5. Count `white blood cell`, `WBC`, `leukocyte`, or a named white-cell subtype as exact recognition.
6. Archive the prompt, presentation method, participant count, raw responses, coding decisions, and results.
7. Iterate the artwork with fresh participants until both palettes reach at least 10 of 12 exact-recognition
   responses and no alternative concept dominates.

The raw free-response record remains the primary recognition result; forced choice supplies confuser detail.

## Improvement 3: capture the complete frequency set

Capture all five sources in a clean private browser session and make every screenshot readable at 100% PDF
zoom.

| Source | Required configuration |
| --- | --- |
| Google Search | `white-blood-cell`; Tools open; visible result count; personalization minimized |
| Google Video Search | `white-blood-cell`; visible result count; personalization minimized |
| Google Trends Web Search | `white blood cell` versus `elephant`; Worldwide; all categories; widest range |
| Google Trends Image Search | Same terms; Worldwide; all categories; widest range; Image Search selected |
| Google Books Ngram | `white blood cell` versus `elephant`; widest supported range; corpus and smoothing recorded |

For every capture, record:

- full reproducible URL;
- capture date;
- query and grouping;
- location;
- time range;
- search mode and category;
- visible result count or plotted values; and
- a concise interpretation.

Use a manual clean browser session for Google pages that challenge automated traffic. Preserve the required
screenshots and the machine-readable Ngram response. The proposal should state the numerical evidence directly
and use medical or scientific sources only to establish ordinary communication contexts, not as substitutes
for frequency.

## Improvement 4: write the affirmative final proposal

Use the current template and put the conclusion first in every factor.

### Page 1

Include at the top:

1. `Proposal for Emoji: White Blood Cell`;
2. submitter and main contact: Shuhan He;
3. current revision date;
4. search-oriented keywords and proposed category;
5. all four exact-size images; and
6. a direct rights statement confirming that Shuhan He owns or controls the artwork rights, releases the
   images under CC0 1.0, and agrees to Unicode's proposal license.

### Body

- Define the semantic gap before discussing background.
- State `Breaks new ground: Yes` immediately.
- Use the recognition results and actual-size comparison boards to establish distinctiveness.
- Present all five frequency sources with readable screenshots and concise numerical interpretation.
- Keep Multiple meanings, Completeness, and Compatibility as direct `N/A` answers.
- Use the strongest two or three ordinary communication contexts, supported by durable citations.
- Answer each exclusion as a short rebuttal and close it cleanly.
- Keep design guidance focused on the essential cues and vendor freedoms.
- Cite every material factual claim.

### Final advocate edit

Every sentence in the submission must do at least one of these jobs:

- satisfy a current Unicode requirement;
- establish expected use;
- establish visual recognition;
- prove the independent semantic gap;
- answer a required exclusion; or
- guide vendor rendering.

The final PDF contains only the approved proposition, final artwork, reproducible evidence, supported claims,
and concise required rebuttals. Internal review material remains outside the submission.

## Improvement 5: build the canonical `v1.11.0` package

The current `v1.9.0-white-blood-cell.1` audit remains immutable. Build the final package from a fresh copy of
canonical `v1.10.0` so Kidney's promoted work is preserved.

1. Copy the complete canonical `submissions/v1.10.0/` packet to `submissions/v1.11.0/`.
2. Apply only the approved White Blood Cell source, art, evidence, validation, and PDF changes.
3. Update `VERSION`, manifest, package changelog, proposal date, and file-role labels.
4. Name the proposal source and PDF `white-blood-cell_emoji_proposal_SUBMIT`.
5. Keep all untouched Kidney, Stomach, and Liver files byte-identical to `v1.10.0`.
6. Record the source commit and SHA-256 hash of the final PDF.

## Improvement 6: final QA, publication, and submission

### Content and technical QA

- Validate every local reference and external URL.
- Confirm source, assets, PDF, manifest, and form data use the same name, date, authorship, rights statement,
  and version.
- Verify page count, file size, encryption status, text extraction, embedded fonts, hyperlink annotations, and
  exact image dimensions.
- Render and inspect every page at 100% and 144 DPI for evidence readability, clipping, overlap, blank pages,
  broken images, page breaks, and visual hierarchy.
- Search source and extracted PDF text for internal review language and remove it.
- Run `git diff --check` and all validation commands associated with changed scripts.

### Final review

1. Obtain factual/domain review of terminology, immune-cell statements, and white-cell-count contexts.
2. Obtain Unicode-process review of format, factors, evidence, rights language, and exclusions.
3. Apply review corrections, rebuild, rerun QA, and record signoff on the exact final PDF.

### Publish and file

1. Publish the exact final PDF at a stable public HTTPS URL.
2. Verify access in a logged-out browser and confirm that the downloaded hash matches the reviewed PDF.
3. Prepare the official form so its submitter, proposal name, date, rights answers, and URL match the PDF.
4. Recheck the public Unicode status sheet immediately before submission.
5. Submit through the official form and archive the confirmation.

Official form:

https://forms.gle/6KSiYHrUdBkTMNaB8

## Execution schedule

| Target | Deliverable |
| --- | --- |
| 2026-07-26 | Three 18-pixel art families and manual evidence session |
| 2026-07-27 | Selected art, complete computer validation, and five-source evidence set |
| 2026-07-28 | Human recognition results and final art exports |
| 2026-07-29 | Affirmative proposal source and fully rendered `v1.11.0` PDF |
| 2026-07-30 | Factual and Unicode-process review, final QA, and public PDF |
| 2026-07-31 | Status recheck, form submission, and confirmation archive |

## Definition of done

- [ ] White Blood Cell's semantic gap is stated clearly and affirmatively.
- [ ] The rights statement reflects Shuhan He's confirmed ownership or control and required license grant.
- [ ] All five current frequency captures are readable, reproducible, and interpreted.
- [ ] Four exact-size images and editable sources pass reproducible computer validation.
- [ ] Both 18x18 variants pass unprompted general-viewer recognition.
- [ ] Every material factual claim has a durable citation.
- [ ] The proposal follows the current field and factor order.
- [ ] The final advocate edit leaves only reviewer-facing submission content.
- [ ] The exact PDF passes page-by-page visual and technical QA.
- [ ] Factual/domain and Unicode-process reviewers approve the exact PDF.
- [ ] The exact PDF is public and accessible without login.
- [ ] The form matches the PDF and the submission confirmation is archived.

## Semantic version decision

This specification adds the substantive execution contract for the approved White Blood Cell submission but
does not edit proposal content. Advance the project version from `0.40.1` to `0.41.0`. Keep the current
canonical proposal release at `v1.10.0`; implementation will create canonical `v1.11.0`.
