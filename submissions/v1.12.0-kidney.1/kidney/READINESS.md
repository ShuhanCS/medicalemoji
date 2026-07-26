# Kidney Proposal Readiness Review

Review date: 2026-07-26

Package: 1.12.0-kidney.1

Status: **REVISION REQUIRED**

Provisional internal score: **93/100**. This is a project control, not a Unicode score or approval prediction.

## Authorship decision

The proposal preserves the ten consenting individual submitters in this order:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk; David Rhew; Heena Purohit.

Shuhan He remains the main point of contact. No additional internal consent artifact or external human
validation is required for this prerelease.

## Artwork decision

Shuhan He approved the GPT Image 2 paired-kidney concept on 2026-07-26. The generated raster is retained as a
design reference; the proposal assets are a deterministic project-authored SVG redraw with separate 18-pixel
masters and exact-size PNG exports.

The redraw restores two inward-facing kidney forms, offsets the right kidney downward, removes the full
vascular tower, shortens the plumbing cues, and uses outlined rather than solid black-and-white artwork.

## Must-pass gates

| Gate | Result | Finding |
| --- | --- | --- |
| Eligibility | Pass | The current slate records Kidney as eligible for the 2026 intake. |
| Authorship | Pass | Consent is confirmed for the ten names preserved in this prerelease. |
| Main contact | Pass | Shuhan He is identified as the main point of contact. |
| Rights | Pass | Page 1 contains Shuhan He's direct ownership warranty and CC0 release; the generated concept is reference-only and the submission assets are project-authored SVGs. |
| Required art | Pass | Color and true black-and-white assets are present at exact 18x18 and 72x72 dimensions. |
| Artwork direction | Pass | Shuhan He approved the paired-kidney direction. |
| Technical image checks | Pass | Dimensions, strict black-and-white palette, and foreground connectedness pass. |
| Geometric comparator | Open | Color 18x18 IoU with Lungs is 0.750 against the prerelease ceiling of 0.72; dHash distance passes at 23. |
| Semantic computer validation | Open | Add a reproducible kidney-vs-confusion label test; geometric distance alone cannot establish the depicted concept. |
| Frequency evidence | Pass | All five required screenshots are present, reproducible, legible, and use `elephant` where required. |
| Citations | Pass | Material meaning and medical claims cite dictionary, NIH/NIDDK, MedlinePlus, or Unicode sources. |
| PDF layout | Pass | The rebuilt ten-page Letter PDF has embedded fonts, intact links, deliberate evidence pages, and no clipping, overlap, or stranded headings. |
| Public PDF | Open | Publish only after the computer and rendered-PDF gates pass. |
| Official form | Open | Reconcile the form with the eventual canonical PDF and archive filing confirmation. |

## Computer-validation decision

The corrected foreground segmentation now excludes transparent and border-connected white canvas pixels. It
therefore measures the artwork rather than the full opaque image square. The four required assets pass
dimension, palette, and connectedness tests. Eleven of twelve geometric comparisons pass; the only open row is
the color 18x18 silhouette against Lungs.

This prerelease does not lower or silently alter the predeclared IoU threshold. The open geometric result is
recorded alongside the passing hash distance while a semantic computer test is designed. No human-recognition
panel is required.

## Changes in 1.12.0-kidney.1

- Stores the approved GPT Image 2 paired-kidney concept in the project design record.
- Rebuilds the concept as deterministic color and black-and-white SVG/PNG assets at 18x18 and 72x72.
- Restores paired-organ recognition while removing the old full vascular tower and thin anatomy.
- Corrects the alpha-only foreground-mask bug in the Kidney validator.
- Updates the proposal and design specification to the paired paradigm.

No frequency screenshot, submitter name, main contact, or filing authorization changed in this prerelease.
