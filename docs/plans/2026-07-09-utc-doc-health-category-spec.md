# Spec: UTC document — "Health as a Category in Emoji Ordering"

> **DUE 2026-07-21.** Seven days before UTC #188 opens (July 28–30, 2026, Redmond, WA).
> Twelve days from this spec. Ten days *earlier* than the emoji submission deadline.

Status: SPEC — the document is not written, not submitted.
Drafted 2026-07-09.

This document is **not** an emoji proposal. It asks the UTC to change the **grouping** of emoji in Emoji
Ordering. It is gated on no artwork, no image licence, and no re-review eligibility. It can move now.

---

## 1. Submission mechanics

All verbatim from <https://www.unicode.org/pending/docsubmit.html>.

| Item | Requirement |
|---|---|
| Channel | Email **docsubmit@unicode.org** — "to request that the document be added to the agenda" |
| **Not** the emoji form | "Do not submit emoji or character proposals to this address." |
| Subject line | `UTC Doc: Health as a Category in Emoji Ordering` — "Make sure you have the following format" |
| Format | "Documents may be submitted in PDF or HTML format. The preferred document format is PDF." |
| Fonts | "**Font embedding is required:** Please embed all of your fonts when you create PDF files for submission. **This is extremely important!**" |
| First page | "must clearly identify the author or submitter, the subject, and the date of submission" |
| Also | Page numbers; headers/footers on multi-page documents; final form; under 6 MB |
| Deadline | "seven days before the start of the meeting at which they are to be considered" |
| Result | Unicode assigns an `L2/26-nnn` number, tells the submitter, and the document enters the public register |

**Meeting:** UTC #188, July 28–30, 2026, Redmond, WA (hybrid), per
<https://www.unicode.org/L2/meetings/utc-meetings.html>. The register lists the location but **names no
host organization** — do not claim Microsoft hosts it.
**Fallback:** UTC #189, October 26–28, 2026, Nancy, France. Deadline ~2026-10-19.

### Authorship

Unlike the emoji form, the UTC channel has no "individual only" rule — it asks for "the author or
submitter." Recommended byline:

> David Rhew, MD (Microsoft); Shuhan He, MD (Massachusetts General Hospital)

with Rhew as point of contact. Microsoft may appear as an organization here.

### The parallel filing

`emoji-test.txt` states *"The file is in CLDR order."* UTS #51 §5 *Ordering and Grouping* states the
Emoji Ordering data *"has been incorporated into CLDR."* The grouping therefore has two owners:

1. **UTC / Emoji Standard & Research Working Group** — the policy decision. This document.
2. **CLDR Technical Committee** — the data change. A Jira ticket at
   <https://unicode-org.atlassian.net/projects/CLDR/> ("To file a ticket, click the red 'Create' button").

File the CLDR ticket the same week and cross-reference the L2 number in both directions. A document that
lands in one room and not the other will die quietly.

---

## 2. The ask, stated precisely

The document must ask for one concrete, actionable thing. Vague papers get "noted."

> **Request:** That the UTC direct the Emoji Standard & Research Working Group and the CLDR Technical
> Committee to establish a top-level **Health** group in Emoji Ordering, populated by the existing
> `medical` subgroup and a new `body-organ` subgroup, and to assign future health-related emoji to it by
> default.

**Fallback ask, stated in the document** so the committee has somewhere to land short of the full change:

> If the UTC declines to create a top-level group at this time, we ask that it (a) formally designate
> `Objects > medical` as the default destination for future health emoji, and (b) direct the working
> group to report on health-emoji organization at a subsequent meeting.

Never ask for emoji in this document. It is about structure. Mentioning the kidney by name invites the
committee to read it as a proposal in disguise and bounce it to the emoji form.

---

## 3. The evidence

Every number below was computed on 2026-07-09 from
<https://unicode.org/Public/emoji/latest/emoji-test.txt> (Emoji 17.0, dated 2025-08-04), counting
`fully-qualified` entries. **Recompute and re-date before filing.** Include the method so it is
reproducible — that is the standard the emoji guidelines hold submitters to, and the committee will
apply it to us.

### 3.1 There is no Health group

Ten top-level groups exist. None is health.

| Group | Fully-qualified emoji |
|---|---|
| Smileys & Emotion | 171 |
| People & Body | 2,418 |
| Component | 0 |
| Animals & Nature | 160 |
| Food & Drink | 131 |
| Travel & Places | 219 |
| Activities | 85 |
| Objects | 266 |
| Symbols | 224 |
| Flags | 270 |
| **Total** | **3,944** |

### 3.2 `medical` is a drawer, and a small one

`medical` is one of 18 subgroups of `Objects`, holding **seven** emoji:
💉 syringe · 🩸 drop of blood · 💊 pill · 🩹 adhesive bandage · 🩼 crutch · 🩺 stethoscope · 🩻 x-ray

Ranked among Objects' subgroups:

| Subgroup | Count |
|---|---|
| clothing | 47 |
| tool | 27 |
| household | 25 |
| office | 23 |
| book-paper | 17 |
| light & video | 16 |
| computer | 14 |
| musical-instrument | 13 |
| mail | 13 |
| money | 11 |
| sound / music / other-object | 9 each |
| writing / science / **medical** | **7 each** |
| phone / lock | 6 each |

Medicine is allotted the same space as `writing`, less than `musical-instrument`, and a seventh of
`clothing`.

### 3.3 Health is scattered across seven of the ten groups

This is the strongest single table in the document. Thirty-seven health-related emoji, in **14 subgroups
across 7 groups**:

| Group > Subgroup | Emoji |
|---|---|
| Objects > medical | 💉 🩸 💊 🩹 🩼 🩺 🩻 |
| People & Body > body-parts | 🧠 🫀 🫁 🦷 🦾 🦿 🦻 |
| Smileys & Emotion > face-unwell | 😷 🤒 🤕 🤢 🤮 🤧 🥴 |
| People & Body > person-activity | 🧑‍🦯 🧑‍🦼 🧑‍🦽 |
| Objects > science | 🧪 🧫 🧬 |
| People & Body > person-role | 🧑‍⚕️ 🫄 |
| Animals & Nature > animal-mammal | 🦮 🐕‍🦺 |
| Animals & Nature > animal-bug | 🦠 microbe |
| People & Body > person-gesture | 🧏 deaf person |
| Symbols > other-symbol | ⚕️ medical symbol |
| Symbols > transport-sign | ♿ wheelchair symbol |
| Travel & Places > place-building | 🏥 hospital |
| Travel & Places > transport-ground | 🚑 ambulance |
| Smileys & Emotion > face-negative | ☠️ skull and crossbones |

The `medical` subgroup contains **7 of the ~37** health emoji in the standard. **The anatomical heart 🫀
and lungs 🫁 — encoded specifically as medical emoji in Emoji 13.0 — are not in `medical`.** They are
filed under `body-parts`, beside the mechanical arm and the ear.

The argument writes itself: health is not under-served. It is **structurally homeless**.

### 3.4 The group list is not immutable — precedent

This is the linchpin, and it is provable from Unicode's own published data files:

| Release | Top-level groups |
|---|---|
| Emoji 5.0 (2017) | Smileys & People · Animals & Nature · Food & Drink · Travel & Places · Activities · Objects · Symbols · Flags — **8** |
| Emoji 11.0 (2018) | identical — **8** |
| **Emoji 12.0 (2019)** | Smileys & Emotion · **People & Body** · **Component** · Animals & Nature · Food & Drink · Travel & Places · Activities · Objects · Symbols · Flags — **10** |
| Emoji 17.0 (2025) | identical to 12.0 — **10** |

Sources: `https://unicode.org/Public/emoji/{5.0,11.0,12.0,13.0}/emoji-test.txt`

In Emoji 12.0 the UTC **split** `Smileys & People` into two top-level groups and **added** a third.
Reorganization at the top level has precedent, it was done within living memory, and nothing broke.

Worth noting quietly in the document, not leaning on it: **Emoji 12.0 is also the release that shipped
Apple's accessibility set** (L2/18-080). The release that reorganized the groups is the release that
absorbed a coherent health-adjacent set.

### 3.5 Salience: why health, and why now

> Costa-Gomes B, Tolmachev P, … King D, Suleyman M. *Public use of a generalist LLM chatbot for health
> queries.* Nature Health 2026. doi:10.1038/s44360-026-00117-x
> Preprint: <https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/copilot-health-usage-report.pdf>

Verbatim:

- *"over 500,000 de-identified health-related conversations with Microsoft Copilot from January 2026"*
- *"nearly one in five conversations involve users describing their own symptoms, interpreting their own
  test results, or managing their own conditions"*
- *"across both condition information and symptom questions, one in seven conversations are on behalf of
  someone else, whether a child, an aging parent, or a partner"*
- *"The largest category, 'Health Information & Education,' accounts for over 40% of conversations."*
- prior work: *"health-related queries on consumer Microsoft Copilot were the most prevalent topic
  category on mobile"*

**In this document, the Copilot data is the primary argument, not a supplement.** A category is a claim
about salience — about how people reach for a concept — and this is the largest published measurement of
how people reach for health in a text interface. In an *emoji* proposal the same data would be
subordinate to the mandated Google evidence; here it is the point.

State the limitations, because the committee will find them anyway: single platform, single month,
queries not outcomes, ~22% US and ~45% English. The paper states all four.

---

## 4. Proposed structure

Be surgical. Every emoji you move is a fight; every one you leave is goodwill.

### Move

| Into | From | Emoji |
|---|---|---|
| `Health > medical` | `Objects > medical` | 💉 🩸 💊 🩹 🩼 🩺 🩻 (intact, all 7) |
| `Health > body-organ` (new) | `People & Body > body-parts` | 🧠 🫀 🫁 (organs only) |

### Do not move — and say so explicitly

| Emoji | Stays | Why |
|---|---|---|
| 😷 🤒 🤕 🤢 🤮 🤧 🥴 | Smileys & Emotion > face-unwell | They are faces. Users find them among faces. |
| 🦾 🦿 🦻 🦷 | People & Body > body-parts | Body parts and worn devices, not clinical objects |
| 🧑‍⚕️ 🫄 🧏 🧑‍🦯 🧑‍🦼 🧑‍🦽 | People & Body | They are people |
| 🏥 🚑 | Travel & Places | A building and a vehicle |
| ⚕️ ♿ | Symbols | Signage and symbols |
| 🦠 🧪 🧫 🧬 | Animals & Nature / Objects > science | Biology, not care |

Proposing to move ten emoji out of `Smileys & Emotion` would sink the document. Ask for three organs and
one intact subgroup.

### Forward-looking clause

Ask that **future** health emoji be assigned to `Health` by default. This is the clause that matters most
in the long run and costs the committee nothing today. It is also the clause that would have put the
anatomical heart and lungs in the right drawer in 2020.

---

## 5. Stability analysis — write this section, unprompted

The committee's first question will be "what breaks?" Answer it before it is asked. Grouping is
presentation, not identity:

| Unaffected | Affected |
|---|---|
| Code points | CLDR emoji ordering data |
| Character names | `emoji-test.txt` group/subgroup comments |
| Properties (`Emoji`, `Emoji_Presentation`, …) | Keyboard palette section headings |
| Encoding stability guarantees | Emoji chart pages |
| Existing sequences and ZWJ behaviour | Downstream palettes that hard-code group names |

No emoji is added, removed, renamed or re-encoded. Unicode's stability policy governs code points and
names; the Emoji 12.0 precedent establishes that group membership is revisable.

**Name the cost honestly:** users who have learned to find 💊 under Objects will find it under Health.
That is a one-time relearning, identical in kind to the 2019 split. Muscle memory is a real cost; say so,
then note that the 2019 change was absorbed without incident.

---

## 6. Objections, and the answers

| Objection | Answer |
|---|---|
| "This is a proposal for emoji in disguise." | The document requests no character. Say so in the abstract, in the first sentence. |
| "Categories are stable; we don't move things." | Emoji 12.0 split one group into two and added a third. Cite the data files. |
| "Health is a 'cause.'" | The emoji guidelines discount cause arguments *for encoding a character*. This is an organization question about a measured, dominant usage domain. Argue salience and coherence, never awareness. |
| "Seven emoji don't need their own group." | `Component` is a top-level group with **zero** fully-qualified emoji. And the group would hold ten, with the organs. |
| "Where does it end — a group for law, one for finance?" | The forward-looking clause bounds it: this asks for one group, defined by the `medical` subgroup plus internal organs, with a stated intent not to seek further reorganization. |
| "This is CLDR's business." | Correct, in part. That is why a parallel CLDR ticket is filed and cross-referenced. The UTC owns UTS #51; CLDR owns the ordering data. |

---

## 7. Document skeleton

Target 4–6 pages plus appendix. Dense, tabular, no rhetoric.

1. **Title block** — title, author(s), subject, date. Required on the first page.
2. **Abstract** — five sentences. First sentence: *this document proposes no new emoji.*
3. **Request** — the ask and the fallback ask, in a box, at the top. Not buried on page 5.
4. **Background** — how Emoji Ordering works; that the data lives in CLDR; that groups are presentation.
5. **Finding 1** — no Health group; the ten groups (table 3.1).
6. **Finding 2** — `medical` is 7 emoji, third-smallest drawer in `Objects` (table 3.2).
7. **Finding 3** — health is scattered across 7 groups and 14 subgroups; the heart and lungs are not in
   `medical` (table 3.3). **This is the centerpiece.**
8. **Finding 4** — precedent: 8 groups → 10 in Emoji 12.0 (table 3.4).
9. **Salience** — the Nature Health data, with its stated limitations (§3.5).
10. **Proposed structure** — what moves, what does not, and the forward-looking clause (§4).
11. **Stability analysis** (§5).
12. **Anticipated objections** (§6).
13. **Appendix A** — full census: every health-related emoji, its group and subgroup, with the script
    used to generate it, so the committee can reproduce the count.
14. **Appendix B** — the group lists of Emoji 5.0, 11.0, 12.0 and 17.0, with source URLs.

---

## 8. Writing rules

Per `reference_proposal_writing_rules` and the tone the committee expects:

- No em dashes. No "not X, but Y." Introduce every acronym once (UTC, ESR, CLDR, UTS).
- No advocacy language. No "awareness," no "the medical community deserves," no patient stories.
- Every claim gets a citation or a reproducible query. State the retrieval date on every count.
- Tables over paragraphs. The committee reads dozens of documents per meeting.
- Never mention the kidney, the four-year bar, or any pending proposal.
- Run `/humanizer` before export. Embed fonts. Check page numbers.

---

## 9. Phases

### Phase 1 — Data (by 2026-07-12)
Recompute every count against the then-current `emoji-test.txt`. Commit the script and its output to
`evidence/`. Verify the Emoji 5.0/11.0/12.0 group lists still resolve at their URLs.

**CHECKPOINT:** `evidence/` committed with a dated census and the generating script.

### Phase 2 — Draft (by 2026-07-16)
Write to the skeleton in §7. Legal review is *not* required: no images, no licence grant, no IP.
Microsoft Comms review of the byline and the Copilot framing probably is.

**CHECKPOINT:** draft committed; `/humanizer` run; Rhew and He review.

### Phase 3 — Produce (by 2026-07-19)
Export PDF **with fonts embedded**. Page numbers. Under 6 MB. Confirm the first page carries author,
subject and date.

**CHECKPOINT:** PDF committed; a colleague opens it on a machine without the fonts installed and confirms
it renders.

### Phase 4 — File (by 2026-07-21, hard)
Email docsubmit@unicode.org, subject `UTC Doc: Health as a Category in Emoji Ordering`. File the CLDR
Jira ticket the same day; cross-reference once the L2 number arrives.

**CHECKPOINT:** L2 number recorded in this repo. Diarise UTC #188, July 28–30.

---

## 10. Human gates

- [ ] Rhew agrees to be named author and point of contact
- [ ] Microsoft Comms clears use of the Copilot/Nature data in a public UTC document
- [ ] Decision on the fallback ask — do we offer it, or hold firm on the group?
- [ ] CLDR Jira account created
- [ ] **Filed by 2026-07-21**
