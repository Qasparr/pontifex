#!/usr/bin/env python3
# =============================================================================
# "If it isn't on the page, it didn't happen." — the desk
#
# Thelemic date: Tue 2026-11-10 (Dies Martis), Sol in Scorpio, Anno V:xii e.n.
#
# 93.
#
# build_divine_nine_abroad_ii_german_pdf.py — builds THE-DIVINE-NINE-
# ABROAD-II-GERMAN.pdf from the Markdown master THE-DIVINE-NINE-ABROAD-
# II-GERMAN.md: THE DIVINE NINE ABROAD, Essay II, the German dialect —
# the pure five on declared roads, the umlauts as born hybrids (AE
# weighing 6 in three banks at once), IE as German's improper
# diphthong, the EI seat classified as an OFFSET of Δ1 against the
# Greek hybrid seat ΕΙ, and the Nine Rules for Hybrid Dialects
# derived from the German evidence. The master is the authority;
# this script only dresses the essay for the page as its Teacher's
# Revision (MAGVS) edition. Built on the pattern of
# build_nine_vowels_magvs_pdf.py, the parent audit's builder.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice).
#
# METHOD (Scientific Illuminism): Inputs  — the Markdown master, the
# Doctrine logo PNG, the DejaVu font family. Processes — line-wise
# rendering (title, sections, tables as set lines, blockquotes),
# footer with resolving page count via the {nb} alias, the two marked
# substitutions of MECHANISM NOTES below. Outputs — the PDF beside
# the master. Tolerances — the page count in every footer must
# resolve to the true count; no line may silently lose a character
# the fonts cannot carry (coverage verified glyph by glyph before
# this build: German Ä Ö Ü ä ö ü ß, the full Milesian numeral set,
# Δ and the arrows all present in DejaVu Serif); every key number of
# the audit (486, 485, 15, 14, 6, 27) must survive onto the page —
# the desk greps the built text layer for them before signing.
#
# MECHANISM NOTES:
#  * Every multi_cell passes new_x=XPos.LMARGIN, new_y=YPos.NEXT —
#    the house gotcha (AGENTS.md, 2026-10-04): multi_cell(w=0)
#    otherwise parks the pen at the right margin and the next call
#    dies for want of width.
#  * MARKED SUBSTITUTION 1 (declared in the essay, Footnote 8): the
#    superscript e of the historical spellings aͤ oͤ uͤ is a COMBINING
#    mark (U+0364) DejaVu Serif does not carry; the page prints the
#    modifier letter ᵉ (U+1D49, carried) instead — aͤ -> aᵉ. The
#    master keeps the combining form.
#  * MARKED SUBSTITUTION 2 (declared in the essay, Footnote 8): the
#    two right-to-left strings (the KEY bridge's Hebrew and Arabic
#    names) are carried by transliteration per SCRIPT_MAP — the
#    toolchain does not shape right-to-left scripts honestly.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import re
import sys
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

# DOCTRINE: paths are absolute so the build is reproducible from any cwd.
BASE = Path.home() / "workspace/goals/cross-gematria-777-gap-filling/files"
MASTER = BASE / "THE-DIVINE-NINE-ABROAD-II-GERMAN.md"
OUTPUT = BASE / "THE-DIVINE-NINE-ABROAD-II-GERMAN.pdf"
LOGO = Path.home() / "workspace/templates/doctrine-logo.png"

# MECHANISM: the enumerated right-to-left strings of the essay, each
# with the transliteration the PDF carries instead (declared in the
# essay, Footnote 8). Verified by a full scan of the master: the
# Key's two names, Hebrew and Arabic, and no other RTL strings.
SCRIPT_MAP = {
    "מפתח": "Miftach",
    "مفتاح": "Miftah",
}
# MECHANISM: longest keys first so a whole word is replaced before any
# single letter inside it can be.
SCRIPT_KEYS = sorted(SCRIPT_MAP, key=len, reverse=True)

# MECHANISM: the combining-e substitution of header note 1 — the
# three historical superscript spellings, each to its modifier form.
SUPERSCRIPT_E = {"aͤ": "aᵉ", "oͤ": "oᵉ", "uͤ": "uᵉ", "Aͤ": "Aᵉ", "Oͤ": "Oᵉ", "Uͤ": "Uᵉ"}

FOOTER = "— {n} of {nb} — | All Rights Reserved, Without Prejudice | " \
         "Flagpole of Claim and Coinage reserved"


class AbroadGermanPDF(FPDF):
    """MECHANISM: an FPDF whose every page carries the house footer.

    DOCTRINE: the footer numbers must resolve — {nb} is the alias the
    renderer substitutes with the true total at output time."""

    def footer(self):
        self.set_y(-14)
        self.set_font("serif", "", 8)
        self.cell(0, 8, FOOTER.format(n=self.page_no(), nb="{nb}"),
                  align="C")


def transliterate(text):
    """MECHANISM: apply the two declared substitutions — superscript
    e to its modifier form, RTL strings to their transliterations.

    DOCTRINE: marked substitutions, declared in the document
    (Footnote 8) — never silent ones."""
    for src, dst in SUPERSCRIPT_E.items():
        text = text.replace(src, dst)
    for key in SCRIPT_KEYS:
        text = text.replace(key, SCRIPT_MAP[key])
    return text


def clean(text):
    """MECHANISM: strip Markdown emphasis marks for the page; the
    master keeps them, the PDF does not need them."""
    text = text.replace("**", "").replace("*", "")
    return transliterate(text)


def main():
    lines = MASTER.read_text(encoding="utf-8").splitlines()

    pdf = AbroadGermanPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(20, 16, 20)
    pdf.alias_nb_pages("{nb}")
    pdf.add_font("serif", "", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    pdf.add_font("serif", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
    pdf.add_font("serif", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf")
    pdf.add_page()

    def para(text, size=10.5, style="", align="L", space=2.2, indent=0):
        # MECHANISM: one paragraph per call; the pen is explicitly
        # returned to the left margin after every multi_cell (the
        # house gotcha).
        pdf.set_font("serif", style, size)
        if indent:
            pdf.set_x(pdf.l_margin + indent)
        pdf.multi_cell(pdf.epw - indent, 5.4, text, align=align,
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(space)

    def heading(text, size, space_before=5):
        pdf.ln(space_before)
        pdf.set_font("serif", "B", size)
        pdf.multi_cell(0, size * 0.62, text, align="L",
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2.4)

    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1
        if not line:
            continue
        if line.startswith("!["):  # MECHANISM: the logo slot -> the seal itself.
            w = 42
            pdf.image(str(LOGO), x=(pdf.w - w) / 2, w=w)
            pdf.ln(4)
            continue
        if line == "---":
            pdf.ln(2)
            continue
        if line.startswith("### "):
            heading(clean(line[4:]), 12)
            continue
        if line.startswith("## "):
            heading(clean(line[3:]), 13.5)
            continue
        if line.startswith("# "):
            pdf.set_font("serif", "B", 19)
            pdf.multi_cell(0, 9.5, clean(line[2:]), align="C",
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(2)
            continue
        if line.startswith("|"):
            # MECHANISM: a table is gathered whole and set in small
            # type, one source row per line, pipes become breaths.
            rows = []
            while i <= len(lines) and (line.startswith("|")):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append("  ·  ".join(clean(c) for c in cells))
                if i < len(lines):
                    line = lines[i].strip()
                    i += 1
                else:
                    break
            for r in rows:
                para(r, size=8.6, space=1.1, indent=3)
            pdf.ln(1.5)
            continue
        if line.startswith("> "):
            para(clean(line[2:]), size=11, style="I", align="C", indent=8)
            continue
        if line.startswith("- "):
            para("•  " + clean(line[2:]), indent=5)
            continue
        if re.match(r"^\d+\. ", line):
            para(clean(line), indent=5)
            continue
        # MECHANISM: a plain paragraph may wrap across source lines;
        # gather until a blank or a structural line.
        buf = [line]
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "|", ">", "- ", "---")) \
                    or re.match(r"^\d+\. ", nxt):
                break
            buf.append(nxt)
            i += 1
        para(clean(" ".join(buf)))

    pdf.output(str(OUTPUT))
    print(f"built {OUTPUT} — {pdf.pages_count} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
