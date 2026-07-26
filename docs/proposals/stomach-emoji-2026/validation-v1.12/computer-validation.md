# Stomach Artwork Computer Validation

Validation date: 2026-07-26

Status: **PASS**

## Scope

This deterministic test validates exact dimensions, a true black-and-white palette, foreground connectedness,
and machine-visible silhouette separation from six declared confusers. It does not measure or replace human
semantic recognition.

Thresholds were fixed before the release run: normalized silhouette IoU must be at most
`0.72`, 64-bit difference-hash distance must be at least `16`, foreground
components must not exceed two, and the largest component must contain at least 95% of visible pixels.

## Required assets

| Asset | Dimensions | B&W palette | Components | Result |
| --- | ---: | --- | ---: | --- |
| stomach_color_18x18_SUBMIT.png | 18x18 | n/a | 1 | PASS |
| stomach_color_72x72_SUBMIT.png | 72x72 | n/a | 1 | PASS |
| stomach_bw_18x18_SUBMIT.png | 18x18 | pass | 1 | PASS |
| stomach_bw_72x72_SUBMIT.png | 72x72 | pass | 1 | PASS |

## 18x18 silhouette comparisons

| Proposal asset | Comparator | Normalized IoU | dHash distance | Result |
| --- | --- | ---: | ---: | --- |
| color_18x18 | anatomical heart | 0.599 | 26 | PASS |
| color_18x18 | beans | 0.638 | 19 | PASS |
| color_18x18 | meat on bone | 0.580 | 24 | PASS |
| color_18x18 | kidney | 0.628 | 23 | PASS |
| color_18x18 | liver | 0.542 | 27 | PASS |
| color_18x18 | generic organ | 0.535 | 26 | PASS |
| black_and_white_18x18 | anatomical heart | 0.576 | 21 | PASS |
| black_and_white_18x18 | beans | 0.626 | 20 | PASS |
| black_and_white_18x18 | meat on bone | 0.566 | 23 | PASS |
| black_and_white_18x18 | kidney | 0.584 | 26 | PASS |
| black_and_white_18x18 | liver | 0.511 | 28 | PASS |
| black_and_white_18x18 | generic organ | 0.527 | 19 | PASS |

## Comparator hashes

- anatomical heart: `d085a08da7477258c7c9d97b336c1cd9890b2759da3212455d641cb88bb49673`
- beans: `e37d8c68eb71eb2eb9845e1bc57d92ebd566f01fba48c33117c9fc55a4b3d8d9`
- meat on bone: `c35bb6b51f8abed799d429a01a90d6d82eda8c9f129a62061eec4f99ea254c35`
- kidney: `86da05075456926c625272323423467b1cbfc6f985791ef82e2244cc1eafbdfe`
- liver: `682cbe299bb1944c4fbe632a851655ebe78820a0be158878bc1720486a83d29f`
- generic organ: `4f5a7d7654dcb807a58a1293dcf2c3b8dacbf761a083c0eea6fb45be507f56af`

Complete provenance and licenses are in `comparator-manifest.json`.

## Comparison boards

- `comparison-color-18.png`
- `comparison-bw-18.png`
- `comparison-color-72.png`
- `comparison-bw-72.png`

Reproduce with:

```powershell
python scripts/validate_stomach_artwork.py `
  --proposal-dir submissions/v1.11.0/stomach `
  --output-dir docs/proposals/stomach-emoji-2026/validation-v1.12
```
