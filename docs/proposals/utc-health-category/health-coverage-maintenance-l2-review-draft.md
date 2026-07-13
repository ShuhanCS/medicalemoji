---
title: "Health-related emoji coverage"
author-meta: "Shuhan He"
date-meta: "2026-07-13"
subject: "Draft technical discussion document for Microsoft review"
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
Source: Shuhan He
Date:   2026-07-13
Status: Draft for Microsoft standards review; not submitted to Unicode
Action: Microsoft review for possible UTC submission and ESR referral
```

**Status:** Shuhan He prepared this discussion draft independently for Microsoft review. Microsoft has not endorsed it. The draft raises a process question rather than requesting the encoding of an emoji.

# Summary

Health-related emoji appear across anatomy, diagnostics, laboratory science, medication, emergency care, and clinical equipment. Individual proposals are evaluated one at a time, but they often raise the same questions about existing substitutes, visual similarity, expected usage, and whether a proposal would lead to an open-ended set.

If submitted, this document would ask whether the Unicode Technical Committee should refer a short review of existing health emoji and recurring proposal questions to the Emoji Standard & Research Working Group. The review would examine how current health-related emoji are represented and found, and whether the existing proposal guidance gives enough direction for closely related medical concepts. Every new emoji would continue to require its own complete submission through the official Emoji Submission Form.

# Questions for discussion

1. Would reviewing related health emoji together help ESR assess existing substitutes and closely related proposals consistently?
2. Are common health-related emoji easy to find through current names, keywords, ordering, and vendor keyboard layouts? If not, which standards or platform group should address the gap?
3. Does the published guidance give enough direction for proposals that are medically distinct but visually related, such as Blood Bag and IV Bag or Pill Box and Pill Pack?
4. Would a short public note on small-size recognition, black-and-white legibility, and category-completion arguments help future submitters avoid predictable problems?
5. If no additional guidance is needed, can ESR identify the current material that already answers these questions?

# Why the question has arisen

The Medical Emoji proposal archive contains concepts from several parts of health communication. Some are familiar objects, such as Pill Box and Inhaler. Others are procedures, laboratory concepts, or anatomy. Reviewers must decide whether each concept is independently useful, whether an existing emoji can express the intended meaning, and whether the image remains clear at emoji size.

These questions recur across individual proposals. Reviewing them together could make the reasons for advancing or declining related concepts easier to understand and apply consistently.

The 2026 intake also makes the process distinction important. Individual emoji proposals must be submitted through the Emoji Submission Form. A technical discussion document follows Unicode's document-submission process and may be placed on a UTC agenda or referred to a working group. The two routes serve different purposes.

# Related history

## Apple's 2018 accessibility proposal

Apple's L2/18-080 proposed nine accessibility emoji organized around four areas: Blind and Low Vision, Deaf and Hard of Hearing, Physical Motor, and Hidden Disabilities. Apple described the set as a finite starting point rather than a comprehensive catalogue, worked with disability organizations, and addressed the selection factors and open-ended concern directly.

The Apple document is a public example of a vendor explaining how several related concepts fit together. It used the emoji-proposal process available in 2018. Under the 2026 guidance, each emoji encoding proposal must use the official form and will be evaluated on its own evidence.

Source: https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf

## Anatomical Heart and Lungs

In 2019, Christian Kamkoff, Shuhan He, and Melissa Thermidor submitted separate proposals for Anatomical Heart and Lungs. Unicode later encoded both characters. Their history shows that related health concepts can be considered individually, each with its own evidence and selection-factor case.

Sources:

- https://www.unicode.org/L2/L2019/19149-lung-emoji.pdf
- https://www.unicode.org/L2/L2019/19150-heart-emoji.pdf

# Scope of a possible ESR review

A short review could use six working areas without treating them as proposed keyboard categories:

- **Anatomy:** how proposed internal organs should address category completion and open-endedness.
- **Diagnostics:** when CT Scan, Ultrasound, or another modality adds a recognizable procedure or object beyond X-Ray and Stethoscope.
- **Laboratory science:** visual confusion among cells, microbes, specimens, and laboratory equipment.
- **Medication:** how organizers, packaging, delivery devices, and adherence concepts should address existing Pill and Syringe emoji.
- **Emergency care:** when another object adds a broad communication function beyond Adhesive Bandage, Crutch, Ambulance, and Hospital.
- **Clinical equipment:** small-size recognition, color independence, and overlap among equipment silhouettes.

These working areas would organize the analysis only. They would not imply that every gap should produce a character or that Unicode should create a top-level Health group.

# Relationship to individual proposals

Each proposed emoji must stand on its own. A complete submission should include the required color and black-and-white images, keywords, category and sort location, expected-usage evidence, inclusion and exclusion factors, image-rights warranty, and any relevant history.

Recent proposals illustrate recurring comparisons such as Blood Bag and IV Bag, or Pill Box and Pill Pack. This paper takes no position on any candidate. Each would require a separate submission and decision.

# Possible vendor input

If a vendor chooses to comment, useful input could include:

- whether a proposed image is recognizable at common emoji sizes;
- whether the meaning survives in black and white;
- whether the design is platform-neutral and free of text or protected symbols;
- whether two related concepts would be distinguishable in the same emoji set; and
- whether public implementation considerations should be shared with ESR.

A vendor could offer technical observations without committing to implement a candidate. Submitters would remain responsible for evidence, licensing, and proposal completeness.

# Requested disposition

If the UTC finds the question useful, this draft suggests referral to ESR for discussion. ESR could then advise whether the current guidance is sufficient, whether a short review would help, or whether no further work is needed.

If Microsoft agrees that the question merits UTC discussion, its standards team could submit a revised document, coauthor one with Shuhan He, or use this draft as source material for its own document. Microsoft would decide its authorship and position before any submission.

# References

- Unicode, Guidelines for Submitting Unicode Emoji Proposals:\
  https://www.unicode.org/emoji/proposals.html
- Unicode, Pending Document Submission:\
  https://www.unicode.org/pending/docsubmit.html
- Unicode, Emoji Submission FAQ:\
  https://www.unicode.org/faq/emoji_submission.html
- Unicode, Emoji Standard & Research Working Group Report for UTC #186:\
  https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf
- Unicode, Emoji Ordering:\
  https://unicode.org/emoji/charts/emoji-ordering.html
- Unicode, Unicode Emoji List:\
  https://unicode.org/emoji/charts/emoji-list.html
- Unicode, Unicode Standard Annex #51:\
  https://www.unicode.org/reports/tr51/
- Apple, Proposal for New Accessibility Emoji, L2/18-080:\
  https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf
