# 2026 Organ Emoji Submission Audit

Audit date: 2026-07-20

Audited release: `submissions/v1.7.0`

Scope: Kidney, Liver, and Stomach

Standard: `docs/proposals/emoji-proposal-approval-rubric.md`

## Executive result

All three PDFs are formally well structured, technically clean, and eligible according to Shuhan He's
confirmed 2026 slate. None is yet best-in-class submission-ready.

| Proposal | Internal score | Status | Main reason it is not ready |
| --- | ---: | --- | --- |
| Kidney | 79/100 | Strongest; revise before filing | The 18x18 art needs an unprompted recognition test and nearest-emoji comparison; material usage claims need more citations; final review, public URL, and filing controls are incomplete. |
| Stomach | 77/100 | Promising; revise before filing | Four of five frequency captures are from 2020, Search/Video screenshots are small, and final art recognition/reviewer/publication gates remain open. |
| Liver | 64/100 | Not ready | Its own PDF says the U.S.-only 2020 Trends captures must be replaced; the 18x18 black silhouette is not self-identifying; most usage claims lack citations. |

The scores are internal controls, not Unicode scores or approval predictions. A proposal cannot be marked
ready while any must-pass filing gate remains open, even if the prose is strong.

## Audit method

The audit used:

- Unicode's current 2026 requirements:
  https://www.unicode.org/emoji/proposals.html
- ESR's higher-benchmark priorities for Emoji 19.0+:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- The eight accepted proposal documents behind the nine Emoji 18.0 characters:
  https://www.unicode.org/emoji/charts-18.0/emoji-proposals.html
- The corrected accepted-proposal and confirmed-decline evidence audit:
  `docs/research/unicode-winning-submissions/analysis.md`
- Rendered inspection of every page in all three v1.7.0 PDFs.
- Pixel-level inspection of all twelve required PNG assets.
- Technical checks using `pdfinfo`, `pdffonts`, `pdftotext`, and `pdfimages`.

## Common findings

### What already passes

- Each title follows the required `Proposal for Emoji: <name>` form.
- All author names, main point of contact, dates, keywords, categories, and sort locations are on page 1.
- Kidney lists the required complete eight-person author set with semicolons:
  Shuhan He; Edgar Lerma; Caitlyn Vlasschaert; Jade M. Teakell; Harish Seethapathy; Jarone Lee;
  Danielle Miller; Timur Erk.
- Liver and Stomach each list only Shuhan He, as required.
- Each PDF includes color and true two-color black-and-white PNGs at exactly 18x18 and 72x72.
- Shuhan He makes a direct first-page ownership warranty, releases the artwork under CC0 1.0, and grants the
  rights required by Unicode's proposal agreement.
- Each proposal addresses all current inclusion and exclusion headings and correctly uses `Not applicable`
  for unsupported completeness or compatibility claims.
- Each proposal includes all five required evidence types and uses `elephant` in Trends and Ngram.
- No PDF contains a logo, brand, text-bearing emoji image, exact-image demand, directional variation, or other
  automatic-decline category.
- All PDFs are unencrypted, have extractable text, use embedded fonts, and render without clipping, overlap,
  broken images, missing glyphs, or accidental blank pages.

### What remains open for all three

1. The repository still contains pre-confirmation eligibility warnings. The confirmed eligibility record and
   current slate decision need to be reflected in the final release manifest so reviewers do not see
   contradictory status.
2. No logged-out public HTTPS URL exists for the exact final PDF.
3. The final official-form filing and confirmation have not occurred.
4. No final domain/factual reviewer and Unicode/process reviewer signoff is recorded against the exact PDFs.
5. No unprompted 18x18 recognition test or nearest-current-emoji comparison board is included.
6. Many factual statements are asserted without citations. Current guidance says claims used for selection
   factors require screenshots or citations.
7. Any revised PDF must carry the new revision date, not 2026-07-12.

## Score breakdown

| Area | Max | Kidney | Liver | Stomach |
| --- | ---: | ---: | ---: | ---: |
| Eligibility and coordination | 15 | 13 | 13 | 13 |
| First-page format | 10 | 10 | 10 | 10 |
| Image package and rights | 15 | 10 | 8 | 12 |
| Frequency and empirical evidence | 20 | 19 | 11 | 14 |
| Inclusion factors | 15 | 12 | 9 | 13 |
| Exclusion factors | 10 | 9 | 9 | 9 |
| Worldwide and durable case | 5 | 4 | 2 | 4 |
| Independent review | 5 | 0 | 0 | 0 |
| Packet and filing control | 5 | 2 | 2 | 2 |
| **Total** | **100** | **79** | **64** | **77** |

Eligibility receives 13 rather than 15 because Shuhan has confirmed that all three concepts are eligible, but
the final release does not yet archive the confirmation or close duplicate-filing coordination. Packet control
receives partial credit because v1.7.0 is versioned and internally complete, but its manifest is stale and no
public final URL or submission record exists.

## Kidney audit

Files:

- `submissions/v1.7.0/kidney/kidney_emoji_proposal_SUBMIT.md`
- `submissions/v1.7.0/kidney/kidney_emoji_proposal_SUBMIT.pdf`

### Strengths

- The complete confirmed author list is already correct in both source and PDF.
- It has the freshest and strongest required frequency set: 2026 Search, Video, worldwide Web Trends,
  worldwide Image Trends, and a 2026 Ngram capture.
- The multiple-meaning argument is concise and cites `kidney-shaped` usage.
- `Already representable` directly addresses Beans, Droplet, and generic medical emoji.
- `Open-ended` and `Faulty comparison` correctly state that the case does not depend on completing an organ
  set or on the existence of Anatomical Heart, Lungs, or Brain.
- The eight-page PDF uses readable, evidence-forward screenshot pages.

### Material weaknesses

- At 18x18, the color image can read as a red bulb, balloon, or bean with a short handle. The medial notch is
  largely lost. The black-and-white 18x18 version becomes a filled irregular silhouette and does not visibly
  preserve the claimed hilum cue.
- The proposal asserts broad uses across filtration, hydration, urine, dialysis, transplant, medication, and
  donation without citing durable sources for the language or use contexts.
- `Kidney + bean or cooking pot` is understandable but does not strengthen the core organ case and can
  reinforce the visual-confusion objection.
- The nearest-emoji comparison is verbal only. The PDF does not show Kidney beside Beans, Droplet,
  Anatomical Heart, Lungs, and Brain at actual 18x18 size.
- No unprompted recognition result establishes that a general viewer sees `kidney` rather than `bean`.

### Required correction before filing

1. Test the current 18x18 art with unprompted viewers and record the confusion matrix.
2. If the art misses the internal threshold, revise the small master to preserve a visible medial notch and
   short anatomical attachment in both color and black-and-white.
3. Add one compact nearest-emoji comparison figure at 18x18 and 72x72.
4. Add citations for the material multiple-meaning and ordinary-use claims; remove any context that is only a
   plausible invented sequence.
5. Obtain factual/domain and Unicode/process signoff on the rebuilt PDF.
6. Publish and verify the exact final PDF, then file and archive the confirmation.

## Liver audit

Files:

- `submissions/v1.7.0/liver/liver_emoji_proposal_SUBMIT.md`
- `submissions/v1.7.0/liver/liver_emoji_proposal_SUBMIT.pdf`

### Strengths

- The correct sole submitter, Shuhan He, is clearly named.
- Page 1 is complete and the rights statement is direct.
- Marking multiple meanings, completeness, and compatibility `Not applicable` is disciplined and follows the
  current guidance better than inventing weak positive factors.
- The exclusion answers are concise and correctly avoid a complete-anatomy argument.
- The 72x72 color design has a clear asymmetric lobe structure and optional gallbladder cue.

### Blocking weaknesses

- Both 2020 Trends screenshots use United States rather than Worldwide. The current guidelines require the
  widest possible location and range. The proposal itself says both captures `must be refreshed to Worldwide
  before filing`, which is a visible draft/blocker note in the submission PDF.
- Search and Video are also 2020 captures. Historical screenshots are allowed as snapshots, but they do not
  meet a best-in-class current-filing standard when current recapture is feasible.
- At 18x18, the black-and-white liver is a filled horizontal blob. The lobe division and gallbladder cues vanish,
  leaving a material recognition risk. The color image may read as meat or a generic red organ.
- Nearly every stated use context - metabolism, digestion, testing, medication, alcohol, hepatitis, fatty
  liver, donation, transplant, food, and education - is uncited.
- With multiple meanings correctly marked `Not applicable`, the proposal depends heavily on direct frequency,
  semantic gap, and visual recognition. Those three areas therefore need stronger proof than they currently
  receive.
- The Search and Video screenshots are small on the rendered page and are less reviewer-friendly than the
  Kidney evidence pages.

### Required correction before filing

1. Replace all four 2020 web captures with current 2026 Search, Video, Worldwide Web Trends, and Worldwide
   Image Trends captures. Keep the 2026 Ngram if its settings remain current and legible.
2. Remove every `must be refreshed` draft sentence from the final PDF after evidence replacement.
3. Redesign or simplify the 18x18 black-and-white art until unprompted viewers identify the organ reliably.
4. Add a visual comparison against Stomach, Anatomical Heart, meat/food substitutes, and other body-part
   emoji.
5. Cite the high-value direct-use claims and remove low-value lists that cannot be evidenced succinctly.
6. Obtain final reviewers, public URL, and filing records.

## Stomach audit

Files:

- `submissions/v1.7.0/stomach/stomach_emoji_proposal_SUBMIT.md`
- `submissions/v1.7.0/stomach/stomach_emoji_proposal_SUBMIT.pdf`

### Strengths

- The correct sole submitter, Shuhan He, is clearly named.
- The multiple-meaning section is the strongest of the three and cites `butterflies in the stomach` and the
  verb sense of `stomach`.
- The sequence examples connect direct bodily sensation with emotion, appetite, food, and care.
- The J-shaped 18x18 color silhouette remains more recognizable than the current Kidney or Liver small art.
- The Trends captures are Worldwide, and the 2026 Ngram capture is current.
- The already-representable and open-ended answers identify the main alternatives without claiming a complete
  digestive-system set.

### Material weaknesses

- Search, Video, Web Trends, and Image Trends are all dated 2020-08-31. They are genuine snapshots but are not
  best-in-class current evidence for a 2026 filing.
- The Search and Video screenshots are small in the PDF. The repeated result counts in text help, but the
  evidence itself should remain readable without zooming aggressively.
- The 18x18 black-and-white silhouette loses the internal curve and may read as an abstract hollow-organ shape.
  Recognition is plausible but untested.
- `Gut feeling` is broader than `stomach` and needs a source or should not be used as a central meaning claim.
- Several ordinary health uses, including indigestion, reflux, endoscopy, and stomach bug, are uncited.
- Page 7 carries only a short `Other Information` section, creating avoidable whitespace. This is not a formal
  defect, but a final rebuild can be more compact without reducing evidence size.

### Required correction before filing

1. Replace all four 2020 web captures with current 2026 Search, Video, Worldwide Web Trends, and Worldwide
   Image Trends captures.
2. Enlarge Search and Video screenshots in the rebuilt PDF.
3. Run the unprompted 18x18 recognition test and compare against Nauseated Face, food emoji, Anatomical Heart,
   and the proposed Liver/Kidney art.
4. Cite or remove `gut feeling` and the material clinical/everyday-use claims.
5. Tighten the final page flow without shrinking evidence.
6. Obtain final reviewers, public URL, and filing records.

## Recommended correction order

1. Kidney first, because its evidence is current and its remaining risk is concentrated in recognizability,
   citation discipline, and filing control.
2. Stomach second, because the semantic case and artwork are strong but the evidence should be refreshed.
3. Liver third, because both the evidence package and small-size paradigm need substantive work.

Do not submit one proposal merely because another is ready. Each concept must pass every gate independently.
