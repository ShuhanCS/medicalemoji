# Kidney Emoji Submission Packet Manifest

Packet version: `v2.10.0`

Date prepared: 2026-07-28

Proposal identifier: `kidney-emoji-2026`

Status: `NOT FILED - REVIEW REQUIRED`

## What changed from v2.9.0

MINOR packet bump: replaced the malformed downsampled 18x18 examples with purpose-built native-grid artwork
while preserving the 72x72 paired artwork, exact submitter roster, selection-factor answers, links, and all
frequency evidence.

- Drew the color and black-and-white 18x18 examples directly on the native 18-pixel grid instead of reducing a
  larger raster.
- Enlarged the paired kidney bodies within the grid and retained visible medial notches, a central connector,
  and two short ureter cues.
- Added reproducible native SVG sources with an 18x18 viewBox and crisp pixel rendering.
- Preserved `v2.9.0` unchanged as a historical review packet.

## Current submitter order

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Danielle Miller;
Timur Erk; Lauren Beaudin; Heena Purohit (Microsoft for Startups); David Rhew, MD (Chief Medical
Officer, Microsoft).

## Files

| File | Role | Description |
| --- | --- | --- |
| `v2.10.0_kidney_emoji_proposal_SUBMIT.md` | `SUBMIT` | Proposal source aligned to the live 2026 format. |
| `v2.10.0_kidney_emoji_proposal_SUBMIT.pdf` | `SUBMIT` | Rendered proposal for review; not filed or emailed. |
| `images/v2.10.0_*_SUBMIT.png` | `SUBMIT` | Four required paired-kidney example images at 18x18 and 72x72. |
| `images/v2.10.0_*_SOURCE.svg` | `REFERENCE_ONLY` | Reproducible vector and native-pixel sources for the paired artwork. |
| `images/v2.10.0_*_MASTER.png` | `REFERENCE_ONLY` | Master raster sources retained for provenance. |
| `evidence/frequency/v2.10.0_*_SUBMIT.png` | `SUBMIT` | Seven screenshots covering all five required Kidney-to-Elephant comparison methods. |
| `validation/computer-validation.md` | `REFERENCE_ONLY` | Human-readable technical validation of the v2.10.0 artwork. |
| `validation/computer-validation.json` | `REFERENCE_ONLY` | Machine-readable technical validation of the v2.10.0 artwork. |
| `validation/proposal-validation.md` | `REFERENCE_ONLY` | Human-readable v2.10.0 proposal and PDF validation. |
| `validation/proposal-validation.json` | `REFERENCE_ONLY` | Machine-readable v2.10.0 proposal and PDF validation. |
| `v2.10.0_regression_audit_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Records the artwork correction and preserved submission content. |

## Review gates before filing

1. Review the exact PDF and verify that its public logged-out HTTPS copy is byte-identical.
2. Change Compatibility only if every gate in
   `docs/specs/2026-07-28-kidney-compatibility-evidence-spec.md` is met; otherwise retain `Not applicable`.
3. Complete the Unicode form and agreement. Submission remains Shuhan He's action.

All four Search and Video captures were accepted only after Firefox's Tools menu exposed the visible
approximate result count. No blocked, CAPTCHA, count-free, or rate-limit screenshot is used.

No email or Unicode submission is part of this packet update.
