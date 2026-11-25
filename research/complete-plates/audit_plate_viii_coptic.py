#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_viii_coptic.py
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
# MECHANISM: the independent audit of PLATE-VIII-COPTIC. It
# does not read the plate's own figures for its expectations:
# every priced cell is re-weighed on the house engine from
# its source — the bank from pontifex.tables, the frozen
# transcription from research/twelve-tongues/
# coptic-table.csv, the door through engine.coptic(), the
# frame from THE-TWELVE-TABLES §V.8 — and only then compared
# against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the bank entire: the plate's §II.1 rows (27) parsed —
#      seat, sign pair, name, value, class, Greek parent —
#      against COPTIC, the frozen CSV and the living GREEK
#      bank; the Milesian law recomputed per seat;
#      uniqueness (27 distinct values); the sum 4,995 and
#      the class sums printed; the parent bank's key-sum
#      5,201 over 29 keys;
#   3. the boundary: the plate's §II.5 fenced table (7)
#      against the CSV's NO VALUE rows; each of the seven
#      silent at weigh() in both cases (value 0, empty
#      breakdown);
#   4. the descent: the two banks' value sets identical;
#      the holder partings in code (6 kind, 90 lineage,
#      900 kind, 200 form); ⲟⲍ == οζ == 77;
#   5. calibration: the witnesses' worked examples (500 ·
#      12 · 365 · 888 · 999); the case folds; the sweep's
#      corpus rows in the sweep's dresses, the UNKNOWNs
#      verified as fence-crossings; the Greek H-dresses
#      (623 · 221) the audit's strictness finding cites;
#   6. the manuscript door: the marks counted and none
#      priced (overlined ⲧⲝⲉ 365 under 3 marks; ⲁ̿ and
#      ⲁ͵ at face 1, devices counted); the raw bank passing
#      the marks in silence; the jinkim neither stripped
#      nor counted;
#   7. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.8 against the plate's printed census; the plate's
#      183 DOOR rows — cell set and order equal to the
#      register's, each rendering re-weighed against its
#      filed value; the 40 FENCED rows in order, each
#      verified to cross a fenced letter against its filed
#      dash; the 62 HOLE rows present in order; the GAP
#      cell CLXXXIV/10 on the plate;
#   8. the one claim: ⲧ re-weighed at 300; the register's
#      row S155-P0-C0 standing on the plate at 300/300
#      VERIFIED; the companion's coordinate present;
#   9. the §V figures: the seven vowels from the plate's
#      table against the bank and the Greek prices; ⲟⲩ ==
#      470 in both banks; the five tongues' vowel at 8 in
#      their own banks (η · ⲏ · И · Ը · ჱ); ⲓ == 10; ⲱ ==
#      800; οὐδέν == 529; the Nine sum 1779;
#  10. if the MAGVS PDF stands beside the master, its text
#      layer carries all 27 signs, the claim's key, and the
#      frozen exhibit's sentence; its footer resolves; and
#      no Hebrew-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_viii_coptic_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. A figure reproduced through the wrong species
# — the mirror bank cited as an independent witness, a
# mark priced at the door, a fenced letter priced in a
# rendering — is a failure, not a match.
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
from pontifex.engine import _COPTIC_ORDER, coptic as coptic_door
from pontifex.tables import COPTIC, GREEK

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-VIII-COPTIC.md"
PDF = GOAL_FILES / "PLATE-VIII-COPTIC-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "twelve-tongues/coptic-table.csv")
RESULTS = HERE / "audit_plate_viii_coptic_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="coptic"):
    return weigh(word, bank)["value"]


with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
BY_SMALL = {r["lowercase"]: r for r in CSV_ROWS}
SEATS = list(_COPTIC_ORDER)
MILESIAN = ([d for d in range(1, 10)] + [d * 10 for d in range(1, 10)]
            + [d * 100 for d in range(1, 10)])


def class_of(pos):
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    return "hundreds", pos - 18, 2


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
rows = re.findall(r"^\| (\d+) \| (\S) · (\S) \| ([^|]+?) \| (\d+) \| "
                  r"(units|tens|hundreds) \| ([^|]+?) \|", sec2, re.M)
check("bank table: 27 rows parsed", len(rows) == 27, str(len(rows)))
for (pos, small, cap, name, val, cls, parent) in rows:
    pos, val = int(pos), int(val)
    want_cls, d, k = class_of(pos)
    csv_row = BY_SMALL[small]
    check(f"seat {pos} {small}: sign, name, value, class, parent "
          f"== engine + frozen CSV",
          small == SEATS[pos - 1] and cap == csv_row["uppercase"]
          and name == csv_row["letter_name"]
          and val == COPTIC[small] == int(csv_row["value"])
          and val == MILESIAN[pos - 1] and val == d * 10 ** k
          and cls == want_cls
          and parent == csv_row["greek_equivalent"]
          and val in set(GREEK.values()))
check("bank sum 4995 printed", "**4995**" in sec2)
check("bank sum == engine", sum(COPTIC.values()) == 4995)
check("27 signs, 27 distinct values",
      len(COPTIC) == 27 and len(set(COPTIC.values())) == 27)
check("bank maximum 900", max(COPTIC.values()) == 900)
check("parent bank: 29 keys summing 5201 (grid 4995 + ς 200 "
      "+ στ 6)", len(GREEK) == 29 and sum(GREEK.values()) == 5201
      and GREEK["ς"] == 200 and GREEK["στ"] == 6)

# --- 3. the boundary -------------------------------------------------------
frows = re.findall(r"^\| (\S) · (\S) \| ([^|]+?) \| NO VALUE",
                   sec2, re.M)
check("fenced table: 7 rows parsed", len(frows) == 7,
      str(len(frows)))
csv_unvalued = {r["lowercase"]: r for r in CSV_ROWS
                if r["status"] == "NO VALUE"}
check("fenced rows == the CSV's NO VALUE rows",
      {r[0] for r in frows} == set(csv_unvalued)
      and all(r[1] == csv_unvalued[r[0]]["uppercase"]
              and r[2] == csv_unvalued[r[0]]["letter_name"]
              for r in frows))
for r in CSV_ROWS:
    if r["status"] != "NO VALUE":
        continue
    for form in (r["lowercase"], r["uppercase"]):
        w = weigh(form, "coptic")
        check(f"{form} ({r['letter_name']}): silence at the bank",
              w["value"] == 0 and w["breakdown"] == []
              and form not in COPTIC)

# --- 4. the descent ---------------------------------------------------------
check("value sets identical (the descent, 27 of 27)",
      set(COPTIC.values()) == set(GREEK.values()))
check("at 6, kind: ϛ == ⲋ == 6", GREEK["ϛ"] == COPTIC["ⲋ"] == 6)
check("at 90, lineage: ϟ (parent) == ϥ (heir) == 90",
      GREEK["ϟ"] == COPTIC["ϥ"] == 90)
check("at 900, kind: ϡ == ⳁ == 900",
      GREEK["ϡ"] == COPTIC["ⳁ"] == 900)
check("at 200, form: σ == ς == ⲥ == 200",
      GREEK["σ"] == GREEK["ς"] == COPTIC["ⲥ"] == 200)
check("ⲟⲍ == οζ == 77 (one fact in two scripts)",
      value("ⲟⲍ") == value("οζ", "greek") == 77)

# --- 5. calibration -----------------------------------------------------------
for w, want in (("ⲫ", 500), ("ⲓⲃ", 12), ("ⲧⲝⲉ", 365),
                ("ⲱⲡⲏ", 888), ("ⳁϥⲑ", 999)):
    check(f"worked example {w} == {want}", value(w) == want)
    check(f"plate prints {w} at {want}", f"| {w} | {want} |" in sec2)
check("case folds: ⲀⲂⲄ == ⲁⲃⲅ == 6; Ϥⲁ == 91; Ⳁ == 900",
      value("ⲀⲂⲄ") == value("ⲁⲃⲅ") == 6 and value("Ϥⲁ") == 91
      and value("Ⳁ") == 900)
CORPUS = [("ⲁⲝⲟⲛⲉⲙⲉ", 231), ("ⲟⲍ", 77), ("ⲧⲣⲃⲃⲑ", 413),
          ("ⲑⲉⲗⲉⲙⲁ", 90), ("ⲁⲅⲁⲡⲉ", 90), ("ⲑⲉⲗⲏⲙⲁ", 93),
          ("ⲁⲅⲁⲡⲏ", 93), ("ⲃⲁⲃⲁⲗⲟⲛ", 156), ("ⲕⲓⲣⲁ", 131),
          ("ⲗⲓⲃⲉⲣⲧⲓ", 457), ("ⲕⲉⲗⲗ", 85), ("ⲁⲭⲟⲛⲉⲙⲉ", 771),
          ("ϩⲉⲣⲟⲩⲣⲁϩⲁ", 677), ("ⲁⲃⲣⲁϩⲁⲇⲁⲃⲣⲁ", 213)]
for dress, want in CORPUS:
    check(f"sweep corpus {dress} == {want}", value(dress) == want)
    check(f"plate prints the corpus dress {dress} at {want}",
          f"| {dress} | {want} |" in sec2)
for dress in ("ϩⲉⲣⲟⲩⲣⲁϩⲁ", "ⲁⲃⲣⲁϩⲁⲇⲁⲃⲣⲁ"):
    r = weigh(dress, "coptic")
    check(f"UNKNOWN {dress}: a fence-crossing, not merely a sum",
          any(ch not in COPTIC for ch in dress)
          and all(ch in COPTIC for ch, _v in r["breakdown"]))
check("the parent's H-dresses: ηερυραηα == 623, αβραηαδαβρα "
      "== 221 (the strictness finding's other side)",
      value("ηερυραηα", "greek") == 623
      and value("αβραηαδαβρα", "greek") == 221)

# --- 6. the manuscript door ---------------------------------------------------
d = coptic_door("ⲧ\u0305ⲝ\u0305ⲉ\u0305")
t1 = coptic_door("ⲁ\u033f")
t2 = coptic_door("ⲁ\u0375")
check("coptic() counts the marks and prices NONE: overlined "
      "ⲧⲝⲉ == 365 at face, 3 marks",
      d["value"] == 365 and d["overline_marks"] == 3)
check("ⲁ̿ == 1 at face, 1 double overline counted",
      t1["value"] == 1 and t1["double_overline_marks"] == 1)
check("ⲁ͵ == 1 at face, 1 numeral sign counted",
      t2["value"] == 1 and t2["numeral_sign_marks"] == 1)
check("the raw bank passes the marks in silence",
      value("ⲁ\u033f") == 1 and value("ⲁ\u0375") == 1)
jk = coptic_door("ⲁ\u0300")
check("the jinkim: neither stripped nor counted",
      jk["value"] == 1 and jk["overline_marks"] == 0
      and value("ⲁ\u0300") == 1)
check("the frozen exhibit's sentence stands on the plate",
      "prices NONE" in sec2 and "counts the marks" in sec2)


# --- 7. the frame ---------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.8 — The Coptic Table")[1] \
    .split("### §V.9")[0]
cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
               r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
               r"(\d+) · GAP (\d+)", block)
counts = tuple(int(x) for x in cl.groups())
check("register census == (0, 183, 62, 40, 85, 1)",
      counts == (0, 183, 62, 40, 85, 1), str(counts))
for label, n in (("NATIVE", 0), ("DOOR", 183), ("HOLE", 62),
                 ("FENCED", 40)):
    check(f"plate prints census {label} {n}",
          f"{label} **{n}**" in sec3)
reg = {"DOOR": [], "FENCED": [], "HOLE": [], "GAP": []}
for line in block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in reg:
            reg[cells[2]].append(cells)
door_block = sec3.split("**The door register")[1] \
    .split("**The fenced register")[0]
fenc_block = sec3.split("**The fenced register")[1] \
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
plate_fenced = plate_rows(fenc_block)
plate_holes = plate_rows(hole_block)
check("plate door register: 183 rows", len(plate_doors) == 183,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg["DOOR"]])
for cells in reg["DOOR"]:
    check(f"door {cells[0]} {cells[3]}: re-weighed",
          value(cells[3]) == int(cells[4]))
check("plate fenced register: 40 rows", len(plate_fenced) == 40,
      str(len(plate_fenced)))
check("plate fenced rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_fenced]
      == [[c[0], c[1], c[3], c[5]] for c in reg["FENCED"]])
FENCED_ALL = set()
for r in CSV_ROWS:
    if r["status"] == "NO VALUE":
        FENCED_ALL.add(r["lowercase"])
        FENCED_ALL.add(r["uppercase"])
for cells in reg["FENCED"]:
    check(f"fenced {cells[0]} {cells[3]}: crosses a fenced "
          f"letter; the register's value is the dash",
          cells[4] == "—"
          and any(ch in FENCED_ALL for ch in cells[3]))
check("plate hole register: 62 rows", len(plate_holes) == 62,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_holes]
      == [[c[0], c[1], c[3], c[5]] for c in reg["HOLE"]])
check("every hole rendering is the register's dash",
      all(c[3] == "—" for c in reg["HOLE"]))
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 8. the one claim -------------------------------------------------------------
check("ⲧ re-weighed at 300", value("ⲧ") == 300)
check("the claim stands on the plate: S155-P0-C0 at 300/300 "
      "VERIFIED", "S155-P0-C0" in sec4
      and "| 300 | 300 | VERIFIED |" in sec4)
check("plate prints the claim count: 1",
      "**Claims on this plate: 1**" in sec4)
check("the companion at its coordinate: S155-P0-C1 present",
      "S155-P0-C1" in sec4)
check("the three empty Coptic sections named on the plate",
      all(s in sec4 for s in ("Cheema", "Janja"))
      and "§III.153" in sec4)

# --- 9. the §V figures --------------------------------------------------------------
vow = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+) \| (\d+) \|$",
                 sec5, re.M)
vow = [r for r in vow if r[0] in "ⲁⲉⲏⲓⲟⲩⲱ" and len(r[0]) == 1]
check("§V vowel table: 7 rows parsed", len(vow) == 7, str(len(vow)))
for ch, name, v, g in vow:
    check(f"§V vowel {ch}: price == bank == Greek price",
          int(v) == COPTIC[ch] == int(g)
          and name == BY_SMALL[ch]["letter_name"])
check("ⲟⲩ == ΟΥ == 470 (the hybrid's identical total)",
      value("ⲟⲩ") == value("ΟΥ", "greek") == 470)
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
check("ⲓ == 10 and ⲱ == 800 (the Ι and Ω witnesses)",
      value("ⲓ") == 10 and value("ⲱ") == 800)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))

# --- 10. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    missing = [c for c in SEATS if c not in layer]
    check("PDF layer carries all 27 signs", not missing,
          f"missing: {missing}")
    check("PDF layer carries the claim's key",
          "S155-P0-C0" in layer)
    check("PDF layer carries the frozen exhibit's sentence",
          "prices NONE" in layer)
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
lines = ["PLATE-VIII-COPTIC — independent audit",
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
