# Winning Emoji Final Submission Specification

Status: ready to execute
Date: 2026-07-26
Target: one complete public PDF filed through the Unicode Emoji Submission Form by 2026-07-31
Proposal packet version on implementation: `v1.2.0` (MINOR)

## Decision

Prepare **Blood Pressure Cuff** as the sole 2026 candidate, but file it only after it passes every gate in this specification. It is a first-time eligible concept in the public status record (its only related entry, *Blood Pressure*, is expired), has a distinct medical function from the stethoscope, and is more defensible than a hospital bed.

**Do not file Hospital Bed.** The current strategy overlooked two existing emoji: `🛏️ bed` and `🛌 person in bed`. The sequence `🏥🛏️` already communicates a hospital bed, creating a direct already-representable objection. A submission that cannot defeat that sequence should not consume this filing window.

This is a probability-maximizing plan, not a promise of encoding. The project’s historical analysis puts first-time proposals at a 16% advance rate versus 5% for resubmissions; a complete, evidence-led first-time filing is the best available play.

## Objective

Make the reviewer reach this conclusion in the first two pages:

> A blood pressure cuff is a durable, high-frequency, globally understood object for measuring blood pressure; it cannot be conveyed precisely by current emoji; it is recognizable at emoji size; and encoding it does not require a family of near-duplicate medical devices.

The document must stand on that claim alone. Medical importance, disease burden, petitions, support letters, awareness, and the presence of other medical emoji are not the case for encoding.

## Evidence Basis

The repository’s controlled comparison of 55 encoded proposals and 29 unsuccessful proposals sets the working profile:

| Signal | Final-submission rule |
|---|---|
| Winners: 907 median words, 7 pages, 26 images | Target 800–1,100 words, 6–8 pages, and 20–28 purposeful figures/screenshots. Do not pad. |
| Winners answered faulty comparison 92% of the time | Name and defeat the strongest substitute sequence. |
| Winners use `N/A` where honest | Mark multiple meanings, completeness, and compatibility `N/A` unless evidence is genuinely compelling. |
| Losers overused social, petition, and advocacy material | Include none of it as evidence or rationale. |
| Current Unicode rules require five frequency screenshots | Capture all five in a private browser window; include `elephant` in both Trends and Ngram. |

The source documents are [`docs/plans/2026-07-09-winners-vs-losers.md`](../plans/2026-07-09-winners-vs-losers.md), [`docs/proposals/TEMPLATE-emoji-proposal.md`](../proposals/TEMPLATE-emoji-proposal.md), and the current Unicode guidance: https://www.unicode.org/emoji/proposals.html.

## Filing Gates

All gates are pass/fail. A failed gate means do not file this concept in 2026.

### 1. Eligibility and candidate gate

- [ ] Recheck the public Emoji Proposals Status sheet on the day of submission. Record the retrieval URL and date. The public list does not include auto-declined proposals, so absence is not proof of novelty; it is only the best available public screen.
- [ ] Confirm that no active `Under Consideration` or `Prioritization Pending` blood-pressure-cuff proposal is listed.
- [ ] Freeze one name: **Blood Pressure Cuff**. Do not expand the filing into monitor, sphygmomanometer, glucose meter, or another device.
- [ ] Confirm the proposed sort location against the current `emoji-test.txt` and Emoji Ordering data.

### 2. Frequency gate

- [ ] Capture Google Search and Google Video Search result-count screenshots with the `Tools` view visible.
- [ ] Capture Google Trends Web Search and Image Search using the widest range, a qualifying category, `blood-pressure-cuff` and `elephant` as comparisons, and a documented geography.
- [ ] Capture Google Books Ngram using the widest available range with `blood pressure cuff` and `elephant`.
- [ ] Use hyphenated multiword terms where Unicode requires Google search phrasing; record exact queries and raw URLs in the PDF.
- [ ] If the cuff has weak worldwide evidence, add a carefully translated supplementary query only where it improves reproducibility and represents a broad real-world language community.
- [ ] Add a capture statement: month/year, new private browser window, query, location/category, and widest date range.

**Pass condition:** the evidence establishes persistent, broad usage of the object term. Do not manipulate, hide, or explain away a weak comparison. If the candidate trails `elephant`, say so plainly and explain only a valid narrower signal, as successful Orca did.

### 3. Artwork and rights gate

- [ ] Commission or create original art under a written work-for-hire or assignment that gives the submitter all IP rights.
- [ ] Produce colour and black-and-white PNGs at exactly 18×18 and 72×72. Black-and-white must not be grayscale.
- [ ] Use one cuff, a short tube, and a simple bulb or gauge cue. The gauge must contain **no text, digits, logo, barcode, or brand-specific shape**.
- [ ] Test colour and black-and-white 18×18 art with at least 12 independent people, including at least eight non-clinicians. Show candidates alongside stethoscope, bed, thermometer, and pill; ask, without prompting, “What does this depict?”
- [ ] Record first response, confidence, and whether the response is cuff/blood-pressure measurement, another medical device, or unrecognizable.

**Pass condition:** at least 80% identify the colour glyph as a blood-pressure cuff or blood-pressure-measurement device; at least 65% do so in black and white. No more than 10% may call it a stethoscope, thermometer, generic medical device, or unreadable. If it needs numbers to read, it fails.

### 4. Vendor-support gate

- [ ] Obtain a written, attributable Microsoft statement that it anticipates supporting the proposed emoji in Segoe UI Emoji/Windows if Unicode encodes it.
- [ ] Name the signer, role, scope, and date; attach it as a short appendix or cite it precisely in `Other information`.
- [ ] Do not claim vendor support until the statement is received, and do not suggest Microsoft can determine the outcome.

This is differentiated supporting evidence, not a substitute for the selection factors.

### 5. Proposal and delivery gate

- [ ] Create a public PDF whose first page contains the title, individual submitter/point of contact, date, identification, four required images, and true licence statement.
- [ ] Host the PDF at a stable public HTTPS URL that works without login or cookies.
- [ ] Validate the final PDF on desktop and mobile: all figures readable, links resolve, images show at native 18×18 and 72×72, and no source-control or internal-package language appears.
- [ ] Submit only through https://forms.gle/6KSiYHrUdBkTMNaB8 and archive the confirmation, final URL, source, images, raw captures, and the signed rights record in a synchronized `submissions/v1.2.0/` packet.

## Required Narrative

Use the repository template’s order. The proposal is evidence with minimal connective prose, not a medical-advocacy essay.

1. **Identification:** `blood pressure cuff` short name; rich non-redundant search keywords; category and exact sort location.
2. **Four images and licence:** all top-of-first-page requirements, followed by a single true rights sentence.
3. **Thesis:** the one-sentence objective above, with no health-burden claim.
4. **Breaks new ground:** a cuff measures blood pressure; a stethoscope listens to sound. A hospital building, pill, syringe, or bed describes a setting, treatment, or furniture—not the measurement.
5. **Distinctiveness:** native-size strip plus the blinded-recognition result. Explain the visual cues that survive at 18×18.
6. **Use and sequences:** show only ordinary, interpretable messages such as `person + cuff` (checking a person’s pressure), `cuff + heart` (cardiovascular measurement), and `cuff + chart` (recording a reading). Do not imply standardized sequences.
7. **Frequency:** five required figures, raw URLs, method statement, and an honest two-sentence interpretation.
8. **Exclusions:**
   - Already representable: explicitly contrast cuff with stethoscope and representative current sequences.
   - Overly specific: define the cuff as the broad, globally used paradigm for blood-pressure measurement, not a branded instrument or model.
   - Open-ended: establish the boundary—this filing is for the ubiquitous blood-pressure measurement object, not a request for every diagnostic device; name glucose meter, thermometer, and pulse oximeter as devices not being proposed.
   - Transient: use Ngram and long-running public-health/home-use context, not pandemic or campaign evidence.
   - Faulty comparison: state that the request does not depend on other medical emoji being encoded.
9. **Other information:** concise, documented Microsoft anticipated-support statement and non-binding vendor design guidance.

## Production Schedule

| Date | Deliverable | Owner role |
|---|---|---|
| Jul 26 | Candidate and existing-emoji screen; statement request; artwork brief | Proposal lead / Microsoft liaison |
| Jul 27 | Five frequency captures; first art set; rights instrument | Evidence lead / art & IP lead |
| Jul 28 | Blinded 18×18 test; draft PDF; substitute and open-ended review | Independent QA / proposal lead |
| Jul 29 | Microsoft statement received; evidence interpretation and final art frozen | Microsoft liaison / proposal lead |
| Jul 30 | Public-PDF QA, external-reader review, public URL verification | QA lead |
| Jul 31 | Submit early; archive confirmation and the complete `v1.2.0` packet | Individual submitter |

An owner who cannot deliver by the date must declare the corresponding gate failed. Do not replace missing evidence with prose.

## Final Review Questions

Give the finished PDF to one non-clinical reader and one process-aware reviewer without introduction. It passes only if both can answer from the document:

1. What is the glyph at 18×18?
2. What common communication need does it serve?
3. Why do existing emoji and sequences not convey that need precisely?
4. Why would encoding it not require a flood of diagnostic-device emoji?
5. What reliable evidence demonstrates that the concept is durable and broadly used?

## Version Decision

This specification changes planning only. It does not alter the active `v1.1.0` kidney packet. Implementing the new concept is a synchronized **MINOR** packet release, `v1.2.0`, because the proposal scope, claims, evidence, artwork, and attachments all change together.
