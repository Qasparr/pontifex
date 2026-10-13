#!/usr/bin/env python3
# =============================================================================
# "A defense that concedes nothing is a defense that collapses at the first
#  verified quote." — the scribe, on honest advocacy
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# build_defense_brief_pdf.py — render DEFENSE-BRIEF.md as a printable,
# red-pen-ready PDF.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): the Markdown is the single source of truth;
# this script is a pure presentation layer. It parses a small markdown subset
# (headings, blockquotes, italic lines, bold-inline, rules) and renders it.
# It invents nothing.
#
# MECHANISM: line-oriented parse -> fpdf2 document. Blockquotes are set
# indented in oblique; "**...**" inline segments are written bold via
# alternating write() calls; headings are sized by level. HarfBuzz shaping
# is enabled (harmless for Latin, required for any RTL that appears).
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import re
from pathlib import Path

from fpdf import FPDF, XPos, YPos

# ---------------------------------------------------------------------------
# DOCTRINE: paths relative to this script — reproducible from anywhere.
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
MD_PATH = HERE / "DEFENSE-BRIEF.md"
PDF_PATH = HERE / "DEFENSE-BRIEF.pdf"

DJ = "/usr/share/fonts/truetype/dejavu"
FONTS = {
    ("base", ""): f"{DJ}/DejaVuSans.ttf",
    ("base", "B"): f"{DJ}/DejaVuSans-Bold.ttf",
    ("base", "I"): "/usr/share/fonts/truetype/noto/NotoSans-Italic.ttf",
}

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def write_rich(pdf, text, base_style=""):
    """MECHANISM: write a paragraph honoring **bold** inline segments.
    DOCTRINE: the markers are presentation, not content — they are consumed,
    never printed."""
    pdf.set_font("base", base_style, 10)
    pos = 0
    for m in BOLD_RE.finditer(text):
        if m.start() > pos:
            pdf.set_font("base", base_style, 10)
            pdf.write(5, text[pos:m.start()])
        pdf.set_font("base", "B", 10)
        pdf.write(5, m.group(1))
        pos = m.end()
    if pos < len(text):
        pdf.set_font("base", base_style, 10)
        pdf.write(5, text[pos:])
    pdf.ln(7)


def build(md_path, pdf_path):
    """MECHANISM: parse the markdown subset, render block by block."""
    lines = md_path.read_text(encoding="utf-8").splitlines()

    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(14, 16, 14)
    for (fam, style), path in FONTS.items():
        pdf.add_font(fam, style, path)
    pdf.set_text_shaping(True)
    pdf.add_page()

    para = []  # accumulator for body-paragraph lines

    def flush_para():
        # DOCTRINE: a paragraph is rendered only when complete — no
        # half-rendered blocks on the page.
        if para:
            write_rich(pdf, " ".join(para))
            para.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            continue
        if line.startswith("# "):
            flush_para()
            pdf.set_font("base", "B", 18)
            pdf.multi_cell(0, 9, line[2:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(2)
        elif line.startswith("## "):
            flush_para()
            if pdf.get_y() > 245:  # keep headings with their section
                pdf.add_page()
            pdf.set_font("base", "B", 13)
            pdf.multi_cell(0, 7, line[3:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif line.startswith("> "):
            flush_para()
            pdf.set_font("base", "I", 9.5)
            x = pdf.get_x()
            pdf.set_x(x + 8)
            pdf.multi_cell(164, 5.5, line[2:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif line.strip() == "---":
            flush_para()
            pdf.ln(2)
            pdf.line(14, pdf.get_y(), 196, pdf.get_y())
            pdf.ln(4)
        elif line.startswith("*") and line.endswith("*") and len(line) > 2 \
                and not line.startswith("**"):
            flush_para()
            pdf.set_font("base", "I", 9)
            pdf.multi_cell(0, 5.5, line.strip("*"), new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(1)
        elif re.match(r"^\d+\.\s", line):
            flush_para()
            write_rich(pdf, line)
        else:
            para.append(line.strip())
    flush_para()

    for p in range(1, pdf.pages_count + 1):
        pdf.page = p
        pdf.set_y(-14)
        pdf.set_font("base", "", 8)
        pdf.cell(0, 6, f"— {p} —", align="C")

    pdf.output(str(pdf_path))
    return pdf_path


def main():
    # DOCTRINE: fail closed — no source, no PDF. A brief built from a
    # missing source would be a fabrication.
    if not MD_PATH.exists():
        raise SystemExit(f"source not found: {MD_PATH}")
    out = build(MD_PATH, PDF_PATH)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
