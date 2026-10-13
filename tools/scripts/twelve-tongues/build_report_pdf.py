#!/usr/bin/env python3
# =============================================================================
# "Let the log be the witness." — the scribe
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# build_report_pdf.py — render any PONTIFEX work-log Markdown as a
# red-pen-ready PDF. Generalized from build_unity_war_pdf.py.
#
# Usage: python3 build_report_pdf.py <input.md> <output.pdf>
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): the Markdown is the single source of truth;
# this script is a pure presentation layer over a small markdown subset
# (headings, italic lines, rules, bullets, numbered items, paragraphs with
# **bold** and *italic* inline, tables). It invents nothing.
#
# MECHANISM: line-oriented parse -> fpdf2 document. Inline rich text via
# alternating write() calls with font-style toggles; tables via pdf.table()
# with auto row heights. HarfBuzz shaping on for Hebrew/CJK script-forms.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import re
import sys
from pathlib import Path

from fpdf import FPDF, XPos, YPos

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
    "/home/hatch/workspace/pontifex/research/twelve-tongues/fonts/NotoSansSC.ttf",
]

RICH_RE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*)")
NUM_RE = re.compile(r"^(\d+)[.)]\s+")


def write_rich(pdf, text, size=10):
    """MECHANISM: honor **bold** and *italic* inline via alternating write()
    calls. DOCTRINE: markers are consumed, never printed."""
    pdf.set_font("base", "", size)
    for chunk in RICH_RE.split(text):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**") and len(chunk) > 4:
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
    """MECHANISM: header + body through pdf.table(). Column widths split the
    usable page width evenly; the last column (verdict/notes) takes double."""
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    usable = 182.0
    unit = usable / (ncols + 1)  # last col counts double
    widths = [unit] * (ncols - 1) + [unit * 2]
    pdf.set_font("base", "", 8)
    with pdf.table(col_widths=widths, line_height=5) as table:
        hr = table.row()
        for h in rows[0]:
            hr.cell(h)
        for r in rows[1:]:
            row = table.row()
            for c in r:
                row.cell(c)
    pdf.ln(4)


def build(md_path, pdf_path):
    """MECHANISM: parse the subset, render block by block."""
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()

    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(14, 16, 14)
    for (fam, style), path in FONTS.items():
        pdf.add_font(fam, style, path)
    for i, fb in enumerate(FALLBACKS):
        if Path(fb).exists():
            pdf.add_font(f"fb{i}", "", fb)
    pdf.set_fallback_fonts(
        [f"fb{i}" for i, fb in enumerate(FALLBACKS) if Path(fb).exists()])
    pdf.set_text_shaping(True)
    pdf.add_page()

    para, items, table = [], [], []
    in_table = False

    def flush_para():
        if para:
            write_rich(pdf, " ".join(para))
            para.clear()

    def flush_items():
        for marker, text in items:
            pdf.set_font("base", "", 10)
            x = pdf.get_x()
            pdf.set_x(x + 6)
            pdf.write(5.5, marker + " ")
            write_rich(pdf, text, size=10)
        items.clear()

    def flush_table():
        if table:
            render_table(pdf, table)
            table.clear()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_items()
            continue
        if stripped.startswith("|"):
            flush_para()
            flush_items()
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
            flush_items()
            pdf.set_font("base", "B", 18)
            pdf.multi_cell(0, 9, stripped[2:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(2)
        elif stripped.startswith("## "):
            flush_para()
            flush_items()
            if pdf.get_y() > 245:
                pdf.add_page()
            pdf.set_font("base", "B", 13)
            pdf.multi_cell(0, 7, stripped[3:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif stripped.startswith("### "):
            flush_para()
            flush_items()
            pdf.set_font("base", "B", 11)
            pdf.multi_cell(0, 6.5, stripped[4:], new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT)
            pdf.ln(1)
        elif stripped == "---":
            flush_para()
            flush_items()
            pdf.ln(2)
            pdf.line(14, pdf.get_y(), 196, pdf.get_y())
            pdf.ln(4)
        elif stripped.startswith("- "):
            flush_para()
            items.append(("•", stripped[2:]))
        elif NUM_RE.match(stripped):
            flush_para()
            m = NUM_RE.match(stripped)
            items.append((m.group(1) + ".", stripped[m.end():]))
        elif stripped.startswith("*") and stripped.endswith("*") \
                and len(stripped) > 2 and not stripped.startswith("**"):
            flush_para()
            flush_items()
            pdf.set_font("base", "I", 9)
            pdf.multi_cell(0, 5.5, stripped.strip("*"), new_x=XPos.LMARGIN,
                           new_y=YPos.NEXT, align="C")
            pdf.ln(1)
        else:
            flush_items()
            para.append(stripped)
    flush_para()
    flush_items()
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
    if len(sys.argv) != 3:
        raise SystemExit("usage: build_report_pdf.py <input.md> <output.pdf>")
    md_path, pdf_path = Path(sys.argv[1]), Path(sys.argv[2])
    if not md_path.exists():
        raise SystemExit(f"source not found: {md_path}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    out = build(md_path, pdf_path)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
