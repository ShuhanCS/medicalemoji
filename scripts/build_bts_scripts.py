"""Build the behind-the-scenes video scripts as .docx files.

Each source markdown in docs/scripts/ holds one spoken paragraph per line, prefixed
with "He: ". Everything before the first "He: " line is editorial front matter and is
not carried into the .docx.

The output matches the format of BTSHeartEmoji_HeartMonth_02.2026_V4.docx: plain
default-styled paragraphs, no headings, no bullets, no em dashes.

Usage: python scripts/build_bts_scripts.py
"""

import zipfile
from datetime import datetime
from pathlib import Path

from docx import Document

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "docs" / "scripts"

# A .docx is a zip. Both the document properties and the zip entry timestamps default to
# the current time, so an unchanged script would produce different bytes on every build
# and churn in git. Pin both.
EPOCH = datetime(2000, 1, 1)
ZIP_DATE_TIME = (2000, 1, 1, 0, 0, 0)

SCRIPTS = {
    "BTSLungEmoji.md": "BTSLungEmoji_V1.docx",
    "BTSMedicalEmoji_Advocacy.md": "BTSMedicalEmoji_Advocacy_V1.docx",
    "BTSEbVAS_PediatricPRO.md": "BTSEbVAS_PediatricPRO_V1.docx",
}

# The source docx contains none of these. An em dash cannot be read aloud, and a
# straight apostrophe renders wrong in Word.
FORBIDDEN = {"—": "em dash", "–": "en dash", "'": "straight apostrophe"}


def spoken_paragraphs(markdown: str) -> list[str]:
    return [line.strip() for line in markdown.splitlines() if line.startswith("He: ")]


def normalize_zip_timestamps(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        entries = [(info, archive.read(info.filename)) for info in archive.infolist()]

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for info, payload in entries:
            pinned = zipfile.ZipInfo(info.filename, date_time=ZIP_DATE_TIME)
            pinned.compress_type = info.compress_type
            pinned.external_attr = info.external_attr
            archive.writestr(pinned, payload)


def build(source: Path, target: Path) -> int:
    paragraphs = spoken_paragraphs(source.read_text(encoding="utf-8"))
    if not paragraphs:
        raise ValueError(f"{source.name} has no 'He: ' lines")

    for text in paragraphs:
        for char, label in FORBIDDEN.items():
            if char in text:
                raise ValueError(f"{source.name} contains a {label}: {text[:60]}")

    document = Document()
    for text in paragraphs:
        document.add_paragraph(text)

    properties = document.core_properties
    properties.created = EPOCH
    properties.modified = EPOCH
    properties.revision = 1
    properties.last_modified_by = ""

    document.save(target)
    normalize_zip_timestamps(target)
    return len(paragraphs)


def main() -> None:
    for source_name, target_name in SCRIPTS.items():
        count = build(SOURCE_DIR / source_name, SOURCE_DIR / target_name)
        print(f"{target_name}: {count} paragraphs")


if __name__ == "__main__":
    main()
