# TEMPLATE: Proposal for Emoji: {{EMOJI_NAME}}

Fill every `{{PLACEHOLDER}}`. Delete every `> guidance` block before export. Export to PDF, host it
publicly, and submit the link through <https://forms.gle/6KSiYHrUdBkTMNaB8>.

Controlled by the current
[`best-in-class specification`](emoji-proposal-approval-rubric.md) and Unicode's current guidelines:
https://www.unicode.org/emoji/proposals.html

Before filling this template, pass the concept and image gates in the root
[`Medical Emoji Proposal Guide`](../../PROPOSAL-GUIDE.md).

The archived 55-versus-29 comparison has been retired because the 29-document cohort and analysis code were
not preserved. There is no validated winning word, page, or image-count threshold. Write only the prose
needed to make a complete, reproducible case.

---

## Title: Proposal for Emoji: {{EMOJI_NAME}}

**Submitter:** {{FULL NAME}}, {{CREDENTIALS}} ({{AFFILIATION}}), point of contact: {{EMAIL}}
{{; ADDITIONAL AUTHORS, semicolon separated}}

**Date:** {{YYYY-MM-DD}}

> The submission form's Submitter field states: *"The name must be of an individual. Names of organizations
> or companies will not be considered."* Name a person. Affiliations belong in parentheses.
> Update the date on every revision.

---

## 1. Identification

**CLDR short name:** {{lowercase name, e.g. `kidney`}}

**CLDR keywords:** {{keyword}}; {{keyword}}; {{keyword}}; {{keyword}}

> *"Do not repeat the name of the emoji. Consider terms that people would use to find this emoji."*
>
> Examples: orca -> `killer whale`. Lung -> `breath, inhalation, exhalation, respiration`.
> Heart -> `heartbeat, pulse, center`. Our declined kidney used `Kidney`, which only repeated the name.
>
> Fingerprint (`L2/23-258`, encoded) filed sixteen: `biometric; crime; crime scene; criminal; dactylogram;
> dactyloscopy; dermatoglyphics; finger; fingerprint; identification; identity; latent; minutia; phalange;
> phalanx; ridge.` Be generous and specific.

**Category:** {{group}} {{subgroup}}

> Format matches Emoji Ordering, e.g. `Objects medical` or `Animals & Nature animal-marine`. Category is a
> current required field. A separate sort-location field is not required by the 2026 format.

**Optional suggested sort location:** after {{EXISTING EMOJI}}

---

## 2. Images

|  | 18×18 | 72×72 |
|---|---|---|
| **Colour** | {{image}} | {{image}} |
| **Black and white** | {{image}} | {{image}} |

> Colour and black and white are both required. **Grayscale is not acceptable.** The 18×18 render exists to
> prove the emoji survives at keyboard size. Put it first, at actual size, and do not let the reviewer
> squint.
>
> **The image must contain no text, no digits, no barcodes and no letters.** *"Includes text: We no longer
> encode emoji that include text."* That is an automatic decline.

**License:** {{ONE OF:}}

- *"I certify that I am the creator of this image and have appropriate licenses for use by the UTC."*
  (Treasure Chest, `L2/24-255`, encoded)
- *"Artwork by {{ARTIST}}, created as a work for hire or assigned to {{RIGHTS OWNER}}. I certify that the
  Submitter owns all IP Rights in these images."*
- *"{{SOURCE}} ({{CC-BY-SA / CC0 / public domain}}), {{URL where the licence is clearly stated}}"*
  (Orca, `L2/24-249`, encoded)

> Omitting the rights information is an automatic rejection. A historical credit-only line is not a safe
> current model. The requirement holds *"even if the image(s) has been developed by the Submitter with the
> assistance of AI tools."* Separately, the form grants an irrevocable, perpetual, worldwide, royalty-free
> licence. Clear ownership before commissioning art.

---

## 3. Factors for inclusion

> The nearest existing emoji belongs in Breaks new ground and Already representable. `elephant` is the
> required frequency comparator; it is not a substitute for identifying the strongest semantic alternative.

> Answer all seven, in this order. **Write `N/A` where honest.** The guidelines say plainly:
> *"Mark this as n/a unless there are compelling examples."*

**a. Multiple meanings.** {{METAPHORS AND SYMBOLISM, or `N/A`}}

> Puns do not count. Treasure Chest earned this one with everyday specificity: *"finding an earring under a
> car seat or a keepsake in your grandma's attic."* If you cannot do that, write `N/A`.

**b. Use in sequences.** {{SEQUENCES, or `N/A`}}

> Orca: *"The character is a singular emoji, can be used by itself and does not need any modifiers."*

**c. Breaks new ground.** {{Yes/No}}. {{WHY}}

> Answer Yes or No, then justify. The killer test is Unicode's own: *"because there is already an emoji for
> 🧹 broom, an emoji for vacuum cleaner would not break new ground."* Name the nearest existing emoji and
> say precisely what it cannot express.
>
> **Project decision rule:** a normal filing candidate must answer `Yes`. This means a new semantic building
> block, not a novel or obscure underlying subject. If the honest answer is `No`, stop unless a genuine,
> high-frequency compatibility need in a popular existing system has been documented and escalated.
>
> Orca: *"the orca is a new animal species that cannot be represented by any sequence of currently existing
> emojis."*

**d. Distinctiveness.** {{WHY IT READS AT 18×18}}

> Argue from the 18×18 render, not the 72×72. Treasure Chest: *"Even at a small resolution it is still
> distinguishable from a standard box or package."*
>
> Apple's accessibility set explained why each glyph had to be drawn as it was: *"the image of a hearing aid
> would not be sufficiently distinctive at emoji scale; it needs to be shown with an ear in order to
> establish its identity."* Show that you tested the failure mode.

**e. Usage level.** {{ONE PARAGRAPH INTERPRETING THE EVIDENCE IN SECTION 7}}

> Numbers live in the screenshots. This paragraph tells the reader what they mean.
> **Concede the weakness here.** Orca did: *"Google Trends shows that the popularity worldwide of the orca
> is less than that of the elephant."* Then it won a narrower comparison. A reviewer who catches you hiding
> a weakness stops believing your strengths.

**f. Completeness.** {{`N/A` unless the emoji closes a genuinely FIXED set}}

> Completeness means closed sets: the zodiac, blood types, the four card suits. Organs are not a closed set.
> **Writing anything but `N/A` here invites the Open-ended rejection.**

**g. Compatibility.** {{`N/A` unless it exists on Snapchat, X or QQ with evidence}}

---

## 4. Counterarguments to factors for exclusion

> Answer every current exclusion factor by name. This is a current Unicode requirement, not a historical
> success correlation.

**a. Already representable.** {{NO, BECAUSE...}}

> Name the sequence a reviewer would propose, and kill it. Fingerprint (`L2/23-258`, encoded): *"One might
> argue that FINGERPRINT could be represented by 'index pointing up' (U+261D), but this character shows an
> entire hand and does not show friction ridge structure. It is a different emoji entirely."*

**b. Overly specific.** {{WHY IT IS A CATEGORY, NOT A SUBTYPE}}

> The test is 🍣 sushi: the emoji stands for sushi in general; maguro would be overly specific.

**c. Open-ended.** {{WHAT YOU WILL NOT COME BACK FOR}}

> **Draft this answer before you write anything else. If it cannot be written honestly, the proposal is not
> ready.**
>
> Treasure Chest, in seven words: *"No, this is not part of a set."*
> Apple: *"we don't expect such discussion to lead to proposals for a large number of additions beyond the
> current proposal."*
>
> Name the strongest neighboring concepts a reviewer may raise and explain why this concept independently
> merits consideration. Do not promise that no other organ will ever be proposed. Unicode requires one emoji
> per proposal but does not forbid three separate organ proposals in the same cycle.

**d. Transient.** {{WHY IT IS NOT A FAD}}

> Treasure Chest: *"Treasure is a concept that has existed for thousands of years across many cultures…a
> literary trope since the early 1800s."* This is what the Books Ngram long baseline is for.

**e. Faulty comparison.** {{THIS EMOJI DOES NOT DEPEND ON ANALOGY}}

> *"An existing emoji's existence does not justify proposals for emoji like them."*
>
> **Never write "the heart and lungs were encoded, so the kidney should be."** That is the textbook faulty
> comparison and it is how a medical-importance argument tends to be phrased. Earlier encodings are context,
> never justification.

---

## 5. Other information

{{DESIGN GUIDANCE FOR VENDORS}}

> Treasure Chest used this to steer the artwork: *"the contents of the treasure chest can be varied but for
> the sake of simplicity it is recommended that only gold coins be used. At small resolutions, other
> contents may become muddled."* You are advising the people who will draw it.

---

## 6. Evidence of frequency

> *"Please read this section and follow all the instructions; otherwise your proposal will likely be
> rejected."* All five sources. Each a **screenshot**. `elephant` in the Trends and Ngram screenshots.
>
> Include the elephant comparator because the current instructions require it, not because a historical
> percentage predicts approval.

| Source | Screenshot | Notes |
|---|---|---|
| Google Search | {{screenshot}} | Click **Tools**; the result count appears far right |
| Google Video Search | {{screenshot}} | `tbm=vid` |
| Google Trends: Web | {{screenshot}} | `date=all`, **must include `elephant`** |
| Google Trends: Image | {{screenshot}} | `gprop=images`, **must include `elephant`** |
| Google Books Ngram | {{screenshot}} | 1500–2019, `corpus=en-2019`, `smoothing=3`, **must include `elephant`** |

**Capture statement:** *"All data are from {{MONTH YEAR}}; each data item was obtained using a new private
browser window."*

> Copied from Apple's `L2/18-080`. Our packets never stated a capture method, and
> `previous-proposal-review.md` lists that as a top failure.

**Search craft:**

- **Hyphenate multiword terms.** `[blood-bag]`, not `[blood bag]`. *"Otherwise the search data you supply
  will likely be rejected."*
- **Search the proposed concept, not calls for an emoji.** Explain disambiguation or category terms when a
  query has unrelated meanings. Do not use `[kidney emoji]` as frequency evidence for `[kidney]`.
- **Use a qualifying category in Trends, and say so in one sentence.** Orca: *"it has been selected as
  'animal' instead of 'search term' to get correct results regardless of naming or language."*
- **Add another language when the concept is stronger elsewhere.** This is conditional, not a requirement
  for every proposal.
- **Optional:** Add a reproducible supplemental source only when it proves something the five required
  sources do not.

**Do not use as frequency evidence or as the reason for encoding:**

- Petitions, `change.org`, hashtags, or social-media calls requesting the emoji. *"Petitions or 'frequent
  requests' play no role in emoji encoding approval, and are not acceptable as evidence for citation."*
  Follow the current rule even when an old accepted proposal did otherwise. An illustrative mockup of ordinary
  use is different from presenting calls for the emoji as frequency evidence.
- A `Frequently Requested` section. It was in Unicode's 2020 template. It is now disallowed evidence.
- **A cause as the selection justification.** *"Please do not justify the addition of an emoji because it
  furthers a 'cause,' no matter how worthwhile. A proposal may be advanced despite a 'cause' argument, but
  will not be advanced because of it."* Cause-related meanings may be described when they are established and
  cited, but the proposal must still win on independent communicative use and the selection factors. Monarch
  Butterfly is the accepted counterexample that makes this distinction important:
  https://www.unicode.org/L2/L2025/25254-emoji-butterfly.pdf

---

## Pre-flight

- [ ] Open-ended answer drafted first, explaining why this concept stands independently
- [ ] No unnecessary prose; every material claim has a readable screenshot or citation
- [ ] `N/A` written wherever honest, especially Completeness and Compatibility
- [ ] Keywords contain no form of the emoji's name
- [ ] Artwork contains no text, digits or barcodes; 18×18 and 72×72; colour and black and white; not grayscale
- [ ] Both 18x18 assets passed the project unprompted-recognition gate against declared confusers
- [ ] Licence sentence present and true
- [ ] All five sources screenshotted; `elephant` in Trends and Ngram
- [ ] Capture statement with month, year and private-window method
- [ ] No petitions or social-media calls used as evidence; no cause used as the reason for encoding
- [ ] One emoji per proposal; parallel proposals each make an independent Open-ended case
- [ ] Confirm the concept was not declined in the last four years
- [ ] PDF hosted publicly; link submitted through the form
