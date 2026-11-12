#!/usr/bin/env python3
# =============================================================================
# "If it isn't on the page, it didn't happen." — the desk
#
# Thelemic date: Thu 2026-11-12 (Dies Jovis), Sol in Scorpio, Anno V:xii e.n.
#
# 93.
#
# build_divine_nine_abroad_iv_pdf.py — builds
# THE-DIVINE-NINE-ABROAD-IV-THE-SECOND-RECKONING-MAGVS.pdf from the
# Markdown master THE-DIVINE-NINE-ABROAD-IV-THE-SECOND-RECKONING.md:
# the fourth of the founder's Divine Nine Abroad essays — the Second
# Reckoning, in which the Japanese Dialect essay's governing refusal
# (no attested kana letter-value bank) is carried back to the Anchorage
# at the founder's challenge, tested candidate by candidate against a
# thirty-nine-source research dossier (the three modern kazutama banks
# of 2003 and after; the neighbouring arts that do not carry; the
# suppression ledger), ruled FALSE as worded and TRUE as meant, and
# repaired by a dated CORRECTIO, with the full Gate. The master is the
# authority; this script only dresses the essay for the page as its
# Teacher's Revision (MAGVS) edition. Built on the pattern of
# build_divine_nine_abroad_iii_pdf.py, the third essay's builder.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice).
#
# METHOD (Scientific Illuminism): Inputs  — the Markdown master
# THE-DIVINE-NINE-ABROAD-IV-THE-SECOND-RECKONING.md,
# the Doctrine logo PNG, the
# DejaVu font family, and Noto Serif CJK (JP face). Processes — line-wise rendering (title, sections, the
# vowel table as set lines, blockquotes), footer with resolving page
# count via the {nb} alias, Japanese printed in Japanese script: Noto
# Serif CJK (JP) is registered as a fallback font beside the DejaVu body
# (verified glyph by glyph beforehand — see MECHANISM NOTES), so no
# transliteration substitution occurs anywhere in this build; the
# difference from the Hebrew/Arabic precedent is declared in the essay
# itself, Footnote 7. Outputs — the PDF beside the master.
# Tolerances — the page count in every footer must resolve to the true
# count; no line may silently lose a character the fonts cannot carry;
# every key number of the audit (41, 117, 100, 30, 2003, 1294, 485,
# 1779) and every Japanese exhibit (the banks' worked examples, the
# Takeuchi scroll title, the Gobusho) must survive onto the page — the
# desk greps the built text layer for them before signing.
#
# MECHANISM NOTES:
#  * Every multi_cell passes new_x=XPos.LMARGIN, new_y=YPos.NEXT — the
#    house gotcha (AGENTS.md, 2026-10-04): multi_cell(w=0) otherwise
#    parks the pen at the right margin and the next call dies for want
#    of width.
#  * DejaVu Serif carries Latin + Greek honestly (stigma U+03DB,
#    digamma U+03DD, keraia U+02B9 among them) and the IPA dress this
#    essay needs ([\u026f], the combining voiceless ring U+0325, the
#    length mark U+02D0) — verified against the cmap before this build.
#  * The Japanese rides by FALLBACK: Noto Serif CJK Regular/Bold (the
#    .ttc's JP face is the collection's first) is registered as family
#    "cjk" and passed to set_fallback_fonts, so any glyph DejaVu lacks
#    is set in the CJK face mid-line. Every Japanese character in the
#    master was checked against the JP face's cmap before this build —
#    the five vowels, the small kana, the retired seats, and the
#    pre-reform title forms included; none is missing.
#  * No right-to-left strings occur in this master (verified by scan);
#    the sibling builder's SCRIPT_MAP therefore does not ride along.
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
MASTER = BASE / "THE-DIVINE-NINE-ABROAD-IV-THE-SECOND-RECKONING.md"
OUTPUT = BASE / "THE-DIVINE-NINE-ABROAD-IV-THE-SECOND-RECKONING-MAGVS.pdf"
LOGO = Path.home() / "workspace/templates/doctrine-logo.png"


FOOTER = "— {n} of {nb} — | All Rights Reserved, Without Prejudice | " \
         "Flagpole of Claim and Coinage reserved"


class AbroadPDF(FPDF):
    """MECHANISM: an FPDF whose every page carries the house footer.

    DOCTRINE: the footer numbers must resolve — {nb} is the alias the
    renderer substitutes with the true total at output time."""

    def footer(self):
        self.set_y(-14)
        self.set_font("serif", "", 8)
        self.cell(0, 8, FOOTER.format(n=self.page_no(), nb="{nb}"),
                  align="C")


def clean(text):
    """MECHANISM: strip Markdown emphasis marks for the page; the master
    keeps them, the PDF does not need them."""
    return text.replace("**", "").replace("*", "")


def main():
    lines = MASTER.read_text(encoding="utf-8").splitlines()

    pdf = AbroadPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(20, 16, 20)
    pdf.alias_nb_pages("{nb}")
    pdf.add_font("serif", "", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    pdf.add_font("serif", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
    pdf.add_font("serif", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf")
    # MECHANISM: the CJK fallback — registered after the body faces so
    # DejaVu keeps the Latin and Greek, and the JP face supplies only
    # the glyphs DejaVu does not carry (the essay's Footnote 7).
    pdf.add_font("cjk", "", "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc")
    pdf.add_font("cjk", "B", "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc")
    pdf.set_fallback_fonts(["cjk"])
    pdf.add_page()

    def para(text, size=10.5, style="", align="L", space=2.2, indent=0):
        # MECHANISM: one paragraph per call; the pen is explicitly returned
        # to the left margin after every multi_cell (the house gotcha).
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
            # MECHANISM: a table is gathered whole and set in small type,
            # one source row per line, pipes become column breaths.
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
        # MECHANISM: a plain paragraph may wrap across source lines; gather
        # until a blank or a structural line.
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
