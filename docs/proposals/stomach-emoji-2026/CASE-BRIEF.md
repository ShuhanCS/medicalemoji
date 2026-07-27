# Stomach Case Brief

Version: 1.1.0

Assessment date: 2026-07-26

## Current frozen candidate

| Field | Frozen value |
| --- | --- |
| Package | `1.12.0-candidate.6` |
| Candidate commit | `59f69c41ef459146f37cd6011c4eb5cb798f3354` |
| Proposal source | `candidate-v1.12/stomach_emoji_proposal_CANDIDATE.md`; SHA-256 `5e717999cdd67ac1b455400bbfa8b6f73e288c1540d735cb003893df958cb3ce` |
| Reviewer PDF | `candidate-v1.12/stomach_emoji_proposal_CANDIDATE.pdf`; SHA-256 `f32647253183b935fcd11ad2ee23903714f6241be977262daab08642d2ebf9f4` |
| Official guidance | Checked 2026-07-26: https://www.unicode.org/emoji/proposals.html |
| Eligibility and prior status | Eligibility is a settled project input from Shuhan He dated 2026-07-26. Unicode's request/status checks remain the filing control; the proposal does not narrate an eligibility dispute. |
| Authorship | The ordered byline is Shuhan He, MD; David Rhew, MD; Heena Purohit. Shuhan He is the main point of contact. The source is Shuhan He's 2026-07-26 direction in `source-ledger-v1.12.md`; separate written consent records for David Rhew and Heena Purohit are not yet archived. |
| Image rights | Shuhan He's 2026-07-26 confirmation, project-authored SVG geometry, the PDF page-1 certification, and `submissions/v1.11.0/ARTWORK-LICENSE.md` cover the exact candidate assets. |

### Exact artwork

| Asset | SHA-256 |
| --- | --- |
| `images/stomach_color_18x18_SUBMIT.png` | `93f3a656314c6743cabdff594ba062e7e74c2caaa60942689d4f118ea2608cff` |
| `images/stomach_bw_18x18_SUBMIT.png` | `6f4bbcdc3200b9841b597a11ee96132d382f48b7e6bc085e5089ca658dca3235` |
| `images/stomach_color_72x72_SUBMIT.png` | `9dc9a13200e7e6b53f3006f0c2ea6b528161ea24543f54223744eb43fff6762c` |
| `images/stomach_bw_72x72_SUBMIT.png` | `1b93265a60651fb4a199470b9ba3492edc6f29a8bb6cff3c8b6fb84c49ffb20a` |

### Prior decisions and open records

- Eligibility and image rights are settled project inputs.
- Candidate.4 was the case-building baseline and resolved the prior panel's prose actions: it tightened the
  three sequence examples, directly answered the strongest short substitutes, replaced Compatibility jargon,
  and applied a concrete Open-ended boundary.
- The exact-asset decision, David Rhew and Heena Purohit consent records, immutable promotion, public URL, and
  Shuhan's filing authorization remain outside the proposal's substantive case and are not yet complete.
- The five frequency captures are current as of 2026-07-26 and do not require recapture unless the artifact or
  filing date changes enough to make them stale.

### Relevant accepted-proposal lessons

- Lighthouse: keep the first page complete, follow the current factor order, answer genuine `N/A` factors
  directly, and present all required frequency evidence.
  https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf
- Treasure Chest: distinguish a small set of established meanings instead of listing imaginable settings.
  https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf
- Fingerprint: make the nearest-substitute answer fair and keep evidence reproducible.
  https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf
- Orca: concede factors that do not carry the case instead of stretching them.
  https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf

## Selection thesis

Stomach supplies a literal organ and digestion symbol plus appetite, fullness, and tolerance meanings that
Nauseated Face, meal emoji, and Butterfly/Anxious Face combinations cover only in pieces. Its J-shaped organ is
the reusable residual unit.

## Observed communication

| Observed phrase or use | Meaning | Nearest substitute and remaining gap | Source |
| --- | --- | --- | --- |
| The stomach receives food, mixes it with digestive juices, and passes its contents onward. | The literal organ and digestion. | Food emoji show what is eaten; they do not identify the organ doing the digestive work. | NIDDK, https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works |
| Dictionary senses and examples connect `stomach` with appetite and the familiar statement that a stomach is full. | Appetite and fullness after eating. | Fork and Knife can mean a meal or restaurant; it does not say that the stomach is hungry or full. | Merriam-Webster, https://www.merriam-webster.com/dictionary/stomach |
| `Upset stomach` describes feeling ill, especially after eating or drinking. | Stomach discomfort and nausea. | Nauseated Face plus Fork and Knife can suggest sickness after eating, but it does not identify the affected organ. | Cambridge Dictionary, https://dictionary.cambridge.org/us/dictionary/english/upset |
| `Butterflies in your stomach` is an established expression for nervousness or fear. | Nervous anticipation. | Butterfly plus an anxious face can suggest nervousness, but it does not directly render the established stomach expression. | Cambridge Dictionary, https://dictionary.cambridge.org/us/dictionary/english/butterflies-in-stomach |
| The verb `stomach` means to tolerate or bear something unpleasant. | Acceptance, tolerance, or disgust, as in being unable to stomach something. | Nauseated Face can show disgust or illness but cannot carry the verb's tolerance meaning. | Merriam-Webster, https://www.merriam-webster.com/dictionary/stomach |

## Nearest-substitute analysis

Nauseated Face shows nausea or disgust and, with Fork and Knife, sickness after eating. Butterfly plus an anxious
face covers nervous anticipation. Food emoji show a meal. These substitutes receive their strongest readings,
but none identifies the stomach or digestion, conveys fullness in the stomach, or carries the verb `stomach`
meaning to tolerate something. The residual gap remains large enough to support the case.

## Priority and scope

Gut/intestine is the strongest neighboring concept. Merriam-Webster records `gut` as the whole digestive tract or
part of it, the belly, courage, or intuition rather than one organ. A single intestine glyph would not map cleanly
to that range. Stomach maps directly to one recognizable organ and its documented appetite, fullness, verb, and
butterflies meanings. This does not claim intestine can never qualify independently; it shows why encoding
Stomach creates no matching need for intestine, liver, kidney, or an anatomy set. Anatomy or clinical importance
alone would fail this boundary.

## Positive-factor inventory

| Factor | Classification | Reason |
| --- | --- | --- |
| Multiple meanings | `SUPPORTED` | Dictionary records cover the literal organ, body area, appetite, verb sense, and butterflies expression. |
| Use in sequences | `LIMITED` | Three short combinations are legible and use supported meanings, but no claim is made that the combinations are already conventional. |
| Breaks new ground | `SUPPORTED` | No existing emoji or short sequence identifies the organ while also carrying its digestive and figurative meanings. |
| Distinctiveness | `SUPPORTED` | The J shape, inlet, inner curve, broad body, and outlet survive in the exact 18x18 and 72x72 assets and separate from the declared confusers. |
| Expected usage | `SUPPORTED` | All five required captures are present; worldwide Web and Image Trends and English Books compare with `elephant` over the widest ranges. |
| Completeness | `N/A` | Stomach does not complete a recognized closed set. |
| Compatibility | `N/A` | No popular legacy system using this same pictograph is claimed. |

## Strongest decline case

Nauseated Face plus Fork and Knife already covers sickness after eating, food emoji cover meals and hunger, and
Butterfly plus an anxious face covers nervous anticipation. A reviewer could decide that the remaining literal
organ and digestion meanings do not justify a permanent character within an open-ended anatomy class. Evidence
that an existing sequence is conventionally understood as the stomach itself would strengthen that objection.
The current rebuttal is the combination of a missing literal organ, established appetite and tolerance senses,
the butterflies expression, complete required frequency evidence, and a boundary that anatomy alone does not
qualify a neighbor.

## Visual identity

The essential cues are the J-shaped outline, long upper inlet, open inner curve, broad lower body, and short
outlet. The nearest visual confusers are Beans, Anatomical Heart, Meat on Bone, Kidney, Liver, and a generic organ
shape. The exact assets pass the project's dimension, palette, connected-shape, and silhouette-separation checks.
The dated exact-asset decision remains an open project record and is not claimed in the proposal.

## Case gate

| Test | Result | Reason |
| --- | --- | --- |
| Name-swap | `PASS` | The appetite and tolerance senses, butterflies expression, J shape, and digestive-organ gap do not transfer to another organ. |
| Real-message | `PASS` | Each central use maps to a dictionary record, NIDDK description, or required frequency exhibit. |
| Evidence-fit | `PASS` | Dictionaries support meanings, NIDDK supports digestive function, frequency captures support term frequency, and visual checks support only visual claims. |
| Substitute | `PASS` | Nauseated Face plus Fork and Knife receives its strongest fair reading before the residual gap is stated. |
| Priority | `PASS` | The boundary requires everyday and figurative meanings; anatomy or medical importance alone is insufficient. |
| Specificity | `PASS` | The thesis and central uses contain Stomach-specific phrases, verb senses, digestive function, and visual cues. |
| Cause | `PASS` | The case contains no burden, awareness, petition, campaign, or organizational-prestige argument. |
| Concession | `PASS` | Completeness and Compatibility are `N/A`; sequence utility is treated as secondary rather than inflated. |
| Objection | `PASS` | The strongest substitution and open-ended anatomy objections are stated directly. |

Case result: **CASE READY**

## Adversarial draft review

Candidate.4 passed the name-swap, substitute, scope, repetition, and process-language checks. Two passages still
use abstract lists that are weaker than the sourced Stomach case: Expected usage includes `medication`,
`education`, and `figurative emotion`, while Overly specific includes `sensation`, `emotion`, `education`,
`nutrition`, and `health`. Replace them with the sourced meanings in this brief. Also make Completeness and
Faulty comparison perform only their assigned jobs.

Draft result before those edits: **REVISION REQUIRED**

## Candidate.5 post-revision result

| Field | Value |
| --- | --- |
| Package | `1.12.0-candidate.5` |
| Proposal source SHA-256 | `d2679d0dd35c56ffef991f6ff9156ba6dd398a86ddffeff8a723042ef60a47f5` |
| Reviewer PDF SHA-256 | `c442a3491fff8544e298a11f79d8234b0e01c76a51bcd0e1f958ad9f8c7da0c5` |
| PDF artifact review | Pass: 5 US-Letter pages, 5,530 extracted characters, 16 links, no blank or clipped page, and all five evidence exhibits readable at normal zoom. |
| Artwork | Unchanged from the frozen candidate.4 hashes; deterministic validation still passes. |

The abstract usage lists were replaced with sourced appetite, fullness, upset-stomach, digestion, nervousness,
and tolerance meanings. Each sequence now has one reading. Completeness states only that no closed set is being
completed, and Faulty comparison distinguishes the required `elephant` control from organ precedents.

Post-revision result: **DRAFT READY FOR COMPLIANCE**

Candidate.5 panel result: **REVISE AND RERUN**. The skeptical seat required fuller substitute concessions and a
direct stress test against gut/intestine; those actions are implemented in candidate.6.

## Candidate.6 action response

| Field | Value |
| --- | --- |
| Package | `1.12.0-candidate.6` |
| Proposal source SHA-256 | `5e717999cdd67ac1b455400bbfa8b6f73e288c1540d735cb003893df958cb3ce` |
| Reviewer PDF SHA-256 | `f32647253183b935fcd11ad2ee23903714f6241be977262daab08642d2ebf9f4` |
| PDF artifact review | Pass: 5 US-Letter pages, 5,472 extracted characters, 17 links, no blank or clipped page, and all five evidence exhibits readable at normal zoom. |
| Artwork | Unchanged from the frozen hashes; deterministic validation still passes. |

- `C5-003 ACCEPT`: Breaks new ground and Already represented now grant Nauseated Face, meal, disgust, and
  Butterfly/Anxious Face uses before stating the literal-organ, digestion, fullness, and verb residual.
- `C5-004 ACCEPT`: Open-ended now applies the boundary to gut/intestine using the documented mismatch between
  the broad word `gut` and a single intestine glyph. It does not claim that intestine can never qualify.
- `C5-001`, `C5-002`, and `C5-005` remain external record or filing actions and are not represented as closed.

Candidate.6 result: **DRAFT READY FOR COMPLIANCE** and **READY FOR PANEL**.
