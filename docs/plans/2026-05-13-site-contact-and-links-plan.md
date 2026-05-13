# Medical Emoji Site Contact and Links Plan

Date: 2026-05-13

## Goal

Update the Medical Emoji site so the public polish items match the live site needs:

- Use the anatomical-heart logo image as the browser favicon.
- Point press cards to the specific press article URLs.
- Replace the client-side personal Gmail `mailto:` contact form with a captcha-protected server submission to `info@conductscience.com`.
- Add visible citation links to the EbVAS JAMA paper and its Google Scholar citing-articles list on the Visual Analogue Scale page.

## Implementation

- Rebuild `src/app/favicon.ico` from `public/images/misc/cropped-anatomical-heart.png`.
- Update `src/data/press.ts` with article-level URLs supplied for Harvard Medical School, Healio, WCVB Boston, Boston Globe, JAMA, and The Verge.
- Add a Next API route at `src/app/api/contact/route.ts`.
- Use Cloudflare Turnstile for captcha verification via `NEXT_PUBLIC_TURNSTILE_SITE_KEY` and `TURNSTILE_SECRET_KEY`.
- Send email through the Resend HTTP API via `RESEND_API_KEY`, with `CONTACT_FORM_FROM` configured to a verified sender.
- Keep `CONTACT_FORM_TO` optional and default it to `info@conductscience.com`.
- Add a citation section to `src/app/visual-analogue-scale/page.tsx` with the JAMA DOI link and Google Scholar citing-articles link.

## Verification

- Validate the generated ICO structure.
- Run `npm run lint`.
- Run `npm run build`.
