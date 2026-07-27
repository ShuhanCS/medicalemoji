# Kidney Proposal Readiness Review

Review date: 2026-07-26

Package: 1.10.0

Status: **READY TO PUBLISH**

Provisional internal score: **98/100**. This is a project control, not a Unicode score or approval prediction.

## Authorship decision

The proposal names ten consenting individual submitters in this order:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk; David Rhew; Heena Purohit.

Shuhan He confirmed consent on 2026-07-26 and remains the main point of contact. No additional internal consent
artifact or external human validation is required for this release.

## Must-pass gates

| Gate | Result | Finding |
| --- | --- | --- |
| Eligibility | Pass | The current slate records Kidney as eligible for the 2026 intake. |
| Authorship | Pass | Consent is confirmed for the ten names on the exact v1.10.0 filing copy. |
| Main contact | Pass | Shuhan He is identified as the main point of contact. |
| Rights | Pass | Page 1 contains Shuhan He's direct ownership warranty and CC0 release. |
| Required art | Pass | Color and true black-and-white assets are present at exact 18x18 and 72x72 dimensions. |
| Computer validation | Pass | Deterministic palette, connectedness, IoU, and difference-hash checks pass against six pinned Noto Emoji comparators. |
| Frequency evidence | Pass | All five required screenshots are present, reproducible, legible, and use `elephant` where required. |
| Citations | Pass | Material meaning, sequence, physiology, testing, dialysis, transplant, donation, and medication-review claims cite dictionary, NIH/NIDDK, or MedlinePlus sources. |
| PDF layout | Pass | Evidence sections begin on deliberate pages; no heading is stranded from its text or screenshot. |
| Public PDF | Open | Publish and verify the exact v1.10.0 PDF at a stable logged-out HTTPS URL. |
| Official form | Open | Reconcile the form with the exact PDF and archive the filing confirmation. |

## Computer-validation decision

The project uses deterministic computer validation rather than internal or external human-recognition testing
for this proposal. The test checks the required image dimensions, black-and-white palette, foreground
connectedness, and normalized 18x18 silhouette separation from Beans, Droplet, Anatomical Heart, Lungs,
Balloon, and Light Bulb.

Result: **PASS**. Maximum normalized silhouette IoU is 0.684 against a 0.72 ceiling; minimum 64-bit difference-
hash distance is 24 against a floor of 16. The complete method, pinned comparator URLs, hashes, thresholds,
and machine-readable results are in `validation/computer-validation.md` and
`validation/computer-validation.json`.

This validates machine-visible technical separation. It does not claim to measure human semantic recognition.

## Changes in 1.10.0

- Accepts Shuhan He's confirmation that all ten submitters consent to the exact author list.
- Replaces the human-recognition gate with reproducible deterministic computer validation.
- Adds authoritative citations and removes weak or redundant sequence claims.
- Rebuilds the PDF with deliberate evidence-section page breaks and no stranded headings.

No artwork asset, frequency screenshot, submitter name, main contact, or rights statement changed in this
version.
