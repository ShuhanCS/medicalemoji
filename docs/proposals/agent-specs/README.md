# 2026 Proposal Agent Coordination Index

Version: 1.4.0

Date: 2026-07-26

This directory contains five standalone specifications that may be handed to five separate agents. Each agent
works from the same coordinator-supplied `BASE_COMMIT` in an isolated Git worktree and branch.

## Agent assignments

| Concept | Standalone specification | Branch | First prerelease lane |
| --- | --- | --- | --- |
| Kidney | [`kidney-agent-spec.md`](kidney-agent-spec.md) | Completed | Canonical `v1.10.0` |
| White Blood Cell | [`white-blood-cell-agent-spec.md`](white-blood-cell-agent-spec.md) | `agent/white-blood-cell-2026` | `v1.9.0-white-blood-cell.1` |
| Stomach | [`stomach-agent-spec.md`](stomach-agent-spec.md) | `agent/stomach-2026` | `v1.9.0-stomach.1` |
| Liver | [`liver-agent-spec.md`](liver-agent-spec.md) | `agent/liver-2026` | `v1.9.0-liver.1` |
| Pill Pack | [`pill-pack-agent-spec.md`](pill-pack-agent-spec.md) | `agent/pill-pack-2026` | `v1.9.0-pill-pack.1` |

These are valid SemVer prerelease versions. A second immutable update in a lane increments the final number,
for example `v1.10.0-kidney.2`. An agent never edits an earlier lane snapshot.

## Shared case-building gate for the active four

The Stomach, Kidney, Liver, and White Blood Cell agents must follow
[`../CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md`](../CASE-BUILDING-AND-DRAFTING-INSTRUCTIONS.md) before revising
proposal prose. Each creates a concept-specific `CASE-BRIEF.md` and `CLAIM-LEDGER.md` in its active concept
folder and reaches `CASE READY` before drafting. Pill Pack is not included in this assignment.

The shared approval rubric and template are downstream compliance checks. They are not fill-in-the-blank
writing systems, and their example patterns must not be copied across proposals. Candidate-specific evidence,
substitute analysis, priority, meaning, and visual identity must drive the writing.

## Frozen baseline and collision rule

The coordinator gives every agent the same `BASE_COMMIT`, which must contain canonical package `v1.8.0` and
these specifications. Agents must not start from `master`, an older branch tip, or another agent's branch.

The Kidney lane is complete in canonical `v1.10.0`. Agents for the other four already-assigned lanes may
continue from the coordinator-supplied v1.8.0 base and hand back concept-only deltas. Pill Pack also imports its complete historical concept folder from
`submissions/v1.3.0/pill-pack/`. Agents may change only their unique prerelease folder. They must not change
README files, the controlling slate specification, root `CHANGELOG.md`, `package.json`, `package-lock.json`,
another lane, or any canonical package.

The prerelease folder is the agent branch's explicit SemVer trail. Root project release metadata remains under
coordinator control so parallel branches do not collide.

## Canonical promotion

Do not merge agent branches wholesale. After reviewing a lane, the coordinator applies only its accepted
concept delta to a fresh copy of the latest canonical package and creates the next cumulative canonical minor:

1. Kidney authorship and the accepted review delta are canonical in `v1.10.0`.
2. White Blood Cell is applied on top of `v1.10.0` and becomes `v1.11.0`.
3. Stomach is applied on top of `v1.11.0` and becomes `v1.12.0`.
4. Liver is applied on top of `v1.12.0` and becomes `v1.13.0`.
5. Pill Pack, only if advanced, is applied on top of `v1.13.0` and becomes `v1.14.0`.

If an agent needs another revision before acceptance, increment that lane's prerelease number. Canonical
numbers above are expected targets, not reservations that override an intervening coordinator release.

## External-action boundary

No agent may publish a public PDF, submit the Unicode form, email authors or reviewers, push, merge, or deploy
without explicit authorization. A proposal is not `READY TO SUBMIT` until Shuhan He reviews the exact final
PDF, the public logged-out URL and form data are reconciled, and authorization is recorded.

Official Unicode guidelines:

https://www.unicode.org/emoji/proposals.html

Official proposal status definitions:

https://www.unicode.org/emoji/emoji-proposals-status.html

## Required panel handoff

Before a lane can be promoted, its exact final artifact must complete the repeatable
[`ESR/UTC-readiness panel`](../review-panel/README.md). The proposal agent receives the panel's written action
ledger and must answer every action with `ACCEPT`, `REJECT WITH REASON`, or `DEFER WITH OWNER AND DATE`.
Material changes create a new artifact hash and require another panel run. The panel is an internal simulation;
no agent may attribute its feedback or verdict to a named expert, ESR, UTC, or Unicode.
