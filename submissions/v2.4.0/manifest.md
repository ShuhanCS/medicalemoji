# Stomach Emoji Submission Packet Manifest

Packet version: `v2.4.0`

Date prepared: 2026-07-28

Proposal identifier: `stomach-emoji-2026`

Source guidance reviewed: Unicode proposal guidelines last updated 2026-05-20,
`https://unicode.org/emoji/proposals.html`

Status: `REVIEW READY - NOT FILED`. The proposal is formatted for the 2026 intake and scores 90/100 on the
internal approval rubric, but eligibility confirmation, final reviewers, public hosting, and filing remain open.

## Version decision

MINOR bump from Stomach v2.3.1 because this release substantively restructures the reviewer document and adds
an evidence-backed existing-user and interoperability case. The v2.3.1 Stomach and v2.2.0 Kidney packets remain
immutable. The approved Stomach artwork does not change.

## Promotion source

This packet derives from Stomach v2.3.1 at commit `4252dc2f3a07fa50b543b6a9c2f309154370e7d9`.

## What changed

- Reordered the proposal into the current seven-section 2026 structure.
- Kept all first-page administrative, image, and rights information at the top of page one.
- Added a pinned CLDR 48.2 English annotation audit demonstrating the current search-routing gap.
- Connected that gap to existing-user experience and cross-product plain-text interoperability.
- Kept Compatibility at `N/A` because no high-frequency proprietary Stomach pictograph is claimed.
- Moved detailed frequency exhibits into the dedicated Evidence of frequency section.
- Reduced the reviewer PDF to 1,098 extracted words, below the repository template's 1,200-word budget.

## Submit files

| File | Role | Description |
| --- | --- | --- |
| `v2.4.0_stomach_emoji_proposal_SUBMIT.md` | `SUBMIT` | Proposal source in the current 2026 section order. |
| `v2.4.0_stomach_emoji_proposal_SUBMIT.pdf` | `SUBMIT` | Nine-page reviewer PDF rebuilt for the substantive case revision. |
| `images/v2.4.0_stomach_color_18x18_SUBMIT.png` | `SUBMIT` | Approved 18x18 color example. |
| `images/v2.4.0_stomach_color_72x72_SUBMIT.png` | `SUBMIT` | Approved 72x72 color example. |
| `images/v2.4.0_stomach_bw_18x18_SUBMIT.png` | `SUBMIT` | Approved true black-and-white 18x18 example. |
| `images/v2.4.0_stomach_bw_72x72_SUBMIT.png` | `SUBMIT` | Approved true black-and-white 72x72 example. |
| `images/v2.4.0_stomach_distinctiveness_comparison_SUBMIT.png` | `SUBMIT` | Native-size comparison used for Distinctiveness. |
| `evidence/frequency/*_SUBMIT.png` | `SUBMIT` | Required and supplementary empirical-use exhibits. |

## Reference-only files

| File | Role | Description |
| --- | --- | --- |
| `images/v2.4.0_stomach_gpt_image_2_SOURCE_REFERENCE_ONLY.png` | `REFERENCE_ONLY` | Approved 1024x1024 source. |
| `evidence/interoperability/v2.4.0_cldr_english_emoji_search_audit_2026-07-28_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Reproducible CLDR 48.2 audit and limitations. |
| `v2.4.0_rubric_score_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Internal 100-point rubric score and open must-pass gates. |
| `v2.4.0_stomach_artwork_approval_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Dated exact-asset approval and frozen hashes. |
| `v2.4.0_stomach_coauthor_consent_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Three-person byline and verified Microsoft title metadata. |
| `v2.4.0_stomach_review_response_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Historical finding-by-finding review record. |
| `v2.4.0_submission_readiness_REFERENCE_ONLY.md` | `REFERENCE_ONLY` | Completed and remaining submission gates. |
| `v2.4.0_print_REFERENCE_ONLY.css` | `REFERENCE_ONLY` | Print stylesheet used for the reviewer PDF. |
| `evidence/frequency/*_REFERENCE_ONLY.json` | `REFERENCE_ONLY` | Frequency capture logs. |

## Frozen integrity hashes

| Artifact | SHA-256 |
| --- | --- |
| Approved 1024x1024 source | `250389e208e3d71488e1895b49c7d4fd69e95507eb3d06f73060db7b34767d7a` |
| Color 18x18 | `bb0159f241e6163ea9eae2851640125ab90bdc4c69301ef76077c8c6dc10e046` |
| Color 72x72 | `750fb57ced6cd0e0bf2394686770c91f832ae13b9b8db49965ae486dff9c5068` |
| Black-and-white 18x18 | `73ed28b740ddaf4c11ac1246d7a0ca8906ac87d082bc48fa1afabf76c26a78d8` |
| Black-and-white 72x72 | `4d24ea39a0d5ff12542e6912a7e304394d8ab14d725d606b221f0f6f3dfedfdc` |
| Reviewer PDF | `02df5e6ab65160b374abedc8fda373c728ae0a8e4990223a3f4fa65e67781015` |

## Remaining external actions

1. Obtain authoritative confirmation that the four-year re-review bar has expired for the 2026 intake.
2. Obtain one domain review and one Unicode/process review of this exact v2.4.0 PDF.
3. Complete Shuhan He's final review.
4. Host the exact PDF at a stable logged-out HTTPS URL and verify it anonymously.
5. File only after explicit authorization, then archive the URL and form confirmation.
