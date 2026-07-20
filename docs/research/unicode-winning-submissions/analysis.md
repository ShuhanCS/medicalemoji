# Emoji Proposal Evidence Audit

Updated: 2026-07-20

## Bottom line

The current Unicode guidelines are the only controlling submission rules. Accepted proposals are useful
examples, but the repository does not contain a validated statistical model of approval.

The former 55-versus-29 "winners versus losers" analysis is retired as quantitative evidence. Its accepted
archive exists; its 29-document comparison manifest, source texts, and analysis code do not. Several reported
measurements cannot be reproduced, the cohorts were not matched by year or author type, and absence from the
accepted-proposal chart was treated too loosely as a final negative outcome.

This audit preserves the observations that can be reproduced and separates them from internal drafting
heuristics.

## Controlling primary sources

- Current Unicode proposal guidelines:
  https://www.unicode.org/emoji/proposals.html
- Current proposal status definitions:
  https://www.unicode.org/emoji/emoji-proposals-status.html
- Emoji proposal FAQ:
  https://www.unicode.org/faq/emoji_submission.html
- Accepted proposal chart through Emoji 17.0:
  https://www.unicode.org/emoji/charts/emoji-proposals.html
- Accepted proposal chart for Emoji 18.0 beta:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- ESR priorities for Emoji 18.0 and 19.0+:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC #185 minutes recording Emoji 18.0 decisions:
  https://www.unicode.org/L2/L2025/25226.htm

Generated accepted-proposal manifest:

`docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json`

Reproduction code:

`evidence/emoji_proposal_corpus_audit.py`

## Audit of the 55-document accepted archive

The repository contains 55 extracted documents associated with emoji encoded in Emoji 14.0 through 17.0.
They have L2 document dates from 2020 through 2024. Calling them "every winning proposal written since 2020"
is too strong:

- The set begins with Emoji 14.0, not Emoji 13.1.
- Some concepts were drafted earlier and revised or assigned a later L2 number. Orca is dated 2019 inside its
  L2/24-249 PDF.
- At least 17 of 55 name Jennifer Daniel or the Emoji Subcommittee.
- L2/21-075 is a committee strategy document for heart-color coverage, not an ordinary public proposal.
- The accepted chart can associate one encoding decision with a different or consolidated document from the
  original public proposal.

The set is still useful as a reference library. It is not a clean sample of independent public submissions.

### Reproduced text measurements

The following definitions and counts are reproducible from the tracked markdown:

| Measure | Definition | Result |
| --- | --- | ---: |
| Documents | Files containing an L2 ID, source URL, and stored text-layer word count | 55 |
| Median extractable words | Stored `pdftotext -layout` count | 907 |
| Median words excluding the near-empty text layer | Same, excluding files below 100 words | 919.5 |
| Median explicit `N/A` | Case-insensitive `n/a`, allowing spaces around slash | 1 |
| Mentions an exclusion section or term | Word `exclusion` | 52/55 |
| Answers Already representable | Text beginning `already represent` | 53/55 |
| Answers Open-ended | `open-ended` or `open ended` | 52/55 |
| Answers Overly specific | Phrase `overly specific` | 51/55 |
| Answers Transient | Word `transient` | 52/55 |
| Answers Faulty comparison | Phrase `faulty comparison` | 51/55 |
| Mentions elephant | Word `elephant` | 18/55 |
| Mentions Google Trends | Phrase or trends.google URL | 45/55 |
| Mentions audited cause terms | awareness, stigma, advocacy, or deserves representation | 1/55 |

The one near-empty text layer is L2/23-260, Eye Bags Face, at one extractable word. X-Ray, L2/20-214,
contains 1,273 extractable words and is not the image-only outlier described in an earlier report.

### Measurements that depend on the definition

The earlier report said 30% of accepted documents stated a sort location. A literal case-insensitive `sort
location` search finds 33 of 55, or 60%. Normalizing the equivalent phrase `sort order` finds 45 of 55, or
82%. The reported 30% cannot be reproduced without the missing code and should not be used as a success
signal. Current Unicode instructions require a category on page 1; they do not list a separate sort-location
field.

Likewise, "image count" is not stable. Across the downloaded 55 PDFs:

| PDF measurement | Median |
| --- | ---: |
| Pages | 7 |
| All rows reported by `pdfimages -list` | 40 |
| Rows whose type is `image` | 30 |
| Unique underlying image object IDs | 24 |

Masks, reused icons, duplicated objects, and full-page scans all change these totals. None is a count of
meaningful screenshots. The earlier median of 26 cannot be treated as a proposal-quality threshold.

### Percentages must not hide small counts

The earlier report rendered one cause-term hit among 55 as 1%. It is 1.8%, conventionally 2%. More
importantly, a one-document count cannot support a claim that cause language is "thirteen times" more common
without a reproducible comparison cohort, confidence intervals, and stable coding rules. Exact numerators are
used in this audit.

## Why the 29-document comparison is not reproducible

The July 9 report described 29 community proposals from 2017 through 2021 that did not appear in the accepted
chart. Repository history contains only the prose report. It contains no:

- list of the 29 L2 document IDs;
- outcome annotation or annotation date;
- source PDFs or extracted texts;
- inclusion and exclusion decisions;
- regex or analysis program;
- duplicate, revision, renamed-concept, or later-acceptance handling.

The report also claimed that every submitted proposal in that period appeared in an L2 register. That is
false. The public status data and this repository's 15 declined Medical Emoji drafts demonstrate submissions
that never received L2 documents.

An L2-register-minus-accepted-chart design has additional outcome errors. It can include proposals that are
under consideration, expired, merged, revised, or later accepted through another document. For example,
L2/18-204 Lighthouse did not appear as an accepted proposal at the time of that old document, but Lighthouse
is now Recommended to UTC and included in the Emoji 18.0 accepted cohort. The current status sheet also lists
Chainsaw, Orchid, Submarine, and Vulture as Under Consideration. Without the missing 29-document manifest,
there is no way to know how many such cases affected the study.

The two cohorts were not era-matched. The accepted set uses L2 documents from 2020 through 2024, while the
comparison was described as 2017 through 2021. Template changes, current-factor changes, and author experience
can therefore look like approval effects.

## The confirmed declined Medical Emoji archive

The repository does contain 15 project drafts whose concepts and dates correspond to declined rows in the
official proposal-status export. This is the valid failure archive for project learning, with two limits:
the images are not committed, and public status does not reveal the reviewers' full reasoning.

Recomputed from the tracked markdown:

| Measure | Confirmed declined drafts |
| --- | ---: |
| Documents | 15 |
| Median markdown token count | 1,522 |
| Answers all five exclusion headings | 15/15 |
| Median explicit `N/A` count | 0 |
| Mentions Google Trends | 13/15 |
| Mentions elephant | 3/15 |
| Mentions petitions, Instagram, or Twitter | 13/15 |
| Mentions audited cause terms | 7/15 |

The decisive lesson is not that headings or length caused failure. All 15 had the selection-factor skeleton,
and well-formed proposals can still be declined. The reusable lessons are narrower:

1. The old evidence packages do not satisfy the current required-source and elephant instructions.
2. Social-media requests, petitions, and cause framing now expressly detract from the proposal.
3. A bundle of organ proposals makes the Open-ended objection harder; each organ needs an independent case.
4. None of these drafts reached an L2 register, so an L2-only comparison omits exactly the early-screen failure
   mode most relevant to this project.

## Emoji 18.0 update

UTC #185 accepted nine characters from eight proposal documents:

| Document | Proposal | Pages | Extractable words | URL |
| --- | --- | ---: | ---: | --- |
| L2/25-252 | Leftwards and Rightwards Thumb Signs | 10 | 990 | https://www.unicode.org/L2/L2025/25252-emoji-thumb-point.pdf |
| L2/25-253 | Pickle | 8 | 1,405 | https://www.unicode.org/L2/L2025/25253-emoji-pickle.pdf |
| L2/25-254 | Monarch Butterfly | 19 | 3,491 | https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf |
| L2/25-255 | Eraser | 7 | Not reliable | https://www.unicode.org/L2/L2025/25255-emoji-eraser.pdf |
| L2/25-256 | Lighthouse | 9 | 1,142 | https://www.unicode.org/L2/L2025/25256-emoji-lighthouse.pdf |
| L2/25-257 | Meteor | 8 | 799 | https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf |
| L2/25-258 | Net With Handle | 10 | 1,147 | https://www.unicode.org/L2/L2025/25258-emoji-net.pdf |
| L2/25-259 | Squinting Face | 7 | 1,592 | https://www.unicode.org/L2/L2025/25259-emoji-squinting-face.pdf |

The face was later changed to Cracking Face through L2/26-048:

https://www.unicode.org/L2/L2026/26048-cracked-smiling-face-emoji.pdf

These documents range from 7 to 19 pages and include an image-based PDF. They disprove a hard 1,200-word,
page, or image-count rule. UTC #185 says compatibility was unusually important to this set. That is a cohort
theme, not a license to claim compatibility without a real popular-system implementation and high-frequency
evidence.

## Findings that survive the audit

1. Current completeness is mandatory. Answer every current factor, include all five frequency screenshots,
   use elephant where instructed, supply the exact art sizes, and make the rights warranty.
2. Completeness is not competitiveness. The confirmed declined drafts answered the headings too.
3. `N/A` is correct when Unicode tells the submitter to use it. It is not a stylistic trick that causes
   acceptance.
4. Evidence quality is more useful than document-object counts. A reviewer must be able to read, reproduce,
   and interpret each material claim.
5. Current prohibitions control. Historical winners that cited social media or omitted a current item do not
   authorize doing so now.
6. Accepted examples are heterogeneous. Use Treasure Chest for concise structure, Fingerprint for technical
   proof, and current proposals for the current section order. Copy no proposal wholesale.
7. Parallel filing of Kidney, Liver, and Stomach is not forbidden. Unicode requires one emoji per proposal.
   The strategic cost is a stronger Open-ended objection, so each document must stand independently and avoid
   set-completion rhetoric.
8. A readiness score can test completeness and operational control; it cannot estimate approval probability.

## Implications for the 2026 organ slate

- Kidney has the strongest current frequency package but still needs a hard 18x18 test against Beans and the
  complete confirmed author list.
- Stomach has the strongest multiple-meaning case and clear silhouette, but its historical captures need a
  current reproducibility review.
- Liver has the largest evidence and distinctiveness gap because its Trends evidence is old and U.S.-only and
  its small black-and-white silhouette lacks a unique identifying cue.
- Each proposal should state why it is independently broad and useful. None should claim that the three organs
  form a complete set or that existing Heart, Lungs, or Brain justify another organ.
- All three need final citation cleanup, independent review, a stable public PDF URL, and archived filing
  confirmation.

Detailed readiness audit:

`docs/proposals/2026-organ-submission-audit.md`
