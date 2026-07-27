# White Blood Cell v1.19.0 - resume notes

Branch: `feat/wbc-proposal-fixes`
Package: v1.19.0. v1.18.0 is frozen at its released state and is not edited.
Worktree: `C:\Users\Shuha\projects\medicalemoji\.worktrees\wbc-proposal-fixes`
Unicode submission window closes **2026-07-31**.

## The headline finding

The v1.18.0 PDF, released 2026-07-26, reported **"About 125 results"** for `white-blood-cell` on Google Search against
491,000,000 for `elephant`. That number was wrong.

Re-measured 2026-07-27, three independent loads per query, same documented settings
(`hl=en&num=10&pws=0`, Firefox private profile):

| Query | v1.18.0 | Confirmed in v1.19.0 |
| --- | --- | --- |
| `white-blood-cell` Search | about 125 | **about 880,000,000** |
| `elephant` Search | about 491,000,000 | about 491,000,000 (unchanged) |
| `white-blood-cell` Video | about 14,100,000 | about 13,900,000 |
| `elephant` Video | about 86,300,000 | about 84,700,000 |

`elephant` reproduces exactly, which confirms the settings match. The 125 was a bad read, not a
configuration difference.

Hyphenation is not the cause. The probe tested Unicode's own documentation example and found no
grouped-versus-plain gap for any term:

| Concept | grouped | plain |
| --- | --- | --- |
| white blood cell | 880,000,000 | 881,000,000 |
| black swan | 258,000,000 | 258,000,000 |
| first aid kit | 377,000,000 | 376,000,000 |
| elephant | 491,000,000 | 491,000,000 |

**This reverses the usage argument on the most heavily weighted factor.** Search now measures about
1.8x `elephant` instead of four orders of magnitude below it. Video, both Trends properties, and Books
remain below, and Sections 3e and 6 say so plainly.

## Done

- Section 6 rewritten on the corrected figures; all four screenshots recaptured with the count visible.
- Section 3e rewritten. Leads with Search and Video inventory, states that Trends and Books stay well below.
- Section 3a was "Not applicable"; now argues the secondary symbolic sense of internal defense.
- Section 3d embeds a recognition figure, original artwork only, proposed image against a generic cell
  control. Third-party comparator art stays out of the PDF, so the OpenMoji boards in `comparisons/` remain
  internal review artifacts.
- Section 5 acknowledges the 2020 declined proposal on Unicode's published status list and notes the
  re-submission period has elapsed. Vendor design notes softened to suggestions, since a proposal that
  requests an exact image is automatically declined.
- `evidence/EVIDENCE-LOG.md` records the correction and the probe table.
- PDF rebuilt, now fourteen pages.
- `scripts/validate_white_blood_cell_submission.py --package-dir submissions/v1.19.0` passes.

### New tooling

- `scripts/probe_google_hyphen_artifact.mjs` - runs each term grouped and unhyphenated to test the syntax.
- `scripts/recapture_google_search_evidence.mjs` - recaptures Search and Video for the term and the
  `elephant` comparator. Loads each query three times, refuses to save unless every reading lands in the same
  order of magnitude, and refuses to save unless the count is actually visible on screen.
- `scripts/validate_white_blood_cell_submission.py` - now derives required evidence files from the proposal's
  own image references rather than hardcoded dated filenames, and fails if a count the proposal states does
  not match a confirmed figure in the capture log. Negative-tested: reverting the Search figure to 125 makes
  it fail.
- `scripts/build_white_blood_cell_artwork.py --figure-date` - builds the original-art-only recognition figure.

## Not done

**1. The black-and-white 18x18 artwork.** Unchanged, and still the weakest part of the package. The nucleus
renders as solid black lobes inside a near-circular outline, which reads as a soccer ball at keyboard size.
Grayscale is not permitted, so the fix is outlined lobes rather than filled, plus a visibly lumpier membrane.
Section 5 already tells vendors to keep a band of pale cytoplasm around the nucleus; the submitted sample does
not do it, and the new recognition figure on page 3 shows the gap.

Sources: `images/white-blood-cell_bw_18_SOURCE.svg`, `images/white-blood-cell_bw_SOURCE.svg`.
Rebuild: `python scripts/build_white_blood_cell_artwork.py --proposal-dir submissions/v1.19.0/white-blood-cell
--board-date 2026-07-26 --figure-date 2026-07-27`.
Check: `scripts/validate_white_blood_cell_artwork.py`.

**2. The seventeen-section review has not been re-run.** `READINESS.md` opens with a block listing which of
its rows are now stale. Status was moved from `READY TO PUBLISH` to `CHANGED SINCE REVIEW, NOT RE-REVIEWED`.

**3. Section 3b still lists adjacency pairs**, not ZWJ sequences in Unicode's technical sense. Minor, but it
is a scored factor and the wording invites the distinction.

**4. Confirm co-submitter paperwork.** Three submitters are named; David Rhew and Heena Purohit each need to
have signed the Unicode Emoji Proposal Agreement and License on the submission form.

## Note on the other three concepts

Kidney, Liver, and Stomach in `submissions/v1.19.0/` were not touched. Their Google Search evidence was
captured by the same original process that produced the 125, so their result counts are worth re-checking
with `scripts/recapture_google_search_evidence.mjs` before filing. The liver and stomach captures are dated
2020, which is worth a look on its own.
