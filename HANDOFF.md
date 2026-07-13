# Handoff: Unicode medical emoji, state as of 2026-07-13

Read this first. Then read the current
[`David Rhew send manifest`](docs/outreach/2026-07-13-david-rhew-send-manifest.md),
[`email body`](docs/outreach/2026-07-13-david-rhew-send-email.txt),
[`submission-options packet`](output/pdf/2026-07-13-medical-emoji-submission-options-packet.pdf),
and [`role map`](output/pdf/2026-07-13-who-can-help-with-medical-emoji-review.pdf).
The v7 deck and separate decision/technical guides remain source material; the v6 and earlier decks are
archive/research material. None is an additional attachment in the current three-file send package.

**The pitch, in one line.** Shuhan plans to file CT Scan and Blood Bag after revision, with Pill Box as the
first alternate, and asks Microsoft two separate questions: after submission, would its Unicode representatives
ask ESR to consider an upcoming agenda discussion through its normal review process; and would its standards
team help revise the health-coverage discussion draft if the question merits UTC review?

## The situation in six sentences

David Rhew, Global Chief Medical Officer at Microsoft, has agreed to help. Shuhan will file the emoji
proposals himself, as an individual, because the submission form requires it. Fourteen medical concepts were
declined between 2019 and 2024. Their concept/status rows appear in Unicode's public sheet, but their full
proposal PDFs do not appear as numbered Unicode documents because a proposal only receives a document number
once the Emoji Standard and Research Working Group advances it. Anatomical Heart and Lungs succeeded in 2019;
the official proposals name Christian Kamkoff, Shuhan He, and Melissa Thermidor.
The 2026 submission window closes **2026-07-31**.

## Deadlines

| Due | What |
|---|---|
| 2026-07-21 | UTC document, if filed. Seven days before UTC #188 (Redmond, July 28-30) |
| **2026-07-31** | **Emoji submission window closes** |
| 2026-11-30 | Unicode notifies all submitters |

## The five things that decide this

1. **Eligibility and portfolio risk.** The decisive private notices show Kidney, Stomach, and Liver were each
   declined on **2022-11-04**. Four elapsed years have not passed by the intake deadline of **2026-07-31**.
   Treat all three as ineligible for this round. Preserve their working `submissions/v1.7.0/` packets as
   future assets; do not consume Microsoft's July review window on them.

   Ten portfolio concepts are clearly re-eligible now: CT Scan, Blood Bag, Pill Box, Weight Scale, White
   Blood Cell, Inhaler, IV Bag, Leg Cast, Pill Pack, and Maze. Their last public submissions were in 2018 or
   2020. Releases `submissions/v1.3.0/` and `submissions/v1.5.0/` contain independent drafts, original CC0
   artwork, recovered evidence, and filing-readiness manifests. Ultrasound and First Aid Kit have no matching
   public status rows and are treated as first-time public-sheet concepts.

   The current filing plan is CT Scan and Blood Bag, with Pill Box as the medication alternate. All three
   contain the five evidence categories, but their 2020 captures, current-method queries, factor labels,
   metadata, and ownership language require revision before filing. Ultrasound and Weight Scale remain
   promising alternatives with missing evidence. The external packet shows all twelve current-cycle concepts
   instead of treating Ultrasound and CT Scan as the only options.
   Maze now uses a mouse navigating broad corridors, strengthening the learning, memory, decision-making, and
   behavioral-research uses while retaining the general `Maze` name.

   The portfolio evidence still matters. First-time proposals advance 16% of the time; resubmissions advance
   5%. Eligibility is permission to be reviewed, not a reason to file all ten.

2. **The screening gate.** All fourteen died inside the ESR working group. Its membership is not published
   and cannot be discovered from outside. Whether Microsoft sits there is the highest-leverage question in
   the project, and only Vishal Chowdhary (Microsoft's board director) or Peter Constable can answer it.

3. **Vendor support.** Unicode's FAQ names two reasons a *well-formed* proposal is declined: lack of
   evidence for popularity, and **"lack of anticipated support by major vendors."** Microsoft ships Segoe UI
   Emoji. No proposal in the corpus of 55 winners and 29 losers has ever carried a vendor commitment. This is
   the thing Microsoft has that Shuhan does not.

4. **Craft.** Winners are 907 words and 26 images. Losers are 1,485 words and 18 images, with the same
   section headings. Use [`docs/proposals/TEMPLATE-emoji-proposal.md`](docs/proposals/TEMPLATE-emoji-proposal.md).
   Never write cause language, never cite petitions or social media, and draft the Open-ended answer first.

5. **Open-endedness.** Do not frame the work as a complete organ or medical-symbol set. The current releases
   contain twelve independent current-cycle proposals. CT Scan and Blood Bag are the current filing choices;
   Pill Box is the first alternate. Every proposal must stand on its own frequency, distinctiveness, multiple
   meanings, and lack of a substitute.

## What is written and ready

| Artifact | Path | Status |
|---|---|---|
| Emoji proposal template | `docs/proposals/TEMPLATE-emoji-proposal.md` | Ready to fill |
| Winners vs losers evidence | `docs/plans/2026-07-09-winners-vs-losers.md` | Done |
| 55 winning proposals, archived | `docs/proposals/reference-winners-2020-2024/` | Done |
| Our 2 winning proposals (2019) | `docs/proposals/archive-2019-published/` | Done |
| Our 15 declined drafts (2020-21) | `docs/proposals/archive-2020-emojination-drafts/` | Done |
| 6 precedent UTC documents | `docs/proposals/reference-utc-documents/` | Done |
| Unicode org chart and strategy | `docs/strategy/unicode-map-and-strategy.md` | Done |
| What Microsoft can do | `docs/strategy/what-microsoft-can-do.md` | Done |
| UTC discussion document | `docs/proposals/utc-health-category/health-coverage-maintenance-l2-review-draft.md`, `.docx`, and `.pdf` | External review draft, **not sent** |
| Microsoft review deck | `docs/presentations/2026-07-09-microsoft-brief/Emoji-2026-External-Review-v7.pptx` and `output/pdf/2026-07-12-microsoft-medical-emoji-review-deck.pdf` | Current 9-slide external review copy |
| Rhew three-attachment package | `docs/outreach/2026-07-13-david-rhew-send-manifest.md` | Prepared and verified; **not sent** |
| Consolidated proposal options | `output/pdf/2026-07-13-medical-emoji-submission-options-packet.pdf` | 90-page bookmarked packet with all 15 working proposals |
| Microsoft-Unicode role map | `output/pdf/2026-07-13-who-can-help-with-medical-emoji-review.pdf` | One-page external routing guide |
| Three organ submission packets | `submissions/v1.7.0/` | Redesigned review PDFs; eligibility confirmation remains; Stomach/Liver evidence is stale; Liver Trends is U.S.-only |
| Nine clearly re-eligible packets | `submissions/v1.3.0/` | Three working packets contain all five evidence categories but require revision; six additional drafts are evidence-gated |
| Three additional packets | `submissions/v1.5.0/` | Ultrasound, mouse-maze, and First Aid Kit full drafts; reproducible Bing supplements present; four Google captures still missing for each |
| Microsoft decision brief | `docs/strategy/2026-07-12-microsoft-medical-emoji-decision-brief.md`, `output/doc/2026-07-12-microsoft-medical-emoji-decision-brief.docx`, and `output/pdf/2026-07-12-microsoft-medical-emoji-decision-brief.pdf` | Current review copy |
| Technical and rights questions | `docs/strategy/2026-07-12-microsoft-medical-emoji-product-legal-clearance.md`, `output/doc/2026-07-12-microsoft-medical-emoji-product-legal-clearance.docx`, and `output/pdf/2026-07-12-microsoft-medical-emoji-product-legal-clearance.pdf` | Current non-binding review copy |
| CT Scan working proposal | `submissions/v1.3.0/ct-scan/ct-scan_emoji_proposal_SUBMIT.pdf` | Revise before filing |
| Blood Bag working proposal | `submissions/v1.3.0/blood-bag/blood-bag_emoji_proposal_SUBMIT.pdf` | Revise before filing |
| Pill Box working proposal | `submissions/v1.3.0/pill-box/pill-box_emoji_proposal_SUBMIT.pdf` | First alternate; revise before filing |
| Rhew packet email | `docs/outreach/2026-07-13-david-rhew-send-email.txt` | Current three-attachment email body |
| Expanded-slate ranking | `docs/strategy/2026-07-10-expanded-proposal-ranking.md` | Archive/research only; do not send |
| Reproducible census script | `evidence/emoji_group_census.py` | Done |
| What to file, and the pitch | `docs/strategy/2026-07-09-what-to-file.md` | Archive/research only; do not send |
| Resubmission / clock analysis | `evidence/resubmission_analysis.py` | Done |

## The open strategic question

The discussion draft is now a separate review request. It asks whether ESR should examine health-related
coverage, discoverability, and recurring review questions. It does not request a top-level Health group or
encode a slate. Microsoft can review the draft without making it the condition for the individual filings.

## Things that are true and surprising

- Unicode's **UTC chair, Peter Constable, is a Microsoft employee of 23 years.** He chairs on behalf of the
  Consortium, not Microsoft. Ask him about process, never about outcome.
- Only about **4.5 voting members** attend the UTC regularly: Adobe, Apple, Google, Microsoft, UCB.
- Microsoft filed an emoji data proposal in 2016, `L2/16-228`, opening *"Microsoft would like to see…"*.
  Its lead author was Constable.
- Charlotte Buff, a private individual with a Gmail address, has documents discussed by name in UTC minutes.
  One of hers was remanded, then rewritten by others, and adopted. **A remand is not a rejection.**
- Every medical emoji in the standard was filed by Emojination or people in its orbit, including both of
  Shuhan's. But individuals win alone routinely, including `L2/20-214` **X-ray**, a medical emoji filed by
  two individuals in the same window as our fifteen drafts. **Craft, not letterhead.**
- Our own kidney draft asked for `Sort Order: in the BODY PARTS category`. We requested the classification we
  now want changed.
- The kidney's keywords were `Kidney`. The rule is *"Do not repeat the name of the emoji."*

## Claims that must never be repeated as fact

- Individual UTC delegates and ESR membership are **not published anywhere**. Do not name them.
- Do not assert Microsoft hosts UTC #188. The register lists Redmond and names no host.
- Do not claim Microsoft has never proposed an emoji. Not found is not the same as does not exist.
- Do not cite "X% of winners used source Y" as a compliance rate. Those counts read the PDF text layer, and
  the evidence is screenshots.

## Immediate next actions

1. Review and send the exact three-file Rhew package in
   `docs/outreach/2026-07-13-david-rhew-send-manifest.md`. Do not add the v7 deck, separate decision brief,
   technical and rights guide, older organ releases, or any document that names unapproved Microsoft authors.
2. Refresh CT Scan and Blood Bag evidence using the current Unicode query method; update factor labels,
   ownership warranties, citations, and PDF metadata. Apply the same work to Pill Box only if it remains in scope.
3. Ask Microsoft reviewers to compare CT Scan with X-Ray/MRI, Blood Bag with IV Bag, and Pill Box with Pill at
   18x18 and in black and white.
4. After submitting through the official form, ask whether Microsoft's Unicode standards representatives would
   ask ESR to consider an upcoming agenda discussion through its normal review process. Unicode controls timing and outcome.
5. Ask Microsoft's standards team to review the health-coverage discussion draft and, if the question merits
   UTC review, help revise it for submission. Microsoft may submit, coauthor, or use it as source material.
6. File the selected proposal PDFs by 2026-07-31; keep the organ packets for a later eligible round unless
   Unicode confirms a different eligibility interpretation.

Current organ gates are explicit: Unicode must confirm eligibility; Stomach and Liver need fresh evidence;
Liver needs Worldwide rather than United States-only Trends; and this network cannot complete the refresh
because Google Trends returns HTTP 429 while Google Search presents a CAPTCHA.
