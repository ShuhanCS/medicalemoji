# Unicode Accepted Emoji Proposal Manifest And Analysis

Date: 2026-05-13

## Source

Primary source:
https://unicode.org/emoji/charts/emoji-proposals.html

Current Unicode proposal guidelines:
https://www.unicode.org/emoji/proposals.html

Generated manifest:
`docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json`

The manifest contains `268` proposal rows from Unicode's accepted emoji proposal chart, with each row's L2 document ID, title, authors, Unicode document link, resolved L2 document/PDF URL, emoji count, and accepted emoji titles.

Important caveat: Unicode says the accepted-proposals chart is historical background, and many winning proposals predate the current submission format. For kidney and stomach, use the current 2026 guidelines as the controlling format, then use the accepted-proposal manifest to learn patterns.

## What Successful Proposals Tend To Do Well

### 1. They Make The Emoji A Broad Building Block

Strong accepted proposals usually frame the emoji as a broad reusable concept, not as a narrow campaign, one organization, or one clinical condition. For kidney, that means the organ should support anatomy, health, kidney beans, hydration, filtration, donation, transplant, stones, cooking/food language, and everyday body communication. For stomach, that means digestion, hunger, fullness, nausea, belly pain, reflux, eating, intuition, and metaphors such as "butterflies in the stomach."

Practical rule: the proposal should read like the emoji belongs in everyday language first, with medical use as one major use case rather than the only use case.

### 2. They Show The Concept Cannot Be Cleanly Replaced

Winning proposals do not just say "this is important." They explain why existing emoji and common sequences are insufficient. The replacement analysis is usually concrete: what users currently try, why it is ambiguous, and why the proposed emoji adds a distinct semantic unit.

For kidney, the key comparison is not only other organs. It is also bean, drop, hospital, pill, syringe, and generic medical symbols. For stomach, the comparisons are food, nauseated face, hospital, pill, anatomical organs, and generic belly/body language.

### 3. They Keep The Visual Paradigm Simple

Successful proposals treat the submitted image as a paradigm, not a demanded vendor artwork. They show that the idea is visually recognizable at small size and can survive vendor variation. The best submissions include or imply a simple silhouette test: if it fails at 18x18, the concept is in trouble even if the written argument is strong.

For medical anatomy proposals, this is a major risk. The document should include:

- 18x18 and 72x72 color images.
- 18x18 and 72x72 black-and-white images.
- A side-by-side comparison against likely confusable emoji.
- An explanation of what visual cues are essential and what details vendors may vary.

### 4. They Use Evidence, Not Advocacy

Unicode explicitly rejects petitions, hashtags, and anecdotal demand as frequency evidence. Accepted proposals that fit the modern standard are strongest when they include reproducible screenshots and cite durable usage sources.

For our packets, the hard requirement remains:

- Google Search screenshot.
- Google Video Search screenshot.
- Google Trends Web Search with `elephant`.
- Google Trends Image Search with `elephant`.
- Google Books Ngram Viewer with `elephant`.

Support letters are useful for credibility and coordination, but they are not a substitute for usage evidence.

### 5. They Address Exclusion Factors Before Reviewers Have To

Good proposals explicitly neutralize predictable objections:

- Already represented.
- Overly specific.
- Open-ended.
- Transient.
- Faulty comparison to existing emoji.
- Cause-only framing.
- Brand/IP/logos/text/exact image problems.

For kidney and stomach, the open-ended-organ objection is especially important. We should say plainly that the proposal is not a request for every organ; it is a request for this specific organ because of its independent broad usage, recognizability, and multiple concepts.

### 6. They Use Compatibility Only When It Is Real

Some historical accepted rows are compatibility-driven, but current proposals should not invent compatibility arguments. Compatibility is useful only if the exact or near-exact symbol is already widely used in a popular system and the proposal can cite evidence.

For kidney and stomach, compatibility should stay `not applicable` unless we find a documented high-use kidney/stomach pictograph in a major existing system.

### 7. They Are Complete On The First Page

Current Unicode format requires the top of the first page to carry the required administrative and image information. A strong PDF should not force reviewers to hunt for:

- Title.
- Submitters.
- Date.
- 18x18 and 72x72 images in color and black-and-white.
- Image rights/license statement.
- Keywords and category.

The kidney `v0.9.0` packet now does this better because the proposal source includes the image files and key links directly.

### 8. They Have Clean Scope Control

Accepted proposal history includes many multi-emoji and sequence documents, but new single-emoji proposals should stay tightly scoped. When a proposal tries to solve too many nearby concepts at once, it risks looking open-ended or category-building.

For kidney: do not make the case about all organs, all chronic disease, or all nephrology symbols.

For stomach: do not make the case about all GI organs, all digestive diseases, or all abdominal symptoms.

## Manifest Fields

Each JSON proposal entry includes:

- `document_id`: Unicode L2 document number.
- `document_year`: year inferred from the L2 document ID.
- `title`: proposal title from the Unicode chart.
- `authors`: authors from the Unicode chart.
- `document_url`: official Unicode `GetDocumentLink` URL.
- `resolved_document_url`: resolved Unicode L2 document/PDF URL.
- `emoji_count`: number of accepted emoji listed under that proposal row.
- `emoji_titles`: accepted emoji names/codepoint titles associated with the proposal row.

## Recent Successful Proposals To Read First

These recent accepted proposal documents are useful models because they are closer to the current review environment:

| Document | Title | URL |
| --- | --- | --- |
| L2/24-257 | Falling Debris Emoji | https://www.unicode.org/L2/L2024/24257-falling-debris-emoji.pdf |
| L2/24-256 | Proposal for Emoji: Trombone | https://www.unicode.org/L2/L2024/24256-trombone-emoji.pdf |
| L2/24-255 | Proposal for Emoji: Treasure Chest | https://www.unicode.org/L2/L2024/24255-treasure-chest-emoji.pdf |
| L2/24-254 | Fight Cloud Emoji Proposal | https://www.unicode.org/L2/L2024/24254-fight-cloud-emoji.pdf |
| L2/24-251 | Proposal for Emoji: Bigfoot | https://www.unicode.org/L2/L2024/24251-bigfoot-emoji.pdf |
| L2/24-249 | Proposal for Emoji: Orca | https://www.unicode.org/L2/L2024/24249-orca-emoji.pdf |
| L2/23-261 | Splash Emoji | https://www.unicode.org/L2/L2023/23261-splash-emoji.pdf |
| L2/23-260 | Proposal for Emoji Eye Bags Face | https://www.unicode.org/L2/L2023/23260-eye-bags-emoji.pdf |
| L2/23-259 | Proposal for Emoji: SHOVEL | https://www.unicode.org/L2/L2023/23259-shovel-emoji.pdf |
| L2/23-031 | Proposal for Emoji: Lime | https://www.unicode.org/L2/L2023/23031-emoji-lime.pdf |

## How This Should Change Kidney And Stomach

### Kidney

Current priority:

- Finish the three blocked required frequency screenshots.
- Keep the broader non-medical framing from `v0.8.0` and `v0.9.0`.
- Make the 18x18 visual test central, because kidney can be confused with bean-like forms.
- Keep support letters in an appendix role, not as primary evidence.
- Explicitly answer the open-ended-organ objection.

Current packet:
https://github.com/ShuhanCS/medicalemoji/tree/master/submissions/v0.9.0

### Stomach

Current priority:

- Confirm 2026 eligibility because the public submitted-date clock gives 2026-07-28, only three days before the 2026-07-31 intake deadline.
- Build usage evidence around the ordinary term `stomach`, not only GERD or gastroenterology.
- Include everyday metaphors and food/body contexts: hunger, fullness, nausea, gut feeling, butterflies in the stomach, and unable to stomach something.
- Create a visual test against other organ, food, and illness emoji.

Current project:
https://github.com/ShuhanCS/medicalemoji/tree/master/docs/proposals/stomach-emoji-2026

## Next Analysis Pass

The JSON manifest is broad enough for systematic analysis. Recommended next pass:

- Classify each accepted proposal by type: animal, food, object, face/emotion, body/person, symbol, sequence, compatibility, or administrative/data update.
- Flag proposals that are most relevant to medical anatomy or body-part proposals.
- Extract section structure from recent PDF proposals and compare them against kidney/stomach.
- Build a reviewer checklist from the top 20 closest analogs.
