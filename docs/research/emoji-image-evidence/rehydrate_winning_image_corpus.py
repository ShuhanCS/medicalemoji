#!/usr/bin/env python3
"""Fetch official proposal PDFs and render the annotated sample page for local study.

The rendered images are intentionally written outside the repository by default:
they are research copies of third-party proposal documents, not project assets.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import urllib.request
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path(__file__).with_name("unicode-winning-image-corpus.v1.json"),
        help="Path to the versioned corpus manifest.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="External local directory for fetched PDFs and rendered page PNGs.",
    )
    parser.add_argument("--dpi", type=int, default=144)
    args = parser.parse_args()

    corpus = json.loads(args.corpus.read_text(encoding="utf-8"))
    pdf_dir = args.output_dir / "pdf"
    page_dir = args.output_dir / "page-render"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)

    for record in corpus["records"]:
        stem = record["id"].replace("/", "-").lower()
        pdf_path = pdf_dir / f"{stem}.pdf"
        page_prefix = page_dir / stem
        png_path = page_dir / f"{stem}.png"
        if not pdf_path.exists():
            print(f"Downloading {record['id']} from {record['source_pdf']}")
            urllib.request.urlretrieve(record["source_pdf"], pdf_path)
        if not png_path.exists():
            print(f"Rendering {record['id']} page {record['sample_page']}")
            subprocess.run(
                [
                    "pdftoppm",
                    "-f",
                    str(record["sample_page"]),
                    "-l",
                    str(record["sample_page"]),
                    "-singlefile",
                    "-r",
                    str(args.dpi),
                    "-png",
                    str(pdf_path),
                    str(page_prefix),
                ],
                check=True,
            )

    print(f"Rehydrated {len(corpus['records'])} official source pages in {args.output_dir}")


if __name__ == "__main__":
    main()
