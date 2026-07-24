# Liver 18x18 Unprompted Recognition Protocol

Status: **Prepared; no human participants have been tested.**

## Gate

The internal pass target is at least 80% correct unprompted identification at 18x18, with no single wrong
concept above 10% of responses. This is a project quality gate, not a Unicode requirement.

## Participants

- Recruit at least 20 adults who were not involved in the proposal or artwork.
- Do not tell participants that the target is a body part, organ, medical symbol, or Liver.
- Record whether each participant has a clinical or biological-science background, but do not exclude them.
- Test color and black-and-white artwork separately; randomize the order between participants.

## Prompt

Show the isolated 18x18 image at actual size on a normal-density display. Ask only:

> What does this picture represent? Please give the first specific concept that comes to mind.

Do not offer choices, hints, enlarged previews, the proposal title, or the comparison board. Record the first
answer verbatim before any follow-up.

## Coding

- `Correct`: liver or clearly equivalent wording such as hepatic organ.
- `Broader organ`: organ, internal organ, or body part without identifying Liver.
- `Named confusion`: stomach, heart, meat, beans, mushroom, speech bubble, or another specific concept.
- `Unknown`: no answer or explicitly cannot identify.

Two reviewers should independently code ambiguous verbatim answers and reconcile disagreements. Preserve the
de-identified response sheet with the exact artwork hash, test date, participant count, and order assignment.

## Retest rule

If either 18x18 variant misses the gate, revise that variant in a new immutable Liver prerelease snapshot and
repeat the test with new unprompted participants. AI image labels and prompted multiple-choice results do not
count as human recognition evidence.
