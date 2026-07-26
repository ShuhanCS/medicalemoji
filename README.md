# Medical Emoji

## Current 2026 submission slate

The active 2026 filing slate is Kidney, White Blood Cell, Stomach, and Liver, reviewed serially in that order.
Pill Pack is a provisional fifth workstream and must pass a go/no-go review before joining the filing slate.
Shuhan He has confirmed the three organs are eligible, and White Blood Cell is outside the four-year
resubmission bar after its 2020 decline. Eligibility is settled for those four; submission quality is not. The
proposals must be corrected one at a time before filing:

- Best-in-class specification: [`docs/proposals/emoji-proposal-approval-rubric.md`](docs/proposals/emoji-proposal-approval-rubric.md)
- Serial slate, semver, and agent handoff spec: [`docs/proposals/2026-submission-slate-spec.md`](docs/proposals/2026-submission-slate-spec.md)
- Standalone parallel agent specs: [`docs/proposals/agent-specs/`](docs/proposals/agent-specs/)
- Organ-by-organ audit: [`docs/proposals/2026-organ-submission-audit.md`](docs/proposals/2026-organ-submission-audit.md)
- Current complete versioned package: [`submissions/v1.11.0/`](submissions/v1.11.0/)
- Historical organ baseline: [`submissions/v1.7.0/`](submissions/v1.7.0/)
- Historical White Blood Cell baseline: [`submissions/v1.3.0/white-blood-cell/`](submissions/v1.3.0/white-blood-cell/)

Submission packages are immutable semver snapshots. Every update creates a new complete version folder; files
that did not change are copied forward byte for byte. The next substantive proposal revision will be v1.12.0.

Stomach `v1.11.0` replaces the compact prior glyph with a project-authored long-inlet, deep-concavity,
distinct-outlet vector paradigm. Its proposal PDF is rebuilt and visually verified; the proposal remains
revision-required until four historical 2020 evidence captures and the recognition/comparator gates are
completed.

Authorship is fixed for the filing slate: Kidney uses the complete consenting ten-person author list in v1.10.0, adding
David Rhew and Heena Purohit to the eight previously listed submitters; White Blood Cell, Stomach, and Liver
list only Shuhan He. The provisional Pill Pack brief also starts with Shuhan He only and requires
reconfirmation before revision. The 2026 submission window closes at the end of day on 2026-07-31.

## ⏳ Deadlines

| Due | What | Where |
|---|---|---|
| 2026-07-21 | Final UTC discussion paper, after David Rhew and Heena Purohit confirm the text and authorship and Microsoft's current delegate confirms the submission route; not on the emoji-proposal critical path | [`health-related-emoji-coverage-l2-submission.pdf`](docs/proposals/utc-health-category/health-related-emoji-coverage-l2-submission.pdf) |
| 2026-07-31 | Emoji proposal(s), 2026 submission window closes | [Emoji Submission Form](https://forms.gle/6KSiYHrUdBkTMNaB8). Spec: [`docs/plans/2026-07-09-microsoft-health-emoji-proposal.md`](docs/plans/2026-07-09-microsoft-health-emoji-proposal.md) |
| 2026-11-30 | Unicode notifies all submitters of status | — |

The current David Rhew send package is written for an external audience and contains exactly three
attachments. It separates the individual emoji-proposal route from the optional UTC discussion-document
route and puts all 15 working concepts into one indexed options packet:

- [`output/pdf/2026-07-13-health-related-emoji-coverage-l2-submission.pdf`](output/pdf/2026-07-13-health-related-emoji-coverage-l2-submission.pdf)
- [`output/pdf/2026-07-13-medical-emoji-submission-options-packet.pdf`](output/pdf/2026-07-13-medical-emoji-submission-options-packet.pdf)
- [`output/pdf/2026-07-13-who-can-help-with-medical-emoji-review.pdf`](output/pdf/2026-07-13-who-can-help-with-medical-emoji-review.pdf)

Use the exact body and attachment list in the
[`David Rhew send manifest`](docs/outreach/2026-07-13-david-rhew-send-manifest.md). The separate v7 review
deck, decision brief, and technical and rights guide remain useful source material but are not additional
attachments in this send package.

## 🏆 What actually wins

Use the current [`best-in-class specification`](docs/proposals/emoji-proposal-approval-rubric.md) as the
controlling project standard and the [`proposal template`](docs/proposals/TEMPLATE-emoji-proposal.md) as the
drafting structure. The specification incorporates the current Unicode rules and a direct
[`proposal evidence audit`](docs/research/unicode-winning-submissions/analysis.md) of accepted and confirmed
declined proposal documents: their arguments, evidence, artwork, and layout. Lighthouse is the closest current
all-around model; Treasure Chest is the concise model; Fingerprint is the technical-evidence model; and Meteor
is the genuine-compatibility model. No accepted proposal should be copied wholesale.

The older 55-versus-29 comparison is retained only as a methodology warning because its negative cohort was
not preserved. It does not supply a validated approval formula or hard word, page, or image-count threshold.

Six current drafting rules:

1. **Meet every current requirement.** Older accepted proposals do not override the 2026 instructions.
2. **Structure is necessary, not sufficient.** All 15 confirmed declined Medical Emoji drafts answered every
   exclusion heading.
3. **Write `N/A` when instructed.** Especially for Completeness and Compatibility when there is no compelling
   example.
4. **No petitions, calls for an emoji, or `Frequently Requested` evidence.** Current Unicode instructions say
   they are unacceptable.
5. **Do not make a cause the justification.** Importance, awareness, and stigma cannot replace expected-use
   evidence.
6. **Draft the Open-ended answer first.** Kidney, Liver, and Stomach may be filed as three one-emoji proposals,
   but each must stand independently and must not argue for completing an anatomy set.

Never write "the heart and lungs were encoded, so the kidney should be." That is the textbook Faulty
Comparison, and it is how a medical-importance argument tends to phrase itself.

Our own record: [`docs/proposals/archive-2019-published/`](docs/proposals/archive-2019-published/) holds the
two proposals that won. [`docs/proposals/archive-2020-emojination-drafts/`](docs/proposals/archive-2020-emojination-drafts/)
holds the fifteen that never reached Unicode's document register at all.

Medical Emoji is a campaign and proposal workspace for adding high-utility medical emoji to the Unicode Standard.

This repository contains the public website, prior support materials, current Unicode research notes, and proposal planning files for the medical emoji concepts the project has pursued.

Last status check: 2026-07-13

## Current Proposal Releases

Current filing-candidate source for CT Scan, Blood Bag, and Pill Box, all requiring revision before filing:
https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.3.0

Additional evidence-gated drafts for Ultrasound, Maze, and First Aid Kit:
https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.5.0

Latest Kidney, Stomach, and Liver review release, confirmed eligible and pending evidence and small-size design clearance:
https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.7.0

The `v1.7.0` release contains redesigned Kidney, Stomach, and Liver artwork and revised proposal PDFs with
all five required frequency screenshots embedded in each PDF. It is a review release, not authority to file:
Shuhan has confirmed eligibility, while Stomach and Liver still rely on historical 2020 Search, Video, and
Trends captures and Liver's Trends screenshots are United States-only. A 2026-07-12 refresh attempt was
blocked by Google Trends HTTP 429 and a Google Search CAPTCHA. See
[`submissions/v1.7.0/manifest.md`](submissions/v1.7.0/manifest.md).

The `v1.5.0` release contains full drafts for Ultrasound, Maze, and First Aid Kit. Maze now uses a mouse-maze
paradigm. All three have original artwork and a fresh Google Books comparison; all remain evidence-gated until
four fresh Google screenshots are captured. Reproducible Bing Web, Video, and Image supplements are archived
for all three, but are deliberately separated from the missing Google categories. Ultrasound remains a
promising alternative, not a filing-ready proposal. The external Microsoft packet compares it with CT Scan,
Blood Bag, Pill Box, Weight Scale, and the rest of the available slate. See
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
`2022-11-04`, so the ordinary four-year date calculation would extend past this intake. Shuhan He has confirmed
that Unicode considers all three eligible for the 2026 cycle. The project therefore treats them as eligible and
will preserve the written confirmation in the filing record. Ten other concepts are clearly re-eligible now:
the nine in `submissions/v1.3.0/` plus Maze in `submissions/v1.5.0/`. Ultrasound and First Aid Kit have no
matching public status rows and are treated as first-time public-sheet concepts.

## Emoji Submission Status

The table below combines active candidates from `src/data/emoji.ts`, legacy proposal assets, and the current
proposal workspaces. Status rows are from Unicode's live public proposal-status CSV, checked 2026-07-10.

| Concept | Repo source | Unicode public status rows | Latest public status | Last public date submitted | Reeligible by submitted-date clock | Next step |
| --- | --- | --- | --- | --- | --- | --- |
| Kidney / Kidneys | Active site candidate | `Kidney` declined 2019-12-17; `KIDNEYS` declined 2022-07-19; private decline notice 2022-11-04 | Confirmed eligible for 2026 | 2022 | After 2026-11-04 by date alone; separately confirmed eligible | Working candidate in `submissions/v1.7.0/`; add the full author list, improve small-size recognition, refresh evidence, and archive the eligibility confirmation. |
| Liver | Active site candidate | `Liver` declined 2020-12-18; `Liver` declined 2022-07-30; private decline notice 2022-11-04 | Confirmed eligible for 2026 | 2022 | After 2026-11-04 by date alone; separately confirmed eligible | Working candidate in `submissions/v1.7.0/`; improve small-size recognition, replace stale 2020 evidence including U.S.-only Trends captures, and archive the eligibility confirmation. |
| Stomach | Active site candidate | `Stomach` declined 2020-10-27; `Stomach` declined 2022-07-28; private decline notice 2022-11-04 | Confirmed eligible for 2026 | 2022 | After 2026-11-04 by date alone; separately confirmed eligible | Working candidate in `submissions/v1.7.0/`; replace stale 2020 Search, Video, and Trends evidence and archive the eligibility confirmation. |
| Spine | Active site candidate | `Spine` declined 2020-10-27; `Spine` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms a materially different concept is eligible. |
| Intestines | Active site candidate | `Intestines` declined 2020-12-18; `Intestines` declined 2024-04-04 | Declined | 2024-04-04 | 2028-04-04 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| ECG / EKG | Active site candidate | `ECG` declined 2020-12-18; `ECG` declined 2024-04-05 | Declined | 2024-04-05 | 2028-04-05 | Do not resubmit before 2028 unless Unicode confirms eligibility. |
| White Blood Cell | Active 2026 slate | `White Blood Cell` declined 2020-12-18 | Reeligible; selected for 2026 review | 2020-12-18 | 2024-12-18 | Review first; refresh Search and Video, replace Web Trends, add Image Trends, and pass an 18x18 recognition test against Microbe and generic-cell imagery. |
| Blood Bag | Active site candidate | `Blood bag` declined 2017-05-16; `Blood Bag (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Current filing choice in `submissions/v1.3.0/`; refresh evidence, factor labels, metadata, citations, and ownership language before filing. |
| Pill Pack | Active site candidate | `Pill Pack` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; hold behind Pill Box and finish Trends only if advanced. |
| Weight Scale | Active site candidate | `Bathroom Scale` expired 2018-02-27; `Weight Scale (B)` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Challenger draft complete; add two Trends captures. |
| Leg Cast | Legacy proposal asset | `Leg Cast` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; replace Trends and resolve skin-tone behavior. |
| IV Bag | Legacy proposal asset | `IV Bag` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Draft complete; add Trends and hold behind Blood Bag. |
| CT Scan | Legacy proposal asset | `CT Scan` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Current filing choice in `submissions/v1.3.0/`; refresh 2020 evidence, current factor labels, metadata, and ownership language before filing. |
| Pill Box | Legacy proposal asset | `Pill Box` declined 2020-10-27 | Declined | 2020-10-27 | 2024-10-27 | First alternate in `submissions/v1.3.0/`; refresh evidence and ownership records, update metadata and factor labels, and improve 18-pixel recognition before filing. |
| Inhaler | Public 2018 proposal | `Inhaler` declined 2018-07-03 | Declined | 2018-07-03 | 2022-07-03 | Draft complete; add Google Video and global `elephant` Trends evidence. |
| Maze | Public 2018 and 2020 rows | `Maze` declined 2018-04-12; `Maze` declined 2020-12-18 | Declined | 2020-12-18 | 2024-12-18 | Full mouse-maze draft in `v1.5.0`; capture Search, Video, and both Trends categories. |
| Ultrasound / Sonogram | New proposal workspace | No matching public status row found | No public row | — | No public resubmission bar identified | Promising alternative in `v1.5.0`; capture four missing Google categories and complete small-size design review before any filing decision. |
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

Current design-reviewed organ packet:
`submissions/v1.7.0/`

Earlier synchronized packets remain in `submissions/` as release history. They are not the current review
copies and should not be attached to a new Microsoft or Unicode submission.

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
- `submissions/v1.7.0/manifest.md`
- `submissions/v1.7.0/kidney/kidney_emoji_proposal_SUBMIT.pdf`
- `submissions/v1.7.0/stomach/stomach_emoji_proposal_SUBMIT.pdf`
- `submissions/v1.7.0/liver/liver_emoji_proposal_SUBMIT.pdf`
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
