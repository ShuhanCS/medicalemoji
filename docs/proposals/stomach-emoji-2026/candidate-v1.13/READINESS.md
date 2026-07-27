# Stomach v1.13 Candidate Readiness

Date: 2026-07-27

Packet version: `1.13.0-candidate.3`

Status: **CANDIDATE COMPLETE - READY FOR CANONICAL COORDINATION; PUBLICATION AND FILING NOT AUTHORIZED**

Candidate.1 responded to an independent review of the v1.12 PDF. Candidate.2 reconciles those improvements with
the Stomach finalization specification: it preserves the settled eligibility record, keeps the proposal wholly
self-contained, and removes reviewer-facing discussion of discarded comparisons with other active concepts.
Candidate.3 closes the exact-art and coauthor-consent gates without changing the proposal, evidence, artwork, or
verified PDF.

## Settled passes

| Gate | Status | Evidence |
| --- | --- | --- |
| Eligibility | Pass | Eligibility is a settled project input confirmed by Shuhan He on 2026-07-26 and preserved in `source-ledger-v1.12.md`. The proposal does not narrate an eligibility dispute. |
| Byline and contact | Pass | Shuhan He, MD; David Rhew, MD; and Heena Purohit are listed as submitters; Shuhan He remains the main point of contact. |
| Rights | Pass | Project-created GPT Image 2 artwork; Shuhan He confirmed submission and licensing rights. |
| Required artwork | Pass | The exact color and matching true black-and-white PNG derivatives exist at 18x18 and 72x72. Both black-and-white assets contain exactly black and white. |
| Exact artwork integrity | Pass | All four files remain byte-identical to the hashes frozen in `CASE-BRIEF.md`; no art revision was made for Candidate.2. |
| Distinctiveness evidence | Pass | Section D carries an actual-size comparison against the nearest encoded visual alternatives at 72x72 and 18x18. |
| Frequency evidence | Pass | All five required sources include the `elephant` baseline, and every caption was checked against its own exhibit. The mixed result is reported proportionately. |
| Meaning and durability evidence | Pass | Section A includes supplementary Books exhibits for the verb sense and established idioms; the public proposal omits internal discarded-comparison notes. |
| Independent-submission boundary | Pass | The public proposal is one self-contained Stomach document. It does not mention another active filing, coordinated slate, companion concept, or anatomy-completion theory. |
| Exact-asset approval | Pass | Shuhan He recorded `APPROVE` on 2026-07-27 for the four exact files and hashes in `IMAGE-APPROVAL.md`. |
| Coauthor consent | Pass | Shuhan He confirmed on 2026-07-27 that David Rhew and Heena Purohit consented to the exact ordered byline; see `COAUTHOR-CONSENT.md`. |
| Candidate PDF | Pass | Rebuilt from Candidate.2 and checked technically and page by page; see the verification record below. |

## Open gates

| Gate | Status | Remaining action |
| --- | --- | --- |
| Canonical promotion | Coordinator action | Give this accepted Stomach delta to the canonical-package coordinator. The coordinator must combine accepted concept deltas without mixing their proposal prose, evidence, artwork, readiness records, or form data. Do not mutate `submissions/v1.11.0/`. |
| Public URL and form | Not authorized | Publish and file only after explicit authorization from Shuhan He. |

The Stomach candidate gates are complete. Canonical promotion remains a separate coordinator action.
Publication and filing remain separate external actions requiring Shuhan's authorization.

## Candidate.2 verification

- Exact artwork dimensions and hashes rechecked; both black-and-white files contain exactly two colours.
- Candidate source screened for references to another active filing, co-submission language, draft markers, and
  unsupported compatibility or completeness claims.
- PDF rebuilt from the current Markdown and stylesheet, then checked for page size, encryption, embedded fonts,
  extractable text, live link annotations, and page-by-page visual integrity.
- Evidence was not recaptured because the current exhibits remain legible and their query/result claims did not
  change.

## Candidate.3 closure

- `IMAGE-APPROVAL.md` records Shuhan's dated approval tied to the exact four asset hashes.
- `COAUTHOR-CONSENT.md` records Shuhan's confirmation that both coauthors consented to the exact byline.
- The Candidate.2 proposal source and PDF were preserved byte-for-byte; Candidate.3 changes control records only.
