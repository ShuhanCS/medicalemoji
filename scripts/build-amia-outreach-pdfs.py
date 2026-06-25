"""Render the AMIA outreach one-pager and draft letter to styled HTML, which
Edge headless then prints to PDF (see the PowerShell step in build-amia-outreach.ps1).

Run: python scripts/build-amia-outreach-pdfs.py
Outputs: docs/outreach/2026-06-25-amia-briefing.html
         docs/outreach/2026-06-25-amia-medical-emoji-letter-DRAFT.html
"""

import os
import re
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "outreach")

DOCS = [
    ("2026-06-25-amia-briefing.md", "Medical Emoji — A Briefing for AMIA"),
    ("2026-06-25-amia-medical-emoji-letter-DRAFT.md",
     "Draft Letter of Support — AMIA to the Unicode Consortium"),
]

CSS = """
@page { size: Letter; margin: 0.9in 0.85in; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Arial, sans-serif; color: #1f2430; font-size: 11pt;
       line-height: 1.5; max-width: 7in; margin: 0 auto; }
h1 { font-size: 21pt; color: #1a2a6c; border-bottom: 3px solid #3452ff; padding-bottom: 8px; }
h2 { font-size: 14pt; color: #1a2a6c; margin-top: 26px; border-bottom: 1px solid #e5e7eb; padding-bottom: 4px; }
h3 { font-size: 12pt; color: #ff1053; margin-top: 18px; margin-bottom: 4px; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 10pt; }
th, td { border: 1px solid #d6d9e0; padding: 7px 10px; text-align: left; vertical-align: top; }
th { background: #f1f3f9; color: #1a2a6c; }
blockquote { margin: 8px 0; padding: 10px 16px; background: #f7f8fc;
             border-left: 4px solid #3452ff; color: #333a48; }
code { background: #eef0f6; padding: 1px 5px; border-radius: 4px; font-size: 10pt; }
a { color: #3452ff; text-decoration: none; word-break: break-word; }
strong { color: #1f2430; }
hr { border: none; border-top: 1px solid #e5e7eb; margin: 18px 0; }
"""

for md_name, title in DOCS:
    md_path = os.path.join(OUT, md_name)
    with open(md_path, encoding="utf-8") as f:
        src = f.read()
    # Drop HTML comment blocks (finalization notes) so they never render.
    src = re.sub(r"<!--.*?-->", "", src, flags=re.DOTALL)
    body = markdown.markdown(src, extensions=["tables", "sane_lists"])
    html = (f"""<!doctype html><html lang="en"><head><meta charset="utf-8">"""
            f"""<title>{title}</title><style>{CSS}</style></head>"""
            f"""<body>{body}</body></html>""")
    out_html = os.path.join(OUT, md_name.replace(".md", ".html"))
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML: {out_html}")
