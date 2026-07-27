# Kidney Emoji Artwork Specification

Version: 1.1.0

Status: paired concept approved; deterministic small-size refinement built in `v1.12.0-kidney.4`

Generator: GPT Image 2 built-in image workflow

## Goal

Create a Kidney emoji whose identity is carried by a recognizable paired-organ composition rather than by a
generic bean silhouette. Preserve the older campaign artwork's immediate anatomical read while removing the
full vascular tower and other textbook-level detail that fails at 18x18 pixels.

## Reference roles

- `public/images/emoji/kidneysnew2.png`: anatomical identity reference only.
- `submissions/v1.2.0/kidney/images/kidney_color_72x72_SUBMIT.png`: simplified paired-composition reference.
- `submissions/v1.10.0/kidney/images/kidney_color_72x72_SUBMIT.png`: rendering-style reference only.
- `kidney-paired-gpt-image-2-concept.png`: approved GPT Image 2 direction and proportions reference.
- Do not reproduce a reference literally or imitate any vendor's proprietary emoji design.

## Required silhouette

- Two large kidney forms with their medial notches facing inward.
- The kidney on the viewer's left sits slightly higher; the kidney on the viewer's right sits slightly lower.
- Both outer contours remain independently legible at 18x18 pixels.
- One short, thick central vascular junction connects the visual group without becoming a full aorta or vena
  cava column.
- Two short, thick ureter cues descend from the inward hila.
- The complete mark reads as paired kidneys, not two beans, lungs, a uterus, a heart, or a peach.

## Required styling

- Clean vector-like 2D emoji rendering.
- Deep maroon bodies with restrained darker lower shading.
- Dark burgundy continuous outlines with rounded joins.
- Restrained red and blue central vessel cues and warm tan ureters.
- One restrained upper-left highlight on each kidney.
- Pure white background in submission previews.
- Generous, even padding with no cropping.

## Prohibited details

- No full-height aorta or vena cava.
- No bladder, long ureters, nephron detail, labels, letters, numbers, arrows, or medical symbols.
- No thin vessels or anatomy that vanishes below 72 pixels.
- No trachea-like central stem, heart-shaped pairing, bean pod, face, limbs, or decorative background.
- No photorealism, gore, wet tissue, glassy material, watermark, or vendor-specific emoji imitation.

## Small-size acceptance tests

At 18x18 pixels:

1. Two inward-facing kidney bodies remain visibly separate.
2. The vertical offset remains visible and prevents a symmetric lungs or uterus read.
3. The central vessel and downward ureter cues survive without becoming visual noise.
4. The color artwork does not primarily read as beans, lungs, heart, balloon, or a reproductive-organ icon.
5. The true black-and-white version uses white-filled outlined bodies and does not collapse into a solid blob.

At 72x72 pixels:

1. The hila are clear and the paired anatomy reads immediately.
2. Curves and outline weights are consistent.
3. The short plumbing details remain subordinate to the two dominant kidney forms.
4. No raster halos, clipped edges, background noise, or unintended internal marks are visible.

## Computer-validation requirement

Computer validation checks exact dimensions, strict black-and-white palette, connectedness, normalized IoU,
and difference-hash separation against the pinned Anatomical Heart, Balloon, Beans, Droplet, Light Bulb, and
Lungs assets. Comparator labels make the confusion targets explicit, but the calculations remain technical
separation evidence and do not claim human semantic recognition.

Shuhan's dated actual-size decision on the exact four assets is the complete human image gate. No external
participant panel, crowd test, minimum sample, recognition percentage, or confusion matrix is required. A
material asset change invalidates the prior exact-asset decision and returns the changed assets to Shuhan.

The `.4` result passes all twelve comparator rows without changing the fixed thresholds. The former color
18x18 Lungs IoU of `0.750` is `0.698` after the purpose-built small-size refinement, below the unchanged `0.72`
ceiling.

## Current files

- Approved full-size concept: `docs/design/kidney-emoji-2026-07/kidney-paired-gpt-image-2-concept.png`
- Deterministic SVG masters: `submissions/v1.12.0-kidney.4/kidney/images/kidney_color_SOURCE.svg` and
  `submissions/v1.12.0-kidney.4/kidney/images/kidney_bw_SOURCE.svg`
- Purpose-built 18-pixel SVGs: `submissions/v1.12.0-kidney.4/kidney/images/kidney_color_18_SOURCE.svg` and
  `submissions/v1.12.0-kidney.4/kidney/images/kidney_bw_18_SOURCE.svg`
- Exact-size color and true black-and-white PNGs: `submissions/v1.12.0-kidney.4/kidney/images/`

## Generation prompt

Create a refined paired-kidney emoji concept combining the unmistakable anatomical identity of the older
paired design with the clean, chunky legibility of the newer single-kidney design. Use two asymmetrical
maroon kidneys with inward-facing hila, one slightly lower than the other, one short red-and-blue central
vascular junction, and two short tan ureters. Use bold outlines, a limited palette, and no fine anatomy,
full-height vascular tower, bladder, text, watermark, or decorative background.

## Submission-production decision

The generated raster is a design reference rather than an exact Unicode submission asset. Its selected
geometry is rebuilt as project-authored SVG artwork with exact-size color and black-and-white PNG exports in
the isolated Kidney review package. The package must pass rendered-page inspection and computer validation
before canonical promotion.
