"""Render docs/acep-press-kit/insights-and-post-copy.md to a styled HTML file
that Edge headless then prints to PDF (see the PowerShell step that follows).

Run: python scripts/build-acep-insights-pdf.py
Output: public/press/acep/medical-emoji-acep-insights.html
"""

import os
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "docs", "acep-press-kit", "insights-and-post-copy.md")
OUT_HTML = os.path.join(ROOT, "public", "press", "acep", "medical-emoji-acep-insights.html")

with open(MD, encoding="utf-8") as f:
    body = markdown.markdown(f.read(), extensions=["tables", "sane_lists"])

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
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Medical Emoji — Insights & Post Kit for ACEP</title>
<style>{CSS}</style></head><body>{body}</body></html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML: {OUT_HTML}")
