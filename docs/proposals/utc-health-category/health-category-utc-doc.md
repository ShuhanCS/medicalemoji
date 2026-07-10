---
title: "Health as a Category in Emoji Ordering"
author-meta: "David Rhew, MD; Shuhan He, MD"
date-meta: "2026-07-21"
subject: "Proposed reorganization of Emoji Ordering to establish a top-level Health group"
geometry: margin=1in
fontsize: 11pt
mainfont: "Georgia"
mainfontoptions: "Numbers=Lining"
monofont: "Consolas"
colorlinks: true
linkcolor: black
urlcolor: black
numbersections: true
---

```
Title:   Health as a Category in Emoji Ordering
Authors: David Rhew, MD (Microsoft), point of contact;
         Shuhan He, MD (Massachusetts General Hospital)
Date:    2026-07-21
Action:  For consideration by the UTC, and for referral to the
         Emoji Standard and Research Working Group
```

# Abstract

Microsoft would like to see a top-level Health group established in Emoji Ordering. This document proposes
no new emoji. It concerns only the grouping of emoji that are already encoded.
Health related emoji are presently distributed across seven of the ten top-level groups in Emoji
Ordering, and the `medical` subgroup holds seven of approximately thirty-seven of them. The anatomical
heart (`U+1FAC0`) and lungs (`U+1FAC1`), encoded in Emoji 13.0 for medical use, are classified under
`People & Body > body-parts`. We ask the UTC to establish a top-level Health group, to populate it with
the existing `medical` subgroup and a new `body-organ` subgroup, and to assign future health related
emoji to it by default. Precedent exists. The top-level group list changed from eight groups to ten in
Emoji 12.0.

# Request

We request that the UTC direct the ESR Working Group and the CLDR TC to:

1. Establish a top-level group named Health in Emoji Ordering.
2. Move the existing `medical` subgroup into it, intact and unchanged.
3. Create a `body-organ` subgroup within it, containing `U+1F9E0` brain, `U+1FAC0` anatomical heart, and
   `U+1FAC1` lungs.
4. Assign future health related emoji to the Health group by default.

No character is added, removed, renamed, or re-encoded by this request.

**Fallback request.** If the UTC declines to create a top-level group at this time, we ask that it
(a) formally designate `Objects > medical` as the default destination for future health related emoji,
and (b) direct the ESR Working Group to report on health emoji organization at a subsequent meeting.

# Background

Emoji Ordering assigns every emoji to one of ten top-level groups and to a subgroup within it. Unicode
Technical Standard #51 (UTS #51), section 5, *Ordering and Grouping*, states that "Emoji Ordering shows
an ordering for emoji characters that groups them together in a more natural fashion" and that "this data
has been incorporated into CLDR." UTS #51 does not itself enumerate the groups.

The taxonomy is authored in `emojiOrdering.txt` in the `unicode-org/unicodetools` repository, where the
ten top-level groups appear as `@@` lines and the subgroups as `@` lines. `Objects` appears at line 605
and `medical` at line 640 of that file, as retrieved on 2026-07-09 from
<https://raw.githubusercontent.com/unicode-org/unicodetools/main/unicodetools/src/main/resources/org/unicode/tools/emoji/emojiOrdering.txt>.
That file is generated into `emoji-test.txt`, and the resulting ordering is incorporated into CLDR.

Grouping governs presentation. It determines the sections of an emoji keyboard palette and the layout of
the published emoji charts. It does not affect code points, character names, or character properties.
The header of `emoji-test.txt` states that "the groups and subgroups are illustrative" and that CLDR
order "is recommended (but not required!) for keyboard palettes."

We note this plainly, because it bears on the cost of the change we request. The grouping carries no
conformance requirement and no stability guarantee. The Unicode stability policies enumerate encoding,
name, alias, normalization, identity, and property stability. None of them covers emoji group membership.
The change we request is therefore inexpensive to make and imposes no conformance burden on any
implementation.

# Referral

We ask that this document be referred to the Emoji Standard and Research Working Group, which maintains
the emoji ordering data, and that the working group be invited to report a recommendation to the UTC.
We do not ask the UTC to decide the matter on the strength of this document alone.

# Findings

All counts below were computed on 2026-07-09 from `emoji-test.txt` for Emoji 17.0 (file dated
2025-08-04), retrieved from <https://unicode.org/Public/emoji/latest/emoji-test.txt>, counting entries
marked `fully-qualified`. The script that produces every table in this document is described in
Appendix C.

## There is no Health group

| Group | Fully-qualified emoji |
|:---|---:|
| Smileys & Emotion | 171 |
| People & Body | 2,418 |
| Component | 0 |
| Animals & Nature | 160 |
| Food & Drink | 131 |
| Travel & Places | 219 |
| Activities | 85 |
| Objects | 266 |
| Symbols | 224 |
| Flags | 270 |
| **Total** | **3,944** |

The group `Component` is a top-level group containing zero fully-qualified emoji.

## The medical subgroup holds seven emoji

`medical` is one of eighteen subgroups of `Objects`. Its members are:

| Code point | Name | Emoji version |
|:---|:---|:---|
| `U+1F489` | syringe | E0.6 |
| `U+1F48A` | pill | E0.6 |
| `U+1FA78` | drop of blood | E12.0 |
| `U+1FA79` | adhesive bandage | E12.0 |
| `U+1FA7A` | stethoscope | E12.0 |
| `U+1FA7B` | x-ray | E14.0 |
| `U+1FA7C` | crutch | E14.0 |

Ranked against the other subgroups of `Objects`, `medical` is third smallest:

| Subgroup | Count | Subgroup | Count |
|:---|---:|:---|---:|
| clothing | 47 | sound | 9 |
| tool | 27 | music | 9 |
| household | 25 | other-object | 9 |
| office | 23 | writing | 7 |
| book-paper | 17 | science | 7 |
| light & video | 16 | **medical** | **7** |
| computer | 14 | phone | 6 |
| musical-instrument | 13 | lock | 6 |
| mail | 13 | | |
| money | 11 | | |

Medicine is allotted the same space as `writing`, less than `musical-instrument`, and roughly a seventh
of `clothing`.

## Health emoji are distributed across seven of the ten groups

Approximately thirty-seven encoded emoji denote health, illness, care, or clinical objects. They occupy
fourteen subgroups across seven groups. The `medical` subgroup accounts for seven of them.

| Group and subgroup | Members |
|:---|:---|
| Objects > medical | syringe, pill, drop of blood, adhesive bandage, stethoscope, x-ray, crutch |
| People & Body > body-parts | brain, anatomical heart, lungs, tooth, mechanical arm, mechanical leg, ear with hearing aid |
| Smileys & Emotion > face-unwell | face with medical mask, face with thermometer, face with head-bandage, nauseated face, face vomiting, sneezing face, woozy face |
| People & Body > person-activity | person with white cane, person in motorized wheelchair, person in manual wheelchair |
| Objects > science | test tube, petri dish, dna |
| People & Body > person-role | health worker, pregnant person |
| Animals & Nature > animal-mammal | guide dog, service dog |
| Animals & Nature > animal-bug | microbe |
| People & Body > person-gesture | deaf person |
| Symbols > other-symbol | medical symbol |
| Symbols > transport-sign | wheelchair symbol |
| Travel & Places > place-building | hospital |
| Travel & Places > transport-ground | ambulance |
| Smileys & Emotion > face-negative | skull and crossbones |

The anatomical heart (`U+1FAC0`) and lungs (`U+1FAC1`) were encoded in Emoji 13.0 following proposals made
on medical grounds, L2/19-150 and L2/19-149. Both are classified under `People & Body > body-parts`,
alongside the mechanical arm and the ear. Neither appears in the `medical` subgroup.

That classification was assigned in the Emoji Subcommittee's recommendation document, L2/19-190R, which
lists each character against its proposal number and its group:

```
U+1FAC0 HEART    L2/19-150   heartbeat | pulse | center | organ                People_and_Body body-parts
U+1FAC1 LUNGS    L2/19-149   breath | inhalation | exhalation | respiration    People_and_Body body-parts
```

The subgroup `medical` already existed when that recommendation was made. In Emoji 12.0, published earlier
that year, it held the syringe, the pill, the drop of blood, the adhesive bandage and the stethoscope. Two
characters proposed as medical emoji were nonetheless placed among body parts.

A user looking for health emoji must therefore search a minimum of seven palette sections.

## The top-level group list has been revised before

The set of top-level groups is not fixed. It changed in Emoji 12.0.

| Release | Top-level groups | Count |
|:---|:---|---:|
| Emoji 5.0 (2017) | Smileys & People; Animals & Nature; Food & Drink; Travel & Places; Activities; Objects; Symbols; Flags | 8 |
| Emoji 11.0 (2018) | identical to Emoji 5.0 | 8 |
| Emoji 12.0 (2019) | Smileys & Emotion; People & Body; Component; Animals & Nature; Food & Drink; Travel & Places; Activities; Objects; Symbols; Flags | 10 |
| Emoji 17.0 (2025) | identical to Emoji 12.0 | 10 |

Sources are listed in Appendix B, each retrieved 2026-07-09.

In Emoji 12.0 the group `Smileys & People` was divided into two top-level groups, and the group
`Component` was added. The reorganization proposed here is smaller in scope than the change made then.

## Salience

The strongest available measurement of how often people raise health in a text interface comes from a
study of consumer conversational artificial intelligence (AI) usage:

> Costa-Gomes B, Tolmachev P, Taysom E, Sounderajah V, Richardson H, Schoenegger P, Liu X, Nour MM,
> Spielman S, Way SF, Shah Y, Bhaskar M, Nori H, Kelly C, Hames P, Gross B, Suleyman M, King D.
> *Public use of a generalist LLM chatbot for health queries.* Nature Health, 2026.
> doi:10.1038/s44360-026-00117-x

The study analyzed "over 500,000 de-identified health-related conversations with Microsoft Copilot from
January 2026." Its findings include:

* "nearly one in five conversations involve users describing their own symptoms, interpreting their own
  test results, or managing their own conditions"
* "across both condition information and symptom questions, one in seven conversations are on behalf of
  someone else, whether a child, an aging parent, or a partner"
* "The largest category, 'Health Information & Education,' accounts for over 40% of conversations."

Earlier work by the same group found that "health-related queries on consumer Microsoft Copilot were the
most prevalent topic category on mobile."

The authors state four limitations, which we reproduce so that the committee may weigh them. The analysis
covers a single platform. It covers a single month, January 2026, a month associated with health
resolutions. It observes queries and not outcomes. The sample is global, with approximately 22 percent of
conversations originating in the United States and approximately 45 percent in English.

We offer this as evidence of salience, which is the property a top-level group encodes. We do not offer
it as evidence of expected usage frequency for any individual character, and this document requests no
character.

# Proposed structure

The proposal is deliberately narrow. Each emoji that moves imposes a relearning cost on users, so we ask
for the smallest change that resolves the finding in section 4.3.

## Emoji that move

| Destination | Current location | Members |
|:---|:---|:---|
| `Health > medical` | `Objects > medical` | All seven, intact: `U+1F489`, `U+1F48A`, `U+1FA78`, `U+1FA79`, `U+1FA7A`, `U+1FA7B`, `U+1FA7C` |
| `Health > body-organ` | `People & Body > body-parts` | `U+1F9E0` brain, `U+1FAC0` anatomical heart, `U+1FAC1` lungs |

The Health group would contain ten emoji. That exceeds the membership of four existing subgroups of
`Objects` and of the top-level group `Component`.

## Emoji that do not move

We propose no change for the following, and we state this explicitly so that the scope of the request is
unambiguous.

| Emoji | Current location | Rationale for leaving them |
|:---|:---|:---|
| The seven unwell faces | Smileys & Emotion > face-unwell | They are faces, and users locate them among faces |
| tooth, mechanical arm, mechanical leg, ear with hearing aid | People & Body > body-parts | External body parts and worn devices |
| health worker, pregnant person, deaf person, the three wheelchair and cane personas | People & Body | They depict people |
| hospital, ambulance | Travel & Places | A building and a vehicle |
| medical symbol, wheelchair symbol | Symbols | Signage and symbols |
| microbe, test tube, petri dish, dna | Animals & Nature; Objects > science | Biology and laboratory science rather than care |

## Default assignment of future emoji

We ask that health related emoji encoded in future releases be assigned to the Health group by default.
Had such a rule existed in 2020, the anatomical heart and lungs would have been classified with the other
clinical emoji rather than with external body parts.

# Stability analysis

Grouping is presentation. The following table separates what this request affects from what it does not.

| Unaffected | Affected |
|:---|:---|
| Code points | CLDR emoji ordering data |
| Character names | Group and subgroup comments in `emoji-test.txt` |
| Character properties, including `Emoji` and `Emoji_Presentation` | Section headings in keyboard palettes |
| Encoding stability guarantees | The published emoji chart pages |
| Existing sequences and zero-width joiner behavior | Implementations that hard-code group names |

No code point is affected. The Unicode stability policies govern code points and character names, and
neither changes here. The Emoji 12.0 precedent establishes that group membership is revisable.

There is a genuine cost. Users who have learned to find the pill under `Objects` would find it under
Health. This is a one-time relearning of the same kind imposed by the Emoji 12.0 split, which was
absorbed without reported incident.

# Anticipated objections

**This is an emoji proposal in disguise.** It requests no character. Any future character proposal will
be filed through the Unicode Emoji Submission Form, as the guidelines require.

**Categories are stable.** They are not protected as such. The header of `emoji-test.txt` states that
"the groups and subgroups are illustrative." The Unicode stability policies do not enumerate emoji group
membership. And the top-level group list changed in Emoji 12.0, from eight groups to ten. See section 4.4
and Appendix B.

**The groups are illustrative, so the question does not matter.** The groups determine the section
headings of the emoji keyboard palettes shipped by every major vendor, which is where most users meet
emoji. Section 4.3 shows that a user seeking health emoji must search at least seven of those sections.
The label "illustrative" describes the conformance status of the data, and it does not describe the
experience of the people using it.

**Health is a cause, and the guidelines discount cause arguments.** The emoji proposal guidelines
discount cause arguments as justification for encoding a character. This document requests no character.
Its claims concern the coherence and the measured salience of an existing set of characters.

**Ten emoji do not warrant a top-level group.** The top-level group `Component` contains zero
fully-qualified emoji. Four subgroups of `Objects` contain fewer than ten.

**Where does reorganization end.** The request is bounded by section 5.2, which enumerates what does not
move, and by section 5.1, which defines the group as the existing `medical` subgroup plus internal
organs. We do not intend to seek further reorganization.

**Ordering data belongs to CLDR.** In part it does. The taxonomy is authored in `emojiOrdering.txt` in
`unicode-org/unicodetools`, generated into `emoji-test.txt`, and then incorporated into CLDR. CLDR
consumes the grouping rather than defining it. We therefore address this document to the UTC, for
referral to the Emoji Standard and Research Working Group, and we are prepared to file corresponding
issues against the ordering source and the CLDR artifacts at the working group's direction.

# Appendix A: Census of health related emoji

The complete listing, with group and subgroup for each entry, is generated by the script described in
Appendix C. Its output accompanies this document as `census-2026-07-09.txt`.

# Appendix B: Sources for the top-level group lists

Each retrieved 2026-07-09.

| Release | Source |
|:---|:---|
| Emoji 5.0 | <https://unicode.org/Public/emoji/5.0/emoji-test.txt> |
| Emoji 11.0 | <https://unicode.org/Public/emoji/11.0/emoji-test.txt> |
| Emoji 12.0 | <https://unicode.org/Public/emoji/12.0/emoji-test.txt> |
| Emoji 13.0 | <https://unicode.org/Public/emoji/13.0/emoji-test.txt> |
| Emoji 17.0 | <https://unicode.org/Public/emoji/latest/emoji-test.txt> |

# Appendix C: Method

Counts were produced by parsing `emoji-test.txt` and counting lines marked `fully-qualified`, attributing
each to the most recent `# group:` and `# subgroup:` comment above it. The script is published at
<https://github.com/ShuhanCS/medicalemoji/blob/main/evidence/emoji_group_census.py> and its output at
<https://github.com/ShuhanCS/medicalemoji/blob/main/evidence/census-2026-07-09.txt>. Any reader can
reproduce every count in this document by retrieving the same data file and running the script.
