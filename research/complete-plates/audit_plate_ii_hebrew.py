#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_ii_hebrew.py
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
# MECHANISM: the independent audit of PLATE-II-HEBREW. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the bank from pontifex.tables, the claims from the
# mapping register, the NATIVE cells and dresses from
# THE-TWELVE-TABLES — and only then compared against what the
# plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the 27 bank keys, letter by letter, against the plate's
#      §II rows (glyph, value and declared dress parsed from
#      the master; the dress checked against the audit's own
#      copy of the §II scheme);
#   3. the class sums; the matres and their sum; the founding
#      head in all three scripts; HIS in both Latin banks; the
#      key's Hebrew dress through the engine's own door;
#   4. every §IV claim: key present on the plate; for each
#      claim carrying a weighed word, the engine's
#      recomputation equal to the register's recomputed — and,
#      for VERIFIED claims, to the claimed value (Hebrew-script
#      words weighed in the seated bank; the door's words
#      through weigh_via_hebrew_fallback);
#   5. the §III NATIVE renderings and their ninety Aramaic
#      dresses re-weighed against the Tables;
#   6. verdict and subseat counts equal to the register's;
#   7. if the MAGVS PDF stands beside the master, its text
#      layer carries all 146 claim keys, the plate's page
#      furniture resolves, no right-to-left codepoint stands
#      in the layer (the declared substitution entire), and
#      the dress of the sharpest parting stands in its place.
# Output is filed to audit_plate_ii_hebrew_results.txt beside
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

from pontifex import weigh, weigh_via_hebrew_fallback
from pontifex import transliterate_latin_to_hebrew
from pontifex.tables import HEBREW

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-II-HEBREW.md"
PDF = GOAL_FILES / "PLATE-II-HEBREW-MAGVS.pdf"
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUT = HERE / "audit_plate_ii_hebrew_results.txt"

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


def value(word, bank="hebrew"):
    return weigh(word, bank)["value"]


def door_value(word):
    r = weigh_via_hebrew_fallback(word)
    return r["value"] if isinstance(r, dict) else r


text = MASTER.read_text(encoding="utf-8")

# --- 1. Controls ---------------------------------------------------
log("1. CONTROLS")
for word, bank, want in [("θελημα", "greek", 93),
                         ("VAPOUR", "latin_ordinal", 93),
                         ("σφιγξ", "greek", 773)]:
    check(value(word, bank) == want, f"control {word} = {want}")

# --- 2. The bank, letter by letter --------------------------------
log("2. THE BANK — 27 keys re-weighed, plate rows parsed")
SCHEME = {"א": "ʾ", "ב": "b", "ג": "g", "ד": "d", "ה": "h",
          "ו": "w", "ז": "z", "ח": "ḥ", "ט": "ṭ", "י": "y",
          "כ": "k", "ך": "K", "ל": "l", "מ": "m", "ם": "M",
          "נ": "n", "ן": "N", "ס": "s", "ע": "ʿ", "פ": "p",
          "ף": "P", "צ": "ṣ", "ץ": "Ṣ", "ק": "q", "ר": "r",
          "ש": "š", "ת": "t"}
plate_rows = {}
for line in text.splitlines():
    m = re.match(r"\| [^|]+ \| (\S+) \| [^|]+ \| (\d+) \| "
                 r"([^|]+) \|", line)
    if m and m.group(1) in HEBREW:
        plate_rows[m.group(1)] = (int(m.group(2)),
                                  m.group(3).strip())
for glyph, want in HEBREW.items():
    got = value(glyph)
    cells += 1
    prow = plate_rows.get(glyph)
    check(got == want and prow is not None and prow[0] == want
          and prow[1] == SCHEME[glyph],
          f"bank {glyph} = {want}, dress {SCHEME[glyph]}",
          f"(engine {got}, plate {prow})")
check(len(plate_rows) == 27, "plate prints all 27 bank rows",
      f"({len(plate_rows)})")

# --- 3. Sums, matres, the head, HIS, the key's dress ---------------
log("3. SUMS, MATRES, THE HEAD, HIS, THE KEY'S DRESS")
FINALS = ("ך", "ם", "ן", "ף", "ץ")
letters = [g for g in HEBREW if g not in FINALS]
check(sum(HEBREW[g] for g in letters) == 1495
      and "1,495" in text, "the 22 letters sum to 1,495")
check(sum(HEBREW.values()) == 1775 and "1,775" in text,
      "the 27 keys sum to 1,775")
matres = {g: value(g) for g in ("א", "ה", "ו", "י")}
cells += 4
check(matres == {"א": 1, "ה": 5, "ו": 6, "י": 10}
      and sum(matres.values()) == 22,
      f"matres {matres}, sum 22")
cells += 3
check(value("עז") == 77 and value("𐡏𐡆", "aramaic") == 77
      and value("ܥܙ", "aramaic") == 77,
      "the founding head עז = 77 in all three scripts")
cells += 2
check(value("HIS", "latin_ordinal") == 36
      and value("HIS", "agrippa") == 107,
      "HIS = 36 ordinal · 107 Agrippa")
dress = transliterate_latin_to_hebrew("WVII")[0]
cells += 1
check(dress == transliterate_latin_to_hebrew("VVII")[0]
      and value(dress) == 32 and dress in text,
      f"the key's Hebrew dress {dress} = 32, both spellings")

# --- 4. The claims register ---------------------------------------
log("4. THE CLAIMS — 146, keys on the plate, words re-weighed")
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Hebrew"]
check(len(claims) == 146, "register carries 146 Hebrew claims")
missing = [c["claim_key"] for c in claims
           if c["claim_key"] not in text]
check(not missing, "all 146 claim keys stand on the plate",
      f"(missing: {missing})")


def is_hebrew(word):
    return any("\u0590" <= ch <= "\u05ff" for ch in word)


for c in claims:
    if c["weighed_word"]:
        if is_hebrew(c["weighed_word"]):
            got = value(c["weighed_word"])
            road = "bank"
        else:
            got = door_value(c["weighed_word"])
            road = "door"
        cells += 1
        ok = got == c["recomputed"] and (
            c["verdict"] != "VERIFIED" or got == c["claimed"])
        check(ok, f"{c['claim_key']} {c['weighed_word']} = {got} "
              f"({road})",
              f"(register recomputed {c['recomputed']}, "
              f"claimed {c['claimed']}, {c['verdict']})")
reg_verdicts = {}
subseats = {}
for c in claims:
    reg_verdicts[c["verdict"]] = \
        reg_verdicts.get(c["verdict"], 0) + 1
    subseats[c["bank_engine"]] = \
        subseats.get(c["bank_engine"], 0) + 1
check(reg_verdicts == {"VERIFIED": 93, "PARTED": 11,
                       "NOT VERIFIABLE": 42},
      f"register verdicts {reg_verdicts}")
check(subseats == {"hebrew": 111, "hebrew_gadol": 21,
                   "hebrew_fallback": 14},
      f"register subseats {subseats}")
check("93 VERIFIED · 11 PARTED · 42 NOT VERIFIABLE" in text,
      "plate prints the verdict counts entire")
parted = [c for c in claims if c["verdict"] == "PARTED"]
check(all(c["coordinate"] in text for c in parted),
      "all 11 parting coordinates stand entire on the plate")
nv = [c for c in claims if c["verdict"] == "NOT VERIFIABLE"]
check(all(c["coordinate"] in text for c in nv),
      "all 42 NOT VERIFIABLE coordinates stand entire")
vc = [c for c in claims
      if c["verdict"] == "VERIFIED" and c["coordinate"]]
check(len(vc) == 11 and all(c["coordinate"] in text for c in vc),
      "all 11 VERIFIED coordinates stand entire")
br = [c for c in claims
      if c["bridge"] not in ("none.", "none", "")]
check(len(br) == 6 and all(c["bridge"] in text for c in br),
      "all 6 bridge annotations stand entire")

# --- 5. The NATIVE cells and their dresses -------------------------
log("5. THE NATIVES — 45 renderings and 90 dresses re-weighed")
block = TWELVE.read_text(encoding="utf-8") \
    .split("### §V.2 — The Hebrew Table")[1].split("### §V.3")[0]
n = 0
for line in block.splitlines():
    if "| NATIVE |" in line:
        cells_md = [c.strip()
                    for c in line.strip().strip("|").split("|")]
        m = re.search(r"Aramaic dresses: (\S+) · (\S+) = (\d+)\.",
                      cells_md[5])
        want = int(cells_md[4])
        got = value(cells_md[3])
        cells += 1
        n += 1
        check(got == want and cells_md[3] in text,
              f"native {cells_md[0]} {cells_md[3]} = {got}")
        for dress_word in (m.group(1), m.group(2)):
            got_d = value(dress_word, "aramaic")
            cells += 1
            check(got_d == want and dress_word in text,
                  f"dress {cells_md[0]} {dress_word} = {got_d}")
check(n == 45, "forty-five NATIVE cells audited", f"({n})")

# --- 6. The PDF's text layer (when built) ---------------------------
if PDF.exists():
    log("6. THE MAGVS PDF — text layer and furniture")
    txt = subprocess.run(["pdftotext", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    absent = [c["claim_key"] for c in claims
              if c["claim_key"] not in txt]
    check(not absent, "all 146 claim keys in the PDF text layer",
          f"(absent: {absent})")
    m = re.findall(r"— (\d+) of (\d+) —", txt)
    check(bool(m) and m[-1][0] == m[-1][1],
          "footer count resolves", f"(last: {m[-1] if m else None})")
    rtl = [ch for ch in txt
           if "\u0590" <= ch <= "\u05ff"
           or "\u0700" <= ch <= "\u074f"
           or "\U00010800" <= ch <= "\U0001085f"]
    check(not rtl, "no right-to-left codepoint stands in the "
          "text layer — the declared substitution is entire",
          f"(found: {rtl[:5]})")
    check("mʾdyM" in txt, "the dress of מאדים (mʾdyM) stands in "
          "the text layer")
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
