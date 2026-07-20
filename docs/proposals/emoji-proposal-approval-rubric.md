# Best-in-Class Emoji Submission Specification

Version: 2.0

Last checked: 2026-07-20

Applies to: Kidney, Liver, and Stomach proposals for the 2026 Unicode intake

## Decision

There is no single accepted proposal that should be copied verbatim. The best submission model is a
composite of:

1. The current Unicode requirements, which control even when older accepted proposals used a different
   format.
2. The strongest repeatable practices in the historical accepted-proposal corpus.
3. The clearest differences between accepted proposals and a comparison group of proposals that were not
   encoded.
4. The latest Emoji 18.0 accepted cohort and the Emoji 19.0+ priorities published by the Emoji Standard &
   Research Working Group (ESR).

The closest single general-purpose exemplar is Treasure Chest, L2/24-255. It is concise, treats the emoji as
a broad building block, states independent utility, and answers the exclusion factors directly:

https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf

Fingerprint, L2/23-258, is a stronger model for reproducible evidence and disciplined technical presentation:

https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf

Meteor, L2/25-257, is the clearest current model for a genuine interoperability proposal, but its compatibility
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

## Evidence base and limits

### Historical comparison

The repository's prior structured comparison covered:

- 55 proposal documents from 2020 onward associated with emoji encoded in Emoji 13.1 through 17.0.
- 29 community proposal documents from similar registers that do not appear in the accepted-proposal chart.

The second group is a "not encoded" comparison group, not a proven list of proposals declined solely because
of document quality. The results are directional and should not be read as causal.

| Measure | Accepted (n=55) | Not encoded (n=29) |
| --- | ---: | ---: |
| Median words | 907 | 1,485 |
| Median pages | 7 | 9 |
| Median extracted images | 26 | 18 |
| Median explicit `N/A` count | 1 | 0 |
| Answers faulty comparison | 92% | 72% |
| States a sort location | 30% | 10% |
| Includes Trends evidence | 87% | 65% |
| Shows the `elephant` comparator | 32% | 13% |
| Cites petitions or social media | 45% | 75% |
| Uses cause or advocacy language | 1 accepted document | 13 not-encoded documents |

The useful signal is evidence density and disciplined argument, not a hard word or page limit.

### Emoji 18.0 update

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

The Emoji 18 documents range from 7 to 19 pages. Their median is 9 pages and their median extracted image
count is 55. Text extraction is unreliable for the image-only Eraser PDF, so word counts are not treated as a
quality measure for that cohort.

UTC #185 records that the theme of the Emoji 18 set was compatibility. ESR's Emoji 19.0+ priorities then set a
higher benchmark around cited empirical use, compatibility with popular systems where real, and improvements
to the experience of existing emoji. These are current-cycle signals, not new automatic eligibility rules.

## What best-in-class means

A best-in-class proposal is complete, easy to verify, visually credible at 18 pixels, concise enough to review
quickly, and strong on its own merits. It does not try to win by importance, advocacy, professional prestige,
or comparison with weaker historical emoji.

### 1. Must-pass filing gates

If any gate is unresolved, label the proposal `NOT READY TO SUBMIT` regardless of its score.

| Gate | Required outcome |
| --- | --- |
| Eligibility | The concept is confirmed eligible, not already approved, and not blocked by status or the four-year rule. Save the confirmation. |
| Coordination | No unresolved duplicate or parallel submission exists for the concept. |
| Authorship | Every submitter has explicitly agreed to be named. One person is the main point of contact. Multiple names use semicolons. |
| Public PDF | The exact final PDF has a stable public HTTPS URL that works logged out. |
| Official form | The exact public PDF is filed through the official form before the deadline. |
| Rights | The submitter can make the required ownership or open-license warranty. |
| Required art | Color and true black-and-white images at exactly 18x18 and 72x72 appear at the top of page 1. |
| Frequency evidence | All five required screenshots are present, dated, reproducible, and legible. |
| Comparator and scope | Trends and Ngram show `elephant`; tools with range/location settings use the widest possible range. |
| Selection factors | Every current inclusion and exclusion factor is answered; unsupported positive factors are marked `Not applicable`. |
| Automatic-decline screen | No logo, brand, protected work, UI icon, signage, text, exact-image demand, directional variant, or other excluded category is present. |
| Final QA | The PDF has no draft note, stale date, placeholder, broken image, clipped text, unreadable screenshot, or contradictory status statement. |

### 2. First-page contract

The top of page 1 must contain, in this order or an equally obvious arrangement:

- `Proposal for Emoji: <name>`.
- Submitter names and one named main point of contact.
- Current revision date.
- Suggested name, search-oriented keywords that do not repeat the name, category, and useful sort location.
- Color and black-and-white 18x18 and 72x72 images.
- A direct image-rights and license statement by the person authorized to make it.

The reviewer should be able to validate identity, scope, imagery, and rights without leaving page 1.

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

Best-in-class evidence also does the following:

- Uses recent captures for a current filing unless an older snapshot adds historical value.
- Separates frequency evidence from examples of meaning.
- Cites durable dictionary, standards, academic, or institutional sources for metaphorical and factual claims.
- Explains ambiguous search terms and any filtering.
- Never uses petitions, calls for an emoji, hashtags, endorsements, or awareness campaigns as usage evidence.
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

#### Distinctiveness

Prove, rather than assert, recognizability. Include:

- A nearest-emoji comparison board at 18x18 and 72x72.
- Color and black-and-white comparisons.
- The essential silhouette cues and which details vendors may vary.
- A small recognition test with people who were not told the answer in advance.

The pass target for the internal recognition test is at least 80% correct unprompted identification at 18x18,
with no single wrong concept dominating more than 10% of responses. This is an internal quality gate, not a
Unicode rule.

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

- Prefer 800 to 1,200 words of argument, excluding screenshot labels and URLs, when the case fits. This is a
  drafting target, not a Unicode limit.
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
  Danielle Miller; Timur Erk.
- Liver lists Shuhan He only.
- Stomach lists Shuhan He only.
- Shuhan He is the main point of contact for all three.

Credentials and affiliations are optional in the PDF. Names must be consistent between the PDF, public file,
and official form.

## Internal 100-point readiness score

This is a project control, not a Unicode score or approval prediction.

| Area | Points | Full-credit standard |
| --- | ---: | --- |
| Eligibility and coordination | 15 | Confirmation archived; no duplicate filing risk; authorship confirmed. |
| First-page format | 10 | Every current first-page requirement is correct and easy to find. |
| Image package and rights | 15 | Rights are clear; four exact assets pass technical checks and unprompted recognition. |
| Frequency and empirical evidence | 20 | Five current, reproducible captures plus citations for material usage claims. |
| Inclusion factors | 15 | Each factor is direct, evidenced, and uses `N/A` where appropriate. |
| Exclusion factors | 10 | Strongest reviewer objections are answered specifically. |
| Worldwide and durable case | 5 | Evidence is worldwide where available and avoids cause-only framing. |
| Independent review | 5 | Domain/factual and Unicode/process reviewers sign off on the final PDF. |
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
5. Build nearest-emoji art comparisons and run the 18x18 recognition test.
6. Revise the source, update the date, and rebuild the PDF.
7. Render every page and inspect it visually.
8. Run technical checks for image dimensions/colors, text extraction, fonts, encryption, links, and file size.
9. Obtain domain/factual and Unicode/process signoff on the exact PDF.
10. Publish the exact PDF, verify the logged-out URL, file the official form, and archive confirmation.

## Definition of submission-worthy

A proposal is submission-worthy only when it has no unresolved must-pass gate, scores at least 90/100, and a
reviewer can verify the authorship, rights, art, evidence, and independent selection case without relying on
outside campaign context. Eligibility alone means the proposal may be filed; it does not mean the proposal is
ready or likely to advance.
