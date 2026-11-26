#!/usr/bin/env python3
# =============================================================================
# 93 — build_gamma_hebdomad_magvs_pdf.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXVI day of November, Dies Iovis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: builds THE-GAMMA-HEBDOMAD-AUDIT-MAGVS.pdf from the
# Markdown master in the goal's files/, set in the Lex Stellarrvm
# family registered from pontifex/fonts/lex-stellarrvm/ (Serif body,
# SerifBold headings, Sans tables, Oblique the italic seat), Letter
# portrait, the resolving house footer on every page via the {nb}
# alias. The master is rendered line-wise; its tables print as
# Sans row lines. The two session plates are reproduced full width
# on an exhibits spread after §I; the Fiat Lux plate stands at the
# head of §VII. Every multi_cell passes new_x=XPos.LMARGIN,
# new_y=YPos.NEXT — the fpdf2 pen law of the house.
#
# FONT LAW: coverage is audited against every non-ASCII codepoint
# of the master BEFORE the build, against all four registered
# faces; an unheld glyph aborts the build and is named. No glyph
# is silently dropped.
#
# CONTENT TEST: Inputs — the Markdown master, the Doctrine logo,
# the three plate images, the four faces. Processes — coverage
# audit, registration, line-wise rendering with the exhibit
# spreads. Outputs — the MAGVS PDF beside the master, and a copy
# in this research folder. Tolerances — the footer count
# resolves; the page count prints at the end of the build.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())

from fontTools.ttLib import TTFont
from fpdf import FPDF
from fpdf.enums import XPos, YPos

HOME = Path.home()
BASE = HOME / "workspace/goals/cross-gematria-777-gap-filling/files"
MASTER = BASE / "THE-GAMMA-HEBDOMAD-AUDIT.md"
OUTPUT = BASE / "THE-GAMMA-HEBDOMAD-AUDIT-MAGVS.pdf"
RESEARCH = HOME / "workspace/pontifex/research/gamma-hebdomad-audit"
LOGO = HOME / "workspace/templates/doctrine-logo.png"
FONT_DIR = HOME / "workspace/pontifex/fonts/lex-stellarrvm"
EXHIBITS = RESEARCH / "exhibits"

FAMILY = "Lex Stellarrvm"
SANS = "Lex Stellarrvm Sans"
FACES = {
    "Serif": FONT_DIR / "LexStellarrvm-Serif.ttf",
    "SerifBold": FONT_DIR / "LexStellarrvm-SerifBold.ttf",
    "Sans": FONT_DIR / "LexStellarrvm-Sans.ttf",
    "Oblique": FONT_DIR / "LexStellarrvm-Oblique.ttf",
}
FOOTER = ("— {n} of {nb} — | All Rights Reserved, Without "
          "Prejudice | Flagpole of Claim and Coinage reserved")


def coverage_audit(text):
    """Every non-ASCII codepoint of the master must be held by all
    four faces; anything unheld aborts the build, named."""
    cmaps = {k: TTFont(str(p)).getBestCmap() for k, p in FACES.items()}
    bad = sorted({ord(c) for c in text if ord(c) > 127
                  and any(ord(c) not in cm for cm in cmaps.values())})
    if bad:
        raise SystemExit("UNHELD CODEPOINTS: "
                         + ", ".join(f"U+{cp:04X}" for cp in bad))
    return len({ord(c) for c in text if ord(c) > 127})


class Audit(FPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(FAMILY, "", 7.5)
        self.cell(0, 8, FOOTER.format(n=self.page_no(), nb="{nb}"),
                  align="C")


def clean(text):
    """Strip the code-span backticks (their content stands); the
    ** and * runs ride fpdf2's markdown mode to the B and I seats."""
    return text.replace("`", "")


def main():
    text = MASTER.read_text(encoding="utf-8")
    n_cp = coverage_audit(text)
    print(f"coverage audit: {n_cp} non-ASCII codepoints, all held")

    pdf = Audit("P", "mm", "Letter")
    pdf.alias_nb_pages("{nb}")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(20, 16, 20)
    pdf.add_font(FAMILY, "", str(FACES["Serif"]))
    pdf.add_font(FAMILY, "B", str(FACES["SerifBold"]))
    pdf.add_font(FAMILY, "I", str(FACES["Oblique"]))
    pdf.add_font(SANS, "", str(FACES["Sans"]))
    text_w = pdf.w - 40

    def para(body, size=10.5, style="", font=FAMILY, space=2.4,
             markdown=True):
        pdf.set_font(font, style, size)
        pdf.multi_cell(0, size * 0.52, clean(body), markdown=markdown,
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(space)

    def heading(body, size=13.5):
        pdf.ln(3.5)
        pdf.set_font(FAMILY, "B", size)
        pdf.multi_cell(0, size * 0.55, clean(body),
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2.4)

    def plate(path, caption):
        pdf.image(str(path), x=20, w=text_w)
        pdf.ln(2)
        para(caption, size=9, style="I")

    def exhibits_spread():
        pdf.add_page()
        heading("THE EXHIBITS — THE PLATES")
        plate(EXHIBITS / "PLATE-BETA-BLENDING.png",
              "Exhibit 1 — LEX STELLARRVM • BETA • Blending: the three "
              "densities as received (audit §II, claims M-01..M-03).")
        pdf.add_page()
        plate(EXHIBITS / "PLATE-HEBDOMAD-GAMMA-POLES.png",
              "Exhibit 2 — LEX STELLARRVM • HEBDOMAD • Seven Gates • "
              "Gamma Poles: the seven gates as received (audit §§III, V; "
              "the footer's claim stands at M-08).")
        pdf.add_page()

    pdf.add_page()
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        if not line.strip():
            continue
        if line.startswith("[LOGO"):
            w = 34
            pdf.image(str(LOGO), x=(pdf.w - w) / 2, w=w)
            pdf.ln(4)
            continue
        if line.startswith("# "):
            pdf.set_font(FAMILY, "B", 19)
            pdf.multi_cell(0, 10.5, clean(line[2:]), align="C",
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(2)
            continue
        if line.startswith("## "):
            title = line[3:]
            if title.startswith("§II"):
                exhibits_spread()
            heading(title)
            if title.startswith("§VII"):
                plate(EXHIBITS / "PLATE-FIAT-LUX.jpg",
                      "Exhibit 4 — Fiat Lux • Be Light Made: the sphere, "
                      "its three identities, and the four corner letters "
                      "R · C · H · O, as received (audit §VII; the "
                      "corners weighed at §X).")
            continue
        if line.strip() == "---":
            y = pdf.get_y()
            pdf.line(20, y, pdf.w - 20, y)
            pdf.ln(3.4)
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while line.lstrip().startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|")
                         .split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append("  ·  ".join(cells))
                if i < len(lines):
                    line = lines[i].rstrip()
                    i += 1
                else:
                    line = ""
            for row in rows:
                para(row, size=8.8, font=SANS, space=1.2,
                     markdown=False)
            y = pdf.get_y()
            pdf.line(20, y, pdf.w - 20, y)
            pdf.ln(3)
            continue
        # A paragraph: gather wrapped lines until a blank or a block.
        block = [line]
        while i < len(lines) and lines[i].strip() \
                and not lines[i].startswith(("#", "---")) \
                and not lines[i].lstrip().startswith("|"):
            block.append(lines[i].rstrip())
            i += 1
        para(" ".join(b.strip() for b in block))

    pdf.output(str(OUTPUT))
    (RESEARCH / OUTPUT.name).write_bytes(OUTPUT.read_bytes())
    print(f"built {OUTPUT.name}: {pdf.pages_count} pages")


if __name__ == "__main__":
    main()
