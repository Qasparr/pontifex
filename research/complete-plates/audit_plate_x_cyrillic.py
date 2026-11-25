#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_x_cyrillic.py
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
# MECHANISM: the independent audit of PLATE-X-CYRILLIC. It
# does not read the plate's own figures for its expectations:
# every priced cell is re-weighed on the house engine from
# its source — the bank from pontifex.tables, the frozen
# transcription from research/caucasus-north/
# cyrillic-table.csv, the frame from THE-TWELVE-TABLES
# §V.10 — and only then compared against what the plate
# prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the canonical table entire: the plate's §II.1 rows
#      (27) parsed — seat, letter, Greek parent, name,
#      value, class — against CYRILLIC, the frozen CSV and
#      the living GREEK bank at the pairings; the class law
#      recomputed per seat; the canonical sum 4,995 and
#      the class sums printed;
#   3. the variant forms: the plate's §II.2 rows (6)
#      against the bank and the frozen CSV's VARIANT rows;
#      the forms' seat counts (400 ×4 writings incl. the
#      canonical, 800 ×3, 900 ×2);
#   4. the census: 33 keys, 27 distinct values, bank sum
#      8,695, maximum 900; the descent's value sets
#      identical (canonical values == the parent's 27
#      seat values);
#   5. calibration: the witnesses' five worked examples;
#   6. the devices at the door: the ҂ exhibits (6000,
#      32000, 1705, 7118); the titlo counted, priced
#      never; the higher signs counted, priced none;
#      weigh()'s silence on the thousands sign;
#   7. the boundary: cherv == 90; the koppa-letter's
#      silence; the plate's refused-pair rows parsed;
#      the eleven modern letters' silence; the case fold
#      (и == 8; ѹ == 400; ѱз == 707);
#   8. the frame: the census parsed from THE-TWELVE-
#      TABLES §V.10 against the plate's printed census;
#      the plate's 180 DOOR rows — cell set and order
#      equal to the register's, each rendering re-weighed
#      against its filed value; the 43 FENCED rows in
#      order, each crossing a fenced letter, each value
#      the dash; the 62 HOLE rows in order; the GAP cell
#      CLXXXIV/10 on the plate;
#   9. the zero face: the claim count 0 standing on the
#      plate;
#  10. the §V figures: the mirror seven from the plate's
#      table against the bank; the five tongues' vowel
#      at 8 in their own banks (η · ⲏ · И · Ը · ჱ);
#      І == 10 and Ѡ == 800; the Latin counterweights
#      (I == 9 ordinal; O == 15 ordinal, 50 Agrippa);
#      οὐδέν == 529; the Nine sum 1779;
#  11. if the MAGVS PDF stands beside the master, its
#      text layer carries all 33 letters and the zero
#      face's statement; its footer resolves; and no
#      Hebrew-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_x_cyrillic_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. A figure reproduced through the wrong species
# — the descent spent as independent attestation, a
# variant form counted as a seat, a mark priced, either
# half of the refused pair seated — is a failure, not a
# match.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh
from pontifex.engine import cyrillic
from pontifex.tables import CYRILLIC, GREEK

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-X-CYRILLIC.md"
PDF = GOAL_FILES / "PLATE-X-CYRILLIC-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/cyrillic-table.csv")
RESULTS = HERE / "audit_plate_x_cyrillic_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="cyrillic"):
    return weigh(word, bank)["value"]


with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
CANON = [r for r in CSV_ROWS if r["status"] == "SOURCED"]
VARIANTS = [r for r in CSV_ROWS if r["status"] == "VARIANT"]
BY_SEAT = {int(r["seat"]): r for r in CANON}
BY_LETTER_VAR = {r["letter"]: r for r in VARIANTS}

# the letters' names as the generator prints them — the
# audit carries the same record-derived table to compare
# the plate's name cells against (prose furniture; every
# priced figure below is re-weighed independently).
NAMES = {
    "А": "az", "В": "vede", "Г": "glagoli", "Д": "dobro",
    "Е": "yest", "Ѕ": "dzelo", "З": "zemlja", "И": "izhe",
    "Ѳ": "fita", "І": "i", "К": "kako", "Л": "ljudie",
    "М": "myslite", "Н": "nash", "Ѯ": "ksi", "О": "on",
    "П": "pokoj", "Ч": "chrьvъ", "Р": "rьci", "С": "slovo",
    "Т": "tvrьdo", "У": "ukъ", "Ф": "frьtъ", "Х": "xěrъ",
    "Ѱ": "psi", "Ѡ": "omega", "Ц": "ci",
    "Ѵ": "izhitsa", "Ꙋ": "uk (monograph)", "Ѹ": "uk (digraph)",
    "Ѿ": "ot", "Ꙍ": "broad omega", "Ѧ": "little yus",
    "Ҁ": "koppa",
}


def class_of(seat):
    if seat <= 9:
        return "units", seat, 0
    if seat <= 18:
        return "tens", seat - 9, 1
    return "hundreds", seat - 18, 2


master = MASTER.read_text(encoding="utf-8")
# MECHANISM: the section splits are line-anchored ("\n## §…")
# because this plate's subsection headings (### §II.1 …)
# contain the unanchored string as a substring.
sec2 = master.split("\n## §II")[1].split("\n## §III")[0]
sec3 = master.split("\n## §III")[1].split("\n## §IV")[0]
sec4 = master.split("\n## §IV")[1].split("\n## §V")[0]
sec5 = master.split("\n## §V")[1].split("\n## §VI")[0]

# --- 1. controls -------------------------------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)

# --- 2. the canonical table entire ---------------------------------------
rows = re.findall(r"^\| (\d+) \| (\S) \| (\S) \| ([^|]+?) \| "
                  r"(\d+) \| (units|tens|hundreds) \|", sec2, re.M)
check("canonical table: 27 rows parsed", len(rows) == 27,
      str(len(rows)))
for (seat, letter, parent, name, val, cls) in rows:
    seat, val = int(seat), int(val)
    want_cls, digit, power = class_of(seat)
    csv_row = BY_SEAT[seat]
    check(f"seat {seat} {letter}: letter, parent, name, value, "
          f"class == engine + frozen CSV + living GREEK",
          letter == csv_row["letter"]
          and parent == csv_row["greek_pair"]
          and name == NAMES[letter]
          and val == CYRILLIC[letter] == int(csv_row["value"])
          and GREEK[parent.lower()] == val
          and val == digit * 10 ** power
          and cls == want_cls)
check("canonical sum 4995 printed", "**4995**" in sec2
      or "**4,995**" in sec2)
check("canonical sum == Milesian sum",
      sum(int(r["value"]) for r in CANON) == 4995
      and sum(GREEK.values()) - 200 - 6 == 4995)
_cs = {}
for r in CANON:
    c, _d, _p = class_of(int(r["seat"]))
    _cs[c] = _cs.get(c, 0) + int(r["value"])
check("class sums 45/450/4500",
      _cs == {"units": 45, "tens": 450, "hundreds": 4500},
      str(_cs))

# --- 3. the variant forms --------------------------------------------------
vrows = re.findall(r"^\| (\S) \| (\d+) \(the (\S) seat\) \| "
                   r"([^|]+?) \| (\d+) \| variant form \|",
                   sec2, re.M)
check("variant table: 6 rows parsed", len(vrows) == 6,
      str(len(vrows)))
for (letter, seat_val, holder, name, val) in vrows:
    csv_row = BY_LETTER_VAR[letter]
    check(f"variant {letter}: seat, holder, name, value == "
          f"bank + frozen CSV",
          int(val) == CYRILLIC[letter] == int(csv_row["value"])
          and int(seat_val) == int(val)
          and holder in CYRILLIC
          and CYRILLIC[holder] == int(val)
          and name == NAMES[letter])
for v, n in ((400, 4), (800, 3), (900, 2)):
    check(f"the {v}-seat carries {n} writings in the bank",
          sum(1 for x in CYRILLIC.values() if x == v) == n)

# --- 4. the census and the descent -------------------------------------------
check("33 keys, 27 distinct values, sum 8695, maximum 900",
      len(CYRILLIC) == 33
      and len(set(CYRILLIC.values())) == 27
      and sum(CYRILLIC.values()) == 8695
      and max(CYRILLIC.values()) == 900)
check("bank sum 8695 printed", "**8695**" in sec2
      or "**8,695**" in sec2)
check("the descent's value sets identical: canonical values "
      "== the parent's 27 seat values",
      {int(r["value"]) for r in CANON}
      == {GREEK[r["greek_pair"].lower()] for r in CANON}
      and len({int(r["value"]) for r in CANON}) == 27)

# --- 5. calibration ---------------------------------------------------------
for w, want in (("ѰЗ", 707), ("ЦЧѲ", 999), ("РНГ", 153),
                ("КЗ", 27), ("ОВ", 72)):
    check(f"worked example {w} == {want}", value(w) == want)
    check(f"plate prints {w} at {want}", f"| {w} | {want} |" in sec2)

# --- 6. the devices at the door ------------------------------------------------
for w, want in (("҂Ѕ", 6000), ("҂Л҂В", 32000),
                ("҂АѰЕ", 1705), ("҂ЗРИІ", 7118)):
    check(f"door exhibit {w} == {want}",
          cyrillic(w)["value"] == want)
    check(f"plate prints {w} at {want}",
          f"| {w} | {want} |" in sec2)
_t = cyrillic("А҃")
check("the titlo counted, priced never: А҃ == 1, 1 titlo",
      _t["value"] == 1 and _t["titlo_marks"] == 1)
_h = cyrillic("А҉")
check("the higher signs counted, priced none: А҉ == 1, "
      "1 higher mark",
      _h["value"] == 1 and _h["higher_marks"] == 1)
check("weigh() prices no thousands sign: ҂Ѕ == 6 at the "
      "raw bank", value("҂Ѕ") == 6)

# --- 7. the boundary ---------------------------------------------------------
check("cherv at its canonical price: Ч == 90", value("Ч") == 90)
_w = weigh("Ҁ", "cyrillic")
check("the koppa-letter's silence: Ҁ == 0, empty breakdown",
      _w["value"] == 0 and _w["breakdown"] == [])
rrows = re.findall(r"^\| (Ч|Ҁ) \| (\d+) \| ([^|]+?) \| "
                   r"(weighs 90|silence) \|", sec2, re.M)
check("refused-pair table: 2 rows parsed", len(rrows) == 2,
      str(len(rrows)))
check("refused pair as filed: Ч/60 refused, Ҁ/90 refused",
      {(r[0], int(r[1])) for r in rrows} == {("Ч", 60), ("Ҁ", 90)})
for ch in "БЖШЩЪЫЬЭЮЯЙ":
    _w = weigh(ch, "cyrillic")
    check(f"modern letter {ch}: silence at the bank",
          _w["value"] == 0 and _w["breakdown"] == []
          and ch not in CYRILLIC)
check("the case fold: и == 8; ѹ == 400; ѱз == 707",
      value("и") == 8 and value("ѹ") == 400
      and value("ѱз") == 707)

# --- 8. the frame -------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.10 — The Cyrillic Table")[1] \
    .split("### §V.11")[0]
cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
               r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
               r"(\d+) · GAP (\d+)", block)
counts = tuple(int(x) for x in cl.groups())
check("register census == (0, 180, 62, 43, 85, 1)",
      counts == (0, 180, 62, 43, 85, 1), str(counts))
for label, n in (("NATIVE", 0), ("DOOR", 180), ("HOLE", 62),
                 ("FENCED", 43)):
    check(f"plate prints census {label} {n}",
          f"{label} **{n}**" in sec3)
reg = {"DOOR": [], "HOLE": [], "FENCED": []}
for line in block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in reg:
            reg[cells[2]].append(cells)
door_block = sec3.split("**The door register")[1] \
    .split("**The fenced register")[0]
fenced_block = sec3.split("**The fenced register")[1] \
    .split("**The hole register")[0]
hole_block = sec3.split("**The hole register")[1] \
    .split("**The one GAP cell")[0]


def plate_rows(block_text):
    out = []
    for ln in block_text.splitlines():
        if not ln.startswith("| "):
            continue
        cells = [c.strip()
                 for c in ln.strip().strip("|").split("|")]
        if len(cells) == 4 and re.match(r"[A-Z]+/", cells[0]):
            out.append(cells)
    return out


plate_doors = plate_rows(door_block)
plate_fenced = plate_rows(fenced_block)
plate_holes = plate_rows(hole_block)
check("plate door register: 180 rows", len(plate_doors) == 180,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg["DOOR"]])
for cells in reg["DOOR"]:
    check(f"door {cells[0]} {cells[3]}: re-weighed",
          value(cells[3]) == int(cells[4]))
check("plate fenced register: 43 rows", len(plate_fenced) == 43,
      str(len(plate_fenced)))
check("plate fenced rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_fenced]
      == [[c[0], c[1], c[3], c[5]] for c in reg["FENCED"]])
FENCED_SET = set("БЖШЩЪЫЬЭЮЯЙ")
for cells in reg["FENCED"]:
    check(f"fenced {cells[0]} {cells[3]}: crosses a fenced "
          f"letter, value the dash",
          cells[4] == "—"
          and bool(set(cells[3].upper()) & FENCED_SET))
check("plate hole register: 62 rows", len(plate_holes) == 62,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_holes]
      == [[c[0], c[1], c[3], c[5]] for c in reg["HOLE"]])
check("every hole rendering is the register's dash",
      all(c[3] == "—" for c in reg["HOLE"]))
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 9. the zero face -----------------------------------------------------------
check("plate prints the claim count: 0",
      "**Claims on this plate: 0**" in sec4)
check("the zero face stands in §IV", "THE ZERO FACE" in sec4)

# --- 10. the §V figures ------------------------------------------------------------
vow = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+) \|$", sec5, re.M)
vow = [r for r in vow if r[0] in "АЕИІОУѠ" and len(r[0]) == 1]
check("§V vowel table: 7 rows parsed", len(vow) == 7,
      str(len(vow)))
for ch, name, v in vow:
    check(f"§V vowel {ch}: price == bank",
          int(v) == CYRILLIC[ch])
check("the mirror seven at the Greek prices "
      "1/5/8/10/70/400/800",
      [value(c) for c in "АЕИІОУѠ"]
      == [1, 5, 8, 10, 70, 400, 800])
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
check("the mirror witnesses: І == 10, Ѡ == 800 in cyrillic",
      value("І") == 10 and value("Ѡ") == 800)
check("the counterweights: Latin I == 9 (ordinal); "
      "O == 15 (ordinal), 50 (Agrippa)",
      value("I", "latin_ordinal") == 9
      and value("O", "latin_ordinal") == 15
      and value("O", "agrippa") == 50)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))

# --- 11. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    missing = [c for c in CYRILLIC if c not in layer]
    check("PDF layer carries all 33 letters", not missing,
          f"missing: {missing}")
    check("PDF layer carries the zero face's statement",
          "THE ZERO FACE" in layer
          or "Claims on this plate: 0" in layer)
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
lines = ["PLATE-X-CYRILLIC — independent audit",
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
