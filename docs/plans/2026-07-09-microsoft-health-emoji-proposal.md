# Spec: Microsoft health emoji proposal, 2026 cycle

Status: DRAFT SPEC v2 — audited against Unicode's live guidelines, not approved, not filed
Drafted 2026-07-09. Deadline **2026-07-31** (22 days).

Authority for everything below: <https://unicode.org/emoji/proposals.html> (Last Update: 2026-05-20),
read in full from source, plus the live submission form. Quotes are verbatim.

---

## Audit: where spec v1 was wrong

| v1 said | Verdict | What Unicode actually says |
|---|---|---|
| `Submitter: Microsoft Corporation` | **WRONG** | Form field *Submitter Name*: "The name must be of an individual. **Names of organizations or companies will not be considered.**" |
| Apple's L2/18-080 is the template | **WRONG** | "new proposals must follow the current Format for Emoji Proposals. **This format has changed substantially since earlier proposals were submitted.**" Apple is a *rhetorical* model only. |
| Lead with importance and inclusion | **DANGEROUS** | "Please do not justify the addition of an emoji because it furthers a 'cause,' no matter how worthwhile. A proposal may be advanced despite a 'cause' argument … but will not be advanced because of it." |
| Reuse the existing candidate art | **FATAL** | *Automatically Declined* → "**Includes text**: We no longer encode emoji that include text." Our blood bag, IV bag, pill box and weight scale art all carry labels, barcodes or digits. |
| "Microsoft Legal gate" on images | **UNDERSTATED** | A signed **Emoji Proposal Agreement & License** is mandatory: "YOU ARE GRANTING A BROAD IRREVOCABLE LICENSE TO THE UNICODE CONSORTIUM." Checkbox-by-checkbox, signed by the individual submitter. "The Consortium cannot accept any submission that is not accompanied by this warranty and license." |
| Argue "Completeness" for the set | **WRONG FACTOR** | Completeness means *fixed, closed* sets — zodiac, blood types {🅰️🅱️🆎🅾️}, card suits. Organs are not a closed set. Mark n/a. |
| 8–11 concepts is fine | **RISKY** | "many emoji categories are reaching or are at a point of saturation … the Unicode Consortium approves fewer and fewer emoji proposals every year." |

### What survived the audit

Form URL, publicly-hosted PDF requirement, 18×18 and 72×72 in colour and black & white (grayscale ❌),
the five mandated frequency sources with "elephant" as comparator, the ban on petitions/hashtags/
anecdote, the four-year bar, notification by 2026-11-30, and the required top-of-page fields.

---

## Decisions, corrected

| Decision | Choice |
|---|---|
| Target cycle | File in the 2026 window |
| **Submitter** | **A named individual at Microsoft** (David Rhew, MD, or a named Microsoft designer). Microsoft appears as affiliation and throughout the body. Partners credited in the text. |
| Category ask | Two documents: the proposal(s), plus a separate category paper to the working group |

**Open question we cannot answer from public sources:** whether one submission may carry multiple emoji.
The guidelines are written in the singular throughout ("your emoji"), `Identification` is per-emoji, and
the form is 22 pages. Apple's 2018 multi-emoji document predates the form. **Ask the Emoji Standard &
Research Working Group before building one giant PDF.** Default assumption: **one proposal per emoji**.

---

## Deliverables

- **Document A** — one proposal PDF *per concept* in the clear set. Filed via the form.
- **Document B** — kidney, liver, stomach. Filed separately, same window. See Risks.
- **Document C** — `Health as a Category in Emoji Ordering`. A **UTC document**, emailed to
  docsubmit@unicode.org, due **2026-07-21** for UTC #188 (Redmond, July 28–30). Not a form submission,
  and explicitly barred from the emoji form. Plus a parallel CLDR ticket for the data change.

---

## Set composition, graded honestly

The binding factor is **Breaks new ground**, and Unicode's example is brutal:

> "because there is already an emoji for 🧹 broom, an emoji for vacuum cleaner would not break new ground"

The `medical` subgroup already holds 💉 syringe, 🩸 drop of blood, 💊 pill, 🩹 adhesive bandage,
🩼 crutch, 🩺 stethoscope, 🩻 x-ray. Every proposal must clear that bar.

| Concept | Bar status | Nearest existing emoji | Breaks new ground? | Call |
|---|---|---|---|---|
| Kidney | arguable (see B) | 🫀 🫁 🧠 (organs exist, kidney does not) | **Yes** — a distinct organ | **Lead** |
| Liver | arguable | same | Yes | Strong |
| Stomach | arguable | same | Yes | Strong |
| White blood cell | clear | 🦠 microbe | Probably — host cell vs germ, but expect the challenge | Strong |
| Weight scale | clear | ⚖️ balance scale (justice) | Yes — no bathroom scale exists | Medium |
| Leg cast | clear | 🩼 crutch | Immobilisation vs mobility aid | Medium |
| Blood bag | clear | 🩸 drop of blood | Donation/transfusion vs bleeding | Medium |
| IV bag | clear | 💉 syringe | Infusion over time vs injection | Medium |
| Pill box | clear | 💊 pill | Adherence/regimen vs dose | Weak-medium |
| Pill pack | clear | 💊 pill | **Reads as a variant of pill** — the vacuum/broom problem | Weak |
| CT scan | clear | 🩻 x-ray | **Reads as a variant of x-ray** | Weak |

**EXCLUDED — no argument exists:** spine, intestines, ECG. Submitted 2024-04-04/05, barred until 2028
under *either* clock.

**Recommendation:** given saturation, file **five to six**, not eleven. Strongest slate:
kidney, liver, stomach (Document B) + white blood cell, weight scale, blood bag (Document A).
Drop pill pack and CT scan. Hold pill box, leg cast, IV bag for 2027.

---

## Section-by-section writing guide

Everything from `Title` through `License` **must be on the top of the first page**.

### Title
Format: `Proposal for Emoji <name>`. Descriptive, not prescriptive.
Unicode: "Use a descriptive term … rather than something prescriptive."

- ✅ `Proposal for Emoji Kidneys`
- ❌ `Proposal for Emoji Kidney Health Awareness`

Names are provisional: "Proposed emoji names are subject to change."

### Submitter
`<name(s)>`, semicolon-separated, one named as main point of contact.
**Must be individuals.** Write: `David Rhew, MD (Microsoft); Shuhan He, MD (Massachusetts General
Hospital); …` — main contact flagged.

### Date
Update on every revision. Trivial, and people lose proposals on it.

### Identification — Keywords
"Do not repeat the name of the emoji. Consider terms that people would use to find this emoji."

- Kidneys → `nephrology, dialysis, transplant, renal, organ, urology`
- White blood cell → `immune, infection, leukocyte, immunity, blood`
- Blood bag → `donation, transfusion, donor, blood drive`
- Weight scale → `weigh, bathroom, mass, health, fitness`

### Identification — Category
"The proposed category for the emoji in Emoji Ordering." Format like `Smileys & Emotion face-smiling`.

Write: `Objects medical`. Note in *Other information* that organs currently sit in
`People & Body body-parts` (where 🫀 and 🫁 live) — and that this fragmentation is the subject of
Document C. Do **not** argue the category change here; it dilutes the proposal.

### Images
18×18 **and** 72×72, **colour and black & white**. Grayscale ❌. At the top of the document.

> "The small size of the images aids in illustrating if the image is distinctive enough at typical emoji sizes."

**No text, no digits, no barcodes, no letters.** Automatically declined otherwise. This kills the current
art for blood bag (label + barcode), IV bag ("0.9% Sodium Chloride Injection USP" + barcode), pill box
(weekday letters), weight scale (a digital readout). All must be redrawn clean.

Do not request an exact rendering — *Exact images* is an automatic decline. The image is a paradigm:

> "🍺 beer mug represents not just a mug with exactly the shape you see on the screen … but rather beer in general."

### License
Certify ownership of all IP Rights, *"even if the image(s) has been developed by the Submitter with the
assistance of AI tools."* If not owned, give a **URL where the licence or public-domain status is clearly
stated**. "Failure to include this information will result in rejection of the proposal."

Separately, the individual submitter signs the **Emoji Proposal Agreement & License** inside the form:
a "non-exclusive irrevocable, perpetual, worldwide, royalty-free license" to Unicode, sublicensable.
**Microsoft Legal must clear this before any art is commissioned.** Once encoded, "it can never be removed."

---

### Factors for Inclusion — what to write in each

> "None of these factors alone determine eligibility or priority: all of the factors together are taken
> into consideration." … "Your proposal must include screenshots or citations to back up all claims."

**1. Multiple meanings** — "Does the emoji have notable metaphorical references or symbolism? This does
not include puns." *"Mark this as n/a unless there are compelling examples."*

- Kidneys: n/a is honest. Do not reach.
- Weight scale: arguably weight, health, self-monitoring. Thin. Probably n/a.
- Resist inventing symbolism. An unconvincing claim costs credibility on the factors that matter.

**2. Use in sequences** — *"Mark this as n/a unless there are compelling examples."*

- Kidneys: 🫘➕🫀 for transplant; 🩸 + kidneys for dialysis. Weak but real; state plainly or mark n/a.

**3. Breaks new ground** — *"Mark this as Yes or No. If Yes, explain why."* This is where the proposal
is won.

- Kidneys: **Yes.** Anatomical heart, lungs and brain are encoded; no kidney exists, and no sequence of
  existing emoji conveys "kidney." Not a variant of any encoded organ.
- Blood bag: **Yes**, and address the broom/vacuum test head on: a drop of blood denotes bleeding or
  menstruation; a blood bag denotes donation and transfusion — a different act, not a different picture
  of the same thing.
- CT scan: honestly, No. That is why it is cut.

**4. Distinctiveness** — "legible and visually distinctive … recognizable … at typical emoji sizes, such
as 18×18 pixels."

Show the 18×18 render inline and argue from it. Apple's move, worth copying exactly: it explained *why*
each character had to be drawn the way it was —

> "the image of a hearing aid would not be sufficiently distinctive at emoji scale; it needs to be shown
> with an ear in order to establish its identity."

For kidneys: propose the **pair**, as the paired silhouette is what reads at 18×18; a single bean is
ambiguous with a coffee bean 🫘. Say that explicitly — it demonstrates you tested the failure mode.

**5. Usage level** — the mandated evidence. See the protocol below. Screenshots, not assertions.

**6. Completeness** — "Does the proposed emoji fill a gap?" but note the trap:

> "The goal is iconic representation of large categories, not completeness in the sense of filling out
> the categories of a scientific or taxonomic classification system."

Unicode's examples of completeness are **closed** sets: the zodiac, blood types, card suits, three wise
monkeys. Organs are an open set. **Mark n/a.** Arguing completeness here invites the open-ended rejection.

**7. Compatibility** — needed for parity with Snapchat, X, QQ? *"Mark this as n/a unless there are
compelling examples."* n/a for all our concepts.

---

### Factors for Exclusion — the section that decides it

Head it, after Apple, **"Counterarguments to Factors for Exclusion."** Answer each by name.

**1. Already representable** — "Can the concept be represented by another emoji or sequence, even if the
image is not exactly the same?"

- Kidneys: no sequence conveys it. 🫀🫁 do not stand in for a kidney.
- Blood bag: 🩸 is bleeding, not donation. State the failure of the sequence 🩸➕🎒.
- Pill pack: this is where it dies. 💊 already carries it.

**2. Overly specific** — "🍣 sushi represents sushi in general … Adding saba, hamachi … would be overly
specific."

- Kidneys: an organ, not a subtype. Not analogous to a species of owl.
- CT scan: a specific machine; a subtype of medical imaging, which 🩻 already covers. Cut.

**3. Open-ended** — "Is it just one of many … will it result in the need to add other similar types? The
addition of one emoji is the exclusion of another."

**This is the factor that killed the fourteen-organ set.** Answer it the way Apple did:

> "we don't expect such discussion to lead to proposals for a large number of additions beyond the
> current proposal."

Concretely: name the boundary. The proposal covers the organs that are the subject of the most common
chronic disease conversations and transplantation; it does not open the door to the pancreas, gallbladder
and spleen, and we do not intend to propose them. **Say what you will not come back for.**

**4. Transient** — "could it just be a fad?" Chronic kidney disease, transplantation and dialysis are not
fads. Use Books Ngram's long baseline — it exists precisely to answer this factor.

**5. Faulty comparison** — "An existing emoji's existence does not justify proposals for emoji like them."

**Do not write "the heart and lungs were encoded, so the kidney should be."** That is the textbook faulty
comparison, and it is exactly how a medical-importance argument tends to be phrased. The heart and lungs
are context, never justification.

---

### Other information

Design considerations. The Copilot evidence belongs here and in Usage level. One paragraph pointing at
Document C.

---

## Evidence protocol

> "Please read this section and follow all the instructions; otherwise your proposal will likely be rejected."

Required for **each** emoji, each as a **screenshot**:

| Source | Requirement |
|---|---|
| Google Search | screenshot showing the **number of results** (click *Tools*; count appears far right) |
| Google Video Search | screenshot with the number of results (`tbm=vid`) |
| Google Trends: Web Search | `date=all`, widest range, **must include "elephant"** |
| Google Trends: Image Search | same, `gprop=images`, **must include "elephant"** |
| Google Books Ngram Viewer | 1500–2019, `corpus=en-2019`, `smoothing=3`, **must include "elephant"** |

### Search craft — each of these can sink the evidence

- **Hyphenate multiword terms.** `[blood-bag]`, `[pill-box]`, `[white-blood-cell]`, `[ct-scan]`.
  "Otherwise the search data you supply will likely be rejected."
- **Private/incognito window** for every capture, to strip personalisation.
- **Disambiguate with a category term.** `[scale]` is hopeless — it is a fish scale, a music scale, a
  balance. Use `[bathroom-scale]` or `[weighing-scale]`. For Trends, "use a qualifying category."
- **Search the object, not the phrase.** Apple: *"searching for 'person with wheelchair' … did not
  produce significant results."* Search `[kidney]`, never `[kidney emoji]`.
- **Record the capture window and method**, as Apple did: *"All data are from February and March 2018;
  each data item was obtained using a new private browser window."* Our packets never did this, and
  `docs/proposals/kidney-emoji-2026/previous-proposal-review.md` lists it as a top failure.
- **Other languages** if usage is stronger outside English. Kidney/dialysis: consider Spanish, Hindi,
  Arabic.

### Where the Copilot evidence goes

> Costa-Gomes B, Tolmachev P, … King D, Suleyman M. *Public use of a generalist LLM chatbot for health
> queries.* Nature Health 2026. doi:10.1038/s44360-026-00117-x
> Open preprint: <https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/copilot-health-usage-report.pdf>

Verbatim, from the preprint:

- *"nearly one in five conversations involve users describing their own symptoms, interpreting their own
  test results, or managing their own conditions"*
- *"across both condition information and symptom questions, one in seven conversations are on behalf of
  someone else, whether a child, an aging parent, or a partner"*
- *"The largest category, 'Health Information & Education,' accounts for over 40% of conversations."*
- *"over 500,000 de-identified health-related conversations with Microsoft Copilot from January 2026"*

**It is not the frequency evidence and it must not be presented as such.** It is not a petition, a
hashtag or an anecdote — it is legitimate, novel, reproducible platform data. But Unicode asked for five
specific sources, and it measures *how often people discuss health*, not *how often people would type a
kidney*. Conflating importance with usage is precisely how the 2022 packets died.

Placement:
- **Usage level** — mandated Google data first. Copilot second, as corroboration of communicative need:
  health is the topic people bring to a text interface most, at night, and on behalf of others.
- **Document C** — here it is the *primary* argument, because a category is about salience.

### And a warning about the "cause" framing

> "Please do not justify the addition of an emoji because it furthers a 'cause,' no matter how worthwhile.
> A proposal may be advanced **despite** a 'cause' argument … but will not be advanced **because of** it."

Apple's 2018 line — *"the most compelling factor for this proposal is not frequency of use … but the
desire to be inclusive in representation"* — is a cause argument. Apple won **despite** it. Do not copy
that sentence. Copy the structure, the counterarguments and the evidence discipline instead.

---

## Document C — health as a category

### There is no category submission form. There is a document channel.

The emoji form is explicitly the wrong door:

> "Do not submit emoji or character proposals to this address."
> "**Emoji proposals must be submitted only through the Unicode Emoji Submission Form.**"
> — <https://www.unicode.org/pending/docsubmit.html>

A category is neither. It is a change to a Unicode Technical Standard and its data, so it travels as a
**UTC document**, which is how the Emoji Subcommittee's own reports reach the committee.

**Mechanism** (all verbatim from docsubmit.html):

| Item | Requirement |
|---|---|
| Where | Email **docsubmit@unicode.org** — "to request that the document be added to the agenda" |
| Subject | `UTC Doc: <name of your topic>` — "Make sure you have the following format for the subject line" |
| Format | "Documents may be submitted in PDF or HTML format. The preferred document format is PDF." |
| Fonts | "**Font embedding is required:** Please embed all of your fonts … This is extremely important!" |
| First page | "must clearly identify the author or submitter, the subject, and the date of submission" |
| Deadline | "The deadline for document submissions which do not require pre-screening or further review is **seven days before the start of the meeting**" |
| Outcome | Unicode assigns an L2 number (`L2/26-nnn`) and the document becomes public in the register |

There is no prescribed template beyond the first-page rule. Model it on the ESC's own quarterly reports
(e.g. `L2/22-246`).

### The date that matters

**UTC #188 meets July 28–30, 2026, in Redmond, WA** (hybrid), per
<https://www.unicode.org/L2/meetings/utc-meetings.html>. The register does not name a host organization,
so do not assert that Microsoft hosts it — but Redmond is Microsoft's home ground and Rhew's colleagues
are on the board.

Seven days before July 28 is **2026-07-21**. That is **ten days before the emoji deadline**, and twelve
days from this spec.

Fallback: UTC #189, October 26–28, 2026, Nancy, France — deadline ~2026-10-19.

### The data itself lives in CLDR

`emoji-test.txt` states: *"The file is in CLDR order."* And UTS #51 §5 *Ordering and Grouping* says the
Emoji Ordering data *"has been incorporated into CLDR."*

So the change has two owners, and Document C should say so and address both:

1. **UTC / Emoji Standard & Research Working Group** — the policy decision, via the L2 document above.
2. **CLDR Technical Committee** — the data change, via a Jira ticket at
   <https://unicode-org.atlassian.net/projects/CLDR/> ("To file a ticket, click the red 'Create' button").

A third, weakest channel exists for spec comments: the UTS #51 reporting form,
<https://www.unicode.org/reporting.html>. Use it only to log the issue, not to carry the argument.

### The evidence

Evidence from Unicode's own data file, <https://unicode.org/Public/emoji/latest/emoji-test.txt>
(retrieved 2026-07-09):

- Ten top-level groups: Smileys & Emotion, People & Body, Component, Animals & Nature, Food & Drink,
  Travel & Places, Activities, Objects, Symbols, Flags. **None is health.**
- `medical` exists only as a **subgroup of `Objects`**, with **seven** members: 💉 🩸 💊 🩹 🩼 🩺 🩻
- Subgroup sizes: `medical` 7, `science` 7, `money` 11, `musical-instrument` 13, `tool` 27,
  `body-parts` 48.
- 🫀 anatomical heart and 🫁 lungs are **not** in `medical`. They sit in `People & Body body-parts`.

Argument: health is not merely under-served, it is **structurally homeless** — scattered across three
groups, with a seven-item drawer smaller than the one for musical instruments — while being the single
most common thing people bring to a conversational interface (Nature Health, 2026).

Audience: the Emoji Standard & Research Working Group, which recommends; the UTC votes.

---

## Risks

1. **Re-decline restarts the clock.** If Document B is judged ineligible and *declined*, that plausibly
   starts a fresh four-year bar — kidney to 2030. B is a separate PDF so an eligibility ruling cannot
   reach A.
2. **Eligibility is unresolved.** No public decline date exists for any emoji. **It exists in the private
   notification email Unicode sent the submitter ~Nov 2022. Search that mailbox before filing.**
3. **The licence is irrevocable and perpetual.** Microsoft Legal must clear it before art is commissioned.
4. **Artwork must be original and textless.** Existing candidate art fails on both counts.
5. **Saturation.** "fewer and fewer emoji proposals every year." Eleven concepts is not a strategy.
6. **22 days.** Five mandated screenshots × N concepts, plus four image files per concept, plus Legal.

---

## Phases

### Phase 1 — Eligibility and evidence (by 2026-07-14)
Search Shuhan's mail for the ~Nov 2022 Unicode notification; record the true decline date. Ask the working
group whether one submission may carry multiple emoji. Capture the five mandated sources for the final
slate, hyphenated, incognito, with `elephant`, logging the capture method.

**CHECKPOINT:** commit `evidence/` with screenshots and a capture log. If the decline email shows a
post-July date, Document B is dead this cycle. Say so at once and re-scope to Document A.

### Phase 2 — Artwork and licence (by 2026-07-20)
Microsoft design originates 18×18 and 72×72, colour and black & white, **no text of any kind**. Legal
clears the Emoji Proposal Agreement & License and the individual signatory.

**CHECKPOINT:** commit the image set; signatory named.

### Phase 2b — Document C, on its own clock (by 2026-07-21)
Document C is **not** gated on artwork, licences, or eligibility. It is a policy paper with the evidence
already in hand. Its deadline is **2026-07-21**, seven days before UTC #188 opens in Redmond — ten days
*earlier* than the emoji deadline.

**CHECKPOINT:** PDF with embedded fonts, first page naming author/subject/date, emailed to
docsubmit@unicode.org with subject `UTC Doc: Health as a Category in Emoji Ordering`. Record the assigned
L2 number. File the parallel CLDR Jira ticket.

### Phase 3 — Drafting (by 2026-07-24)
Write each proposal against the seven inclusion and five exclusion factors, in Unicode's order and words.
No cause arguments. No faulty comparisons to the heart and lungs.

**CHECKPOINT:** drafts committed. Run `/humanizer`; obey `reference_proposal_writing_rules`.

### Phase 4 — Review (by 2026-07-29)
Clinical review. Microsoft Legal and Comms. Rhew approves.

### Phase 5 — File (2026-07-30/31)
Host the PDFs publicly. Submit each through the form. Send Document C to the working group.

**CHECKPOINT:** confirmations archived. "All submitters will be notified … no later than November 30, 2026."

---

## Human gates

- [ ] Named individual submitter agreed (the form rejects company names)
- [ ] Microsoft Legal clears the irrevocable perpetual licence
- [ ] Decline-date email found, or a decision to file Document B without it
- [ ] Working group answers: one emoji per submission, or many?
- [ ] Final slate agreed (recommend five to six, not eleven)
- [ ] Public hosting location for the PDFs
- [ ] Partner organizations agree to be named
- [ ] **Document C emailed by 2026-07-21** (seven days before UTC #188) — earlier than the emoji deadline
- [ ] CLDR Jira account created and ticket filed for the ordering-data change
