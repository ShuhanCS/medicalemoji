# Stomach Image Approval Record

Version: 2.0.0

Status: Crowd-recognition procedure retired; Shuhan approval required

## Decision

The former twelve-person recognition test is not a submission requirement and must not block the Stomach
proposal. The HTML runner and blank response file remain only as historical development artifacts. Do not
recruit participants, set a sample-size threshold, calculate a recognition percentage, or present this folder
as Unicode-required evidence.

## Required human image gate

Shuhan He personally reviews:

- `../candidate-v1.12/images/stomach_color_18x18_SUBMIT.png`
- `../candidate-v1.12/images/stomach_bw_18x18_SUBMIT.png`
- `../candidate-v1.12/images/stomach_color_72x72_SUBMIT.png`
- `../candidate-v1.12/images/stomach_bw_72x72_SUBMIT.png`
- the matching actual-size color and black-and-white comparison boards in `../validation-v1.12/`

Display the assets at actual size on a neutral background. Shuhan records either `APPROVE` or `REVISE` for the
intended Stomach read and its essential cues. His decision is the complete human approval gate.

## Approval record

Create or update `RESULT.md` with:

- reviewer: Shuhan He;
- decision date;
- `APPROVE` or `REVISE`;
- SHA-256 hashes for the exact four reviewed assets;
- comparison-board version or hashes;
- any requested revision; and
- the Git commit containing the approved assets.

Any material artwork change invalidates the prior approval and requires the exact replacement assets to return
to Shuhan. Computer validation may support the review but cannot replace his decision.
