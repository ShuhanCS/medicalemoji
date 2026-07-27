# Liver Emoji GPT Image 2 Concept Generation Record

Version: 1.0.0

Date: 2026-07-26

Model: `gpt-image-2`

Purpose: execute the concept-exploration stage of the Liver artwork redesign specification without changing
the immutable `v1.12.0-liver.10` submission assets.

## Outputs

### Initial board - superseded

- Artifact version: `1.0.0`
- File: `v1.0.0/liver-concept-board-gpt-image-2-v1.0.0.png`
- Size: 2048x1152 PNG
- Quality: high
- SHA-256: `8F94030915F4CE8ACF60BA45EB9AE5424940299B399A4E934AB16D77449BF68C`
- Decision: retain as the initial exploration, but do not advance. The lobe divisions were too long and
  recreated the cut-or-seam problem identified in the current submission art.

### Corrected board - current review artifact

- Artifact version: `1.0.1`
- File: `v1.0.1/liver-concept-board-gpt-image-2-v1.0.1.png`
- Size: 2048x1152 PNG
- Quality: high
- SHA-256: `C9C784E961125A58930C3C2E5D41FCF06D2D55C13C417ECF0A4EFFE048FA92E8`
- Decision: use for direction selection. Candidate A is the lead, Candidate B is the silhouette control, and
  Candidate C remains exploratory.

## Visual review of version 1.0.1

### Candidate A - lead

The asymmetric wedge, domed dominant lobe, tapered smaller lobe, and shallow lower notch create the strongest
silhouette. The gallbladder is seated in the lower contour and acts as a secondary confirming cue. The revised
short lobe division no longer cuts the organ in half.

### Candidate B - control

The gallbladder-free form remains readable and demonstrates that the outer contour can carry the identity. It
is the required control for deciding whether Candidate A's green cue is confirming the Liver rather than
rescuing an otherwise generic shape.

### Candidate C - exploratory, not preferred

The corrected render removed the distracting doubled underside, but GPT Image 2 also reduced much of the
intended three-quarter-view distinction. It does not currently justify its added viewpoint risk over Candidate
A. Do not advance it unless a later redraw produces a materially clearer actual-size result.

## Important limitation

The bottom-row images are visual approximations of tiny icons, not exact purpose-built 18x18 assets. The
selected direction still requires a controlled project-owned vector redraw followed by separately drawn 72x72
and 18x18 color and true black-and-white masters. Nothing in this concept board is submission-ready artwork.
The black-and-white concept row is also a visual direction only; it has not been reduced or validated as a
two-color bilevel submission asset.

## Initial generation prompt

```text
Use case: logo-brand
Asset type: Unicode Liver emoji candidate selection board for visual design review
Primary request: Create one clean landscape concept sheet comparing three distinct silhouette-first human liver emoji directions. This is an icon design exploration, not a medical illustration.
Scene/backdrop: Pure white flat background, no shadow, no texture, no frame around the whole sheet.
Layout: Three evenly spaced columns labeled only A, B, and C. In each column show: one large color icon, one matching strict pure-black-and-white line icon, and one very small simplified 18-pixel-style color preview. Keep every icon isolated with generous whitespace and consistent scale.
Direction A: anterior asymmetric wedge, one dominant broad domed lobe and one clearly smaller tapered lobe, shallow lower notch, short gently curved lobe division ending inside the organ, and a compact muted olive-green gallbladder nested into the lower notch with at least half its height visually seated within the liver contour; never dangling.
Direction B: same strong anterior asymmetric wedge and lobe hierarchy, a slightly clearer shallow lower notch, no gallbladder, one restrained short curved division. It must succeed by silhouette alone.
Direction C: restrained slight anterior-inferior three-quarter view, still one continuous asymmetric wedge, a small portion of underside visible, compact gallbladder visibly seated under the dominant lobe, no vessels or ducts.
Style/medium: polished modern emoji concept art with simple vector-like geometry, dark rounded burgundy outline, deep warm burgundy body, one darker lower plane, one restrained warm highlight, minimal shading, crisp scalable edges. Friendly and familiar but not cute, no face.
Black-and-white companions: pure black and pure white only, white-filled organ, continuous black outer contour, one short black curved division, preserved lower notch as negative space, no gray, no color, no shaded fill.
Tiny previews: purpose-built simplifications, not mechanical miniatures; retain the domed dominant lobe, tapered smaller lobe, and lower notch; remove detail that becomes noise.
Design objective: At tiny size, every candidate must read as a liver-like asymmetric organ rather than a bean, steak, fruit, leaf, mushroom cap, or generic oval. The outer contour must carry identity; the gallbladder may only confirm it.
Constraints: one continuous organ mass; dominant lobe roughly two thirds of the visible mass; overall width-to-height about 1.6:1; upper contour is one long convex dome without a central dip; smaller lobe ends in a clear taper; surface division is curved, subordinate, and never crosses the full organ.
Avoid: flattened oval, deep kidney-bean C indentation, paired bean shapes, seed-like highlight, dangling gallbladder, thin gallbladder stem, straight diagonal seam, full-height seam, vessels, ducts, labels other than A B C, arrows, medical crosses, badges, frames, gore, wet tissue, photorealism, glassy plastic, cast shadows, text blocks, measurements, watermarks, vendor emoji imitation.
Output intent: A disciplined professional concept board from which a project-owned vector design can be redrawn. Prioritize silhouette differentiation and honest small-size behavior over rendering polish.
```

## Corrective edit prompt

Input image: version `1.0.0`, used as the edit target.

```text
Use case: precise-object-edit
Asset type: Unicode Liver emoji candidate selection board revision
Primary request: Preserve this exact A/B/C comparison-board layout, white background, lettering, icon positions, relative scale, palette, rounded vector-like rendering, and the established outer silhouettes. Make only the following anatomy-to-icon simplifications in every large, black-and-white, and tiny counterpart.
A: Replace the long lobe seam with one short gently curved subordinate lobe-division mark, no longer than about 40 percent of the organ height. It may begin at the upper contour but must end clearly inside the liver well above the lower contour. Keep the compact olive gallbladder nested in the lower notch with no stem and no dangling appearance.
B: Replace the long lobe seam with the same kind of short gently curved subordinate division, ending clearly inside the liver. Keep B entirely without a gallbladder. Preserve its clean silhouette-first lower notch.
C: Keep the slight anterior-inferior three-quarter viewpoint and seated gallbladder, but simplify the underside to one restrained darker lower plane. Remove the doubled ribbon-like lower rim and any extra contour that makes it look folded, layered, or cut open. Use one short curved lobe-division mark ending inside the organ.
Black-and-white row: preserve pure black lines on pure white only, with no gray or shading. Mirror the revised simplified geometry exactly.
Tiny previews: mirror the revised silhouettes, use the shortest possible division cue, and keep them clean rather than mechanically detailed.
Invariants: change only these division-line lengths and C underside simplification; keep all other composition, colors, shapes, labels, whitespace, and style unchanged. No new text, vessels, ducts, gore, shadows, background elements, badges, or vendor imitation.
```

## Decision required before production art

Shuhan should review the exact version `1.0.1` board and choose `A`, `B`, `C`, or `REVISE`. An `A` decision
authorizes a controlled vector redraw of Candidate A, not direct promotion of the generated bitmap.
