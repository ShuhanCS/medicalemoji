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

- `white-blood-cell_color_18_SOURCE.svg`: `14fdcc2af19cba6c69c262a2cacba0f71ad1b1fc4473960f5f73e14a786e8bf0`
- `white-blood-cell_color_SOURCE.svg`: `54d5e06c1ee9f0e81112b40017718d07dd9097d64f3f20bb1806a7e9cc29f134`
- `white-blood-cell_bw_18_SOURCE.svg`: `8a0b963496a86dfbca7c3da9bf4cfc8e2a7b9f2a6ae5fc1bdd1ab170d8f80b9a`
- `white-blood-cell_bw_SOURCE.svg`: `21b2826b54ee0a6be456690eda931064724d024e4aee9076a3e8bf338c3c180f`

OpenMoji comparators are pinned to commit `d05930b34516a0a3ff00aad0288ee05364cebd8b`. Provenance and full URLs are in
`../comparisons/SOURCES.md`.

Reproduce with:

```powershell
python scripts/validate_white_blood_cell_artwork.py `
  --proposal-dir submissions/v1.11.0/white-blood-cell `
  --json-output submissions/v1.11.0/white-blood-cell/validation/computer-validation.json `
  --markdown-output submissions/v1.11.0/white-blood-cell/validation/computer-validation.md
```
