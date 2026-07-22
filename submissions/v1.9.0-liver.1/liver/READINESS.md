# Liver v1.9.0-liver.1 Readiness Report

Review date: 2026-07-21

Status: **REVISION REQUIRED**

Internal readiness score: **74/100**

This is a project control score, not a Unicode score or approval prediction. Open must-pass gates override the
score. Do not publish or submit this prerelease.

## Identity and provenance

- Branch: `agent/liver-2026`
- Frozen base: `f14cd8844dfd0d9dc4b5fe6dcb5ed7e8f9eade00`
- Package: `submissions/v1.9.0-liver.1/`
- Sole submitter and main point of contact: Shuhan He
- Canonical source package: `submissions/v1.8.0/`
- Scope: only this prerelease's `VERSION`, `manifest.md`, `CHANGELOG.md`, and `liver/` differ from v1.8.0

## Decision

The source, artwork, visual-comparison evidence, current Trends/Ngram evidence, and PDF are materially improved.
The package is not ready to publish because current Google Search and Video counts, eligibility timing, human
recognition, confirmation of the revised 18x18 art rights statement, independent review, and external filing
controls remain open.

## Must-pass gates

| Gate | Result | Evidence or blocker |
| --- | --- | --- |
| Eligibility | **Open** | The current public sheet lists Liver as Declined on 2020-12-18 and 2022-07-30. Unicode bars re-review within four years. The public submitted-date clock would reach four years on 2026-07-30, but no archived Unicode/ESR confirmation establishes the controlling date. |
| Coordination and duplicate status | **Partial** | The current public sheet contains no Liver row marked Under Consideration, Prioritization Pending, Recommended to UTC, or Released. Because the sheet is updated annually, reconfirm immediately before filing. |
| Authorship | **Partial** | The package consistently names Shuhan He only, as required by the lane specification. Final approval of the exact PDF is not recorded. |
| Public PDF | **Open** | No stable logged-out public HTTPS URL exists for this exact PDF. |
| Official form | **Open** | No form reconciliation, authorization, filing, or confirmation is recorded. |
| Rights | **Partial** | The carried v1.8.0 license records Shuhan He's certification for the prior Liver art. The proposal contains the required CC0/ownership statement, but Shuhan He must reaffirm it against the revised 18x18 source and PNG files before promotion. |
| Required art | **Partial** | All four PNGs have exact dimensions and both monochrome files contain only black and white. Human recognition is not complete. |
| Frequency evidence | **Open** | Worldwide Web Trends, Worldwide Image Trends, and Ngram are current. Search and Video are clearly labeled 2020 historical snapshots because fresh results were blocked. |
| Comparator and scope | **Pass** | Current Trends and Ngram use `elephant`, Worldwide where available, and widest date ranges. |
| Selection factors | **Pass for prerelease** | Every current inclusion and exclusion factor is answered. Unsupported positive factors are `Not applicable`. |
| Automatic-decline screen | **Pass** | No logo, brand, protected character, text-bearing artwork, exact-image demand, signage, UI icon, or directional variant appears. |
| Final QA | **Pass for prerelease** | The rebuilt PDF has no placeholder, draft note, broken image, clipping, empty page, or contradictory readiness label. External filing gates remain open. |

Official requirements checked 2026-07-21:
https://www.unicode.org/emoji/proposals.html

Public proposal-status source checked 2026-07-21:
https://www.unicode.org/emoji/emoji-requests.html

Embedded public status CSV:
https://docs.google.com/spreadsheets/d/1yXZPw6jh5kYFmbDgIOK13UcRENwkOwYN4a9T3vyirO8/pub?gid=2110764947&single=true&output=csv

## Score

| Area | Max | Score | Reason |
| --- | ---: | ---: | --- |
| Eligibility and coordination | 15 | 10 | Exact public rows checked; controlling four-year date and final coordination remain open. |
| First-page format | 10 | 10 | Identity, date, keywords/category, four images, and rights statement are easy to find. |
| Image package and rights | 15 | 10 | Exact two-tone assets and four comparison boards pass technical review; human recognition and revised-art reaffirmation remain open. |
| Frequency and empirical evidence | 20 | 14 | Three current widest-range sources pass; Search and Video are historical due a documented block. |
| Inclusion factors | 15 | 12 | Unsupported claims were removed and the semantic gap is direct; recognition and complete current frequency still limit the case. |
| Exclusion factors | 10 | 10 | Stomach, Anatomical Heart, Cut of Meat, Beans, generic organ imagery, open-endedness, specificity, transience, and faulty comparison are addressed. |
| Worldwide and durable case | 5 | 5 | Current Trends are Worldwide and Ngram covers 1500-2022. |
| Independent review | 5 | 0 | No domain/factual or Unicode/process signoff exists for the exact PDF. |
| Packet and filing control | 5 | 3 | Immutable prerelease, rebuilt PDF, and technical QA pass; public URL, form, approval, and filing record are open. |
| **Total** | **100** | **74** | **Revision required.** |

## Evidence record

| Source | Date and settings | Result |
| --- | --- | --- |
| Google Search | 2020-07-12 historical snapshot; fresh attempt 2026-07-21 | Historical visible count retained. Fresh URL returned Google's unusual-traffic interstitial. |
| Google Video Search | 2020-07-12 historical snapshot; fresh attempt 2026-07-21 | Historical visible count retained. Fresh URL returned the same block. |
| Google Trends Web | 2026-07-21; Worldwide; 2004-present; All categories; Web Search | Current readable capture against `elephant`; long-run averages 46 and 50. |
| Google Trends Image | 2026-07-21; Worldwide; 2008-present; All categories; Image Search | Current readable capture against `elephant`; the recent endpoint is treated as provisional. |
| Google Books Ngram | 2026-07-21; English; 1500-2022; case-sensitive; smoothing 3 | Current readable widest-range capture against `elephant`. |

Full attempted Search URL:
https://www.google.com/search?q=liver&hl=en&num=10&pws=0

Full attempted Video URL:
https://www.google.com/search?tbm=vid&q=liver&hl=en&num=10&pws=0

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
  literal term, the strongest substitutes, and independent evidence.

## Verification completed

- Copied all 63 v1.8.0 files before editing; initial copy had zero SHA-256 mismatches.
- Hash-compared the final 45 carried-forward files outside `liver/` and package controls; zero mismatches and
  zero unexpected extras.
- Verified all 11 local proposal image links resolve.
- Verified color assets are exactly 18x18 and 72x72.
- Verified monochrome assets are exactly 18x18 and 72x72 and contain only `(0,0,0)` and `(255,255,255)` pixels.
- Rebuilt with `python scripts/make_submission_pdf.py submissions/v1.9.0-liver.1/liver/liver_emoji_proposal_SUBMIT.md`.
- Verified the PDF is 9 letter-size pages, 548,084 bytes, tagged, unencrypted, and free of forms and JavaScript.
- Verified Arial and Arial Bold fonts are embedded and subsetted with Unicode mappings.
- Verified extractable text, all expected hyperlink annotations, and all 13 embedded image objects.
- Rendered every page at 144 DPI and visually inspected evidence readability, clipping, page breaks,
  pagination, empty pages, glyphs, and image integrity.
- Scanned Markdown for TODO, TBD, placeholder, draft, stale-refresh, and contradictory readiness language; none
  remains. The two 2020 dates are intentional and explicitly labeled historical.

## Coordinator promotion notes

Do not merge this branch wholesale. If the lane is accepted after its open gates close, copy only the accepted
Liver delta onto the coordinator's then-current canonical package, expected to become `v1.12.0` under the
current sequence. A further Liver correction before acceptance must create `v1.9.0-liver.2`; do not edit this
snapshot after commit.

Required next actions:

1. Capture current Search and Video results from a clean network with visible counts and record exact URLs.
2. Run the prepared unprompted human recognition test for both 18x18 variants.
3. Confirm the controlling four-year eligibility date and recheck the live duplicate/status list.
4. Have Shuhan He reaffirm authorship, revised-art rights, and the exact PDF.
5. Obtain domain/factual and Unicode/process review.
6. Promote into the then-current canonical package, rebuild, re-verify, publish the exact PDF, reconcile the
   official form, obtain explicit authorization, file, and archive the confirmation.
