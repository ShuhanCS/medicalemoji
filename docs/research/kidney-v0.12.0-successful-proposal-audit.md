# Kidney v0.12.0 Audit Against Successful Unicode Proposals

Date: 2026-05-14

Audited packet:
https://github.com/ShuhanCS/medicalemoji/tree/master/submissions/v0.12.0

Submission source audited:
https://github.com/ShuhanCS/medicalemoji/blob/master/submissions/v0.12.0/v0.12.0_kidney_emoji_proposal_SUBMIT.md

## Executive Finding

The kidney v0.12.0 packet is now structurally viable: it has the required four example images, rights language, five frequency evidence screenshots, broader non-medical framing, a visual review board, exclusion-factor answers, and recovered support-letter links.

Against recent accepted proposals, the biggest remaining weakness is not missing evidence; it is presentation. Successful proposals make the reviewer reach the conclusion quickly. v0.12.0 still asks the reviewer to assemble too much of the argument from narrative text and images. The next version should make the strongest facts visible in tables and compact first-page/first-section summaries.

Recommended next packet target: `v0.13.0`, because the changes below would be substantive proposal changes, not just typo fixes.

## Comparator Set

The highest emoji-count accepted proposals are mostly older carrier-set, compatibility, ZWJ, directionality, or administrative batches. They are not the best model for a 2026 single-emoji kidney proposal because Unicode's submission format has changed substantially.

The better comparator set is recent single-emoji accepted proposals plus one body-adjacent proposal:

| Comparator | Why it matters | URL |
| --- | --- | --- |
| Falling Debris / Landslide | Strong model for closing the open-ended category objection with a defined external taxonomy. | https://www.unicode.org/L2/L2024/24257-falling-debris-emoji.pdf |
| Treasure Chest | Strong model for universal concept, metaphor, sequence examples, and concise substitute analysis. | https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf |
| Lime | Strong model for food/shape distinction and visual design guidance that makes the concept legible at small size. | https://www.unicode.org/L2/L2023/23031-emoji-lime.pdf |
| Orca | Strong model for distinctiveness, comparator frequency, alternate names, and non-substitutability. | https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf |
| Fingerprint | Strong model for reproducible URLs, result counts, sequence examples, and a body-related but non-clinical concept. | https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf |
| Trombone | Strong model for simple "new ground" and visual difference from nearby emoji. | https://www.unicode.org/L2/L2024/24256-trombone-emoji.pdf |

Current Unicode guidelines remain controlling:
https://www.unicode.org/emoji/proposals.html

## What v0.12.0 Already Does Well

| Area | Assessment |
| --- | --- |
| Required assets | Pass. The packet contains 18x18 and 72x72 color and black-and-white images at the top of the proposal source. |
| Rights | Strong draft. ConductScience ownership and Alla Shamanska / ConductScience credit are documented. |
| Frequency evidence | Pass. All five current required evidence categories are present: Google Search, Google Video Search, Google Trends Web, Google Trends Image, and Books Ngram. |
| Broader concept | Improved. The proposal now leads with body, education, food language, hydration, filtration, wellness, donation, transplant, stones, urine, and health rather than only nephrology. |
| Cause-only risk | Mostly controlled. Public-health facts support durability, and the text says support letters are not frequency evidence. |
| Existing substitutes | Good. The bean/drop/hospital/pill/syringe/anatomical-organ substitute table is one of the strongest parts of the current draft. |
| Visual risk | Improved. The proposal now admits the kidney is less iconic than heart and uses paired kidneys with vessels/ureters to reduce bean confusion. |

## Highest-Value Improvements

### 1. Add A Frequency Summary Table Before The Screenshots

Recent successful proposals make frequency data easy to scan. v0.12.0 includes the screenshots but does not summarize the exact captured counts and reproducible URLs in the proposal body.

Add a table immediately before the five figures:

| Evidence source | Query | Captured result | Reproducible URL |
| --- | --- | --- | --- |
| Google Search | `kidney` | About 211,000,000 results | https://www.google.com/search?q=kidney&hl=en&num=10&pws=0 |
| Google Video Search | `kidney` | About 66,000,000 results | https://www.google.com/search?tbm=vid&q=kidney&hl=en&num=10&pws=0 |
| Google Trends Web Search | `elephant,kidney` | Screenshot included | https://trends.google.com/trends/explore?date=all&q=elephant,kidney |
| Google Trends Image Search | `elephant,kidney` | Screenshot included | https://trends.google.com/trends/explore?date=all_2008&gprop=images&q=elephant,kidney |
| Google Books Ngram Viewer | `elephant,kidney` | Screenshot included | https://books.google.com/ngrams/graph?content=elephant%2Ckidney&year_start=1500&year_end=2019&corpus=en-2019&smoothing=3 |

Why this matters: Unicode asks for public, reproducible frequency evidence. The table makes the evidence auditable even if a screenshot is hard to read after PDF export.

### 2. Add Explicit Sort Location

Current v0.12.0 gives the suggested category, but the modern accepted proposals usually include a clear placement. Add:

Suggested category: People & Body, body-parts.

Suggested sort location: after `lungs` in the body-parts subgroup.

Rationale: kidney is an internal organ concept and should sit near `brain`, `anatomical heart`, and `lungs`. The Unicode emoji list places body-part emoji in this cluster:
https://www.unicode.org/emoji/charts/emoji-list.html

### 3. Remove The Emoji Name From Keywords

Unicode's current format says keywords should not repeat the name of the proposed emoji. v0.12.0 currently includes keyword phrases such as `kidney bean`, `kidney-shaped`, `kidney stone`, `kidney health`, and `kidney disease`. Those phrases are useful for the argument, but the keyword list should be cleaner.

Recommended keyword list:

`renal; organ; anatomy; body; urine; filtration; hydration; bean; bean-shaped; stone; health; nephrology; dialysis; transplant; donation; chronic disease; acute injury`

### 4. Make The Open-Ended Answer More Objective

Falling Debris succeeds partly because it uses a stable external category to show the proposal is not an invitation to add every weather-related event. Kidney needs the same style of boundary.

Replace the current open-ended answer with a criteria-based boundary:

Kidney is not proposed because it is one item in an unbounded organ list. It is proposed because it meets all of these independent criteria:

| Criterion | Kidney evidence |
| --- | --- |
| High public frequency | Google Search, Google Video, Trends, Image Trends, and Ngram evidence are included. |
| Broad ordinary-language use | Body part, kidney beans, kidney-shaped objects, hydration, filtration, stones, donation, transplant, and school science. |
| Global and durable concept | Kidney function, kidney disease, dialysis, transplantation, diabetes, hypertension, donation, and medication safety recur across countries and health systems. |
| Not clearly substitutable | Bean, drop, hospital, pill, syringe, heart, lungs, and brain all fail in different contexts. |
| Visually testable | Paired kidney shape, medial indentation, vessels, and ureters can be tested at 18x18. |

This is stronger than saying "we are not asking for every organ" because it gives reviewers a reusable boundary.

### 5. Convert The Visual Distinctiveness Section Into A Reviewer Decision Aid

Lime uses the wedge as a simple visual rule. Orca uses the black-and-white pattern. Trombone uses the slide. Kidney needs an equally simple rule.

Recommended addition:

Essential vendor cues:

| Cue | Required? | Reason |
| --- | --- | --- |
| Paired organ presentation | Strongly preferred | Avoids confusion with a single bean. |
| Medial indentation | Required | Core kidney silhouette. |
| Ureters or simple downward connectors | Strongly preferred | Signals urinary-system anatomy. |
| Red/brown organ color | Optional | Vendors may vary color; shape should carry meaning. |
| Fine vascular detail | Optional | Can be simplified at 18x18. |

Then include the current visual review board and one sentence saying the paired form is the submission's preferred paradigm.

### 6. Move Support Letters Further Out Of The Main Argument

The recovered letters are valuable for coalition credibility, but Unicode explicitly rejects petitions, hashtags, and anecdotal demand as frequency evidence. v0.12.0 already says this, but the support-letter list still takes a lot of visual weight near the end of the proposal.

For v0.13.0, keep a short paragraph in `Other Information`, then move the full letter list to a supplemental appendix or source index. The public PDF can still link to it, but the main proposal should feel evidence-led rather than advocacy-led.

### 7. Tighten The Public-Health Statistics

The WHO, Lancet, and CDC evidence is useful, but the most successful proposals do not let burden statistics replace the emoji case. Keep one global statistic and one sentence about durability; move the rest to source notes.

Recommended structure:

1. Everyday/body/food/shape/function uses.
2. Frequency table and screenshots.
3. Public-health durability in one compact paragraph.
4. Coalition/support letters as supplemental credibility only.

### 8. Add Concrete Message Examples

Treasure Chest and Fingerprint make sequence uses easy to imagine. Kidney's sequence paragraph is good but dense. Add a short table of ordinary messages:

| Message context | Possible emoji sequence |
| --- | --- |
| Hydration reminder | kidney + droplet |
| Kidney beans / chili | kidney + bowl or cooking pot |
| Anatomy class | kidney + book or microscope |
| Kidney stone warning | kidney + warning sign |
| Donation / transplant | kidney + person or hospital |
| Medication safety | kidney + pill |

The table should not request standardized sequences; it should only show compositional utility.

### 9. Make The First Page More Submission-Like

The source has "Top Of First Page" as an internal heading. The final PDF should remove that heading and render like a clean Unicode proposal:

Title: Proposal for Emoji: Kidney

Submitter: ...

Date: ...

Identification: ...

Images: ...

License: ...

This is a presentation issue, not a content blocker, but accepted proposals generally do not expose packet-construction wording in the public PDF.

### 10. Add Final PDF QA As A Gate

Before filing, do a final PDF-specific QA pass:

- Top-of-first-page fields are visible without scrolling.
- All four example images render at actual 18x18 and 72x72 sizes.
- All five frequency screenshots are readable.
- Google Search and Video screenshots show result counts with Tools visible.
- Raw evidence URLs are visible as text, not only embedded in screenshots.
- No GitHub source-control or packet-control language appears in the public PDF.
- The PDF is publicly accessible without login.
- The Unicode submission form receives the public PDF URL:
  https://forms.gle/6KSiYHrUdBkTMNaB8

## Proposed v0.13.0 Change List

1. Add the frequency summary table with exact captured counts and full URLs.
2. Add explicit sort location after `lungs`.
3. Clean the keyword list so it does not repeat `kidney`.
4. Replace the open-ended answer with the five-criterion boundary table.
5. Convert visual distinctiveness into an essential-cues table.
6. Convert sequence examples into a compact ordinary-message table.
7. Shorten public-health statistics and keep the broader everyday case first.
8. Move support-letter inventory to a supplemental appendix/source-index role.
9. Remove "Top Of First Page" construction wording from the public-facing source.
10. Add a PDF QA checklist and only then export/host the public PDF.

Expected readiness effect: v0.12.0 is about 81/100. Implementing these changes should move the content/readability portion into the high 80s or low 90s, leaving only external blockers: eligibility, duplicate-submission coordination, final signoff, public PDF hosting, and form submission.

## Filing Strategy Note

Do not file a second kidney proposal until the duplicate-submission/TKF issue is resolved. If another kidney proposal is pending or recently submitted, the stronger strategy is to coordinate, withdraw/merge where possible, and submit one unified public PDF with the best evidence and broadest coalition.

## Source URLs

Unicode current proposal guidelines:
https://www.unicode.org/emoji/proposals.html

Unicode accepted proposal chart:
https://unicode.org/emoji/charts/emoji-proposals.html

Falling Debris accepted proposal:
https://www.unicode.org/L2/L2024/24257-falling-debris-emoji.pdf

Treasure Chest accepted proposal:
https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf

Lime accepted proposal:
https://www.unicode.org/L2/L2023/23031-emoji-lime.pdf

Orca accepted proposal:
https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf

Fingerprint accepted proposal:
https://www.unicode.org/L2/L2023/23258-fingerprint-emoji.pdf

Trombone accepted proposal:
https://www.unicode.org/L2/L2024/24256-trombone-emoji.pdf

Kidney v0.12.0 packet:
https://github.com/ShuhanCS/medicalemoji/tree/master/submissions/v0.12.0

Kidney v0.12.0 proposal source:
https://github.com/ShuhanCS/medicalemoji/blob/master/submissions/v0.12.0/v0.12.0_kidney_emoji_proposal_SUBMIT.md
