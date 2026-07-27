# Kidney Consolidation — Resume Plan

Save point: 2026-07-27
Branch: `feat/kidney-v2.1.2-consolidated` (worktree `.worktrees/kidney-v211`, based on `codex/kidney-v1-2-argument`)
Filing deadline: **2026-07-31 end of day**

Resume with: `execute docs/plans/2026-07-27-kidney-consolidation.md`

## Situation

Two parallel Kidney proposal lines existed. They have opposite strengths.

| | `v1.12.0-kidney.7` | `v2.1.1` |
| --- | --- | --- |
| Branch | `feat/kidney-18px-redesign` (99 commits deep, off the `codex/finalize-organ-submissions` mega-branch) | `codex/kidney-v1-2-argument` (8 commits, clean off `master`) |
| Paradigm | paired kidneys | **single kidney (better)** |
| Case discipline | **scrubbed of advocacy and disease burden; names neighbours** | carries advocacy, WHO/Lancet/CDC burden, 13 support letters |
| Prose words | ~1,050 | **1,711** (branch rule: under 1,200) |
| Deterministic validator | yes, passes | not wired up |

Decision: **consolidate onto v2.1.1's single-kidney paradigm, import v1.12.0's case discipline.**

Rationale for single-kidney: at 18x18 there are only ~18 px across. Spending them on one
organ roughly doubles the resolution per shape versus splitting across two.

## Done so far

- Mapped every branch. `codex/finalize-organ-submissions` is a mega-branch holding all four
  organs; that is why `feat/kidney-18px-redesign` drags 99 commits. Do not merge it to master.
- Built and shipped `submissions/v1.12.0-kidney.7` on `feat/kidney-18px-redesign` (paired
  paradigm). Validator passes: Lungs IoU 0.698 -> 0.556 color / 0.582 -> 0.545 b&w, dHash 23 -> 33.
  That work is real but targets the line we are now stepping away from. Keep for reference.
- Identified the v2.1.1 artwork defect: **the black-and-white assets fill the hilum solid**, so the
  kidney's defining concavity disappears and it reads as a plain blob. The color assets are correct.
- Wrote `scripts/gen_single_kidney.py` proving the fix direction (open hilum survives at 18x18).
  Its output is NOT ship-ready — reads as "Pac-Man with a straw". Do not file it.

## Remaining work, in order

### Phase 1 — Artwork
Fix the black-and-white pair by editing the existing vector source, not by regenerating raster:
`submissions/v2.1.1/images/v2.1.1_kidney_bw_vector_SOURCE_REFERENCE_ONLY.svg`

- Open the hilum so background shows through the medial concavity.
- Keep the ureter attached to the body at one point (the validator requires at most two
  components with the largest holding >=95% of visible pixels; a detached ureter is ~6% at 18x18
  and will fail).
- Re-export exact 18x18 and 72x72. True black and white only, no grayscale.

### CHECKPOINT: commit artwork

### Phase 2 — Case discipline
Port from `submissions/v1.12.0-kidney.7/kidney/kidney_emoji_proposal_SUBMIT.md`:

- Cut WHO / Lancet / CDC disease-burden counts. Branch rule: advocacy and awareness language
  appears 13x more often in proposals that failed.
- Cut or drastically trim section `5.A Public-Health And Clinical Context` and
  `5.B Coalition And Support Materials`. Move the 13 support-letter links to a
  `REFERENCE_ONLY` file rather than deleting them — they are a real asset, just not proposal body.
- Rewrite `4.C Open-Ended` to **name the neighbours we will not propose** (Liver, Stomach,
  Pancreas, Spleen) and give the bounded rule. Branch rule requires this and v2.1.1 omits it.
- Restore Unicode's own factor names: `A. Multiple meanings` (not "Multiple Concepts"),
  `E. Faulty comparison` (not "Justified By An Existing Emoji").
- Keep v2.1.1's strong material: single-kidney visual-cue table, substitute-failure table.
- Import the `kidney-shaped` evidence for Multiple meanings (Books Ngram: `kidney-shaped` peaks
  above `kidney stone`, sits near two-thirds of it in 2022).
- Target under 1,200 prose words.

### CHECKPOINT: commit prose

### Phase 3 — Validate and build
- Wire `scripts/validate_kidney_artwork.py` to the v2.1.2 asset names and run it.
- Rebuild the PDF with `scripts/make_submission_pdf.py`.
- Render page 1 and eyeball the example-image table.

### CHECKPOINT: commit package

### Phase 4 — Publish
- Merge only this narrow branch to `master`, tag it, and verify the PDF at a logged-out HTTPS URL
  with `curl -o /dev/null -w '%{http_code}'` before the URL goes anywhere near the form.

## Blocking items that are not mine to close

1. **Eligibility.** Unicode declined Kidney twice: 2019-12-17 and 2022-07-19 (status sheet), with a
   notice dated 2022-11-04. The rule is "emoji declined within the last four years are not eligible
   for re-review." Four years from the decision date lands 2026-11-04, after the 2026-07-31
   deadline. Draft inquiry ready at `docs/proposals/2026-eligibility-inquiry.md` on the
   `feat/kidney-18px-redesign` branch. **Send before filing.** This dominates the odds.
2. **Company names in the byline.** Branch rule says the submission form rejects company names.
   `v1.12.0-kidney.7` carries `David Rhew, MD (Microsoft)` and `Heena Purohit (Microsoft for
   Startups)`. v2.1.1's byline is already clean of these — one more reason to consolidate there.
3. **Artwork rights differ between the lines.** v1.12.0 has Shuhan personally warranting ownership
   and releasing CC0. v2.1.1 states Conductscience Foundation owns the artwork and granted rights.
   Pick one and make it consistent before filing.
4. **Do not file Kidney, Liver and Stomach together.** Branch rule forbids it; each must stand alone.

## Odds

~3-6% if filed, dominated by the eligibility question. Base rate from Unicode's own status
spreadsheet is ~2-3% for recent years (2022: 1.9%, 2024: 1.5%, 2025: ~2.5% realistic).
White Blood Cell is the only slate item with clean eligibility (declined 2020-12-18) and is the
safe hedge if no eligibility answer arrives before the 31st.
