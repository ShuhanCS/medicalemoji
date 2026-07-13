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
  - |
    \usepackage{fancyhdr}
    \usepackage{needspace}
    \newcommand{\lTwoSubmissionFooter}{\footnotesize Health-related emoji coverage \enspace\textbar\enspace Rhew, Purohit, He \enspace\textbar\enspace Page \thepage}
    \fancypagestyle{l2submission}{
      \fancyhf{}
      \fancyfoot[C]{\lTwoSubmissionFooter}
      \renewcommand{\headrulewidth}{0pt}
      \renewcommand{\footrulewidth}{0pt}
    }
    \pagestyle{l2submission}
    \fancypagestyle{plain}{
      \fancyhf{}
      \fancyfoot[C]{\lTwoSubmissionFooter}
      \renewcommand{\headrulewidth}{0pt}
      \renewcommand{\footrulewidth}{0pt}
    }
---

```text
Title:  Health-related emoji coverage
Authors: David Rhew; Heena Purohit; Shuhan He
Date:   2026-07-13
Action: Refer to the Emoji Standard & Research Working Group
        for review and recommendation
```

# Summary

Unicode already includes health-related emoji across anatomy, diagnostics, laboratory science, medication,
emergency care, and clinical equipment. Proposals are reviewed individually, but the same practical questions
recur: adequacy of substitutes, visual distinction at emoji size, expected usage, and open-endedness.

We ask the Unicode Technical Committee (UTC) to refer these issues to the Emoji Standard & Research Working
Group (ESR). ESR could examine how easily users can find existing health-related emoji and whether the
published guidance adequately addresses medically distinct but visually similar concepts. A referral would not
change the proposal process. Every new emoji would still require a complete submission through the official
Emoji Submission Form.

# Questions for review

1. Would considering related health emoji together help ESR assess existing substitutes and closely related
   proposals more consistently?
2. Can users readily find common health-related emoji by name, keyword, ordering, or vendor keyboard placement?
   If not, which standards body or platform team should address the problem?
3. Does the published guidance adequately address concepts that are medically distinct but may look similar at
   emoji size, such as Blood Bag and IV Bag or Pill Box and Pill Pack?
4. Would a short public note help submitters address recognition at small sizes, black-and-white legibility, and
   category-completion arguments?
5. If these issues are already covered, which guidance should submitters follow?

# Why now

Health-related emoji are distributed across several sections of the current Unicode Emoji Ordering. Syringe,
Pill, Drop of Blood, Adhesive Bandage, Stethoscope, X-Ray, and Crutch are listed under `Objects > medical`;
Anatomical Heart, Lungs, and Brain under `People & Body > body-parts`; Test Tube, Petri Dish, and DNA under
`Objects > science`; Hospital and Ambulance under `Travel & Places`; and Medical Symbol and Wheelchair Symbol
under `Symbols`. We are not proposing to move any of them. The requested review would consider what this
distribution means for discoverability, existing substitutes, and the treatment of closely related proposals.

These examples are the existing baseline for this review: health-related emoji already include medical
objects, anatomy, laboratory science, care settings, emergency transport, accessibility symbols, and health
symbols. The question is whether that baseline is clear enough for users and for submitters proposing nearby
concepts.

The question is also timely because health communication has moved further into everyday digital channels.
Pew Research Center reported in 2026 that 52% of U.S. adults under 30 get health information from social
media at least sometimes, and McKinsey's 2025 Future of Wellness survey reported that nearly 30% of U.S. Gen
Z and millennial respondents were prioritizing wellness "a lot more" than one year earlier. These trends do
not support any particular emoji on their own. They do show why users may increasingly expect common health
concepts to be represented in the same interoperable visual vocabulary used for daily communication.

Every proposal must address Unicode's published inclusion and exclusion factors, including distinctiveness,
expected usage, and whether an existing emoji or sequence already represents the concept. The proposed image
must also remain recognizable at emoji size.

The 2026 process separates individual emoji proposals from UTC discussion documents. New emoji proposals must
be filed through the Emoji Submission Form. A discussion document follows Unicode's separate document
submission process and may be placed on a UTC agenda or referred to a working group. This document follows the
UTC document submission process.

# Related history

## Apple's 2018 accessibility proposal

Apple's L2/18-080 proposed nine accessibility emoji in four areas: Blind and Low Vision, Deaf and Hard of
Hearing, Physical Motor, and Hidden Disabilities. Apple presented the set as a finite starting point rather
than a comprehensive catalogue. Apple worked with disability organizations and addressed Unicode's open-ended
exclusion factor directly.

Apple submitted the nine related concepts together under the emoji-proposal process in effect in 2018. Under
the 2026 guidance, each candidate must be submitted through the official form and evaluated on its own evidence.

Source: <https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf>

## Anatomical Heart and Lungs

In 2019, Christian Kamkoff, Shuhan He, and Melissa Thermidor submitted separate proposals for Anatomical Heart
and Lungs. Unicode later encoded both characters. The proposals were related, but each made its own case.

Sources:

- <https://www.unicode.org/L2/L2019/19149-lung-emoji.pdf>
- <https://www.unicode.org/L2/L2019/19150-heart-emoji.pdf>

# Scope of the review

We suggest six topics for the review. They are not proposed keyboard categories.

- Anatomy: How should internal-organ proposals address category completion and open-endedness?
- Diagnostics: When would CT Scan, Ultrasound, or another modality represent a procedure or object that X-Ray
  and Stethoscope do not adequately convey?
- Laboratory science: How should proposals address visual overlap among cells, microbes, specimens, and
  equipment?
- Medication: How should proposals for organizers, packaging, delivery devices, or adherence concepts establish
  that they are distinct from Pill and Syringe?
- Emergency care: When would an additional object support a broad communication need not met by Adhesive
  Bandage, Crutch, Ambulance, or Hospital?
- Clinical equipment: Which designs remain recognizable at small sizes, work without color, and avoid overlap
  with other equipment silhouettes?

A gap alone would not warrant a character, and this document does not propose a top-level Health group.

\Needspace{11\baselineskip}

# Relationship to individual proposals

Each candidate needs its own complete submission under the current form and guidelines. Required elements
include color and black-and-white images, keywords, category, frequency evidence, all selection factors, an
image-rights warranty, and the required license.

This document does not endorse or oppose any candidate. Each candidate requires a separate decision.

# Vendor input

Vendors can comment on design and implementation without committing to include a candidate in their products.
Relevant questions include:

- Can someone unfamiliar with the concept identify it at common emoji sizes?
- Does the image retain its meaning in black and white?
- Is the design platform-neutral and free of text, logos, brands, or other third-party intellectual property?
- Would two related concepts remain distinguishable in the same emoji set?
- Are there implementation or interoperability concerns that ESR should consider?

Submitters remain responsible for their evidence, licensing, and the completeness of their proposals.

# Requested action

We ask the UTC to refer this document to ESR for review and recommendation. ESR could advise that the current
guidance is sufficient and no further action is needed, or recommend a short public note or focused review.

We are asking only for referral, not character encoding or bundled approval. Every candidate must still be
submitted through the official Emoji Submission Form and reviewed independently under Unicode's published
criteria.

# References

- Unicode, Guidelines for Submitting Unicode Emoji Proposals:\
  <https://www.unicode.org/emoji/proposals.html>
- Unicode, Pending Document Submission:\
  <https://www.unicode.org/pending/docsubmit.html>
- Unicode, Emoji Ordering:\
  <https://unicode.org/emoji/charts/emoji-ordering.html>
- Apple, Proposal for New Accessibility Emoji, L2/18-080:\
  <https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf>
- Pew Research Center, "Users of social media and AI chatbots for health information are more likely to say
  they are convenient than accurate":\
  <https://www.pewresearch.org/science/2026/04/07/users-of-social-media-and-ai-chatbots-for-health-information-are-more-likely-to-say-they-are-convenient-than-accurate/>
- McKinsey & Company, "The Future of Wellness trends survey 2025":\
  <https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/future-of-wellness-trends>
