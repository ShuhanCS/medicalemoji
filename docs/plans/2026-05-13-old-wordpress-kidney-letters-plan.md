# Old WordPress Kidney Letter Recovery Plan - 2026-05-13

## Goal

Recover the kidney emoji support letters that were referenced by the current Medical Emoji kidney page but were originally hosted on the old WordPress site.

## Scope

- Identify whether an old WordPress copy of `medicalemoji.org` is still reachable.
- Recover support-letter assets for the kidney campaign.
- Save recovered assets in the repo so the renewed proposal does not depend on the old server.
- Document exact source URLs and access method.

## Findings

- Current public DNS for `medicalemoji.org` resolves to Vercel:
  - `medicalemoji.org` A records: `76.76.21.21`, `76.76.21.61`
  - nameservers: `dns1.registrar-servers.com`, `dns2.registrar-servers.com`
- The old WordPress site is still reachable on GliaServer/InMotion at `192.249.115.15` when the `Host` is forced to `medicalemoji.org`.
- The old WordPress page path is `https://medicalemoji.org/kidney/`, not the current static route `https://medicalemoji.org/emoji/kidney`.
- The old REST media endpoint works when forced to the old IP:
  - `https://medicalemoji.org/wp-json/wp/v2/media?per_page=100&search=kidney`

## Recovery Method

Use `curl --resolve` so TLS/SNI and the HTTP Host header still say `medicalemoji.org` while the TCP connection goes to the old server:

```powershell
curl.exe -k --resolve medicalemoji.org:443:192.249.115.15 "https://medicalemoji.org/kidney/"
curl.exe -k --resolve medicalemoji.org:443:192.249.115.15 "https://medicalemoji.org/wp-json/wp/v2/media?per_page=100&search=kidney"
```

## Deliverables

- `public/documents/kidney-support-letters/` - recovered old WordPress image/asset originals.
- `docs/proposals/kidney-emoji-2026/old-wordpress-letter-recovery.md` - source map and access notes.
- `docs/proposals/kidney-emoji-2026/support-letter-inventory.md` - coalition letter inventory.
- `docs/proposals/kidney-emoji-2026/previous-proposal-review.md` - old proposal review.
- `docs/proposals/kidney-emoji-2026/proposal-working-draft.md` - current working proposal draft.

## Status

- Done: Located the old WordPress copy on `192.249.115.15`.
- Done: Recovered missing support-letter image assets.
- Done: Documented the asset map and proposal implications.
- Next: Review the recovered image letters manually for signer/title extraction and use them as supplementary coalition material in the renewed PDF.
