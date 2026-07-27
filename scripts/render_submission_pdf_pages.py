"""Render a submission PDF to PNG pages with Poppler's Cairo backend.

The Cairo backend provides a deterministic primary rendering path for visual
inspection. The script verifies that the renderer produced exactly one PNG for
every PDF page.

Usage:
    python scripts/render_submission_pdf_pages.py \
        submissions/v1.13.0/white-blood-cell/white-blood-cell_emoji_proposal_SUBMIT.pdf \
        tmp/pdfs/white-blood-cell-v1.13.0
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=150)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf = args.pdf.resolve()
    output_dir = args.output_dir.resolve()
    renderer = shutil.which("pdftocairo")
    if renderer is None:
        raise SystemExit("pdftocairo is required but was not found on PATH")

    output_dir.mkdir(parents=True, exist_ok=True)
    for stale_page in output_dir.glob("page-*.png"):
        stale_page.unlink()

    subprocess.run(
        [renderer, "-png", "-r", str(args.dpi), str(pdf), str(output_dir / "page")],
        check=True,
        timeout=120,
    )

    expected_pages = len(PdfReader(pdf).pages)
    rendered_pages = sorted(output_dir.glob("page-*.png"))
    if len(rendered_pages) != expected_pages:
        raise SystemExit(
            f"rendered {len(rendered_pages)} pages; expected {expected_pages}"
        )

    print(f"Rendered {len(rendered_pages)} pages to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
