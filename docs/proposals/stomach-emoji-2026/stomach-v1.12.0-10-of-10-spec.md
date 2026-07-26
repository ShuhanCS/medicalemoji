# Stomach v1.12.0 10/10 Submission Specification

Specification version: 1.1.0

Date: 2026-07-26

Status: Ready for execution

Controlling guide:

https://github.com/ShuhanCS/medicalemoji/blob/codex/proposal-guide-2026/PROPOSAL-GUIDE.md

Companion 100-point rubric:

https://github.com/ShuhanCS/medicalemoji/blob/codex/proposal-guide-2026/docs/proposals/emoji-proposal-approval-rubric.md

## Decision

Produce a new immutable Stomach submission revision that earns 100/100 under the project's internal readiness
rubric and presents the strongest truthful case for approval. The concept, eligibility, authorship, rights,
and selected artwork direction are settled. Do not reopen them unless new contradictory primary evidence
appears.

The current v1.11.0 proposal has a strong case, a strong first page, and substantially improved art. Its remaining
work is current empirical evidence, straightforward small-size artwork checks, and final packet control. The next
revision does not need a conceptual rewrite or new art unless a technical check reveals a specific visual problem.

## Fixed facts

- **Eligibility: Pass.** Shuhan He has confirmed that Stomach is eligible for this submission cycle.
- **Authorship: Pass.** Shuhan He, MD; David Rhew, MD; and Heena Purohit are the submitters. Shuhan He is the main
  point of contact.
- **Rights: Pass.** The submitted image is project-created artwork. GPT Image 2 was used for concept
  exploration, and the filing assets were rebuilt as original deterministic SVG geometry for this project.
  Shuhan He has confirmed that the project has the rights required to submit and license the artwork.
- **One proposal, one emoji: Pass.** The document proposes only Stomach.
- **Breaks new ground: Yes.** No existing emoji or short sequence directly identifies the stomach as an organ.
- **Completeness: Not applicable.** The case must never ask Unicode to complete an anatomy set.
- **Compatibility: Not applicable.** Do not claim compatibility without evidence of an existing popular-system
  pictograph.
- **Selected art direction: Fixed unless a technical check fails.** Preserve the asymmetric J shape, long inlet,
  open inner curve, broad lower body, and distinct outlet from v1.11.0.

## Definition of 10/10

The submission is 10/10 only when it satisfies all three conditions:

1. It earns 100/100 under the internal readiness rubric below.
2. Every must-pass guide gate is complete for the exact PDF being released.
3. A page-by-page advocate review finds no stale evidence, unsupported claim, internal doubt, process note,
   layout defect, or self-defeating language in the reviewer-facing PDF.

This is a readiness standard, not a prediction that Unicode will approve the character.

## Version and artifact strategy

Do not alter the committed `submissions/v1.11.0/` packet.

1. Perform research and testing in `docs/proposals/stomach-emoji-2026/` and ignored temporary directories.
2. While any gate remains open, use `REVIEW` or `CANDIDATE` filenames, never `_SUBMIT`.
3. After every pre-publication gate passes, copy the complete canonical package to `submissions/v1.12.0/`.
4. Update package `VERSION`, `CHANGELOG.md`, `manifest.md`, `ARTWORK-LICENSE.md`, and Stomach `READINESS.md`.
5. Generate the exact `_SUBMIT.md` and `_SUBMIT.pdf` only after the content, evidence, artwork, rights, technical
   checks, and review are complete.
6. Preserve every non-Stomach file byte-for-byte from v1.11.0 unless a package-control file must change.
7. Publish and file only after Shuhan He explicitly authorizes those external actions.

## Required deliverables

The completed work must contain:

- Five current, readable frequency screenshots.
- A source ledger for every material factual or usage claim.
- A set of closest visual alternatives and a source manifest with SHA-256 hashes.
- Actual-size comparison boards for color and black-and-white at 18x18 and 72x72.
- Machine-readable artwork-check results.
- Final color and true black-and-white SVG sources and exact PNG exports.
- Current-format proposal Markdown and rendered PDF.
- A PDF technical report and page-by-page visual review record.
- A completed readiness record mapping evidence to all 100 rubric points.
- A stable public HTTPS URL, logged-out access check, form reconciliation record, and archived filing
  confirmation after filing is authorized.

## Workstream 1: current empirical evidence

Replace all four 2020 exhibits. Recapture the Ngram exhibit as well so the complete evidence set has one
consistent review date and reproducibility standard.

### Capture requirements common to all five sources

- Capture on the same calendar date where practical.
- Use a private browser window where possible.
- Keep the query, result, comparator, date, range, location, search mode, and relevant settings visible.
- Crop only to remove unrelated browser material while preserving the query, settings, and result.
- Record the complete query URL exactly as used.
- Record browser locale, capture date, viewport, and any category filter in the source ledger.
- Make every embedded figure readable at 100% PDF zoom.
- Do not use petitions, endorsements, hashtags, campaign traffic, or calls for an emoji as frequency evidence.

### Required captures

1. **Google Search:** query `stomach`; select Tools; show the result count and query.
2. **Google Video Search:** query `stomach`; show the result count and query.
3. **Google Trends - Web Search:** compare `stomach` with `elephant`; Worldwide; Web Search; widest available
   time range.
4. **Google Trends - Image Search:** compare `stomach` with `elephant`; Worldwide; Image Search; widest
   available time range.
5. **Google Books Ngram Viewer:** compare `stomach` with `elephant`; English corpus; widest supported range;
   record smoothing and corpus version.

### Evidence interpretation requirements

- Lead with the numerical or directly visible observation from each source.
- State the strongest directly visible result from each source.
- Use Trends and Ngram to support worldwide and durable interest, not merely a large raw search count.
- Cite established figurative meanings from durable dictionary sources.
- Cite or remove material claims about digestion, hunger, nausea, appetite, fullness, reflux, and emotional
  expression. Ordinary illustrative examples do not need inflated medical statistics.
- Do not add disease burden, campaign support, professional endorsements, or social-media advocacy to the
  frequency case.

### Acceptance tests

- All five screenshots have a 2026 capture date.
- Both Trends screenshots visibly show `stomach`, `elephant`, Worldwide, the search type, and widest range.
- Ngram visibly shows both terms, corpus, range, and smoothing.
- Search and Video captures visibly show the query and result count.
- Every screenshot, caption, URL, setting, and written interpretation agrees.
- Every material usage claim appears in the source ledger with a readable citation or is removed.

## Workstream 2: artwork clarity and technical checks

### Design definition

**Design sentence:** A broad, familiar human stomach represented by a bold asymmetric J shape whose inlet, open
inner curve, lower body, and outlet remain clear at emoji size.

**Essential cues:**

1. Asymmetric J-shaped outline.
2. Long connected inlet.
3. Open inner curve and visibly separate short outlet.

**Vendor freedoms:** Vendors may change angle, coral/red hue, outline weight, highlight, shading, and minor
curvature. They may not remove the inlet, close the inner curve, merge the outlet into the body, or make color
the only identifying cue.

### Closest visual alternatives

Use pinned, rights-compatible representations for:

- Beans emoji.
- Anatomical Heart emoji.
- Meat on Bone or another clearly declared food/meat emoji.
- The current Kidney proposal image.
- The current Liver proposal image.
- A simple organ/blob control created for comparison.

The manifest must identify the exact file, source URL where applicable, license basis, dimensions, and SHA-256
hash for every comparison image. If an image changes, version the check and rerun the full set.

### Comparison boards

Create four actual-size boards:

1. 18x18 color.
2. 18x18 black-and-white.
3. 72x72 color.
4. 72x72 black-and-white.

Each board must show Stomach beside every closest visual alternative on a neutral light background. Also inspect the
Stomach assets at actual size on a neutral dark background. Labels may appear outside the glyph cells for the
internal board; do not place text inside any emoji asset.

### Automated artwork checks

Create a reproducible command and machine-readable report that verifies:

- Exact 18x18 and 72x72 PNG dimensions.
- True black-and-white assets contain only `(0,0,0)` and `(255,255,255)` pixels.
- No text, alpha halo, clipped foreground, or unintended background color exists.
- The intended foreground is connected, with any exception explicitly justified.
- Every source and output file has a recorded SHA-256 hash.
- The 18x18 images remain measurably separate from every comparison image under the project's fixed checks.

These checks are internal production controls. The proposal should describe the visible J shape, inlet, open
inner curve, lower body, and outlet in ordinary language.

## Workstream 3: reviewer-facing proposal edit

Use the current 2026 heading order exactly. Keep the strongest affirmative case and remove internal process
language from the final PDF.

### Page 1

Retain:

- `Proposal for Emoji: Stomach`.
- Shuhan He, MD; David Rhew, MD; and Heena Purohit as submitters, with Shuhan He as main point of contact.
- Current revision date.
- Search-oriented keywords and `People & Body - body-parts` category.
- Four exact images at the top of the page.
- The direct ownership, CC0, and Unicode-license statement.

Improve:

- Keep the design description to one compact paragraph.
- State the essential visible cues and vendor freedom without demanding an exact vendor glyph.
- Confirm that the 18x18 samples render at actual size and the 72x72 samples remain sharp in the PDF.

### Inclusion factors

1. **Multiple meanings:** Retain only cited, established literal and figurative meanings. Lead with the
   conclusion. Do not inflate weak expressions.
2. **Use in sequences:** Use four strong combinations at most: food/meal, nausea, butterfly/nervousness, and
   pill or hospital/care. Explain the distinct message created by Stomach.
3. **Breaks new ground:** Begin `Yes.` Name Nauseated Face and food emoji as the strongest substitutes, then
   state the remaining gap: neither directly identifies the stomach organ.
4. **Distinctiveness:** Explain the J shape, inlet, open inner curve, lower body, and outlet. Keep the full
   technical record internal.
5. **Usage level:** Replace every historical exhibit and historical caption. Interpret all five current
   sources directly and confidently.
6. **Completeness:** Keep `Not applicable` and state that the proposal does not seek a complete anatomy set.
7. **Compatibility:** Keep `Not applicable` without speculative partnership language.

### Exclusion factors

1. **Already represented:** Name Nauseated Face and food emoji first. Explain that they express symptoms or
   inputs, not the organ itself.
2. **Overly specific:** Define Stomach as a broad everyday organ concept, not a disease, procedure, specialty,
   campaign, subtype, or brand.
3. **Open-ended:** State that encoding Stomach does not imply encoding liver, kidney, intestine, or every
   anatomical structure. Ground selectivity in Stomach's own demonstrated usage, established figurative
   meanings, everyday use, and clear J-shaped design.
4. **Transient:** Connect the current evidence to the long-duration Ngram record and cited durable idioms.
5. **Faulty comparison:** State that the proposal does not depend on Anatomical Heart, Lungs, Brain, or another
   organ already existing.

### Advocate edit

The final PDF must not contain:

- `historical capture`, `pending`, `blocked`, `open`, `weak`, `risk`, `review required`, `provisional`, `TODO`,
  `placeholder`, or internal readiness scores.
- Discussion of rejected artwork or failed iterations.
- Doubt about eligibility, ownership, rights, or authorship.
- Arguments based on completing anatomy, disease burden, petitions, endorsements, campaign visibility, or
  another organ's acceptance.
- Technical test methods, thresholds, hashes, or pass/fail reports.
- More prose than the supported case requires.

Every final sentence must satisfy a current field, prove a selection factor, rebut a required exclusion,
establish rights, interpret evidence, or guide vendor design.

## Workstream 4: PDF production and QA

Generate the PDF with the repository's established builder. Then perform both technical and visual review.

### Technical checks

- PDF opens without a password and is not encrypted.
- Document title is `Proposal for Emoji: Stomach`.
- Page size is US Letter unless the builder's established current standard changes.
- Fonts are embedded or subset and all text extracts correctly.
- All external links are valid, complete, and clickable.
- All local image references resolve before generation.
- The document contains no blank page, broken image, stale date, placeholder, or draft marker.
- Page numbers and section transitions are consistent.
- Screenshots remain readable at 100% zoom.
- File hash and byte size are recorded for the exact candidate and final PDF.

### Visual checks

Render every page to PNG after every meaningful PDF revision. Inspect each page at normal scale for:

- clipping, overlap, stranded headings, split labels, and excessive blank space;
- sharp 72x72 art and visible 18x18 art;
- legible evidence queries, settings, values, captions, and legends;
- consistent margins, typography, tables, headers, footers, and page numbers;
- raw URLs that wrap cleanly without disrupting the page; and
- a persuasive flow from the meaning existing emoji cannot express through empirical use and exclusion rebuttals.

Zero visual or technical defects are allowed in the final candidate.

## Workstream 5: 100-point release gate

| Area | Points | Required evidence for full credit |
| --- | ---: | --- |
| Eligibility and coordination | 15 | Eligibility treated as confirmed; one Stomach proposal; all confirmed authors listed; Shuhan He is the main contact; no known duplicate filing conflict. |
| First-page format | 10 | All current fields, four images, and rights language are correct and immediately visible. |
| Image package and rights | 15 | Rights pass and all four exact assets pass the project technical checks. |
| Frequency and empirical evidence | 20 | Five current, readable, reproducible captures plus a complete source ledger for material claims. |
| Inclusion factors | 15 | Every factor is direct and evidenced; `Breaks new ground` says Yes; Completeness and Compatibility use `Not applicable`. |
| Exclusion factors | 10 | The strongest substitutes and open-ended objection are answered specifically and concisely. |
| Worldwide and durable case | 5 | Current worldwide Trends plus long-range Ngram and durable cited meanings; no cause-only framing. |
| Validation and reproducibility | 5 | Comparison images, hashes, thresholds, and machine-readable checks reproduce cleanly. |
| Packet and filing control | 5 | Immutable versioned packet, clean exact PDF, public HTTPS URL, logged-out check, reconciled form, and archived filing record. |
| **Total** | **100** | **Every item complete for the same exact PDF and image hashes.** |

No compensating points are allowed. If an item is incomplete, do not award its points and do not describe the
submission as 10/10.

## Execution order

1. Freeze v1.11.0 inputs and record hashes.
2. Build the claim source ledger.
3. Capture and validate all five current frequency exhibits.
4. Pin the closest visual alternatives and generate actual-size comparison boards.
5. Run the automated artwork checks.
6. Apply the reviewer-facing advocate edit using the passing art and current evidence.
7. Generate a candidate PDF and perform technical plus page-by-page visual QA.
8. Obtain factual, Unicode-process, and Shuhan He approval for the exact candidate.
9. Promote the complete packet to immutable `submissions/v1.12.0/` and generate `_SUBMIT` files.
10. Re-run every automated and visual check against the promoted files and compare hashes.
11. After explicit authorization, publish the exact PDF, verify logged-out HTTPS access, reconcile and file the
    official form, and archive confirmation.

## Stop conditions

Do not promote or publish if:

- a current evidence capture is missing or unreadable;
- a required artwork check fails;
- any material claim lacks support;
- the exact PDF has not passed page-by-page review;
- candidate and promoted hashes differ unexpectedly; or
- Shuhan He has not authorized the external publication or filing action.

## Completion report

The implementer must report:

- final readiness score and evidence for every awarded point;
- proposal package version and Git commit;
- exact PDF SHA-256 hash, byte size, and page count;
- all five evidence capture dates and query URLs;
- comparator manifest and validation result;
- PDF technical and visual QA result;
- public raw HTTPS URL and logged-out result after publication; and
- official-form confirmation after filing.
