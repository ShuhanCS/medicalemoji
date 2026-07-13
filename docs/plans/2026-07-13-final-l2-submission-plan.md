# Final health-coverage L2 submission plan

**Date:** 2026-07-13

**Audience:** David Rhew, Heena Purohit, Microsoft standards reviewers, and the Unicode Technical Committee

## Objective

Replace the Microsoft review draft in the Rhew send package with a direct, L2-format UTC submission paper.
The paper will name David Rhew, Heena Purohit, and Shuhan He as authors, contain no status label, and ask the
UTC to refer the questions to the Emoji Standard & Research Working Group.

## Deliverables

1. Add a canonical Markdown, DOCX, and PDF submission set under
   `docs/proposals/utc-health-category/health-related-emoji-coverage-l2-submission.*`.
2. Use only four visible first-page fields: title, source/authors, date, and requested action.
3. Remove review-stage phrasing, Microsoft approval conditions, draft labels, and status fields from the
   paper and its PDF metadata.
4. Replace the first Rhew attachment with
   `output/pdf/2026-07-13-health-related-emoji-coverage-l2-submission.pdf`.
5. Update the email, send manifest, packet builder, README, handoff, and UTC-document README so the canonical
   L2-ready document is easy to find and the earlier variants are clearly archival.

## Important distinction

The authors can finalize the submission PDF, but they cannot assign an official `L2/26-nnn` number. Unicode
assigns that number after the PDF is submitted and accepted into the document register. Until then, the file
is the final L2-format submission document rather than a numbered Unicode L2 document.

## Verification

- Build both DOCX and PDF from the canonical Markdown source.
- Confirm the final PDF contains all three authors and no occurrence of `status`, `draft`, `if submitted`, or
  an unassigned L2 number.
- Confirm fonts are embedded, links resolve, metadata is final, and every page renders cleanly.
- Run the ConductScience email dry run with the renamed attachment and exactly three files.
- Apply a final humanizer pass to the external prose.

## Version decision

Advance the project from `0.27.0` to `0.28.0`. This release promotes a review artifact to a canonical external
submission document and changes the send package. The individual emoji proposal release remains `v1.7.0`.
