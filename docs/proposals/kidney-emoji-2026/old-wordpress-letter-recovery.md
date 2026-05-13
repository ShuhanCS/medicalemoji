# Old WordPress Letter Recovery

Date: 2026-05-13

## Practical Finding

The missing kidney support-letter assets were on the old WordPress version of `medicalemoji.org`. The current public site is served from Vercel, but the old WordPress copy still responds on the GliaServer/InMotion IP `192.249.115.15` when the request is sent with `medicalemoji.org` as the host.

Current DNS:

- `https://medicalemoji.org/` resolves to Vercel A records `76.76.21.21` and `76.76.21.61`.
- The old WordPress copy is not reached by normal public DNS.

Old WordPress access pattern:

```powershell
curl.exe -k --resolve medicalemoji.org:443:192.249.115.15 "https://medicalemoji.org/kidney/"
curl.exe -k --resolve medicalemoji.org:443:192.249.115.15 "https://medicalemoji.org/wp-json/wp/v2/media?per_page=100&search=kidney"
```

The old WordPress kidney page is:

https://medicalemoji.org/kidney/

The current static kidney page is:

https://medicalemoji.org/emoji/kidney

## Recovered Files Saved In This Repo

These files were downloaded from the old WordPress media library and saved under:

`public/documents/kidney-support-letters/`

| Organization / asset | Recovered repo file | Old WordPress source URL |
| --- | --- | --- |
| ASDIN support letter image | `public/documents/kidney-support-letters/ASDIN.jpg` | https://medicalemoji.org/wp-content/uploads/2021/12/ASDIN.jpg |
| GlomCon support letter image | `public/documents/kidney-support-letters/Glomcon.jpg` | https://medicalemoji.org/wp-content/uploads/2021/12/Glomcon.jpg |
| Renal Physicians Association support letter image | `public/documents/kidney-support-letters/RPA.png` | https://medicalemoji.org/wp-content/uploads/2021/12/RPA.png |
| International Society of Nephrology support letter image | `public/documents/kidney-support-letters/ISN.png` | https://medicalemoji.org/wp-content/uploads/2022/01/ISN.png |
| International Society of Nephrology duplicate/export | `public/documents/kidney-support-letters/ISN-1.png` | https://medicalemoji.org/wp-content/uploads/2022/01/ISN-1.png |
| National Kidney Foundation support letter image | `public/documents/kidney-support-letters/NKF-1.png` | https://medicalemoji.org/wp-content/uploads/2022/01/NKF-1.png |
| National Kidney Foundation duplicate/export | `public/documents/kidney-support-letters/NKF-1-1.png` | https://medicalemoji.org/wp-content/uploads/2022/01/NKF-1-1.png |
| ASN long-form image export | `public/documents/kidney-support-letters/ASN_Long.png` | https://medicalemoji.org/wp-content/uploads/2022/01/ASN_Long.png |
| ASN long-form duplicate/export | `public/documents/kidney-support-letters/ASN_Long-1.png` | https://medicalemoji.org/wp-content/uploads/2022/01/ASN_Long-1.png |
| ASN long-form duplicate/export | `public/documents/kidney-support-letters/ASN_Long-2.png` | https://medicalemoji.org/wp-content/uploads/2022/01/ASN_Long-2.png |
| Kidney proposal art from old page | `public/documents/kidney-support-letters/kidneysnew2.png` | https://medicalemoji.org/wp-content/uploads/2022/01/kidneysnew2.png |
| Kidney menu/campaign art from old page | `public/documents/kidney-support-letters/6-kidneys.png` | https://medicalemoji.org/wp-content/uploads/2021/12/6-kidneys.png |

Important: the old source URLs above are real WordPress media URLs, but because public DNS now points at Vercel, direct browser access may not reach the old assets unless the request is forced to `192.249.115.15` or the assets are served from this repo/current site.

## Assets Already Present Before This Recovery

The repo already had these kidney support materials in `public/documents/`:

- `public/documents/21-12-17-Letter-to-the-Unicode-Consortium-about-the-Kidney-Emoji-3.pdf`
- `public/documents/AAKP-Kidney-Emoji-Letter-1.7.22.pdf`
- `public/documents/Kidney_Emoji_Letter-1.pdf`
- `public/documents/Kidney-Foundation-of-WNY-kidney-emoji-letter.pdf`
- `public/documents/NephJC_KidneyEmoji.pdf`
- `public/documents/The-Unicode-Consortium_Signed.pdf`
- `public/documents/Kidney-Emoji-WIN-Letter-Head-V4B-converted.docx`

## Server Notes

Infrastructure repo reference:

https://github.com/ShuhanCS/infrastructure/

The infrastructure repo records `medicalemoji.org` as a quality domain / Medical Emoji alternate domain, but it did not identify the WordPress asset path directly. The useful clue was server topology: `192.249.115.15` is the GliaServer/InMotion cPanel server. Forcing `medicalemoji.org` to that IP exposed the old WordPress site and media library.

Attempts to locate the same files by SSH filesystem search from the available shell account did not reveal a readable home-directory path. The HTTP/WordPress route is currently the reliable recovery path.
