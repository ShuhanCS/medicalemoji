# White Blood Cell v1.18.0 - resume notes

Branch: `feat/wbc-proposal-fixes`
Worktree: `C:\Users\Shuha\projects\medicalemoji\.worktrees\wbc-proposal-fixes`
Unicode submission window closes **2026-07-31**.

## The headline finding

The submitted v1.18.0 PDF reports **"About 125 results"** for `white-blood-cell` on Google Search
against 491,000,000 for `elephant`. That number is wrong.

Re-measured 2026-07-27, three independent page loads per query, same settings the proposal
documents (`hl=en&num=10&pws=0`, Firefox private profile):

| Query | Submitted PDF | Re-measured 2026-07-27 |
| --- | --- | --- |
| `white-blood-cell` Search | about 125 | **about 880,000,000** |
| `elephant` Search | about 491,000,000 | about 491,000,000 (unchanged) |
| `white-blood-cell` Video | about 14,100,000 | about 14,000,000 |
| `elephant` Video | about 86,300,000 | about 84,700,000 |

`elephant` reproduces exactly, which confirms the re-measurement matches the original capture
conditions. So the 125 was a bad read at capture time, not a settings difference.

**This reverses the usage argument on the strongest-weighted factor.** White blood cell now measures
about **1.79x elephant** on Google Search instead of four orders of magnitude below it.

Hyphenation is not the cause. `scripts/probe_google_hyphen_artifact.mjs` tested Unicode's own
documentation example and found no grouped-vs-plain gap for any term:

| Concept | grouped | plain |
| --- | --- | --- |
| white blood cell | 880,000,000 | 881,000,000 |
| black swan | 258,000,000 | 258,000,000 |
| first aid kit | 377,000,000 | 376,000,000 |
| elephant | 491,000,000 | 491,000,000 |

Raw data: `evidence/frequency/google_hyphen_artifact_probe.json` and
`evidence/frequency/white-blood-cell_google_recapture_log_2026-07-27.json`.

## What is done

- `scripts/probe_google_hyphen_artifact.mjs` - proves the hyphen syntax is not the cause. Runs clean.
- `scripts/recapture_google_search_evidence.mjs` - recaptures Search + Video for the term and the
  `elephant` comparator. Loads each query three times and refuses to save unless every reading lands
  in the same order of magnitude. This guard is what would have caught the 125.

## What is NOT done - blocking

**1. The four 2026-07-27 screenshots are not usable yet.**

They are on disk as `*_DRAFT-NO-VISIBLE-COUNT.png`. The counts were read from the DOM
(`#result-stats` has the text even while the Tools panel is collapsed), but the panel is closed in
the shot, so the number is not visible on screen. Evidence screenshots have to show the count the
way the current `*_2026-07-26_SUBMIT.png` files do.

Where it stands: `exposeCountOnScreen()` in the recapture script asserts `#result-stats` is visible
before saving, and correctly refuses to save. Getting the panel open is the remaining problem.
Findings from debugging the `#hdtb-tls` toggle:

- normal `.click()` hangs (jsaction overlay swallows the pointer event)
- `.click({force:true})` times out
- `.evaluate(el => el.click())` toggles `aria-expanded` back to `false`
- `.dispatchEvent("click")` **does** set `aria-expanded="true"`, but Playwright still reports
  `#result-stats` as not visible

Next thing to try: after `dispatchEvent("click")`, find the element whose own text matches
`/^About [\d,]+ results/` and check its bounding box directly, rather than trusting the
`#result-stats` id. There may be a second node that is the one actually rendered. A debug snippet
that enumerates candidates is in the git history of this note's commit message, or just rewrite it.

Fallback if the automation stays stubborn: capture the two Search screenshots by hand in the same
Firefox profile with Tools open, keep the three-load confirmation from the script as the audit
trail, and note the manual capture in `evidence/EVIDENCE-LOG.md`.

Do not ship the `_DRAFT-NO-VISIBLE-COUNT` files.

**2. None of the proposal text is edited yet.** `white-blood-cell_emoji_proposal_SUBMIT.md` is
untouched. Still to do, in priority order:

- **Section 6 Google Search + Video** - rewrite around 880,000,000 vs 491,000,000 and the corrected
  video figures. Swap in the new screenshots. Update `evidence/EVIDENCE-LOG.md` to match.
- **Section 3e Usage level** - currently concedes "Its relative Trends and Ngram levels are below
  `elephant`". With Search now above elephant, this section should lead with the Search and Video
  result inventory and treat Trends and Ngram as the secondary, weaker signals. Keep it honest:
  Trends really is 3 vs 72.
- **Section 3d Distinctiveness** - embed a comparison strip. The boards already exist and are not
  referenced by the proposal:
  `comparisons/white-blood-cell_comparison-board_color_2026-07-26.png` and
  `comparisons/white-blood-cell_comparison-board_black_2026-07-26.png`.
- **Section 5** - acknowledge the prior submission. Unicode's public ledger has
  `White Blood Cell | Declined | 12/18/2020`. The four-year bar has elapsed. Three sentences: prior
  submission, bar elapsed, what is materially different now.
- **Section 3a Multiple meanings** - currently "Not applicable", which forfeits a scored factor.
  Write a real paragraph on immune defense as metaphor.
- **Date** - bump from 2026-07-26 to the actual resubmission date.
- Rebuild the PDF (`scripts/make_submission_pdf.py`) and re-run
  `scripts/validate_white_blood_cell_submission.py`.

**3. Artwork is unchanged and still has the problem from the review.** The B&W 18x18 reads as a
soccer ball: solid black nucleus lobes inside a near-circular outline. Grayscale is not allowed, so
the fix is outlined lobes plus a lumpier membrane. Section 5 already tells vendors to keep a band of
pale cytoplasm around the nucleus, but the submitted sample does not do it.
Source SVGs: `images/white-blood-cell_bw_18_SOURCE.svg`, `images/white-blood-cell_bw_SOURCE.svg`.
Rebuild with `scripts/build_white_blood_cell_artwork.py`, check with
`scripts/validate_white_blood_cell_artwork.py`.

## Process item

Three submitters are named. Confirm David Rhew and Heena Purohit have each signed the Unicode Emoji
Proposal Agreement and License on the submission form.
