# Liver Artwork Computer Validation

Reproducible checks cover exact dimensions, palette, hashes, and separation against pinned comparators.

| Comparator | Silhouette IoU | 64-bit dHash distance |
| --- | ---: | ---: |
| Anatomical Heart | 0.5238 | 27 |
| Lungs | 0.6191 | 25 |
| Brain | 0.7069 | 27 |
| Cut of Meat | 0.5817 | 30 |
| Beans | 0.5177 | 29 |

Comparison board: `liver-comparison-board.png`

Pinned assets and hashes are recorded in `computer-validation.json`.
