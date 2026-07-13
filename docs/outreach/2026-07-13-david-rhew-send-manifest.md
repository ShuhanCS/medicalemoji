# David Rhew send manifest

**Status:** Prepared and verified; not sent

**From:** `shuhan@conductscience.com`

**To:** `david.rhew@microsoft.com`
**Subject:** Medical Emoji submissions and final UTC discussion paper

The recipient address is confirmed in the June 30, 2026 Microsoft introduction thread. The ConductScience
Gmail sender has been authenticated by the local send script, which refuses to send from any account other
than `shuhan@conductscience.com`.

## Email body

Use:

`docs/outreach/2026-07-13-david-rhew-send-email.txt`

## Attach these four files

1. `output/pdf/2026-07-13-health-related-emoji-coverage-l2-submission.pdf`
   - Three-page final UTC/L2-format submission document.
   - Names David Rhew, Heena Purohit, and Shuhan He as authors.
   - Unicode will assign the official L2 number only after accepting the document into its public register.
2. `output/pdf/2026-07-13-medical-emoji-submission-options-packet.pdf`
   - Ninety-page bookmarked packet.
   - Contains the external decision brief and all 15 current working proposal PDFs.
   - The cover distinguishes planned, alternate, evidence-gated, draft, and later-cycle concepts.
3. `output/pdf/2026-07-13-who-can-help-with-medical-emoji-review.pdf`
   - One-page Microsoft-only Unicode routing contact map.
   - Lists public Microsoft roles, Unicode roles, and what each person does at Unicode.
4. `output/zip/2026-07-13-medical-emoji-potential-submissions-pdfs.zip`
   - Contains exactly the 15 individual proposal PDFs and no other file type.
   - Status-aware filenames distinguish planned-after-revision, alternate, evidence-incomplete, review,
     working-draft, and later-cycle concepts.

Do not attach the v7 deck, the separate product/legal discussion guide, or the older multi-file email draft.
Do not file the paper publicly with Unicode until David Rhew and Heena Purohit confirm the text and their
authorship and Microsoft's standards team confirms the appropriate contributor-license and submission route.

## Verified send command

Run once with `--dry-run`, inspect the sender, recipient, subject, and attachment count, then remove only
`--dry-run` if Shuhan has approved live sending:

```powershell
python "C:\Users\Shuha\projects\codex-config\scripts\send-conductscience-gmail.py" `
  --to "david.rhew@microsoft.com" `
  --subject "Medical Emoji submissions and final UTC discussion paper" `
  --body-file "C:\Users\Shuha\shuputerdesktop\medicalemoji\.worktrees\eligible-2026-slate\docs\outreach\2026-07-13-david-rhew-send-email.txt" `
  --attachment "C:\Users\Shuha\shuputerdesktop\medicalemoji\.worktrees\eligible-2026-slate\output\pdf\2026-07-13-health-related-emoji-coverage-l2-submission.pdf" `
  --attachment "C:\Users\Shuha\shuputerdesktop\medicalemoji\.worktrees\eligible-2026-slate\output\pdf\2026-07-13-medical-emoji-submission-options-packet.pdf" `
  --attachment "C:\Users\Shuha\shuputerdesktop\medicalemoji\.worktrees\eligible-2026-slate\output\pdf\2026-07-13-who-can-help-with-medical-emoji-review.pdf" `
  --attachment "C:\Users\Shuha\shuputerdesktop\medicalemoji\.worktrees\eligible-2026-slate\output\zip\2026-07-13-medical-emoji-potential-submissions-pdfs.zip" `
  --dry-run
```
