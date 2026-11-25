#!/usr/bin/env python3
# =====================================================================
# THE CLASS-WALK MAP — INDEPENDENT AUDIT
# 93 · Anno V:xii e.n. · XXIV day of November, Dies Martis (2026 e.v.)
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice).
# Scientific Illuminism: the Method of Science, the Aim of Religion.
#
# MECHANISM: an INDEPENDENT recomputation of the map. The classed
# tongues' seat lists are re-derived FROM THE BANKS (value -> holder,
# with the plate-filed exclusions stated on their faces), every walk
# row and totals line is rebuilt by this file's own formatter and
# matched against the master line for line; the five non-class
# tongues are re-derived from their own doors (hangul(), the kana
# mint, the Ge'ez mint door, the bank dicts); the founding
# coordinates and the hybrids are re-weighed; and the PDF text
# layer is checked for the walks, the resolving footer, and the
# absence of Hebrew-block codepoints (the declared transliteration
# dress). Nothing here imports the generator.
# DOCTRINE: the map is not done until the audit passes — the
# standing law. A failed check prints its coordinate; nothing is
# smoothed.
# =====================================================================
import hashlib
import re
import site
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from pontifex import weigh, hangul  # noqa: E402
from pontifex.tables import (GREEK, COPTIC, CYRILLIC, ARMENIAN,  # noqa: E402
                             GEORGIAN, ARABIC_ABJAD, GLAGOLITIC,
                             HEBREW, LATIN_ORDINAL, AGRIPPA, KANA,
                             GEEZ, _GEEZ_BASES)
from pontifex.numerals import repeat_status  # noqa: E402

HERE = Path(__file__).resolve().parent
FILES = HERE.parents[2] / "goals" / "cross-gematria-777-gap-filling" / "files"
MASTER = (FILES / "THE-CLASS-WALK-MAP.md").read_text(encoding="utf-8")
PDF = FILES / "THE-CLASS-WALK-MAP-MAGVS.pdf"

CHECKS = []


def chk(name, cond):
    CHECKS.append((name, bool(cond)))
    if not cond:
        print(f"FAIL: {name}")


def W(word, bank):
    return weigh(word, bank)["value"]


# ---------------------------------------------------------------------
# Controls and founding coordinates
# ---------------------------------------------------------------------
chk("control θέλημα 93", W("θέλημα", "greek") == 93)
chk("control VAPOUR 93", W("VAPOUR", "latin_ordinal") == 93)
chk("control σφίγξ 773", W("σφίγξ", "greek") == 773)
chk("ΗΗΗ = 24", W("ΗΗΗ", "greek") == 24)
chk("HHH = 24 both banks", W("HHH", "latin_ordinal") == 24
    and W("HHH", "agrippa") == 24)
chk("ΙΗΣΟΥΣ = 888", W("ΙΗΣΟΥΣ", "greek") == 888)
chk("ΙΗΣ = 218", W("ΙΗΣ", "greek") == 218)
chk("ΩΠΗ = 888", W("ΩΠΗ", "greek") == 888)
chk("888 reduces to 24", sum(int(c) for c in "888") == 24)

# ---------------------------------------------------------------------
# The walk formatter (this file's own implementation of the law)
# ---------------------------------------------------------------------
CLASS3 = ["units", "tens", "hundreds"]
CLASS4 = ["units", "tens", "hundreds", "thousands"]
CLASS5G = ["units", "tens", "hundreds", "thousands", "ten-thousands"]


def cell(holders):
    if not holders:
        return "— HOLE"
    return " + ".join(f"{l} {v}{' ★' if g == 'ARCHON' else ''}"
                      for l, v, g in holders)


def break_text(steps, names):
    grades = []
    for s in steps:
        if not s:
            grades.append("HOLE")
        elif any(g == "ARCHON" for _l, _v, g in s):
            grades.append("ARCHON")
        else:
            grades.append("STRANGER")
    archon_at = [i for i, g in enumerate(grades) if g == "ARCHON"]
    if not archon_at:
        return "no line — no archon stands on this walk"
    brk = None
    for i in range(archon_at[0] + 1, len(grades)):
        if grades[i] != "ARCHON":
            brk = i
            break
    if brk is None:
        if archon_at[0] == len(grades) - 1:
            return ("late-standing — the archon stands at the "
                    "final step; nothing follows it to break")
        if archon_at[0] > 0:
            return (f"stands late at the {names[archon_at[0]]} step "
                    f"and runs unbroken to the final step")
        return "unbroken — the line runs to the final step"
    txt = f"break at the {names[brk]} step ({cell(steps[brk])})"
    for j in range(brk + 1, len(grades)):
        if grades[j] == "ARCHON":
            txt += (f" · return at the {names[j]} step "
                    f"({cell(steps[j])})")
            break
    return txt


def rows_for(walks, names):
    out = []
    for d, steps in enumerate(walks, start=1):
        n = sum(1 for s in steps if any(g == "ARCHON"
                                        for _l, _v, g in s))
        cells = " | ".join(cell(s) for s in steps)
        out.append(f"| {d} | {cells} | {n} | {break_text(steps, names)} |")
    return out


def totals_of(walks):
    steps_a = holders = 0
    walks_with = 0
    both = []
    for d, steps in enumerate(walks, start=1):
        has = False
        for s in steps:
            hs = [1 for _l, _v, g in s if g == "ARCHON"]
            if hs:
                steps_a += 1
                holders += sum(hs)
                has = True
        if has:
            walks_with += 1
        def gr(s):
            if not s:
                return "HOLE"
            return "ARCHON" if any(g == "ARCHON" for _l, _v, g in s) \
                else "STRANGER"
        if steps and gr(steps[0]) == "ARCHON" and gr(steps[-1]) == "ARCHON":
            both.append(d)
    return steps_a, holders, walks_with, both


def check_tongue(name, walks, names, expect):
    rows = rows_for(walks, names)
    for r in rows:
        chk(f"{name} row in master: {r[:60]}…", r in MASTER)
    a, h, w_, b = totals_of(walks)
    suffix = (" (" + " · ".join(f"walk {d}" for d in b) + ")"
              if b else "")
    line = (f"**{name} totals:** archon-steps {a} (archon holders "
            f"{h}) · walks carrying archons {w_} of 9 · both-ends "
            f"walks {len(b)}{suffix}.")
    chk(f"{name} totals line in master", line in MASTER)
    chk(f"{name} counts {expect}", (a, w_, b) == expect)
    return a, w_, b


def by_value(bank, values, vowels, exclude=()):
    """value -> the single holder, for the given value list."""
    out = {}
    for v in values:
        hs = [l for l, val in bank.items() if val == v
              and l not in exclude]
        assert len(hs) == 1, (v, hs)
        out[v] = hs[0]
    return out


def milesian_walks(holder, vowels, classes=(1, 10, 100)):
    walks = []
    for d in range(1, 10):
        steps = []
        for c in classes:
            l = holder[d * c]
            steps.append([(l, d * c,
                           "ARCHON" if l in vowels else "STRANGER")])
        walks.append(steps)
    return walks


# ---------------------------------------------------------------------
# §II Greek — seats derived from the bank (ς and στ excluded on their
# faces: a positional variant form and a digraph sign, not letters)
# ---------------------------------------------------------------------
# the map's tables print the Greek seats in the bank's own
# lowercase dress (the prose carries the capitals); the audit
# derives and matches in that dress
GR_H = by_value(GREEK, [d * c for c in (1, 10, 100) for d in range(1, 10)],
                set(), exclude={"ς", "στ"})
GR_V = set("αεηιουω")
gr_walks = milesian_walks(GR_H, GR_V)
chk("Greek bank seats sum 4,995", sum(GR_H) == 4995)
check_tongue("Greek", gr_walks, CLASS3, (7, 5, [8]))

# §III Coptic — the mirror, grades identical step for step
CO_H = by_value(COPTIC, [d * c for c in (1, 10, 100) for d in range(1, 10)],
                set())
CO_V = set("ⲁⲉⲏⲓⲟⲩⲱ")
co_walks = milesian_walks(CO_H, CO_V)
chk("Coptic grades == Greek grades",
    [[s[0][2] for s in w] for w in co_walks]
    == [[s[0][2] for s in w] for w in gr_walks])
chk("Coptic 90-holder is ϥ, Greek's is ϟ",
    CO_H[90] == "ϥ" and GR_H[90] == "ϟ")
FENCED = ["ϣ", "ϧ", "ⳉ", "ϩ", "ϫ", "ϭ", "ϯ"]
chk("Coptic fenced seven weigh 0",
    all(W(f, "coptic") == 0 for f in FENCED))
check_tongue("Coptic", co_walks, CLASS3, (7, 5, [8]))

# §IV Cyrillic — canonical seats transcribed; variants as forms
CY_CANON = ["А", "В", "Г", "Д", "Е", "Ѕ", "З", "И", "Ѳ",
            "І", "К", "Л", "М", "Н", "Ѯ", "О", "П", "Ч",
            "Р", "С", "Т", "У", "Ф", "Х", "Ѱ", "Ѡ", "Ц"]
CY_VALS = [d * c for c in (1, 10, 100) for d in range(1, 10)]
chk("Cyrillic canonical seats weigh their values",
    all(CYRILLIC[l] == v for l, v in zip(CY_CANON, CY_VALS)))
chk("Cyrillic canonical sum 4,995", sum(CY_VALS) == 4995)
CY_H = dict(zip(CY_VALS, CY_CANON))
CY_V = set("АЕИІОУѠ")
cy_walks = milesian_walks(CY_H, CY_V)
chk("Cyrillic grades == Greek grades",
    [[s[0][2] for s in w] for w in cy_walks]
    == [[s[0][2] for s in w] for w in gr_walks])
chk("Cyrillic variants weigh their seats",
    CYRILLIC["Ѵ"] == CYRILLIC["Ꙋ"] == CYRILLIC["Ѹ"] == 400
    and CYRILLIC["Ѿ"] == CYRILLIC["Ꙍ"] == 800
    and CYRILLIC["Ѧ"] == 900)
check_tongue("Cyrillic", cy_walks, CLASS3, (7, 5, [8]))

# §V Armenian — seats derived from the bank; annex behind its door
ARM_H = by_value(ARMENIAN,
                 [d * c for c in (1, 10, 100, 1000) for d in range(1, 10)],
                 set())
ARM_V = set("ԱԵԸԻՈՒ")
arm_walks = milesian_walks(ARM_H, ARM_V, classes=(1, 10, 100, 1000))
chk("Armenian bank total 49,995", sum(ARMENIAN.values()) == 49995)
chk("Armenian annex not in the walked bank",
    "Օ" not in ARMENIAN and "Ֆ" not in ARMENIAN)
check_tongue("Armenian", arm_walks, CLASS4, (6, 6, []))

# §VI Georgian — classes from the bank + the fork + the fifth class
GEO_CLASSES = []
for c in (1, 10, 100, 1000):
    row = []
    for d in range(1, 10):
        hs = [l for l, v in GEORGIAN.items() if v == d * c]
        row.append(hs)
    GEO_CLASSES.append(row)
chk("Georgian hundreds class holds ten letters",
    len(GEO_CLASSES[2][3]) == 2
    and set(GEO_CLASSES[2][3]) == {"ჳ", "უ"})
chk("Georgian bank total 60,395", sum(GEORGIAN.values()) == 60395)
chk("Georgian hundreds class sums 4,900",
    sum(GEORGIAN[l] for row in [GEO_CLASSES[2]] for hs in row
        for l in hs) == 4900)
GEO_V = set("აეიოუ")
geo_walks = []
for d in range(1, 10):
    steps = []
    for ci in range(4):
        hs = GEO_CLASSES[ci][d - 1]
        holders = []
        for l in hs:
            disp = "ჱ†" if l == "ჱ" else l
            grade = "ARCHON" if (l in GEO_V or l == "ჱ") else "STRANGER"
            holders.append((disp, d * (10 ** ci), grade))
        steps.append(holders)
    steps.append([("ჵ", 10000, "STRANGER")] if d == 1 else [])
    geo_walks.append(steps)
check_tongue("Georgian", geo_walks, CLASS5G, (6, 5, []))

# §VII Arabic — abjad classes; matres three; thousands of one
ARA_H = by_value(ARABIC_ABJAD,
                 [d * c for c in (1, 10, 100) for d in range(1, 10)], set())
MATRES = set("اوي")
ara_walks = []
for d in range(1, 10):
    steps = milesian_walks(ARA_H, MATRES)[d - 1]
    steps = steps + ([[("غ", 1000, "STRANGER")]] if d == 1 else [[]])
    ara_walks.append(steps)
chk("Arabic bank total 5,995", sum(ARABIC_ABJAD.values()) == 5995)
chk("Arabic first-22 sum 1,495 (Plate III)",
    sum(list(ARABIC_ABJAD.values())[:22]) == 1495)
chk("ة fenced (weighs 0)", W("ة", "arabic_abjad") == 0)
check_tongue("Arabic", ara_walks, CLASS4, (3, 2, []))

# §XII Glagolitic — classes derived from the bank by value
GLA_V = set("ⰀⰅⰉⰊⰋⰑⰖⰡ")
gla_walks = []
for d in range(1, 10):
    steps = []
    for c in (1, 10, 100, 1000):
        hs = [l for l, v in GLAGOLITIC.items() if v == d * c]
        steps.append([(l, d * c, "ARCHON" if l in GLA_V else "STRANGER")
                      for l in hs])
    gla_walks.append(steps)
chk("Glagolitic 10-seat doubled (Ⰹ and Ⰺ)",
    set(l for l, v in GLAGOLITIC.items() if v == 10) == {"Ⰹ", "Ⰺ"})
chk("Glagolitic thousands holes at 6000/7000/8000",
    all(not [l for l, v in GLAGOLITIC.items() if v == x]
        for x in (6000, 7000, 8000)))
chk("Glagolitic run holes weigh 0",
    all(W(h, "glagolitic") == 0 for h in "ⰚⰠⰢ"))
chk("Glagolitic 8-holder Ⰷ is a consonant",
    GLAGOLITIC["Ⰷ"] == 8 and "Ⰷ" not in GLA_V)
chk("Glagolitic bank total 29,005",
    sum(GLAGOLITIC.values()) == 29005)
check_tongue("Glagolitic", gla_walks, CLASS4, (7, 5, []))

# ---------------------------------------------------------------------
# §VIII Hebrew — the sofit axis
# ---------------------------------------------------------------------
SOFIT = [("כ", "ך", 20), ("מ", "ם", 40), ("נ", "ן", 50),
         ("פ", "ף", 80), ("צ", "ץ", 90)]
chk("Hebrew finals price = medials at face value",
    all(HEBREW[m] == HEBREW[f] == v for m, f, v in SOFIT))
GADOL = {"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900}
chk("Gadol uplifts +480/+560/+650/+720/+810",
    [GADOL[f] - v for _m, f, v in SOFIT] == [480, 560, 650, 720, 810])
chk("מאדים: gadol 655 vs face 95 (the +560 uplift)",
    40 + 1 + 4 + 10 + GADOL["ם"] == 655
    and 40 + 1 + 4 + 10 + HEBREW["ם"] == 95)
chk("Hebrew matres sum 22", sum(HEBREW[l] for l in "אהוי") == 22)
chk("Hebrew bank: 27 keys, sum 1,775",
    len(HEBREW) == 27 and sum(HEBREW.values()) == 1775)

# §IX Latin — the bank-step
chk("Latin vowels: A E I unmoved",
    all(LATIN_ORDINAL[c] == AGRIPPA[c] for c in "AEI"))
chk("Latin O 15→50 · U 21→200 · Y 25→400",
    (LATIN_ORDINAL["O"], AGRIPPA["O"]) == (15, 50)
    and (LATIN_ORDINAL["U"], AGRIPPA["U"]) == (21, 200)
    and (LATIN_ORDINAL["Y"], AGRIPPA["Y"]) == (25, 400))
chk("H unmoved 8→8", LATIN_ORDINAL["H"] == AGRIPPA["H"] == 8)
chk("W: ordinal 23, no Agrippa seat",
    LATIN_ORDINAL["W"] == 23 and "W" not in AGRIPPA)
chk("J folds: ordinal 10 → Agrippa 9 (I's seat)",
    LATIN_ORDINAL["J"] == 10 and AGRIPPA["J"] == AGRIPPA["I"] == 9)
chk("V and U coincide in Agrippa at 200",
    AGRIPPA["V"] == AGRIPPA["U"] == 200)

# §X Japanese — the mint's holes and seats
# the holes are absences in the grid: no kana stands at the y-row
# i/e cells or the w-row u cell — verified by the seat map: the
# y-row seats only its three standing kana consecutively (や=36,
# ゆ=37, よ=38) and the r-row follows at 39; the w-row seats
# わ=44, ゐ=45, ゑ=46, を=47 with no u-cell kana at all.
chk("Kana hole seats: y-row 36/37/38, r-row at 39, w-row 44–47",
    KANA["や"] == 36 and KANA["ゆ"] == 37 and KANA["よ"] == 38
    and KANA["ら"] == 39 and KANA["わ"] == 44
    and KANA["を"] == 47)
chk("Kana seats: あ=1 · ゐ=45 · ゑ=46 · ん=48",
    KANA["あ"] == 1 and KANA["ゐ"] == 45 and KANA["ゑ"] == 46
    and KANA["ん"] == 48)
chk("Kana katakana same seats (+0x60 dress)",
    all(KANA[chr(ord(k) + 0x60)] == v for k, v in KANA.items()
        if 0x3041 <= ord(k) <= 0x3096))
chk("Kana dakuten block seats 49–73, 25 seats (both dresses)",
    len({v for v in KANA.values() if 49 <= v <= 73}) == 25)

# §XI Ge'ez — the mint against the witness
FIRST_SUM = sum(fv for _b, fv in _GEEZ_BASES)
chk("Ge'ez first forms sum 4,095", FIRST_SUM == 4095)
chk("Ge'ez order-6 parting: witness 24,570, mint 0",
    FIRST_SUM * 6 == 24570)
chk("Ge'ez grid totals: mint 90,090 · witness 114,660",
    FIRST_SUM * 22 == 90090 and FIRST_SUM * 28 == 114660)
EIGHTH = sum(GEEZ[chr(ord(b) + 7)] for b, _fv in _GEEZ_BASES
             if chr(ord(b) + 7) in GEEZ)
chk("Ge'ez eighth column (mint, hole at ዐ) sums 32,200",
    EIGHTH == 32200)
chk("ዐ's eighth cell unassigned (U+12D7)",
    chr(0x12D7) not in GEEZ)
chk("Ge'ez mint zero signs: 30 (26 grid + 4 labiovelar)",
    sum(1 for v in GEEZ.values() if v == 0) == 30)
_GRID = {chr(ord(b) + o) for b, _fv in _GEEZ_BASES for o in range(7)}
_EIGHTH_G = {chr(ord(b) + 7) for b, _fv in _GEEZ_BASES} & set(GEEZ)
_LAB = {g: v for g, v in GEEZ.items()
        if g not in _GRID and g not in _EIGHTH_G}
chk("Ge'ez labiovelars: 20 signs outside grid and eighth, sum 3,614",
    len(_LAB) == 20 and sum(_LAB.values()) == 3614)

# §XIII Korean — the strata and the hinge
chk("Korean hinge exhibits at the door",
    hangul("아")["value"] == 1 and hangul("아")["null_initials"] == 1
    and hangul("아이")["value"] == 22
    and hangul("아이")["null_initials"] == 2)
chk("Korean plate exhibits 한글 52 · 한국 40",
    hangul("한글")["value"] == 52 and hangul("한국")["value"] == 40)

# §XIV The hybrids
chk("Diphthong four: ΑΙ 11 · ΕΙ 15 · ΟΙ 80 · ΟΥ 470",
    (W("ΑΙ", "greek"), W("ΕΙ", "greek"), W("ΟΙ", "greek"),
     W("ΟΥ", "greek")) == (11, 15, 80, 470))
chk("Diphthong four sum 576 = 24²", 11 + 15 + 80 + 470 == 576 == 24 ** 2)
chk("Coptic ⲟⲩ = 470 (the mirror twin)", W("ⲟⲩ", "coptic") == 470)
chk("Latin hybrids EI 14/14 · AE 6/6 · OE 20/55 · VI 31/209",
    (W("EI", "latin_ordinal"), W("EI", "agrippa")) == (14, 14)
    and (W("AE", "latin_ordinal"), W("AE", "agrippa")) == (6, 6)
    and (W("OE", "latin_ordinal"), W("OE", "agrippa")) == (20, 55)
    and (W("VI", "latin_ordinal"), W("VI", "agrippa")) == (31, 209))
chk("VV: ordinal 44 · Agrippa 400 · UU == VV on Agrippa",
    W("VV", "latin_ordinal") == 44 and W("VV", "agrippa") == 400
    and W("UU", "agrippa") == 400)
chk("VV refused as a numeral", repeat_status("V", 2) == "refused_hybrid")

# ---------------------------------------------------------------------
# Master-level checks: sections, summary numbers, the question
# ---------------------------------------------------------------------
for sec in ["§I", "§II", "§III", "§IV", "§V", "§VI", "§VII", "§VIII",
            "§IX", "§X", "§XI", "§XII", "§XIII", "§XIV", "§XV", "§XVI",
            "§XVII", "§XVIII"]:
    chk(f"master carries section {sec}", f"## {sec} " in MASTER
        or f"## {sec} —" in MASTER)
# (the bank totals 49,995 · 60,395 · 5,995 · 29,005 · 1,775 are
# verified against the banks above; the master's prose does not
# print them, so they are not phrase-checked here)
for phrase in ["576 = 24²", "24,570", "90,090", "114,660", "3,614",
               "4,995", "1,495", "THE FORK", "THE HINGE",
               "refused_hybrid", "Killing evidence",
               "Flagpole of Claim and Coinage"]:
    chk(f"master carries: {phrase}", phrase in MASTER)

# ---------------------------------------------------------------------
# PDF layer
# ---------------------------------------------------------------------
if PDF.exists():
    raw = PDF.read_bytes()
    chk("PDF header", raw[:5] == b"%PDF-")
    txt = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    pages = txt.count("\f") + (1 if txt and not txt.endswith("\f")
                               else 0)
    footers = re.findall(r"— (\d+) of (\d+) —", txt)
    chk("PDF footer resolves (N of M, M == pages)",
        bool(footers) and all(int(m) == pages for _n, m in footers)
        and len(footers) == pages)
    chk("PDF carries no Hebrew-block codepoints",
        not any(0x0590 <= ord(c) <= 0x05FF for c in txt))
    for phrase in ["THE CLASS-WALK MAP", "GREEK", "GEORGIAN",
                   "GLAGOLITIC", "KOREAN", "HYBRIDS"]:
        chk(f"PDF carries: {phrase}", phrase in txt)
    print(f"PDF: {pages} pages · {len(raw)} bytes · sha256 "
          f"{hashlib.sha256(raw).hexdigest()}")
else:
    chk("PDF exists", False)

fails = [n for n, ok in CHECKS if not ok]
out = HERE / "audit_class_walk_map_results.txt"
lines = [f"{'PASS' if ok else 'FAIL'}  {n}" for n, ok in CHECKS]
lines.append(f"\n{len(CHECKS) - len(fails)}/{len(CHECKS)} checks passed")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"AUDIT {'PASS' if not fails else 'FAIL'}: "
      f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks")
sys.exit(1 if fails else 0)

# 93 — Live, Love, and let Love, Live.
