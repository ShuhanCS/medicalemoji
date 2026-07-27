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
| white-blood-cell_bw_72x72_SUBMIT.png | 72x72 | pass | 1 | PASS |

## 18x18 comparisons

| Variant | Comparator | Silhouette IoU | Silhouette dHash | Feature IoU | Feature dHash | Result |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| color | microbe | 0.492 | 28 | 0.234 | 27 | PASS |
| color | drop of blood | 0.628 | 25 | 0.335 | 28 | PASS |
| color | soap | 0.508 | 20 | 0.200 | 29 | PASS |
| color | bubbles | 0.549 | 29 | 0.285 | 27 | PASS |
| color | generic cell | 0.860 | 17 | 0.392 | 15 | PASS |
| black | microbe | 0.203 | 35 | 0.103 | 33 | PASS |
| black | drop of blood | 0.212 | 29 | 0.128 | 29 | PASS |
| black | soap | 0.193 | 33 | 0.130 | 31 | PASS |
| black | bubbles | 0.209 | 33 | 0.169 | 30 | PASS |
| black | generic cell | 0.403 | 16 | 0.403 | 16 | PASS |

## Editable-source hashes

- `white-blood-cell_color_18_SOURCE.svg`: `180ed62f72ba4d6d112993ccdca7277597ca10f92a96311034853486df8b2701`
- `white-blood-cell_color_SOURCE.svg`: `9ea9083ece3fa26e36a6e90149adeb65e3dde910a52e93e58c64944784b2eebc`
- `white-blood-cell_bw_18_SOURCE.svg`: `22cfd98181041a6daff9f9dac9829791282a111250a621fff3416c530675e155`
- `white-blood-cell_bw_SOURCE.svg`: `f945a716916c73d2bc043007b48eb695ee64954946b339e631bd9b83aecbfe6e`

OpenMoji comparators are pinned to commit `d05930b34516a0a3ff00aad0288ee05364cebd8b`. Provenance and full URLs are in
`../comparisons/SOURCES.md`.

Reproduce with:

```powershell
python scripts/validate_white_blood_cell_artwork.py `
  --proposal-dir submissions/v1.19.0/white-blood-cell `
  --json-output submissions/v1.19.0/white-blood-cell/validation/computer-validation.json `
  --markdown-output submissions/v1.19.0/white-blood-cell/validation/computer-validation.md
```
