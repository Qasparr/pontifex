#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_final.py
═══════════════════════════════════════════════════════════════════════════════
"Let your communication be, Yea, yea; Nay, nay."
    — The Gospel According to Matthew 5:37 (KJV)

93.

Date: XXV day of October, Dies Solis, Sol in Scorpio, Anno V:xii e.n. (2026 e.v.)

Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
(Greek, -ARR, All Rights Reserved, Without Prejudice).

Classification: Enterprise • Educational • Research & Development
Method of Science, Aim of Religion.

DOCTRINE
────────
This script builds the FINAL single-volume Teacher's Edition of Black's
Law Dictionary, Second Edition (1910): all 13,145 parsed entries, the
four well-phase annotation sets layered as in Volume I, the fifth-edition
(1979) apparatus mapped per entry, the KJV text-diff corrections applied
and printed as errata, the scan-limitation markers printed where the
scan failed, and the register of headwords new in the fifth edition.

Dispositions in this build are MARKED, never vanished (his clarification,
2026-10-25 14:14 EDT): the SANS JOUR footnote stands in place, struck
through and labeled; every KJV correction prints its old reading beside
the new; every scan gap carries its marker in the open. Nothing is
silently corrected, silently removed, or silently completed.

Copyright boundary, absolute: no fifth-edition entry text appears
anywhere in this book — headwords and status only.

MECHANISM
─────────
1. Load entries.json; clean bodies R1–R4 (identical to the base and
   Vol. I builders; the foundation text is unchanged).
2. Apply the KJV corrections to the Scripture phase data by (key, idx)
   locator, asserting the recorded old reading before any swap.
3. Join the four well sets (REHOME table as Vol. I; law/LAST stands
   excluded for want of a host — disclosed in §VII of the book).
4. Typeset: cover frontispiece; directive-format front matter (apparatus
   key + census reconciliation, marker definitions, errata + flags);
   entries with per-entry 5e apparatus, scan markers at their loci, and
   well footnotes (red-letter rule as Vol. I); register appendix;
   colophon.
5. Print build stats as JSON for the coordinator's verification.

93 93/93.

"Do what thou wilt shall be the whole of the Law."
    — Liber AL vel Legis I:40
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
BASE = Path.home() / "workspace/your_files/blacks-teachers-editions"
ENTRIES_JSON = BASE / "2e/entries.json"
LAW_JSON = BASE / "well-phases/phase-1-law/law-well-annotations.json"
SCR_JSON = BASE / "well-phases/phase-2-scripture/scripture-well-annotations.json"
HH_JSON = BASE / "well-phases/phase-3-hiphop/hiphop-well-annotations.json"
HUM_JSON = BASE / "well-phases/phase-4-humanity/humanity-well-annotations.json"
MAPPING_JSON = HERE / "work-census/mapping.json"
REGISTER_JSON = HERE / "work-census/register.json"
CORRECTIONS_JSON = HERE / "work-kjv/corrections.json"
FLAGS_JSON = HERE / "work-kjv/flags.json"
MARKERS_JSON = HERE / "work-scan/markers.json"
COVER_PNG = (Path.home() / "workspace/your_files/blacks-hardcover-designs"
             / "cover-iv-scales.png")
OUT_PDF = HERE / "blacks-2e-final-teachers-edition.pdf"

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT_REG = FONT_DIR / "DejaVuSans.ttf"
FONT_BLD = FONT_DIR / "DejaVuSans-Bold.ttf"

THELEMIC_DATE = ("XXV day of October, Dies Solis, Sol in Scorpio, "
                 "Anno V:xii e.n. (2026 e.v.)")
AUTHOR_LINE = ("Authorship attributed exclusively to Johnathan "
               "'Qasparr' Monroe (Greek, -ARR, All Rights Reserved, "
               "Without Prejudice)")
FLAGPOLE = ("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, "
            "ARR, All Rights Reserved, Without Prejudice. Right of claim "
            "hereby reserved and coined under the authority of the "
            "Living Man.")
HONEST_LABEL = ("PARSED AND CLEANED — SCAN-VERIFICATION PENDING. "
                "NOT AUDITED.")
BLOOD = (163, 18, 18)
RUST = (150, 55, 35)
STRUCK_LABEL = (
    "STRUCK — per ruling 2026-10-25. This annotation was ruled a thin "
    "Law footnote and struck. By the Architect's clarification of the "
    "same day it is NOT removed: it stands here, struck through, so "
    "the record shows the annotation and its disposition together.")
MARK_STRONG = "[TEXT INCOMPLETE — scan limitation]"
MARK_CANDIDATE = "[TEXT POSSIBLY INCOMPLETE — scan candidate]"

# ═══════════════════════════════════════════════════════════════════════════
# The REHOME table and DROP/EXCLUSION records — identical to the Vol. I
# layered build (build_vol1_layered.py), which see for the verification
# notes on every target. LAST (law) stands excluded: the 'last clear
# chance' text it claimed appears nowhere in the 13,145 entries; the
# annotation is preserved in the phase JSON and the exclusion is
# disclosed in §VII of this book.
# ═══════════════════════════════════════════════════════════════════════════
REHOME = {
    ("law", "AT ARM'S LENGTH"): "AT ARM’S LENGTH",
    ("law", "BAIL"): "BAHADUM",
    ("law", "COMMENDATIO"): "COMMENDATXO",
    ("law", "COMMON LAW"): "COMMON BENCH",
    ("law", "COMMORIENTES"): "COMMORXENTES",
    ("law", "COSAS COMUNES"): "COSAS COMUSES",
    ("law", "COUNSEL"): "COUNCIL OF THE NORTH",
    ("law", "CREPUSCULUM"): "CREPUSGUL1TM",
    ("law", "CY-PRES"): "GY-PRES",
    ("law", "DAMNI INJURIAE ACTIO"): "DAMNATU8",
    ("law", "DAY"): "DAUPHIN",
    ("law", "DAYLIGHT"): "DAYXIGHT",
    ("law", "DE AEQUITATE"): "DE -XQUITATE",
    ("law", "DE ARBITRATIONE FACTA"): "DE ARBITRATIONS FACTA",
    ("law", "DE ARRESTANDIS BONIS NE DISSIPENTUR"): "DE ARRE8TANPI8 BONIS NE DISSIPENTUR",
    ("law", "DE BIEN ET DE MAL"): "DE BIEN ET DE MAE",
    ("law", "DE BONA MEMORIA"): "DE BONE MEMORIE",
    ("law", "DISCOVERY"): ("idx", 3921),
    ("law", "DUE"): "DUCROERE",
    ("law", "EN MORT MEYNE"): "EN MOST MEYNE",
    ("law", "EXPATRIATION"): "EXORDIUM",
    ("law", "EXTERRITORIALITY"): "EXTERRITORIAXITY",
    ("law", "FABRICARE"): "FABRIC ARE",
    ("law", "FALSUS"): "F ALSUS",
    ("law", "FATUM"): "FATOM",
    ("law", "FLAG"): "IX AO",
    ("law", "FOR"): ("idx", 5322),
    ("law", "IMPEACHMENTS"): "COURT FOR THE RELIEF OF INSOLVENT DEBTORS",
    ("law", "JURA"): "JUBA",
    ("law", "JURARE"): "JUR ARE",
    ("law", "KING'S EVIDENCE"): "KING’S EVIDENCE",
    ("law", "LAND"): "LANCETI",
    ("law", "LAS PARTEDAS"): "LAS PARTED AS",
    ("law", "LATA GULPA"): "LATA GULP A",
    ("law", "LETTER"): "LETBADO",
    ("law", "LIBEL"): "LIAKD",
    ("law", "LIBERTY"): "LIBERTIES",
    ("law", "LITEM SUAM FACERE"): "LITEM SHAM FACERE",
    ("law", "MANDAMUS"): "MANDAMIENTO",
    ("law", "MANUMISSION"): "MANJTMISSION",
    ("law", "NOVODAMUS"): "NOVODAKUB",
    ("law", "PUBLICATION"): "PUBLICANUS",
    ("scripture", "A MENSA ET THORO"): "A MENS A ET THORO",
    ("scripture", "ACCEPTILATION"): "ACCEPTTLATION",
    ("scripture", "ACCREDULITARE"): "ACOREDUUTARE",
    ("scripture", "AD WABACTUM"): "AS WABACTUM",
    ("scripture", "ADDICTIO"): "ASDICTIO",
    ("scripture", "ADMINICULATOR"): "ADMINICUXATOR",
    ("scripture", "ADSTIPULATOR"): "ADSTIFULATOR",
    ("scripture", "ADVOCATIONE DECIMARUM"): "ADVOCATIONE DECIMARTJM",
    ("scripture", "AEDILITUM EDICTUM"): "JEDELITUM EDICTUM",
    ("scripture", "AES"): "JES",
    ("scripture", "AESTIMATIO CAPITIS"): "ABSTIMATIO CAPITIS",
    ("scripture", "AFFRANCHIR"): "AFFRANCHXR",
    ("scripture", "COMPROMISSARIUS"): "COMPROMISSARITJS",
    ("scripture", "DIGAMY"): "DIFFORCIARE",
    ("scripture", "DISAFFIRM"): "D IS AFFIRM",
    ("scripture", "DISCOVERY"): ("idx", 3921),
    ("scripture", "DISINTERESTED"): "DISINTER",
    ("scripture", "DIVINARE"): "D IVIN ARE",
    ("scripture", "DOMINICA PALMARUM"): "DOMINICA PALM ARUM",
    ("scripture", "DONNEUR D'AVAL"): "DONNEUR D’AVAX",
    ("scripture", "DOWER"): "DOWEB",
    ("scripture", "DRY-CRAEFT"): "DRY-CRJEFT",
    ("scripture", "DURESS"): "DURESS, 17",
    ("scripture", "EJIDOS"): "EJXDOS",
    ("scripture", "EMBASSAGE"): "EMBASSADOR",
    ("scripture", "EMBLER DE GENTZ"): "EMBLEM BE GENTZ",
    ("scripture", "EMBRACERY"): "EMBBACEBY",
    ("scripture", "EMENDA"): "EMEND A",
    ("scripture", "IN GENUITAS"): "IN GENUIT AS",
    ("scripture", "IN PIOS USUS"): "IN PIOS TXSUS",
    ("scripture", "IN VINCULIS"): "IN VTNCULIS",
    ("scripture", "INSCRIBERE"): "XNSCRIBERE",
    ("scripture", "ITA TE DEUS ADJUVET"): "ITA TE DEVS ADJUVET",
    ("scripture", "RELEASE"): "RELAXATION",
    ("scripture", "RENDER"): "RENCOUNTER",
    ("scripture", "TRANSGRESSIO"): "TRANSGRE8SIO",
    ("scripture", "ULTIMUM SUPPLICIUM"): "ULTIMUM SUFPLICIUM",
    ("scripture", "UNITAS PERSONARUM"): "UNITAB PERSONARUM",
    ("scripture", "UNTHRIFT"): "UN THRIFT",
    ("scripture", "WIFE'S EQUITY"): "WIFE’S EQUITY",
    ("humanity", "GYNARCHY"): "GYLTW1TE",
}
DROP_LOG = [("law", "LAST")]
EXCLUDED_VERIFIED = [
    ("humanity", "SELF-DEFENSE"), ("humanity", "SERVITUDE"),
    ("humanity", "SILENCE"), ("scripture", "POSTERITY"),
]
WELL_ORDER = ["law", "scripture", "hiphop", "humanity"]
WELL_SIGLA = {"law": "[Law]", "scripture": "[Scripture]",
              "hiphop": "[Hip-hop]", "humanity": "[Humanity]"}
WELL_NAMES = {"law": "Law", "scripture": "Scripture",
              "hiphop": "Hip-hop", "humanity": "Humanity / Fiction & Film"}


class Cleaner:
    """Cleanup rules R1–R4 — identical to the base and Vol. I builders."""
    def __init__(self):
        self.counts = {"R1_tabs": 0, "R2_multispace": 0,
                       "R3_hyphen_join": 0, "R4_trailing_ws": 0}

    def clean(self, text: str) -> str:
        n = text.count("\t")
        if n:
            self.counts["R1_tabs"] += n
            text = text.replace("\t", " ")
        def _squash(m):
            self.counts["R2_multispace"] += 1
            return " "
        text = re.sub(r" {2,}", _squash, text)
        def _join(m):
            self.counts["R3_hyphen_join"] += 1
            return m.group(1)
        text = re.sub(r"-\s*\n\s*([a-z])", _join, text)
        lines = text.split("\n")
        stripped = [ln.rstrip() for ln in lines]
        self.counts["R4_trailing_ws"] += sum(
            1 for a, b in zip(lines, stripped) if a != b)
        return "\n".join(stripped).strip()


from fpdf import FPDF


class BlacksPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 10,
                  f"\u2014 {self.page_no()} of 00000 \u2014 | "
                  f"All Rights Reserved, Without Prejudice | "
                  f"Flagpole of Claim and Coinage reserved",
                  align="C")


def probe_strikethrough() -> bool:
    """Verify fpdf2 renders the strikethrough style before relying on it."""
    try:
        p = FPDF()
        p.add_font("DejaVu", "", str(FONT_REG))
        p.add_page()
        p.set_font("DejaVu", "S", 10)
        p.cell(0, 10, "probe")
        p.output()
        return True
    except Exception:
        return False


def normalize_annotation(well, raw, source_key):
    text = raw.get("note", "") or ""
    bridge = None
    if well == "hiphop":
        lyric = raw.get("lyric") or raw.get("quote")
        if lyric:
            text = lyric
            bridge = raw.get("note", "")
    verbatim = True
    if well == "humanity" and "(paraphrase)" in text.lower():
        verbatim = False
    return {
        "well": well,
        "text": text,
        "bridge": bridge,
        "citation": raw.get("citation", ""),
        "reasoning": raw.get("reasoning", ""),
        "verbatim": verbatim,
        "deity_verbatim": bool(raw.get("deity_verbatim", False)),
        "rehome_note": None,
        "source_key": source_key,
        "struck": (well == "law" and source_key == "SANS JOUR"),
    }


def anchor_regex(anchor: str) -> re.Pattern:
    parts = re.split(r"(\s+)", anchor)
    pat = "".join(r"\s+" if p.isspace() else re.escape(p) for p in parts)
    return re.compile(pat)


def build() -> dict:
    stats = {}
    strike_ok = probe_strikethrough()
    stats["strikethrough_ok"] = strike_ok

    # ── load corpus ──
    entries = json.loads(ENTRIES_JSON.read_text(encoding="utf-8"))
    head_to_idxs = {}
    for i, e in enumerate(entries):
        head_to_idxs.setdefault(e["headword"], []).append(i)
    cleaner = Cleaner()
    bodies = [cleaner.clean(e.get("body", "") or "") for e in entries]
    stats["entries"] = len(entries)
    stats["cleanup"] = cleaner.counts

    # ── load wells ──
    phase_data = {
        "law": json.loads(LAW_JSON.read_text(encoding="utf-8")),
        "scripture": json.loads(SCR_JSON.read_text(encoding="utf-8")),
        "hiphop": json.loads(HH_JSON.read_text(encoding="utf-8")),
        "humanity": json.loads(HUM_JSON.read_text(encoding="utf-8")),
    }
    for well, key in EXCLUDED_VERIFIED:
        assert key not in phase_data[well], f"phantom key present: {well}/{key}"
    stats["phantom_keys_absent"] = True

    # ── apply KJV corrections (assert old reading before any swap) ──
    corrections = json.loads(CORRECTIONS_JSON.read_text(encoding="utf-8"))
    applied = 0
    for c in corrections:
        cur = phase_data["scripture"][c["key"]][c["idx"]]["note"]
        assert cur == c["old_note"], (
            f"KJV correction locator mismatch at {c['key']}[{c['idx']}] — "
            f"refusing to misapply")
        phase_data["scripture"][c["key"]][c["idx"]]["note"] = c["new_note"]
        applied += 1
    stats["kjv_corrections_applied"] = applied
    flags = json.loads(FLAGS_JSON.read_text(encoding="utf-8"))
    stats["kjv_flags_printed"] = len(flags)

    # ── drops (no honest host — the standing Vol. I merge state) ──
    dropped = 0
    for well, key in DROP_LOG:
        if key in phase_data[well]:
            dropped += len(phase_data[well].pop(key))
    stats["dropped_last_annotations"] = dropped

    # ── join with re-homing (as Vol. I) ──
    footnotes = {i: [] for i in range(len(entries))}
    rehome_count = 0
    direct_count = 0
    for well in WELL_ORDER:
        for key, anns in phase_data[well].items():
            target = REHOME.get((well, key))
            idxs = None
            rehome_note = None
            if target is not None:
                rehome_count += 1
                if isinstance(target, tuple) and target[0] == "idx":
                    idxs = [target[1]]
                    rehome_note = (f"re-homed from {key!r} to entries.json "
                                   f"index {target[1]} (duplicate headword, "
                                   f"sense-matched)")
                else:
                    idxs = head_to_idxs.get(target, [])
                    rehome_note = (f"re-homed from {key!r} to {target!r} "
                                   f"(OCR headword / parser-merge artifact)")
                if not idxs:
                    raise RuntimeError(f"re-home target missing: {well}/{key}")
            else:
                idxs = head_to_idxs.get(key, [])
                if not idxs:
                    raise RuntimeError(f"orphan annotation key: {well}/{key}")
                direct_count += 1
                if len(idxs) > 1:
                    idxs = idxs[:1]
            for a in anns:
                fn = normalize_annotation(well, a, key)
                if rehome_note:
                    fn["rehome_note"] = rehome_note
                for i in idxs:
                    footnotes[i].append(fn)
    per_well = Counter()
    entries_with_notes = 0
    red_letter = 0
    struck_found = 0
    for i, fns in footnotes.items():
        if fns:
            entries_with_notes += 1
            for fn in fns:
                per_well[fn["well"]] += 1
                if fn["deity_verbatim"]:
                    red_letter += 1
                if fn["struck"]:
                    struck_found += 1
    stats["per_well"] = dict(per_well)
    stats["entries_with_notes"] = entries_with_notes
    stats["red_letter"] = red_letter
    stats["sans_jour_marked"] = struck_found
    stats["rehomes"] = rehome_count
    stats["direct_joins"] = direct_count

    # ── mapping + markers + register ──
    mapping = {int(k): v for k, v in
               json.loads(MAPPING_JSON.read_text(encoding="utf-8")).items()}
    markers = {int(k): v for k, v in
               json.loads(MARKERS_JSON.read_text(encoding="utf-8")).items()}
    register = json.loads(REGISTER_JSON.read_text(encoding="utf-8"))
    stats["mapping_entries"] = len(mapping)
    stats["marker_entries"] = len(markers)
    stats["markers_total"] = sum(len(v) for v in markers.values())
    stats["register_entries"] = len(register)

    # ── typeset ──
    pdf = BlacksPDF("P", "mm", "Letter")
    pdf.set_margins(25, 25, 25)
    pdf.set_auto_page_break(True, 25)
    pdf.add_font("DejaVu", "", str(FONT_REG))
    pdf.add_font("DejaVu", "B", str(FONT_BLD))
    pdf.alias_nb_pages("00000")

    def h1(t, size=22):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 9, t, align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    def h2(t, size=14):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 8, t, align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    def h3(t, size=12):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 7, t, align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    def para(t, size=11, bold=False, align="J", color=(0, 0, 0)):
        pdf.set_font("DejaVu", "B" if bold else "", size)
        pdf.set_text_color(*color)
        pdf.multi_cell(0, 6, t, align=align, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1.5)

    def roman_section(numeral, title, paragraphs, footnotes_):
        pdf.add_page()
        h2(f"{numeral}. {title}", 15)
        pdf.ln(2)
        for p in paragraphs:
            para(p, 11)
        if footnotes_:
            pdf.ln(2)
            pdf.set_draw_color(150, 150, 150)
            pdf.line(25, pdf.get_y(), 80, pdf.get_y())
            pdf.ln(2)
            for i, fn in enumerate(footnotes_, 1):
                para(f"{i}. {fn}", 9)

    def marker_line(text):
        pdf.set_font("DejaVu", "B", 8.5)
        pdf.set_text_color(*RUST)
        pdf.multi_cell(0, 5, text, align="L", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(0.5)

    # ── FRONTISPIECE — Design IV, the Scales of Ma'at (his ruled cover) ──
    pdf.add_page()
    img_w = 138.0
    img_h = img_w * 1792 / 1280
    pdf.image(str(COVER_PNG), x=(215.9 - img_w) / 2, y=22, w=img_w, h=img_h)
    pdf.set_y(22 + img_h + 8)
    para("Design IV — The Scales of Ma'at.", 11, bold=True, align="C")
    para("His ruled cover for the main text: the full dictionary under "
         "the Scales; the Teacher's Edition with the audits under the "
         "Open Word. This single volume carries both.", 9.5, align="C")

    # ── TITLE PAGE ──
    pdf.add_page()
    pdf.ln(10)
    para("DOCTRINE — BLACK'S LAW DICTIONARY, SECOND EDITION", 10,
         bold=True, align="C")
    h1("BLACK'S LAW DICTIONARY", 26)
    h2("Second Edition — West Publishing Co., 1910", 15)
    h3("THE FINAL TEACHER'S EDITION — One Volume Complete", 13)
    h3("The Complete Text with the Four Wells, the Fifth-Edition "
       "Apparatus, the Errata, and the Register of New Headwords", 11)
    h3("Under the Scales of Ma'at — Law, Scripture, Hip-hop, Humanity", 11)
    pdf.ln(4)
    para(AUTHOR_LINE, 10, align="C")
    para(f"this {THELEMIC_DATE}", 10, align="C")
    pdf.ln(2)
    para("Classification: Enterprise \u2022 Educational \u2022 "
         "Research & Development", 10, align="C")
    para("Method of Science, Aim of Religion", 10, align="C")
    pdf.ln(4)
    pdf.set_fill_color(255, 243, 224)
    pdf.set_font("DejaVu", "B", 12)
    pdf.multi_cell(0, 8, HONEST_LABEL, align="C", fill=True,
                   new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    para("This volume carries the complete parsed text of the 1910 "
         "second edition, layered with the four well-phase annotation "
         "sets, the fifth-edition apparatus mapped entry by entry, the "
         "KJV text-diff errata, and open markers wherever the scan of "
         "the original failed. It has not yet passed the TRVVTH "
         "scan-verification audit; that audit is the 2027 work. Nothing "
         "in these pages claims 'audited' or 'restored.' Every "
         "annotation is a finding, never doctrine, until his red pen "
         "rules.", 10)
    pdf.ln(4)
    para(FLAGPOLE, 9, bold=True, align="C")

    # ── FRONT MATTER ──
    roman_section(
        "I", "STATEMENT OF THE WORK",
        ["This is the final Teacher's Edition of Black's Law "
         "Dictionary, Second Edition (1910), complete in one volume: "
         "the full dictionary text with the Four Wells layered entry by "
         "entry — Law, Scripture, Hip-hop, and Humanity with Fiction & "
         "film — together with the Teacher's apparatus that the "
         "two-volume plan reserved for the second volume: the "
         "fifth-edition mapping, the KJV errata, the scan-limitation "
         "markers, and the register of headwords new in the fifth "
         "edition. The two-volume set (the dictionary under the Scales "
         "of Ma'at; the Teacher's Edition under the Open Word) is here "
         "married into a single book, at his order.",
         "The honest label on the title page is the load-bearing beam "
         "of this volume. A text that claimed audit it had not done "
         "would be false in one thing, and therefore suspect in all. "
         "Where the scan of the original failed, this book says so, in "
         "the open, at the very place of the failure (§VI). Where a "
         "ruling has marked a footnote, the footnote stands marked, "
         "not vanished (§VII). The gaps in these pages are limitations "
         "of the scan-to-text process, openly shown — nothing is being "
         "hidden, and nothing has been editorially omitted."],
        ["The Gospel According to Matthew 5:37 (KJV): 'let your "
         "communication be, Yea, yea; Nay, nay.'",
         "Legal maxim: falsus in uno, falsus in omnibus — false in one "
         "thing, false in all."])

    roman_section(
        "II", "SOURCE, METHOD, AND MERGE",
        ["Source: the Internet Archive OCR text of the 1910 second "
         "edition, title page verified as Second Edition, West "
         "Publishing Co., 1910. The parser recovered 13,145 entries.",
         "Base method: four deterministic cleanup rules — tabs to "
         "spaces, multiple spaces collapsed (paragraph breaks "
         "preserved), OCR line-break hyphenation rejoined, trailing "
         "whitespace stripped. Glyph misreads are deliberately NOT "
         "corrected in the base text; they wait for scan evidence in "
         "the 2027 audit. Two classes of change ARE made in this "
         "final build, each logged and each printed in the open: the "
         "eight KJV transcription corrections in the Scripture "
         "annotations (§VII, old reading beside new), and nothing "
         "else. No other word of the base text or the annotations is "
         "altered.",
         "Merge method: annotation keys are the workers' chunk-exact "
         "OCR headwords, joined to entries on exact match. Where a key "
         "did not match — OCR-normalized spellings, or definitions "
         "fused by the parser into neighboring entries' bodies — the "
         "coordinators' placement notes were applied, each verified "
         "against the actual entry bodies (83 re-homes), and every "
         "move logged in the build log. Three Phase 4 annotations "
         "— for SELF-DEFENSE, SERVITUDE, and SILENCE — found no "
         "parsed entry to attach to (the parse left those "
         "headwords' text unsegmented inside preceding entries) "
         "and were struck at phase merge in 2026, preserved in "
         "the worker's struck file; the annotations were never "
         "part of this book. One Law annotation (LAST) stands "
         "excluded, as it has since the merge, because the text it "
         "claimed to illuminate exists nowhere in the 13,145 entries; "
         "the exclusion and its reason are disclosed at §VII, and the "
         "annotation itself remains preserved in the phase data.",
         "Dispositions in this book are marked, never vanished — the "
         "Architect's standing rule, so that a future researcher "
         "retracing the work can see what was marked, why, and by "
         "whom.",
         "Footnotes are reference material, not legal advice; no "
         "legal effect is claimed by any of them."],
        ["The First Epistle to the Thessalonians 5:21 (KJV): 'Prove "
         "all things; hold fast that which is good.'",
         "Nullius in verba — 'take nobody's word for it.'"])

    roman_section(
        "III", "THE FOUR WELLS AND THE KJV TEXT-DIFF",
        [f"Four phases, each a full pass of all 13,145 entries through "
         f"one well, each with its own audit, each worked by a fresh "
         f"team of 24 agents whose ultra-verbose thought logs are "
         f"preserved for future analysis. Yield: Law — "
         f"{per_well['law']} footnotes; Scripture — "
         f"{per_well['scripture']} footnotes ({red_letter} in the "
         f"deity's own voice, red-lettered); Hip-hop — "
         f"{per_well['hiphop']} footnotes; Humanity with Fiction & "
         f"film — {per_well['humanity']} footnotes. "
         f"{entries_with_notes} entries carry at least one footnote; "
         f"the rest stand bare — the emptiness is a finding, not a "
         f"failure.",
         "Discipline: genuine links only, verbatim or not at all, "
         "never force-fit, never fabricated. Where a well had nothing "
         "genuine for an entry, nothing was drawn.",
         "The KJV text-diff — the Scripture workers' standing "
         "recommendation, executed for this build: every one of the "
         "1,621 Scripture annotations was mechanically diffed against "
         "the King James Version (Project Gutenberg #10; the verse "
         "index validated at 31,102 verses in 66 books, and "
         "cross-checked against a second structured transcription on "
         "all 833 distinct cited verses). Result: 1,424 exact, 176 "
         "clean partial quotations, 8 genuine transcription errors "
         "(corrected in the text; printed at §VII with their old "
         "readings), 10 flagged, 1 wrong reference (flagged, not "
         "altered — reference correction is the Architect's pen "
         "alone), and 2 excluded as non-KJV (the Qur'an annotations). "
         "Measured plainly: 98.8% of the KJV annotations stood exact "
         "or clean partial as written. The two public transcriptions "
         "of the KJV themselves disagree at a handful of verses; "
         "where an annotation follows the other printing, it is "
         "flagged as an edition variant, never 'corrected' toward "
         "one printing over another."],
        ["Ecclesiastes 3:1 (KJV): 'To every thing there is a season, "
         "and a time to every purpose under the heaven.'",
         "Festina lente — 'make haste slowly.'"])

    roman_section(
        "IV", "THE RED-LETTER RULE",
        ["In this volume, the verbatim speech of a deity is set in "
         "blood red, so the reader knows a deity is speaking — the "
         "classic red-letter edition convention. This covers Jesus' "
         "verbatim words, first-person divine speech ('Thus saith the "
         "LORD'), and any deity's verbatim words in any scripture. "
         "Narrative about a deity stays in the body ink.",
         f"{red_letter} Scripture footnotes carry the red letter in "
         "this volume."],
        ["The Gospel According to John 1:1 (KJV): 'In the beginning "
         "was the Word, and the Word was with God, and the Word was "
         "God.'"])


    roman_section(
        "V", "THE FIFTH-EDITION APPARATUS — KEY AND RECONCILIATION",
        ["Beneath every entry in this book stands one apparatus line, "
         "giving that entry's fate in the fifth edition (West, 1979) "
         "exactly as the census data supports — no more. The line "
         "reads one of two ways: 'Carried into the 5th edition "
         "(1979)' (with the fifth edition's own headword form shown "
         "when it differs from this book's headword beyond case and "
         "punctuation), or 'Not carried into the 5th edition (1979)'.",
         "Method: the fifth-edition census was regenerated from the "
         "cleaned fifth-edition study text and the second-edition "
         "scan text, reproducing its published figures exactly — "
         "21,979 unique fifth-edition headwords; 12,892 unique "
         "headwords in the census's own second-edition parse; 3,881 "
         "survived; 9,011 lost; 18,098 new. The join key is the "
         "normalized headword (lowercase alphanumeric). This book's "
         "apparatus is counted per ENTRY of the shipped base parse "
         "(13,145 entries over 13,028 distinct keys): 3,872 entries "
         "carried, 9,273 not carried. The two survivals — 3,881 "
         "census keys, 3,872 book entries — are both correct; they "
         "count different sets, and the difference is the parse "
         "divergence reconciled below.",
         "The 253 reconciliation, in brief: the census's turnover "
         "was computed against its own 12,892-key parse, not against "
         "this book's 13,145 entries. The gap decomposes exactly, "
         "with zero residue: 253 = 117 duplicate-key collapses inside "
         "the base parse (91 keys carrying extra entries — genuine "
         "repeated entries that normalize identically) + 522 "
         "base-only keys − 386 census-only keys. The base-only keys "
         "are headwords the census parser's rules could not crown: "
         "182 carry commas (inverted titles), 161 are headwords "
         "wrapped across two or three scan lines (the census crowns "
         "their tail fragments under other keys), 70 carry periods "
         "(dotted initialisms), 66 carry the curly apostrophe, and "
         "the remaining 43 fall to length minima, parentheses, a "
         "page-artifact guard, and one ornament-defeated anchor. The "
         "full decomposition, with examples and the census-side "
         "partition, is published with this build's data files "
         "(reconciliation.md).",
         "Changed form: the apparatus prints NO changed-form state, "
         "because the data does not support one. Two stated methods "
         "for detecting same-lemma form changes (trailing-plural "
         "normalization; Levenshtein distance ≤ 1) were tested "
         "against lemma-checked samples at a pre-set 100% precision "
         "gate, and both failed it (56.7% and 63.3% — the failures "
         "are distinct entries one letter apart, of the ACT/ACTS "
         "kind). Printing near-matches as fates would assert what "
         "was not verified. The candidate pairs stand recorded as "
         "UNCHARTED in the census work files, for a future pass under "
         "a fresh, pre-registered sample.",
         "Copyright boundary, absolute: this apparatus carries "
         "headwords and status only. No fifth-edition definition "
         "text appears anywhere in this book — the same analytical "
         "line the married Teacher's Edition kept. The fifth edition "
         "remains in copyright; its text stays private."],
        ["The Gospel According to Luke 14:28 (KJV): 'For which of "
         "you, intending to build a tower, sitteth not down first, "
         "and counteth the cost.'"])

    roman_section(
        "VI", "SCAN-LIMITATION MARKERS — WHAT THE MARKS MEAN",
        ["This book marks, in the open and at the very place of the "
         "failure, every locus its rules detect where the text is "
         "incomplete because of the scan of the original. The marks "
         "mean: the scan-to-text process failed here. They do not "
         "mean the editors omitted anything. Nothing behind a mark "
         "has been reconstructed, completed, or invented; repair "
         "belongs to the 2027 scan-verification audit, which will "
         "work from the scan images themselves.",
         f"Two marks are used. The strong mark — {MARK_STRONG} — "
         "prints where the break is definite: an entry body empty in "
         "the scan (23 loci), a body ending mid-word on a hyphen "
         "(49), a body ending on a comma (49), a passage degenerated "
         "into letter-digit garble (4, including the headword "
         "JU8TITIA), or a defect flagged by the 2026 stratified "
         "audit (8). The candidate mark — " + MARK_CANDIDATE + " — "
         "prints where the pattern is consistent with scan loss but "
         "may be authorial: a body ending without terminal "
         "punctuation (601), or an entry whose scan verification "
         "stands OPEN on the stratified audit's record (44). In "
         "all, 775 marks over 772 entries: 132 strong, 643 "
         "candidate.",
         "The candidate mark's honesty cuts both ways, and the "
         "reader should know it: most no-terminal-punctuation loci "
         "are probably complete entries whose final period the scan "
         "dropped, not missing text. They are marked anyway — as "
         "candidates, in the weaker form — because among them stand "
         "real truncations, and silence would hide those. Where a "
         "pattern is known to be authorial, it is not marked at "
         "all: 146 entries ending on an authority's name (the "
         "dictionary's own citation habit) were excluded from the "
         "candidate rule, and short one-line definitions and "
         "see-references — complete entries, authorially brief — "
         "carry no mark. The full marker census, with every locus "
         "and its rule, is published with this build's data files "
         "(marker-census.md), so any mark can be retraced to its "
         "reason."],
        ["The Book of Job 38:11 (KJV): 'Hitherto shalt thou come, "
         "but no further.' — the mark shows where the text, as "
         "scanned, comes to its hitherto."])

    # ── §VII — errata, flags, and marked dispositions (from the data) ──
    pdf.add_page()
    h2("VII. ERRATA, FLAGS, AND MARKED DISPOSITIONS", 15)
    pdf.ln(2)
    para("Corrections applied. Eight Scripture annotations carried "
         "genuine transcription errors against the King James text. "
         "They are corrected in the entries, and printed here with "
         "their old readings beside the new — the correction is "
         "applied, and the record of what stood before stands with "
         "it.", 11)
    for i, c in enumerate(corrections, 1):
        para(f"{i}. {c['key']} — {c['ref']}", 9.5, bold=True)
        para(f"As annotated: \u201c{c['old_note']}\u201d", 9)
        para(f"As corrected: \u201c{c['new_note']}\u201d", 9)
    pdf.ln(2)
    para("Flags — texts unchanged. Eleven annotations are flagged "
         "below and stand in the entries exactly as written. A flag "
         "is not a correction; where a reference itself is wrong, "
         "its correction belongs to the Architect's pen alone.", 11)
    for i, f in enumerate(flags, 1):
        para(f"{i}. {f['key']} — {f['ref']}. {f['reason']}", 9)
    pdf.ln(2)
    para("Marked dispositions. (1) SANS JOUR (Law well): ruled a "
         "thin footnote and struck, 2026-10-25. It stands in its "
         "entry below, struck through and labeled — marked, not "
         "removed — so the record shows the annotation and its "
         "disposition together. (2) LAST (Law well): one annotation "
         "stands excluded from print, as it has since the merge, "
         "because the 'last clear chance' text it claimed to "
         "illuminate exists nowhere in the 13,145 entries — there "
         "is no honest locus to attach it to. The exclusion is "
         "disclosed here rather than silent; the annotation itself "
         "remains preserved in the phase data. (3) Three "
         "annotations written in Phase 4 (Humanity) — for "
         "SELF-DEFENSE, SERVITUDE, and SILENCE — were struck at "
         "phase merge in 2026 and preserved in that worker's "
         "struck file (worker-21-STRUCK-phantom-keys.json). The "
         "ground was hostlessness, stated exactly: the three are "
         "genuine headwords of the 1910 book, but the base parse "
         "did not segment their entries — their definition text "
         "stands in this book unseparated at the tail of the "
         "preceding parsed entries (SELF-DEFENSE within the entry "
         "headed SELECTMEN; SERVITUDE within the entry headed VM, "
         "its own heading garbled in the scan; SILENCE within the "
         "entry headed SIONTJM, likewise garbled). An annotation "
         "cannot honestly attach to an entry the parse does not "
         "contain, so the three were struck as phantom keys; no "
         "footnote in this book derives from them, and the struck "
         "annotations remain in the phase data, marked — a "
         "disposition is a mark, not a vanishing.", 11)

    roman_section(
        "VIII", "TABLE OF AUTHORITIES (CONDENSED)",
        ["— Black's Law Dictionary, Second Edition. St. Paul, Minn.: "
         "West Publishing Co., 1910. (The text of this volume; public "
         "domain.)",
         "— Internet Archive OCR scan text; title page tool-verified "
         "as Second Edition, 1910.",
         "— Black's Law Dictionary, Fifth Edition (1979) — census "
         "data only: headwords and status, no entry text, per the "
         "copyright boundary stated at §V.",
         "— The Holy Bible, King James Version (public domain); the "
         "diff text is Project Gutenberg #10, cross-checked against "
         "a second structured transcription. Qur'an annotations rest "
         "on the Pickthall and Yusuf Ali translations, as cited in "
         "place.",
         "— U.S. Code, Uniform Commercial Code, and reported case "
         "law — footnote references only, no legal effect claimed.",
         "— Legal maxims: falsus in uno, falsus in omnibus; nullius "
         "in verba; festina lente."],
        [])

    roman_section(
        "IX", "CONTENT TEST — INPUTS, PROCESSES, OUTPUTS, TOLERANCES",
        ["Inputs: the verified 1910 OCR source; the 13,145-entry "
         "parse; the four audited well-phase annotation sets; the "
         "regenerated fifth-edition census (headwords and status "
         "only); the King James text (Project Gutenberg #10); the "
         "stratified sample audit of 2026; the rulings and "
         "clarifications of 2026-10-25 — SANS JOUR marked struck, "
         "dispositions marked never vanished, scan gaps marked in "
         "the open; the system-wide directive format; the Living "
         "Man's order and his red pen, which rules all.",
         "Processes: join on exact keys with verified re-homing; "
         "mechanical KJV text-diff with corrections printed as "
         "errata; census join with the 253-gap reconciliation "
         "published; rule-based scan-gap detection with per-rule "
         "precision review; typeset in directive format with "
         "red-letter rendering, marked dispositions, and markers at "
         "their loci; verification by count, extraction, and render "
         "inspection.",
         "Outputs: this volume — the complete final Teacher's "
         "Edition, parsed and cleaned, scan-verification pending, "
         "never claiming audit — together with its build log and "
         "data files: the census, mapping, and register; the diff "
         "results, corrections, and flags; the marker census. "
         "Every annotation a finding awaiting his pen.",
         "Tolerances: this volume fails the Method of Science the "
         "moment it claims an audit it has not done, prints a "
         "fifth-edition definition, hides a gap the scan left, "
         "asserts a changed-form match the data did not verify, or "
         "vanishes anything a ruling has marked; it fails the Aim "
         "of Religion if the wells were padded rather than honest. "
         "Both failures are recorded here in advance, without "
         "prejudice, so they cannot happen unnoticed."],
        [])

    # ── THE ENTRIES ──
    pdf.add_page()
    h1("THE ENTRIES", 20)
    para("All 13,145 entries, A to Z, with the Four Wells layered "
         "beneath. Headword in bold; body below; the fifth-edition "
         "apparatus line after the body; well notes last, grouped by "
         "well. Blood-red text is the voice of a deity. Rust marks "
         "are the scan-limitation markers defined at §VI.", 10,
         align="C")
    pdf.ln(4)

    def norm_key(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())

    markers_printed = Counter()
    substring_fallbacks = 0
    apparatus_counts = Counter()
    current_letter = ""
    rendered = 0
    for idx, (e, body) in enumerate(zip(entries, bodies)):
        disp = (e.get("head_line") or e.get("headword") or "").strip()
        if not disp:
            continue
        letter = disp[0].upper()
        if letter != current_letter and letter.isalpha():
            current_letter = letter
            pdf.ln(4)
            pdf.set_font("DejaVu", "B", 24)
            pdf.set_text_color(60, 60, 60)
            pdf.cell(0, 12, current_letter, align="C",
                     new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(2)
        pdf.set_font("DejaVu", "B", 11)
        if pdf.get_y() > 250:
            pdf.add_page()
        pdf.multi_cell(0, 6.5, disp, new_x="LMARGIN", new_y="NEXT")

        entry_markers = markers.get(idx, [])
        end_lines = []
        # headword-anchored markers print immediately under the headword
        for m in entry_markers:
            if m["anchor"] == "HEADWORD":
                marker_line(MARK_STRONG if m["strength"] == "strong"
                            else MARK_CANDIDATE)
                markers_printed[m["strength"]] += 1
        # substring-anchored markers insert inline into the body text
        body_text = body
        for m in entry_markers:
            anchor = m["anchor"]
            if anchor in ("END", "EMPTY", "ENTRY", "HEADWORD"):
                continue
            text_marker = (MARK_STRONG if m["strength"] == "strong"
                           else MARK_CANDIDATE)
            pat = anchor_regex(anchor)
            if pat.search(body_text):
                body_text = pat.sub(
                    lambda mm: mm.group(0) + " " + text_marker,
                    body_text, count=1)
                markers_printed[m["strength"]] += 1
            else:
                end_lines.append(m)
                substring_fallbacks += 1
        # body paragraphs
        paragraphs = []
        for pg in body_text.split("\n\n"):
            pg = pg.replace("\n", " ").strip()
            if pg:
                paragraphs.append(pg)
        pdf.set_font("DejaVu", "", 10)
        for pg in paragraphs:
            pdf.multi_cell(0, 5.5, pg, align="J",
                           new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
        if not paragraphs:
            for m in entry_markers:
                if m["anchor"] == "EMPTY":
                    marker_line(MARK_STRONG if m["strength"] == "strong"
                                else MARK_CANDIDATE)
                    markers_printed[m["strength"]] += 1
        # end/entry-anchored marker lines (END before ENTRY)
        for want in ("END", "ENTRY"):
            for m in entry_markers:
                if m["anchor"] == want:
                    marker_line(MARK_STRONG if m["strength"] == "strong"
                                else MARK_CANDIDATE)
                    markers_printed[m["strength"]] += 1
        for m in end_lines:
            marker_line(MARK_STRONG if m["strength"] == "strong"
                        else MARK_CANDIDATE)
            markers_printed[m["strength"]] += 1

        # ── fifth-edition apparatus ──
        fate = mapping[idx]
        if fate["fate"] == "carried":
            apparatus_counts["carried"] += 1
            form = fate.get("e5_form")
            if form and norm_key(form) != norm_key(e.get("headword", "")):
                app = (f"5e apparatus — Carried into the 5th edition "
                       f"(1979) as \u201c{form}\u201d.")
            else:
                app = ("5e apparatus — Carried into the 5th edition "
                       "(1979).")
        else:
            apparatus_counts["not-carried"] += 1
            app = ("5e apparatus — Not carried into the 5th edition "
                   "(1979).")
        pdf.set_font("DejaVu", "", 8.5)
        pdf.set_text_color(70, 70, 70)
        pdf.multi_cell(0, 5, app, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)

        # ── well footnotes (as Vol. I, + the marked-struck rendering) ──
        fns = footnotes.get(idx, [])
        if fns:
            pdf.ln(1)
            pdf.set_draw_color(150, 150, 150)
            pdf.line(25, pdf.get_y(), 70, pdf.get_y())
            pdf.ln(1.5)
            for w in WELL_ORDER:
                wfns = [f for f in fns if f["well"] == w]
                if not wfns:
                    continue
                pdf.set_font("DejaVu", "B", 9)
                pdf.set_text_color(90, 60, 10)
                pdf.multi_cell(0, 5, f"{WELL_SIGLA[w]} — {WELL_NAMES[w]}",
                               new_x="LMARGIN", new_y="NEXT")
                pdf.set_text_color(0, 0, 0)
                for fn in wfns:
                    if fn["struck"]:
                        pdf.set_font("DejaVu", "B", 8.5)
                        pdf.set_text_color(120, 30, 20)
                        pdf.multi_cell(0, 5, STRUCK_LABEL, align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                        pdf.set_text_color(0, 0, 0)
                    cit_style = "BS" if (fn["struck"] and strike_ok) else "B"
                    pdf.set_font("DejaVu", cit_style, 8.5)
                    pdf.multi_cell(0, 5, fn["citation"] or "(no citation)",
                                   new_x="LMARGIN", new_y="NEXT")
                    note_style = "S" if (fn["struck"] and strike_ok) else ""
                    if fn["deity_verbatim"]:
                        pdf.set_font("DejaVu", note_style, 9)
                        pdf.set_text_color(*BLOOD)
                        pdf.multi_cell(0, 5, fn["text"], align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                        pdf.set_text_color(0, 0, 0)
                    else:
                        pdf.set_font("DejaVu", note_style, 9)
                        pv = "" if fn["verbatim"] else " (paraphrase)"
                        pdf.multi_cell(0, 5, fn["text"] + pv, align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                    if fn["bridge"]:
                        pdf.set_font("DejaVu", "", 8.5)
                        pdf.multi_cell(0, 5, fn["bridge"], align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                    tag = fn["reasoning"].strip()
                    if len(tag) > 220:
                        tag = tag[:217].rstrip() + "…"
                    extra = ""
                    if fn["rehome_note"]:
                        extra = f" [{fn['rehome_note']}]"
                    pdf.set_font("DejaVu", "", 8)
                    pdf.set_text_color(80, 80, 80)
                    pdf.multi_cell(0, 4.5, f"Why: {tag}{extra}",
                                   align="J", new_x="LMARGIN", new_y="NEXT")
                    pdf.set_text_color(0, 0, 0)
                    pdf.ln(1)
        pdf.ln(2)
        rendered += 1
        if rendered % 2000 == 0:
            print(f"  … typeset {rendered} entries", flush=True)
    stats["rendered"] = rendered
    stats["markers_printed"] = dict(markers_printed)
    stats["substring_fallbacks"] = substring_fallbacks
    stats["apparatus_counts"] = dict(apparatus_counts)

    # ── REGISTER APPENDIX ──
    pdf.add_page()
    h1("APPENDIX — HEADWORDS NEW IN THE FIFTH EDITION", 17)
    para("The 18,155 headwords of the fifth edition (1979) that no "
         "entry in this book's second-edition parse witnesses — the "
         "new vocabulary of the 1979 re-founding. Against the "
         "census's own count of new headwords (18,098, measured "
         "against its parse), this register runs 57 longer: 104 "
         "fifth-edition headwords are witnessed in the second "
         "edition only by census-only keys, and 47 are witnessed "
         "only by base-only keys (§V). Headwords only — no "
         "fifth-edition text — sorted by normalized key.", 10,
         align="C")
    pdf.ln(3)
    groups = {}
    for hw in register:
        g = hw[0].upper() if hw and hw[0].isalpha() else "#"
        groups.setdefault(g, []).append(hw)
    for g in sorted(groups):
        pdf.set_font("DejaVu", "B", 14)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 9, g, align="L", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)
        items = groups[g]
        for i in range(0, len(items), 300):
            chunk = " \u00b7 ".join(items[i:i + 300])
            pdf.set_font("DejaVu", "", 8.5)
            pdf.multi_cell(0, 4.8, chunk, align="J",
                           new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
        pdf.ln(2)

    # ── COLOPHON ──
    pdf.add_page()
    h2("COLOPHON", 16)
    para("The Final Teacher's Edition — the complete text, the four "
         "wells, the fifth-edition apparatus, the errata, the "
         "scan-limitation markers, and the register — was generated "
         "under the discipline of Scientific Illuminism on this "
         + THELEMIC_DATE + ".", 11)
    pdf.ln(2)
    para(AUTHOR_LINE + ".", 11, align="C")
    pdf.ln(2)
    para("All Rights Reserved. Without Prejudice. Flagpole of Claim "
         "and Coinage planted and reserved under the authority of "
         "the Living Man.", 11, align="C")
    pdf.ln(2)
    para("Method of Science. Aim of Religion.", 11, bold=True, align="C")
    pdf.ln(4)
    para(FLAGPOLE, 9, bold=True, align="C")

    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT_PDF))
    stats["pages"] = pdf.page_no()
    stats["out_pdf"] = str(OUT_PDF)
    return stats


if __name__ == "__main__":
    result = build()
    print("BUILD STATS:", json.dumps(result, indent=1))
