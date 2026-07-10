# Three-organ 2026 submissions and Microsoft internal brief

Date: 2026-07-09

## Audience and outcome

The emoji proposals are written for Unicode's Emoji Standard & Research Working Group (ESR). The Microsoft
brief is written for David Rhew and Vishal Chowdhary as an internal routing and decision document.

The outcome is a versioned release containing standalone Kidney, Stomach, and Liver proposal PDFs, plus a
short Microsoft document that asks for procedural clarification, vendor implementation support, and design
ownership without asking any Unicode officer to favor an outcome.

## Deliverables

1. Create `submissions/v1.2.0/` with a manifest and one self-contained packet for each organ.
2. Rewrite all three proposals to the current 2026 Unicode structure and target the concise pattern found in
   recent successful proposals: direct answers, concrete sequence examples, explicit exclusion-factor
   rebuttals, `n/a` where a factor does not apply, and no petition, campaign, or cause argument.
3. Supply original, textless vector reference artwork in color and true black-and-white, rendered at 18x18
   and 72x72 pixels. Keep editable SVG sources and a reproducible build script.
4. Include all five required frequency-evidence categories in every proposal. Reuse the project's real
   archived Google Search, Video, Trends Web, and Trends Image captures where fresh capture is blocked, label
   their capture period honestly, and add current Google Books Ngram captures with `elephant`.
5. Record the November 4, 2022 decline notices and the unresolved four-year-rule interpretation in a private
   project evidence note. Do not put eligibility caveats inside the proposal argument itself.
6. Create a Monday-ready Microsoft internal brief in Markdown, DOCX, and PDF. Its first action is a narrow
   eligibility/process clarification; its substantive request is written anticipated vendor support for the
   three proposals, Fluent Emoji design ownership, and identification of Microsoft's ESR participant.
7. Update the project semantic version and changelog, validate all PDFs visually and textually, commit only
   task files, and push the feature branch.

## Evidence and integrity rules

- Never fabricate search counts, screenshots, endorsements, vendor commitments, rights assignments, or
  Unicode decisions.
- A historical screenshot is labeled with its actual capture period; it is not represented as a 2026 capture.
- Google Search and Trends are currently returning CAPTCHA/429 responses to automation. This is documented in
  the release manifest. A morning recapture is recommended even when the historical evidence satisfies the
  structural packet requirement.
- The four-year rule is treated as unresolved because Unicode calls it new in March 2024, does not define the
  clock's start date or retroactivity, and nevertheless lists April 2024 submissions for three concepts that
  had late-2020 declines.
- The proposal PDFs contain no placeholders, TODOs, internal planning language, or unsigned Microsoft claims.
- Artwork is built from project-authored vector paths, not copied third-party art. The submission form still
  requires Shuhan He to make the final rights warranty and accept Unicode's license.

## Verification

- Run placeholder and prohibited-language scans across all three Markdown sources and extracted PDF text.
- Confirm every proposal contains the current title, submitter, point of contact, date, keywords, category,
  four required example images, rights statement, all inclusion and exclusion factors, and other information.
- Confirm all image dimensions, color modes, and true two-tone black-and-white output.
- Render every PDF page to PNG with Poppler and inspect every page for clipping, bad breaks, unreadable images,
  and footer/page-number defects.
- Render and inspect the Microsoft DOCX and PDF; if DOCX conversion cannot be performed locally, generate the
  PDF independently and flag the DOCX layout for user review.

## Semantic version decision

This is a minor release because it adds two new complete proposal packets and materially revises the kidney
packet and Microsoft strategy artifacts. Bump the application/workspace version from `0.19.11` to `0.20.0`
and publish the proposal packet as `v1.2.0`.
