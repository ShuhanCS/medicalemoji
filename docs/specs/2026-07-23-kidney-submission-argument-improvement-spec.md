# Kidney Emoji Submission Argument Improvement Specification

Status: proposed

Date: 2026-07-23

Scope: strengthen the substantive Unicode case for the Kidney proposal. This specification deliberately excludes eligibility, coordination, signing, hosting, and form-submission operations.

## Decision

The current v1.1.0 narrative is a credible, well-structured proposal, but it should not be treated as the strongest possible case yet. The next substantive packet should make one simple claim easy to accept:

> **Kidney is a durable, broadly used human concept that people cannot express precisely with existing emoji, and it can be shown clearly enough at emoji size without creating a demand for an anatomy taxonomy.**

Every major section, example, and visual should provide evidence for one part of that claim. Health advocacy and organizational support remain useful context, but must not carry the argument.

## Goals

- Make the non-clinical, everyday use case as convincing as the clinical one.
- Demonstrate recognizability at 18x18 pixels with independent, documented feedback.
- Replace assertion-heavy claims with short, directly relevant evidence.
- Make the open-ended-organ objection easier to reject in one pass.
- Show that frequency measures a usefully broad concept, not merely the occurrence of a medical term.

## Non-goals

- Do not argue that kidney deserves encoding merely because other organs are emoji.
- Do not present support letters, petitions, social posts, or disease burden as frequency evidence.
- Do not request a specific vendor rendering or make clinical-outcome claims.
- Do not make the proposal a request to complete all anatomy, all organs, or all medical emoji.

## Target Reader and Reading Order

The reader is an Emoji Standard & Research Working Group reviewer who may scan the proposal quickly and is skeptical of a specialist or advocacy-driven request.

The first two pages must answer, in this order:

1. What is being proposed?
2. Can people recognize it at normal emoji size?
3. Why is it useful outside a narrow medical setting?
4. Why do existing emoji and sequences fail?
5. Why does this not require every organ to be encoded?

## Required Argument Changes

### 1. Lead with ordinary-language utility

Replace the broad list of possible associations with four to six concrete, non-specialist message contexts. Each must show an expression that becomes materially clearer with Kidney than with available emoji.

| Context | Message the proposal should demonstrate | Existing-emoji limitation |
| --- | --- | --- |
| Body/anatomy education | `Kidney + book` for a lesson or anatomy explainer | A bean or organ-neutral symbol changes the meaning. |
| Hydration and body function | `Kidney + droplet` for kidney function or urine production | A droplet alone is ambiguous. |
| Food and shape language | Kidney bean / kidney-shaped contexts | Establishes ordinary familiarity with the term, without claiming a kidney image replaces the bean emoji. |
| Personal and family health updates | `Kidney + person/family` for a kidney-specific update | Hospital, pill, and syringe identify setting or treatment, not the subject. |
| Donation and transplant | `Kidney + person/hospital` | Existing organs are semantically wrong; generic medical sequences lack the organ reference. |

Keep clinical examples, but place them after ordinary communication. Remove any metaphor claim (for example, "filtering" or "cleansing") unless it is supported by examples a general reader will immediately recognize.

### 2. Make distinctiveness independently testable

The current paired illustration must not be defended solely through design rationale. Its 18x18 recognizability needs evidence from people who were not told the answer.

Required test:

- Recruit at least 12 people, including at least 8 non-medical participants.
- Show each participant the 18x18 color and black-and-white image at native size, in randomized order with Bean, anatomical Heart, Lungs, and Brain as comparison items.
- Ask an open question: "What does this emoji depict?"
- Record first answer, confidence (1-5), and whether the participant had healthcare training.
- Success threshold: at least 80% identify the color image as kidney or a urinary-system organ; at least 65% do so for black-and-white. Fewer than 10% may call it a bean, heart, peach, or unspecified red organ.

Artwork direction should follow the existing design specification: a single, bold kidney with a visible hilum notch and one or two chunky vessel/ureter cues. Do not retain a paired design merely because it is anatomically complete. The visual proof must determine the final paradigm.

Add one compact figure to the proposal:

- Native-size 18x18 strip: candidate Kidney, Bean, Heart, Lungs, Brain.
- One-sentence test result with sample size and identification rate.
- A caption that states the artwork is illustrative and vendors may vary it.

### 3. Tighten the frequency argument

The evidence section should distinguish term frequency from emoji need.

- Retain the five required sources and their reproducible URLs.
- Use the comparator consistently wherever current Unicode guidance requires it.
- Refresh captures close to the filing date.
- Add a two-sentence interpretation after the table: the data establishes that *kidney* is a common, durable term; the prior sections establish why the concept needs a distinct emoji rather than an existing substitute.
- Do not use raw result counts as proof of demand by themselves.

### 4. Turn the substitute table into the argument's center of gravity

The existing substitute table is good but generic. Revise it so every row follows the same test: what exact message becomes unclear, misleading, or impossible without Kidney?

| Substitute | Keep or change | Required improvement |
| --- | --- | --- |
| Bean | Keep | Lead with the food-versus-anatomy semantic conflict. |
| Droplet | Keep | Show ambiguity across water, sweat, tears, blood, and urine. |
| Hospital, pill, syringe | Consolidate | Explain that these identify place, treatment, or procedure—not the affected organ. |
| Heart, lungs, brain | Keep, shorten | State only that each represents a different organ; do not imply precedent creates entitlement. |
| Existing sequences | Add | Show two representative sequences and explain the residual ambiguity. |

The table must be concise enough that a reviewer can understand the gap without reading surrounding prose.

### 5. Make the bounded-category answer sharper

Keep the criteria-based answer, but front-load it with a plain rule:

> Kidney is not proposed as one member of an organ list. It is proposed only because it combines high term frequency, broad ordinary-language use, distinct health and body-function meaning, demonstrated visual recognizability, and a clear failure of existing substitutes.

Follow with no more than five criteria. Each criterion must point to evidence elsewhere in the proposal. Remove language that implies any future organ meeting one or two criteria is automatically entitled to encoding.

### 6. Reduce advocacy weight

Move the coalition/support-letter material to a short final appendix or a one-paragraph supplemental section. Keep it explicitly labeled as professional context, not evidence of expected usage.

The proposal should read persuasively even if every support letter is removed.

## Proposed Narrative Structure

1. Required first-page metadata and four example images.
2. Identification and image explanation.
3. A one-paragraph thesis: broad concept, clear gap, bounded case.
4. Distinctiveness: native-size comparison strip and independent recognition result.
5. Everyday and clinical communication contexts, with five concise sequences.
6. Existing-substitute failure table.
7. Frequency evidence and interpretation.
8. Inclusion and exclusion factors, including the bounded-category rule.
9. Global durability, limited to evidence that strengthens the everyday case.
10. Short supplemental coalition context.

## Acceptance Criteria

- [ ] A skeptical, non-medical reader can summarize the case in one sentence without referring to disease advocacy.
- [ ] The proposal includes independent 18x18 recognition data meeting the stated thresholds.
- [ ] Every claim about visual distinction points to the comparison/test evidence.
- [ ] Every frequency source is refreshed and accompanied by the required comparator and reproducible URL.
- [ ] The proposed image is demonstrably distinguishable from Bean at native size.
- [ ] The substitute table explains concrete communication failures, not just semantic differences.
- [ ] The open-ended response states a limited evidence-based rule and does not argue for organ-set completion.
- [ ] Support materials remain supplemental and are not cited as expected-usage evidence.
- [ ] The revised proposal can lose its health-burden paragraph without collapsing the core argument.

## Reviewer Test

Before creating the next packet, give the revised PDF to one non-medical reader and one emoji-process reviewer with no verbal introduction. Ask them to answer:

1. What does the image depict at 18x18?
2. What would people use it to communicate beyond clinical medicine?
3. Why are Bean, Droplet, and existing organ emoji insufficient?
4. Why does this not require adding every organ?

The revision passes only when both readers answer all four questions from the document itself, without prompting.

## Sequencing and Version Decision

1. Run the visual-recognition test and select a final art direction.
2. Rewrite the distinctiveness, everyday-use, substitutes, and bounded-category sections as one integrated edit.
3. Refresh frequency captures and verify current presentation requirements.
4. Assemble and test the revised PDF with the two-reader reviewer test.

This specification is a planning-only document, so it does not change the active v1.1.0 packet. Implementing its substantive narrative, artwork, or evidence changes requires a synchronized **MINOR** packet update to `v1.2.0` under the repository's packet versioning rules.
