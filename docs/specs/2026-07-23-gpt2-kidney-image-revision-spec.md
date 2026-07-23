# GPT2 Implementation Spec: Kidney Proposal Image Revision

Status: ready for implementation  
Target submission package: `v2.1.0`  
Supersedes for this revision: the Kidney-specific rendering instructions in `docs/design/kidney-emoji-2026-06/kidney-emoji-design-spec.md` where they permit gloss, gradients, gray B&W shading, or edge-touching 18px art.

## 1. Objective

Create a replacement four-image Kidney proposal set that satisfies Unicode's image requirements and the repository's Proposal Image Rubric v1.1.0. The new artwork must make a single kidney recognizable at native 18x18 size without relying on its red-brown color or fine interior detail.

This is a **proposal paradigm**, not final vendor artwork. Do not imitate Apple, Google, or any other vendor style.

## 2. Source material and authority

Read before editing:

1. `docs/research/emoji-image-evidence/proposal-image-rubric.v1.md`
2. `docs/research/emoji-image-evidence/case-studies/kidney-v2.0.0-assessment.md`
3. `docs/design/kidney-emoji-2026-06/final/` (editable vector/source assets)
4. `submissions/v2.0.0/` (current filing packet; preserve unchanged)

The controlling external requirement is Unicode's proposal guidance: https://www.unicode.org/emoji/proposals.html

## 3. Non-negotiable visual contract

### Invariant cues

Every output must communicate these, in priority order:

1. **Renal silhouette:** one vertically oriented, asymmetric bean-shaped organ.
2. **Medial hilum:** a plainly visible inward concavity on the viewer's right side.
3. **Descending ureter:** one short, attached tube leaving the hilum and moving down-right.

The kidney should never read as a smooth generic bean, ear, balloon, stomach, or drop. Do not add a second kidney, a central vascular column, labels, text, or a medical symbol.

### Composition

- Produce native 72x72 vector/raster artwork and a separately hand-tuned 18x18 raster. Never generate the 18px file by a blind resize of the 72px file.
- At 18x18, retain at least one fully transparent pixel between the alpha bounding box and **every** canvas edge.
- At 72x72, retain at least four fully transparent pixels between the alpha bounding box and every canvas edge.
- Keep the ureter attached to the hilum; it cannot look like a detached ring, pin, or decorative stroke.
- Reduce all nonessential gloss and shading. At 18px, use a flat body fill, a dark outline, and no more than one secondary color region.

### Color version

- Use a restrained organ palette: burgundy/maroon body, darker keyline, and a small tan ureter.
- The hilum and ureter must remain visible when viewed at 100% size.
- At 72px, one subtle darker body region is allowed; no photorealistic texture, high-gloss spot, or multi-stop gradient is required for recognition.
- At 18px, avoid any highlight that competes with the hilum or ureter.

### Black-and-white version

- Use only pure black (`#000000`) and pure white (`#FFFFFF`) for fully opaque pixels. Intermediate edge tones, if any, must be represented by transparency rather than opaque gray pixels.
- Do not use gray fill, shadow, hatching, gradients, or texture.
- Generate and compare two native 18px B&W candidates internally:
  - **Variant A:** black-filled kidney silhouette with a clearly cut medial notch and a black ureter.
  - **Variant B:** white-filled kidney with a heavy black outline, visible medial notch, and black ureter.
- Select the variant that is more visibly distinct on a white background and preserves the three invariant cues. Retain the nonselected variant only as `REFERENCE_ONLY`; do not include it in the filing packet.

## 4. Required deliverables

Create a new semver package at `submissions/v2.1.0/`; do not edit the frozen v2.0.0 assets.

Required final images:

```text
submissions/v2.1.0/images/v2.1.0_kidney_color_18x18_SUBMIT.png
submissions/v2.1.0/images/v2.1.0_kidney_color_72x72_SUBMIT.png
submissions/v2.1.0/images/v2.1.0_kidney_bw_18x18_SUBMIT.png
submissions/v2.1.0/images/v2.1.0_kidney_bw_72x72_SUBMIT.png
```

Also provide:

- Editable color and B&W source vectors in `docs/design/kidney-emoji-2026-06/final/` or a versioned `v2.1.0/` subfolder there.
- A regenerated visual-review board in the v2.1.0 evidence directory that shows all four files at actual 18px and 72px sizes on white and near-black backgrounds.
- A case-study analysis saved as `docs/research/emoji-image-evidence/case-studies/kidney-v2.1.0-image-analysis.json`.
- A short case-study assessment that records the cue inventory, forced-choice alternatives, all measured results, and whether human testing has been run.
- Updated v2.1.0 proposal source/PDF references and the root README current-packet link, only after all checks pass.

## 5. Automated acceptance gates

Run the generic inspector against the new assets:

```powershell
python docs/research/emoji-image-evidence/analyze_proposal_image_set.py `
  --input-dir submissions/v2.1.0/images `
  --output docs/research/emoji-image-evidence/case-studies/kidney-v2.1.0-image-analysis.json `
  --asset-set "Kidney proposal v2.1.0" `
  --color-18 v2.1.0_kidney_color_18x18_SUBMIT.png `
  --color-72 v2.1.0_kidney_color_72x72_SUBMIT.png `
  --bw-18 v2.1.0_kidney_bw_18x18_SUBMIT.png `
  --bw-72 v2.1.0_kidney_bw_72x72_SUBMIT.png
```

The v2.1.0 package may be marked `SUBMIT` only when all of the following are true:

| Check | Required result |
| --- | --- |
| Dimensions | All four files are exactly 18x18 or 72x72 as named. |
| B&W palette | `black_and_white_samples_have_strict_binary_opaque_palette: true`. |
| B&W visibility on white | At least 0.40 visible canvas fraction at 18px and at least 0.35 at 72px under the analyzer's recorded threshold. |
| Silhouette alignment | Color/B&W alpha-mask IoU is at least 0.93 at both sizes. |
| Edge safety | Alpha bounding box has the margin specified in Section 3. |
| File integrity | PNG/RGBA, transparent outside the artwork, no text or logo. |
| Submission packet | All image names, visual-review board, proposal source, proposal PDF, manifests, and checks are versioned `v2.1.0`. |

If any gate fails, retain the package as `REFERENCE_ONLY` and record the exact failure. Do not rationalize a failure as acceptable because a historical proposal used a different format.

## 6. Human-recognition evidence required after rendering

Automated checks are necessary but not sufficient. Use the rubric's blinded protocol before asserting that the artwork is recognizable:

- At least 30 independent adults, with no proposal title or description shown.
- Three-second unprompted recognition trials for color/B&W at 18px and 72px.
- Forced-choice alternatives: Kidney, Beans, stomach, ear, balloon, drop, other.
- Record the selected answer and the cue reported by each correct respondent.

The target is at least 80% correct unprompted recognition for color 18px, 70% for B&W 18px, 90% at 72px, and at least 75% forced-choice selection of Kidney in each 18px mode. No wrong alternative may exceed 15%.

Do not invent, simulate, or imply participant results. Until the test is run, the proposal may state only that the assets passed deterministic format checks.

## 7. Revision logic after a test

| Main error | Required next adjustment |
| --- | --- |
| Beans | Deepen the medial concavity and make the ureter emerge clearly from it. Do not add more shading. |
| Ear or balloon | Break the smooth outer rim and strengthen the kidney's asymmetric top/bottom shape. |
| Stomach | Make the lower-right ureter direction and mid-right hilum more distinct. |
| B&W fails but color passes | Strengthen black silhouette and negative-space hilum before adding interior lines. |
| Several alternatives | Remove details until the 18px artwork has one primary silhouette and one high-contrast differentiator. |

## 8. Rights and provenance

Use only the Medical Emoji project's original vector work. Conductscience Foundation owns the reference artwork and has granted the submitter the rights required to use it in the Unicode proposal. Do not incorporate artwork, screenshots, or vendor assets from previous Unicode submissions.

## 9. Handoff checklist for GPT2

1. Copy `v2.0.0` to `v2.1.0`, preserving the older version unchanged.
2. Produce B&W A/B internal candidates, evaluate them on white and near-black backgrounds, and select one.
3. Create native 18px and 72px color/B&W final files with the exact names above.
4. Run the generic analyzer and satisfy every automated gate.
5. Update the v2.1.0 packet, manifests, review board, source vectors, and semver metadata.
6. Record unrun human testing honestly; do not assign recognition points without data.
7. Commit and push the new package with a project semver patch bump.
