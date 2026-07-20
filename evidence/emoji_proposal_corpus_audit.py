"""Reproduce the repository's emoji-proposal corpus measurements.

This script deliberately separates measurements that can be reproduced from the
tracked text archive from PDF-object measurements that require downloading the
linked Unicode PDFs. It does not infer acceptance probability.

Examples:

    python evidence/emoji_proposal_corpus_audit.py
    python evidence/emoji_proposal_corpus_audit.py --pdf-dir tmp/pdfs/rubric-audit

The historical 29-document comparison cannot be reproduced because neither its
membership manifest nor its extracted documents were committed to the repository.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACCEPTED_DIR = ROOT / "docs/proposals/reference-winners-2020-2024"
DRAFT_DIR = ROOT / "docs/proposals/archive-2020-emojination-drafts"


FEATURES = {
    "mentions_exclusion": r"\bexclusion\b",
    "answers_open_ended": r"open[- ]ended",
    "answers_already_representable": r"already represent",
    "answers_overly_specific": r"overly specific",
    "answers_transient": r"\btransient\b",
    "answers_faulty_comparison": r"faulty comparison",
    "literal_sort_location": r"sort\s+location",
    "normalized_sort_location_or_order": r"sort\s+(?:location|order)",
    "mentions_google_trends": r"google\s+trends|trends\.google",
    "mentions_trends_anywhere": r"\btrends\b",
    "mentions_elephant": r"\belephant\b",
    "mentions_petition_instagram_or_twitter": r"petition|instagram|twitter",
    "mentions_broader_social_terms": (
        r"petition|social media|instagram|twitter|facebook|hashtag"
    ),
    "mentions_cause_terms": (
        r"\bawareness\b|\bstigma\b|\badvocacy\b|\bdeserves? representation\b"
    ),
}


def median(values: list[int]) -> float | int:
    value = statistics.median(values)
    return int(value) if value == int(value) else value


def accepted_documents() -> list[dict]:
    rows = []
    for path in sorted(ACCEPTED_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        words = re.search(r"Text-layer word count:\s*([0-9,]+)", text)
        doc_id = re.search(r"Unicode document \*\*(L2/[^*]+)\*\*", text)
        source = re.search(r"Source PDF: <(https://[^>]+)>", text)
        authors = re.search(r"Authors:\s*(.+?)\.", text)
        if not all((words, doc_id, source, authors)):
            continue
        lowered = text.casefold()
        rows.append(
            {
                "document_id": doc_id.group(1),
                "file": path.relative_to(ROOT).as_posix(),
                "source_url": source.group(1),
                "authors": authors.group(1),
                "extractable_words": int(words.group(1).replace(",", "")),
                "explicit_na_count": len(
                    re.findall(r"\bn\s*/\s*a\b", lowered, flags=re.IGNORECASE)
                ),
                "features": {
                    key: bool(re.search(pattern, lowered, flags=re.IGNORECASE))
                    for key, pattern in FEATURES.items()
                },
            }
        )
    return rows


def draft_documents() -> list[dict]:
    rows = []
    for path in sorted(DRAFT_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.casefold()
        rows.append(
            {
                "file": path.relative_to(ROOT).as_posix(),
                "markdown_token_count": len(re.findall(r"\b[\w'-]+\b", text)),
                "explicit_na_count": len(
                    re.findall(r"\bn\s*/\s*a\b", lowered, flags=re.IGNORECASE)
                ),
                "features": {
                    key: bool(re.search(pattern, lowered, flags=re.IGNORECASE))
                    for key, pattern in FEATURES.items()
                },
            }
        )
    return rows


def summarize_text(rows: list[dict], word_key: str, word_measurement: str) -> dict:
    return {
        "document_count": len(rows),
        "word_measurement": word_measurement,
        "median_words": median([row[word_key] for row in rows]),
        "median_explicit_na_count": median(
            [row["explicit_na_count"] for row in rows]
        ),
        "feature_document_counts": {
            key: sum(row["features"][key] for row in rows) for key in FEATURES
        },
    }


def pdf_metrics(rows: list[dict], pdf_dir: Path) -> dict:
    measurements = []
    by_name = {Path(row["file"]).stem: row for row in rows}
    for stem, row in by_name.items():
        path = pdf_dir / f"{stem}.pdf"
        if not path.exists():
            continue
        info = subprocess.run(
            ["pdfinfo", str(path)],
            capture_output=True,
            check=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        ).stdout
        image_list = subprocess.run(
            ["pdfimages", "-list", str(path)],
            capture_output=True,
            check=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        ).stdout
        pages_match = re.search(r"^Pages:\s+(\d+)", info, flags=re.MULTILINE)
        image_rows = [
            line.split()
            for line in image_list.splitlines()
            if re.match(r"^\s*\d+\s+\d+\s+", line)
        ]
        measurements.append(
            {
                "document_id": row["document_id"],
                "pages": int(pages_match.group(1)),
                "all_pdf_image_objects": len(image_rows),
                "objects_with_type_image": sum(
                    parts[2] == "image" for parts in image_rows
                ),
                "unique_underlying_image_object_ids": len(
                    {
                        (parts[10], parts[11])
                        for parts in image_rows
                        if len(parts) > 11 and parts[2] == "image"
                    }
                ),
            }
        )
    if not measurements:
        return {"document_count": 0}
    return {
        "document_count": len(measurements),
        "median_pages": median([row["pages"] for row in measurements]),
        "median_all_pdf_image_objects": median(
            [row["all_pdf_image_objects"] for row in measurements]
        ),
        "median_objects_with_type_image": median(
            [row["objects_with_type_image"] for row in measurements]
        ),
        "median_unique_underlying_image_object_ids": median(
            [row["unique_underlying_image_object_ids"] for row in measurements]
        ),
        "warning": (
            "PDF image-object counts are implementation details, not counts of "
            "meaningful screenshots. Masks, duplicated objects, and scanned pages "
            "produce materially different totals."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pdf-dir",
        type=Path,
        help="Optional directory containing PDFs named after the accepted markdown files.",
    )
    args = parser.parse_args()

    accepted = accepted_documents()
    drafts = draft_documents()
    result = {
        "schema_version": "1.0.0",
        "accepted_text_archive": summarize_text(
            accepted, "extractable_words", "stored pdftotext text-layer count"
        ),
        "medical_emoji_declined_draft_archive": summarize_text(
            drafts, "markdown_token_count", "regex token count over tracked markdown"
        ),
        "historical_29_document_comparison": {
            "reproducible": False,
            "reason": (
                "No cohort manifest, source documents, extracted texts, or analysis "
                "code for the 29 documents exists in repository history."
            ),
        },
    }
    if args.pdf_dir:
        result["accepted_pdf_archive"] = pdf_metrics(accepted, args.pdf_dir)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
