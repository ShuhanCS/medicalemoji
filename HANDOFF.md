# Handoff: Unicode medical emoji, state as of 2026-07-10

Read this first. Then read [`docs/strategy/2026-07-09-what-to-file.md`](docs/strategy/2026-07-09-what-to-file.md),
[`docs/strategy/what-microsoft-can-do.md`](docs/strategy/what-microsoft-can-do.md) and
[`docs/strategy/unicode-map-and-strategy.md`](docs/strategy/unicode-map-and-strategy.md). Everything else is
supporting evidence.

**The pitch, in one line.** Not *"help us relitigate the kidney"*, but *"help us land the first medical emoji
that Microsoft commits to ship."* Unicode declines a well-formed proposal for two reasons: weak popularity
evidence, and *"lack of anticipated support by major vendors."* Microsoft can answer the second, and none of
the 84 winning and unsuccessful proposals in this project's reviewed corpus carried that commitment.

## The situation in six sentences

David Rhew, Global Chief Medical Officer at Microsoft, has agreed to help. Shuhan will file the emoji
proposals himself, as an individual, because the submission form requires it. Fourteen medical concepts were
declined between 2019 and 2024. Their concept/status rows appear in Unicode's public sheet, but their full
proposal PDFs do not appear as numbered Unicode documents because a proposal only receives a document number
once the Emoji Standard and Research Working Group advances it. Two proposals succeeded, in 2019, both filed
under Emojination's name.
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
   Treat all three as ineligible for this round. Preserve their complete `submissions/v1.2.0/` packets as
   future assets; do not consume Microsoft's July review window on them.

   Ten portfolio concepts are clearly re-eligible now: CT Scan, Blood Bag, Pill Box, Weight Scale, White
   Blood Cell, Inhaler, IV Bag, Leg Cast, Pill Pack, and Maze. Their last public submissions were in 2018 or
   2020. Releases `submissions/v1.3.0/` and `submissions/v1.5.0/` contain independent drafts, original CC0
   artwork, recovered evidence, and filing-readiness manifests. Ultrasound and First Aid Kit have no matching
   public status rows and are treated as first-time public-sheet concepts.

   Ultrasound is now the conditional lead because its recent Google Books signal is approximately 1.70 times
   `elephant` and its monitor-plus-probe form opens a genuinely new healthcare concept. It still needs four
   fresh Google captures and a Microsoft small-size design review. CT Scan remains the filing-ready fallback.
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
   contain twelve independent proposals, but the strategy is to advance one lead and retain one fallback.
   Every proposal must stand on its own frequency, distinctiveness, multiple uses, and lack of a substitute.

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
| Nine clearly re-eligible packets | `submissions/v1.3.0/` | Three complete packets; six evidence-gated drafts |
| Three additional packets | `submissions/v1.5.0/` | Ultrasound, mouse-maze, and First Aid Kit full drafts; reproducible Bing supplements present; four Google captures still missing for each |
| Expanded-slate ranking | `docs/strategy/2026-07-10-expanded-proposal-ranking.md` | Ultrasound conditional lead; CT Scan filing-ready fallback |
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

1. Send Rhew the revised Monday decision brief and cover email in `docs/strategy/` and `output/`.
2. Run the 48-hour Ultrasound evidence sprint: manually capture Search, Video, Web Trends, and Image Trends.
   Use `npm run evidence:capture -- --concept=ultrasound --release=v1.5.0` from a Microsoft corporate or
   ordinary residential network Google accepts, and complete Google's human check in the visible persistent
   Firefox window if prompted. If Google remains inaccessible, ask Microsoft standards and Bing Search owners
   to clear a complete public, reproducible substitute; do not present the existing three-image Bing
   supplement as a replacement for the missing Trends charts.
3. Ask the Windows/Segoe UI Emoji and Fluent Emoji owners to test Ultrasound and CT Scan at 18x18 and in
   black-and-white; select CT Scan if Ultrasound misses the evidence or recognition gate.
4. Ask Microsoft Legal to review the selected CC0 paradigm and anticipated-implementation text.
5. Replace the selected draft's evidence notices, rebuild the proposal PDF, and inspect every page.
6. File one selected proposal by 2026-07-31; keep the three organ packets for a later eligible round.
