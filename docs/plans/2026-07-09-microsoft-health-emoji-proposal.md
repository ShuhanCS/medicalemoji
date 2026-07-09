# Spec: Microsoft-submitted health emoji proposal, 2026 cycle

Status: DRAFT SPEC — not approved, not filed
Author: drafted 2026-07-09
Deadline: **2026-07-31**, the close of the Unicode emoji submission window (22 days from drafting)

## Decisions taken

| Decision | Choice |
|---|---|
| Target cycle | File the whole set in the 2026 window |
| Submitter | `Submitter: Microsoft Corporation`, partners credited in the body (Apple's shape) |
| Category ask | Two documents: the emoji proposal, and a separate category paper to the working group |

## Template

Apple's [L2/18-080](https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf) is the structural
model. Unicode's **current** requirements govern the actual form; the 2018 lettering (A–K) is obsolete.
Current source: <https://unicode.org/emoji/proposals.html>

Submission is **not** a document sent to Unicode. It is a form:

> "Provide a **link** to your proposal document (PDF required) using the Unicode Emoji Submission Form."
> "Your PDF link needs to be publicly accessible. Email, FAX, or hard copies are not acceptable."

Form: <https://forms.gle/6KSiYHrUdBkTMNaB8>

---

## Deliverables

- **Document A** — `Proposal for New Health Emoji`. The clean set. Filed via the form.
- **Document B** — `Proposal for Health Emoji: Organs`. Kidney, liver, stomach. Filed separately, same
  window. **Separated deliberately** — see Risks.
- **Document C** — `Health as a Category in Emoji Ordering`. A short paper to the Emoji Standard &
  Research Working Group. Not a proposal, not filed through the form.

---

## Set composition and the eligibility ledger

The rule: *"Emoji declined within the last four years are not eligible for re-review."*
(<https://unicode.org/emoji/proposals.html>). Unicode publishes only the **submission** date; the
decline lands at cycle end. See `docs/presentations/2026-07-09-microsoft-brief/README.md` for the full
derivation.

### Document A — clear to file (8 concepts)

| Concept | Last submitted | Status | Bar |
|---|---|---|---|
| White blood cell | 2020-12-18 | Declined | lapsed ~2025 |
| Pill pack | 2020-12-18 | Declined | lapsed ~2025 |
| Pill box | 2020-10-27 | Declined | lapsed ~2025 |
| Blood bag | 2020-12-18 | Declined | lapsed ~2025 |
| Leg cast | 2020-12-18 | Declined | lapsed ~2025 |
| IV bag | 2020-12-18 | Declined | lapsed ~2025 |
| CT scan | 2020-12-18 | Declined | lapsed ~2025 |
| Weight scale | 2020-12-18 | Declined | lapsed ~2025 |

Optional ninth: **Inhaler** (declined 2018-07-03; bar long lapsed; never part of the 14).

### Document B — arguable (3 concepts)

| Concept | Submitted | Clears under submission clock | Clears under decline clock |
|---|---|---|---|
| Kidney | 2022-07-19 | 2026-07-19 — **12 days before deadline** | ~Nov 2026 — misses |
| Stomach | 2022-07-28 | 2026-07-28 — **3 days before** | ~Nov 2026 — misses |
| Liver | 2022-07-30 | 2026-07-30 — **1 day before** | ~Nov 2026 — misses |

### EXCLUDED — no argument exists (3 concepts)

**Spine, intestines, ECG.** Submitted 2024-04-04/05. Barred until 2028 under *either* clock. Filing
them invites summary dismissal. Do not include them.

---

## Document A skeleton

Section headings mirror Unicode's current required fields, in order.

1. **Title** — `Proposal for New Health Emoji`
2. **Submitter** — `Microsoft Corporation`, with the main point of contact identified.
   Body credits, in Apple's exact idiom ("Developed in collaboration with…"): Massachusetts General
   Hospital, Shuhan He MD, ACEP, AGA, the International Society of Nephrology.
3. **Date** — must be updated on every revision.
4. **Identification** — per concept:
   - CLDR short name
   - Keywords. *"Do not repeat the name of the emoji. Consider terms that people would use to find this emoji."*
   - **Category**: `Objects > medical` (the category that exists today — see Document C).
5. **Images** — *"Example color and black & white images must be included at the top of your proposal
   with dimensions of 18×18 and 72×72 pixels."* Colour ✅, black & white ✅, **grayscale ❌**.
6. **License** — the Submitter warrants it owns the IP, *or* identifies the source and warrants public
   domain / open-source licensing. **Microsoft Legal gate.** The 14 existing candidate PNGs in the
   brief deck have unclear provenance and almost certainly cannot be used.
7. **Factors for Inclusion** — all seven, in Unicode's order:
   1. Multiple meanings
   2. Use in sequences
   3. Breaks new ground
   4. Distinctiveness
   5. Usage level  ← the frequency evidence lives here
   6. Completeness
   7. Compatibility
8. **Factors for Exclusion** — a section headed, after Apple, **"Counterarguments to Factors for
   Exclusion"**, answering each by name:
   1. Already representable
   2. Overly specific
   3. Open-ended
   4. Transient
   5. Faulty comparison
9. **Other information** — design considerations; the Copilot evidence; the category argument in brief.

### Per-concept exclusion risk to pre-rebut

| Concept | The exclusion it will trip | Required counterargument |
|---|---|---|
| Pill pack, pill box | Already representable (💊 pill) | A blister pack / weekly organizer denotes *adherence and regimen*, not a dose |
| Blood bag | Already representable (🩸 drop of blood) | Donation and transfusion vs. bleeding |
| IV bag | Already representable (💉 syringe) | Infusion over time vs. injection |
| Leg cast | Already representable (🩼 crutch) | Immobilization vs. mobility aid |
| CT scan, weight scale | Distinctiveness at 18×18 | Must show the 18×18 renders; a CT gantry may read as a grey ring |
| The whole set | **Open-ended** | Apple's move, verbatim in spirit: state that the set is a starting point, not a taxonomy |

---

## Evidence protocol — read this before gathering anything

Unicode **mandates** these sources, each as a **screenshot**, for every proposed emoji:

1. Google Search
2. Google Video Search
3. Google Trends: Web Search
4. Google Trends: Image Search
5. Google Books Ngram Viewer

And: *"include 'elephant' as a comparative search term."*

And, disqualifying: *"Petitions, hashtags on social media, and anecdotal evidence are not acceptable
data, and will not be considered."*

### What this means for the Copilot evidence

The Nature paper is powerful and it is **not** the frequency evidence.

> Costa-Gomes B, Tolmachev P, … King D, Suleyman M. *Public use of a generalist LLM chatbot for health
> queries.* Nature Health, 2026. doi:10.1038/s44360-026-00117-x
> Open preprint: <https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/copilot-health-usage-report.pdf>

Verbatim, from the preprint:

- *"nearly one in five conversations involve users describing their own symptoms, interpreting their own
  test results, or managing their own conditions"*
- *"across both condition information and symptom questions, one in seven conversations are on behalf of
  someone else, whether a child, an aging parent, or a partner"*
- *"The largest category, 'Health Information & Education,' accounts for over 40% of conversations."*
- Prior work: *"health-related queries on consumer Microsoft Copilot were the most prevalent topic
  category on mobile."*
- Dataset: *"over 500,000 de-identified health-related conversations with Microsoft Copilot from January
  2026"*; global, ~22% US, ~45% English.

It proves **people talk about health constantly**. It does not prove **anyone would type a kidney
emoji**. Those are different claims, and the 2022 packets died by conflating importance with usage.

Placement:
- **Usage level (inclusion factor 5)** — mandated Google data first, as the evidence Unicode asked for.
  Copilot data second, as corroboration of the *communicative need*: health is the topic people bring to
  a text interface most, at night, and on behalf of others.
- **Document C** — the Copilot data is the *primary* argument, because a category is about salience.

### Capture discipline — steal this from Apple

> *"All data are from February and March 2018; each data item was obtained using a new private browser
> window."*

State the capture window and method. Our packets never did; `previous-proposal-review.md` lists
"missing reproducible frequency evidence" as a top failure.

### Frequency by proxy — also from Apple

> *"searching for 'person with wheelchair' or 'person with white cane' did not produce significant results"*

So Apple searched the **object** — "wheelchair", "prosthetic" — and benchmarked each against terms for
**existing** emoji. Do the same: search `kidney`, `IV bag`, `blister pack`. Never `kidney emoji`.

---

## Document C — health as a category

Evidence, straight from Unicode's own data file
(<https://unicode.org/Public/emoji/latest/emoji-test.txt>, retrieved 2026-07-09):

- Ten top-level groups exist: Smileys & Emotion, People & Body, Component, Animals & Nature, Food &
  Drink, Travel & Places, Activities, Objects, Symbols, Flags. **None is health.**
- `medical` exists only as a **subgroup of `Objects`**, containing **seven** emoji:
  💉 syringe, 🩸 drop of blood, 💊 pill, 🩹 adhesive bandage, 🩼 crutch, 🩺 stethoscope, 🩻 x-ray.
- Sizes for comparison: `medical` 7, `science` 7, `money` 11, `musical-instrument` 13, `tool` 27,
  `body-parts` 48.
- The anatomical heart 🫀 and lungs 🫁 — the two medical emoji this project already landed — are **not**
  in `medical`. They sit in `People & Body > body-parts`.

The argument: health is not under-served, it is **structurally homeless**. It is scattered across
`Objects`, `People & Body`, and `Smileys & Emotion`, with a seven-item drawer smaller than the one for
musical instruments. Meanwhile it is the single most common thing people bring to a conversational
interface.

Audience: the Emoji Standard & Research Working Group (recommends), then the UTC (votes). This is a
data/ordering change, not a character proposal — it does not go through the submission form.

---

## Risks

1. **Re-decline restarts the clock.** If Document B is judged ineligible and *declined*, that plausibly
   starts a fresh four-year bar — kidney to 2030. This is the single largest downside of filing organs
   now, and it is why B is a separate PDF: an eligibility ruling on B must not reach A.
2. **Eligibility is unresolved.** No public decline date exists for any emoji (UTC #173 minutes carry
   none; the ESC report was oral). **The decline date is in the private notification email Unicode sent
   the submitter in ~Nov 2022. Search that mailbox before filing.** It settles this outright.
3. **IP on the artwork.** Every image needs a warranty. Existing candidate art is unlikely to qualify.
   Microsoft design must originate it, or it must be provably open-source.
4. **Open-ended.** Eight to eleven concepts at once reads as a taxonomy unless explicitly disclaimed.
5. **22 days.** Google evidence × 8–11 concepts × 5 sources = 40–55 screenshots, plus 18×18 and 72×72
   colour and B&W art × 11, plus Microsoft Legal. This is the binding constraint, not the writing.

---

## Phases

### Phase 1 — Evidence and eligibility (by 2026-07-14)
Search Shuhan's mail for the ~Nov 2022 Unicode notification and record the actual decline date. Gather
the mandated Google evidence for all 8 clear concepts, with `elephant` as comparator, capture method
recorded. Pull the verbatim Copilot statistics with page references.

**CHECKPOINT:** commit `evidence/` with screenshots and a capture log. If the decline email surfaces and
shows a post-July-31 date, Document B is dead for this cycle — say so immediately and re-scope.

### Phase 2 — Artwork and IP (by 2026-07-20)
Microsoft design originates 18×18 and 72×72, colour and black & white, per concept. Legal executes the
License warranty.

**CHECKPOINT:** commit the image set; License section drafted and countersigned.

### Phase 3 — Drafting (by 2026-07-24)
Write Document A against the seven inclusion and five exclusion factors, in Unicode's order, in
Unicode's words. Write Document B with an explicit, non-defensive eligibility section. Write Document C.

**CHECKPOINT:** commit all three drafts. Run `/humanizer`. No em dashes, no "not X but Y" (see
`reference_proposal_writing_rules`).

### Phase 4 — Review (by 2026-07-29)
Clinical review (Shuhan, societies). Microsoft Legal and Comms sign-off. Rhew approves.

**CHECKPOINT:** signed approvals recorded.

### Phase 5 — File (2026-07-30 / 07-31)
Host Documents A and B as publicly accessible PDFs. Submit each through
<https://forms.gle/6KSiYHrUdBkTMNaB8>. Send Document C to the Emoji Standard & Research Working Group.

**CHECKPOINT:** submission confirmations archived. Note: *"All submitters will be notified of the status
of their document no later than November 30, 2026."*

---

## Human gates

- [ ] Rhew confirms Microsoft Corporation as submitter
- [ ] Microsoft Legal clears the License warranty and the use of Copilot data
- [ ] Decline-date email found, or a decision made to file Document B without it
- [ ] Public hosting location agreed for the PDFs
- [ ] Partner organizations agree to be named
