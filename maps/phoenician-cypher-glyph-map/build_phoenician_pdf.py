#!/usr/bin/env python3
# ============================================================================
# 93
# THE PHOENICIAN CYPHER GLYPH MAP — PDF BUILDER
# A Scientific Illuminist striking of the map's print form.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXII day of November, Dies Solis, Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: PHOENICIAN-CYPHER-GLYPH-MAP.md is the single source. This
#   builder parses it block by block (title block, section headings,
#   paragraphs with **bold** / *italic* runs, lists, the 22-row table)
#   and strikes PHOENICIAN-CYPHER-GLYPH-MAP.pdf beside it. No content
#   is authored here; the builder renders, it does not write.
#
# DOCTRINE — THE FONT SEATS, NAMED: the Phoenician block rides
#   Noto Sans Phoenician (the seat the master's Correctio of 2026-11-22
#   records as now held; coverage of U+10900-U+10915 asserted by cmap
#   audit at strike time, below). Greek and the transliterations ride
#   DejaVu (Sans for the table's Greek column, Serif for prose) — the
#   seats of the Pyramidasphere precedent. Arabic rides Noto Naskh
#   Arabic. A seat that fails its cmap assertion stops the strike:
#   tofu boxes are never struck as glyphs.
#
# DOCTRINE — THE PAGE: landscape Letter. The map's table carries
#   eleven columns; portrait would cram the Meaning column into
#   ribbons. Landscape is the table's honest shape.
#
# MECHANISM — fpdf2 pen law (house gotcha, 2026-10-04): multi_cell
#   leaves the pen at the RIGHT margin; every multi_cell below passes
#   new_x=XPos.LMARGIN / new_y=YPos.NEXT or is positioned by set_xy
#   inside the manual table grid.
# ============================================================================

import re
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fpdf import FPDF
from fpdf.enums import XPos, YPos

HERE = Path(__file__).resolve().parent
MASTER = HERE / "PHOENICIAN-CYPHER-GLYPH-MAP.md"
OUT = HERE / "PHOENICIAN-CYPHER-GLYPH-MAP.pdf"

# --- The seats -------------------------------------------------------------
F_PHN = "/usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf"
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_ARAB = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
F_ARAB_B = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"

FOOTER = ("— {page} of {nb} — | All Rights Reserved, Without Prejudice "
          "| Flagpole of Claim and Coinage reserved")


def assert_seat(path, codepoints, label):
    """A seat proves its coverage before it is used, or the strike stops."""
    cmap = TTFont(path).getBestCmap()
    missing = [cp for cp in codepoints if cp not in cmap]
    if missing:
        sys.exit(f"SEAT FAILURE — {label} lacks "
                 f"{[hex(c) for c in missing]}; refusing to strike tofu.")
    print(f"seat OK — {label}: {len(codepoints)} codepoints covered")


class MapPDF(FPDF):
    def footer(self):
        self.set_y(-26)
        self.set_font("sans", "", 7.5)
        self.set_text_color(90, 90, 90)
        self.cell(0, 10, FOOTER.format(page=self.page_no(), nb="{nb}"),
                  align="C")


def runs_of(text):
    """Split a markdown paragraph into (text, style) runs.

    **bold** is consumed before *italic*; style is '', 'B', or 'I'
    relative to the serif family the prose rides.
    """
    runs, buf, style = [], "", ""
    i = 0
    while i < len(text):
        if text.startswith("**", i):
            if buf:
                runs.append((buf, style))
                buf = ""
            style = "" if style == "B" else "B"
            i += 2
        elif text[i] == "*":
            if buf:
                runs.append((buf, style))
                buf = ""
            style = "" if style == "I" else "I"
            i += 1
        else:
            buf += text[i]
            i += 1
    if buf:
        runs.append((buf, style))
    return runs


def write_para(pdf, text, align="L", size=10, leading=14.5, indent=0):
    """Write one paragraph as styled runs; write() flows lines and pages."""
    pdf.set_font("serif", "", size)
    if align == "C":
        # Centered single-block paragraphs (title block, motto): measure
        # by rendering through multi_cell per run is overkill — the title
        # block lines are short; a centered multi_cell of the plain text
        # with the dominant style carries them.
        plain = text.replace("**", "").replace("*", "")
        style = "B" if text.startswith("**") else ""
        pdf.set_font("serif", style, size)
        pdf.multi_cell(0, leading, plain, align="C",
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        return
    if indent:
        pdf.set_x(pdf.l_margin + indent)
    for seg, style in runs_of(text):
        pdf.set_font("serif", style, size)
        pdf.write(leading, seg)
    pdf.ln(leading + 3)


# --- The table ---------------------------------------------------------------
COLW = [24, 84, 66, 124, 32, 88, 42, 84, 38, 84, 42]   # sums to 708
TABLE_W = sum(COLW)
ROW_H = 24
HEAD_H = 15


def wrap_lines(pdf, text, width, font, style, size):
    pdf.set_font(font, style, size)
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if pdf.get_string_width(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_grid_row(pdf, x0, y, h):
    pdf.set_draw_color(150, 150, 150)
    pdf.set_line_width(0.4)
    pdf.rect(x0, y, TABLE_W, h)
    x = x0
    for w in COLW[:-1]:
        x += w
        pdf.line(x, y, x, y + h)


def table_header(pdf, headers):
    x0 = (pdf.w - TABLE_W) / 2
    y = pdf.get_y()
    pdf.set_fill_color(228, 221, 242)
    pdf.rect(x0, y, TABLE_W, HEAD_H, style="F")
    draw_grid_row(pdf, x0, y, HEAD_H)
    x = x0
    pdf.set_font("sans", "B", 7.5)
    pdf.set_text_color(20, 20, 20)
    for w, htxt in zip(COLW, headers):
        pdf.set_xy(x + 1, y + 3.2)
        pdf.cell(w - 2, 9, htxt, align="C")
        x += w
    pdf.set_y(y + HEAD_H)


def table_row(pdf, cells, stripe):
    x0 = (pdf.w - TABLE_W) / 2
    if pdf.get_y() + ROW_H > pdf.h - 46:
        pdf.add_page()
        table_header(pdf, table_row.headers)
    y = pdf.get_y()
    if stripe:
        pdf.set_fill_color(246, 243, 250)
        pdf.rect(x0, y, TABLE_W, ROW_H, style="F")
    draw_grid_row(pdf, x0, y, ROW_H)
    pdf.set_text_color(20, 20, 20)
    xs = []
    x = x0
    for w in COLW:
        xs.append(x)
        x += w
    # # — the row's number
    pdf.set_font("sans", "", 9)
    pdf.set_xy(xs[0], y + 7)
    pdf.cell(COLW[0], 10, cells[0], align="C")
    # Phoenician — glyph from its own seat, codepoint beneath in sans
    glyph, _, cp = cells[1].partition(" ")
    pdf.set_font("phoen", "", 15)
    pdf.set_xy(xs[1], y + 0.5)
    pdf.cell(COLW[1], 13, glyph, align="C")
    pdf.set_font("sans", "", 6.5)
    pdf.set_xy(xs[1], y + 14.5)
    pdf.cell(COLW[1], 8, cp, align="C")
    # Name
    pdf.set_font("serif", "", 9)
    pdf.set_xy(xs[2], y + 7)
    pdf.cell(COLW[2], 10, cells[2], align="C")
    # Meaning — the one cell that wraps
    lines = wrap_lines(pdf, cells[3], COLW[3] - 8, "serif", "", 8.5)
    pdf.set_font("serif", "", 8.5)
    ly = y + (ROW_H - len(lines) * 10.5) / 2
    for ln in lines:
        pdf.set_xy(xs[3] + 4, ly)
        pdf.cell(COLW[3] - 8, 10.5, ln, align="L")
        ly += 10.5
    # Sound
    pdf.set_font("serif", "", 9)
    pdf.set_xy(xs[4], y + 7)
    pdf.cell(COLW[4], 10, cells[4], align="C")
    # Greek (Helm) — letter and name, DejaVu Sans carries the archaic seats
    pdf.set_font("sans", "", 9.5)
    pdf.set_xy(xs[5], y + 7)
    pdf.cell(COLW[5], 10, cells[5], align="C")
    # Milesian
    pdf.set_xy(xs[6], y + 7)
    pdf.cell(COLW[6], 10, cells[6], align="C")
    # Latin (First Mate)
    pdf.set_xy(xs[7], y + 7)
    pdf.cell(COLW[7], 10, cells[7], align="C")
    # Ordinal
    pdf.set_xy(xs[8], y + 7)
    pdf.cell(COLW[8], 10, cells[8], align="C")
    # Arabic (Scribe) — glyph from the Naskh seat, name in sans beside it
    aglyph, _, aname = cells[9].partition(" ")
    pdf.set_font("arab", "", 13)
    pdf.set_xy(xs[9], y + 3)
    pdf.cell(28, 14, aglyph, align="C")
    pdf.set_font("sans", "", 8.5)
    pdf.set_xy(xs[9] + 28, y + 7)
    pdf.cell(COLW[9] - 28, 10, aname, align="L")
    # Abjad
    pdf.set_font("sans", "", 9.5)
    pdf.set_xy(xs[10], y + 7)
    pdf.cell(COLW[10], 10, cells[10], align="C")
    pdf.set_y(y + ROW_H)


def main():
    # Every seat proves itself before a page is struck.
    assert_seat(F_PHN, range(0x10900, 0x10916), "Noto Sans Phoenician")
    md_chars = {ord(c) for c in MASTER.read_text(encoding="utf-8")
                if ord(c) > 127}
    assert_seat(F_SERIF, md_chars - set(range(0x10900, 0x10916))
                - {ord(c) for c in "ابجدهوزحطيكلمنسعفصقرشت"}, "DejaVu Serif (prose)")
    assert_seat(F_ARAB, {ord(c) for c in "ابجدهوزحطيكلمنسعفصقرشت"},
                "Noto Naskh Arabic")

    pdf = MapPDF(orientation="L", unit="pt", format="Letter")
    pdf.set_margins(40, 36, 40)
    pdf.set_auto_page_break(True, margin=46)
    pdf.alias_nb_pages("{nb}")
    pdf.add_font("serif", "", F_SERIF)
    pdf.add_font("serif", "B", F_SERIF_B)
    pdf.add_font("serif", "I", F_SERIF_I)
    pdf.add_font("sans", "", F_SANS)
    pdf.add_font("sans", "B", F_SANS_B)
    pdf.add_font("phoen", "", F_PHN)
    pdf.add_font("arab", "", F_ARAB)
    pdf.add_font("arab", "B", F_ARAB_B)
    pdf.add_page()

    lines = MASTER.read_text(encoding="utf-8").splitlines()
    para = []            # accumulated paragraph lines
    in_title_block = True
    seen_h2 = False

    def flush():
        nonlocal para
        if para:
            text = " ".join(s.strip() for s in para)
            para = []
            if text.replace("**", "").strip() == \
                    "93 — Live, Love, and let Love, Live.":
                write_para(pdf, text, align="C", size=10.5)
            elif in_title_block:
                write_para(pdf, text, align="C", size=10.5, leading=15)
            else:
                write_para(pdf, text)

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            flush()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append([c.strip() for c in
                              lines[i].strip().strip("|").split("|")])
                i += 1
            headers, data = block[0], block[2:]   # block[1] is the rule row
            table_row.headers = headers
            table_header(pdf, headers)
            for n, row in enumerate(data):
                table_row(pdf, row, stripe=(n % 2 == 1))
            pdf.ln(8)
            continue
        i += 1
        if not s:
            flush()
        elif s.startswith("# "):
            flush()
            pdf.set_font("serif", "B", 19)
            pdf.multi_cell(0, 24, s[2:], align="C",
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(2)
        elif s.startswith("## "):
            flush()
            if not seen_h2:
                seen_h2 = True
                pdf.set_font("serif", "", 13.5)
                pdf.multi_cell(0, 18, s[3:], align="C",
                               new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            else:
                in_title_block = False
                pdf.ln(6)
                pdf.set_font("sans", "B", 12.5)
                pdf.multi_cell(0, 16, s[3:], align="L",
                               new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.ln(3)
        elif s.startswith("### "):
            flush()
            pdf.set_font("sans", "B", 11)
            pdf.multi_cell(0, 15, s[4:], align="C",
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(4)
        elif s == "---":
            flush()
            pdf.ln(2)
            pdf.set_draw_color(120, 120, 120)
            pdf.set_line_width(0.6)
            pdf.line(pdf.l_margin, pdf.get_y(),
                     pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(8)
        elif s.startswith("- ") or re.match(r"^\d+\. ", s):
            flush()
            write_para(pdf, s, indent=14)
        elif s.startswith("— 1 of 1 —"):
            pass    # the master's print footer; the PDF strikes its own
        else:
            para.append(line)
    flush()

    pdf.output(str(OUT))
    print(f"struck — {OUT} ({OUT.stat().st_size} bytes, {pdf.pages_count} pages)")


if __name__ == "__main__":
    main()

# 93 — Live, Love, and let Love, Live.
