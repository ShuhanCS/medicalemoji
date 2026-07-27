# Stomach Emoji Artwork Specification

Status: concept approved and selected as the Candidate.8 submission artwork; Shuhan's exact-asset approval remains open

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

## Current GPT Image 2 artwork

- Approved full-size source: `docs/design/stomach-emoji-2026-07/stomach-gpt-image-2-concept.png`
- Approved source SHA-256: `250389e208e3d71488e1895b49c7d4fd69e95507eb3d06f73060db7b34767d7a`
- Reproducible builder: `scripts/build_stomach_concept_assets.py`
- Exact-size color and true black-and-white PNGs:
  `docs/proposals/stomach-emoji-2026/candidate-v1.12/images/`
- The v1.11.0 SVG reconstruction is historical and is not the selected Candidate.8 artwork.

## Submission-production requirement

The approved project artwork is the submission source. Candidate.8 uses direct deterministic reductions for
the 18x18 and 72x72 color examples and matching strict black-and-white silhouette derivatives. Before filing,
complete deterministic comparator validation, obtain Shuhan's dated approval of the exact four assets at
actual size, and complete final review of the artwork-rights record. No participant panel or blind recognition
study is required.
