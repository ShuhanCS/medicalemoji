# Stomach v1.13: Response To Independent Review

Review date: 2026-07-27

Reviewed artifact: `candidate-v1.12/stomach_emoji_proposal_CANDIDATE.pdf`

Current packet: `1.13.0-candidate.2`

Candidate.2 preserves the evidence and distinctiveness corrections below while applying the later Stomach
finalization specification. Eligibility is again treated as the settled project input recorded by Shuhan He,
the public proposal no longer discusses discarded multi-concept comparisons, and the Open-ended answer now
states only the bounded Stomach-specific limiting principle.

The review rebuilt Unicode's requirement set from the live guidance page rather than from the project's own
notes, measured each frequency claim against its own screenshot at the pixel level, and established base rates
from Unicode's published proposal-status data.

## Findings and disposition

### 1. Google Trends Image Search caption did not match its own chart

**Finding.** v1.12 said stomach showed "sustained worldwide image-search interest across the full available
range and a strong recent peak above elephant." Measuring the two plotted series from the screenshot, stomach
is the higher line in 14 of 926 sampled columns, which is 1.5 percent of the timeline, and all 14 fall inside
the final 5 percent. Elephant holds the higher mean position across the range. The sentence was literally true
and read as advocacy.

**Fixed.** The caption now states that this is the weakest of the five sources, that elephant is the higher line
across most of the range and holds the higher displayed average, and that no weight is placed on the terminal
crossover because a final Trends interval can be incomplete.

### 2. Google Trends Web Search caption overstated the range

**Finding.** v1.12 claimed the higher average "across the full range." The same measurement shows stomach above
elephant in 638 of 838 columns, which is 76 percent, with elephant leading in the earliest years.

**Fixed.** The caption now claims the higher displayed average and the higher line across most of the charted
range, and states that elephant leads in the earliest years.

### 3. Elephant comparison was missing from two of the five required sources

**Finding.** Unicode's Required Information section says to include `elephant` as a comparative search term and
to screenshot each of the five sources. v1.12 carried the comparison on Trends Web, Trends Image, and Ngram, but
not on Google Search or Google Video Search.

**Fixed.** Both baselines captured 2026-07-27 by `scripts/capture_elephant_baseline.mjs`, which reuses the
existing evidence browser profile, never bypasses a challenge, and refuses to save a screenshot unless a result
count is visible. Section E now opens with a comparison table covering all five sources.

The result is mixed and is reported as mixed:

| Source | `stomach` | `elephant` | Higher |
| --- | --- | --- | --- |
| Google Search | 353,000,000 | 491,000,000 | elephant |
| Google Video Search | 139,000,000 | 86,300,000 | stomach |
| Google Trends, Web Search | higher average | lower average | stomach |
| Google Trends, Image Search | lower across most of range | higher across most of range | elephant |
| Google Books Ngram | substantially higher recently | lower recently | stomach |

### 4. Distinctiveness was asserted but not shown

**Finding.** Section D claimed the art is distinguishable from Beans, Anatomical Heart, and Meat on Bone at
18x18 without showing any comparison. The 2026-07-20 organ audit had already asked for this figure and v1.12
did not carry it.

**Fixed.** `scripts/build_stomach_comparison_board.py` renders the proposed art beside Beans, Anatomical Heart,
Lungs, and Meat on Bone at 72x72 and at 18x18. The 18x18 row is the submitted file enlarged with
nearest-neighbour sampling so the true pixel structure is visible rather than a smoothed approximation.
Comparison glyphs are from the open-licensed Noto Emoji project and the caption states that they are not part of
the artwork covered by the rights certification.

### 5. The strongest available argument was asserted rather than evidenced

**Finding.** The one thing `stomach` has that other organ words lack is an established non-anatomical sense in
ordinary English. v1.12 stated this via dictionary links only, and the Open-ended answer rested on assertion.

**Fixed.** Section A adds two supplementary Ngram exhibits: the tagged verb sense of `stomach`, in continuous
published use since the seventeenth century and now at its charted peak, and the idioms `a strong stomach`,
`turn my stomach`, and `butterflies in my stomach`. Exclusion C is rebuilt so the selection criterion is the
idiomatic load of the word rather than membership in the anatomy, which makes the criterion self-limiting on
evidence rather than by assertion. Exclusion D now cites the same exhibits.

**Rejected during this work.** A multi-concept part-of-speech comparison was captured and discarded because
Ngram's tagger produced implausible historical baselines. The reliable single-term chart is used instead.
Candidate.2 removes this internal experiment from the public proposal because it does not help a reviewer
evaluate Stomach and could imply coordination with another filing.

### 6. Capture method was undisclosed

**Fixed.** Section E states that captures were made in a private browser window with personalization disabled,
that the widest available date range was used for each tool, and why no qualifying category was applied to the
Trends exhibits: `stomach` is not ambiguous in the way `seal` or `fly` are, and a health category would distort
the required `elephant` baseline.

### 7. Date and eligibility record

**Reconciled in Candidate.2.** The proposal is dated 2026-07-27, the revision date used by this candidate.
Eligibility is a settled project input confirmed by Shuhan He and remains an internal filing control; the
reviewer-facing PDF does not narrate an eligibility dispute.

## Findings not fixed in the document

These are filing records or honest factor limits, not defects in the prose.

1. **Exact-art approval.** Shuhan's dated decision on the four exact files remains open.
2. **Coauthor consent.** Written consent from David Rhew and Heena Purohit remains open.
3. **Compatibility scores nothing.** ESR's stated intake focus for Emoji 19.0 and beyond, in L2/25-128, names
   compatibility with social apps, other standards, or operating systems. Section G is `Not applicable`. That is
   honest and should stay honest unless real evidence exists.

## Verification performed on the Candidate.2 PDF

- 8 US Letter pages at 612x792, unencrypted, extractable text, embedded subset fonts.
- No TODO, PLACEHOLDER, FIXME, DRAFT, or "must be refreshed" markers.
- 19 link annotations retained for the cited sources and reproducible queries.
- Both black-and-white assets re-verified as exactly two colours at 18x18 and 72x72.
- The prior Google Books page-start clipping was fixed with an explicit section page break.
- Every page rendered and visually inspected for clipping, overlap, stranded headings, and blank pages.
