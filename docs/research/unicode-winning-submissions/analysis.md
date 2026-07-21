# Emoji Proposal Evidence Audit

Updated: 2026-07-20

## Bottom line

This is an audit of proposal documents: what they argue, what evidence they show, how their artwork performs,
and how easily a reviewer can validate the case. L2 identifiers are citations only; registry numbering is not
being treated as a proposal-quality signal.

The strongest current general-purpose model is Lighthouse. Treasure Chest is the strongest concise model,
Fingerprint is the strongest technical-evidence model, and Meteor is the strongest genuine compatibility model.
No accepted proposal is a perfect template, and acceptance does not endorse every sentence or design choice in
the PDF.

The most defensible finding is not a magic word count or a phrase that predicts approval. Strong proposals make
an independently selective concept easy to understand and verify. The confirmed declined Medical Emoji drafts
often had all the headings, but leaned on medical importance, disease burden, desired awareness, petitions, or
calls for an emoji where current review requires evidence of ordinary communicative use.

## Proposal corpus actually reviewed

- First pages of 63 accepted proposal PDFs were visually reviewed for identity, art, rights, evidence framing,
  and layout.
- Six representative accepted proposals were reviewed page by page: Lighthouse, Meteor, Monarch Butterfly,
  Treasure Chest, Fingerprint, and Orca.
- Extracted text and PDF measurements were recomputed for the 55-proposal accepted archive associated with
  Emoji 14.0 through 17.0.
- All eight proposal documents in the latest Emoji 18.0 accepted set were reviewed, including documents whose
  text layers are incomplete or image-based.
- Full text was reviewed for 15 Medical Emoji proposal drafts whose concepts and dates match confirmed decline
  records.

The declined drafts' original embedded images are no longer present in the repository or the searched local
source locations. Their arguments and evidence descriptions can be audited, but their artwork and page design
cannot. Unicode's public status data also does not disclose complete reviewer reasoning. Findings from that
group are therefore risk indicators, not causal proof.

## Best proposal exemplars

| Proposal | Best use as a model | Limitation | Source |
| --- | --- | --- | --- |
| Lighthouse | Best current all-around structure: clean first page, current factor order, direct `N/A`, all five evidence sources, and complete exclusions | Nine pages; still needs concept-specific adaptation | https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf |
| Treasure Chest | Best concise structure and broad-building-block argument | Some evidence screenshots are small | https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf |
| Fingerprint | Best evidence discipline, technical explanation, and nearest-substitute rebuttal | Dense text and older-looking layout | https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf |
| Meteor | Best real interoperability/compatibility case | Compatibility cannot be copied without equivalent popular-system evidence | https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf |
| Monarch Butterfly | Important counterexample: accepted with extensive awareness and advocacy context because an independent compatibility case existed | Nineteen pages and unusually cause-heavy; not a general template | https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf |
| Orca | Useful concession of weak evidence and direct selection-factor reasoning | Several screenshots render as broken or blank warning icons; not a layout model | https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf |

## What successful proposal documents actually do

### 1. Make page 1 do real work

The best current first pages expose the proposal title, individual submitters, revision date, short name,
keywords, category, color and black-and-white artwork at 18x18 and 72x72, and the image-rights statement. This
is both current-rule compliance and good review design: identity, scope, art, and rights can be checked before
the reviewer enters the argument.

### 2. Define a semantic gap, not merely an important subject

Strong proposals name the nearest existing emoji or sequence and state what ordinary message remains
unexpressed. Treasure Chest and Fingerprint are especially direct. The proposal's topic may be important, but
importance is background; the selection case is the missing communicative building block.

### 3. Treat selection factors as tests

Successful proposals do not need to claim every positive factor. Direct `N/A` answers can make the case more
credible when Multiple meanings, Completeness, or Compatibility is not real. Invented metaphors, an imaginary
closed set, or a weak platform analogy create more objections than points.

### 4. Let the 18-pixel artwork carry the identity

The accepted first pages show the proposed glyph at keyboard scale, not only as a large illustration. The best
art has a distinctive outer shape and only a few essential internal cues. Details that disappear in true
black-and-white or at 18x18 cannot carry the recognition case.

### 5. Make evidence readable and reproducible

Current best practice is to include all five requested sources and preserve the query, settings, range,
location, date, comparator, and visible result. Strong proposals interpret the evidence and concede weaknesses
instead of cropping them away. A screenshot count or PDF image-object count is not a substitute for readable
proof.

### 6. Answer the actual reasons the proposal could fail

The strongest exclusion sections identify the best substitute, the specificity boundary, and the open-ended
risk. For organ proposals, Open-ended cannot be answered by saying anatomy is important or that Heart and Lungs
already exist. Each organ must have an independent category-level case that does not imply an unbounded set.

### 7. Use compatibility only when it is genuine

Meteor and the latest compatibility-themed cohort show that an existing high-use pictograph in a popular
system can be decisive. Compatibility is not a visual resemblance, a niche icon, or a desired partnership. If
the same character is not already deployed at high frequency in a popular system, `N/A` is stronger.

## What the confirmed declined proposal documents reveal

The 15 confirmed declined Medical Emoji drafts all had recognizable proposal structure and all five exclusion
headings. Their recurring weaknesses are more substantive:

1. Clinical burden, mortality, professional importance, or desired awareness was often offered where evidence
   of ordinary communicative use was needed.
2. Thirteen of 15 mention petitions, Instagram, or Twitter. Calls for the emoji are not acceptable frequency
   evidence under the current rules.
3. Open-ended answers often asserted breadth or importance without demonstrating why that candidate is
   independently selective among many organs, diseases, procedures, or specialties.
4. The drafts rarely used `N/A`, which encouraged speculative positive-factor arguments.
5. The evidence predates the current five-source, `elephant`, widest-range, and reproducibility instructions.
6. A bundle of related medical proposals makes the set-expansion objection more visible even though filing
   three separate eligible proposals is permitted.

These observations do not mean medical terms, length, or cause-related words are independently negative.
Medical subject matter is confounded with this declined archive. The safe inference is narrower: importance and
advocacy cannot replace a concept's expected use and independent selectivity.

## Counterexamples that corrected earlier rules

### Cause language is not absolutely forbidden

Monarch Butterfly contains extensive awareness and advocacy context and was accepted. The official rule is
that a proposal will not advance *because* it furthers a cause; it may advance despite cause context when the
selection case independently succeeds. The template therefore must ban cause advocacy as the justification,
not ban the words `awareness` or `advocacy` wherever they are accurate and cited.

### Medical importance is context, not an automatic defect

X-Ray includes medical importance but also establishes a recognizable diagnostic object, a clear gap, and
ordinary expressive use. It was accepted:

https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf

The lesson is not to strip all medical context from Kidney, Liver, or Stomach. It is to ensure that the proposal
would still satisfy the selection factors if every disease-burden and awareness paragraph were removed.

### Accepted PDFs can be imperfect

Orca contains broken or blank figures. Eraser is substantially image-based. Thumb Point explains that a Google
Video result count was unavailable. Monarch Butterfly is 19 pages and has 3,491 extractable words. These
accepted cases disprove hard thresholds for length, words, or PDF object counts. They do not justify avoidable
defects in a new filing.

Thumb Point:

https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf

Eraser:

https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf

## Latest accepted proposal set

UTC #185 accepted nine characters from eight proposal documents:

| Proposal | Pages | Extractable words | URL |
| --- | ---: | ---: | --- |
| Leftwards and Rightwards Thumb Signs | 10 | 990 | https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf |
| Pickle | 8 | 1,405 | https://www.unicode.org/L2/L2025/25253-emoji-pickle.pdf |
| Monarch Butterfly | 19 | 3,491 | https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf |
| Eraser | 7 | Not reliable | https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf |
| Lighthouse | 9 | 1,142 | https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf |
| Meteor | 8 | 799 | https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf |
| Net With Handle | 10 | 1,147 | https://www.unicode.org/L2/L2025/25258-emoji-net.pdf |
| Squinting Face | 7 | 1,592 | https://www.unicode.org/L2/L2025/25259-emoji-squinting-face.pdf |

The face was later changed to Cracking Face:

https://www.unicode.org/L2/L2026/26048-cracked-smiling-face-emoji.pdf

These proposals are heterogeneous. Their strongest shared lesson is not a page count; it is that a proposal
must have a clear selection theory. UTC #185 records that compatibility was unusually important to this set.
That is a cohort-specific fact, not permission to manufacture a compatibility claim.

## Reproducible corpus measurements

The accepted text archive contains 55 extracted documents associated with Emoji 14.0 through 17.0. It is a
useful reference library, not a clean sample of independent public submissions: at least 17 name Jennifer
Daniel or the Emoji Subcommittee, one is a committee strategy document, and some concepts were revised or
consolidated.

| Measure | Accepted archive | Confirmed declined drafts |
| --- | ---: | ---: |
| Documents | 55 | 15 |
| Median extractable text/token count | 907 words | 1,522 markdown tokens |
| Median explicit `N/A` count | 1 | 0 |
| Each exclusion term appears | 51-53/55, depending on term | 15/15 for every term |
| Mentions Google Trends | 45/55 | 13/15 |
| Mentions `elephant` | 18/55 | 3/15 |
| Mentions petitions, Instagram, or Twitter | 25/55 | 13/15 |
| Mentions audited cause terms | 1/55 | 7/15 |

Text counts require caution. One accepted PDF has a near-empty text layer, another is image-based, and term
mentions do not show how a term was used. PDF image-object counts are also unstable because masks, repeated
objects, and full-page scans inflate them. Neither measure is a submission-quality threshold.

Reproduction code:

`evidence/emoji_proposal_corpus_audit.py`

Generated measurements:

`docs/research/unicode-winning-submissions/corpus-audit-2026-07-20.json`

## Why the older 55-versus-29 approval model is retired

The repository contains the prose report but no manifest, source files, extracted text, outcome annotations, or
analysis code for its 29-document comparison group. The groups were not matched by era or author type, and
absence from an accepted chart was treated too loosely as a final negative outcome. The old percentages and
causal claims cannot be reproduced and must not set word, page, image, sort-location, or language thresholds.

This limitation is about the old comparison design. It does not prevent direct learning from actual proposal
documents with known outcomes, as long as observations are labeled descriptive and counterexamples are kept.

## Proposal-level findings that survive the audit

1. Current completeness is mandatory, but headings alone do not make a proposal competitive.
2. The central argument is an independently selective communicative gap, not importance or deservingness.
3. `N/A` is evidence discipline, not a trick: use it whenever a positive factor is not compelling.
4. Art must be recognizable in color and true black-and-white at 18x18.
5. Evidence must be readable, reproducible, current, and interpreted honestly.
6. Petitions and social-media calls for the emoji are not frequency evidence.
7. A cause may be context, but cannot be the reason for encoding.
8. Accepted proposals are too heterogeneous to support hard length or image-count rules.
9. Acceptance does not turn a broken figure, weak paragraph, or exceptional omission into best practice.
10. Parallel Kidney, Liver, and Stomach filings are permitted, but each increases the need for a bounded,
    independent Open-ended answer.

## Implications for the 2026 organ slate

- Kidney has the strongest current frequency package, but needs the complete confirmed author list and a hard
  18x18 recognition test against Beans.
- Stomach has the strongest multiple-meaning case and clearest silhouette, but its historical captures need a
  current reproducibility review.
- Liver has the largest evidence and distinctiveness gap because its Trends evidence is old and U.S.-only and
  its small black-and-white silhouette lacks a unique identifying cue.
- Each proposal must make a broad ordinary-use case that remains persuasive without disease-burden, awareness,
  or comparison-to-existing-organs arguments.
- All three need citation cleanup, independent factual and process review, a stable public PDF URL, and archived
  filing confirmation.

Detailed readiness audit:

`docs/proposals/2026-organ-submission-audit.md`

## Controlling primary sources

- Current Unicode proposal guidelines:
  https://www.unicode.org/emoji/proposals.html
- Current proposal status definitions:
  https://www.unicode.org/emoji/emoji-proposals-status.html
- Emoji proposal FAQ:
  https://www.unicode.org/faq/emoji_submission.html
- Accepted proposal chart through Emoji 17.0:
  https://www.unicode.org/emoji/charts/emoji-proposals.html
- Accepted proposal chart for Emoji 18.0 beta:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- ESR priorities for Emoji 18.0 and 19.0+:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC #185 minutes recording Emoji 18.0 decisions:
  https://www.unicode.org/L2/L2025/25226.htm
