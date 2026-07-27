# Stomach v1.13 Candidate Readiness

Date: 2026-07-27

Packet version: `1.13.0-candidate.1`

Status: **REVISED CANDIDATE - ELIGIBILITY CONFIRMATION NOT ARCHIVED; EXACT-ASSET APPROVAL AND COAUTHOR CONSENT OPEN**

v1.13 responds to an independent external review of the v1.12 candidate PDF. See `REVIEW-RESPONSE-v1.13.md`
for the finding-by-finding record.

## Settled passes

| Gate | Status | Evidence |
| --- | --- | --- |
| Byline and contact | Pass | Shuhan He, MD; David Rhew, MD; and Heena Purohit are listed as submitters; Shuhan He remains the main point of contact. |
| Rights | Pass | Project-created GPT Image 2 artwork; Shuhan He confirmed submission and licensing rights. |
| Required artwork | Pass | Exact color and matching true black-and-white PNG derivatives exist at 18x18 and 72x72. Both black-and-white assets re-verified as exactly two colours, so the grayscale prohibition is met. |
| Distinctiveness evidence | Pass | Section D now carries a nearest-emoji comparison figure at 72x72 and 18x18 against Beans, Anatomical Heart, Lungs, and Meat on Bone, built by `scripts/build_stomach_comparison_board.py`. Previously the claim was prose only. |
| Elephant comparison on all five sources | Pass | Google Search and Google Video Search elephant baselines captured 2026-07-27 by `scripts/capture_elephant_baseline.mjs`. Trends and Ngram already carried the comparison. |
| Claim-to-exhibit agreement | Pass | Every frequency caption was re-checked against its own screenshot by pixel measurement. See `REVIEW-RESPONSE-v1.13.md`. |
| Metaphor and idiom evidence | Pass | Section A adds two supplementary Ngram exhibits: the tagged verb sense of `stomach`, and the idioms `a strong stomach`, `turn my stomach`, and `butterflies in my stomach`. |
| Method disclosure | Pass | Section E states private-window capture, widest available ranges, and the reason no qualifying Trends category was applied. |
| Candidate PDF | Pass | 8 pages, US Letter, unencrypted, embedded subset fonts, extractable text, no draft markers, 20 link annotations, page-by-page visual inspection. |

## Open gates

| Gate | Status | Remaining action |
| --- | --- | --- |
| Eligibility | **Not archived** | The public status sheet lists `Stomach` declined twice, submitted 2020-10-27 and 2022-07-28. The Emoji Submission FAQ bars re-submission for four years from the decline, not from the submission. The 2022 intake was decided around UTC #173 on 2022-11-01 to 11-03, so the bar may not lift before the 2026-07-31 window closes. Obtain a written eligibility confirmation from Unicode/ESR, or the original decline notice with its date, and archive it here before filing. |
| Filing date | Open | Do not file before 2026-07-28. Filing on 2026-07-26 or 2026-07-27 falls inside the four-year bar under every reading of it. The PDF is dated 2026-07-28 to match. |
| Concurrent organ filings | Open decision | Exclusion C argues Stomach is not one member of an anatomy series. Filing Kidney, Liver, or White Blood Cell into the same intake window weakens that answer. Decide whether Stomach is filed alone this cycle. |
| Exact-asset approval | Open | Record Shuhan's dated `APPROVE` or `REVISE` for the four exact assets and their hashes. The comparison figure now supports this decision directly. |
| Coauthor consent records | Open | Preserve written confirmation from David Rhew and Heena Purohit that each agrees to be listed as a submitter. |
| Final promotion | Candidate only | After the open records are complete, rebuild once, repeat PDF QA, and promote the immutable packet to `submissions/v1.13.0/`. |
| Public URL and form | Not authorized | Publish and file only after explicit authorization from Shuhan He. |

Do not promote this candidate to `submissions/v1.13.0/` or rename it `_SUBMIT` until the eligibility record,
exact-asset approval, coauthor consent records, and final PDF QA are complete.
