# Kidney v2.0.0 Image Assessment

Status: **revise before relying on the image argument**  
Framework: [Proposal Image Rubric v1.1.0](../proposal-image-rubric.v1.md)

## Recorded checks

The deterministic result is [`kidney-v2.0.0-image-analysis.json`](kidney-v2.0.0-image-analysis.json).

- All four supplied image files match their required 18x18 or 72x72 dimensions.
- Color and black-and-white alpha masks are closely aligned: 0.9897 IoU at 18px and 0.9705 at 72px.
- Both black-and-white PNGs contain opaque neutral-gray values, failing the framework's conservative strict black-and-white palette check. Regenerate them with pure black/white opaque pixels before submission.
- At 18px the artwork's alpha bounding box reaches the left and bottom canvas edges. This is an operational presentation risk, not a Unicode dimension failure.
- The black-and-white 18px sample is visibly distinct from only 24.38% of a white canvas under the recorded contrast threshold, versus 59.26% for color. This is a comparability warning, not a recognition result.

## Candidate-specific test setup

Primary cue: renal bean-shaped contour with a medial hilum indentation.  
Secondary cues: attached descending ureter; organ-style red-brown color (color only).

Forced-choice alternatives: Beans, stomach, ear, balloon, drop, other.

The human recognition and confusability tests have **not** been run. Therefore Kidney v2.0.0 has no valid score for the rubric's 30-point 18px recognition, 20-point confusability, or 15-point 72px recognition dimensions.

## Revision direction

Use a native-size binary black-and-white design: a high-contrast kidney silhouette with a clear medial indentation and attached ureter. Preserve those cues in color, add a small safe margin, then run the generic blinded protocol before revising the submission package.
