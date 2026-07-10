---
title: "Health-Related Emoji Coverage as a Standards-Maintenance Issue"
author-meta: "David Rhew, MD; Shuhan He, MD"
date-meta: "2026-07-10"
subject: "Discussion document for UTC and the Emoji Standard and Research Working Group"
geometry: margin=1in
fontsize: 10pt
---

```text
Title:  Health-Related Emoji Coverage as a Standards-Maintenance Issue
Source: David Rhew, Microsoft; Shuhan He
Date:   2026-07-10
Status: Individual Contribution
Action: For consideration by UTC; refer to ESR
```

**Status:** Final discussion document for Microsoft review and referral to the Unicode Technical Committee (UTC) and the Emoji Standard and Research Working Group (ESR).

## Executive summary

Health-related emoji coverage is now a coherent standards-maintenance problem. Health concepts are distributed across anatomy, diagnostic, laboratory, medication, emergency-care, and clinical-equipment contexts, while users and implementers encounter them as one practical communication domain. The issue is not that every medical concept should become an emoji. The issue is that the current coverage and review process does not provide a clear way to identify gaps, compare candidates, or coordinate vendor support.

This document asks the UTC to authorize ESR to review the maintenance issue and report back on the organization of the domain, prioritization criteria, procedural handling of individual concepts, and bounded vendor support for design, accessibility, rights, evidence, and anticipated implementation.

No character is requested, approved, or prioritized by this document. Each concept remains subject to the current Unicode Emoji proposal requirements, including public evidence, distinctiveness, exclusion-factor analysis, image rights, and the normal submission form.

## Why now

The 2026 Emoji proposal window is open through July 31, 2026. Several health-related concepts have prior proposal history, and the current project drafts are being rebuilt against the current evidence, image-rights, and submission requirements. A bounded maintenance review would improve process coherence while leaving every individual concept to the normal proposal process.

## Concrete UTC action requested

Microsoft respectfully asks the UTC to authorize the Emoji Standard and Research Working Group to conduct a bounded review of health-related emoji coverage and report back with recommendations on scope, prioritization criteria, and procedural handling of individual proposals. The review mandate should address the following five questions:

1. **Recognize health-related emoji coverage as a coherent standards-maintenance issue.** The domain should be assessed as a connected coverage problem even when its existing characters remain in different keyboard groups.
2. **Review how the domain is organized.** The review should examine anatomy, diagnostics, laboratory medicine, medication, emergency care, and clinical equipment, including the relationship between existing emoji and missing concepts.
3. **Establish criteria for prioritizing missing concepts.** Criteria should include broad and reproducible usage evidence, distinctiveness, multiple durable meanings, combinability, category completion, non-duplication, visual legibility, accessibility, rights readiness, and implementation feasibility.
4. **Refer individual concepts to the normal Emoji proposal process.** A coverage review must not become a bundled encoding request. Kidney, liver, stomach, EKG/ECG, white blood cell, Pill Box, Inhaler, First Aid Kit, Blood Bag, IV Bag, Leg Cast, Weight Scale, and any other concept must be evaluated in its own complete submission.
5. **Clarify vendor support.** Vendors may contribute design review, accessibility testing, rights and provenance information, evidence reproducibility, and anticipated implementation planning without asking the Consortium to adopt vendor artwork or pre-commit to encoding.

The requested outcome is an ESR recommendation and documented review framework, not automatic approval. The UTC need not decide every candidate in the same meeting.

## Two-track structure

**Track A - standards maintenance.** ESR reviews the organization of existing health-related emoji, the six-domain coverage framework, prioritization criteria, and any process recommendations that should be reported to the UTC.

**Track B - individual proposals.** Each candidate is prepared and submitted as a separate, complete Unicode Emoji proposal. Track B does not depend on creation of a new category, and Track A does not pre-approve any candidate.

## Scope of the maintenance review

The review should use a coverage matrix with six domains:

| Domain | Existing examples | Gap questions |
| --- | --- | --- |
| Anatomy | brain, anatomical heart, lungs, tooth, mechanical limbs | Are major internal organs and body systems represented distinctly enough for ordinary communication? |
| Diagnostics | x-ray, stethoscope, thermometer-related face | Are common diagnostic modalities and readings represented without over-specific device branding? |
| Laboratory medicine | test tube, petri dish, DNA, microbe | Are specimen, cell, blood, and laboratory concepts organized coherently? |
| Medication | pill, syringe, drop of blood | Are medication-use concepts such as Pill Box and Inhaler independently useful and visually distinct? |
| Emergency care | adhesive bandage, crutch, ambulance, hospital | Are first-response objects and care actions represented as broad paradigms rather than logos? |
| Clinical equipment | stethoscope, x-ray, crutch | Which equipment concepts have broad public use, a clear silhouette, and no existing substitute? |

The matrix is an analytical tool. It does not imply that every row or gap should produce a character.

## Prioritization framework

Each candidate should receive a documented assessment against the following factors, with evidence attached to its own proposal:

1. **Independent concept:** the candidate represents a recognizable entity or activity not already represented by an existing emoji or sequence.
2. **Multiple durable uses:** the concept supports ordinary, educational, public-health, clinical, or metaphorical communication beyond one narrow diagnosis or campaign.
3. **Distinctive visual paradigm:** a non-specialist should identify it at 18x18 without relying on text, a logo, or exact vendor artwork.
4. **Evidence of usage:** the proposal supplies the current Unicode evidence set and explains query disambiguation and reproducibility.
5. **Category completion:** the candidate fills a meaningful gap in an existing family without arguing for an open-ended taxonomy.
6. **Combinability:** the candidate supports useful sequences with existing emoji, while no sequence is requested as part of encoding.
7. **Non-duplication and exclusion control:** the proposal addresses already represented, overly specific, open-ended, transient, and existing-emoji-substitute concerns.
8. **Accessibility:** color is not the only carrier of meaning; the silhouette and essential cues survive small-size and black-and-white review.
9. **Rights readiness:** all submitted example images have an ownership, assignment, public-domain, or compatible open-license chain.
10. **Implementation readiness:** vendors can evaluate the paradigm without being asked to adopt a prescribed design.

No single factor decides a candidate. A high-profile medical endorsement cannot substitute for public frequency evidence, and a high search count cannot cure an indistinct or overly specific design.

## Relationship to individual submissions

The individual submission is the operative Unicode artifact. Each packet must be complete on its own and publicly accessible as a PDF. The L2 document may explain why the domain deserves a coordinated review, but it cannot carry missing evidence for a candidate.

For each proposed concept, the packet must include the required title, submitter and date, identification, keywords and category, images, inclusion factors, exclusion factors, other information, and the image-rights warranty required by the current Unicode guidelines. The packet must include its own frequency screenshots for Google Search, Google Video Search, Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer, or a clearly justified reproducible substitute where a required source is unavailable.

The current project drafts and evidence work are inputs, not substitutes for the final packet. Every TODO, placeholder, pending screenshot, unresolved rights statement, and unverified eligibility date is a release blocker.

## Vendor participation model

Vendor participation should be optional, transparent, non-binding, and non-exclusive. It should be bounded to:

- review whether a candidate remains legible at common emoji sizes;
- test color and black-and-white paradigms for accessibility;
- identify ambiguous cues, misleading clinical details, and platform-neutral alternatives;
- confirm that example images can be licensed under the Consortium's requirements;
- provide anticipated implementation considerations without promising adoption; and
- return technical comments through the normal UTC/ESR process.

Vendor review is not a vote, a frequency statistic, a substitute for Unicode evidence, a request for exact artwork, an exclusive endorsement, or a commitment to ship an encoded character.

## Requested referral and working-group action

Microsoft respectfully asks that this document be routed to ESR for the bounded review described above. Microsoft further asks that any associated individual proposal materials be reviewed through the ordinary Emoji process on their complete technical merits, including evidence, distinctiveness, public utility, image rights, accessibility, and anticipated vendor-support considerations. Microsoft sponsorship does not constitute evidence of usage, eligibility, or likely acceptance.

The requested working-group output is a recommendation on the maintenance framework and procedural handling of the individual concepts. The working group need not decide every candidate in the same meeting, and no candidate should advance without a complete packet.

## Boundaries and safeguards

- This is not a request for a top-level Health group as a prerequisite to encoding.
- This is not a request to encode a comprehensive anatomy taxonomy.
- This is not a bundled submission or a request to bypass the normal Emoji proposal form.
- Professional society letters provide legitimacy and domain context; they are not frequency evidence.
- Medical prevalence, clinical importance, and patient need explain durability and utility; they do not replace Unicode's required usage evidence.
- Eligibility for a previously declined concept must be checked against Unicode's operative date rule immediately before filing.
- No submitted artwork should be treated as required vendor artwork.

## References

- Unicode, Guidelines for Submitting Unicode Emoji Proposals: https://www.unicode.org/emoji/proposals.html
- Unicode, Pending Document Submission: https://www.unicode.org/pending/docsubmit.html
- Unicode, Emoji Submission Form: https://forms.gle/6KSiYHrUdBkTMNaB8
