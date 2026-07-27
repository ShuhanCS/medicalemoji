# Liver Artwork Computer Validation

Reproducible checks cover exact dimensions, palette, hashes, and separation against pinned comparators.

| Comparator | Silhouette IoU | 64-bit dHash distance |
| --- | ---: | ---: |
| Anatomical Heart | 0.5748 | 28 |
| Lungs | 0.6853 | 22 |
| Brain | 0.7683 | 26 |
| Cut of Meat | 0.6741 | 33 |
| Beans | 0.5996 | 26 |

Comparison board: `liver-comparison-board.png`

Pinned assets and hashes are recorded in `computer-validation.json`.
