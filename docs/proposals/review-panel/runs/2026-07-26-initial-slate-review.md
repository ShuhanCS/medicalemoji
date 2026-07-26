# Initial 2026 submission-slate panel review

Panel protocol: 1.0.0

Review date: 2026-07-26

Status: **INTERNAL RED TEAM COMPLETE - NO PROPOSAL CLEARED FOR FILING TODAY**

This is a simulated review based on public Unicode criteria and public expert work. It is not feedback,
endorsement, a recommendation, or an approval prediction from Unicode, ESR, UTC, Jennifer Daniel, Jennifer 8.
Lee, Ned Holbrook, or any other named person.

## Controlling public sources

- 2026 proposal requirements: https://www.unicode.org/emoji/proposals.html
- Emoji submission FAQ: https://www.unicode.org/faq/emoji_submission.html
- Proposal status meanings: https://www.unicode.org/emoji/emoji-proposals-status.html
- ESR remit: https://www.unicode.org/emoji/techindex.html
- Current Unicode technical group leadership: https://www.unicode.org/consortium/techcommittees.html
- Unicode technical group procedures: https://www.unicode.org/consortium/tc-procedures.html
- ESR priorities for Unicode 18.0 and beyond: https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf

## Frozen artifacts

| Proposal | Exact artifact | SHA-256 | Pages |
| --- | --- | --- | ---: |
| Kidney | `submissions/v1.12.0-kidney.2/kidney/kidney_emoji_proposal_SUBMIT.pdf` | `fff5de7f0bf5456bbf14de288862b066b4d35a478e10b5cdaf1810fa9a9ec2be` | 10 |
| White Blood Cell | `submissions/v1.8.0/white-blood-cell/white-blood-cell_emoji_proposal_DRAFT.pdf` | `2c360cc9c080805c16d27738fd0e2e45a4d4334ada447c217a6d15171f7c9b7f` | 5 |
| Stomach | `docs/proposals/stomach-emoji-2026/candidate-v1.12/stomach_emoji_proposal_CANDIDATE.pdf` | `01821a1eec18b294fd7fa1cc3e24eeba154f9694d1f4b754723ddbe7de20e18f` | 7 |
| Liver | `submissions/v1.12.0-liver.3/liver/liver_emoji_proposal_SUBMIT.pdf` | `3598642f0722358415ad5edc2fea5593d048981d9411b6bb2deb45408b43b5de` | 10 |
| Pill Pack | `submissions/v1.3.0/pill-pack/pill-pack_emoji_proposal_DRAFT.pdf` | `1fc930b14dbf894fb3a6d0a3e969eec36ebaa63abb0e6a7d0491fbbce53e2e55` | 5 |

All pages rendered without clipping, overlap, missing glyphs, or material layout breakage. Visual quality is
not the same as selection strength.

## Panel decision

| Rank | Proposal | Panel result on this artifact | Decisive reason |
| ---: | --- | --- | --- |
| 1 | Stomach | `STOP THIS CYCLE` unless written eligibility is obtained; otherwise `REVISE AND RERUN` and likely advance | Strongest prose, evidence, and image; 2022 decline timing and Shuhan's exact-asset approval remain open. |
| 2 | Kidney | `STOP THIS CYCLE` unless written eligibility is obtained; otherwise `REVISE AND RERUN` | Strong evidence, but the public PDF contains the exact machine-validation jargon that should remain internal and the 18x18 design is close to Lungs. |
| 3 | Liver | `STOP THIS CYCLE` unless written eligibility is obtained; otherwise `REVISE AND RERUN` | Complete packet, but the independent-use case and 18x18 recognition are not strong enough for the current 97/100 internal claim. |
| 4 | White Blood Cell | `REVISE AND RERUN` | Missing mandatory Trends evidence, stale Search/Video captures, uncited uses, unresolved authorship, and generic-cell recognition. |
| 5 | Pill Pack | `STOP THIS CYCLE` | PillPack brand contamination, incomplete evidence, weak independence from Pill combinations, and keypad-like art. |

The panel does not recommend filing any of these exact artifacts today. Stomach is the only near-ready content
case. Kidney is second after eligibility, art, and prose correction. Liver needs a more skeptical reset than
its readiness record currently indicates. White Blood Cell needs substantive work. Pill Pack should not consume
the current filing slot.

## Cross-slate hard blockers

### 1. Re-review eligibility is not documented

The official rule says an emoji declined within the last four years is not eligible for re-review. Repository
records show 2022 submissions for Kidney/KIDNEYS, Stomach, and Liver, and the project's decline-timing research
places the actual decision or notification in early November 2022. No written Unicode/ESR clarification or
exception is archived with the reviewed artifacts.

Shuhan's confirmation is the project decision to prepare the slate. It does not prove what date Unicode uses
for its four-year rule. Before filing any of the three organs, archive a written Unicode answer identifying the
controlling date and confirming eligibility for the 2026 window. Without it, stop those filings.

### 2. The organ proposals do not yet defeat the portfolio objection

"No emoji names this organ" applies equally to many missing organs. Each Open-ended section must explain why
this concept, on its own, has unusually broad ordinary messages, durable use, and recognizable art. Saying that
other organs can be reviewed separately does not answer why this one deserves one of a small number of annual
additions.

### 3. Internal QA is leaking into reviewer-facing prose

Kidney publicly reports connectedness, IoU `0.750`, a `0.72` threshold, dHash `23`, and an unfinished semantic
computer comparison. Delete that paragraph. Hashes, algorithms, thresholds, and validation gates belong in
internal readiness records. The public proposal should state only what a reviewer can see at actual size.

Across the slate, replace `paradigm`, `semantic building block`, `semantic gap`, `medial hila`, and `inner
concavity` with ordinary language.

### 4. Authorship must be exact but page 1 must stay concise

- Kidney keeps its verified ten-person semicolon-separated list, but removes consent commentary, job titles,
  affiliation verification, and source links from the proposal header.
- Stomach keeps Shuhan He; David Rhew; Heena Purohit, with Shuhan as main contact.
- Liver changes the formal line to `Submitters: Shuhan He; David Rhew; Heena Purohit`, with Shuhan as main
  contact. It removes affiliations from the reviewer-facing header.
- White Blood Cell and Pill Pack must use their own current consent records. Neither may default to Shuhan alone
  merely because he is the contact or rights certifier.

### 5. Shuhan's art approval and the proposal panel are separate

Shuhan alone approves the exact four final artwork assets at actual size. No crowd study or participant panel
is required. This five-seat proposal panel reviews the complete filing argument and PDF; it does not replace or
expand the human image-approval requirement.

## Proposal-agent feedback

### Kidney

Strongest one-sentence case: Kidney identifies the organ in messages about tests, dialysis, donation, and
transplantation where Beans and general medical emoji cannot name the body part.

Strongest decline case: the candidate may be ineligible, its 18x18 pair can read as Lungs, and its own public
proposal announces a failed internal geometric check.

Keep:

- the Beans-versus-organ rebuttal;
- the five frequency exhibits;
- cited direct uses such as dialysis, donation, and transplant; and
- the verified ten-person author list in one concise line.

Actions:

| ID | Severity | Change | Owner | Acceptance condition | Rerun |
| --- | --- | --- | --- | --- | --- |
| K-01 | BLOCKER | Obtain written Unicode/ESR clarification of four-year eligibility. | Coordinator | Dated response is archived and explicitly covers the 2026 Kidney filing. | Intake, UTC |
| K-02 | BLOCKER | Remove the full connectedness/IoU/dHash/threshold/semantic-computer paragraph from Distinctiveness. | Kidney proposal agent | No machine-validation term or unresolved internal gate remains in the PDF. | Selection, mentor |
| K-03 | MAJOR | Simplify the 18x18 color and monochrome design so it reads as Kidney, not Lungs or Beans. | Kidney art agent, then Shuhan | Exact four assets pass technical checks and receive Shuhan's dated actual-size approval. | Visual, selection |
| K-04 | MAJOR | Replace anatomical wording with: "Two offset kidney shapes with short connecting tubes distinguish the image from Beans and Lungs." | Kidney proposal agent | No `paradigm`, `medial hila`, or unexplained anatomy remains. | Mentor |
| K-05 | MAJOR | Mark Multiple meanings `N/A` unless a durable figurative meaning beyond `kidney-shaped` and `kidney bean` is sourced. | Kidney proposal agent | The section is honest and citation-backed. | Selection |
| K-06 | MAJOR | Make Open-ended explain Kidney-specific ordinary demand rather than merely denying an anatomy set. | Kidney proposal agent | The answer states why Kidney has priority over other missing organs. | Selection, UTC |
| K-07 | MINOR | Move affiliations, roles, verification links, and consent commentary to the internal author ledger. | Kidney proposal agent | Page 1 retains only required submitters/contact/date metadata. | Intake |

### White Blood Cell

Strongest one-sentence case: White Blood Cell would identify the body's immune cell, which Microbe, Drop of
Blood, Shield, and laboratory emoji cannot express.

Strongest decline case: the PDF is incomplete and the artwork requires foreknowledge to read as a leukocyte
rather than a generic cell, germ, flower, gear, or camera lens.

Keep:

- the broad leukocyte rather than subtype framing; and
- the direct comparison with Microbe and Drop of Blood.

Actions:

| ID | Severity | Change | Owner | Acceptance condition | Rerun |
| --- | --- | --- | --- | --- | --- |
| W-01 | BLOCKER | Recapture all five sources; use `white-blood-cell` for Search/Video and `elephant` in both widest-range Trends captures. | Evidence agent | Five current, legible, reproducible screenshots are embedded; no petri-dish comparator or draft note remains. | Intake, selection |
| W-02 | BLOCKER | Reconfirm the concept-specific author list. | Coordinator | Current consent record, PDF, and form draft agree; no sole-author default was applied. | Intake |
| W-03 | MAJOR | Mark Multiple meanings `N/A`; cite or delete clinical, education, and research uses. | WBC proposal agent | Every retained claim has a durable citation and the heading matches the current factor. | Selection, mentor |
| W-04 | MAJOR | Enlarge and simplify the three-lobed nucleus, reduce peripheral circles, and strengthen the irregular membrane. | WBC art agent, then Shuhan | At 18x18 the intended cell is distinguishable from Microbe, Bubbles, and generic cell art; Shuhan approves the exact assets. | Visual, selection |
| W-05 | MAJOR | Explain why a neutrophil-like drawing represents the general leukocyte category. | WBC proposal agent | Name and drawing no longer conflict without explanation. | Visual, UTC |
| W-06 | MAJOR | Replace the indirect CC0 sentence with a direct rights warranty by the authorized submitter. | WBC proposal agent | Page 1 contains the required ownership/open-license grant. | Intake |
| W-07 | MINOR | Recheck category and sort location against current emoji ordering; do not state Drop of Blood is in body-parts if it is not. | WBC proposal agent | Category and neighbor match the current data. | Visual |

### Stomach

Strongest one-sentence case: Stomach identifies the body part behind everyday messages about hunger, fullness,
nausea, digestion, and established figurative expressions, while food and face emoji identify only the meal or
feeling.

Strongest decline case: it may still be ineligible under the four-year rule, and several health uses and final
art approval are not yet documented.

Keep:

- the current five-source evidence;
- the literal plus figurative meaning case;
- the J-shaped artwork direction; and
- the direct food/face substitute comparison.

Actions:

| ID | Severity | Change | Owner | Acceptance condition | Rerun |
| --- | --- | --- | --- | --- | --- |
| S-01 | BLOCKER | Obtain written Unicode/ESR clarification of four-year eligibility. | Coordinator | Dated response is archived and explicitly covers the 2026 Stomach filing. | Intake, UTC |
| S-02 | BLOCKER | Review the exact four assets and comparison boards with Shuhan. | Shuhan | Dated `APPROVE` tied to final SHA-256 hashes, or revised assets return to review. | Visual |
| S-03 | MAJOR | Cite or remove reflux, indigestion, medication, stomach bug, treatment, and any unsupported idiom. | Stomach proposal agent | Every retained medical or figurative use is cited. | Selection, mentor |
| S-04 | MINOR | Replace technical art language with "recognizable J shape, inlet, open curve, and outlet." | Stomach proposal agent | No `paradigm`, `semantic building block`, or `inner concavity` remains. | Mentor |
| S-05 | MINOR | Lead Open-ended with Stomach's daily food, sensation, and figurative uses; cut vague sequences such as Stomach + Hospital. | Stomach proposal agent | The section explains independent priority in one short paragraph. | Selection, UTC |

If S-01 and S-02 close and the small prose actions are completed, this is the panel's first candidate for
`RECOMMEND ONWARD`.

### Liver

Strongest one-sentence case: Liver identifies the organ in messages about tests, medication monitoring,
donation, and transplant where Hospital and Test Tube can express care but not the body site.

Strongest decline case: every missing organ has clinical uses, while this image can read as meat, a leaf, or a
generic organ at 18x18 and the reported Search evidence is anomalously weak.

Keep:

- the five-source structure, subject to Search recapture;
- `N/A` for Multiple meanings, Completeness, and Compatibility; and
- the concise substitute discussion.

Actions:

| ID | Severity | Change | Owner | Acceptance condition | Rerun |
| --- | --- | --- | --- | --- | --- |
| L-01 | BLOCKER | Obtain written Unicode/ESR clarification of four-year eligibility. | Coordinator | Dated response is archived and explicitly covers the 2026 Liver filing. | Intake, UTC |
| L-02 | BLOCKER | Change the formal header to all three confirmed submitters; remove affiliations and job titles. | Liver proposal agent | `Submitters: Shuhan He; David Rhew; Heena Purohit` and `Main point of contact: Shuhan He` appear, matching the consent record. | Intake |
| L-03 | MAJOR | Recapture and verify the Google Search result; the current approximately 183,000 result conflicts sharply with Video Search. | Evidence agent | Private-window screenshot, query, date, and count are legible and reproducible. | Intake, selection |
| L-04 | MAJOR | Make the silhouette more wedge-shaped, shorten the internal seam, and make the gallbladder a small attached oval rather than a dangling mark. | Liver art agent, then Shuhan | Monochrome 18x18 does not read as a leaf/slashed oval; Shuhan approves the exact assets. | Visual, selection |
| L-05 | MAJOR | Cite or remove food, education, donation, and other unsupported uses. | Liver proposal agent | Every retained material claim is cited. | Selection, mentor |
| L-06 | MAJOR | Explain why Liver has independent priority over pancreas, spleen, and other unencoded organs. | Liver proposal agent | Open-ended answers the actual portfolio objection, not only the anatomy-set claim. | Selection, UTC |
| L-07 | MINOR | Replace `semantic building block`, `paradigm`, and similar internal language with concrete messages and visible features. | Liver proposal agent | An educated general reader can read the section once without definitions. | Mentor |

### Pill Pack

Strongest possible case: a medication blister could show sealed doses and remaining supply, which a single Pill
does not depict.

Strongest decline case: Pill plus Calendar, Package, Check Mark, or a number covers most proposed messages;
the current name collides with Amazon's PillPack brand; and the 18x18 art resembles a keypad or remote.

Actions:

| ID | Severity | Change | Owner | Acceptance condition | Rerun |
| --- | --- | --- | --- | --- | --- |
| P-01 | BLOCKER | Do not file or continue under `Pill Pack`. Run a fresh go/no-go under generic `Blister Pack` or `Medication Blister Pack`. | Coordinator | Trademark/name and concept decision is recorded before any proposal polishing. | ALL |
| P-02 | BLOCKER | Discard the old frequency package and separate generic blister-pack demand from the PillPack company. | Evidence agent | Five current, hyphenated-query exhibits are uncontaminated and complete. | Intake, selection |
| P-03 | BLOCKER | Test every claimed message against Pill plus Calendar, Package, Check Mark, and numbers. | Pill Pack proposal agent | A written substitute matrix shows a material remaining meaning, or the concept is stopped. | Selection, UTC |
| P-04 | MAJOR | Compare directly with Pill Box and advance at most one medication-container concept. | Coordinator | One go/no-go decision is recorded; no draft treats Pill Box as encoded. | UTC |
| P-05 | MAJOR | If retained, try an angled blister with medication-shaped wells and one empty cavity. | Art agent, then Shuhan | The 18x18 image reads as medication packaging without text, logos, or context; Shuhan approves it. | Visual |
| P-06 | MAJOR | Mark Multiple meanings `N/A` and cite any global-packaging claims. | Proposal agent | No literal packaging function is mislabeled as metaphor/symbolism. | Selection, mentor |

Current panel decision: `DO NOT ADVANCE`. Reframing creates a new concept review; it does not preserve this
artifact's work or verdict.

## Coordinator handoff order

1. Ask the narrow eligibility question for Kidney, Stomach, and Liver and archive the answer.
2. Stop Pill Pack; decide whether a new Blister Pack go/no-go is worth opening.
3. Fix Stomach's citations and obtain Shuhan's final image approval.
4. Remove Kidney's machine-validation prose and resolve Lungs ambiguity.
5. Rebuild White Blood Cell evidence and art before additional prose polishing.
6. Reset Liver's byline, Search evidence, independent-use argument, and 18x18 art.
7. Generate a new hash-bound panel dossier for each changed PDF and rerun all affected seats.

No prior readiness score overrides the blockers in this report.
