# Microsoft medical emoji review packet

## Current send/review deck - v6

Use only these current deck files for Microsoft review:

- `Emoji-2026-Brief-v6.pptx`
- `../../../output/pdf/2026-07-12-microsoft-medical-emoji-review-deck.pdf`

The v6 deck is an eight-slide, decision-focused review copy prepared by Shuhan He. It does not assign
authorship, endorsement, implementation, or Unicode-outcome language to Microsoft without explicit approval.

| # | Slide | Purpose |
|---|---|---|
| 1 | Medical Emoji | Defines the narrow decision and review deadline. |
| 2 | The decision is narrow | Keeps Ultrasound as the conditional lead, CT Scan as fallback, and the organs on hold. |
| 3 | Four non-negotiable submission checks | Summarizes eligibility, rights, evidence, and small-size recognition gates. |
| 4 | Submission readiness determines the 2026 order | Separates potential from filing readiness. |
| 5 | Organ art was rebuilt for small-size review | Shows the redesigned `v1.7.0` Kidney, Stomach, and Liver assets. |
| 6 | Microsoft's role is technical review, not outcome-seeking | Defines the legitimate product, design, standards, and legal review. |
| 7 | Run a 48-hour evidence and design gate | Assigns the remaining evidence and recognition work. |
| 8 | What we need from Microsoft | Requests named owners, a lead/fallback decision, and technical review authority. |

Current supporting materials:

- `../../strategy/2026-07-12-microsoft-medical-emoji-decision-brief.md`
- `../../../output/doc/2026-07-12-microsoft-medical-emoji-decision-brief.docx`
- `../../../output/pdf/2026-07-12-microsoft-medical-emoji-decision-brief.pdf`
- `../../strategy/2026-07-12-microsoft-medical-emoji-product-legal-clearance.md`
- `../../../output/doc/2026-07-12-microsoft-medical-emoji-product-legal-clearance.docx`
- `../../../output/pdf/2026-07-12-microsoft-medical-emoji-product-legal-clearance.pdf`
- `../../outreach/2026-07-12-david-rhew-microsoft-packet-email.md`
- `../../../submissions/v1.7.0/manifest.md`

Remaining gates are not optional: Kidney, Stomach, and Liver need Unicode eligibility confirmation; Stomach
and Liver use stale 2020 evidence; Liver's Trends captures are United States-only; and the current Google
refresh is blocked because Trends returns HTTP 429 while Search presents a CAPTCHA.

## Archived v5/v4 build and research notes - do not send

The remainder of this file documents how the older v5/v4 decks were built and fact-checked. Those decks are
retained as research history only. They are not the current Microsoft review packet.

## Slide 8: the set precedent

Verified by loading the primary document
(<https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf>):

> "Proposal For New Accessibility Emoji **Submitter: Apple Inc. Date: March 2018**"

> "Developed in collaboration with internationally respected community organizations such as
> American Council of the Blind, the Cerebral Palsy Foundation and the National Association of the Deaf"

Nine concepts shipped in Emoji 12.0 (2019): guide dog, service dog, probing cane, manual and
motorized wheelchairs, ear with hearing aid, deaf person, mechanical arm, mechanical leg.

**The technique matters more than the precedent.** Apple pre-emptively disarmed Unicode's
"Open-ended" exclusion factor in its own text:

> "This is not meant to be a comprehensive list of all possible depictions of disabilities, but to
> provide an initial starting point."

Compare Unicode's selection factors (<https://unicode.org/emoji/proposals.html>): *"Is it just one
of many...? If this emoji is added, will it result in the need to add other similar types."* and
*"The goal is iconic representation of large categories, not completeness in the sense of filling
out the categories of a scientific or taxonomic classification system."*

A fourteen-organ set reads as a taxonomy — which is very likely part of why every one was declined.
A curated set, carried by a member, reads as Apple 2018.

Other precedents on the slide: Plan International UK + NHS Blood and Transplant (drop of blood,
Emoji 12.0; their narrower "period pants" was declined first); Tinder + Emojination (71
holding-hands combinations, Emoji 12.1); Google (gender-inclusive designs, L2/19-078).

## Slide 9: how L2/18-080 was actually argued

Apple walked Unicode's selection factors in order and wrote a section headed **"Counterarguments to
Factors for Exclusion,"** pre-rebutting each exclusion by name. All quotes verbatim from the PDF:

| Factor | Apple wrote |
|---|---|
| Frequency | "the most compelling factor for this proposal is **not** frequency of use of each character, but the desire to be inclusive in representation." Then filed Google Trends data anyway: "each data item was obtained using a new private browser window." |
| Breaking new ground | "Other than the wheelchair symbol, there are currently no emoji that can be used to depict various forms of disability." |
| Image distinctiveness | "the image of a hearing aid would not be sufficiently distinctive at emoji scale; it needs to be shown with an ear in order to establish its identity." Argued manual vs motorized wheelchairs must be separate characters. |
| **Open-ended** | "we don't expect such discussion to lead to proposals for a large number of additions beyond the current proposal." |
| Partners | "Developed in collaboration with … American Council of the Blind, the Cerebral Palsy Foundation and the National Association of the Deaf." |

Two techniques worth stealing:

1. **Frequency by proxy.** Apple noted "searching for 'person with wheelchair' or 'person with white
   cane' did not produce significant results," so it ran Google Trends on the *object* ("wheelchair",
   "prosthetic") and benchmarked each term against terms for *existing* emoji.
2. **Reproducibility.** "All data are from February and March 2018; each data item was obtained using
   a new private browser window." Our packets never stated a capture method.

These map one-to-one onto the five gaps in `docs/proposals/kidney-emoji-2026/previous-proposal-review.md`
(medical-importance over-reliance, missing reproducible frequency evidence, weak breaks-new-ground,
undeveloped 18×18 distinctiveness, open-ended-organ concerns).

Note: "Partners" is **not** a Unicode selection factor. It is labelled that way on the slide so the
column does not imply otherwise.

**Not claimed on the slide:** that Microsoft has never proposed an emoji. No Microsoft-authored
proposal was found, but the master proposals chart could not be fully parsed, so the slide says the
medical set is unclaimed rather than asserting a negative about Microsoft.

## Files

- `Emoji-2026-Brief-v6.pptx` - current eight-slide Microsoft review deck
- `build_v6.js` / `finalize_v6.ps1` - rebuild and PowerPoint-finalize the current deck
- `Emoji-2026-Brief-v5.pptx` - archived ten-slide deck; do not send
- `Emoji-2026-Brief-v4.pptx` - archived nine-slide deck; do not send
- `build_sets_slide.py` / `sets.png` — slide 8 and its proof
- `Emoji-2026-Brief-v3.pptx` — 8-slide deck, input to the sets slide
- `infographic-unicode-orgchart.png` — slide 7 at 3200×1800, for dropping into any deck
- `deck_kit.py` — shared chrome/card/text helpers and the geometry QA pass
- `build_orgchart.py` — rebuilds slide 7 from the v2 deck; touches no other slide
- `orgchart.png` — 1600×900 proof of slide 7
- `Emoji-2026-Brief-v2.pptx` — Shuhan's edited 9→8 slide deck, the input to the org chart
- `build_slides.py` — **frozen**; produced the original v2 slides. Predates `deck_kit.py`.
- `infographic-unicode-microsoft.png`, `render-6/7/8.png` — v2-era proofs

Source deck: `C:\Users\Shuha\Downloads\Emoiji 2026 Brief.pptx` (not in this repo, too large).
The scripts locate slides by title rather than by index, and print a geometry QA pass
(out-of-bounds and overlap checks) on every run.

**Gotcha:** add a new slide *before* dropping one. A part created after a drop reuses the
freed partname (`slide8.xml`) and silently overwrites the Request slide.

## The finding that matters

**Kidney, Stomach, and Liver are held from the 2026-07-31 deadline unless Unicode confirms eligibility.**

Unicode's rule is four years, not two, and it runs from the *decline*:

> "Emoji declined within the last four years are not eligible for re-review."
> — <https://unicode.org/emoji/proposals.html>

> "Emoji that have been declined are not eligible to be re-submitted for four (4) years."
> — Status Key, <https://unicode.org/emoji/emoji-proposals-status.html>

The public status sheet publishes the **submission** date, not the decline date. Three
independent confirmations:

1. Blood drop is document [L2/18-092](https://www.unicode.org/L2/L2018/18092-blood-drop-emoji.pdf),
   submitted 2018 and approved Feb 2019 for Emoji 12.0. The sheet lists `4/3/2018`.
2. Charlotte Buff, Unicode contributor: *"The 'Date' column appears to show proposal
   submission dates based on document IDs."*
3. Our rows cluster on window boundaries: spine/intestines/ECG are `4/4/2024` and
   `4/5/2024`, two days after the 2024 window opened on April 2. Kidney/stomach/liver are
   `7/19`, `7/28`, `7/30` of 2022 — the final days before the July 31, 2022 close.
   Declines would not cluster that way.

Kidney, stomach and liver were therefore submitted in July 2022 and **declined around
November 2022** (the ESC report for UTC #173 is dated 2022-10-31; submitters are notified
at cycle end). Four years from that decline lands ~November 2026, after the 2026 window
shuts. Counted from submission instead, they clear by 12, 3 and 1 day respectively.

The private 2022-11-04 notices put all three within four elapsed years of the 2026-07-31 deadline. Confirm
eligibility with Unicode before filing any proposal from `submissions/v1.7.0/`.

### There is no public decline date — for any emoji

Checked 2026-07-09 and confirmed by loading each artifact:

- The status sheet has three columns only: `Emoji | Status | Date Submitted`. No decline column.
  The column cannot be a decline date: rows with status `Under Consideration` carry dates too.
- **UTC #173 minutes** (<https://www.unicode.org/L2/L2022/22241.htm>) record no per-proposal emoji
  declines. The Emoji Subcommittee report was delivered orally. The UTC does not vote proposals
  down individually.
- The Q3/Q4 2022 ESC reports (L2/22-126, L2/22-246) are scanned image PDFs with no decline table.
- The [Notices of Non-Approval archive](https://www.unicode.org/alloc/nonapprovals.html) stops at
  2019 and covers formal character rejections, not emoji ESC declines.

Charlotte Buff: declined decisions "were only shared privately with the proposal authors."

**So the decline date exists in exactly one place: the private notification email Unicode sent the
submitter, ~November 2022. Shuhan is the submitter. Search that mailbox before asking Unicode.**

A logical corollary worth remembering: a proposal submitted inside a window is always declined
*after* that window closed. So a 2022-cycle proposal can never clear a 2026-07-31 deadline under
the decline clock, whatever the exact date. The two readings necessarily disagree for anything
filed in a window's final days.

One argument in our favour: the bar was **two years** until the four-year text appeared (present by
the March 2024 reopening announcement, <http://blog.unicode.org/2024/03/emoji-submissions-intake-process-re.html>).
Under the rule in force at the time of the ~Nov 2022 decline, the bar lapsed ~Nov 2024. Whether
Unicode applies the longer bar retroactively is unaddressed by any source. (The two-year history
comes from archived snapshots; web.archive.org is unfetchable from here, so re-verify before
relying on it.)

### 2026-07-31 eligibility

| Status | Concepts |
|--------|----------|
| Clear to file now | white blood cell, pill pack, pill box, blood bag, leg cast, IV bag, CT scan, weight scale |
| Hold unless Unicode confirms eligibility | kidney, stomach, liver |
| Barred (~Nov 2028) | spine, intestines, ECG |

## Fact-check notes

Verified against primary sources and safe to present:

- UTC voting: Full member = 1 vote, Supporting = ½, all other tiers none — <https://www.unicode.org/consortium/utc.html>
- Microsoft holds a Board of Directors seat: "Vishal Chowdhary, 2026 to present … Vice President
  of Science at Microsoft where he leads Office AI Science team in Microsoft 365 Copilot" — verified
  2026-07-09 at <https://unicode.org/consortium/directors.html>
- The five UTC working groups: Emoji Standard & Research, Script Encoding, CJK & Unihan,
  Properties & Algorithms, Editorial — <https://www.unicode.org/consortium/utc.html>
- The Consortium has "three technical committees and the editorial committee" (UTC, CLDR TC,
  ICU TC, Editorial Committee) — <https://www.unicode.org/consortium/consort.html>. That page
  does **not** state a Board→committee reporting line; don't draw one.
- The emoji body is now the **Emoji Standard & Research Working Group**, formerly the Emoji
  Subcommittee (ESC). It recommends; the UTC votes. It has no final encoding authority.
- 2026 window: opened April 2, closes July 31; submitters notified by November 30 — <https://unicode.org/emoji/proposals.html>
- Heart and lungs shipped in **Emoji 13.0 (2020)**. The website's "Unicode 14.0 in 2021"
  (`src/app/page.tsx`, `src/components/Timeline.tsx`) contradicts the memos and is wrong.

Deliberately **not** on the slides, because they could not be confirmed from a primary source:

- The exact Full Member roster and count (Wikipedia says six; that conflicts with Google,
  Adobe and Airbnb holding board seats).
- Membership fee figures.
- Any named Microsoft representative on the UTC or the emoji working group. The deck says
  Microsoft votes in the UTC — which follows from Full membership — and does not claim a
  Microsoft seat on the emoji working group.
- Whether the JAMA figure depicted all 14 concepts. Shuhan (an author) confirmed the set.
