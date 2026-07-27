# Liver Emoji Artwork Redesign Specification

Version: 1.0.0

Date: 2026-07-26

Status: design direction proposed; no submission artwork changed

Scope: Liver artwork only. Proposal eligibility, authorship, rights, evidence, and selection-factor prose are
settled inputs and are not reopened by this specification.

## Decision

Replace the current flattened-oval direction with a silhouette-first anterior liver emblem. The recommended
design uses one continuous asymmetric wedge with a dominant domed lobe, a smaller tapered lobe, a shallow lower
notch, a short curved lobe division, and a gallbladder nested into the lower contour rather than hanging below
the organ.

Develop the final artwork as a controlled vector system. Use image generation for concept exploration only,
then redraw the selected geometry deliberately and create a separate purpose-built 18x18 master. Do not treat a
mechanical reduction of a 1024px or 72px image as the final keyboard-size asset.

## Why the current artwork should be reconsidered

Current exact assets:

- `submissions/v1.12.0-liver.10/liver/images/liver_color_18x18_SUBMIT.png`
- `submissions/v1.12.0-liver.10/liver/images/liver_color_72x72_SUBMIT.png`
- `submissions/v1.12.0-liver.10/liver/images/liver_bw_18x18_SUBMIT.png`
- `submissions/v1.12.0-liver.10/liver/images/liver_bw_72x72_SUBMIT.png`

The current artwork is clean and technically valid, but it asks color and context to do too much of the
recognition work:

1. The outer contour is close to a low rounded oval. The difference between the two lobes is less visible than
   the proposal prose suggests.
2. The straight diagonal division reads more like a cut or seam than a natural surface landmark.
3. The gallbladder hangs from the bottom as a separate droplet. In black and white it merges with the seam and
   can look like a pendant, leaf, or punctuation mark.
4. At 18x18, the large-lobe/small-lobe relationship collapses. The result can read as a bean, fruit, meat cut,
   leaf, or unspecified internal organ.
5. The highlight and shading make the 72px version attractive, but they do not repair the weak 18px silhouette.

The redesign problem is therefore not "make it more anatomical." It is "choose the anatomical facts that
create the strongest icon."

## What successful submissions teach us

The current Unicode rule is recognizability without foreknowledge at typical emoji size, supported by exact
18x18 and 72x72 color and true black-and-white examples:

https://www.unicode.org/emoji/proposals.html

Accepted proposals show several workable visual styles. The repeatable lesson is that one strong outer contour
plus two or three stable landmarks matters more than realism or detail.

| Accepted proposal | Visual strategy | Lesson for Liver | What not to copy |
| --- | --- | --- | --- |
| Anatomical Heart, L2/19-150 | Muscular teardrop body plus a crown of large vessels. The vessel crown survives as a category cue even when small. | Give Liver one unmistakable mass and a few large anatomical cues. | Its 2019 first page says black-and-white art was pending, so use it as a visual lesson, not a current-format model. |
| X-Ray, L2/20-214 | High-contrast square field plus ribs and spine. The image is understood from a small number of conventional cues. | Use landmarks that remain readable after detail disappears. | Do not add a frame, medical cross, label, or diagnostic-device context to Liver. |
| Fingerprint, L2/23-258 | Simple fingertip arch plus a sparse ridge system shared by color and black-and-white versions. | A conventional graphic motif can be more recognizable than realistic rendering. | Do not introduce fine surface anatomy merely to appear precise. |
| Lighthouse, L2/25-256 | Tapered tower, repeated bands, lantern, and light beam. Color and line art preserve the same hierarchy. | Design the color and black-and-white forms as one visual system. | Do not mistake AI rendering polish for small-size identity. |
| Beans, L2/20-226 | Deep kidney-bean curve, seed highlight, and a small cluster establish the category. | Treat Beans as a direct visual confuser and avoid its deep C-shaped indentation. | Do not use a kidney-bean contour, paired red shapes, or a seed-like highlight. |

Source proposals:

- https://www.unicode.org/L2/L2019/19150-heart-emoji.pdf
- https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf
- https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf
- https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf
- https://www.unicode.org/L2/L2020/20226-beans-emoji.pdf

These documents were accepted under different historical formats. Their artwork can inform visual judgment,
but the 2026 proposal requirements control the final deliverables.

## Anatomy-to-icon abstraction

The proposed mark should preserve five facts and discard the rest.

### Preserve

1. One continuous organ mass, not two attached ovals.
2. A dominant rounded lobe occupying roughly two thirds of the mass.
3. A smaller lobe that tapers to a flatter, narrower end.
4. A shallow lower notch or step that breaks the oval contour.
5. A short surface division that reinforces the lobe relationship without cutting the organ in half.

The gallbladder is a secondary cue. It may help the color image, but the Liver must remain identifiable when it
is removed.

### Discard

- Portal vessels, bile ducts, veins, labels, arrows, lobule texture, cut surfaces, and surgical detail.
- A textbook inferior view with several fossae or impressions.
- A perfectly smooth ellipse.
- A deep central bean indentation.
- A full-height seam from top edge to bottom edge.
- Any cue that resembles a medical logo, badge, or UI icon.

## Candidate directions

Produce three directions before selecting final art. Each direction must be shown in color and strict black and
white at actual 18x18 and 72x72 sizes.

### Candidate A: Anterior wedge with nested gallbladder - recommended

- Single broad wedge with a long domed upper contour.
- Dominant lobe on one side and a visibly thinner, tapered lobe on the other.
- Lower edge rises into a shallow notch before the tapered lobe.
- Short curved lobe division, ending inside the organ rather than touching both outer edges.
- Gallbladder sits partly inside the lower notch, with no thin stem and no dangling appearance.

Why this is strongest: the outer contour carries the identity, while the lobe division and nested gallbladder
confirm it. It remains compatible with vendor simplification because either secondary cue can be reduced.

### Candidate B: Pure anterior silhouette without gallbladder - required backup

- Same dominant-lobe/tapered-lobe structure as Candidate A.
- More pronounced lower notch.
- No green secondary object.
- One restrained curved surface division in color and black and white.

Why it is useful: it tests whether the Liver can succeed on silhouette alone. If Candidate A only wins because
of the green gallbladder, the underlying shape is not strong enough.

### Candidate C: Slight anterior-inferior three-quarter view - exploratory

- Moderate tilt exposes a small portion of the underside.
- Gallbladder is visibly seated under the dominant lobe.
- No vessels or duct system.
- Outer contour remains a single wedge rather than a folded or cut-open organ.

Risk: this direction can become anatomically busy, meat-like, or unrecognizable at 18x18. Select it only if the
actual-size assets clearly outperform both anterior directions.

## Recommended geometry for Candidate A

These are design targets, not medical measurements.

- Canvas occupancy at 72x72: approximately 60-62px wide and 36-40px high, centered with even optical padding.
- Canvas occupancy at 18x18: approximately 15-16px wide and 10px high.
- Overall width-to-height target: 1.50-1.70. Avoid the flatter appearance produced by ratios near 2:1.
- Dominant lobe: approximately 62-68 percent of the visible mass.
- Smaller lobe: approximately 32-38 percent, ending in a clear taper rather than another round bulb.
- Upper contour: one long convex dome with no central dip.
- Lower contour: one shallow step or V-like notch, followed by a rising tapered edge.
- Surface division: gently curved, visually subordinate, and no longer than about half the organ height.
- Gallbladder at 72px: compact oval or pear form seated into the notch, with at least half its height overlapping
  the liver silhouette.
- Gallbladder at 18px: at most a 2x3px green cue. It may be omitted if it creates noise.

Do not force anatomical laterality into the proposal. Vendors may mirror or restyle the image. The submission
example only needs a coherent, recognizable liver paradigm.

## Color system

- Main body: deep warm liver red or burgundy, not bright candy red.
- Secondary body tone: one darker plane under the dominant lobe or lower edge.
- Highlight: one restrained warm highlight supporting volume, not a glossy white spot that reads as fruit.
- Outline: dark burgundy, continuous, rounded, and visually heavier than the surface division.
- Gallbladder: muted olive or natural green, small enough to remain subordinate.
- Background: pure white in submission assets.
- No cast shadow, floor, badge, frame, glow, wet-tissue texture, or photorealism.

The 72px image may use restrained gradients. The 18px image should use a reduced palette and placed pixels so
that the lobe boundary and lower notch remain stable.

## True black-and-white system

Use line art rather than an automatic grayscale conversion.

- Pure black and pure white only. No gray, transparency-as-gray, or anti-aliased colored edge pixels.
- White-filled liver with a continuous black outer contour.
- One short black curved surface division.
- Preserve the lower notch as white negative space.
- If the gallbladder is included, separate it from the body with a visible white gap or nested negative-space
  boundary. It must not merge into the surface division as in the current version.
- If the gallbladder harms the 18px black-and-white read, omit it at 18px. The silhouette must remain sufficient.

## Purpose-built size masters

### 72x72 master

- Establish the final proportions, outline system, restrained volume, and optional gallbladder.
- Keep every essential cue large enough to have a deliberate 18px analogue.
- Do not add detail that exists only to make the large image feel finished.

### 18x18 master

- Redraw after the 72px direction is selected.
- Use a one-pixel outer contour where needed, with no broken outline.
- Preserve the upper dome, tapered end, and lower notch before preserving shading.
- Shorten or simplify the surface division rather than letting it become a full diagonal slash.
- Remove any gallbladder stem, minor highlight, or shading step that creates a one-pixel artifact.
- Check the asset at actual size on a normal white document page, not only enlarged with nearest-neighbor pixels.

## Actual-size selection board

Build one board with rows for:

1. Color 72x72.
2. Color 18x18.
3. Black-and-white 72x72.
4. Black-and-white 18x18.
5. Solid-silhouette-only 18x18.

Use columns for Current, Candidate A, Candidate B, Candidate C, Anatomical Heart, Lungs, Brain, Cut of Meat, and
Beans. The accepted emoji comparators are for confusion testing, not justification by precedent.

Shuhan's actual-size choice of the exact four final assets is the controlling human decision. No participant
panel, recognition percentage, or invented scoring threshold is required.

## Selection questions

Answer these in order:

1. Does the solid outer contour read as one asymmetric liver-like organ rather than a bean or oval?
2. Is the dominant-lobe/tapered-lobe relationship obvious at 18x18?
3. Does the lower notch survive without turning into a deep bean indentation?
4. Does the black-and-white asset preserve the same identity as the color asset?
5. Is the gallbladder confirming the image rather than rescuing it?
6. Can a vendor omit the gallbladder, change the color, and simplify the shading without destroying identity?

Reject a candidate immediately if it needs the label "Liver" to beat Beans or Cut of Meat, if the 18px form is
just a red oval, or if the color and black-and-white versions appear to be different symbols.

## Production workflow

1. Generate a concept sheet containing Candidates A, B, and C on white, with no text inside the artwork.
2. Select the strongest silhouette before evaluating rendering polish.
3. Redraw the chosen direction as simple project-owned vector geometry with as few paths as practical.
4. Produce the 72px color and true black-and-white masters.
5. Draw separate 18px masters using the selected geometry as a guide.
6. Build the actual-size selection board and compare against the current art and encoded confusers.
7. Obtain Shuhan's explicit `APPROVE` or `REVISE` decision on the exact four assets.
8. If approved, create the next immutable Liver submission package, update the proposal's visual description,
   rebuild the PDF, and inspect every page.

Do not replace the current `.10` assets during concept exploration. Artwork promotion happens only after an
exact-asset decision.

## Image-generation prompt for concept exploration

> Create a clean emoji concept sheet for a human liver on a pure white background. Explore three distinct
> silhouette-first directions: A) an anterior asymmetric wedge with one dominant domed lobe, one smaller tapered
> lobe, a shallow lower notch, a short curved lobe division, and a small gallbladder nested into the notch; B) the
> same strong anterior silhouette with no gallbladder; C) a restrained anterior-inferior three-quarter view with
> the gallbladder seated under the dominant lobe. Use deep warm burgundy, a dark rounded outline, one restrained
> highlight, and minimal shading. The organ must read at emoji size from its outer contour. Avoid a flat oval,
> kidney-bean curve, steak or meat-cut appearance, leaf shape, mushroom cap, dangling gallbladder, full diagonal
> seam, vessels, ducts, labels, arrows, medical crosses, frames, text, faces, limbs, photorealism, gore, wet tissue,
> glassy plastic, shadows, watermarks, and imitation of any vendor emoji. Show each direction large and as a tiny
> 18-pixel-style preview, first in color and then as a matching strict black-and-white companion.

This prompt creates exploration material, not final submission files. The selected concept must still be redrawn
and verified at exact size.

## Deliverables for the next artwork package

- Three concept directions in color.
- Three matching black-and-white concept directions.
- Selected project-owned vector source.
- Purpose-built 18x18 color PNG.
- Purpose-built 18x18 true black-and-white PNG.
- 72x72 color PNG.
- 72x72 true black-and-white PNG.
- Actual-size selection board.
- Updated image-approval record with exact file hashes after Shuhan's decision.
- New immutable Liver SemVer package only after approval.

## Final recommendation

Proceed with Candidate A first and Candidate B as the control. The largest expected gain comes from changing the
outer contour and nesting the gallbladder, not from adding anatomical detail or rendering polish. If Candidate A
does not beat the current art in solid-silhouette and black-and-white comparisons at 18x18, do not promote it.
