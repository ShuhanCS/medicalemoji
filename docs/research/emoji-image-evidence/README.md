# Emoji Image Evidence Database

Version: `1.1.0`
Created: 2026-07-23

This is a reusable research database for assessing any Medical Emoji proposal's artwork. It is not a claim that a particular illustration caused an emoji to be encoded. Unicode's selection decision also depends on expected use, scope, completeness, and the whole proposal.

## What is in the database

- `unicode-winning-image-corpus.v1.json` — a curated, outcome-verified visual benchmark of 10 successful proposals. It combines two directly comparable anatomical-organ precedents with eight successful proposals that exercise different small-scale visual problems.
- `proposal-image-rubric.v1.md` — the reusable criteria, evidence labels, test protocol, and scoring method.
- `analyze_proposal_image_set.py` — a parameterized deterministic inspection tool for any required four-image proposal set.
- `rehydrate_winning_image_corpus.py` — fetches the authoritative public source PDFs and renders their annotated pages outside the repository for review.
- `case-studies/` — candidate-specific recorded analyses. Kidney v2.0.0 is the first case study, not the framework's default candidate.

Each corpus record gives the official Unicode PDF URL, proposal page where the sample image appears, encoding outcome, and narrowly stated visual annotation. It deliberately does **not** copy third-party proposal art into this public repository. The original public documents remain the authoritative image source.

## Source hierarchy

1. **Binding requirements:** Unicode's current [Guidelines for Submitting Unicode Emoji Proposals](https://www.unicode.org/emoji/proposals.html). They require color and black-and-white examples at both 18x18 and 72x72 pixels; the images must demonstrate that the paradigm is recognizable at typical size, without foreknowledge. Unicode expressly says the supplied image is not production art.
2. **Historical context:** Unicode's [accepted emoji proposals chart](https://unicode.org/emoji/charts/emoji-proposals.html) and the official L2 PDFs in the corpus.
3. **Operational tests:** the database rubric's blinded-recognition and confusability tests. These make the word “recognizable” measurable, but their thresholds are our decision rules, not Unicode-published pass marks.

## How to reproduce the current image inspection

From the repository root, replace the values with the candidate's package and filenames:

```powershell
python docs/research/emoji-image-evidence/analyze_proposal_image_set.py `
  --input-dir submissions/vX.Y.Z/images `
  --output docs/research/emoji-image-evidence/case-studies/<candidate>-vX.Y.Z-image-analysis.json `
  --asset-set "<Candidate> proposal vX.Y.Z" `
  --color-18 <candidate>_color_18x18_SUBMIT.png `
  --color-72 <candidate>_color_72x72_SUBMIT.png `
  --bw-18 <candidate>_bw_18x18_SUBMIT.png `
  --bw-72 <candidate>_bw_72x72_SUBMIT.png
```

The script uses only image-file properties. It cannot determine whether a person recognizes the intended candidate correctly. The required blinded test is specified in the rubric and remains the decisive next evidence item.

## Corpus design

The seed corpus is intentionally not a random sample. It is a **contrast set** that can be filtered for each candidate's design question:

- Heart (Organ) and Lung are anatomical-organ precedents.
- Beans and Beet are food-shape comparators.
- X-Ray is a medically adjacent concept.
- Orca and Jellyfish are successful silhouette-dependent concepts.
- Fingerprint, Treasure Chest, and Falling Debris show detail-dense, object, and abstract paradigms at proposal size.

The repository's broader `docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json` remains the parent outcome register (268 historical accepted rows, including 55 successful 2020–2024 proposal documents archived as extracted text). Future corpus versions should add annotations or checks from that register rather than relabeling a small sample as universal evidence.

## Adding a new case study

1. Add the candidate's semver package under `submissions/` first.
2. Run the parameterized inspector and save its JSON under `case-studies/`.
3. Create a short assessment that identifies the candidate's likely confusables, invariant visual cues, and blinded-test result or explicitly states that the test has not been run.
4. If the candidate has a novel visual family, add official successful comparators to the corpus in a new dataset version with a source page and an outcome-verified record.
