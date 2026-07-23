# Emoji Image Evidence Database

Version: `1.0.0`  
Created: 2026-07-23

This is a research database for assessing proposal artwork, not a claim that a particular illustration caused an emoji to be encoded. Unicode's selection decision also depends on expected use, scope, completeness, and the whole proposal.

## What is in the database

- `winning-image-corpus.v1.json` — a curated, outcome-verified visual benchmark of 10 successful proposals. It combines two directly comparable anatomical-organ precedents with eight successful proposals that exercise different small-scale visual problems.
- `unicode-image-rubric.v1.md` — the criteria, evidence labels, and scoring method.
- `analyze_image_set.py` — a deterministic inspection tool for the required four proposal images.
- `kidney-v2.0.0-image-analysis.json` — the recorded inspection of the current Kidney image set.

Each corpus record gives the official Unicode PDF URL, proposal page where the sample image appears, encoding outcome, and narrowly stated visual annotation. It deliberately does **not** copy third-party proposal art into this public repository. The original public documents remain the authoritative image source.

## Source hierarchy

1. **Binding requirements:** Unicode's current [Guidelines for Submitting Unicode Emoji Proposals](https://www.unicode.org/emoji/proposals.html). They require color and black-and-white examples at both 18x18 and 72x72 pixels; the images must demonstrate that the paradigm is recognizable at typical size, without foreknowledge. Unicode expressly says the supplied image is not production art.
2. **Historical context:** Unicode's [accepted emoji proposals chart](https://unicode.org/emoji/charts/emoji-proposals.html) and the official L2 PDFs in the corpus.
3. **Operational tests:** the database rubric's blinded-recognition and confusability tests. These make the word “recognizable” measurable, but their thresholds are our decision rules, not Unicode-published pass marks.

## How to reproduce the current image inspection

From the repository root:

```powershell
python docs/research/emoji-image-evidence/analyze_image_set.py `
  --input-dir submissions/v2.0.0/images `
  --output docs/research/emoji-image-evidence/kidney-v2.0.0-image-analysis.json
```

The script uses only image-file properties. It cannot determine whether a person recognizes an organ correctly. The required blinded test is specified in the rubric and remains the decisive next evidence item.

## Corpus design

The seed corpus is intentionally not a random sample. It is a **contrast set** built to answer the Kidney design question:

- Heart (Organ) and Lung are the closest successful anatomical-organ precedents.
- Beans and Beet test the most likely food-shape confusion.
- X-Ray is the closest successful medical concept.
- Orca and Jellyfish are successful silhouette-dependent concepts.
- Fingerprint, Treasure Chest, and Falling Debris show detail-dense, object, and abstract paradigms at proposal size.

The repository's broader `docs/research/unicode-winning-submissions/accepted-emoji-proposals-manifest.json` remains the parent outcome register (268 historical accepted rows, including 55 successful 2020–2024 proposal documents archived as extracted text). Future corpus versions should add annotations or checks from that register rather than relabeling a small sample as universal evidence.
