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

1. **Eligibility and portfolio risk.** The private notices were found: Kidney, Stomach, and Liver were each
   declined on **2022-11-04**. Unicode bars a declined emoji from re-review for four years, but **which date
   starts the clock and whether the rule is retroactive are genuinely unknown.** Do not claim to know.

   Run `python evidence/resubmission_analysis.py`. The evidence leans toward a submission-date clock but does
   not establish one. Six resubmissions ever advanced:

   | Concept | Gap | Submission clock | Decline clock |
   |---|---|---|---|
   | Hand heart | 1.17y | barred | barred |
   | Phoenix | 0.48y | barred | barred |
   | Pink heart | 2.00y | barred by 1 day | barred |
   | Lime | 2.32y | eligible | barred |
   | Raspberry | 2.09y | eligible | barred |
   | Treasure chest | 5.79y | eligible | eligible |

   Under the submission clock, 3 of 6 advances are anomalies; under the decline clock, 5 of 6 are. The bar
   is demonstrably not enforced mechanically under either reading: Phoenix advanced after six months.
   Only Unicode can give a controlling interpretation. The exact question and notice record are in
   [`docs/research/2022-organ-decline-notifications.md`](docs/research/2022-organ-decline-notifications.md).

   The portfolio evidence still matters. First-time proposals advance 16% of the time; resubmissions advance
   5%. A never-before-proposed medical concept therefore remains the higher-probability fallback described in
   [`docs/strategy/2026-07-09-what-to-file.md`](docs/strategy/2026-07-09-what-to-file.md).

   **User decision, 2026-07-09:** keep Kidney, Stomach, and Liver fully drafted and ready while the process
   question is answered. Release `submissions/v1.2.0/` does that. The first-time concept is a parallel
   portfolio option, not a reason to delete or downgrade the three requested organ packets.

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

5. **Open-endedness.** Do not frame the work as a complete organ or medical-symbol set. The 2026 release
   contains three separate proposals, each supported by its own frequency, distinctiveness, multiple uses,
   and lack of a substitute. Each proposal answers the Open-ended exclusion directly.

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
| Three organ submission packets | `submissions/v1.2.0/` | Final PDFs drafted; external filing preflight remains |
| Microsoft Monday decision brief | `output/doc/2026-07-13-microsoft-medical-emoji-decision-brief.docx` | Ready for Rhew/Chowdhary review |
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

1. Send Rhew the Monday decision brief and cover email in `docs/strategy/` and `output/`.
2. Ask Chowdhary who Microsoft's UTC delegate is, whether Microsoft sits on ESR, and which procedural
   channel should answer the four-year eligibility question.
3. Ask the responsible Windows/Segoe UI Emoji product owner to approve or narrow the anticipated
   implementation statement.
4. Ask Microsoft design and legal to review the CC0 proposal art and Unicode licensing route.
5. File Kidney, Stomach, and Liver separately by 2026-07-31 if the process interpretation permits them.
6. Keep a never-before-proposed concept available as the higher-probability fallback if the organ filings
   are ruled ineligible or Microsoft prefers a first-time candidate.
