# Reusable ESR/UTC Readiness Panel

Version: 1.0.0

This is an internal, repeatable red-team review of emoji proposals before filing. It is not a review by the
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

## Five independent seats

Each run uses five role-based seats. The first-pass reviewers work independently and do not see one another's
notes. A coordinator then synthesizes the record without deleting minority objections.

1. **Intake gatekeeper.** Checks eligibility, prior-status timing, required sections, evidence captures,
   rights, public-PDF readiness, authorship consistency, and automatic-decline conditions.
2. **ESR selection reviewer.** Tests the strongest inclusion case and every exclusion factor under the current
   published criteria. It must state the strongest good-faith reason to decline.
3. **Community proposal mentor.** Tests whether an educated general reader can understand the need, whether
   the proposal relies on a cause or prestige, and whether the ordinary messages are concrete and global.
4. **Visual and implementation reviewer.** Inspects the exact 18x18 and 72x72 color and black-and-white assets,
   nearest confusers, vendor freedom, CLDR name/keywords/category, and cross-platform feasibility. Shuhan's
   separate image approval remains the project's only human image gate.
5. **UTC skeptical reviewer.** Assumes encoding is permanent and scarce. Tests broad scope, durability,
   open-endedness, duplication, system consistency, and whether the case survives removal of every weak claim.

## Required verdicts

Every seat must choose exactly one:

- `RECOMMEND ONWARD`: internally suitable for Shuhan's filing decision; not a prediction of Unicode action.
- `REVISE AND RERUN`: potentially viable, with named corrections that require another full panel run.
- `STOP THIS CYCLE`: a hard eligibility problem or a weak independent case makes more polishing a poor use of
  the current intake window.

The panel synthesis may say `RECOMMEND ONWARD` only when all hard gates pass, at least four seats recommend
onward, no seat identifies an unresolved automatic-decline condition, and every dissent is reproduced. A tie,
missing seat, or incomplete artifact is `REVISE AND RERUN`. Shuhan makes the final internal decision.

## Anti-rubber-stamp rules

Every reviewer must:

- review the exact artifact hash, not a filename or draft description;
- cite the page, section, asset, or source behind every material criticism;
- identify the nearest existing emoji or sequence and make its strongest substitution case;
- write the strongest reasonable decline rationale before recommending onward;
- separate a missing required item from a strategic weakness and a cosmetic preference;
- list what evidence would change the verdict;
- avoid invented approval probabilities, Unicode scores, or claims about private committee thinking; and
- return exact agent actions with an owner, acceptance condition, and rerun trigger.

## Repeatable run protocol

1. Freeze the artifact and compute its SHA-256 hash.
2. Record the proposal name, package version, Git commit, current official-guideline retrieval date, authorship
   source, image-source/license source, and prior proposal status.
3. Render every PDF page to images. Inspect every page plus the four exact-size artwork files.
4. Give the same frozen dossier to all five seats. Run first-pass reviews independently.
5. Have each seat complete the output contract in [REVIEW-TEMPLATE.md](REVIEW-TEMPLATE.md).
6. The coordinator checks citations, merges duplicate actions, preserves disagreement, and issues the panel
   result. It does not average away a hard blocker.
7. Proposal agents receive the action ledger. Every action is `ACCEPT`, `REJECT WITH REASON`, or `DEFER WITH
   OWNER AND DATE`.
8. Any change to proposal prose, evidence, artwork, authorship, rights, or PDF layout creates a new artifact
   hash and requires a new run. A rerun never overwrites an earlier record.

Generate a frozen run record with:

```powershell
npm run panel:prepare -- --proposal stomach --artifact submissions/v1.12.0/stomach/stomach_emoji_proposal_SUBMIT.pdf --package v1.12.0
```

The command writes a timestamped dossier under `docs/proposals/review-panel/runs/`. Agents then fill the five
seat sections and the coordinator synthesis. Use `--output <path>` to select a stable filename.

## Agent handoff contract

Written feedback is not "make this stronger." Every action must include:

| Field | Required content |
| --- | --- |
| Finding | One falsifiable problem or confirmed strength |
| Severity | `BLOCKER`, `MAJOR`, `MINOR`, or `KEEP` |
| Evidence | Exact PDF page/section/asset and controlling source |
| Change | Concrete edit, replacement, deletion, or verification |
| Owner | Proposal agent, evidence agent, art agent, coordinator, or Shuhan |
| Acceptance condition | Observable result that closes the action |
| Rerun | Seats that must re-review after the change; `ALL` for material changes |

The proposal agent returns the updated artifact hash and an action-by-action response. The panel then reviews
the new artifact from scratch; prior recommendations do not carry forward.
