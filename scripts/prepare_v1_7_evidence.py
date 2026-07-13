"""Prepare cleaner v1.7 Kidney evidence crops from the preserved v1.6 captures.

The transformations are visual crops only. They preserve the captured result
count, query terms, geographic setting, date range, search mode, and chart.

Usage:
    python scripts/prepare_v1_7_evidence.py
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "submissions" / "v1.6.0" / "kidney" / "evidence" / "frequency"
DESTINATION = ROOT / "submissions" / "v1.7.0" / "kidney" / "evidence" / "frequency"

CROPS = {
    "kidney_google_search_2026-05-13_SUBMIT.png": (0, 0, 1440, 1150),
    "kidney_google_trends_web_elephant_2026-05-13_SUBMIT.png": (0, 0, 1440, 800),
    "kidney_google_trends_image_elephant_2026-05-13_SUBMIT.png": (0, 0, 1440, 800),
}


def main() -> None:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for name, box in CROPS.items():
        source = SOURCE / name
        destination = DESTINATION / name
        with Image.open(source) as image:
            cropped = image.convert("RGB").crop(box)
            cropped.save(destination, optimize=True)
        print(destination)


if __name__ == "__main__":
    main()
