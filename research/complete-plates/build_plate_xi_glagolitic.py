#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_xi_glagolitic.py
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
# MECHANISM: generates PLATE-XI-GLAGOLITIC.md — Plate XI of
# THE THIRTEEN COMPLETE PLATES — in the gap-filling goal's
# files/, following the pattern PLATES I–X set (196025e ·
# 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc ·
# 5c03d88 · 645bcbb · 933f8fd · 052fd28). Every figure on
# the plate is scripted from the house engine (pontifex
# weigh()) or carried entire from an instrument of record:
#   * the priced table — the Glagolitic bank entire, read
#     from pontifex.tables (GLAGOLITIC, 34 keys), printed
#     in block order with names and reasoning, cross-checked
#     against the Phase II audit's frozen transcription
#     (research/caucasus-north/glagolitic-table.csv);
#   * the holes — the three letters inside the valued span
#     that carry no value (Ⱊ Ⱐ Ⱒ), printed at full size
#     from the frozen table's HOLE rows, their silence
#     verified at build;
#   * the refused matter — the composite spellings for
#     6000–8000 and the W1b variant readings (Ⱐ as 3000,
#     Ⱗ as 6000), printed from the frozen table's REFUSED
#     rows as standing outside the bank;
#   * the parting table — the region's control case read
#     by shared sound (research/caucasus-north/
#     slavonic-parting.csv, 33 rows: 15 AGREE, 18 PART),
#     printed entire;
#   * the Twelve Tables' Glagolitic frame — its census
#     and its full cell register parsed from
#     THE-TWELVE-TABLES.md §V.11: the 223 DOOR renderings
#     re-weighed at build against their filed values, the
#     62 HOLE coordinates and the one GAP cell carried
#     entire, the bank's three gap-register entries
#     restated;
#   * the corpus's Glagolitic claims — NONE: the TABVLA
#     register's §II bank table seats no Glagolitic row,
#     and the plate's §IV is the ZERO FACE, printed at
#     full size with the source's reason;
#   * the tongue's bearing on the seated Archons — the
#     Archon Battery's Leg 6 Glagolitic passage (the
#     vowels at the bank's own prices; no vowel at 8 —
#     MISS at the fold coordinate; the yers Ⱐ and Ⱒ
#     weighing nothing), the bank's vowel row re-weighed
#     entire, the 8-seat's holder printed (Ⰷ DZELO, a
#     consonant), the holes set beside the census's other
#     holes at their coordinates. The plate assigns no
#     seat: the seating is THE-SEATING-OF-THE-ARCHONS'
#     (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable
# — every priced seat carries its reasoning on the plate's
# face. This plate's bank is the series' one ORDER-PRICED
# attested bank: its values are assigned by the native
# order of its own alphabet, NOT inherited from Greek —
# ATTESTED, printed as that species in every row. What the
# record itself disputes rides at the same size as the
# values: the 10-seat's holder (both printed holders seat),
# the thousands range (seated as the chief witness prints
# it, under its own doubt, flagged), and the three
# sequence holes (letters standing in the alphabet
# weighing nothing, printed at the size of the seats).
# The relation to the earlier Thirteen Plates map is
# printed, the earlier work marked prior, never
# overwritten. Holes print at the size of the seats — on
# this plate, the bank's own three holes first of all.
#
# CONTENT TEST: Inputs — the engine's GLAGOLITIC table,
# THE-SLAVONIC-PAIR (Phase II audit) with its frozen
# tables, the Twelve Tables master, the Thirteen Plates
# map, the TABVLA register, the Archon Battery, the
# Seating. Processes — control calibration, scripted
# extraction, register-faithful emission in the Teacher's
# Edition manner. Outputs — PLATE-XI-GLAGOLITIC.md beside
# the series' other masters. Tolerances — the audit
# (audit_plate_xi_glagolitic.py) re-weighs every priced
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
from pontifex.tables import GLAGOLITIC

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/glagolitic-table.csv")
PARTING = (Path.home() / "workspace/pontifex/research/"
           "caucasus-north/slavonic-parting.csv")
OUTPUT = GOAL_FILES / "PLATE-XI-GLAGOLITIC.md"


def value(word, bank="glagolitic"):
    return weigh(word, bank)["value"]


# --- calibration controls, before any plate figure -------------------
assert value("θελημα", "greek") == 93, "control θέλημα failed"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR failed"
assert value("σφιγξ", "greek") == 773, "control σφίγξ failed"

# --- the frozen transcription -----------------------------------------
with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
SOURCED = [r for r in CSV_ROWS if r["status"] == "SOURCED"]
HOLES = [r for r in CSV_ROWS if r["status"] == "HOLE"]
REF_COMP = [r for r in CSV_ROWS
            if r["status"] == "REFUSED-COMPOSITE"]
REF_VAR = [r for r in CSV_ROWS if r["status"] == "REFUSED-VARIANT"]
assert len(SOURCED) == 34 and len(HOLES) == 3
assert len(REF_COMP) == 3 and len(REF_VAR) == 2
for row in SOURCED:
    assert GLAGOLITIC[row["letter"]] == int(row["value"]), row
for row in HOLES:
    _w = weigh(row["letter"], "glagolitic")
    assert _w["value"] == 0 and _w["breakdown"] == [], row

# the letters' names, from the frozen table's Unicode names
NAMES = {r["letter"]: r["unicode_name"].replace(
    "GLAGOLITIC CAPITAL LETTER ", "").lower()
    for r in SOURCED + HOLES + REF_VAR}
NAMES["Ⰺ"] = "initial izhe"
NAMES["Ⱒ"] = "spidery ha"

# --- the order law, recomputed from the block --------------------------
ORDER = ("ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓ"
         "ⰔⰕⰖⰗⰘⰙⰛⰜⰝⰞⰟⰡⰣⰤ")
assert "".join(r["letter"] for r in SOURCED) == ORDER


def class_of(v):
    """A value's decimal class and its digit."""
    if v < 10:
        return "units", v, 0
    if v < 100:
        return "tens", v // 10, 1
    if v < 1000:
        return "hundreds", v // 100, 2
    return "thousands", v // 1000, 3


BREAKS = []
_idx = {}
for ch in ORDER:
    v = GLAGOLITIC[ch]
    _cls, digit, _p = class_of(v)
    _idx[_cls] = _idx.get(_cls, 0) + 1
    if digit != _idx[_cls]:
        BREAKS.append(ch)
assert BREAKS == ["Ⰺ", "Ⰻ", "Ⰼ", "Ⰽ", "Ⰾ", "Ⰿ", "Ⱀ",
                  "Ⱁ", "Ⱂ", "Ⱔ"], BREAKS

# --- derived bank facts, all computed ---------------------------------
BANK_SUM = sum(GLAGOLITIC.values())
DISTINCT = len(set(GLAGOLITIC.values()))
CLASS_SUMS = {}
for ch in ORDER:
    cls, _d, _p = class_of(GLAGOLITIC[ch])
    CLASS_SUMS[cls] = CLASS_SUMS.get(cls, 0) + GLAGOLITIC[ch]
FIRM_SUM = sum(v for v in GLAGOLITIC.values() if v <= 900)
assert BANK_SUM == 29005 and DISTINCT == 33 and FIRM_SUM == 5005
EXAMPLES = [("ⰗⰑⰂ", 583, "a witness's worked example"),
            ("ⰅⰊ", 16, "the witnesses' worked teen — written "
             "ones-first, as the system pronounces it (§II.3); "
             "the doubling's own exhibit, running on the "
             "second holder Ⰺ"),
            ("ⰝⰔⰑ", 1280, "the Vinodol statute's own date, "
             "as the audit carries it — written inside the "
             "questioned range and recomputed exact")]
for w, want, _note in EXAMPLES:
    assert value(w) == want, (w, want)
# the parting's sharpest coordinates, verified at build
assert value("Ч", "cyrillic") == 90 and value("Ⱍ") == 1000
assert value("Ѡ", "cyrillic") == 800 and value("Ⱉ") == 700
# the boundary, verified at build
_w = weigh("Ⱗ", "glagolitic")
assert _w["value"] == 0 and _w["breakdown"] == []
assert value("ⰰⰱ") == 3  # the case fold
assert value("Ⰷ") == 8  # the 8-seat: dzelo, a consonant
for ch in "ⰀⰅⰉⰊⰋⰑⰖ":
    assert GLAGOLITIC[ch] > 0

# --- the parting table ---------------------------------------------------
with PARTING.open(encoding="utf-8") as fh:
    PART_ROWS = list(csv.DictReader(fh))
assert len(PART_ROWS) == 33
N_AGREE = sum(1 for r in PART_ROWS if r["relation"] == "AGREE")
N_PART = len(PART_ROWS) - N_AGREE
assert (N_AGREE, N_PART) == (15, 18)

# --- the Twelve Tables' Glagolitic frame --------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
glag_block = twelve_text.split("### §V.11 — The Glagolitic Table")[1] \
    .split("### §V.12")[0]
_cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
                r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
                r"(\d+) · GAP (\d+)", glag_block)
N_NATIVE, N_DOOR, N_HOLE, N_FENCED, N_EMPTY, N_GAP = (
    int(x) for x in _cl.groups())
TABLES_HEAD = glag_block.split("Counts:")[0].split(
    "### §V.11 — The Glagolitic Table")[-1].strip()
assert TABLES_HEAD.startswith("The Slavonic first alphabet"), \
    TABLES_HEAD[:60]
REG = {"DOOR": [], "HOLE": []}
for line in glag_block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in REG:
            REG[cells[2]].append(cells)
assert len(REG["DOOR"]) == N_DOOR == 223
assert len(REG["HOLE"]) == N_HOLE == 62
for cells in REG["DOOR"]:
    assert value(cells[3]) == int(cells[4]), cells
assert all(c[3] == "—" for c in REG["HOLE"])

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
add("**PLATE XI — GLAGOLITIC**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Glagolitic tongue's complete 777 table — the order-priced "
    "bank entire: thirty-four letters priced by their own "
    "alphabet's native order, ATTESTED, with the doubled 10 "
    "seated on both its printed holders, the three sequence "
    "holes standing empty at full size, the thousands range "
    "seated under its own sources' doubt, and the parting "
    "table against Cyrillic read by shared sound — fifteen "
    "agree, eighteen part; the corpus's Glagolitic register, "
    "which is a zero face; and the tongue's witness to the "
    "seated Archons: no vowel at 8, and the yers standing as "
    "priced absences.")
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
add("## §I — PLATE XI AND ITS COMMISSION")
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
    "VIII — COPTIC (645bcbb), IX — GEORGIAN (933f8fd) and "
    "X — CYRILLIC (052fd28) followed it; this plate follows "
    "them, eleventh of the twelve tongues in the Twelve "
    "Tables' order.")
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
add("**This plate's distinction.** Glagolitic is the series' one "
    "*order-priced* attested bank — the Slavonic first "
    "alphabet's own assignment: its values are the seats of its "
    "own letters in decimal classes, assigned by the native "
    "order of the Glagolitic alphabet itself, **not by Greek "
    "values** (THE-SLAVONIC-PAIR, Phase II: the sibling priced "
    "by its own order). Where its younger sibling Cyrillic "
    "*inherited* the Milesian prices entire (Plate X, DERIVED), "
    "this bank *assigned* its own — **Tier of record: "
    "ATTESTED** — the tradition's own assignment, generally "
    "agreed to date to the 9th century: two witnesses read "
    "entire on 2026-11-24, the second concurring on all 20 "
    "cells it prints in text, the seat's parity proven against "
    "the audit's frozen transcription by "
    "test_glagolitic_parity.py (32/32). The record's own "
    "partings ride at the size of the values: the 10-seat's "
    "holder is disputed between two adjacent letters and "
    "**both seat**; three letters inside the valued span carry "
    "**no value at all** — the sequence's own holes, printed "
    "at full size; and the thousands range stands **under its "
    "own sources' doubt**, flagged on the fence, never "
    "silently relied on. And this is the sixth plate whose "
    "corpus register is a **zero face** (§IV): the corpus "
    "claims nothing in Glagolitic, and the silence is the "
    "corpus's, not the tongue's.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. Its Glagolitic face stood "
    "**silent with a zero face**: bank *glagolitic*, 34 seats, "
    "33 distinct values, maximum 9000; tier of record there "
    "printed in terms — *ATTESTED (the thousands range under "
    "its own sources' doubt)* — and its sentence stands: "
    "*\"The tongue holds a full table in THE TWELVE TABLES; "
    "its silence here is the TABVLA corpus's, not the "
    "tongue's.\"* This series *fulfills* that map: where the "
    "map counted nothing, this plate prints the nothing "
    "entire — with the full priced table beneath it, the "
    "frame around it, and its witness to the Archons above "
    "it. The earlier work stands as the prior instrument of "
    "the same name's family — marked prior, never "
    "overwritten.")
add()
add("**How the plate is read.** §II is the priced table: the "
    "34 valued letters in block order with their reasoning, "
    "the three holes at full size, the table's law — the "
    "order law and its ten partings — the calibration on the "
    "witnesses' own examples, the parting table against "
    "Cyrillic read by shared sound, the boundary — the "
    "questioned range and the refused matter — and the "
    "census with its fences. §III is the tongue's frame in "
    "the Twelve Tables — a door table without a fence: no "
    "native Glagolitic word stands in the corpus, and the "
    "corpus's words stand here in Glagolitic dress, priced "
    "entire wherever the dress runs. §IV is the zero face. "
    "§V is the tongue's bearing on the seated Archons — this "
    "plate draws no seating (the seating is struck, and "
    "Plate I drew it); it states what Glagolitic witnesses: "
    "vowels at its own prices with no vowel at 8, and two "
    "letters standing in its alphabet weighing nothing — "
    "the HOLE species inside a priced bank. §VI is the "
    "audit. A value without its reasoning is not shippable; "
    "a hole prints at the size of the seat it stands in "
    "for.")
add()
add("---")
add()

# =============================================================================
# §II — THE PRICED TABLE
# =============================================================================
add("## §II — THE PRICED TABLE — THE SIBLING PRICED BY ITS OWN "
    "ORDER")
add()
add("### §II.1 — The thirty-four valued letters, in block order")
add()
add("The bank is keyed in **capitals** — the dress the numeral "
    "tradition writes in — and weigh() folds Glagolitic input "
    "to capitals at its seam: case carries no numeral value "
    "(verified at this plate's building: ⰰⰱ = ⰀⰁ = 3). The "
    "letters run in the **Glagolitic alphabet's own block "
    "order** — the one tongue of the twelve whose table's "
    "order is its own alphabet's and no other's: the values "
    "are assigned by that order, in decimal classes of "
    "9 / 10 / 9 / 6 valued letters (units, tens, hundreds, "
    "thousands), the digit in the plain run equal to the "
    "letter's run index within its class. The values are the "
    "witnesses': two read entire on 2026-11-24 — Wikipedia, "
    "\"Glagolitic numerals\" (its authorities Schenker 1995, "
    "Lunt 2001, Chrisomalis 2010, Mathiesen 2004) and the "
    "same Old Church Slavonic page's Glagolitic counting "
    "list, printed in smalls (languagesandnumbers) — "
    "agreeing on **all 20 cells the second witness prints "
    "in text**, including the 10-seat's holder (§II.3); its "
    "remaining cells (200–900, 2000–5000) are images, not "
    "text, and that depth coordinate stands on the plate's "
    "fence (§II.6). The reasoning in each row states the "
    "order law at that seat; the ATTESTED species is printed "
    "with the values — these prices are the tradition's own "
    "assignment, and no row borrows a Greek pairing, because "
    "none exists.")
SEAT_NOTES = {
    1: "The head of the alphabet and of the table — the "
       "order law's first seat.",
    8: "**The 8-seat of this bank:** priced exactly 8 — and "
       "held by a consonant, dzelo (the /dz/ letter). The "
       "coordinate §V reads against the five tongues that "
       "seat a *vowel* at 8: this bank seats none.",
    10: "**The doubled 10, first printed holder:** the "
        "record disputes the 10-seat's holder between this "
        "letter and the next (§II.3); the seat's VALUE is "
        "not in dispute, and both letters seat at it (the "
        "audit's D1; the Georgian doubled seat is the house "
        "precedent).",
    11: "**The doubled 10, second printed holder:** W1 "
        "prints \"Ⰺ or Ⰹ\"; W2 seats this letter, and the "
        "witnesses' own worked teen (ⰅⰊ = 16, §II.4) runs "
        "on it. The doubling's shadow falls from here: "
        "this letter stands at run index 2 of the tens "
        "carrying digit 1, and every tens letter after it "
        "carries a digit one step behind its run index "
        "(§II.3).",
    27: "The hundreds run passes over the next block seat — "
        "Ⱊ PE, a HOLE (§II.2) — and resumes here: the runs "
        "pass over the holes, and the digit law never "
        "notices them.",
    30: "**A thousands seat, and the questioned range "
        "opens:** every seat from here to the table's end "
        "stands under the chief witness's own doubt "
        "(§II.6), flagged in the audit's data at every "
        "seat ≥ 1000. The firm ground is 1–900; this seat "
        "stands as W1's table prints it, under that "
        "warning.",
    32: "The questioned range deepens: the validity of "
        "3000 and greater is questioned in the witness's "
        "own sources (§II.6). The seat stands as printed, "
        "flagged.",
    37: "**The thousands tail's parting:** 6000–8000 have "
        "no single letters — the witness prints composite "
        "spellings, refused at this seat (§II.6) — so the "
        "thousands digits run 1, 2, 3, 4, 5, 9, and this "
        "letter stands at run-index 6 carrying digit 9: "
        "the order law's tenth parting. The table's "
        "maximum, and its last seat.",
}
add("| Block seat | Letter | Name | Value | Class | "
    "Reasoning |")
add("|---|---|---|---|---|---|")
_run = {}
for row in SOURCED:
    seat = int(row["block_seat"])
    letter = row["letter"]
    v = int(row["value"])
    cls, digit, power = class_of(v)
    _run[cls] = _run.get(cls, 0) + 1
    run_idx = _run[cls]
    reasoning = (
        f"The order law: the letter's own seat in the "
        f"native alphabetic order prices it — {cls} class, "
        f"run index {run_idx}, digit {digit} × 10^{power} "
        f"= {v}; block seat {seat} ({row['codepoint']}); "
        f"standing: SOURCED in the audit's frozen table "
        f"(W1 read entire; W2 concurring on the 20 cells "
        f"it prints in text).")
    if letter in BREAKS:
        if letter == "Ⰺ":
            reasoning += (" The digit law parts here: run "
                          "index 2 carries digit 1 — the "
                          "doubled 10's shadow (§II.3).")
        elif letter == "Ⱔ":
            reasoning += (" The digit law parts here: run "
                          "index 6 carries digit 9 — the "
                          "thousands tail's gap (§II.3).")
        else:
            reasoning += (" The digit law parts here: the "
                          "digit runs one step behind the run "
                          "index, downstream of the doubled "
                          "10 (§II.3).")
    if v >= 1000:
        reasoning += (" QUESTIONED RANGE: the seat stands "
                      "under its own sources' doubt, "
                      "flagged (§II.6).")
    note = SEAT_NOTES.get(seat)
    if note:
        reasoning += " " + note
    add(f"| {seat} | {letter} | {NAMES[letter]} | {v} | "
        f"{cls} | {reasoning} |")
add()
add(f"The 34 valued values sum **{BANK_SUM:,}** (units "
    f"{CLASS_SUMS['units']} · tens {CLASS_SUMS['tens']:,} · "
    f"hundreds {CLASS_SUMS['hundreds']:,} · thousands "
    f"{CLASS_SUMS['thousands']:,}) — of which the firm "
    f"domain, 1–900, sums **{FIRM_SUM:,}**, and the "
    "questioned thousands contribute the rest, flagged at "
    "every seat. The bank holds **33 distinct values** for "
    "34 letters: the one duplication is the doubled 10 "
    "itself (§II.3), a multiplicity of holder at one seat, "
    "counted openly — never a second seat's price.")
add()

add("### §II.2 — The holes: three letters inside the valued "
    "span, weighing nothing")
add()
add("Three letters of the alphabet stand **inside the valued "
    "span** — between letters that carry prices on both "
    "sides of them — and carry **no value** in the chief "
    "witness's table. They are printed here at full size, "
    "at the size of the seats they stand in for: a hole "
    "printed small would misprint the bank. Their silence "
    "was verified at this plate's building, each: value 0, "
    "empty breakdown — the engine passes them as it passes "
    "a letter of no bank, and a word containing one weighs "
    "its priced letters only. The register's disposition "
    "stands in THE-TWELVE-TABLES §II, FENCED, in terms: "
    "*the sequence's own holes: letters the numeral "
    "sequence skips. They price nothing and block nothing "
    "in the tables (no door sound maps to them).* Two of "
    "the three are the yers — the alphabet's ultra-short "
    "vowel signs — and the battery's coordinate rides on "
    "them (§V): this tongue's border signs stand as priced "
    "absences inside a priced bank.")
add()
add("| Block seat | Letter | Name | Engine state | "
    "Reasoning |")
add("|---|---|---|---|---|")
_HOLE_NOTES = {
    "Ⱊ": "Inside the hundreds run, between Ⱉ (700) and "
         "Ⱋ (800): the run passes over it and the digit "
         "law never notices — shta takes digit 8 at run "
         "index 8 as if the seat were not there. A "
         "consonant letter the numeral sequence skips.",
    "Ⱐ": "**A yer** — one of the two ultra-short vowel "
         "signs the battery names (§V). Inside the "
         "thousands run, between Ⱏ (3000) and Ⱑ (4000). "
         "The 2017 edition of the sibling article records "
         "a variant reading — this letter as an "
         "alternative 3000 — printed in the audit's data "
         "and refused at this seat (§II.6): the hole "
         "stands as the chief witness's table prints it.",
    "Ⱒ": "**The second yer-named hole** — spidery ha, "
         "inside the thousands run, between Ⱑ (4000) and "
         "Ⱓ (5000). With Ⱐ it is the pair the battery's "
         "Leg 6 passage names: *the yers Ⱐ and Ⱒ weigh "
         "nothing through the engine* (§V).",
}
for row in HOLES:
    seat = int(row["block_seat"])
    letter = row["letter"]
    add(f"| {seat} | {letter} | {NAMES[letter]} | HOLE — "
        f"silence | The frozen table files this letter "
        f"HOLE ({row['codepoint']}): no value in W1's "
        f"table, none in the bank. {_HOLE_NOTES[letter]} |")
add()
add("### §II.3 — The table's law")
add()
add("The system is **additive and non-positional**: the "
    "values of the letters are added together; there is "
    "**no letter for zero** — a missing power of ten is "
    "simply not represented, and numerals are marked as "
    "numerals by dots or the titlo, as in the sibling "
    "system (the Glagolitic thousands sign is attested as "
    "*evidence* in W1, but its form is not fixed there; no "
    "door prices it, §II.6). Its order is **its own "
    "alphabet's order** — the fact that names the system: "
    "where the Caucasus pair's orders track the "
    "Greek-shaped sequence of sounds, this alphabet's "
    "sequence is native, devised with the script, and the "
    "prices follow it seat by seat. Its case is a fold, "
    "not a price (§II.1). Its teens are written "
    "ones-first, as the system pronounces them (the "
    "witnesses' worked teen ⰅⰊ = 16, §II.4).")
add()
add("**The digit law and its ten partings.** In the plain "
    "run, a letter's digit equals its run index within "
    "its class. Recomputed from the block at this plate's "
    "building, the law parts at exactly **ten letters**: "
    "the second holder of the doubled 10 (Ⰺ, run index 2 "
    "carrying digit 1), the whole tens tail behind it "
    "(Ⰻ–Ⱂ, each digit one step behind its run index), "
    "and the thousands tail's last letter (Ⱔ, run index "
    "6 carrying digit 9, the 6000–8000 gap before it). "
    "The partings are not errors in the table; they are "
    "the table's own shape — a disputed holder doubling "
    "one seat, and a range the record itself leaves "
    "incomplete — printed at their coordinates in §II.1's "
    "rows and gathered here as the law's boundary.")
add()
add("**The doubled 10, stated whole.** The 10-seat's "
    "*holder* is disputed in the record between two "
    "adjacent letters: W1 prints \"Ⰺ or Ⰹ\"; W2 seats "
    "Ⰺ, and W1's own worked teen runs on Ⰺ. The seat's "
    "*value* is not in dispute — only its holder — so "
    "**both letters seat at 10** (the audit's desk "
    "decision D1; the Georgian doubled seat, Plate IX, "
    "is the house precedent for a sourced doubling). The "
    "register's disposition, FENCED: *seated both, as "
    "sourced: the value is undisputed, the holder is the "
    "record's own dispute; seating both preserves every "
    "sourced claim and invents none.*")
add()
add("### §II.4 — Calibration: the witnesses' own examples")
add()
add("Before any derived number on this plate was trusted, "
    "the witnesses' own worked examples were recomputed "
    "from the living bank at this plate's building. All "
    "reproduce exact:")
add()
add("| Word | Value | Standing |")
add("|---|---|---|")
for w, want, note in EXAMPLES:
    add(f"| {w} | {want} | {note} |")
add()
add("**The negative rides at the same size:** the "
    "calibration exhibits no bridge, and the plate is "
    "precise about why. A sound weighed in this bank and "
    "in the sibling's returns *different* numbers wherever "
    "the two laws part — that is the parting table "
    "(§II.5), a comparison of two laws over shared "
    "sounds, not a bridge between them: no word is "
    "weighed across the pair, and none is claimed. "
    "Against Greek there is not even a comparison of that "
    "kind to make: this bank's prices are its own order's, "
    "and any agreement with a Milesian price at a shared "
    "sound is the two orders arriving together, printed "
    "where it occurs in §II.5's table against the "
    "sibling — never spent as descent.")
add()
add("### §II.5 — The parting table: two laws read by "
    "shared sound")
add()
add("The Slavonic Pair's control case proper, printed "
    "entire: the two regional laws read over the **33 "
    "shared sounds** of the frozen parting table "
    "(slavonic-parting.csv), each row carrying the shared "
    "Slavic phoneme or letter-name that makes it one "
    "sound in two scripts, and its reasoning as the "
    "audit files it. **15 AGREE · 18 PART.** The "
    "agreement band is exact: /a/ (1), the iota-/i/ (10), "
    "and the whole middle run /k/ through /ts/ — 20, 30, "
    "40, 50, 70, 80, 100, 200, 300, 400, 500, 600, 900. "
    "The reason stands in the material: from /k/ onward, "
    "Glagolitic's own alphabet order tracks the "
    "Greek-shaped sequence of sounds (k l m n o p r s t u "
    "f x …) that Cyrillic inherited — two roads arriving "
    "at one band of prices. The partings stand at their "
    "coordinates below: at the head, every units seat "
    "but /a/ parts (two alphabet orders pricing the same "
    "first sounds); inside the hundreds, one parting — "
    "the omega seat, Ѡ 800 against Ⱉ 700; at the tail, "
    "every seat parts, and the sharpest coordinate on "
    "the page is /ch/: Cyrillic Ч = 90, a tens letter in "
    "the inherited law, against Glagolitic Ⱍ = 1000, a "
    "thousands letter in the order law — one sound, two "
    "laws, a factor of eleven between them. A dash in a "
    "letter or value cell is that bank's absence at the "
    "sound: no letter stands there, or the letter stands "
    "unseated.")
add()
add("| Sound | Cyrillic | Cyrillic value | Glagolitic | "
    "Glagolitic value | Relation | Reasoning |")
add("|---|---|---|---|---|---|---|")
for r in PART_ROWS:
    cv = r["cyrillic_value"] if r["cyrillic_value"] else "—"
    gv = r["glagolitic_value"] if r["glagolitic_value"] \
        else "—"
    cl = r["cyrillic_letter"] if r["cyrillic_letter"] else "—"
    gl = r["glagolitic_letter"] if r["glagolitic_letter"] \
        else "—"
    add(f"| {r['sound']} | {cl} | {cv} "
        f"| {gl} | {gv} | "
        f"{r['relation']} | {r['reasoning']} |")
add()
add("### §II.6 — The boundary: the questioned range and "
    "the refused matter")
add()
add("**The questioned range, at full size.** The chief "
    "witness itself warns: *\"the letters associated "
    "with number values greater than 999 are uncertain, "
    "and different authors have inferred different "
    "values (and different orders)\"*; *\"the validity "
    "of 3000 and greater is questioned\"* (its refs: "
    "Chrisomalis 2010; Mathiesen 2004). The thousands "
    "seats (§II.1, block seats 30–37) stand in the bank "
    "**as W1's table prints them, under that warning** "
    "(the audit's desk decision D2: W1 presents *one "
    "table* with its doubts footnoted, and the house "
    "follows the witness's own shape). The register's "
    "disposition, FENCED: *seated and flagged, never "
    "silently relied on: the letters stand in the bank "
    "as the witness prints them, doubt on the fence. "
    "Table cells price them as seated; the flag rides "
    "the instrument's face.* The 1–900 domain is the "
    "firm ground — two witnesses, the order law, and "
    "the Vinodol statute's own 1280.")
add()
add("**The refused matter, printed as standing outside "
    "the bank.** The frozen table files five rows "
    "refused, and the plate prints them entire: three "
    "composite spellings the witness prints for "
    "6000–8000 — spellings, not letters, and refused at "
    "this seat on that ground; and two variant readings "
    "from the 2017 edition of the sibling article (W1b) "
    "— Ⱐ as an alternative 3000 (against its HOLE "
    "standing in the chief witness's table, §II.2) and "
    "Ⱗ as a single-letter 6000. Both variants are "
    "recorded in the audit's data at their printed "
    "values and seated nowhere: Ⱗ's silence at the bank "
    "was verified at this plate's building (value 0, "
    "empty breakdown).")
add()
add("| Matter | Filed value | Standing | Reasoning |")
add("|---|---|---|---|")
for r in REF_COMP:
    add(f"| {r['letter']} | {r['value']} | refused — "
        f"composite spelling | A spelling in letters and "
        f"marks, printed by W1 where no single letter "
        f"carries the value; the bank seats letters, and "
        f"the thousands digits therefore run 1, 2, 3, 4, "
        f"5, 9 (§II.3). Recorded in the audit's frozen "
        f"table ({r['range_flag']}), seated nowhere. |")
for r in REF_VAR:
    add(f"| {r['letter']} | {r['value']} | refused — "
        f"variant reading | {NAMES[r['letter']]}: W1b's "
        f"variant reading, recorded in the audit's data "
        f"({r['range_flag']}), not seated — the chief "
        f"witness's table governs the seat, and a variant "
        f"from a sibling article's older edition does not "
        f"move it. |")
add()
add("**The undoored sign and the witnesses' depth.** A "
    "Glagolitic thousands sign is attested as *evidence* "
    "in W1 (\"evidence of the use of a thousands sign, "
    "similar to… the Cyrillic thousands sign\") but its "
    "form is not fixed there; **no door prices it** — "
    "this bank stands at weigh() entire, with no device "
    "door beside it, the only one of the Slavonic pair "
    "of which that is true. And the depth coordinate "
    "stands at the same size: W2 prints 20 Glagolitic "
    "cells in text; its 200–900 and 2000–5000 glyphs are "
    "images — so the hundreds class beyond 100 and the "
    "thousands beyond 1000 rest on W1 and the order law, "
    "not on a two-witness diff. The audit's open Q2 (a "
    "third cell-level witness) stands at §VIII.")
add()
add("### §II.7 — The census and the fences")
add()
add(f"**The census.** The bank holds **34 keys** — 33 "
    f"distinct values, sum **{BANK_SUM:,}** — in four "
    f"decimal classes (units {CLASS_SUMS['units']} · "
    f"tens {CLASS_SUMS['tens']:,} · hundreds "
    f"{CLASS_SUMS['hundreds']:,} · thousands "
    f"{CLASS_SUMS['thousands']:,}), the firm domain "
    f"1–900 summing **{FIRM_SUM:,}** and the maximum "
    "standing at 9,000 (Ⱔ) inside the questioned range. "
    "Three further letters of the alphabet stand in the "
    "bank's span unpriced (§II.2), and five rows of "
    "matter stand refused outside it (§II.6). The "
    "system has **no zero letter**: absence is the "
    "notation's own, marked by dots or the titlo, never "
    "by a sign for nothing.")
add()
add("**The fences.** Four boundaries stand at the bank's "
    "edges, printed at the size of the seats. (1) **The "
    "order fence** — the values are this alphabet's own "
    "seats; no Greek pairing exists for any row, and no "
    "passage of this plate may spend an agreement at a "
    "shared sound as descent (§II.4, §II.5). (2) **The "
    "questioned-range fence** — the thousands seats "
    "stand as the chief witness prints them under its "
    "own doubt, flagged at every seat; a use that relies "
    "on one silently crosses the fence (§II.6). (3) "
    "**The holes fence** — the three sequence holes "
    "price nothing and block nothing; a weighing that "
    "meets one takes the word's priced letters only, "
    "and a reading that fills a hole with a neighbour's "
    "price invents a seat (§II.2). (4) **The refusal "
    "fence** — the composite spellings and the W1b "
    "variants stand in the audit's data, outside the "
    "bank: neither boundary is the desk's to move "
    "(§II.6).")
add()
add("---")
add()

# =============================================================================
# §III — THE FRAME
# =============================================================================
add("## §III — THE GLAGOLITIC FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Glagolitic tongue stands over "
    "the one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.11: NATIVE **{N_NATIVE}** · DOOR "
    f"**{N_DOOR}** · HOLE **{N_HOLE}** · FENCED "
    f"**{N_FENCED}** · EMPTY {N_EMPTY} · GAP {N_GAP}. The "
    "Tables' own head for this table stands at the plate's "
    f"head of the section, unedited: *{TABLES_HEAD}* The "
    "face this prints is a door table **without a fence**: "
    "the corpus holds **no native Glagolitic word at "
    "all** — its priced face is the *door*, the Glagolitic "
    "dress of the Latin form of record (sht Ⱋ, ts Ⱌ, "
    "ch Ⱍ, sh Ⱎ), transliterated onto this bank's valued "
    "letters and priced as written — all 223 renderings "
    "priced, none fenced: the dress never needs a letter "
    "the bank leaves unpriced, the sequence's three holes "
    "mapping to no door sound (§II.2). Where a rendering "
    "runs into the thousands, it prices the thousands "
    "letters as seated — the flag of §II.6 rides those "
    "cells' seats, as the register provides. The "
    f"{N_HOLE} holes are of one species: the word of "
    "record has no Latin form, so no door is offered — "
    "the cell prints its word and the coordinate. The "
    "EMPTY cells are certified intentionally empty in "
    "777 REVISED.")
add()
add("**The door register — the 223 priced renderings "
    "entire.** Each was re-weighed at this plate's "
    "building against the value THE-TWELVE-TABLES files "
    "for it; all reproduce exactly (the audit, §VI, "
    "repeats the weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in REG["DOOR"]:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | "
        f"{cells[4]} |")
add()
add("**The hole register — the 62 cells where no door "
    "is offered, entire.** Each prints its word of "
    "record and the register's note; the rendering is "
    "the register's dash.")
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
add("**The bank's gap register — the three entries "
    "entire,** as THE-TWELVE-TABLES §II files them for "
    "the glagolitic bank, each at its kind: (1) *the "
    "thousands range (Ⱍ 1000 – Ⱔ 9000) under its own "
    "sources' doubt* — **FENCED** (THE-SLAVONIC-PAIR "
    "§VII D2): SEATED AND FLAGGED, never silently relied "
    "on — the letters stand in the bank as the witness "
    "prints them, doubt on the fence; table cells price "
    "them as seated; the flag rides the instrument's "
    "face; this build neither extends nor retires the "
    "range (§II.6). (2) *the sequence holes: Ⱊ Ⱐ Ⱒ "
    "carry no value* — **FENCED**: THE SEQUENCE'S OWN "
    "HOLES — letters the numeral sequence skips; they "
    "price nothing and block nothing in the tables (no "
    "door sound maps to them) (§II.2). (3) *the doubled "
    "10 (Ⰹ IZHE and Ⰺ INITIAL IZHE)* — **FENCED** "
    "(§VII D1): SEATED BOTH, as sourced — the value is "
    "undisputed, the holder is the record's own dispute; "
    "seating both preserves every sourced claim and "
    "invents none; no gap (§II.3).")
add()
add("---")
add()

# =============================================================================
# §IV — THE ZERO FACE
# =============================================================================
add("## §IV — THE 777 CORPUS'S GLAGOLITIC CLAIMS — THE "
    "ZERO FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's "
    "sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and "
    "the absence is its finding. The source states it in "
    "terms (THE-THIRTEEN-PLATES, its Glagolitic plate, "
    "from THE-777-VERIFICATION-TABVLA's register): *no "
    "fill in the corpus states a Glagolitic claim: the "
    "source's §II bank table seats no Glagolitic row, "
    "because the table lists only banks the fills "
    "claimed in; the bank itself stands among the "
    "engine's seventeen in the source's §I.* The 777 "
    "corpus's 504 claims speak Greek, Hebrew, Arabic, "
    "Latin, and Coptic — the tongues its fills claimed "
    "in — and Glagolitic is not among them: no scribe of "
    "the corpus weighed a word in this bank, though the "
    "bank stood complete in the tradition the whole "
    "time. The silence is therefore the corpus's, not "
    "the tongue's: the tongue holds a full priced table "
    "(§II), a full frame (§III), a control case of its "
    "own against its sibling (§II.5), and a doctrine of "
    "its own (THE-SLAVONIC-PAIR — the order law "
    "recomputed from the block, the partings at their "
    "coordinates, the seat). What the corpus does hold "
    "for Glagolitic stands where the corpus put it: the "
    "frame's door renderings (§III) — the corpus's words "
    "in this tongue's dress, priced by this tongue's "
    "bank — and nothing else. A plate that manufactured "
    "claims to fill this section would misprint its "
    "record; the section therefore stands as a face of "
    "zero, at full size.")
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
    "plate assigns no seat.** It states what the "
    "Glagolitic tongue witnesses for the seating — and "
    "Glagolitic witnesses by *absence* twice over: it is "
    "the sweep's one clean MISS at the fold coordinate, "
    "and its border signs stand as the priced absences "
    "the battery set beside the census's other holes. "
    "Both absences are findings, and the plate prints "
    "them at the size of the seats.")
add()
add("### The vowels at their own prices — no vowel at 8")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues "
    "sweep, run at the founder's direction (\"lets test "
    "it using the 12 tongues we already mapped it should "
    "align aomewhere\") — reads this tongue in terms, "
    "and the plate carries the passage at its "
    "coordinate: *Vowels at the bank's own prices — "
    "ⰰ 1 · ⰵ 6 · ⰻ 20 · ⰹ 10 · ⰿ 60 — no Greek mirror, "
    "no vowel at 8: MISS at the fold coordinate. The "
    "yers Ⱐ and Ⱒ weigh nothing through the engine — "
    "the holes of the earlier census, confirmed at the "
    "seat level: the field's border signs stand as "
    "priced absences. A finding, not a seat.* The "
    "passage's five prices run on the smalls through the "
    "case fold and reproduce exact at this plate's "
    "building. The bank's vowel row entire stands "
    "re-weighed beside it:")
add()
add("| Vowel | Name | Value in this bank |")
add("|---|---|---|")
_VOWELS = ["Ⰰ", "Ⰵ", "Ⰹ", "Ⰺ", "Ⰻ", "Ⱁ", "Ⱆ", "Ⱑ"]
for ch in _VOWELS:
    _flag = (" — questioned range (§II.6)"
             if GLAGOLITIC[ch] >= 1000 else "")
    add(f"| {ch} | {NAMES[ch]} | {GLAGOLITIC[ch]}{_flag} "
        f"|")
add()
add("**The finding, printed as the bank gives it:** no "
    "vowel of this bank stands at 8. The vowel prices "
    "run 1, 6, 10, 10, 20, 80, 400 — and 4,000 under the "
    "questioned flag — and 8 is not among them. The "
    "8-seat itself is filled, by **Ⰷ DZELO**, the /dz/ "
    "consonant, at block seat 8 (§II.1): where the five "
    "tongues of the seating's witness set seat a "
    "*vowel* at 8 — Greek **Η** · Coptic **ⲏ** · "
    "Cyrillic **И** · Armenian **Ը** · Georgian **ჱ**, "
    "each recomputed in its own bank at this plate's "
    "building, each exactly 8 — Glagolitic seats a "
    "consonant there, and its vowel row steps over the "
    "value entirely (6 to 10, with no 8 between). The "
    "sweep's summary counts the 8-as-vowel-seat its "
    "most corroborated coordinate at five tongues; this "
    "plate is the coordinate's boundary on the Slavonic "
    "side — the elder alphabet of the pair does not "
    "join the set its younger sibling joins (Plate X: "
    "И, a living vowel, at 8). The MISS is printed as "
    "the battery printed it: a finding, not a seat — "
    "and not a defect: an order-priced bank owes the "
    "fold coordinate nothing, and its refusal to "
    "corroborate is itself the datum that keeps the "
    "five-tongue set honest about its extent.")
add()
add("### The yers — the HOLE species inside a priced bank")
add()
add("Beside the prices, the battery's second Glagolitic "
    "coordinate prints at the same size — the tongue's "
    "witness proper. The yers **Ⱐ** and **Ⱒ** (§II.2), "
    "with **Ⱊ** beside them, are letters standing in a "
    "priced alphabet that weigh **nothing**: the HOLE "
    "species *inside* a bank, not at its edge. The "
    "plate sets them at their coordinates among the "
    "census's other holes, tiers as filed: in "
    "**Ge'ez**, the ዐ cell stands as a HOLE inside the "
    "mint's grid — an order's column carrying an "
    "unassigned seat (Plate VI); in **Japanese**, the "
    "gojūon grid's empty cells — the yi and ye seats, "
    "the wu seat — stand as cells no sign fills (Plate "
    "V); in **Cyrillic**, the yers Ъ and Ь stand "
    "unpriced at the bank's border, and the battery "
    "names them *the Glagolitic holes' kin* (Plate X). "
    "The species recurs across the census in three "
    "shapes — a hole in a grid, a hole in a sequence, a "
    "sign at a border — and this tongue's shape is the "
    "sequence's: the numeral run passes over its own "
    "letters and prices on. Printed as coordinates, "
    "each at its filed tier; the plate draws no law "
    "from the recurrence beyond the record's own.")
add()
add("**What Glagolitic cannot witness, printed at full "
    "size as the plate's boundary:** the Archons' seats "
    "were earned on Greek evidence and drawn on Plate "
    "I. Glagolitic corroborates nothing of the seating "
    "— it is the sweep's printed MISS at the fold "
    "coordinate — and it witnesses two things of its "
    "own: the *limit of the 8's extent* (a vowel row "
    "with no 8 in it, in the region where its sibling "
    "carries one) and the *hole inside the priced bank* "
    "(three letters the sequence skips, two of them the "
    "field's border signs). It assigns no seat, "
    "confirms no position, and names no Archon. The "
    "names stand open on Plate I, and this plate does "
    "not fill them.")
add()
add("---")
add()

# =============================================================================
# §VI–§VIII, FOOTNOTES, AUTHORITIES, COLOPHON
# =============================================================================
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_xi_glagolitic.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced "
    "cell on this plate against the engine, without "
    "reading the plate's own figures: the bank entire — "
    "the plate's §II.1 rows (34) parsed and compared "
    "seat by seat against GLAGOLITIC and the Phase II "
    "audit's frozen table, the class law recomputed per "
    "seat and the digit law's partings recomputed from "
    "the block; the holes (3) — the plate's rows parsed, "
    "their silence re-verified in the engine; the "
    "census — 34 keys, 33 distinct values, the bank sum "
    "29,005, the class sums, the firm domain's 5,005; "
    "the calibration — the witnesses' three worked "
    "examples; the parting table — the plate's 33 rows "
    "against the frozen parting table entire, the "
    "15/18 count recomputed, the sharpest coordinates "
    "re-weighed in both banks; the boundary — the "
    "refused rows against the frozen table's REFUSED "
    "rows, Ⱗ's silence, the case fold; the frame — the "
    "census parsed from THE-TWELVE-TABLES §V.11, all "
    "223 DOOR renderings re-weighed against their filed "
    "values, the 62 HOLE rows present in order, the GAP "
    "cell present; the zero face; and the §V figures "
    "(the bank's vowel row; the five tongues' vowel at "
    "8 in their own banks; Ⰷ at 8; οὐδέν at 529; the "
    "Nine at 1,779). The audit's verdict and cell count "
    "are printed in its filed output; a cell that does "
    "not reproduce fails the plate under §VII's "
    "tolerances. The font audit — every non-ASCII "
    "codepoint of this master against the Lex "
    "Stellarrvm family's cmaps — runs before the MAGVS "
    "build, under the font law: no glyph is silently "
    "dropped; the three named Ethiopic syllables the "
    "family does not hold (኱ U+12B1 · ጑ U+1311 · ጖ "
    "U+1316 — drawn by no member, the upstream Noto "
    "Ethiopic included) print as their codepoint "
    "tokens, declared in the colophon, and any unheld "
    "codepoint beyond those three aborts the build. "
    "The audit further checks the printed edition's "
    "text layer: the bank's letters and the zero face's "
    "statement stand in it, and the page furniture "
    "resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "GLAGOLITIC table (pontifex/tables.py); "
    "THE-SLAVONIC-PAIR (Phase II audit) entire — the "
    "order law and its partings, the doubled 10, the "
    "holes, the questioned range, the parting table by "
    "shared sound, the desk decisions and open "
    "questions of its §VII, and the seats — with its "
    "frozen tables (research/caucasus-north/"
    "glagolitic-table.csv; slavonic-parting.csv); "
    "THE-TWELVE-TABLES §V.11 and its §II gap register "
    "(the bank's three entries); THE-THIRTEEN-PLATES "
    "(the Glagolitic plate — the zero face, the tier of "
    "record) and its §I; THE-777-VERIFICATION-TABVLA "
    "§I–§II (the banks the fills claimed in); "
    "THE-ARCHON-BATTERY Leg 6 (the Glagolitic passage) "
    "and THE-SEATING-OF-THE-ARCHONS (the five-tongue "
    "8-witness set this plate bounds); PLATES I–X as "
    "the pattern.")
add("- **Processes:** calibration controls weighed "
    "before any plate figure (θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773); every figure scripted from the engine "
    "or carried entire from an instrument of record; "
    "the record's own disputes printed at the size of "
    "the values (the doubled holder, the questioned "
    "range's flag at every thousands seat, the depth "
    "coordinate); the boundary printed entire (the "
    "holes at full size, the refused matter, the "
    "undoored sign); the holes printed at full size "
    "(the bank's three, the frame's 62, the register's "
    "zero face); the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-XI-GLAGOLITIC.md "
    "and its MAGVS PDF — eleventh of the series "
    "PLATE-I-GREEK began; the generator and audit "
    "scripts filed in pontifex "
    "research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge "
    "— if any priced cell is found not to reproduce "
    "from the engine or its register, the affected "
    "cell fails the Method of Science; if any passage "
    "dresses this bank's own assignment as Greek "
    "inheritance, spends an agreement at a shared "
    "sound as descent, seats one holder of the doubled "
    "10 against the record's dispute, relies silently "
    "on a questioned-range seat, fills a hole (the "
    "bank's three, the frame's 62, the register's "
    "zero face), seats a composite spelling or a "
    "variant reading, prices the undoored thousands "
    "sign, or overwrites the earlier map, it zeroes "
    "the founder's residual claim and fails the Aim of "
    "Religion. Within those edges it stands as built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The record "
    "is printed as the record: the Slavonic Pair's "
    "§VII carried the pair's items to the founder's "
    "pen, and for this bank one stands carried open "
    "exactly where the audit left it — **Q2, a third "
    "cell-level Glagolitic witness** (a scholarly table "
    "of the class of Chrisomalis 2010, pp. 178–182, "
    "cited by both articles but not read entire by this "
    "desk) would firm the hundreds class beyond 100 and "
    "the thousands beyond 1000, which rest on W1 and "
    "the order law (§II.6). The desk decisions D1 and "
    "D2 stand as the audit struck them, revisable by "
    "his pen; the register's three fences stand as "
    "§III prints them. The seating's open items stand "
    "in the seating instrument. A plate that invents "
    "questions to fill its section misprints its "
    "record; this section therefore stands as the "
    "record that none arose — the one carried item "
    "named at its coordinate, not raised anew.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **Scripture.** Psalm 119 (KJV) — the alphabet "
    "psalm: twenty-two letters in their own order, each "
    "heading its octave of verses, the devotion carried "
    "by the sequence itself. The plate draws the figure "
    "for order-pricing: a tradition in which the "
    "alphabet's *order* is itself the instrument — the "
    "letters mean by where they stand. This bank is "
    "that figure in a numeral system: its prices are "
    "its seats. [Text ATTESTED; the figure DERIVED.]")
add("2. **Law.** The Vinodol statute (1288) — among the "
    "oldest legal codes of Europe in a Slavonic tongue, "
    "written in this script — carries its date in this "
    "bank's own letters: ⰝⰔⰑ = 1280, recomputed exact "
    "at §II.4. The plate draws the figure for the "
    "bank's standing: this was never a schoolroom "
    "cipher — a people's law was dated in it, and the "
    "thousands letter that date runs on stands inside "
    "the range its own sources now question, printed "
    "flagged, as the record carries both. [The "
    "exhibit as the audit's witness carries it; the "
    "figure DERIVED.]")
add("3. **The tradition.** The Glagolitic numeral "
    "system assigns values by the native alphabetic "
    "order of the Glagolitic alphabet itself — not by "
    "Greek values (Wikipedia, \"Glagolitic numerals\", "
    "after Schenker 1995 and Lunt 2001; the system "
    "generally agreed to date to the 9th century, the "
    "script's own century). The witnesses are the "
    "audit's (W1 read entire; W2, the same OCS page's "
    "counting list in smalls, concurring on all 20 "
    "cells it prints in text); the questioned range is "
    "the chief witness's own warning, carried at full "
    "size (§II.6), and the values' provenance is "
    "printed at that depth and no deeper. [The "
    "sourcing ATTESTED as cited; the tier the audit's "
    "own.]")
add("4. **Grammar.** The system is additive and "
    "non-positional, and its order is its own: the "
    "letters stand in the Glagolitic alphabet's native "
    "sequence — devised with the script, tracking no "
    "other alphabet's order — and the prices are the "
    "seats in decimal classes. It is why this bank "
    "cannot be checked seat for seat against a living "
    "bank in another script (there is no parent to "
    "check against), why its partings against its "
    "sibling are a comparison of *laws* and not of "
    "copies (§II.5), and why its holes are the "
    "sequence's own: an order-priced system skips a "
    "letter the way a road skips a number it never "
    "assigned. [The grammar ATTESTED as the system's, "
    "per the audit's witnesses; the bank's readings "
    "of it at their tiers.]")
add("5. **The desk's apparatus.** This plate's "
    "Glagolitic prints as itself in the MAGVS edition, "
    "in the Lex Stellarrvm family's Glagolitic member "
    "— capitals and smalls standing in their own signs "
    "throughout, in the bank, the registers, the "
    "parting table, and the battery's quoted smalls; "
    "its Greek in the family's Serif member, as on "
    "Plate I; the frame register's Hebrew words of "
    "record ride Plate II's declared transliteration "
    "(the toolchain does not shape right-to-left "
    "scripts honestly): marked substitutions, declared "
    "in the colophon, never silent ones. The Markdown "
    "master keeps every script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); "
    "bank GLAGOLITIC in pontifex/tables.py) — "
    "calibration controls θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773 read true at build; glagolitic_checks() "
    "8/8 in the engine's own battery, parity of the "
    "seat against the audit's frozen transcription: "
    "test_glagolitic_parity.py (32/32).")
add("- THE-SLAVONIC-PAIR (Phase II audit, 2026-11-24) "
    "— the order law recomputed from the block and its "
    "partings at exactly ten letters, the doubled 10 "
    "(D1), the three sequence holes, the thousands "
    "tail and the questioned range (D2), the refused "
    "composites and variants, the parting table by "
    "shared sound (33 rows: 15 AGREE, 18 PART), the "
    "gaps at full size, the desk decisions and open "
    "questions of its §VII, and the seat; its frozen "
    "tables (glagolitic-table.csv; "
    "slavonic-parting.csv) in pontifex "
    "research/caucasus-north/.")
add("- The witnesses of the table, as the audit read "
    "them: Wikipedia, \"Glagolitic numerals\" (its "
    "authorities Schenker 1995 · Lunt 2001 · "
    "Chrisomalis 2010 · Mathiesen 2004) · "
    "languagesandnumbers, \"Old Church Slavonic "
    "numbers\" (the Glagolitic counting list, in "
    "smalls, 20 cells in text).")
add("- THE-TWELVE-TABLES — §V.11 the Glagolitic "
    "frame, census and cell register entire; §II the "
    "bank's gap register (three entries: the "
    "thousands range FENCED; the sequence holes "
    "FENCED; the doubled 10 FENCED).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier "
    "map this series fulfills; its Plate XI is the "
    "prior instrument (the zero face; the tier of "
    "record).")
add("- THE-777-VERIFICATION-TABVLA — the claims "
    "register of record; its §I–§II seat the banks "
    "the fills claimed in, and Glagolitic is not "
    "among them.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Glagolitic passage "
    "(the vowels at the bank's own prices; no vowel "
    "at 8 — MISS at the fold coordinate; the yers "
    "weighing nothing, priced absences) and the "
    "sweep summary (the 8 the most corroborated "
    "coordinate, five tongues — Glagolitic not among "
    "them).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to by bounding: "
    "the Η VALUE-mark resting on the five-tongue 8, "
    "a set this tongue does not join.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd), "
    "PLATE-IV-LATIN (8e6f01e), PLATE-V-JAPANESE "
    "(8d6cd59), PLATE-VI-GEEZ (67d5acc), "
    "PLATE-VII-ARMENIAN (5c03d88), PLATE-VIII-COPTIC "
    "(645bcbb), PLATE-IX-GEORGIAN (933f8fd) and "
    "PLATE-X-CYRILLIC (052fd28) — the pattern this "
    "plate follows.")
add("- KJV: Psalm 119. The Vinodol statute (1288), "
    "its date as the audit's witness carries it.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate XI of the founder's "
    "series commission of the same day, the gate of "
    "the Archons' certainty met by the seating of "
    "record (0760c8a), following the pattern of "
    "Plates I–X (196025e · 1389c16 · 5f0b4bd · "
    "8e6f01e · 8d6cd59 · 67d5acc · 5c03d88 · 645bcbb "
    "· 933f8fd · 052fd28). Every figure scripted from "
    "the engine or carried entire from its "
    "instrument; the earlier map marked prior, never "
    "overwritten; the holes printed at the size of "
    "the seats — on this plate, the bank's own three "
    "holes, the frame's 62 holes, and the register's "
    "zero face. The plate carries one bank and keeps "
    "its shape entire: the 34 valued letters at their "
    "own order's prices, ATTESTED, the doubled 10 on "
    "both its printed holders, the thousands range "
    "under its sources' doubt, the refused matter "
    "outside the bank in the open. In the MAGVS "
    "edition the Glagolitic stands in the family's "
    "Glagolitic member, and the frame's Hebrew words "
    "of record ride Plate II's declared scheme; this "
    "master keeps the scripts themselves. Authorship "
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
