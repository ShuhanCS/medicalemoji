# Kidney Submission Finalization Specification

Version: 3.1.0

Date: 2026-07-27

Status: Ready to execute

Supersedes: 3.0.0 (packet v2.1.2) and 2.0.0 (2026-07-26), which targeted the retired
`v1.12.0-kidney` line.

## Version history

3.1.0 retargets the spec from packet v2.1.2 to v2.2.0 after the CLDR-led case revision.

## What changed from 2.0.0

Version 2.0.0 described a proposal that no longer exists. It pointed at
`submissions/v1.12.0-kidney.7`, specified a paired-kidney artwork paradigm, mandated a ten-person
byline containing company names, and instructed the editor to keep neighbouring organs out of the
public Open-ended answer. All four are now wrong. It also cited the ESR priorities documents without
acting on what they say.

| Item | 2.0.0 | current |
| --- | --- | --- |
| Source of truth | `submissions/v1.12.0-kidney.7` | `submissions/v2.2.0` |
| Artwork paradigm | Paired bodies, medial notches, diagonal offset, short central attachment | Single kidney, medial hilum, short ureter cue |
| Byline | Ten authors including `(Microsoft)` and `(Microsoft for Startups)` | Eight authors, no company names |
| Open-ended | Do not catalog neighbouring organs publicly | Name Liver, Stomach, Pancreas, Spleen explicitly |
| Compatibility | `Not applicable` | Live CLDR keyword mismatch; see below |
| Sequences | Kidney + Rock, Kidney + Test Tube | Ordinary compositions; no invented named sequences |

## Mission

Finalize `submissions/v2.2.0` as one independent Emoji 19.0 proposal, close the remaining
eligibility, artwork-approval, publication, and form gates, and file it alone.

## The controlling strategic fact

ESR's stated intake priorities for Emoji 19.0 (L2/25-128, reconfirmed in L2/26-098) are:

1. Requiring empirical evidence of use, with citation
2. Emphasizing a need for compatibility with social apps, other standards, and/or operating systems
3. General focus on improving user experience with existing emoji

L2/26-098 states priorities "remain consistent with last year's ... with a focus on existing
customer problems centered on interoperability and improving criteria for inclusion." The Emoji 18.0
additions it discusses (pickle, monarch butterfly, meteor) were accepted to resolve interoperability
defects, not because the concepts were popular.

Kidney has a genuine claim on all three, and it is not the frequency argument. In CLDR English
annotation data, `kidney` is a keyword on exactly one emoji:

```
<annotation cp="🫘">beans | food | kidney | legume | small</annotation>
```

Source: https://github.com/unicode-org/cldr/blob/main/common/annotations/en.xml

That is U+1FAD8 BEANS, a Food & Drink pictograph, and it is the only character in the English
annotation set reachable by the term. Every operating-system picker and in-app emoji search that
consumes CLDR inherits this: a user searching for an organ is shown a legume. That is an existing
user-facing defect, which is the category ESR says it is prioritizing.

**Lead with this.** Frequency evidence is supporting context. The proposal must argue that Kidney
resolves a live mismatch in the standard, not merely that kidneys are important or commonly
discussed.

## Fixed inputs

- Byline, in this order: Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish
  Seethapathy; Jarone Lee; Danielle Miller; Timur Erk. **No company names.** The submission form
  rejects them and a named individual must submit.
- Shuhan He is the main point of contact.
- The five required frequency exhibits pass. Do not recapture them because prose or artwork changed.
- Artwork is the single-kidney paradigm. All four assets pass deterministic validation as one
  connected component each.
- Completeness is `Not applicable`.
- Compatibility is **not** `Not applicable`. See above.

## Required factor strategy

| Factor | Required treatment |
| --- | --- |
| Multiple meanings | Retain the cited `kidney-shaped` furniture, pool, and tray sense with its Books comparison. Do not inflate it into an unsupported metaphor. |
| Use in sequences | Ordinary compositions only. Do not request a standardized sequence or pad with invented combinations. |
| Breaks new ground | Lead with the CLDR keyword mismatch as a concrete, citable defect. Concede that Beans is searchable under `kidney` and explain why searchability is not representation. |
| Distinctiveness | Explain the single curved body, medial hilum, and short ureter cue. Support it with the 18x18 comparator board against Beans, Lungs, Anatomical heart, and Droplet rather than with assertion. |
| Expected usage | Lead with observed Beans substitution, citing third-party references. Interpret the five exhibits honestly including `kidney bean` contamination. Never argue from disease burden. |
| Completeness | Brief `Not applicable`. |
| Compatibility | State the CLDR routing problem and that downstream pickers inherit it. Do not request a specific annotation change; keyword assignment is a CLDR matter. |
| Already representable | Lead with Beans. Distinguish being reachable by a search term from representing the concept. |
| Overly specific | The common organ noun spanning several established uses. |
| Open-ended | Name Liver, Stomach, Pancreas, and Spleen as the neighbours this proposal declines to argue for. Concede that `stomach` and `liver` exceed `kidney` in recent English Books data. State the bounded rule. |
| Transient | Durable Books record plus current authoritative terminology. |
| Faulty comparison | Existing body-part emoji are visual comparators only and create no entitlement. |

## Prohibitions

- No advocacy, awareness, stigma, or campaign language.
- No disease-burden figures. WHO, Lancet, and CDC prevalence counts are not selection arguments.
- No petitions, hashtags, or social-media request counts.
- No support letters in the proposal body. They are retained in
  `submissions/v2.2.0/v2.2.0_support_letters_REFERENCE_ONLY.md`.
- No "heart and lungs were encoded, so kidney should be."
- No reference to Stomach, Liver, a co-submission, an organ set, or anatomy completion.
- No company names anywhere in the byline or form.
- Prose stays under 1,200 words.

## Work required

1. Archive the written Unicode/ESR record confirming eligibility for the 2026 intake beside the
   prior decline record. **This is the top blocker.** Kidney was declined 2019-12-17 and 2022-07-19,
   with a notice dated 2022-11-04. The four-year re-review bar clears on either 2026-07-19 or
   2026-11-04 depending on which date governs, and the deadline is 2026-07-31. Inquiry drafted at
   `docs/proposals/2026-eligibility-inquiry.md`. If no controlling answer arrives, stop before
   filing.
2. Resolve the artwork rights position. The retired lines disagreed: one attributed ownership to
   ConductScience Foundation with rights granted to the submitter, the other had the submitter
   warranting personal ownership under CC0. v2.2.0 asserts only originality and absence of
   third-party material. Choose one and state it.
3. Present the exact four assets to Shuhan He and record a dated `APPROVE` or `REVISE` tied to file
   hashes.
4. Raise the image count. Repository analysis notes encoded proposals tend to carry more than twenty
   images; v2.2.0 has ten. Add evidence captures, not padding.
5. Never mutate a committed packet. Prose or artwork changes create `submissions/v2.2.1/`.
6. Rebuild and inspect the PDF after any change. Confirm intact links, embedded fonts, readable
   evidence, correct pagination, and no `REFERENCE_ONLY` or internal-QA language.
7. Publish at a logged-out HTTPS URL and verify anonymous access and byte identity before the URL
   goes on the form.
8. File one Kidney form entry and archive the confirmation.

## Stop conditions

Do not publish or file if:

- the controlling written eligibility record is not archived;
- Shuhan has not approved the exact four assets;
- the byline contains a company name;
- a material claim is unsupported or an exhibit is unreadable;
- the proposal refers to another organ filing, a coordinated set, or anatomy completion;
- Beans is dismissed instead of answered;
- the Open-ended answer implies another organ must follow; or
- Shuhan has not authorized the external action.

## Completion report

Report the packet version, commit, exact PDF path and hash, eligibility record, byline, exact-art
approval result, factor changes, evidence disposition, verification performed, public raw HTTPS URL,
form reconciliation, filing confirmation, and any remaining blocker. Do not call the proposal
`READY TO SUBMIT` until the public URL, form, author records, eligibility record, and authorization
all agree.
