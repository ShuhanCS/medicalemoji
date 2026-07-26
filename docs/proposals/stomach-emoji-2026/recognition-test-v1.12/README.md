# Stomach 18px Recognition Test

Version: 1.0.0

Status: Ready to run

## Purpose

Test whether general viewers identify the selected Stomach glyph without being told the concept. This human
test is required because computer shape metrics cannot establish semantic recognition.

## Participants

- Recruit at least 12 people who did not create or review the artwork.
- Do not tell participants that the target is a stomach, organ, medical symbol, or emoji proposal.
- Assign anonymous participant codes `P01` through `P12` or higher.
- Do not collect names or unnecessary personal information.

## Materials

- Color stimulus: `../candidate-v1.12/images/stomach_color_18x18_SUBMIT.png`
- Black-and-white stimulus: `../candidate-v1.12/images/stomach_bw_18x18_SUBMIT.png`
- Confuser boards: `../validation-v1.12/comparison-color-18.png` and
  `../validation-v1.12/comparison-bw-18.png`
- Response sheet: `responses.csv`
- Randomized local runner: `recognition-test.html`

Show each glyph at its actual 18x18 pixel size on a neutral background. Do not zoom it for the participant.

## Procedure

1. Randomize participants between color-first and black-and-white-first orders.
2. Show the first 18x18 stimulus alone.
3. Ask exactly: `What is this?`
4. Record the complete free-text response before giving any hint or choices.
5. Show the second stimulus in a separate pass and repeat the same question.
6. Present the matching confuser board and record one forced-choice answer.
7. Do not correct or coach the participant until all responses are recorded.

## Predeclared scoring

Accepted unprompted answers are `stomach`, `human stomach`, or an unambiguous equivalent-language
translation. `Organ`, `body part`, `gut`, `blob`, `bean`, `liver`, `kidney`, `heart`, `meat`, `pouch`, and
`balloon` are not accepted as correct unprompted identifications.

The artwork passes only if:

- at least 10 of 12 participants identify Stomach correctly in the color pass;
- at least 10 of 12 participants identify Stomach correctly in the black-and-white pass; and
- no single wrong concept dominates either pass.

Preserve the raw responses. Do not replace them with a percentage-only summary.

## Local runner

Open `recognition-test.html` in Firefox at 100% zoom. It randomizes color-first versus black-and-white-first,
prevents forced choice until both free responses are recorded, stores anonymous rows in that browser profile,
and exports a CSV matching `responses.csv`. Keep one facilitator in control of the browser so participants do
not see the image filenames or source paths.

## Result record

After collection, add a signed and dated `RESULT.md` containing participant count, exact asset SHA-256 hashes,
color score, black-and-white score, forced-choice score, dominant wrong answers, pass/fail decision, and the
Git commit containing `responses.csv`.
