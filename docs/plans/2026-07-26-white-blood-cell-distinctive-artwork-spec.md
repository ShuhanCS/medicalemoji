# Definitive White Blood Cell Emoji Artwork Specification

Version: 2.0.0

Date: 2026-07-26

Status: Definitive production brief; final assets require visual approval and validation

## Decision

Use one front-facing, stylized white blood cell based on the familiar neutrophil form: a pale, softly irregular
cell body enclosing one large, connected, asymmetric three-lobed purple nucleus. The silhouette should borrow
the supplied reference image's broad organic membrane character, but not its dense surface fuzz or opaque
photorealism.

This is the strongest direction because it combines three cues that survive at emoji size:

1. A pale rounded body communicates a cell.
2. A softly folded, irregular edge makes it organic rather than a generic diagram.
3. One connected segmented nucleus distinguishes a white blood cell from Microbe, Drop of Blood, and a generic
   cell with a round center.

The artwork represents the broad White Blood Cell category. Neutrophil morphology is the visual model, not a
narrower proposed character name.

## Visual concept

### Pose and composition

- Show one complete cell, centered and viewed straight on.
- Use a compact, nearly round silhouette with deliberate asymmetry; it must not be a perfect circle.
- Give the membrane five to seven shallow, broad undulations. They should read as soft folds, not spikes,
  tentacles, cilia, or hairs.
- Place the nucleus slightly off-center so it feels biological and does not resemble a target, flower, face, or
  camera lens.
- Arrange the nucleus as a loose bent chain or shallow S: one larger oval lobe, one medium lobe, and one smaller
  lobe, joined by clearly visible bridges. Do not arrange three equal circles as a clover.
- Keep the exterior transparent. Do not add a blood-vessel scene, red-cell background, shield, cross, sparkle,
  text, badge, or enclosing circle.

### Required recognition order

At first glance, the image must read in this order:

1. One organic cell.
2. One large segmented center.
3. A pale immune cell rather than a germ or red blood drop.

The nucleus is the identity cue. Membrane texture supports it but never competes with it.

## Colour artwork

### Palette

| Element | Target | Function |
| --- | --- | --- |
| Cytoplasm | Cool near-white, approximately `#EEF7F6` | Reads as a white cell while remaining visible |
| Membrane edge | Muted blue-teal grey, approximately `#668B91` | Defines the pale body on light and dark interfaces |
| Nucleus | Deep violet, approximately `#64398F` | Supplies the strongest internal recognition cue |
| Nucleus shade | Dark violet, approximately `#4D2C73`, 72x72 only | Adds restrained depth without fragmenting the nucleus |
| Surface accents | Pale blue-grey or lavender within 8% contrast of the body | Adds organic character at 72x72 only |

The exact colour values may be adjusted for contrast, but the body must remain pale and the nucleus must remain
the darkest, most saturated feature. Avoid pink or red cytoplasm, green germ-like colouring, and multicolour
granules.

### Form

- Use a clean outer membrane with modest depth, not a heavy cartoon stroke.
- Let the cytoplasm remain mostly open and quiet around the nucleus.
- At 72x72, add at most three to five broad, low-contrast dimples or folds. These are secondary texture, not
  separate objects.
- Use no photorealistic noise, pores, filaments, glossy beads, or dense granulation.
- Do not reproduce, trace, or embed pixels from the supplied reference. It is morphology reference only.

## Exact 18x18 master

The 18x18 asset is the design master for recognition, not a mechanical reduction of the 72x72 illustration.

- Canvas: exactly 18x18 pixels.
- Cell footprint: approximately 15x15 to 16x16 pixels, with at least one transparent pixel of breathing room on
  every side.
- Membrane: one-pixel visible edge; five to seven shallow turns around the silhouette; no projection narrower
  than two pixels at its base.
- Cytoplasm: one quiet pale mass. Remove all surface accents that cannot occupy at least a two-pixel form.
- Nucleus: one continuous dark-violet feature occupying approximately 38% to 46% of the visible cell area.
- Lobes: three unequal rounded lobes arranged asymmetrically along a bent path, not three equal discs.
- Bridges: at least two pixels thick at their narrowest rendered point so the nucleus remains visibly connected.
- Separation: retain at least one pixel of pale cytoplasm between the nucleus and membrane everywhere.
- Shading: one body colour, one edge colour, and one nucleus colour are sufficient. Any extra colour must improve
  the native-size read rather than appear only under enlargement.
- Pixel review: inspect at native 18x18, not only at zoom. Pixel-snap the silhouette, bridges, and clear-space
  manually after any generated or vector source is reduced.

The 18x18 colour PNG may use antialiasing, but its structure must remain legible without relying on translucent
single-pixel noise.

## Exact 72x72 master

- Canvas: exactly 72x72 pixels, transparent outside the cell.
- Preserve the 18x18 silhouette, nucleus arrangement, and relative proportions.
- Use a two-to-three-pixel membrane edge, softened where appropriate.
- Add shallow volume through one restrained highlight and one restrained shadow.
- Add only broad membrane folds or dimples; keep all surface texture below the visual contrast of the nucleus.
- Keep the three nucleus lobes visibly connected at native 72x72 and after reduction to 18x18.
- Avoid extra biological detail that changes the category, including visible organelles, antibodies, engulfed
  microbes, labels, or subtype-specific annotations.

## True black-and-white artwork

The black-and-white assets must be purpose-built two-colour drawings, not greyscale conversions.

- Use only pure black `#000000` and pure white `#FFFFFF` in the exported PNGs.
- Use a black outer membrane, white cell body, and one solid black connected three-lobed nucleus.
- Preserve the same silhouette and nucleus arrangement as the colour version.
- Do not use grey, transparency within the cell, hatching, stippling, or disconnected black texture.
- The result may contain two main black components—the membrane and nucleus—but neither may fragment.

## Distinction from the nearest visual alternatives

| Alternative | White Blood Cell must differ by |
| --- | --- |
| Microbe | No radial spikes, corona, face, or germ-like surface field; the connected lobed nucleus dominates |
| Drop of Blood | No teardrop point, liquid highlight, red fill, or falling orientation |
| Generic cell diagram | No perfect circular membrane or single round nucleus; use an irregular edge and segmented center |
| Bubbles | No repeated detached circles or cluster of equal round forms |
| Flower or clover | Unequal nucleus lobes follow a bent chain and remain enclosed inside a cell membrane |
| Pollen or fuzzy sphere | No dense hairs, repeated nodules, or opaque surface that hides the nucleus |

## GPT Image production prompt

Use this prompt to generate a high-resolution concept source. The result is an art-direction reference and must
then be redrawn or cleaned into the exact 18x18 and 72x72 masters above.

> Create an original emoji-style pictograph of one white blood cell, using a neutrophil as the visual model for
> the broad white-blood-cell category. Front-facing isolated cell on a transparent background, centered with
> generous clear space. The cell body is cool near-white with a muted blue-teal membrane edge and a softly
> irregular, organic silhouette made from five to seven broad shallow folds. Inside is one dominant deep-purple
> nucleus made of three unequal rounded lobes connected into a bent chain or shallow S, slightly off-center. The
> nucleus is unmistakably one connected feature, not three separate circles. Clean modern emoji rendering,
> simple bold forms, restrained soft depth, excellent recognition at 18 pixels. No text, no face, no shield, no
> medical cross, no blood-vessel scene, no red background, no other cells, no microbe, no radial spikes, no
> tentacles, no hairs, no dense granules, no photorealism, no flower or clover arrangement, and no perfect circular
> cell or nucleus.

Generate the colour concept first. Derive the black-and-white design from the approved geometry rather than
asking the model to reinterpret the object.

## Production workflow

1. Generate several high-resolution concepts from the single prompt without using third-party emoji art as a
   visual reference.
2. Select the concept with the clearest asymmetric three-lobed nucleus and quietest organic silhouette.
3. Redraw it as original editable vector geometry; do not place generated raster pixels directly into the final
   proposal assets.
4. Construct and pixel-snap the 18x18 colour master independently.
5. Construct the matching 72x72 colour master.
6. Build true two-colour 18x18 and 72x72 variants from the same geometry.
7. Validate dimensions, palette, nucleus connectedness, clear space, and separation from the nearest existing
   emoji.
8. Review all four assets at native size on white, black, and mid-grey interface backgrounds.
9. Place only the four original final assets in the reviewer-facing proposal. Do not include OpenMoji or the
   supplied reference image in the PDF.

## Acceptance gates

The artwork is ready only when every gate passes:

- **Native-size identity:** At 18x18, the cell body and connected segmented nucleus are both immediately visible.
- **Microbe separation:** No viewer-facing cue depends on spikes, fuzz, or a germ-like outline.
- **Broad-category fit:** The image can be described as White Blood Cell without naming a subtype.
- **Silhouette integrity:** The cell remains one compact mass with no detached membrane fragments.
- **Nucleus integrity:** The nucleus remains one connected, asymmetric three-lobed feature in colour and black
  and white.
- **Monochrome parity:** The true black-and-white image retains the same identity without shade or colour.
- **Small-size restraint:** No important feature exists only at 72x72.
- **Rights integrity:** All final geometry is original Medical Emoji work and can be covered by the proposal's
  CC0 and rights statement.
- **Reviewer-facing restraint:** The proposal describes stable visible cues and leaves vendors free to vary
  outline, lobe count, colour, and shading.

Before claiming recognition in the proposal, conduct and record a genuine human test. A useful internal gate is
to show the unlabeled 18x18 asset among Microbe, Drop of Blood, and a generic cell to at least ten people: at
least eight should identify it as a white blood cell or immune cell, and no more than one should identify it as a
virus or germ.

## Proposal wording supported by this design

> White Blood Cell is shown as a pale, softly irregular cell with one large, connected, three-lobed center, or
> nucleus. At 18 pixels, that segmented center distinguishes it from Microbe's spiked edge, Drop of Blood's
> teardrop shape, and a generic cell's round interior. Vendors may vary the outline, lobe count, colour, and
> shading while preserving the pale cell body and single connected lobed center.

This paragraph specifies the essential recognition cues without requiring vendors to reproduce the sample
image exactly.
