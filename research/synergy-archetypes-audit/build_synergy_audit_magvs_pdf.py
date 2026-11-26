#!/usr/bin/env python3
# =============================================================================
# 93 — build_synergy_audit_magvs_pdf.py
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
# MECHANISM: builds THE-SYNERGY-OF-ARCHETYPES-AUDIT-MAGVS.pdf from the
# Markdown master in the goal's files/, set in the Lex Stellarrvm family
# registered from pontifex/fonts/lex-stellarrvm/ (Serif body, SerifBold
# headings), Letter portrait, the resolving house footer on every page
# via the {nb} alias. Every multi_cell passes new_x=XPos.LMARGIN,
# new_y=YPos.NEXT — the fpdf2 pen law of the house.
#
# FONT LAW: coverage is audited against every non-ASCII codepoint of
# the master BEFORE the build, against the registered faces' union;
# an unheld glyph aborts the build and is named. No silent drops.
#
# CONTENT TEST: Inputs — the Markdown master, the Doctrine logo, the
# Lex faces. Processes — coverage audit, registration, line-wise
# rendering. Outputs — the MAGVS PDF beside the master and a copy in
# this research folder. Tolerances — the footer count resolves; the
# page count prints at the end of the build.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import sys
from pathlib import Path

import site
sys.path.insert(0, site.getusersitepackages())

from fontTools.ttLib import TTFont
from fpdf import FPDF
from fpdf.enums import XPos, YPos

HOME = Path.home()
BASE = HOME / "workspace/goals/cross-gematria-777-gap-filling/files"
MASTER = BASE / "THE-SYNERGY-OF-ARCHETYPES-AUDIT.md"
OUTPUT = BASE / "THE-SYNERGY-OF-ARCHETYPES-AUDIT-MAGVS.pdf"
RESEARCH = HOME / "workspace/pontifex/research/synergy-archetypes-audit"
LOGO = HOME / "workspace/templates/doctrine-logo.png"
FONT_DIR = HOME / "workspace/pontifex/fonts/lex-stellarrvm"
FACES = {"Serif": "LexStellarrvm-Serif.ttf", "SerifBold": "LexStellarrvm-SerifBold.ttf",
         "Sans": "LexStellarrvm-Sans.ttf"}

text = MASTER.read_text(encoding="utf-8")

# FONT LAW: audit coverage of every non-ASCII codepoint against the union.
union = set()
for fn in FACES.values():
    union |= set(TTFont(str(FONT_DIR / fn)).getBestCmap())
missing = sorted({c for c in text if ord(c) > 127 and ord(c) not in union})
if missing:
    print("ABORT — unheld glyphs:", [hex(ord(c)) for c in missing]); sys.exit(1)
print(f"font audit: {len({c for c in text if ord(c) > 127})} non-ASCII codepoints, all held")


class Audit(FPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font("Serif", "", 8)
        self.cell(0, 8, f"— {self.page_no()} of {{nb}} — | All Rights Reserved, "
                        "Without Prejudice | Flagpole of Claim and Coinage reserved",
                  align="C")


pdf = Audit("P", "mm", "Letter")
for name, fn in FACES.items():
    pdf.add_font(name, "", str(FONT_DIR / fn))
pdf.set_auto_page_break(True, margin=18)
pdf.set_margins(19, 16, 19)
pdf.alias_nb_pages()
pdf.add_page()
if LOGO.exists():
    pdf.image(str(LOGO), x=88, w=34)
    pdf.ln(4)

for raw in text.splitlines():
    line = raw.rstrip()
    if not line or line == "---" or line.startswith("— 1 of"):
        if line == "---":
            pdf.ln(3)
        continue
    if line.startswith("# "):
        pdf.set_font("SerifBold", "", 17); pdf.multi_cell(0, 8.5, line[2:], new_x=XPos.LMARGIN, new_y=YPos.NEXT); pdf.ln(2)
    elif line.startswith("## "):
        pdf.set_font("SerifBold", "", 12.5); pdf.multi_cell(0, 6.5, line[3:], new_x=XPos.LMARGIN, new_y=YPos.NEXT); pdf.ln(1.5)
    elif line.startswith("- "):
        pdf.set_font("Serif", "", 10); pdf.multi_cell(0, 5.2, "• " + line[2:], new_x=XPos.LMARGIN, new_y=YPos.NEXT); pdf.ln(1)
    else:
        pdf.set_font("Serif", "", 10); pdf.multi_cell(0, 5.2, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT); pdf.ln(1.6)

pdf.output(str(OUTPUT))
(RESEARCH / OUTPUT.name).write_bytes(OUTPUT.read_bytes())
print("built:", OUTPUT, "pages:", pdf.pages_count)
