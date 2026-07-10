# Medical Emoji

## ⏳ Deadlines

| Due | What | Where |
|---|---|---|
| 2026-07-21 | Optional UTC data document, if Microsoft chooses to carry it; not on the emoji-proposal critical path | Spec: [`docs/plans/2026-07-09-utc-doc-health-category-spec.md`](docs/plans/2026-07-09-utc-doc-health-category-spec.md) |
| 2026-07-31 | Emoji proposal(s), 2026 submission window closes | [Emoji Submission Form](https://forms.gle/6KSiYHrUdBkTMNaB8). Spec: [`docs/plans/2026-07-09-microsoft-health-emoji-proposal.md`](docs/plans/2026-07-09-microsoft-health-emoji-proposal.md) |
| 2026-11-30 | Unicode notifies all submitters of status | — |

The immediate Microsoft ask is the internal process and product route, not the optional category document.
See [`docs/strategy/2026-07-13-microsoft-medical-emoji-decision-brief.md`](docs/strategy/2026-07-13-microsoft-medical-emoji-decision-brief.md).

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
6. **Draft the Open-ended answer first.** Do not argue that Unicode should encode a complete organ or
   medical set. Every concept must stand on independent evidence.

Never write "the heart and lungs were encoded, so the kidney should be." That is the textbook Faulty
Comparison, and it is how a medical-importance argument tends to phrase itself.

Our own record: [`docs/proposals/archive-2019-published/`](docs/proposals/archive-2019-published/) holds the
two proposals that won. [`docs/proposals/archive-2020-emojination-drafts/`](docs/proposals/archive-2020-emojination-drafts/)
holds the fifteen that never reached Unicode's document register at all.

Medical Emoji is a campaign and proposal workspace for adding high-utility medical emoji to the Unicode Standard.

This repository contains the public website, prior support materials, current Unicode research notes, and proposal planning files for the medical emoji concepts the project has pursued.

Last status check: 2026-07-10

## Current Submission Link

Current three-concept release:
https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.5.0

Prior re-eligible portfolio release and CT Scan fallback:
https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.3.0

The current release contains full drafts for Ultrasound, Maze, and First Aid Kit. Maze now uses a mouse-maze
paradigm. All three have original artwork and a fresh Google Books comparison; all remain evidence-gated until
four fresh Google screenshots are captured. Reproducible Bing Web, Video, and Image supplements are archived
for all three, but are deliberately separated from the missing Google categories. Ultrasound is the
conditional Microsoft lead, and the complete CT Scan packet in `v1.3.0` is the filing-ready fallback. See
[`submissions/v1.5.0/MANIFEST.md`](submissions/v1.5.0/MANIFEST.md).

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

- Last update: `2026-05-20`.
- Current intake window: accepting submissions until `2026-07-31`.
- Declined emoji are not eligible for re-review within the last four years.
- The page body still contains some stale 2025 text, so date-sensitive submissions should be verified with Unicode/ESR before filing.

Important practical note: the three private decline notices for Kidney, Stomach, and Liver are dated
`2022-11-04`. Four elapsed years have not passed by `2026-07-31`, so this workspace treats the three organs
as ineligible for the current intake. Their completed `v1.2.0` packets remain future assets. Ten concepts are
clearly re-eligible now: the nine in `submissions/v1.3.0/` plus Maze in `submissions/v1.5.0/`. Ultrasound and
First Aid Kit have no matching public status rows and are treated as first-time public-sheet concepts.

## Emoji Submission Status

The table below combines active candidates from `src/data/emoji.ts`, legacy proposal assets, and the current
proposal workspaces. Status rows are from Unicode's live public proposal-status CSV, checked 2026-07-10.

| Concept | Repo source | Unicode public status rows | Latest public status | Last public date submitted | Reeligible by submitted-date clock | Next step |
| --- | --- | --- | --- | --- | --- | --- |
| Kidney / Kidneys | Active site candidate | `Kidney` declined 2019-12-17; `KIDNEYS` declined 2022-07-19; private decline notice 2022-11-04 | Declined | 2022 | After 2026-11-04 | Preserve `submissions/v1.2.0/`; do not file in the intake closing 2026-07-31. |
| Liver | Active site candidate | `Liver` declined 2020-12-18; `Liver` declined 2022-07-30; private decline notice 2022-11-04 | Declined | 2022 | After 2026-11-04 | Preserve `submissions/v1.2.0/`; do not file in the intake closing 2026-07-31. |
| Stomach | Active site candidate | `Stomach` declined 2020-10-27; `Stomach` declined 2022-07-28; private decline notice 2022-11-04 | Declined | 2022 | After 2026-11-04 | Preserve `submissions/v1.2.0/`; do not file in the intake closing 2026-07-31. |
| Spine | Active site candidate | `Spine` declined 2020-10-27; `Spine` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms a materially different concept is eligible. |
| Intestines | Active site candidate | `Intestines` declined 2020-12-18; `Intestines` declined 2024-04-04 | Declined | 2024-04-04 | 2028-04-04 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| ECG / EKG | Active site candidate | `ECG` declined 2020-12-18; `ECG` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| White Blood Cell | Active site candidate | `White Blood Cell` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete in `submissions/v1.3.0/`; replace Trends evidence. |
| Blood Bag | Active site candidate | `Blood bag` declined 2017-05-16; `Blood Bag (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Complete fallback packet in `submissions/v1.3.0/`. |
| Pill Pack | Active site candidate | `Pill Pack` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; hold behind Pill Box and finish Trends only if advanced. |
| Weight Scale | Active site candidate | `Bathroom Scale` expired 2018-02-27; `Weight Scale (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Challenger draft complete; add two Trends captures. |
| Leg Cast | Legacy proposal asset | `Leg Cast` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; replace Trends and resolve skin-tone behavior. |
| IV Bag | Legacy proposal asset | `IV Bag` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; add Trends and hold behind Blood Bag. |
| CT Scan | Legacy proposal asset | `CT Scan` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Lead complete packet in `submissions/v1.3.0/`. |
| Pill Box | Legacy proposal asset | `Pill Box` declined 2020-10-27 | Declined | 2020-10-27 | 2024-10-27 | Complete packet; hold because of Pill/Pill Pack overlap. |
| Inhaler | Public 2018 proposal | `Inhaler` declined 2018-07-03 | Declined | 2018-07-03 | 2022-07-03 | Draft complete; add Google Video and global `elephant` Trends evidence. |
| Maze | Public 2018 and 2020 rows | `Maze` declined 2018-04-12; `Maze` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Full mouse-maze draft in `v1.5.0`; capture Search, Video, and both Trends categories. |
| Ultrasound / Sonogram | New proposal workspace | No matching public status row found | No public row | — | No public resubmission bar identified | Conditional lead in `v1.5.0`; capture four missing Google categories and complete Microsoft design review. |
| First Aid Kit | New proposal workspace | No matching `First Aid Kit` row; distinct `First Aid Ointment` expired 2017-11-30 | No matching public row | — | No public resubmission bar identified | Full `v1.5.0` draft; hold unless current evidence overcomes low Ngram and substitute risk. |

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

If Google is unavailable or inaccessible in the capture region, Unicode permits another search engine that
displays real data only when the alternative is publicly available, reproducible, and comparable in quality.
The tested browser and Bing-supplement workflows are documented in
[`docs/research/2026-07-10-playwright-google-evidence-capture.md`](docs/research/2026-07-10-playwright-google-evidence-capture.md).

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

Current planned submission packet:
`submissions/v1.1.0/`

Key files:

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
- `submissions/v1.1.0/manifest.md`
- `submissions/v1.1.0/v1.1.0_kidney_emoji_proposal_SUBMIT.md`
- `submissions/v1.1.0/v1.1.0_submission_finalization_SIGNATURE_REQUIRED.md`
- `submissions/v1.1.0/images/v1.1.0_kidney_color_18x18_SUBMIT.png`
- `submissions/v1.1.0/images/v1.1.0_kidney_color_72x72_SUBMIT.png`
- `submissions/v1.1.0/images/v1.1.0_kidney_bw_18x18_SUBMIT.png`
- `submissions/v1.1.0/images/v1.1.0_kidney_bw_72x72_SUBMIT.png`
- `submissions/v1.1.0/images/v1.1.0_kidney_bw_generated_SOURCE_REFERENCE_ONLY.png`
- `submissions/v1.1.0/evidence/visual-review/v1.1.0_18x18_visual_review_board_SUBMIT.png`
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
