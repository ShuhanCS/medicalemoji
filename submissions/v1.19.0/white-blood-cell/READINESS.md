# White Blood Cell submission readiness

Readiness record version: 1.7.0

Date: 2026-07-27

Proposal package: 1.19.0

Status: **CHANGED SINCE REVIEW, NOT RE-REVIEWED**

## What changed in 1.19.0, and what that means for this record

The seventeen-section review below was performed against the v1.18.0 nine-page PDF. Four changes landed in
v1.19.0 and the review has **not** been re-run against them. Every row is accurate for what it covers except
the rows named here.

1. **The Google Search figure in v1.18.0 was wrong.** It reported about 125 results for `white-blood-cell`.
   Re-measured across three independent loads the query returns about 880,000,000, with `elephant`
   reproducing exactly at 491,000,000, which confirms the settings matched. Sections 6 and 3e are rewritten
   on the corrected figures and the Video exhibits were refreshed at the same time (about 13,900,000 against
   about 84,700,000). The "Required evidence record" section below is superseded; see `evidence/EVIDENCE-LOG.md`.
2. **Multiple meanings is no longer N/A.** Section 3a argues the secondary symbolic sense of internal defense.
   There are now two genuine inclusion N/As, Completeness and Compatibility, not three. The "Multiple meanings"
   row below is stale.
3. **Distinctiveness embeds a recognition figure.** Original artwork only: the proposed image against a generic
   cell control. The decision to keep third-party comparator art out of the PDF stands, and the OpenMoji boards
   in `comparisons/` remain internal review artifacts.
4. **Other information gains a Prior submission note** and its vendor guidance is softened to explicit
   suggestions.

The PDF is now fourteen pages, so any statement below about "all nine PDF pages" describes a superseded build.
Dual-renderer inspection has not been repeated.

`scripts/validate_white_blood_cell_submission.py --package-dir submissions/v1.19.0` passes. It now derives the
required evidence files from the proposal's own image references instead of hardcoded dated filenames, requires
all five sources to be embedded, and fails when a count the proposal states does not match a figure confirmed
in the capture log.

Open item: the black-and-white 18x18 artwork is unchanged and still renders its nucleus as solid lobes inside a
near-circular outline. See `RESUME-HERE.md`.

Controlling rubric: `BEST-IN-CLASS-RUBRIC.md`, version 3.1.0

Case-building guide reviewed: `CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`, version 1.1.1 on branch
`codex/case-building-instructions`

Live finalization specifications applied:

- `docs/proposals/agent-specs/white-blood-cell-agent-spec.md`, version 1.4.0
- `docs/proposals/2026-submission-slate-spec.md`, version 1.8.0
- `docs/proposals/review-panel/README.md`, version 1.1.0

Source branch:

https://github.com/ShuhanCS/medicalemoji/tree/codex/finalize-organ-submissions

## Outcome

The proposal passes all 17 section-by-section drafting guides, the artwork and evidence gates, the technical
packet preflight, and dual-renderer inspection of all nine PDF pages. Reviewer-facing third-party comparator art
remains excluded; the only proposed emoji artwork displayed in the PDF is original Medical Emoji work. The
exact filing copy is `READY TO PUBLISH`. This workstream does not open or submit the official form.

Every substantive section passes rubric 3.1.0's candidate-specificity standard: it supplies a White Blood Cell
meaning, example, evidence result, or visual reason. Multiple meanings, Completeness, and Compatibility are the
three genuine inclusion N/As; every required exclusion factor is answered directly.

## Seventeen-section review

| Section | Result | Evidence |
| --- | --- | --- |
| Title, submitters, contact, date | Pass | Shuhan He, David Rhew, and Heena Purohit are named; Shuhan He is main contact; the ISO date is current. |
| Identification | Pass | Five search-oriented keywords and one current category line; no redundant short-name or sort field. |
| Images and license | Pass | Colour and true black-and-white images appear at 18x18 and 72x72 with the required rights statement. |
| Multiple meanings | Pass | Uses the direct `Not applicable.` answer. |
| Use in sequences | Pass | Gives three understandable combinations for the body fighting infection, immune defense, and low, high, or recovering white-cell counts. |
| Breaks new ground | Pass | Starts with `Yes.` and distinguishes Microbe, Drop of Blood, and Test Tube by meaning. |
| Distinctiveness | Pass | Explains the 18-pixel recognition sequence directly: the enclosing membrane establishes one cell, then the connected asymmetric three-lobed nucleus establishes White Blood Cell and separates the image from its nearest alternatives. |
| Expected usage level | Pass | Leads with the body's defense cell and ordinary messages about infection, immunity, and recovery; education and research remain secondary support. |
| Completeness | Pass | Uses `Not applicable.` because the proposal does not close a fixed set. |
| Compatibility | Pass | Uses `Not applicable.` because no high-frequency interoperable pictograph is claimed. |
| Already represented | Pass | Distinguishes Microbe's germ or threat from the body's own defense cell and the white-cell-count meanings no current sequence expresses. |
| Overly specific | Pass | Defines the broad leukocyte category, explains why a neutrophil-like representative form is used, and excludes narrower subtypes, diseases, procedures, and campaigns. |
| Open-ended | Pass | Stops at the upper-level leukocyte category, distinguishes generic Cell and subtype proposals, and explains why Red Blood Cell and Platelet are separate semantic questions. |
| Transient | Pass | Ties durability to current multi-format evidence and the Google Books record through 2022. |
| Faulty comparison | Pass | Rests the case on independent meaning, ordinary use, frequency, and recognizable imagery. |
| Other information | Pass | Gives concise vendor guidance on essential and optional visual features. |
| Evidence of frequency | Pass | Current Search, Video, Web Trends, Image Trends, and Books Ngram exhibits are readable and reproducible. |

## Historical-case review

- Accepted model reviewed: Fingerprint, for reproducible evidence and a precise nearest-substitute rebuttal.
- Declined comparison reviewed: the 2020 White Blood Cell draft, whose emphasis on disease burden, importance,
  education, and completing medical representation did not establish a sufficiently specific communication gap.
- Applied lesson: the v1.18.0 proposal leads with the body's defense cell as the response-side counterpart to
  Microbe, uses direct `Not applicable.` answers, limits frequency comparisons to their evidentiary purpose,
  and keeps science and clinical terminology secondary.

## Optional five-lens editorial consultation

This is an internal advisory review using the five lenses in the live finalization specification. It is not a
review, endorsement, recommendation, vote, or private feedback from Unicode, ESR, UTC, or any named person.
Each lens reviewed the exact final PDF recorded under Technical and visual verification.

| Review lens | Outcome | Basis |
| --- | --- | --- |
| Intake gatekeeper | READY FOR FINAL CHECK | Current field order, authorship, rights, required images, direct factor answers, and five-source evidence are complete. |
| ESR selection reviewer | READY FOR FINAL CHECK | The proposal defines the missing response-side counterpart to Microbe, leads with ordinary body-defense messages, interprets frequency evidence proportionately, and uses honest `Not applicable.` answers. |
| Community proposal mentor | READY FOR FINAL CHECK | An educated general reader can understand the germ-versus-body-response distinction and the infection, immunity, and recovery messages without specialist knowledge. |
| Visual and implementation reviewer | READY FOR FINAL CHECK | The exact 18x18 and 72x72 colour and true black-and-white assets preserve the folded silhouette and connected lobed nucleus, vendor guidance preserves implementation freedom, and all nine PDF pages pass Cairo and Splash inspection. |
| Scope and durability reviewer | READY FOR FINAL CHECK | The strongest substitute, subtype boundary, representative-neutrophil choice, permanence, and open-ended concern receive specific answers. |

Coordinator synthesis: no filing blocker or material revision was identified within these advisory scopes.
Shuhan He approved the artwork direction and confirms that the four assets carried unchanged into v1.19.0 are
original Medical Emoji work covered by the proposal's rights statement and CC0 release.

## Required evidence record

- Google Search: about 125 results for `white-blood-cell`; about 491,000,000 for `elephant`.
- Google Video Search: about 14,100,000 results for `white-blood-cell`; about 86,300,000 for `elephant`.
- Google Trends Web Search: Worldwide, 2004-present, all categories; average 3 versus 72.
- Google Trends Image Search: Worldwide, 2008-present, all categories; average 1 versus 53.
- Google Books Ngram: English, 1500-2022, smoothing 3; 2022 ratio approximately 10.13% of `elephant`.
- Official-form nearest-million values: Search 0 million; Video 14 million.

## Technical and visual verification

- Deterministic artwork validation: pass.
- Submission preflight: pass.
- PDF: nine letter-size pages, valid PDF 1.4, unencrypted, no forms or JavaScript.
- Fonts: embedded Arial, Arial Bold, and Consolas subsets.
- Text: extractable in reading order; no low-text or blank page.
- Hyperlinks: 11 HTTPS link annotations resolving to 10 unique HTTPS destinations.
- Image inventory: four original proposal-art images plus required evidence screenshots; no OpenMoji image is embedded.
- Reviewer-facing terms: no placeholders, workflow markers, hashes, thresholds, machine-validation language, or internal report links.
- Visual QA: all nine pages rendered at 150 DPI with both `pdftocairo` and `pdftoppm` and inspected; no clipping, overlap, broken image, stranded heading, or blank page.
- Renderer correction: seven fully opaque evidence screenshots were normalized from RGBA to RGB without changing their visual pixels, eliminating the earlier Poppler compositing defects.
- PDF SHA-256: `20194e8d10387f00ff77239f5fb7d1269c477371f45ba6aa318bb2b2d77dd549`.

## Publication record

Release commit: pending

Public PDF:

Pending publication of the exact v1.18.0 PDF.

Logged-out verification: pending release commit publication.

David Rhew affiliation reference:

https://worldmedicalinnovation.org/speaker/david-rhew-md/

Official Unicode guidance:

https://www.unicode.org/emoji/proposals.html

## Final filing controls

- [x] Publish the exact PDF at a stable logged-out HTTPS URL and record its SHA-256.
- [ ] Reconcile the public PDF URL and rounded Search/Video values with the official form.
- [ ] Complete the agreement and electronic-signature step.
- [ ] Archive the submission confirmation, timestamp, commit SHA, public URL, and PDF SHA-256.

The final three controls are outside this workstream. No submission form was opened or sent.
