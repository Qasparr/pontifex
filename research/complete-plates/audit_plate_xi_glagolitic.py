#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_xi_glagolitic.py
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
# MECHANISM: the independent audit of PLATE-XI-GLAGOLITIC. It
# does not read the plate's own figures for its expectations:
# every priced cell is re-weighed on the house engine from
# its source — the bank from pontifex.tables, the frozen
# transcriptions from research/caucasus-north/
# glagolitic-table.csv and slavonic-parting.csv, the frame
# from THE-TWELVE-TABLES §V.11 — and only then compared
# against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the valued table entire: the plate's §II.1 rows
#      (34) parsed — block seat, letter, name, value,
#      class — against GLAGOLITIC and the frozen CSV; the
#      class law recomputed per seat; the order law's
#      digit partings recomputed from the block (exactly
#      the ten letters); the bank sum 29,005 and the
#      class sums printed;
#   3. the holes: the plate's §II.2 rows (3) against the
#      frozen CSV's HOLE rows; each hole's silence
#      re-verified in the engine;
#   4. the census: 34 keys, 33 distinct values, bank sum
#      29,005, firm domain (1–900) sum 5,005, maximum
#      9,000;
#   5. calibration: the witnesses' three worked examples;
#   6. the parting table: the plate's 33 rows against the
#      frozen parting table entire — sound, both letters,
#      both values (the dash for a bank's silence),
#      relation, reasoning; the 15 AGREE / 18 PART count
#      recomputed; the sharpest coordinates re-weighed in
#      both banks (/ch/ 90 vs 1000; the omega seat 800
#      vs 700);
#   7. the boundary: the plate's refused rows (3
#      composites, 2 variants) against the frozen CSV's
#      REFUSED rows; Ⱗ's silence; the case fold
#      (ⰰⰱ == 3);
#   8. the frame: the census parsed from THE-TWELVE-
#      TABLES §V.11 against the plate's printed census;
#      the plate's 223 DOOR rows — cell set and order
#      equal to the register's, each rendering re-weighed
#      against its filed value; the 62 HOLE rows in
#      order, every rendering the register's dash; the
#      GAP cell CLXXXIV/10 on the plate;
#   9. the zero face: the claim count 0 standing on the
#      plate;
#  10. the §V figures: the plate's vowel table (8 rows)
#      against the bank, the questioned flag on the
#      thousands vowel only; no vowel at 8 in the bank;
#      the 8-seat's holder Ⰷ == 8; the five tongues'
#      vowel at 8 in their own banks (η · ⲏ · И · Ը ·
#      ჱ); the battery's five quoted prices through the
#      case fold (ⰰ 1 · ⰵ 6 · ⰻ 20 · ⰹ 10 · ⰿ 60);
#      οὐδέν == 529; the Nine sum 1779;
#  11. if the MAGVS PDF stands beside the master, its
#      text layer carries all 34 letters and the zero
#      face's statement; its footer resolves; and no
#      Hebrew-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_xi_glagolitic_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. A figure reproduced through the wrong species
# — the order-pricing dressed as inheritance, a hole
# filled, a questioned seat silently relied on, a variant
# seated — is a failure, not a match.
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
from pontifex.tables import GLAGOLITIC

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-XI-GLAGOLITIC.md"
PDF = GOAL_FILES / "PLATE-XI-GLAGOLITIC-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/glagolitic-table.csv")
PARTING = (Path.home() / "workspace/pontifex/research/"
           "caucasus-north/slavonic-parting.csv")
RESULTS = HERE / "audit_plate_xi_glagolitic_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="glagolitic"):
    return weigh(word, bank)["value"]


with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
SOURCED = [r for r in CSV_ROWS if r["status"] == "SOURCED"]
HOLES = [r for r in CSV_ROWS if r["status"] == "HOLE"]
REF_COMP = [r for r in CSV_ROWS
            if r["status"] == "REFUSED-COMPOSITE"]
REF_VAR = [r for r in CSV_ROWS if r["status"] == "REFUSED-VARIANT"]
BY_SEAT = {int(r["block_seat"]): r for r in SOURCED}
with PARTING.open(encoding="utf-8") as fh:
    PART_ROWS = list(csv.DictReader(fh))

NAMES = {r["letter"]: r["unicode_name"].replace(
    "GLAGOLITIC CAPITAL LETTER ", "").lower()
    for r in SOURCED + HOLES + REF_VAR}
NAMES["Ⰺ"] = "initial izhe"
NAMES["Ⱒ"] = "spidery ha"


def class_of(v):
    if v < 10:
        return "units"
    if v < 100:
        return "tens"
    if v < 1000:
        return "hundreds"
    return "thousands"


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

# --- 2. the valued table entire ---------------------------------------
rows = re.findall(r"^\| (\d+) \| (\S) \| ([^|]+?) \| (\d+) \| "
                  r"(units|tens|hundreds|thousands) \|",
                  sec2, re.M)
check("valued table: 34 rows parsed", len(rows) == 34,
      str(len(rows)))
for (seat, letter, name, val, cls) in rows:
    seat, val = int(seat), int(val)
    csv_row = BY_SEAT[seat]
    check(f"block seat {seat} {letter}: letter, name, value, "
          f"class == engine + frozen CSV",
          letter == csv_row["letter"]
          and name == NAMES[letter]
          and val == GLAGOLITIC[letter] == int(csv_row["value"])
          and cls == class_of(val))
ORDER = "".join(r["letter"] for r in SOURCED)
breaks, idx = [], {}
for ch in ORDER:
    v = GLAGOLITIC[ch]
    p = 0 if v < 10 else 1 if v < 100 else 2 if v < 1000 else 3
    idx[p] = idx.get(p, 0) + 1
    if v // (10 ** p) != idx[p]:
        breaks.append(ch)
check("the digit law parts at exactly the ten letters",
      breaks == ["Ⰺ", "Ⰻ", "Ⰼ", "Ⰽ", "Ⰾ", "Ⰿ", "Ⱀ",
                 "Ⱁ", "Ⱂ", "Ⱔ"], str(breaks))
check("bank sum 29,005 printed", "**29,005**" in sec2)
_cs = {}
for ch in ORDER:
    c = class_of(GLAGOLITIC[ch])
    _cs[c] = _cs.get(c, 0) + GLAGOLITIC[ch]
check("class sums 45/460/4500/24000",
      _cs == {"units": 45, "tens": 460, "hundreds": 4500,
              "thousands": 24000}, str(_cs))

# --- 3. the holes --------------------------------------------------------
hrows = re.findall(r"^\| (\d+) \| (\S) \| ([^|]+?) \| "
                   r"HOLE — silence \|", sec2, re.M)
check("hole table: 3 rows parsed", len(hrows) == 3,
      str(len(hrows)))
HOLE_BY_SEAT = {int(r["block_seat"]): r for r in HOLES}
for (seat, letter, name) in hrows:
    seat = int(seat)
    csv_row = HOLE_BY_SEAT[seat]
    _w = weigh(letter, "glagolitic")
    check(f"hole block seat {seat} {letter}: letter, name == "
          f"frozen CSV; silence in the engine",
          letter == csv_row["letter"]
          and name == NAMES[letter]
          and letter not in GLAGOLITIC
          and _w["value"] == 0 and _w["breakdown"] == [])

# --- 4. the census ---------------------------------------------------------
check("34 keys, 33 distinct values, sum 29005, maximum 9000",
      len(GLAGOLITIC) == 34
      and len(set(GLAGOLITIC.values())) == 33
      and sum(GLAGOLITIC.values()) == 29005
      and max(GLAGOLITIC.values()) == 9000)
check("firm domain (1–900) sums 5005",
      sum(v for v in GLAGOLITIC.values() if v <= 900) == 5005)
check("firm sum 5,005 printed", "**5,005**" in sec2)

# --- 5. calibration ---------------------------------------------------------
for w, want in (("ⰗⰑⰂ", 583), ("ⰅⰊ", 16), ("ⰝⰔⰑ", 1280)):
    check(f"worked example {w} == {want}", value(w) == want)
    check(f"plate prints {w} at {want}", f"| {w} | {want} |" in sec2)

# --- 6. the parting table ----------------------------------------------------
prows = re.findall(r"^\| ([^|]+?) \| (\S+) \| (\d+|—) \| (\S+) \| "
                   r"(\d+|—) \| ([^|]+?) \| ([^|]+?) \|$",
                   sec2, re.M)
check("parting table: 33 rows parsed", len(prows) == 33,
      str(len(prows)))
for prow, crow in zip(prows, PART_ROWS):
    sound, cl, cv, gl, gv, rel, why = prow
    check(f"parting {crow['sound']}: row == frozen table",
          sound == crow["sound"]
          and cl == (crow["cyrillic_letter"] or "—")
          and cv == (crow["cyrillic_value"] or "—")
          and gl == (crow["glagolitic_letter"] or "—")
          and gv == (crow["glagolitic_value"] or "—")
          and rel == crow["relation"]
          and why == crow["reasoning"])
check("the count recomputed: 15 AGREE, 18 PART",
      sum(1 for r in PART_ROWS if r["relation"] == "AGREE") == 15
      and sum(1 for r in PART_ROWS
              if r["relation"] != "AGREE") == 18)
check("the sharpest coordinate: /ch/ — Ч == 90 (cyrillic), "
      "Ⱍ == 1000 (glagolitic)",
      value("Ч", "cyrillic") == 90 and value("Ⱍ") == 1000)
check("the hundreds parting: Ѡ == 800 (cyrillic), "
      "Ⱉ == 700 (glagolitic)",
      value("Ѡ", "cyrillic") == 800 and value("Ⱉ") == 700)

# --- 7. the boundary ---------------------------------------------------------
rrows = re.findall(r"^\| (\S+) \| (\d+) \| refused — "
                   r"(composite spelling|variant reading) \|",
                   sec2, re.M)
check("refused table: 5 rows parsed", len(rrows) == 5,
      str(len(rrows)))
check("refused composites as filed: 6000, 7000, 8000",
      [(r[0], int(r[1])) for r in rrows[:3]]
      == [(r["letter"], int(r["value"])) for r in REF_COMP])
check("refused variants as filed: Ⱐ at 3000, Ⱗ at 6000",
      [(r[0], int(r[1])) for r in rrows[3:]]
      == [(r["letter"], int(r["value"])) for r in REF_VAR])
_w = weigh("Ⱗ", "glagolitic")
check("Ⱗ's silence: == 0, empty breakdown",
      _w["value"] == 0 and _w["breakdown"] == [])
check("the case fold: ⰰⰱ == 3", value("ⰰⰱ") == 3)

# --- 8. the frame -------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.11 — The Glagolitic Table")[1] \
    .split("### §V.12")[0]
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

# --- 9. the zero face -----------------------------------------------------------
check("plate prints the claim count: 0",
      "**Claims on this plate: 0**" in sec4)
check("the zero face stands in §IV", "THE ZERO FACE" in sec4)

# --- 10. the §V figures ------------------------------------------------------------
vow = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+)( — questioned "
                 r"range \(§II\.6\))? \|$", sec5, re.M)
check("§V vowel table: 8 rows parsed", len(vow) == 8,
      str(len(vow)))
for ch, name, v, flag in vow:
    check(f"§V vowel {ch}: name, price == bank; flag only "
          f"on the thousands vowel",
          name == NAMES[ch] and int(v) == GLAGOLITIC[ch]
          and bool(flag) == (GLAGOLITIC[ch] >= 1000))
check("no vowel of this bank stands at 8",
      all(GLAGOLITIC[c] != 8 for c in "ⰀⰅⰉⰊⰋⰑⰖⰡ"))
check("the 8-seat's holder: Ⰷ == 8 (dzelo, a consonant)",
      value("Ⰷ") == 8)
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
for small, want in (("ⰰ", 1), ("ⰵ", 6), ("ⰻ", 20),
                    ("ⰹ", 10), ("ⰿ", 60)):
    check(f"the battery's quoted price: {small} == {want} "
          f"through the fold", value(small) == want)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))

# --- 11. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    missing = [c for c in GLAGOLITIC if c not in layer]
    check("PDF layer carries all 34 letters", not missing,
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
lines = ["PLATE-XI-GLAGOLITIC — independent audit",
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
