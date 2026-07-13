---
title: "Health-related emoji coverage"
author-meta: "David Rhew; Heena Purohit; Shuhan He"
date-meta: "2026-07-13"
subject: "UTC discussion document on health-related emoji coverage"
geometry: margin=1in
fontsize: 10pt
mainfont: "Georgia"
numbersections: true
colorlinks: false
header-includes:
  - \usepackage{xurl}
  - \usepackage[none]{hyphenat}
---

```text
Title:  Health-related emoji coverage
Authors: David Rhew; Heena Purohit; Shuhan He
Date:   2026-07-13
Action: Refer to the Emoji Standard & Research Working Group for review and recommendation
```

# Summary

Health-related emoji appear across anatomy, diagnostics, laboratory science, medication, emergency care,
and clinical equipment. Individual proposals are reviewed one at a time, but they often raise the same
questions: whether an existing emoji is an adequate substitute, whether two concepts are visually distinct,
whether expected usage is broad enough, and whether one proposal would lead to an open-ended set.

We ask the Unicode Technical Committee to refer these recurring questions to the Emoji Standard & Research
Working Group. The review would examine how existing health-related emoji are represented and found, and
whether the current proposal guidance gives enough direction for closely related medical concepts. Every new
emoji would continue to require its own complete submission through the official Emoji Submission Form.

# Questions for review

1. Would a review of related health emoji help ESR assess existing substitutes and closely related proposals
   more consistently?
2. Are common health-related emoji easy to find through their current names, keywords, ordering, and vendor
   keyboard layouts? If not, which standards or platform group should address the problem?
3. Does the published guidance give enough direction for concepts that are medically distinct but visually
   related, such as Blood Bag and IV Bag or Pill Box and Pill Pack?
4. Would a short public note on recognition at small sizes, black-and-white legibility, and category-completion
   arguments help submitters avoid recurring problems?
5. If the current guidance already answers these questions, can ESR identify the material that submitters
   should follow?

# Why this question has arisen

The current Unicode Emoji Ordering places Syringe, Pill, Drop of Blood, Adhesive Bandage, Stethoscope, X-Ray,
and Crutch in `Objects > medical`. Anatomical Heart, Lungs, and Brain are in
`People & Body > body-parts`; Test Tube, Petri Dish, and DNA are in `Objects > science`; Hospital and Ambulance
are in `Travel & Places`; and Medical Symbol and Wheelchair Symbol are in `Symbols`. This document does not
propose moving those emoji. Their distribution is one reason a focused review of discoverability, existing
substitutes, and closely related proposals may be useful.

An individual proposal must still show that its concept is independently useful, that an existing emoji cannot
express it adequately, and that the image remains clear at emoji size.

The 2026 intake also makes the procedural distinction important. Individual emoji proposals must be submitted
through the Emoji Submission Form. A UTC discussion document follows Unicode's separate document-submission
process and may be placed on a UTC agenda or referred to a working group. The two routes serve different
purposes.

# Related history

## Apple's 2018 accessibility proposal

Apple's L2/18-080 proposed nine accessibility emoji organized around four areas: Blind and Low Vision, Deaf
and Hard of Hearing, Physical Motor, and Hidden Disabilities. Apple described the set as a finite starting
point rather than a comprehensive catalogue, worked with disability organizations, and addressed Unicode's
open-ended exclusion factor directly.

The Apple document is a public example of a vendor explaining how several related concepts fit together. It
used the emoji-proposal process available in 2018. Under the 2026 guidance, each encoding proposal must use the
official form and is evaluated on its own evidence.

Source: <https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf>

## Anatomical Heart and Lungs

In 2019, Christian Kamkoff, Shuhan He, and Melissa Thermidor submitted separate proposals for Anatomical Heart
and Lungs. Unicode later encoded both characters. Their history shows that related health concepts can be
considered together while each proposal makes its own case.

Sources:

- <https://www.unicode.org/L2/L2019/19149-lung-emoji.pdf>
- <https://www.unicode.org/L2/L2019/19150-heart-emoji.pdf>

# Scope of the review

The review could use six working areas. These are not proposed keyboard categories.

- **Anatomy:** how proposed internal organs should address category completion and open-endedness.
- **Diagnostics:** when CT Scan, Ultrasound, or another modality adds a recognizable procedure or object beyond
  X-Ray and Stethoscope.
- **Laboratory science:** visual overlap among cells, microbes, specimens, and laboratory equipment.
- **Medication:** how organizers, packaging, delivery devices, and adherence concepts should address the
  existing Pill and Syringe emoji.
- **Emergency care:** when an additional object has a broad communication function beyond Adhesive Bandage,
  Crutch, Ambulance, and Hospital.
- **Clinical equipment:** recognition at small sizes, color independence, and overlap among equipment
  silhouettes.

These areas would organize the review. They do not imply that every gap should produce a character or that
Unicode should create a top-level Health group.

# Relationship to individual proposals

Each proposed emoji must stand on its own. A complete submission includes the required color and
black-and-white images, keywords, category and sort location, expected-usage evidence, inclusion and exclusion
factors, image-rights warranty, and relevant proposal history.

This document takes no position on any candidate. Each candidate requires a separate submission and decision.

# Vendor input

Vendor reviewers can provide useful technical observations without committing to implement a candidate. Their
input may address:

- whether an unfamiliar viewer can identify the image at common emoji sizes;
- whether the meaning survives in black and white;
- whether the design is platform-neutral and free of text or protected symbols;
- whether two related concepts would be distinguishable in the same emoji set; and
- whether implementation or interoperability concerns should be shared with ESR.

Submitters remain responsible for evidence, licensing, and proposal completeness.

# Requested action

We ask the UTC to refer this document to ESR for review and recommendation. ESR could advise whether the
current guidance is sufficient, whether a short public note or focused review would help, or whether no
further action is needed.

This document requests no character encoding and no bundled approval. Every candidate remains subject to the
official Emoji Submission Form and an independent review under Unicode's published criteria.

# References

- Unicode, Guidelines for Submitting Unicode Emoji Proposals:\
  <https://www.unicode.org/emoji/proposals.html>
- Unicode, Pending Document Submission:\
  <https://www.unicode.org/pending/docsubmit.html>
- Unicode, Emoji Submission FAQ:\
  <https://www.unicode.org/faq/emoji_submission.html>
- Unicode, Emoji Standard & Research Working Group Report for UTC #186:\
  <https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf>
- Unicode, Emoji Ordering:\
  <https://unicode.org/emoji/charts/emoji-ordering.html>
- Unicode, Unicode Emoji List:\
  <https://unicode.org/emoji/charts/emoji-list.html>
- Unicode, Unicode Standard Annex #51:\
  <https://www.unicode.org/reports/tr51/>
- Apple, Proposal for New Accessibility Emoji, L2/18-080:\
  <https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf>
