# Kidney v2.1.0 Image Assessment

Status: **deterministic format gates passed; human recognition evidence pending**  
Framework: [Proposal Image Rubric v1.1.0](../proposal-image-rubric.v1.md)

## Recorded checks

The deterministic result is [`kidney-v2.1.0-image-analysis.json`](kidney-v2.1.0-image-analysis.json).

- All four files match their named 18x18 or 72x72 dimensions.
- Both B&W files use a strict black-and-white opaque palette; no opaque gray values are present.
- The 18px alpha bounding box is `[1, 1, 15, 17]`, leaving at least one transparent pixel at every canvas edge.
- The 72px alpha bounding boxes are at least seven pixels from every canvas edge, exceeding the four-pixel target.
- B&W visible-canvas fraction on white is 0.4537 at 18px and 0.3752 at 72px, passing the v2.1.0 thresholds of 0.40 and 0.35.
- Color/B&W alpha-mask overlap is 1.0000 at 18px and 0.9880 at 72px, passing the 0.93 silhouette-alignment threshold.

## Candidate-specific test setup

Primary cue: vertically oriented renal bean contour with a medial hilum indentation.  
Secondary cues: an attached descending ureter; organ-style red-brown color in the color version only.

Forced-choice alternatives: Beans, stomach, ear, balloon, drop, other.

## What remains unscored

The human recognition and confusability tests have **not** been run. Kidney v2.1.0 therefore has no valid score for the rubric's 30-point 18px recognition, 20-point confusability, or 15-point 72px recognition dimensions. The deterministic result supports a controlled test; it does not prove that people recognize a kidney without foreknowledge.

## Decision

Use v2.1.0 as the test candidate. Do not describe it as “recognizable” in external material until the 30-participant blinded protocol in the rubric has produced recorded results.
