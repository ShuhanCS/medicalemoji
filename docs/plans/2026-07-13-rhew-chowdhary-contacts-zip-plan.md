# David Rhew Unicode handoff plan

## Audience and purpose

This package is for David Rhew and the Microsoft and Unicode contacts he may approach. It should let him
understand the two official review routes, forward a concise note to Vishal Chowdhary, and inspect every
current proposal option without suggesting that all 15 are ready to file.

## Deliverables

1. A single shareable handoff page with links to the final UTC paper, the proposal packet, the contact map,
   the PDF-only archive, and the two email drafts.
2. A natural-language draft from David Rhew to Vishal Chowdhary asking for Microsoft routing help rather
   than a preferred Unicode outcome.
3. An accessible text contact map and a matching PDF showing:
   - confirmed current Unicode leadership relevant to emoji and UTC review;
   - Microsoft-affiliated people supported by current public sources;
   - Microsoft member, standards, design, font, and accessibility roles that Vishal should identify;
   - the separate official routes for emoji forms and UTC documents.
4. A ZIP containing only the 15 current proposal PDFs. Status-aware filenames will retain the planned,
   alternate, evidence-gated, draft, and later-cycle labels; the shareable handoff page will provide the
   readable index. The UTC paper and the combined options packet will remain outside the ZIP because neither
   is an individual emoji submission.

## Accuracy rules

- Use current official Unicode sources for public roles and meeting participation.
- Do not infer Microsoft's private delegate assignments from meeting attendance.
- State that the Unicode Board does not select emoji and that ESR recommendations remain subject to UTC
  action.
- Keep the final UTC paper separate from the individual emoji proposals.
- Do not describe a working draft as filing-ready.

## Verification

- Build generated files reproducibly from a checked-in script.
- Confirm every generated PDF opens, has extractable text, and uses embedded fonts.
- Render and inspect every page of the new contact map and archive index, including a grayscale check of the
  contact map.
- Confirm the ZIP contains exactly the 15 expected proposal PDFs, passes integrity testing, and preserves
  each source PDF byte-for-byte.
- Review all external prose for natural voice and remove internal planning language.

## Version decision

Advance the workspace package from `0.28.0` to `0.29.0`. The proposal release remains `v1.7.0` because the
individual proposal PDFs are being packaged, not revised.
