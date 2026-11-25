#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_vi_geez.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: the independent audit of PLATE-VI-GEEZ. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the banks from pontifex.tables, the doors through
# engine.geez()/halehame(), the frame from THE-TWELVE-TABLES
# §V.6 — and only then compared against what the plate prints.
# Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the shared foundation: the plate's §II.1 bases table
#      (26 rows) — position, base, and first-form value
#      against both banks' first-form maps; the class law
#      recomputed per position; the fixed point (value =
#      position, positions 1–10) and its parting at 11;
#   3. both grids entire: the plate's §II.3 mint and witness
#      tables parsed cell by cell (182 cells each) against
#      GEEZ and HALEHAME, row sums and column totals; the
#      grids' difference equal to the witness's order-6
#      column;
#   4. the labiovelar table (20 rows): mint prices against
#      the bank, witness silence at every row; the eighth
#      column (25 priced rows + the hole): glyph = base + 7,
#      price = first × 8, U+12D7 unassigned in the standard;
#   5. the seat register: the plate's §II.6 rows (227) parsed
#      and compared seat by seat — sign, base, order, both
#      banks' prices — against GEEZ_BASE and the banks; the
#      thirty Zero signs, all at order 6;
#   6. the calibration heads at all four doors (ክርስቶስ
#      70/80/80/490 · ሰላም 15/13/13/39), the plate's printed
#      readings beside the engine's; the fences: the derived
#      rows' silence in both banks, the Ethiopic numerals'
#      skip;
#   7. the census totals as printed (125904 · 114660 ·
#      90090) against the banks' sums; 90 distinct mint
#      values, maximum 6400; 87 distinct witness values,
#      maximum 5600;
#   8. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.6 against the plate's printed census; the plate's
#      205 DOOR rows — cell set and order equal to the
#      register's, each rendering re-weighed against its
#      filed value; the 80 HOLE rows present in order with
#      coordinates, every shown rendering crossing an
#      unseated sign; the GAP cell CLXXXIV/10 on the plate;
#   9. the §V figures: the five tongues' vowel at 8 in their
#      own banks (η · ⲏ · И · Ը · ჱ); οὐδέν == 529; the
#      Nine sum 1779;
#  10. if the MAGVS PDF stands beside the master, its text
#      layer carries the calibration head, all 26 base
#      signs, the zero face's statement, and the three
#      codepoint tokens; its footer resolves; and no
#      Hebrew-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_vi_geez_results.txt beside
# this script. VERDICT PASS requires every check green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. The two banks are audited as two: a figure
# reproduced from the wrong bank is a failure, not a match.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh
from pontifex.engine import geez as geez_door, halehame as halehame_door
from pontifex.tables import (GEEZ, GEEZ_FIRST, GEEZ_BASE, HALEHAME,
                             HALEHAME_FIRST, _GEEZ_BASES,
                             _GEEZ_LABIOVELAR_HEADS,
                             _GEEZ_LABIOVELAR_OFFSETS,
                             _GEEZ_EIGHTH_SLOT_HOLE)

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-VI-GEEZ.md"
PDF = GOAL_FILES / "PLATE-VI-GEEZ-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
RESULTS = HERE / "audit_plate_vi_geez_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="geez"):
    return weigh(word, bank)["value"]


master = MASTER.read_text(encoding="utf-8")
# MECHANISM: the section splits are line-anchored ("\n## §…")
# because this plate's subsection headings (### §II.1 …) contain
# the unanchored string as a substring — an unanchored split
# cuts the section at its first subsection.
sec2 = master.split("\n## §II")[1].split("\n## §III")[0]
sec3 = master.split("\n## §III")[1].split("\n## §IV")[0]
sec5 = master.split("\n## §V")[1].split("\n## §VI")[0]

# --- 1. controls -------------------------------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)

# --- 2. the shared foundation -------------------------------------------
bases = re.findall(r"^\| (\d+) \| (\S) \| ([^|]+?) \| (\d+) \| "
                   r"(units|tens|hundreds) \|", sec2, re.M)
check("bases table: 26 rows parsed", len(bases) == 26, str(len(bases)))
for (pos, b, _nm, fv, cls), (eb, efv) in zip(bases, _GEEZ_BASES):
    pos, fv = int(pos), int(fv)
    check(f"base {pos} {b}: first form {fv} == both banks",
          b == eb and fv == efv == GEEZ_FIRST[b] == HALEHAME_FIRST[b])
    want_cls = "units" if pos <= 10 else "tens" if pos <= 19 \
        else "hundreds"
    check(f"base {pos} {b}: class {cls}", cls == want_cls)
    if pos <= 10:
        check(f"fixed point at {pos}: value == position", fv == pos)
check("fixed point parts at 11: ኀ == 20 at position 11",
      _GEEZ_BASES[10] == ("ኀ", 20))
check("first-form sum 4095 printed", "**4095**" in sec2)
check("first-form sum == 4095",
      sum(fv for _b, fv in _GEEZ_BASES) == 4095)

# --- 3. both grids --------------------------------------------------------
def parse_grid(block, bank, label):
    rows = re.findall(r"^\| (\S) \((\d+)\) \| (.+) \| (\d+) \|$",
                      block, re.M)
    check(f"{label} grid: 26 rows parsed", len(rows) == 26,
          str(len(rows)))
    col_tot = {o: 0 for o in range(1, 8)}
    for (b, fv, cells_s, rowsum), (eb, efv) in zip(rows, _GEEZ_BASES):
        check(f"{label} row head {b} ({fv})", b == eb
              and int(fv) == efv)
        cells = cells_s.split(" | ")
        check(f"{label} row {b}: 7 cells", len(cells) == 7)
        tot = 0
        for o, cell in enumerate(cells, 1):
            m = re.match(r"(\S) — (\d+)$", cell)
            sign = chr(ord(b) + o - 1)
            ok = m and m.group(1) == sign \
                and int(m.group(2)) == bank[sign]
            check(f"{label} cell {sign}: price == engine", ok,
                  cell)
            tot += bank[sign]
            col_tot[o] += bank[sign]
        check(f"{label} row {b}: sum == printed",
              tot == int(rowsum), f"{tot} vs {rowsum}")
    return col_tot


mint_block = sec2.split("**The mint's grid**")[1] \
    .split("**The witness's grid**")[0]
wit_block = sec2.split("**The witness's grid**")[1] \
    .split("**The columns.**")[0]
mint_cols = parse_grid(mint_block, GEEZ, "mint")
wit_cols = parse_grid(wit_block, HALEHAME, "witness")
for o in range(1, 8):
    check(f"mint column {o} == 4095 × {0 if o == 6 else o}",
          mint_cols[o] == 4095 * (0 if o == 6 else o))
    check(f"witness column {o} == 4095 × {o}",
          wit_cols[o] == 4095 * o)
check("grids' difference == witness order-6 column (24570)",
      sum(wit_cols.values()) - sum(mint_cols.values())
      == wit_cols[6] == 24570)

# --- 4. labiovelars and the eighth column ---------------------------------
lab = re.findall(r"^\| (\S) \| (\S) \| (\S) \| (\d+) \| (\d+) \| "
                 r"(\d+) \| \*\*GAP\*\*", sec2, re.M)
check("labiovelar table: 20 rows parsed", len(lab) == 20,
      str(len(lab)))
expect_lab = []
for head, base in _GEEZ_LABIOVELAR_HEADS:
    fv = dict(_GEEZ_BASES)[base]
    for order, off in sorted(_GEEZ_LABIOVELAR_OFFSETS.items()):
        expect_lab.append((chr(ord(head) + off), head, base, fv,
                           order))
for (ch, head, base, fv, order, mv), exp in zip(lab, expect_lab):
    check(f"labiovelar {ch}: seat and mint price == engine",
          (ch, head, base, int(fv), int(order)) == exp
          and int(mv) == GEEZ[ch])
    check(f"labiovelar {ch}: witness silence", ch not in HALEHAME)
check("labiovelar total 3614 printed", "**3614**" in sec2)
check("labiovelar total == engine",
      sum(GEEZ[c] for c in GEEZ_BASE[182:202]) == 3614)

eighth = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+) \| (\S) \| "
                    r"(\d+) \|$", sec2, re.M)
eighth = [r for r in eighth if r[0] in dict(_GEEZ_BASES)
          and len(r[0]) == 1]
check("eighth column: 25 priced rows parsed", len(eighth) == 25,
      str(len(eighth)))
for b, _nm, fv, g, mv in eighth:
    check(f"eighth {b}: glyph {g} == base + 7, price == first × 8",
          g == chr(ord(b) + 7) and int(mv) == GEEZ[g]
          and int(mv) == int(fv) * 8)
check("the hole stands on the plate: ዐ + U+12D7 + HOLE",
      "**HOLE**" in sec2 and "U+12D7" in sec2
      and _GEEZ_EIGHTH_SLOT_HOLE == "ዐ")
try:
    unicodedata.name(chr(0x12D7))
    hole_real = False
except ValueError:
    hole_real = True
check("U+12D7 is unassigned in the standard", hole_real)
check("U+12D7 is not a key of the mint", chr(0x12D7) not in GEEZ)
check("eighth total 32200 printed", "**32200**" in sec2)
check("eighth total == engine",
      sum(GEEZ[c] for c in GEEZ_BASE[202:]) == 32200)

# --- 5. the seat register ---------------------------------------------------
reg = re.findall(r"^\| (\d+) \| (\S) \| (\S) \| (\d+) \| (\d+) \| "
                 r"(\d+|GAP) \|$", sec2, re.M)
check("seat register: 227 rows parsed", len(reg) == 227,
      str(len(reg)))
for (seat, ch, b, order, mv, wv) in reg:
    seat, order, mv = int(seat), int(order), int(mv)
    ok = GEEZ_BASE[seat - 1] == ch and GEEZ[ch] == mv
    if seat <= 182:
        eb, _f = _GEEZ_BASES[(seat - 1) // 7]
        ok = ok and b == eb and order == (seat - 1) % 7 + 1
    elif seat <= 202:
        esign, _h, ebase, _fv, eorder = expect_lab[seat - 183]
        ok = ok and ch == esign and b == ebase and order == eorder
    else:
        ok = ok and b == chr(ord(ch) - 7) and order == 8
    if wv == "GAP":
        ok = ok and ch not in HALEHAME
    else:
        ok = ok and HALEHAME.get(ch) == int(wv)
    check(f"seat {seat} {ch}: base/order/prices == engine", ok)
zeros = [c for c in GEEZ_BASE if GEEZ[c] == 0]
check("thirty Zero signs in the mint", len(zeros) == 30)
check("every Zero sign stands at order 6",
      all(GEEZ_BASE.index(c) % 7 == 5 or GEEZ_BASE.index(c) >= 182
          for c in zeros))
m = re.search(r"Zero column entire: ([^.]+)\.", sec2)
printed_zeros = m.group(1).split(" · ") if m else []
check("the plate prints the thirty Zero signs entire",
      printed_zeros == zeros,
      f"{len(printed_zeros)} printed")

# --- 6. calibration and fences ----------------------------------------------
check("ክርስቶስ MW == 70", value("ክርስቶስ", "geez") == 70)
check("ክርስቶስ MF == 80", geez_door("ክርስቶስ")["value"] == 80)
check("ክርስቶስ WP == 80", halehame_door("ክርስቶስ")["value"] == 80)
check("ክርስቶስ WG == 490", value("ክርስቶስ", "halehame") == 490)
for door, want in (("MF", 80), ("WP", 80), ("MW", 70), ("WG", 490)):
    mm = re.search(rf"\| {door} — [^|]+ \| \*\*(\d+)\*\*", sec2)
    check(f"plate prints ክርስቶስ {door} == {want}",
          mm and int(mm.group(1)) == want)
check("ሰላም doors == 15/13/13/39",
      (value("ሰላም", "geez"), geez_door("ሰላም")["value"],
       halehame_door("ሰላም")["value"], value("ሰላም", "halehame"))
      == (15, 13, 13, 39))
for probe in ("ሸ", "ቸ", "ቐ", "ጀ"):
    check(f"derived sign {probe}: silence in both banks",
          probe not in GEEZ and probe not in HALEHAME
          and weigh(probe, "geez")["breakdown"] == []
          and weigh(probe, "halehame")["breakdown"] == [])
check("numeral ፩ skipped in both banks",
      weigh("፩", "geez")["breakdown"] == []
      and weigh("፩", "halehame")["breakdown"] == [])

# --- 7. census ----------------------------------------------------------------
check("mint total 125904 printed", "**125904**" in sec2)
check("mint total == engine", sum(GEEZ.values()) == 125904)
check("witness total 114660 printed", "**114660**" in sec2)
check("witness total == engine", sum(HALEHAME.values()) == 114660)
check("mint grid total 90090 printed", "**90090**" in sec2)
check("mint: 90 distinct values, max 6400",
      len(set(GEEZ.values())) == 90 and max(GEEZ.values()) == 6400)
check("witness: 87 distinct values, max 5600",
      len(set(HALEHAME.values())) == 87
      and max(HALEHAME.values()) == 5600)
check("folk examples in the grid: ሁ 2 · ሉ 4 · ፖ 5600",
      HALEHAME["ሁ"] == 2 and HALEHAME["ሉ"] == 4
      and HALEHAME["ፖ"] == 5600)

# --- 8. the frame ---------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.6 — The Ge'ez Table")[1] \
    .split("### §V.7")[0]
cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
               r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
               r"(\d+) · GAP (\d+)", block)
counts = tuple(int(x) for x in cl.groups())
check("register census == (0, 205, 80, 0, 85, 1)",
      counts == (0, 205, 80, 0, 85, 1), str(counts))
for label, n in (("NATIVE", 0), ("DOOR", 205), ("HOLE", 80),
                 ("FENCED", 0)):
    check(f"plate prints census {label} {n}",
          f"{label} **{n}**" in sec3)
reg_doors, reg_holes = [], []
for line in block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] == "DOOR":
            reg_doors.append(cells)
        elif len(cells) == 6 and cells[2] == "HOLE":
            reg_holes.append(cells)
plate_doors, plate_holes = [], []
for ln in sec3.splitlines():
    if not ln.startswith("| "):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) == 4 and re.match(r"[A-Z]+/", cells[0]) \
            and cells[3].isdigit():
        plate_doors.append(cells)
    elif len(cells) == 4 and re.match(r"[A-Z]+/", cells[0]) \
            and not cells[3].isdigit():
        plate_holes.append(cells)
check("plate door register: 205 rows", len(plate_doors) == 205,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg_doors])
for cells in reg_doors:
    check(f"door {cells[0]} {cells[3]}: re-weighed",
          value(cells[3]) == int(cells[4]))
check("plate hole register: 80 rows", len(plate_holes) == 80,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_holes]
      == [[c[0], c[1], c[3], c[5]] for c in reg_holes])
shown = [c for c in reg_holes if c[3] != "—"]
check("hole species: shown renderings cross unseated signs",
      all(any(ch not in GEEZ for ch in c[3] if ch.strip())
          for c in shown), f"{len(shown)} shown")
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 9. the §V figures ------------------------------------------------------------
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))
check("zero face stands in §IV", "THE ZERO FACE" in master
      and "**Claims on this plate: 0**" in master)

# --- 10. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    check("PDF layer carries the calibration head ክርስቶስ",
          "ክርስቶስ" in layer)
    missing = [b for b, _f in _GEEZ_BASES if b not in layer]
    check("PDF layer carries all 26 base signs", not missing,
          f"missing: {missing}")
    check("PDF layer carries the zero face", "ZERO FACE" in layer)
    for tok in ("[U+12B1]", "[U+1311]", "[U+1316]"):
        check(f"PDF layer carries token {tok}", tok in layer)
    check("PDF layer: no Hebrew-block codepoint",
          not any(0x590 <= ord(c) <= 0x5FF for c in layer))
    info = subprocess.run(["pdfinfo", str(PDF)], capture_output=True,
                          text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    check(f"PDF footer resolves ({pages} of {pages})",
          f"{pages} of {pages}" in layer)
else:
    check("MAGVS PDF exists", False, "not built")

# --- verdict ---------------------------------------------------------------------------
failed = [(n, d) for n, ok, d in CHECKS if not ok]
lines = ["PLATE-VI-GEEZ — independent audit",
         f"checks: {len(CHECKS)} · failed: {len(failed)}", ""]
for name, ok, detail in CHECKS:
    lines.append(f"{'PASS' if ok else 'FAIL'}  {name}"
                 + (f"  [{detail}]" if detail and not ok else ""))
lines.append("")
lines.append(f"VERDICT: {'PASS' if not failed else 'FAIL'} — "
             f"{len(CHECKS)} checks, {len(failed)} failures")
RESULTS.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[-3:]))
sys.exit(0 if not failed else 1)
