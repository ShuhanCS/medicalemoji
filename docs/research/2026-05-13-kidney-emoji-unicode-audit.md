# Kidney Emoji Unicode Audit - 2026-05-13

## Context

Email thread: `C:\Users\Shuha\Downloads\Re_ Question re_ previous kidney emoji initiative.eml`

Danielle Miller at ISN asked Edgar Lerma whether the previous kidney emoji team knew about a new Turkish Society of Nephrology kidney emoji effort. Edgar replied that the previous team was not aware and asked Danielle to connect the teams.

## Practical Answer

Reply with a coordinating posture, not a territorial one:

- The prior team was not aware of the Turkish Society effort.
- The previous kidney/kidneys submissions were declined, and current Unicode rules bar re-review of declined emoji for four years.
- The public Unicode status sheet lists `Kidney` as declined with date submitted `2019-12-17` and `KIDNEYS` as declined with date submitted `2022-07-19`.
- The public sheet does not expose the actual date of decline, so the 2026 eligibility date should be verified before anyone submits or resubmits.
- The current intake page says submissions are being accepted until `2026-07-31`, but the body text still contains stale 2025 dates. Treat the header as the active window and verify with Unicode/ESR if timing matters.
- The useful next step is a joint call/document exchange with the Turkish Society team so there is one aligned proposal and no duplicate or ineligible resubmission.

## Unicode Status Audit

Source status page:
https://www.unicode.org/emoji/emoji-proposals-status.html

Public status CSV export captured locally:
`sources/unicode_emoji_proposals_status_20260513.csv`

Raw CSV URL:
https://docs.google.com/spreadsheets/d/1yXZPw6jh5kYFmbDgIOK13UcRENwkOwYN4a9T3vyirO8/pub?gid=2110764947&single=true&output=csv

Relevant rows from the public status sheet:

| Emoji | Status | Date Submitted |
| --- | --- | --- |
| Heart (Organ) | Released as Emoji | 2019-04-23 |
| Lung (Organ) | Released as Emoji | 2019-04-23 |
| Kidney | Declined | 2019-12-17 |
| KIDNEYS | Declined | 2022-07-19 |
| Stomach | Declined | 2020-10-27 |
| Spine | Declined | 2020-10-27 |
| Intestines | Declined | 2020-12-18 |
| ECG | Declined | 2020-12-18 |
| White Blood Cell | Declined | 2020-12-18 |
| Pill Pack | Declined | 2020-12-18 |
| Blood Bag (B) | Declined | 2020-12-18 |
| Liver | Declined | 2020-12-18 |
| Stomach | Declined | 2022-07-28 |
| Liver | Declined | 2022-07-30 |
| Intestines | Declined | 2024-04-04 |
| Spine | Declined | 2024-04-05 |
| ECG | Declined | 2024-04-05 |

The current full emoji list includes `anatomical heart` and `lungs`, but a `kidney` search returned no match:
https://www.unicode.org/emoji/charts/full-emoji-list.html

## Current Unicode Submission Rules

Primary guidelines:
https://www.unicode.org/emoji/proposals.html

FAQ:
https://www.unicode.org/faq/emoji_submission.html

Proposal agreement/license:
https://www.unicode.org/emoji/emoji-proposal-agreement.pdf

Submission form:
https://forms.gle/6KSiYHrUdBkTMNaB8

Key current requirements:

- Declined emoji are not eligible for re-review/resubmission for four years.
- A submission is a proposal plus example images.
- Proposal document must be a publicly accessible PDF submitted through the Unicode Emoji Submission Form. Email, fax, or hard copies are not accepted.
- The agreement/license is mandatory. Submitters must warrant rights and grant broad non-exclusive, irrevocable, perpetual, worldwide, royalty-free rights.
- Current proposals must follow the current format, which Unicode says has changed substantially since earlier proposals.
- Proposal top matter must include title, submitter names, date, identification keywords/category, and color plus black-and-white example images.
- Images must appear at 18x18 and 72x72 pixels, in both color and black-and-white. Grayscale is not acceptable.
- Image IP/license provenance must be explicit, including public-domain or open-source URL if the submitter does not own all rights.
- One proposal should cover one emoji. The FAQ says omnibus/multiple-emoji proposals are no longer accepted.
- Required frequency evidence includes reproducible screenshots from Google Search, Google Video Search, Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer.
- Trends and Ngram evidence must include `elephant` as the comparison term.
- Petitions, social media hashtags, anecdotal evidence, and examples of people asking for the emoji are not acceptable frequency evidence.
- A proposal should not rely on a cause argument, even if the cause is worthwhile.
- Inclusion factors include multiple meanings, use in sequences, breaking new ground, visual distinctiveness at emoji size, high usage level, completeness of a set, and compatibility.
- Exclusion factors include already representable, overly specific, open-ended, transient, and faulty comparison to existing emoji.

## Existing Medical Emoji Assets

The repo already has kidney campaign support materials:

- `public/documents/21-12-17-Letter-to-the-Unicode-Consortium-about-the-Kidney-Emoji-3.pdf` - ASN support letter.
- `public/documents/AAKP-Kidney-Emoji-Letter-1.7.22.pdf` - AAKP support letter.
- `public/documents/Kidney_Emoji_Letter-1.pdf` - Canadian Society of Nephrology support letter.
- `public/documents/Kidney-Foundation-of-WNY-kidney-emoji-letter.pdf` - Kidney Foundation of Western New York support letter.
- `public/documents/NephJC_KidneyEmoji.pdf` - NephJC support letter.
- `public/documents/The-Unicode-Consortium_Signed.pdf` - KDIGO support letter.
- `src/data/emoji.ts` lists existing supporters including AAKP, ASN, ASDIN, CSN, Glomerular Disease Consortium, ISN, KDIGO, NKF, NephJC, RPA, Kidney Foundation of Western New York, and Women Nephrology India.

These letters are useful coalition evidence, but they do not substitute for Unicode's required frequency evidence.

## Risk Assessment

Main risk: the Turkish Society proposal may be interpreted as a resubmission of a declined `Kidney/KIDNEYS` concept inside the four-year bar. The public sheet only shows date submitted, not date declined, so the safest answer is to coordinate and verify eligibility rather than promise that a July 2026 resubmission is available.

Substantive proposal risk: Unicode now emphasizes objective, high expected usage and broad scope. A kidney proposal that leans mainly on disease burden, society support, petitions, or awareness will likely be weak under current rules. A stronger proposal needs reproducible search/trends/ngram data, careful visual-distinctiveness evidence at 18x18, and an argument that kidney is broad and iconic rather than one organ in an open-ended anatomy set.

## Recommended Email Reply

Subject: Re: Question re: previous kidney emoji initiative

Hi Danielle, Edgar, and everyone,

Thanks for looping me in. We were not aware that the Turkish Society of Nephrology was preparing a kidney emoji submission this year, so yes, it would be very helpful to be connected with them.

The main thing I would flag is timing/process. Unicode's public status sheet lists both prior kidney-related submissions as declined: `Kidney`, submitted December 17, 2019, and `KIDNEYS`, submitted July 19, 2022. Current Unicode guidance says declined emoji are not eligible for re-review/resubmission for four years. The public sheet does not show the actual decline date, so before anyone moves forward we should verify whether a 2026 submission would be eligible and make sure we are not creating duplicate or conflicting submissions.

The process also appears to have tightened since our earlier effort. Unicode now requires a public PDF submitted through their form, current-format proposal sections, open-license image rights, 18x18 and 72x72 color and black-and-white images, and reproducible usage evidence from Google Search, Video Search, Trends, Image Trends, and Books Ngram. Petitions, hashtags, social media asks, and support letters are helpful for coalition-building but do not count as the required frequency evidence.

I would be glad to share our prior materials, support letters, and lessons learned, and I think the best next step is for us to compare notes with the Turkish Society team and coordinate a single aligned strategy. If they have already drafted or submitted something, it would be useful to see the proposal, date submitted, and any response from Unicode/ESR.

Best,
Shuhan

## Next Steps

1. Ask Danielle to introduce the Turkish Society lead immediately.
2. Request their proposal PDF or draft, submission date, intended emoji name (`kidney` vs `kidneys`), image/license source, and any Unicode correspondence.
3. Confirm whether the four-year clock is calculated from submission date, decline date, annual status update, or ESR notification.
4. If eligible, rebuild the proposal in current Unicode format and replace petition/support-letter emphasis with reproducible frequency evidence.
5. Keep ISN and existing society supporters aligned behind one submission.
