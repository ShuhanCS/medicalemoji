# Support Letter Recovery And Linking Plan - 2026-05-13

## Goal

Recover the old WordPress support-letter links for all currently listed Medical Emoji candidate pages and make the new Vercel pages link to stable local copies where possible.

## Scope

- Query old WordPress page content on `192.249.115.15` for current candidate pages.
- Map each supporter card to the old `cta_1_url` value.
- Preserve old WordPress-linked documents in `public/documents/`.
- Convert image-only kidney letter assets to PDFs for public linking.
- Update the Vercel supporter cards to link to recovered documents.

## Old WordPress Pages Checked

- `https://medicalemoji.org/kidney/`
- `https://medicalemoji.org/liver/`
- `https://medicalemoji.org/stomach/`
- `https://medicalemoji.org/intestine/`
- `https://medicalemoji.org/spine/`
- `https://medicalemoji.org/wbc/`
- `https://medicalemoji.org/ekg/`
- `https://medicalemoji.org/the-blood-bag-emoji/`
- `https://medicalemoji.org/the-pill-pack-emoji/`
- `https://medicalemoji.org/the-weight-scale-emoji/`

Access command:

```powershell
curl.exe -k --resolve medicalemoji.org:443:192.249.115.15 "https://medicalemoji.org/wp-json/wp/v2/pages?slug=kidney"
```

## Findings

- Kidney had 12 supporter links on the old page.
- Liver had AGA, ASGE, and Hepatology links.
- Stomach had AGA and ASGE links.
- Intestine had AGA and ASGE links.
- Spine had a Spine Journal article link.
- WBC, EKG, Blood Bag, Pill Pack, and Weight Scale pages did not expose support-letter links in the old page content.
- The old AGA `gastro.org` PDF URL is now returning 404, but the old WordPress media library already contains signed AGA PDF copies under `public/documents/`.

## Local Link Strategy

- Use local PDFs for recovered letters whenever available.
- Use PDF conversions for old image-only kidney letters.
- Keep external journal article links where the old page linked to an article rather than a support letter.
- Keep the Women Nephrology India link as DOCX until a faithful PDF conversion is available.

## Status

- Done: old page supporter URLs extracted.
- Done: image-only kidney letters converted to PDF.
- Done: supporter cards linked in the current Vercel app data.
- Next: manually QA document rendering in deployed Vercel after push.
