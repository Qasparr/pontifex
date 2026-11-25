#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_iii_arabic.py
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
# MECHANISM: the independent audit of PLATE-III-ARABIC. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the bank from pontifex.tables, the claims from the
# mapping register, the NATIVE cells from THE-TWELVE-TABLES —
# and only then compared against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the 28 bank keys, letter by letter, against the plate's
#      §II rows (glyph, value and declared dress parsed from
#      the master; the dress checked against the audit's own
#      copy of the §II scheme);
#   3. the class sums; the first-twenty-two identity against
#      the Hebrew bank; the matres and their sum; the unseated
#      signs' silence (ة, أ, ء — value 0, empty breakdown); the
#      KEY in both Semitic banks;
#   4. every §IV claim: key present on the plate; for each
#      claim carrying a weighed word, the engine's
#      recomputation in the seated abjad bank equal to the
#      register's recomputed — and, for VERIFIED claims, to
#      the claimed value (this tongue has no door: every
#      recomputation runs in the one bank);
#   5. the §III NATIVE renderings re-weighed against the
#      Tables;
#   6. verdict and subseat counts equal to the register's; the
#      seven parting coordinates, the one NOT VERIFIABLE
#      coordinate and the three VERIFIED coordinates entire on
#      the plate; the bridges' stated absence;
#   7. if the MAGVS PDF stands beside the master, its text
#      layer carries all 35 claim keys, the plate's page
#      furniture resolves, no Arabic-block or Hebrew-block
#      codepoint stands in the layer (the declared substitution
#      entire), and the dress of the signature parting stands
#      in its place.
# Output is filed to audit_plate_iii_arabic_results.txt beside
# this script. VERDICT PASS requires every check green.
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
from pontifex.tables import ARABIC_ABJAD, HEBREW

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-III-ARABIC.md"
PDF = GOAL_FILES / "PLATE-III-ARABIC-MAGVS.pdf"
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUT = HERE / "audit_plate_iii_arabic_results.txt"

lines_out = []
failures = []
cells = 0  # priced cells re-weighed


def log(text):
    lines_out.append(text)
    print(text)


def check(ok, label, detail=""):
    if not ok:
        failures.append(f"{label} {detail}")
    log(f"  [{'OK' if ok else 'FAIL'}] {label} {detail}")


def value(word, bank="arabic_abjad"):
    return weigh(word, bank)["value"]


text = MASTER.read_text(encoding="utf-8")

# --- 1. Controls ---------------------------------------------------
log("1. CONTROLS")
for word, bank, want in [("θελημα", "greek", 93),
                         ("VAPOUR", "latin_ordinal", 93),
                         ("σφιγξ", "greek", 773)]:
    check(value(word, bank) == want, f"control {word} = {want}")

# --- 2. The bank, letter by letter --------------------------------
log("2. THE BANK — 28 keys re-weighed, plate rows parsed")
SCHEME = {"ا": "ʾ", "ب": "b", "ج": "j", "د": "d", "ه": "h",
          "و": "w", "ز": "z", "ح": "ḥ", "ط": "ṭ", "ي": "y",
          "ك": "k", "ل": "l", "م": "m", "ن": "n", "س": "s",
          "ع": "ʿ", "ف": "f", "ص": "ṣ", "ق": "q", "ر": "r",
          "ش": "š", "ت": "t", "ث": "ṯ", "خ": "ḵ", "ذ": "ḏ",
          "ض": "ḍ", "ظ": "ẓ", "غ": "ġ"}
plate_rows = {}
for line in text.splitlines():
    m = re.match(r"\| [^|]+ \| (\S+) \| [^|]+ \| (\d+) \| "
                 r"([^|]+) \|", line)
    if m and m.group(1) in ARABIC_ABJAD:
        plate_rows[m.group(1)] = (int(m.group(2)),
                                  m.group(3).strip())
for glyph, want in ARABIC_ABJAD.items():
    got = value(glyph)
    cells += 1
    prow = plate_rows.get(glyph)
    check(got == want and prow is not None and prow[0] == want
          and prow[1] == SCHEME[glyph],
          f"bank {glyph} = {want}, dress {SCHEME[glyph]}",
          f"(engine {got}, plate {prow})")
check(len(plate_rows) == 28, "plate prints all 28 bank rows",
      f"({len(plate_rows)})")

# --- 3. Sums, the identity, matres, silence, the KEY ---------------
log("3. SUMS, THE IDENTITY, MATRES, SILENCE, THE KEY")
vals = list(ARABIC_ABJAD.values())
check(sum(vals[:9]) == 45 and sum(vals[9:18]) == 450
      and sum(vals[18:]) == 5500 and sum(vals) == 5995
      and "5,995" in text,
      "class sums 45 · 450 · 5,500; bank total 5,995")
FINALS_H = ("ך", "ם", "ן", "ף", "ץ")
hebrew22 = sum(v for g, v in HEBREW.items() if g not in FINALS_H)
cells += 1
check(sum(vals[:22]) == 1495 and hebrew22 == 1495
      and sum(vals[22:]) == 4500 and "1,495" in text,
      "the first 22 sum to 1,495 = the Hebrew bank's 22")
matres = {g: value(g) for g in ("ا", "و", "ي")}
cells += 3
check(matres == {"ا": 1, "و": 6, "ي": 10}
      and sum(matres.values()) == 17,
      f"matres {matres}, sum 17 — three, not four")
for sign in ("ة", "أ", "ء"):
    r = weigh(sign, "arabic_abjad")
    cells += 1
    check(r["value"] == 0 and r["breakdown"] == [],
          f"unseated sign {sign} returns silence "
          f"(0, empty breakdown)")
cells += 2
check(value("مفتاح") == 529
      and value("מפתח", "hebrew") == 528,
      "the KEY: مفتاح = 529 · מפתח = 528 (Δ1)")

# --- 4. The claims register ---------------------------------------
log("4. THE CLAIMS — 35, keys on the plate, words re-weighed")
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Arabic"]
check(len(claims) == 35, "register carries 35 Arabic claims")
missing = [c["claim_key"] for c in claims
           if c["claim_key"] not in text]
check(not missing, "all 35 claim keys stand on the plate",
      f"(missing: {missing})")
for c in claims:
    if c["weighed_word"]:
        got = value(c["weighed_word"])
        cells += 1
        ok = got == c["recomputed"] and (
            c["verdict"] != "VERIFIED" or got == c["claimed"])
        check(ok, f"{c['claim_key']} {c['weighed_word']} = {got} "
              f"(bank)",
              f"(register recomputed {c['recomputed']}, "
              f"claimed {c['claimed']}, {c['verdict']})")
reg_verdicts = {}
subseats = {}
for c in claims:
    reg_verdicts[c["verdict"]] = \
        reg_verdicts.get(c["verdict"], 0) + 1
    subseats[c["bank_engine"]] = \
        subseats.get(c["bank_engine"], 0) + 1
check(reg_verdicts == {"VERIFIED": 27, "PARTED": 7,
                       "NOT VERIFIABLE": 1},
      f"register verdicts {reg_verdicts}")
check(subseats == {"arabic_abjad": 35},
      f"register subseats {subseats} — the one subseat")
check("27 VERIFIED · 7 PARTED · 1 NOT VERIFIABLE" in text,
      "plate prints the verdict counts entire")
parted = [c for c in claims if c["verdict"] == "PARTED"]
check(len(parted) == 7
      and all(c["coordinate"] in text for c in parted),
      "all 7 parting coordinates stand entire on the plate")
ta = [c for c in parted if "ة priced as ه" in c["coordinate"]]
hz = [c for c in parted if "hamza-alif" in c["coordinate"]]
check(len(ta) == 6
      and all(c["claimed"] - c["recomputed"] == 5 for c in ta)
      and len(hz) == 1
      and hz[0]["claimed"] - hz[0]["recomputed"] == 1,
      "the two species: six ة partings at Δ5, one hamza "
      "parting at Δ1")
nv = [c for c in claims if c["verdict"] == "NOT VERIFIABLE"]
check(len(nv) == 1 and nv[0]["coordinate"] in text,
      "the one NOT VERIFIABLE coordinate stands entire")
vc = [c for c in claims
      if c["verdict"] == "VERIFIED" and c["coordinate"]]
check(len(vc) == 3 and all(c["coordinate"] in text for c in vc),
      "all 3 VERIFIED coordinates stand entire")
br = [c for c in claims
      if c["bridge"] not in ("none.", "none", "")]
check(len(br) == 0 and "carries no bridge" in text,
      "no bridge annotations in the register; the plate "
      "prints the absence")

# --- 5. The NATIVE cells -------------------------------------------
log("5. THE NATIVES — 11 renderings re-weighed")
block = TWELVE.read_text(encoding="utf-8") \
    .split("### §V.3 — The Arabic Table")[1].split("### §V.4")[0]
n = 0
for line in block.splitlines():
    if "| NATIVE |" in line:
        cells_md = [c.strip()
                    for c in line.strip().strip("|").split("|")]
        want = int(cells_md[4])
        got = value(cells_md[3])
        cells += 1
        n += 1
        check(got == want and cells_md[3] in text,
              f"native {cells_md[0]} {cells_md[3]} = {got}")
check(n == 11, "eleven NATIVE cells audited", f"({n})")

# --- 6. The PDF's text layer (when built) ---------------------------
if PDF.exists():
    log("6. THE MAGVS PDF — text layer and furniture")
    txt = subprocess.run(["pdftotext", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    absent = [c["claim_key"] for c in claims
              if c["claim_key"] not in txt]
    check(not absent, "all 35 claim keys in the PDF text layer",
          f"(absent: {absent})")
    m = re.findall(r"— (\d+) of (\d+) —", txt)
    check(bool(m) and m[-1][0] == m[-1][1],
          "footer count resolves", f"(last: {m[-1] if m else None})")
    rtl = [ch for ch in txt
           if "\u0590" <= ch <= "\u05ff"
           or "\u0600" <= ch <= "\u06ff"]
    check(not rtl, "no Arabic-block or Hebrew-block codepoint "
          "stands in the text layer — the declared substitution "
          "is entire", f"(found: {rtl[:5]})")
    check("Twlhm" in txt, "the dress of ةولهم (Twlhm) stands "
          "in the text layer")
    check("marked substitution" in txt,
          "the substitution's declaration stands in the layer")
else:
    log("6. THE MAGVS PDF — not yet built; text-layer check "
        "deferred to the post-build run")

log("")
log(f"PRICED CELLS RE-WEIGHED: {cells}")
verdict = "PASS" if not failures else "FAIL"
log(f"AUDIT VERDICT: {verdict}"
    + ("" if not failures else f" — {failures}"))
OUT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
sys.exit(0 if not failures else 1)
