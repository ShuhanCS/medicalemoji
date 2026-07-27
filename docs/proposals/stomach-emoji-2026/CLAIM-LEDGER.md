# Stomach Claim Ledger

Version: 1.3.0

Review date: 2026-07-26

This ledger maps material claims to what their sources actually support. Analytical conclusions are marked as
such and must remain traceable to the cited observations rather than presented as external facts.

## Authorship, eligibility, and rights

| Claim | Source | What the source supports | Proposal use |
| --- | --- | --- | --- |
| Stomach is eligible in the current cycle. | Shuhan He confirmation, 2026-07-26; `source-ledger-v1.12.md` | Internal eligibility decision. | Internal gate only; do not narrate the dispute in the PDF. |
| The submitters are Shuhan He, MD; David Rhew, MD; Heena Purohit, with Shuhan as main contact. | Shuhan He direction, 2026-07-26; `source-ledger-v1.12.md` | Ordered byline and contact. It does not substitute for separately archived coauthor consent. | PDF page 1. |
| Shuhan owns the exact proposal artwork and releases it under CC0. | Shuhan He confirmation; project SVG sources; `submissions/v1.11.0/ARTWORK-LICENSE.md`; exact hashes in `CASE-BRIEF.md` | Ownership and licensing of the exact four candidate assets. | PDF page-1 certification. |
| The current format, evidence, images, and factor order are required. | Unicode Emoji Proposal Guidelines, https://www.unicode.org/emoji/proposals.html | Current official submission requirements and selection factors. | Proposal structure and internal QA. |

## Meanings and observed communication

| Claim | Source | What the source supports | Proposal use |
| --- | --- | --- | --- |
| Stomach names the digestive organ and the surrounding body area. | Merriam-Webster, https://www.merriam-webster.com/dictionary/stomach | Literal anatomical and body-area senses. | Multiple meanings; Overly specific. |
| The stomach receives food, mixes it with digestive juices, and moves the contents onward. | NIDDK, https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works | Basic digestive function. | Breaks new ground and the interpretation of Stomach + Fork and Knife. |
| `Stomach` can mean appetite, and ordinary examples include a full stomach. | Merriam-Webster, https://www.merriam-webster.com/dictionary/stomach | Appetite sense and fullness usage. | Multiple meanings; Expected usage; sequences. |
| `Upset stomach` means feeling ill, especially after eating or drinking. | Cambridge Dictionary, https://dictionary.cambridge.org/us/dictionary/english/upset | Established everyday illness phrase. | Expected usage; Stomach + Nauseated Face; substitute analysis. |
| `Butterflies in your stomach` means nervousness or fear. | Cambridge Dictionary, https://dictionary.cambridge.org/us/dictionary/english/butterflies-in-stomach | Established figurative expression. | Multiple meanings; Stomach + Butterfly; Transient. |
| The verb `stomach` means tolerate or bear something unpleasant. | Merriam-Webster, https://www.merriam-webster.com/dictionary/stomach | Established verb sense. | Multiple meanings; Already represented; Open-ended; Transient. |
| A strong stomach and being unable to stomach something are established uses. | Cambridge Dictionary, https://dictionary.cambridge.org/us/dictionary/english/stomach | Established literal/figurative wording. | Multiple meanings and Open-ended. |

## Selection analysis

| Claim | Source | What the source supports | Proposal use |
| --- | --- | --- | --- |
| Nauseated Face plus Fork and Knife can suggest sickness after eating. | Compositional analysis of existing emoji meanings, checked against the Cambridge `upset stomach` use | A fair reading of the strongest short substitute; not evidence of a conventional sequence. | Already represented. |
| Nauseated Face plus Pill can suggest treatment. | Compositional analysis of existing emoji meanings | A fair secondary substitute; not an established sequence claim. | Already represented only. |
| The substitutes cover individual situations but do not provide a common Stomach anchor for digestion, fullness, butterflies, and tolerance. | Comparison of the cited Stomach meanings with the semantic content of the existing emoji | Analytical residual-gap conclusion. | Breaks new ground; Already represented. |
| Stomach does not imply an open-ended anatomy set. | Candidate-specific priority analysis based on the cited meanings and visible J-shaped form | The limiting principle is one recognizable organ connecting literal digestion with established appetite, fullness, tolerance, and nervous-anticipation meanings. | Open-ended. |
| `Gut` does not map cleanly to a single intestine glyph. | Merriam-Webster, https://www.merriam-webster.com/dictionary/gut | `Gut` may mean the digestive tract or part of it, belly, courage, or intuition. | Internal stress test only; Candidate.8 preserves the positive boundary and does not introduce gut or intestine in the reviewer-facing Open-ended answer. |
| Stomach is broader than a disease or procedure. | Merriam-Webster senses cover organ, body area, appetite, and verb; Cambridge covers everyday expressions | A durable category boundary rather than a list of possible medical uses. | Overly specific. |
| Completeness is not part of the case. | Review of the current Unicode emoji categories and candidate rationale | No recognized closed set is being completed. | Completeness: `Not applicable`. |
| Compatibility is not part of the case. | No project evidence of significant use of the same pictograph in a popular legacy system | No compatibility claim is supported. | Compatibility: `Not applicable`. |
| Existing organ emoji are not entitlement precedents. | Unicode Faulty comparison factor, https://www.unicode.org/emoji/proposals.html | Existing emoji do not justify a new one by comparison alone. | Faulty comparison. |

## Frequency evidence

| Claim | Source | What the source supports | Proposal use |
| --- | --- | --- | --- |
| Google Search displayed about 353,000,000 results for `stomach` on 2026-07-26. | Screenshot and query: https://www.google.com/search?q=stomach&hl=en&filter=0 | A dated result-count snapshot for the required query. | Expected usage caption only. |
| Google Video Search displayed about 139,000,000 results for `stomach` on 2026-07-26. | Screenshot and query: https://www.google.com/search?tbm=vid&q=stomach&hl=en&num=10&pws=0 | A dated video result-count snapshot. | Expected usage caption only. |
| Worldwide Web Search interest for `stomach` exceeds `elephant` on the displayed average and in recent years. | Screenshot and query: https://trends.google.com/trends/explore?date=all&q=stomach,elephant | Relative search interest over 2004-present with visible settings. | Expected usage caption. |
| Worldwide Image Search interest is sustained and has a recent `stomach` peak above `elephant`. | Screenshot and query: https://trends.google.com/trends/explore?date=all&gprop=images&q=stomach,elephant | Relative image-search interest over 2008-present with visible settings. | Expected usage caption. |
| English Books use of `stomach` substantially exceeds `elephant` in the latest displayed years and persists across the range. | Screenshot and query: https://books.google.com/ngrams/graph?content=elephant%2Cstomach&year_start=1500&year_end=2022&corpus=en&smoothing=3 | Relative published-book frequency, not emoji demand. | Expected usage and Transient. |

## Visual and implementation claims

| Claim | Source | What the source supports | Proposal use |
| --- | --- | --- | --- |
| The design has a J shape, long inlet, open inner curve, broad lower body, and short outlet. | Exact four candidate assets and their SVG sources | Directly visible identity cues. | Distinctiveness; Other Information. |
| The exact assets remain distinct from the declared visual confusers at 18x18 and 72x72. | `validation-v1.12/computer-validation.md` and the four actual-size comparison boards | Technical and visual separation from Anatomical Heart, Beans, Meat on Bone, Kidney, Liver, and a generic organ shape. | Distinctiveness; never include validator metrics in the PDF. |
| Vendors can vary color, angle, outline, and shading while keeping the essential outline cues. | Design analysis of the exact assets and Unicode's paradigm principle | Implementation recommendation, not an exact-image demand. | Distinctiveness; Other Information. |

## Claims excluded from the filing PDF

- Disease burden, reflux prevalence, cancer incidence, professional endorsement, campaign support, petitions,
  and calls for an emoji do not establish selection or expected emoji use.
- Search result counts are not counts of users or intended emoji uses. The proposal states only the displayed
  result and date, without internal methodological commentary.
- Computer validation metrics, asset hashes, panel verdicts, readiness labels, and internal approval records
  remain internal controls.
- No claim is made that the proposed sequences are already conventional or that Unicode will approve the
  proposal.
