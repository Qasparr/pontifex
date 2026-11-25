#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_iv_latin.py
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
# MECHANISM: generates PLATE-IV-LATIN.md — Plate IV of THE
# THIRTEEN COMPLETE PLATES — in the gap-filling goal's files/,
# following the pattern PLATES I–III set (196025e · 1389c16 ·
# 5f0b4bd). Every figure on the plate is scripted from the
# house engine (pontifex weigh()) or carried entire from an
# instrument of record:
#   * the priced tables — BOTH Latin banks entire, read from
#     pontifex.tables (LATIN_ORDINAL, 26 keys; AGRIPPA, 25
#     keys, W unseated), each seat printed with its reasoning;
#   * the U/V seam — QUANTVM / QUANTUM / QVANTVM weighed in
#     both banks at build;
#   * the Roman doubles annex — pontifex.numerals entire: the
#     seven givens, the doubles' statuses and promotions, the
#     triples, the six subtractives, the joins page against
#     the Latin doubles map (pontifex.doubles), the evaluator
#     exhibits, and parse('VVII');
#   * the Phoenician map's Latin column — the 22 rows' filed
#     Latin heirs cross-checked against the engine letter by
#     letter, the column total recomputed from the map's own
#     JSON (maps/phoenician-cypher-glyph-map/);
#   * the claims register — the Latin plate's 262 claims read
#     from research/thirteen-plates/mapping_register.json,
#     verdicts as audited in THE-777-VERIFICATION-TABVLA (262
#     VERIFIED · 0 PARTED · 0 NOT VERIFIABLE, on three
#     subseats), each claim recomputed at build in its own
#     bank (the 9 english_ordinal claims through latin_ordinal,
#     the dress the mapping itself states);
#   * the Twelve Tables' Latin frame — its census counts and
#     its 178 NATIVE cells, parsed from THE-TWELVE-TABLES.md
#     §V.4, each cell's two bank values re-weighed at build;
#   * the tongue's bearing on the seated Archons — the Latin
#     Nine and its four seated hybrids from
#     THE-DIVINE-NINE-ABROAD-I-LATIN, the Greek nine in
#     primary Latin dress from THE-ARCHON-BATTERY Leg 2, and
#     VVII's anatomy from the battery and the seating. The
#     plate assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) are
# weighed BEFORE any plate figure is taken; a control failure
# aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's face.
# The relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes
# print at the size of the seats — on this plate, W's empty
# seat in Agrippa and the two empty verdict registers. The
# plate's own Latin is rendered in classical dress (V for U)
# in its inscriptions, under the founder's inscriptional
# rule; the seam that dress opens is itself a subject of §II.
#
# CONTENT TEST: Inputs — the engine's two Latin banks, the
# numerals instrument, the Phoenician map's JSON, the mapping
# register, the Twelve Tables master, the Latin essay, the
# battery, the seating. Processes — control calibration,
# scripted extraction, register-faithful emission in the
# Teacher's Edition manner. Outputs — PLATE-IV-LATIN.md
# beside the series' other masters. Tolerances — the audit
# (audit_plate_iv_latin.py) re-weighs every priced cell
# independently; a figure that does not reproduce fails the
# plate.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh               # the house weighing engine
from pontifex.tables import LATIN_ORDINAL, AGRIPPA
from pontifex import numerals            # the Roman doubles annex
from pontifex.doubles import DOUBLES as LATIN_PAIRS

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
MAP_JSON = (Path.home() / "workspace/pontifex/maps/"
            "phoenician-cypher-glyph-map/"
            "phoenician-cypher-glyph-map.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-IV-LATIN.md"


def value(word, bank="latin_ordinal"):
    """One weighing, unwrapped to its integer."""
    return weigh(word, bank)["value"]


def digits(n):
    """The digital root, by the house's reduction chains."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


# ---------------------------------------------------------------------
# Calibration — the banks are not trusted until the controls read
# true.
# ---------------------------------------------------------------------
CONTROLS = [("θελημα", "greek", 93), ("VAPOUR", "latin_ordinal", 93),
            ("σφιγξ", "greek", 773)]
for word, bank, want in CONTROLS:
    got = value(word, bank)
    assert got == want, f"CONTROL FAIL: {word} {got} != {want}"
print("controls: θέλημα 93 · VAPOUR 93 · σφίγξ 773 — all true")

# ---------------------------------------------------------------------
# The ordinal bank — the sequence A=1 … Z=26, in three runs, each
# seat with its reasoning. Reasoning doctrine: the reasoning states
# the letter's place, its office where it has one, and the
# coordinates the corpus keeps for the seat — the vowels marked,
# the border letter marked, the banks' agreement and parting
# marked where they fall.
# ---------------------------------------------------------------------
ORD_RUN1 = [  # A–I, the sequence's units, 1–9
    ("A", "The first letter and the unit. A pure vowel — first of "
          "the Latin Nine's five pure letters (§V)."),
    ("B", "Second seat of the sequence."),
    ("C", "Third seat. In the numeral annex (§II) C is a power — "
          "100: the letter's two systems share the glyph and no "
          "value."),
    ("D", "Fourth seat; in the annex, the five-sign 500."),
    ("E", "Fifth seat. A pure vowel. E is invariant across the "
          "two banks (5 in both) — the banks agree through the "
          "whole units run and do not part until J."),
    ("F", "Sixth seat."),
    ("G", "Seventh seat. The Phoenician map's unhoused second "
          "Latin heir stands at this price in the map's Qore "
          "seats (G, Latin ordinal 7, ATTESTED there)."),
    ("H", "Eighth seat — 8 in both banks: the fold's number "
          "carried in this tongue by a consonant. The vowel "
          "seated at 8 is Greek's Η and its sisters' (§V)."),
    ("I", "Ninth seat. A pure vowel — and in the classical "
          "stock a letter of two offices, vowel and consonant "
          "in one sign, as V is: the grammarians' standing "
          "note. In Agrippa it shares its seat with J."),
]
ORD_RUN2 = [  # J–S, 10–19
    ("J", "Tenth seat — the sequence's own addition to the "
          "classical stock. In Agrippa it falls back to I's 9: "
          "the banks' first parting stands at this letter "
          "(Δ1)."),
    ("K", "Eleventh seat. The classical stock's Greek-loan "
          "letter, kept for Greek words and a handful of "
          "native ones."),
    ("L", "Twelfth seat; in the annex, the five-sign 50."),
    ("M", "Thirteenth seat; in the annex, the power 1,000."),
    ("N", "Fourteenth seat."),
    ("O", "Fifteenth seat. A pure vowel."),
    ("P", "Sixteenth seat."),
    ("Q", "Seventeenth seat — the letter that never walks "
          "alone: Q carries V (in modern dress U) behind it, "
          "as the seam word of §II shows."),
    ("R", "Eighteenth seat."),
    ("S", "Nineteenth seat; the run closes."),
]
ORD_RUN3 = [  # T–Z, 20–26
    ("T", "Twentieth seat."),
    ("U", "Twenty-first seat — the vocalic face of the border "
          "letter. In classical dress this letter is V, and "
          "the distance between the two spellings is the seam "
          "of §II: Δ1 per letter in this bank, identity in "
          "Agrippa."),
    ("V", "Twenty-second seat — the border letter itself: "
          "vowel and consonant in one sign, the classical "
          "stock's letter of two offices, and the seat the "
          "founder's hybrid ruling turns on (§II annex). It "
          "is also Υ's primary Latin dress in the Archon "
          "Battery (§V)."),
    ("W", "Twenty-third seat — the youngest letter, a doubled "
          "V by birth, as its very name says. Priced here; in "
          "Agrippa it has no seat at all (the boundary at the "
          "Agrippa table)."),
    ("X", "Twenty-fourth seat; in the annex, the power 10 — "
          "and VV's promotion there."),
    ("Y", "Twenty-fifth seat — the Greek-loan vowel, "
          "upsilon's Latin dress. In Agrippa it carries "
          "upsilon's own Greek price, 400 (§V)."),
    ("Z", "Twenty-sixth seat; the sequence closes."),
]
# ---------------------------------------------------------------------
# The Agrippa bank — the decade reckoning: units, tens, hundreds.
# ---------------------------------------------------------------------
AGR_UNITS = [  # A–J, 1–9 (J at I's seat)
    ("A", "The unit. The banks agree through the whole units "
          "run: Agrippa's first seats are the ordinal's own "
          "numbers."),
    ("B", "Second unit; the banks agree here."),
    ("C", "Third unit; the banks agree here."),
    ("D", "Fourth unit; the banks agree here."),
    ("E", "Fifth unit. A pure vowel, invariant across the "
          "banks."),
    ("F", "Sixth unit; the banks agree here."),
    ("G", "Seventh unit; the banks agree here."),
    ("H", "Eighth unit — 8, as in the ordinal: the fold's "
          "number at a consonant's seat in both banks."),
    ("I", "Ninth unit — the seat J shares: the bank prices "
          "the classical stock, in which I does both offices."),
    ("J", "Priced as I, 9: the bank seats no separate J — "
          "the letter is the younger sequence's addition. "
          "The banks' first parting stands here (ordinal "
          "10, Agrippa 9)."),
]
AGR_TENS = [  # K–S, 10–90
    ("K", "The first decade."),
    ("L", "Second decade, in Agrippa's order."),
    ("M", "Third decade, in Agrippa's order."),
    ("N", "Fourth decade, in Agrippa's order."),
    ("O", "Fifth decade. A pure vowel at 50."),
    ("P", "Sixth decade, in Agrippa's order."),
    ("Q", "Seventh decade, in Agrippa's order."),
    ("R", "Eighth decade, in Agrippa's order."),
    ("S", "Ninth decade; the tens close."),
]
AGR_HUNDREDS = [  # T–Z, 100–500
    ("T", "The first hundred."),
    ("U", "Two hundred — and V's twin: in this bank U and V "
          "weigh the same 200. This identity is the ground "
          "of UU == VV == 400 in the Latin doubles map, and "
          "of the seam's Agrippa identity (§II): QUANTVM "
          "and QUANTUM both weigh 641 here."),
    ("V", "Two hundred, U's twin — the border letter at one "
          "price in both its faces in this bank."),
    ("X", "Three hundred, in Agrippa's order."),
    ("Y", "Four hundred — upsilon's own Greek price, "
          "carried by its Latin dress: the VALUE-mark that "
          "rode Υ's seat in the seating (§V)."),
    ("Z", "Five hundred — the bank's seat maximum, and "
          "its close."),
]

ord_runs = [("The units of the sequence (1–9)", ORD_RUN1),
            ("The second run (10–19)", ORD_RUN2),
            ("The third run (20–26)", ORD_RUN3)]
agr_runs = [("The units (1–9)", AGR_UNITS),
            ("The tens (10–90)", AGR_TENS),
            ("The hundreds (100–500)", AGR_HUNDREDS)]
ord_sums = [sum(LATIN_ORDINAL[g] for g, _r in run)
            for _t, run in ord_runs]
agr_sums = [sum(AGRIPPA[g] for g, _r in run)
            for _t, run in agr_runs]
ord_total = sum(LATIN_ORDINAL.values())
agr_total = sum(AGRIPPA.values())
assert len(LATIN_ORDINAL) == 26 and len(AGRIPPA) == 25
assert "W" not in AGRIPPA and value("W", "agrippa") == 0
assert ord_sums == [45, 145, 161] and ord_total == 351
assert agr_sums == [54, 450, 1700] and agr_total == 2204

# The seam, weighed at build in both banks and all three dresses.
seam = {(w, b): value(w, b)
        for w in ("QUANTVM", "QUANTUM", "QVANTVM")
        for b in ("latin_ordinal", "agrippa")}
assert seam[("QUANTVM", "latin_ordinal")] == 108
assert seam[("QUANTUM", "latin_ordinal")] == 107
assert seam[("QVANTVM", "latin_ordinal")] == 109
assert seam[("QUANTVM", "agrippa")] == 641
assert seam[("QUANTUM", "agrippa")] == 641
assert seam[("QVANTVM", "agrippa")] == 641

# ---------------------------------------------------------------------
# The Roman doubles annex — every figure from pontifex.numerals
# and the Latin doubles map, computed at build.
# ---------------------------------------------------------------------
assert numerals.numerals_checks() and \
    all(ok for _n, ok, _g in numerals.numerals_checks())
DOUBLES = numerals.DOUBLES
lawful = {p: e["value"] for p, e in DOUBLES.items()
          if e["status"] == "lawful"}
refused = {p: e for p, e in DOUBLES.items()
           if e["status"] in ("refused", "refused_hybrid")}
assert lawful == {"II": 2, "XX": 20, "CC": 200, "MM": 2000}
assert {p: e["status"] for p, e in refused.items()} == \
    {"VV": "refused_hybrid", "LL": "refused", "DD": "refused"}
assert {p: e["promotion"] for p, e in refused.items()} == \
    {"VV": "X", "LL": "C", "DD": "M"}
JOINS = ("II", "VV", "XX", "LL", "CC", "DD", "MM")
joins = {p: (DOUBLES[p]["value"], LATIN_PAIRS[p]["ordinal"],
             LATIN_PAIRS[p]["agrippa"]) for p in JOINS}
assert joins == {"II": (2, 18, 18), "VV": (None, 44, 400),
                 "XX": (20, 48, 600), "LL": (None, 24, 40),
                 "CC": (200, 6, 6), "DD": (None, 8, 8),
                 "MM": (2000, 26, 60)}, joins
SUBTRACTIVES = numerals.SUBTRACTIVES
assert SUBTRACTIVES == {"IV": 4, "IX": 9, "XL": 40, "XC": 90,
                        "CD": 400, "CM": 900}
exhibits = {w: numerals.parse(w)
            for w in ("LXXVII", "XCIII", "MDCCLXXVI", "MMXXVI")}
assert exhibits == {"LXXVII": 77, "XCIII": 93,
                    "MDCCLXXVI": 1776, "MMXXVI": 2026}
vvii_parse = numerals.parse("VVII")
assert vvii_parse == 12, vvii_parse

# ---------------------------------------------------------------------
# The Phoenician map's Latin column — the 22 rows' heirs,
# cross-checked letter by letter; the column total from the
# map's filed values, as the map files them.
# ---------------------------------------------------------------------
phoe = json.loads(MAP_JSON.read_text(encoding="utf-8"))
prows = phoe["rows"]
assert len(prows) == 22
for r in prows:
    lat = r["latin"]
    if len(lat) == 1:
        assert value(lat) == r["latin_value"], r
    else:  # the digraph TH and the empty heir file no price
        assert r["latin_value"] is None, r
phoe_latin_total = sum(r["latin_value"] for r in prows
                       if r["latin_value"] is not None)
assert phoe_latin_total == 243 == 3 ** 5
assert phoe["column_totals"] == {"greek": 1095, "latin": 243,
                                 "arabic": 1495}
th_row = next(r for r in prows if r["latin"] == "TH")
th_as_string = value("TH")
assert th_as_string == 28
empty_row = next(r for r in prows if r["latin"] == "")

# ---------------------------------------------------------------------
# §V figures — the Latin Nine, the six candidates, the Greek
# nine in Latin dress, VVII — all weighed at build.
# ---------------------------------------------------------------------
PURE5 = ("A", "E", "I", "O", "V")
pure5_ord = sum(LATIN_ORDINAL[g] for g in PURE5)
pure5_agr = sum(AGRIPPA[g] for g in PURE5)
assert (pure5_ord, pure5_agr) == (52, 265)
HYBRIDS4 = ("EI", "AE", "OE", "VI")
hyb = {h: (value(h), value(h, "agrippa")) for h in HYBRIDS4}
assert hyb == {"EI": (14, 14), "AE": (6, 6), "OE": (20, 55),
               "VI": (31, 209)}, hyb
nine_ord = pure5_ord + sum(v[0] for v in hyb.values())
nine_agr = pure5_agr + sum(v[1] for v in hyb.values())
assert (nine_ord, nine_agr) == (123, 549)
assert (digits(nine_ord), digits(nine_agr)) == (6, 9)
CAND6 = ("AE", "AV", "OE", "EI", "EV", "VI")
cand6 = {h: (value(h), value(h, "agrippa"),
             value({"AE": "ΑΙ", "AV": "ΑΥ", "OE": "ΟΙ",
                    "EI": "ΕΙ", "EV": "ΕΥ", "VI": "ΥΙ"}[h],
                   "greek")) for h in CAND6}
assert cand6 == {"AE": (6, 6, 11), "AV": (23, 201, 401),
                 "OE": (20, 55, 80), "EI": (14, 14, 15),
                 "EV": (27, 205, 405), "VI": (31, 209, 410)}, cand6
assert sum(v[0] for v in cand6.values()) == 121 == 11 ** 2
assert sum(v[1] for v in cand6.values()) == 690
assert digits(690) == 6
# The Greek nine in primary Latin dress (the battery, Leg 2):
DRESS9 = [("Α", "A"), ("Ε", "E"), ("Η", "E"), ("Ι", "I"),
          ("Ο", "O"), ("Υ", "V"), ("Ω", "O"), ("ΕΙ", "EI"),
          ("ΟΥ", "OV")]
dress9 = [(g, d, value(d), value(d, "agrippa")) for g, d in DRESS9]
dress9_ord = sum(r[2] for r in dress9)
dress9_agr = sum(r[3] for r in dress9)
assert (dress9_ord, dress9_agr) == (123, 584)
assert digits(dress9_agr) == 8 and digits(dress9_ord) == 6
assert value("EI", "agrippa") == 14 and value("Y") == 25
assert value("Y", "agrippa") == 400 == value("υ", "greek")
assert value("U") == 21 and value("U", "agrippa") == 200
# VVII's anatomy:
vvii = (value("VVII"), value("VVII", "agrippa"))
assert vvii == (62, 418) and digits(62) == 8
assert digits(418) == 4 and sum(int(d) for d in "418") == 13

# ---------------------------------------------------------------------
# The claims register — the Latin plate's 262, from the mapping.
# ---------------------------------------------------------------------
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Latin"]
assert len(claims) == 262, len(claims)
verdicts = {}
for c in claims:
    verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
assert verdicts == {"VERIFIED": 262}, verdicts
sections = {c["section_number"] for c in claims}
assert len(sections) == 104, len(sections)
subseats = {}
for c in claims:
    sub = subseats.setdefault(c["bank_engine"], {})
    sub[c["verdict"]] = sub.get(c["verdict"], 0) + 1
assert subseats == {"latin_ordinal": {"VERIFIED": 167},
                    "agrippa": {"VERIFIED": 86},
                    "english_ordinal": {"VERIFIED": 9}}, subseats
for c in claims:  # every claim recomputed at build, in its bank
    bank = ("latin_ordinal" if c["bank_engine"] == "english_ordinal"
            else c["bank_engine"])
    got = value(c["weighed_word"], bank)
    assert got == c["recomputed"] == c["claimed"], c["claim_key"]
    assert "|" not in c["proposal_raw"]
    assert "|" not in (c["weighed_word"] or "")
bridges = [c for c in claims
           if c["bridge"] not in ("none.", "none", "")]
assert len(bridges) == 7, len(bridges)
verified_coords = [c for c in claims
                   if c["verdict"] == "VERIFIED" and c["coordinate"]]
assert len(verified_coords) == 30, len(verified_coords)
by_bank = {b: [c for c in claims if c["bank_engine"] == b]
           for b in ("latin_ordinal", "agrippa", "english_ordinal")}

# ---------------------------------------------------------------------
# The Twelve Tables' Latin frame — census and priced cells.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
latin_block = twelve_text.split("### §V.4 — The Latin Table")[1] \
    .split("### §V.5")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", latin_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
natives, doors = [], []
for line in latin_block.splitlines():
    if "| NATIVE |" in line or "| DOOR |" in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.match(r"ordinal (\d+) · Agrippa (\d+)", cells[4])
        o_want, a_want = int(m.group(1)), int(m.group(2))
        assert value(cells[3]) == o_want, cells
        assert value(cells[3], "agrippa") == a_want, cells
        (natives if cells[2] == "NATIVE" else doors).append(cells)
assert len(natives) == n_native == 178, len(natives)
assert len(doors) == n_door == 45, len(doors)

L = []  # the master's lines


def add(text=""):
    L.append(text)


# ---------------------------------------------------------------------
# Title block — the Teacher's Edition manner.
# ---------------------------------------------------------------------
add("![The Doctrine's Logo — TVRRIS VERITATIS seal]"
    "(~/workspace/templates/doctrine-logo.png)")
add()
add("# THE THIRTEEN COMPLETE PLATES")
add()
add("**PLATE IV — LATIN**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Latin "
    "tongue's complete 777 table — both banks entire, the "
    "sequence and the decade reckoning; the U/V seam; the Roman "
    "doubles annexed; the 777 corpus's Latin claims with their "
    "verification verdicts; and the tongue's witness to the "
    "seated Archons: the hybrids' second home, the Nine in "
    "Latin dress, and the key-string VVII taken apart.")
add()
add("Authorship attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without Prejudice)")
add("XXIV day of November, Dies Martis, Sol in Sagittarius, "
    "Anno V:xii e.n. (2026 e.v.)")
add()
add("Classification: Enterprise • Educational • Research & "
    "Development")
add("Method of Science, Aim of Religion")
add()
add("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, "
    "ARR, All Rights Reserved, Without Prejudice. Right of claim "
    "hereby reserved and coined under the authority of the "
    "Living Man.")
add()
add("---")

# ---------------------------------------------------------------------
# §I — The commission and the relation.
# ---------------------------------------------------------------------
add()
add("## §I — PLATE IV AND ITS COMMISSION")
add()
add("The founder's commission of 2026-11-24 (18:39–18:41 EST) "
    "opens the series this plate continues, in his words: "
    "*\"When we have the Archons for sure then we can begin the "
    "777 complete tables in the 12 tongues on 13 plates the 13th "
    "plate being the infrastructure for the clock and counter of "
    "the dial\"* — and its cadence: *\"as each plate gets "
    "rendered push and post it in succession until the 12 "
    "tongues are all plated.\"* The gate the commission names is "
    "met: the Archons are seated (THE-SEATING-OF-THE-ARCHONS, "
    "pontifex 0760c8a — T1 PASSES whole at graded classes; T2 "
    "PARTS at the axis). PLATE I — GREEK (pontifex 196025e) set "
    "the pattern; PLATE II — HEBREW (1389c16) and PLATE III — "
    "ARABIC (5f0b4bd) followed it; this plate follows them, "
    "fourth of the twelve tongues in the Twelve Tables' order.")
add()
add("**The series.** Thirteen plates: one for each tongue of "
    "the Twelve Tables in their order — I Greek · II Hebrew · "
    "III Arabic · IV Latin · V Japanese · VI Ge'ez · VII "
    "Armenian · VIII Coptic · IX Georgian · X Cyrillic · XI "
    "Glagolitic · XII Korean — and Plate XIII, a separate "
    "species commissioned last: the infrastructure for the "
    "clock and counter of the dial. Each plate renders its "
    "tongue's complete 777 table: the full priced letter-table "
    "as the house engine seats it; every correspondence the 777 "
    "corpus assigns in that tongue, with the verification "
    "verdicts of THE-777-VERIFICATION-TABVLA riding with each "
    "row; and the tongue's bearing on the seated Archons.")
add()
add("**This plate's distinction.** Latin is the one tongue of "
    "the twelve that carries **two banks** — the ordinal "
    "sequence and Agrippa's decade reckoning — and the one "
    "whose register is **perfect**: its 262 claims verify "
    "entire, without one parting. It is also the largest plate "
    "of the series by register, and the hybrids' second home: "
    "the tongue whose own Nine is completed by four seated "
    "hybrids, as Greece's was completed by two (§V).")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. This series *fulfills* "
    "that map: where the map counted the Latin claims, this "
    "plate prints them entire, with both of the tongue's "
    "priced tables beneath them and its witness to the "
    "Archons stated above them. The earlier work stands as "
    "the prior instrument of the same name's family — marked "
    "prior, never overwritten; its Latin face (262 claims · "
    "262 verified · 0 parted · 0 not verifiable, on three "
    "subseats) is this plate's §IV register, carried entire.")
add()
add("**How the plate is read.** §II is the banks: both tables "
    "at their prices, each seat with its reasoning; the seam "
    "between the spellings; and the Roman doubles annexed, "
    "the tongue's own older arithmetic. §III is the tongue's "
    "frame in the Twelve Tables — the census of its 371 "
    "cells, each priced cell carrying both banks' values. "
    "§IV is the corpus's Latin register entire. §V is the "
    "tongue's bearing on the seated Archons — this plate "
    "draws no seating (the seating is struck, and Plate I "
    "drew it); it states what Latin witnesses. §VI is the "
    "audit. A value without its reasoning is not shippable; "
    "a hole prints at the size of the seat it stands in for.")

# ---------------------------------------------------------------------
# §II — The complete priced tables, both banks.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §II — THE COMPLETE LATIN PRICED TABLES")
add()
add("Latin carries two banks, and the plate prints both "
    "entire. **The ordinal bank** is the sequence itself — "
    "A = 1 through Z = 26, the letter priced by its place; "
    "the reckoning the modern ordinal tables keep. **The "
    "Agrippa bank** is the decade reckoning of the "
    "occult-philosophical tradition that bears Agrippa's "
    "name: units 1–9, tens 10–90, hundreds 100–500, over "
    "the classical letter-stock. Tier of the banks: the "
    "values **ATTESTED** as the traditions that keep them "
    "state them — the sequence by its own definition, the "
    "decade table as the Agrippa tradition hands it down — "
    "and the engine seats both as sourced. The banks agree "
    "through the units run (A–I at 1–9 in both) and part "
    "first at J; every parting below is printed where it "
    "stands, not smoothed.")
add()
add("**Two boundaries are named before the tables.** "
    "First: **W has no seat in the Agrippa bank.** The "
    "bank's gap-register entry stands FENCED — *the "
    "tradition's own boundary: Agrippa's table predates "
    "W's letterhood; the letter passes in silence and the "
    "coordinate prints wherever it bites* — and it bites "
    "in the register (§IV), where four verified claims "
    "carry the coordinate of a W skipped in silence. The "
    "letter's empty seat is printed at the Agrippa table's "
    "hundreds run, at the size of the seat. Second: **VV "
    "the refused double** carries the founder's RULING, "
    "resolved in the gap register by his own word — *VV "
    "seats as the hybrid — refused as a numeral, seated "
    "under the legend's law — in numerals.py/doubles.py, "
    "not in the letter banks; the letter tables are "
    "untouched by it* — and the annex below prints the "
    "ruling's instrument entire. Both resolutions stand "
    "revisable by his pen; this plate reclassifies "
    "nothing.")


def bank_table(title, rows, bank):
    add()
    add(f"### {title}")
    add()
    add("| Letter | Value | Reasoning |")
    add("|---|---|---|")
    table = LATIN_ORDINAL if bank == "latin_ordinal" else AGRIPPA
    for glyph, why in rows:
        add(f"| {glyph} | {table[glyph]} | {why} |")


add()
add("### The ordinal bank — the sequence (26 letters)")
for title, rows in ord_runs:
    bank_table(title, rows, "latin_ordinal")
add()
add(f"**The ordinal sums.** The runs sum {ord_sums[0]} · "
    f"{ord_sums[1]} · {ord_sums[2]} — the 26 letters sum to "
    f"**{ord_total}**. The Phoenician map's Latin column "
    f"carries this bank's other figure of record: over the "
    f"map's 22 rows — the letters of the shared Phoenician "
    f"line at their Latin heirs — the column totals "
    f"**{phoe_latin_total} = 3⁵**, recomputed at this "
    f"plate's build from the map's own file: each "
    f"single-letter heir's engine price equals the map's "
    f"filed value, and the filed values sum to "
    f"{phoe_latin_total}. Two coordinates of that column "
    f"print with it: the ṭēth row's Latin heir is the "
    f"digraph **TH**, which the map files unpriced — no "
    f"single Latin letter carries it; priced as a Latin "
    f"string it would weigh {th_as_string}, and the "
    f"column would read {phoe_latin_total + th_as_string} "
    f"— the seam printed, not smoothed — and the ṣādē "
    f"row's heir stands empty in the map, no Latin letter "
    f"at all. The map's totals stand as the map files "
    f"them (Greek 1,095 · Latin 243 · Arabic 1,495); the "
    f"identity with Plate III's Arabic column is the "
    f"shared line's arithmetic, stated there.")
add()
add("### The Agrippa bank — the decade reckoning (25 letters)")
for title, rows in agr_runs:
    bank_table(title, rows, "agrippa")
add()
add("| W | — | **No seat.** Agrippa's table predates W's "
    "letterhood; weighed in this bank, W passes in silence "
    "(value 0, no priced letters). The seat stands printed "
    "as a hole — FENCED, the tradition's own boundary, per "
    "the gap register — at the size of the seat it would "
    "hold, between V's twin hundreds and X. |")
add()
add(f"**The Agrippa sums.** Units {agr_sums[0]} · tens "
    f"{agr_sums[1]} · hundreds {agr_sums[2]:,} — the 25 "
    f"letters sum to **{agr_total:,}**. Against the "
    f"ordinal's {ord_total}: the two banks weigh the same "
    "alphabet at two reckonings, and their totals part as "
    "the reckonings part — no seam constant of this plate "
    "joins them, and none is claimed. Where the banks "
    "agree letter for letter (the units run, A–I), the "
    "agreement is the classical stock showing through "
    "both; where they part (J onward), each letter "
    "carries two prices, and every claim of §IV is judged "
    "against the bank it names.")
add()
add("**The zero.** Neither Latin bank has a figure for "
    "zero, and the Roman system annexed below has no zero "
    "sign at all — the medieval *nulla*, N, is a word's "
    "initial doing a zero's work, not a numeral sign, as "
    "the annex's instrument states. The founder's Zero "
    "Point seat — οὐδέν, the word that weighs 529 — is "
    "Greek's, and stands on Plate I. Latin's zero stands "
    "on this plate as a printed absence, as Arabic's did: "
    "a hole at the size of the seat.")
add()
add("### The seam — QVANTVM, and the Offset Law's type case")
add()
add("The founder's inscriptional rule renders Latin in "
    "classical dress — V for U — in the inscriptions of "
    "his house, this plate's own included. The dress opens "
    "a measurable seam, and the Nine Vowels essay states "
    "it as the Offset Law's type case; the plate weighs "
    "all three dresses at its build and prints them:")
add()
add("| Dress | Ordinal | Agrippa |")
add("|---|---|---|")
for w in ("QUANTUM", "QUANTVM", "QVANTVM"):
    add(f"| {w} | {seam[(w, 'latin_ordinal')]} | "
        f"{seam[(w, 'agrippa')]} |")
add()
add("In the ordinal, each U that takes its classical V "
    "steps the total by exactly **Δ1** — QUANTUM 107, "
    "QUANTVM 108, QVANTVM 109: a defined seam, a constant "
    "distance, both spellings true at their coordinates. "
    "In Agrippa the three dresses are **identical at "
    "641**: U and V keep one seat in the old bank (200 "
    "each), so the seam closes there entirely. The "
    "essay's classification stands: an **OFFSET** — not a "
    "failure that got lucky, a different relation "
    "entirely. [The values ATTESTED, recomputed here; "
    "the classification the founder's ruling, legislated "
    "in the Nine Vowels essay §VI.]")
add()
add("### Annex — the Roman doubles: the tongue's older "
    "arithmetic")
add()
add("The Roman numeral system is this tongue's annex: "
    "not a letter bank but the arithmetic the letters "
    "also carry as numerals, built by the house as "
    "pontifex/numerals.py — *the missing link of the "
    "Codex Legend, legend piece (i)* — on the founder's "
    "theory of 2026-11-24, stated in the module's "
    "epigraph in his words: *\"If there is a missing "
    "piece to the codex legend its going to be the roman "
    "numeral double letter system.\"* Its seven givens "
    "are ATTESTED (I 1 · V 5 · X 10 · L 50 · C 100 · "
    "D 500 · M 1,000); everything below is DERIVED from "
    "them by the module's stated law, computed at this "
    "plate's build from the instrument itself — the "
    "doubles' statuses, the promotions, the subtractive "
    "seats, and the module's own checks, which the "
    "plate re-ran entire and which stand green.")
add()
add("**The law.** Repetition is the system's "
    "arithmetic. The signs divide by their values into "
    "the POWERS (I, X, C, M — 1, 10, 100, 1,000), which "
    "may repeat to three, and the FIVES (V, L, D — 5, "
    "50, 500), which may never repeat: a doubled five "
    "is written as the next power instead — the "
    "PROMOTION. Four of anything stands outside the "
    "standard form; the answer to four is the "
    "subtractive seat. The doubles therefore stand:")
add()
add("| Double | Status | Numeral value | Promotion | "
    "Ordinal | Agrippa |")
add("|---|---|---|---|---|---|")
for p in JOINS:
    e = DOUBLES[p]
    val = ("—" if e["value"] is None else f"{e['value']:,}")
    prom = ("—" if e["promotion"] is None
            else f"{e['promotion']} "
                 f"({numerals.NUMERAL_VALUES[e['promotion']]:,})")
    add(f"| {p} | {e['status']} | {val} | {prom} | "
        f"{joins[p][1]} | {joins[p][2]} |")
add()
add("**The lawful doubles** — II 2 · XX 20 · CC 200 · "
    "MM 2,000 — weigh twice their sign: repetition is "
    "the arithmetic. **The refused** — LL and DD — "
    "carry no numeral value as spelled, and point at "
    "their promotions (LL → C, DD → M): Rome does not "
    "forbid the value, it forbids the spelling. **VV "
    "stands between**: refused as a numeral exactly as "
    "LL and DD are, promoted to X exactly as they are "
    "to C and M — and seated as the Roman face's "
    "**HYBRID** by the founder's ruling of 2026-11-24 "
    "(tier FOUNDER, his coinage under his Flagpole), "
    "on his ground as the module records it: *\"its "
    "both a double constanant and a double vowel\"* — "
    "V is the one classical letter that carries both "
    "natures (vocalic U and consonantal V are one "
    "letter; the Latin doubles map prints UU == VV == "
    "400 on Agrippa's bank, U read as V), so its "
    "double is a double consonant and a double vowel "
    "in the same glyphs. The seat is the founder's; "
    "the refusal is Rome's; the map prints both, "
    "flattened into neither. LL and DD carry no "
    "hybrid seat: their candidacy stands open for his "
    "pen, and the instrument does not extend his "
    "ruling for him.")
add()
add("**The joins page.** Weighed against the Latin "
    "doubles map (the twenty-six pairs of doubles.py), "
    "the two Latin banks agree with each other at "
    "exactly three of the seven pairs — II (18/18), "
    "CC (6/6), DD (8/8) — and the numeral doubles, "
    "where lawful, agree with *neither* bank anywhere: "
    "the two systems share the seven letters and no "
    "value at all. **The triples** stand lawful for "
    "the powers (III 3 · XXX 30 · CCC 300 · MMM "
    "3,000) and refused for the fives. **The six "
    "subtractive seats**, generated by the rule — a "
    "power before its five or the power above it "
    "weighs the difference: IV 4 · IX 9 · XL 40 · "
    "XC 90 · CD 400 · CM 900. **The evaluator "
    "exhibits**, whole numerals weighed by the "
    "system's own reading: LXXVII = 77, the house's "
    "number, itself built of two lawful doubles "
    "around V · XCIII = 93, a subtractive seat "
    "carrying a lawful triple · MDCCLXXVI = 1776 · "
    "MMXXVI = 2026. And one exhibit this plate adds "
    "from the seating's evidence: the instrument "
    f"parses **VVII = {vvii_parse}** — V + VII read "
    "additively — the key-string of §V standing as a "
    "numeral in this tongue's older arithmetic while "
    "its banks price it otherwise. The annex's tier: "
    "the givens ATTESTED, the map DERIVED, the "
    "hybrid seat FOUNDER.")

# ---------------------------------------------------------------------
# §III — The Twelve Tables' Latin frame.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §III — THE LATIN FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Latin tongue stands over the "
    "one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state — one tongue, two "
    "banks: every priced cell carries both values, ordinal "
    "and Agrippa, and W passes in silence in Agrippa, the "
    "tradition's own boundary (§II). Its census, from "
    f"THE-TWELVE-TABLES §V.4: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED "
    f"**{n_fenced}** · EMPTY {n_empty} · GAP {n_gap}. The "
    "face this prints is the inverse of Arabic's: where "
    "Arabic's frame was a door with eleven natives, "
    "Latin's is a native table — 178 of the corpus's own "
    "words stand in Latin letters as their own form, the "
    "largest native census of any tongue in the Tables, "
    "because the corpus's Latin-letter forms are the "
    "record's working dress. The 62 holes print with "
    "their coordinates in the Tables; the EMPTY cells "
    "are certified intentionally empty in 777 REVISED.")
add()
add("**The 178 NATIVE cells** — the corpus's own "
    "Latin-letter words, each priced in both banks:")
add()
add("| Cell | Word of record | Ordinal | Agrippa |")
add("|---|---|---|---|")
for cells in natives:
    m = re.match(r"ordinal (\d+) · Agrippa (\d+)", cells[4])
    add(f"| {cells[0]} | {cells[3]} | {m.group(1)} | "
        f"{m.group(2)} |")
add()
add(f"The door's {n_door} priced renderings — the "
    "corpus's printed transliterations of other tongues' "
    "words, priced in both banks — and the frame's full "
    "cell register stand in THE-TWELVE-TABLES §V.4, which "
    "this plate cites and does not reprint: the plate's "
    "tables are the *banks* (§II) and the corpus's "
    "*claims* (§IV); the frame's census rides here so "
    "the tongue's depth is data on the plate's face, as "
    "the Tables' own law requires. Every priced cell of "
    "the frame, native and door alike, was re-weighed "
    "in both banks at this plate's build and at its "
    "audit (§VI): the frame and the banks are one "
    "reckoning in two presentations.")

# ---------------------------------------------------------------------
# §IV — The corpus's Latin claims entire.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §IV — THE 777 CORPUS'S LATIN CLAIMS")
add()
add("The TABVLA's Latin register entire: **262 claims** "
    f"across {len(sections)} claim-bearing sections, each "
    "carried with its verdict as audited in "
    "THE-777-VERIFICATION-TABVLA and mapped in "
    "THE-THIRTEEN-PLATES. The counts: **262 VERIFIED · 0 "
    "PARTED · 0 NOT VERIFIABLE** — the register is "
    "perfect, the only perfect register among the "
    "plates struck so far, and its perfection is itself "
    "printed as a coordinate with its shape: the claims "
    "ride on **three subseats** — the Latin ordinal "
    "bank (167), the Agrippa bank (86), and the English "
    "ordinal dress (9), the last verified through "
    "latin_ordinal, English ordinal and the engine's "
    "ordinal bank being the same 26-seat table (A = 1 "
    "… Z = 26), as the mapping states on its face. "
    "The TABVLA's own count of the Latin banks stands "
    "as the register's summary: ordinal 167/167, "
    "Agrippa 86/86 — every claim the corpus states in "
    "a Latin bank recomputes to the digit in the bank "
    "it names. A VERIFIED claim recomputes to the "
    "digit. This register has no other verdict to "
    "print: the parting register and the "
    "not-verifiable register stand beneath the tables "
    "at full size, empty, as Plate I's Greek parting "
    "register stood empty — an absence with its "
    "coordinates stated, not a section skipped.")
for bank, title in (("latin_ordinal",
                    "The Latin ordinal subseat (167 claims)"),
                   ("agrippa", "The Agrippa subseat (86 claims)"),
                   ("english_ordinal",
                    "The English ordinal dress (9 claims, "
                    "verified through latin_ordinal)")):
    add()
    add(f"### {title}")
    add()
    add("| Claim | Cell | Proposal (word of record) | "
        "Weighed | Claimed | Recomputed | Verdict |")
    add("|---|---|---|---|---|---|---|")
    for c in by_bank[bank]:
        add(f"| {c['claim_key']} | {c['cell_id']} | "
            f"{c['proposal_raw']} | {c['weighed_word']} | "
            f"{c['claimed']:,} | {c['recomputed']:,} | "
            f"{c['verdict']} |")
add()
add("**The parting register — EMPTY, at full size.** No "
    "claim of the 262 parts from the bank it names. The "
    "register's perfection is bounded by its own "
    "coordinates and the plate prints the bound: the "
    "Latin claims are the corpus's claims *stated in "
    "Latin banks against Latin-letter words* — the "
    "fills' home ground, where their conventions and "
    "the banks coincide. The corpus's partings live "
    "where a fill's convention crosses a bank's "
    "silence (Arabic's tāʾ marbūṭa, Hebrew's gadol); "
    "Latin's one "
    "silence, W in Agrippa, is carried by four verified "
    "claims as a coordinate, not a parting (below). "
    "Perfection here is a property of the register's "
    "ground, printed as such — not a claim about any "
    "other tongue's register.")
add()
add("**The NOT VERIFIABLE register — EMPTY, at full "
    "size.** Every Latin claim prints its weighed word "
    "in its section; no claim of the 262 rests on an "
    "unprinted transliteration. The species that fills "
    "the other plates' registers — the word present "
    "only in another script's dress — does not occur "
    "on this plate.")
add()
add("**The VERIFIED coordinates** — the register "
    "carries coordinates for thirty verified claims, "
    "and the plate prints them entire because the "
    "register carries them. They are of three species: "
    "the nine English-dress claims, whose coordinate "
    "states the dress's identity with the ordinal "
    "bank; the four Agrippa claims whose words carry "
    "a W the bank skips in silence — the boundary of "
    "§II biting inside verified claims, the claims "
    "verifying *because* the fills priced W at "
    "silence, as the bank does; and the weapon-table "
    "claims whose weighed forms carry letters of "
    "other tongues' scripts at no price in the bank "
    "named, skipped in silence likewise:")
add()
for c in verified_coords:
    add(f"- **{c['claim_key']}** ({c['cell_id']}, "
        f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The bridges.** Seven claims of the register "
    "carry bridge annotations, and the plate prints "
    "them entire, at the tiers the TABVLA flags them "
    "— two flagged as bridge *candidates* under a "
    "chance flag, the rest as transliteration bridges "
    "at the constructed tier. A bridge annotation is "
    "not a verdict: each claim stands VERIFIED in its "
    "own bank on its own row above; the annotation "
    "records that the same number stands in a second "
    "bank, at the flag the register gives it:")
add()
for c in bridges:
    add(f"- **{c['claim_key']}** ({c['cell_id']}, "
        f"{c['source_coordinate']}): {c['bridge']}")

# ---------------------------------------------------------------------
# §V — The tongue's bearing on the seated Archons.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §V — THE TONGUE'S BEARING ON THE SEATED ARCHONS")
add()
add("The seating is THE-SEATING-OF-THE-ARCHONS' "
    "(0760c8a), struck on the Archon Battery's evidence "
    "under the founder's conditional order; Plate I "
    "drew it. **This plate assigns no seat.** It states "
    "what the Latin tongue witnesses for the seating — "
    "and Latin witnesses more than any tongue yet "
    "plated: it is the hybrids' second home, the "
    "tongue in which the Greek Nine itself was weighed "
    "abroad, and the tongue whose banks price the "
    "key-string the battery weighed. Its witness runs "
    "at four coordinates.")
add()
add("### The Latin Nine — five pure letters, four seated "
    "hybrids")
add()
add("THE-DIVINE-NINE-ABROAD-I-LATIN — the house's own "
    "essay, the Divine Nine carried abroad — seats a "
    "Latin Nine by Latin's own road: **five pure "
    "vowels, A · E · I · O · V, and exactly four seated "
    "hybrids, EI · AE · OE · VI.** The composition is "
    "the mirror-image of the Greek construction, and "
    "the essay prints the inversion exactly: Greece's "
    "canon was seven letters completed by two "
    "digraphs; Latin's letter-stock is five, completed "
    "by four. The Archon Battery's twelve-tongues "
    "sweep reads the seat a **HIT — the sweep's "
    "cleanest: a hybrid class of exactly four, seated "
    "by the house's own instrument.** The four, with "
    "their coordinates as the essay seats them:")
add()
add("| Hybrid | Ordinal | Agrippa | Greek twin | Seat |")
add("|---|---|---|---|---|")
add(f"| EI | {hyb['EI'][0]} | {hyb['EI'][1]} | ΕΙ = 15 | "
    "**Full seat** — Latin's improper diphthong, the "
    "Greek hybrid's exact twin in mechanism, standing "
    "Δ1 from it across the banks: the bridge (below). |")
add(f"| AE | {hyb['AE'][0]} | {hyb['AE'][1]} | ΑΙ = 11 | "
    "**Dialectal coordinate** — a hybrid in motion: "
    "proper at the standard's coordinate, single in "
    "sound on the spoken road; ΑΙ's Latin heir. |")
add(f"| OE | {hyb['OE'][0]} | {hyb['OE'][1]} | ΟΙ = 80 | "
    "**Dialectal coordinate** — as AE: the glide "
    "closed on the spoken road, its seat carrying its "
    "coordinate. |")
add(f"| VI | {hyb['VI'][0]} | {hyb['VI'][1]} | ΥΙ = 410 | "
    "**Micro-seat** — valid inside its two-word "
    "reservation (the closed pronoun class), claiming "
    "nothing outside it. |")
add()
add("The essay weighed six candidates and refused "
    "two, and the refusals print beside the seats, as "
    "the essay prints them: **AV** (23/201) — a proper "
    "diphthong at every classical coordinate, the "
    "glide never closes, REFUSED; **EV** (27/205) — "
    "Greece's digraph in Latin dress, REFUSED as "
    "native and recorded as a loan, its ordinal 27 = "
    "3³ standing in the record as the discipline's "
    "exhibit. The six together weigh 121 = 11² in the "
    "ordinal — a perfect square over the whole "
    "candidate field, seated and refused alike. "
    f"The Latin Nine's totals: ordinal **{nine_ord}** "
    f"(the pure five {pure5_ord} + the hybrids "
    f"{nine_ord - pure5_ord}), reducing to "
    f"{digits(nine_ord)} — the mirror digit, the same "
    f"root the Greek nine reduces to; Agrippa "
    f"**{nine_agr}** (the pure five {pure5_agr} + "
    f"{nine_agr - pure5_agr}), reducing to "
    f"{digits(nine_agr)} — the count itself. The "
    "chiasm is the essay's, printed as found. And "
    "the essay's fence stands on this plate as on "
    "its own face: identity with the Greek Nine "
    "FAILS (123 ≠ 549 ≠ 1,779) — the Latin Nine is "
    "the same *form*, a canon completed by its "
    "hybrids, standing on Latin ground at Latin "
    "totals. [The inventory ATTESTED; the seatings "
    "DERIVED; the composition CONSTRUCTED — the "
    "founder's commissioned extension, as the essay "
    "tiers it.] Beside the four, the battery's sweep "
    "marks a fifth hybridity of a different kind in "
    "this tongue: **V, the border letter** — vowel "
    "and consonant in one sign (§II) — the letter "
    "the hybrids cluster at, as the essay's own "
    "maxim directs: *find the border letter first.*")
add()
add("### The Greek Nine in Latin dress — the 123 identity")
add()
add("The Archon Battery's Leg 2 weighed the seated "
    "Archons' own vowels abroad — each Greek vowel in "
    "its primary Latin dress, the transliteration "
    "choices stated as choices in the battery and "
    "carried here as it states them:")
add()
add("| Vowel | Greek | Latin dress (primary) | Ordinal | "
    "Agrippa |")
add("|---|---|---|---|---|")
greek_vals = {"Α": 1, "Ε": 5, "Η": 8, "Ι": 10, "Ο": 70,
              "Υ": 400, "Ω": 800, "ΕΙ": 15, "ΟΥ": 470}
for g, d, o, a in dress9:
    add(f"| {g} | {greek_vals[g]} | {d} | {o} | {a} |")
add()
add(f"The totals over the primary dresses: ordinal "
    f"**{dress9_ord}** · Agrippa **{dress9_agr}**. The "
    f"first coordinate is the battery's sharpest Latin "
    f"finding: the Greek nine in Latin dress totals "
    f"**{dress9_ord} in the ordinal — the exact total "
    f"the Latin essay computed for the Latin Nine "
    f"itself.** The two nines, Greek and Latin, weigh "
    f"the same in the ordinal bank under the stated "
    f"dresses; under Η's long dress (EI for E) the "
    f"total moves to 132, which also reduces to 6 — "
    f"the root is dress-stable, the total is not, and "
    f"the battery prints both. The second coordinate: "
    f"in Agrippa dress the nine total {dress9_agr}, "
    f"reducing to {digits(dress9_agr)} — **8, the "
    f"hybrids' own root**: the whole nine, carried "
    f"abroad into this tongue's old bank, lands where "
    f"its two hybrids land at home. The dresses' "
    f"partings stand in the battery entire (Η → E "
    f"5/5 against Η → EI 14/14, Δ9 in both banks; Υ → "
    f"V 22/200 against Υ → Y 25/400 and Υ → U "
    f"21/200; the long dresses Ō and Ē returned "
    f"silence in both banks — the long/short "
    f"distinction Greek carries in two letters cannot "
    f"be priced in Latin dress at all). [The "
    f"weighings ATTESTED as arithmetic on the stated "
    f"dresses; the coordinates DERIVED — the "
    f"battery's, carried at its tier.]")
add()
add("### VVII — the key-string taken apart in this tongue")
add()
add("The founder's third candidate key (2026-11-24 "
    "18:17 EST, verbatim: *\"Its the double vs and "
    "the Is? Wvii?\"* — the key built of the double "
    "Vs and the Is) is a Latin string, and this "
    "tongue's instruments take it apart entire. Its "
    "anatomy is letter-exact: **VV + II** — VV the "
    "refused hybrid of the annex, promoted to X "
    "there; II the lawful double, 2 there. In the "
    "letter banks it prices otherwise, and the "
    "battery weighed both prices as the key's "
    f"evidence: ordinal **{vvii[0]}**, reducing to "
    f"{digits(vvii[0])} — 8, the fold's number; "
    f"Agrippa **{vvii[1]}**, running 418 → 13 → "
    f"{digits(vvii[1])} — through the 13-gate to 4, "
    "the cross's own count. In the annex's older "
    f"arithmetic the same glyphs parse as a numeral: "
    f"**VVII = {vvii_parse}** (V + VII, read "
    "additively by the instrument), while WVII — "
    "the founder's spelling with W written whole — "
    "the Roman instrument refuses outright: W is "
    "not a numeral letter, *not a numeral*. And in "
    "Hebrew the two spellings collapse to one word "
    "(וויי = 32, Δ0 — Plate II, §V). The battery's "
    "grading stands: of the three candidate keys, "
    "VVII touches the hybrids' coordinates at the "
    "most seats in its home tongue. The key's "
    "specification itself stands open in the "
    "seating instrument, for the founder's pen; "
    "this plate prints the anatomy and the prices, "
    "and specifies nothing.")
add()
add("### The VALUE-mark at Υ's seat, and what this "
    "tongue cannot witness")
add()
add("One of the seating's riding marks is this "
    "tongue's own: **Υ's VALUE-mark** — upsilon in "
    "its Y dress weighs **400 in Agrippa, its own "
    "Greek price** (§II, the Agrippa table). The "
    "battery's sentence stands: *the Latin bank's "
    "Greek-loan letter carries the vowel itself.* "
    "The seating seated Υ at Triad III with that "
    "mark riding; this plate is the mark's home "
    "bank, and it prints the coordinate at its "
    "seat. — What Latin cannot witness, printed at "
    "full size as the plate's boundary: the "
    "Archons' seats were earned on Greek evidence "
    "and drawn on Plate I; Latin's witness "
    "corroborates the *form* (a nine completed by "
    "hybrids, at its own totals), the *dress totals* "
    "(123 in the ordinal, the nine reducing to the "
    "hybrids' root in Agrippa), and the *key's "
    "anatomy* — and it assigns no seat, confirms no "
    "position, and names no Archon. The names stand "
    "open on Plate I, and this plate does not fill "
    "them.")

# ---------------------------------------------------------------------
# §VI — The audit.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_iv_latin.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced "
    "cell on this plate against the engine, without "
    "reading the plate's own figures: both banks letter "
    "by letter (26 ordinal keys, 25 Agrippa keys, and "
    "W's silence in Agrippa weighed); the run sums and "
    "bank totals; the seam in its three dresses and "
    "both banks; the Phoenician column recomputed from "
    "the map's file, heir by heir; the annex entire "
    "from pontifex.numerals — the doubles' statuses, "
    "promotions and joins, the triples, the six "
    "subtractives, the evaluator exhibits, "
    "parse('VVII'), and the module's own checks "
    "re-run; the §V figures (the pure five, the four "
    "hybrids, the six candidates with their Greek "
    "twins, the Latin Nine's totals, the nine dresses "
    "and their totals, VVII's two prices and "
    "reductions); every claim of §IV recomputed in "
    "its own bank (262, the English dress through "
    "latin_ordinal) against the register's claimed "
    "and recomputed; and the frame's priced cells — "
    "178 natives and 45 doors — re-weighed in both "
    "banks against THE-TWELVE-TABLES. It then "
    "reconciles the plate against its sources: all "
    "262 claim keys present, verdict and subseat "
    "counts equal to the register's, the thirty "
    "VERIFIED coordinates and the seven bridge "
    "annotations entire on the plate, the two empty "
    "registers printed as empty. The audit's verdict "
    "and cell count are printed in its filed output; "
    "a cell that does not reproduce fails the plate "
    "under §VII's tolerances. The font audit — every "
    "non-ASCII codepoint of this master against the "
    "Lex Stellarrvm family's cmaps — runs before the "
    "MAGVS build, under the font law: no glyph is "
    "silently dropped, and any unheld codepoint "
    "beyond the three named Ethiopic syllables aborts "
    "the build. The audit further checks the printed "
    "edition's text layer for the dress's entirety: "
    "no Hebrew-block or Arabic-block codepoint "
    "stands in it (the master's Hebrew runs are "
    "carried by the declared transliteration of the "
    "colophon; its Greek stands in the Serif member, "
    "as on Plate I).")

# ---------------------------------------------------------------------
# §VII — The four elements.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "LATIN_ORDINAL and AGRIPPA banks; pontifex/numerals.py "
    "and doubles.py (the annex and the joins); the "
    "Phoenician map's JSON (maps/phoenician-cypher-glyph-"
    "map/); THE-777-VERIFICATION-TABVLA's register as "
    "mapped in research/thirteen-plates/mapping_register"
    ".json; THE-TWELVE-TABLES §V.4 and its §II gap "
    "register (the latin entries); THE-DIVINE-NINE-"
    "ABROAD-I-LATIN (the Latin Nine, the six candidates, "
    "the seats and refusals); THE-ARCHON-BATTERY (Leg 2 "
    "the dresses; Leg 6 the Latin HIT; §VI.3 the key "
    "strings) and THE-SEATING-OF-THE-ARCHONS entire; the "
    "Nine Vowels essay (the seam; the Offset Law); "
    "PLATES I–III as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ "
    "773); every figure scripted from the engine or "
    "carried entire from an instrument of record; the "
    "tongue's bearing stated at the tiers its sources "
    "carry, the empty registers and the empty seat "
    "printed at full size; the independent audit of "
    "§VI.")
add("- **Outputs:** this plate — PLATE-IV-LATIN.md and "
    "its MAGVS PDF — fourth of the series PLATE-I-GREEK "
    "began; the generator and audit scripts filed in "
    "pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — "
    "if any priced cell is found not to reproduce from "
    "the engine or its register, the affected cell "
    "fails the Method of Science; if any passage seats "
    "what the seating did not earn, raises a tier, "
    "fills a hole (W's seat, the Archons' names), "
    "prices a sign a bank leaves silent, or overwrites "
    "the earlier map, it zeroes the founder's residual "
    "claim and fails the Aim of Religion. Within those "
    "edges it stands as built.")

# ---------------------------------------------------------------------
# §VIII — Questions for his pen.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none.** No question arose in "
    "this plate's building that its sources do not "
    "already carry: the W fence and the VV ruling stand "
    "resolved in the gap register, revisable by his pen "
    "as their faces state; LL's and DD's hybrid "
    "candidacy stands open in the annex's instrument, "
    "where the founder's pen is already named as its "
    "seat; the key's specification and the seating's "
    "open items stand in the seating instrument. A "
    "plate that invents questions to fill its section "
    "misprints its record; this section therefore "
    "stands as the record that none arose.")

# ---------------------------------------------------------------------
# Footnotes — the wells, from more than one tradition.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **Scripture, in this tongue's own dress.** John "
    "1:1 in the Vulgate, the Latin Bible of record: "
    "*\"In principio erat Verbum, et Verbum erat apud "
    "Deum, et Deus erat Verbum\"* — \"In the beginning "
    "was the Word.\" On the Latin plate the verse "
    "stands in the tongue this plate prices: the Word "
    "weighed in Latin letters is this plate's whole "
    "subject, and its first verse is about a word. "
    "[ATTESTED text; application DERIVED.]")
add("2. **Grammar.** The classical grammarians' "
    "standing note: in the classical stock, **I and V "
    "are each both vowel and consonant** — one sign, "
    "two offices, the distinction carried by position "
    "and sound, not by letter. The border letter of "
    "§II is therefore not the house's invention: the "
    "tradition itself seats V (and I) across the "
    "vowel/consonant line, and the founder's hybrid "
    "ruling at VV builds on the tradition's own "
    "border. [The note ATTESTED at this level; the "
    "ruling the founder's.]")
add("3. **The numeral tradition.** The Roman system "
    "of the annex has no zero sign; the medieval "
    "*nulla* — N, a word's initial — did a zero's "
    "work without being a numeral. The annex's "
    "instrument (pontifex/numerals.py) states its "
    "sources on its face: the values and the standard "
    "form as read in the standard references on Roman "
    "numerals, read 2026-11-24. A system of pure "
    "addition and promotion has no empty seat to "
    "price — which is why the founder's Zero Point "
    "had to be seated in Greek, on Plate I. [The "
    "system ATTESTED; the reading DERIVED.]")
add("4. **Law.** In the early printed law reports, "
    "u and v — and i and j — pass as one letter: the "
    "old books print them interchangeably, and a "
    "citation is read through the dress of its age. "
    "The seam of §II is the same figure in the "
    "gematria account: a distance that belongs to "
    "the spelling, not the word — and in Agrippa, "
    "where the two letters keep one seat, the "
    "distance vanishes, as in the old reports it "
    "was never counted. Beside it, the register's "
    "own law, carried from Plate III: every claim "
    "is judged against the bank it names (the "
    "principle the law states for instruments "
    "generally — a writing is read by its own "
    "terms; Black's Law Dictionary, *construction*). "
    "[The printing practice ATTESTED; the parallels "
    "DERIVED.]")
add("5. **The proverb.** *Verba volant, scripta "
    "manent* — spoken words fly away; written "
    "things remain. The plate is the proverb's "
    "workshop: 262 claims survive to be re-weighed "
    "because they were written, and every figure on "
    "this plate stands or falls by reproduction "
    "from the written banks. [The proverb ATTESTED "
    "as a Latin proverb; the application DERIVED.]")
add("6. **The desk's apparatus.** This plate's "
    "Latin inscriptions are rendered in classical "
    "dress — V for U, VV for W — under the founder's "
    "inscriptional rule (infrastructure and Latin "
    "only; ordinary body prose is never respelled), "
    "and the seam that dress opens is measured at "
    "§II rather than hidden by it. In the printed "
    "MAGVS edition, the master's Hebrew runs are "
    "carried by transliteration under Plate II's "
    "declared scheme — the toolchain does not shape "
    "right-to-left scripts honestly — and its Greek "
    "by the family's Serif member, as on Plate I: "
    "marked substitutions, declared in the "
    "colophon, never silent ones.")

# ---------------------------------------------------------------------
# Table of Authorities + colophon.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); banks "
    "LATIN_ORDINAL and AGRIPPA in pontifex/tables.py) — "
    "calibration controls θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773 read true at build.")
add("- pontifex/numerals.py — the Roman doubles annex: "
    "the seven givens, the law, DOUBLES / TRIPLES / "
    "SUBTRACTIVES computed, numerals_checks() green at "
    "build; the founder's hybrid ruling and his ground "
    "as the module records them.")
add("- pontifex/doubles.py — the Latin doubles map (the "
    "joins page: VV 44/400, UU == VV in Agrippa).")
add("- PHOENICIAN-CYPHER-GLYPH-MAP (maps/phoenician-"
    "cypher-glyph-map.json) — the 22 rows and their "
    "Latin heirs; the column total 243 = 3⁵, recomputed "
    "at build; the totals as stated in VESTIGATOR-"
    "TABVLA (Greek 1,095 · Latin 243 · Arabic 1,495).")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its Latin face 262 claims (262/0/0), "
    "its bank counts ordinal 167/167 · Agrippa 86/86.")
add("- research/thirteen-plates/mapping_register.json — "
    "the mapping of the register into the plates, claim "
    "by claim; the Latin plate's three subseats "
    "(167/86/9).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate IV is the prior "
    "instrument.")
add("- THE-TWELVE-TABLES — §V.4 the Latin frame, census "
    "and priced cells; §II the latin bank's gap "
    "register (two entries: W FENCED; VV RULING).")
add("- THE-DIVINE-NINE-ABROAD-I-LATIN — the Latin Nine: "
    "the six candidates weighed (§III there), the "
    "seats and refusals (§IV), the totals 123/549, "
    "the identity fence.")
add("- THE-ARCHON-BATTERY (656d667) — the evidence run: "
    "Leg 2 the Trinity weighing and the dresses (the "
    "123 identity; the Agrippa 584 → 8); Leg 6 the "
    "sweep's Latin (the HIT; V the border mark); §VI "
    "the key strings (VVII's prices).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to; Υ's "
    "VALUE-mark.")
add("- THE-NINE-VOWELS-ESSAY-AND-AUDIT §VI — the "
    "Offset Law and the QVANTVM seam (108/107; Agrippa "
    "641 = 641).")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16) and PLATE-III-ARABIC (5f0b4bd) — the "
    "pattern this plate follows.")
add("- Vulgate, John 1:1. The classical grammarians on "
    "I and V. The Roman-numeral references as cited "
    "in pontifex/numerals.py. Black's Law Dictionary, "
    "*construction*. The proverb *scripta manent*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate IV of the founder's "
    "series commission of the same day, the gate of "
    "the Archons' certainty met by the seating of "
    "record (0760c8a), following the pattern of "
    "Plates I–III (196025e · 1389c16 · 5f0b4bd). Every "
    "figure scripted from the engine or carried "
    "entire from its instrument; the earlier map "
    "marked prior, never overwritten; the holes "
    "printed at the size of the seats — on this "
    "plate, W's empty Agrippa seat and the two empty "
    "verdict registers; the register's perfection "
    "printed with its bound. In the MAGVS edition "
    "the master's Hebrew runs are carried by the "
    "declared transliteration of Plate II's scheme; "
    "this master keeps the scripts themselves. "
    "Authorship attributed exclusively to Johnathan "
    "'Qasparr' Monroe (Greek, -ARR, All Rights "
    "Reserved, Without Prejudice).")
add()
add("Method of Science. Aim of Religion.")
add()
add("**Flagpole of Claim and Coinage: Johnathan 'Qasparr' "
    "Monroe, ARR, All Rights Reserved, Without Prejudice. "
    "Right of claim hereby reserved and coined under the "
    "authority of the Living Man.**")
add()
add("93 — Live, Love, and let Love, Live.")

OUTPUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"built {OUTPUT} — {len(L)} lines, "
      f"{OUTPUT.stat().st_size} bytes")
print(f"claims: {len(claims)} in {len(sections)} sections; "
      f"verdicts {verdicts}; subseats {subseats}; "
      f"natives {len(natives)}; doors {len(doors)}; "
      f"bridges {len(bridges)}; verified coords "
      f"{len(verified_coords)}")
