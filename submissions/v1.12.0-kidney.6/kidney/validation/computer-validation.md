# Kidney Artwork Computer Validation

Validation date: 2026-07-26

Status: **PASS**

## Scope

This is a deterministic technical separability test. It validates exact image dimensions, a true
black-and-white palette, foreground connectedness, and machine-visible silhouette distance from six nearby or
plausible-confusion emoji. It does not claim to measure human semantic recognition.

Thresholds were fixed before the release run: normalized silhouette IoU must be at most
`0.72`, 64-bit difference-hash distance must be at least `16`, foreground
components must not exceed two, and the largest component must contain at least 95% of visible pixels.

## Required assets

| Asset | Dimensions | B&W palette | Components | Result |
| --- | ---: | --- | ---: | --- |
| kidney_color_18x18_SUBMIT.png | 18x18 | n/a | 1 | PASS |
| kidney_color_72x72_SUBMIT.png | 72x72 | n/a | 1 | PASS |
| kidney_bw_18x18_SUBMIT.png | 18x18 | pass | 1 | PASS |
| kidney_bw_72x72_SUBMIT.png | 72x72 | pass | 1 | PASS |

## 18x18 silhouette comparisons

| Proposal asset | Comparator | Normalized IoU | dHash distance | Result |
| --- | --- | ---: | ---: | --- |
| color_18x18 | anatomical heart | 0.467 | 33 | PASS |
| color_18x18 | balloon | 0.394 | 28 | PASS |
| color_18x18 | beans | 0.607 | 25 | PASS |
| color_18x18 | droplet | 0.441 | 30 | PASS |
| color_18x18 | light bulb | 0.364 | 38 | PASS |
| color_18x18 | lungs | 0.698 | 23 | PASS |
| bw_18x18 | anatomical heart | 0.436 | 27 | PASS |
| bw_18x18 | balloon | 0.319 | 30 | PASS |
| bw_18x18 | beans | 0.503 | 27 | PASS |
| bw_18x18 | droplet | 0.390 | 26 | PASS |
| bw_18x18 | light bulb | 0.344 | 32 | PASS |
| bw_18x18 | lungs | 0.582 | 23 | PASS |

## Comparator provenance

All comparators are pinned to Noto Emoji commit `8998f5dd683424a73e2314a8c1f1e359c19e8742`:

- anatomical heart: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1fac0.png (SHA-256 `d085a08da7477258c7c9d97b336c1cd9890b2759da3212455d641cb88bb49673`)
- balloon: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1f388.png (SHA-256 `7efbfa64b59cbee4a61a17b1d5af8887cb70dda9b94e9e8463a557fe6e01cd11`)
- beans: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1fad8.png (SHA-256 `e37d8c68eb71eb2eb9845e1bc57d92ebd566f01fba48c33117c9fc55a4b3d8d9`)
- droplet: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1f4a7.png (SHA-256 `f523b07e40891a9765bac75766fc426c4cbcf405eaf9bde95a2657971755a463`)
- light bulb: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1f4a1.png (SHA-256 `3b57447c18ca9a6bd2df7f17fdf22fb5ee1135bd07fda592e2a34c705060c1c2`)
- lungs: https://raw.githubusercontent.com/googlefonts/noto-emoji/8998f5dd683424a73e2314a8c1f1e359c19e8742/png/128/emoji_u1fac1.png (SHA-256 `61dc72e8d34d51870196ae3a2fd0644a44e283781fe2ef9d9456a0d8eeec8e32`)

Noto Emoji license:

https://github.com/googlefonts/noto-emoji/blob/master/LICENSE

Reproduce with:

```powershell
python scripts/validate_kidney_artwork.py `
  --proposal-dir submissions/v1.12.0-kidney.6/kidney `
  --json-output submissions/v1.12.0-kidney.6/kidney/validation/computer-validation.json `
  --markdown-output submissions/v1.12.0-kidney.6/kidney/validation/computer-validation.md
```
