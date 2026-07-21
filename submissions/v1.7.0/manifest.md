# Medical Emoji Proposal Release v1.7.0

Prepared: 2026-07-12

Status: **Confirmed eligible submission candidates. Refresh the identified evidence and complete the
one-by-one proposal review before filing.**

Guidance reviewed: Unicode's `Guidelines for Submitting Unicode Emoji Proposals`, updated 2026-05-20.

https://www.unicode.org/emoji/proposals.html

## Included proposals

| Proposal | Submission PDF | Source | Embedded frequency evidence |
| --- | --- | --- | --- |
| Kidney | `kidney/kidney_emoji_proposal_SUBMIT.pdf` | `kidney/kidney_emoji_proposal_SUBMIT.md` | Five of five required screenshots |
| Stomach | `stomach/stomach_emoji_proposal_SUBMIT.pdf` | `stomach/stomach_emoji_proposal_SUBMIT.md` | Five of five required screenshots |
| Liver | `liver/liver_emoji_proposal_SUBMIT.pdf` | `liver/liver_emoji_proposal_SUBMIT.md` | Five of five required screenshots |

Each PDF contains:

- Title, individual submitter names, main point of contact, revision date, keywords, category, and sort location.
- Color and true black-and-white example images at 18x18 and 72x72 on the first page.
- An explicit first-page ownership and rights certification.
- Every current inclusion and exclusion factor, using `Not applicable` where a factor is not claimed.
- Embedded screenshots for Google Search, Google Video Search, Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer.
- Full reproducible evidence URLs and the true date and geographic scope of each capture.
- Original editable 72x72 and purpose-built 18x18 SVG artwork plus PNG exports covered by `ARTWORK-LICENSE.md`.

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

Shuhan He has confirmed that Kidney, Stomach, and Liver are eligible for the 2026 intake. Preserve the written
confirmation in the filing record. Eligibility is settled; the v1.7.0 PDFs are not yet submission-ready.
Complete the one-by-one review in the
[2026 submission slate specification](../../docs/proposals/2026-submission-slate-spec.md).

After each proposal passes the content, evidence, art, and technical gates, the individual submitter must:

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

## Change from v1.6.0

- Replaces the schematic organ drawings with a coherent emoji-art system: dominant silhouettes, dark keylines, restrained depth, and purpose-built 18x18 masters.
- Changes Kidney from a paired anatomy diagram to one bold kidney with a hilum and short vessel/ureter cues.
- Rebuilds Stomach as a clean J-shaped organ and Liver as a fuller asymmetric wedge with a tucked gallbladder.
- Restores the verified Kidney co-author list as bare individual names and retains Shuhan He as the main point of contact.
- Removes the redundant Section E summary tables and places the result, date, settings, and reproducible URL next to each embedded screenshot.
- Crops the Kidney Search capture to remove browser-automation chrome and focuses both Kidney Trends captures on the query controls and interest-over-time chart without changing the underlying evidence.
- Adds citations for the Kidney and Stomach multiple-meaning claims.
- Corrects Liver's internal wording so it does not claim multiple meanings after marking that factor not applicable.
- Retains the eligibility and evidence-refresh gates without presenting historical captures as current evidence.

## Rebuild commands

```powershell
python scripts/build_organ_proposal_assets.py --release v1.7.0
python scripts/make_submission_pdf.py submissions/v1.7.0/kidney/kidney_emoji_proposal_SUBMIT.md
python scripts/make_submission_pdf.py submissions/v1.7.0/stomach/stomach_emoji_proposal_SUBMIT.md
python scripts/make_submission_pdf.py submissions/v1.7.0/liver/liver_emoji_proposal_SUBMIT.md
```
