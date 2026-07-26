# Kidney v2.1.1 Image Assessment

Status: **deterministic format gates passed; ready for packet review; no standalone participant study required**
Framework: [Proposal Image Rubric v1.1.1](../proposal-image-rubric.v1.md)

## Recorded checks

The deterministic result is [`kidney-v2.1.1-image-analysis.json`](kidney-v2.1.1-image-analysis.json).

- All four files match their named 18x18 or 72x72 dimensions.
- Both B&W files use a strict black-and-white opaque palette; no opaque gray values are present.
- The 18px alpha bounding box is `[1, 1, 15, 17]`, leaving at least one transparent pixel at every canvas edge.
- The 72px alpha bounding boxes are at least seven pixels from every canvas edge, exceeding the four-pixel target.
- B&W visible-canvas fraction on white is 0.4537 at 18px and 0.3752 at 72px, passing the package thresholds of 0.40 and 0.35.
- Color/B&W alpha-mask overlap is 1.0000 at 18px and 0.9880 at 72px, passing the 0.93 silhouette-alignment threshold.

## Visual evidence used in the packet

Primary cue: vertically oriented renal bean contour with a medial hilum indentation.
Secondary cues: an attached descending ureter; organ-style red-brown color in the color version only.

Likely confusables shown on the native-size review board: Beans and a generic paired organ. The public proposal does not claim that these checks prove universal recognition. It presents the required four examples and the board for Unicode visual review.

## Scope of the score

No participant recognition or confusability study was run, and no study result is claimed. The generic rubric leaves its optional participant-test dimensions unscored in that circumstance. That is an internal evidence limitation, not a Unicode eligibility condition or filing hold.

## Decision

Retain v2.1.1 as the submission candidate. Before filing, verify the exported public PDF keeps the four native-size examples and visual-review board readable, and complete the packet's signer, public-hosting, and form controls.
