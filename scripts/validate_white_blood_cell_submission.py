"""Preflight the canonical White Blood Cell proposal packet before filing."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-dir", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    package_dir = parse_args().package_dir.resolve()
    proposal_dir = package_dir / "white-blood-cell"
    proposal = proposal_dir / "white-blood-cell_emoji_proposal_SUBMIT.md"
    pdf = proposal.with_suffix(".pdf")

    proposal_text = proposal.read_text(encoding="utf-8") if proposal.is_file() else ""

    # Evidence filenames carry their capture date, so they change whenever a
    # capture is redone. Deriving them from the proposal's own image references
    # keeps this check from going stale and, more usefully, fails when the
    # document points at a file that is not on disk.
    referenced = [
        proposal_dir / target
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", proposal_text)
        if not target.startswith(("http://", "https://"))
    ]

    required = [
        package_dir / "VERSION",
        package_dir / "manifest.md",
        package_dir / "CHANGELOG.md",
        package_dir / "ARTWORK-LICENSE.md",
        proposal,
        pdf,
        *referenced,
        proposal_dir / "validation/computer-validation.json",
        proposal_dir / "comparisons/white-blood-cell_comparison-board_color_2026-07-26.png",
        proposal_dir / "comparisons/white-blood-cell_comparison-board_black_2026-07-26.png",
    ]
    missing = [str(path.relative_to(package_dir)) for path in required if not path.is_file()]
    if missing:
        raise ValueError("missing required files:\n- " + "\n- ".join(missing))

    # Every one of the five required sources must actually appear in the PDF.
    for source in (
        "google_search",
        "google_video_search",
        "google_trends_web",
        "google_trends_image",
        "google_books_ngram",
    ):
        if not any(source in path.name for path in referenced):
            raise ValueError(f"proposal does not embed any {source} evidence screenshot")

    if any("DRAFT" in path.name for path in referenced):
        raise ValueError("proposal references a DRAFT evidence file")

    version = (package_dir / "VERSION").read_text(encoding="utf-8").strip()
    expected_version = package_dir.name.removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError(f"VERSION must be semantic, found {version!r}")
    if version != expected_version:
        raise ValueError(
            f"VERSION {version!r} must match package directory {package_dir.name!r}"
        )

    # The v1.18.0 draft quoted "about 125 results" for a query that returns
    # about 880,000,000. Every count the proposal states must match a figure
    # that the capture log confirmed across repeated loads.
    for log_path in sorted(proposal_dir.glob("evidence/frequency/*_google_recapture_log_*.json")):
        for record in json.loads(log_path.read_text(encoding="utf-8"))["records"]:
            if record["count"] is None:
                raise ValueError(f"{log_path.name}: {record['label']} has no confirmed count")
            if f"{record['count']:,}" not in proposal_text:
                raise ValueError(
                    f"proposal does not state the confirmed {record['label']} count "
                    f"{record['count']:,} (from {log_path.name})"
                )

    if "{{" in proposal_text or "}}" in proposal_text:
        raise ValueError("proposal contains unresolved placeholders")
    for forbidden in (
        "TODO",
        "TBD",
        "BLOCKED",
        "not yet",
        "must remain",
        "IoU",
        "difference hash",
        "dHash",
        "threshold",
        "machine-readable",
        "pinned comparator",
        "computer-validation.md",
    ):
        if forbidden.casefold() in proposal_text.casefold():
            raise ValueError(f"proposal contains reviewer-facing workflow language: {forbidden}")

    validation = json.loads(
        (proposal_dir / "validation/computer-validation.json").read_text(encoding="utf-8")
    )
    if not validation.get("overall_pass"):
        raise ValueError("computer validation does not pass")

    sizes = {
        "white-blood-cell_color_18x18_SUBMIT.png": (18, 18),
        "white-blood-cell_color_72x72_SUBMIT.png": (72, 72),
        "white-blood-cell_bw_18x18_SUBMIT.png": (18, 18),
        "white-blood-cell_bw_72x72_SUBMIT.png": (72, 72),
    }
    for filename, expected in sizes.items():
        with Image.open(proposal_dir / "images" / filename) as image:
            if image.size != expected:
                raise ValueError(f"{filename}: expected {expected}, found {image.size}")

    if pdf.read_bytes()[:5] != b"%PDF-":
        raise ValueError("proposal PDF has an invalid header")

    print("White Blood Cell submission preflight: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
