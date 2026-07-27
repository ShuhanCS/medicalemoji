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
| white-blood-cell_bw_18x18_SUBMIT.png | 18x18 | pass | 2 | PASS |
| white-blood-cell_bw_72x72_SUBMIT.png | 72x72 | pass | 2 | PASS |

## 18x18 comparisons

| Variant | Comparator | Silhouette IoU | Silhouette dHash | Feature IoU | Feature dHash | Result |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| color | microbe | 0.495 | 29 | 0.270 | 29 | PASS |
| color | drop of blood | 0.631 | 26 | 0.304 | 28 | PASS |
| color | soap | 0.510 | 21 | 0.165 | 33 | PASS |
| color | bubbles | 0.552 | 30 | 0.242 | 23 | PASS |
| color | generic cell | 0.864 | 18 | 0.328 | 17 | PASS |
| black | microbe | 0.190 | 37 | 0.121 | 31 | PASS |
| black | drop of blood | 0.189 | 33 | 0.129 | 27 | PASS |
| black | soap | 0.153 | 35 | 0.071 | 33 | PASS |
| black | bubbles | 0.272 | 31 | 0.183 | 26 | PASS |
| black | generic cell | 0.350 | 18 | 0.350 | 18 | PASS |

## Editable-source hashes

- `white-blood-cell_color_18_SOURCE.svg`: `70b502eb0e6d454bbb926f09ca776cd85b9e773be44b090989dbb156d87f6ce3`
- `white-blood-cell_color_SOURCE.svg`: `50f9e4b6a4fc5024c2ed9eb9987a1f7957f40e7e89c531f827a85b8cf19b87ce`
- `white-blood-cell_bw_18_SOURCE.svg`: `cf171071a8077367134bb3af0cab4877feb2f077a5b5ea48447ce869e5b7d5a8`
- `white-blood-cell_bw_SOURCE.svg`: `09a930ec33acad061763d409a9d81d65510389c2070a94f4743cf98fde90d101`

OpenMoji comparators are pinned to commit `d05930b34516a0a3ff00aad0288ee05364cebd8b`. Provenance and full URLs are in
`../comparisons/SOURCES.md`.

Reproduce with:

```powershell
python scripts/validate_white_blood_cell_artwork.py `
  --proposal-dir submissions/v1.17.0/white-blood-cell `
  --json-output submissions/v1.17.0/white-blood-cell/validation/computer-validation.json `
  --markdown-output submissions/v1.17.0/white-blood-cell/validation/computer-validation.md
```
