#!/usr/bin/env python3
# =============================================================================
# 93 — build_branch_offsets_magvs_pdf.py
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
# MECHANISM: builds THE-BRANCH-OFFSET-REGISTER-MAGVS.pdf from the
# Markdown master in the goal's files/, set in the Lex Stellarrvm
# family registered from pontifex/fonts/lex-stellarrvm/. The body
# face is the Serif; but this register's prose carries letters of
# nine scripts inside its paragraphs (Hebrew, Arabic, Syriac,
# Imperial Aramaic, Armenian, Georgian, Coptic, Glagolitic, and the
# Cyrillic signs), and no single face holds them all — so the
# renderer writes each paragraph as a sequence of RUNS, switching
# faces at script boundaries: a character is set in the first face
# of the house's ordered candidate list whose cmap holds it (Serif
# seats first, then the script-dedicated faces, Sans the catch-all).
# Script runs inside a bold or italic span ride their regular face —
# the script faces carry no bold seat, and the letters are exhibits,
# not emphasis. Letter portrait; the resolving house footer on
# every page via the {nb} alias.
#
# FONT LAW: coverage is audited BEFORE the build against the union
# of every registered face: every non-ASCII codepoint of the master
# must resolve to a face, or the build aborts and names it. No glyph
# is silently dropped — the audit of 2026-11-26 found 124 non-ASCII
# codepoints in the master, all held by the family union.
#
# CONTENT TEST: Inputs — the Markdown master, the Doctrine logo,
# the Lex Stellarrvm faces. Processes — union coverage audit, face
# registration, run-segmented line-wise rendering. Outputs — the
# MAGVS PDF beside the master, and a copy in this research folder.
# Tolerances — the footer count resolves; the page count prints
# at the end of the build.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
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
MASTER = BASE / "THE-BRANCH-OFFSET-REGISTER.md"
OUTPUT = BASE / "THE-BRANCH-OFFSET-REGISTER-MAGVS.pdf"
RESEARCH = HOME / "workspace/pontifex/research/branch-offsets"
LOGO = HOME / "workspace/templates/doctrine-logo.png"
FONT_DIR = HOME / "workspace/pontifex/fonts/lex-stellarrvm"

FAMILY = "Lex Stellarrvm"
SANS = "Lex Stellarrvm Sans"
# family name -> (file, cmap) for every face the renderer may call
FACES = {
    FAMILY: FONT_DIR / "LexStellarrvm-Serif.ttf",
    "LS-Bold": FONT_DIR / "LexStellarrvm-SerifBold.ttf",
    "LS-Oblique": FONT_DIR / "LexStellarrvm-Oblique.ttf",
    SANS: FONT_DIR / "LexStellarrvm-Sans.ttf",
    "LS-Hebrew": FONT_DIR / "LexStellarrvm-Hebrew.ttf",
    "LS-Arabic": FONT_DIR / "LexStellarrvm-Arabic.ttf",
    "LS-Syriac": FONT_DIR / "LexStellarrvm-Syriac.ttf",
    "LS-Imperial": FONT_DIR / "LexStellarrvm-ImperialAramaic.ttf",
    "LS-Armenian": FONT_DIR / "LexStellarrvm-Armenian.ttf",
    "LS-Georgian": FONT_DIR / "LexStellarrvm-Georgian.ttf",
    "LS-Coptic": FONT_DIR / "LexStellarrvm-Coptic.ttf",
    "LS-Glagolitic": FONT_DIR / "LexStellarrvm-Glagolitic.ttf",
    "LS-Ethiopic": FONT_DIR / "LexStellarrvm-Ethiopic.ttf",
    "LS-Signs": FONT_DIR / "LexStellarrvm-Signs.ttf",
    "LS-Symbols": FONT_DIR / "LexStellarrvm-Symbols.ttf",
}
CMAPS = {}
# ordered fallback after the Serif seats: the script-dedicated
# faces in block order, the Signs and Symbols, Sans the catch-all
FALLBACK = ["LS-Hebrew", "LS-Arabic", "LS-Syriac", "LS-Imperial",
            "LS-Armenian", "LS-Georgian", "LS-Coptic",
            "LS-Glagolitic", "LS-Ethiopic", "LS-Signs",
            "LS-Symbols", SANS]
FOOTER = ("— {n} of {nb} — | All Rights Reserved, Without "
          "Prejudice | Flagpole of Claim and Coinage reserved")


def load_cmaps():
    for name, path in FACES.items():
        CMAPS[name] = TTFont(str(path)).getBestCmap()


def face_for(ch, style=""):
    """The (family, style) that sets this character: the Serif seat
    for its style first, then the ordered fallback faces. None if
    no registered face holds it — the audit forbids that case."""
    cp = ord(ch)
    if cp < 128:
        return (FAMILY, style)
    if style == "B" and cp in CMAPS["LS-Bold"]:
        return (FAMILY, "B")
    if style == "I" and cp in CMAPS["LS-Oblique"]:
        return (FAMILY, "I")
    if cp in CMAPS[FAMILY]:
        return (FAMILY, "")
    for name in FALLBACK:
        if cp in CMAPS[name]:
            return (name, "")
    return None


def coverage_audit(text):
    """Every non-ASCII codepoint must resolve to a registered face;
    anything unheld aborts the build, named."""
    bad = sorted({ord(c) for c in text if ord(c) > 127
                  and face_for(c) is None})
    if bad:
        raise SystemExit("UNHELD CODEPOINTS: "
                         + ", ".join(f"U+{cp:04X}" for cp in bad))
    return len({ord(c) for c in text if ord(c) > 127})


class Register(FPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(FAMILY, "", 7.5)
        self.cell(0, 8, FOOTER.format(n=self.page_no(), nb="{nb}"),
                  align="C")


def spans(text):
    """Split a Markdown paragraph into (text, style) spans on the
    ** bold and * italic runs; backticks are stripped, their
    content stands."""
    text = text.replace("`", "")
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if i % 2 == 1:
            out.append((part, "B"))
            continue
        for j, sub in enumerate(re.split(r"\*(.+?)\*", part)):
            out.append((sub, "I" if j % 2 == 1 else ""))
    return [(t, s) for t, s in out if t]


def runs(text, style):
    """Split one span into face runs at script boundaries."""
    out = []
    cur_face, cur = None, ""
    for ch in text:
        f = face_for(ch, style)
        if f != cur_face and cur:
            out.append((cur_face, cur))
            cur = ""
        cur_face, cur = f, cur + ch
    if cur:
        out.append((cur_face, cur))
    return out


def main():
    load_cmaps()
    text = MASTER.read_text(encoding="utf-8")
    n_cp = coverage_audit(text)
    print(f"coverage audit: {n_cp} non-ASCII codepoints, all held")

    pdf = Register("P", "mm", "Letter")
    pdf.alias_nb_pages("{nb}")
    pdf.set_auto_page_break(True, margin=18)
    pdf.set_margins(20, 16, 20)
    pdf.add_font(FAMILY, "", str(FACES[FAMILY]))
    pdf.add_font(FAMILY, "B", str(FACES["LS-Bold"]))
    pdf.add_font(FAMILY, "I", str(FACES["LS-Oblique"]))
    for name in FALLBACK:
        pdf.add_font(name, "", str(FACES[name]))

    def write_spans(body, size, base_style="", align=None):
        if align == "C":
            # centred single lines (the title): measure and place
            total = 0.0
            for t, s in spans(body):
                for (fam, sty), run in runs(t, s or base_style):
                    pdf.set_font(fam, sty, size)
                    total += pdf.get_string_width(run)
            pdf.set_x((pdf.w - total) / 2)
        for t, s in spans(body):
            for (fam, sty), run in runs(t, s or base_style):
                pdf.set_font(fam, sty, size)
                pdf.write(size * 0.52, run)
        pdf.ln(size * 0.52)

    def para(body, size=10.5, space=2.4):
        write_spans(body, size)
        pdf.ln(space)

    def heading(body, size=13.5):
        pdf.ln(3.5)
        write_spans(body, size, base_style="B")
        pdf.ln(2.4)

    pdf.add_page()
    lines = text.split("\n")
    i = 0
    first_block = True
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
        if line.startswith("## "):
            heading(line[3:])
            continue
        if line.strip() == "---":
            y = pdf.get_y()
            pdf.line(20, y, pdf.w - 20, y)
            pdf.ln(3.4)
            continue
        block = [line]
        while i < len(lines) and lines[i].strip() \
                and not lines[i].startswith(("#", "---")) \
                and not lines[i].lstrip().startswith("- "):
            block.append(lines[i].rstrip())
            i += 1
        body = " ".join(b.strip() for b in block)
        if first_block and body.startswith("**THE BRANCH"):
            # the title line rides centred and large; the subtitle
            # follows as its own centred italic line
            title, _, rest = body.partition(" *Subtitle:*")
            pdf.ln(2)
            write_spans(title, 16, align="C")
            pdf.ln(1.5)
            write_spans("*Subtitle:*" + rest, 10, align="C")
            pdf.ln(3)
        else:
            para(body)
        first_block = False

    pdf.output(str(OUTPUT))
    (RESEARCH / OUTPUT.name).write_bytes(OUTPUT.read_bytes())
    print(f"built {OUTPUT.name}: {pdf.pages_count} pages")


if __name__ == "__main__":
    main()
