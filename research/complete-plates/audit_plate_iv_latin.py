#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_iv_latin.py
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
# MECHANISM: the independent audit of PLATE-IV-LATIN. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the banks from pontifex.tables, the annex from
# pontifex.numerals and doubles, the Phoenician column from
# the map's JSON, the claims from the mapping register, the
# frame cells from THE-TWELVE-TABLES — and only then compared
# against what the plate prints. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. both banks, letter by letter, against the plate's §II
#      rows (letter and value parsed from the master), the
#      run sums and totals, W's Agrippa silence and its
#      printed hole row, the seam's three dresses in both
#      banks;
#   3. the Phoenician column: each single-letter heir's
#      engine price against the map's filed value; TH and
#      the empty heir filed unpriced; the filed total 243;
#   4. the annex: the module's own checks re-run; the
#      doubles' statuses, promotions and joins; the
#      triples; the subtractives; the exhibits;
#      parse('VVII') = 12; WVII refused by the instrument;
#   5. the §V figures: the pure five, the four hybrids, the
#      six candidates with their Greek twins, the Latin
#      Nine's totals and roots, the nine dresses and their
#      totals, VVII's prices and reductions, Y's Agrippa
#      400 against upsilon's Greek price;
#   6. every §IV claim: key present on the plate; the
#      engine's recomputation in the claim's own bank (the
#      English dress through latin_ordinal) equal to the
#      register's claimed and recomputed; verdict and
#      subseat counts equal; the 30 VERIFIED coordinates
#      and 7 bridge annotations entire on the plate; the
#      two empty registers printed as empty;
#   7. the §III frame cells — 178 natives and 45 doors —
#      re-weighed in both banks against the Tables;
#   8. if the MAGVS PDF stands beside the master, its text
#      layer carries all 262 claim keys, the plate's page
#      furniture resolves, and no Hebrew-block or
#      Arabic-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_iv_latin_results.txt beside
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
from pontifex.tables import LATIN_ORDINAL, AGRIPPA
from pontifex import numerals
from pontifex.doubles import DOUBLES as LATIN_PAIRS

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-IV-LATIN.md"
PDF = GOAL_FILES / "PLATE-IV-LATIN-MAGVS.pdf"
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
MAP_JSON = (Path.home() / "workspace/pontifex/maps/"
            "phoenician-cypher-glyph-map/"
            "phoenician-cypher-glyph-map.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUT = HERE / "audit_plate_iv_latin_results.txt"

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


def value(word, bank="latin_ordinal"):
    return weigh(word, bank)["value"]


def digits(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


text = MASTER.read_text(encoding="utf-8")

# --- 1. Controls ---------------------------------------------------
log("1. CONTROLS")
for word, bank, want in [("θελημα", "greek", 93),
                         ("VAPOUR", "latin_ordinal", 93),
                         ("σφιγξ", "greek", 773)]:
    check(value(word, bank) == want, f"control {word} = {want}")

# --- 2. The banks, letter by letter --------------------------------
log("2. THE BANKS — 26 + 25 keys re-weighed, plate rows parsed")
ord_section = text.split("### The ordinal bank")[1] \
    .split("**The ordinal sums.**")[0]
agr_section = text.split("### The Agrippa bank")[1] \
    .split("**The Agrippa sums.**")[0]


def parse_rows(section):
    rows = {}
    for line in section.splitlines():
        m = re.match(r"\| ([A-Z]) \| (\d+) \|", line)
        if m:
            rows[m.group(1)] = int(m.group(2))
    return rows


ord_rows = parse_rows(ord_section)
agr_rows = parse_rows(agr_section)
for glyph, want in LATIN_ORDINAL.items():
    got = value(glyph)
    cells += 1
    check(got == want and ord_rows.get(glyph) == want,
          f"ordinal {glyph} = {want}",
          f"(engine {got}, plate {ord_rows.get(glyph)})")
check(len(ord_rows) == 26, "plate prints all 26 ordinal rows",
      f"({len(ord_rows)})")
for glyph, want in AGRIPPA.items():
    got = value(glyph, "agrippa")
    cells += 1
    check(got == want and agr_rows.get(glyph) == want,
          f"agrippa {glyph} = {want}",
          f"(engine {got}, plate {agr_rows.get(glyph)})")
check(len(agr_rows) == 25, "plate prints all 25 Agrippa rows",
      f"({len(agr_rows)})")
check("W" not in AGRIPPA and value("W", "agrippa") == 0
      and "| W | — |" in agr_section,
      "W unseated in Agrippa (silence), its hole row printed")
check(sum(LATIN_ORDINAL.values()) == 351
      and sum(AGRIPPA.values()) == 2204
      and "**351**" in text and "**2,204**" in text,
      "bank totals: ordinal 351 · Agrippa 2,204")
for w, o, a in (("QUANTUM", 107, 641), ("QUANTVM", 108, 641),
                ("QVANTVM", 109, 641)):
    cells += 2
    check(value(w) == o and value(w, "agrippa") == a
          and f"| {w} | {o} | {a} |" in text,
          f"the seam: {w} = {o} ordinal · {a} Agrippa")

# --- 3. The Phoenician column ---------------------------------------
log("3. THE PHOENICIAN COLUMN — 22 rows cross-checked")
phoe = json.loads(MAP_JSON.read_text(encoding="utf-8"))
total = 0
for r in phoe["rows"]:
    lat = r["latin"]
    if len(lat) == 1:
        cells += 1
        check(value(lat) == r["latin_value"],
              f"map row {r['n']}: heir {lat} = "
              f"{r['latin_value']}")
        total += r["latin_value"]
    else:
        check(r["latin_value"] is None,
              f"map row {r['n']}: heir {lat!r} filed unpriced")
check(total == 243 == phoe["column_totals"]["latin"]
      and "**243 = 3⁵**" in text,
      "the column totals 243 = 3⁵, as filed")
cells += 1
check(value("TH") == 28 and "would weigh 28" in text,
      "TH priced as a string = 28 — the seam printed")

# --- 4. The annex ----------------------------------------------------
log("4. THE ANNEX — numerals.py re-run entire")
mod_checks = numerals.numerals_checks()
n_green = sum(1 for _n, ok, _g in mod_checks if ok)
check(all(ok for _n, ok, _g in mod_checks),
      f"numerals_checks(): {n_green}/{len(mod_checks)} green")
D = numerals.DOUBLES
check({p: D[p]["value"] for p in ("II", "XX", "CC", "MM")}
      == {"II": 2, "XX": 20, "CC": 200, "MM": 2000},
      "lawful doubles: II 2 · XX 20 · CC 200 · MM 2000")
check(D["VV"]["status"] == "refused_hybrid"
      and D["LL"]["status"] == "refused"
      and D["DD"]["status"] == "refused"
      and (D["VV"]["promotion"], D["LL"]["promotion"],
           D["DD"]["promotion"]) == ("X", "C", "M"),
      "statuses: VV refused_hybrid · LL, DD refused; "
      "promotions X · C · M")
for p in ("II", "VV", "XX", "LL", "CC", "DD", "MM"):
    cells += 2
    o, a = LATIN_PAIRS[p]["ordinal"], LATIN_PAIRS[p]["agrippa"]
    check(f"| {p} |" in text and f"| {o} | {a} |" in text,
          f"joins page: {p} at ordinal {o} · Agrippa {a}")
check(numerals.SUBTRACTIVES == {"IV": 4, "IX": 9, "XL": 40,
                                "XC": 90, "CD": 400, "CM": 900},
      "the six subtractives, generated by the rule")
for w, want in (("LXXVII", 77), ("XCIII", 93),
                ("MDCCLXXVI", 1776), ("MMXXVI", 2026),
                ("VVII", 12)):
    cells += 1
    check(numerals.parse(w) == want, f"parse({w}) = {want}")
try:
    numerals.parse("WVII")
    wvii_refused = False
except ValueError:
    wvii_refused = True
check(wvii_refused, "the instrument refuses WVII outright")
check("its both a double constanant and a double vowel" in text,
      "the founder's ground for the VV seat stands on the "
      "plate, as filed")

# --- 5. The §V figures ----------------------------------------------
log("5. THE BEARING — the Latin Nine, the dresses, VVII")
pure5 = ("A", "E", "I", "O", "V")
cells += 10
check(sum(LATIN_ORDINAL[g] for g in pure5) == 52
      and sum(AGRIPPA[g] for g in pure5) == 265,
      "the pure five: 52 ordinal · 265 Agrippa")
for h, o, a in (("EI", 14, 14), ("AE", 6, 6), ("OE", 20, 55),
                ("VI", 31, 209), ("AV", 23, 201),
                ("EV", 27, 205)):
    cells += 2
    check(value(h) == o and value(h, "agrippa") == a,
          f"candidate {h} = {o} ordinal · {a} Agrippa")
check(sum(value(h) for h in
          ("AE", "AV", "OE", "EI", "EV", "VI")) == 121 == 11 ** 2,
      "the six candidates sum to 121 = 11² in the ordinal")
nine_o = 52 + sum(value(h) for h in ("EI", "AE", "OE", "VI"))
nine_a = 265 + sum(value(h, "agrippa")
                   for h in ("EI", "AE", "OE", "VI"))
cells += 8
check((nine_o, nine_a) == (123, 549)
      and digits(nine_o) == 6 and digits(nine_a) == 9
      and "**123**" in text and "**549**" in text,
      "the Latin Nine: 123 ordinal (→ 6) · 549 Agrippa (→ 9)")
DRESS9 = [("Α", "A", 1), ("Ε", "E", 5), ("Η", "E", 8),
          ("Ι", "I", 10), ("Ο", "O", 70), ("Υ", "V", 400),
          ("Ω", "O", 800), ("ΕΙ", "EI", 15), ("ΟΥ", "OV", 470)]
to, ta = 0, 0
for g, d, gv in DRESS9:
    cells += 3
    check(value(g, "greek") == gv and f"| {g} | {gv} | {d} |"
          in text, f"dress {g} → {d} (Greek {gv})")
    to += value(d)
    ta += value(d, "agrippa")
check((to, ta) == (123, 584) and digits(ta) == 8,
      "the Greek nine in Latin dress: 123 ordinal · "
      "584 Agrippa (→ 8, the hybrids' root)")
cells += 3
check(value("VVII") == 62 and digits(62) == 8
      and value("VVII", "agrippa") == 418
      and digits(418) == 4,
      "VVII: ordinal 62 (→ 8) · Agrippa 418 (→ 13 → 4)")
check(value("Y", "agrippa") == 400 == value("υ", "greek"),
      "Υ's VALUE-mark: Y in Agrippa = 400 = upsilon's "
      "Greek price")

# --- 6. The claims register -----------------------------------------
log("6. THE CLAIMS — 262, keys on the plate, words re-weighed")
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Latin"]
check(len(claims) == 262, "register carries 262 Latin claims")
missing = [c["claim_key"] for c in claims
           if c["claim_key"] not in text]
check(not missing, "all 262 claim keys stand on the plate",
      f"(missing: {missing})")
for c in claims:
    bank = ("latin_ordinal"
            if c["bank_engine"] == "english_ordinal"
            else c["bank_engine"])
    got = value(c["weighed_word"], bank)
    cells += 1
    check(got == c["recomputed"] == c["claimed"],
          f"{c['claim_key']} {c['weighed_word']} = {got} "
          f"({c['bank_engine']})",
          f"(register {c['recomputed']}/{c['claimed']})")
reg_verdicts = {}
subseats = {}
for c in claims:
    reg_verdicts[c["verdict"]] = \
        reg_verdicts.get(c["verdict"], 0) + 1
    subseats[c["bank_engine"]] = \
        subseats.get(c["bank_engine"], 0) + 1
check(reg_verdicts == {"VERIFIED": 262},
      f"register verdicts {reg_verdicts} — the perfect "
      "register")
check(subseats == {"latin_ordinal": 167, "agrippa": 86,
                   "english_ordinal": 9},
      f"register subseats {subseats}")
check("262 VERIFIED · 0 PARTED · 0 NOT VERIFIABLE" in text,
      "plate prints the verdict counts entire")
check("The parting register — EMPTY" in text
      and "The NOT VERIFIABLE register — EMPTY" in text,
      "the two empty registers stand printed as empty")
vc = [c for c in claims if c["coordinate"]]
check(len(vc) == 30
      and all(c["coordinate"] in text for c in vc),
      "all 30 VERIFIED coordinates stand entire")
br = [c for c in claims
      if c["bridge"] not in ("none.", "none", "")]
check(len(br) == 7
      and all(c["bridge"] in text for c in br),
      "all 7 bridge annotations stand entire")

# --- 7. The frame cells ----------------------------------------------
log("7. THE FRAME — 178 natives + 45 doors, both banks")
block = TWELVE.read_text(encoding="utf-8") \
    .split("### §V.4 — The Latin Table")[1].split("### §V.5")[0]
n_nat = n_door = 0
for line in block.splitlines():
    if "| NATIVE |" in line or "| DOOR |" in line:
        cells_md = [c.strip()
                    for c in line.strip().strip("|").split("|")]
        m = re.match(r"ordinal (\d+) · Agrippa (\d+)",
                     cells_md[4])
        o_want, a_want = int(m.group(1)), int(m.group(2))
        o_got = value(cells_md[3])
        a_got = value(cells_md[3], "agrippa")
        cells += 2
        if cells_md[2] == "NATIVE":
            n_nat += 1
            present = cells_md[3] in text
        else:
            n_door += 1
            present = True  # doors are cited, not reprinted
        check(o_got == o_want and a_got == a_want and present,
              f"frame {cells_md[0]} {cells_md[3]} = "
              f"{o_got} · {a_got} ({cells_md[2]})")
check(n_nat == 178 and n_door == 45,
      "frame census: 178 NATIVE · 45 DOOR priced cells",
      f"({n_nat}/{n_door})")
check("NATIVE **178** · DOOR **45** · HOLE **62**" in text,
      "plate prints the frame census entire")

# --- 8. The PDF's text layer (when built) ---------------------------
if PDF.exists():
    log("8. THE MAGVS PDF — text layer and furniture")
    txt = subprocess.run(["pdftotext", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    absent = [c["claim_key"] for c in claims
              if c["claim_key"] not in txt]
    check(not absent, "all 262 claim keys in the PDF text "
          "layer", f"(absent: {absent})")
    m = re.findall(r"— (\d+) of (\d+) —", txt)
    check(bool(m) and m[-1][0] == m[-1][1],
          "footer count resolves",
          f"(last: {m[-1] if m else None})")
    rtl = [ch for ch in txt
           if "\u0590" <= ch <= "\u05ff"
           or "\u0600" <= ch <= "\u06ff"]
    check(not rtl, "no Hebrew-block or Arabic-block "
          "codepoint stands in the text layer — the "
          "declared dress is entire",
          f"(found: {rtl[:5]})")
    check("PLATE IV" in txt, "the plate's head stands in "
          "the layer")
else:
    log("8. THE MAGVS PDF — not yet built; text-layer check "
        "deferred to the post-build run")

log("")
log(f"PRICED CELLS RE-WEIGHED: {cells}")
verdict = "PASS" if not failures else "FAIL"
log(f"AUDIT VERDICT: {verdict}"
    + ("" if not failures else f" — {failures}"))
OUT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
sys.exit(0 if not failures else 1)
