#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_ix_georgian.py
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
# MECHANISM: the independent audit of PLATE-IX-GEORGIAN. It
# does not read the plate's own figures for its expectations:
# every priced cell is re-weighed on the house engine from
# its source — the bank from pontifex.tables, the frozen
# transcriptions from research/caucasus-north/
# georgian-table.csv and georgian-control-case.csv, the
# frame from THE-TWELVE-TABLES §V.9 — and only then compared
# against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the bank entire: the plate's §II.1 rows (38) parsed —
#      position, letter, Asomtavruli and Nuskhuri partners,
#      name, value, class — against GEORGIAN and the frozen
#      CSV; the class law recomputed per seat (digit read
#      off the value); the seat law's parting at exactly
#      positions 23–28; the sum 60,395 and the class sums
#      printed; 37 distinct values; maximum 10,000;
#   3. calibration: the witnesses' five worked examples;
#      the two spellings of 494; the largest writable
#      19,999;
#   4. the control case: the plate's 37 value rows against
#      the frozen CSV in order; each row's seat counts
#      recomputed from both living banks; the relations
#      counted (35 AGREE · 2 PART at 400 and 10,000); the
#      Armenian value set inside the Georgian value set
#      (the shared domain entire);
#   5. the boundary: both holders of 400 in the bank; the
#      five obsolete letters seated at their CSV standing;
#      the older dresses' silence at the bank (all 76
#      partner forms: value 0, empty breakdown); the
#      Mtavruli fold (Ა == 1; a headline word weighs as
#      itself);
#   6. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.9 against the plate's printed census; the plate's
#      223 DOOR rows — cell set and order equal to the
#      register's, each rendering re-weighed against its
#      filed value; the 62 HOLE rows present in order; the
#      GAP cell CLXXXIV/10 on the plate;
#   7. the zero face: the claim count 0 standing on the
#      plate;
#   8. the §V figures: the five living vowels from the
#      plate's table against the bank; the five tongues'
#      vowel at 8 in their own banks (η · ⲏ · И · Ը · ჱ);
#      οὐδέν == 529; the Nine sum 1779;
#   9. if the MAGVS PDF stands beside the master, its text
#      layer carries all 38 letters and the zero face's
#      statement; its footer resolves; and no Hebrew-block
#      codepoint stands in the layer (the declared dress
#      entire).
# Output is filed to audit_plate_ix_georgian_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. A figure reproduced through the wrong species
# — one holder of 400 silently chosen, a second dress
# seated as a bank, the control case's agreement promoted
# to a bridge — is a failure, not a match.
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
from pontifex.tables import ARMENIAN, GEORGIAN

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-IX-GEORGIAN.md"
PDF = GOAL_FILES / "PLATE-IX-GEORGIAN-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/georgian-table.csv")
CONTROL = (Path.home() / "workspace/pontifex/research/"
           "caucasus-north/georgian-control-case.csv")
RESULTS = HERE / "audit_plate_ix_georgian_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="georgian"):
    return weigh(word, bank)["value"]


with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
BY_POS = {int(r["position"]): r for r in CSV_ROWS}
with CONTROL.open(encoding="utf-8") as fh:
    CC_ROWS = list(csv.DictReader(fh))


def class_of(pos):
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    if pos <= 28:
        return "hundreds", pos - 18, 2
    if pos <= 37:
        return "thousands", pos - 28, 3
    return "ten-thousands", 1, 4


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

# --- 2. the bank entire --------------------------------------------------
rows = re.findall(r"^\| (\d+) \| (\S) · (\S) · (\S) \| ([^|]+?) \| "
                  r"(\d+) \| (units|tens|hundreds|thousands|"
                  r"ten-thousands) \|", sec2, re.M)
check("bank table: 38 rows parsed", len(rows) == 38, str(len(rows)))
seat_parts = []
for (pos, letter, aso, nus, name, val, cls) in rows:
    pos, val = int(pos), int(val)
    want_cls, seat_idx, power = class_of(pos)
    digit = val // 10 ** power
    csv_row = BY_POS[pos]
    check(f"seat {pos} {letter}: letter, partners, name, value, "
          f"class == engine + frozen CSV",
          letter == csv_row["letter"]
          and aso == csv_row["asomtavruli"]
          and nus == csv_row["nuskhuri"]
          and name == csv_row["name"]
          and val == GEORGIAN[letter] == int(csv_row["value"])
          and val == digit * 10 ** power
          and cls == want_cls == csv_row["class"])
    if seat_idx != digit:
        seat_parts.append(pos)
check("the seat law parts at exactly positions 23–28",
      seat_parts == [23, 24, 25, 26, 27, 28], str(seat_parts))
check("bank sum 60395 printed", "**60395**" in sec2)
check("bank sum == engine", sum(GEORGIAN.values()) == 60395)
check("38 letters, 37 distinct values",
      len(GEORGIAN) == 38 and len(set(GEORGIAN.values())) == 37)
check("bank maximum 10000 (ჵ)", max(GEORGIAN.values()) == 10000
      and GEORGIAN["ჵ"] == 10000)
_cs = {}
for r in CSV_ROWS:
    _cs[r["class"]] = _cs.get(r["class"], 0) + int(r["value"])
check("class sums 45/450/4900/45000/10000",
      _cs == {"units": 45, "tens": 450, "hundreds": 4900,
              "thousands": 45000, "ten-thousands": 10000},
      str(_cs))

# --- 3. calibration ---------------------------------------------------------
for w, want in (("ჩღჲთ", 1769), ("ჩყპზ", 1887), ("ციბ", 2012),
                ("ჩყმვ", 1846), ("ცკვ", 2026)):
    check(f"worked example {w} == {want}", value(w) == want)
    check(f"plate prints {w} at {want}", f"| {w} | {want} |" in sec2)
check("494 in two spellings: ჳჟდ == უჟდ == 494",
      value("ჳჟდ") == value("უჟდ") == 494)
check("the largest writable: ჵჰშჟთ == 19999",
      value("ჵჰშჟთ") == 19999 and "| ჵჰშჟთ | 19999 |" in sec2)

# --- 4. the control case ------------------------------------------------------
cc = re.findall(r"^\| (\d+) \| (\S*) \| (\d+) \| (\S*) \| (\d+) \| "
                r"(AGREE|PART) \|", sec2, re.M)
check("control-case table: 37 rows parsed", len(cc) == 37,
      str(len(cc)))
check("plate rows == frozen CSV rows, in order",
      [[c[0], c[1], c[2], c[3], c[4], c[5]] for c in cc]
      == [[r["value"], r["georgian_letters"],
           r["georgian_seats"], r["armenian_letters"],
           r["armenian_seats"], r["relation"]] for r in CC_ROWS])
for r in CC_ROWS:
    v = int(r["value"])
    g_hold = [ch for ch, x in GEORGIAN.items() if x == v]
    a_hold = [ch for ch, x in ARMENIAN.items() if x == v]
    check(f"control {v}: seat counts recomputed from both banks",
          "".join(g_hold) == r["georgian_letters"]
          and len(g_hold) == int(r["georgian_seats"])
          and "".join(a_hold) == r["armenian_letters"]
          and len(a_hold) == int(r["armenian_seats"]))
rels = [r["relation"] for r in CC_ROWS]
check("relations: 35 AGREE · 2 PART, at 400 and 10000",
      rels.count("AGREE") == 35 and rels.count("PART") == 2
      and [int(r["value"]) for r in CC_ROWS
           if r["relation"] == "PART"] == [400, 10000])
check("the shared domain entire: every Armenian value is a "
      "Georgian value", set(ARMENIAN.values())
      <= set(GEORGIAN.values()))

# --- 5. the boundary ---------------------------------------------------------
check("the doubled seat: ჳ == უ == 400, both in the bank",
      GEORGIAN["ჳ"] == GEORGIAN["უ"] == 400)
obsolete = [r["letter"] for r in CSV_ROWS
            if r["standing"] == "obsolete"]
check("the five obsolete letters seated in the bank",
      sorted(obsolete) == sorted("ჱჲჳჴჵ")
      and all(ch in GEORGIAN for ch in obsolete), str(obsolete))
for r in CSV_ROWS:
    for form in (r["asomtavruli"], r["nuskhuri"]):
        w = weigh(form, "georgian")
        check(f"{form} ({r['letter']} partner): silence at the "
              f"bank", w["value"] == 0 and w["breakdown"] == []
              and form not in GEORGIAN)
check("the Mtavruli fold: Ა == 1; ᲐᲑᲒ weighs as აბგ == 6",
      value("Ა") == 1 and value("ᲐᲑᲒ") == value("აბგ") == 6)

# --- 6. the frame -------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.9 — The Georgian Table")[1] \
    .split("### §V.10")[0]
cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
               r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
               r"(\d+) · GAP (\d+)", block)
counts = tuple(int(x) for x in cl.groups())
check("register census == (0, 223, 62, 0, 85, 1)",
      counts == (0, 223, 62, 0, 85, 1), str(counts))
for label, n in (("NATIVE", 0), ("DOOR", 223), ("HOLE", 62),
                 ("FENCED", 0)):
    check(f"plate prints census {label} {n}",
          f"{label} **{n}**" in sec3)
reg = {"DOOR": [], "HOLE": []}
for line in block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in reg:
            reg[cells[2]].append(cells)
door_block = sec3.split("**The door register")[1] \
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
plate_holes = plate_rows(hole_block)
check("plate door register: 223 rows", len(plate_doors) == 223,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg["DOOR"]])
for cells in reg["DOOR"]:
    check(f"door {cells[0]} {cells[3]}: re-weighed",
          value(cells[3]) == int(cells[4]))
check("plate hole register: 62 rows", len(plate_holes) == 62,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_holes]
      == [[c[0], c[1], c[3], c[5]] for c in reg["HOLE"]])
check("every hole rendering is the register's dash",
      all(c[3] == "—" for c in reg["HOLE"]))
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 7. the zero face -----------------------------------------------------------
check("plate prints the claim count: 0",
      "**Claims on this plate: 0**" in sec4)
check("the zero face stands in §IV", "THE ZERO FACE" in sec4)

# --- 8. the §V figures ------------------------------------------------------------
vow = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+) \|$", sec5, re.M)
vow = [r for r in vow if r[0] in "აეიოუ" and len(r[0]) == 1]
check("§V vowel table: 5 rows parsed", len(vow) == 5, str(len(vow)))
for ch, name, v in vow:
    check(f"§V vowel {ch}: price == bank",
          int(v) == GEORGIAN[ch])
check("the living five at the Greek prices 1/5/10/70/400",
      [value(c) for c in "აეიოუ"] == [1, 5, 10, 70, 400])
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))

# --- 9. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    missing = [c for c in GEORGIAN if c not in layer]
    check("PDF layer carries all 38 letters", not missing,
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
lines = ["PLATE-IX-GEORGIAN — independent audit",
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
