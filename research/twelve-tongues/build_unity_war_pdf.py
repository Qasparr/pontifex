#!/usr/bin/env python3
# =============================================================================
# "The control is the finding." — the scribe, on the Latin fallback
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# build_unity_war_pdf.py — render UNITY-WAR-TERMS.md as a printable,
# red-pen-ready PDF.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): the Markdown is the single source of truth;
# this script is a pure presentation layer over a small markdown subset
# (headings, italic lines, rules, bullets, paragraphs with **bold** and
# *italic* inline, one comparison table). It invents nothing.
#
# MECHANISM: line-oriented parse -> fpdf2 document. Inline rich text is
# written via alternating write() calls with font-style toggles; the table
# uses pdf.table() with auto row heights. HarfBuzz shaping on for the Hebrew
# and CJK script-forms.
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
MD_PATH = HERE / "UNITY-WAR-TERMS.md"
PDF_PATH = HERE / "UNITY-WAR-TERMS.pdf"

DJ = "/usr/share/fonts/truetype/dejavu"
NOTO = "/usr/share/fonts/truetype/noto"
FONTS = {
    ("base", ""): f"{DJ}/DejaVuSans.ttf",
    ("base", "B"): f"{DJ}/DejaVuSans-Bold.ttf",
    ("base", "I"): f"{NOTO}/NotoSans-Italic.ttf",
}
FALLBACKS = [
    f"{NOTO}/NotoSansCoptic-Regular.ttf",
    f"{NOTO}/NotoSansEthiopic-ExtraLight.ttf",
    str(HERE / "fonts" / "NotoSansSC.ttf"),
]

RICH_RE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*)")


def write_rich(pdf, text, size=10):
    """MECHANISM: honor **bold** and *italic* inline via alternating write()
    calls. DOCTRINE: markers are consumed, never printed."""
    pdf.set_font("base", "", size)
    for chunk in RICH_RE.split(text):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**"):
            pdf.set_font("base", "B", size)
            pdf.write(5.5, chunk[2:-2])
        elif chunk.startswith("*") and chunk.endswith("*") and len(chunk) > 2:
            pdf.set_font("base", "I", size)
            pdf.write(5.5, chunk[1:-1])
        else:
            pdf.set_font("base", "", size)
            pdf.write(5.5, chunk)
    pdf.ln(7)


def render_table(pdf, rows):
    """MECHANISM: header + body rows through pdf.table(); column widths tuned
    for the verdict column's long text."""
    header, body = rows[0], rows[1:]
    widths = (24, 42, 34, 90)
    pdf.set_font("base", "", 8)
    with pdf.table(col_widths=widths, line_height=5) as table:
        hr = table.row()
        for h in header:
            hr.cell(h)
        for r in body:
            row = table.row()
            for c in r:
                row.cell(c)
    pdf.ln(4)


def build(md_path, pdf_path):
    """MECHANISM: parse the subset, render block by block."""
    lines = md_path.read_text(encoding="utf-8").splitlines()

    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(14, 16, 14)
    for (fam, style), path in FONTS.items():
        pdf.add_font(fam, style, path)
    for i, fb in enumerate(FALLBACKS):
        pdf.add_font(f"fb{i}", "", fb)
    pdf.set_fallback_fonts([f"fb{i}" for i in range(len(FALLBACKS))])
    pdf.set_text_shaping(True)
    pdf.add_page()

    para, bullets, table = [], [], []
    in_table = False

    def flush_para():
        if para:
            write_rich(pdf, " ".join(para))
            para.clear()

    def flush_bullets():
        for b in bullets:
            pdf.set_font("base", "", 10)
            x = pdf.get_x()
            pdf.set_x(x + 6)
            pdf.write(5.5, "• ")
            write_rich(pdf, b, size=10)
        bullets.clear()

    def flush_table():
        if table:
            render_table(pdf, table)
            table.clear()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_bullets()
            continue
        if stripped.startswith("|"):
            flush_para()
            flush_bullets()
            in_table = True
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                table.append(cells)
            continue
        if in_table:
            flush_table()
            in_table = False
        if stripped.startswith("# "):
            flush_para()
            pdf.set_font("base", "B", 18)
            pdf.multi_cell(0, 9, stripped[2:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(2)
        elif stripped.startswith("## "):
            flush_para()
            if pdf.get_y() > 245:
                pdf.add_page()
            pdf.set_font("base", "B", 13)
            pdf.multi_cell(0, 7, stripped[3:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif stripped.startswith("### "):
            flush_para()
            pdf.set_font("base", "B", 11)
            pdf.multi_cell(0, 6.5, stripped[4:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif stripped == "---":
            flush_para()
            pdf.ln(2)
            pdf.line(14, pdf.get_y(), 196, pdf.get_y())
            pdf.ln(4)
        elif stripped.startswith("- "):
            flush_para()
            bullets.append(stripped[2:])
        elif stripped.startswith("*") and stripped.endswith("*") \
                and len(stripped) > 2 and not stripped.startswith("**"):
            flush_para()
            flush_bullets()
            pdf.set_font("base", "I", 9)
            pdf.multi_cell(0, 5.5, stripped.strip("*"), new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(1)
        else:
            flush_bullets()
            para.append(stripped)
    flush_para()
    flush_bullets()
    flush_table()

    for p in range(1, pdf.pages_count + 1):
        pdf.page = p
        pdf.set_y(-14)
        pdf.set_font("base", "", 8)
        pdf.cell(0, 6, f"— {p} —", align="C")

    pdf.output(str(pdf_path))
    return pdf_path


def main():
    # DOCTRINE: fail closed — no source, no PDF.
    if not MD_PATH.exists():
        raise SystemExit(f"source not found: {MD_PATH}")
    out = build(MD_PATH, PDF_PATH)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
