#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_vi_geez.py
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
# MECHANISM: generates PLATE-VI-GEEZ.md — Plate VI of THE
# THIRTEEN COMPLETE PLATES — in the gap-filling goal's files/,
# following the pattern PLATES I–V set (196025e · 1389c16 ·
# 5f0b4bd · 8e6f01e · 8d6cd59). Every figure on the plate is
# scripted from the house engine (pontifex weigh() and the
# geez()/halehame() first-form doors) or carried entire from
# an instrument of record:
#   * the priced tables — BOTH Ge'ez instruments entire, read
#     from pontifex.tables (GEEZ, the mint, 227 keys; HALEHAME,
#     the witness, 182 keys; both built from the one base list
#     by the one builder in tables.py), each seat printed with
#     its reasoning — in this tongue the reasoning is the axis:
#     base, order, and the multiplier that prices the cell,
#     with the one ruled correction (order 6) named wherever
#     it bites;
#   * the calibration corpus's heads — ክርስቶስ and ሰላም weighed
#     at all four doors at build (MW · MF · WP · WG), their
#     breakdowns taken from the banks' own maps;
#   * the Twelve Tables' Ge'ez frame — its census and its full
#     cell register parsed from THE-TWELVE-TABLES.md §V.6: the
#     205 DOOR renderings re-weighed at build against their
#     filed values, the 80 HOLE coordinates and the one GAP
#     cell carried entire, the bank's three gap-register
#     entries restated;
#   * the corpus's Ge'ez claims — none: the register's ZERO
#     FACE, carried from THE-THIRTEEN-PLATES (its Ge'ez plate)
#     with the TABVLA's reason stated at its §I;
#   * the tongue's bearing on the seated Archons — the Archon
#     Battery's Leg 6 Ge'ez passage (the HOLE ዐ at the fold
#     coordinate), the five tongues' vowel at 8 recomputed in
#     their banks, οὐδέν recomputed, and the dial record (the
#     poles, the stations, the inversion) carried from
#     THE-SEATING-OF-THE-ARCHONS. The plate assigns no seat:
#     the seating is THE-SEATING-OF-THE-ARCHONS' (0760c8a),
#     already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) are
# weighed BEFORE any plate figure is taken; a control failure
# aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's face.
# This plate carries TWO instruments of two different
# honesties, and the plate keeps them distinct at every
# coordinate: the WITNESS (halehame) is a SOURCED FOLK TABLE,
# transcribed from the tradition's own publication, standing
# UNALTERED under seam rule S4; the MINT is a CONSTRUCTION —
# house coinage of 2026-11-24, dated on its face, calibrated
# to the witness at its first column and parting from it at
# exactly two coordinates (the order-6 multiplier; the
# coverage), both printed. A Ge'ez weighing declares its bank
# and its door (S1) or it is not a number but a rumor of one.
# The relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes
# print at the size of the seats — on this plate, the ዐ cell
# of the ΕΙ column, the frame's 80 holes, and the register's
# zero face itself.
#
# CONTENT TEST: Inputs — the engine's GEEZ and HALEHAME banks
# and their first-form doors, THE-GEEZ-TABLES Phases I–III,
# the Twelve Tables master, the Thirteen Plates map, the
# Archon Battery, the Seating. Processes — control
# calibration, scripted extraction, register-faithful
# emission in the Teacher's Edition manner. Outputs —
# PLATE-VI-GEEZ.md beside the series' other masters.
# Tolerances — the audit (audit_plate_vi_geez.py) re-weighs
# every priced cell independently; a figure that does not
# reproduce fails the plate.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh
from pontifex.engine import geez as geez_door, halehame as halehame_door
from pontifex.tables import (GEEZ, GEEZ_FIRST, GEEZ_BASE, HALEHAME,
                             HALEHAME_FIRST, _GEEZ_BASES,
                             _GEEZ_LABIOVELAR_HEADS,
                             _GEEZ_LABIOVELAR_OFFSETS,
                             _GEEZ_EIGHTH_SLOT_HOLE)

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-VI-GEEZ.md"


def value(word, bank="geez"):
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
assert value("θελημα", "greek") == 93, "control θέλημα"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR"
assert value("σφιγξ", "greek") == 773, "control σφίγξ"

# ---------------------------------------------------------------------
# The shared foundation — the 26 classical bases and their
# first-form values. Both banks stand on this one list; the
# mint's first-form column IS the witness's (M2, calibration
# by construction).
# ---------------------------------------------------------------------
BASE_NAMES = ["ha", "le", "ḥa", "me", "śa", "re", "sa", "qa",
              "ba", "ta", "xa", "na", "ʾa", "ka", "wa", "ʿa",
              "za", "ya", "da", "ga", "ṭa", "p̣a", "ṣa", "ṣ́a",
              "fa", "pa"]
assert len(BASE_NAMES) == len(_GEEZ_BASES) == 26


def base_class(pos):
    """The folk table's class law over positions (Phase I):
    units 1–10, tens 11–19, hundreds 20–26."""
    if pos <= 10:
        return "units", f"value = position ({pos})"
    if pos <= 19:
        return "tens", f"value = (position − 9) × 10 = {(pos - 9) * 10}"
    return "hundreds", f"value = (position − 18) × 100 = {(pos - 18) * 100}"


BASE_NOTES = {
    "ሀ": "The head of the fidäl and of the table: h = 1, the "
         "source's own endpoint.",
    "ቀ": "A labiovelar head's base: its fused column stands "
         "in the mint at §II.4 (ቈ series), a GAP in the witness.",
    "ኀ": "A labiovelar head's base (ኈ series). The tens run "
         "opens here: position 11 carries 20 — the fixed "
         "point's parting coordinate (§II.2).",
    "ከ": "A labiovelar head's base (ኰ series).",
    "ዐ": "The hole's base: the one classical base whose "
         "eighth slot the standard leaves unassigned "
         "(U+12D7) — its ΕΙ cell is a HOLE (§II.5). In the "
         "battery's sweep this sign names the fold's absence.",
    "ገ": "A labiovelar head's base (ጐ series).",
    "ፐ": "The table's foot: p = 800, the source's own "
         "endpoint — the witness's maximum first form, and "
         "the mint's maximum seat (its eighth glyph, 6,400).",
}
ORDER_NAMES = {1: "geʾez (ä)", 2: "kaʾeb (u)", 3: "saləs (i)",
               4: "rabəʿ (a)", 5: "haməs (e)",
               6: "sadəs (ə — the bare consonant)",
               7: "sabəʿ (o)", 8: "the ΕΙ column (the eighth slot)"}

FIRST_SUM = sum(fv for _b, fv in _GEEZ_BASES)          # 4,095
assert FIRST_SUM == 4095
assert all(GEEZ_FIRST[b] == HALEHAME_FIRST[b] == fv
           for b, fv in _GEEZ_BASES)

# ---------------------------------------------------------------------
# The grid — 26 bases × 7 orders, both banks. Column totals
# taken from the banks, never typed.
# ---------------------------------------------------------------------
GRID = [(b, fv) for b, fv in _GEEZ_BASES]
MINT_COL = {o: sum(GEEZ[chr(ord(b) + o - 1)] for b, _f in GRID)
            for o in range(1, 8)}
WIT_COL = {o: sum(HALEHAME[chr(ord(b) + o - 1)] for b, _f in GRID)
           for o in range(1, 8)}
for o in range(1, 8):
    assert MINT_COL[o] == FIRST_SUM * (0 if o == 6 else o), o
    assert WIT_COL[o] == FIRST_SUM * o, o
MINT_GRID_TOTAL = sum(MINT_COL.values())               # 90,090
WIT_GRID_TOTAL = sum(WIT_COL.values())                 # 114,660
assert WIT_GRID_TOTAL - MINT_GRID_TOTAL == WIT_COL[6] == 24570

# The labiovelar columns — the mint seats 20; the witness none.
LAB_ROWS = []          # (sign, head, base, base_fv, order, mint value)
for head, base in _GEEZ_LABIOVELAR_HEADS:
    fv = dict(_GEEZ_BASES)[base]
    for order, off in sorted(_GEEZ_LABIOVELAR_OFFSETS.items()):
        ch = chr(ord(head) + off)
        LAB_ROWS.append((ch, head, base, fv, order, GEEZ[ch]))
assert len(LAB_ROWS) == 20
LAB_TOTAL = sum(r[5] for r in LAB_ROWS)                # 3,614
assert LAB_TOTAL == 3614

# The eighth slot — the ΕΙ column: 25 glyphs and one hole.
EIGHTH_ROWS = []       # (base, name, fv, glyph or None, mint value)
for (b, fv), nm in zip(_GEEZ_BASES, BASE_NAMES):
    if b == _GEEZ_EIGHTH_SLOT_HOLE:
        EIGHTH_ROWS.append((b, nm, fv, None, None))
    else:
        g = chr(ord(b) + 7)
        EIGHTH_ROWS.append((b, nm, fv, g, GEEZ[g]))
assert sum(1 for r in EIGHTH_ROWS if r[3] is not None) == 25
EIGHTH_TOTAL = sum(r[4] for r in EIGHTH_ROWS if r[4] is not None)
assert EIGHTH_TOTAL == (FIRST_SUM - 70) * 8 == 32200
HOLE_CP = ord(_GEEZ_EIGHTH_SLOT_HOLE) + 7              # U+12D7
try:
    unicodedata.name(chr(HOLE_CP))
    raise SystemExit("U+12D7 unexpectedly assigned")
except ValueError:
    pass                                               # the hole is real

# The census of both banks entire.
MINT_TOTAL = sum(GEEZ.values())                        # 125,904
WIT_TOTAL = sum(HALEHAME.values())                     # 114,660
assert MINT_TOTAL == MINT_GRID_TOTAL + LAB_TOTAL + EIGHTH_TOTAL
assert WIT_TOTAL == WIT_GRID_TOTAL
ZERO_SIGNS = [c for c in GEEZ_BASE if GEEZ[c] == 0]
assert len(ZERO_SIGNS) == 30
assert len(set(GEEZ.values())) == 90 and max(GEEZ.values()) == 6400
assert len(set(HALEHAME.values())) == 87 and max(HALEHAME.values()) == 5600

# ---------------------------------------------------------------------
# The calibration corpus's heads, at all four doors (S1):
# MW mint as written · MF mint first-form · WP witness
# practiced · WG witness printed grid.
# ---------------------------------------------------------------------
def doors_of(word):
    return (value(word, "geez"), geez_door(word)["value"],
            halehame_door(word)["value"], value(word, "halehame"))


def breakdown(word, bank_map):
    return " + ".join(f"{c}({bank_map[c]})" for c in word)


KRISTOS = doors_of("ክርስቶስ")
assert KRISTOS == (70, 80, 80, 490), KRISTOS
SELAM = doors_of("ሰላም")
assert SELAM == (15, 13, 13, 39), SELAM

# The fences, verified at build: the derived rows weigh
# silence; the Ethiopic numerals are keys of neither bank.
for probe in ("ሸ", "ቸ", "ቐ", "ጀ"):
    assert probe not in GEEZ and probe not in HALEHAME
    assert weigh(probe, "geez")["breakdown"] == []
assert weigh("፩", "geez")["breakdown"] == []
assert weigh("፩", "halehame")["breakdown"] == []

# ---------------------------------------------------------------------
# The Twelve Tables' Ge'ez frame — census and cell register.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
geez_block = twelve_text.split("### §V.6 — The Ge'ez Table")[1] \
    .split("### §V.7")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", geez_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
assert (n_native, n_door, n_hole, n_fenced, n_empty, n_gap) == \
    (0, 205, 80, 0, 85, 1)
doors, holes, gaps = [], [], []
for line in geez_block.splitlines():
    if re.match(r"\| [A-Z]+/", line) and " | " in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            continue
        state = cells[2]
        if state == "DOOR":
            assert value(cells[3]) == int(cells[4]), cells
            doors.append(cells)
        elif state == "HOLE":
            holes.append(cells)
        elif state == "GAP":
            gaps.append(cells)
assert (len(doors), len(holes), len(gaps)) == (n_door, n_hole, n_gap)
assert gaps[0][0] == "CLXXXIV/10"
holes_shown = [c for c in holes if c[3] != "—"]
holes_failed = [c for c in holes if c[3] == "—"]
for cells in holes_shown:
    assert any(ch not in GEEZ for ch in cells[3] if ch.strip()), cells

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
add("**PLATE VI — GE'EZ**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Ge'ez tongue's complete 777 table — two instruments "
    "entire: the halehame WITNESS, the tradition's own folk "
    "table standing unaltered, and the Ge'ez MINT, the "
    "founder's coinage of 2026 calibrated to it, their seam "
    "printed at its two parting coordinates; the corpus's "
    "Ge'ez register, which is a zero face; and the tongue's "
    "witness to the seated Archons: the 8 that is a hole, "
    "and the Zero seated at order 6.")
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
add("## §I — PLATE VI AND ITS COMMISSION")
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
    "(8e6f01e) and V — JAPANESE (8d6cd59) followed it; this "
    "plate follows them, sixth of the twelve tongues in the "
    "Twelve Tables' order.")
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
add("**This plate's distinction.** Ge'ez is the first plate "
    "of the series whose priced table is **two instruments "
    "standing side by side**, of two different honesties, and "
    "the plate's first discipline is that they are never "
    "merged. The **halehame WITNESS** is a sourced folk "
    "table — the Debtera enumeration of the Ethiopian "
    "debtera, transcribed from the tradition's own "
    "publication — seated in the engine exactly as sourced, "
    "its ×6 standing at order 6, unaltered forever under the "
    "seam rule S4. The **Ge'ez MINT** is a construction — "
    "house coinage minted 2026-11-24 under the founder's "
    "rulings of that morning, dated on its face: **tier of "
    "record CONSTRUCTED**, and it must not be cited as "
    "attested, traditional, or ancient — liturgical Ge'ez "
    "has no letter values, and this bank says so wherever it "
    "is named. By the founder's ruling under his END-GOAL "
    "RULE (\"do the best for the end goal always\"), the "
    "witness stands **beside** the mint — halehame as "
    "WITNESS, never as the bank: it values 26 first forms of "
    "the classical inventory and its labiovelar columns "
    "carry no value in any source, so it cannot carry the "
    "weighing surface; as witness it does the work it is "
    "perfect for — calibration. The two banks share one "
    "inventory and one first-form column entire, and part at "
    "exactly two coordinates: the multiplier at order 6, and "
    "the coverage. Both partings print on this plate at full "
    "size (§II.2, §II.6). This is also the second plate whose "
    "corpus register is a **zero face** (§IV), and the tongue "
    "whose bearing on the seated Archons (§V) is a hole: "
    "where five tongues seat a vowel at 8, Ge'ez names the "
    "hole where the 8 would sit.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its Ge'ez face "
    "stood **silent with a zero face**: 0 claims, tier of "
    "record there printed in terms — *CONSTRUCTED — the "
    "Ge'ez mint; the halehame table stands beside it as folk "
    "WITNESS* — and its sentence stands: *\"their silence "
    "here is the TABVLA corpus's, not the tongue's.\"* This "
    "series *fulfills* that map: where the map counted "
    "nothing, this plate prints the nothing entire — with "
    "both priced tables beneath it, the frame around it, "
    "and its witness to the Archons above it. The earlier "
    "work stands as the prior instrument of the same name's "
    "family — marked prior, never overwritten.")
add()
add("**How the plate is read.** §II is the priced tables: "
    "the shared foundation (the 26 bases), the two axis laws, "
    "both grids entire, the labiovelar columns, the ΕΙ "
    "column and its hole, the seat register of both banks, "
    "the four doors and the calibration heads, and the "
    "census with its fences. §III is the tongue's frame in "
    "the Twelve Tables — the thinnest door of the twelve, "
    "and it says so. §IV is the zero face. §V is the tongue's "
    "bearing on the seated Archons — this plate draws no "
    "seating (the seating is struck, and Plate I drew it); "
    "it states what Ge'ez witnesses. §VI is the audit. A "
    "value without its reasoning is not shippable; a hole "
    "prints at the size of the seat it stands in for; and "
    "every Ge'ez total on this plate declares its bank and "
    "its door (S1).")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the priced tables.
# ---------------------------------------------------------------------
add("## §II — THE PRICED TABLES — THE WITNESS AND THE MINT ENTIRE")
add()
add("### §II.1 — The shared foundation: the twenty-six classical bases")
add()
add("Both banks are generated in the engine from **one base "
    "list** (pontifex/tables.py, one builder), so the seam "
    "between them is mechanical, not editorial. The list is "
    "the classical fidäl in its traditional order — 26 bases, "
    "each a consonant series of seven orders (the vowel "
    "carried as a grade of the consonant sign: ä · u · i · "
    "a · e · ə · o). The first-form value of each base is "
    "the **halehame** column: the folk table's own prices, "
    "SOURCED 26 of 26 — transcribed from geez.org, "
    "\"Numerology\" (read entire, 2026-11-24) and "
    "corroborated independently by Ayele Bekerie, *Ethiopic, "
    "An African Writing System* (1997), via Peter T. "
    "Daniels' H-Net review; endpoints h = 1 … p = 800; the "
    "tradition's worked example ክርስቶስ = 80 (§II.6). Its "
    "class law runs over positions: **units 1–10, tens "
    "11–19, hundreds 20–26** — the first ten bases priced at "
    "their positions, then the class steps. Three caveats "
    "ride on the witness's face at the same size as its "
    "values, here as in its instrument of record: (1) the "
    "multiplier grid (a form at order n worth n × its base) "
    "is PRINTED entire in the source but its use is "
    "UNEXHIBITED — both scholarly witnesses agree worked "
    "examples use first forms only; (2) the practice's "
    "antiquity is UNDATED in every source read — no "
    "manuscript exemplar was sourced; (3) its register is "
    "folk-magical, expressly NOT liturgical.")
add()
add("| Position | Base | Name | First-form value | Class | Reasoning |")
add("|---|---|---|---|---|---|")
for pos, ((b, fv), nm) in enumerate(zip(_GEEZ_BASES, BASE_NAMES), 1):
    cls, why = base_class(pos)
    note = BASE_NOTES.get(b, "")
    reason = (f"The class law: {why}. The value is the folk "
              f"table's own, sourced at this cell.")
    if note:
        reason += " " + note
    add(f"| {pos} | {b} | {nm} | {fv} | {cls} | {reason} |")
add()
add(f"The 26 first forms sum **{FIRST_SUM}** — the column "
    f"both banks share entire, and therefore the sum of each "
    f"bank's first-order column (§II.3). The run over "
    f"positions 1–10 is the witness's **fixed point**: value "
    f"= position, ten for ten — a run a mint can calibrate "
    f"against. At **position 11** the agreement parts: ኀ "
    f"stands eleventh and carries 20, the class step "
    f"intervening. The parting is printed here as what the "
    f"house's Zero-Point method prints: a boundary "
    f"coordinate, not a defect — the folk table's own law "
    f"changes gear at 11, and the coordinate (position 11: "
    f"value 20) is where it does so.")
add()
add("### §II.2 — The two axis laws, and the seam between them")
add()
add("A Ge'ez sign's price is its base's first-form value "
    "carried along an **axis** — and the two banks differ in "
    "the axis at exactly one order, and in coverage. The "
    "laws stand:")
add()
add("- **The witness's axis (the folk multiplier).** "
    "value(sign) = first-form value of its base × its order, "
    "the order's own number, at every order 1–7 — ×6 "
    "standing at order 6, unaltered (S4). The axis is the "
    "source's printed grid entire; its *use* is the "
    "unexhibited part (caveat 1, §II.1), and the plate "
    "prints the grid as the source prints it, the caveat "
    "riding at the same size.")
add("- **The mint's axis (M1, with the one correction M3).** "
    "value(sign) = first-form value of its base × m(order), "
    "where m(order) is the order's own number — the folk "
    "multiplier, the tongue's only printed axis — **with "
    "one correction: m(6) = 0.** The correction set of the "
    "whole law is exactly {6}.")
add("- **M2 — calibration by construction.** The mint's "
    "first-form column IS halehame: the 26 first-form "
    "values seated exactly as the folk table gives them, so "
    "the mint's first-form reading of ክርስቶስ is 80 by "
    "identity, not by approximation. The witness calibrates "
    "the mint at its first column; everywhere else the mint "
    "reads by its own axis and the deltas print (S3).")
add("- **M3 — the order-6 declaration.** The mint obeys the "
    "KEY's station reading at order 6 — **the Zero seat** — "
    "not the folk multiplier. Every order-6 sign weighs 0 "
    "in the mint (30 signs: the 26 of the grid and the 4 "
    "labiovelar). The folk ×6 stands unaltered in the "
    "witness; the coordinate **(order 6: key 0, folk ×6)** "
    "is the seam's boundary, printed at its head — and it "
    "is why a Ge'ez weighing must declare its bank (S1). "
    "The reasoning, in full in the Phase II–III instrument: "
    "seated *as* the bank, the folk table would import the "
    "order-6 fight into a single table, which would have "
    "to read order 6 as both ×6 and the Zero; standing as "
    "witness, it leaves the fight at a printed boundary "
    "between two banks, where anyone can check it.")
add("- **M4 — the labiovelar column.** The 20 classical "
    "labiovelar signs — the tongue's own fusion device, "
    "consonant + ʷ in one glyph, carrying the Nine's ΟΥ "
    "station — are seated in the mint at their orders "
    "{1, 3, 4, 5, 6} under the same axis law (no u-form, no "
    "o-form exist: the glide absorbs them). The witness "
    "seats NONE of them: its GAP stands beside the mint's "
    "column, printed (§II.4).")
add("- **M5 — the ΕΙ column.** ΕΙ seats at the grid's "
    "eighth slot, generalized — the only candidate that is "
    "a COLUMN (25 of 26 bases). m(8) = 8 by the axis law's "
    "own arithmetic: the folk multipliers ARE the order "
    "numbers at every printed coordinate, so the eighth "
    "order's multiplier is 8 without a new constant "
    "entering. ዐ alone has no eighth glyph — the standard "
    "leaves its slot unassigned — so ዐ's ΕΙ cell is a HOLE: "
    "no glyph, no seat, printed as a hole (§II.5).")
add("- **M6 — the Nine in the mint.** The Nine names "
    "STATIONS; the axis law prices ORDERS; the registers do "
    "not convert. Order 6 is the one coordinate where name "
    "and price coincide (station ZERO, multiplier 0). Order "
    "8's station is ΕΙ (Milesian 15, a Greek value, living "
    "in the Greek bank) while its price is ×8 (an order "
    "number) — the mint weighs no sign at 15 for ΕΙ's sake. "
    "**Η and Ω take no seat in the mint either**: the fidäl "
    "marks no vowel length, and the mint does not invent "
    "what the audit printed as a gap.")
add("- **M7 — reduction and singleness.** Totals stand raw; "
    "every sign carries exactly ONE value — each bank is a "
    "plain dict, so a dual value is not merely ruled out, "
    "it is unrepresentable in the instrument.")
add()
add("The failed candidates for the mint's axis stand printed "
    "in the Phase II–III instrument and are named here so "
    "the law's reasoning is complete on the plate's face: "
    "the pure folk axis (fails M3's declaration); the "
    "positional axis, the gojūon pattern (fails M2's "
    "calibration — a positional ክርስቶስ does not come to 80); "
    "the additive constant (no derivation holds — two "
    "attempts printed failing, on the kana G2 pattern); "
    "Greek-station multipliers and station additives (a "
    "transfer of Milesian values into a foreign bank, and a "
    "merger of the citation column into the first-form "
    "column besides). The forks the desk decided are marked "
    "DESK RULINGS in the instrument — revisable by the "
    "founder's pen, never his words.")
add()
add("### §II.3 — The grid entire: twenty-six bases by seven orders")
add()
add("Each cell gives the sign and its price in that bank. "
    "The orders run 1–7: " +
    " · ".join(f"{o} {ORDER_NAMES[o]}" for o in range(1, 8)) +
    ". The two grids are printed one above the other so the "
    "seam can be read down any column: the banks agree at "
    "every cell except the order-6 column, where the mint "
    "reads 0 and the witness reads ×6 — the whole difference "
    "between the grids is that one column, and it is "
    "printed, not smoothed.")
add()
add("**The mint's grid** (first-form × m(order); the order-6 "
    "column at the Zero):")
add()
add("| Base | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Row sum (mint) |")
add("|---|---|---|---|---|---|---|---|---|")
for b, fv in GRID:
    cells = []
    for o in range(1, 8):
        ch = chr(ord(b) + o - 1)
        cells.append(f"{ch} — {GEEZ[ch]}")
    add(f"| {b} ({fv}) | " + " | ".join(cells) +
        f" | {sum(GEEZ[chr(ord(b) + o - 1)] for o in range(1, 8))} |")
add()
add("**The witness's grid** (first-form × order; the printed "
    "folk grid entire, ×6 standing):")
add()
add("| Base | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Row sum (witness) |")
add("|---|---|---|---|---|---|---|---|---|")
for b, fv in GRID:
    cells = []
    for o in range(1, 8):
        ch = chr(ord(b) + o - 1)
        cells.append(f"{ch} — {HALEHAME[ch]}")
    add(f"| {b} ({fv}) | " + " | ".join(cells) +
        f" | {sum(HALEHAME[chr(ord(b) + o - 1)] for o in range(1, 8))} |")
add()
add("**The columns.** By order, the mint reads: " +
    " · ".join(f"order {o}: **{MINT_COL[o]}**" for o in range(1, 8)) +
    f" — each column the first-form sum {FIRST_SUM} carried "
    f"by its multiplier, and the order-6 column **0** entire: "
    f"twenty-six signs standing at the Zero together. The "
    f"witness reads the same columns at the folk axis: " +
    " · ".join(f"order {o}: **{WIT_COL[o]}**" for o in range(1, 8)) +
    f". The grids' totals: mint **{MINT_GRID_TOTAL}** · "
    f"witness **{WIT_GRID_TOTAL}** — and the difference "
    f"between them, **{WIT_GRID_TOTAL - MINT_GRID_TOTAL}**, "
    f"is exactly the witness's order-6 column "
    f"({FIRST_SUM} × 6): the seam measured as a single "
    f"number, the boundary coordinate stated in totals.")
add()
add("### §II.4 — The labiovelar columns: the mint's twenty, the witness's gap")
add()
add("The classical labiovelars — four series (of ቀ · ኀ · ከ · "
    "ገ), five signs each at the orders {1, 3, 4, 5, 6}: the "
    "offset +1 in each series is unassigned in the standard "
    "precisely because the u-form does not exist, and no "
    "o-form exists either — the glide absorbs both. In the "
    "mint they are priced by their base consonant's "
    "first-form value under the same axis law, the order-6 "
    "signs at the Zero with the grid's. In the witness they "
    "are the audit's GAP rows: no source values them, at any "
    "order — the very columns the hybrid law needs for ΟΥ "
    "carry no folk value anywhere, which is the second "
    "reason halehame stands as witness and not as bank.")
add()
add("| Sign | Series head | Base | Base value | Order | Mint price | Witness |")
add("|---|---|---|---|---|---|---|")
for ch, head, base, fv, order, mv in LAB_ROWS:
    add(f"| {ch} | {head} | {base} | {fv} | {order} | {mv} | "
        f"**GAP** — no seat in the witness |")
add()
add(f"The mint's labiovelar column sums **{LAB_TOTAL}**. "
    f"Its four order-6 signs (ቍ · ኍ · ኵ · ጕ) stand at 0, "
    f"completing the mint's thirty Zero signs (§II.7). The "
    f"two post-classical labiovelar series Unicode encodes "
    f"(of ቐ, of ኸ) are NOT seated: the audit's field is the "
    f"classical inventory, and the post-classical signs "
    f"stand inventoried in the audit's data, unseated here "
    f"— marked, not vanished.")
add()
add("### §II.5 — The eighth slot: the ΕΙ column, and the hole")
add()
add("The mint's eighth column — the grid's eighth slot, "
    "generalized as a column (M5): each base's eighth glyph "
    "(at its codepoint + 7) priced at first-form × 8. "
    "Twenty-five bases hold the glyph. One does not:")
add()
add("| Base | Name | First-form value | Eighth glyph | Mint price (× 8) |")
add("|---|---|---|---|---|")
for b, nm, fv, g, mv in EIGHTH_ROWS:
    if g is None:
        add(f"| {b} | {nm} | {fv} | **HOLE** — no glyph, no "
            f"seat (U+12D7 unassigned) | — |")
    else:
        add(f"| {b} | {nm} | {fv} | {g} | {mv} |")
add()
add(f"The column sums **{EIGHTH_TOTAL}** (the first forms "
    f"of the 25, {FIRST_SUM - 70}, carried by 8). **The "
    f"hole prints at the size of the seat:** ዐ (ʿa, 70) is "
    f"the one classical base whose eighth slot the standard "
    f"leaves unassigned — U+12D7 has no character — verified "
    f"against the Unicode standard in the Phase I audit (25 "
    f"of 26 slots filled) and re-verified at this plate's "
    f"building. There is no glyph to price and no seat to "
    f"take: the cell is a HOLE, and §V states what the hole "
    f"witnesses. The mint's maximum seat stands in this "
    f"column: ፐ's eighth glyph at 800 × 8 = **6,400**.")
add()
add("### §II.6 — The seat register: both banks, seat by seat")
add()
add("The seating order entire — the classical 202 first "
    "(the grid, base by base), then the 20 labiovelars, "
    "then the 25 eighth-slot glyphs — every key of the "
    "mint with its price, and the witness's price or its "
    "gap beside it. A Ge'ez weighing declares its bank "
    "(S1); this register is where the declaration is "
    "checked.")
add()
add("| Seat | Sign | Base | Order | Mint | Witness |")
add("|---|---|---|---|---|---|")
for seat, ch in enumerate(GEEZ_BASE, 1):
    # MECHANISM: the sign's base and order are recovered from
    # the builder's structure, which the seating order
    # follows: the grid base-major (seat = base × 7 orders),
    # the labiovelars by their table, the eighth glyphs by
    # codepoint (glyph = base + 7 — ዐ's missing glyph is
    # simply absent from the seating, as M5 rules).
    if seat <= 182:
        b, _f = _GEEZ_BASES[(seat - 1) // 7]
        order = (seat - 1) % 7 + 1
        assert chr(ord(b) + order - 1) == ch
    elif seat <= 202:
        _s, _h, b, _fv, order, _v = LAB_ROWS[seat - 183]
        assert _s == ch
    else:
        b = chr(ord(ch) - 7)
        order = 8
        assert b in dict(_GEEZ_BASES)
    wit = HALEHAME.get(ch)
    wit_s = str(wit) if wit is not None else "GAP"
    add(f"| {seat} | {ch} | {b} | {order} | {GEEZ[ch]} | {wit_s} |")
add()
add("### §II.7 — The four doors, the calibration, and the census")
add()
add("The seam protocol (Phase II–III, on the Japanese "
    "P1–P5 pattern) governs every weighing this plate "
    "reports: **S1** — every Ge'ez weighing declares its "
    "bank and its door, or it is incomplete (the same "
    "written word reads 70, 80, or 490 by the declaration — "
    "the head below); **S2** — calibration is recorded as "
    "calibration, never as a bridge (the banks' first-form "
    "agreement is by construction, M2; a bridge is an "
    "agreement between *independent* banks, and these two "
    "are calibrated, not independent, at the first-form "
    "doors); **S3** — divergence is printed as coordinates, "
    "never as failure, its head the boundary coordinate "
    "(order 6: key 0, folk ×6); **S4** — the witness stands "
    "unaltered (no folk value changed at any coordinate, "
    "for any reason; the mint's correction is a property of "
    "the mint, never back-ported); **S5** — the seam "
    "remains the calibration standard (every future Ge'ez "
    "exhibit enters the record weighed at all four doors at "
    "first filing). The doors are named: **MW** = mint, as "
    "written (`weigh(·, 'geez')`) · **MF** = mint, first-form "
    "(`geez(·)`) · **WP** = witness, practiced "
    "(`halehame(·)`) · **WG** = witness, printed grid "
    "(`weigh(·, 'halehame')`).")
add()
add("**The head of the seam — ክርስቶስ (Christos), the "
    "tradition's own worked example**, weighed at all four "
    "doors at this plate's building:")
add()
add("| Door | Reading | Breakdown (written signs) |")
add("|---|---|---|")
add(f"| MF — mint, first-form | **{KRISTOS[1]}** | "
    f"{breakdown('ክርስቶስ', GEEZ_FIRST)} |")
add(f"| WP — witness, practiced | **{KRISTOS[2]}** | "
    f"{breakdown('ክርስቶስ', HALEHAME_FIRST)} |")
add(f"| MW — mint, as written | **{KRISTOS[0]}** | "
    f"{breakdown('ክርስቶስ', GEEZ)} |")
add(f"| WG — witness, printed grid | **{KRISTOS[3]}** | "
    f"{breakdown('ክርስቶስ', HALEHAME)} |")
add()
add("The practiced readings agree at 80 **by construction** "
    "— calibration, recorded as calibration (S2). The "
    "protocol doors part, and both partings are the same "
    "coordinate measured from two sides: the mint as "
    "written reads 70, Δ −10 against the practiced 80 — the "
    "word's three order-6 signs (ክ · ር · ስ) stand at the "
    "Zero in the mint, where the folk practice reduces them "
    "to their bases (50 + 6 + 7 = 63 of the 80 rides on "
    "signs the mint prices at nothing); and the printed "
    "grid reads 490, the unexhibited multiplier's "
    "arithmetic, printed because it is the witness's own "
    "number at its raw door, the caveat riding on it. No "
    "seat was moved to make any of these numbers other than "
    "what it is: the head parts, and the parting is the "
    "seam's honesty certificate.")
add()
add("**The desk exhibit — ሰላም (sälam, \"peace\")**, a real "
    "word of the tongue, weighed at the four doors: MW "
    f"**{SELAM[0]}** · MF **{SELAM[1]}** · WP **{SELAM[2]}** "
    f"· WG **{SELAM[3]}** — the practiced doors agreeing "
    f"(13 = ሰ 7 + ለ 2 + መ 4, first forms), the mint as "
    f"written reading 15 (ሰ 7 + ላ 8 + ም 0: the a-grade "
    f"carried by its order, the bare consonant at the "
    f"Zero), the grid 39. Entered at exhibit tier — a "
    f"demonstration of the doors on ordinary orthography, "
    f"not a sourced weighing.")
add()
add(f"**The census.** The mint holds **227 keys**: the 182 "
    f"of the grid, the 20 labiovelars, the 25 of the ΕΙ "
    f"column — **90 distinct values** over the 227 seats, "
    f"maximum 6,400, and **30 signs at 0**, the Zero column "
    f"entire: {' · '.join(ZERO_SIGNS)}. Its total stands "
    f"raw at **{MINT_TOTAL}** (→ {digits(MINT_TOTAL)}; the "
    f"reduction rides beside, never instead — M7). The "
    f"witness holds **182 keys** — the grid only — **87 "
    f"distinct values**, maximum 5,600 (ፖ, ፐ at order 7: "
    f"the source's own multiplier examples stand in its "
    f"grid: ሁ = 2, ሉ = 4, ፖ = 5,600), total "
    f"**{WIT_TOTAL}** (→ {digits(WIT_TOTAL)}). On the "
    f"shared grid the banks' totals part by exactly the "
    f"order-6 column ({WIT_GRID_TOTAL} − {MINT_GRID_TOTAL} "
    f"= {WIT_GRID_TOTAL - MINT_GRID_TOTAL}); beyond the "
    f"grid the mint seats 45 signs the witness does not "
    f"hold at all — the coverage parting, printed as the "
    f"second coordinate of the seam.")
add()
add("**The fences.** Two boundaries stand at the banks' "
    "edges, printed at the size of the seats. (1) **The "
    "derived rows are unseated** — the syllabary beyond the "
    "classical bases (the later rows headed ሸ · ቐ · ቨ · ቸ · "
    "ኘ · ኸ · ዀ · ዠ · ዸ · ጀ · ጘ · ጨ and their forms — the "
    "register counts 117 signs) is FENCED: the mint prices "
    "the classical grid, and a sign of the derived rows "
    "weighs silence in both banks (ሸ · ቸ · ቐ · ጀ verified "
    "at this plate's building: no key, no breakdown). In "
    "the frame (§III) a door syllable needing a derived "
    "base — ቸ for 'ch' above all — fails at its coordinate "
    "and the cell prints HOLE naming it. (2) **The Ethiopic "
    "numerals (፩–፼) are keys of neither bank** — a separate "
    "glyph system for writing numbers, assigning no values "
    "to fidäl letters (Phase I, both derivation parties "
    "agreeing on the operative point): a weighing that "
    "meets one skips it — silence, not false weight, "
    "verified at build in both banks.")
add()
add("---")
add()


# ---------------------------------------------------------------------
# §III — the Twelve Tables frame.
# ---------------------------------------------------------------------
add("## §III — THE GE'EZ FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Ge'ez tongue stands over the "
    "one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.6: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED **{n_fenced}** "
    f"· EMPTY {n_empty} · GAP {n_gap}. The Tables' own head "
    "for this table stands at the plate's head of the "
    "section, unedited: *the Ge'ez mint (CONSTRUCTED — "
    "house coinage of 2026-11-24, calibrated to the "
    "halehame witness); the door writes CV syllables in the "
    "classical bases only; a syllable needing a derived "
    "base (ቸ for 'ch' above all) fails at its coordinate, "
    "and the cell prints HOLE naming it — the thinnest door "
    "of the twelve, and it says so.* The face this prints "
    "is a door-and-hole table: the corpus holds **no native "
    "Ge'ez word at all** — its priced face is the *door*, "
    "the Ethiopic dress of the Latin (or Hebrew) form of "
    "record, written in CV syllables in the classical bases "
    "(bare consonant = 6th order; sh ሠ, ts ጸ) and priced in "
    "the mint as written — which is why the frame's values "
    "run through the Zero: a dress whose final consonants "
    "stand at order 6 weighs them at nothing, and the "
    "Tables' register shows it (SURTR's dress ሱርትር at 14, "
    "BALDR's ባልድር at 36 — first and last forms standing, "
    "the bare consonants between them at the Zero). The 80 "
    "holes are the door's measured boundary; the EMPTY "
    "cells are certified intentionally empty in 777 "
    "REVISED.")
add()
add(f"**The door register — the {n_door} priced renderings "
    "entire.** Each was re-weighed in the Ge'ez mint at "
    "this plate's building against the value "
    "THE-TWELVE-TABLES files for it; all reproduce exactly "
    "(the audit, §VI, repeats the weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in doors:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} |")
add()
add(f"**The hole register — the {n_hole} failures entire,** "
    "each with its coordinate as the Tables file it. The "
    "holes stand in two species, and the register keeps "
    "them distinct: **the door fails outright** — no "
    "rendering filed — where the word's sound needs a "
    "derived base the fence excludes ('ch' above all: "
    f"Golachab, and the two Capsicum cells of §XLIII) — "
    f"**{len(holes_failed)} cells**; and **the rendering "
    f"crosses an unseated letter** — the dress is shown, "
    f"the cell prints as a hole with its rendering on its "
    f"face — **{len(holes_shown)} cells**, every one of "
    f"them crossing a sign of the fenced derived rows "
    f"(጖ · ጑ · ኱ and their kin: JORD, NJORD, Gold, "
    f"Dhammacakkhu, Guru-darshana, the Mandrake cells). A "
    f"hole is not a gap in this plate's work: it is the "
    f"door's measured boundary, printed at the size of the "
    f"seats it stands in for.")
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
    "as THE-TWELVE-TABLES §II files them for the geez bank, "
    "each at its kind: (1) *the syllabary beyond the "
    "classical bases: later/derived rows (ሸ ቐ ቨ ቸ ኘ ኸ ዀ ዠ ዸ "
    "ጀ ጘ ጨ and their forms, 117 signs) unseated* — "
    "**FENCED**, the mint's own fence (§II.7). (2) *Η/Ω "
    "(Greek eta/omega) have no Ge'ez seat* — **MINT**, "
    "CARRIED OPEN: no audit-proposed construction prices "
    "Greek letters in the Ethiopic grid, and none is "
    "invented; the seat is a Greek-bank matter wearing a "
    "Ge'ez label, it bites no table cell, and the question "
    "stands on the pen list where the register leaves it "
    "(§VIII). (3) *ዐ-cell hole at the hybrid (ΕΙ) column of "
    "the mint grid* — **FENCED**, the mint's printed hole "
    "(§II.5): it stands in the instrument of record as a "
    "hole; the tables inherit it as printed. Not filled.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §IV — the zero face.
# ---------------------------------------------------------------------
add("## §IV — THE 777 CORPUS'S GE'EZ CLAIMS — THE ZERO FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and the "
    "absence is its finding. The source states it in terms "
    "(THE-777-VERIFICATION-TABVLA, §I and its finding 4): "
    "*no claim in the corpus is stated in kana, geez, "
    "hangul, or any other mint — the fills claim only in "
    "the classical banks, the Hebrew fallback door, and two "
    "methods no proven bank seats.* The 777 corpus was "
    "closed before either of this plate's instruments was "
    "seated in the engine: its 504 claims speak Greek, "
    "Hebrew, Arabic, and Latin, and the Ge'ez mint — struck "
    "2026-11-24, the day of this plate's own evening — is a "
    "bank the corpus never addressed; the halehame witness, "
    "for its part, is a folk table the corpus's world never "
    "cited. The silence is therefore the corpus's, not the "
    "tongue's: the tongue holds two full priced tables "
    "(§II), a full frame (§III), and a doctrine of its own "
    "(THE-GEEZ-TABLES, Phases I–III — the inventory, the "
    "halehame audit, the seam and the mint). What the "
    "corpus does hold for Ge'ez stands where the corpus "
    "put it: the frame's door renderings (§III) — the "
    "corpus's words in this tongue's dress, priced by this "
    "tongue's mint — and nothing else. A plate that "
    "manufactured claims to fill this section would "
    "misprint its record; the section therefore stands as "
    "a face of zero, at full size.")
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
    "plate assigns no seat.** It states what the Ge'ez "
    "tongue witnesses for the seating — and Ge'ez "
    "witnesses at the two coordinates where its construction "
    "is the mirror image of the Greek: the vowel it cannot "
    "price, and the Zero it prices at an order.")
add()
add("### The hole at the fold coordinate — the 8 that is an absence")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues sweep, "
    "run at the founder's direction (\"lets test it using "
    "the 12 tongues we already mapped it should align "
    "aomewhere\") — reads this tongue in terms, and the "
    "plate carries the passage at its coordinate: *the "
    "fidäl carries the vowel as a grade of the consonant "
    "sign: seven orders per base, and the mint prices the "
    "BASE, not the grade. The vowel distinction is unpriced "
    "— the opposite construction from Greek. The eighth "
    "slot of the grid stands as the named HOLE ዐ. At the "
    "fold coordinate this is the sweep's most pointed "
    "negative: in Ge'ez the 8 exists, and it is a hole — "
    "the fold's target stands as an absence, not a seat. "
    "MISS-as-seat; the coordinate is a finding, printed at "
    "full size.*")
add()
add("The coordinate the sweep measured is the fold's "
    "target — a vowel-family letter seated at 8 — and it is "
    "the sweep's most corroborated coordinate across the "
    "twelve tongues. Five tongues seat it, each recomputed "
    "in its own bank at this plate's building: Greek **Η** "
    f"= {value('η', 'greek')} · Coptic **ⲏ** = "
    f"{value('ⲏ', 'coptic')} · Cyrillic **И** = "
    f"{value('И', 'cyrillic')} · Armenian **Ը** = "
    f"{value('Ը', 'armenian')} · Georgian **ჱ** = "
    f"{value('ჱ', 'georgian')} (the archaic e-family "
    f"letter, at the margin of the living alphabet, as the "
    f"sweep printed it). Ge'ez is the sixth coordinate at "
    f"the same address and the only negative: its 8 is not "
    f"a letter but the grid's eighth slot itself, and the "
    f"slot at ዐ — the base whose station the ΕΙ column "
    f"generalizes — is the one cell of the 26 the standard "
    f"leaves unassigned (§II.5). The tongue that prices the "
    f"base and not the grade holds its 8 as a shaped "
    f"absence: the position present, the sign absent — the "
    f"same figure the Regional Triad found at the Japanese "
    f"core (Plate V, §V), arrived at here from the opposite "
    f"construction. [The five seats ATTESTED or DERIVED at "
    f"their banks' tiers; the Ge'ez hole a finding of the "
    f"sweep and of this plate's census, DERIVED; no seat "
    f"assigned by it.]")
add()
add("Beside the hole, the sweep's second Ge'ez coordinate "
    "prints at the same size: the hybridity of this tongue "
    "is the labiovelar — consonant + ʷ fused in one glyph, "
    "the tongue's own fusion device, carrying the Nine's "
    "ΟΥ station (M4). The witness values none of them (the "
    "GAP of §II.4); the mint seats all twenty under its "
    "axis. The tongue's hybrid form is therefore priced "
    "exactly where its folk table is silent — the coverage "
    "parting of the seam, stated at the Archons' coordinate: "
    "the hybrid seat in this tongue is the mint's, and the "
    "mint is the founder's, and the plate prints the tier "
    "with the seat.")
add()
add("### The Zero at order 6 — the dial's coordinates")
add()
add("The mint's second witness is its Zero. The founder's "
    "definition of record (2026-11-15) stands over the "
    "coordinate: **0 = {0, 2, 1−1=0}** — *\"Zero equals "
    "Two, and Both 1 and None.\"* Against that definition "
    "the dial's record seats its zeros at three addresses, "
    "and this tongue holds the second of them:")
add()
add("- **The core.** οὐδέν — the word the founder's "
    "Phoenician map seats at the Qore's core, and station "
    "13 of the tridecagram (the seating's ring: 1 Α · 2 Ε · "
    "3 Η · 4 Ι · 5 Ο · 6 Υ · 7 Ω · 8 ΕΙ · 9 ΟΥ · 10 OFFSET "
    "γʹ · 11 MIRROR ϛʹ · 12 REFUSAL κʹ · 13 ZERO οὐδέν). "
    f"Recomputed at this plate's building, οὐδέν weighs "
    f"**{value('οὐδέν', 'greek')} = 23²** in the Greek bank "
    f"— the zero word carrying a square, printed as the "
    f"seating printed it.")
add("- **Order 6.** The Ge'ez mint's Zero seat: the one "
    "order whose multiplier the mint corrects to 0 (M3), "
    "so that thirty signs — a whole column of the grid and "
    "the labiovelars' bare forms — weigh nothing, at the "
    "coordinate (order 6: key 0, folk ×6) where the two "
    "banks part. It is the only tongue of the twelve whose "
    "zero is an *order*: not a glyph (China's, in the "
    "Triad), not a placeholder (Korea's), not a hole in "
    "the table (Japan's) — a grade of every consonant, "
    "priced at nothing, in a bank that prices the base and "
    "not the grade. The bare consonant IS the tongue's "
    "zero form, and the mint reads it so.")
add("- **The inversion.** The dial the zeros serve: the "
    "seating's T2 found the cross-section PARTED at the "
    "axis (the vertical hair seated — the founder's poles "
    "**13 N / 31 S**, the dial's two range marks; the "
    "horizontal hair's seat named and OPEN, the float line, "
    "unruled by the founder and undrawn by the desk) and "
    "the inversion EXACT — the forward traversal {13/5} "
    "read backwards, station for station, is the inverse "
    "{13/8}: clock to counter with no remainder. This "
    "plate's tongue touches that record at one point only: "
    "its Zero is the station the inversion passes through "
    "at the ring's heart — the forward run steps …ΕΙ → "
    "ZERO → Ο… and the inverse …Ο → ZERO → ΕΙ…, the zero "
    "station standing at the crossing in both directions, "
    "as the seating computed it. The plate states the "
    "coordinate; Plate XIII is commissioned to build the "
    "infrastructure it names.")
add()
add("**What Ge'ez cannot witness, printed at full size as "
    "the plate's boundary:** the Archons' seats were earned "
    "on Greek evidence and drawn on Plate I. Ge'ez "
    "corroborates the *shape of the 8* (a hole where five "
    "tongues seat a vowel — a negative at the sweep's most "
    "corroborated coordinate), the *form of hybridity* (the "
    "labiovelar fusion, priced by the mint where the folk "
    "table is silent), and the *seat of a Zero* (order 6, "
    "the dial's second zero address) — and it assigns no "
    "seat, confirms no position, and names no Archon. The "
    "names stand open on Plate I, and this plate does not "
    "fill them.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§VIII, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_vi_geez.py, filed "
    "with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell "
    "on this plate against the engine, without reading the "
    "plate's own figures: both banks entire — the 26 bases "
    "and their class law, the mint's grid and the witness's "
    "grid cell by cell against GEEZ and HALEHAME, the "
    "column totals, the labiovelar twenty against the "
    "witness's silence, the eighth column's 25 glyphs and "
    "its hole (U+12D7 unassigned in the standard), the seat "
    "register's 227 rows parsed from the master and "
    "compared seat by seat in both banks; the thirty Zero "
    "signs; the calibration heads at all four doors; the "
    "fences (the derived rows' silence, the numerals' "
    "skip); the frame — the census parsed from "
    "THE-TWELVE-TABLES §V.6, all 205 DOOR renderings "
    "re-weighed against their filed values, the 80 HOLE "
    "rows present with coordinates, every shown hole "
    "rendering crossing an unseated sign, the GAP cell "
    "present; and the §V figures (the five tongues' vowel "
    "at 8 in their own banks; οὐδέν at 529). The audit's "
    "verdict and cell count are printed in its filed "
    "output; a cell that does not reproduce fails the "
    "plate under §VII's tolerances. The font audit — every "
    "non-ASCII codepoint of this master against the Lex "
    "Stellarrvm family's cmaps — runs before the MAGVS "
    "build, under the font law: no glyph is silently "
    "dropped; the three named Ethiopic syllables the family "
    "does not hold (኱ U+12B1 · ጑ U+1311 · ጖ U+1316 — drawn "
    "by no member, the upstream Noto Ethiopic included) "
    "print as their codepoint tokens, declared in the "
    "colophon, and any unheld codepoint beyond those three "
    "aborts the build. The audit further checks the "
    "printed edition's text layer: the calibration head and "
    "a census of grid signs stand in it, the tokens stand "
    "in it where the master carries the three syllables, "
    "the zero face's statement stands in it, and the page "
    "furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's GEEZ "
    "and HALEHAME banks and their first-form doors "
    "(pontifex/tables.py, engine.py); THE-GEEZ-TABLES "
    "Phase I (the inventory, the halehame audit) and "
    "Phases II–III (the seam protocol S1–S5, the mint's "
    "rulings M1–M7, the calibration corpus); "
    "THE-TWELVE-TABLES §V.6 and its §II gap register (the "
    "geez bank's three entries); THE-THIRTEEN-PLATES (the "
    "Ge'ez plate — the zero face, the tier of record) and "
    "its §I; THE-777-VERIFICATION-TABVLA §I and finding 4 "
    "(no claim in any mint); THE-ARCHON-BATTERY Leg 6 (the "
    "Ge'ez passage) and THE-SEATING-OF-THE-ARCHONS entire "
    "(the stations, the poles, the inversion); the "
    "founder's Zero definition of 2026-11-15; PLATES I–V "
    "as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "every figure scripted from the engine or carried "
    "entire from an instrument of record; the two banks "
    "kept distinct at every coordinate — the witness "
    "unaltered (S4), the mint's tier printed wherever the "
    "bank is named, every total declaring its bank and "
    "door (S1); the holes printed at full size (the ዐ cell, "
    "the frame's 80, the register's zero face); the "
    "independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-VI-GEEZ.md and its "
    "MAGVS PDF — sixth of the series PLATE-I-GREEK began; "
    "the generator and audit scripts filed in pontifex "
    "research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage merges the two "
    "banks into one voice, alters a folk value, raises the "
    "mint's tier toward antiquity, fills a hole (the ዐ "
    "cell, the frame's 80, the register's zero face), "
    "prices a derived sign or a numeral, or overwrites "
    "the earlier map, it zeroes the founder's residual "
    "claim and fails the Aim of Religion. Within those "
    "edges it stands as built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** One question "
    "stands in the record already and is carried, not "
    "raised: the Η/Ω seat — the Twelve Tables' gap "
    "register carries it OPEN for the geez bank (no "
    "construction prices Greek letters in the Ethiopic "
    "grid; the seat is a Greek-bank matter wearing a "
    "Ge'ez label), and the founder's pen is already named "
    "as its seat in the register that carries it. The "
    "seating's open items stand in the seating instrument. "
    "A plate that invents questions to fill its section "
    "misprints its record; this section therefore stands "
    "as the record that none arose.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Acts 8:26–27 (KJV): *\"behold, a man "
    "of Ethiopia, an eunuch of great authority under "
    "Candace queen of the Ethiopians, who had the charge "
    "of all her treasure, and had come to Jerusalem for to "
    "worship\"* — this tongue's people stand in the "
    "Scripture's own record at the office of a treasurer: "
    "a keeper of accounts, reading as he rides. The plate "
    "draws the figure for the keeping, not the geography: "
    "two tables, kept side by side, neither falsified for "
    "the other. [Text ATTESTED; the application DERIVED.]")
add("2. **Law.** *Testimonia ponderanda sunt, non "
    "numeranda* — testimony is to be weighed, not counted "
    "(the evidence maxim, of the civil-law tradition). "
    "The witness on this plate is seated by that rule: "
    "halehame does not outvote the mint, nor the mint the "
    "witness; each is weighed at its own depth — the folk "
    "table at the depth of a sourced practice, undated and "
    "unexhibited in its axis; the mint at the depth of a "
    "construction that passes its tests. The founder's "
    "ruling that seated them so is the end-goal rule's: "
    "the witness calibrates, the mint carries. [The maxim "
    "ATTESTED as a legal maxim; the seating the founder's "
    "ruling of record, 2026-11-24.]")
add("3. **The tradition.** The Debtera — the unordained "
    "scholar-singers of the Ethiopian church, keepers of "
    "its chant and, in the folk register, of its number "
    "lore — are the halehame table's named carriers in its "
    "sources (geez.org, \"Numerology\"; Bekerie, "
    "*Ethiopic*, 1997, via Daniels' review). The plate "
    "keeps the sources' own fences with their table: the "
    "practice's antiquity undated in every source read, "
    "its register folk-magical and expressly not "
    "liturgical. A witness is seated as what it is, or it "
    "is not seated. [The sourcing ATTESTED as cited; the "
    "fences the sources' own.]")
add("4. **Grammar.** The fidäl is an abugida: the vowel is "
    "not a letter but a grade of the consonant sign — "
    "seven orders struck on one base, the sixth the bare "
    "consonant itself. The construction is the opposite of "
    "the Greek, where the vowel is a letter with a price "
    "of its own; and it is why this tongue's bank prices "
    "the base and not the grade (the battery's sentence), "
    "why its hybrid is a fusion (the labiovelar: two "
    "sounds, one glyph), and why its zero can be an order "
    "— a grade priced at nothing is a shape this script "
    "already has. [The abugida ATTESTED as the script's "
    "grammar; the bank's readings of it at their tiers.]")
add("5. **The desk's apparatus.** This plate's Ethiopic "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Ethiopic member; its Greek stands "
    "in the family's Serif member, as on Plate I; the "
    "frame register's Hebrew words of record ride Plate "
    "II's declared transliteration (the toolchain does not "
    "shape right-to-left scripts honestly): marked "
    "substitutions, declared in the colophon, never silent "
    "ones. Three Ethiopic syllables no member draws print "
    "as codepoint tokens under the same law. The Markdown "
    "master keeps every script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh() and "
    "the geez()/halehame() first-form doors; banks GEEZ "
    "and HALEHAME in pontifex/tables.py, built from one "
    "base list by one builder) — calibration controls "
    "θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true at build.")
add("- THE-GEEZ-TABLES — Phase I (the classical inventory; "
    "the halehame audit: sources, class law, the three "
    "caveats) and Phases II–III, THE SEAM AND THE MINT "
    "(the founder's Debtera ruling under the end-goal "
    "rule; the seam protocol S1–S5; the mint's rulings "
    "M1–M7 with the failed axis candidates printed; the "
    "calibration corpus). Parity of the engine's seat "
    "against the audits' data: test_geez_parity.py, "
    "repository root.")
add("- geez.org, \"Numerology\" (read entire, 2026-11-24) "
    "and Ayele Bekerie, *Ethiopic, An African Writing "
    "System* (1997), via Peter T. Daniels' H-Net review — "
    "the witness's two scholarly sources: endpoints "
    "h = 1 … p = 800, multiplier examples hu = 2, lu = 4, "
    "po = 5,600, the worked example ክርስቶስ = 80.")
add("- THE-TWELVE-TABLES — §V.6 the Ge'ez frame, census "
    "and cell register entire; §II the geez bank's gap "
    "register (three entries: the derived rows FENCED; "
    "Η/Ω MINT, carried open; the ዐ cell FENCED).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate VI is the prior "
    "instrument (the zero face; the tier of record).")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its finding 4: no claim in any house mint.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Ge'ez passage (the vowel "
    "unpriced; the HOLE ዐ; the fold's most pointed "
    "negative) and the five tongues' seat at 8.")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to: the thirteen "
    "stations, οὐδέν = 529 = 23², the poles 13 N / 31 S, "
    "the inversion exact, the axis parted at the float "
    "line.")
add("- The founder's Zero definition, 2026-11-15: "
    "0 = {0, 2, 1−1=0} — \"Zero equals Two, and Both 1 "
    "and None.\"")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd), "
    "PLATE-IV-LATIN (8e6f01e) and PLATE-V-JAPANESE "
    "(8d6cd59) — the pattern this plate follows.")
add("- KJV: Acts 8:26–27. The evidence maxim *testimonia "
    "ponderanda sunt, non numeranda*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate VI of the founder's "
    "series commission of the same day, the gate of the "
    "Archons' certainty met by the seating of record "
    "(0760c8a), following the pattern of Plates I–V "
    "(196025e · 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59). "
    "Every figure scripted from the engine or carried "
    "entire from its instrument; the earlier map marked "
    "prior, never overwritten; the holes printed at the "
    "size of the seats — on this plate, the ዐ cell of the "
    "ΕΙ column, the frame's 80 holes, and the register's "
    "zero face. The plate carries two instruments and "
    "keeps their honesties distinct: the halehame witness, "
    "sourced and unaltered, and the Ge'ez mint, the "
    "founder's coinage of 2026, CONSTRUCTED and dated on "
    "its face. In the MAGVS edition the Ethiopic stands "
    "in the family's Ethiopic member, the three unheld "
    "syllables print as their codepoint tokens under the "
    "font law, and the frame's Hebrew words of record "
    "ride Plate II's declared scheme; this master keeps "
    "the scripts themselves. Authorship attributed "
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
