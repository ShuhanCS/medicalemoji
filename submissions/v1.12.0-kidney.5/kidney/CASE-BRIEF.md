# Kidney Selection Case Brief

Case-brief version: 1.1.0

Review date: 2026-07-26

Active package: `1.12.0-kidney.5`

Status: **CASE READY**

This is an internal reasoning record. It is not proposal prose and must not be included in the submission PDF.

## Phase 1 - Frozen candidate

| Field | Frozen value |
| --- | --- |
| Source package | `submissions/v1.12.0-kidney.3/` |
| Source package version | `1.12.0-kidney.3` |
| Freeze commit | `226ca7158b19a7d9bd5c794bd563e10ce6092c8d` |
| Proposal source | `submissions/v1.12.0-kidney.3/kidney/kidney_emoji_proposal_SUBMIT.md` |
| Proposal-source SHA-256 | `2245adde5f9b0e42b4d9fe5f2b821a19095e3fbe366f43eaee4befd901ec5523` |
| Reviewer-facing PDF | `submissions/v1.12.0-kidney.3/kidney/kidney_emoji_proposal_SUBMIT.pdf` |
| PDF SHA-256 | `be5623599d621d0f1ad0266bd8cb88e8acf04147634f41b5bca8ddf25ef02d68` |
| Official-guidance check | 2026-07-26; https://www.unicode.org/emoji/proposals.html |
| Prior-status source | `docs/research/2022-organ-decline-notifications.md`; https://www.unicode.org/emoji/emoji-proposals-status.html |
| Exact-hash panel | `docs/proposals/review-panel/runs/2026-07-26-kidney-v1.12.0-kidney.3.md` |

### Frozen artwork

| Asset | SHA-256 |
| --- | --- |
| `images/kidney_color_18x18_SUBMIT.png` | `fa12aea97659461d22b0dda82cd0257005b14b53bb05e4af1816ba56049daacb` |
| `images/kidney_color_72x72_SUBMIT.png` | `a32d298c9563185410ae65d8a8777d5ca6c5e20e6a7ddc3bd8852405c75983cf` |
| `images/kidney_bw_18x18_SUBMIT.png` | `360b899469daf402b9f96de6b89fc46d28605a4ff2c3059d03c5ce78d0145478` |
| `images/kidney_bw_72x72_SUBMIT.png` | `87c945f86fff9b34571dba8291ce17a983cb198f29c958fa747a22f875211b22` |

### Identity, authorship, and rights

The controlling concept is the human kidney represented by a paired-kidney paradigm. The proposed short name
is singular `Kidney`; the relationship to the prior public `KIDNEYS` entry must be made explicit before filing.

Preserve all confirmed authors in this order:

Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee; Danielle Miller;
Timur Erk; David Rhew; Heena Purohit.

Shuhan He remains the main point of contact. The current consent source is the project-owner confirmation
recorded in `submissions/v1.12.0-kidney.3/kidney/READINESS.md`. David Rhew and Heena Purohit must remain authors.

Image rights are controlled by the direct warranty on PDF page 1 and
`submissions/v1.12.0-kidney.3/ARTWORK-LICENSE.md`. The warranty covers the four frozen project-authored assets;
any artwork change requires renewed asset hashes, rights reconciliation, and Shuhan's dated approval.

### Prior decisions and unresolved blockers

- The exact-hash five-seat panel returned `STOP THIS CYCLE`: one compliance seat stopped on eligibility and
  four seats required a substantive/artwork rerun.
- The repository records a Unicode status notice dated 2022-11-04, while the 2026 intake closes 2026-07-31 and
  the current guidance excludes concepts declined within the last four years. Shuhan reports that Unicode
  considers Kidney eligible, but the record must reconcile that confirmation with the dated notice.
- Duplicate-filing coordination remains open.
- The final PDF is not yet published at a logged-out HTTPS URL and no official form record exists.
- The color 18x18 asset has normalized silhouette IoU `0.750` against Lungs, above the predeclared `0.72`
  ceiling. The threshold must not be weakened.
- The `.3` proposal uses generic domain lists and rubric language rather than observed Kidney-specific
  communication.
- The current Use in sequences and Open-ended answers did not pass the exact-hash panel.
- All five required frequency captures are present and readable; no recapture is currently indicated unless
  later reproduction shows a changed or noncompliant setting.

### Relevant accepted-proposal exemplars

| Exemplar | Lesson used for Kidney | Full source |
| --- | --- | --- |
| Lighthouse | Complete current structure, direct `N/A`, readable evidence, and serious exclusions | https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf |
| Fingerprint | Fair nearest-substitute analysis and reproducible evidence | https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf |
| Treasure Chest | Concrete meanings and a concise case rather than abstract versatility claims | https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf |
| Orca | Concede a weak comparison instead of hiding it | https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf |

Meteor is not a compatibility model for Kidney because no high-use popular system using the same kidney
pictograph has been established: https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf

## Phase 2 - Case construction

### Selection thesis

Kidney merits an emoji because the organ anchors established messages - kidney stone, kidney tests, dialysis,
kidney transplant, and living donation - that Beans or generic medical emoji cannot identify, while its paired,
notched form supplies a bounded pictograph.

### Observed communication

| Observed phrase or instruction | Communication setting | Evidence |
| --- | --- | --- |
| `kidney stone` and `kidney stone analysis` | A patient collects a passed stone and returns it to a provider or laboratory for analysis. | https://medlineplus.gov/lab-tests/kidney-stone-analysis/ |
| `kidney tests`, `kidney function tests`, and `kidney panel` | Patients and clinicians discuss blood, urine, and imaging tests that check kidney function. | https://medlineplus.gov/kidneytests.html |
| `I want to have a kidney transplant` | NIDDK instructs a patient to tell a doctor or nurse that they want a kidney transplant; a transplant team then evaluates, tests, lists, and follows the patient. | https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/kidney-transplant |
| `donate a kidney`, `living donor`, and `kidney paired donation` | Donors, recipients, families, and transplant programs discuss donating one kidney, matching, and paired exchange. | https://www.hrsa.gov/optn/patients/organ-donation/living-donation and https://www.hrsa.gov/optn/patients/kidney-paired-donation-for-patients |
| dialysis as kidney-replacement treatment | Patients, families, and care teams choose among hemodialysis, peritoneal dialysis, and kidney transplant; dialysis replaces part, not all, of kidney function. | https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/choosing-treatment and https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/hemodialysis |

These are established names and patient-facing instructions. The proposal does not claim that a Kidney emoji
would replace the medical words, a diagnosis, or informed clinical communication; it would provide the missing
literal organ in the same informal pictographic layer where Rock, Test Tube, Hospital, and other concepts
already exist.

### Nearest-substitute analysis

`Beans` (🫘) is the strongest single substitute. Unicode names it `beans`, places it in Food & Drink, and includes
`kidney` among its search keywords. That keyword is a real advantage: a user searching the keyboard for
`kidney` may find Beans. It is nevertheless a food pictograph, not a kidney pictograph.

`Beans + Hospital` (🫘🏥) is the strongest short general-purpose sequence. With shared context it can suggest
kidney care, but without that context it also reads as food, diet, or beans at a hospital. The same residual
ambiguity survives in the two strongest phrase-specific attempts: `Beans + Rock` reads literally as beans and
a rock rather than naming `kidney stone`, and `Beans + Test Tube` does not name `kidney tests`. Generic medical
emoji can supply care or testing, but none supplies the organ noun.

Sources: https://unicode.org/emoji/charts/emoji-list.html and
https://unicode.org/emoji/charts/full-emoji-list.html

### Priority and scope

The closest unencoded neighbors are Liver, Stomach, Pancreas, and Spleen. Raw English Books frequency does not
put Kidney first: over 2013-2022, `stomach` and `liver` are above `kidney`, while `kidney` is above `pancreas`
and `spleen`. `liver transplant` is also slightly above `kidney transplant`. Those are concessions, not reasons
to reorder Unicode by word count.

Kidney's bounded case is the combination of three conditions: the literal organ noun anchors multiple
established messages in unrelated activities; the strongest existing pictograph remains a food item even when
retrievable by `kidney`; and the missing noun creates concrete sequence gaps for `kidney stone` and `kidney
tests`. Kidney is unusually supported by the combined stone + testing + dialysis + donation/transplant cluster.
Liver shares transplantation and donation; it does not share the kidney-stone and dialysis conventions.
Stomach has higher raw word frequency; it does not share that cluster. Pancreas and Spleen must likewise stand
on their own observed messages and substitute failures.

The limiting rule is therefore not “encode important organs” or “complete anatomy.” It is: encode an organ only
when its literal noun is necessary across multiple established messages, an existing emoji or short sequence
does not identify it, required frequency evidence is strong, and the final art has a stable small-size identity.
Kidney satisfies all four in the `.4` candidate. The revised purpose-built 18x18 artwork passes the fixed
technical-separation checks without changing the approved 72x72 paradigm.

Reproducible comparison:

https://books.google.com/ngrams/graph?content=kidney%2Cliver%2Cstomach%2Cpancreas%2Cspleen&year_start=1800&year_end=2022&corpus=en&smoothing=3

Phrase comparison:

https://books.google.com/ngrams/graph?content=kidney%20stone%2Ckidney%20test%2Ckidney%20transplant%2Ckidney%20donor%2Ckidney%20dialysis%2Cliver%20test%2Cliver%20transplant%2Cliver%20donor%2Cstomach%20test%2Cstomach%20transplant%2Cpancreas%20test%2Cpancreas%20transplant%2Cpancreas%20donor%2Cspleen%20test%2Cspleen%20transplant&year_start=1980&year_end=2022&corpus=en&smoothing=3

### Positive-factor inventory

| Factor | Initial classification | Reason before research |
| --- | --- | --- |
| Multiple meanings | `N/A` | The literal organ is the case; `kidney-shaped` is descriptive rather than a separate pictographic meaning. |
| Use in sequences | `SUPPORTED` | Kidney + Rock names the evidenced phrase `kidney stone`; Kidney + Test Tube names the evidenced phrase `kidney tests`. |
| Breaks new ground | `SUPPORTED` | Beans is a discoverable but food-first substitute; generic medical emoji do not supply the literal organ noun. |
| Distinctiveness | `SUPPORTED` | Paired inward-facing forms, medial notches, diagonal offset, and short central attachment are stable cues; the `.4` 18x18 color and black-and-white assets pass every fixed comparator check. |
| Expected usage | `SUPPORTED` | Five required captures show sustained term frequency; their exact interpretation remains bounded. |
| Completeness | `N/A` | Internal organs are not a fixed set. |
| Compatibility | `N/A` | No qualifying popular-system pictograph is established. |

### Strongest decline case

The strongest decline case is that Kidney is one member of an open-ended organ category; Unicode already makes
Beans searchable with the keyword `kidney`; the frequency exhibits prove word interest rather than emoji demand;
and paired artwork risks reading as Lungs at small size.

The answer is deliberately limited. Kidney does not claim selection from medical importance or search volume
alone. Its residual semantic job is the literal noun in evidenced phrases that Beans cannot compose cleanly,
especially `kidney stone` and `kidney tests`, within a broader stone + testing + dialysis + donation/transplant
cluster. The raw-word and Image Trends weaknesses are disclosed. The `.4` small-size refinement also preserves
the approved paired paradigm while moving the color 18x18 Lungs IoU from `0.750` to `0.698` under the unchanged
`0.72` ceiling; all twelve stored comparator rows pass.

### Visual identity

Essential cues are two inward-facing kidney forms, visible medial notches, deliberate vertical offset, and a
short central attachment. Likely confusers are Lungs and Beans, followed by Anatomical Heart, Balloon, Droplet,
and Light Bulb. Computer validation measures technical separation only; Shuhan's dated asset decision remains
the project human image gate.

## Case gate

| Test | Result | Reason |
| --- | --- | --- |
| Name-swap | `PASS` | Replacing Kidney with Liver, Stomach, Pancreas, or Spleen breaks the `kidney stone` and dialysis parts of the thesis and changes the Beans substitute analysis. |
| Real-message | `PASS` | Every retained use is an established patient-facing phrase or instruction in NIDDK, MedlinePlus, HRSA, or NHS Blood and Transplant guidance; speculative hydration, medication, caregiver, and awareness uses were removed. |
| Evidence-fit | `PASS` | Meaning sources prove only the phrase or care convention; frequency captures prove only dated term visibility; Ngram comparisons are not treated as emoji demand or entitlement. |
| Substitute | `PASS` | Beans and Beans + Hospital receive their strongest reading, including Unicode's own `kidney` search keyword, before the residual ambiguity is stated. |
| Priority | `PASS` | The case names four neighboring organs, concedes Kidney is not the raw-frequency leader, and applies a four-part rule based on observed messages, substitute failure, frequency, and visual identity rather than set completion. |
| Specificity | `PASS` | The thesis and central uses depend on kidney stone, kidney tests, dialysis, living kidney donation, paired medial notches, and the food-first Beans collision. |
| Cause | `PASS` | Removing disease burden, advocacy, awareness, and organizational mission leaves the full semantic case intact. |
| Concession | `PASS` | Multiple meanings, Completeness, and Compatibility are `N/A`; weaker Image Trends, higher Stomach/Liver raw frequency, slightly higher `liver transplant`, and the initial Lungs failure are explicit. |
| Objection | `PASS` | The answer addresses the actual strongest decline theory - open-ended organs plus a searchable Beans substitute and a Lungs visual confuser - rather than a weaker “no emoji exists” claim; the fixed art comparison now passes. |

Result: **CASE READY**.

This result authorizes proposal drafting under the case-building instructions. It does not make the package
submission-ready: eligibility documentation, duplicate coordination, Shuhan's approval of the exact revised
18x18 assets, exact-hash panel review, publication, and form reconciliation remain separate must-pass gates.

## Phase 4 - Artifact update

The 72x72 color and black-and-white paradigm assets are byte-identical to `.3`. The purpose-built 18x18 SVGs
were refined to use a clearer diagonal offset, deeper inward separation, and thinner small-size plumbing. The
fixed validator passes all dimensions, true black-and-white palette, connectedness, IoU, and difference-hash
checks. This is technical evidence only and does not claim human semantic recognition.

| Current `.4` asset | SHA-256 |
| --- | --- |
| `images/kidney_color_18x18_SUBMIT.png` | `619ec36cecf9a0637789a0a1ebbc3dbc2443c964405ccf395ea7f35fc30f950e` |
| `images/kidney_color_72x72_SUBMIT.png` | `a32d298c9563185410ae65d8a8777d5ca6c5e20e6a7ddc3bd8852405c75983cf` |
| `images/kidney_bw_18x18_SUBMIT.png` | `b006dc320958ff14bf1fc9024644dc7de8d199588887ffa63dd9f17a20e70d5b` |
| `images/kidney_bw_72x72_SUBMIT.png` | `87c945f86fff9b34571dba8291ce17a983cb198f29c958fa747a22f875211b22` |

## Candidate-specific section audit

Applied standard: every substantive section contains a Kidney-specific meaning, example, evidence result, or
visual reason; unsupported inclusion factors use a brief `N/A`; every required exclusion factor is answered.

| Proposal section | Candidate-specific content or disposition | Result |
| --- | --- | --- |
| Multiple meanings | Brief `Not applicable`; no invented metaphor | `PASS` |
| Use in sequences | Kidney + Rock for `kidney stone`; Kidney + Test Tube for `kidney tests` | `PASS` |
| Breaks new ground | Beans is officially searchable by `kidney` but remains a Food & Drink pictograph | `PASS` |
| Distinctiveness | Opposed medial notches, diagonal offset, central attachment, and Lungs/Beans comparison | `PASS` |
| Expected usage | Named stone, testing, dialysis, transplant, and donation messages plus five interpreted captures | `PASS` |
| Completeness | Brief `Not applicable`; no anatomy-set argument | `PASS` |
| Compatibility | Brief `Not applicable`; no invented popular-system evidence | `PASS` |
| Already representable | Beans, Beans + Hospital, Beans + Rock, and Beans + Test Tube receive a direct answer | `PASS` |
| Overly specific | Same organ noun spans stone analysis, tests, dialysis, transplant, and donation | `PASS` |
| Open-ended | Names Liver, Stomach, Pancreas, and Spleen and applies the stone + testing + dialysis + donation/transplant boundary | `PASS` |
| Transient | 1500-2022 Books evidence and current NIDDK, MedlinePlus, HRSA, and NHS Blood and Transplant terminology | `PASS` |
| Faulty comparison | Heart, Lungs, and Brain are limited to visual comparison, not encoding entitlement | `PASS` |
| Other Information | Resolves singular name versus paired paradigm and states essential vendor cues | `PASS` |
