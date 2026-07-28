# Kidney v2.10.0 Artwork Computer Validation

Validation date: 2026-07-28

Status: **PASS**

## Scope

This is deterministic file inspection. It validates dimensions, alpha geometry, color counts, black-and-white
palette, and consistency between the color and black-and-white silhouettes. It does not claim to establish
human semantic recognition.

## Required assets

| Asset | Dimensions | Opaque palette | Alpha components | Result |
| --- | ---: | --- | ---: | --- |
| `v2.10.0_kidney_color_18x18_SUBMIT.png` | 18x18 | 6 colors | 1 | PASS |
| `v2.10.0_kidney_color_72x72_SUBMIT.png` | 72x72 | color | 1 | PASS |
| `v2.10.0_kidney_bw_18x18_SUBMIT.png` | 18x18 | strict black and white | 1 | PASS |
| `v2.10.0_kidney_bw_72x72_SUBMIT.png` | 72x72 | strict black and white | 1 | PASS |

## Native 18-pixel checks

- Both assets have exact 18x18 dimensions and a transparent outer margin.
- Both use fully transparent background pixels and fully opaque foreground pixels; no fractional alpha is used.
- The foreground bounding box is `(2, 2)-(16, 14)`, leaving at least two transparent pixels on every edge.
- The color and black-and-white alpha masks have an intersection-over-union of `0.9464`.
- The black-and-white asset uses only pure black and pure white opaque pixels.
- The sources declare `width="18"`, `height="18"`, `viewBox="0 0 18 18"`, and
  `shape-rendering="crispEdges"`.
- The native-size and nearest-neighbor enlarged review board was visually inspected on a white background.

## Regression controls

- Both 72x72 submission PNGs are byte-identical to v2.9.0.
- Both master PNGs and both 72x72 source SVGs are byte-identical to v2.9.0.
- The new 18x18 PNGs were generated directly from hand-authored native-grid geometry by
  `scripts/build_kidney_v210_18px.py`; they are not downsampled versions of the master artwork.

## Reproduction commands

```powershell
python scripts/build_kidney_v210_18px.py submissions/v2.10.0/images --prefix v2.10.0
python docs/research/emoji-image-evidence/analyze_proposal_image_set.py `
  --input-dir submissions/v2.10.0/images `
  --output submissions/v2.10.0/validation/computer-validation.json `
  --asset-set "Kidney proposal v2.10.0" `
  --color-18 v2.10.0_kidney_color_18x18_SUBMIT.png `
  --color-72 v2.10.0_kidney_color_72x72_SUBMIT.png `
  --bw-18 v2.10.0_kidney_bw_18x18_SUBMIT.png `
  --bw-72 v2.10.0_kidney_bw_72x72_SUBMIT.png
```
