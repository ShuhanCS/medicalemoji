# Liver Selection-Factor Correction Specification

**Spec version:** 1.0.1

**Date:** 2026-07-26

**Status:** Decision-ready implementation specification

**Target:** The next Liver submission revision after the coordinated `v1.10.0` package is finalized

## Decision

Keep the answer to **C. Breaks new ground** as **Yes**.

The proposal should not answer No merely to appear conservative. Under Unicode's current selection factors, breaking new ground is a positive inclusion factor: the proposed emoji should add a concept that is not already represented, rather than a variation of an existing emoji. A No answer is not automatically disqualifying, but it voluntarily gives up a relevant positive factor. Liver has a truthful Yes case because no current emoji or reliable sequence identifies the liver.

The proposal must separate that semantic-gap argument from two arguments Unicode discourages:

1. It must not say that Liver deserves encoding because Anatomical Heart, Lungs, or Brain already exist.
2. It must not imply that Unicode should complete a set of internal organs.

The winning formulation is therefore: **Yes, Liver adds a missing literal body-site term; no, existing organs are not precedent and this is not a category-completion request.**

## Confidence and limits

Confidence is **high** that Yes is the correct answer under the published criteria and the evidence currently assembled. Confidence is only **moderate** that any particular wording will lead to acceptance, because proposal documents and UTC minutes are descriptive evidence, not a causal approval model. The UTC may accept or reject a character for considerations not visible in the public proposal.

Historical acceptance also shows that No is survivable, not preferable. The accepted Harp proposal said it did not substantially break new ground. That counterexample proves the factor is not a mandatory gate; it does not show that a candidate with a valid positive case should waive it.

## Evidence hierarchy

Implementation and review must use this order of authority:

1. **Official current Unicode guidance** for the meaning of each factor.
2. **Official proposal PDFs, charts, and UTC minutes** for historical practice.
3. **Repository research and rubric** for repeatable patterns and proposal QA.
4. **Internal judgment** only where the higher sources do not decide the issue.

The repository's controlling best-practices guide is:

- `submissions/v1.10.0/BEST-IN-CLASS-RUBRIC.md`

Its supporting historical analysis is:

- `docs/research/unicode-winning-submissions/analysis.md`
- `docs/research/unicode-winning-submissions/README.md`

The rubric's relevant instructions are to answer Yes or No immediately, identify the nearest current emoji, explain the semantic gap in ordinary communication, avoid relying on other body-part emoji, and make an independently selective open-ended case.

## Historical findings that control this decision

### Current rule

Unicode treats a concept that is new and different as a positive inclusion factor. The relevant comparison is semantic coverage: can a current emoji or reliable sequence already communicate the proposed concept? Liver is not a skin-tone, gender, direction, or other variation of an existing emoji.

### Recent accepted proposals

Review of the latest extractable accepted proposal texts found that six of seven made a positive new-ground case; Net With Handle used N/A. The Eraser PDF was not reliable enough for text extraction and should not be counted either way. The latest cohort was unusually influenced by compatibility considerations, and UTC minutes specifically note that Monarch would not have been recommended without compatibility. Liver has no equivalent compatibility basis, so its strongest honest case should not discard a valid semantic-gap factor.

### Accepted counterexample

Harp was accepted despite answering that it did not substantially break new ground. This establishes that No is not fatal. It does not make No a best practice, and Harp's total case cannot be transferred to Liver.

### Declined medical proposals

The repository's declined-medical-proposal review identifies recurring risks that matter here:

- substituting medical importance or awareness for communicative use;
- relying on petitions, campaigns, or social calls;
- making a weak open-ended argument;
- using stale or irreproducible evidence; and
- treating nearby encoded items as precedent rather than proving an independent semantic gap.

The Liver revision must address those risks directly. “Breaks new ground: Yes” is defensible only when paired with independently documented usage, non-substitutability, and distinctiveness.

## Factual baseline

The public proposal must keep the Liver case independent and limit semantic comparisons to currently encoded emoji or clearly identified generic controls. Separate submission candidates, artwork, and evidence are out of scope.

Current encoded anatomical emoji relevant to this comparison include:

- Brain (`U+1F9E0`)
- Anatomical Heart (`U+1FAC0`)
- Lungs (`U+1FAC1`)

There is no encoded Liver emoji in the current official emoji test data. The Liver proposal must not include or rely on material from separate submissions.

Cut of Meat and Beans may be discussed as ambiguous substitutes, but neither reliably identifies the liver. General medical emoji can add context, but they do not supply the missing body-site term.

## Required proposal text

The next Liver revision should use the following substance. Minor copyediting is allowed only if it preserves each explicit boundary.

### C. Breaks new ground

> **Yes.** No current emoji or reliable emoji sequence identifies the liver. Anatomical Heart, Lungs, and Brain identify different body parts; Cut of Meat and Beans do not reliably identify a liver. Medical-context emoji can convey testing, imaging, medication, or care, but none supplies the missing body-site term. Liver therefore adds a distinct literal semantic building block for ordinary messages that explicitly identify the organ. This claim does not depend on the existence of other organ emoji or on completing an anatomy set.

### Already representable

> **No existing emoji or reliable sequence identifies the liver.** Anatomical Heart, Lungs, and Brain identify different organs. Cut of Meat and Beans shift the meaning toward food and remain ambiguous. General medical emoji can add context only after the body site is identifiable.

### Open-ended

> **No.** Liver is not proposed to complete an anatomy set. Its candidacy rests on independently documented literal usage, the absence of a reliable substitute, and a visually testable whole-organ paradigm. Encoding Liver would not establish that every internal organ qualifies; any future candidate would need to satisfy the same usage, non-substitutability, and distinctiveness tests.

The final open-ended paragraph must not claim that Liver is the most common, most important, or uniquely deserving internal organ unless the submission includes reproducible comparative evidence supporting that exact claim.

### Faulty comparison

> **No.** The proposal does not rely on the existence or importance of Anatomical Heart, Lungs, Brain, or any other encoded emoji. Its independent case is documented literal usage, absence of a substitute, and a distinct visual paradigm.

## Comparison-board policy

The public Liver PDF should compare the candidate only with **currently encoded** items and clearly identified generic controls. It must not include artwork, names, or evidence from separate submissions; doing so would create a visual anatomy-slate argument even when the prose disclaims one.

Preferred public comparison set:

- Liver candidate;
- Anatomical Heart;
- Lungs;
- Brain;
- Cut of Meat; and
- Beans or a clearly labeled generic-organ control.

Any internal cross-candidate QA material must remain outside the Liver submission package and must not be evidence for Section C.

## Other corrections bundled into the next Liver revision

The currently reviewed Liver PDF has additional defects that should be corrected in the same revision:

1. Make the Google Ngram narrative match the screenshot's actual case-sensitivity setting.
2. Remove page-title, footer, and body-text clipping or overlap in the rendered PDF.
3. Preserve the required color and black-and-white artwork at both 18 px and 72 px on page 1.
4. Keep every evidence screenshot reproducible, dated, and tied to its source and settings.
5. Verify that every claimed public URL resolves before submission.
6. Keep internal scoring and unsupported approval predictions out of the public proposal.

These layout and evidence corrections do not alter the Section C decision, but unresolved presentation defects would undermine an otherwise sound argument.

## Acceptance criteria

The correction is complete only when all of the following are true:

- Section C begins with **Yes** and explains the missing semantic term before discussing nearby emoji.
- Section C does not use existing body-part emoji as precedent or request category completion.
- The open-ended and faulty-comparison exclusions state an independent, selective basis for Liver.
- No public-facing Liver content refers to or depicts a separate submission candidate.
- The public comparison board does not visually imply an official or inseparable anatomy set.
- Every named encoded comparator is verified against the current official `emoji-test.txt` data.
- Claims about usage or comparative standing are backed by reproducible evidence; unsupported superlatives are removed.
- The Ngram prose and screenshot use the same settings and interpretation.
- A full-page render inspection finds no clipping, overlap, broken glyphs, or unreadable footers.
- The 18 px and 72 px color and black-and-white artwork requirements are visibly satisfied on page 1.
- The final PDF and all public evidence URLs resolve from a clean checkout.

## Verification procedure

1. Search the public Liver sources and extracted PDF text for `breaks new ground`, `open-ended`, and `faulty comparison`, plus the names of every other active submission candidate.
2. Remove every reference to, depiction of, or comparison with a separate submission candidate.
3. Verify encoded names and code points against the official current emoji test file.
4. Regenerate the PDF using the repository's normal build path.
5. Render every page to images and inspect at full-page and detail scale.
6. Compare extracted Ngram prose with the visible screenshot setting and values.
7. Run the repository's proposal validation checks and confirm a clean build from tracked inputs.
8. Review the final diff to ensure the implementation touches only the intended next-version Liver package and shared source files that genuinely require the correction.

## Versioning and implementation boundary

This specification is versioned independently as **1.0.1**. It does not change the repository package version (`0.39.0`) because it is a decision/specification document and does not alter the generated submission artifact or application behavior.

Do not rewrite a frozen historical snapshot. Implement this in the next available Liver submission revision after checking the final state of the coordinated `v1.10.0` work. If `v1.10.0` is already the immutable published snapshot, create the next semantically appropriate patch revision rather than editing it in place.

## Primary sources

- Unicode emoji proposal submission and selection guidelines: https://www.unicode.org/emoji/proposals.html
- Unicode Emoji 18.0 proposal status chart: https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- Emoji Standard and Research Working Group priorities: https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC meeting 185 minutes: https://www.unicode.org/L2/L2025/25226.htm
- Accepted Harp proposal: https://www.unicode.org/L2/L2023/23256-harp-emoji.pdf
- Official current emoji test data: https://www.unicode.org/Public/emoji/latest/emoji-test.txt

## Final review question

Before release, ask one question: **Does the proposal prove that Liver independently adds a useful missing term, or does it merely make Liver look like the next member of an organ set?** Only the first case is submission-ready.
