# Handoff: Unicode medical emoji, state as of 2026-07-09

Read this first. Then read [`docs/strategy/unicode-map-and-strategy.md`](docs/strategy/unicode-map-and-strategy.md)
and [`docs/strategy/what-microsoft-can-do.md`](docs/strategy/what-microsoft-can-do.md). Everything else is
supporting evidence.

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

1. **Eligibility.** Unicode bars a declined emoji from re-review for **four years, counted from the
   decline**, not the submission.

   Do **not** go hunting for the decline email. It is unnecessary, and it may not exist in any findable
   form. Unicode publishes no sender, no template, and says *"we are unable to respond to inquiries
   regarding the status of your proposal."*

   The decline date is already bounded by published facts. Kidney was submitted 2022-07-19. The 2022 window
   closed 2022-07-31, so review followed. Submitters are notified *"no later than November 30."* The status
   sheet *"is updated once per year, usually in early December."* **Therefore the decline fell between
   August and December 2022, and four years later falls between August and December 2026. Every possible
   value is after 2026-07-31.**

   So under the decline clock, kidney, stomach and liver are barred for this window, provably. Under a
   submission clock they clear by 12, 3 and 1 day. **The only open question is which date Unicode counts
   from, and only Unicode can answer it.** A drafted, unsent email asking exactly that is in
   `docs/proposals/kidney-emoji-2026/decline-date-submission-update.md`.

   The 2020-cohort concepts (white blood cell, blood bag, IV bag, CT scan, pill pack, pill box, leg cast,
   weight scale) were declined in the 2020 or 2021 cycle, so they clear under **either** clock. If the goal
   is to file something this window without an eligibility fight, file one of those.

   Note also, from the status page: *"Auto-declined proposals are not included in this list."* All fourteen
   of ours are listed. They were reviewed by a human and declined on the merits, not rejected on a
   technicality.

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

1. Decide the eligibility question. Either ask Unicode which date starts the four-year clock, or sidestep it
   by filing a 2020-cohort concept that clears under either reading. Do not hunt for the decline email.
2. Email Chowdhary: who is Microsoft's UTC delegate, and does Microsoft sit on ESR?
3. Get Microsoft to commit, in writing, to implementing in Segoe UI Emoji.
4. Get Microsoft design to originate textless artwork with a clean licence.
5. File **one** emoji, to the template.
