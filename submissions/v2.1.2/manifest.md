# Kidney Emoji Submission Packet Manifest

Packet version: `v2.1.2`

Date prepared: 2026-07-27

Proposal identifier: `kidney-emoji-2026`

Status: `NOT FILED`. Artwork and case are consolidated; eligibility and publication remain open.

## What changed from v2.1.1

This packet consolidates the two parallel Kidney lines. It keeps v2.1.1's single-kidney paradigm and
adopts the case discipline from the `v1.12.0-kidney` line.

### Artwork

- Rebuilt all four example images. The v2.1.1 black-and-white assets carried the medial hilum only
  as a 2px white stroke, which did not survive rasterization, so the kidney read as a featureless
  blob. The hilum is now real path geometry.
- The gap separating the ureter from the body was previously painted opaque white. That would halo
  on dark backgrounds and was counted as part of the silhouette. It is now transparency.
- Geometry is size-specific. At 18x18 the ureter is a short thick stub, because a long thin tube
  fragments into loose pixels, and its color is darkened because the 72px tan washes out.
- Deterministic validation now runs against the packet and passes on all four assets.

### Case

- `A. Multiple meanings` claims the established non-medical `kidney-shaped` sense, evidenced by
  retail and design catalogues and a Books comparison against `kidney stone`. v2.1.1 had no such
  claim under its `Multiple Concepts` heading.
- `C. Open-ended` now names the neighbours this proposal declines to argue for: Liver, Stomach,
  Pancreas, and Spleen. It also concedes that `stomach` and `liver` exceed `kidney` in recent
  English Books data. v2.1.1 named none of them.
- Removed the WHO, Lancet, and CDC disease-burden figures and the public-health and coalition
  sections. Repository proposal rules state that advocacy and awareness language appears far more
  often in declined proposals and that petition-style support is disallowed evidence.
- Restored Unicode's own factor names: `A. Multiple meanings` and `E. Faulty comparison`.
- Prose reduced from 1,711 words to under 1,000, against a 1,200 ceiling.
- Added an 18x18 comparator board showing the proposed image beside Beans, Lungs, Anatomical heart,
  and Droplet, supporting `D. Distinctiveness` with a visual rather than an assertion.

## Files

| File | Role | Description |
| --- | --- | --- |
| `v2.1.2_kidney_emoji_proposal_SUBMIT.md` | `SUBMIT` | PDF-facing proposal source. |
| `v2.1.2_kidney_emoji_proposal_SUBMIT.pdf` | `SUBMIT` | Rendered PDF. Not yet hosted at a public URL. |
| `images/` | `SUBMIT` | Four required example images plus their vector sources. |
| `evidence/frequency/` | `SUBMIT` | Five required frequency exhibits, captured 2026-05-13. |
| `evidence/visual-review/` | `SUBMIT` | 18x18 comparator board. |
| `validation/` | `REFERENCE_ONLY` | Deterministic artwork validation output. |
| `v2.1.2_support_letters_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | The 13 institutional support letters, retained but kept out of the proposal. |

## Open before filing

1. **Eligibility.** Kidney was declined 2019-12-17 and 2022-07-19, with a notice dated 2022-11-04.
   The four-year re-review bar may or may not have cleared before the 2026-07-31 deadline depending
   on which date governs. Inquiry drafted at `docs/proposals/2026-eligibility-inquiry.md`. Send
   before filing.
2. **Artwork rights.** The two source lines state different owners. v2.1.1 attributes ownership to
   ConductScience Foundation; the `v1.12.0-kidney` line has the submitter warranting personal
   ownership and releasing CC0. This packet states only that the artwork is original and free of
   third-party material. Reconcile and state one position before filing.
3. **Image count.** Repository rules note that encoded proposals tend to carry more than twenty
   images; this packet has ten. Additional evidence captures would strengthen it.
4. **Publication.** Host the exact PDF at a logged-out HTTPS URL and verify anonymously before the
   URL goes on the form.
5. **Do not file Kidney, Liver, and Stomach together.** Each must stand alone.
