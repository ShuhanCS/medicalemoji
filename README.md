# Medical Emoji

## ⏳ Deadlines

| Due | What | Where |
|---|---|---|
| **2026-07-21** | **UTC document: "Health as a Category in Emoji Ordering"** — seven days before UTC #188 (July 28–30, Redmond, WA) | Email `docsubmit@unicode.org`, subject `UTC Doc: <topic>`. Spec: [`docs/plans/2026-07-09-utc-doc-health-category-spec.md`](docs/plans/2026-07-09-utc-doc-health-category-spec.md) |
| 2026-07-31 | Emoji proposal(s), 2026 submission window closes | [Emoji Submission Form](https://forms.gle/6KSiYHrUdBkTMNaB8). Spec: [`docs/plans/2026-07-09-microsoft-health-emoji-proposal.md`](docs/plans/2026-07-09-microsoft-health-emoji-proposal.md) |
| 2026-11-30 | Unicode notifies all submitters of status | — |

The UTC document is due **ten days before** the emoji deadline and is gated on none of the artwork,
licensing, or eligibility work. It moves first.

## 🏆 What actually wins

**Write proposals from [`docs/proposals/TEMPLATE-emoji-proposal.md`](docs/proposals/TEMPLATE-emoji-proposal.md).
Nothing else.** Evidence: [`docs/plans/2026-07-09-winners-vs-losers.md`](docs/plans/2026-07-09-winners-vs-losers.md),
comparing 55 proposals whose emoji were encoded against 29 from the same registers that were not.

| | Winners (55) | Losers (29) |
|---|---|---|
| Median words | **907** | 1,485 |
| Median images | **26** | 18 |
| Has an exclusion section | 94% | 93% |
| Answers Faulty comparison | **92%** | 72% |
| Cites a petition or social media | 45% | **75%** |
| Uses awareness / stigma / advocacy language | **1%** | **13%** |

Six rules, each earned from that data:

1. **Structure wins nothing.** Losers fill in the headings too. Never conclude a proposal was sound because
   it had the right sections.
2. **Under 1,200 words, over 20 images.** Losers write 60% more prose and show a third fewer screenshots.
3. **Write `N/A`.** Especially for Completeness and Compatibility. Arguing every factor drowns the strong ones.
4. **No petitions, no Instagram, no `Frequently Requested`.** Disallowed evidence, offered unprompted.
5. **No cause language.** *"A proposal may be advanced despite a 'cause' argument, but will not be advanced
   because of it."* Awareness and stigma appear thirteen times more often in the documents that failed.
6. **Draft the Open-ended answer first.** Name the neighbours you will not come back for. If that sentence
   cannot be written honestly, the proposal is not ready. It forbids filing kidney, liver and stomach together.

Never write "the heart and lungs were encoded, so the kidney should be." That is the textbook Faulty
Comparison, and it is how a medical-importance argument tends to phrase itself.

Our own record: [`docs/proposals/archive-2019-published/`](docs/proposals/archive-2019-published/) holds the
two proposals that won. [`docs/proposals/archive-2020-emojination-drafts/`](docs/proposals/archive-2020-emojination-drafts/)
holds the fifteen that never reached Unicode's document register at all.

Medical Emoji is a campaign and proposal workspace for adding high-utility medical emoji to the Unicode Standard.

This repository contains the public website, prior support materials, current Unicode research notes, and proposal planning files for the medical emoji concepts the project has pursued.

Last status check: 2026-05-14

## Current Submission Link

Unicode requires a publicly accessible PDF proposal submitted through the official form. Email, fax, and hard-copy submissions are not accepted.

Official Unicode emoji proposal guidelines:
https://www.unicode.org/emoji/proposals.html

Official Unicode Emoji Submission Form:
https://forms.gle/6KSiYHrUdBkTMNaB8

Resolved Google Form URL:
https://docs.google.com/forms/d/e/1FAIpQLSesdtPEbXCxXQnOb34UwhK7yPuCk52Pqix4FfQYgmW9Kt5cAw/viewform?usp=send_form

Unicode emoji proposal status page:
https://www.unicode.org/emoji/emoji-proposals-status.html

Live public status CSV:
https://docs.google.com/spreadsheets/d/1yXZPw6jh5kYFmbDgIOK13UcRENwkOwYN4a9T3vyirO8/pub?gid=2110764947&single=true&output=csv

Emoji Submission FAQ:
https://www.unicode.org/faq/emoji_submission

Emoji Proposal Agreement and License:
https://www.unicode.org/emoji/emoji-proposal-agreement.pdf

## 2026 Unicode Intake

Unicode's guidelines page says:

- Last update: `2026-04-02`.
- Current intake window: accepting submissions until `2026-07-31`.
- Declined emoji are not eligible for re-review within the last four years.
- The page body still contains some stale 2025 text, so date-sensitive submissions should be verified with Unicode/ESR before filing.

Important practical note: Unicode's public status sheet lists `Date Submitted`, not the actual decline decision date or notification date. The "reeligible by submitted-date clock" column below is a planning estimate only. Before filing any resubmission, confirm whether Unicode counts the four-year bar from the submitted date, internal decline decision date, notification email date, or status publication/update date.

## Emoji Submission Status

The table below combines active candidates from `src/data/emoji.ts` and legacy proposal assets in `public/images/emoji/`. Status rows are from Unicode's live public proposal status CSV, checked 2026-05-13.

| Concept | Repo source | Unicode public status rows | Latest public status | Last public date submitted | Reeligible by submitted-date clock | Next step |
| --- | --- | --- | --- | --- | --- | --- |
| Kidney / Kidneys | Active site candidate | `Kidney` declined 2019-12-17; `KIDNEYS` declined 2022-07-19 | Declined | 2022-07-19 | 2026-07-19 | Verify actual 2022 decline/notification date before any 2026 filing; coordinate with ISN and Turkish Society of Nephrology on one aligned proposal. |
| Liver | Active site candidate | `Liver` declined 2020-12-18; `Liver` declined 2022-07-30 | Declined | 2022-07-30 | 2026-07-30 | Technically falls just before the 2026-07-31 intake deadline by submitted-date clock, but verify actual decline date before filing. |
| Stomach | Active site candidate | `Stomach` declined 2020-10-27; `Stomach` declined 2022-07-28 | Declined | 2022-07-28 | 2026-07-28 | Verify actual decline date; if eligible, rebuild with current evidence and image-license requirements. |
| Spine | Active site candidate | `Spine` declined 2020-10-27; `Spine` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms a materially different concept is eligible. |
| Intestines | Active site candidate | `Intestines` declined 2020-12-18; `Intestines` declined 2024-04-04 | Declined | 2024-04-04 | 2028-04-04 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| ECG / EKG | Active site candidate | `ECG` declined 2020-12-18; `ECG` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| White Blood Cell | Active site candidate | `White Blood Cell` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; verify actual decline date, then build current-format evidence. |
| Blood Bag | Active site candidate | `Blood bag` declined 2017-05-16; `Blood Bag (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; refresh evidence and avoid relying on blood-donation cause framing alone. |
| Pill Pack | Active site candidate | `Pill Pack` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; decide whether to pursue pill pack or pill box to avoid duplicate/overlapping proposals. |
| Weight Scale | Active site candidate | `Bathroom Scale` expired 2018-02-27; `Weight Scale (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; needs strong broad-usage evidence beyond obesity/weight-loss cause framing. |
| Leg Cast | Legacy proposal asset | `Leg Cast` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; needs current proposal folder, usage evidence, and open-license images. |
| IV Bag | Legacy proposal asset | `IV Bag` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; clarify broad meaning versus already represented medical-care emoji. |
| CT Scan | Legacy proposal asset | `CT Scan` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Reeligible by submitted-date clock; likely needs a strong visual distinctiveness case at 18x18. |
| Pill Box | Legacy proposal asset | `Pill Box` declined 2020-10-27 | Declined | 2020-10-27 | 2024-10-27 | Reeligible by submitted-date clock; decide whether this is stronger or weaker than pill pack before filing. |

## Submission Package Requirements

Every renewed proposal needs a current-format PDF. The top of the first page must include:

- Title: `Proposal for Emoji: <name>`.
- Submitter names, separated with semicolons if there are multiple authors.
- One main point of contact.
- Date, updated on revisions.
- Identification keywords and proposed emoji category.
- Color and black-and-white example images at both `18x18` and `72x72`.
- Image rights/license statement.

The proposal body must address:

- Factors for inclusion: multiple meanings, use in sequences, breaks new ground, visual distinctiveness, high expected usage, completeness if applicable, compatibility if applicable.
- Factors for exclusion: already represented, overly specific, open-ended, transient, and justified only by comparison to existing emoji.
- Other information, including design considerations and source notes.

Required frequency evidence:

- Google Search screenshot with result count.
- Google Video Search screenshot with result count.
- Google Trends Web Search screenshot.
- Google Trends Image Search screenshot.
- Google Books Ngram Viewer screenshot.
- Trends and Ngram evidence must include `elephant` as the comparator.

Evidence that does not count:

- Petitions.
- Hashtags.
- Social posts asking for the emoji.
- Anecdotes.
- Society support letters as frequency evidence.
- Cause/awareness arguments by themselves.

## Submission Packet Semver

Submission packets use semantic versioning. Treat the packet version as the version of the full set of files submitted or prepared for submission, not as the version of any one document.

- `MAJOR`: legal/entity/signature/offer structure changed, or a submitted package is being replaced.
- `MINOR`: substantive response change, scope change, pricing method change, added/removed attachment, changed claim, or changed supplier diversity commitment.
- `PATCH`: typo, formatting, filename cleanup, or non-substantive clarification.

If any file in a submission packet changes, create the next packet version and copy or rename every retained submission file to the new version number, even if the retained file content did not change. This keeps packet contents synchronized and prevents accidental mixing of old and new files.

Example: if `v2.1.2_price_catalog_SUBMIT.xlsx` changes, the synchronized packet becomes:

```text
v2.1.3_application_response_SUBMIT.docx
v2.1.3_price_catalog_SUBMIT.xlsx
v2.1.3_supplier_diversity_plan_SUBMIT.docx
```

Recommended folder structure:

```text
submissions/vX.Y.Z/
  manifest.md
  vX.Y.Z_application_response_SUBMIT.pdf
  vX.Y.Z_support_letters_REFERENCE_ONLY.pdf
  vX.Y.Z_proposal_SUBMIT.pdf
```

## Submission Packet Manifest

Every `submissions/vX.Y.Z/` folder must include `manifest.md` with:

- Packet version.
- Date prepared.
- Bid/opportunity ID or proposal identifier, plus source RFP/addendum/source-guidance version reviewed.
- Files included and each file role: `SUBMIT`, `SIGNATURE_REQUIRED`, or `REFERENCE_ONLY`.
- Approval status, signer/submitter, and known blockers.
- Change notes from the previous packet version.

## Next Steps When Reeligible

1. Verify the exact eligibility date with Unicode/ESR or the original decline notification email.
2. Pick one lead proposal per intake cycle to avoid splitting effort across overlapping concepts.
3. Coordinate submitters and supporters before filing so there is one clean submission.
4. Create a proposal folder under `docs/proposals/<emoji>-emoji-<year>/`.
5. Capture live frequency screenshots in a private browser session.
6. Produce color and black-and-white images at `18x18` and `72x72`.
7. Document image ownership, assignment, work-for-hire status, or open-license/public-domain source URL.
8. Draft the current-format PDF and make it publicly accessible.
9. Submit through the official Unicode Emoji Submission Form.
10. Archive the submitted PDF, screenshots, source URLs, and confirmation details in this repo.

## Current Proposal Workspaces

Kidney 2026 workspace:
`docs/proposals/kidney-emoji-2026/`

Stomach 2026 workspace:
`docs/proposals/stomach-emoji-2026/`

Liver 2026 workspace:
`docs/proposals/liver-emoji-2026/`

First synchronized preliminary submission packet:
`submissions/v0.1.0/`

Current readiness packet:
`submissions/v0.2.0/`

Current standalone submission packets:

- Kidney: `submissions/v2.2.0/`
- Stomach: `submissions/v2.3.1/`

Key files:

- `submissions/v2.3.1/manifest.md`
- `submissions/v2.3.1/v2.3.1_stomach_emoji_proposal_SUBMIT.md`
- `submissions/v2.3.1/v2.3.1_stomach_emoji_proposal_SUBMIT.pdf`
- `submissions/v2.3.1/images/v2.3.1_stomach_gpt_image_2_SOURCE_REFERENCE_ONLY.png`
- `submissions/v2.3.1/images/v2.3.1_stomach_color_18x18_SUBMIT.png`
- `submissions/v2.3.1/images/v2.3.1_stomach_color_72x72_SUBMIT.png`
- `submissions/v2.3.1/images/v2.3.1_stomach_bw_18x18_SUBMIT.png`
- `submissions/v2.3.1/images/v2.3.1_stomach_bw_72x72_SUBMIT.png`
- `submissions/v2.2.0/manifest.md`
- `submissions/v2.2.0/v2.2.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v2.2.0/v2.2.0_kidney_emoji_proposal_SUBMIT.pdf`
- `docs/proposals/kidney-emoji-2026/README.md`
- `docs/proposals/emoji-proposal-approval-rubric.md`
- `docs/proposals/kidney-emoji-2026/decline-date-submission-update.md`
- `docs/proposals/kidney-emoji-2026/evidence-capture-checklist.md`
- `docs/proposals/kidney-emoji-2026/fact-base.md`
- `docs/proposals/kidney-emoji-2026/proposal-draft-outline.md`
- `docs/proposals/kidney-emoji-2026/unicode-timeline-and-guidelines.md`
- `docs/proposals/stomach-emoji-2026/README.md`
- `docs/proposals/stomach-emoji-2026/proposal-working-draft.md`
- `docs/proposals/stomach-emoji-2026/evidence-capture-checklist.md`
- `docs/proposals/stomach-emoji-2026/submission-readiness-checklist.md`
- `docs/proposals/liver-emoji-2026/README.md`
- `docs/proposals/liver-emoji-2026/proposal-working-draft.md`
- `docs/proposals/liver-emoji-2026/support-letter-inventory.md`
- `docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json`
- `docs/research/unicode-winning-submissions/analysis.md`
- `docs/research/kidney-v0.12.0-successful-proposal-audit.md`
- `docs/plans/2026-05-13-kidney-v0.10.0-improvement-plan.md`
- `docs/specs/2026-07-23-kidney-submission-argument-improvement-spec.md`
- `submissions/v2.1.1/manifest.md`
- `submissions/v2.1.1/v2.1.1_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v2.1.1/v2.1.1_kidney_emoji_proposal_SUBMIT.pdf`
- `submissions/v2.1.1/v2.1.1_submission_finalization_SIGNATURE_REQUIRED.md`
- `submissions/v2.1.1/images/v2.1.1_kidney_color_18x18_SUBMIT.png`
- `submissions/v2.1.1/images/v2.1.1_kidney_color_72x72_SUBMIT.png`
- `submissions/v2.1.1/images/v2.1.1_kidney_bw_18x18_SUBMIT.png`
- `submissions/v2.1.1/images/v2.1.1_kidney_bw_72x72_SUBMIT.png`
- `submissions/v2.1.1/evidence/visual-review/v2.1.1_18x18_visual_review_board_SUBMIT.png`
- `submissions/v0.13.3/manifest.md`
- `submissions/v0.13.3/v0.13.3_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.13.3/images/v0.13.3_kidney_bw_18x18_SUBMIT.png`
- `submissions/v0.13.3/images/v0.13.3_kidney_bw_72x72_SUBMIT.png`
- `submissions/v0.13.3/evidence/visual-review/v0.13.3_18x18_visual_review_board_SUBMIT.png`
- `submissions/v0.13.2/manifest.md`
- `submissions/v0.13.2/v0.13.2_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.13.2/images/v0.13.2_kidney_bw_18x18_SUBMIT.png`
- `submissions/v0.13.2/images/v0.13.2_kidney_bw_72x72_SUBMIT.png`
- `submissions/v0.13.2/evidence/visual-review/v0.13.2_18x18_visual_review_board_SUBMIT.png`
- `submissions/v0.13.1/manifest.md`
- `submissions/v0.13.1/v0.13.1_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.13.1/v0.13.1_18x18_visual_review_REFERENCE_ONLY.md`
- `submissions/v0.13.1/evidence/visual-review/v0.13.1_18x18_visual_review_board_SUBMIT.png`
- `submissions/v0.13.0/manifest.md`
- `submissions/v0.13.0/v0.13.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.13.0/v0.13.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.13.0/v0.13.0_frequency_evidence_review_REFERENCE_ONLY.md`
- `submissions/v0.12.0/manifest.md`
- `submissions/v0.12.0/v0.12.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.12.0/v0.12.0_frequency_evidence_review_REFERENCE_ONLY.md`
- `submissions/v0.11.0/manifest.md`
- `submissions/v0.11.0/v0.11.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.11.0/v0.11.0_submission_text_scan_REFERENCE_ONLY.md`
- `submissions/v0.10.0/manifest.md`
- `submissions/v0.10.0/v0.10.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.10.0/v0.10.0_accepted_proposal_comparator_review_REFERENCE_ONLY.md`
- `submissions/v0.1.0/manifest.md`
- `submissions/v0.1.0/v0.1.0_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.1.0/v0.1.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.1.0/v0.1.0_sources_and_evidence_index_REFERENCE_ONLY.md`
- `submissions/v0.2.0/manifest.md`
- `submissions/v0.2.0/v0.2.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.2.0/v0.2.0_execution_log_REFERENCE_ONLY.md`
- `submissions/v0.3.0/manifest.md`
- `submissions/v0.3.0/v0.3.0_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.3.0/v0.3.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.3.0/v0.3.0_sources_and_evidence_index_REFERENCE_ONLY.md`
- `submissions/v0.3.0/v0.3.0_execution_log_REFERENCE_ONLY.md`
- `submissions/v0.4.0/manifest.md`
- `submissions/v0.4.0/v0.4.0_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.4.0/v0.4.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.4.0/v0.4.0_sources_and_evidence_index_REFERENCE_ONLY.md`
- `submissions/v0.4.0/v0.4.0_execution_log_REFERENCE_ONLY.md`
- `submissions/v0.4.0/images/v0.4.0_kidney_color_18x18_REFERENCE_ONLY.png`
- `submissions/v0.4.0/images/v0.4.0_kidney_color_72x72_REFERENCE_ONLY.png`
- `submissions/v0.4.0/images/v0.4.0_kidney_bw_18x18_REFERENCE_ONLY.png`
- `submissions/v0.4.0/images/v0.4.0_kidney_bw_72x72_REFERENCE_ONLY.png`
- `submissions/v0.5.0/manifest.md`
- `submissions/v0.5.0/v0.5.0_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.5.0/v0.5.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.5.0/v0.5.0_rubric_alignment_REFERENCE_ONLY.md`
- `submissions/v0.5.0/v0.5.0_sources_and_evidence_index_REFERENCE_ONLY.md`
- `submissions/v0.5.0/v0.5.0_execution_log_REFERENCE_ONLY.md`
- `submissions/v0.6.0/manifest.md`
- `submissions/v0.6.0/v0.6.0_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.6.0/v0.6.0_submission_readiness_checklist_REFERENCE_ONLY.md`
- `submissions/v0.6.0/v0.6.0_frequency_evidence_review_REFERENCE_ONLY.md`
- `submissions/v0.6.0/v0.6.0_18x18_visual_review_REFERENCE_ONLY.md`
- `submissions/v0.6.0/evidence/frequency/`
- `submissions/v0.6.0/evidence/visual-review/`
- `submissions/v0.6.1/manifest.md`
- `submissions/v0.6.1/v0.6.1_kidney_emoji_proposal_REFERENCE_ONLY.md`
- `submissions/v0.6.1/v0.6.1_submission_url_REFERENCE_ONLY.md`
- `submissions/v0.6.1/v0.6.1_frequency_evidence_review_REFERENCE_ONLY.md`
- `submissions/v0.6.1/v0.6.1_18x18_visual_review_REFERENCE_ONLY.md`
- `submissions/v0.7.0/manifest.md`
- `submissions/v0.7.0/v0.7.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.7.0/v0.7.0_submission_finalization_SIGNATURE_REQUIRED.md`
- `submissions/v0.7.0/images/v0.7.0_kidney_color_18x18_SUBMIT.png`
- `submissions/v0.7.0/images/v0.7.0_kidney_color_72x72_SUBMIT.png`
- `submissions/v0.7.0/images/v0.7.0_kidney_bw_18x18_SUBMIT.png`
- `submissions/v0.7.0/images/v0.7.0_kidney_bw_72x72_SUBMIT.png`
- `submissions/v0.8.0/manifest.md`
- `submissions/v0.8.0/v0.8.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.8.0/v0.8.0_sources_and_evidence_index_REFERENCE_ONLY.md`
- `submissions/v0.9.0/manifest.md`
- `submissions/v0.9.0/v0.9.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v0.9.0/images/v0.9.0_kidney_color_18x18_SUBMIT.png`
- `submissions/v0.9.0/images/v0.9.0_kidney_color_72x72_SUBMIT.png`
- `submissions/v0.9.0/images/v0.9.0_kidney_bw_18x18_SUBMIT.png`
- `submissions/v0.9.0/images/v0.9.0_kidney_bw_72x72_SUBMIT.png`

## Development

This is a Next.js site.

```bash
npm install
npm run dev
npm run lint
npm run build
```

## Contact Form Environment

The site contact form posts to `/api/contact`, verifies Cloudflare Turnstile, and sends mail through Resend.

Required production environment variables:

- `NEXT_PUBLIC_TURNSTILE_SITE_KEY`
- `TURNSTILE_SECRET_KEY`
- `RESEND_API_KEY`
- `CONTACT_FORM_FROM` - a Resend-verified sender address
- `CONTACT_FORM_TO` - optional; defaults to `info@conductscience.com`

## Repository

GitHub:
https://github.com/ShuhanCS/medicalemoji
