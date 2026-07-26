# Medical Emoji Submission Package v1.9.0

Package version: 1.9.0

Created: 2026-07-26

Status: **Kidney authorship review snapshot. Not ready to submit.**

Official deadline: End of day 2026-07-31

Official guidelines:

https://www.unicode.org/emoji/proposals.html

## Package contents

| Component | Component version/provenance | Status in v1.9.0 |
| --- | --- | --- |
| Ideal proposal template | Template 1.0.0, derived from the accepted/declined proposal audit | Carried forward byte for byte from v1.8.0 |
| Best-in-class rubric | Rubric 2.3 | Authorship control updated for the ten-person Kidney list |
| White Blood Cell | Submission package v1.8.0 | Complete folder carried forward byte for byte; evidence-gated draft |
| Kidney | Submission package v1.9.0 | David Rhew and Heena Purohit added; review gates remain open |
| Stomach | Submission package v1.8.0 | Complete folder carried forward byte for byte; revision required |
| Liver | Submission package v1.8.0 | Complete folder carried forward byte for byte; revision required |
| Artwork license | Package 1.8.0 | Carried forward byte for byte without expanding the rights record |

Folder layout:

```text
submissions/v1.9.0/
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

1. White Blood Cell - Shuhan He only.
2. Kidney - Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee;
   Danielle Miller; Timur Erk; David Rhew; Heena Purohit.
3. Stomach - Shuhan He only.
4. Liver - Shuhan He only.

Shuhan He is the main point of contact for all four proposals.

## Immutable semver snapshot rule

Every package update creates a new complete `submissions/vMAJOR.MINOR.PATCH/` folder. Never modify a committed
submission-version folder in place.

- `PATCH`: Non-substantive formatting, typo, filename, packaging, or metadata correction that changes no claim,
  evidence interpretation, artwork paradigm, rights statement, or submission decision.
- `MINOR`: Backward-compatible substantive improvement, including proposal prose, citations, evidence captures,
  artwork, generated PDFs, template/rubric changes, or adding/removing a pre-filing candidate.
- `MAJOR`: Incompatible filing-history or legal transition, such as replacing an already submitted package,
  changing controlling ownership/licensing, or restructuring the package so prior review records cannot be
  compared directly.

For every new version:

1. Copy the entire latest package to the new semver folder.
2. Copy every untouched file byte for byte; do not recreate or reformat it.
3. Change only the files required for that version's work.
4. Rebuild a proposal PDF only when its source or embedded asset changed.
5. Update `VERSION`, this manifest, and `CHANGELOG.md` in the new folder.
6. Record each changed component and the source version of each carried-forward component.
7. Verify copied-file hashes, local links, image dimensions, and PDF integrity before committing.

The next substantive proposal correction after this snapshot will therefore create `submissions/v1.10.0/` by
copying all of v1.9.0 and changing only the reviewed proposal plus package control files.

## Current readiness gates

- White Blood Cell: refresh Search and Video; replace Web Trends and add Image Trends against `elephant`; pass
  18x18 recognition against Microbe and generic-cell imagery.
- Kidney: obtain and archive consent from all ten named submitters; pass the 18x18 recognition/nearest-emoji
  comparison; strengthen citations; correct the rendered page flow.
- Stomach: refresh four 2020 evidence captures and pass recognition/comparison review.
- Liver: replace four 2020 captures, including U.S.-only Trends; improve the small black-and-white paradigm and
  citations.
- All four: complete proposal-level audit, rendered-page inspection, public logged-out PDF URL, exact form
  reconciliation, final authorization, and archived submission confirmation.

One-by-one review specification:

https://github.com/ShuhanCS/medicalemoji/blob/codex/eligible-2026-slate/docs/proposals/2026-submission-slate-spec.md
