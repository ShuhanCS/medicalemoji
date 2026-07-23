# Emoji Image Evidence Database Plan

## Objective

Create a reproducible, historically grounded visual-evidence database for evaluating Medical Emoji proposal artwork. The database will distinguish Unicode's binding image requirements from descriptive patterns in proposals that were subsequently encoded, then use a transparent rubric to assess the current Kidney artwork.

## Scope

- Use Unicode's current proposal guidance as the controlling standard.
- Use official Unicode L2 proposal documents that resulted in encoded emoji as the historical source set.
- Start with a curated, visually relevant benchmark set: anatomical organs, a medically adjacent concept, an intentionally confusable bean-shaped food, and successful proposals with simple, complex, and abstract silhouettes.
- Preserve source URLs and page locations rather than republishing third-party artwork. Store only factual annotations and reproducible asset references.
- Evaluate the four current Kidney samples: 18x18 and 72x72, each in color and black-and-white.

## Deliverables

1. A versioned corpus manifest with source provenance, outcome, visual family, and relevance annotations.
2. An evidence rubric that labels each criterion as either a Unicode requirement, an operational test, or a non-scoring historical observation.
3. A repeatable native-size image-inspection script and a recorded Kidney result.
4. A concise historical analysis explaining what can and cannot be inferred from successful proposals.

## Method

1. Verify the current Unicode image rules against the official guideline page.
2. Select and annotate a benchmark subset from the repository's existing 55 successful-proposal register, adding the successful 2019 Heart (Organ) and Lung proposals as direct anatomical comparators.
3. Run deterministic checks on the Kidney image files: exact dimensions, image mode, transparency/background behavior, occupied bounding box, contrast, connected components, and color-versus-black-and-white equivalence.
4. Identify visual risks that the deterministic checks cannot resolve and specify a blinded recognition test; do not present unrun tests as results.
5. Bump the workspace patch version, document the new data-package version, verify the generated records, commit, and push.

## Non-goals

- This will not claim that image style caused an emoji to be encoded; outcome also depends on frequency, scope, and the overall proposal.
- This will not copy or redistribute artwork from other submitters without an explicit reuse right.
- This will not modify the submitted Kidney artwork until the evidence review identifies a concrete design change.
