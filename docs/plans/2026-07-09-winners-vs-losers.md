# Retired: winners versus losers comparison

Status: Retired as quantitative evidence on 2026-07-20

This file formerly reported a 55-document accepted cohort against 29 documents labeled "losers." Do not use
the former percentages, medians, causal claims, or drafting thresholds. The 29-document cohort manifest,
source texts, and analysis code do not exist in the repository or its history, so its membership and metrics
cannot be reproduced.

The controlling audit is:

`docs/research/unicode-winning-submissions/analysis.md`

The reproducible measurement program is:

`evidence/emoji_proposal_corpus_audit.py`

The current submission specification is:

`docs/proposals/emoji-proposal-approval-rubric.md`

## Why it was retired

1. The report said every submitted proposal from 2017 through 2021 appeared in Unicode's L2 registers. This
   project's 15 confirmed declined drafts did not receive L2 documents, disproving that premise.
2. The 29 document IDs and their outcome annotations were never recorded.
3. Absence from the accepted chart does not prove formal decline. A proposal can be expired, revised, merged,
   under consideration, or later accepted through another document.
4. The groups were not era-matched: accepted L2 documents from 2020 through 2024 were compared with an
   unavailable group described as 2017 through 2021.
5. At least 17 of the 55 accepted documents name Jennifer Daniel or the Emoji Subcommittee, and one is a
   committee strategy document. Author experience and submission channel were not controlled.
6. Several text measures depended on undocumented matching rules. For example, the old 30% accepted
   sort-location result cannot be reproduced: `sort location` appears in 33 of 55, and normalized `sort
   location` or `sort order` appears in 45 of 55.
7. PDF image totals count implementation objects, not meaningful screenshots. The same PDFs have medians of
   40, 30, or 24 depending on whether masks, image-type rows, or unique object IDs are counted.

## Findings retained in narrower form

- Current Unicode completeness rules are mandatory, but completed headings do not guarantee advancement.
- The 55 accepted-document archive has a median of 907 extractable words and 7 pages. These are descriptions,
  not targets.
- `N/A` should be used when the current guideline says to use it and there is no compelling example.
- Faulty comparison deserves a direct answer because the current guideline explicitly requires it, not
  because an unverified percentage predicts success.
- Petitions, social-media calls for an emoji, and cause-first arguments should be removed because current
  Unicode instructions say they are unacceptable or non-determinative.
- Each proposed organ must stand on its own. Filing Kidney, Liver, and Stomach as three separate proposals is
  allowed, but it makes the Open-ended case more demanding.

## Useful exemplars

- Treasure Chest, concise broad-building-block case:
  https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf
- Fingerprint, technical distinction and reproducible evidence:
  https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf
- X-Ray, nearby medical concept:
  https://www.unicode.org/L2/L2020/20214-x-ray-emoji.pdf
- Meteor, current compatibility-led case:
  https://www.unicode.org/L2/L2025/25257-emoji-meteor.pdf

No exemplar overrides the current guidelines:

https://www.unicode.org/emoji/proposals.html
