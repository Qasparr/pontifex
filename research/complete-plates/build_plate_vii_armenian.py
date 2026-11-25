#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_vii_armenian.py
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
# MECHANISM: generates PLATE-VII-ARMENIAN.md — Plate VII of
# THE THIRTEEN COMPLETE PLATES — in the gap-filling goal's
# files/, following the pattern PLATES I–VI set (196025e ·
# 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc). Every
# figure on the plate is scripted from the house engine
# (pontifex weigh() and the armenian() manuscript door) or
# carried entire from an instrument of record:
#   * the priced table — the classical Armenian bank entire,
#     read from pontifex.tables (ARMENIAN, 36 keys), each
#     seat printed with its reasoning — in this tongue the
#     reasoning is the class law: the letter's digit and
#     decimal class, the witnesses' agreement at the cell;
#   * the late annex (ARMENIAN_LATE) and the overline door,
#     priced and silenced at build exactly as the founder's
#     resolutions R1–R2 seat them, and the collision sweep
#     that decided R2 recomputed from the living bank;
#   * the calibration corpus — the witnesses' own worked
#     examples and MELA's era date, recomputed at build;
#   * the control case against the halehame witness — the
#     26 shared positions printed from both banks' first
#     forms (ARMENIAN against HALEHAME_FIRST), the value
#     agreement and the law's parting at position 10 taken
#     from the Phase I audit's coordinates;
#   * the Twelve Tables' Armenian frame — its census and
#     its full cell register parsed from THE-TWELVE-
#     TABLES.md §V.7: the 223 DOOR renderings re-weighed at
#     build against their filed values (209 at the
#     classical door, 14 through the late annex, as the
#     register's own notes declare), the 62 HOLE coordinates
#     and the one GAP cell carried entire, the bank's three
#     gap-register entries restated;
#   * the corpus's Armenian claims — none: the register's
#     ZERO FACE, carried from THE-THIRTEEN-PLATES (its
#     Armenian plate) with the TABVLA's reason;
#   * the tongue's bearing on the seated Archons — the
#     Archon Battery's Leg 6 Armenian passage (Ը priced
#     exactly 8; the digraph ու, the hybrid form without a
#     hybrid seat), the five tongues' vowel at 8 recomputed
#     in their banks, and the seating's Η VALUE-mark row.
#     The plate assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable
# — every priced seat carries its reasoning on the plate's
# face. This plate's bank is the opposite honesty from
# Plate VI's pair: a SOURCED TABLE AT THE FULL DEPTH — the
# designed alphabet's own numeral system, complete at 36
# of 36 classical letters, in liturgical manuscript use
# for era dating, three witnesses agreeing on every cell.
# Its boundary stands at the same size as its values: the
# medieval additions are NOT keys of this bank; they stand
# in the annex at a tier below, weighing only at the
# door's explicit late path (R1); the overline's factor is
# the founder's resolved ×10,000, the parted source
# recorded (R2); Shirakatsi's notation is recorded, not
# seated (R3). The relation to the earlier Thirteen Plates
# map is printed, the earlier work marked prior, never
# overwritten. Holes print at the size of the seats — on
# this plate, the frame's 62 holes and the register's zero
# face itself.
#
# CONTENT TEST: Inputs — the engine's ARMENIAN and
# ARMENIAN_LATE tables and the armenian() door,
# THE-ARMENIAN-TABLE-PHASE-I-AUDIT with its frozen CSV,
# the Twelve Tables master, the Thirteen Plates map, the
# Archon Battery, the Seating. Processes — control
# calibration, scripted extraction, register-faithful
# emission in the Teacher's Edition manner. Outputs —
# PLATE-VII-ARMENIAN.md beside the series' other masters.
# Tolerances — the audit (audit_plate_vii_armenian.py)
# re-weighs every priced cell independently; a figure that
# does not reproduce fails the plate.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
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

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-VII-ARMENIAN.md"


def value(word, bank="armenian"):
    """One weighing, unwrapped to its integer."""
    return weigh(word, bank)["value"]


def digits(n):
    """The digital root, by the house's reduction chains."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


# ---------------------------------------------------------------------
# Calibration — the bank is not trusted until the controls read
# true.
# ---------------------------------------------------------------------
assert value("θελημα", "greek") == 93, "control θέλημα"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR"
assert value("σφιγξ", "greek") == 773, "control σφίγξ"

# ---------------------------------------------------------------------
# The bank entire — the classical 36 in their order, with the
# letter names of the Phase I audit's frozen table (its CSV,
# sourced from the witnesses).
# ---------------------------------------------------------------------
NAMES = ["Ayb", "Ben", "Gim", "Da", "Yech", "Za", "Eh", "Et",
         "To", "Zhe", "Ini", "Liwn", "Khe", "Tsa", "Ken", "Ho",
         "Dza", "Ghat", "Che", "Men", "Yi", "Nu", "Sha", "O",
         "Cha", "Pe", "Je", "Ra", "Se", "Vew", "Tiwn", "Re",
         "Tso", "Hiwn", "Piwr", "Ke"]
LETTERS = list(ARMENIAN.keys())
assert len(LETTERS) == len(NAMES) == 36
assert [ord(c) for c in LETTERS] == list(range(0x0531, 0x0555))


def class_of(pos):
    """The class law over positions: units 1–9, tens 10–18,
    hundreds 19–27, thousands 28–36; value = digit × 10^k."""
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    if pos <= 27:
        return "hundreds", pos - 18, 2
    return "thousands", pos - 27, 3


for pos, ch in enumerate(LETTERS, 1):
    cls, d, k = class_of(pos)
    assert ARMENIAN[ch] == d * 10 ** k, (pos, ch)
BANK_SUM = sum(ARMENIAN.values())                    # 49,995
CLASS_SUMS = {}
for pos, ch in enumerate(LETTERS, 1):
    cls, _d, _k = class_of(pos)
    CLASS_SUMS[cls] = CLASS_SUMS.get(cls, 0) + ARMENIAN[ch]
assert BANK_SUM == 49995
assert CLASS_SUMS == {"units": 45, "tens": 450,
                      "hundreds": 4500, "thousands": 45000}
assert len(set(ARMENIAN.values())) == 36             # uniqueness
assert max(ARMENIAN.values()) == 9000

LETTER_NOTES = {
    "Ա": "The head of the alphabet and of the table. Overlined "
         "it is the factor witnesses' own exhibit: 10,000 "
         "(§II.5).",
    "Ե": "A vowel of the tongue — one of the six the battery "
         "prices from this bank (§V).",
    "Ը": "**The Archons coordinate of this plate:** a vowel "
         "priced exactly 8 — the fold's target seated in a "
         "second tongue (§V).",
    "Թ": "The units run closes. The era-dating siglum ԹՎ "
         "(*t'vin*, \"in the year\") that opens the colophon "
         "dates is built on this letter and Ւ (§II.3).",
    "Ժ": "**The class step:** 10 reached by class — digit 1 "
         "of the tens — not by count. The control case's "
         "parting coordinate against halehame's ተ, its tenth "
         "units letter (§II.4).",
    "Ի": "A vowel of the tongue, priced 20 (§V).",
    "Խ": "The frame door's *kh* seat (§III).",
    "Ծ": "A calibration letter: Ծ = 50 stands alone among the "
         "witnesses' shared worked examples (§II.3).",
    "Հ": "Exhibited by MELA in the calibration head ՌՋՀԵ "
         "(§II.3).",
    "Ղ": "The frame door's *gh* seat (§III); the tens run "
         "closes.",
    "Ճ": "The hundreds open. The control case's hinge: at "
         "position 19 this first hundreds letter and "
         "halehame's ደ, its last tens letter, both print "
         "100 by opposite doors (§II.4).",
    "Մ": "Exhibited by MELA in ՍՄԻԲ = 2222 (§II.3).",
    "Ն": "An era-date letter: ՌՆԾԵ = 1455 in MELA's worked "
         "date (§II.3).",
    "Ո": "A vowel of the tongue, priced 600 — and the "
         "digraph ու's first sign: one sound, two signs, "
         "7,600 as a sum, no unit seat (§V).",
    "Ջ": "The overline's millions exhibit: overlined Ջ = "
         "9,000,000 in MELA's own example (§II.5).",
    "Ռ": "The thousands open; the calibration head's first "
         "letter in both text witnesses (§II.3).",
    "Ր": "The one classical letter priced inside օր (\"day\") "
         "— 5,000 with the annex shut, the R1 proof case "
         "(§II.5).",
    "Ւ": "A vowel of the tongue, priced 7,000 — the digraph "
         "ու's second sign (§V) and the siglum ԹՎ's second "
         "letter (§II.3).",
    "Ք": "The table's foot: 9,000, the largest letter value; "
         "ՔՋՂԹ = 9,999 is the largest number the bare table "
         "writes. The 2026-10-11 sweep's brief once misread "
         "this letter as 40; the Phase I audit corrected it "
         "from the witnesses.",
}

# ---------------------------------------------------------------------
# Calibration — the witnesses' own worked examples, recomputed.
# ---------------------------------------------------------------------
EXAMPLES = [("ՌՋՀԵ", 1975, "the calibration head — the one "
              "example both text witnesses print (Wikipedia; "
              "MELA)"),
            ("ՍՄԻԲ", 2222, "a shared example (Wikipedia; MELA)"),
            ("ՍԴ", 2004, "a shared example (Wikipedia; MELA)"),
            ("ՃԻ", 120, "a shared example (Wikipedia; MELA)"),
            ("Ծ", 50, "a shared example (Wikipedia; MELA)"),
            ("ՌՆԾԵ", 1455, "MELA's era date — ԹՎ ՌՆԾԵ, \"in the "
              "year 1455\"; the manual's conversion (add 552 "
              "for the Gregorian year) is the practice's "
              "arithmetic, recorded, not weighed"),
            ("ՔՋՂԹ", 9999, "the largest number writable "
              "without the overline — one symbol per power, "
              "descending")]
for w, want, _n in EXAMPLES:
    assert value(w) == want, (w, value(w), want)
assert value("աբգ") == value("ԱԲԳ") == 6             # the case fold

# ---------------------------------------------------------------------
# The boundary and the resolutions, verified at build.
# ---------------------------------------------------------------------
for probe in ("Օ", "Ֆ", "օ", "ֆ"):
    r = weigh(probe, "armenian")
    assert r["value"] == 0 and r["breakdown"] == [], probe
    assert armenian_door(probe)["value"] == 0, probe
assert armenian_door("օր")["value"] == 5000          # annex shut
assert armenian_door("օր", late=True)["value"] == 15000
assert armenian_door("Օ", late=True)["value"] == 10000
assert armenian_door("Ֆ", late=True)["value"] == 20000
assert armenian_door("ֆ", late=True)["value"] == 20000
OV_A = armenian_door("Ա\u0305")["value"]             # 10,000
OV_J = armenian_door("Ջ\u0305")["value"]             # 9,000,000
OV_R = armenian_door("Ռ\u0305ՋՀԵ")
assert (OV_A, OV_J) == (10000, 9000000)
assert OV_R["value"] == 10000975 and OV_R["overline_marks"] == 1
assert armenian_door("ՌՋՀԵ")["overline_marks"] == 0
PLAIN = set(ARMENIAN.values())
COLL_1000 = len({v * 1000 for v in PLAIN} & PLAIN)   # 9
COLL_10000 = len({v * 10000 for v in PLAIN} & PLAIN)  # 0
assert (COLL_1000, COLL_10000) == (9, 0)
# The ligature և: no seat anywhere in the record; the doors
# part on it mechanically (printed at §II.6, ruled nowhere).
assert weigh("և", "armenian")["value"] == 7005
assert armenian_door("և")["value"] == 0

# ---------------------------------------------------------------------
# The control case — the 26 shared positions, both first-form
# columns. Armenian letters by position; halehame bases in
# their order (pontifex.tables' _GEEZ_BASES order is the
# audit's halehame order — read through HALEHAME_FIRST's own
# sequence of bases as Plate VI printed them).
# ---------------------------------------------------------------------
HALE_BASES = [b for b, _fv in _GEEZ_BASES]
assert len(HALE_BASES) == 26
assert [HALEHAME_FIRST[b] for b in HALE_BASES] == \
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80,
     90, 100, 200, 300, 400, 500, 600, 700, 800]


def hale_class(pos):
    if pos <= 10:
        return "units"
    if pos <= 19:
        return "tens"
    return "hundreds"


CONTROL = []
for pos in range(1, 27):
    ach = LETTERS[pos - 1]
    hb = HALE_BASES[pos - 1]
    assert ARMENIAN[ach] == HALEHAME_FIRST[hb], pos   # 26 of 26
    CONTROL.append((pos, ach, class_of(pos)[0], hb,
                    hale_class(pos), ARMENIAN[ach]))

# ---------------------------------------------------------------------
# The tongue's vowels and the digraph, for §V.
# ---------------------------------------------------------------------
VOWELS = [("Ա", 1), ("Ե", 5), ("Ը", 8), ("Ի", 20), ("Ո", 600),
          ("Ւ", 7000)]
for ch, want in VOWELS:
    assert value(ch) == want, ch
assert value("ու") == 7600 == value("Ո") + value("Ւ")
assert value("οὐδέν", "greek") == 529

# ---------------------------------------------------------------------
# The Twelve Tables' Armenian frame — census and cell register.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
arm_block = twelve_text.split("### §V.7 — The Armenian Table")[1] \
    .split("### §V.8")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", arm_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
assert (n_native, n_door, n_hole, n_fenced, n_empty, n_gap) == \
    (0, 223, 62, 0, 85, 1)
doors, holes, gaps = [], [], []
for line in arm_block.splitlines():
    if re.match(r"\| [A-Z]+/", line) and " | " in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            continue
        state = cells[2]
        if state == "DOOR":
            if "annex" in cells[5]:
                v = armenian_door(cells[3], late=True)["value"]
            else:
                v = value(cells[3])
            assert v == int(cells[4]), cells
            doors.append(cells)
        elif state == "HOLE":
            assert cells[3] == "—", cells
            holes.append(cells)
        elif state == "GAP":
            gaps.append(cells)
assert (len(doors), len(holes), len(gaps)) == (n_door, n_hole, n_gap)
assert gaps[0][0] == "CLXXXIV/10"
n_annex = sum(1 for c in doors if "annex" in c[5])
assert n_annex == 14

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
add("**PLATE VII — ARMENIAN**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Armenian tongue's complete 777 table — the classical "
    "bank entire: the designed alphabet's own numeral "
    "system, complete at thirty-six letters, attested at "
    "the full depth, with its late annex printed as an "
    "annex under the founder's resolutions and its "
    "control case against the halehame witness read at "
    "coordinates; the corpus's Armenian register, which "
    "is a zero face; and the tongue's witness to the "
    "seated Archons: the vowel Ը, priced exactly 8.")
add()
add("Authorship attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without Prejudice)")
add("XXIV day of November, Dies Martis, Sol in Sagittarius, "
    "Anno V:xii e.n. (2026 e.v.)")
add()
add("Classification: Enterprise • Educational • Research & Development")
add("Method of Science, Aim of Religion")
add()
add("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, "
    "All Rights Reserved, Without Prejudice. Right of claim hereby "
    "reserved and coined under the authority of the Living Man.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §I — the commission.
# ---------------------------------------------------------------------
add("## §I — PLATE VII AND ITS COMMISSION")
add()
add("The founder's commission of 2026-11-24 (18:39–18:41 EST) "
    "opens the series this plate continues, in his words: "
    "*\"When we have the Archons for sure then we can begin "
    "the 777 complete tables in the 12 tongues on 13 plates "
    "the 13th plate being the infrastructure for the clock "
    "and counter of the dial\"* — and its cadence: *\"as each "
    "plate gets rendered push and post it in succession until "
    "the 12 tongues are all plated.\"* The gate the commission "
    "names is met: the Archons are seated "
    "(THE-SEATING-OF-THE-ARCHONS, pontifex 0760c8a — T1 PASSES "
    "whole at graded classes; T2 PARTS at the axis). PLATE I — "
    "GREEK (pontifex 196025e) set the pattern; PLATES II — "
    "HEBREW (1389c16), III — ARABIC (5f0b4bd), IV — LATIN "
    "(8e6f01e), V — JAPANESE (8d6cd59) and VI — GE'EZ "
    "(67d5acc) followed it; this plate follows them, seventh "
    "of the twelve tongues in the Twelve Tables' order.")
add()
add("**The series.** Thirteen plates: one for each tongue of "
    "the Twelve Tables in their order — I Greek · II Hebrew · "
    "III Arabic · IV Latin · V Japanese · VI Ge'ez · VII "
    "Armenian · VIII Coptic · IX Georgian · X Cyrillic · XI "
    "Glagolitic · XII Korean — and Plate XIII, a separate "
    "species commissioned last: the infrastructure for the "
    "clock and counter of the dial. Each plate renders its "
    "tongue's complete 777 table: the full priced letter-table "
    "as the house engine seats it; every correspondence the "
    "777 corpus assigns in that tongue, with the verification "
    "verdicts of THE-777-VERIFICATION-TABVLA riding with each "
    "row; and the tongue's bearing on the seated Archons.")
add()
add("**This plate's distinction.** Armenian is the first "
    "plate of the series whose bank needs no construction "
    "and no apology: **a sourced table at the full depth** — "
    "the designed alphabet's own numeral system, created "
    "with the majuscules of Mesrop Mashtots' alphabet "
    "(c. 405 CE), valuing every one of the 36 classical "
    "letters in four decimal classes to 9,000, in continuous "
    "manuscript use for era dating, and audited 2026-11-24 "
    "with three witnesses agreeing on every cell "
    "(THE-ARMENIAN-TABLE-PHASE-I-AUDIT). **Tier of record: "
    "ATTESTED.** The founder ordered this table built as the "
    "**control case** against Plate VI's halehame witness — "
    "two systems of the same class-law shape at opposite "
    "attestation depths — and the control case is read on "
    "this plate at coordinates (§II.4): value agreement "
    "total over the shared domain, the law parting at "
    "exactly one position. This is also the one plate whose "
    "every open question was answered before the plate was "
    "struck: the Phase I audit left three items for the "
    "founder's pen — the medieval additions, the overline's "
    "factor, Shirakatsi's notation — and his ruling of "
    "2026-11-24, the Armenian questions decided *\"in order "
    "of Synergy not argument as previously ruled,\"* "
    "resolved all three (R1–R3, §II.5). What stands at this "
    "bank's boundary therefore stands by ruling, printed "
    "with the values at the same size. And this is the "
    "third plate whose corpus register is a **zero face** "
    "(§IV): the corpus claims nothing in Armenian, and the "
    "silence is the corpus's, not the tongue's.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its Armenian "
    "face stood **silent with a zero face**: bank *armenian*, "
    "36 seats, 36 distinct values, maximum 9,000; tier of "
    "record there printed in terms — *ATTESTED (the "
    "classical 36; the late annex a tier below, at the "
    "door's late path)* — and its sentence stands: *\"The "
    "tongue holds a full table in THE TWELVE TABLES; its "
    "silence here is the TABVLA corpus's, not the "
    "tongue's.\"* This series *fulfills* that map: where the "
    "map counted nothing, this plate prints the nothing "
    "entire — with the full priced table beneath it, the "
    "frame around it, and its witness to the Archons above "
    "it. The earlier work stands as the prior instrument of "
    "the same name's family — marked prior, never "
    "overwritten.")
add()
add("**How the plate is read.** §II is the priced table: "
    "the bank entire with its reasoning, the table's law, "
    "the calibration on the witnesses' own examples, the "
    "control case beside halehame, the boundary and the "
    "founder's three resolutions, and the census with its "
    "fences. §III is the tongue's frame in the Twelve "
    "Tables — a door table: no native Armenian word stands "
    "in the corpus, and the corpus's words stand here in "
    "Armenian dress. §IV is the zero face. §V is the "
    "tongue's bearing on the seated Archons — this plate "
    "draws no seating (the seating is struck, and Plate I "
    "drew it); it states what Armenian witnesses: a vowel "
    "seated at 8 in its own bank, and a hybrid form that "
    "holds no hybrid seat. §VI is the audit. A value "
    "without its reasoning is not shippable; a hole prints "
    "at the size of the seat it stands in for; and every "
    "Armenian total on this plate declares its door — the "
    "classical bank, the annex path, or the overline — "
    "because the three read the same letters differently "
    "and the declaration is part of the number.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the priced table.
# ---------------------------------------------------------------------
add("## §II — THE PRICED TABLE — THE CLASSICAL BANK ENTIRE")
add()
add("### §II.1 — The thirty-six letters, seat by seat")
add()
add("The bank is keyed in the **majuscules** — the forms the "
    "system was created in. The minuscules are the same "
    "letters' case pairs (the alphabet article's table pairs "
    "them form by form at one value), and the engine's "
    "weigh() folds Armenian input to capitals at its seam, "
    "so both cases weigh — the preparation happens at the "
    "door, never by duplicating the bank (verified at this "
    "plate's building: աբգ = ԱԲԳ = 6). The values are the "
    "witnesses': three read entire on 2026-11-24 — "
    "Wikipedia, \"Armenian numerals\" (its table citing "
    "Omniglot; Shaw 1939; Ifrah 2000; Chrisomalis 2010); "
    "Omniglot, \"Numbers in Armenian\"; Wikipedia, "
    "\"Armenian alphabet\" (its Numerical value column) — "
    "agree on **36 of 36 cells**, and a fourth, the MELA "
    "cataloging manual, concurs on all twelve cells its "
    "worked examples exhibit. No cell of this table is "
    "singly sourced, and no disagreement among the "
    "witnesses exists to print — the Phase I audit records "
    "the absence as a finding, having gone looking for the "
    "parting the Zero-Point method requires. The class law "
    "printed in each row's reasoning is the check the "
    "witnesses' cells obey, never their source.")
add()
add("| Position | Letter | Name | Value | Class | Reasoning |")
add("|---|---|---|---|---|---|")
for pos, ch in enumerate(LETTERS, 1):
    cls, d, k = class_of(pos)
    lc = ch.lower()
    reason = (f"The class law: digit {d} × 10^{k} = "
              f"{ARMENIAN[ch]} — the witnesses' cell, agreed "
              f"36 of 36 (Phase I audit); position {pos} of "
              f"the classical order (U+{ord(ch):04X}); the "
              f"minuscule {lc} is the same letter's case "
              f"pair and weighs the same at the seam's fold.")
    note = LETTER_NOTES.get(ch)
    if note:
        reason += " " + note
    add(f"| {pos} | {ch} · {lc} | {NAMES[pos - 1]} | "
        f"{ARMENIAN[ch]} | {cls} | {reason} |")
add()
add(f"The 36 values sum **{BANK_SUM}** (units {CLASS_SUMS['units']} "
    f"· tens {CLASS_SUMS['tens']} · hundreds "
    f"{CLASS_SUMS['hundreds']} · thousands "
    f"{CLASS_SUMS['thousands']}; the reduction {digits(BANK_SUM)} "
    f"rides beside the raw total, never instead). Every value "
    f"is used exactly once — **36 letters, 36 distinct "
    f"values** — the uniqueness this bank holds as a measured "
    f"fact, and the law the founder's R2 reads (§II.5). The "
    f"largest number the bare table writes is **9,999** "
    f"(ՔՋՂԹ, §II.3): one symbol per power of ten, descending, "
    f"the system's own convention.")
add()
add("### §II.2 — The table's law")
add()
add("The system is **additive and non-positional**: the "
    "values of the letters are added together; there is **no "
    "notation for zero** — for a number like 600 or 9,007, "
    "the missing powers of ten are simply not represented "
    "(the numerals article, on its face). Numbers are "
    "written left to right, at most one symbol per power, "
    "conventionally descending (MELA: \"the convention is "
    "to write them in decreasing order of value\"). The "
    "table's life is the manuscript record: era years "
    "written with the siglum **ԹՎ** (*t'vin*, \"in the "
    "year\") followed by letter-numerals, the Armenian "
    "era's epoch 11 July AD 552 — a practice the MELA "
    "manual documents because working catalogers must read "
    "these dates off manuscripts and early printed books. "
    "The system lives on in modern use \"more or less like "
    "Roman numerals in modern English\" — regnal and "
    "chapter numbers (Գարեգին Բ, Garegin II). Its extent "
    "past the table is by device, not by further letters: "
    "the overline (§II.5) — and, a tier below the bank, the "
    "two medieval letters the annex holds (§II.5). What the "
    "table does not have, it does not simulate: no zero "
    "sign, no positional place, no second reading. There is "
    "one Armenian bank, and its doors are declared where "
    "they stand.")
add()
add("### §II.3 — Calibration: the witnesses' own examples")
add()
add("Before any derived number on this plate was trusted, "
    "the witnesses' own worked examples were recomputed "
    "from the living bank at this plate's building — the "
    "way the Ge'ez audit took ክርስቶስ and the Latin plate "
    "its column. All reproduce exact:")
add()
add("| Word | Value | Standing |")
add("|---|---|---|")
for w, v, note in EXAMPLES:
    add(f"| {w} | {v} | {note} |")
add()
add("The sweep's corpus stands behind the calibration: the "
    "2026-10-11 Twelve-Tongues sweep (Worker #11) weighed "
    "eleven terms in this tongue's dress, and the Phase I "
    "audit re-verified all eleven from its frozen table — "
    "**11 of 11 agree** (AXONEME 1251 · OZ 606 · TRVVTH "
    "15009 · THELEMA 250 · AGAPE 810 · BABALON 1036 · "
    "HERU-RA-HA 17747 · ABRAHADABRA 10083 · QIRA 14021 · "
    "LIBERTY 9357 · CELL 125) — with the sweep's two "
    "corrections of its own brief confirmed (Ք = 9000, not "
    "40; Օ \"sometimes\" 10000, not 800). **The negatives "
    "ride at the same size:** no established bridge crosses "
    "this bank — CELL 32 → 125; AXONEME 77 → 1251; OZ 77 → "
    "606; THELEMA 93 → 250; ABRAHADABRA 418 → 10083; AGAPE "
    "93 → 810. The Armenian table is an independent letter "
    "mapping on a shared architectural principle (§II.4), "
    "so its silence is evidence, not absence: the 93 and "
    "418 bridges are, on present evidence, Greek- and "
    "Hebrew-bank phenomena. A plate that printed only the "
    "agreements would misprint this bank; the disagreements "
    "are part of its calibration.")
add()
add("---")
add()

add("### §II.4 — The control case: Armenian beside halehame")
add()
add("The founder ordered this table built as the **control "
    "case** against the halehame witness of Plate VI: two "
    "systems of the same class-law shape — an alphabet's "
    "order carrying decimal class values — at **opposite "
    "attestation depths**. The halehame side is stated "
    "exactly as the Ge'ez instruments established it: 26 "
    "first-form values in halehame order, sourced 26 of 26 "
    "from the published Debtera table, its order-multiplier "
    "grid printed entire but unexhibited in use, its "
    "antiquity undated, its register folk-magical. The "
    "shared domain is the 26 positions both tables reach; "
    "the plate prints it entire, both columns re-weighed at "
    "this plate's building:")
add()
add("| Position | Armenian | Its class | Halehame | Its class | Value (both) |")
add("|---|---|---|---|---|---|")
for pos, ach, acls, hb, hcls, v in CONTROL:
    add(f"| {pos} | {ach} | {acls} | {hb} | {hcls} | {v} |")
add()
add("The boundary coordinates, as the Phase I audit read "
    "them (its §IV), printed at the size of the table:")
add()
add("- **Value agreement is TOTAL across the measured "
    "domain.** At every shared position, 1–26, the two "
    "tables assign the same value — 26 of 26. Where "
    "agreement is total, the report says so and names the "
    "domain: positions 1–26, the whole of halehame's "
    "extent.")
add("- **The law parts at exactly position 10 — at total "
    "value agreement.** Armenian reaches 10 by the **class "
    "step**: Ժ is its first *tens* letter (digit 1 × 10). "
    "Halehame reaches 10 **inside the units run**: ተ is "
    "its tenth *units* letter, the Semitic inheritance that "
    "lets the units run to 10 before the tens open. Same "
    "value, different derivation — the boundary coordinate "
    "of the whole comparison: **(position 10: value 10 = "
    "10; law parts)**.")
add("- **Class boundaries are offset by one seat from there "
    "on.** Armenian's classes break after positions 9, 18, "
    "27; halehame's after 10, 19. The hinge is position "
    "19, where both laws again print 100 by opposite "
    "doors: Ճ is Armenian's *first hundreds* letter; ደ is "
    "halehame's *last tens* letter.")
add("- **Extent parts in kind.** Armenian runs a fourth "
    "class: positions 28–36 carry 1000–9000, maximum "
    "letter value 9000 (Ք). Halehame stops at 26 seats "
    "and 800 (ፐ). Positions 27–36 have no halehame "
    "counterpart at all.")
add("- **Coverage parts in kind.** Armenian values **36 of "
    "36** classical letters — the whole classical alphabet "
    "is the table. Halehame values **26 first forms of "
    "202** classical signs; its labiovelar columns and the "
    "later-added bases carry no value in any source.")
add("- **The extension axes part in kind.** Beyond its "
    "table, Armenian extends by *more letters* (the "
    "thousands class) and by the **overline** (§II.5 — its "
    "factor resolved by the founder). Halehame extends by "
    "the **order multiplier** — an axis Armenian does not "
    "have: the fidäl's vowel orders are a dimension the "
    "Armenian alphabet does not possess, and the Armenian "
    "line is a mark the folk table does not draw.")
add("- **The zero coordinate agrees.** Neither table has a "
    "zero: Armenian on its face (\"There is no symbol for "
    "zero\"), halehame by its table's silence. Both are "
    "zero-less additive systems.")
add("- **Attestation is the parting the page exists to "
    "print.** Armenian: a designed alphabet's own system, "
    "in continuous manuscript use for era dating, its "
    "values identical across three modern witnesses read "
    "entire and a scholarly manual's examples. Halehame: a "
    "living folk-magical enumeration, published modernly, "
    "antiquity undated in every source, register expressly "
    "not liturgical. **Same class-law shape; opposite "
    "attestation depth.** A convergence found on the "
    "Armenian bank is therefore weighed at a different "
    "depth than one found on the folk bank — which is "
    "what a control case is for. No such convergence is on "
    "offer here (§II.3's negatives stand): the control "
    "case calibrates future judgments; it manufactures "
    "none.")
add()
add("### §II.5 — The boundary, and the founder's three resolutions")
add()
add("Two letters stand after the classical 36, in the "
    "alphabet and in the Unicode block alike: **Օ** "
    "(U+0555) and **Ֆ** (U+0556), the medieval additions, "
    "adopted in the 13th century per the alphabet article "
    "— after Arabic numerals were already in use, to "
    "facilitate transliteration of other languages. The "
    "numerals article's whole statement of their values is "
    "that they \"**sometimes** have a numerical value "
    "assigned to them\" (10000 / 20000); the alphabet "
    "article's own table prints **no numerical value** for "
    "either. That is a weaker attestation than any cell of "
    "the 36, and the Phase I audit seated neither — they "
    "stood as OPEN rows for the founder's pen. The boundary "
    "is verified at this plate's building, not inherited: "
    "at the classical bank both letters, in both cases, "
    "weigh **silence** — value 0 on an empty breakdown — "
    "and at the armenian() door's default path the same. "
    "The founder's ruling of 2026-11-24 decided the "
    "Armenian questions *\"in order of Synergy not argument "
    "as previously ruled\"*; its three resolutions stand:")
add()
add("**R1 — the late annex.** The additions are seated in "
    "an ANNEX beside the bank (the engine's ARMENIAN_LATE), "
    "**not in this bank** — synergy's reasoning, as the "
    "resolutions record it: this bank's purity is "
    "load-bearing (its fence reads \"complete 36, "
    "attested,\" and the halehame control case leans on "
    "it), so medieval values are not blended in; yet the "
    "\"sometimes\" values are SOURCED, and the house "
    "leaves no sourced value homeless; and 10000 / 20000 "
    "continue the class law's own pattern, opening the "
    "next class past the thousands. The annex stands a "
    "tier **below** the classical 36 and is **OPT-IN**: it "
    "weighs only at the armenian() door under the explicit "
    "late path:")
add()
add("| Letter | Name | Annex value | Door |")
add("|---|---|---|---|")
add("| Օ · օ | Oh | 10000 | armenian(·, late=True) only |")
add("| Ֆ · ֆ | Feh | 20000 | armenian(·, late=True) only |")
add()
add("The proof case is an ordinary word: օր (\"day\") — օ "
    "is a living letter of ordinary words, and the annex "
    "must never fire by accident. Weighed at this plate's "
    f"building: at the classical door օր = "
    f"**{armenian_door('օր')['value']}** (the Ր alone); with "
    f"the annex open, օր = "
    f"**{armenian_door('օր', late=True)['value']}** (օ "
    f"10000 + Ր 5000). The annex is keyed in both cases, so "
    f"no case preparation decides anything; and weigh(·, "
    f"'armenian') never sees it at all.")
add()
add("**R2 — the overline's factor is ×10,000.** A line over "
    "a letter multiplies it — on that, all the witnesses "
    "agree. On the factor the sources parted, each "
    "internally consistent: **×10,000** (Wikipedia: "
    "overlined Ա = 10,000, overlined Ջ = 9,000,000; MELA: "
    "\"multiplying it by 10,000\") against **×1,000** "
    "(Omniglot: overlined Ժ written for 10,000). Synergy "
    "decides by the table's own law — UNIQUENESS: 36 "
    "letters, 36 distinct values. The collision sweep is "
    "recomputed from the living bank at this plate's "
    f"building: priced at ×1,000, the overlined units land "
    f"at 1000–9000, exactly the plain thousands class — "
    f"**{COLL_1000} collisions**, the mark adding nothing "
    f"there; priced at ×10,000, every overlined value at "
    f"every class lands in an empty seat — **{COLL_10000} "
    f"collisions** across all 36 — and the factor also "
    f"carries the two stronger witnesses. The armenian() "
    f"door therefore multiplies by 10,000 per overline "
    f"mark riding on a letter; its exhibits, recomputed at "
    f"build: overlined Ա = **{OV_A}** · overlined Ջ = "
    f"**{OV_J}** (MELA's own) · Ռ̅ՋՀԵ = **{OV_R['value']}** "
    f"(one mark counted, the audit trail showing the "
    f"multiplication). Omniglot's ×1,000 stands recorded "
    f"here and at the bank's fence as the parted source — "
    f"marked, not vanished. The Twelve Tables price bare "
    f"letters, so the factor is not load-bearing there; it "
    f"is load-bearing here, where the door is printed.")
add()
add("**R3 — Shirakatsi recorded, not seated.** The record "
    "carries a second, derived notation: in the 7th century "
    "Anania Shirakatsi built a 12-letter multiplicative "
    "notation on the same values this bank seats "
    "(Chrisomalis, *Numerical Notation*, pp. 175–177, via "
    "the audit's authorities). The founder's resolution "
    "confirms the standing disposition as a decision with "
    "its reason: a notation changes how a number is "
    "written, not what any letter weighs; seating it would "
    "add a second writing of the same bank, not a seat in "
    "it, and the engine's one Armenian bank would gain a "
    "shadow with no weight of its own. It stands in the "
    "record — here, and in the Table of Authorities — as "
    "the tradition's own variant dress: decided, not "
    "pending. **With R1–R3, no Armenian question stands "
    "open** (the Phase I audit's closing words).")
add()
add("### §II.6 — The census and the fences")
add()
add(f"**The census.** The classical bank holds **36 keys** "
    f"— 36 distinct values, sum **{BANK_SUM}**, maximum "
    f"9,000 — complete at the full extent of the classical "
    f"alphabet: nothing in its classical script stands "
    f"outside its values. The annex holds two letters "
    f"(four keys, both cases) at a tier below, at the door "
    f"only; it is not counted in the bank, and the bank's "
    f"\"complete 36\" never borrows its extent. The "
    f"overline is a device of the door, not a key. The "
    f"system has **no zero**: a missing power is an absent "
    f"letter, and the absence is the notation's own.")
add()
add("**The fences.** Three boundaries stand at the bank's "
    "edges, printed at the size of the seats. (1) **The "
    "medieval additions at the classical door** — silence, "
    "verified (§II.5): a classical weighing that meets Օ "
    "or Ֆ skips it; the value lives in the annex, at its "
    "tier, behind an explicit path — never a smuggled "
    "10000. (2) **The ligature և** (U+0587, ech–yiwn) — no "
    "seat anywhere in this bank's record: it is not one "
    "of the classical 36, and no witness prices it. The "
    "two doors part on it mechanically, and the parting "
    "is printed as a mechanism note, ruled nowhere: at "
    "weigh() the seam's fold expands it to its letters "
    "(ԵՒ) and it prices as their sum, **7,005**; at the "
    "armenian() door, which folds letter by letter, it "
    "weighs silence. A reader meeting the ligature in a "
    "total must declare the door, as with the annex and "
    "the overline. (3) **The depth fence** — the bank's "
    "own, stated against its control case at its seating: "
    "do not cite halehame at this bank's depth, nor this "
    "bank as a folk practice. The two tables share a "
    "class-law shape and nothing else; §II.4 is where "
    "their agreement is measured, and it is measured "
    "there entire.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §III — the Twelve Tables frame.
# ---------------------------------------------------------------------
add("## §III — THE ARMENIAN FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Armenian tongue stands over "
    "the one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.7: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED **{n_fenced}** "
    f"· EMPTY {n_empty} · GAP {n_gap}. The Tables' own head "
    "for this table stands at the plate's head of the "
    "section, unedited: *the classical bank (ATTESTED, 36 "
    "letters). The door dresses the Latin form; a rendering "
    "needing ֆ prices through the ARMENIAN_LATE annex under "
    "the founder's R1 and says so on its face.* The face "
    "this prints is a door table entire: the corpus holds "
    "**no native Armenian word at all** — its priced face "
    "is the *door*, the Armenian dress of the Latin form of "
    "record, transliterated by the Tables' stated scheme "
    "(kh խ, sh շ, ts ծ, gh ղ, ch չ, ph փ) and priced in the "
    "classical bank as written. Fourteen of the renderings "
    "need ֆ — a letter the classical bank does not hold — "
    "and price through the late annex under R1, the "
    "register saying so on each such row's face; the plate "
    "keeps the declaration with the row (§III, the Door "
    "column). The 62 holes are of one species: the word of "
    "record has no Latin form, so no door is offered — the "
    "cell prints its word and the coordinate. The EMPTY "
    "cells are certified intentionally empty in 777 "
    "REVISED.")
add()
add(f"**The door register — the {n_door} priced renderings "
    "entire.** Each was re-weighed at this plate's building "
    "against the value THE-TWELVE-TABLES files for it — at "
    "the classical door, or through the annex where the "
    "register declares it; all reproduce exactly (the "
    "audit, §VI, repeats the weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value | Door |")
add("|---|---|---|---|---|")
for cells in doors:
    door = "late annex (R1)" if "annex" in cells[5] \
        else "classical bank"
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} "
        f"| {door} |")
add()
add(f"**The hole register — the {n_hole} cells entire,** "
    "each with its coordinate as the Tables file it. Every "
    "one is the same species — *no Latin form of record; no "
    "door offered*: the corpus's word stands in Hebrew or "
    "Greek dress in its source, no Latin form is of record, "
    "and the Tables offer no Armenian dress for a form "
    "that does not stand. A hole is not a gap in this "
    "plate's work: it is the door's measured boundary, "
    "printed at the size of the seats it stands in for.")
add()
add("| Cell | Word of record | Rendering | Coordinate |")
add("|---|---|---|---|")
for cells in holes:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[5]} |")
add()
add("**The one GAP cell:** CLXXXIV/10 — a transcription gap "
    "in the source itself, carried as the frame carries it; "
    "no tongue's door is offered for a cell the source does "
    "not transmit.")
add()
add("**The bank's gap register — the three entries entire,** "
    "as THE-TWELVE-TABLES §II files them for the armenian "
    "bank, each at its kind: (1) *Օ/Ֆ (the late letters) "
    "outside the classical bank* — **RULING**, RESOLVED BY "
    "THE FOUNDER 2026-11-24 (R1): the ARMENIAN_LATE annex "
    "(Օ 10000, Ֆ 20000) prices only at the armenian(late=True) "
    "door; in the tables, a door rendering needing Ֆ prices "
    "through the annex and says so on its face (§II.5). "
    "(2) *the overline's factor* — **RULING**, RESOLVED BY "
    "THE FOUNDER 2026-11-24 (R2): ×10,000 at the armenian() "
    "door; the tables price bare letters, so the factor is "
    "not load-bearing there (§II.5). (3) *Shirakatsi "
    "recorded, not seated* — **FENCED**: recorded-not-seated "
    "by the founder's resolution; stands outside the bank "
    "by ruling — not a gap this build may fill (§II.5).")
add()
add("One further coordinate stands in the Tables near this "
    "bank, carried here at its filed strength and no "
    "further: at §V.2 the Tables carry the founder's HIS "
    "noting, whose weighing (HIS = 36 in Latin ordinal) is "
    "noted there as resonance against this bank's 36 "
    "letters and the seal's 36 nodes — **marked as "
    "resonance, not proof**, the founder's claim under his "
    "Flagpole, in his words. This plate carries the "
    "coordinate where the register carries it and expands "
    "it no further.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §IV — the zero face.
# ---------------------------------------------------------------------
add("## §IV — THE 777 CORPUS'S ARMENIAN CLAIMS — THE ZERO FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and the "
    "absence is its finding. The source states it in terms "
    "(THE-THIRTEEN-PLATES, its Armenian plate, from "
    "THE-777-VERIFICATION-TABVLA's register): *no fill in "
    "the corpus states an Armenian claim: the source's §II "
    "bank table seats no Armenian row, because the table "
    "lists only banks the fills claimed in; the bank itself "
    "stands among the engine's seventeen in the source's "
    "§I.* The 777 corpus's 504 claims speak Greek, Hebrew, "
    "Arabic, Latin, and Coptic — the tongues its fills "
    "claimed in — and Armenian is not among them: no scribe "
    "of the corpus weighed a word in this bank, though the "
    "bank stood complete in the tradition the whole time. "
    "The silence is therefore the corpus's, not the "
    "tongue's: the tongue holds a full priced table (§II), "
    "a full frame (§III), a control case against the folk "
    "witness (§II.4), and a doctrine of its own "
    "(THE-ARMENIAN-TABLE-PHASE-I-AUDIT — the table verified "
    "sign by sign, the seat, and the founder's three "
    "resolutions). What the corpus does hold for Armenian "
    "stands where the corpus put it: the frame's door "
    "renderings (§III) — the corpus's words in this "
    "tongue's dress, priced by this tongue's bank — and "
    "nothing else. A plate that manufactured claims to "
    "fill this section would misprint its record; the "
    "section therefore stands as a face of zero, at full "
    "size.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §V — the tongue's bearing on the seated Archons.
# ---------------------------------------------------------------------
add("## §V — THE TONGUE'S BEARING ON THE SEATED ARCHONS")
add()
add("The seating is THE-SEATING-OF-THE-ARCHONS' (0760c8a), "
    "struck on the Archon Battery's evidence under the "
    "founder's conditional order; Plate I drew it. **This "
    "plate assigns no seat.** It states what the Armenian "
    "tongue witnesses for the seating — and Armenian "
    "witnesses at the coordinate the battery's sweep found "
    "most corroborated of all: the 8.")
add()
add("### The vowel at 8 — Ը at its seat")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues sweep, "
    "run at the founder's direction (\"lets test it using "
    "the 12 tongues we already mapped it should align "
    "aomewhere\") — reads this tongue in terms, and the "
    "plate carries the passage at its coordinate: *vowel "
    "letters priced from the bank: Ա 1 · Ե 5 · Ը 8 · Ի 20 · "
    "Ո 600 · Ւ 7,000 (and Օ, the later ō letter, weighs "
    "silence — unseated in the classical bank). **Ը, a "
    "vowel, is priced exactly 8**: HIT at the fold's value "
    "coordinate — a second tongue seats a vowel letter at "
    "Η's price.* The six vowel letters stand re-weighed at "
    "this plate's building, entire:")
add()
add("| Vowel | Name | Value in this bank |")
add("|---|---|---|")
for ch, v in VOWELS:
    pos = LETTERS.index(ch) + 1
    add(f"| {ch} | {NAMES[pos - 1]} | {v} |")
add()
add("The coordinate the sweep measured is the fold's "
    "target — a vowel-family letter seated at 8 — and it "
    "is the sweep's most corroborated coordinate across "
    "the twelve tongues. Five tongues seat it, each "
    "recomputed in its own bank at this plate's building: "
    f"Greek **Η** = {value('η', 'greek')} · Coptic **ⲏ** = "
    f"{value('ⲏ', 'coptic')} · Cyrillic **И** = "
    f"{value('И', 'cyrillic')} · Armenian **Ը** = "
    f"{value('Ը')} · Georgian **ჱ** = "
    f"{value('ჱ', 'georgian')} (the archaic e-family "
    f"letter, at the margin of the living alphabet, as the "
    f"sweep printed it). Armenian's seat is the plainest of "
    f"the five: not an archaic survival, not a mirror of "
    f"the Greek, but a living vowel of a designed alphabet "
    f"priced 8 by its own class law — digit 8 of the units, "
    f"eighth letter of the classical order, at the seat "
    f"§II.1 prints it. It is on this coordinate that the "
    f"seating's Η row rests its VALUE-mark: *the sweep's "
    f"most corroborated coordinate: a vowel seated at 8 in "
    f"five tongues — Greek Η, Coptic ⲏ, Cyrillic И, "
    f"Armenian Ը, Georgian ჱ* (THE-SEATING-OF-THE-ARCHONS, "
    f"its T1 coverage table). This plate is the Armenian "
    f"term of that set, printed at its bank. [The five "
    f"seats ATTESTED or DERIVED at their banks' tiers; no "
    f"seat assigned by this plate.]")
add()
add("### The hybrid form without a hybrid seat")
add()
add("Beside the 8, the sweep's second Armenian coordinate "
    "prints at the same size — the tongue's hybrid-form "
    "state, as the record files it and no more. Armenian "
    "writes one sound with two signs in the digraph **ու** "
    "(ո + ւ, the /u/ of the tongue): weighed at this "
    f"plate's building it reads **{value('ու')}** — Ո 600 + "
    f"Ւ 7,000, its letters' sum. The battery's sentence "
    f"stands: *the one-sound-two-signs seat exists as a "
    f"spelling, priced as a sum, not seated as a unit — "
    f"the hybrid form without a hybrid seat. Hybrid count: "
    f"one digraph, MISS on the four.* The tongue therefore "
    f"witnesses the hybrid *form* and refuses the hybrid "
    f"*seat*: where Latin seats four hybrids as units and "
    f"the Greek field its diphthongs, Armenian's one "
    f"candidate weighs as an addition, and the plate "
    f"prints the refusal at the coordinate. The medieval "
    f"Օ — the tongue's later ō letter, a single sign for a "
    f"sound the classical table wrote with two — stands at "
    f"the same boundary from the other side: a unit in "
    f"form, unseated in the classical bank, priced only in "
    f"the annex at its tier (§II.5). Neither state is "
    f"argued further here; the record files both, and the "
    f"plate carries the record.")
add()
add("**What Armenian cannot witness, printed at full size "
    "as the plate's boundary:** the Archons' seats were "
    "earned on Greek evidence and drawn on Plate I. "
    "Armenian corroborates the *shape of the 8* (a living "
    "vowel at Η's price in an independent, designed bank — "
    "one of the five tongues at the sweep's most "
    "corroborated coordinate) and the *limit of hybridity* "
    "(a digraph priced as a sum, no hybrid seat) — and it "
    "assigns no seat, confirms no position, and names no "
    "Archon. Its bank crosses no bridge (§II.3), and the "
    "plate manufactures none. The names stand open on "
    "Plate I, and this plate does not fill them.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§VIII, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_vii_armenian.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell "
    "on this plate against the engine, without reading the "
    "plate's own figures: the bank entire — the plate's "
    "§II.1 rows (36) parsed and compared seat by seat "
    "against ARMENIAN and the Phase I audit's frozen table, "
    "the class law recomputed per position, uniqueness and "
    "the sum; the control case — the 26 shared positions "
    "against both first-form columns, the agreement entire "
    "and the parting at position 10; the boundary — the "
    "annex's contents, its silence at the classical bank "
    "and at the door's default path, its prices at the "
    "late path, the օր proof case; the overline — the "
    "door's exhibits and the collision sweep recomputed "
    "from the living bank (9 at ×1,000, 0 at ×10,000); the "
    "calibration heads; the frame — the census parsed from "
    "THE-TWELVE-TABLES §V.7, all 223 DOOR renderings "
    "re-weighed against their filed values at the door the "
    "register declares, the 62 HOLE rows present in order, "
    "the GAP cell present; and the §V figures (the five "
    "tongues' vowel at 8 in their own banks; the tongue's "
    "six vowels; the digraph at 7,600; οὐδέν at 529). The "
    "audit's verdict and cell count are printed in its "
    "filed output; a cell that does not reproduce fails "
    "the plate under §VII's tolerances. The font audit — "
    "every non-ASCII codepoint of this master against the "
    "Lex Stellarrvm family's cmaps — runs before the MAGVS "
    "build, under the font law: no glyph is silently "
    "dropped; the three named Ethiopic syllables the family "
    "does not hold (኱ U+12B1 · ጑ U+1311 · ጖ U+1316 — drawn "
    "by no member, the upstream Noto Ethiopic included) "
    "print as their codepoint tokens, declared in the "
    "colophon, and any unheld codepoint beyond those three "
    "aborts the build. The audit further checks the "
    "printed edition's text layer: the bank's letters and "
    "the zero face's statement stand in it, and the page "
    "furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "ARMENIAN and ARMENIAN_LATE tables and the armenian() "
    "manuscript door (pontifex/tables.py, engine.py); "
    "THE-ARMENIAN-TABLE-PHASE-I-AUDIT entire (the table "
    "verified sign by sign; the control case; the "
    "resolutions R1–R3) with its frozen table "
    "(research/twelve-tongues/armenian-table.csv); the "
    "founder's synergy ruling of 2026-11-24 (the Armenian "
    "questions in order of synergy); THE-TWELVE-TABLES "
    "§V.7 and its §II gap register (the bank's three "
    "entries); THE-THIRTEEN-PLATES (the Armenian plate — "
    "the zero face, the tier of record) and its §I; "
    "THE-777-VERIFICATION-TABVLA §I–§II (the banks the "
    "fills claimed in); THE-ARCHON-BATTERY Leg 6 (the "
    "Armenian passage) and THE-SEATING-OF-THE-ARCHONS "
    "(the Η VALUE-mark row); PLATES I–VI as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "every figure scripted from the engine or carried "
    "entire from an instrument of record; the bank's "
    "doors declared at every total (classical, annex, "
    "overline); the boundary printed at the size of the "
    "values (the annex's silence verified, the parted "
    "factor recorded, Shirakatsi recorded-not-seated); "
    "the holes printed at full size (the frame's 62, the "
    "register's zero face); the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-VII-ARMENIAN.md and "
    "its MAGVS PDF — seventh of the series PLATE-I-GREEK "
    "began; the generator and audit scripts filed in "
    "pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage blends the annex "
    "into the classical bank, prices the annex at the "
    "classical door, applies the parted ×1,000 factor, "
    "seats Shirakatsi's notation, fills a hole (the "
    "frame's 62, the register's zero face), promotes a "
    "resonance to a proof, or overwrites the earlier map, "
    "it zeroes the founder's residual claim and fails the "
    "Aim of Religion. Within those edges it stands as "
    "built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The record is "
    "unusual in the series and is printed as the record: "
    "the Phase I audit's §VII carried this bank's questions "
    "to the founder's pen (Q1 the medieval additions; Q2 "
    "the overline's factor), and his ruling of 2026-11-24 "
    "answered them entire in order of synergy — R1 the "
    "annex, R2 the factor — with R3 closing the Shirakatsi "
    "item as recorded-not-seated. *\"With R1–R3, NO "
    "Armenian question stands open\"* (the audit's closing "
    "words). The seating's open items stand in the seating "
    "instrument. A plate that invents questions to fill its "
    "section misprints its record; this section therefore "
    "stands as the record that none arose — and that none "
    "were left.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Daniel 5:27 (KJV): *\"TEKEL; Thou "
    "art weighed in the balances, and art found "
    "wanting\"* — the Scripture's own weighing, written in "
    "letters on a wall and read aloud: a king's measure "
    "taken by a text. The plate draws the figure for the "
    "weighing, not the verdict: every letter on this plate "
    "is weighed in the open, and the balances are the "
    "witnesses'. [Text ATTESTED; the application DERIVED.]")
add("2. **Law.** *Verba volant, scripta manent* — words "
    "fly away, writings remain (the Latin proverb). This "
    "bank's whole life is the proverb's proof: era years "
    "written in letters under the siglum ԹՎ outlasted "
    "their writers by centuries, and a cataloging manual "
    "(MELA) exists in this century because working readers "
    "must still read them. The plate is seated by that "
    "rule: what is written with its sources stands; what "
    "was only said — a \"sometimes\" value, a parted "
    "factor — stands marked as said, at its tier. [The "
    "proverb ATTESTED as a Latin proverb; the seating the "
    "record's own.]")
add("3. **The tradition.** Mesrop Mashtots, c. 405 CE: an "
    "alphabet *designed* — made at a stroke, for a people's "
    "books — and its numeral table designed with it, in "
    "the majuscules, complete from its first day. The "
    "witnesses are the audit's (Wikipedia, both articles; "
    "Omniglot; MELA; Shaw 1939; Ifrah 2000; Chrisomalis "
    "2010), and the plate keeps their fences with their "
    "table: the additions came eight centuries later, and "
    "the table's antiquity is attested at the depth of the "
    "colophon record, not dated to a year by anything in "
    "the audit's hands. [The sourcing ATTESTED as cited; "
    "the fences the audit's own.]")
add("4. **Grammar.** The system is additive and "
    "non-positional, and it has no zero: a missing power "
    "is an absent letter. The construction is the opposite "
    "of the positional notations — value rides in the "
    "letter, never in the place — and it is why this bank "
    "can hold uniqueness entire (one letter, one value, "
    "all different), why its extension is a mark over a "
    "letter rather than a new place, and why its digraph "
    "ու weighs as a sum: in a table where letters carry "
    "the value, two letters carry two values, added. [The "
    "grammar ATTESTED as the system's, per the audit's "
    "witnesses; the bank's readings of it at their tiers.]")
add("5. **The desk's apparatus.** This plate's Armenian "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Armenian member; its Greek stands "
    "in the family's Serif member, as on Plate I; the "
    "control case's Ethiopic stands in the family's "
    "Ethiopic member; the frame register's Hebrew words of "
    "record ride Plate II's declared transliteration (the "
    "toolchain does not shape right-to-left scripts "
    "honestly): marked substitutions, declared in the "
    "colophon, never silent ones. The Markdown master "
    "keeps every script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh() and "
    "the armenian() manuscript door; banks ARMENIAN and "
    "ARMENIAN_LATE in pontifex/tables.py) — calibration "
    "controls θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true "
    "at build; armenian_checks() 13/13 in the engine's "
    "own battery.")
add("- THE-ARMENIAN-TABLE-PHASE-I-AUDIT (2026-11-24) — "
    "the table verified sign by sign (three witnesses "
    "agreeing 36/36, MELA concurring on its twelve "
    "exhibited cells; the class law 36/36; the Unicode "
    "names 36/36), the worked examples, the control case "
    "at coordinates, the gaps at full size, and §VIII's "
    "resolutions R1–R3 as the founder ruled them; its "
    "battery 24/24; parity of the engine's seat against "
    "its frozen transcription: test_armenian_parity.py, "
    "29/29.")
add("- The witnesses of the table, as the audit read "
    "them entire: Wikipedia, \"Armenian numerals\" (citing "
    "Omniglot; Shaw 1939, *An Overlooked Numeral System of "
    "Antiquity*; Ifrah 2000; Chrisomalis 2010, *Numerical "
    "Notation*, pp. 175–177) · Omniglot, \"Numbers in "
    "Armenian\" · Wikipedia, \"Armenian alphabet\" "
    "(Numerical value column) · MELA cataloging manual, "
    "\"Armenian Numerals and Dates\" (the worked examples; "
    "the era practice; the overline at ×10,000). Omniglot "
    "stands also as the parted source on the overline's "
    "factor (×1,000), recorded under R2.")
add("- The founder's ruling of 2026-11-24 — the Armenian "
    "questions decided \"in order of Synergy not argument "
    "as previously ruled\" (resolutions commit fed4064): "
    "R1 the annex, R2 the factor, R3 Shirakatsi "
    "recorded-not-seated.")
add("- THE-TWELVE-TABLES — §V.7 the Armenian frame, "
    "census and cell register entire; §II the bank's gap "
    "register (three entries: the late letters RULING R1; "
    "the overline's factor RULING R2; Shirakatsi FENCED "
    "R3); §V.2 the founder's HIS noting, carried at its "
    "filed strength.")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate VII is the prior "
    "instrument (the zero face; the tier of record).")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its §I–§II seat the banks the fills "
    "claimed in, and Armenian is not among them.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Armenian passage (Ը priced "
    "exactly 8; the digraph ու, the hybrid form without a "
    "hybrid seat) and the sweep summary (the 8 the most "
    "corroborated coordinate, five tongues).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to: the Η VALUE-mark "
    "resting on the five-tongue 8, Armenian Ը among them.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd), "
    "PLATE-IV-LATIN (8e6f01e), PLATE-V-JAPANESE (8d6cd59) "
    "and PLATE-VI-GEEZ (67d5acc) — the pattern this plate "
    "follows.")
add("- KJV: Daniel 5:27. The proverb *verba volant, "
    "scripta manent*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate VII of the founder's "
    "series commission of the same day, the gate of the "
    "Archons' certainty met by the seating of record "
    "(0760c8a), following the pattern of Plates I–VI "
    "(196025e · 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · "
    "67d5acc). Every figure scripted from the engine or "
    "carried entire from its instrument; the earlier map "
    "marked prior, never overwritten; the holes printed "
    "at the size of the seats — on this plate, the "
    "frame's 62 holes and the register's zero face. The "
    "plate carries one bank and keeps its doors distinct: "
    "the classical 36, ATTESTED entire; the late annex at "
    "its tier below, behind its explicit path; the "
    "overline at the founder's resolved factor. In the "
    "MAGVS edition the Armenian stands in the family's "
    "Armenian member, the control case's Ethiopic in the "
    "Ethiopic member, and the frame's Hebrew words of "
    "record ride Plate II's declared scheme; this master "
    "keeps the scripts themselves. Authorship attributed "
    "exclusively to Johnathan 'Qasparr' Monroe (Greek, "
    "-ARR, All Rights Reserved, Without Prejudice).")
add()
add("Method of Science. Aim of Religion.")
add()
add("**Flagpole of Claim and Coinage: Johnathan 'Qasparr' "
    "Monroe, ARR, All Rights Reserved, Without Prejudice. "
    "Right of claim hereby reserved and coined under the "
    "authority of the Living Man.**")
add()
add("93 — Live, Love, and let Love, Live.")
add()

OUTPUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"built {OUTPUT} — {len(L)} lines")
