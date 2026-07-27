# Unicode Image Rubric for Emoji Proposal Artwork

Version: `1.1.1`
Date: 2026-07-23

## Evidence labels

| Label | Meaning |
| --- | --- |
| **Unicode requirement** | Directly required or defined by Unicode's current proposal guidance. Failure makes a submission incomplete or fails the stated image expectation. |
| **Operational test** | A reproducible Medical Emoji decision rule that makes a Unicode concept measurable. It is not an official Unicode numeric threshold. |
| **Historical observation** | A pattern or lesson from the successful-proposal corpus. It is descriptive, not evidence of causation. |

## The controlling Unicode standard

Unicode requires four example images at the top of the proposal: color and black-and-white at both **18x18** and **72x72** pixels. Grayscale is not acceptable. The supplied examples are paradigms, not exact production artwork. Unicode defines “recognizable” as most people being able to discern the intended particular entity **without foreknowledge**, and says the 18x18 sample demonstrates recognition at typical mobile emoji size.

Primary source: https://www.unicode.org/emoji/proposals.html

Unicode does not publish a visual point score, a preferred illustration style, a required number of internal details, or a specific recognition percentage. Therefore the score below is an internal decision tool, and every threshold is explicitly labeled as operational. Optional participant tests strengthen internal evidence but are not Unicode filing conditions.

## Internal scorecard (100 points after format gate)

| Dimension | Points | Evidence label | Passing evidence |
| --- | ---: | --- | --- |
| Required four-sample format | Gate | Unicode requirement | Exact 18x18 and 72x72 pixel dimensions; color plus black-and-white; no grayscale treatment. As a conservative file check, black-and-white art should use only pure black and white for opaque pixels; edge antialiasing may use transparency, not opaque gray. |
| Native-size concept recognition | 30 | Optional operational test of Unicode recognizability | A blinded, no-context test of at least 30 independent adult participants: at least 80% top-1 correct in color 18x18 and at least 70% in black-and-white 18x18. |
| Confusability against the nearest alternatives | 20 | Operational test of “distinctive enough” | In a forced-choice test containing the candidate and its five most plausible alternatives, the candidate is selected at least 75% of the time for each 18x18 mode; no single wrong alternative exceeds 15%. |
| 72x72 visual hierarchy | 15 | Optional operational test | At 72x72, blinded participants identify the candidate at least 90%; visual annotation identifies one primary silhouette cue and no more than two secondary cues required for recognition. |
| Color independence | 10 | Operational test | The black-and-white version retains the same primary silhouette and key differentiator as color. It cannot require a candidate-specific color association to be understood. |
| Background and rendering resilience | 10 | Operational test | Samples remain visibly separable from both white and near-black backgrounds; no text, gradients, shadows, or thin detail is required to convey the concept. |
| Vendor flexibility | 10 | Unicode paradigm principle + operational test | The proposal names only the invariant cues. A renderer can change palette, line style, and minor anatomy while preserving recognition. |
| Evidence quality | 5 | Operational test | File checks and source vector are included; where a recognition study is run, its protocol/results are recorded and assertions are not substituted for test results. |

## Interpretation

| Score | Decision |
| --- | --- |
| 90–100 | Strong visual evidence; ready to rely on in the proposal. |
| 80–89 | Promising, but close the named evidence gap before submission. |
| 70–79 | Revise or test before relying on the image argument. |
| Below 70 | The image evidence is not yet persuasive under Unicode's 18x18 recognizability standard. |

An unrun recognition or confusability test receives **0** for that optional internal-score dimension. This is intentionally conservative: “looks recognizable to us” is not evidence that most people recognize the intended paradigm without foreknowledge. An unrun optional test does not make an otherwise compliant Unicode packet ineligible or create a filing hold; it simply cannot be cited as evidence.

## What the historical corpus supports

The 10-record seed corpus is linked in `unicode-winning-image-corpus.v1.json`; all outcomes and source documents are official Unicode records. It supports only these descriptive lessons:

1. The current format is newer than several successful proposals. Heart (Organ), Lung, Beans, Treasure Chest, and Falling Debris do not visibly show the complete current four-sample layout on their first page. Historical success is not permission to omit current requirements.
2. The clearest current-format seed example is Orca (`L2/24-249`): its tiny samples preserve an instantly legible body outline and a small number of high-contrast landmark cues.
3. Successful proposals sometimes simplify deliberately. Treasure Chest states that, at small resolution, only gold coins should be used because other contents muddle. This supports reducing nonessential detail; it does not support copying any particular art style.
4. A shape-adjacent encoded emoji can be a real confound. Any candidate sharing a compact bean-like silhouette, for example, should include Beans (`L2/20-226`) in its forced-choice alternatives rather than treating that confusion as hypothetical.
5. The direct anatomical-organ precedents use more than a generic outline: Heart exposes vessels/chambers and Lung exposes paired lobes/trachea. For an organ candidate, that supports testing whether one structural landmark improves recognition; it is not a Unicode mandate.

## Reusable candidate test card

### Stimuli

- Candidate color 18x18, black-and-white 18x18, color 72x72, black-and-white 72x72.
- Matching white and near-black backgrounds.
- Randomized trials using the same display scaling for every participant.

### Task 1: unprompted recognition

Show one sample for three seconds. Ask: “What does this image depict?” Score a response as correct only if it names the candidate or an unambiguous synonym. Do not present the proposal title, description, or candidate list.

### Task 2: forced-choice confusability

Before testing, select the five most plausible alternatives from the historical corpus, existing emoji, and pilot open-text responses. Show the same sample with randomized answer order: Candidate, Alternative 1, Alternative 2, Alternative 3, Alternative 4, Alternative 5, Other. This identifies the actual failure mode that open text answers can conceal.

### Task 3: cue audit

Before testing, prepare a candidate-specific cue inventory with one primary silhouette cue and up to two secondary cues. Ask participants who answered correctly which feature guided them. Code responses against that inventory and `other`. If a color-only or barely visible secondary cue is the only cue at 18px, the black-and-white design needs revision.

### Design decision rules

- If one alternative is the main error: identify the shared visual feature, then strengthen the candidate's invariant cue rather than adding decorative detail.
- If several alternatives are selected: simplify the 18px design to one primary silhouette and one high-contrast differentiator.
- If black-and-white fails while color passes: make the black silhouette/negative space do the identifying work before adding interior detail.
- If 72px succeeds but 18px fails: redraw the 18px sample as native pixel-aware art rather than mechanically reducing the 72px illustration.

## Limits

This rubric is intentionally evidence-based but not falsely empirical. A 10-record visual seed set is too small to estimate a causal “winning style,” and Unicode does not publish reject/accept decisions by image quality. The database’s value is traceability, controlled comparators, and a defensible test protocol.
