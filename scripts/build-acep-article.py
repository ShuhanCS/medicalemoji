"""Render docs/acep-press-kit/article.md into:
  - public/press/acep/medical-emoji-acep-article.html  (styled, hosted preview)
  - build/acep/article-body.html                       (paste-ready body for a CMS)

A PowerShell step then prints the styled HTML to PDF via Edge.

Run: python scripts/build-acep-article.py
"""

import os
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "docs", "acep-press-kit", "article.md")
OUT_HTML = os.path.join(ROOT, "public", "press", "acep", "medical-emoji-acep-article.html")
OUT_BODY = os.path.join(ROOT, "docs", "acep-press-kit", "article-body.html")

with open(MD, encoding="utf-8") as f:
    body = markdown.markdown(f.read(), extensions=["tables", "sane_lists"])

# Paste-ready body: absolute links already; ensure they stay intact.
os.makedirs(os.path.dirname(OUT_BODY), exist_ok=True)
with open(OUT_BODY, "w", encoding="utf-8") as f:
    f.write(body)

CSS = """
@page { size: Letter; margin: 0.9in 0.85in; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; color: #1f2430; font-size: 12pt;
       line-height: 1.6; max-width: 7in; margin: 0 auto; }
h1 { font-family: 'Segoe UI', Arial, sans-serif; font-size: 23pt; color: #1a2a6c;
     line-height: 1.15; border-bottom: 3px solid #3452ff; padding-bottom: 10px; }
h1 + p em, body > p:first-of-type em { color: #5b6475; }
h2 { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15pt; color: #1a2a6c; margin-top: 26px; }
li { margin: 5px 0; }
a { color: #3452ff; text-decoration: none; }
hr { border: 0; border-top: 1px solid #e5e7eb; margin: 26px 0; }
strong { color: #1f2430; }
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ACEP Supports Standardized Medical Emoji</title>
<style>{CSS}</style></head><body>{body}</body></html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("article HTML:", OUT_HTML)
print("paste body  :", OUT_BODY)
