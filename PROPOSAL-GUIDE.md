# Medical Emoji Proposal Guide (2026)

Guide version: 1.0.1

Last verified: 2026-07-26

Status: Controlling practical guide for agents preparing or reviewing a Medical Emoji proposal. Unicode's
current instructions remain the external authority.

Official instructions:
https://www.unicode.org/emoji/proposals.html

## The answer that matters first

| Question | Answer | Practical meaning |
| --- | --- | --- |
| **Does the proposal break new ground?** | **Yes, for a normal proposal worth filing.** | It must add a useful semantic building block that no existing emoji or reasonable sequence already expresses. |
| Does "new ground" mean scientific novelty, an unfamiliar object, or radical artwork? | **No.** | The concept should already be familiar and used. The *gap in the emoji vocabulary* is new, not the underlying thing. |
| Should an organ proposal argue that Unicode needs a complete anatomy set? | **No.** | Completeness should be `N/A`; anatomy is not a fixed set. A set-completion argument creates an Open-ended objection. |
| Is medical importance, disease burden, or awareness enough? | **No.** | It may provide context, but it cannot replace evidence of ordinary communicative use. |
| Must every positive inclusion factor be claimed? | **No.** | Use `N/A` when Multiple meanings, Sequences, Completeness, or Compatibility is not genuinely supported. |
| Are correct headings and four image files enough? | **No.** | All 15 confirmed declined Medical Emoji drafts answered every exclusion heading. Technical compliance is only the entry gate. |
| Is an accepted old proposal a valid 2026 template? | **No.** | Older proposals were evaluated under older formats. Use them as evidence, never as permission to ignore current rules. |

Unicode explicitly asks whether the proposed emoji "Breaks new ground" and instructs submitters to mark the
answer `Yes` or `No`. More weight is given to concepts that are not variants of existing emoji or sequences.
For this project, a `No` answer is normally a **stop decision**. The only escalation path is a documented,
high-frequency compatibility need in a popular existing system; resemblance to an icon or a hoped-for platform
partnership is not compatibility.

This resolves a common misunderstanding:

- We **do want** a new semantic capability in the emoji vocabulary.
- We **do not want** a scientifically novel, obscure, overly specific, or visually experimental subject.
- We **do not want** to argue that a new organ is justified because Heart and Lungs already exist.

## Submission posture: advocate for approval; do not self-litigate

**The purpose of every submission is to get the emoji approved.** Every final PDF must put the project's
strongest accurate case forward. It should help the reviewer reach `Yes`; it must not read like an internal
audit, a debate transcript, or a brief against our own proposal.

The controlling rule is:

> **Red-team privately. Submit persuasively.**

Internal review should be skeptical and exhaustive so weak concepts, claims, evidence, and images are fixed or
stopped before filing. The submission should contain the final passing work and the clearest affirmative case.
Keep the two records separate:

| Keep in internal review files | Put in the submitted proposal |
| --- | --- |
| Failed image variants, raw miscues, rejected claims, internal scores, unresolved gates, TODOs, and speculative objections | Final passing images, strongest reproducible evidence, supported claims, current required fields, and concise answers to actual exclusion factors |
| Debate about whether the concept should be filed | The reason the eligible, cleared concept should be approved |
| Every possible argument against us | The strongest likely objection, answered directly and then closed |
| Process narration and agent uncertainty | Reviewer-facing evidence and conclusions |

Submission-writing rules:

1. **Lead with the winning conclusion.** Write `Yes - this breaks new ground because...`, not a page of doubt
   before the answer.
2. **Treat exclusion sections as rebuttals, not prosecution briefs.** Name the real substitute or objection,
   answer it with evidence, and move on. Do not invent additional reasons to reject the proposal.
3. **Do not export internal language.** Remove `weak`, `risk`, `blocked`, `not ready`, `might fail`, `must be
   refreshed`, TODOs, internal thresholds, abandoned alternatives, and review commentary from the final PDF.
4. **Use only decision-relevant limitations.** If a material evidence limitation must be disclosed for
   accuracy, state it precisely and immediately explain why the complete evidence still supports approval.
5. **Do not apologize for the proposal.** Avoid hesitant, defensive, or self-deprecating framing. Make every
   supported claim directly.
6. **Do not include internal scoring or approval predictions.** The submission proves the criteria; it does
   not narrate our confidence level or ask the reviewer to resolve our internal debate.
7. **Run a final advocate edit.** Every sentence must do at least one job: satisfy a current requirement,
   prove a selection factor, rebut a required exclusion, establish rights, or guide vendor design. Delete
   sentences that only create doubt.

Putting our best foot forward does not permit false claims, selective cropping, hidden contradictions, or
misleading evidence. It means fixing defects before filing and presenting the strongest truthful version of
the case without litigating against ourselves in the submission.

## What this guide is based on

The repository audit reviewed:

- the first page of 63 accepted proposal PDFs;
- six representative accepted proposals page by page;
- all eight proposal documents for the nine Emoji 18.0 accepted characters;
- a reproducible 55-document accepted archive associated with Emoji 14.0 through 17.0; and
- the full text of 15 Medical Emoji drafts whose concepts and dates match confirmed decline records.

The declined drafts' original images are not available in the repository, so no claim is made about their
artwork. Unicode's public status sheet also does not publish complete reviewer reasoning. The historical
findings are therefore descriptive risk signals, not a formula that predicts acceptance.

The old 55-winner versus 29-loser calculation is retired. Its negative corpus and code were not preserved, so
its percentages, word target, page target, and image-count target cannot be reproduced. Do not use them.

### Previous work recovered from Git history

The earlier work was not lost; it was distributed across these commits and later corrected:

| Commit | What it contains | How this guide uses it |
| --- | --- | --- |
| `605712b` | Archived the accepted 2019 Anatomical Heart and Lungs PDFs and text, alongside the Medical Emoji draft archive. | Retained as project history and medical-image precedent. |
| `ab69aa6` | Archived extracted text for 55 accepted proposals from 2020-2024 and wrote the first winning-proposal guide. | Retained as the main local accepted-proposal reading library. |
| `78f1d82` | Created the winners-versus-losers report and fill-in proposal template. | Template structure retained; unsupported quantitative claims retired. |
| `2340a29` | Added the official accepted-proposal manifest and first reproducibility analysis. | Retained as the source manifest and audit foundation. |
| `596822c` | Rebuilt the analysis with reproducible code, confirmed-decline records, and explicit methodology limits. | Controlling correction to the earlier formula. |
| `ce2482c` | Refocused the rubric on proposal content and the latest accepted cohort. | Retained and extended by this guide's image study and decision gates. |

The historical commits remain useful because they preserve the actual proposal documents. They should not be
used to restore the retired claim that a specific word count, page count, image count, or phrase makes a
proposal win.

Full methodology and source audit:
[`docs/research/unicode-winning-submissions/analysis.md`](docs/research/unicode-winning-submissions/analysis.md)

Machine-readable measurements:
[`docs/research/unicode-winning-submissions/corpus-audit-2026-07-20.json`](docs/research/unicode-winning-submissions/corpus-audit-2026-07-20.json)

## The five gates, in order

Agents must run these gates in order. Do not begin polished prose or final artwork for a concept that fails an
earlier gate.

### Gate 1: eligibility, ownership, and automatic-decline screen

Confirm all of the following before drafting:

- The concept is not already approved, pending prioritization, or under consideration.
- It has not been declined within the last four years, unless Unicode has supplied written eligibility
  confirmation for this intake.
- One proposal covers one emoji.
- An individual submitter and one main point of contact are identified.
- The concept is not a logo, brand, protected work, UI icon, sign, specific person, specific building or
  landmark, deity, unrequested flag, directional variant, text-bearing image, or exact-image demand.
- The submitter can make the required image-rights warranty and license grant, including for AI-assisted work.
- The final PDF can be hosted at a public HTTPS URL and filed through the official form.

Official status page:
https://www.unicode.org/emoji/emoji-proposals-status.html

Official FAQ:
https://www.unicode.org/faq/emoji_submission.html

Official proposal agreement and license:
https://www.unicode.org/emoji/emoji-proposal-agreement.pdf

If any item is unresolved, label the proposal `BLOCKED`; do not call it submission-ready.

### Gate 2: independent semantic case

Write these five one-sentence answers before drafting the proposal body:

1. **Nearest substitute:** What existing emoji or short sequence would a skeptical reviewer use instead?
2. **Remaining gap:** What ordinary message still cannot be expressed clearly with that substitute?
3. **Breaks new ground:** `Yes` or `No`, followed by the semantic difference in one sentence.
4. **Overly specific:** Why is this a broad paradigm or building block rather than a subtype, disease,
   procedure, specialty, campaign, or branded object?
5. **Open-ended:** Why does this concept stand independently without implying that many similar items must be
   encoded next?

Decision rule:

- `Breaks new ground = Yes` and the other four answers are credible: continue.
- `Breaks new ground = No`: stop unless a genuine, evidenced compatibility case is escalated for review.
- The only Open-ended answer is "other organs are important too": stop.
- The remaining gap is merely "a more accurate picture": stop; emoji encode semantic paradigms, not exact art.

### Gate 3: empirical use

The concept must be in broad, durable, ordinary use before the emoji is proposed. The current format requires
screenshots of all five sources:

1. Google Search, with the result count visible after selecting **Tools**.
2. Google Video Search, with the result count visible.
3. Google Trends - Web Search, with `elephant`, widest time range, and widest location range.
4. Google Trends - Image Search, with `elephant`, widest time range, and widest location range.
5. Google Books Ngram Viewer, with `elephant` and the widest supported range.

Every capture must expose the query, settings, date, comparator, and visible result. Use a private browser
window where possible. Hyphenate multiword queries, disambiguate noisy terms, and use category filters when
needed. Explain limitations rather than cropping them away.

Do not use petitions, hashtags, calls for an emoji, anecdotes, society letters, disease burden, or awareness
campaigns as frequency evidence. Support letters can establish coordination or domain context; they do not
show ordinary language use.

### Gate 4: image paradigm and recognition

The proposal image is evidence that the concept can survive as an emoji. It is not a logo, a final vendor
glyph, a medical illustration, or decoration.

#### Official image requirements

The top of page 1 must contain:

- color at exactly 18x18 pixels;
- color at exactly 72x72 pixels;
- true black-and-white at exactly 18x18 pixels;
- true black-and-white at exactly 72x72 pixels; and
- a truthful ownership or open-license statement.

Grayscale does not satisfy black-and-white. The image must not contain text, numbers, a barcode, branding, or
protected visual material. Unicode says the example image will not be used in products; it demonstrates that
the paradigm is recognizable at typical emoji size, and vendors remain free to draw it differently.

#### Project image-quality standard

An agent must define these items before choosing art:

- **Paradigm sentence:** one sentence naming the broad entity the glyph represents.
- **Essential cues:** one outer silhouette and no more than three interior or attached cues that can survive
  at 18x18.
- **Confuser set:** the nearest existing emoji, proposed sibling emoji, and ordinary objects a viewer may name
  instead.
- **Vendor freedoms:** details, shading, angle, or color vendors may change without changing the meaning.

Then follow this design sequence:

1. Sketch several silhouette families, not merely color variations of one drawing.
2. Draw a dedicated 18x18 master. Do not assume a detailed 72x72 illustration will downsample well.
3. Design black-and-white independently so negative space and outline carry the identity without color.
4. Compare every candidate beside the confuser set at actual 18x18 and 72x72 size.
5. Inspect at 100% scale on light and dark backgrounds. Zoomed inspection is for pixel QA only.
6. Render the first PDF page and confirm that the 18x18 sample remains visible and the 72x72 sample remains
   sharp.
7. Run technical checks for dimensions, palette, transparency, connected components, file hashes, and source
   reproducibility.
8. Run the unprompted recognition test below. Computer similarity metrics cannot prove semantic recognition.

#### Required internal recognition test

This is a Medical Emoji quality gate, not a Unicode rule.

- Use at least 12 people who were not told the target concept and are not reviewing their own artwork.
- Show the 18x18 color image alone at actual size on a neutral background. Ask, "What is this?"
- Repeat with the 18x18 black-and-white image in a separately randomized pass.
- Record raw free-text answers before showing any choices.
- Then run a forced-choice confuser test using the declared confuser set.
- Pass only if at least 10 of 12 viewers identify the intended concept or an accepted synonym in both color
  and black-and-white, and no wrong concept dominates the responses.
- Archive the prompt, participant count, raw answers, scoring rule, and result. Do not report only a percentage.

If the concept is specialized, add domain reviewers for factual accuracy, but do not replace general viewers;
Unicode's recognizability test is whether most people can discern the intended paradigm without foreknowledge.

#### What accepted images teach

| Proposal | Reusable image lesson | Do not copy |
| --- | --- | --- |
| Treasure Chest | Open lid, box silhouette, interior cavity, and a few coins survive in both sizes and both palettes. | Dense treasure detail at 18px. |
| Lighthouse | Tall tapered tower plus an outward beam creates an unmistakable action silhouette. | Photorealistic shading as the only identity cue. |
| Fingerprint | The ridge pattern is the concept; the proposal keeps enough negative space for it to remain legible. | Thin decorative lines that disappear after rasterization. |
| Meteor | A round head plus directional tail distinguishes it from Fire and Shooting Star. | Compatibility claims without popular-system evidence. |
| Monarch Butterfly | The butterfly outline remains clear; orange/black pattern adds subtype identity. | Treating detailed wing markings as the only cue. |
| Pickle | Curvature, taper, and bumpy surface separate it from Cucumber at small size. | Assuming green color alone proves the concept. |
| Thumb Point | The hand pose carries the meaning and is compared with the crowded hand-emoji set. | Ignoring directionality and neighboring gesture confusers. |
| Net With Handle | Hoop, mesh, and handle form a compact tool silhouette in color and line art. | Treating old credit-only rights language as current compliance. |
| Anatomical Heart and Lungs | Strong outer anatomy and attached structures made the medical objects identifiable. | Their 2019 first pages; they predate the current four-image and rights format. |

Accepted proposals also contain imperfect pages. Orca has broken or blank evidence figures, Eraser is largely
image-based, and several old accepted documents omit fields now required. Acceptance shows that the concept
advanced; it does not certify every layout, sentence, or image decision as best practice.

Accepted exemplars:

- Lighthouse: https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf
- Treasure Chest: https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf
- Fingerprint: https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf
- Meteor: https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf
- Monarch Butterfly: https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf
- Pickle: https://www.unicode.org/L2/L2025/25253-emoji-pickle.pdf
- Thumb Point: https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf
- Net With Handle: https://www.unicode.org/L2/L2025/25258-emoji-net.pdf

#### Current Medical Emoji baseline diagnosis

This table describes the canonical `v1.10.0` first pages inspected on 2026-07-26. Kidney's v1.10.0 validation
passes declared palette, connectedness, silhouette-IoU, and difference-hash checks. Its own report correctly
states that those checks do not measure human semantic recognition; the visible 18x18 black-and-white sample
still requires the human gate below. The other three first pages are unchanged from v1.9.0.

| Concept | Breaks new ground? | 18px image finding | Filing decision from image alone |
| --- | --- | --- | --- |
| Kidney | **Yes, defensible.** Beans, Droplet, and existing anatomy do not express the kidney organ. | Color can read as a bean or bulb; black-and-white loses the hilum and becomes a filled blob. Deterministic separation is not the same as recognition. | **No-file until human recognition passes against Beans and generic red objects.** |
| Stomach | **Yes, defensible.** Nauseated Face, food, and existing organs do not express the stomach entity. | The color J-shape is the strongest current organ silhouette; black-and-white loses some internal curve. | **Closest to passing, but still requires the recognition gate.** |
| Liver | **Yes, defensible.** No current emoji expresses the liver entity. | The small black-and-white image is a horizontal blob; color can read as meat or a generic red organ. | **No-file; redesign the small paradigm.** |
| White Blood Cell | **Yes, but high-risk.** Microbe and Drop of Blood do not express an immune cell. | The small image reads as a generic cell or dot; nucleus and membrane cues are too weak. | **No-file until it separates from Microbe, generic cell, and blood imagery.** |

`Breaks new ground = Yes` is therefore necessary but not sufficient. A concept can pass the semantic test and
still fail distinctiveness, usage, Open-ended, or quality gates.

### Gate 5: current-format document and filing control

Use this exact 2026 structure even when an older accepted proposal used something else.

#### Top of page 1

1. `Proposal for Emoji: <name>`.
2. Individual submitter names separated with semicolons.
3. One named main point of contact.
4. Current revision date.
5. Identification: search-oriented keywords that do not merely repeat the name, and proposed category.
6. The four required image assets.
7. The image-rights and license statement.

A suggested sort location may help the reviewer, but the 2026 format requires Category; it does not require a
separate sort-location field.

#### Factors for inclusion, in current order

1. Multiple meanings - `N/A` unless established non-pun meanings are cited.
2. Use in sequences - `N/A` unless the combinations add distinct plausible messages.
3. Breaks new ground - answer `Yes` or `No` immediately.
4. Distinctiveness - show how the 18x18 color and black-and-white paradigms survive their confusers.
5. Usage level - interpret all five required frequency sources honestly.
6. Completeness - `N/A` for organs and other open taxonomies.
7. Compatibility - `N/A` without an existing high-frequency pictograph in a popular system.

#### Factors for exclusion, in current order

1. Already represented - name the strongest emoji or sequence substitute and the remaining gap.
2. Overly specific - show that the concept is a broad paradigm.
3. Open-ended - explain why it stands independently and does not demand a continuing series.
4. Transient - establish durable use rather than merely saying the underlying organ is old.
5. Faulty comparison - state that the case does not depend on another emoji's existence or importance.

#### Other information

Give concise vendor design guidance: the essential cues, acceptable variation, and details that should not be
allowed to carry the meaning. Do not demand an exact rendering.

Drafting template:
[`docs/proposals/TEMPLATE-emoji-proposal.md`](docs/proposals/TEMPLATE-emoji-proposal.md)

Approval specification:
[`docs/proposals/emoji-proposal-approval-rubric.md`](docs/proposals/emoji-proposal-approval-rubric.md)

## Proposal-by-proposal research lessons

| Source | Best lesson | Important limitation |
| --- | --- | --- |
| Lighthouse | Best current all-around first page, factor order, direct `N/A`, evidence set, exclusions, and image presentation. | Nine pages; still needs concept-specific adaptation. |
| Treasure Chest | Best concise broad-building-block case and short Open-ended answer. | Some embedded evidence is small. |
| Fingerprint | Best technical distinction, substitute rebuttal, and reproducible evidence discipline. | Dense and visually older than the current ideal. |
| Meteor | Best genuine interoperability/compatibility case. | Compatibility cannot be borrowed without equivalent deployment evidence. |
| Monarch Butterfly | Shows that cause context is not fatal when an independent compatibility case succeeds. | Nineteen pages and unusually advocacy-heavy; UTC recorded that it would not have advanced without compatibility. |
| X-Ray | Shows that medical background can coexist with a recognizable object and ordinary use. | Its 2020 format and rights line are not a 2026 template. |
| Anatomical Heart and Lungs | Prove that medical anatomy can advance when iconic, distinct, and broadly useful. | Their existence does not justify Kidney, Liver, Stomach, or a complete anatomy set. |
| Orca | Shows that a proposal may concede weak Trends evidence and still make a narrower case. | Broken figures make it a poor layout model. |

X-Ray:
https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf

Orca:
https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf

UTC #185 minutes record that compatibility was central to the Emoji 18.0 cohort and specifically to Monarch
Butterfly:
https://www.unicode.org/L2/L2025/25226.htm

ESR's stated Emoji 19.0+ direction raises the benchmark around cited empirical use, compatibility with social
apps/standards/operating systems, and improvements to existing emoji user experience:
https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf

## What the declined Medical Emoji drafts teach

The 15 confirmed declined drafts were not rejected merely because they were medical or long. The repeatable
risks were:

1. Clinical importance, mortality, awareness, or professional value substituted for ordinary use.
2. Thirteen of 15 mentioned petitions, Instagram, or Twitter; current rules reject calls for the emoji as
   frequency evidence.
3. Open-ended answers did not explain why one organ, procedure, or specialty deserved selection from a large
   possible set.
4. The drafts rarely used `N/A`, encouraging weak claims for every positive factor.
5. Their evidence predates the current five-source, `elephant`, widest-range, private-window, and
   reproducibility instructions.
6. Bundling related medical concepts made the set-expansion objection easier to see.

The safe lesson is narrow: importance and advocacy cannot replace expected use and independent selectivity.
Do not claim that any word, page count, medical topic, or advocacy mention independently caused rejection.

## Agent operating contract

Every proposal agent must produce the following artifacts or explicitly return `BLOCKED`:

1. A one-page concept gate with the five semantic answers from Gate 2.
2. A source ledger linking every material factual claim to a readable citation.
3. The five current frequency captures and reproducible query URLs/settings.
4. A written image paradigm, cue list, vendor freedoms, and confuser set.
5. Color and true black-and-white SVG sources plus exact 18x18 and 72x72 PNG exports.
6. An actual-size comparison board against the declared confusers.
7. Technical image-validation output and the raw recognition-test record.
8. A current-format Markdown source and rendered PDF.
9. A page-by-page visual review and PDF technical report covering fonts, text extraction, links, encryption,
   image dimensions, clipping, and blank pages.
10. A final advocate edit confirming that internal doubts, failed iterations, scores, TODOs, and self-defeating
    commentary remain in review records rather than the submitted PDF.
11. The exact public PDF URL, logged-out accessibility check, official-form confirmation, and archived filing
    record.

Agents must never:

- turn an unresolved gate into confident prose;
- use a later version number without creating a complete immutable packet snapshot;
- revise a historical packet in place;
- call a proposal `SUBMIT` while an image, evidence, eligibility, authorship, rights, review, URL, or filing gate
  remains open;
- infer recognition from dimensions, connectedness, IoU, perceptual hashes, or AI opinion alone;
- copy an old accepted proposal's obsolete format; or
- optimize for an unsupported word, page, or image-count target.

## Final no-file checklist

- [ ] Eligibility and coordination are documented.
- [ ] `Breaks new ground` says **Yes** and names the semantic gap; otherwise a genuine compatibility escalation
      is documented.
- [ ] Completeness is `N/A` for an organ; the case never asks Unicode to complete anatomy.
- [ ] Open-ended stands on independent evidence and names the strongest neighboring concepts.
- [ ] All five evidence screenshots are current, readable, reproducible, and honestly interpreted.
- [ ] Every material claim has a citation or has been removed.
- [ ] Four exact images and truthful rights language appear at the top of page 1.
- [ ] Both 18x18 assets pass unprompted general-viewer recognition against declared confusers.
- [ ] The PDF follows the 2026 field and factor order, contains no draft notes, and has been visually inspected.
- [ ] Domain/factual and Unicode/process reviewers approved the exact PDF.
- [ ] The exact PDF is public, works logged out, was filed through the official form, and confirmation is archived.

If any box is open, the proposal is not ready to file.

## Controlling primary sources

- Current Unicode proposal guidelines, updated 2026-05-20:
  https://www.unicode.org/emoji/proposals.html
- Current proposal status and definitions:
  https://www.unicode.org/emoji/emoji-proposals-status.html
- Emoji proposal FAQ:
  https://www.unicode.org/faq/emoji_submission.html
- Emoji proposal agreement and license:
  https://www.unicode.org/emoji/emoji-proposal-agreement.pdf
- Accepted proposal chart through Emoji 17.0:
  https://www.unicode.org/emoji/charts/emoji-proposals.html
- Accepted proposal chart for Emoji 18.0 beta:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- ESR priorities for Emoji 18.0 and Emoji 19.0+:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC #185 minutes recording the Emoji 18.0 decisions:
  https://www.unicode.org/L2/L2025/25226.htm
