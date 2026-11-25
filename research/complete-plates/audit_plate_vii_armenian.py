#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_vii_armenian.py
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
# MECHANISM: the independent audit of PLATE-VII-ARMENIAN. It
# does not read the plate's own figures for its expectations:
# every priced cell is re-weighed on the house engine from
# its source — the bank from pontifex.tables, the door
# through engine.armenian(), the frame from
# THE-TWELVE-TABLES §V.7 — and only then compared against
# what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the bank entire: the plate's §II.1 rows (36) parsed —
#      position, letters, name, value, class — against
#      ARMENIAN and the letter names of the Phase I audit's
#      frozen CSV; the class law recomputed per position;
#      uniqueness (36 distinct values); the sum 49,995 and
#      the class sums printed;
#   3. calibration: the witnesses' worked examples and
#      MELA's era date recomputed (1975 · 2222 · 2004 ·
#      120 · 50 · 1455 · 9999); the case fold (աբգ = ԱԲԳ);
#   4. the control case: the plate's §II.4 rows (26) —
#      Armenian letter and class, halehame base and class,
#      the shared value — against ARMENIAN and
#      HALEHAME_FIRST; agreement entire; the parting at
#      position 10 (Ժ tens vs ተ units at value 10);
#   5. the boundary and the resolutions: ARMENIAN_LATE's
#      contents; Օ/Ֆ silence at weigh() (value 0, empty
#      breakdown) and at the door's default path; prices
#      at late=True in both cases; the օր proof (5000 shut,
#      15000 open); the overline exhibits (Ա̅ 10000 ·
#      Ջ̅ 9000000 · Ռ̅ՋՀԵ 10000975, one mark); the
#      collision sweep recomputed (9 at ×1000, 0 at
#      ×10000); the ligature's two doors (7005 at weigh(),
#      silence at the door);
#   6. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.7 against the plate's printed census; the plate's
#      223 DOOR rows — cell set and order equal to the
#      register's, each rendering re-weighed against its
#      filed value at the door the register declares (209
#      classical, 14 annex); the 62 HOLE rows present in
#      order, every rendering a dash; the GAP cell
#      CLXXXIV/10 on the plate;
#   7. the §V figures: the five tongues' vowel at 8 in
#      their own banks (η · ⲏ · И · Ը · ჱ); the tongue's
#      six vowels from the plate's table against the bank;
#      the digraph ու == 7600 as a sum; οὐδέν == 529; the
#      Nine sum 1779;
#   8. if the MAGVS PDF stands beside the master, its text
#      layer carries all 36 majuscules, the era siglum's
#      letters, and the zero face's statement; its footer
#      resolves; and no Hebrew-block codepoint stands in
#      the layer (the declared dress entire).
# Output is filed to audit_plate_vii_armenian_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers. A figure reproduced through the wrong door —
# the annex at the classical bank, the parted factor at
# the overline — is a failure, not a match.
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

from pontifex import weigh
from pontifex.engine import armenian as armenian_door
from pontifex.tables import (ARMENIAN, ARMENIAN_LATE, HALEHAME_FIRST,
                             _GEEZ_BASES)

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-VII-ARMENIAN.md"
PDF = GOAL_FILES / "PLATE-VII-ARMENIAN-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
RESULTS = HERE / "audit_plate_vii_armenian_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="armenian"):
    return weigh(word, bank)["value"]


NAMES = ["Ayb", "Ben", "Gim", "Da", "Yech", "Za", "Eh", "Et",
         "To", "Zhe", "Ini", "Liwn", "Khe", "Tsa", "Ken", "Ho",
         "Dza", "Ghat", "Che", "Men", "Yi", "Nu", "Sha", "O",
         "Cha", "Pe", "Je", "Ra", "Se", "Vew", "Tiwn", "Re",
         "Tso", "Hiwn", "Piwr", "Ke"]
LETTERS = list(ARMENIAN.keys())


def class_of(pos):
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    if pos <= 27:
        return "hundreds", pos - 18, 2
    return "thousands", pos - 27, 3


master = MASTER.read_text(encoding="utf-8")
# MECHANISM: the section splits are line-anchored ("\n## §…")
# because this plate's subsection headings (### §II.1 …)
# contain the unanchored string as a substring.
sec2 = master.split("\n## §II")[1].split("\n## §III")[0]
sec3 = master.split("\n## §III")[1].split("\n## §IV")[0]
sec5 = master.split("\n## §V")[1].split("\n## §VI")[0]

# --- 1. controls -------------------------------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)

# --- 2. the bank entire --------------------------------------------------
rows = re.findall(r"^\| (\d+) \| (\S) · (\S) \| ([^|]+?) \| (\d+) \| "
                  r"(units|tens|hundreds|thousands) \|", sec2, re.M)
check("bank table: 36 rows parsed", len(rows) == 36, str(len(rows)))
for (pos, cap, low, name, val, cls) in rows:
    pos, val = int(pos), int(val)
    want_cls, d, k = class_of(pos)
    check(f"seat {pos} {cap}: letter, name, value, class == engine",
          cap == LETTERS[pos - 1] and low == cap.lower()
          and name == NAMES[pos - 1] and val == ARMENIAN[cap]
          and val == d * 10 ** k and cls == want_cls)
check("bank sum 49995 printed", "**49995**" in sec2)
check("bank sum == engine", sum(ARMENIAN.values()) == 49995)
check("36 letters, 36 distinct values",
      len(ARMENIAN) == 36 and len(set(ARMENIAN.values())) == 36)
check("bank maximum 9000", max(ARMENIAN.values()) == 9000)

# --- 3. calibration ---------------------------------------------------------
for w, want in (("ՌՋՀԵ", 1975), ("ՍՄԻԲ", 2222), ("ՍԴ", 2004),
                ("ՃԻ", 120), ("Ծ", 50), ("ՌՆԾԵ", 1455),
                ("ՔՋՂԹ", 9999)):
    check(f"worked example {w} == {want}", value(w) == want)
    check(f"plate prints {w} at {want}",
          f"| {w} | {want} |" in sec2)
check("case fold: աբգ == ԱԲԳ == 6",
      value("աբգ") == value("ԱԲԳ") == 6)

# --- 4. the control case ------------------------------------------------------
ctl = re.findall(r"^\| (\d+) \| (\S) \| (units|tens|hundreds|"
                 r"thousands) \| (\S) \| (units|tens|hundreds) \| "
                 r"(\d+) \|$", sec2, re.M)
check("control table: 26 rows parsed", len(ctl) == 26, str(len(ctl)))
hale_bases = [b for b, _fv in _GEEZ_BASES]


def hale_class(pos):
    return "units" if pos <= 10 else "tens" if pos <= 19 \
        else "hundreds"


for (pos, ach, acls, hb, hcls, v) in ctl:
    pos, v = int(pos), int(v)
    check(f"control {pos}: {ach} vs {hb} at {v}",
          ach == LETTERS[pos - 1] and hb == hale_bases[pos - 1]
          and acls == class_of(pos)[0] and hcls == hale_class(pos)
          and ARMENIAN[ach] == HALEHAME_FIRST[hb] == v)
check("the parting at 10: Ժ is tens, ተ is units, value 10 both",
      class_of(10)[0] == "tens" and hale_class(10) == "units"
      and ARMENIAN["Ժ"] == HALEHAME_FIRST["ተ"] == 10)

# --- 5. the boundary and the resolutions ---------------------------------------
check("ARMENIAN_LATE == the annex of record",
      ARMENIAN_LATE == {"Օ": 10000, "օ": 10000,
                        "Ֆ": 20000, "ֆ": 20000})
for probe in ("Օ", "Ֆ", "օ", "ֆ"):
    r = weigh(probe, "armenian")
    check(f"{probe}: silence at the classical bank",
          r["value"] == 0 and r["breakdown"] == [])
    check(f"{probe}: silence at the door's default path",
          armenian_door(probe)["value"] == 0)
check("annex prices at late=True",
      armenian_door("Օ", late=True)["value"] == 10000
      and armenian_door("օ", late=True)["value"] == 10000
      and armenian_door("Ֆ", late=True)["value"] == 20000
      and armenian_door("ֆ", late=True)["value"] == 20000)
check("օր proof: 5000 shut, 15000 open",
      armenian_door("օր")["value"] == 5000
      and armenian_door("օր", late=True)["value"] == 15000)
check("plate prints the օր proof", "**5000**" in sec2
      and "**15000**" in sec2)
check("overline Ա̅ == 10000", armenian_door("Ա\u0305")["value"] == 10000)
check("overline Ջ̅ == 9000000",
      armenian_door("Ջ\u0305")["value"] == 9000000)
ovr = armenian_door("Ռ\u0305ՋՀԵ")
check("Ռ̅ՋՀԵ == 10000975, one mark counted",
      ovr["value"] == 10000975 and ovr["overline_marks"] == 1)
plain = set(ARMENIAN.values())
check("collision sweep: 9 at ×1000, 0 at ×10000",
      len({v * 1000 for v in plain} & plain) == 9
      and len({v * 10000 for v in plain} & plain) == 0)
check("ligature և: 7005 at weigh(), silence at the door",
      value("և") == 7005 and armenian_door("և")["value"] == 0)

# --- 6. the frame ---------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.7 — The Armenian Table")[1] \
    .split("### §V.8")[0]
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
    if len(cells) == 5 and re.match(r"[A-Z]+/", cells[0]) \
            and cells[3].isdigit():
        plate_doors.append(cells)
    elif len(cells) == 4 and re.match(r"[A-Z]+/", cells[0]):
        plate_holes.append(cells)
check("plate door register: 223 rows", len(plate_doors) == 223,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg_doors])
check("plate door column == the register's declared doors",
      all((p[4] == "late annex (R1)") == ("annex" in r[5])
          for p, r in zip(plate_doors, reg_doors)))
n_annex = 0
for cells in reg_doors:
    if "annex" in cells[5]:
        n_annex += 1
        v = armenian_door(cells[3], late=True)["value"]
    else:
        v = value(cells[3])
    check(f"door {cells[0]} {cells[3]}: re-weighed", v == int(cells[4]))
check("annex-priced door rows == 14", n_annex == 14, str(n_annex))
check("plate hole register: 62 rows", len(plate_holes) == 62,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_holes]
      == [[c[0], c[1], c[3], c[5]] for c in reg_holes])
check("every hole rendering is the register's dash",
      all(c[3] == "—" for c in reg_holes))
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 7. the §V figures ------------------------------------------------------------
for word, bank in (("η", "greek"), ("ⲏ", "coptic"),
                   ("И", "cyrillic"), ("Ը", "armenian"),
                   ("ჱ", "georgian")):
    check(f"the 8 seated: {word} == 8 in {bank}",
          value(word, bank) == 8)
vow = re.findall(r"^\| (\S) \| ([^|]+?) \| (\d+) \|$", sec5, re.M)
vow = [r for r in vow if r[0] in "ԱԵԸԻՈՒ" and len(r[0]) == 1]
check("§V vowel table: 6 rows parsed", len(vow) == 6, str(len(vow)))
for ch, name, v in vow:
    check(f"§V vowel {ch}: price == bank",
          int(v) == ARMENIAN[ch]
          and name == NAMES[LETTERS.index(ch)])
check("digraph ու == 7600 as a sum",
      value("ու") == 7600 == ARMENIAN["Ո"] + ARMENIAN["Ւ"])
check("plate prints the digraph at 7600", "**7600**" in sec5)
check("οὐδέν == 529 in greek", value("οὐδέν", "greek") == 529)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779", nine == 1779, str(nine))
check("zero face stands in §IV", "THE ZERO FACE" in master
      and "**Claims on this plate: 0**" in master)

# --- 8. the PDF layer --------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    missing = [c for c in LETTERS if c not in layer]
    check("PDF layer carries all 36 majuscules", not missing,
          f"missing: {missing}")
    check("PDF layer carries the zero face", "ZERO FACE" in layer)
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
lines = ["PLATE-VII-ARMENIAN — independent audit",
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
