# Maze, Ultrasound, and First Aid Kit proposal plan

Date: 2026-07-10
Target packet: `submissions/v1.4.0/`
Project version target: `0.22.0`

## Goal

Build three independent, current-format Unicode emoji proposal packets for the 2026 intake: Maze,
Ultrasound, and First Aid Kit. Each packet will contain original open-license color and true black-and-white
artwork at 18x18 and 72x72, a reviewer-facing proposal draft, reproducible frequency-source links, and a
rendered PDF.

The same work will update the Microsoft internal decision brief so David Rhew can ask Vishal Chowdhary to
route one focused candidate through Microsoft's standards, product, design, and legal owners.

## Audience and framing

- Proposal audience: Unicode Emoji Standard & Research Working Group reviewers.
- Microsoft brief audience: Microsoft internal standards, Windows/Segoe UI Emoji, Fluent Emoji, and legal
  owners.
- Maze will be framed as a general puzzle, path, navigation, complexity, choice, and problem-solving concept.
  Cognitive and research uses are secondary; the proposal will not be a neuroscience-awareness argument.
- Ultrasound will be framed as a broad real-time imaging method represented by a monitor and handheld probe,
  not as a pregnancy-only or fetus image.
- First Aid Kit will use a generic green case and white safety cross. It will not reproduce the protected Red
  Cross emblem, a commercial mark, or text.

## Evidence controls

- Verify each concept against Unicode's live proposal-status sheet and the latest released emoji data.
- Include all five frequency categories required by the 2026 guidance: Google Search, Google Video Search,
  Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer.
- Mark a proposal `DRAFT` until every required screenshot is available and compliant. Reproducible URLs and
  an explicit evidence-capture checklist are not substitutes for missing screenshots.
- Treat absence from the public status sheet as strong public-record evidence, not proof that no proposal was
  ever auto-declined, because Unicode omits automatically declined requests from that sheet.

## Deliverables

- [x] Status and evidence note for the three concepts.
- [x] Original editable SVG sources and color/black-and-white PNGs at 18x18 and 72x72.
- [x] Three standalone Markdown proposal drafts and rendered PDFs.
- [x] `v1.4.0` manifest, artwork license, and combined portfolio ranking.
- [x] Revised Microsoft decision brief, cover email, DOCX, and PDF.
- [x] Updated README, HANDOFF, changelog, project version, and proposal status record.
- [x] Validation of image dimensions/two-tone artwork, proposal sections, PDF rendering, and app build/lint.

## Semver decision

This is a minor proposal release and a minor application/documentation release. It adds three substantive
proposal packets and changes the recommended Microsoft decision, so the proposal packet advances from
`v1.3.0` to `v1.4.0` and the project version advances from `0.21.0` to `0.22.0`.

## Completion record

- [x] All deliverables completed and inspected.
- [x] Task files committed and pushed to `codex/eligible-2026-slate`.
