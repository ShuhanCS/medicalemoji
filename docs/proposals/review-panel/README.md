# Reusable ESR/UTC Readiness Panel

Version: 1.1.0

This is an optional, repeatable editorial review of emoji proposals. It is not a filing gate or a review by the
Unicode Consortium, the Emoji Standard & Research Working Group (ESR), the Unicode Technical Committee (UTC),
or any person named below. It must never be described as an endorsement, recommendation, vote, or private
feedback from those people or groups.

The current Unicode group is the **Emoji Standard & Research Working Group (ESR)**, a working group under the
UTC. There is no current body called the "Emoji Technical Committee." ESR reviews emoji submissions and makes
recommendations; the UTC makes technical decisions.

Official sources, retrieved 2026-07-26:

- Current emoji submission requirements: https://www.unicode.org/emoji/proposals.html
- Emoji submission FAQ: https://www.unicode.org/faq/emoji_submission.html
- ESR remit and participation: https://www.unicode.org/emoji/techindex.html
- Current technical group leadership: https://www.unicode.org/consortium/techcommittees.html
- Unicode technical group procedures: https://www.unicode.org/consortium/tc-procedures.html
- Proposal status meanings: https://www.unicode.org/emoji/emoji-proposals-status.html

## Public-expert provenance, not impersonation

Named experts identify public bodies of work that inform a review lens. Agents do not write in a person's
voice, speculate about private views, or claim that the person saw the proposal.

| Public source | Verified public relationship | What the panel may learn from it | What the panel must not claim |
| --- | --- | --- | --- |
| Jennifer Daniel | Current ESR chair on Unicode's leadership page | Current ESR priorities, selection-factor discipline, visual communication, portfolio-level tradeoffs | "Jennifer Daniel reviewed/recommended this" or a prediction of her vote |
| Jennifer 8. Lee and Emojination | Emojination founder and proposal mentor; Unicode announced her as an Emoji Subcommittee vice-chair in 2017 | Submitter coaching, broad public meaning, persuasive plain language, and anticipating reviewer questions | A current Unicode title unless newly verified; personal feedback or endorsement |
| Ned Holbrook | Current ESR vice-chair on Unicode's leadership page | Cross-platform implementation, typography, naming, and small-size system fit | "Ned Holbrook approved the design" or vendor support |
| UTC leadership and procedures | Current UTC chair/vice-chair and published technical procedures | Permanence, consistency, scope, and the difference between a working-group recommendation and a UTC decision | A UTC outcome, vote count, or insider access |

Historical source for Jennifer 8. Lee's 2017 role:
https://blog.unicode.org/2017/08/new-emoji-subcommittee-vice-chairs.html

Current Emojination biography:
https://www.emojination.org/who-we-are

## Five available review lenses

Use the lenses that would materially help the current draft. A full run may use all five independently; a
focused consultation may use fewer. The coordinator synthesizes useful findings without turning preferences
or hypothetical objections into requirements.

1. **Intake gatekeeper.** Checks eligibility, prior-status timing, required sections, evidence captures,
   rights, public-PDF readiness, authorship consistency, and automatic-decline conditions.
2. **ESR selection reviewer.** Checks whether the inclusion and exclusion sections make a compelling,
   candidate-specific case under the current published criteria.
3. **Community proposal mentor.** Tests whether an educated general reader can understand the need, whether
   the proposal relies on a cause or prestige, and whether the ordinary messages are concrete and global.
4. **Visual and implementation reviewer.** Inspects the exact 18x18 and 72x72 color and black-and-white assets,
   nearest confusers, vendor freedom, CLDR name/keywords/category, and cross-platform feasibility. Shuhan's
   separate image approval remains the project's only human image gate.
5. **Scope and durability reviewer.** Checks permanence, breadth, open-endedness, duplication, and system
   consistency without requiring the proposal to argue against itself.

## Optional review outcomes

When a concise outcome helps coordination, a reviewer may use:

- `READY FOR FINAL CHECK`: no material issue found in that reviewer's scope.
- `REVISION SUGGESTED`: a concrete change would improve compliance, clarity, accuracy, artwork, or persuasion.
- `FILING BLOCKER`: a cited official requirement is unmet.

No quorum, vote count, numeric verdict, or simulated approval recommendation is required. Shuhan makes the
final internal decision using the proposal, official requirements, and any useful editorial feedback.

## Review quality rules

Every reviewer must:

- review the exact artifact hash, not a filename or draft description;
- cite the page, section, asset, or source behind every material criticism;
- separate a missing official requirement from a substantive suggestion and a cosmetic preference;
- avoid invented approval probabilities, Unicode scores, or claims about private committee thinking; and
- recommend only concrete changes that improve the proposal.

## Repeatable run protocol

1. Freeze the artifact and compute its SHA-256 hash.
2. Record the proposal name, package version, Git commit, current official-guideline retrieval date, authorship
   source, image-source/license source, and prior proposal status.
3. Render every PDF page to images. Inspect every page plus the four exact-size artwork files.
4. Give the dossier to the review lenses that would help and run them independently when multiple lenses are
   used.
5. Reviewers may use [REVIEW-TEMPLATE.md](REVIEW-TEMPLATE.md) or return shorter focused notes.
6. The coordinator checks citations, merges duplicates, separates official blockers from suggestions, and
   chooses which suggestions improve the proposal.
7. Rerun a lens only when the coordinator wants a second look at a material revision. Preserve any earlier
   record rather than overwriting it.

Generate a frozen run record with:

```powershell
npm run panel:prepare -- --proposal stomach --artifact submissions/v1.12.0/stomach/stomach_emoji_proposal_SUBMIT.pdf --package v1.12.0
```

The command writes a timestamped dossier under `docs/proposals/review-panel/runs/`. Agents then fill the five
seat sections and the coordinator synthesis. Use `--output <path>` to select a stable filename.

## Optional editorial handoff

Useful feedback is specific enough to apply without creating a litigation-style action ledger. It may include:

| Field | Useful content |
| --- | --- |
| Finding | One falsifiable problem or confirmed strength |
| Type | `OFFICIAL BLOCKER`, `SUBSTANTIVE SUGGESTION`, `COPYEDIT`, or `KEEP` |
| Evidence | Exact PDF page/section/asset and controlling source |
| Change | Concrete edit, replacement, deletion, or verification |

The proposal agent is not required to answer every suggestion. Apply changes that improve compliance,
accuracy, clarity, artwork, or persuasion. A new panel run is optional unless an official filing blocker needs
confirmation.
