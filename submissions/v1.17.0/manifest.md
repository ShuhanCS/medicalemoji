# Medical Emoji Submission Package v1.17.0

Package version: 1.17.0

Created: 2026-07-26

Status: **White Blood Cell v1.17.0 release published and verified.**

Official deadline: End of day 2026-07-31

Official guidelines:

https://www.unicode.org/emoji/proposals.html

## Package contents

| Component | Component version/provenance | Status in v1.17.0 |
| --- | --- | --- |
| Ideal proposal template | Template 1.0.0 from v1.11.0 | Carried forward byte for byte |
| Best-in-class rubric | Rubric 3.1.0 | Adds the candidate-specificity standard and explicitly covers White Blood Cell |
| White Blood Cell | Submission package v1.17.0 | New organic artwork and concise candidate-specific prose |
| Kidney | Submission package v1.10.0 | Carried forward byte for byte |
| Stomach | Submission package v1.9.0 | Carried forward byte for byte |
| Liver | Submission package v1.9.0 | Carried forward byte for byte |
| Artwork license | Package v1.17.0 | New original White Blood Cell source geometry and exports released under CC0 |

Folder layout:

```text
submissions/v1.17.0/
|-- VERSION
|-- manifest.md
|-- CHANGELOG.md
|-- ARTWORK-LICENSE.md
|-- IDEAL-EMOJI-PROPOSAL-TEMPLATE.md
|-- BEST-IN-CLASS-RUBRIC.md
|-- white-blood-cell/
|-- kidney/
|-- stomach/
`-- liver/
```

## Fixed 2026 slate

1. White Blood Cell - Shuhan He; David Rhew; Heena Purohit.
2. Kidney - Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee;
   Danielle Miller; Timur Erk; David Rhew; Heena Purohit.
3. Stomach - Shuhan He only.
4. Liver - Shuhan He only.

Shuhan He is the main point of contact for all four proposals.

## Immutable semver snapshot rule

Every package update creates a complete `submissions/vMAJOR.MINOR.PATCH/` folder. Untouched files are copied
byte for byte from the preceding package. Substantive proposal prose, citations, evidence captures, artwork,
generated PDFs, or validation changes require a MINOR release.

This snapshot copies v1.16.0 and changes the White Blood Cell colour and black-and-white artwork, editable
sources, internal artwork QA, reviewer-facing proposal and PDF, helper usage examples, and package control files.
The rubric and five mandatory frequency exhibits remain unchanged.

The White Blood Cell package applies the live `finalize-organ-submissions` White Blood Cell agent specification
1.4.0, submission slate specification 1.8.0, and advisory review-panel guidance 1.1.0. Panel notes are internal
editorial consultation only; they do not claim a Unicode review, score, vote, or endorsement.

## Completion record

- Four exact-size assets and editable sources: complete; computer validation passes.
- Comparison boards and pinned comparator provenance: retained for internal QA and excluded from the proposal PDF.
- Web Trends, Image Trends, and Google Books Ngram: captured and documented on 2026-07-26.
- Google Search and Video plus matching `elephant` pages: captured and documented in Firefox Private Browsing
  on 2026-07-26.
- Proposal PDF: rebuilt, technically validated, and visually inspected using both Cairo and Splash renderers.
- Frequency screenshots: normalized losslessly to RGB so the PDF renders consistently across Poppler backends.
- Artwork review: the folded membrane and connected asymmetric three-lobed nucleus remain legible at 18x18 in
  colour and true black and white, and deterministic comparison checks pass.
- Editorial review: Distinctiveness, Already represented, Overly specific, and Other information use concrete
  visible cues and ordinary messages without repeated technical framing.
- Supplemental evidence decision: the optional `white-blood-cell-count` query is not included because a
  reproducible result clearly stronger than the mandatory exhibits was not verified.
- Public logged-out URL: verified against release commit `67bb59e2a7c1659377eb4d61b6cde2dcc30516f4`:
  https://raw.githubusercontent.com/ShuhanCS/medicalemoji/67bb59e2a7c1659377eb4d61b6cde2dcc30516f4/submissions/v1.17.0/white-blood-cell/white-blood-cell_emoji_proposal_SUBMIT.pdf
- Form filing and confirmation archive: intentionally not performed in this workstream.
