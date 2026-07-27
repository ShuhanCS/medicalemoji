# White Blood Cell artwork computer validation

Validation date: 2026-07-26

Status: **PASS**

## Scope

This reproducible technical test validates the four exact assets, editable-source hashes, true
black-and-white palette, foreground connectedness, and machine-visible separation from Microbe, Drop of Blood,
Soap, Bubbles, and a generic-cell control. Actual-size comparison boards are recorded separately.

## Required assets

| Asset | Dimensions | B&W palette | Components | Result |
| --- | ---: | --- | ---: | --- |
| white-blood-cell_color_18x18_SUBMIT.png | 18x18 | n/a | 1 | PASS |
| white-blood-cell_color_72x72_SUBMIT.png | 72x72 | n/a | 1 | PASS |
| white-blood-cell_bw_18x18_SUBMIT.png | 18x18 | pass | 1 | PASS |
| white-blood-cell_bw_72x72_SUBMIT.png | 72x72 | pass | 2 | PASS |

## 18x18 comparisons

| Variant | Comparator | Silhouette IoU | Silhouette dHash | Feature IoU | Feature dHash | Result |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| color | microbe | 0.492 | 28 | 0.347 | 28 | PASS |
| color | drop of blood | 0.636 | 25 | 0.392 | 31 | PASS |
| color | soap | 0.508 | 20 | 0.298 | 26 | PASS |
| color | bubbles | 0.541 | 31 | 0.228 | 26 | PASS |
| color | generic cell | 0.860 | 19 | 0.500 | 12 | PASS |
| black | microbe | 0.293 | 32 | 0.136 | 34 | PASS |
| black | drop of blood | 0.173 | 30 | 0.105 | 28 | PASS |
| black | soap | 0.250 | 28 | 0.157 | 30 | PASS |
| black | bubbles | 0.267 | 32 | 0.156 | 29 | PASS |
| black | generic cell | 0.371 | 17 | 0.371 | 17 | PASS |

## Editable-source hashes

- `white-blood-cell_color_18_SOURCE.svg`: `e9cef7b8e9171a519173efed74250aeec25d839ff7acae3a51c255e29a7ed9b1`
- `white-blood-cell_color_SOURCE.svg`: `423f2f43c8face188ef49e7dbac3fb208ab16732dfd4f89b9acacf109b1cd250`
- `white-blood-cell_bw_18_SOURCE.svg`: `f0e8d54afda6557e3f9c357863eb4f94858d46712e474ee60317ee55f236f55a`
- `white-blood-cell_bw_SOURCE.svg`: `059e54a4a31e2ba2c9eaf4cad043034e4c1305510ab3dfa46ae7ead05c144bf2`

OpenMoji comparators are pinned to commit `d05930b34516a0a3ff00aad0288ee05364cebd8b`. Provenance and full URLs are in
`../comparisons/SOURCES.md`.

Reproduce with:

```powershell
python scripts/validate_white_blood_cell_artwork.py `
  --proposal-dir submissions/v1.16.0/white-blood-cell `
  --json-output submissions/v1.16.0/white-blood-cell/validation/computer-validation.json `
  --markdown-output submissions/v1.16.0/white-blood-cell/validation/computer-validation.md
```
