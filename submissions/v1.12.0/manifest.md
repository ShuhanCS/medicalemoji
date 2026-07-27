# Medical Emoji Submission Package v1.12.0

Package version: 1.12.0

Created: 2026-07-26

Status: **White Blood Cell panel corrections complete; publication verification in progress.**

Official deadline: End of day 2026-07-31

Official guidelines:

https://www.unicode.org/emoji/proposals.html

## Package contents

| Component | Component version/provenance | Status in v1.12.0 |
| --- | --- | --- |
| Ideal proposal template | Template 1.0.0 from v1.11.0 | Carried forward byte for byte |
| Best-in-class rubric | Rubric 3.0.0 from v1.11.0 | Carried forward byte for byte |
| White Blood Cell | Submission package v1.12.0 | Representative-neutrophil disclosure, standards-based use evidence, bounded follow-on analysis, historical-case revision, and corrected cross-renderer output |
| Kidney | Submission package v1.10.0 | Carried forward byte for byte |
| Stomach | Submission package v1.9.0 | Carried forward byte for byte |
| Liver | Submission package v1.9.0 | Carried forward byte for byte |
| Artwork license | Package v1.12.0 | White Blood Cell paradigm provenance clarified; image rights unchanged |

Folder layout:

```text
submissions/v1.12.0/
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

This snapshot copies v1.11.0 and changes only the White Blood Cell component, the artwork and validation
helpers, and package control files.

## Completion record

- Four exact-size assets and editable sources: complete; computer validation passes.
- Comparison boards and pinned comparator provenance: complete.
- Web Trends, Image Trends, and Google Books Ngram: captured and documented on 2026-07-26.
- Google Search and Video plus matching `elephant` pages: captured and documented in Firefox Private Browsing
  on 2026-07-26.
- Proposal PDF: rebuilt, technically validated, and visually inspected using both Cairo and Splash renderers.
- Frequency screenshots: normalized losslessly to RGB so the PDF renders consistently across Poppler backends.
- Case-building review: accepted Fingerprint and declined 2020 White Blood Cell lessons applied; generic case
  phrases replaced with the candidate-specific host-cell communication gap.
- Public logged-out URL: recorded after the release commit is pushed.
- Form filing and confirmation archive: intentionally not performed in this workstream.
