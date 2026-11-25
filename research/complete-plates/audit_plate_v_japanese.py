#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_v_japanese.py
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
# MECHANISM: the independent audit of PLATE-V-JAPANESE. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the bank from pontifex.tables, the door through
# engine.kana(), the bridges in both banks, the frame from
# THE-TWELVE-TABLES §V.5 — and only then compared against what
# the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the bank entire: the plate's §II seat register parsed
#      from the master (73 rows) — each sign's printed price
#      against weigh() in both dresses; the values 1–73 each
#      exactly once; the grid and dakuten tables' cells and
#      row sums; the column totals and the inventory total;
#      the small-kana table (12 rows) at their partners'
#      seats under G4/G5; the bank census (170 keys, 85 + 85);
#   3. the ー door: the exhibits through kana() (かー 7 ·
#      とー 25 · んー 48 · word-initial 0) and the raw door's
#      skip (かー weighs 6 raw); the seam exhibits weighed as
#      written (おう 8 · えい 6); the yōon exhibit きゃ 43;
#   4. the three bridges in both banks (ゆず/YUZU 93 ·
#      かな/KANA 27 · しおん/SHION 65);
#   5. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.5 against the plate's printed census; the plate's
#      211 DOOR rows — cell set equal to the register's,
#      each rendering re-weighed against its filed value;
#      the 74 HOLE rows present with coordinates; the GAP
#      cell CLXXXIV/10 on the plate;
#   6. the §V figures: the five vowel seats in the kana
#      mint and at the Greek stations; VV unpriced in the
#      Nine's sum (1,779 stands on the seven + two hybrids
#      alone);
#   7. if the MAGVS PDF stands beside the master, its text
#      layer carries the three bridges, the zero face's
#      statement, and every one of the 73 base hiragana;
#      its footer resolves (25 of 25); and no Hebrew-block
#      codepoint stands in the layer (the declared dress
#      entire).
# Output is filed to audit_plate_v_japanese_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh, kana as kana_door
from pontifex.tables import KANA, KANA_BASE, KANA_VOWEL

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-V-JAPANESE.md"
PDF = GOAL_FILES / "PLATE-V-JAPANESE-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
RESULTS = HERE / "audit_plate_v_japanese_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="kana"):
    return weigh(word, bank)["value"]


master = MASTER.read_text(encoding="utf-8")
sec2 = master.split("## §II")[1].split("## §III")[0]
sec3 = master.split("## §III")[1].split("## §IV")[0]
sec5 = master.split("## §V")[1].split("## §VI")[0]

# --- 1. controls -----------------------------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)

# --- 2. the bank ------------------------------------------------------
check("bank census: 170 keys", len(KANA) == 170, str(len(KANA)))
hira = sum(1 for c in KANA if 0x3040 <= ord(c) <= 0x309F)
kata = sum(1 for c in KANA if 0x30A0 <= ord(c) <= 0x30FF)
check("bank census: 85 hiragana + 85 katakana", (hira, kata) == (85, 85),
      f"{hira}/{kata}")
check("plate prints the 170-key census", "**170 keys**" in sec2)

reg = re.findall(r"^\| (\d+) \| (\S) \| (\S) \| ([^|]+?) \| (\d+) \|",
                 sec2, re.M)
check("seat register: 73 rows parsed", len(reg) == 73, str(len(reg)))
seen = []
for seat, h, k, _rom, price in reg:
    seat, price = int(seat), int(price)
    seen.append(price)
    check(f"seat {seat}: {h} price {price} == engine",
          value(h) == price == KANA[h] == seat)
    check(f"seat {seat}: katakana dress {k} shares the seat",
          value(k) == price and ord(k) == ord(h) + 0x60)
check("values 1–73 each exactly once",
      sorted(seen) == list(range(1, 74)))

for label, block in (("grid", sec2.split("### The dakuten block")[0]),
                     ("dakuten", sec2.split("### The dakuten block")[1]
                      .split("### The seat register")[0])):
    rows = [ln for ln in block.splitlines()
            if ln.startswith("| the ")]
    for ln in rows:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        total = 0
        for cell in cells[1:6]:
            if cell.startswith("**HOLE**"):
                continue
            m = re.match(r"(\S) — (\d+)$", cell)
            check(f"{label} cell {cell}: price == engine",
                  m and KANA[m.group(1)] == int(m.group(2)))
            total += int(m.group(2))
        check(f"{label} row {cells[0]}: sum == printed",
              total == int(cells[6]), f"{total} vs {cells[6]}")

cols = {c: sum(KANA[s] for s in KANA_BASE if KANA_VOWEL.get(s) == c)
        for c in range(1, 6)}
for name, c in (("a", 1), ("i", 2), ("u", 3), ("e", 4), ("o", 5)):
    m = re.search(rf"{name}-column \*\*(\d+)\*\*", sec2)
    check(f"column total {name}: printed == engine",
          m and int(m.group(1)) == cols[c],
          f"{m.group(1) if m else None} vs {cols[c]}")
check("inventory total 2701 on the plate", "**2701**" in sec2)
check("inventory total: sum of base == 2701",
      sum(KANA[s] for s in KANA_BASE) == 2701)

smalls = re.findall(r"^\| (\S) \| (G[45]) — \S+ \| (\S) \| (\d+) \|",
                    sec2, re.M)
check("small-kana table: 12 rows parsed", len(smalls) == 12,
      str(len(smalls)))
for small, _law, partner, seat in smalls:
    check(f"small {small}: partner {partner}'s seat {seat}",
          KANA[small] == KANA[partner] == int(seat))

# --- 3. the ー door ----------------------------------------------------
check("かー through the door == 7", kana_door("かー")["value"] == 7)
check("とー through the door == 25", kana_door("とー")["value"] == 25)
check("んー through the door == 48", kana_door("んー")["value"] == 48)
check("word-initial ー through the door == 0",
      kana_door("ー")["value"] == 0)
check("raw weigh(かー) skips the mark == 6", value("かー") == 6)
check("ー is not a key of the bank", "ー" not in KANA)
check("seam as written: おう == 8", value("おう") == 8)
check("seam as written: えい == 6", value("えい") == 6)
check("yōon exhibit: きゃ == 43", value("きゃ") == 43)

# --- 4. the bridges ----------------------------------------------------
for kj, rj, want in (("ゆず", "YUZU", 93), ("かな", "KANA", 27),
                     ("しおん", "SHION", 65)):
    check(f"bridge {kj} == {want} in kana", value(kj) == want)
    check(f"bridge {rj} == {want} in latin_ordinal",
          value(rj, "latin_ordinal") == want)
    check(f"bridge {kj} stands on the plate", kj in sec5)

# --- 5. the frame -------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.5 — The Japanese Table")[1] \
    .split("### §V.6")[0]
cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
               r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
               r"(\d+) · GAP (\d+)", block)
counts = tuple(int(x) for x in cl.groups())
check("register census == (0, 211, 74, 0, 85, 1)",
      counts == (0, 211, 74, 0, 85, 1), str(counts))
for label, n in (("NATIVE", 0), ("DOOR", 211), ("HOLE", 74),
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
    elif len(cells) == 3 and re.match(r"[A-Z]+/", cells[0]):
        plate_holes.append(cells)
check("plate door register: 211 rows", len(plate_doors) == 211,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg_doors])
for cells in reg_doors:
    check(f"door {cells[0]} {cells[3] or '(empty)'}: re-weighed",
          value(cells[3]) == int(cells[4]))
empty_reg = [c for c in reg_doors if c[3] == ""]
check("the register's 13 empty-rendering door rows, all filed 0",
      len(empty_reg) == 13
      and all(c[4] == "0" for c in empty_reg), str(len(empty_reg)))
check("plate hole register: 74 rows", len(plate_holes) == 74,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2]] for c in plate_holes]
      == [[c[0], c[1], c[5]] for c in reg_holes])
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 6. the §V figures ---------------------------------------------------
for sign, want in (("あ", 1), ("い", 2), ("う", 3), ("え", 4),
                   ("お", 5)):
    check(f"vowel seat {sign} == {want}", KANA[sign] == want)
for word, want in (("α", 1), ("ε", 5), ("ι", 10), ("ο", 70)):
    check(f"station {word} == {want}", value(word, "greek") == want)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779 without VV", nine == 1779, str(nine))
check("zero face stands in §IV", "THE ZERO FACE" in master
      and "**Claims on this plate: 0**" in master)

# --- 7. the PDF layer -----------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    for kj in ("ゆず", "かな", "しおん"):
        check(f"PDF layer carries bridge {kj}", kj in layer)
    check("PDF layer carries the zero face", "ZERO FACE" in layer)
    missing = [s for s in KANA_BASE if s not in layer]
    check("PDF layer carries all 73 base hiragana", not missing,
          f"missing: {missing}")
    check("PDF layer: no Hebrew-block codepoint",
          not any(0x590 <= ord(c) <= 0x5FF for c in layer))
    info = subprocess.run(["pdfinfo", str(PDF)], capture_output=True,
                          text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    check(f"PDF footer resolves ({pages} of {pages})",
          f"{pages} of {pages}" in layer)
else:
    check("MAGVS PDF exists", False, "not built")

# --- verdict --------------------------------------------------------------
n_cells = sum(1 for name, _ok, _d in CHECKS)
failed = [(n, d) for n, ok, d in CHECKS if not ok]
lines = [f"PLATE-V-JAPANESE — independent audit",
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
