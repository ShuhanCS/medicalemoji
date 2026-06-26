"""Build the AMIA outreach PDFs.

Two artifacts:
  1. One-pager  — docs/outreach/2026-06-25-amia-briefing.html is a hand-authored,
                  visual single page (committed as the source of truth). Rendered as-is.
  2. Draft letter — generated from 2026-06-25-amia-medical-emoji-letter-DRAFT.md into a
                  styled HTML, then to PDF. HTML comment blocks (finalization notes) are stripped.

Both HTMLs are printed to PDF with Microsoft Edge headless (the browse daemon isn't built here).

Run: python scripts/build-amia-outreach-pdfs.py
"""

import os
import re
import shutil
import subprocess
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "outreach")

BRIEFING_HTML = os.path.join(OUT, "2026-06-25-amia-briefing.html")          # hand-authored
LETTER_MD = os.path.join(OUT, "2026-06-25-amia-medical-emoji-letter-DRAFT.md")
LETTER_HTML = LETTER_MD.replace(".md", ".html")                            # transient

LETTER_CSS = """
@page { size: Letter; margin: 0.9in 0.85in; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Arial, sans-serif; color: #1f2430; font-size: 11pt;
       line-height: 1.5; max-width: 7in; margin: 0 auto; }
h1 { font-size: 21pt; color: #1a2a6c; border-bottom: 3px solid #3452ff; padding-bottom: 8px; }
h2 { font-size: 14pt; color: #1a2a6c; margin-top: 26px; }
p { margin: 8px 0; }
strong { color: #1a2a6c; }
a { color: #3452ff; text-decoration: none; word-break: break-word; }
"""


def build_letter_html():
    with open(LETTER_MD, encoding="utf-8") as f:
        src = re.sub(r"<!--.*?-->", "", f.read(), flags=re.DOTALL)
    body = markdown.markdown(src, extensions=["tables", "sane_lists"])
    html = (f"""<!doctype html><html lang="en"><head><meta charset="utf-8">"""
            f"""<title>Draft Letter of Support — AMIA to the Unicode Consortium</title>"""
            f"""<style>{LETTER_CSS}</style></head><body>{body}</body></html>""")
    with open(LETTER_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML: {LETTER_HTML}")


def find_edge():
    for p in (
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ):
        if os.path.exists(p):
            return p
    edge = shutil.which("msedge") or shutil.which("chrome")
    if not edge:
        raise SystemExit("No Edge/Chrome found for headless PDF printing.")
    return edge


def render_pdf(edge, html_path):
    pdf_path = html_path.replace(".html", ".pdf")
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    uri = "file:///" + html_path.replace("\\", "/")
    subprocess.run([edge, "--headless", "--disable-gpu",
                    f"--print-to-pdf={pdf_path}", "--no-pdf-header-footer", uri],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"PDF:  {pdf_path}  ({os.path.getsize(pdf_path):,} bytes)")
    return pdf_path


if __name__ == "__main__":
    build_letter_html()
    edge = find_edge()
    render_pdf(edge, BRIEFING_HTML)
    render_pdf(edge, LETTER_HTML)
    os.remove(LETTER_HTML)   # letter HTML is transient; md is the source
    print("Done. Briefing HTML is the committed source for the one-pager.")
