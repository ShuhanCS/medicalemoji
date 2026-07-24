# Liver v1.9.0-liver.3 Readiness Report

Review date: 2026-07-24

Status: **REVISION REQUIRED**

Internal readiness score: **85/100**

This is a project control score, not a Unicode score or approval prediction. Open must-pass gates override the
score. Do not publish or submit this prerelease.

## Identity and provenance

- Branch: `codex/liver-evidence`
- Frozen base: `762c054cca66ed0899eeab26ba3e070b5fbfec1d`
- Package: `submissions/v1.9.0-liver.3/`
- Sole submitter and main point of contact: Shuhan He
- Canonical source package: `submissions/v1.9.0-liver.2/`
- Scope: only this prerelease's `VERSION`, `manifest.md`, `CHANGELOG.md`, and `liver/` differ from
  `v1.9.0-liver.2`.

## Decision

The source, artwork, visual-comparison evidence, current frequency evidence, and PDF are materially improved.
Google’s native visible result counts now replace the prior overlays, and the literal semantic gap is more
concrete. The package is not ready to publish because human recognition, confirmation of the revised 18x18 art
rights statement, independent review, and external filing controls remain open.

## Must-pass gates

| Gate | Result | Evidence or blocker |
| --- | --- | --- |
| Eligibility | **Pass** | The project owner confirmed on 2026-07-23 that the eligibility timing is satisfied. The public sheet's 2020-12-18 and 2022-07-30 Declined rows remain retained as background evidence. |
| Coordination and duplicate status | **Partial** | The current public sheet contains no Liver row marked Under Consideration, Prioritization Pending, Recommended to UTC, or Released. Because the sheet is updated annually, reconfirm immediately before filing. |
| Authorship | **Partial** | The package consistently names Shuhan He only, as required by the lane specification. Final approval of the exact PDF is not recorded. |
| Public PDF | **Open** | No stable logged-out public HTTPS URL exists for this exact PDF. |
| Official form | **Open** | No form reconciliation, authorization, filing, or confirmation is recorded. |
| Rights | **Partial** | The carried v1.8.0 license records Shuhan He's certification for the prior Liver art. The proposal contains the required CC0/ownership statement, but Shuhan He must reaffirm it against the revised 18x18 source and PNG files before promotion. |
| Required art | **Partial** | All four PNGs have exact dimensions and both monochrome files contain only black and white. Human recognition is not complete. |
| Frequency evidence | **Pass** | All five required sources are current. Google Search and Video totals are visibly rendered in Google’s own Tools menu in unmodified 2026-07-24 captures. |
| Comparator and scope | **Pass** | Current Trends and Ngram use `elephant`, Worldwide where available, and widest date ranges. |
| Selection factors | **Pass for prerelease** | Every current inclusion and exclusion factor is answered. Unsupported positive factors are `Not applicable`. |
| Automatic-decline screen | **Pass** | No logo, brand, protected character, text-bearing artwork, exact-image demand, signage, UI icon, or directional variant appears. |
| Final QA | **Pass for prerelease** | The rebuilt PDF has no placeholder, draft note, broken image, clipping, empty page, or contradictory readiness label. External filing gates remain open. |

Official requirements checked 2026-07-24:
https://www.unicode.org/emoji/proposals.html

Public proposal-status source checked 2026-07-24:
https://www.unicode.org/emoji/emoji-requests.html

Embedded public status CSV:
https://docs.google.com/spreadsheets/d/1yXZPw6jh5kYFmbDgIOK13UcRENwkOwYN4a9T3vyirO8/pub?gid=2110764947&single=true&output=csv

## Score

| Area | Max | Score | Reason |
| --- | ---: | ---: | --- |
| Eligibility and coordination | 15 | 13 | Eligibility is confirmed. Final duplicate/status recheck remains part of filing control. |
| First-page format | 10 | 10 | Identity, date, keywords/category, four images, and rights statement are easy to find. |
| Image package and rights | 15 | 10 | Exact two-tone assets and four comparison boards pass technical review; human recognition and revised-art reaffirmation remain open. |
| Frequency and empirical evidence | 20 | 20 | All five sources are current; the Search and Video counts are preserved in Google’s native rendered Tools menu. |
| Inclusion factors | 15 | 14 | Unsupported claims were removed. The literal semantic gap now names concrete body-site communication contexts; recognition still limits the case. |
| Exclusion factors | 10 | 10 | Stomach, Anatomical Heart, Cut of Meat, Beans, generic organ imagery, open-endedness, specificity, transience, and faulty comparison are addressed. |
| Worldwide and durable case | 5 | 5 | Current Trends are Worldwide and Ngram covers 1500-2022. |
| Independent review | 5 | 0 | No domain/factual or Unicode/process signoff exists for the exact PDF. |
| Packet and filing control | 5 | 3 | Immutable prerelease, rebuilt PDF, and technical QA pass; public URL, form, approval, and filing record are open. |
| **Total** | **100** | **85** | **Revision required.** |

## Evidence record

| Source | Date and settings | Result |
| --- | --- | --- |
| Google Search | 2026-07-24; Google Web results; Tools control open | Google visibly renders `About 223,000,000 results (0.20s)` in its Tools menu. |
| Google Video Search | 2026-07-24; Google Video results; Tools control open | Google visibly renders `About 76,900,000 results (0.20s)` in its Tools menu. |
| Google Trends Web | 2026-07-21; Worldwide; 2004-present; All categories; Web Search | Current readable capture against `elephant`; long-run averages 46 and 50. |
| Google Trends Image | 2026-07-21; Worldwide; 2008-present; All categories; Image Search | Current readable capture against `elephant`; the recent endpoint is treated as provisional. |
| Google Books Ngram | 2026-07-21; English; 1500-2022; case-sensitive; smoothing 3 | Current readable widest-range capture against `elephant`. |

Full Search URL:
https://www.google.com/search?q=liver&hl=en&num=10&pws=0

Full Video URL:
https://www.google.com/search?udm=7&q=liver&hl=en&num=10&pws=0

Full Web Trends URL:
https://trends.google.com/trends/explore?date=all&q=liver%2Celephant

Full Image Trends URL:
https://trends.google.com/trends/explore?date=all_2008&gprop=images&q=liver,elephant

Full Ngram URL:
https://books.google.com/ngrams/graph?content=elephant%2Cliver&year_start=1500&year_end=2022&corpus=en&smoothing=3

## Recognition status

The revised color and black-and-white 18x18 artwork has not been tested with human participants. No recognition
percentage or confusion matrix is claimed. `RECOGNITION-PROTOCOL.md` defines a minimum 20-person unprompted
test, the 80% correct target, the 10% maximum for any single wrong concept, verbatim response recording, and a
new-participant retest after any art revision.

The visual boards cover Liver, Stomach, Anatomical Heart, Cut of Meat, Beans, and generic organ imagery at
18x18 and 72x72 in color and black and white. The new outlined monochrome art is materially more legible than
the v1.8.0 filled blob, but visual inspection is not a substitute for the human gate.

## Claim review

- Removed positive claims about metabolism, detoxification, disease, alcohol, donation/transplant, food,
  cuisine, courage, temperament, education, and cultural or metaphorical meanings.
- Marked Multiple meanings, Use in sequences, Completeness, and Compatibility `Not applicable`.
- Retained only a narrow National Cancer Institute citation for literal anatomy and lobe structure:
  https://www.cancer.gov/publications/dictionaries/cancer-terms/def/liver
- Rewrote Already representable, Overly specific, Open-ended, Transient, and Faulty comparison around the
  literal term, the strongest substitutes, independent evidence, and a bounded case that does not infer an
  anatomy-set entitlement.
- Adds specific literal contexts—an abnormal liver test, a liver lesion on a scan, and liver anatomy homework—
  to demonstrate the body-site ambiguity left by generic medical and education symbols.

## Verification completed

- Copied all 77 v1.9.0-liver.2 files before editing; initial copy had zero SHA-256 mismatches.
- Hash-compared the final 45 carried-forward files outside `liver/` and package controls; zero mismatches and
  zero unexpected extras.
- Verified all 11 local proposal image links resolve.
- Verified color assets are exactly 18x18 and 72x72.
- Verified monochrome assets are exactly 18x18 and 72x72 and contain only `(0,0,0)` and `(255,255,255)` pixels.
- Rebuilt with `python scripts/make_submission_pdf.py submissions/v1.9.0-liver.3/liver/liver_emoji_proposal_SUBMIT.md`.
- Verified the PDF is 10 letter-size pages, 1,088,430 bytes, tagged, unencrypted, and free of forms and
  JavaScript.
- Verified embedded Arial, Arial Bold, and Consolas fonts are subsetted with Unicode mappings.
- Verified all local Markdown image links resolve and the PDF contains the four required example images, two
  embedded visual-comparison boards, two current unmodified Google evidence captures, and three remaining frequency
  captures. The two additional comparison boards remain in the package as supplementary evidence.
- Rendered the changed evidence pages at 144 DPI and visually inspected the count labels, queries, page breaks,
  and image integrity.
- Scanned the proposal source for TODO, TBD, placeholder, draft, and stale-refresh language; none remains.

## Coordinator promotion notes

Do not merge this branch wholesale. If the lane is accepted after its open gates close, copy only the accepted
Liver delta onto the coordinator's then-current canonical package, expected to become `v1.12.0` under the
current sequence. A further Liver correction before acceptance must create a new patch version; do not edit this
snapshot after commit.

Required next actions:

1. Run the prepared unprompted human recognition test for both 18x18 variants.
2. Have Shuhan He reaffirm authorship, revised-art rights, and the exact PDF.
3. Obtain domain/factual and Unicode/process review.
4. Recheck the live duplicate/status list as part of the final form reconciliation.
5. Promote into the then-current canonical package, rebuild, re-verify, publish the exact PDF, reconcile the
   official form, obtain explicit authorization, file, and archive the confirmation.
