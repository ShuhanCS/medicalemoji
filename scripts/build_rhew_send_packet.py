#!/usr/bin/env python
"""Build the three-attachment David Rhew review package.

The source proposal PDFs are preserved byte-for-byte as pages inside the merged
options packet. This script adds accurate external-facing front matter,
bookmarks, and clean document metadata; it does not make any proposal filing-ready.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import textwrap

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
TMP = ROOT / "output" / "tmp" / "rhew-send-packet"

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
UTC_DRAFT = (
    ROOT
    / "docs"
    / "proposals"
    / "utc-health-category"
    / "health-coverage-maintenance-l2-review-draft.pdf"
)

OPTIONS_PACKET = OUT / "2026-07-13-medical-emoji-submission-options-packet.pdf"
ROLE_MAP = OUT / "2026-07-13-who-can-help-with-medical-emoji-review.pdf"
UTC_SEND_COPY = OUT / "2026-07-13-health-related-emoji-coverage-discussion-draft.pdf"


def require_inputs() -> None:
    required = [DECISION_BRIEF, UTC_DRAFT, *(proposal.path for proposal in PROPOSALS)]
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


def build_role_map(path: Path) -> None:
    width, height = landscape(LETTER)
    pdf = canvas.Canvas(str(path), pagesize=(width, height), pageCompression=1)
    pdf.setTitle("Who can help with the Medical Emoji review")
    pdf.setAuthor("Shuhan He")
    pdf.setSubject("Microsoft and Unicode roles for two separate review routes")

    pdf.setFillColor(BLUE_DARK)
    pdf.rect(0, height - 66, width, 66, fill=1, stroke=0)
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawString(34, height - 34, "Who can help with the Medical Emoji review")
    pdf.setFont("Helvetica", 9)
    pdf.drawString(34, height - 51, "Two Unicode routes, the Microsoft roles that can help, and where technical authority remains")

    # Route 1: individual emoji proposals.
    pdf.setFillColor(BLUE_DARK)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(34, height - 92, "ROUTE 1  |  Individual emoji proposals")
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 7.4)
    pdf.drawRightString(width - 34, height - 92, "Each selected candidate follows this route separately")

    route_y = height - 184
    box_w, box_h, gap = 157, 68, 23
    x_positions = [34 + i * (box_w + gap) for i in range(4)]
    flow_box(pdf, x_positions[0], route_y, box_w, box_h, "Shuhan He", "Completes and files each final proposal", fill=BLUE_LIGHT, stroke=BLUE)
    flow_box(pdf, x_positions[1], route_y, box_w, box_h, "Official Emoji Submission Form", "Required entry point for 2026 proposal review", fill=BLUE_LIGHT, stroke=BLUE)
    flow_box(pdf, x_positions[2], route_y, box_w, box_h, "Emoji Standard & Research WG", "Reviews submissions and makes recommendations", fill=AMBER_LIGHT, stroke=AMBER)
    flow_box(pdf, x_positions[3], route_y, box_w, box_h, "Unicode Technical Committee", "Retains authority over technical decisions", fill=GREEN_LIGHT, stroke=GREEN)
    for index in range(3):
        arrow(pdf, x_positions[index] + box_w + 3, route_y + box_h / 2, x_positions[index + 1] - 4, route_y + box_h / 2)

    # Route 2: UTC discussion document.
    pdf.setFillColor(CYAN)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(34, height - 216, "ROUTE 2  |  Health-coverage discussion document")
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 7.4)
    pdf.drawRightString(width - 34, height - 216, "This document cannot replace an individual emoji proposal")

    route2_y = height - 309
    flow_box(pdf, x_positions[0], route2_y, box_w, box_h, "Shuhan + Microsoft standards team", "May revise, coauthor, or use the draft as source", fill=CYAN_LIGHT, stroke=CYAN)
    flow_box(pdf, x_positions[1], route2_y, box_w, box_h, "UTC document submission", "Separate submission with a requested agenda disposition", fill=CYAN_LIGHT, stroke=CYAN)
    flow_box(pdf, x_positions[2], route2_y, box_w, box_h, "UTC discussion", "UTC may discuss the question or refer work", fill=GREEN_LIGHT, stroke=GREEN)
    flow_box(pdf, x_positions[3], route2_y, box_w, box_h, "Possible ESR referral", "ESR may advise whether guidance or review would help", fill=AMBER_LIGHT, stroke=AMBER)
    for index in range(3):
        arrow(pdf, x_positions[index] + box_w + 3, route2_y + box_h / 2, x_positions[index + 1] - 4, route2_y + box_h / 2, color=CYAN)

    # Microsoft routing roles.
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawString(34, height - 344, "Who David can connect")

    roles_y = 102
    roles_h = 96
    roles_gap = 12
    roles_w = (width - 68 - roles_gap * 3) / 4
    roles = [
        (
            "Microsoft Unicode standards lead / current UTC delegate",
            "Checks process and timing; reviews the discussion draft; may request normal agenda consideration.",
            BLUE_LIGHT,
            BLUE,
        ),
        (
            "Emoji, font, and accessibility reviewers",
            "Test 18-pixel color and black-and-white recognition and platform-neutral implementation feasibility.",
            CYAN_LIGHT,
            CYAN,
        ),
        (
            "Microsoft legal / IP",
            "Needed only if Microsoft contributes artwork, coauthors, or approves an implementation-support statement.",
            GREEN_LIGHT,
            GREEN,
        ),
        (
            "Optional executive routing",
            "Vishal Chowdhary is Microsoft's Unicode Board director. The Board does not decide which emoji are encoded.",
            AMBER_LIGHT,
            AMBER,
        ),
    ]
    for index, (title, body, fill, stroke) in enumerate(roles):
        x = 34 + index * (roles_w + roles_gap)
        rounded_box(pdf, x, roles_y, roles_w, roles_h, fill=fill, stroke=stroke, radius=7, line_width=1.0)
        pdf.setFillColor(stroke)
        pdf.setFont("Helvetica-Bold", 7.5)
        title_y = roles_y + roles_h - 16
        for line in wrapped_lines(title, "Helvetica-Bold", 7.5, roles_w - 16)[:3]:
            pdf.drawString(x + 8, title_y, line)
            title_y -= 9
        body_y = title_y - 4
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica", 6.5)
        for line in wrapped_lines(body, "Helvetica", 6.5, roles_w - 16)[:5]:
            pdf.drawString(x + 8, body_y, line)
            body_y -= 8

    rounded_box(pdf, 34, 47, width - 68, 42, fill=LIGHT, stroke=MID, radius=6, line_width=0.6)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 7.2)
    pdf.drawString(45, 74, "NAMED PEOPLE IN THE PUBLIC RECORD")
    pdf.setFont("Helvetica", 6.7)
    pdf.setFillColor(SLATE)
    people = (
        "Peter Constable - UTC chair; UTC #187 minutes list him for Microsoft  |  "
        "Judy Safran-Aasen - UTC #187 minutes list her for Microsoft  |  "
        "Jennifer Daniel - ESR chair  |  Vishal Chowdhary - Unicode Board director, Microsoft"
    )
    draw_wrapped(pdf, people, 45, 61, width - 90, size=6.7, color=SLATE, leading=8)

    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica", 5.7)
    pdf.drawString(34, 29, "The public record does not identify Microsoft's primary voting delegate or whether Microsoft has an ESR participant; David can confirm the current owners.")
    pdf.drawString(34, 17, "Sources: https://www.unicode.org/emoji/proposals.html  |  https://www.unicode.org/pending/docsubmit.html  |  https://www.unicode.org/consortium/techcommittees.html")
    pdf.drawString(34, 8, "https://www.unicode.org/L2/L2026/26093.htm  |  https://www.unicode.org/consortium/directors.html  |  https://www.unicode.org/consortium/tc-procedures.html")
    pdf.save()


def make_clean_copy(source: Path, destination: Path, *, title: str, subject: str) -> None:
    reader = PdfReader(str(source))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "Shuhan He",
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
    make_clean_copy(
        UTC_DRAFT,
        UTC_SEND_COPY,
        title="Health-related emoji coverage - discussion draft",
        subject="Draft for Microsoft standards review; not submitted to Unicode",
    )

    outputs = [UTC_SEND_COPY, OPTIONS_PACKET, ROLE_MAP]
    for output in outputs:
        reader = PdfReader(str(output))
        print(f"{output.relative_to(ROOT)} | {len(reader.pages)} pages | {output.stat().st_size} bytes")


if __name__ == "__main__":
    main()
