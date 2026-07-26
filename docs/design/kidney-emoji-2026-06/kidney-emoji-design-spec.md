# Kidney Emoji — Design Specification

Status: superseded by `../kidney-emoji-2026-07/design-spec.md` · 2026-07-26
Author: Medical Emoji design pass
Supersedes the artwork in `submissions/v0.13.4/images/` (not the proposal text yet — see §10)

---

## 0. TL;DR

The v0.13.4 artwork is an **anatomy diagram**, not an emoji. It puts two organs plus a
full red/blue aorta-and-vena-cava column plus ureters into the frame. At 18×18 px — the
size Unicode actually tests — it fractures into "blob · colored bars · blob" and the four
hues fight each other. Every approved organ emoji does the opposite: **one bold specimen
that fills the frame.**

**Recommendation: a single kidney**, rendered in the established organ-emoji house style —
maroon body, dark keyline, soft upper-left highlight, with a short renal-vessel stub and a
tan ureter stub emerging from the hilum notch. The vessel + ureter + organ color are what
separate it from the existing 🫘 *beans* emoji; we do **not** need two kidneys to do that.

Candidate renders (built to spec) are in `candidates/`. See `candidates/comparison_board.png`.

---

## 1. Why the current art fails Unicode

Unicode's proposal guidance: example images **must** be supplied at **18×18 and 72×72 px**,
in **color and black-and-white** (grayscale is rejected), and must stay **recognizable at
18×18** — "most people should be able to discern... without foreknowledge."

The v0.13.4 color image breaks three of these in one shot:

| Problem | Effect at 18px |
|---|---|
| Two organs side by side | Splits into two small blobs with a gap; no single focal point |
| Full aorta + vena cava column (red + blue, full height) | Two vertical bars read as random colored noise, not anatomy |
| Ureters as thin lines | Vanish entirely below ~30px |
| Four competing hues (kidney brown, arterial red, venous blue, tan) | No dominant color; muddy |

The B&W line-art version collapses into a shape closer to a **heart or a pair of
parentheses** with a smudge in the middle. (Renders of the originals are in the v0.13.4
submission folder; the failure is visible the moment you downscale them.)

This is the single most common way medical/anatomy emoji proposals get rejected: the art
is drawn for a textbook, not for a 1-em glyph.

---

## 2. What approved organ emoji actually do (the house style)

The kidney would sort in **People & Body → body-parts**, right after 🫁 *lungs*. Its
neighbors define the bar: 🫀 anatomical heart, 🫁 lungs, 🧠 brain, 🦷 tooth, 🦴 bone.
Every one of them shares the same construction:

1. **One silhouette filling ~75–85% of the frame.** Even lungs — the only "paired" organ —
   is fused into a *single* unit by a central trachea. There is no version with a gap down
   the middle.
2. **A dark keyline** around the whole shape — a darkened version of the fill color, ~2 px
   at 72px scale. This is what holds the shape together when it shrinks.
3. **Soft directional shading:** lighter highlight upper-left, darker shadow lower-right,
   plus one small glossy specular dot. Gives the "wet specimen" read.
4. **A 2–3 hue palette.** No more.
5. **Chunky, simplified detail.** Where 🫀 has vessels, they are *fat rounded stubs*, never
   thin lines. Anything thinner than ~3 px at 72px disappears at 18px, so it doesn't exist.
6. **A slight tilt** (~10–15°) so it reads as a 3-D object, not a logo.

The kidney spec below is just this checklist applied to a kidney.

---

## 3. Recommended design — SINGLE kidney

### 3.1 Silhouette & orientation
- One kidney, classic bean form: **convex lateral (outer) edge, concave medial (inner)
  edge with the hilum notch** at mid-height.
- Tilt **~12° counter-clockwise** (top leans right). Hilum faces the **viewer's right**.
- Body fills roughly **x:8–62, y:8–64** of the 72-grid (≈6 px breathing room all sides).
- Proportions ~ 1 : 1.35 (width : height). Avoid making it perfectly symmetric top-to-bottom;
  a kidney is slightly fuller at the top pole.

### 3.2 The hilum + vessels (this is the whole differentiation strategy)
From the medial notch, **two chunky stubs** emerge — they are mandatory, not decoration:
- **Renal vessel** — a fat rounded tube angling up-and-right, arterial red. (A single stub
  is enough at emoji size. A designer may split it into artery-red + vein-darker if it still
  reads at 18px; drop the split if it muddies.)
- **Ureter** — a fat rounded tube curving **down-and-right**, in cream/tan. The tan is the
  one **non-red cue** in the whole image; it is what tells a viewer "organ with plumbing,"
  not "kidney bean." Keep it thick enough (≥3 px at 72px) to survive downscaling.

Both stubs use the same keyline treatment as the body. They should read as *emerging from
behind* the notch, not stuck on top.

### 3.3 Palette (sRGB hex)

| Role | Hex | Notes |
|---|---|---|
| Body highlight (upper-left) | `#C75B54` | lightest maroon |
| Body mid | `#A23730` | dominant color |
| Body shadow (lower-right) | `#7D251F` | deepest |
| Keyline | `#5C1813` | whole-shape outline + vessel outlines |
| Renal vessel | `#CF4036` | arterial red, slightly brighter than body |
| Ureter fill | `#E7D4A4` → `#D8BF86` | tan gradient |
| Ureter keyline | `#B59B63` | |
| Specular highlight | `#FFFFFF` @ ~30% | one soft ellipse, upper-left |

Gradient direction on the body: linear, top-left → bottom-right (highlight → shadow).

### 3.4 Black-and-white version
Required by Unicode. Pure line art:
- Body: **white fill**, `#1A1A1A` keyline (~2 px @72).
- Hilum notch indicated by the inner contour; vessel + ureter as **outlined stubs** (white
  fill, same keyline) so the silhouette still reads as organ-with-plumbing.
- Optional: a single light-gray (`#D9D9D9`) shadow shape lower-right for form. No gradients.
- No internal hatching or texture — it will not survive 18px.

### 3.5 18×18 hinting rules (designer must hand-tune, do not just downscale)
- Keep the **outer silhouette + keyline** as the priority; sacrifice internal gloss first.
- The **hilum notch must stay visible** as at least a 1–2 px concavity — it is what stops the
  shape reading as a plain bean.
- Keep **at least one vessel stub** as a 1–2 px nub on the right. If both won't fit, keep the
  **tan ureter** (color contrast) over the red vessel (which blends into the body).
- Snap the keyline to the pixel grid; let the body be a solid maroon mass with a 1 px darker rim.

---

## 4. Documented alternative — PAIRED kidneys (not recommended)

The v0.13.4 proposal text argues for paired kidneys to avoid bean confusion. A redesigned
pair (lungs-style: lobes fused, **one** short shared vessel instead of the full column,
ureters dropped) is included as a candidate. It is rejected for the hero because:

- At 18px it **collapses into a red two-lobe blob that reads as a heart or a peach** — the
  exact confusion the pairing was meant to prevent, just relocated.
- The B&W pair **tangles in the center** (two contours + bridge + hila meeting) into noise.
- It violates the house-style rule (every organ emoji is a single specimen; lungs only
  "pairs" because the lobes physically fuse).

Bean confusion is better solved by **color + vessel cue** (§3.2) than by doubling the count.
The paired render is kept in `candidates/` for the record and for the side-by-side.

---

## 5. Differentiation from 🫘 *beans* (U+1FAD8)

This is the reviewers' likely objection, so the art answers it directly:

| Cue | Kidney | 🫘 Beans |
|---|---|---|
| Color | Maroon/organ-red, glossy | Tan/brown, matte |
| Plumbing | Renal vessel + ureter at hilum | None |
| Hilum notch | Pronounced medial concavity | Smooth |
| Count | One organ | Multiple beans in/near a pod |
| Finish | Wet-specimen gloss + soft shadow | Food, flatter |

State this table in the proposal's Distinctiveness section.

---

## 6. Production pipeline

1. **Vector master** (SVG/AI/Figma) at a 72-unit artboard. The candidate masters in
   `candidates/*.svg` are a starting point — a designer should redraw the body curve by hand
   for a more organic edge and add proper multi-stop shading.
2. **Export 72×72 PNG**, RGBA, transparent background.
3. **Produce 18×18 by hand-hinting** per §3.5 — start from a downscale, then clean up on the
   pixel grid. Do not ship a raw downscale.
4. Repeat for B&W. Four PNGs total: `{color,bw} × {18,72}`.
5. Keep transparent backgrounds; no baked-in white box.

`build_candidates.py` in this folder reproduces the candidate art and the comparison board
(`python build_candidates.py`). It is a concept tool, not the final art path.

---

## 7. Files in this folder

- `kidney-emoji-design-spec.md` — this document
- `build_candidates.py` — generator (SVG → Chrome raster → downscale → board)
- `candidates/comparison_board.png` — **the one-look artifact**: single vs paired, 72 + 18,
  color + B&W, with 8× zoom of the 18px
- `candidates/single_color_{72,18}.png`, `single_bw_{72,18}.png` — **recommended hero**
- `candidates/paired_color_{72,18}.png`, `paired_bw_{72,18}.png` — alternative, for record
- `candidates/*.svg` — editable vector masters

---

## 8. Acceptance criteria (definition of done for final art)

- [ ] Single kidney, organ-styled, per §3.
- [ ] Reads as a kidney/organ — not a bean, heart, or peach — at **18×18 actual size** to a
      viewer with no foreknowledge (test on ≥3 people cold).
- [ ] Hilum notch + at least one vessel stub legible at 18px.
- [ ] Color and B&W, each at 18 and 72, transparent background, hand-hinted at 18.
- [ ] B&W is line art, not grayscale.
- [ ] Distinct from 🫘 beans by the §5 cues.

---

## 9. Open questions for Shuhan

1. **Single vs paired** — spec recommends single; the comparison board is built to let you
   confirm. (Decision already leaning "spec both, render candidates"; this is the render.)
2. **Vessel detail** — one vessel stub, or artery-red + vein? Recommend one for clarity;
   designer tests two at 18px.
3. **Who executes final art** — Alla Shamanska (did the v0.13.4 color art) is the natural
   choice; this spec is written so any emoji designer can run it.

---

## 10. Proposal-text impact (do not skip)

The submitted `v0.13.4_kidney_emoji_proposal_SUBMIT.md` currently states the **paired**
presentation is "the preferred direction." If we adopt the single-kidney hero, the following
must change before the next submission version:

- §2 Images / Essential Visual Cues — change "paired organ presentation: strongly preferred"
  to describe the single-organ-with-hilum-and-vessels paradigm.
- §3.D Distinctiveness — replace the paired-vs-bean argument with the §5 color/vessel table.
- The 18×18 visual review board evidence image — regenerate against the new hero.

Treat the artwork change and the text change as one coupled edit for the next version
(v0.13.5). Until both are done, the submission is internally inconsistent.
