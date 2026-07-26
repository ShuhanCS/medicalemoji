# Best-in-Class Emoji Submission Specification

Version: 3.1.0

Last checked: 2026-07-26

Applies to: Kidney, Liver, and Stomach proposals for the 2026 Unicode intake

## Decision

This specification evaluates proposal documents, not L2 numbering or registry mechanics. L2 identifiers are
used only to cite source PDFs.

There is no single accepted proposal that should be copied verbatim. The best submission model is a composite
of:

1. The current Unicode requirements, which control even when older accepted proposals used a different
   format.
2. The strongest repeatable practices in the historical accepted-proposal corpus.
3. Direct review of accepted proposal arguments, evidence, artwork, and page design, plus this project's
   confirmed declined drafts. These observations are not an approval model.
4. The latest Emoji 18.0 accepted cohort and the Emoji 19.0+ priorities published by the Emoji Standard &
   Research Working Group (ESR).

The closest current general-purpose exemplar is Lighthouse. It has a clean first page, follows the current
factor order, presents all five frequency sources, uses `N/A` directly, and answers the exclusions without
trying to win by importance:

https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf

Treasure Chest is the strongest concise exemplar. It treats the emoji as a broad building block, states
independent utility, and answers the exclusion factors directly in four pages:

https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf

Fingerprint is the strongest model for reproducible evidence and disciplined technical presentation:

https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf

Meteor is the clearest current model for a genuine interoperability proposal, but its compatibility
case must not be copied by a concept that lacks equivalent system evidence:

https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf

## Controlling sources

- Current proposal guidelines, updated 2026-05-20:
  https://www.unicode.org/emoji/proposals.html
- Emoji Proposal Agreement and License:
  https://www.unicode.org/emoji/emoji-proposal-agreement.pdf
- Official submission form:
  https://forms.gle/6KSiYHrUdBkTMNaB8
- Emoji 19.0+ ESR priorities:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- Emoji 18.0 accepted proposal chart:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- UTC #185 minutes recording the Emoji 18.0 acceptances:
  https://www.unicode.org/L2/L2025/25226.htm
- Current proposal status definitions:
  https://www.unicode.org/emoji/emoji-proposals-status.html

The 2026 submission window closes at the end of day on 2026-07-31. The PDF must be publicly accessible
without a login and submitted through the official form.

## Evidence hierarchy and limits

Every requirement in this specification has one of four evidence levels:

- `U - Unicode requirement`: stated in the current official guidelines, agreement, form, or status rules.
- `D - Current decision evidence`: stated in UTC minutes, ESR priorities, or the current accepted cohort.
- `O - Observed practice`: a reproducible descriptive pattern in proposal documents. It does not prove cause.
- `I - Internal control`: a project quality gate chosen to reduce filing risk. It is not a Unicode rule or an
  approval predictor.

When sources conflict, `U` controls. A historical accepted proposal is never permission to ignore a current
requirement.

## What the proposal review actually found

The review covered the first page of 63 accepted proposal PDFs, complete page-by-page review of six
representative accepted proposals, and the full text of 15 confirmed declined Medical Emoji proposal drafts.
The accepted set included the latest cohort. The declined drafts' original embedded images are no longer
available, so no visual claim is made about that group.

### Repeatable strengths in successful proposals

- The first page lets a reviewer identify the concept, submitters, date, keywords/category, artwork, and rights
  quickly. This is especially consistent in recent proposals because the current rules require it.
- The proposal defines a narrow meaning that existing emoji cannot express, names the strongest existing
  substitute, and explains what the new character would express that the substitute cannot.
- Selection factors are treated as tests, not boxes to inflate. Strong proposals use `N/A` instead of inventing
  meanings, completeness, or compatibility.
- Frequency screenshots are readable and interpreted. Stronger documents preserve query settings, dates, and
  comparators so the evidence can be reproduced.
- The artwork's identity comes from its outline or a few stable cues that survive at 18x18, not from internal
  detail visible only at 72x72.
- The exclusions are answered against the proposal's real failure modes, especially Already representable,
  Overly specific, and Open-ended.
- Genuine compatibility can be decisive, but only when an existing popular system uses the same pictograph at
  demonstrably high frequency.

### Repeatable risks in the confirmed declined proposals

The 15 confirmed declined drafts are not a controlled experiment, and Unicode did not publish complete
reviewer reasoning. They nevertheless expose relevant proposal-level risks:

- Clinical burden, professional importance, or desired awareness was often asked to do the work of expected
  communicative use.
- Petitions, calls for an emoji, Instagram, or Twitter appeared in 13 of 15 drafts. Those are not acceptable
  frequency evidence under the current rules.
- All 15 contained the exclusion-section skeleton. Completeness of headings did not rescue a weak concept-level
  case.
- Open-ended answers often argued that a symbol would be broadly important without showing why that candidate
  was independently selective and would not imply an unbounded organ set.
- The old evidence packages do not meet today's five-source, `elephant`, widest-range, and reproducibility
  instructions.

These are risk indicators, not proof that a particular word or section caused a decline. Medical subject matter
is confounded with this archive and must not be treated as a negative factor by itself.

### Accepted counterexamples that corrected this rubric

- Monarch Butterfly was accepted despite extensive awareness and advocacy context. Unicode's rule is that a
  cause cannot be the reason for encoding, not that cause-related words may never appear. Its independent
  compatibility case was central:
  https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf
- X-Ray shows that medical importance can provide background when the proposal also establishes an iconic,
  recognizable, broadly usable building block. Importance still cannot substitute for expected use:
  https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf
- Orca was accepted even though several screenshots in the final PDF render as broken or blank warning icons.
  Its reasoning can be learned from; its layout is not a quality model:
  https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf
- Thumb Point explains that a requested Google Video count was unavailable, and Eraser is substantially
  image-based. These are evidence that accepted proposals can contain exceptions or technically awkward PDFs,
  not permission to plan a best-in-class filing around an exception:
  https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf
  https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf

There is no validated hard limit for pages, words, or embedded PDF image objects. Recent accepted proposals
range from compact to long and from polished to awkward. The controllable target is reviewer effort: complete,
legible, reproducible, and no longer than the case needs.

## Method note on the historical comparison

The former 55-versus-29 "winners versus losers" study is not reliable enough to support numeric approval
claims. The repository contains the 55 accepted texts, but no membership manifest, source files, extracted
texts, or analysis code for the 29-document comparison group. Repository history confirms those artifacts were
never committed.

The groups were also not matched: the accepted documents have L2 dates from 2020 through 2024, while the
unavailable comparison was described as 2017 through 2021. At least 17 of the 55 accepted documents name
Jennifer Daniel or the Emoji Subcommittee, and one is a committee strategy document rather than an ordinary
public submission. Register absence, chart absence, and formal decline are different outcomes. Current status
can also change: a proposal may be under consideration or later succeed through another document.

The exact 29-document percentages and causal statements derived from them are retired. They must not be used
to set word, page, image, sort-location, social-media, or cause-language thresholds.

### Reproducible corpus measurements

The tracked accepted archive contains 55 documents associated with Emoji 14.0 through 17.0. Direct
recomputation finds:

- Median extractable text: 907 words; 919.5 after excluding the one near-empty text layer.
- Median pages: 7.
- Median explicit case-insensitive `N/A` count: 1.
- The exclusion terms appear in 52 of 55; Faulty comparison in 51 of 55; elephant in 18 of 55.
- A literal `sort location` match appears in 33 of 55, while normalized `sort location` or `sort order`
  appears in 45 of 55. The former reported 30% rate cannot be reproduced.
- Depending on whether masks, repeated objects, or unique PDF object IDs are counted, the median PDF image
  total is 40, 30, or 24. PDF object counts are not counts of meaningful screenshots.

The confirmed declined Medical Emoji archive contains 15 drafts. All 15 answer every exclusion heading,
13 mention social-media or petition terms, 7 contain the audited cause terms, and only 3 mention elephant.
This is useful project-specific failure evidence, but it still does not establish why each proposal was
declined.

Reproduction code and the detailed audit are in:

- `evidence/emoji_proposal_corpus_audit.py`
- `docs/research/unicode-winning-submissions/analysis.md`

### Latest accepted proposal set

The eight accepted proposal documents for the nine Emoji 18.0 characters are:

- L2/25-252, Leftwards and Rightwards Thumb Signs:
  https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf
- L2/25-253, Pickle:
  https://www.unicode.org/L2/L2025/25253-emoji-pickle.pdf
- L2/25-254, Monarch Butterfly:
  https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf
- L2/25-255, Eraser:
  https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf
- L2/25-256, Lighthouse:
  https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf
- L2/25-257, Meteor:
  https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf
- L2/25-258, Net With Handle:
  https://www.unicode.org/L2/L2025/25258-emoji-net.pdf
- L2/25-259, Squinting Face:
  https://www.unicode.org/L2/L2025/25259-emoji-squinting-face.pdf

The face was later changed to Cracking Face using L2/26-048:

https://www.unicode.org/L2/L2026/26048-cracked-smiling-face-emoji.pdf

The Emoji 18 documents range from 7 to 19 pages. Text extraction is unreliable for the image-only Eraser PDF,
and embedded-image counts vary with PDF construction, so neither word count nor PDF object count is treated as
a quality threshold for that cohort.

UTC #185 records that the theme of the Emoji 18 set was compatibility. ESR's Emoji 19.0+ priorities then set a
higher benchmark around cited empirical use, compatibility with popular systems where real, and improvements
to the experience of existing emoji. These are current-cycle signals, not new automatic eligibility rules.

## What best-in-class means

A best-in-class proposal is complete, easy to verify, visually credible at 18 pixels, concise enough to review
quickly, and strong on its own merits. Importance, advocacy, professional prestige, and comparison with weaker
historical emoji may provide context, but cannot be the reason for encoding.

### 1. Must-pass filing gates

If any gate is unresolved, label the proposal `NOT READY TO SUBMIT` regardless of its score.

| Gate | Level | Required outcome |
| --- | --- | --- |
| Eligibility | U | The concept is confirmed eligible, not already approved, and not blocked by status or the four-year rule. Save the confirmation. |
| Coordination | U/I | No unresolved duplicate exists for the concept. Coordinate parallel authors where possible. |
| Authorship | U/I | Every submitter has explicitly agreed to be named. One person is the main point of contact. Multiple names use semicolons. |
| Public PDF | U | The exact final PDF has a stable public HTTPS URL that works logged out. |
| Official form | U | The exact public PDF is filed through the official form before the deadline. |
| Rights | U | The submitter can make the required ownership or open-license warranty. |
| Required art | U | Color and true black-and-white images at exactly 18x18 and 72x72 appear at the top of page 1. |
| Frequency evidence | U | All five required screenshots are present, reproducible, and legible. |
| Comparator and scope | U | Trends and Ngram show `elephant`; tools with range/location settings use the widest possible range. |
| Selection factors | U | Every current inclusion and exclusion factor is answered; unsupported positive factors are marked `Not applicable`. |
| Automatic-decline screen | U | No logo, brand, protected work, UI icon, signage, text, exact-image demand, directional variant, or other excluded category is present. |
| Final QA | I | The PDF has no draft note, stale date, placeholder, broken image, clipped text, unreadable screenshot, or contradictory status statement. |

### 2. First-page contract

The top of page 1 must contain, in this order or an equally obvious arrangement:

- `Proposal for Emoji: <name>`.
- Submitter names and one named main point of contact.
- Current revision date.
- Search-oriented keywords that do not repeat the proposal name, and the proposed category.
- Color and black-and-white 18x18 and 72x72 images.
- A direct image-rights and license statement by the person authorized to make it.

The reviewer should be able to validate identity, scope, imagery, and rights without leaving page 1. A suggested
sort location can be included as optional reviewer assistance, but the current format requires category, not a
separate sort-location field.

### 3. Evidence standard

Required evidence is necessary but not sufficient. Every factual claim used to earn a selection factor must
also be supported by a screenshot or citation.

Required screenshots:

1. Google Search, with visible result count.
2. Google Video Search, with visible result count.
3. Google Trends Web Search, concept versus `elephant`, Worldwide, widest date range.
4. Google Trends Image Search, concept versus `elephant`, Worldwide, widest date range.
5. Google Books Ngram Viewer, concept versus `elephant`, widest available date range.

For every capture, record the date, complete query URL, location, range, search mode, and any category filter.
Use a private browser when possible. Do not silently crop away the settings or the result needed to reproduce
the claim.

Best-in-class evidence also does the following (`I`, unless the current guideline states otherwise):

- Uses recent captures for a current filing unless an older snapshot adds historical value.
- Separates frequency evidence from examples of meaning.
- Cites durable dictionary, standards, academic, or institutional sources for metaphorical and factual claims.
- Explains ambiguous search terms and any filtering.
- Never uses petitions, calls for an emoji, hashtags, endorsements, or campaign advocacy as frequency evidence.
  Cause-related usage may be described when it is established, cited, and not the reason for encoding.
- Does not claim worldwide relevance from U.S.-only data.

### 4. Section-by-section argument guide

This guide separates three things that are easy to conflate:

- `Unicode asks`: the question the current guideline requires the proposal to answer.
- `Accepted pattern`: a repeated, useful practice observed in accepted proposals. It is descriptive, not a
  causal approval formula.
- `Drafting pattern`: the recommended reviewer-facing shape for this project.

The accepted corpus is heterogeneous. Its median extractable text is 907 words, but accepted documents range
from compact to long and from polished to awkward. Exclusion terms appear in 52 of 55 tracked accepted texts,
and the median text contains one explicit `N/A`. These measurements support direct answers and justified omission;
they do not establish a winning length or magic phrase.

#### Title, submitter, and date

**Unicode asks:** Identify the proposed emoji, the individual submitters, one main point of contact, and the
current revision date.

**Accepted pattern:** Strong recent first pages treat this as metadata, not a pitch. The title names the entity;
the names and date are easy to scan; no slogan or biography interrupts the required information.

**Drafting pattern:** Use the exact title `Proposal for Emoji: <name>`, one compact submitter line, one main
contact, and an ISO date. Do not spend a paragraph establishing credentials, institutional prestige, or campaign
history.

#### Identification

**Unicode asks:** Supply suggested search-oriented keywords and the proposed category. The 2026 format does not
require a separate CLDR short-name or sort-location field, and keywords must not merely repeat the proposal name.

**Accepted pattern:** Strong proposals give concrete synonyms, actions, associations, or meanings that help a
person find the emoji. They keep the category line short and use the current Emoji Ordering vocabulary.

**Drafting pattern:** Use a compact keyword list and one category line. Add prose only when a name is genuinely
ambiguous. Prefer familiar search words over technical taxonomies or an exhaustive medical vocabulary.

#### Images and license

**Unicode asks:** Put color and true black-and-white images at 18x18 and 72x72 at the top of page 1, followed by
a rights statement that satisfies the current agreement.

**Accepted pattern:** The best first pages show the four images in a simple matrix and state ownership or the
open license directly. The artwork is allowed to carry the visual claim before the proposal discusses it.

**Drafting pattern:** Show the assets, then use one precise ownership/license paragraph. If the art is external,
include the source and license URL. Do not narrate commissioning, AI assistance, file conversion, asset hashes,
or the validation pipeline unless a legal fact makes that information necessary.

#### Multiple meanings

**Unicode asks:** Does the proposed emoji have established metaphorical references, symbolism, or meanings beyond
the literal entity? Puns do not count, and the guideline says to use `N/A` without compelling examples.

**Accepted pattern:** Strong answers begin with the literal meaning, then give a small number of recognizable
extensions. Treasure Chest moves from valuables to discovery and sentimental value through concrete situations,
not abstract claims of versatility.

**Drafting pattern:** Start with one conclusion sentence. Follow with two to four established meanings, each
understandable without specialist knowledge, and cite a dictionary or durable source when the meaning is not
self-evident. Do not relabel clinical use cases as metaphor. Use `Not applicable` rather than inventing a pun.

#### Use in sequences

**Unicode asks:** Can the character combine with existing emoji to make an additional, understandable message?
The guideline says to use `N/A` without compelling examples.

**Accepted pattern:** Useful answers present a few short combinations and translate each into ordinary language.
The second emoji changes or narrows the message; it is not merely adjacent decoration. Some accepted historical
proposals say the emoji stands alone, but that does not answer the current positive factor.

**Drafting pattern:** Give two to five `candidate + existing emoji: resulting message` examples. Choose the
clearest combinations, not every medically related emoji. If the sequences would require explanation longer than
the message, write `Not applicable`.

#### Breaks new ground

**Unicode asks:** Answer `Yes` or `No`: does the candidate add a meaning that is new and different rather than a
variant of an existing emoji or sequence?

**Accepted pattern:** Strong answers name the closest current substitute and identify the ordinary message it
cannot convey. Treasure Chest distinguishes discovery and sentimental value from money; Lighthouse identifies a
maritime guidance structure not expressed by a house, flashlight, or wave.

**Drafting pattern:** Use `Yes.` or `No.` first. Then write: `[closest emoji or sequence] expresses [existing
meaning], but it does not express [remaining meaning]. [Candidate] adds [broad communicative function].` Do not
argue that the field, disease, or organ is important, or that similar emoji already exist.

#### Distinctiveness

**Unicode asks:** Explain why most people should recognize the intended entity without foreknowledge at typical
emoji size, especially 18x18.

**Accepted pattern:** Strong answers name a few visible cues and the nearest visual confusion. Treasure Chest
points to the open rounded chest and coins; Apple's accessibility proposal explains why a hearing aid needed an
ear to establish its identity. The explanation stays on what a person can see.

**Drafting pattern:** Write: `[Candidate] is shown with [two to four stable visible cues]. At 18 pixels, [primary
cue] distinguishes it from [nearest visual alternatives]. Vendors may vary [nonessential details] while keeping
[essential cues].`
**Internal human approval:** Shuhan He reviews the exact 18x18 and 72x72 color and black-and-white assets at
actual size beside the nearest visual alternatives and records a dated `APPROVE` or `REVISE` decision. His
approval is the complete human image gate for this project. No participant panel, blind test, crowd study,
minimum sample size, recognition percentage, or confusion matrix is required. Any material artwork change
invalidates the prior approval and returns the final assets to Shuhan.

Computer checks remain useful internal controls for dimensions, palette, connectedness, and geometric
separation. Their algorithms, hashes, pinned assets, thresholds, pass/fail language, and machine-readable reports
belong in `READINESS`, validation, or QA records, not the submission PDF. Keep reviewer-facing prose focused on
the visible features that distinguish the image at emoji size.

#### Expected usage level

**Unicode asks:** Provide the five required frequency screenshots and enough interpretation to show current and
historical use of the concept.

**Accepted pattern:** Strong proposals state the most relevant accurate result plainly and preserve the query,
date, and settings. Fingerprint labels searches and dates so the reader can reproduce them; Orca connects its
comparison to the candidate's actual case.

**Drafting pattern:** Lead with one synthesis sentence about breadth, durability, or relative interest. Give the
observed figures and settings next to their screenshots. Explain an ambiguous search only when the ambiguity
would prevent a reviewer from understanding the exhibit. Do not bury the result in methodological disclaimers.
Disease prevalence, professional importance, or an organization's audience cannot substitute for
concept-frequency data.

#### Completeness

**Unicode asks:** Does the candidate close a genuinely fixed set, such as the zodiac, four card suits, or blood
types? Scientific and taxonomic categories are not fixed sets for this purpose.

**Accepted pattern:** Concise successful proposals commonly write `N/A`. A positive answer works only when the
proposal can name the finite set, its existing members, and how this one addition closes it.

**Drafting pattern:** For an organ, write `Not applicable.` Do not convert an anatomy taxonomy into a finite set
or say that existing body-part emoji create an entitlement to another.

#### Compatibility

**Unicode asks:** Is the same pictograph already used at high frequency in a popular existing system, making
Unicode encoding necessary for interoperability?

**Accepted pattern:** Genuine compatibility proposals identify the systems, show the actual pictographs, and
explain the mismatch encoding would resolve. Meteor is the clearest current model because its case concerns
inconsistent vendor implementations, not generic popularity or similar imagery online.

**Drafting pattern:** Unless equivalent system evidence exists, write `Not applicable.` If it does exist, name
the systems, show the same pictograph in use, quantify or document high usage, and state the exact interoperability
problem. Stickers, search images, branding, and ordinary social-media posts are not compatibility by themselves.

#### Already represented

**Unicode asks:** Can an existing emoji or short sequence already express the concept, even if it does not use the
same picture?

**Accepted pattern:** Strong answers volunteer the reviewer's best substitute and explain the remaining ambiguity.
Fingerprint addresses Index Pointing Up directly; Treasure Chest explains why money emoji cannot carry discovery
or sentimental value. Merely saying “there is no stomach emoji” does not answer the test.

**Drafting pattern:** Write: `[strongest substitute] can express [overlap], but it cannot clearly express [specific
remaining meanings].` Address meaning before appearance, and do not construct an implausibly long sequence just
to make the candidate look necessary.

#### Overly specific

**Unicode asks:** Is the proposal a narrow subtype when a broader existing or proposed character would serve?

**Accepted pattern:** Strong answers define the general class the image represents and explain why its visible
form is a recognizable example rather than a request for a narrow subtype. Treasure Chest explains that the coins
make the broad concept readable without limiting the meaning to coins.

**Drafting pattern:** State the broad communicative category first, then distinguish the candidate from a disease,
procedure, specialty, brand, model, species variant, or decorative style. Do not defend specificity by saying
that Unicode already encoded something equally narrow; that becomes faulty comparison.

#### Open-ended

**Unicode asks:** Would accepting this candidate invite an unbounded series of equally valid additions, with no
principled reason to choose this one?

**Accepted pattern:** Strong answers supply a limiting principle. A terse “not part of a set” works only when it
is obviously true. Better answers identify the neighboring concepts a reviewer will raise and show why this
candidate's independent meanings, usage, or function make it separately selectable.

**Drafting pattern:** Name the likely follow-on candidates and explain the boundary that prevents automatic
expansion. For organs, do not promise that no other organ will ever be proposed and do not argue that anatomy
should be completed. Show why this organ stands on its own under the same criteria.

#### Transient

**Unicode asks:** Is expected use durable, rather than tied to a fad, temporary event, campaign, or product?

**Accepted pattern:** Strong answers point to a long-lived concept, established expression, historical record, or
Books Ngram evidence. Treasure Chest ties the symbol to longstanding cross-cultural use and a durable literary
trope rather than merely asserting that treasure is old.

**Drafting pattern:** Give one conclusion sentence and one or two dated, cited indicators of continuity. Avoid
unsupported phrases such as “since the beginning of time” or assuming that biological age proves communicative
durability.

#### Faulty comparison

**Unicode asks:** Is the proposal justified primarily because a similar, less useful, or less important emoji was
encoded in the past?

**Accepted pattern:** Strong answers disclaim analogy briefly and restate the independent basis: current use,
distinct meaning, and recognizability. They do not reopen a catalog of historical inconsistencies.

**Drafting pattern:** Write: `This proposal does not depend on [existing emoji] being encoded. Its case rests on
[candidate's independent use, meanings, and visual identity].` Never write “Heart and Lungs exist, so Kidney
should too.”

#### Other information

**Unicode asks:** Supply genuinely helpful information not covered above, especially design considerations.

**Accepted pattern:** The most useful answers advise vendors which visual cues are essential and which may vary.
Treasure Chest recommends a simple coin-filled design because other contents become unclear at small sizes.

**Drafting pattern:** Use one short paragraph about vendor freedom and essential cues. Add naming or cultural
ambiguity only when it changes implementation. Do not put biographies, advocacy, internal scores, test methods,
release status, asset manifests, or project workflow here.

#### Evidence of frequency

**Unicode asks:** Include readable screenshots for Google Search, Google Video Search, Google Trends Web Search,
Google Trends Image Search, and Google Books Ngram Viewer; use `elephant` where required and preserve the widest
available ranges.

**Accepted pattern:** Strong evidence sections label each source, show the screenshot at readable size, and add a
short interpretation rather than forcing the reviewer to infer the result. They record dates and settings and
state the relevant result accurately.

**Drafting pattern:** For each source use: `Captured <date> using <query/settings>. The displayed result shows
<observation>.` Add disambiguation only when essential to interpret the result. Keep the complete reproducible
URL with the capture record; in the PDF, use a readable link treatment that does not break the page. Never use
petitions, hashtags, calls for the emoji, or endorsements as frequency evidence.

### 5. Writing, language, and layout standard

- Write for an educated general reader who knows the Unicode criteria but does not know medicine, computer
  vision, software engineering, or this project's workflow.
- Prefer ordinary words, direct sentences, concrete examples, and active voice. Use “meaning that existing emoji
  cannot express” instead of “semantic gap,” and “closest visual alternatives” instead of “declared confusers.”
- If a specialist term is essential to the concept, define it once immediately in plain English. Do not use a
  technical term merely because it sounds more precise.
- Keep internal QA language out of the proposal. Do not publish algorithms, hashes, thresholds, gates, pass/fail
  reports, pinned-asset language, or machine-validation statistics unless Unicode specifically requests them.
- Give each paragraph one job: conclusion first, strongest evidence or example second, nearest objection when
  relevant, then stop.
- Use no more prose than the case needs. There is no validated winning word, page, or image-count threshold. A
  short proposal is useful only when it remains complete and evidentially strong.
- Use direct section names that mirror the current guidelines, and preserve their current order.
- Use tables only when they reduce reviewer effort.
- Keep screenshots large enough to read at 100% zoom.
- Avoid large blank pages, stranded headings or paragraphs, split labels, and long raw URLs that disrupt the page.
- Use page numbers and a stable document title.
- Do not add biographies, endorsements, press language, campaign history, or internal release status unless
  directly required.

## Authorship source of truth

- A proposal may have one or many individual submitters. The confirmed byline for that proposal controls; there
  is no project-wide author-count rule.
- Separate multiple names with semicolons. Credentials and affiliations are optional, and a proposal may list
  more than one affiliation for an author when accurate.
- Before editing a byline, read the proposal's latest consent, author-verification, or source-ledger record and
  preserve every confirmed individual in the recorded order. A later explicit confirmation supersedes an older
  record.
- Freeze the exact author names, credentials, and affiliations before the final PDF is built. Keep them
  consistent in the source record, PDF, public file, and official form.
- Name one main point of contact even when a proposal has several authors or affiliations.
- Preserve written confirmation that every person agreed to be named. Do not add, remove, or reorder authors to
  satisfy an assumed preferred author count.

Unicode requires one emoji per proposal; it does not forbid one submitter from filing three separate proposals
in the same cycle. Kidney, Liver, and Stomach may therefore be filed as three documents. Because parallel organ
proposals intensify the `Open-ended` objection, each document must avoid a set-completion argument and prove why
that organ independently deserves one of the limited annual additions. Do not promise that no other organ will
be proposed, and do not claim that filing one organ logically requires the other two.

## Internal 100-point readiness score

This is a project control, not a Unicode score or approval prediction.

| Area | Points | Full-credit standard |
| --- | ---: | --- |
| Eligibility and coordination | 15 | Confirmation archived; no duplicate filing risk; authorship confirmed. |
| First-page format | 10 | Every current first-page requirement is correct and easy to find. |
| Image package and rights | 15 | Rights are clear; four exact assets pass technical checks and have Shuhan's recorded actual-size approval. |
| Frequency and empirical evidence | 20 | Five current, reproducible captures plus citations for material usage claims. |
| Inclusion factors | 15 | Each factor is direct, evidenced, and uses `N/A` where appropriate. |
| Exclusion factors | 10 | Strongest reviewer objections are answered specifically. |
| Worldwide and durable case | 5 | Evidence is worldwide where available and avoids cause-only framing. |
| Validation and reproducibility | 5 | Computer checks, sources, thresholds, hashes, and machine-readable results reproduce cleanly. |
| Packet and filing control | 5 | Versioned packet, clean PDF, public URL, and filing record are synchronized. |

Minimum to circulate: 80/100 with every known gap labeled.

Minimum to file: 90/100, every must-pass gate complete.

Target for these resubmissions: 100/100 before filing.

## One-at-a-time audit and correction workflow

For each concept, complete the following before moving to the next:

1. Freeze the exact author list and confirm one point of contact.
2. Red-team the strongest `Already representable`, `Overly specific`, and `Open-ended` objections.
3. Verify every factual claim has a citation or remove it.
4. Recapture all five required evidence sources with current, widest-range settings.
5. Build nearest-emoji art comparisons, run the reproducible 18x18 computer validation, and obtain Shuhan's
   dated approval of the exact four final assets at actual size.
6. Revise the source, update the date, and rebuild the PDF.
7. Render every page and inspect it visually.
8. Run technical checks for image dimensions/colors, text extraction, fonts, encryption, links, and file size.
9. Obtain domain/factual and Unicode/process signoff on the exact PDF.
10. Publish the exact PDF, verify the logged-out URL, file the official form, and archive confirmation.

## Definition of submission-worthy

A proposal is submission-worthy only when it has no unresolved must-pass gate, scores at least 90/100, and its
authorship, rights, art, evidence, validation, and independent selection case are reproducible without relying
on outside campaign context. Eligibility alone means the proposal may be filed; it does not mean the proposal
is ready or likely to advance.
