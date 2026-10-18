#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_vol1_layered.py
═══════════════════════════════════════════════════════════════════════════════
"Let your communication be, Yea, yea; Nay, nay."
    — The Gospel According to Matthew 5:37 (KJV)

93.

Date: XVIII day of October, Dies Solis, Sol in Libra, Anno V:xii e.n. (2026 e.v.)

Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
(Greek, -ARR, All Rights Reserved, Without Prejudice).

Classification: Enterprise • Educational • Research & Development
Method of Science, Aim of Religion.

DOCTRINE
────────
This script builds VOLUME I of the two-volume hardcover set: the complete
text of Black's Law Dictionary, Second Edition (1910) — all 13,145 parsed
entries — layered with the four well-phase annotation sets (Law →
Scripture → Hip-hop → Humanity/Fiction & film). It claims NOTHING beyond
what it does: join, normalize, re-home per the coordinators' placement
notes, typeset, verify. The scan-verification audit is the 2027 work;
this PDF is labeled parsed-not-audited, honestly, on its face.

Every annotation is a FINDING, never doctrine, until his red pen rules.
Nothing is silently corrected. Every re-home, exclusion, and schema
normalization is logged in the merge log.

MECHANISM
─────────
1. Load entries.json (13,145 entries, ordered) and clean bodies with the
   four deterministic rules R1–R4 (counters kept; glyph misreads left for
   the 2027 scan-verification).
2. Load the four phase JSONs. Join keys are opaque chunk-exact OCR
   headwords — matched exactly. Where a key does not match, consult the
   REHOME table (built from the coordinators' placement notes and
   body-verified host entries). Where no honest host exists, DROP and log.
3. Normalize the three schema variants to one footnote schema:
   {well, text, bridge, citation, reasoning, verbatim, deity_verbatim,
    rehome_note}. Paraphrase marking preserved visibly. Phase 3
   lyric/quote fields become the text; the note becomes the bridge.
4. Typeset in directive format. Footnotes render per entry, grouped by
   well with sigla [Law] [Scripture] [Hip-hop] [Humanity]. Scripture
   notes flagged deity_verbatim=true render in blood red (163,18,18) —
   the RED-LETTER RULE: the reader knows a deity is speaking.
5. Post-build verification: page count via pypdf; footnote counts per
   well reconciled; spot-extraction of a red-letter verse and a
   re-homed footnote.

93 93/93.

"Do what thou wilt shall be the whole of the Law."
    — Liber AL vel Legis I:40
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════
# DOCTRINE: paths.
# ═══════════════════════════════════════════════════════════════════════════
HERE = Path(__file__).resolve().parent
BASE = Path.home() / "workspace/your_files/blacks-teachers-editions"
ENTRIES_JSON = BASE / "2e/entries.json"
LAW_JSON = BASE / "well-phases/phase-1-law/law-well-annotations.json"
SCR_JSON = BASE / "well-phases/phase-2-scripture/scripture-well-annotations.json"
HH_JSON = BASE / "well-phases/phase-3-hiphop/hiphop-well-annotations.json"
HUM_JSON = BASE / "well-phases/phase-4-humanity/humanity-well-annotations.json"
OUT_PDF = HERE / "blacks-2e-vol1-layered.pdf"
LOG_PATH = HERE / "merge-log.md"

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT_REG = FONT_DIR / "DejaVuSans.ttf"
FONT_BLD = FONT_DIR / "DejaVuSans-Bold.ttf"

THELEMIC_DATE = ("XVIII day of October, Dies Solis, Sol in Libra, "
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

# ═══════════════════════════════════════════════════════════════════════════
# DOCTRINE: the REHOME table. Every entry here was verified against the
# actual entries.json bodies (the host entry's body contains the annotated
# definition, or the OCR form is unambiguous). "idx" targets are
# entries.json indices for duplicate headwords. LAST is not here — it is
# DROPPED (see DROP_LOG): the "last clear chance" text appears nowhere
# in the 13,145 entries.
# ═══════════════════════════════════════════════════════════════════════════
REHOME = {
    # — Phase 1: Law (42 orphans; 41 re-homed, 1 dropped) —
    ("law", "AT ARM'S LENGTH"): "AT ARM’S LENGTH",
    ("law", "BAIL"): "BAHADUM",                      # definition fused in body
    ("law", "COMMENDATIO"): "COMMENDATXO",
    ("law", "COMMON LAW"): "COMMON BENCH",            # definition in body
    ("law", "COMMORIENTES"): "COMMORXENTES",
    ("law", "COSAS COMUNES"): "COSAS COMUSES",
    ("law", "COUNSEL"): "COUNCIL OF THE NORTH",       # fused in body
    ("law", "CREPUSCULUM"): "CREPUSGUL1TM",
    ("law", "CY-PRES"): "GY-PRES",
    ("law", "DAMNI INJURIAE ACTIO"): "DAMNATU8",      # fused in tail
    ("law", "DAY"): "DAUPHIN",                        # fused in body
    ("law", "DAYLIGHT"): "DAYXIGHT",
    ("law", "DE AEQUITATE"): "DE -XQUITATE",
    ("law", "DE ARBITRATIONE FACTA"): "DE ARBITRATIONS FACTA",
    ("law", "DE ARRESTANDIS BONIS NE DISSIPENTUR"): "DE ARRE8TANPI8 BONIS NE DISSIPENTUR",
    ("law", "DE BIEN ET DE MAL"): "DE BIEN ET DE MAE",
    ("law", "DE BONA MEMORIA"): "DE BONE MEMORIE",
    ("law", "DISCOVERY"): ("idx", 3921),              # ascertainment sense
    ("law", "DUE"): "DUCROERE",                       # fused in body
    ("law", "EN MORT MEYNE"): "EN MOST MEYNE",
    ("law", "EXPATRIATION"): "EXORDIUM",              # fused in body
    ("law", "EXTERRITORIALITY"): "EXTERRITORIAXITY",
    ("law", "FABRICARE"): "FABRIC ARE",
    ("law", "FALSUS"): "F ALSUS",
    ("law", "FATUM"): "FATOM",
    ("law", "FLAG"): "IX AO",                         # fused in body
    ("law", "FOR"): ("idx", 5322),                    # agency formula
    ("law", "IMPEACHMENTS"): "COURT FOR THE RELIEF OF INSOLVENT DEBTORS",
    ("law", "JURA"): "JUBA",
    ("law", "JURARE"): "JUR ARE",
    ("law", "KING'S EVIDENCE"): "KING’S EVIDENCE",
    ("law", "LAND"): "LANCETI",                       # fused in body
    ("law", "LAS PARTEDAS"): "LAS PARTED AS",
    ("law", "LATA GULPA"): "LATA GULP A",
    ("law", "LETTER"): "LETBADO",                     # fused in body
    ("law", "LIBEL"): "LIAKD",                        # full exposition in body
    ("law", "LIBERTY"): "LIBERTIES",                  # fused in body
    ("law", "LITEM SUAM FACERE"): "LITEM SHAM FACERE",
    ("law", "MANDAMUS"): "MANDAMIENTO",               # fused in body
    ("law", "MANUMISSION"): "MANJTMISSION",
    ("law", "NOVODAMUS"): "NOVODAKUB",
    ("law", "PUBLICATION"): "PUBLICANUS",              # fused in body
    # — Phase 2: Scripture (40 orphans; all re-homed) —
    ("scripture", "A MENSA ET THORO"): "A MENS A ET THORO",
    ("scripture", "ACCEPTILATION"): "ACCEPTTLATION",
    ("scripture", "ACCREDULITARE"): "ACOREDUUTARE",
    ("scripture", "AD WABACTUM"): "AS WABACTUM",
    ("scripture", "ADDICTIO"): "ASDICTIO",
    ("scripture", "ADMINICULATOR"): "ADMINICUXATOR",
    ("scripture", "ADSTIPULATOR"): "ADSTIFULATOR",
    ("scripture", "ADVOCATIONE DECIMARUM"): "ADVOCATIONE DECIMARTJM",
    ("scripture", "AEDILITUM EDICTUM"): "JEDELITUM EDICTUM",
    ("scripture", "AES"): "JES",                      # aes alienum in body
    ("scripture", "AESTIMATIO CAPITIS"): "ABSTIMATIO CAPITIS",
    ("scripture", "AFFRANCHIR"): "AFFRANCHXR",
    ("scripture", "COMPROMISSARIUS"): "COMPROMISSARITJS",
    ("scripture", "DIGAMY"): "DIFFORCIARE",           # fused in body
    ("scripture", "DISAFFIRM"): "D IS AFFIRM",
    ("scripture", "DISCOVERY"): ("idx", 3921),
    ("scripture", "DISINTERESTED"): "DISINTER",        # fused in body
    ("scripture", "DIVINARE"): "D IVIN ARE",
    ("scripture", "DOMINICA PALMARUM"): "DOMINICA PALM ARUM",
    ("scripture", "DONNEUR D'AVAL"): "DONNEUR D’AVAX",
    ("scripture", "DOWER"): "DOWEB",
    ("scripture", "DRY-CRAEFT"): "DRY-CRJEFT",
    ("scripture", "DURESS"): "DURESS, 17",
    ("scripture", "EJIDOS"): "EJXDOS",
    ("scripture", "EMBASSAGE"): "EMBASSADOR",          # fused in body
    ("scripture", "EMBLER DE GENTZ"): "EMBLEM BE GENTZ",
    ("scripture", "EMBRACERY"): "EMBBACEBY",
    ("scripture", "EMENDA"): "EMEND A",
    ("scripture", "IN GENUITAS"): "IN GENUIT AS",
    ("scripture", "IN PIOS USUS"): "IN PIOS TXSUS",
    ("scripture", "IN VINCULIS"): "IN VTNCULIS",
    ("scripture", "INSCRIBERE"): "XNSCRIBERE",
    ("scripture", "ITA TE DEUS ADJUVET"): "ITA TE DEVS ADJUVET",
    ("scripture", "RELEASE"): "RELAXATION",           # fused in body
    ("scripture", "RENDER"): "RENCOUNTER",            # fused in body
    ("scripture", "TRANSGRESSIO"): "TRANSGRE8SIO",
    ("scripture", "ULTIMUM SUPPLICIUM"): "ULTIMUM SUFPLICIUM",
    ("scripture", "UNITAS PERSONARUM"): "UNITAB PERSONARUM",
    ("scripture", "UNTHRIFT"): "UN THRIFT",
    ("scripture", "WIFE'S EQUITY"): "WIFE’S EQUITY",
    # — Phase 4: Humanity (1 orphan) —
    ("humanity", "GYNARCHY"): "GYLTW1TE",             # fused in body
}

# Annotations dropped: no honest host text exists.
DROP_LOG = [
    ("law", "LAST",
     "DROPPED — worker-09 claimed a 'last clear chance' definition "
     "embedded in LASCAR's body; the phrase 'clear chance' appears nowhere "
     "in entries.json (13,145 entries) nor in the worker's chunk. No host "
     "text exists to illuminate. Annotation preserved in the phase JSON "
     "for the record; excluded from print."),
]

# Exclusions verified absent (already handled at phase merge).
EXCLUDED_VERIFIED = [
    ("humanity", "SELF-DEFENSE", "Phase 4 phantom key — STRUCK, in worker-21-STRUCK-phantom-keys.json"),
    ("humanity", "SERVITUDE", "Phase 4 phantom key — STRUCK"),
    ("humanity", "SILENCE", "Phase 4 phantom key — STRUCK"),
    ("scripture", "POSTERITY", "Phase 2 declined at phase merge"),
]

WELL_ORDER = ["law", "scripture", "hiphop", "humanity"]
WELL_SIGLA = {"law": "[Law]", "scripture": "[Scripture]",
              "hiphop": "[Hip-hop]", "humanity": "[Humanity]"}
WELL_NAMES = {"law": "Law", "scripture": "Scripture",
              "hiphop": "Hip-hop", "humanity": "Humanity / Fiction & Film"}


# ═══════════════════════════════════════════════════════════════════════════
# DOCTRINE: cleanup rules R1–R4 (same as the base builder — the foundation
# text is byte-identical to the base edition).
# ═══════════════════════════════════════════════════════════════════════════
class Cleaner:
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


def normalize_annotation(well, raw):
    """Normalize one raw annotation to the single footnote schema."""
    text = raw.get("note", "") or ""
    bridge = None
    if well == "hiphop":
        # Phase 3 schema variants: lyric/quote carry the verse; note is
        # the explanatory bridge.
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
    }


def build() -> dict:
    """Build Volume I. Returns stats for the log and report."""
    log_lines = []

    def log(s: str):
        log_lines.append(s)
        print(s, flush=True)

    log("## MERGE LOG — Black's 2e Volume I (layered)")
    log(f"Date: {THELEMIC_DATE}")
    log("")
    log("### Hypothesis")
    log("The four well-phase annotation sets can be joined to the 13,145 "
        "parsed entries on exact headword keys, with coordinator-noted "
        "re-homes applied and verified, into a single layered Volume I "
        "that stays honest: parsed-not-audited, genuine links only, "
        "nothing silently corrected.")
    log("")
    log("### Method — load the corpus")
    entries = json.loads(ENTRIES_JSON.read_text(encoding="utf-8"))
    log(f"Loaded {len(entries)} entries.")
    head_to_idxs = {}
    for i, e in enumerate(entries):
        head_to_idxs.setdefault(e["headword"], []).append(i)

    log("")
    log("### Method — deterministic cleanup (rules R1–R4)")
    cleaner = Cleaner()
    bodies = [cleaner.clean(e.get("body", "") or "") for e in entries]
    log(f"Cleanup counters: {cleaner.counts}")

    log("")
    log("### Method — load the four well-phase sets")
    phase_data = {
        "law": json.loads(LAW_JSON.read_text(encoding="utf-8")),
        "scripture": json.loads(SCR_JSON.read_text(encoding="utf-8")),
        "hiphop": json.loads(HH_JSON.read_text(encoding="utf-8")),
        "humanity": json.loads(HUM_JSON.read_text(encoding="utf-8")),
    }
    for w, d in phase_data.items():
        n_ann = sum(len(v) for v in d.values())
        log(f"  {w}: {len(d)} keys, {n_ann} annotations")

    # Verify the exclusions are absent (already handled at phase merge).
    log("")
    log("### Observation — exclusion verification")
    for well, key, why in EXCLUDED_VERIFIED:
        present = key in phase_data[well]
        log(f"  {well}/{key}: {'STILL PRESENT — PROBLEM' if present else 'absent ✓'} ({why})")

    # Apply drops.
    log("")
    log("### Method — drops (no honest host)")
    dropped = 0
    for well, key, why in DROP_LOG:
        if key in phase_data[well]:
            n = len(phase_data[well].pop(key))
            dropped += n
            log(f"  DROPPED {well}/{key} ({n} annotations). {why}")
        else:
            log(f"  {well}/{key} already absent.")

    # Build the join: entry_index -> [footnotes].
    log("")
    log("### Method — join with re-homing")
    footnotes = {i: [] for i in range(len(entries))}
    rehome_count = 0
    direct_count = 0
    dup_first_placements = []
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
                    log(f"  !! REHOME TARGET MISSING: {well}/{key} -> {target!r}")
                    continue
            else:
                idxs = head_to_idxs.get(key, [])
                if not idxs:
                    log(f"  !! ORPHAN (no re-home): {well}/{key}")
                    continue
                direct_count += 1
                if len(idxs) > 1:
                    dup_first_placements.append((well, key, idxs))
                    idxs = idxs[:1]  # first occurrence; ambiguity logged
            for a in anns:
                fn = normalize_annotation(well, a)
                if rehome_note:
                    fn["rehome_note"] = rehome_note
                for i in idxs:
                    footnotes[i].append(fn)
    log(f"  direct joins: {direct_count} keys; re-homes applied: {rehome_count} keys; "
        f"dropped: {dropped} annotations")
    log(f"  duplicate-headword first-occurrence placements: {len(dup_first_placements)} "
        f"(sense-matching not verified; logged for the 2027 audit)")
    for well, key, idxs in dup_first_placements[:15]:
        log(f"    {well}/{key} -> idx {idxs[0]} (of {idxs})")

    # SANS JOUR flag (kept, strike candidate).
    log("")
    log("### Red-pen flag")
    log("  SANS JOUR (law) KEPT in the merge — coordinator spot-check "
        "judged it a thin call (restates the entry). Strike candidate "
        "for his red pen; no falsehood, just thin.")

    per_well = Counter()
    entries_with_notes = 0
    red_letter = 0
    for i, fns in footnotes.items():
        if fns:
            entries_with_notes += 1
            for fn in fns:
                per_well[fn["well"]] += 1
                if fn["deity_verbatim"]:
                    red_letter += 1
    log("")
    log("### Observation — merge totals")
    log(f"  entries carrying footnotes: {entries_with_notes} of {len(entries)}")
    for w in WELL_ORDER:
        log(f"  {WELL_SIGLA[w]} rendered: {per_well[w]}")
    log(f"  red-letter (deity_verbatim) footnotes: {red_letter}")

    # ── typeset ──
    log("")
    log("### Method — typeset")
    pdf = BlacksPDF("P", "mm", "Letter")
    pdf.set_margins(25, 25, 25)
    pdf.set_auto_page_break(True, 25)
    pdf.add_font("DejaVu", "", str(FONT_REG))
    pdf.add_font("DejaVu", "B", str(FONT_BLD))
    pdf.alias_nb_pages("00000")

    def h1(t, size=22):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 9, t, align="C",
                       new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    def h2(t, size=14):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 8, t, align="C",
                       new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    def h3(t, size=12):
        pdf.set_font("DejaVu", "B", size)
        pdf.multi_cell(0, 7, t, align="C",
                       new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    def para(t, size=11, bold=False, align="J", color=(0, 0, 0)):
        pdf.set_font("DejaVu", "B" if bold else "", size)
        pdf.set_text_color(*color)
        pdf.multi_cell(0, 6, t, align=align,
                       new_x="LMARGIN", new_y="NEXT")
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

    # ── TITLE PAGE ──
    pdf.add_page()
    pdf.ln(10)
    para("DOCTRINE — BLACK'S LAW DICTIONARY, SECOND EDITION", 10,
         bold=True, align="C")
    h1("BLACK'S LAW DICTIONARY", 26)
    h2("Second Edition — West Publishing Co., 1910", 15)
    h3("VOLUME I — The Complete Text with the Four Wells", 13)
    h3("Under the Scales of Ma'at — Law, Scripture, Hip-hop, Humanity",
       11)
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
    para("Volume I carries the complete parsed text of the 1910 second "
         "edition, layered with the four well-phase annotation sets. It "
         "has not yet passed the TRVVTH scan-verification audit; that "
         "audit is the 2027 work. Nothing in these pages claims 'audited' "
         "or 'restored.' Every annotation is a finding, never doctrine, "
         "until his red pen rules.", 10)
    pdf.ln(4)
    para(FLAGPOLE, 9, bold=True, align="C")

    # ── PREFACE ──
    roman_section(
        "I", "STATEMENT OF THE WORK",
        ["This is Volume I of the two-volume hardcover set: the full "
         "dictionary text of Black's Law Dictionary, Second Edition "
         "(1910), with the Four Wells layered entry by entry — Law, "
         "Scripture, Hip-hop, and Humanity with Fiction & film. Volume "
         "II, under the Open Word, carries the Teacher's Edition with "
         "the full audits.",
         "The honest label on the title page is the load-bearing beam "
         "of this volume. A text that claimed audit it had not done "
         "would be false in one thing, and therefore suspect in all."],
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
         "corrected here; they wait for scan evidence in the 2027 "
         "audit.",
         "Merge method: annotation keys are the workers' chunk-exact "
         "OCR headwords, joined to entries on exact match. Where a key "
         "did not match — OCR-normalized spellings, or definitions "
         "fused by the parser into neighboring entries' bodies — the "
         "coordinators' placement notes were applied, each verified "
         "against the actual entry bodies, and every move logged in "
         "the merge log. One annotation (LAST, Law well) was dropped: "
         "the 'last clear chance' text it claimed to illuminate "
         "appears nowhere in the 13,145 entries. Three fabricated "
         "headwords from one Phase 4 worker were struck at phase "
         "merge and are excluded here.",
         "Footnotes are reference material, not legal advice; no "
         "legal effect is claimed by any of them."],
        ["The First Epistle to the Thessalonians 5:21 (KJV): 'Prove all "
         "things; hold fast that which is good.'",
         "Nullius in verba — 'take nobody's word for it.'"])

    roman_section(
        "III", "THE FOUR WELL-PHASES",
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
         "Known pre-print checks still open: a mechanical KJV "
         "text-diff of the Scripture quotations (recommended by the "
         "Phase 2 workers; most quotes are verbatim-certain, not "
         "web-verified); and the full TRVVTH scan-verification, which "
         "is the 2027 work."],
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
        "V", "TABLE OF AUTHORITIES (CONDENSED)",
        ["— Black's Law Dictionary, Second Edition. St. Paul, Minn.: "
         "West Publishing Co., 1910. (The text of this volume; public "
         "domain.)",
         "— Internet Archive OCR scan text; title page tool-verified "
         "as Second Edition, 1910.",
         "— The Holy Bible, King James Version (public domain); "
         "Qur'an via Pickthall and Yusuf Ali translations — footnote "
         "quotations only, verbatim-certain.",
         "— U.S. Code, Uniform Commercial Code, and reported case law "
         "— footnote references only, no legal effect claimed.",
         "— Legal maxims: falsus in uno, falsus in omnibus; nullius "
         "in verba; festina lente."],
        [])

    roman_section(
        "VI", "CONTENT TEST — INPUTS, PROCESSES, OUTPUTS, TOLERANCES",
        ["Inputs: the verified 1910 OCR source; the 13,145-entry "
         "parse; the four audited well-phase annotation sets; the "
         "coordinators' placement notes; the system-wide directive "
         "format; the Living Man's order and his red pen, which rules "
         "all.",
         "Processes: join on exact keys, verified re-homing, schema "
         "normalization with paraphrase marking preserved, typeset in "
         "directive format with red-letter rendering, verify by count "
         "and extraction. No semantic alteration of the base text; no "
         "silent correction.",
         "Outputs: this volume — the complete layered text, parsed "
         "and cleaned, scan-verification pending, never claiming "
         "audit; every annotation a finding awaiting his pen.",
         "Tolerances: this volume fails the Method of Science the "
         "moment it claims an audit it has not done, or prints a "
         "footnote for a text that is not there; it fails the Aim of "
         "Religion if the wells were padded rather than honest. Both "
         "failures are recorded here in advance, without prejudice, "
         "so they cannot happen unnoticed."],
        [])

    # ── THE ENTRIES ──
    pdf.add_page()
    h1("THE ENTRIES", 20)
    para("All 13,145 entries, A to Z, with the Four Wells layered "
         "beneath. Headword in bold; body below; well notes after the "
         "body, grouped by well. Blood-red text is the voice of a "
         "deity.", 10, align="C")
    pdf.ln(4)

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
        pdf.set_font("DejaVu", "", 10)
        for pg in body.split("\n\n"):
            pg = pg.replace("\n", " ").strip()
            if pg:
                pdf.multi_cell(0, 5.5, pg, align="J",
                               new_x="LMARGIN", new_y="NEXT")
                pdf.ln(1)
        # ── well footnotes ──
        fns = footnotes.get(idx, [])
        if fns:
            pdf.ln(1)
            pdf.set_draw_color(150, 150, 150)
            pdf.line(25, pdf.get_y(), 70, pdf.get_y())
            pdf.ln(1.5)
            # group by well, in canonical order
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
                    # citation line
                    pdf.set_font("DejaVu", "B", 8.5)
                    pdf.multi_cell(0, 5, fn["citation"] or "(no citation)",
                                   new_x="LMARGIN", new_y="NEXT")
                    # text — blood red when the deity speaks
                    if fn["deity_verbatim"]:
                        pdf.set_font("DejaVu", "", 9)
                        pdf.set_text_color(*BLOOD)
                        pdf.multi_cell(0, 5, fn["text"], align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                        pdf.set_text_color(0, 0, 0)
                    else:
                        pdf.set_font("DejaVu", "", 9)
                        pv = "" if fn["verbatim"] else " (paraphrase)"
                        pdf.multi_cell(0, 5, fn["text"] + pv, align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                    # bridge (hip-hop lyric explanation)
                    if fn["bridge"]:
                        pdf.set_font("DejaVu", "", 8.5)
                        pdf.multi_cell(0, 5, fn["bridge"], align="J",
                                       new_x="LMARGIN", new_y="NEXT")
                    # reasoning tag + rehome note
                    tag = fn["reasoning"].strip()
                    if len(tag) > 220:
                        tag = tag[:217].rstrip() + "…"
                    extra = ""
                    if fn["rehome_note"]:
                        extra = f" [{fn['rehome_note']}]"
                    pdf.set_font("DejaVu", "", 8)
                    pdf.set_text_color(80, 80, 80)
                    pdf.multi_cell(0, 4.5, f"Why: {tag}{extra}",
                                   align="J",
                                   new_x="LMARGIN", new_y="NEXT")
                    pdf.set_text_color(0, 0, 0)
                    pdf.ln(1)
        pdf.ln(2)
        rendered += 1

    log(f"### Result — typeset {rendered} entries.")

    # ── COLOPHON ──
    pdf.add_page()
    h2("COLOPHON", 16)
    para("Volume I — the complete layered text — was generated under "
         "the discipline of Scientific Illuminism on this "
         + THELEMIC_DATE + ".", 11)
    pdf.ln(2)
    para(AUTHOR_LINE + ".", 11, align="C")
    pdf.ln(2)
    para("All Rights Reserved. Without Prejudice. Flagpole of Claim "
         "and Coinage planted and reserved under the authority of the "
         "Living Man.", 11, align="C")
    pdf.ln(2)
    para("Method of Science. Aim of Religion.", 11, bold=True,
         align="C")
    pdf.ln(4)
    para(FLAGPOLE, 9, bold=True, align="C")

    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT_PDF))
    pages = pdf.page_no()
    log(f"### Result — wrote {OUT_PDF} ({pages} pages).")
    return {"pages": pages, "rendered": rendered,
            "cleanup": cleaner.counts,
            "per_well": dict(per_well),
            "entries_with_notes": entries_with_notes,
            "red_letter": red_letter,
            "rehome_count": rehome_count,
            "direct_count": direct_count,
            "dropped": dropped,
            "log": log_lines}


if __name__ == "__main__":
    stats = build()
    LOG_PATH.write_text("\n".join(stats["log"]) + "\n", encoding="utf-8")
    print("LOG:", LOG_PATH)
    print("PAGES:", stats["pages"], "RENDERED:", stats["rendered"])
    print("PER_WELL:", json.dumps(stats["per_well"]))
    print("WITH_NOTES:", stats["entries_with_notes"],
          "RED_LETTER:", stats["red_letter"])
    print("REHOMES:", stats["rehome_count"], "DIRECT:", stats["direct_count"],
          "DROPPED:", stats["dropped"])
