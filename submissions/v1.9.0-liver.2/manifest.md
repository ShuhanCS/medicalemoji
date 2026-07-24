# Medical Emoji Submission Package v1.9.0-liver.2

Package version: 1.9.0-liver.2

Created: 2026-07-24

Status: **Liver prerelease lane. Revision required; not ready to publish or submit.**

Official deadline: End of day 2026-07-31

Official guidelines:
https://www.unicode.org/emoji/proposals.html

## Provenance and scope

This complete prerelease snapshot was copied byte for byte from `submissions/v1.9.0-liver.1/`. Only
`VERSION`, `manifest.md`, `CHANGELOG.md`, and files under `liver/` differ from that frozen prerelease.

| Component | Provenance | Status in v1.9.0-liver.2 |
| --- | --- | --- |
| Ideal proposal template | v1.8.0 byte-identical | Carried forward |
| Best-in-class rubric | v1.8.0 byte-identical | Carried forward |
| Artwork license | v1.8.0 byte-identical | Carried forward |
| White Blood Cell | v1.8.0 byte-identical | Evidence-gated draft |
| Kidney | v1.8.0 byte-identical | Revision required |
| Stomach | v1.8.0 byte-identical | Revision required |
| Liver | Revised in this lane | Revision required; see `liver/READINESS.md` |

## Liver changes

- Replaces the historical 2020 Google Search and Video captures with current 2026-07-24 captures.
- Google currently collapses the native `#result-stats` element to a zero-layout area. The evidence screenshots
  therefore reveal the exact live DOM value in a clearly labeled overlay: about 194,000 Web results and about
  82,000,000 Video results. See `liver/evidence/frequency/EVIDENCE-NOTES.md`.
- Records project-owner confirmation that the Liver eligibility timing is satisfied.

## Fixed identity and rights

Liver lists Shuhan He as the sole submitter and main point of contact. The proposal retains Shuhan He's
first-page warranty that the example images are original, owned by him, released under CC0 1.0, and licensed
as required by the Unicode Emoji Proposal Agreement and License.

## Open gates

- Human 18x18 recognition results meeting the internal 80%/10% gate.
- Domain/factual and Unicode/process review of the exact PDF.
- Public logged-out HTTPS URL, exact form reconciliation, Shuhan He's approval, filing, and archived
  confirmation.

No score overrides these gates. See `liver/READINESS.md` for the complete decision record.

## Immutable snapshot rule

Do not edit this committed prerelease snapshot. A later Liver revision must copy the complete folder to a new
patch version and record only that revision's changes.

Coordination specification:
https://github.com/ShuhanCS/medicalemoji/blob/codex/finalize-organ-submissions/docs/proposals/agent-specs/README.md
