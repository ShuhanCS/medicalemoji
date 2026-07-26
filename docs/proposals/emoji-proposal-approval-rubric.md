# Best-in-Class Emoji Submission Specification

Version: 3.0

Last checked: 2026-07-26

Applies to: Kidney, Liver, and Stomach proposals for the 2026 Unicode intake

Practical agent entry point:
[`../../PROPOSAL-GUIDE.md`](../../PROPOSAL-GUIDE.md)

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
- The proposal defines a narrow semantic gap, names the strongest existing substitute, and explains what the
  new character would express that the substitute cannot.
- Selection factors are treated as tests, not boxes to inflate. Strong proposals use `N/A` instead of inventing
  meanings, completeness, or compatibility.
- Frequency screenshots are readable and interpreted. Stronger documents preserve query settings, dates,
  comparators, and limitations so the evidence can be reproduced.
- The artwork's identity comes from a silhouette or a few stable cues that survive at 18x18, not from internal
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
- Suggested name, search-oriented keywords that do not repeat the name, and category.
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

### 4. Selection-factor standard

#### Multiple meanings

Use only established non-pun meanings backed by citations. Mark `Not applicable` when the literal concept is
the real case. A short valid `N/A` is stronger than a speculative list.

#### Use in sequences

Give a small set of combinations that create distinct, plausible messages. Do not list every adjacent medical
emoji. Show what becomes clearer because the proposed emoji exists.

#### Breaks new ground

Answer `Yes` or `No` immediately. Identify the nearest current emoji and explain the semantic gap in ordinary
communication. Do not rely on the existence of other body-part emoji.

For a normal Medical Emoji filing candidate, the project answer must be `Yes`. This means the character adds a
new semantic building block; it does not mean the underlying object should be novel, obscure, scientifically
new, or visually experimental. If the honest answer is `No`, stop the proposal unless a genuine high-frequency
compatibility need in a popular existing system is documented and escalated. Completeness of anatomy is not
such an exception.

#### Distinctiveness

Prove, rather than assert, recognizability. Include:

- A nearest-emoji comparison at 18x18 and 72x72.
- Color and black-and-white comparisons.
- The essential silhouette cues and which details vendors may vary.
- A reproducible computer-validation report with pinned comparator assets, hashes, declared thresholds, and
  machine-readable output.
- An unprompted general-viewer recognition test at actual 18x18 size, with raw answers preserved.

For Kidney, the coordinator-selected computer gate requires exact dimensions, a true black-and-white palette,
foreground connectedness, normalized silhouette IoU no greater than 0.72, and 64-bit difference-hash distance
of at least 16 against each declared comparator. This is an internal technical-separability control, not a
Unicode rule or a claim about human semantic recognition. It is a useful engineering check, but it cannot
replace recognition testing: two silhouettes can be measurably different while both are named `bean`, `blob`,
or `generic organ` by viewers.

The internal recognition gate uses at least 12 people who were not told the target. Test the 18x18 color and
black-and-white images separately at actual size, free response before forced choice. At least 10 of 12 must
name the intended concept or an accepted synonym in both passes, with no wrong concept dominating. Archive the
prompt, raw answers, scoring rule, and confuser list. This is a project quality standard, not a Unicode rule.

#### Expected usage

Lead with the five required reproducible sources and numerical observations. Add only cited, durable contexts
that show breadth. Disease burden or professional importance cannot substitute for actual use of the concept.

#### Completeness and compatibility

Mark each `Not applicable` unless there is compelling evidence. An organ does not complete a finite anatomy
set. Compatibility earns weight only when a popular social app, standard, or operating system already uses the
same or nearly identical pictograph at demonstrably high frequency.

### 5. Exclusion-factor standard

Write these answers before polishing the inclusion case:

- `Already representable`: identify the strongest substitute or sequence and explain the remaining ambiguity.
- `Overly specific`: show that the proposed concept is a broad building block, not a disease, procedure,
  specialty, campaign, subtype, or branded image.
- `Open-ended`: explain why this concept stands independently and does not imply that every organ must follow.
- `Transient`: support durable use over time rather than asserting that anatomy is old.
- `Faulty comparison`: state that existing organs do not justify this one and restate the independent evidence.

### 6. Writing and layout standard

- Use no more prose than the case needs. There is no validated winning word, page, or image-count threshold.
  A short proposal is useful only when it remains complete and evidentially strong.
- Use direct section names that mirror the current guidelines.
- Put the conclusion first in each factor.
- Use tables only when they reduce reviewer effort.
- Keep screenshots large enough to read at 100% zoom.
- Avoid large blank pages, stranded headings, split labels, and long raw URLs that disrupt the page.
- Use page numbers and a stable document title.
- Do not add biographies, endorsements, press language, or campaign history unless directly required.

## Authorship rules for the 2026 organ slate

- Kidney must list the complete confirmed author set:
  Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee;
  Danielle Miller; Timur Erk; David Rhew; Heena Purohit.
- Liver lists Shuhan He only.
- Stomach lists Shuhan He only.
- Shuhan He is the main point of contact for all three.

Credentials and affiliations are optional in the PDF. Names must be consistent between the PDF, public file,
and official form.

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
| Image package and rights | 15 | Rights are clear; four exact assets pass technical checks and unprompted 18x18 recognition. |
| Frequency and empirical evidence | 20 | Five current, reproducible captures plus citations for material usage claims. |
| Inclusion factors | 15 | Each factor is direct, evidenced, and uses `N/A` where appropriate. |
| Exclusion factors | 10 | Strongest reviewer objections are answered specifically. |
| Worldwide and durable case | 5 | Evidence is worldwide where available and avoids cause-only framing. |
| Validation and reproducibility | 5 | Computer checks reproduce cleanly and the raw human-recognition record passes the declared gate. |
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
5. Build nearest-emoji art comparisons, run reproducible computer validation, and pass the unprompted 18x18
   recognition test.
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
