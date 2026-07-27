# Kidney 18x18 Redesign — Findings

Date: 2026-07-26
Against package: `submissions/v1.12.0-kidney.6`

## 1. Root cause of the 18x18 legibility failure

The current `kidney_bw_18x18_SUBMIT.png` is an **outline** render: hollow lobes drawn with
1px strokes, plus a vessel cluster in the medial gap. At 18px an outline style spends its
entire pixel budget on the stroke and leaves no interior signal, so the form collapses into
an ambiguous keyhole. Pixel dump of the shipped asset:

```
..................
..####............
.#...##...........
##....#...........
##....##..........
#.....#...........
#....##.....####..
#...#########..##.
#...#.######....##
#...##.#..##....##
##...###..####...#
##....##..#..#...#
.#....##..#..#...#
.##...##..###...##
..######..##....#.
....##....##...##.
...........#####..
............###...
```

Two compounding problems: the vertical offset between lobes is ~5 rows (too large to read as
a pair), and the vessel bundle occupies the center where the medial notch signal should be.

Note this also contradicts the proposal text. Page 8 states "full vascular anatomy is
intentionally omitted for legibility at 18x18," but the shipped 18x18 color asset visibly
retains the aorta, vena cava, and ureters.

## 2. The validator cannot see this problem

`scripts/validate_kidney_artwork.py` scores separability via `normalize_mask`, which builds a
foreground mask by flood-filling **from the image borders**. Interior white that is enclosed
by the artwork is never reached by the flood, so it is classified as foreground.

Consequence: the IoU and dHash comparisons measure the **outer silhouette only**. They are
structurally blind to whether the interior is a hollow outline or a solid fill. A hollow
outline and a solid silhouette of the same shape score identically.

This is not a bug to fix — the validator is honest that it is "a technical separability test,
not a claim about human semantic recognition." But it means **passing computer validation
carries no information about the legibility problem**, and solid-filling the lobes costs
nothing against the fixed 0.72 IoU / 16 dHash thresholds.

## 3. The binding constraint is connectivity, not IoU

```python
connectedness_pass = len(components) <= 2 and largest_share >= 0.95
```

At most two components AND the largest holding >=95% of visible pixels. Two separate lobes
split 50/50 and fail. Every design must therefore keep the pair joined at 18px. This
constraint, not the IoU ceiling, is what drives the silhouette.

## 4. Three generations explored

| Gen | Approach | Result |
| --- | --- | --- |
| 1 | Solid lobes welded by a centered horizontal bar | Best IoU (0.543–0.611) but reads as a **dumbbell**. Legibly the wrong object. |
| 2 | Lobes nestled so notch lips touch top and bottom | Traps an enclosed white lens; reads as a **bowtie**. IoU also degraded to 0.62–0.65. |
| 3 | Notch raised on the medial edge + real vertical offset, contact at **one** point only | Two distinct offset lobes, medial gap opens downward. No dumbbell, no bowtie. |

Gen-1 and Gen-2 are retained in `compare_18.png` and `compare_18b.png` as negative results.

## 5. Finalists

Both pass every hard gate and beat the shipped asset on both metrics.

| Asset | Lungs IoU | Beans IoU | dHash vs Lungs | Components |
| --- | ---: | ---: | ---: | ---: |
| **shipped** color | 0.698 | 0.607 | 23 | 1 |
| **shipped** b&w | 0.582 | 0.503 | 23 | 1 |
| P5_deep_hi color | **0.556** | 0.539 | **33** | 1 |
| P5_deep_hi b&w | **0.545** | 0.528 | **33** | 1 |
| P7_slim_hi color | **0.547** | 0.547 | 29 | 1 |
| P7_slim_hi b&w | **0.537** | 0.536 | 29 | 1 |

P5 has the deeper notch and the strongest hash separation. P7 is slimmer and taller, closer
to anatomical proportion. Selection is a taste call and belongs to Shuhan.

## 6. Reproduce

```powershell
python scripts/gen18.py    # gen-1 (barbell, negative result)
python scripts/gen18b.py   # gen-2 (nestled, negative result)
```

Gen-3 parameters are recorded in `candidate-scores.json`. Both scripts import the repo
validator directly so scores are computed with identical functions and the same pinned Noto
comparators.

## 7. Open item

If a finalist is adopted, page 8 of the proposal must be corrected so the "vascular anatomy
omitted at 18x18" sentence matches the asset. In the finalists it is true; in the shipped
asset it is not.
