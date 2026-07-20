# The 2020 to 2021 Emojination drafts

Fifteen emoji proposal drafts, recovered from `Emoji Proposals-20260710T003129Z-2-001.zip` and converted from
`.docx` to markdown on 2026-07-09. **None became an L2 document.** Their concepts and dates correspond to
Declined rows in Unicode's public proposal-status export, making this the repository's confirmed project
failure archive. The public status data does not disclose every review reason, and the archive may not contain
every proposal the project ever submitted.

Fourteen of the sixteen files in the archive carry the title `… Emoji Proposal for Emojination`. A
sixteenth, `Proposal for Emoji_ Tarsier.docx`, is unrelated to this project and was not imported.

**Images are not committed.** The archive is 56 MB, almost all screenshots and artwork. Figures appear in
these files as `*[figure: imageN.png]*`. The source `.docx` remain in Shuhan's Downloads folder.

## What was written

| Concept | Date | Requested sort order | Ngram | "elephant" | Instagram |
|---|---|---|:-:|:-:|:-:|
| Kidney | 2020-07-04 | `BODY PARTS`, after HEART | no | no | no |
| Liver | 2020-07-12 | none stated | **yes** | **yes** | no |
| Pill box | 2020-08-25 | `MEDICAL`, after PILL | **yes** | **yes** | no |
| White blood cell | 2020-08-29 | `MEDICAL`, after DROP OF BLOOD | no | no | no |
| Stomach | 2020-08-31 | `BODY PARTS`, after LUNGS | **yes** | **yes** | no |
| Blood bag | 2020-08-31 | none stated | no | no | no |
| Crutches | 2020-08-31 | `medical`, after ADHESIVE BANDAGE | no | no | yes |
| CT scan | 2020-08-31 | none stated | no | no | no |
| ECG | 2020-08-31 | none stated | no | no | yes |
| IV bag | 2020-08-31 | `MEDICAL`, after SYRINGE | no | no | no |
| Leg cast | 2020-08-31 | `medical`, after ADHESIVE BANDAGE | no | no | yes |
| Pill pack | 2020-08-31 | `MEDICAL`, after PILL | no | no | no |
| Spine | 2020-08-31 | none stated | no | no | no |
| Weight scale | 2020-08-31 | `MEDICAL`, after STETHOSCOPE | no | no | no |
| Intestines | 2021-11-20 | `body parts`, after LUNGS | no | no | yes |

Authors across the set: Shuhan He, Debbie Lai, Ali Raja, Daniel Wang, Geoffrey Burrows, Alister Martin,
Adi Balk, Jarone Lee. Lai and Lee are the co-authors of the 2021 JAMA paper.

## The honest review

### These are not bad documents

Every one of the fifteen carries the full selection-factor skeleton: Compatibility, Expected Usage Level,
Frequency, Multiple Usages, Use in Sequences, Breaking New Ground, Image Distinctiveness, Completeness,
then Selection Factors Exclusion with Already Represented, Overly Specific, Open-ended, Transient and
Faulty Comparison. They carry real search evidence. They are competently argued.

**They match the format of a proposal that succeeded.** The crutch proposal, `L2/19-379`, which shipped in
Emoji 14.0, uses Bing Search, and contains the line `E. Frequently requested n/a`. Both features appear in
these drafts. They were written to the template of the day, and the template of the day worked for other
people.

This proves that structural completeness alone did not advance them. It does not prove that writing and
evidence quality played no role; Unicode's public status only says the selection criteria were not fulfilled.

### What has since become disqualifying

Judged against the **current** guidelines, and only against those:

- **Google Books Ngram Viewer is now a required source. It appears in three of fifteen.** Liver, pill box
  and stomach have it. Twelve do not.
- **Trends screenshots must include "elephant" as a comparative term. Three of fifteen do.** The same three.
- **`Frequently Requested` appears in all fifteen.** In 2020 this was a section in Unicode's own template,
  as `L2/19-379` shows. Today: *"Petitions or 'frequent requests' play no role in emoji encoding approval,
  and are not acceptable as evidence for citation."* The kidney draft's entire entry reads *"Kidneys are
  frequently referred to on the Internet, including in memes."*
- **Instagram Search appears in four**, and thirteen mention social media or petitions. Today: *"Do not
  include examples from social media of people calling for the emoji. That is not reliable enough data to
  be useful, and detracts from the strength of your proposal."*
- **Bing Search appears in fourteen.** Now permitted only *"if Google is not available or accessible in
  your region."*

### The finding that matters most

Look at the sort-order column.

**The kidney asked to be placed in `BODY PARTS`, after HEART. Stomach and intestines asked for `body
parts`, after LUNGS.**

We requested the classification we are now asking the Unicode Technical Committee to undo. The organs went
to `body-parts` because we put them there, and because the Emoji Subcommittee's recommendation
`L2/19-190R` did the same for the anatomical heart and lungs. Nobody was being careless. There was no
better destination, which is precisely the argument of
[the Health category document](../utc-health-category/health-category-utc-doc.md).

Note also that six of the fifteen asked for the `MEDICAL` category. Those six are devices. Every proposal
for an **organ** asked for `body parts`. The split in our own drafts is the split the standard still has.

### What the record can and cannot explain

The status export confirms decline but does not publish a factor-by-factor rationale. The defensible findings
are:

1. **They stopped before the L2 register.** An analysis limited to public L2 documents omits this early-screen
   failure mode entirely.
2. **The old evidence packages do not meet the current rules.** Most lack Ngram and elephant, and most include
   social-media or frequent-request material that current instructions reject.
3. **The organ slate raises an Open-ended risk.** Filing several organs together does not automatically fail
   them and is not prohibited. It does require each one to show an independent, broad use case rather than a
   claim that Unicode should complete an anatomy set.

Do not infer that an organization is required. X-Ray, L2/20-214, was filed by two individuals and encoded in
Emoji 14.0:

https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf

See [`docs/strategy/unicode-map-and-strategy.md`](../../strategy/unicode-map-and-strategy.md) for the full
provenance evidence.

## Missing from this archive: maze, origami, and paper crane

Unicode's public status sheet lists several declined proposals whose drafts are **not** in the zip and are
not anywhere on disk:

| Concept | Status | Date submitted |
|---|---|---|
| Maze | Declined | 2018-04-12 |
| **Maze** | **Declined** | **2020-12-18** |
| origami | Declined | 2021-06-20 |
| Origami | Declined | 2024-04-16 |
| Paper Crane (B) | Declined | 2020-02-05 |
| Paper Crane (A) | Declined | 2020-02-13 |
| Paper Crane | Declined | 2024-04-04 |
| Crane Bird | Declined | 2024-07-30 |

**The 2020-12-18 maze shares its submission date with ten of the drafts above** (liver, intestines, ECG,
white blood cell, pill pack, blood bag, leg cast, IV bag, CT scan, weight scale). Shuhan runs Maze
Engineers. That is suggestive and it is **not proof**: the status sheet lists concepts, never submitters.

None of maze, origami or paper crane appears in any L2 register from 2016 to 2026, so none of them ever
advanced. If drafts exist, they should be added here. If they were someone else's proposals, that is worth
knowing too, because it changes how many times this project has actually been declined.

## Reusing this material

The prose, the clinical argument and the reference lists are worth keeping. The frequency evidence must be
recaptured from scratch: incognito, hyphenated search terms, all five mandated sources, `elephant` in the
Trends and Ngram screenshots, and a stated capture date. Delete every `Frequently Requested` section and
every Instagram citation before reuse. They now count against the proposal.
