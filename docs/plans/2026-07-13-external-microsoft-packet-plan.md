# External Microsoft review packet rewrite plan

Date: 2026-07-13

## Audience

The packet is for David Rhew and Microsoft standards, design, product, accessibility, and legal reviewers who have not followed the Medical Emoji project's internal planning. It must explain the available proposals, the evidence behind the ranking, and the specific help requested without assuming prior context.

## Problem to correct

The current v6 deck calls the decision "narrow" and presents Ultrasound, CT Scan, and the three organ proposals without first showing the broader eligible slate. Pill Box, Pill Pack, Blood Bag, Weight Scale, White Blood Cell, Inhaler, IV Bag, Leg Cast, Maze, and First Aid Kit are available in the repository, but they were omitted because of evidence gaps, overlap with existing emoji, design questions, or lower expected usage. That reasoning belongs in the packet. Without it, the recommendation looks arbitrary.

## Rewrite decisions

- Present every available proposal and separate eligibility from submission readiness and strategic strength.
- Treat CT Scan, Blood Bag, and Pill Box as working re-eligible packets that contain all five evidence categories, while stating clearly that all three require revision before filing.
- Present Ultrasound and Weight Scale as promising candidates that still need current Google evidence and small-size design review.
- Explain why Pill Pack is not currently recommended: it lacks the required Trends evidence and overlaps both Pill and Pill Box.
- Keep Kidney, Stomach, and Liver visible as future-cycle work, not as options for the July 2026 intake unless Unicode confirms eligibility.
- State Shuhan's plan to submit CT Scan and Blood Bag after revision, with Pill Box as the first alternate. Ask Microsoft for technical and design review and for help with the two Unicode process questions; do not ask Microsoft to make the filing decision.
- Remove internal planning terms such as "gate," "conditional lead," "fallback," "cold-test," and "portfolio boundary" unless plain-language context is supplied.
- Apply the `humanizer` skill to every reader-visible sentence: remove AI-style symmetry, defensive process language, promotional claims, over-formatting, and unexplained jargon. Preserve concrete dates, evidence gaps, and source links.

## Deliverables

1. Rewrite the Microsoft review deck and export a new external-review PPTX and PDF.
2. Rewrite the decision brief as a short slate review rather than a pre-decided lead/fallback memo.
3. Rewrite the product/legal review sheet so it can be used with any selected proposal.
4. Rewrite the Rhew email to explain the attachments and ask whether Microsoft's representatives would seek an ESR agenda discussion through the normal review process and whether its standards team would help revise the separate UTC discussion draft.
5. Mark the v6 internal deck as superseded and update current repository pointers.
6. Render and inspect every page and slide, run the final humanizer anti-AI pass, validate the files, bump the project version, commit, and push.

## Semantic version decision

This is a substantive rewrite of the current Microsoft review packet and its public-facing standards draft. Bump the project version from `0.25.0` to `0.26.0`. The proposal release remains `v1.7.0` because this task does not change an individual proposal packet.

## Quality checks

- A new reader can see why Pill Box is included in the review but Pill Pack is not currently recommended.
- Every available proposal appears once with an accurate status.
- The packet distinguishes "all five evidence categories present" from "ready to file."
- The four files with weak small-size artwork remain labeled working proposals; the packet asks Microsoft for design review rather than calling the artwork final.
- No sentence implies Microsoft sponsorship, authorship, endorsement, or implementation.
- No affiliations are added to author or submitter lines.
- The final recommendation is presented as Shuhan He's recommendation, not as an established Microsoft decision.
