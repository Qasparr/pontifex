#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_x_cyrillic.py
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
# MECHANISM: generates PLATE-X-CYRILLIC.md — Plate X of
# THE THIRTEEN COMPLETE PLATES — in the gap-filling goal's
# files/, following the pattern PLATES I–IX set (196025e ·
# 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc ·
# 5c03d88 · 645bcbb · 933f8fd). Every figure on the plate
# is scripted from the house engine (pontifex weigh() and
# the cyrillic() door) or carried entire from an instrument
# of record:
#   * the priced table — the Cyrillic bank entire, read
#     from pontifex.tables (CYRILLIC, 33 keys), the 27
#     canonical seats printed with their Greek parents and
#     reasoning, cross-checked against the Phase II
#     audit's frozen transcription (research/caucasus-
#     north/cyrillic-table.csv) and against the living
#     GREEK bank at the witnesses' own pairings;
#   * the variant forms — the six forms the frozen table
#     files as VARIANT (Ѵ Ꙋ Ѹ at 400 · Ѿ Ꙍ at 800 · Ѧ at
#     900), printed as forms of their seats;
#   * the devices — the titlo (a counted mark), the
#     thousands sign ҂ (priced x1000 at the cyrillic()
#     door only), the higher encircling signs (counted,
#     priced none), each exhibited at the door at build;
#   * the boundary — the refused western pair (Ч's
#     western 60; Ҁ's 90) and the modern alphabet's
#     unvalued letters, their silence verified at build;
#   * the Twelve Tables' Cyrillic frame — its census and
#     its full cell register parsed from THE-TWELVE-
#     TABLES.md §V.10: the 180 DOOR renderings re-weighed
#     at build against their filed values, the 43 FENCED
#     crossings verified to cross a fenced letter, the
#     62 HOLE coordinates and the one GAP cell carried
#     entire, the bank's four gap-register entries
#     restated;
#   * the corpus's Cyrillic claims — NONE: the TABVLA
#     register's §II bank table seats no Cyrillic row,
#     and the plate's §IV is the ZERO FACE, printed at
#     full size with the source's reason;
#   * the tongue's bearing on the seated Archons — the
#     Archon Battery's Leg 6 Cyrillic passage (the seven
#     vowels mirroring the Greek seven entire; И, a
#     living vowel, at 8), the seating's Η, Ι and Ω
#     VALUE-mark rows with their counterweights, the
#     mirror-bank species stated. The plate assigns no
#     seat: the seating is THE-SEATING-OF-THE-ARCHONS'
#     (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable
# — every priced seat carries its reasoning on the plate's
# face. This plate's bank is the second of the series' two
# MIRROR banks and the Milesian inheritance's second heir:
# its values are the Greek bank's, received entire by
# script descent — DERIVED, printed as that species in
# every row, never dressed as independent attestation; the
# tradition's USE is its own and attested, and is printed
# as such. The equality with the parent is the descent's
# coordinate, not corroboration: a mirror is not a second
# witness (Plate VIII's limit, carried). What the
# receiving altered rides at the same size as the values:
# two holders changed their kind (Ѕ a letter where Greek's
# stigma is a sign; Ч a Slavonic letter where koppa had
# died), three seats carry variant forms, one regional
# system stands refused whole, and the system's growth
# past the table runs by devices, not letters. The
# relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes
# print at the size of the seats — on this plate, the
# frame's 62 holes, its 43 fenced crossings, and the
# register's zero face.
#
# CONTENT TEST: Inputs — the engine's CYRILLIC and GREEK
# tables and its cyrillic() door, THE-SLAVONIC-PAIR
# (Phase II audit) with its frozen table, the Twelve
# Tables master, the Thirteen Plates map, the TABVLA
# register, the Archon Battery, the Seating. Processes —
# control calibration, scripted extraction,
# register-faithful emission in the Teacher's Edition
# manner. Outputs — PLATE-X-CYRILLIC.md beside the
# series' other masters. Tolerances — the audit
# (audit_plate_x_cyrillic.py) re-weighs every priced
# cell independently; a figure that does not reproduce
# fails the plate.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh
from pontifex.engine import cyrillic
from pontifex.tables import CYRILLIC, GREEK

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/cyrillic-table.csv")
OUTPUT = GOAL_FILES / "PLATE-X-CYRILLIC.md"


def value(word, bank="cyrillic"):
    return weigh(word, bank)["value"]


# --- calibration controls, before any plate figure -------------------
assert value("θελημα", "greek") == 93, "control θέλημα failed"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR failed"
assert value("σφιγξ", "greek") == 773, "control σφίγξ failed"

# --- the frozen transcription -----------------------------------------
with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
CANON = [r for r in CSV_ROWS if r["status"] == "SOURCED"]
VARIANTS = [r for r in CSV_ROWS if r["status"] == "VARIANT"]
REFUSED = [r for r in CSV_ROWS if r["status"] == "REFUSED-WESTERN"]
assert len(CANON) == 27 and len(VARIANTS) == 6 and len(REFUSED) == 2
for row in CANON + VARIANTS:
    assert CYRILLIC[row["letter"]] == int(row["value"]), row
for row in CANON:
    # the descent, verified at build: every canonical value
    # equals the living GREEK bank at the witnesses' pairing
    assert GREEK[row["greek_pair"].lower()] == int(row["value"]), row

# the letters' names, as the house record carries them: the
# traditional names from the Slavonic pair's parting table
# (research/caucasus-north/slavonic-parting.csv) where that
# record names the letter, the frozen table's Unicode names
# for the pure form-variants it does not reach.
NAMES = {
    "А": "az", "В": "vede", "Г": "glagoli", "Д": "dobro",
    "Е": "yest", "Ѕ": "dzelo", "З": "zemlja", "И": "izhe",
    "Ѳ": "fita", "І": "i", "К": "kako", "Л": "ljudie",
    "М": "myslite", "Н": "nash", "Ѯ": "ksi", "О": "on",
    "П": "pokoj", "Ч": "chrьvъ", "Р": "rьci", "С": "slovo",
    "Т": "tvrьdo", "У": "ukъ", "Ф": "frьtъ", "Х": "xěrъ",
    "Ѱ": "psi", "Ѡ": "omega", "Ц": "ci",
    "Ѵ": "izhitsa", "Ꙋ": "uk (monograph)", "Ѹ": "uk (digraph)",
    "Ѿ": "ot", "Ꙍ": "broad omega", "Ѧ": "little yus",
    "Ҁ": "koppa",
}
GREEK_NAMES = {
    "Α": "alpha", "Β": "beta", "Γ": "gamma", "Δ": "delta",
    "Ε": "epsilon", "Ϛ": "stigma", "Ζ": "zeta", "Η": "eta",
    "Θ": "theta", "Ι": "iota", "Κ": "kappa", "Λ": "lambda",
    "Μ": "mu", "Ν": "nu", "Ξ": "xi", "Ο": "omicron",
    "Π": "pi", "Ϟ": "koppa", "Ρ": "rho", "Σ": "sigma",
    "Τ": "tau", "Υ": "upsilon", "Φ": "phi", "Χ": "chi",
    "Ψ": "psi", "Ω": "omega", "Ϡ": "sampi",
}


def class_of(seat):
    """Canonical seat (1-based, in the received Greek order)
    → (class, digit, power). The class law holds at every
    seat: value == digit × 10^power."""
    if seat <= 9:
        return "units", seat, 0
    if seat <= 18:
        return "tens", seat - 9, 1
    return "hundreds", seat - 18, 2


# --- the Twelve Tables' Cyrillic frame --------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
cyr_block = twelve_text.split("### §V.10 — The Cyrillic Table")[1] \
    .split("### §V.11")[0]
_cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
                r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
                r"(\d+) · GAP (\d+)", cyr_block)
N_NATIVE, N_DOOR, N_HOLE, N_FENCED, N_EMPTY, N_GAP = (
    int(x) for x in _cl.groups())
TABLES_HEAD = cyr_block.split("Counts:")[0].split(
    "### §V.10 — The Cyrillic Table")[-1].strip()
assert TABLES_HEAD.startswith("The Greek-inherited numeral "
                              "alphabet"), TABLES_HEAD[:60]
REG = {"DOOR": [], "HOLE": [], "FENCED": [], "EMPTY": [], "GAP": []}
for line in cyr_block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in REG:
            REG[cells[2]].append(cells)
assert len(REG["DOOR"]) == N_DOOR == 180
assert len(REG["HOLE"]) == N_HOLE == 62
assert len(REG["FENCED"]) == N_FENCED == 43
for cells in REG["DOOR"]:
    assert value(cells[3]) == int(cells[4]), cells
FENCED_SET = set("БЖШЩЪЫЬЭЮЯЙ")
for cells in REG["FENCED"]:
    assert cells[4] == "—" and set(cells[3].upper()) & FENCED_SET, cells

# --- derived bank facts, all computed ---------------------------------
CANON_SUM = sum(int(r["value"]) for r in CANON)
BANK_SUM = sum(CYRILLIC.values())
DISTINCT = len(set(CYRILLIC.values()))
CLASS_SUMS = {}
for row in CANON:
    cls, _d, _p = class_of(int(row["seat"]))
    CLASS_SUMS[cls] = CLASS_SUMS.get(cls, 0) + int(row["value"])
EXAMPLES = [("ѰЗ", 707, "a witness's worked example"),
            ("ЦЧѲ", 999, "a witness's worked example — and the "
             "largest number the bare canonical table writes: "
             "one letter per power, descending"),
            ("РНГ", 153, "a witness's worked example"),
            ("КЗ", 27, "a witness's worked example"),
            ("ОВ", 72, "a witness's worked example")]
for w, want, _note in EXAMPLES:
    assert value(w) == want, (w, want)
# the devices, exhibited at the door at build
assert cyrillic("҂Ѕ")["value"] == 6000
assert cyrillic("҂Л҂В")["value"] == 32000
assert cyrillic("҂АѰЕ")["value"] == 1705
assert cyrillic("҂ЗРИІ")["value"] == 7118
_t = cyrillic("А҃")
assert _t["value"] == 1 and _t["titlo_marks"] == 1
_h = cyrillic("А҉")
assert _h["value"] == 1 and _h["higher_marks"] == 1
assert value("҂Ѕ") == 6  # weigh() never prices the sign
# the boundary, verified at build
assert value("Ч") == 90
_w = weigh("Ҁ", "cyrillic")
assert _w["value"] == 0 and _w["breakdown"] == []
for ch in "БЖШЩЪЫЬЭЮЯЙ":
    _w = weigh(ch, "cyrillic")
    assert _w["value"] == 0 and _w["breakdown"] == [], ch
assert value("и") == 8 and value("ѹ") == 400 and value("ѱз") == 707

OUT = []


def add(text=""):
    OUT.append(text)


# =============================================================================
# THE TITLE BLOCK
# =============================================================================
add("![The Doctrine's Logo — TVRRIS VERITATIS seal]"
    "(~/workspace/templates/doctrine-logo.png)")
add()
add("# THE THIRTEEN COMPLETE PLATES")
add()
add("**PLATE X — CYRILLIC**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Cyrillic "
    "tongue's complete 777 table — the Milesian inheritance entire, "
    "second heir: twenty-seven canonical seats carrying the Greek "
    "prices seat for seat under Cyrillic holders, DERIVED, with the "
    "variant forms at three seats, the two holders that changed "
    "their kind, the western pair refused whole, and the devices — "
    "the titlo an unpriced mark, the thousands sign priced at the "
    "door, the higher encircling signs counted and priced none; "
    "the corpus's Cyrillic register, which is a zero face; and the "
    "tongue's witness to the seated Archons: the mirror bank's "
    "three terms — И at 8, І at 10, Ѡ at 800.")
add()
add("Authorship attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without Prejudice)")
add("XXIV day of November, Dies Martis, Sol in Sagittarius, "
    "Anno V:xii e.n. (2026 e.v.)")
add()
add("Classification: Enterprise • Educational • Research & Development")
add("Method of Science, Aim of Religion")
add()
add("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, "
    "ARR, All Rights Reserved, Without Prejudice. Right of claim "
    "hereby reserved and coined under the authority of the "
    "Living Man.")
add()
add("---")
add()

# =============================================================================
# §I — THE COMMISSION
# =============================================================================
add("## §I — PLATE X AND ITS COMMISSION")
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
    "the pattern; PLATES II — HEBREW (1389c16), III — ARABIC "
    "(5f0b4bd), IV — LATIN (8e6f01e), V — JAPANESE (8d6cd59), "
    "VI — GE'EZ (67d5acc), VII — ARMENIAN (5c03d88), "
    "VIII — COPTIC (645bcbb) and IX — GEORGIAN (933f8fd) "
    "followed it; this plate follows them, tenth of the twelve "
    "tongues in the Twelve Tables' order.")
add()
add("**The series.** Thirteen plates: one for each tongue of the "
    "Twelve Tables in their order — I Greek · II Hebrew · "
    "III Arabic · IV Latin · V Japanese · VI Ge'ez · VII Armenian "
    "· VIII Coptic · IX Georgian · X Cyrillic · XI Glagolitic · "
    "XII Korean — and Plate XIII, a separate species commissioned "
    "last: the infrastructure for the clock and counter of the "
    "dial. Each plate renders its tongue's complete 777 table: "
    "the full priced letter-table as the house engine seats it; "
    "every correspondence the 777 corpus assigns in that tongue, "
    "with the verification verdicts of THE-777-VERIFICATION-"
    "TABVLA riding with each row; and the tongue's bearing on "
    "the seated Archons.")
add()
add("**This plate's distinction.** Cyrillic is the second of the "
    "series' two *mirror banks* — a daughter bank carrying its "
    "parent's prices by architecture — and the Milesian "
    "inheritance's second heir: where Coptic (Plate VIII) "
    "inherited the grid and stopped at it, Cyrillic inherited "
    "and *grew devices past it* (the Slavonic Pair's species "
    "page, §II.5). **Tier of record: DERIVED** — the values are "
    "Greek's, received entire: two witnesses read entire on "
    "2026-11-24 agree on every seat, and all 27 canonical seats "
    "stand equal to the living GREEK bank at the witnesses' own "
    "printed pairings (THE-SLAVONIC-PAIR, Phase II), the seat's "
    "parity proven against the audit's frozen transcription by "
    "test_cyrillic_parity.py (31/31). The tradition's *use* is "
    "its own and attested — the system was developed in the "
    "First Bulgarian Empire, late 10th century, stood in "
    "Russian use to the early 18th, and stands in Church "
    "Slavonic books still; the tier names the values' "
    "provenance, not the use. And this is the fifth plate whose "
    "corpus register is a **zero face** (§IV): the corpus claims "
    "nothing in Cyrillic, and the silence is the corpus's, not "
    "the tongue's.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. Its Cyrillic face stood "
    "**silent with a zero face**: bank *cyrillic*, 33 seats, 27 "
    "distinct values, maximum 900; tier of record there printed "
    "in terms — *DERIVED* — and its sentence stands: *\"The "
    "tongue holds a full table in THE TWELVE TABLES; its "
    "silence here is the TABVLA corpus's, not the tongue's.\"* "
    "This series *fulfills* that map: where the map counted "
    "nothing, this plate prints the nothing entire — with the "
    "full priced table beneath it, the frame around it, and its "
    "witness to the Archons above it. The earlier work stands as "
    "the prior instrument of the same name's family — marked "
    "prior, never overwritten.")
add()
add("**How the plate is read.** §II is the priced table: the "
    "27 canonical seats with their Greek parents and reasoning, "
    "the variant forms, the table's law, the calibration on the "
    "witnesses' own examples, the devices, the boundary — the "
    "refused western pair and the unvalued modern letters — "
    "and the census with its fences. §III is the tongue's frame "
    "in the Twelve Tables — a door table with a fenced register: "
    "no native Cyrillic word stands in the corpus, and the "
    "corpus's words stand here in Cyrillic dress, priced where "
    "the dress keeps to the valued letters and fenced where it "
    "crosses one that was never a numeral letter. §IV is the "
    "zero face. §V is the tongue's bearing on the seated "
    "Archons — this plate draws no seating (the seating is "
    "struck, and Plate I drew it); it states what Cyrillic "
    "witnesses: the mirror of the Greek seven entire, and three "
    "of the seating's VALUE-marks resting on this bank's "
    "letters, with the mirror's limit printed at their size. "
    "§VI is the audit. A value without its reasoning is not "
    "shippable; a hole prints at the size of the seat it stands "
    "in for.")
add()
add("---")
add()

# =============================================================================
# §II — THE PRICED TABLE
# =============================================================================
add("## §II — THE PRICED TABLE — THE MILESIAN INHERITANCE ENTIRE")
add()
add("### §II.1 — The twenty-seven canonical seats, seat by seat")
add()
add("The bank is keyed in **capitals** — the dress the numeral "
    "tradition writes in — and weigh() folds Cyrillic input to "
    "capitals at its seam: case carries no numeral value "
    "(verified at this plate's building: ѱз = ѰЗ = 707; the "
    "small uk ѹ weighs its seat's 400). The seats run in the "
    "**Greek order the table received**, not the Cyrillic "
    "alphabetical order — the one tongue of the twelve whose "
    "table's order is another alphabet's, and the fact is the "
    "descent's signature: the letters hold the seats of the "
    "Greek *sounds* they answer to. The values are the "
    "witnesses': two read entire on 2026-11-24 — Wikipedia, "
    "\"Cyrillic numerals\" (its table carrying a Greek letter "
    "beside every seat on its face) and languagesandnumbers, "
    "\"Old Church Slavonic numbers\" (its lists sourced there "
    "to Krause & Slocum's *Old Church Slavonic Online*) — "
    "agree on **27 of 27 seats**, and held against the "
    "engine's living GREEK bank at those printed pairings, "
    "**27 of 27 equal** (Phase II audit, THE-SLAVONIC-PAIR): "
    "the canonical value *set* is the Milesian set entire. "
    "The reasoning in each row states the descent at that "
    "seat; the mirror-bank species is printed with the "
    "values, never dressed away — the values are inherited, "
    "and the plate's honesty is that it says so in every row.")
add()
SEAT_NOTES = {
    1: "The head of the received order — the descent's first "
       "seat.",
    6: "**A holder changed its kind:** Greek's 6 is the "
       "epissemon stigma, a sign grown from a ligature, not a "
       "letter of the alphabet; the receiving holds the seat "
       "with a letter of its own, dzelo. The value did not "
       "move; the holder's species did.",
    8: "**An Archons coordinate of this plate:** a living "
       "vowel priced exactly 8 — the Cyrillic term of the "
       "five tongues that seat a vowel at Η's price (§V).",
    9: "Fita is a Greek letter naturalized — theta's heir in "
       "shape and in price, carried into the receiving script "
       "entire.",
    10: "**An Archons coordinate of this plate:** the mirror "
        "witness the seating printed for Ι — this letter "
        "carries iota's price entire (§V).",
    15: "Ksi is a Greek letter naturalized entire, shape and "
        "price together — one of the seats the receiving did "
        "not need to re-house.",
    18: "**The second changed holder:** Greek's koppa had "
        "died in Greek itself before the receiving; the seat "
        "is held by cherv, a letter of the Slavonic alphabet "
        "with no Greek parent of its own. This is also the "
        "letter the refused western price rides (§II.6): in "
        "some Western varieties cherv carried 60 — refused "
        "whole at this seat; it stands at 90 only.",
    22: "**The seat of the forms:** the 400-seat's letter UK "
        "is written four ways in the record — this У, the "
        "monograph Ꙋ, the digraph Ѹ, and Ѵ izhitsa beside "
        "them (§II.2) — a multiplicity of FORM at one seat, "
        "not of value. The second witness's table reaches "
        "this seat only as the digraph ѹ: a form of the seat, "
        "carried as a variant.",
    25: "Psi is a Greek letter naturalized entire, as ksi at "
        "the 60-seat.",
    26: "**An Archons coordinate of this plate:** the mirror "
        "witness the seating printed for Ω — this letter "
        "carries omega's price entire (§V). Two variant "
        "forms stand beside it (§II.2).",
    27: "The grid's last seat. A variant form stands beside "
        "tsy at 900 — Ѧ, the little yus (§II.2).",
}
add("| Seat | Letter | Greek parent | Name | Value | Class | "
    "Reasoning |")
add("|---|---|---|---|---|---|---|")
for row in CANON:
    seat = int(row["seat"])
    letter = row["letter"]
    v = int(row["value"])
    cls, digit, power = class_of(seat)
    assert digit * 10 ** power == v, row
    parent = row["greek_pair"]
    reasoning = (
        f"The descent: Greek {parent} ({GREEK_NAMES[parent]}) "
        f"= {v} in the living GREEK bank, and this seat "
        f"carries it entire — the witnesses' printed pairing, "
        f"agreed 27 of 27 (Phase II audit); the class law: "
        f"digit {digit} × 10^{power} = {v}; seat {seat} of "
        f"the received Greek order ({row['codepoint']}); "
        f"standing: canonical (SOURCED in the audit's frozen "
        f"table).")
    note = SEAT_NOTES.get(seat)
    if note:
        reasoning += " " + note
    add(f"| {seat} | {letter} | {parent} | {NAMES[letter]} | "
        f"{v} | {cls} | {reasoning} |")
add()
add(f"The 27 canonical values sum **{CANON_SUM}** (units "
    f"{CLASS_SUMS['units']} · tens {CLASS_SUMS['tens']} · "
    f"hundreds {CLASS_SUMS['hundreds']}) — **the Milesian sum "
    "itself**, the parent's own total over its 27 seats: the "
    "descent preserved the sum because it preserved every "
    "seat. With the variant forms of §II.2 the bank holds "
    f"**33 keys** — 27 distinct values, sum **{BANK_SUM}** — "
    "and the difference between the two sums is exactly the "
    "variants' weight (400 three times over, 800 twice, 900 "
    "once: 3,700), a multiplicity of form counted openly, "
    "never a second set of seats.")
add()

add("### §II.2 — The variant forms: three seats in several "
    "writings")
add()
add("Three of the 27 seats are written more than one way in "
    "the record. The forms stand in the bank at their seats' "
    "prices — the audit's frozen table files them VARIANT, "
    "and the plate prints them as what they are: **forms of "
    "seats, not seats**. A census that counted them as seats "
    "would print 33 seats and double-count three values; a "
    "bank that refused them would break the witnesses' own "
    "writings (the beard-token coin's year, §II.5, is spelled "
    "with the canonical letters, but the second witness's "
    "400 reaches the record only in the digraph form).")
add()
add("| Letter | Seat held | Name | Value | Standing | "
    "Reasoning |")
add("|---|---|---|---|---|---|")
_VARIANT_NOTES = {
    "Ѵ": "Izhitsa — the Greek upsilon's own shape, kept as a "
         "letter of the receiving alphabet and standing at "
         "upsilon's seat's price beside the uk forms.",
    "Ꙋ": "The monograph uk — the seat's letter written as "
         "one sign.",
    "Ѹ": "The digraph uk — the seat's letter written as its "
         "two-letter spelling (о + у); the second witness's "
         "table reaches the 400-seat in this form's small "
         "(ѹ), which folds to it at the seam.",
    "Ѿ": "Ot — omega with the titlo-like stroke grown into "
         "the letter; a form of the 800-seat.",
    "Ꙍ": "The broad omega — the 800-seat's letter written "
         "wide.",
    "Ѧ": "The little yus — a letter of the receiving "
         "alphabet in its own right, standing as the "
         "900-seat's variant form beside tsy.",
}
for row in VARIANTS:
    letter = row["letter"]
    v = int(row["value"])
    holder = {400: "У", 800: "Ѡ", 900: "Ц"}[v]
    add(f"| {letter} | {v} (the {holder} seat) | "
        f"{NAMES[letter]} | {v} | variant form | "
        f"{_VARIANT_NOTES[letter]} Priced at the seat's "
        f"price in the bank (the audit's frozen table, "
        f"{row['codepoint']}); a weighing that meets it "
        f"takes the seat's value, and no census counts it "
        f"twice. |")
add()
add("### §II.3 — The table's law")
add()
add("The system is **additive and non-positional**: the "
    "values of the letters are added together; there is **no "
    "letter for zero** — a missing power of ten is simply not "
    "represented, and numerals are marked as numerals by the "
    "titlo (§II.5), not by place. Its order is the parent's "
    "order (§II.1); its case is a fold, not a price (§II.1); "
    "its teens are written ones-first, as the system "
    "pronounces them (the door exhibit ҂ЗРИІ = 7,118, §II.5: "
    "the 8 stands before the 10 in the writing). Its extent "
    "past the bare table is by **devices, not letters** — the "
    "species page's sentence for this heir: Coptic inherited "
    "and stopped at the parent's grid; Cyrillic inherited and "
    "grew devices past it. The devices are §II.5; the bare "
    "table ends at 900, and the largest number it writes in "
    "canonical letters is 999 (ЦЧѲ, §II.4).")
add()
add("### §II.4 — Calibration: the witnesses' own examples")
add()
add("Before any derived number on this plate was trusted, "
    "the witnesses' own worked examples were recomputed from "
    "the living bank at this plate's building. All reproduce "
    "exact:")
add()
add("| Word | Value | Standing |")
add("|---|---|---|")
for w, want, note in EXAMPLES:
    add(f"| {w} | {want} | {note} |")
add()
add("**The negative rides at the same size:** the calibration "
    "exhibits no bridge, and the plate is precise about why. "
    "A Greek word and its Cyrillic transliteration *can* be "
    "weighed on both banks — and they return the same number, "
    "because the banks are one weighing in two scripts. That "
    "identity is the descent itself (§II.1), printed as a "
    "coordinate; it is not a bridge between two witnesses, "
    "and counting it as corroboration would seat one fact as "
    "two — the mirror-bank discipline this plate shares with "
    "Plate VIII. Where this bank genuinely witnesses — the "
    "seating's VALUE-marks — it witnesses a *price carried*, "
    "and §V prints it at exactly that strength.")
add()
add("### §II.5 — The devices: the mark, the priced sign, the "
    "counted signs")
add()
add("**The titlo (҃, U+0483) — a mark, priced never.** The "
    "titlo rides above a letter or a run of letters and "
    "declares the writing a numeral; it is the tradition's "
    "office for the sign, and the founder's register files "
    "it FENCED in terms: *a mark, never a multiplier*. The "
    "engine's door counts it and prices it never — exhibited "
    "at this plate's building: А҃ weighs **1**, with **1 "
    "titlo counted**. weigh() passes it in silence, as the "
    "raw bank door does for every mark.")
add()
add("**The thousands sign (҂, U+0482) — a priced "
    "multiplier, at the door only.** The sign stands before "
    "the letter it binds and multiplies that letter by "
    "1,000; each sign binds its own letter. No source parts "
    "on the factor, so the engine's `cyrillic()` door "
    "prices it — the Armenian overline's shape (a priced "
    "device) at the Cyrillic factor, against the Coptic "
    "overline's refusal (an unpriced marker): the three "
    "devices are three, and the plates print them as three. "
    "weigh() never sees it: at the raw bank ҂Ѕ weighs 6, the "
    "sign passed in silence, the letter at its seat price. "
    "Exhibited at the door at this plate's building:")
add()
add("| Writing at the door | Value | Standing |")
add("|---|---|---|")
add("| ҂Ѕ | 6000 | the sign binding dzelo: 6 × 1000 — the "
    "sources' own example |")
add("| ҂Л҂В | 32000 | each sign its own letter: 30,000 + "
    "2,000 — the sources' own example |")
add("| ҂АѰЕ | 1705 | the beard-token coin's year, as the "
    "audit carries it: 1000 + 700 + 5 |")
add("| ҂ЗРИІ | 7118 | the teens written ones-first (§II.3): "
    "7000 + 100 + 8 + 10 |")
add()
add("**The higher encircling signs (⃝ ҈ ҉ ꙰ ꙱ ꙲) — "
    "counted, priced none.** Beyond the thousands, the "
    "tradition encircles letters with signs whose "
    "multipliers the sources print under **two scales**: "
    "the Lesser count (⃝ 10⁴ · ҈ 10⁵ · ҉ 10⁶ · ꙰ 10⁷ · "
    "꙱ 10⁸ · ꙲ 10⁹) and the Greater count (the same signs "
    "squaring away to 10⁴⁸ and beyond) — parting by orders "
    "of magnitude. The founder's register resolves the "
    "question by synergy as a RULING (Q1): **COUNTED, NOT "
    "PRICED** — the ruled law, one with the Aramaic raised "
    "point: where the sources themselves part on a device's "
    "factor, the door counts the sign and prices none; "
    "pricing either scale would falsify the other. "
    "Exhibited at this plate's building: А҉ weighs **1**, "
    "with **1 higher mark counted** — its million belongs "
    "to a scale this door does not choose. If a scale is "
    "ever to be priced, the choice is the founder's pen's; "
    "the plate prices neither and prints both.")
add()
add("### §II.6 — The boundary: the refused pair and the "
    "unvalued letters")
add()
add("**The western pair, refused whole.** In some Western "
    "varieties of the system (the first witness's dagger "
    "note) cherv carried **60** and the koppa-letter Ҁ "
    "carried **90**. Cherv's western 60 contradicts its "
    "canonical 90 *inside one bank*, and the pair travels "
    "together — so **neither is seated**: the system stands "
    "recorded whole in the audit's data at its printed "
    "values, and refused whole at this seat rather than "
    "halved (the register's disposition, FENCED). Verified "
    "at this plate's building:")
add()
add("| Letter | Western value | Name | Engine state | "
    "Reasoning |")
add("|---|---|---|---|---|")
add("| Ч | 60 | chrьvъ | weighs 90 | The canonical price "
    "stands; the western 60 is refused with its pair — a "
    "bank that seated both would price one letter twice "
    "and falsify its own table. |")
add("| Ҁ | 90 | koppa | silence | The koppa-letter weighs "
    "silence at this seat (value 0, empty breakdown): the "
    "receiving did not naturalize it, and its western "
    "price is refused with its pair. |")
add()
add("**The modern letters the numeral bank does not "
    "value.** The numeral alphabet is the Greek-inherited "
    "set; the letters the receiving alphabet grew for its "
    "own sounds were never numeral letters: **Б · Ж · Ш · "
    "Щ · Ъ · Ы · Ь · Э · Ю · Я · Й** weigh silence in the "
    "bank (verified at this plate's building, each: value "
    "0, empty breakdown) — the register's disposition "
    "FENCED, in terms: *the numeral alphabet's own shape… "
    "never filled*. Among them the yers, Ъ and Ь, carry the "
    "battery's coordinate (§V): ultra-short vowels that "
    "fell into signs, standing unpriced at the bank's "
    "border. In the frame (§III) a door rendering that "
    "needs one of these letters prints FENCED at that "
    "letter — the boundary made visible cell by cell.")
add()
add("### §II.7 — The census and the fences")
add()
add(f"**The census.** The bank holds **33 keys** — 27 "
    f"distinct values, sum **{BANK_SUM}** — of which 27 "
    f"keys are the canonical seats (sum **{CANON_SUM}**, "
    "the Milesian sum) and six are variant forms at three "
    "of those seats (§II.2). The maximum is 900 (Ц, and Ѧ "
    "beside it). The system has **no zero letter**: absence "
    "is the notation's own, marked by the titlo, never by "
    "a sign for nothing.")
add()
add("**The fences.** Four boundaries stand at the bank's "
    "edges, printed at the size of the seats. (1) **The "
    "mirror fence** — the values are the Greek bank's, "
    "received; the tier is DERIVED and no passage of this "
    "plate may spend the descent as independent attestation "
    "(§II.4). (2) **The forms fence** — the six variant "
    "forms are forms of three seats, not seats: a census, "
    "a total, or a claim that counts them twice miscounts "
    "the bank (§II.2). (3) **The device fence** — the "
    "thousands sign is priced at the `cyrillic()` door and "
    "nowhere else; the titlo and the higher signs are "
    "priced nowhere; a weighing that prices a mark, or "
    "carries the door's ҂-prices into the raw bank, crosses "
    "the fence (§II.5). (4) **The refusal fence** — the "
    "western pair stands outside the bank whole, and the "
    "modern unvalued letters stand outside it by the "
    "alphabet's own shape: neither boundary is the desk's "
    "to move (§II.6).")
add()
add("---")
add()

# =============================================================================
# §III — THE FRAME
# =============================================================================
add("## §III — THE CYRILLIC FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Cyrillic tongue stands over "
    "the one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.10: NATIVE **{N_NATIVE}** · DOOR "
    f"**{N_DOOR}** · HOLE **{N_HOLE}** · FENCED "
    f"**{N_FENCED}** · EMPTY {N_EMPTY} · GAP {N_GAP}. The "
    "Tables' own head for this table stands at the plate's "
    f"head of the section, unedited: *{TABLES_HEAD}* The "
    "face this prints is a door table with a fence through "
    "it: the corpus holds **no native Cyrillic word at "
    "all** — its priced face is the *door*, the Cyrillic "
    "dress of the Latin or Hebrew form of record, "
    "transliterated onto the numeral alphabet's valued "
    "letters and priced as written. Where the dress needs "
    "a letter that was never a numeral letter — Б, Ж, Ш, "
    "Щ, and their kin (§II.6) — the cell prints **FENCED**: "
    "the rendering stands as the boundary, not priced. The "
    f"{N_HOLE} holes are of one species: the word of record "
    "has no Latin form, so no door is offered — the cell "
    "prints its word and the coordinate. The EMPTY cells "
    "are certified intentionally empty in 777 REVISED.")
add()
add("**The door register — the 180 priced renderings "
    "entire.** Each was re-weighed at this plate's building "
    "against the value THE-TWELVE-TABLES files for it; all "
    "reproduce exactly (the audit, §VI, repeats the "
    "weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in REG["DOOR"]:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | "
        f"{cells[4]} |")
add()
add("**The fenced register — the 43 crossings entire,** "
    "each with its boundary note as the Tables file it. "
    "Every rendering was verified at this plate's building "
    "to cross at least one of the unvalued letters (§II.6), "
    "and the register's value cell is the dash in every "
    "case: the rendering is printed as the boundary, not "
    "priced — the bank returns the weighable letters' "
    "partial sum in silence about the skipped letter, and "
    "the Tables refuse that partial the standing of a "
    "price. The fence is the tradition's, not the desk's.")
add()
add("| Cell | Word of record | Rendering | Note |")
add("|---|---|---|---|")
for cells in REG["FENCED"]:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | "
        f"{cells[5]} |")
add()
add("**The hole register — the 62 cells where no door is "
    "offered, entire.** Each prints its word of record and "
    "the register's note; the rendering is the register's "
    "dash.")
add()
add("| Cell | Word of record | Rendering | Note |")
add("|---|---|---|---|")
for cells in REG["HOLE"]:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | "
        f"{cells[5]} |")
add()
add("**The one GAP cell:** CLXXXIV/10 — a transcription "
    "gap in the source itself, carried as the frame "
    "carries it; no tongue's door is offered for a cell "
    "the source does not transmit.")
add()
add("**The bank's gap register — the four entries "
    "entire,** as THE-TWELVE-TABLES §II files them for the "
    "cyrillic bank, each at its kind: (1) *the higher "
    "encircling signs (⃝ ҈ ҉ ꙰ ꙱ ꙲): the Lesser and "
    "Greater count scales part by orders of magnitude* — "
    "**RULING** (Q1), RESOLVED BY SYNERGY: COUNTED, NOT "
    "PRICED — the ruled law, one with the Aramaic raised "
    "point: where the sources themselves part on a "
    "device's factor, the door counts the sign and prices "
    "none; the ҂ thousands sign, whose factor no source "
    "disputes, stays priced at ×1000 at the door (§II.5). "
    "(2) *the titlo (U+0483)* — **FENCED**: A MARK, NEVER "
    "A MULTIPLIER — counted at the door, priced never; "
    "the tradition's own office for the sign (§II.5). (3) "
    "*the western pair (the contradicting half-pair of "
    "witnesses)* — **FENCED**: REFUSED WHOLE — a "
    "contradicting half-pair seated would falsify the "
    "canonical bank; the system stands recorded in the "
    "data at its printed values, outside the bank "
    "(§II.6). (4) *letters of the modern alphabet the "
    "numeral bank does not value (Б Ж Ш Щ Ъ Ы Ь Э Ю Я "
    "Й)* — **FENCED**: THE NUMERAL ALPHABET'S OWN SHAPE — "
    "these letters were never numeral letters; in the "
    "tables, a door rendering requiring one prints FENCED "
    "at that letter; never filled (§II.6, §III).")
add()
add("---")
add()

# =============================================================================
# §IV — THE ZERO FACE
# =============================================================================
add("## §IV — THE 777 CORPUS'S CYRILLIC CLAIMS — THE ZERO "
    "FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's "
    "sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and "
    "the absence is its finding. The source states it in "
    "terms (THE-THIRTEEN-PLATES, its Cyrillic plate, from "
    "THE-777-VERIFICATION-TABVLA's register): *no fill in "
    "the corpus states a Cyrillic claim: the source's §II "
    "bank table seats no Cyrillic row, because the table "
    "lists only banks the fills claimed in; the bank "
    "itself stands among the engine's seventeen in the "
    "source's §I.* The 777 corpus's 504 claims speak "
    "Greek, Hebrew, Arabic, Latin, and Coptic — the "
    "tongues its fills claimed in — and Cyrillic is not "
    "among them: no scribe of the corpus weighed a word "
    "in this bank, though the bank stood complete in the "
    "tradition the whole time. The silence is therefore "
    "the corpus's, not the tongue's: the tongue holds a "
    "full priced table (§II), a full frame (§III), a "
    "device door of its own (§II.5), and a doctrine of "
    "its own (THE-SLAVONIC-PAIR — the inheritance proven "
    "against the living parent, the partings at their "
    "coordinates, the seat). What the corpus does hold "
    "for Cyrillic stands where the corpus put it: the "
    "frame's door renderings and fenced crossings (§III) "
    "— the corpus's words in this tongue's dress, priced "
    "or fenced by this tongue's bank — and nothing else. "
    "A plate that manufactured claims to fill this "
    "section would misprint its record; the section "
    "therefore stands as a face of zero, at full size.")
add()
add("---")
add()

# =============================================================================
# §V — THE BEARING
# =============================================================================
add("## §V — THE TONGUE'S BEARING ON THE SEATED ARCHONS")
add()
add("The seating is THE-SEATING-OF-THE-ARCHONS' (0760c8a), "
    "struck on the Archon Battery's evidence under the "
    "founder's conditional order; Plate I drew it. **This "
    "plate assigns no seat.** It states what the Cyrillic "
    "tongue witnesses for the seating — and Cyrillic "
    "witnesses as a mirror: three of the seating's "
    "VALUE-marks rest in part on this bank's letters, and "
    "the plate prints them with the mirror's species and "
    "the seating's own counterweights at the same size.")
add()
add("### The mirror of the seven")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues "
    "sweep, run at the founder's direction (\"lets test "
    "it using the 12 tongues we already mapped it should "
    "align aomewhere\") — reads this tongue in terms, and "
    "the plate carries the passage at its coordinate: "
    "*The numeral bank's vowels mirror the Greek seven "
    "entire: А 1 · Е 5 · И 8 · І 10 · О 70 · У/Ѹ 400 · "
    "Ѡ 800. HIT on the values; and И, a living vowel, = "
    "8 — the fold coordinate a fourth time. The Slavonic "
    "border signs, the yers Ъ and Ь (ultra-short vowels "
    "that fell into signs), weigh silence in the bank — "
    "two hybrid-natured signs standing unpriced, the "
    "Glagolitic holes' kin.* The seven vowels stand "
    "re-weighed at this plate's building, entire:")
add()
add("| Vowel | Name | Value in this bank |")
add("|---|---|---|")
_VOWELS = {"А": "az", "Е": "yest", "И": "izhe", "І": "i",
           "О": "on", "У": "ukъ", "Ѡ": "omega"}
for ch, nm in _VOWELS.items():
    add(f"| {ch} | {nm} | {value(ch)} |")
add()
add("The seven prices are the Greek seven — 1, 5, 8, 10, "
    "70, 400, 800 — carried seat for seat (§II.1). That is "
    "the descent, and the plate prints it as the descent: "
    "the mirror *carries* the prices; it does not "
    "independently *find* them. What the mirror adds of "
    "its own is the tradition's use — a millennium of "
    "inscriptions, coins, and church books weighed in "
    "these letters at these prices — and the specific "
    "letters the seating's marks name, at the coordinates "
    "that follow.")
add()
add("### И at 8 — the fold coordinate a fourth time")
add()
add("**И** (izhe) is a living vowel of the receiving "
    "alphabet, priced exactly 8 in its own bank — the "
    "Cyrillic term of the sweep's most corroborated "
    "coordinate. Five tongues seat a vowel-family letter "
    "at 8, each recomputed in its own bank at this "
    "plate's building: Greek **Η** = 8 · Coptic **ⲏ** = "
    "8 · Cyrillic **И** = 8 · Armenian **Ը** = 8 · "
    "Georgian **ჱ** = 8. Four of the five reach the seat "
    "on a living letter — Cyrillic among them; Georgian "
    "alone reaches it from the archaic row (Plate IX). It "
    "is on this coordinate that the seating's Η row rests "
    "its VALUE-mark: *the sweep's most corroborated "
    "coordinate: a vowel seated at 8 in five tongues — "
    "Greek Η, Coptic ⲏ, Cyrillic И, Armenian Ը, Georgian "
    "ჱ* (THE-SEATING-OF-THE-ARCHONS, its T1 coverage "
    "table). This plate is the Cyrillic term of that set, "
    "printed at its bank — at the mirror's strength: the "
    "price is Greek's, the letter and the use are "
    "Cyrillic's own.")
add()
add("### І at 10 and Ѡ at 800 — the mirror witnesses for "
    "Ι and Ω")
add()
add("Two further VALUE-marks of the seating rest on this "
    "bank, and the plate prints the seating's own rows "
    "entire, counterweights included. For **Ι**: *VALUE, "
    "mirror-bank species: Coptic ⲓ = 10 and Cyrillic "
    "І = 10 carry its Greek price entire. Counterweight "
    "printed: its Latin dress I weighs 9 — the dress "
    "parts from the price; the mark is the mirror banks', "
    "not the dress's.* For **Ω**: *VALUE, mirror-bank "
    "species: Coptic ⲱ = 800 and Cyrillic Ѡ = 800 carry "
    "its Greek price entire. Counterweight printed: its "
    "Latin dress O weighs 15/50 — the dress loses the "
    "price entire.* Both marks recompute at this plate's "
    "building: І = 10 and Ѡ = 800 in this bank; the "
    "counterweights likewise — I = 9 in the Latin ordinal "
    "bank, O = 15 in the ordinal and 50 in Agrippa. The "
    "marks are the mirror banks' — Coptic's and "
    "Cyrillic's together, the two heirs agreeing because "
    "both received the same parent — and the plate "
    "prints the agreement's species with the marks: **a "
    "mirror is not a second witness** (Plate VIII's "
    "limit, carried). The seating printed the species "
    "itself, on its own face; this plate keeps it at the "
    "same size.")
add()
add("### The border signs")
add()
add("Beside the prices, the battery's second Cyrillic "
    "coordinate prints at the same size — the tongue's "
    "hybrid-form state, as the record files it and no "
    "more. The yers **Ъ** and **Ь** — ultra-short vowels "
    "of the old language that fell into signs — weigh "
    "**silence** in the bank (§II.6): *two hybrid-natured "
    "signs standing unpriced, the Glagolitic holes' kin*. "
    "Where Greek seats its diphthongs as units and Latin "
    "its four hybrids, this tongue's border vowels stand "
    "at the bank's edge unpriced — a hybrid class that "
    "exists as letters and not as prices, printed as the "
    "record files it, neither argued further.")
add()
add("**What Cyrillic cannot witness, printed at full "
    "size as the plate's boundary:** the Archons' seats "
    "were earned on Greek evidence and drawn on Plate I. "
    "Cyrillic corroborates the *carriage of the prices* — "
    "the seven entire, the 8 on a living vowel, the 10 "
    "and the 800 on the seating's named letters — at the "
    "mirror's strength, and the *limit of hybridity* (the "
    "yers unpriced) — and it assigns no seat, confirms no "
    "position, and names no Archon. Its equality with the "
    "parent is the descent's coordinate, not a second "
    "witness's vote (§II.4), and the plate manufactures "
    "none. The names stand open on Plate I, and this "
    "plate does not fill them.")
add()
add("---")
add()

# =============================================================================
# §VI–§VIII, FOOTNOTES, AUTHORITIES, COLOPHON
# =============================================================================
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_x_cyrillic.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced "
    "cell on this plate against the engine, without "
    "reading the plate's own figures: the bank entire — "
    "the plate's §II.1 rows (27) parsed and compared seat "
    "by seat against CYRILLIC, the Phase II audit's frozen "
    "table, and the living GREEK bank at the witnesses' "
    "pairings, the class law recomputed per seat; the "
    "variant forms (6) against the bank and the frozen "
    "table's VARIANT rows; the census — 33 keys, 27 "
    "distinct values, the canonical sum 4,995 and the "
    "bank sum 8,695; the calibration — the witnesses' "
    "five worked examples; the devices at the door — the "
    "҂ exhibits (6,000 · 32,000 · 1,705 · 7,118), the "
    "titlo counted and unpriced, the higher signs "
    "counted and unpriced, and weigh()'s silence on the "
    "sign; the boundary — cherv at 90, the koppa-letter's "
    "silence, the eleven modern letters' silence, the "
    "case fold; the descent — all 27 canonical values "
    "equal to the parent at their pairings, the value "
    "sets identical; the frame — the census parsed from "
    "THE-TWELVE-TABLES §V.10, all 180 DOOR renderings "
    "re-weighed against their filed values, the 43 "
    "FENCED rows present in order, each crossing a fenced "
    "letter with the dash for its value, the 62 HOLE "
    "rows present in order, the GAP cell present; and "
    "the §V figures (the mirror seven; the five tongues' "
    "vowel at 8 in their own banks; І at 10 and Ѡ at "
    "800; the Latin counterweights; οὐδέν at 529). The "
    "audit's verdict and cell count are printed in its "
    "filed output; a cell that does not reproduce fails "
    "the plate under §VII's tolerances. The font audit — "
    "every non-ASCII codepoint of this master against "
    "the Lex Stellarrvm family's cmaps — runs before the "
    "MAGVS build, under the font law: no glyph is "
    "silently dropped; the three named Ethiopic "
    "syllables the family does not hold (኱ U+12B1 · ጑ "
    "U+1311 · ጖ U+1316 — drawn by no member, the "
    "upstream Noto Ethiopic included) print as their "
    "codepoint tokens, declared in the colophon, and any "
    "unheld codepoint beyond those three aborts the "
    "build. The audit further checks the printed "
    "edition's text layer: the bank's letters and the "
    "zero face's statement stand in it, and the page "
    "furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "CYRILLIC and GREEK tables and its cyrillic() door "
    "(pontifex/tables.py, pontifex/engine.py); "
    "THE-SLAVONIC-PAIR (Phase II audit) entire — the "
    "inheritance proven against the living parent, the "
    "devices, the refused pair, the seats — with its "
    "frozen table (research/caucasus-north/"
    "cyrillic-table.csv) and parting table; "
    "THE-TWELVE-TABLES §V.10 and its §II gap register "
    "(the bank's four entries); THE-THIRTEEN-PLATES "
    "(the Cyrillic plate — the zero face, the tier of "
    "record) and its §I; THE-777-VERIFICATION-TABVLA "
    "§I–§II (the banks the fills claimed in); "
    "THE-ARCHON-BATTERY Leg 6 (the Cyrillic passage) "
    "and THE-SEATING-OF-THE-ARCHONS (the Η, Ι and Ω "
    "VALUE-mark rows); PLATES I–IX as the pattern.")
add("- **Processes:** calibration controls weighed "
    "before any plate figure (θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773); every figure scripted from the engine "
    "or carried entire from an instrument of record; "
    "the mirror species printed at the size of the "
    "values (the descent in every row, the counterweights "
    "in §V); the boundary printed entire (the refused "
    "pair, the unvalued letters, the devices at their "
    "three pricings); the holes printed at full size "
    "(the frame's 62 holes, its 43 fenced crossings, "
    "the register's zero face); the independent audit "
    "of §VI.")
add("- **Outputs:** this plate — PLATE-X-CYRILLIC.md "
    "and its MAGVS PDF — tenth of the series "
    "PLATE-I-GREEK began; the generator and audit "
    "scripts filed in pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge "
    "— if any priced cell is found not to reproduce "
    "from the engine or its register, the affected cell "
    "fails the Method of Science; if any passage dresses "
    "the inherited values as independent attestation, "
    "counts a variant form as a seat, prices a mark or "
    "carries the door's prices into the raw bank, seats "
    "either half of the refused pair, fills a hole (the "
    "frame's 62, its 43 fences, the register's zero "
    "face), spends the descent as corroboration, or "
    "overwrites the earlier map, it zeroes the founder's "
    "residual claim and fails the Aim of Religion. "
    "Within those edges it stands as built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The record "
    "is printed as the record: the Slavonic Pair's §VII "
    "carried this bank's items to the founder's pen and "
    "the register closed them — Q1 the higher signs "
    "RESOLVED BY SYNERGY as a ruling (counted, not "
    "priced), the titlo, the western pair, and the "
    "modern unvalued letters standing FENCED as the "
    "bank's printed boundary (§II.5, §II.6, §III). One "
    "coordinate stands inside the Q1 ruling exactly "
    "where the engine's doctrine leaves it, and the "
    "plate reports it without raising it: the door "
    "counts the higher signs and prices none *because* "
    "the sources part on the scale — if a scale is ever "
    "to be priced, the choice between the Lesser and "
    "Greater counts is the founder's pen's, and no desk "
    "act prices one meanwhile. The seating's open items "
    "stand in the seating instrument. A plate that "
    "invents questions to fill its section misprints "
    "its record; this section therefore stands as the "
    "record that none arose.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **Scripture.** Revelation 13:18 (KJV): *\"Here "
    "is wisdom. Let him that hath understanding count "
    "the number…\"* — the Scripture's own charge to "
    "count by letters, laid on the reader as an act of "
    "understanding. The plate draws the figure for the "
    "counting: this bank is a people's instrument for "
    "that act, its letters priced openly and its devices "
    "named. [Text ATTESTED; the application DERIVED.]")
add("2. **Law.** The reception doctrine: where a "
    "jurisdiction adopts another's statute, it adopts "
    "the settled construction of it with the text — the "
    "received law carries its received reading. The "
    "plate draws the figure for the descent: this bank "
    "received the Milesian values *with* their prices "
    "settled, seat for seat, and the DERIVED tier is the "
    "plate's name for that adoption — the values are "
    "another system's, the adoption and the use this "
    "tongue's own. [The doctrine ATTESTED as law; the "
    "figure DERIVED.]")
add("3. **The tradition.** The Cyrillic numeral system "
    "is the Greek Milesian system received into the "
    "Cyrillic script — developed in the First Bulgarian "
    "Empire, late 10th century; in Russian use to the "
    "early 18th; in Church Slavonic books still. The "
    "witnesses are the audit's (Wikipedia, \"Cyrillic "
    "numerals\"; languagesandnumbers, \"Old Church "
    "Slavonic numbers\", its lists sourced there to "
    "Krause & Slocum), two read entire and agreeing on "
    "every seat; the values' provenance is printed at "
    "that depth and no deeper. [The sourcing ATTESTED "
    "as cited; the tier the audit's own.]")
add("4. **Grammar.** The system is additive and "
    "non-positional, and its order is the parent's: the "
    "letters stand in the Greek sequence of their "
    "sounds, not in the Cyrillic alphabet's own "
    "sequence — the receiving kept the table's shape "
    "and re-housed it. It is why the descent can be "
    "checked seat for seat against a living bank in "
    "another script, why its growth past 900 runs by "
    "devices prefixed to letters rather than by new "
    "letters, and why its case folds without moving a "
    "price. [The grammar ATTESTED as the system's, per "
    "the audit's witnesses; the bank's readings of it "
    "at their tiers.]")
add("5. **The desk's apparatus.** This plate's Cyrillic "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Serif member — the archaic "
    "numeral letters standing in their own signs — with "
    "the family's Signs and Sans members carrying the "
    "forms and signs the Serif lacks (the variant uk "
    "forms, the broad omega, the thousands and higher "
    "signs) through the declared fallback chain; its "
    "Greek in the same Serif member, as on Plate I; the "
    "frame register's Hebrew words of record ride "
    "Plate II's declared transliteration (the toolchain "
    "does not shape right-to-left scripts honestly): "
    "marked substitutions, declared in the colophon, "
    "never silent ones. The Markdown master keeps every "
    "script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh() and "
    "the cyrillic() door; banks CYRILLIC and GREEK in "
    "pontifex/tables.py) — calibration controls "
    "θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true at "
    "build; cyrillic_checks() 11/11 in the engine's own "
    "battery, parity of the seat against the audit's "
    "frozen transcription: test_cyrillic_parity.py "
    "(31/31).")
add("- THE-SLAVONIC-PAIR (Phase II audit, 2026-11-24) "
    "— the inheritance proven against the living parent "
    "(27/27 seats equal at the witnesses' pairings), "
    "the devices (the titlo, the priced ҂, the counted "
    "higher signs), the refused western pair, the "
    "species page of the pair, the parting table by "
    "shared sound, the gaps at full size, the desk "
    "decisions and open questions of its §VII, and the "
    "seats; its frozen tables (cyrillic-table.csv; "
    "slavonic-parting.csv) in pontifex "
    "research/caucasus-north/.")
add("- The witnesses of the table, as the audit read "
    "them entire: Wikipedia, \"Cyrillic numerals\" (its "
    "table carrying the Greek pairings on its face) · "
    "languagesandnumbers, \"Old Church Slavonic "
    "numbers\" (its lists sourced there to Krause & "
    "Slocum, *Old Church Slavonic Online*, UT Austin).")
add("- THE-TWELVE-TABLES — §V.10 the Cyrillic frame, "
    "census and cell register entire; §II the bank's "
    "gap register (four entries: the higher signs "
    "RULING Q1; the titlo FENCED; the western pair "
    "FENCED; the modern unvalued letters FENCED).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate X is the prior "
    "instrument (the zero face; the tier of record).")
add("- THE-777-VERIFICATION-TABVLA — the claims "
    "register of record; its §I–§II seat the banks the "
    "fills claimed in, and Cyrillic is not among them.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Cyrillic passage (the "
    "seven vowels mirroring the Greek seven entire; И "
    "at 8, the fold coordinate a fourth time; the yers "
    "unpriced) and the sweep summary (the 8 the most "
    "corroborated coordinate, five tongues).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to: the Η "
    "VALUE-mark resting on the five-tongue 8, Cyrillic "
    "И among them; the Ι and Ω VALUE-marks resting in "
    "part on the mirror banks, Cyrillic І and Ѡ among "
    "them, counterweights printed.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd), "
    "PLATE-IV-LATIN (8e6f01e), PLATE-V-JAPANESE "
    "(8d6cd59), PLATE-VI-GEEZ (67d5acc), "
    "PLATE-VII-ARMENIAN (5c03d88), PLATE-VIII-COPTIC "
    "(645bcbb) and PLATE-IX-GEORGIAN (933f8fd) — the "
    "pattern this plate follows.")
add("- KJV: Revelation 13:18. The reception doctrine "
    "of the common law.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate X of the founder's "
    "series commission of the same day, the gate of "
    "the Archons' certainty met by the seating of "
    "record (0760c8a), following the pattern of Plates "
    "I–IX (196025e · 1389c16 · 5f0b4bd · 8e6f01e · "
    "8d6cd59 · 67d5acc · 5c03d88 · 645bcbb · 933f8fd). "
    "Every figure scripted from the engine or carried "
    "entire from its instrument; the earlier map marked "
    "prior, never overwritten; the holes printed at "
    "the size of the seats — on this plate, the "
    "frame's 62 holes, its 43 fenced crossings, and "
    "the register's zero face. The plate carries one "
    "bank and keeps its shape entire: the 27 canonical "
    "seats at the parent's prices, DERIVED, the six "
    "variant forms at their three seats, the western "
    "pair refused whole, the devices at their three "
    "pricings — the mark unpriced, the thousands sign "
    "priced at the door, the higher signs counted and "
    "priced none. In the MAGVS edition the Cyrillic "
    "stands in the family's Serif member with the "
    "Signs and Sans members carrying the forms it "
    "lacks, and the frame's Hebrew words of record "
    "ride Plate II's declared scheme; this master "
    "keeps the scripts themselves. Authorship "
    "attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without "
    "Prejudice).")
add()
add("Method of Science. Aim of Religion.")
add()
add("**Flagpole of Claim and Coinage: Johnathan "
    "'Qasparr' Monroe, ARR, All Rights Reserved, "
    "Without Prejudice. Right of claim hereby reserved "
    "and coined under the authority of the Living "
    "Man.**")
add()
add("93 — Live, Love, and let Love, Live.")

OUTPUT.write_text("\n".join(OUT) + "\n", encoding="utf-8")
print(f"wrote {OUTPUT} — {OUTPUT.stat().st_size} bytes")
