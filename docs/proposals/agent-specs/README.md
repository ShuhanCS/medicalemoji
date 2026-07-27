# 2026 Proposal Agent Coordination Index

Version: 1.7.0

Date: 2026-07-26

This directory contains concept-specific execution specifications. Stomach and Kidney are active 2026
finalization lanes; the other records remain available for their own independent concept work.

## Agent assignments

| Concept | Standalone specification | Current input | Next controlled output |
| --- | --- | --- | --- |
| Stomach | [`stomach-agent-spec.md`](stomach-agent-spec.md), v2.0.0 | `1.12.0-candidate.9` | Next candidate revision if changed, then cumulative canonical `v1.12.0` |
| Kidney | [`kidney-agent-spec.md`](kidney-agent-spec.md), v2.0.0 | `v1.12.0-kidney.7` | Complete `v1.12.0-kidney.8` if changed, then cumulative canonical `v1.12.0` |
| White Blood Cell | [`white-blood-cell-agent-spec.md`](white-blood-cell-agent-spec.md) | Historical lane | Deferred independent revision |
| Liver | [`liver-agent-spec.md`](liver-agent-spec.md) | `v1.12.0-liver.11` | Deferred independent publication decision |
| Pill Pack | [`pill-pack-agent-spec.md`](pill-pack-agent-spec.md) | Historical lane | Deferred go/no-go review |

Every committed package snapshot is immutable. Kidney changes increment the final prerelease number; Stomach
changes increment its candidate number until canonical promotion. An editor never revises an earlier snapshot
in place.

## Shared proposal-building guidance

Every active concept editor must follow
[`../CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`](../CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md) before revising
proposal prose. It directs editors to study the historical acceptance and decline record, understand the goal
of each Unicode section, and make a compelling candidate-specific argument.

The shared approval rubric and template are downstream compliance checks. They are not fill-in-the-blank
writing systems, and their example patterns must not be copied across proposals. Candidate-specific evidence,
substitute analysis, priority, meaning, and visual identity must drive the writing. The shared guidance does
not require new process documents or formal gate statuses.

Only current Unicode submission requirements are filing gates. Detailed evidence logs, computer validators,
comparison boards, readiness scores, artifact hashes, and panel records are optional internal tools. They must
not expand the public proposal or block it unless they expose a real compliance, factual, artwork, or
presentation problem.

## Same-cycle independence rule

Stomach, Maze, and Kidney may all be filed in the same cycle if each packet matures, but they are three
independent proposals. Never describe them as a `co-submission`, `medical emoji set`, `organ set`, campaign
bundle, or completeness request. Each PDF and form must use its own evidence, byline, artwork, selection theory,
and positive Open-ended limiting principle without naming another active filing.

Maze creates no Open-ended tension with either organ. Filing Stomach and Kidney together makes an anatomy-set
objection more foreseeable, but it is not a contradiction: Stomach is bounded by its literal, appetite,
tolerance, fullness, and nervous-anticipation meanings; Kidney is bounded by its shape, stone, testing,
treatment, donation/transplant, frequency, and substitution evidence. Neither argument promises that no other
organ will ever be proposed, and neither creates an obligation to encode one.

## Canonical promotion

Do not merge concept branches or candidate folders wholesale. Starting from canonical `submissions/v1.11.0/`,
the coordinator applies only the accepted Stomach and Kidney deltas and creates cumulative canonical
`submissions/v1.12.0/`. The package may contain both candidates, but their proposal folders, PDFs, evidence,
artwork, authorship, readiness conclusions, public URLs, and form entries remain separate. Maze follows its own
package history and filing record.

If either organ needs another revision before acceptance, increment only that concept's candidate or
prerelease number. Do not mutate an accepted or committed snapshot.

## External-action boundary

No agent may publish a public PDF, submit the Unicode form, email authors or reviewers, push, merge, or deploy
without explicit authorization. A proposal is not `READY TO SUBMIT` until Shuhan He reviews the exact final
PDF, the public logged-out URL and form data are reconciled, and authorization is recorded.

Official Unicode guidelines:

https://www.unicode.org/emoji/proposals.html

Official proposal status definitions:

https://www.unicode.org/emoji/emoji-proposals-status.html

## Optional panel consultation

The coordinator may use the repeatable [`ESR/UTC-readiness panel`](../review-panel/README.md) when another
editorial perspective would help. Its feedback is advisory: no action ledger, numeric verdict, exact-hash gate,
or automatic rerun is required. Apply suggestions only when they improve the proposal. The panel is an internal
simulation; no agent may attribute its feedback or verdict to a named expert, ESR, UTC, or Unicode.
