# Kidney Emoji Submission Packet Manifest

Packet version: `v2.7.0`

Date prepared: 2026-07-28

Proposal identifier: `kidney-emoji-2026`

Status: `NOT FILED - REVIEW REQUIRED`

## What changed from v2.6.0

MINOR bump: made the review PDF materially more space-efficient while preserving the complete proposal argument,
required fields, paired artwork, exact submitter roster, links, and all five frequency exhibits.

- Removed repository-only forced page breaks; the Unicode 2026 proposal format does not require one evidence
  exhibit per page.
- Cropped only the unused lower portions of the retained Search and Video screenshots. The exact query, search
  type, Tools menu, visible result count, and result context remain visible.
- Used the lower portion of the Expected usage page for Search, grouped Video with Trends Web Search, and grouped
  Trends Image Search with Books Ngram.
- Reduced the rendered packet from nine pages to seven without deleting proposal content or evidence.
- Preserved `v2.6.0` unchanged as a historical review packet.

## Current submitter order

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Danielle Miller;
Timur Erk; Lauren Beaudin; Heena Purohit (Microsoft for Startups); David Rhew, MD (Chief Medical
Officer, Microsoft).

## Files

| File | Role | Description |
| --- | --- | --- |
| `v2.7.0_kidney_emoji_proposal_SUBMIT.md` | `SUBMIT` | Proposal source aligned to the live 2026 format. |
| `v2.7.0_kidney_emoji_proposal_SUBMIT.pdf` | `SUBMIT` | Seven-page rendered proposal for review; not filed or emailed. |
| `images/v2.7.0_*_SUBMIT.png` | `SUBMIT` | Four required paired-kidney example images at 18x18 and 72x72. |
| `images/v2.7.0_*_SOURCE.svg` | `REFERENCE_ONLY` | Reproducible vector sources for the paired artwork. |
| `images/v2.7.0_*_MASTER.png` | `REFERENCE_ONLY` | Master raster sources retained for provenance. |
| `evidence/frequency/v2.7.0_*_SUBMIT.png` | `SUBMIT` | Five required frequency exhibits embedded in the proposal. |
| `validation/computer-validation.md` | `REFERENCE_ONLY` | Human-readable July 26 validation carried forward for byte-identical artwork. |
| `validation/computer-validation.json` | `REFERENCE_ONLY` | Machine-readable July 26 validation carried forward for byte-identical artwork. |
| `validation/proposal-validation.md` | `REFERENCE_ONLY` | Human-readable v2.7.0 proposal and PDF validation. |
| `validation/proposal-validation.json` | `REFERENCE_ONLY` | Machine-readable v2.7.0 proposal and PDF validation. |
| `v2.7.0_regression_audit_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Records the layout-only changes and preserved submission content. |

## Review gates before filing

1. Review the exact PDF and host that immutable file at a public logged-out HTTPS URL.
2. Change Compatibility only if every gate in
   `docs/specs/2026-07-28-kidney-compatibility-evidence-spec.md` is met; otherwise retain `Not applicable`.
3. Complete the Unicode form and agreement. Submission remains Shuhan He's action.

The 2026-07-28 private-Firefox refresh was not accepted into the packet: Search/Video did not expose the
required visible result count, and Trends returned HTTP 429 after the CAPTCHA handoff. The valid May/July
exhibits were retained; no blocked, count-free, or rate-limit screenshot is used.

No email or Unicode submission is part of this packet update.
