# Case-Building and Drafting Instructions for Proposal Agents

Version: 1.0.0

Date: 2026-07-26

Applies to: Stomach, Kidney, Liver, and White Blood Cell

## Purpose

Use this specification to build the reasoning for a proposal before polishing its prose. It is not a proposal
template and does not supply sentences to copy. The approval rubric remains the final compliance and quality
check; it must not be used as a fill-in-the-blank writing system.

The shared rules explain how not to fail. A competitive proposal still needs a concept-specific reason to be
selected. If the concept name can be exchanged for another medical object without materially changing the
argument, the case is not ready to draft.

The current Unicode instructions control whenever repository guidance conflicts with them:

https://www.unicode.org/emoji/proposals.html

## What to learn from successful proposals

Study accepted proposals for their decisions, not their wording:

- Lighthouse is the strongest current model for a useful first page, current factor order, direct `N/A`
  answers, complete evidence, and complete exclusions.
- Treasure Chest shows how to distinguish several established meanings without turning the section into a
  list of imaginable contexts.
- Fingerprint shows reproducible evidence, technical explanation that serves a reviewer, and a serious answer
  to the nearest substitute.
- Meteor shows that Compatibility can be powerful only when the same pictograph already has genuine, popular
  system use. It is not a reason to search for a weak analogy.
- Orca shows that conceding a weak factor can be more credible than stretching the evidence.
- Monarch Butterfly is an exception whose independent compatibility case carried cause-heavy background; it
  is not a general model for medical advocacy.

Sources and the comparative acceptance/decline analysis are recorded in
[`../research/unicode-winning-submissions/analysis.md`](../research/unicode-winning-submissions/analysis.md).
No accepted proposal should be copied wholesale. Acceptance does not make every sentence, figure, or omission
in an older proposal a best practice.

## Required outputs

Before revising proposal prose, create these files inside the active concept folder:

1. `CASE-BRIEF.md` — the concept-specific selection case and the result of every gate below.
2. `CLAIM-LEDGER.md` — every material factual or usage claim, its source, what the source actually supports,
   and its intended proposal section.

After drafting, update the concept's existing `READINESS.md`. Do not create the PDF merely to make an
underdeveloped case look complete.

## Phase 1: freeze the actual candidate

Record the following in `CASE-BRIEF.md` before research or rewriting:

- exact source package, version, Git commit, proposal source, PDF, and four image assets being assessed;
- current official-guidance check date and eligibility/duplicate-status source;
- latest concept-specific authorship and consent record, preserving every confirmed author and identifying
  Shuhan He only as the main point of contact when that is what the record says;
- image-rights source and whether it covers the exact assets;
- prior decisions, unresolved blockers, and any evidence that must be recaptured; and
- the nearest accepted-proposal exemplars relevant to this candidate and the particular lesson taken from each.

Never infer authorship, consent, rights, human approval, or a Unicode/ESR decision from an older package.

## Phase 2: build the case before prose

Write the following as research notes, not submission language.

### Selection thesis

State in no more than 40 words the exact missing meaning, the strongest existing emoji or short sequence that
comes closest, the residual meaning it cannot express, and why this candidate is a reusable unit rather than a
single campaign, diagnosis, or event.

The thesis must identify a communicative choice. Importance, disease burden, professional prestige, public
awareness, and the fact that other organs are encoded do not establish that choice.

### Observed communication

Document three to five distinct, evidenced communication situations. For each one, record:

- an actual phrase, usage, convention, source example, or search behavior;
- who is communicating with whom, only when the evidence establishes it;
- the meaning conveyed; and
- why the nearest existing emoji or short sequence changes, obscures, or omits that meaning.

Do not substitute lists of medical specialties, diseases, stakeholders, or messages that people merely
*could* send. One strong observed use is better than five invented scenarios.

### Nearest-substitute analysis

Choose the strongest existing substitute, even if it weakens the proposal. Show what it communicates well and
then isolate the remaining gap. Include the strongest short sequence, not only a single emoji. If a substitute
works adequately for the central uses, mark the case blocked instead of hiding it.

### Priority and scope

Name the closest neighboring unencoded concepts that a reviewer is likely to raise. Explain the principle
that makes this candidate a better bounded encoding decision without implying that the whole neighboring set
must follow. The answer must rely on this candidate's meaning, evidence, or representation problem—not on its
place in an anatomy checklist.

### Positive-factor inventory

For Multiple meanings, Use in sequences, Breaks new ground, Distinctiveness, Expected usage, Completeness, and
Compatibility, classify the factor as:

- `SUPPORTED` — direct evidence is strong enough to carry a proposal claim;
- `LIMITED` — true but narrow, uncertain, or secondary and must be described with that limitation; or
- `N/A` — not a real part of this candidate's case.

Do not reward the case for having more `SUPPORTED` labels. Honest `N/A` answers are preferable to invented
metaphor, false completeness, or weak compatibility.

### Strongest decline case

Write the most persuasive reviewer argument for declining the candidate. Identify what evidence would confirm
that objection and what current evidence, if any, rebuts it. If the response is only that the subject matters,
the case is not ready.

### Visual identity

Identify the few visible cues that must survive at 18x18 in color and true black-and-white, then list likely
confusers. Computer checks establish technical properties and measurable separation only. Shuhan He's dated
review of the exact four final assets establishes project approval; no invented crowd study, recognition
percentage, or named external reviewer may be claimed.

## Case gate

Run every test below before changing the proposal. Record `PASS` or `FAIL` with a short reason in
`CASE-BRIEF.md`. Any failure means `CASE BLOCKED` until repaired.

1. **Name-swap test:** replace the candidate's name with another medical concept. If most of the thesis,
   observed uses, priority argument, and substitute analysis still work, the case is generic.
2. **Real-message test:** every claimed use is observed or supported, not introduced only by words such as
   “could,” “may,” or “would allow.”
3. **Evidence-fit test:** each source supports the precise claim assigned to it. Search volume does not prove a
   meaning; burden statistics do not prove emoji use; a visual resemblance does not prove Compatibility.
4. **Substitute test:** the strongest existing single emoji and short sequence receive a fair hearing.
5. **Priority test:** the case explains why this candidate can be selected without committing Unicode to an
   anatomy set, immune-cell taxonomy, or other open-ended series.
6. **Specificity test:** the thesis and at least two central uses contain facts, phrases, cultural meanings,
   visual cues, or representation problems unique to this candidate.
7. **Cause test:** remove disease burden, awareness, advocacy, and organizational mission. The selection case
   still works.
8. **Concession test:** unsupported positive factors are marked `N/A`, and weaknesses in required evidence are
   stated rather than concealed.
9. **Objection test:** the draft answer addresses the strongest plausible decline reason, not an easier version
   invented by the submitter.

Permitted result: `CASE READY` or `CASE BLOCKED`. An agent must not rewrite proposal paragraphs while the result
is `CASE BLOCKED`; it should instead repair research, narrow the claim, improve the candidate, or report the
blocker.

## Phase 3: give every section one job

After `CASE READY`, draft in the official factor order. Each fact and argument should have one primary home.
Cross-reference it elsewhere rather than restating it in new words.

| Section | Its one job | Keep out |
| --- | --- | --- |
| Multiple meanings | Establish independently recognizable literal, metaphorical, or symbolic meanings with evidence | Lists of audiences, diseases, or merely possible uses |
| Use in sequences | Show two or three legible combinations that express evidenced messages | Long menus of speculative combinations |
| Breaks new ground | Identify the residual semantic unit missing after the best existing substitute | General importance, full substitute catalog, or anatomy-set claims |
| Distinctiveness | Explain the few visible cues that differentiate the glyph at emoji size while preserving vendor freedom | Internal validator narrative, scores, hashes, or a claim that appearance proves usage |
| Expected usage | Present all required evidence reproducibly and explain only what each result supports | Approval predictions, cropped weaknesses, petitions as frequency evidence, or burden as use |
| Completeness | Make a genuine established-set argument, if one exists | A list of body parts or the existence of Heart/Lungs |
| Compatibility | Document the same pictograph's significant use in a popular existing system, if one exists | Similar medical logos, hoped-for partnerships, or niche icon sets |
| Already representable | Fairly test the strongest single emoji and short sequence, then explain the important residual meaning | Straw substitutes or a paraphrase of Breaks new ground |
| Overly specific | Define the candidate's durable category boundary and explain why it is not a subtype, result, or one-off event | Broad claims that it can mean everything related to the subject |
| Open-ended | Apply a candidate-specific priority principle against named neighboring concepts | “It stands alone,” “each proposal is independent,” or a denial that any neighbors exist |
| Transient | Establish durable language, imagery, and communication over time | Short-lived campaigns or current-event popularity |
| Faulty comparison | Clarify that evidence comparators are measurement controls and that precedents are not entitlement | A second summary of the whole selection case |
| Other information | Give only implementation-relevant information that did not fit above | Internal workflow, reviewer simulation, QA results, or project history |

Use plain, concrete language. Prefer an actual noun, verb, phrase, visual cue, or measured result over labels
such as “high utility,” “broad use,” “multiple contexts,” or “fills a gap.” The phrases below are warning signs
when they appear without an immediately adjacent candidate-specific fact:

- “broad communicative building block”;
- “independently useful”;
- “ordinary messages”;
- “stands on its own”;
- “not merely to complete a set”;
- “multiple contexts”; and
- “the case rests on its own evidence.”

These phrases are not banned facts; they are conclusions that must be earned. Do not copy them across the four
proposals.

## Phase 4: adversarial draft review

Before applying the final rubric, inspect the prose as an opposing reviewer:

1. Mask the candidate name and title. Flag every paragraph that could belong unchanged in another organ or
   medical proposal.
2. Require every substantive paragraph to contain at least one candidate-specific observed use, source
   interpretation, substitute problem, scope boundary, or visible cue.
3. Map every material factual sentence back to `CLAIM-LEDGER.md`; remove or qualify unmapped claims.
4. Highlight repeated arguments. Keep the strongest occurrence and replace later occurrences with a concise
   cross-reference or delete them.
5. Verify that the strongest substitute and strongest decline case are presented fairly.
6. Verify that Open-ended establishes a real priority boundary against named neighbors.
7. Remove internal process language, including validator mechanics, asset hashes, panel roles, scoring,
   readiness labels, and statements about what the checks “establish.”
8. Read the proposal aloud. Replace abstract noun chains and policy-sounding boilerplate with direct sentences
   a general reviewer can understand once.

Only now use the approval rubric and proposal template as compliance checklists. Their drafting patterns are
diagnostic examples, not required wording. A rubric score cannot convert a generic or unsupported case into a
competitive proposal.

Permitted result after this phase: `DRAFT READY FOR COMPLIANCE` or `REVISION REQUIRED`.

## Phase 5: compliance, artifact review, and panel

Once the case and prose pass their gates:

1. Apply the current official requirements and every must-pass item in the repository rubric.
2. Reconcile authorship, consent, rights, eligibility, evidence settings, artwork, and proposal text against the
   exact package being built.
3. Rebuild the PDF, extract its text, render every page, and inspect the artifact at normal zoom.
4. Present the exact 18x18 and 72x72 color and black-and-white assets to Shuhan He at actual size and record his
   dated `APPROVE` or `REVISE` decision.
5. Run the repeatable ESR/UTC-readiness panel on the exact final artifact hash. It is an internal red team, not
   testimony or endorsement by any named expert, ESR, UTC, or Unicode.
6. Answer every panel action in the action ledger. Any material change requires a new artifact and panel run.

Permitted result: `READY FOR PANEL`, `REVISION REQUIRED`, or the lane's existing publication status. Never use
`READY TO SUBMIT` until the public URL, form data, confirmed authorship, exact PDF, and Shuhan He's explicit
authorization are reconciled.

## Agent execution instruction

An assigned agent should execute this sequence without asking for stylistic preferences:

1. Freeze and record the exact candidate inputs.
2. Produce `CASE-BRIEF.md` and `CLAIM-LEDGER.md` from primary or authoritative sources.
3. Run the case gate and stop proposal drafting on any failure.
4. Draft each official section for its single assigned job, using the candidate's evidence and language rather
   than shared sentence patterns.
5. Run the adversarial draft review and repair generic, repetitive, or unsupported prose.
6. Apply the current rubric as final compliance QA.
7. Build and inspect the exact artifact, obtain Shuhan's image decision, and complete the panel feedback loop.
8. Report the case status, unresolved objections, changed files, evidence limitations, verification, and next
   required decision. Do not publish, submit, email, push, merge, or deploy without explicit authorization.
