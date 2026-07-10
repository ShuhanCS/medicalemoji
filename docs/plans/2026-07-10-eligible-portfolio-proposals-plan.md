# Eligible portfolio proposal slate plan

Date: 2026-07-10

## Audience and outcome

The proposal packets are written for Unicode's Emoji Standard & Research Working Group. The release manifest
and ranking brief are written for Shuhan He and Microsoft collaborators deciding what to file in the 2026
window.

The outcome is a versioned `submissions/v1.3.0/` release containing complete draft packets for the existing
Medical Emoji portfolio concepts whose last public submission was in 2020, plus the explicitly requested
2018 Inhaler concept. Every included concept's four-year wait has clearly elapsed under either a
submission-date or decline-date interpretation.

## Confirmed slate

1. White Blood Cell
2. Blood Bag
3. Pill Pack
4. Weight Scale
5. Leg Cast
6. IV Bag
7. CT Scan
8. Pill Box
9. Inhaler

Pill Pack and Pill Box remain distinct drafts because one is medication packaging and the other is a reusable
organizer. The release must explicitly compare them and recommend against filing both without a product-level
decision about overlap and distinctiveness.

## Deliverables

1. Record the live Unicode status rows and eligibility reasoning in `docs/research/`.
2. Recover real historical Search, Video, Trends Web, and Trends Image evidence from the archived 2020 DOCX
   files. Label every capture with its actual historical date or period; never imply it is current.
3. Add a current Google Books Ngram capture with `elephant` for each concept. Recover the official 2018
   Inhaler proposal evidence and record its narrower historical scope honestly.
4. Create original, textless vector paradigm images in color and true black-and-white at 18x18 and 72x72,
   with editable SVG sources and a deterministic build script.
5. Draft one concise, standalone Unicode proposal per concept. Each proposal must address every current
   inclusion and exclusion factor, use `Not applicable` when appropriate, and avoid petition, campaign,
   awareness, stigma, or faulty-comparison arguments.
6. Render every proposal to a public PDF and visually inspect every page.
7. Produce a slate ranking that distinguishes submission readiness from strategic merit. Include expected
   usage, distinctiveness, overlap, existing-emoji substitutes, and implementation complexity.
8. Update the repository handoff, README, changelog, and semantic version.

## Evidence rules

- The Unicode status sheet is the source of record for public submission dates and statuses.
- Historical Google result counts are snapshots, not current counts.
- Google Search and Trends automation may be rate-limited. A fresh manual recapture is a filing preflight,
  not a reason to fabricate evidence.
- The five required frequency categories must appear in every PDF: Google Search, Google Video Search,
  Google Trends Web Search, Google Trends Image Search, and Google Books Ngram Viewer.
- Medical burden, society support, and campaign activity may explain durable meanings but do not substitute
  for Unicode frequency evidence.
- Each concept stands on its own. The proposals do not argue for completion of a medical set.

## Artwork decision

These are simple emoji paradigms and the repository uses editable SVG sources. The image workflow therefore
routes to deterministic code-native vector artwork rather than generated raster illustrations. All final art
will be released under the proposal release's CC0 artwork license.

## Verification

- Confirm all required PNG dimensions and true two-tone black-and-white output.
- Scan proposal sources and extracted PDF text for placeholders and internal planning language.
- Confirm every proposal contains all required headings, four example images, and five frequency sources.
- Render every PDF page with Poppler and inspect at readable scale.
- Run `npm run lint`, `npm run build`, Python compilation, and `git diff --check`.

## Semantic version decision

This is a minor release because it adds nine new proposal packets and a portfolio ranking. Bump the
application/workspace version from `0.20.0` to `0.21.0` and publish the proposal release as `v1.3.0`.
