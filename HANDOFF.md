# Handoff: Unicode medical emoji, state as of 2026-07-09

Read this first. Then read [`docs/strategy/2026-07-09-what-to-file.md`](docs/strategy/2026-07-09-what-to-file.md),
[`docs/strategy/what-microsoft-can-do.md`](docs/strategy/what-microsoft-can-do.md) and
[`docs/strategy/unicode-map-and-strategy.md`](docs/strategy/unicode-map-and-strategy.md). Everything else is
supporting evidence.

**The pitch, in one line.** Not *"help us relitigate the kidney"*, but *"help us land the first medical emoji
that Microsoft commits to ship."* Unicode declines a well-formed proposal for two reasons: weak popularity
evidence, and *"lack of anticipated support by major vendors."* Microsoft can answer the second, and no emoji
proposal in Unicode's history ever has.

## The situation in six sentences

David Rhew, Global Chief Medical Officer at Microsoft, has agreed to help. Shuhan will file the emoji
proposals himself, as an individual, because the submission form requires it. Fourteen medical concepts were
declined between 2019 and 2024, and **none of them appears anywhere in Unicode's public record**, because a
proposal only receives a document number once the Emoji Standard and Research Working Group advances it. So
they died at screening, invisibly. Two proposals succeeded, in 2019, both filed under Emojination's name.
The 2026 submission window closes **2026-07-31**.

## Deadlines

| Due | What |
|---|---|
| 2026-07-21 | UTC document, if filed. Seven days before UTC #188 (Redmond, July 28-30) |
| **2026-07-31** | **Emoji submission window closes** |
| 2026-11-30 | Unicode notifies all submitters |

## The five things that decide this

1. **Eligibility, and why it is the wrong thing to obsess over.** Unicode bars a declined emoji from
   re-review for four years. **Which date starts the clock is genuinely unknown.** All three published
   phrasings anchor on the decline (*"emoji declined within the last four years"*), and no source anchors on
   the submission, but Unicode never states it. Do not claim to know.

   I tested it. Run `python evidence/resubmission_analysis.py`. **The evidence leans toward the submission
   clock, and does not establish it.**

   Six resubmissions ever advanced. Count how many each model has to explain away as an anomaly:

   | Concept | Gap | Submission clock | Decline clock |
   |---|---|---|---|
   | Hand heart | 1.17y | barred | barred |
   | Phoenix | 0.48y | barred | barred |
   | Pink heart | 2.00y | barred by 1 day | barred |
   | Lime | 2.32y | eligible | barred |
   | Raspberry | 2.09y | eligible | barred |
   | Treasure chest | 5.79y | eligible | eligible |

   Under the submission clock, 3 of 6 advances are violations. Under the decline clock, 5 of 6 are. Fewer
   anomalies favours the submission clock.

   **But the bar is demonstrably not enforced mechanically under either reading.** Phoenix was resubmitted
   six months after a decline and released. Once discretion is proven, anomaly-counting stops being
   decisive. Note also that two of the three both-barred advances were subcommittee insiders: Pink Heart by
   Jennifer Daniel, chair of ESR, and Phoenix by Jennifer 8. Lee / ESC. The third, Hand Heart, was an
   outsider.

   Only Unicode can answer this. A drafted, unsent email asking exactly that is in
   `docs/proposals/kidney-emoji-2026/decline-date-submission-update.md`.

   **What the data does settle is about us.** Five of the fourteen concepts were resubmitted *while barred*,
   even under the generous submission clock:

   | Concept | Prior | Resubmitted | Gap | Bar then |
   |---|---|---|---|---|
   | Liver | 2020-12-18 | 2022-07-30 | 1.61y | 2y |
   | Stomach | 2020-10-27 | 2022-07-28 | 1.75y | 2y |
   | Intestines | 2020-12-18 | 2024-04-04 | 3.29y | 4y |
   | ECG | 2020-12-18 | 2024-04-05 | 3.30y | 4y |
   | Spine | 2020-10-27 | 2024-04-05 | 3.44y | 4y |

   They were never going to be reviewed. **Five of the "fourteen rejections" were ineligible filings, not
   verdicts on medical emoji.**

   **And resubmission is a losing move regardless.** First-time proposals advance 16% of the time.
   Resubmissions advance **5%**. Of 53 resubmissions filed inside the bar, 50 were declined. Of the three
   that ever beat the bar, two were subcommittee insiders: Pink Heart by Jennifer Daniel, chair of ESR, and
   Phoenix by Jennifer 8. Lee / ESC.

   **So the play is not the kidney.** A never-before-proposed medical concept carries no bar, no history,
   and three times the odds. Nothing in the status sheet has ever been submitted for: hospital bed, insulin
   pen, glucose meter, nebulizer, oxygen mask, walker, ice pack. Pair one of those with Microsoft's vendor
   commitment, which answers a named decline reason and which **no proposal in the corpus has ever carried**,
   and it is the strongest filing this project has ever made.

   Note also, from the status page: *"Auto-declined proposals are not included in this list."* All fourteen
   of ours are listed, so a human saw them. But the five above were barred on arrival.

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

5. **Open-endedness.** Filing fourteen organ and device proposals at once *is* the answer to Unicode's
   Open-ended exclusion factor, and the answer is yes. File one.

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
| UTC document (Health category) | `docs/proposals/utc-health-category/` | Drafted, **not sent** |
| Microsoft brief deck | `docs/presentations/2026-07-09-microsoft-brief/` | 11 slides |
| Reproducible census script | `evidence/emoji_group_census.py` | Done |
| What to file, and the pitch | `docs/strategy/2026-07-09-what-to-file.md` | **Decision needed** |
| Resubmission / clock analysis | `evidence/resubmission_analysis.py` | Done |

## The open strategic question

The Health category document is drafted but **should probably not be Microsoft's first ask.** Grouping is
presentation; Unicode's own data file calls the groups *"illustrative"*; no selection factor mentions the
category. It cannot approve an emoji. Recommended order is in
[`docs/strategy/what-microsoft-can-do.md`](docs/strategy/what-microsoft-can-do.md).

If a structural document is filed, the smaller and more defensible ask is to move the anatomical heart,
lungs and brain from `body-parts` into `medical`, citing `L2/19-190R`, in which the Emoji Subcommittee
itself made that classification because no better destination existed.

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

1. Stop trying to resubmit the kidney. File a never-proposed concept instead: **hospital bed** or **blood
   pressure cuff** are the lead candidates. No bar, no history, 3x the odds. See
   [`docs/strategy/2026-07-09-what-to-file.md`](docs/strategy/2026-07-09-what-to-file.md).
2. Email Chowdhary: who is Microsoft's UTC delegate, and does Microsoft sit on ESR?
3. Get Microsoft to commit, in writing, to implementing in Segoe UI Emoji.
4. Get Microsoft design to originate textless artwork with a clean licence.
5. File **one** emoji, to the template.
