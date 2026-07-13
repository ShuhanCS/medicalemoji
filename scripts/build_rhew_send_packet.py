#!/usr/bin/env python
"""Build the four-file David Rhew review package.

The source proposal PDFs are preserved byte-for-byte as pages inside the merged
options packet and as entries in the PDF-only archive. This script adds accurate
external-facing front matter, bookmarks, and clean document metadata; it does not
make any proposal filing-ready.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import textwrap
import zipfile

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
TMP = ROOT / "output" / "tmp" / "rhew-send-packet"

WINDOWS_FONT_DIR = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
pdfmetrics.registerFont(TTFont("Helvetica", str(WINDOWS_FONT_DIR / "segoeui.ttf")))
pdfmetrics.registerFont(TTFont("Helvetica-Bold", str(WINDOWS_FONT_DIR / "segoeuib.ttf")))

BLUE = HexColor("#1F49B6")
BLUE_DARK = HexColor("#173A83")
BLUE_LIGHT = HexColor("#EAF0FF")
CYAN = HexColor("#0D8AA6")
CYAN_LIGHT = HexColor("#E8F7FA")
GREEN = HexColor("#16835A")
GREEN_LIGHT = HexColor("#EAF7F1")
AMBER = HexColor("#A76600")
AMBER_LIGHT = HexColor("#FFF5DD")
INK = HexColor("#182230")
SLATE = HexColor("#526070")
MID = HexColor("#B8C2CF")
LIGHT = HexColor("#F5F7FA")


@dataclass(frozen=True)
class Proposal:
    name: str
    status: str
    note: str
    relative_path: str

    @property
    def path(self) -> Path:
        return ROOT / self.relative_path


PROPOSALS = [
    Proposal(
        "CT Scan",
        "Planned",
        "Revise evidence, rights, metadata, and small-size artwork before filing",
        "submissions/v1.3.0/ct-scan/ct-scan_emoji_proposal_SUBMIT.pdf",
    ),
    Proposal(
        "Blood Bag",
        "Planned",
        "Revise evidence and compare directly with IV Bag before filing",
        "submissions/v1.3.0/blood-bag/blood-bag_emoji_proposal_SUBMIT.pdf",
    ),
    Proposal(
        "Pill Box",
        "Alternate",
        "First alternate; refresh weak usage evidence and test against Pill",
        "submissions/v1.3.0/pill-box/pill-box_emoji_proposal_SUBMIT.pdf",
    ),
    Proposal(
        "Ultrasound",
        "Evidence",
        "Promising concept; required Google evidence remains incomplete",
        "submissions/v1.5.0/ultrasound/ultrasound_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Weight Scale",
        "Evidence",
        "Promising alternative; evidence and recognition work remains",
        "submissions/v1.3.0/weight-scale/weight-scale_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Inhaler",
        "Review",
        "Worth another look; evidence and worldwide-recognition case remain",
        "submissions/v1.3.0/inhaler/inhaler_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "White Blood Cell",
        "Draft",
        "Current-cycle draft with evidence and small-size recognition gaps",
        "submissions/v1.3.0/white-blood-cell/white-blood-cell_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "IV Bag",
        "Draft",
        "Missing Trends evidence; compare directly with Blood Bag",
        "submissions/v1.3.0/iv-bag/iv-bag_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Leg Cast",
        "Draft",
        "Current-cycle draft; prior decline and recognition case need review",
        "submissions/v1.3.0/leg-cast/leg-cast_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Pill Pack",
        "Draft",
        "Evidence, comparator, naming, and 18-pixel recognition problems",
        "submissions/v1.3.0/pill-pack/pill-pack_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Maze",
        "Draft",
        "Current-cycle draft; missing Google evidence and prior declines",
        "submissions/v1.5.0/maze/maze_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "First Aid Kit",
        "Draft",
        "Current-cycle draft; missing Google evidence and substitute concerns",
        "submissions/v1.5.0/first-aid-kit/first-aid-kit_emoji_proposal_DRAFT.pdf",
    ),
    Proposal(
        "Kidney",
        "Later cycle",
        "November 2022 decline remains inside the four-year bar",
        "submissions/v1.7.0/kidney/kidney_emoji_proposal_SUBMIT.pdf",
    ),
    Proposal(
        "Stomach",
        "Later cycle",
        "November 2022 decline remains inside the four-year bar",
        "submissions/v1.7.0/stomach/stomach_emoji_proposal_SUBMIT.pdf",
    ),
    Proposal(
        "Liver",
        "Later cycle",
        "November 2022 decline remains inside the four-year bar",
        "submissions/v1.7.0/liver/liver_emoji_proposal_SUBMIT.pdf",
    ),
]

DECISION_BRIEF = OUT / "2026-07-12-microsoft-medical-emoji-decision-brief.pdf"
L2_SUBMISSION = (
    ROOT
    / "docs"
    / "proposals"
    / "utc-health-category"
    / "health-related-emoji-coverage-l2-submission.pdf"
)

OPTIONS_PACKET = OUT / "2026-07-13-medical-emoji-submission-options-packet.pdf"
ROLE_MAP = OUT / "2026-07-13-who-can-help-with-medical-emoji-review.pdf"
L2_SEND_COPY = OUT / "2026-07-13-health-related-emoji-coverage-l2-submission.pdf"
PDF_ARCHIVE = (
    ROOT
    / "output"
    / "zip"
    / "2026-07-13-medical-emoji-potential-submissions-pdfs.zip"
)

ARCHIVE_NAMES = [
    "01-ct-scan--planned-needs-revision.pdf",
    "02-blood-bag--planned-needs-revision.pdf",
    "03-pill-box--first-alternate-needs-revision.pdf",
    "04-ultrasound--evidence-incomplete.pdf",
    "05-weight-scale--evidence-incomplete.pdf",
    "06-inhaler--under-review.pdf",
    "07-white-blood-cell--working-draft.pdf",
    "08-iv-bag--working-draft.pdf",
    "09-leg-cast--working-draft.pdf",
    "10-pill-pack--working-draft.pdf",
    "11-maze--working-draft.pdf",
    "12-first-aid-kit--working-draft.pdf",
    "13-kidney--later-cycle.pdf",
    "14-stomach--later-cycle.pdf",
    "15-liver--later-cycle.pdf",
]


def require_inputs() -> None:
    required = [DECISION_BRIEF, L2_SUBMISSION, *(proposal.path for proposal in PROPOSALS)]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing required input(s):\n" + "\n".join(missing))


def wrapped_lines(text: str, font: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if not current or stringWidth(trial, font, size) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    *,
    font: str = "Helvetica",
    size: float = 9,
    color=INK,
    leading: float | None = None,
) -> float:
    leading = leading or size * 1.28
    pdf.setFillColor(color)
    pdf.setFont(font, size)
    for line in wrapped_lines(text, font, size, width):
        pdf.drawString(x, y, line)
        y -= leading
    return y


def rounded_box(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    fill,
    stroke=MID,
    radius: float = 8,
    line_width: float = 0.8,
) -> None:
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def page_counts() -> dict[str, int]:
    counts = {proposal.name: len(PdfReader(str(proposal.path)).pages) for proposal in PROPOSALS}
    counts["Decision brief"] = len(PdfReader(str(DECISION_BRIEF)).pages)
    return counts


def proposal_starts(counts: dict[str, int]) -> dict[str, int]:
    # Page 1 is the navigator; the decision brief follows immediately.
    page = 2 + counts["Decision brief"]
    starts: dict[str, int] = {}
    for proposal in PROPOSALS:
        starts[proposal.name] = page
        page += counts[proposal.name]
    return starts


def build_options_cover(path: Path, starts: dict[str, int]) -> None:
    width, height = LETTER
    pdf = canvas.Canvas(str(path), pagesize=LETTER, pageCompression=1)
    pdf.setTitle("Medical Emoji submission options for Microsoft review")
    pdf.setAuthor("Shuhan He")
    pdf.setSubject("Navigator for fifteen working Medical Emoji proposals")

    pdf.setFillColor(BLUE_DARK)
    pdf.rect(0, height - 92, width, 92, fill=1, stroke=0)
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawString(40, height - 28, "MICROSOFT REVIEW  |  13 JULY 2026")
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(40, height - 58, "Medical Emoji submission options")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(40, height - 77, "One indexed packet containing all 15 current working proposals")

    rounded_box(pdf, 40, height - 174, width - 80, 64, fill=BLUE_LIGHT, stroke=BLUE)
    pdf.setFillColor(BLUE_DARK)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(54, height - 132, "Current plan")
    draw_wrapped(
        pdf,
        "CT Scan and Blood Bag are planned after revision. Pill Box is the first alternate. "
        "Unicode's published submission window closes July 31, 2026.",
        54,
        height - 149,
        width - 108,
        size=8.8,
        color=INK,
        leading=11,
    )

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(40, height - 198, "Options and page guide")
    pdf.setFont("Helvetica", 7.4)
    pdf.setFillColor(SLATE)
    pdf.drawRightString(width - 40, height - 198, "The two-page decision brief begins on page 2")

    table_x = 40
    table_y_top = height - 211
    table_width = width - 80
    col_status = 68
    col_concept = 92
    col_page = 30
    col_note = table_width - col_status - col_concept - col_page
    header_h = 19
    row_h = 27.2

    pdf.setFillColor(INK)
    pdf.rect(table_x, table_y_top - header_h, table_width, header_h, fill=1, stroke=0)
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold", 7)
    pdf.drawString(table_x + 6, table_y_top - 13, "STATUS")
    pdf.drawString(table_x + col_status + 6, table_y_top - 13, "CONCEPT")
    pdf.drawString(table_x + col_status + col_concept + 6, table_y_top - 13, "WHAT REMAINS")
    pdf.drawRightString(table_x + table_width - 6, table_y_top - 13, "PAGE")

    y = table_y_top - header_h
    for index, proposal in enumerate(PROPOSALS):
        y_next = y - row_h
        if proposal.status == "Planned":
            status_color, status_fill = BLUE_DARK, BLUE_LIGHT
        elif proposal.status == "Alternate":
            status_color, status_fill = GREEN, GREEN_LIGHT
        elif proposal.status in {"Evidence", "Review"}:
            status_color, status_fill = AMBER, AMBER_LIGHT
        elif proposal.status == "Later cycle":
            status_color, status_fill = SLATE, LIGHT
        else:
            status_color, status_fill = SLATE, white

        pdf.setFillColor(LIGHT if index % 2 else white)
        pdf.rect(table_x, y_next, table_width, row_h, fill=1, stroke=0)
        pdf.setStrokeColor(MID)
        pdf.setLineWidth(0.35)
        pdf.line(table_x, y_next, table_x + table_width, y_next)

        pdf.setFillColor(status_fill)
        pdf.roundRect(table_x + 5, y_next + 7, col_status - 10, 13, 5, fill=1, stroke=0)
        pdf.setFillColor(status_color)
        pdf.setFont("Helvetica-Bold", 6.3)
        pdf.drawCentredString(table_x + col_status / 2, y_next + 11.4, proposal.status.upper())

        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 7.4)
        pdf.drawString(table_x + col_status + 6, y_next + 10.2, proposal.name)

        note_lines = wrapped_lines(proposal.note, "Helvetica", 6.35, col_note - 12)[:2]
        pdf.setFillColor(SLATE)
        pdf.setFont("Helvetica", 6.35)
        note_y = y_next + 15.8
        for note_line in note_lines:
            pdf.drawString(table_x + col_status + col_concept + 6, note_y, note_line)
            note_y -= 7.5

        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 7.2)
        pdf.drawRightString(table_x + table_width - 7, y_next + 10.2, str(starts[proposal.name]))
        y = y_next

    rounded_box(pdf, 40, 35, width - 80, 48, fill=AMBER_LIGHT, stroke=AMBER)
    pdf.setFillColor(AMBER)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(52, 65, "WORKING MATERIALS - NOT FIFTEEN PROPOSED FILINGS")
    draw_wrapped(
        pdf,
        "The packet supports comparison and routing. Every selected proposal still needs its own final review and official Unicode form submission.",
        52,
        51,
        width - 104,
        size=7.2,
        color=INK,
        leading=9,
    )
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 6.5)
    pdf.drawString(40, 20, "Prepared independently by Shuhan He. Microsoft has not endorsed these proposals or committed to implement them.")
    pdf.drawRightString(width - 40, 20, "Page 1 of 90")
    pdf.save()


def append_pdf(writer: PdfWriter, source: Path) -> int:
    reader = PdfReader(str(source))
    for page in reader.pages:
        writer.add_page(page)
    return len(reader.pages)


def build_options_packet(cover: Path, starts: dict[str, int]) -> None:
    writer = PdfWriter()
    append_pdf(writer, cover)
    append_pdf(writer, DECISION_BRIEF)

    writer.add_outline_item("Packet guide", 0)
    writer.add_outline_item("Decision brief", 1)
    proposals_parent = writer.add_outline_item("Working proposal PDFs", 3)

    page_index = 3
    for proposal in PROPOSALS:
        writer.add_outline_item(
            f"{proposal.name} - {proposal.status}",
            page_index,
            parent=proposals_parent,
        )
        page_index += append_pdf(writer, proposal.path)

    writer.add_metadata(
        {
            "/Title": "Medical Emoji submission options for Microsoft review",
            "/Author": "Shuhan He",
            "/Subject": "Fifteen working Medical Emoji proposal options with decision brief",
            "/Keywords": "medical emoji, Unicode, Microsoft review, emoji proposals",
        }
    )
    writer.page_mode = "/UseOutlines"
    with OPTIONS_PACKET.open("wb") as stream:
        writer.write(stream)


def arrow(pdf: canvas.Canvas, x1: float, y1: float, x2: float, y2: float, color=BLUE) -> None:
    pdf.setStrokeColor(color)
    pdf.setFillColor(color)
    pdf.setLineWidth(1.5)
    pdf.line(x1, y1, x2, y2)
    pdf.line(x2, y2, x2 - 5, y2 + 3)
    pdf.line(x2, y2, x2 - 5, y2 - 3)


def flow_box(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    body: str,
    *,
    fill,
    stroke,
) -> None:
    rounded_box(pdf, x, y, width, height, fill=fill, stroke=stroke, radius=7, line_width=1.0)
    pdf.setFillColor(stroke)
    pdf.setFont("Helvetica-Bold", 8.2)
    title_lines = wrapped_lines(title, "Helvetica-Bold", 8.2, width - 16)[:2]
    title_y = y + height - 16
    for title_line in title_lines:
        pdf.drawCentredString(x + width / 2, title_y, title_line)
        title_y -= 10
    body_y = title_y - 2
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 6.5)
    for body_line in wrapped_lines(body, "Helvetica", 6.5, width - 16)[:4]:
        pdf.drawCentredString(x + width / 2, body_y, body_line)
        body_y -= 8


def role_map_header(pdf: canvas.Canvas, width: float, height: float, page: int, subtitle: str) -> None:
    # Explicitly paint the page background. This avoids transparent-page rendering
    # differences between PDF viewers after ReportLab starts a new page.
    pdf.setFillColor(white)
    pdf.rect(0, 0, width, height, fill=1, stroke=0)
    pdf.setFillColor(BLUE_DARK)
    pdf.rect(0, height - 70, width, 70, fill=1, stroke=0)
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold", 21)
    pdf.drawString(34, height - 34, "Who can help route the Medical Emoji work")
    pdf.setFont("Helvetica", 9.2)
    pdf.drawString(34, height - 53, subtitle)
    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawRightString(width - 34, height - 34, f"13 JULY 2026  |  {page} OF 3")


def readable_flow_box(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    body: str,
    *,
    fill,
    stroke,
) -> None:
    rounded_box(pdf, x, y, width, height, fill=fill, stroke=stroke, radius=7, line_width=1.1)
    pdf.setFillColor(stroke)
    pdf.setFont("Helvetica-Bold", 9.2)
    title_y = y + height - 17
    for line in wrapped_lines(title, "Helvetica-Bold", 9.2, width - 18)[:2]:
        pdf.drawCentredString(x + width / 2, title_y, line)
        title_y -= 11
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 8)
    body_y = title_y - 3
    for line in wrapped_lines(body, "Helvetica", 8, width - 18)[:3]:
        pdf.drawCentredString(x + width / 2, body_y, line)
        body_y -= 10


def contact_card(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    name: str,
    badge: str,
    body: str,
    source: str,
    *,
    fill=white,
    stroke=BLUE,
) -> None:
    rounded_box(pdf, x, y, width, height, fill=fill, stroke=stroke, radius=8, line_width=1.0)
    pdf.setFillColor(stroke)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x + 14, y + height - 24, name)
    badge_width = stringWidth(badge, "Helvetica-Bold", 6.8) + 14
    pdf.setFillColor(stroke)
    pdf.roundRect(x + width - badge_width - 12, y + height - 28, badge_width, 17, 6, fill=1, stroke=0)
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold", 6.8)
    pdf.drawCentredString(x + width - badge_width / 2 - 12, y + height - 22.5, badge)
    body_y = draw_wrapped(
        pdf,
        body,
        x + 14,
        y + height - 44,
        width - 28,
        size=8.5,
        color=INK,
        leading=10.5,
    )
    source_y = max(y + 12, body_y - 1)
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 6.7)
    pdf.drawString(x + 14, source_y, source)


def linked_source(pdf: canvas.Canvas, url: str, x: float, y: float, max_width: float) -> float:
    lines = wrapped_lines(url, "Helvetica", 6.1, max_width)
    pdf.setFillColor(BLUE_DARK)
    pdf.setFont("Helvetica", 6.1)
    for line in lines:
        pdf.drawString(x, y, line)
        line_width = stringWidth(line, "Helvetica", 6.1)
        pdf.linkURL(url, (x, y - 2, x + line_width, y + 6), relative=0)
        y -= 7.4
    return y


def build_role_map(path: Path) -> None:
    width, height = landscape(LETTER)
    pdf = canvas.Canvas(str(path), pagesize=(width, height), pageCompression=1)
    pdf.setTitle("Who can help route the Medical Emoji work")
    pdf.setAuthor("Shuhan He")
    pdf.setSubject("Current Microsoft and Unicode contacts and the two official review routes")

    # Page 1: practical route and formal decision paths.
    role_map_header(
        pdf,
        width,
        height,
        1,
        "Start with Microsoft routing, then use the separate official paths for emoji proposals and the UTC paper.",
    )
    pdf.setFillColor(BLUE_DARK)
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawString(34, 516, "RECOMMENDED MICROSOFT ROUTE")
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 8)
    pdf.drawRightString(width - 34, 516, "Public roles are confirmed; private Microsoft assignments still need confirmation")

    route_x = [34, 178, 380, 572]
    route_w = [130, 188, 178, 186]
    route_y = 423
    route_h = 72
    readable_flow_box(pdf, route_x[0], route_y, route_w[0], route_h, "David Rhew", "Clinical sponsor and Microsoft connector", fill=BLUE_LIGHT, stroke=BLUE)
    readable_flow_box(pdf, route_x[1], route_y, route_w[1], route_h, "Peter Constable", "Best first call: Microsoft employee and UTC chair", fill=BLUE_LIGHT, stroke=BLUE)
    readable_flow_box(pdf, route_x[2], route_y, route_w[2], route_h, "Microsoft roles to confirm", "Member representative, UTC and ESR delegates", fill=CYAN_LIGHT, stroke=CYAN)
    readable_flow_box(pdf, route_x[3], route_y, route_w[3], route_h, "UTC leadership", "Peter Constable and Ned Holbrook", fill=GREEN_LIGHT, stroke=GREEN)
    for index in range(3):
        arrow(pdf, route_x[index] + route_w[index] + 4, route_y + route_h / 2, route_x[index + 1] - 5, route_y + route_h / 2)

    rounded_box(pdf, 34, 382, width - 68, 28, fill=AMBER_LIGHT, stroke=AMBER, radius=6, line_width=0.8)
    pdf.setFillColor(AMBER)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(45, 392, "EXECUTIVE ROUTING")
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 8.2)
    pdf.drawString(139, 392, "Vishal Chowdhary can make the Microsoft introductions. His Unicode Board role does not decide technical outcomes.")

    flow_x = [34, 222, 410, 598]
    flow_w = 160
    pdf.setFillColor(BLUE_DARK)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(34, 356, "ROUTE 1  |  Individual emoji proposals")
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 7.8)
    pdf.drawRightString(width - 34, 356, "Each selected candidate must be filed separately")
    flow_y = 278
    readable_flow_box(pdf, flow_x[0], flow_y, flow_w, 62, "Selected proposal PDF", "Final evidence, rights, metadata, and art", fill=BLUE_LIGHT, stroke=BLUE)
    readable_flow_box(pdf, flow_x[1], flow_y, flow_w, 62, "2026 Emoji Submission Form", "The only accepted intake route", fill=BLUE_LIGHT, stroke=BLUE)
    readable_flow_box(pdf, flow_x[2], flow_y, flow_w, 62, "ESR review", "Jennifer Daniel and Ned Holbrook lead", fill=AMBER_LIGHT, stroke=AMBER)
    readable_flow_box(pdf, flow_x[3], flow_y, flow_w, 62, "UTC action", "UTC retains technical authority", fill=GREEN_LIGHT, stroke=GREEN)
    for index in range(3):
        arrow(pdf, flow_x[index] + flow_w + 3, flow_y + 31, flow_x[index + 1] - 4, flow_y + 31)

    pdf.setFillColor(CYAN)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(34, 238, "ROUTE 2  |  Health-related emoji coverage paper")
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 7.8)
    pdf.drawRightString(width - 34, 238, "A separate UTC document; it does not submit any emoji")
    flow_y = 160
    readable_flow_box(pdf, flow_x[0], flow_y, flow_w, 62, "Authors confirm", "David Rhew, Heena Purohit, and Shuhan He", fill=CYAN_LIGHT, stroke=CYAN)
    readable_flow_box(pdf, flow_x[1], flow_y, flow_w, 62, "UTC document channel", "docsubmit plus a member agenda request", fill=CYAN_LIGHT, stroke=CYAN)
    readable_flow_box(pdf, flow_x[2], flow_y, flow_w, 62, "UTC discussion", "UTC may discuss, defer, or refer the work", fill=GREEN_LIGHT, stroke=GREEN)
    readable_flow_box(pdf, flow_x[3], flow_y, flow_w, 62, "Possible ESR referral", "ESR may study the questions and advise UTC", fill=AMBER_LIGHT, stroke=AMBER)
    for index in range(3):
        arrow(pdf, flow_x[index] + flow_w + 3, flow_y + 31, flow_x[index + 1] - 4, flow_y + 31, color=CYAN)

    rounded_box(pdf, 34, 80, width - 68, 56, fill=LIGHT, stroke=MID, radius=6, line_width=0.7)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.6)
    pdf.drawString(46, 117, "WHAT MICROSOFT CAN HELP WITH")
    draw_wrapped(
        pdf,
        "Confirm the member representative and delegates; advise on the UTC paper and agenda timing; identify Fluent Emoji, Segoe UI, font-engineering, and accessibility reviewers. Microsoft support cannot replace the submission form or promise an encoding outcome.",
        46,
        101,
        width - 92,
        size=8.1,
        color=INK,
        leading=10,
    )
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 6.6)
    pdf.drawString(34, 39, "Official paths: https://www.unicode.org/emoji/proposals.html  |  https://www.unicode.org/pending/docsubmit.html")
    pdf.drawString(34, 26, "The 15-PDF archive is an options set, not a plan to file 15 proposals. Contact roles were checked against official sources on 13 July 2026.")
    pdf.showPage()

    # Page 2: the people most likely to help.
    role_map_header(
        pdf,
        width,
        height,
        2,
        "Named contacts are ordered by practical usefulness, not by organizational rank.",
    )
    rounded_box(pdf, 34, 487, width - 68, 38, fill=BLUE_LIGHT, stroke=BLUE, radius=6, line_width=0.8)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 8.8)
    pdf.drawString(46, 502, "Recommended start: Peter Constable for the technical path and Vishal Chowdhary for Microsoft introductions.")

    card_w = (width - 68 - 18) / 2
    card_h = 112
    card_x = [34, 34 + card_w + 18]
    card_y = [357, 227, 97]
    contacts = [
        (
            "Peter Constable",
            "FIRST CALL",
            "Microsoft employee; Unicode Technical Vice President; UTC chair; Release Management chair. He represented Microsoft at UTC #187. Best first contact for process, agenda, and Microsoft routing.",
            "Source: Unicode technical leadership; UTC #187 minutes",
            BLUE_LIGHT,
            BLUE,
        ),
        (
            "Vishal Chowdhary",
            "EXECUTIVE SPONSOR",
            "Microsoft Vice President of Science; Unicode Board director since 2026. Best executive connector. The Board does not select emoji or decide technical outcomes.",
            "Source: Unicode Board of Directors",
            AMBER_LIGHT,
            AMBER,
        ),
        (
            "Jennifer Daniel",
            "ESR CHAIR",
            "Chair of the Emoji Standard & Research Working Group, which reviews new emoji proposals and develops recommendations for UTC. Individual proposal intake still requires the official form.",
            "Source: Unicode technical leadership; Emoji technical page",
            AMBER_LIGHT,
            AMBER,
        ),
        (
            "Ned Holbrook",
            "UTC + ESR VICE-CHAIR",
            "Vice-chair of both UTC and ESR in Unicode's current leadership directory; Apple typographic engineer and UTS #51 co-editor. Useful second technical contact.",
            "Source: Unicode technical leadership; UTS #51",
            GREEN_LIGHT,
            GREEN,
        ),
        (
            "Judy Safran-Aasen",
            "CONFIRM ROLE",
            "Represented Microsoft at UTC #187. A useful current Microsoft lead, but the public minutes do not identify her as Microsoft's primary delegate or alternate.",
            "Source: UTC #187 minutes",
            CYAN_LIGHT,
            CYAN,
        ),
        (
            "Andrew Glass",
            "ADJACENT MS STANDARDS",
            "Microsoft Principal Product Manager; chair of the CLDR Keyboard Working Group; works on font rendering, input, and shaping. Useful standards and font connector, not an emoji intake gate.",
            "Source: Unicode technical leadership",
            CYAN_LIGHT,
            CYAN,
        ),
    ]
    for index, contact in enumerate(contacts):
        x = card_x[index % 2]
        y = card_y[index // 2]
        contact_card(pdf, x, y, card_w, card_h, *contact[:4], fill=contact[4], stroke=contact[5])

    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 6.7)
    pdf.drawString(34, 61, "Unicode does not publish a complete current ESR roster or Microsoft's private delegate designations. Ask Peter or Vishal to confirm those roles internally.")
    pdf.drawString(34, 45, "The current central leadership directory lists Ned Holbrook as UTC vice-chair; a separate older UTC landing page still lists Craig Cummings.")
    pdf.drawString(34, 29, "Sources: https://www.unicode.org/consortium/techchairs.html  |  https://www.unicode.org/consortium/techcommittees.html  |  https://www.unicode.org/L2/L2026/26093.htm")
    pdf.showPage()

    # Page 3: operations, specialist help, and internal roles to identify.
    role_map_header(
        pdf,
        width,
        height,
        3,
        "Use these contacts for administration, specialist questions, or escalation after the normal route is clear.",
    )
    rounded_box(pdf, 34, 487, width - 68, 38, fill=LIGHT, stroke=MID, radius=6, line_width=0.7)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 8.8)
    pdf.drawString(46, 502, "These are not substitutes for the formal submission channels and are not first-line proposal reviewers.")

    card_h = 116
    card_y = [352, 218]
    contacts = [
        (
            "Michelle Perham",
            "OPERATIONS",
            "Unicode Program & Production Manager. Relevant to document administration and posting. Use the official document channel rather than guessing a personal address.",
            "Source: Unicode executive officers and staff",
            BLUE_LIGHT,
            BLUE,
        ),
        (
            "Mark Davis",
            "UTS #51 SPECIALIST",
            "UTS #51 co-editor, Unicode cofounder, and CLDR chair. A specialist for emoji specification, data, and interoperability questions, not routine intake.",
            "Source: UTS #51; Unicode technical leadership",
            CYAN_LIGHT,
            CYAN,
        ),
        (
            "Cathy Wissink",
            "GOVERNANCE ESCALATION",
            "Unicode Board chair and interim CTO; formerly led Microsoft's UTC participation. Appropriate only for a genuine governance or process escalation.",
            "Source: Unicode executive officers and staff",
            AMBER_LIGHT,
            AMBER,
        ),
        (
            "Toral Cowieson",
            "ORGANIZATIONAL ESCALATION",
            "Unicode CEO. Relevant to a membership or organizational issue, not to technical review of an emoji proposal.",
            "Source: Unicode executive officers and staff",
            GREEN_LIGHT,
            GREEN,
        ),
    ]
    for index, contact in enumerate(contacts):
        x = card_x[index % 2]
        y = card_y[index // 2]
        contact_card(pdf, x, y, card_w, card_h, *contact[:4], fill=contact[4], stroke=contact[5])

    rounded_box(pdf, 34, 82, width - 68, 112, fill=LIGHT, stroke=MID, radius=7, line_width=0.8)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 9.5)
    pdf.drawString(48, 173, "MICROSOFT ROLES PETER OR VISHAL SHOULD IDENTIFY")
    role_lines = [
        "1. Primary Unicode Organizational Member Representative",
        "2. Primary UTC delegate and alternate",
        "3. Microsoft ESR delegate or participant, if one is designated",
        "4. Fluent Emoji, Segoe UI, font-engineering, and accessibility owners",
        "5. Legal or IP reviewer only if Microsoft contributes artwork, coauthors, or an implementation statement",
    ]
    pdf.setFont("Helvetica", 8.3)
    pdf.setFillColor(INK)
    y = 154
    for line in role_lines:
        pdf.drawString(48, y, line)
        y -= 14

    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica-Bold", 6.2)
    pdf.drawString(34, 65, "OFFICIAL SOURCES")
    sources = [
        "https://www.unicode.org/consortium/directors.html",
        "https://www.unicode.org/consortium/officers.html",
        "https://www.unicode.org/consortium/techchairs.html",
        "https://www.unicode.org/consortium/techcommittees.html",
        "https://www.unicode.org/L2/L2026/26093.htm",
        "https://www.unicode.org/emoji/proposals.html",
        "https://www.unicode.org/pending/docsubmit.html",
        "https://www.unicode.org/consortium/tc-procedures.html",
    ]
    source_x = [34, 404]
    source_y = [53, 53]
    for index, source in enumerate(sources):
        column = 0 if index < 4 else 1
        source_y[column] = linked_source(pdf, source, source_x[column], source_y[column], 350)

    pdf.save()


def build_pdf_archive(path: Path) -> None:
    if len(ARCHIVE_NAMES) != len(PROPOSALS):
        raise ValueError("Every proposal must have exactly one archive filename")
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for proposal, archive_name in zip(PROPOSALS, ARCHIVE_NAMES, strict=True):
            info = zipfile.ZipInfo(archive_name, date_time=(2026, 7, 13, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(
                info,
                proposal.path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def make_clean_copy(
    source: Path,
    destination: Path,
    *,
    title: str,
    author: str,
    subject: str,
) -> None:
    reader = PdfReader(str(source))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": author,
            "/Subject": subject,
            "/Keywords": "medical emoji, Unicode, UTC discussion document",
        }
    )
    with destination.open("wb") as stream:
        writer.write(stream)


def main() -> None:
    require_inputs()
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    counts = page_counts()
    starts = proposal_starts(counts)
    cover = TMP / "options-cover.pdf"
    build_options_cover(cover, starts)
    build_options_packet(cover, starts)
    build_role_map(ROLE_MAP)
    build_pdf_archive(PDF_ARCHIVE)
    make_clean_copy(
        L2_SUBMISSION,
        L2_SEND_COPY,
        title="Health-related emoji coverage",
        author="David Rhew; Heena Purohit; Shuhan He",
        subject="UTC submission document requesting review and referral to ESR",
    )

    outputs = [L2_SEND_COPY, OPTIONS_PACKET, ROLE_MAP]
    for output in outputs:
        reader = PdfReader(str(output))
        print(f"{output.relative_to(ROOT)} | {len(reader.pages)} pages | {output.stat().st_size} bytes")
    print(
        f"{PDF_ARCHIVE.relative_to(ROOT)} | {len(PROPOSALS)} proposal PDFs | "
        f"{PDF_ARCHIVE.stat().st_size} bytes"
    )


if __name__ == "__main__":
    main()
