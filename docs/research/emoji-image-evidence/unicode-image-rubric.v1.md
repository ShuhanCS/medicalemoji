# Unicode Image Rubric for Emoji Proposal Artwork

Version: `1.0.0`  
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

Unicode does not publish a visual point score, a preferred illustration style, a required number of internal details, or a specific recognition percentage. Therefore the score below is an internal decision tool, and every threshold is explicitly labeled as operational.

## Internal scorecard (100 points after format gate)

| Dimension | Points | Evidence label | Passing evidence |
| --- | ---: | --- | --- |
| Required four-sample format | Gate | Unicode requirement | Exact 18x18 and 72x72 pixel dimensions; color plus black-and-white; no grayscale treatment. As a conservative file check, black-and-white art should use only pure black and white for opaque pixels; edge antialiasing may use transparency, not opaque gray. |
| Native-size concept recognition | 30 | Operational test of Unicode recognizability | A blinded, no-context test of at least 30 independent adult participants: at least 80% top-1 correct in color 18x18 and at least 70% in black-and-white 18x18. |
| Confusability against the nearest alternatives | 20 | Operational test of “distinctive enough” | In a forced-choice test containing Kidney, beans, stomach, ear, balloon, and drop, Kidney is selected at least 75% of the time for each 18x18 mode; no single wrong alternative exceeds 15%. |
| 72x72 visual hierarchy | 15 | Operational test | At 72x72, blinded participants identify Kidney at least 90%; visual annotation identifies one primary silhouette cue and no more than two secondary cues required for recognition. |
| Color independence | 10 | Operational test | The black-and-white version retains the same primary silhouette and key differentiator as color. It cannot require the organ's red/brown color to be understood. |
| Background and rendering resilience | 10 | Operational test | Samples remain visibly separable from both white and near-black backgrounds; no text, gradients, shadows, or thin detail is required to convey the concept. |
| Vendor flexibility | 10 | Unicode paradigm principle + operational test | The proposal names only the invariant cues. A renderer can change palette, line style, and minor anatomy while preserving recognition. |
| Evidence quality | 5 | Operational test | File checks, source vector, and a recorded blind-test protocol/results are included; assertions are not substituted for test results. |

## Interpretation

| Score | Decision |
| --- | --- |
| 90–100 | Strong visual evidence; ready to rely on in the proposal. |
| 80–89 | Promising, but close the named evidence gap before submission. |
| 70–79 | Revise or test before relying on the image argument. |
| Below 70 | The image evidence is not yet persuasive under Unicode's 18x18 recognizability standard. |

An unrun recognition or confusability test receives **0** for that dimension. This is intentionally conservative: “looks recognizable to us” is not evidence that most people recognize the intended paradigm without foreknowledge.

## What the historical corpus supports

The 10-record seed corpus is linked in `winning-image-corpus.v1.json`; all outcomes and source documents are official Unicode records. It supports only these descriptive lessons:

1. The current format is newer than several successful proposals. Heart (Organ), Lung, Beans, Treasure Chest, and Falling Debris do not visibly show the complete current four-sample layout on their first page. Historical success is not permission to omit current requirements.
2. The clearest current-format seed example is Orca (`L2/24-249`): its tiny samples preserve an instantly legible body outline and a small number of high-contrast landmark cues.
3. Successful proposals sometimes simplify deliberately. Treasure Chest states that, at small resolution, only gold coins should be used because other contents muddle. This supports reducing nonessential detail; it does not support copying any particular art style.
4. A shape-adjacent encoded emoji can be a real confound. Beans (`L2/20-226`) is therefore a mandatory forced-choice alternative for Kidney; “bean-like” is not a hypothetical objection.
5. The two direct anatomical-organ precedents use more than a generic bean outline: Heart exposes vessels/chambers and Lung exposes paired lobes/trachea. That is a useful hypothesis for Kidney, not a Unicode mandate.

## Kidney-specific test card

### Stimuli

- Color 18x18, black-and-white 18x18, color 72x72, black-and-white 72x72.
- Matching white and near-black backgrounds.
- Randomized trials using the same display scaling for every participant.

### Task 1: unprompted recognition

Show one sample for three seconds. Ask: “What does this image depict?” Score a response as correct only if it says *kidney* or an unambiguous synonym. Do not present the proposal title, description, or candidate list.

### Task 2: forced-choice confusability

Show the same sample with randomized answer order: Kidney, beans, stomach, ear, balloon, drop, other. This identifies the actual failure mode that open text answers can conceal.

### Task 3: cue audit

Ask participants who answered Kidney which feature guided them. Code responses independently as: organ/bean silhouette, hilum indentation, ureter, red-brown organ color, or other. If color or a barely visible ureter is the only cue at 18px, the black-and-white design needs revision.

### Design decision rules

- If *beans* is the main error: deepen/clarify the medial indentation and separate the ureter from the body silhouette.
- If *ear* or *balloon* is the main error: move the ureter attachment and reduce the outer ear-like rim.
- If *stomach* is the main error: make the bean-shaped renal contour and lower ureter direction clearer.
- If black-and-white fails while color passes: make the black silhouette/negative space do the identifying work before adding interior anatomy.

## Limits

This rubric is intentionally evidence-based but not falsely empirical. A 10-record visual seed set is too small to estimate a causal “winning style,” and Unicode does not publish reject/accept decisions by image quality. The database’s value is traceability, controlled comparators, and a defensible test protocol.
