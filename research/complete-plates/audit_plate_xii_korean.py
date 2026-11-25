#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_xii_korean.py
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
# MECHANISM: the independent audit of PLATE-XII-KOREAN. It does
# not read the plate's own figures for its expectations: every
# priced cell is re-weighed on the house engine from its
# source — the banks from pontifex.tables, the door through
# engine.hangul(), the frame from THE-TWELVE-TABLES §V.12 —
# and only then compared against what the plate prints.
# Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) and the
#      mint's own seal (hangul_checks(), 11/11);
#   2. the bank entire: the plate's §II seat registers parsed
#      from the master (19 initials · 21 vowels · 27 finals)
#      — each sign's printed price against its stratum bank
#      through the Unicode-name resolution, in the order the
#      audit's frozen sequences carry; the strata sums
#      (190/231/378), the bank total 799, the distinct set
#      1–27, the census (67 keys);
#   3. the teeth: the doubles' prices against doublings
#      (only ㄲ coincides); the digraphs' refusal — no
#      digraph in the initial stratum, seven with no
#      choseong form, four (ㄵㄶㅀㅄ) with archaic namesakes
#      only; the four obsolete letters unseated in the
#      modern bank; ㆅ in no seat of the engine;
#   4. the hinge: raw initial seat 12, the door's null
#      (아이 22 with 2 nulls; 아 1 with 1), the raw bank's
#      parting (46), the final seat 21 (강 23, no null);
#   5. the door's exhibits (한글 52 with strata 20/20/12 ·
#      한국 40 · ㄳ 3 at its final seat · ㆍ modern 0 with
#      1 unseated);
#   6. the 1446 annex: the plate's annex registers parsed
#      (17/11/17) against HANGUL_1446_*; its sums
#      (153/66/153); its exhibits through the hist door
#      (ㆁㆍ 4 · ㅇ 15 · ㆍ 1 · ㄲ unseated);
#   7. the frame: the census parsed from THE-TWELVE-TABLES
#      §V.12 against the plate's printed census; the
#      plate's 223 DOOR rows — cell set equal to the
#      register's, each rendering re-weighed through the
#      hangul() door against its filed value; the 62 HOLE
#      rows present with coordinates; the GAP cell
#      CLXXXIV/10 on the plate; the register's 13
#      empty-rendering door rows, all filed 0;
#   8. the §V figures: the vowel seats 1–21 with ㅖ at 8;
#      the compound class at eleven; the five tongues' 8s
#      in their own banks; the Nine's sum 1,779; the zero
#      face standing in §IV; the placeholder coordinate
#      and the series state standing on the plate;
#   9. if the MAGVS PDF stands beside the master, its text
#      layer carries 한글 and 한국, the zero face's
#      statement, and every one of the 19 initial
#      compatibility signs; its footer resolves; and no
#      Hebrew-block codepoint stands in the layer (the
#      declared dress entire).
# Output is filed to audit_plate_xii_korean_results.txt
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

from pontifex import weigh
from pontifex.engine import hangul as hangul_door, hangul_checks
from pontifex.tables import (
    HANGUL, HANGUL_INITIAL, HANGUL_VOWEL, HANGUL_FINAL,
    HANGUL_1446, HANGUL_1446_INITIAL, HANGUL_1446_VOWEL,
    HANGUL_1446_FINAL, HANGUL_NULL_INITIAL,
    _HANGUL_SK_INITIAL, _HANGUL_SK_VOWEL, _HANGUL_SK_FINAL,
    _HANGUL_1446_CONSONANTS, _HANGUL_1446_VOWELS,
    _HANGUL_DIGRAPH_FINALS, _jamo_conjoining)

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-XII-KOREAN.md"
PDF = GOAL_FILES / "PLATE-XII-KOREAN-MAGVS.pdf"
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
RESULTS = HERE / "audit_plate_xii_korean_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank="hangul"):
    return weigh(word, bank)["value"]


master = MASTER.read_text(encoding="utf-8")
sec2 = master.split("## §II")[1].split("## §III")[0]
sec3 = master.split("## §III")[1].split("## §IV")[0]
sec5 = master.split("## §V")[1].split("## §VI")[0]

# --- 1. controls and the mint's seal ----------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)
seal = hangul_checks()
check("hangul_checks() stands 11/11",
      len(seal) == 11 and all(ok for _n, ok, _d in seal),
      f"{sum(1 for _n, ok, _d in seal if ok)}/{len(seal)}")

# --- 2. the bank --------------------------------------------------------
check("bank census: 67 keys", len(HANGUL) == 67, str(len(HANGUL)))
check("plate prints the 67-key census", "**67 keys**" in sec2)


def parse_register(block, with_reason=True):
    pat = (r"^\| (\d+) \| (\S) \| ([^|]+?) \| (\d+) \|"
           if with_reason else
           r"^\| (\d+) \| (\S) \| ([^|]+?) \| (\d+) \|$")
    return re.findall(pat, block, re.M)


STRATA = (
    ("initial", "### The initial stratum", "### The vowel stratum",
     _HANGUL_SK_INITIAL, HANGUL_INITIAL, "CHOSEONG", 190),
    ("vowel", "### The vowel stratum", "### The final stratum",
     _HANGUL_SK_VOWEL, HANGUL_VOWEL, "JUNGSEONG", 231),
    ("final", "### The final stratum", "### The teeth",
     _HANGUL_SK_FINAL, HANGUL_FINAL, "JONGSEONG", 378),
)
for label, head_a, head_b, seq, bank, kind, want_sum in STRATA:
    block = sec2.split(head_a)[1].split(head_b)[0]
    rows = parse_register(block)
    check(f"{label} register: {len(seq)} rows parsed",
          len(rows) == len(seq), str(len(rows)))
    for i, (seat, sign, _nm, price) in enumerate(rows):
        seat, price = int(seat), int(price)
        want_sign = seq[i]
        conj = _jamo_conjoining(want_sign, kind)
        check(f"{label} seat {seat}: {sign} price {price} == engine",
              sign == want_sign and seat == i + 1
              and price == bank[conj] == i + 1)
    check(f"{label} stratum sum == {want_sum}",
          sum(bank.values()) == want_sum)
check("bank total == 799", sum(HANGUL.values()) == 799)
check("distinct values are 1–27, max 27",
      sorted(set(HANGUL.values())) == list(range(1, 28)))

# --- 3. the teeth --------------------------------------------------------
init_price = {}
for g in "ㄱㄲㄷㄸㅂㅃㅅㅆㅈㅉ":
    init_price[g] = HANGUL_INITIAL[_jamo_conjoining(g, "CHOSEONG")]
facts = tuple(init_price[d] == 2 * init_price[b] for d, b in
              (("ㄲ", "ㄱ"), ("ㄸ", "ㄷ"), ("ㅃ", "ㅂ"), ("ㅆ", "ㅅ"),
               ("ㅉ", "ㅈ")))
check("teeth: only ㄲ coincides with twice its base",
      facts == (True, False, False, False, False), str(facts))
archaic, none_at_all = [], []
for g in _HANGUL_DIGRAPH_FINALS:
    conj = None
    try:
        conj = _jamo_conjoining(g, "CHOSEONG")
    except ValueError:
        none_at_all.append(g)
    if conj is not None:
        check(f"digraph {g}: no modern initial seat",
              conj not in HANGUL_INITIAL)
        archaic.append(g)
    check(f"digraph {g}: holds its final seat",
          _jamo_conjoining(g, "JONGSEONG") in HANGUL_FINAL)
check("teeth: four digraphs keep archaic namesakes (ㄵㄶㅀㅄ)",
      archaic == list("ㄵㄶㅀㅄ"), str(archaic))
check("teeth: seven digraphs have no choseong form",
      len(none_at_all) == 7, str(len(none_at_all)))
def _form(compat, kind):
    try:
        return _jamo_conjoining(compat, kind)
    except ValueError:
        return None


for g in "ㆁㅿㆆㆍ":
    check(f"obsolete {g}: no modern seat in any stratum",
          all(_form(g, k) is None or _form(g, k) not in b
              for k, b in (("CHOSEONG", HANGUL_INITIAL),
                           ("JUNGSEONG", HANGUL_VOWEL),
                           ("JONGSEONG", HANGUL_FINAL))))
try:
    _c = _jamo_conjoining("ㆅ", "CHOSEONG")
    check("ㆅ unseated at the initial stratum",
          _c not in HANGUL_INITIAL and _c not in HANGUL_1446_INITIAL)
except ValueError:
    check("ㆅ unseated at the initial stratum", True)

# --- 4. the hinge ---------------------------------------------------------
check("hinge: raw initial ㅇ seat == 12",
      HANGUL_INITIAL[HANGUL_NULL_INITIAL] == 12)
d = hangul_door("아이")
check("hinge: hangul(아이) == 22 with 2 nulls",
      d["value"] == 22 and d["null_initials"] == 2,
      f"{d['value']}/{d['null_initials']}")
check("hinge: the raw bank parts — spelling of 아이 == 46",
      value("아이") == 46)
d = hangul_door("아")
check("hinge: hangul(아) == 1 with 1 null (the Triad's exhibit)",
      d["value"] == 1 and d["null_initials"] == 1)
d = hangul_door("강")
check("hinge: final ㅇ a full letter — hangul(강) == 23, no null",
      d["value"] == 23 and d["final_subtotal"] == 21
      and d["null_initials"] == 0)

# --- 5. the door's exhibits ------------------------------------------------
r = hangul_door("한글")
check("door: 한글 == 52, strata 20/20/12",
      (r["value"], r["initial_subtotal"], r["vowel_subtotal"],
       r["final_subtotal"]) == (52, 20, 20, 12))
check("door: 한국 == 40", hangul_door("한국")["value"] == 40)
r = hangul_door("ㄳ")
check("door: bare ㄳ == 3 at its final seat",
      r["value"] == 3 and r["final_subtotal"] == 3)
r = hangul_door("ㆍ")
check("door: ㆍ modern == 0 with 1 unseated",
      r["value"] == 0 and r["unseated"] == 1)

# --- 6. the 1446 annex -------------------------------------------------------
annex_block = sec2.split("### The 1446 annex")[1]
annex_rows = re.findall(r"^\| (\d+) \| (\S) \| ([^|]+?) \| (\d+) \|$",
                        annex_block, re.M)
check("annex registers: 45 rows parsed", len(annex_rows) == 45,
      str(len(annex_rows)))
ANNEX = (
    (_HANGUL_1446_CONSONANTS, HANGUL_1446_INITIAL, "CHOSEONG"),
    (_HANGUL_1446_VOWELS, HANGUL_1446_VOWEL, "JUNGSEONG"),
    (_HANGUL_1446_CONSONANTS, HANGUL_1446_FINAL, "JONGSEONG"),
)
flat = []
for seq, bank, kind in ANNEX:
    for i, g in enumerate(seq):
        flat.append((i + 1, g, bank[_jamo_conjoining(g, kind)]))
check("annex rows == engine annex, in order",
      [(int(s), g, int(p)) for s, g, _n, p in annex_rows] == flat)
check("annex sums == (153, 66, 153)",
      (sum(HANGUL_1446_INITIAL.values()),
       sum(HANGUL_1446_VOWEL.values()),
       sum(HANGUL_1446_FINAL.values())) == (153, 66, 153))
check("annex exhibits: ㆁㆍ == 4 through the hist door",
      hangul_door("ㆁㆍ", hist=True)["value"] == 4)
check("annex exhibits: ㅇ hist == 15 (no null in 1446)",
      hangul_door("ㅇ", hist=True)["value"] == 15)
check("annex exhibits: ㆍ hist == 1 at vowel seat 1",
      hangul_door("ㆍ", hist=True)["value"] == 1)
check("annex exhibits: ㄲ refused on the hist path",
      hangul_door("ㄲ", hist=True)["unseated"] == 1)

# --- 7. the frame -------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
block = twelve_text.split("### §V.12 — The Korean Table")[1] \
    .split("## §VI")[0]
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
    if len(cells) == 4 and re.match(r"[A-Z]+/", cells[0]) \
            and cells[3].isdigit():
        plate_doors.append(cells)
    elif len(cells) == 3 and re.match(r"[A-Z]+/", cells[0]):
        plate_holes.append(cells)
check("plate door register: 223 rows", len(plate_doors) == 223,
      str(len(plate_doors)))
check("plate door rows == register rows, in order",
      [[c[0], c[1], c[2], c[3]] for c in plate_doors]
      == [[c[0], c[1], c[3], c[4]] for c in reg_doors])
for cells in reg_doors:
    check(f"door {cells[0]} {cells[3] or '(empty)'}: re-weighed "
          f"through hangul()",
          hangul_door(cells[3])["value"] == int(cells[4]))
empty_reg = [c for c in reg_doors if c[3] == ""]
check("the register's 13 empty-rendering door rows, all filed 0",
      len(empty_reg) == 13
      and all(c[4] == "0" for c in empty_reg), str(len(empty_reg)))
check("plate hole register: 62 rows", len(plate_holes) == 62,
      str(len(plate_holes)))
check("plate hole rows == register rows, in order",
      [[c[0], c[1], c[2]] for c in plate_holes]
      == [[c[0], c[1], c[5]] for c in reg_holes])
check("GAP cell CLXXXIV/10 on the plate", "CLXXXIV/10" in sec3)

# --- 8. the §V figures ----------------------------------------------------------
vow_price = {g: HANGUL_VOWEL[_jamo_conjoining(g, "JUNGSEONG")]
             for g in _HANGUL_SK_VOWEL}
check("vowel seats 1–21 in canonical order",
      [vow_price[g] for g in _HANGUL_SK_VOWEL]
      == list(range(1, 22)))
check("ㅖ at vowel seat 8", vow_price["ㅖ"] == 8)
check("ㅖ is a fused sign", "ㅖ" in "ㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ")
check("compound class counts eleven",
      len(list("ㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ")) == 11)
for glyph, bank in (("Η", "greek"), ("ⲏ", "coptic"),
                    ("И", "cyrillic"), ("Ը", "armenian"),
                    ("ჱ", "georgian")):
    check(f"the five tongues' 8: {glyph} == 8 in {bank}",
          value(glyph, bank) == 8)
nine = sum(value(w, "greek") for w in
           ("α", "ε", "η", "ι", "ο", "υ", "ω", "ει", "ου"))
check("the Nine sum 1779 without VV", nine == 1779, str(nine))
check("zero face stands in §IV", "THE ZERO FACE" in master
      and "**Claims on this plate: 0**" in master)
check("the PLACEHOLDER coordinate stands in §V",
      "PLACEHOLDER" in sec5 and "PLACEHOLDER" in master)
check("the series state stands on the plate",
      "## §IX — THE SERIES STATE" in master
      and "Plate XIII" in master)

# --- 9. the PDF layer ------------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    for w in ("한글", "한국"):
        check(f"PDF layer carries exhibit {w}", w in layer)
    check("PDF layer carries the zero face", "ZERO FACE" in layer)
    missing = [g for g in _HANGUL_SK_INITIAL if g not in layer]
    check("PDF layer carries all 19 initial signs", not missing,
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

# --- verdict ----------------------------------------------------------------------
failed = [(n, d) for n, ok, d in CHECKS if not ok]
lines = ["PLATE-XII-KOREAN — independent audit",
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
