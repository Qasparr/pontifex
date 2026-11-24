#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_i_greek.py
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
# MECHANISM: the independent audit of PLATE-I-GREEK. It does not
# read the plate's own figures for its expectations: every priced
# cell is re-weighed on the house engine from its source — the
# bank from pontifex.tables, the claims from the mapping
# register, the NATIVE cells from THE-TWELVE-TABLES — and only
# then compared against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the 29 bank keys, letter by letter, against the plate's
#      §II rows (glyph and value parsed from the master);
#   3. οὐδέν, the four diphthongs, their sum, the nine's total;
#   4. every §IV claim: key present on the plate; for each claim
#      carrying a weighed word, the engine's recomputation equal
#      to the register's recomputed — and, for VERIFIED claims,
#      to the claimed value;
#   5. the §III NATIVE renderings re-weighed against the Tables;
#   6. verdict counts on the plate equal to the register's;
#   7. if the MAGVS PDF stands beside the master, its text layer
#      carries all 38 claim keys and the plate's page furniture
#      resolves (the footer count is read from the last page).
# Output is filed to audit_plate_i_greek_results.txt beside this
# script. VERDICT PASS requires every check green.
#
# DOCTRINE: an audit that trusts the document it audits proves
# nothing; this one trusts only the engine and the registers.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh
from pontifex.tables import GREEK

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-I-GREEK.md"
PDF = GOAL_FILES / "PLATE-I-GREEK-MAGVS.pdf"
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUT = HERE / "audit_plate_i_greek_results.txt"

lines_out = []
failures = []
cells = 0  # priced cells re-weighed


def log(text):
    lines_out.append(text)
    print(text)


def check(ok, label, detail=""):
    global cells
    if not ok:
        failures.append(f"{label} {detail}")
    log(f"  [{'OK' if ok else 'FAIL'}] {label} {detail}")


def value(word, bank="greek"):
    return weigh(word, bank)["value"]


text = MASTER.read_text(encoding="utf-8")

# --- 1. Controls ---------------------------------------------------
log("1. CONTROLS")
for word, bank, want in [("θελημα", "greek", 93),
                         ("VAPOUR", "latin_ordinal", 93),
                         ("σφιγξ", "greek", 773)]:
    check(value(word, bank) == want, f"control {word} = {want}")

# --- 2. The bank, letter by letter --------------------------------
log("2. THE BANK — 29 keys re-weighed, plate rows parsed")
plate_rows = {}
for line in text.splitlines():
    m = re.match(r"\| [^|]+ \| (\S+) \| [^|]+ \| (\d+) \|", line)
    if m and m.group(1) in GREEK:
        plate_rows[m.group(1)] = int(m.group(2))
for glyph, want in GREEK.items():
    got = value(glyph)
    cells += 1
    check(got == want == plate_rows.get(glyph),
          f"bank {glyph} = {want}",
          f"(engine {got}, plate {plate_rows.get(glyph)})")
check(len(plate_rows) == 29, "plate prints all 29 bank rows",
      f"({len(plate_rows)})")

# --- 3. The zero, the diphthongs, the nine -------------------------
log("3. THE ZERO, THE DIPHTHONGS, THE NINE")
cells += 1
check(value("ουδεν") == 529 and "529" in text, "οὐδέν = 529")
dip = {d: value(d) for d in ("αι", "ει", "οι", "ου")}
cells += 4
check(dip == {"αι": 11, "ει": 15, "οι": 80, "ου": 470},
      f"diphthongs {dip}")
check(sum(dip.values()) == 576, "diphthong four sum 576 = 24²")
nine = sum(value(v) for v in ("α", "ε", "η", "ι", "ο", "υ", "ω")) \
    + dip["ει"] + dip["ου"]
cells += 9
check(nine == 1779, "the nine weigh 1779")

# --- 4. The claims register ---------------------------------------
log("4. THE CLAIMS — 38, keys on the plate, words re-weighed")
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Greek"]
check(len(claims) == 38, "register carries 38 Greek claims")
missing = [c["claim_key"] for c in claims
           if c["claim_key"] not in text]
check(not missing, "all 38 claim keys stand on the plate",
      f"(missing: {missing})")
for c in claims:
    if c["weighed_word"]:
        got = value(c["weighed_word"])
        cells += 1
        ok = got == c["recomputed"] and (
            c["verdict"] != "VERIFIED" or got == c["claimed"])
        check(ok, f"{c['claim_key']} {c['weighed_word']} = {got}",
              f"(register recomputed {c['recomputed']}, "
              f"claimed {c['claimed']}, {c['verdict']})")
reg_verdicts = {}
for c in claims:
    reg_verdicts[c["verdict"]] = reg_verdicts.get(c["verdict"], 0) + 1
check(reg_verdicts == {"VERIFIED": 21, "NOT VERIFIABLE": 17},
      f"register verdicts {reg_verdicts}")
check("21 VERIFIED · 0 PARTED · 17 NOT VERIFIABLE" in text,
      "plate prints the verdict counts entire")

# --- 5. The NATIVE cells -------------------------------------------
log("5. THE NATIVES — 11 renderings re-weighed")
block = TWELVE.read_text(encoding="utf-8") \
    .split("### §V.1 — The Greek Table")[1].split("### §V.2")[0]
n = 0
for line in block.splitlines():
    if "| NATIVE |" in line:
        cells_md = [c.strip()
                    for c in line.strip().strip("|").split("|")]
        got = value(cells_md[3])
        cells += 1
        n += 1
        check(got == int(cells_md[4]) and cells_md[3] in text,
              f"native {cells_md[0]} {cells_md[3]} = {got}")
check(n == 11, "eleven NATIVE cells audited", f"({n})")

# --- 6. The seating's marks, spot-recomputed -----------------------
log("6. THE SEATING'S GREEK COORDINATES")
check(value("ου") == 470, "ΟΥ = 470 (Triad III mark)")
check(value("ει") == 15, "ΕΙ = 15 (Triad II mark)")


def root(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


frame_b = [sum(value(v) for v in triad) for triad in
           (("α", "ε", "η"), ("ι", "ει", "ο"), ("υ", "ου", "ω"))]
cells += 9
check(frame_b == [14, 95, 1670] and
      all(root(s) == 5 for s in frame_b),
      f"Frame B triad sums {frame_b}, each reducing to root 5")

# --- 7. The PDF's text layer (when built) ---------------------------
if PDF.exists():
    log("7. THE MAGVS PDF — text layer and furniture")
    txt = subprocess.run(["pdftotext", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    absent = [c["claim_key"] for c in claims
              if c["claim_key"] not in txt]
    check(not absent, "all 38 claim keys in the PDF text layer",
          f"(absent: {absent})")
    m = re.findall(r"— (\d+) of (\d+) —", txt)
    check(bool(m) and m[-1][0] == m[-1][1],
          "footer count resolves", f"(last: {m[-1] if m else None})")
else:
    log("7. THE MAGVS PDF — not yet built; text-layer check "
        "deferred to the post-build run")

log("")
log(f"PRICED CELLS RE-WEIGHED: {cells}")
verdict = "PASS" if not failures else "FAIL"
log(f"AUDIT VERDICT: {verdict}"
    + ("" if not failures else f" — {failures}"))
OUT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
sys.exit(0 if not failures else 1)
