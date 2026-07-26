"""Render a submission markdown file to PDF via Chrome headless.

Usage:
    python scripts/make_submission_pdf.py submissions/v0.13.4/v0.13.4_kidney_emoji_proposal_SUBMIT.md

Writes the PDF next to the markdown file with the same basename.
Relative image paths resolve against the markdown file's directory.
Bare URLs are turned into clickable links.
"""

import re
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path

import markdown

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = """
@page {
    size: letter;
    margin: 1in;
    @bottom-center { content: counter(page) " of " counter(pages); font-family: Helvetica, Arial, sans-serif; font-size: 9pt; color: #666; }
}
* { box-sizing: border-box; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #111; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 16pt; }
h2 { font-size: 14pt; margin: 18pt 0 8pt; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 13pt 0 6pt; break-after: avoid; }
h4 { font-size: 10.5pt; margin: 12pt 0 6pt; break-after: avoid; }
p { margin: 0 0 8pt; break-inside: avoid; orphans: 3; widows: 3; }
a { color: #1a4fd6; text-decoration: none; overflow-wrap: anywhere; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f3f3f3; padding: 0 2pt; border-radius: 2pt; }
img { break-inside: avoid; max-width: 100%; max-height: 7.5in; }
p:has(+ p > img) { break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 12pt; break-inside: avoid; font-size: 9.5pt; }
th, td { border: 0.5pt solid #999; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #f0f0f0; }
.page-break { break-before: page; }
"""


def main() -> int:
    md_path = Path(sys.argv[1]).resolve()
    text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    document_title = title_match.group(1).strip() if title_match else md_path.stem

    # Linkify bare URLs (not already inside markdown link/image syntax).
    text = re.sub(r"(?<![<(\]])(https?://\S+)", r"<\1>", text)

    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    html_document = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{escape(document_title)}</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )

    # HTML must live in the markdown's directory so relative image paths resolve.
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", dir=md_path.parent, delete=False, encoding="utf-8"
    ) as f:
        f.write(html_document)
        html_path = Path(f.name)

    pdf_path = md_path.with_suffix(".pdf")
    try:
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                html_path.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
    finally:
        html_path.unlink(missing_ok=True)

    print(pdf_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
