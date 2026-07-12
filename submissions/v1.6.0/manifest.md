# Medical Emoji Proposal Release v1.6.0

Prepared: 2026-07-12

Status: **Content-final submission candidates. Confirm eligibility before filing.**

Guidance reviewed: Unicode's `Guidelines for Submitting Unicode Emoji Proposals`, updated 2026-05-20.

https://www.unicode.org/emoji/proposals.html

## Included proposals

| Proposal | Submission PDF | Source | Embedded frequency evidence |
| --- | --- | --- | --- |
| Kidney | `kidney/kidney_emoji_proposal_SUBMIT.pdf` | `kidney/kidney_emoji_proposal_SUBMIT.md` | Five of five required screenshots |
| Stomach | `stomach/stomach_emoji_proposal_SUBMIT.pdf` | `stomach/stomach_emoji_proposal_SUBMIT.md` | Five of five required screenshots |
| Liver | `liver/liver_emoji_proposal_SUBMIT.pdf` | `liver/liver_emoji_proposal_SUBMIT.md` | Five of five required screenshots |

Each PDF contains:

- Title, individual submitter, main point of contact, revision date, keywords, category, and sort location.
- Color and true black-and-white example images at 18x18 and 72x72 on the first page.
- An explicit first-page ownership and rights certification.
- Every current inclusion and exclusion factor, using `Not applicable` where a factor is not claimed.
- Embedded screenshots for Google Search, Google Video Search, Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer.
- Full reproducible evidence URLs and the true date and geographic scope of each capture.
- Original editable SVG artwork and PNG exports covered by `ARTWORK-LICENSE.md`.

## Evidence record

| Proposal | Search, Video, and Trends captures | Books Ngram capture | Known evidence limitation |
| --- | --- | --- | --- |
| Kidney | 2026-05-13, worldwide Trends | 2026-07-09 | None identified in the embedded set |
| Stomach | 2020-08-31, worldwide Trends | 2026-07-09 | A fresh 2026 recapture would strengthen the filing |
| Liver | 2020-07-12, United States Trends | 2026-07-09 | Replace both Trends images with worldwide captures before filing if Google becomes accessible |

The historical screenshots are preserved as genuine dated snapshots. They are not described as 2026 captures.
An attempted worldwide Liver Trends recapture on 2026-07-12 returned HTTP 429 from Google, so no replacement
was fabricated or substituted.

## Filing gate

The content and PDFs are complete, but the recorded decline notices for Kidney, Stomach, and Liver are dated
2022-11-04. Unicode's live guidance says emoji declined within the last four years are not eligible for
re-review, while the 2026 intake closes 2026-07-31. Do not file these three PDFs in the current intake unless
Unicode confirms that the concepts are eligible under its controlling-date interpretation.

After eligibility is confirmed, the individual submitter must:

1. Review the final publicly hosted PDF.
2. Accept the Unicode Emoji Proposal Agreement and License.
3. Submit each concept separately through the official form.
4. Archive the public PDF URL and submission confirmation.

Official form:

https://forms.gle/6KSiYHrUdBkTMNaB8

Resolved full form URL:

https://docs.google.com/forms/d/e/1FAIpQLSesdtPEbXCxXQnOb34UwhK7yPuCk52Pqix4FfQYgmW9Kt5cAw/viewform?usp=send_form

Emoji Proposal Agreement and License:

https://www.unicode.org/emoji/emoji-proposal-agreement.pdf

## Change from v1.2.0

- Republishes the three organ proposals as the current synchronized organ release.
- Updates proposal dates and current 2026 factor labels.
- Makes the first-page image ownership certification explicit.
- States directly that all five frequency screenshots are embedded in each proposal.
- Corrects historical Trends descriptions so `present` is not used for captures made in 2020.
- Removes stale feature-branch links from the public proposal text.
- Adds meaningful SVG title and description metadata and reproducible `--release` artwork generation.
- Sets descriptive PDF document titles.

## Rebuild commands

```powershell
python scripts/build_organ_proposal_assets.py --release v1.6.0
python scripts/make_submission_pdf.py submissions/v1.6.0/kidney/kidney_emoji_proposal_SUBMIT.md
python scripts/make_submission_pdf.py submissions/v1.6.0/stomach/stomach_emoji_proposal_SUBMIT.md
python scripts/make_submission_pdf.py submissions/v1.6.0/liver/liver_emoji_proposal_SUBMIT.md
```
