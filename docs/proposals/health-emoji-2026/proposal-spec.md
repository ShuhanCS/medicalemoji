# Spec: Health and Medicine Emoji Proposal, 2026 Intake

Status: draft spec, not a proposal.
Date: 2026-07-09.
Intake deadline: 2026-07-31 (22 days from this spec).
Target format: Unicode "Format for Emoji Proposals", https://www.unicode.org/emoji/proposals.html
Reference implementation in this repo: `docs/proposals/stomach-emoji-2026/stomach_emoji_proposal_SUBMIT.md`

This spec covers what to file, what cannot be filed, what evidence supports it, and what
is missing. It does not contain proposal prose. Write that from this spec.

---

## 1. Requested scope

Shuhan's stated scope: all the organs, the EKG, and the white blood cell.

| Concept | Prior public status | Art in repo | Filable 2026-07-31 |
| --- | --- | --- | --- |
| Kidney | Declined, submitted 2022-07-19 | Submission ready | Knife edge |
| Liver | Declined, submitted 2022-07-30 | Thin | Knife edge |
| Stomach | Declined, submitted 2022-07-28 | Partial | Knife edge |
| Spine | Declined, submitted 2024-04-05 | Thin | **No, barred to ~2028** |
| Intestines | Declined, submitted 2024-04-04 | Thin | **No, barred to ~2028** |
| ECG / EKG | Declined, submitted 2024-04-05 | **None** | **No, barred to ~2028** |
| White blood cell | Declined, submitted 2020-12-18 | **None** | Yes |

Read that table before writing a single line of proposal prose. Four of the seven
requested concepts cannot go in this cycle, and two of the remainder have no artwork.

## 2. The blocking constraint

Unicode: "Emoji declined within the last four years are not eligible for re-review."

The bar runs **four years from the decline**, not from the submission. The public status
CSV publishes only the submission date, which is why this is easy to get wrong. See
`docs/research/` and the project memory note for the three-way confirmation of this
reading.

Consequences:

- **Spine, intestines, ECG** were submitted 2024-04-04 and 2024-04-05, days after the
  2024 window opened, and were declined later that year. They are barred until roughly
  2028. Including them in a 2026 filing invites rejection of the characters and wastes
  reviewer goodwill on the rest.
- **Kidney, liver, stomach** were submitted 2022-07-19 through 2022-07-30 and declined
  around November 2022 (UTC #173). From the decline, the bar lifts around November 2026,
  which is **after this window shuts**. From the submission date they clear by 12, 3, and
  1 day respectively. This is genuinely uncertain and must be settled with Unicode before
  filing, not after.
- **White blood cell** was submitted 2020-12-18 and is clear under either reading.

Also clear under either reading, though not in the requested scope: pill pack, pill box,
blood bag, leg cast, IV bag, CT scan, weight scale.

### Action required before any filing

Ask the Emoji Standard and Research Working Group, in writing, which date starts the
four-year clock: the submission date, the internal decline decision date, the
notification date, or the status-page publication date. Everything in section 1 depends
on the answer. Microsoft, as a voting member, can ask this question through a channel
the project does not have.

## 3. Filing strategy

Three options. Recommendation first.

**Option A, recommended. File white blood cell alone this cycle, as a Microsoft-backed
proposal.** It is unambiguously eligible, it is the only requested concept with no
eligibility risk, and it lets the Copilot evidence carry a single clean character rather
than a contested set. Build the artwork, which does not exist. Stage kidney, liver, and
stomach for the next window once the clock question is answered.

**Option B. File white blood cell plus kidney, liver, and stomach**, with an explicit
eligibility note in Section 5 as the stomach proposal already does. Higher reward, real
risk: if the clock runs from the decline, three of the four characters are ineligible on
arrival and the packet reads as careless.

**Option C. File nothing this cycle.** Answer the clock question, build artwork for the
white blood cell and the EKG, and come back in 2027 with a complete set. Costs a year.
Defensible only if the artwork cannot be finished in 22 days.

Do not file spine, intestines, or ECG under any option.

## 4. Document structure

Follow Unicode's required order exactly. The stomach proposal in this repo already does;
mirror it.

1. Title: "Proposal for Emoji: <name>"
2. Submitter, date
3. Required example images, with the license and rights statement
4. Identification: CLDR short name, keywords, category, sort location
5. Images
6. Factors for inclusion: A multiple concepts, B use in sequences, C breaks new ground,
   D distinctiveness, E expected usage level, F completeness, G compatibility
7. Factors for exclusion: A already represented, B overly specific, C open-ended,
   D transient, E justified by an existing emoji
8. Other information: clinical context, coalition and support materials, eligibility
   caveat, submission mechanics

## 5. Evidence architecture

Unicode is explicit about what does not count. Petitions, hashtag campaigns, social-media
requests, and support letters are **not** usage evidence. The stomach proposal in this
repo states this correctly and the health proposal must keep that discipline.

### 5.1 Required frequency evidence

Unicode requires reproducible frequency evidence from a fixed set of sources, captured as
screenshots in a clean browser session immediately before filing. Comparator convention
in this repo is `elephant`.

| Source | Query | URL pattern |
| --- | --- | --- |
| Google Search | `white blood cell` | `google.com/search?q=<term>&hl=en&num=10&pws=0` |
| Google Video Search | `white blood cell` | `google.com/search?tbm=vid&q=<term>&hl=en&num=10&pws=0` |
| Google Trends, web | `elephant,white blood cell` | `trends.google.com/trends/explore?date=all&q=elephant,<term>` |
| Google Trends, image | `elephant,white blood cell` | `trends.google.com/trends/explore?date=all_2008&gprop=images&q=elephant,<term>` |
| Google Books Ngram | `elephant,white blood cell` | `books.google.com/ngrams/graph?content=elephant%2C<term>&...` |

Supplemental terms for white blood cell: `immune system`, `immunity`, `infection`,
`leukocyte`, `neutrophil`, `white count`, `fighting infection`.

### 5.2 Supplemental usage evidence: the Copilot paper

David Rhew asked for facts from this paper in the proposal. Here they are, in
proposal-ready form. Paste and cite.

**Citation.** Costa-Gomes B, Tolmachev P, Taysom E, et al. Public use of a generalist LLM
chatbot for health queries. *Nature Health.* 2026;1(7):689-696.
doi:10.1038/s44360-026-00117-x. Open access, CC-BY. Analysis of 617,827 de-identified
Microsoft Copilot health conversations from January 2026.

**Citable facts.**

1. Nearly one in five health conversations involve people describing their own symptoms,
   interpreting their own test results, or managing their own conditions. The authors call
   this a lower bound.
2. Among conversations about symptoms and conditions, roughly one in seven concern someone
   other than the user: a child, an aging parent, or a partner. Conversational health
   support is caregiving as well as self-care.
3. Personal health queries rise markedly in the evening and nighttime hours, when
   traditional healthcare is least available.
4. Usage splits sharply by device. Mobile concentrates on personal health concerns, while
   desktop is dominated by professional and academic work.

Facts 3 and 4 are the ones that matter most for an emoji proposal, and neither appears in
the summaries circulating online. Emoji are a mobile keyboard feature. Personal health
conversation is a mobile, after-hours behaviour. That is the connection worth drawing.

**Two guardrails.** The paper studied only health conversations, so it cannot support a
claim that health outranks other topics on Copilot. And it never mentions emoji, so cite
it for where and when people discuss health, not as evidence that emoji are used in
health communication.

### 5.3 Support letters

Usable in Section 8, "Other information", to demonstrate professional support. Never in
Section 6.E as usage evidence. The 2026 multi-specialty ACEP letter names ten medical
concepts and is already public:
https://medicalemoji.org/documents/ACEP-Medical-Emoji-Support-Letter-2026.pdf

## 6. Exclusion factors, white blood cell

Draft rebuttals. Each needs evidence before it goes into prose.

- **Already represented.** No existing emoji denotes an immune cell. The microbe emoji
  (U+1F9A0) denotes a pathogen, which is the opposite referent. Verify no sequence
  conveys it.
- **Overly specific.** Argue the concept is `white blood cell` as a class, the body's
  defense, and not a neutrophil or a lymphocyte. Resist any temptation to propose a
  specific leukocyte lineage.
- **Open-ended.** The weak point. Why the white blood cell and not the red blood cell, the
  platelet, the neuron? Answer it directly rather than hoping it is not asked. The red
  blood cell is arguably already served by the drop of blood emoji (U+1FA78). Build the
  argument that immunity is a distinct, high-salience public concept, which the pandemic
  made permanent rather than transient.
- **Transient.** Rebut with the Ngram record, which long predates 2020.
- **Justified by an existing emoji.** Do not argue "the anatomical heart was accepted, so
  this should be too." That is the named exclusion factor. Argue independent merit.

## 7. Images

Unicode auto-rejects proposals with nonconforming images. "Failure to include this
information will result in rejection of the proposal."

Requirements: 18x18 and 72x72 pixels, at the top of the document, in **both** color and
black-and-white. Grayscale is not acceptable. The submitter must warrant ownership of all
intellectual property rights, or supply a URL establishing public domain or open-source
license status.

| Concept | 18x18 color | 72x72 color | 18x18 b/w | 72x72 b/w |
| --- | --- | --- | --- | --- |
| Kidney | Ready | Ready | Ready | Ready |
| White blood cell | **Missing** | **Missing** | **Missing** | **Missing** |
| ECG | **Missing** | **Missing** | **Missing** | **Missing** |
| Liver, stomach, spine, intestines | Partial, needs review | | | |

The kidney pipeline in `docs/design/kidney-emoji-2026-06/` is the model. It renders SVG,
exports both sizes in both modes, and builds an 18x18 visual review board. Reuse it.

The white blood cell has a distinctiveness problem worth solving on paper before drawing:
at 18x18 a lobed nucleus inside a pale cell body may read as a generic blob, or worse, as
the existing microbe emoji. The design must be legible against 🦠 at emoji size. Build the
comparison board first.

## 8. Microsoft's role

Verified: Microsoft ships Segoe UI Emoji, and therefore designs the glyph that a large
share of the world would see if a character is encoded.

**Unverified, and load-bearing.** Microsoft's Unicode membership class could not be
confirmed from the primary source in this pass. The members page renders its Full Member
tab dynamically. The project memory records Microsoft as a Full Member with a board seat,
and the same note warns against publishing the Full Member roster or naming any Microsoft
representative on the emoji working group. Confirm the membership class from
https://home.unicode.org/membership/members/ before any proposal or briefing relies on it.

What Microsoft can do that the project cannot:

1. Settle the four-year clock question through a member channel.
2. Contribute the Copilot usage evidence as an author or a named data source, which is
   materially stronger than a third party citing their paper.
3. Vote.

What Microsoft must not be asked to do: submit anything that reads as a vendor lobbying
for its own logo or product. The proposal is for a body's defense cell, not for Copilot.

## 9. Risks

1. **The clock.** Highest risk, entirely unresolved, and it determines scope. Resolve
   first.
2. **Artwork in 22 days.** The white blood cell has no art and a real distinctiveness
   problem. This is the schedule risk.
3. **Open-endedness.** The white blood cell's weakest factor. If the answer to "why not
   the red blood cell" is not convincing, the proposal fails on a named exclusion factor.
4. **Overreading the Copilot paper.** It is evidence about conversation volume, not about
   emoji. Cite it for what it measures.
5. **Set framing.** Proposing "the organs" as a group invites the completeness objection
   that Unicode does not encode arbitrary categories. The stomach proposal already handles
   this correctly by arguing independent merit and explicitly disclaiming a demand that
   Unicode encode every organ. Keep that posture.

## 10. Open questions

1. Which date starts the four-year re-review clock? Unresolved, and it determines scope.
2. Is Microsoft a Full Member, and will they co-submit, supply data, or only endorse?
   Membership class unconfirmed from the primary source.
3. ~~Does the Copilot paper support the three claims?~~ Resolved in section 5.2. Two of
   three verified with narrowed denominators. The third is not supported by this paper.
4. Can white blood cell artwork reach submission quality and pass an 18x18 review board
   before 2026-07-31?
5. If only one character can be filed, is the white blood cell the right one?

On question 5: the Copilot paper reports no organ-level breakdown, so it supports the
program rather than any single character. Cite it as context in Section 8 and let the
Google frequency evidence in 5.1 carry the expected-usage case for whichever character
is filed.
