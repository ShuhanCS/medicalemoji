# Accepted Emoji Proposal Analysis

Updated: 2026-07-20

## Purpose

This file records the research behind the project's best-in-class submission specification. The controlling
implementation standard is:

`docs/proposals/emoji-proposal-approval-rubric.md`

Primary sources:

- Current Unicode proposal guidelines:
  https://www.unicode.org/emoji/proposals.html
- Accepted proposal chart for Emoji 17.0 and earlier:
  https://www.unicode.org/emoji/charts/emoji-proposals.html
- Accepted proposal chart for Emoji 18.0 beta:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- ESR priorities for Emoji 18.0 and 19.0+:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC #185 minutes recording the Emoji 18.0 decisions:
  https://www.unicode.org/L2/L2025/25226.htm

Generated accepted-proposal manifest:

`docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json`

The manifest contains 268 proposal rows from Unicode's accepted-proposal chart. Older accepted proposals are
historical evidence only. Unicode expressly warns that the required format has changed and that acceptance
does not mean the UTC endorsed every argument in the proposal.

## Corpus

### Historical structured comparison

The prior analysis compared 55 documents associated with emoji encoded in Emoji 13.1 through 17.0 against
29 community proposal documents from similar registers that do not appear in the accepted-proposal chart.

The 29-document group must be described as `not encoded`, not as a verified set of formal rejections caused by
proposal-writing quality. Selection decisions are multi-factor and internal review history is not public for
every document.

| Measure | Accepted (n=55) | Not encoded (n=29) |
| --- | ---: | ---: |
| Median words | 907 | 1,485 |
| Median pages | 7 | 9 |
| Median extracted images | 26 | 18 |
| Median explicit `N/A` count | 1 | 0 |
| Includes exclusion section | 94% | 93% |
| Answers faulty comparison | 92% | 72% |
| States sort location | 30% | 10% |
| Includes Trends evidence | 87% | 65% |
| Shows `elephant` comparator | 32% | 13% |
| Cites petitions or social media | 45% | 75% |
| Uses cause or advocacy language | 1 document | 13 documents |

The useful inference is that structure alone does not distinguish a winner. Accepted proposals tend to be
shorter, more evidence-dense, more willing to use `N/A`, and more explicit about faulty comparison. The
comparison does not prove that any single stylistic choice caused acceptance.

### Emoji 18.0 accepted cohort

UTC #185 accepted nine characters from eight proposal documents:

| Document | Proposal | Pages | Extracted words | Extracted images | URL |
| --- | --- | ---: | ---: | ---: | --- |
| L2/25-252 | Leftwards and Rightwards Thumb Signs | 10 | 990 | 63 | https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf |
| L2/25-253 | Pickle | 8 | 1,405 | 36 | https://www.unicode.org/L2/L2025/25253-emoji-pickle.pdf |
| L2/25-254 | Monarch Butterfly | 19 | 3,491 | 66 | https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf |
| L2/25-255 | Eraser | 7 | Not reliable | 42 | https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf |
| L2/25-256 | Lighthouse | 9 | 1,142 | 27 | https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf |
| L2/25-257 | Meteor | 8 | 799 | 146 | https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf |
| L2/25-258 | Net With Handle | 10 | 1,147 | 39 | https://www.unicode.org/L2/L2025/25258-emoji-net.pdf |
| L2/25-259 | Squinting Face | 7 | 1,592 | 148 | https://www.unicode.org/L2/L2025/25259-emoji-squinting-face.pdf |

The cohort median is 9 pages and 55 extracted images. The Eraser PDF is image-based, so its extracted word
count is meaningless. These numbers reinforce evidence density, but they disprove any rigid claim that an
accepted proposal must stay under a particular word or page limit.

The Squinting Face character was later replaced by Cracking Face through L2/26-048:

https://www.unicode.org/L2/L2026/26048-cracked-smiling-face-emoji.pdf

### What the newest decisions actually show

1. Compatibility was unusually important. UTC #185 records that Monarch Butterfly would not have been
   recommended without its compatibility case and that compatibility was the theme of the set.
2. Compatibility is not transferable rhetoric. A proposal needs screenshots and high-frequency evidence from
   the existing social app, standard, or operating system.
3. Accepted documents still vary widely in polish, length, and argumentative quality. Acceptance is not proof
   that every sentence is a best practice.
4. Evidence remains visual. The newer proposals embed many screenshots, comparisons, and examples.
5. The strongest current proposals put the nearest existing emoji, visual distinction, and sort context near
   the front of the document.
6. ESR's stated Emoji 19.0+ direction raises the benchmark: cited empirical use, real compatibility where it
   exists, and improvement to the user experience of the existing emoji set.

## Best repeatable practices

### Build a reusable semantic unit

The proposal should make the concept useful in ordinary language across several durable contexts. Medical
importance can support context, but it cannot be the sole reason for encoding.

### Prove the gap against the strongest substitute

Name the nearest current emoji or sequence and show why it remains ambiguous. Do not compare only with weak
alternatives and do not argue that one organ deserves encoding because other organs exist.

### Treat 18x18 art as evidence

The submitted image is a paradigm, not final vendor art. Strong proof includes exact-size color and
black-and-white examples, nearest-emoji comparison, essential silhouette cues, and unprompted recognition.

### Cite claims, not prestige

Every factual or metaphorical claim used to earn a factor should have a screenshot or durable source.
Petitions, endorsements, requests, awareness campaigns, and author credentials are not usage evidence.

### Use `Not applicable` honestly

Completeness and compatibility should usually be `Not applicable` for an independently useful organ.
Inventing a finite anatomy set or unsupported platform compatibility makes the proposal weaker.

### Draft exclusions first

The highest-risk organ objections are `Already representable`, `Overly specific`, `Open-ended`, and
`Faulty comparison`. A proposal should survive those objections before prose is expanded elsewhere.

## Closest useful exemplars

- Treasure Chest, concise broad-building-block case:
  https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf
- Fingerprint, reproducible technical evidence:
  https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf
- X-Ray, nearby health/medical concept:
  https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf
- Shovel, cause-affiliated submitter that still argues ordinary utility rather than the cause:
  https://www.unicode.org/L2/L2023/23259-shovel-emoji.pdf
- Meteor, current compatibility-led model:
  https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf
- Lighthouse, current non-organ model with worldwide symbolism and a full current factor structure:
  https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf

No one exemplar controls. The current guidelines always take precedence.

## Implications for the 2026 organ slate

- Kidney has the strongest current frequency package, but needs a harder 18x18 test against Beans and other
  confusable silhouettes.
- Stomach has the strongest multiple-meaning case and the clearest small silhouette, but four web captures are
  from 2020 and should be refreshed.
- Liver has the largest readiness gap because its Trends evidence is 2020 and U.S.-only and its black 18x18
  silhouette lacks a unique identifying cue.
- All three need final citation cleanup, two independent review signoffs, a stable public PDF URL, and archived
  official-form confirmation.

Detailed audit:

`docs/proposals/2026-organ-submission-audit.md`
