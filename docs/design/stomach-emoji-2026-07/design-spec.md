# Stomach Emoji Artwork Specification

Status: concept approved and rebuilt as deterministic v1.11.0 submission artwork; recognition testing remains open

Generator: `gpt-image-2`, high quality, 1024x1024 edit workflow

## Goal

Create a stomach emoji whose identity is carried by its outer silhouette and remains immediately recognizable
at 18x18 pixels. The artwork should combine the older campaign image's strong anatomical read with a clean,
contemporary emoji finish.

## Reference roles

- `public/images/emoji/3-stomach.png`: anatomical silhouette reference only.
- `submissions/v1.9.0/stomach/images/stomach_color_72x72_SUBMIT.png`: simplified rendering reference only.
- Do not reproduce either reference literally or imitate a vendor's proprietary emoji design.

## Required silhouette

- Strong asymmetric J-shaped stomach.
- Long, narrow inlet visible from above.
- Deep inner concavity that remains open at 18x18.
- Broad lower body shaped as an organ rather than a circle, bean, or pouch.
- Distinct short outlet separated from the body at small size.
- Anatomically plausible without becoming a textbook diagram.
- Recognizable from the solid silhouette alone.

## Required styling

- Clean vector-like 2D emoji rendering.
- Warm coral-red body with restrained darker lower shading.
- Dark cranberry continuous outline with rounded joins.
- One restrained highlight for volume.
- Pure white background in submission previews.
- Generous, even padding with no cropping.

## Prohibited details

- No face, limbs, labels, letters, numbers, arrows, or medical symbols.
- No veins, folds, rugae, incisions, decorative crease, or internal anatomy.
- No cut-open inlet or visible lumen.
- No cast shadow, floor, frame, badge, or background decoration.
- No photorealism, gore, wet tissue, glassy material, or plastic-toy rendering.
- No trademark, watermark, or vendor-specific emoji imitation.

## Small-size acceptance tests

At 18x18 pixels:

1. The inlet, inner concavity, and outlet remain visually separate.
2. The image reads as a stomach without a label or surrounding proposal text.
3. It does not primarily resemble a kidney, bean, liver, anatomical heart, meat-on-bone, balloon, or pouch.
4. The outline does not close the inner concavity or merge the outlet into the body.
5. A true black-and-white derivative remains recognizable from silhouette alone.

At 72x72 pixels:

1. Curves are smooth and the outline weight is consistent.
2. The highlight supports volume without becoming a second visual feature.
3. No raster halos, clipped edges, background noise, or unintended internal marks are visible.

## Current GPT Image 2 concept

- Full-size design reference: `docs/design/stomach-emoji-2026-07/stomach-gpt-image-2-concept.png`
- Deterministic SVG masters: `submissions/v1.11.0/stomach/images/stomach_color_SOURCE.svg` and
  `submissions/v1.11.0/stomach/images/stomach_bw_SOURCE.svg`
- Purpose-built 18-pixel SVGs: `submissions/v1.11.0/stomach/images/stomach_color_18_SOURCE.svg` and
  `submissions/v1.11.0/stomach/images/stomach_bw_18_SOURCE.svg`
- Exact-size color and true black-and-white PNGs: `submissions/v1.11.0/stomach/images/`

## Submission-production requirement

The generated raster remains a design reference, not a Unicode submission asset. The selected geometry has
been rebuilt as project-authored SVG artwork with exact-size color and true black-and-white PNG exports in
v1.11.0. Before filing, complete deterministic comparator validation, blind human recognition testing, and
final review of the artwork-rights record.
