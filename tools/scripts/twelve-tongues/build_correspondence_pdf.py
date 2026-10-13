#!/usr/bin/env python3
# =============================================================================
# "Every number is a word, and every word is a bridge — but only if the
#  table is honest." — the scribe, on the twelve-tongues sweep
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# build_correspondence_pdf.py — render correspondence.csv as a printable,
# red-pen-ready PDF: THE TWELVE-TONGUES CORRESPONDENCE.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): the CSV is the single source of truth —
# machine-readable, replayable, built by build_correspondence.py. This script
# is a pure *presentation* layer: it reads the CSV, groups rows by meeting,
# and renders them. It invents nothing. If the CSV changes, re-run this
# script; the PDF is downstream, never upstream.
#
# TYPOGRAPHIC DOCTRINE: the table carries Hebrew, Greek, Arabic, Coptic,
# Ethiopic (Ge'ez), and Chinese script-forms. A single font cannot hold them
# all, so the base face (DejaVu Sans — Latin, Greek, Hebrew, Arabic) is
# backed by per-script fallback faces (Noto Coptic, Noto Ethiopic,
# Noto Sans SC). HarfBuzz shaping is enabled so Hebrew and Arabic render in
# true right-to-left order with proper joining — unshaped, עז would print
# reversed, which would be a falsehood on the page. TRVVTH: the rendering
# must not lie about the scripts.
#
# MECHANISM: csv.DictReader -> group by meeting_id (order-preserving) ->
# fpdf2 document with pdf.table() for the bank rows -> one section per
# meeting: heading, verdict paragraph, bank table -> correspondence.pdf.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
from collections import OrderedDict
from pathlib import Path

from fpdf import FPDF, XPos, YPos

# ---------------------------------------------------------------------------
# DOCTRINE: paths are relative to this script, so the build is reproducible
# from any working directory. The CSV stays the authority; the PDF is its
# shadow on paper.
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "correspondence.csv"
PDF_PATH = HERE / "correspondence.pdf"
FONTS_DIR = HERE / "fonts"

# ---------------------------------------------------------------------------
# MECHANISM: font registration. DejaVu Sans is the workhorse (Latin, Greek,
# Hebrew, Arabic verified in its cmap); the three Noto faces are registered
# as *fallback* fonts so any glyph the base face lacks is pulled from the
# correct script face instead of rendering as tofu (.notdef boxes).
# DOCTRINE: tofu on a correspondence table would be a silent falsehood —
# the reader would see a box where a letter stands. Fallbacks prevent it.
# ---------------------------------------------------------------------------
BASE_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BASE_FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FALLBACKS = [
    "/usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf",
    "/usr/share/fonts/truetype/noto/NotoSansEthiopic-ExtraLight.ttf",
    str(FONTS_DIR / "NotoSansSC.ttf"),
]


def load_meetings(csv_path):
    """MECHANISM: read the CSV and group rows by meeting_id, preserving the
    file's row order inside each meeting. Returns an OrderedDict."""
    meetings = OrderedDict()
    with open(csv_path, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            meetings.setdefault(row["meeting_id"], []).append(row)
    return meetings


def build_pdf(meetings, pdf_path):
    """MECHANISM: one section per meeting — heading, verdict, bank table."""
    pdf = FPDF(format="A4", orientation="P", unit="mm")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(10, 14, 10)

    # DOCTRINE: register the base face first, then the fallbacks, then enable
    # HarfBuzz shaping so RTL scripts render truthfully (see header).
    pdf.add_font("base", "", BASE_FONT)
    pdf.add_font("base", "B", BASE_FONT_BOLD)
    for i, fb in enumerate(FALLBACKS):
        pdf.add_font(f"fb{i}", "", fb)
    pdf.set_fallback_fonts([f"fb{i}" for i in range(len(FALLBACKS))])
    pdf.set_text_shaping(True)

    # -- Title block ---------------------------------------------------------
    # MECHANISM: centered title, subtitle, provenance line. The provenance
    # line states the CSV is the source, so no reader mistakes the PDF for
    # the authority.
    pdf.add_page()
    pdf.set_font("base", "B", 18)
    pdf.cell(0, 10, "THE TWELVE-TONGUES CORRESPONDENCE", new_x=XPos.LMARGIN,
             new_y=YPos.NEXT, align="C")
    pdf.set_font("base", "", 11)
    pdf.cell(0, 7, "PONTIFEX sweep — twelve languages, one shared corpus",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("base", "", 8)
    pdf.cell(0, 6, "Rendered from correspondence.csv (the source of truth) — "
             "2026-10-11", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(4)

    # -- Meeting sections ----------------------------------------------------
    for mid, rows in meetings.items():
        first = rows[0]
        concept = first["concept"]
        number = first["number"]
        verdict = first["meeting_verdict"]

        # MECHANISM: page-break guard — a meeting section should not strand
        # its heading at the bottom of a page.
        if pdf.get_y() > 235:
            pdf.add_page()

        pdf.set_font("base", "B", 13)
        # DOCTRINE: multi_cell with explicit new_x/new_y — the fpdf2 pen
        # gotcha (multi_cell leaves the pen at the right margin) is avoided
        # by naming the pen position every time.
        pdf.multi_cell(0, 7, f"{mid} — {concept} — {number}",
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("base", "", 9)
        pdf.multi_cell(0, 5, verdict, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

        # MECHANISM: the bank table. Five columns; widths sum to the 190mm
        # text width. pdf.table() sizes row heights to the tallest cell.
        pdf.set_font("base", "", 8)
        col_widths = (20, 38, 32, 38, 62)
        headers = ("Language", "Script form", "Table used",
                   "Provenance tier", "Independence note")
        with pdf.table(col_widths=col_widths, line_height=5,
                       text_align=("LEFT",) * 5) as table:
            hdr = table.row()
            for h in headers:
                hdr.cell(h)
            for r in rows:
                row = table.row()
                row.cell(r["language"])
                row.cell(r["script_form"])
                row.cell(r["table_used"])
                row.cell(r["provenance_tier"])
                row.cell(r["independence_note"])
        pdf.ln(6)

    # -- Footer --------------------------------------------------------------
    # MECHANISM: page numbers, so the red pen can cite "p.3" unambiguously.
    for p in range(1, pdf.pages_count + 1):
        pdf.page = p
        pdf.set_y(-14)
        pdf.set_font("base", "", 8)
        pdf.cell(0, 6, f"— {p} —", align="C")

    pdf.output(str(pdf_path))
    return pdf_path


def main():
    # DOCTRINE: fail closed — no CSV, no PDF. A PDF built from a missing or
    # unreadable source would be a fabrication.
    if not CSV_PATH.exists():
        raise SystemExit(f"source CSV not found: {CSV_PATH}")
    meetings = load_meetings(CSV_PATH)
    out = build_pdf(meetings, PDF_PATH)
    print(f"wrote {out} ({len(meetings)} meetings)")


if __name__ == "__main__":
    main()

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
