# White Blood Cell rubric 3.0.0 correction specification

Specification version: 1.0.0

Date: 2026-07-26

Status: **Document published; official form filing in progress**

Target proposal package: `submissions/v1.11.0/white-blood-cell/`

Target project version: `0.42.0`

Controlling rubric: exact version 3.0.0 blob `29c824366ef3a30c507063cecb33da46e536fa30` from commit
`5c0700b`, stored in `docs/proposals/emoji-proposal-approval-rubric.md` and
`submissions/v1.11.0/BEST-IN-CLASS-RUBRIC.md`.

Repository:

https://github.com/ShuhanCS/medicalemoji

## Locked decisions

- The proposal is for the broad White Blood Cell concept.
- Submitters are Shuhan He, David Rhew, and Heena Purohit.
- Shuhan He is the main point of contact and the person making the artwork ownership and license statement.
- Eligibility, coordination, permission to publish, and artwork rights are confirmed.
- `Breaks new ground` remains `Yes`.
- Multiple meanings, Completeness, and Compatibility remain `Not applicable`.
- The submitted PDF is an affirmative reviewer-facing case. Internal scores, workflow narration, failed
  iterations, blockers, hashes, thresholds, and machine-validation terminology stay outside it.
- The deterministic artwork, pinned comparator sources, machine-readable validation output, and actual-size
  comparison boards remain part of the reproducible project record.

## Current state

Complete:

- four exact-size White Blood Cell images and four editable SVG sources;
- true black-and-white exports;
- colour and black-and-white actual-size comparison boards;
- deterministic validation against Microbe, Drop of Blood, Soap, Bubbles, and a generic-cell control;
- Google Trends Web, Google Trends Image, and Google Books Ngram evidence captured on 2026-07-26;
- affirmative factor and exclusion structure;
- three-author proposal metadata and Shuhan He as main contact;
- artwork rights statement.

Evidence session completed:

- Firefox Private Browsing captured current Google Search and Video pages for White Blood Cell and `elephant`
  with visible result counts;
- exact displayed counts are recorded in the proposal and evidence log;
- nearest-million form values are recorded separately in the evidence log.

## Correction 1: synchronize the controlling rubric

The repository contained three rubric versions at the start of this review:

- canonical `medicalemoji` worktree: 3.0.0;
- active proposal worktree: 3.1;
- packaged `submissions/v1.11.0/BEST-IN-CLASS-RUBRIC.md`: 2.4.

Use rubric 3.0.0 for this proposal review and make the final packet internally consistent:

1. Copy the canonical 3.0.0 rubric into the active worktree's rubric location.
2. Copy the same file into `submissions/v1.11.0/BEST-IN-CLASS-RUBRIC.md`.
3. Update package manifest and changelog provenance to rubric 3.0.0.
4. Verify the two copied rubric files are byte-identical to the canonical source.
5. Do not blend the 3.1 wording into the 3.0.0 file during synchronization.

## Correction 2: simplify the first-page metadata

Update `white-blood-cell_emoji_proposal_SUBMIT.md`:

1. Keep the exact title, three submitter names, main contact, and ISO revision date.
2. Keep credentials and affiliations compact; do not add biographies, endorsements, or institutional claims.
3. Remove the separate `CLDR short name` line because the 2026 format does not require it.
4. Keep exactly five search-oriented keywords that do not repeat `white`, `blood`, or `cell`:
   `leukocyte; immunity; infection; inflammation; laboratory`.
5. Keep one category line using current Emoji Ordering vocabulary.
6. Remove the optional sort-location line to reduce first-page reviewer effort.
7. Preserve the four-image matrix and rights paragraph at the top of page 1.

Acceptance:

- the reviewer can identify concept, authors, contact, date, keywords, category, four images, and rights without
  leaving page 1;
- no author biography or campaign history appears.

## Correction 3: rewrite Distinctiveness for a general reader

The current section incorrectly exports internal validation language. Remove these reviewer-facing terms and
ideas:

- deterministic comparison checks;
- declared thresholds;
- pinned-source record;
- machine-readable results;
- validation-report promotion;
- hashes, IoU, difference hash, connected-component statistics, or pass/fail pipeline language.

Replace the section with the rubric 3.0.0 drafting pattern:

1. State the visible paradigm: pale irregular cell body and one connected three-lobed nucleus.
2. State the nearest visual alternatives: Microbe, Drop of Blood, Bubbles, and a generic cell.
3. Explain the visible separation at 18 pixels: no spikes, no teardrop silhouette, no separate bubbles, and no
   face-like arrangement.
4. State vendor freedoms: shading, membrane contour, lobe proportions, and fine detail may vary.
5. State essential cues: irregular body plus one bold connected multi-lobed nucleus.
6. Retain the colour and black-and-white actual-size comparison boards as visual exhibits.
7. Credit the OpenMoji comparator artwork in one concise exhibit note with its license URL; do not turn the
   attribution into a validation narrative.

The validation report and source provenance remain in `validation/` and `comparisons/SOURCES.md`, linked from
the repository documentation rather than promoted in the proposal argument.

## Correction 4: tighten the inclusion factors

### Multiple meanings

Replace bare `N/A.` with `Not applicable.`

### Use in sequences

Keep only the three strongest combinations:

- White Blood Cell + Microbe: immune response to infection;
- White Blood Cell + up or down arrow: high or low white-cell count;
- White Blood Cell + Test Tube: blood count, laboratory testing, or research.

Move the NCI and MedlinePlus factual background out of this section so the sequence answer remains direct.

### Breaks new ground

Keep `Yes.` first. Preserve the ordinary-language contrast:

- Microbe expresses an organism;
- Drop of Blood expresses blood as a fluid;
- Test Tube expresses a container or laboratory activity;
- none expresses a human immune cell, white-cell count, or host defense cell.

### Expected usage level

Move the NCI and MedlinePlus sources here. Use them only to establish durable communication contexts, not
medical importance. After Search and Video capture:

1. synthesize breadth across routine laboratory testing, immunity, infection, treatment monitoring,
   education, and research;
2. state the displayed Search and Video estimates accurately;
3. state that result inventories estimate indexed pages, not users or emoji demand;
4. state that Trends and Ngram are below `elephant` while remaining sustained over the available record;
5. avoid disease prevalence, organizational reach, or professional prestige as selection evidence.

### Completeness and Compatibility

Use the exact answer `Not applicable.` for each. Completeness may retain one short sentence stating that White
Blood Cell is independently useful and does not close a fixed set.

## Correction 5: strengthen and normalize the exclusion factors

1. Rename `Already representable` to `Already represented`.
2. Keep the strongest substitute, `Microbe + Shield`, and explain that it can suggest protection from a germ
   but cannot express a leukocyte, white-cell count, or laboratory finding.
3. Keep Overly specific at the broad leukocyte category; do not argue from medical importance.
4. Strengthen Open-ended by naming the likely follow-ons: Red Blood Cell, Platelet, generic Cell, and individual
   leukocyte subtypes.
5. State the limiting principle: White Blood Cell stands independently because it is the category-level human
   immune-defense cell, has distinct white-cell-count uses, combines productively with existing emoji, and has
   its own frequency record. Encoding it would not automatically justify every blood component or cell type.
6. Keep Transient tied to dated Google Books and current multi-format evidence.
7. Keep Faulty comparison concise and independent of existing organ emoji.

## Correction 6: complete and normalize frequency evidence

Capture native Google pages without hiding settings or result counts.

Required files:

- `white-blood-cell_google_search_2026-07-26_SUBMIT.png`;
- `white-blood-cell_google_search_elephant_2026-07-26_SUBMIT.png`;
- `white-blood-cell_google_video_search_2026-07-26_SUBMIT.png`;
- `white-blood-cell_google_video_search_elephant_2026-07-26_SUBMIT.png`.

For Search and Video:

1. use `white-blood-cell` for the candidate query;
2. use the same language, personalization, and result-page settings for `elephant`;
3. open Tools when necessary to reveal the result count;
4. record the exact displayed count in the evidence log and proposal source;
5. record the nearest-million value separately for the official form;
6. do not describe the count as users, messages, or intended emoji uses.

For all five sources:

- preserve capture date, complete URL, location, range, category, and mode in `evidence/EVIDENCE-LOG.md`;
- keep screenshots readable at 100% PDF zoom;
- use readable Markdown link labels in the PDF rather than long raw URLs that disrupt pagination;
- retain the raw complete URLs in the evidence log;
- remove every placeholder before PDF generation.

The proposal may include the extra `elephant` Search and Video pages to match the live 2026 form wording even
though rubric 3.0.0 explicitly requires the comparator for Trends and Ngram.

## Correction 7: keep internal QA out of the submitted PDF

Preserve these files as internal reproducibility records:

- `validation/computer-validation.json`;
- `validation/computer-validation.md`;
- `comparisons/SOURCES.md`;
- colour and black-and-white comparison boards;
- artwork build and validation scripts.

Update `scripts/validate_white_blood_cell_submission.py` to reject reviewer-facing occurrences of:

- `{{` or `}}`;
- `TODO`, `TBD`, `BLOCKED`, or `not yet`;
- `IoU`, `difference hash`, `dHash`, `threshold`, `machine-readable`, `pinned comparator`, or
  `computer-validation.md`.

The preflight should continue to require the four artwork files, five evidence categories, both comparison
boards, passing internal validation, package version 1.11.0, and a valid PDF header.

## Correction 8: clean the canonical v1.11.0 package

Before commit:

1. Remove `white-blood-cell_emoji_proposal_DRAFT.md` and its PDF from v1.11.0.
2. Remove stale 2020 Search, Video, and Web Trends files from the active v1.11.0 White Blood Cell evidence
   folder; they remain recoverable in immutable v1.10.0 and earlier snapshots.
3. Remove the superseded 2026-07-10 Ngram capture after confirming the 2026-07-26 capture is embedded.
4. Keep only one final `SUBMIT.md` and one matching `SUBMIT.pdf`.
5. Update `VERSION`, manifest, package changelog, and artwork license consistently.
6. Record White Blood Cell authors as Shuhan He, David Rhew, and Heena Purohit, with Shuhan as main contact.
7. Hash-compare Kidney, Stomach, Liver, the template, and every other declared carried-forward file against
   v1.10.0; only documented package controls and White Blood Cell files may differ.

## Correction 9: build and inspect the final PDF

Build from the exact final Markdown source:

```powershell
python scripts/make_submission_pdf.py `
  submissions/v1.11.0/white-blood-cell/white-blood-cell_emoji_proposal_SUBMIT.md
```

Technical QA:

- valid PDF header and no encryption;
- stable document title;
- page numbers present;
- fonts embedded or reliably rendered;
- text extracts in reading order;
- hyperlinks resolve;
- no blank pages, broken images, clipped text, stranded headings, or split labels;
- four first-page artwork assets retain their exact intrinsic dimensions;
- evidence screenshots remain readable at 100% zoom;
- no placeholders or internal QA language survive.

Visual QA:

1. Render every page to PNG in `tmp/pdfs/`.
2. Inspect every page, not only the first and evidence pages.
3. Verify page 1 contains the complete first-page contract.
4. Verify the two comparison boards are legible and do not dominate the proposal.
5. Verify each frequency screenshot shows the claimed settings and observation.
6. Rebuild and repeat inspection after every source or layout change.

## Correction 10: publish, reconcile, and file

1. Run the final packet preflight and project verification commands.
2. Commit package 1.11.0 and project 0.42.0 with only task files staged.
3. Push `codex/proposal-guide-2026` to:
   https://github.com/ShuhanCS/medicalemoji
4. Use an immutable commit-addressed HTTPS PDF URL when possible.
5. Open the PDF URL in a logged-out or private browser and verify it downloads or renders without login.
6. Reconcile the form exactly with the PDF:
   - submitters: Shuhan He; David Rhew; Heena Purohit;
   - main contact: Shuhan He;
   - proposed name: White Blood Cell;
   - five keywords and category;
   - previous request status;
   - Search and Video counts rounded to the nearest million;
   - exact public PDF URL.
7. Complete the required agreement and electronic-signature step through the official form.
8. Submit before end of day 2026-07-31.
9. Archive the confirmation screenshot, timestamp, submitted URL, form values, commit SHA, and PDF SHA-256.

Official form:

https://forms.gle/6KSiYHrUdBkTMNaB8

## Execution order

1. Complete the visible Firefox Search and Video captures.
2. Synchronize rubric 3.0.0.
3. Apply proposal prose and heading corrections.
4. Update preflight rules and package controls.
5. Remove superseded v1.11.0 draft and evidence files.
6. Build the final PDF.
7. Run technical and page-by-page visual QA.
8. Reconcile the 17 rubric sections and 12 must-pass gates.
9. Commit and push project 0.42.0 / package 1.11.0.
10. Verify the public PDF logged out, file the form, and archive confirmation.

## Definition of done

- [x] Canonical, active, and packaged rubric references use version 3.0.0 consistently.
- [ ] All three authors and the main contact match across proposal, manifest, public PDF, and form.
- [x] Page 1 source satisfies the complete first-page contract.
- [x] Distinctiveness uses visible cues and ordinary language, with internal validation details excluded.
- [x] All 17 rubric sections follow their drafting patterns in the proposal source.
- [x] All five frequency categories are current, reproducible, legible, and interpreted accurately.
- [x] No placeholder, draft language, internal score, workflow narration, or technical-validation jargon appears
  in the submitted PDF.
- [x] The final PDF passes technical checks and visual inspection of every page.
- [ ] Rubric score is 100/100 and every must-pass gate is complete.
- [x] The exact PDF is public through a stable logged-out HTTPS URL.
- [ ] The official form matches the PDF and the confirmation record is archived.
