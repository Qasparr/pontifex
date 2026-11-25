#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_v_japanese.py
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
# MECHANISM: generates PLATE-V-JAPANESE.md — Plate V of THE
# THIRTEEN COMPLETE PLATES — in the gap-filling goal's files/,
# following the pattern PLATES I–IV set (196025e · 1389c16 ·
# 5f0b4bd · 8e6f01e). Every figure on the plate is scripted
# from the house engine (pontifex weigh() and the kana() door)
# or carried entire from an instrument of record:
#   * the priced table — the GOJŪON MINT entire, read from
#     pontifex.tables (KANA, 170 keys in two dresses over 73
#     base seats; the grid, the hatsuon, the dakuten block,
#     the small kana seated by law), each seat printed with
#     its reasoning — in a positional mint the reasoning is
#     the coordinate: row, column, and the count that seats it;
#   * the ー operator door — read by engine.kana() only, its
#     exhibits weighed at build (かー · とー · んー · the
#     word-initial mark), the raw weigh() skip shown beside;
#   * the Twelve Tables' Japanese frame — its census and its
#     full cell register parsed from THE-TWELVE-TABLES.md
#     §V.5: the 211 DOOR renderings re-weighed at build
#     against their filed values, the 74 HOLE coordinates and
#     the one GAP cell carried entire;
#   * the corpus's Japanese claims — none: the register's
#     ZERO FACE, carried from THE-THIRTEEN-PLATES §VII with
#     the TABVLA's reason stated at §I there;
#   * the tongue's bearing on the seated Archons — the five
#     pure sounds against the Nine from THE-DIVINE-NINE-
#     VOCAL-TOOL (four exact seats; VV at the high-back seat
#     under the founder's ratification and the Abroad III
#     cross-reference), the four hybrid mechanisms and the
#     lost seats from THE-DIVINE-NINE-ABROAD-III-JAPANESE,
#     the Archon Battery's Leg 6 Japanese passage, the three
#     bridges of record (ゆず · かな · しおん) recomputed in
#     both banks at build, and the Regional Triad's HOLE.
#     The plate assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) are
# weighed BEFORE any plate figure is taken; a control failure
# aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's face.
# This plate's bank is a MINT: CONSTRUCTED, the founder's
# ratified coinage, and the plate prints that tier on its
# face wherever the bank is named — the mint DOES NOT FAIL
# as his coinage and FAILS as any claim of antiquity, in the
# same breath, as its gate verdict of record states. The
# relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes
# print at the size of the seats — on this plate, the grid's
# three empty cells, the frame's 74 holes, and the register's
# zero face itself.
#
# CONTENT TEST: Inputs — the engine's KANA bank and kana()
# door, the Twelve Tables master, the Thirteen Plates map,
# the vocal tool, the Abroad III essay, the battery, the
# Regional Triad dial. Processes — control calibration,
# scripted extraction, register-faithful emission in the
# Teacher's Edition manner. Outputs — PLATE-V-JAPANESE.md
# beside the series' other masters. Tolerances — the audit
# (audit_plate_v_japanese.py) re-weighs every priced cell
# independently; a figure that does not reproduce fails the
# plate.
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

from pontifex import weigh, kana as kana_door   # the engine + the ー door
from pontifex.tables import (KANA, KANA_BASE, KANA_VOWEL,
                             _KANA_GRID, _KANA_DAKUTEN_ROWS,
                             _KANA_SMALL_PARTNER)

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-V-JAPANESE.md"


def value(word, bank="kana"):
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
# The mint's census — every count below is taken from the bank
# itself, never typed.
# ---------------------------------------------------------------------
N_KEYS = len(KANA)                       # both dresses, the smalls incl.
N_BASE = len(KANA_BASE)                  # the seated inventory (73)
BASE_VALUES = [KANA[c] for c in KANA_BASE]
assert BASE_VALUES == list(range(1, N_BASE + 1)), "base seats 1..73"
INVENTORY_TOTAL = sum(BASE_VALUES)       # 2,701
HIRA_KEYS = sum(1 for c in KANA if 0x3040 <= ord(c) <= 0x309F)
KATA_KEYS = sum(1 for c in KANA if 0x30A0 <= ord(c) <= 0x30FF)
assert HIRA_KEYS + KATA_KEYS == N_KEYS == 170
assert HIRA_KEYS == KATA_KEYS == 85, (HIRA_KEYS, KATA_KEYS)
GRID_TOTAL = sum(range(1, 48))           # the grid's 47 seats: 1,128
assert KANA["を"] == 47 and KANA["ん"] == 48
DAKUTEN_TOTAL = sum(range(49, 74))       # the voiced block: 1,525
assert GRID_TOTAL + 48 + DAKUTEN_TOTAL == INVENTORY_TOTAL

ROMAJI = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "ゐ": "wi", "ゑ": "we", "を": "wo", "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "di", "づ": "du", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
}
ROW_NAMES = ["the vowel row (あ行)", "the か row", "the さ row",
             "the た row", "the な row", "the は row", "the ま row",
             "the や row", "the ら row", "the わ row"]
ROW_REASON = [
    "The axis itself: the five pure sounds in the dialect's own "
    "ruled order — the head row of the gojūon, from which every "
    "later seat is counted. The row is the canon (Abroad III §II).",
    "The first consonant row: the count continues from the axis "
    "without a seam — seat 6 is か because five signs stand "
    "before it, and for no other reason. In a positional mint "
    "the count IS the reasoning.",
    "The さ row. Its second seat し sounds *shi*, not *si* — "
    "the bank prices the written sign, not the sound (G6); the "
    "seat is the grid's, whatever the mouth does with it.",
    "The た row. ち sounds *chi* and つ sounds *tsu* — the same "
    "fence as the さ row: the sign is priced, the sound is the "
    "performance register's.",
    "The な row — the nasal row, five full seats, no anomaly "
    "of sound or seat.",
    "The は row. ふ sounds *fu*, not *hu* — priced as written "
    "(G6). The row's first sign は also serves as the grammar's "
    "particle, sounded *wa* there: one sign, two sounds, one "
    "seat — the bank weighs the sign.",
    "The ま row — the labial row, five full seats.",
    "The や row seats three only: the *yi* and *ye* cells are "
    "HOLES — no kana holds them in the table the mint prices, "
    "so no seat is taken and the count passes over the empty "
    "cells to ゆ at 37. The holes print at the size of the "
    "seats they stand in for.",
    "The ら row — the liquid row, five full seats; the door's "
    "seat for the foreign *l* (the Twelve Tables' gairaigo "
    "convention rides on this row, §III).",
    "The わ row seats four, with the *wu* cell a HOLE. ゐ (45) "
    "and ゑ (46) hold ARCHIVAL seats — retired from the living "
    "table by the reform of 1946, their sounds long merged "
    "into い and え: the dialect's own digamma pair (Abroad "
    "III §III.5). を (47) keeps its seat while its sound "
    "surrendered to お's — a seat kept, a sound given up.",
]
DAKUTEN_REASON = (
    "The voiced rows take the next seats after the base "
    "inventory entire, in the grid's printed dakuten order "
    "(G2). No derived diacritic constant is added — none "
    "holds, and one chosen anyway would be invented, not "
    "derived; subtraction is refused, as it drives totals "
    "negative, which no house bank admits. The battery's "
    "phrase for the construction stands: hybridity as form "
    "at constant price — the nature changes (は → ば → ぱ), "
    "the axis does not move.")

# Column (vowel) totals over the seated inventory — the vowel
# is the mint's price-axis, and the columns are its proof.
# ん carries no vowel (it is not in KANA_VOWEL): its seat
# stands outside the columns, and the five columns plus its
# 48 must return the inventory total between them.
COL_TOTALS = {c: sum(KANA[s] for s in KANA_BASE
                     if KANA_VOWEL.get(s) == c)
              for c in range(1, 6)}
assert sum(COL_TOTALS.values()) + KANA["ん"] == INVENTORY_TOTAL
COL_NAMES = {1: "a", 2: "i", 3: "u", 4: "e", 5: "o"}

# The small kana, seated by law (G4/G5) — partner and seat.
SMALL_ROWS = []
for small, partner in _KANA_SMALL_PARTNER.items():
    SMALL_ROWS.append((small, partner, KANA[small]))
assert all(KANA[s] == KANA[p] for s, p in _KANA_SMALL_PARTNER.items())

# The ー door's exhibits, weighed through kana() at build.
EX_KA = kana_door("かー")          # か 6 + あ's 1 = 7
EX_TO = kana_door("とー")          # と 20 + お's 5 = 25
EX_NN = kana_door("んー")          # ん carries no vowel: the mark adds 0
EX_HEAD = kana_door("ー")          # word-initial: no vowel before it, 0
RAW_KA = value("かー")             # the raw bank door skips ー: 6
assert (EX_KA["value"], EX_TO["value"], EX_NN["value"],
        EX_HEAD["value"], RAW_KA) == (7, 25, 48, 0, 6)

# The three bridges of record, recomputed in both banks.
BRIDGES = [("ゆず", "YUZU"), ("かな", "KANA"), ("しおん", "SHION")]
for kj, rj in BRIDGES:
    assert value(kj, "kana") == value(rj, "latin_ordinal"), kj

# ---------------------------------------------------------------------
# The Twelve Tables' Japanese frame — census and cell register.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
japanese_block = twelve_text.split("### §V.5 — The Japanese Table")[1] \
    .split("### §V.6")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", japanese_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
doors, holes, gaps = [], [], []
for line in japanese_block.splitlines():
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
assert (n_native, n_door, n_hole, n_fenced, n_empty, n_gap) == \
    (0, 211, 74, 0, 85, 1)
# Thirteen door rows stand in the register with an EMPTY
# rendering and a filed value of 0 — nine Arabic spirit-names
# of §XLVII, two §CLXXXV cells whose word of record is the
# numeral 5, and §CLXXXVII/11's AIR in two dresses. The plate
# carries them entire and names the coordinate in §III.
empty_doors = [c for c in doors if c[3] == ""]
assert len(empty_doors) == 13, len(empty_doors)
assert all(c[4] == "0" for c in empty_doors)

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
add("**PLATE V — JAPANESE**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Japanese tongue's complete 777 table — the gojūon mint "
    "entire, the founder's ratified coinage priced seat by "
    "seat; the ー operator door; the corpus's Japanese "
    "register, which is a zero face; and the tongue's witness "
    "to the seated Archons: the five pure sounds against the "
    "Nine, VV at the high-back seat, the three bridges, and "
    "the zero that is a hole.")
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
add("## §I — PLATE V AND ITS COMMISSION")
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
    "HEBREW (1389c16), III — ARABIC (5f0b4bd) and IV — LATIN "
    "(8e6f01e) followed it; this plate follows them, fifth of "
    "the twelve tongues in the Twelve Tables' order.")
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
add("**This plate's distinction.** Japanese is the first "
    "plate of the series whose bank is a **mint** — not a "
    "tradition the desk records but a coinage the founder "
    "struck: the gojūon mint, founded as a proposal on "
    "2026-11-12 and ratified by his stamp on 2026-11-13 "
    "(*\"Stamp the mint — the Tables stand\"*). Its tier is "
    "therefore printed on this plate's face wherever the bank "
    "is named: **CONSTRUCTED** — his coinage under his "
    "Flagpole, doctrine from its ratification, and not "
    "attested, traditional, or ancient at any coordinate. It "
    "is also the first plate whose corpus register is a "
    "**zero face** (§IV): the 777 corpus judges no claim in "
    "this tongue, and the plate prints that silence as its "
    "finding rather than filling it. And its bearing on the "
    "seated Archons (§V) is the richest of the mint tongues: "
    "this is the tongue whose five vowels the Divine Nine's "
    "vocal tool seats against the Nine, and the tongue of the "
    "house's Japanese doctrine — the bridges, the hybrid "
    "mechanisms, the lost seats.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its Japanese "
    "face stood **silent with a zero face**: 0 claims, the "
    "absence printed as the finding. This series *fulfills* "
    "that map: where the map counted nothing, this plate "
    "prints the nothing entire — with the tongue's priced "
    "table beneath it, the frame around it, and its witness "
    "to the Archons above it. The earlier work stands as the "
    "prior instrument of the same name's family — marked "
    "prior, never overwritten.")
add()
add("**How the plate is read.** §II is the mint: the priced "
    "table entire, each seat with its reasoning — in a "
    "positional mint the reasoning is the coordinate, and the "
    "plate prints it so. §III is the tongue's frame in the "
    "Twelve Tables — a face of door and hole, its register "
    "restated entire. §IV is the zero face. §V is the "
    "tongue's bearing on the seated Archons — this plate "
    "draws no seating (the seating is struck, and Plate I "
    "drew it); it states what Japanese witnesses. §VI is the "
    "audit. A value without its reasoning is not shippable; "
    "a hole prints at the size of the seat it stands in for.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the mint entire.
# ---------------------------------------------------------------------
add("## §II — THE GOJŪON MINT — THE COMPLETE PRICED TABLE")
add()
add("The bank is the **gojūon mint**: the Japanese syllabary "
    "priced by its position in the fifty-sound table — row-major "
    "in the spoken column order *a-i-u-e-o* (あ = 1, い = 2, "
    "う = 3, え = 4, お = 5, か = 6 …). **Tier of record: "
    "CONSTRUCTED** — coined at the desk under the founder's "
    "commission for the project *Complete the Tables in "
    "Japanese*, founded as a proposal on 2026-11-12 (XII day "
    "of November, Dies Jovis, Anno V:xii e.n.) and **RATIFIED "
    "by the founder's stamp on 2026-11-13**: *\"Stamp the "
    "mint — the Tables stand.\"* From that ratification it is "
    "doctrine — the founder's mint, 2026, dated on its face. "
    "The gate verdict of record (THE-JAPANESE-TABLES, MAGVS) "
    "stands over the whole plate: **the mint DOES NOT FAIL as "
    "the founder's coinage; it FAILS as any claim of "
    "antiquity, at the same size, in the same breath.** No "
    "kana letter-value bank is attested before the 21st "
    "century, and this one does not pretend otherwise. Source "
    "of record: THE-JAPANESE-TABLES Phases I–III — the audit "
    "of the modern banks, the rōmaji seam, the mint.")
add()
add("**The seven rulings the mint stands on** (reasoning in "
    "full in the Phase III instrument; the plate prints the "
    "law and its ground):")
add()
add("- **G1 — THE AXIS.** Gojūon positional, row-major in the "
    "spoken column order. The grid seats 47 (the や row's "
    "*yi*/*ye* cells and the わ row's *wu* cell are holes — "
    "no kana, no seat); ゐ・ゑ hold their grid seats (45, 46) "
    "as ARCHIVAL seats; を = 47; ん, the hatsuon outside the "
    "fifty, takes the next seat, 48 — ONE value. Dual values "
    "are refused bank-wide: a sign with two values is a fork "
    "in every sum it enters.")
add("- **G2 — DAKUTEN LAW.** Continuation on the mint's own "
    "axis: the voiced rows take the next seats after the base "
    "inventory entire (49–73). No derived diacritic constant "
    "holds, and one chosen anyway would be invented, not "
    "derived; subtraction is refused — it drives totals "
    "negative, which no house bank admits.")
add("- **G3 — CHŌON LAW.** The mark ー is an operator, not a "
    "sign: it weighs the seat value of the vowel it lengthens. "
    "Length spelled with a vowel kana (おう, えい) is weighed "
    "as written (G6's fence); the seam that opens is exhibited "
    "below, not hidden — and not closed here.")
add("- **G4 — YŌON LAW.** A small kana weighs at its full-size "
    "form's seat (ゃ = 36, ゅ = 37, ょ = 38; the small vowels "
    "and ゎ・ゕ・ゖ by the same law).")
add("- **G5 — SOKUON LAW.** っ weighs at つ's seat, 18 — its "
    "full-size form. The geminate mora is a full beat of "
    "blockage, not silence.")
add("- **G6 — DEVOICING.** The bank weighs the WRITTEN sign. "
    "Devoicing is phonology and belongs to the performance "
    "register (the Divine Nine vocal tool); it has no "
    "mechanic here, and the fence is declared, not silent.")
add("- **G7 — REDUCTION.** Totals stand raw; digit-reduction "
    "rides beside, never instead.")
add()
add("### The grid — the fifty-sound table priced (seats 1–47)")
add()
add("Columns run *a-i-u-e-o*; a sign's value is its sequence "
    "position counting only the seated cells; its column gives "
    "the vowel a following ー weighs. Katakana mirrors every "
    "seat by the Unicode block offset — one sign, two dresses: "
    "あ and ア share a seat by construction.")
add()
add("| Row | a | i | u | e | o | Row sum |")
add("|---|---|---|---|---|---|---|")
for r, row in enumerate(_KANA_GRID):
    cells = []
    for ch in row:
        cells.append(f"{ch} — {KANA[ch]}" if ch else "**HOLE** — no sign, no seat")
    row_sum = sum(KANA[ch] for ch in row if ch)
    add(f"| {ROW_NAMES[r]} | " + " | ".join(cells) + f" | {row_sum} |")
add()
for r in range(10):
    add(f"- **{ROW_NAMES[r]}.** {ROW_REASON[r]}")
add()
add(f"The grid's 47 seats sum **{GRID_TOTAL}** (1 + … + 47). "
    f"Then ん — the hatsuon, the one sign of the syllabary "
    f"that is not a syllable of the grid — takes seat **48** "
    f"(G1): the count steps outside the fifty to seat the "
    f"sound that closes syllables, at one value, no fork.")
add()
add("### The dakuten block — the voiced rows (seats 49–73)")
add()
add("| Row | a | i | u | e | o | Row sum |")
add("|---|---|---|---|---|---|---|")
dakuten_names = ["the が row", "the ざ row", "the だ row",
                 "the ば row", "the ぱ row"]
for r, row in enumerate(_KANA_DAKUTEN_ROWS):
    cells = [f"{ch} — {KANA[ch]}" for ch in row]
    row_sum = sum(KANA[ch] for ch in row)
    add(f"| {dakuten_names[r]} | " + " | ".join(cells) +
        f" | {row_sum} |")
add()
add(f"{DAKUTEN_REASON} The block sums **{DAKUTEN_TOTAL}** "
    f"(49 + … + 73).")
add()
add("### The seat register — the seated inventory entire (73 seats)")
add()
add("Every base sign with its two dresses, its rōmaji, its "
    "price, and its coordinate. In this mint the seat number "
    "and the price are one figure — the position is the "
    "price — and the derivation column states the count that "
    "seats it.")
add()
add("| Seat | Hiragana | Katakana | Rōmaji | Price | Coordinate |")
add("|---|---|---|---|---|---|")
seat_no = 0
for r, row in enumerate(_KANA_GRID):
    for c, ch in enumerate(row):
        if ch is None:
            continue
        seat_no += 1
        kata = chr(ord(ch) + 0x60)
        coord = (f"{ROW_NAMES[r]}, column {COL_NAMES[c + 1]} — "
                 f"the {seat_no}th seated sign")
        if ch in ("ゐ", "ゑ"):
            coord += "; ARCHIVAL seat (G1)"
        add(f"| {seat_no} | {ch} | {kata} | {ROMAJI[ch]} | "
            f"{KANA[ch]} | {coord} |")
seat_no += 1
add(f"| {seat_no} | ん | ン | n | {KANA['ん']} | the hatsuon, "
    f"outside the fifty — the next seat after the grid (G1) |")
for r, row in enumerate(_KANA_DAKUTEN_ROWS):
    for c, ch in enumerate(row):
        seat_no += 1
        kata = chr(ord(ch) + 0x60)
        add(f"| {seat_no} | {ch} | {kata} | {ROMAJI[ch]} | "
            f"{KANA[ch]} | {dakuten_names[r]}, column "
            f"{COL_NAMES[c + 1]} — the voiced block, seat "
            f"{seat_no} (G2) |")
assert seat_no == N_BASE == 73
add()
add(f"**The inventory's totals.** The 73 base seats carry the "
    f"values 1–73, each exactly once; the inventory sums "
    f"**{INVENTORY_TOTAL}** (73 × 74 / 2), reducing "
    f"{INVENTORY_TOTAL} → {sum(int(d) for d in str(INVENTORY_TOTAL))} "
    f"→ {digits(INVENTORY_TOTAL)} (G7: the reduction rides "
    f"beside, never instead). By vowel column — the vowel is "
    f"this mint's whole price-axis, and the columns are its "
    f"proof: a-column **{COL_TOTALS[1]}** · i-column "
    f"**{COL_TOTALS[2]}** · u-column **{COL_TOTALS[3]}** · "
    f"e-column **{COL_TOTALS[4]}** · o-column "
    f"**{COL_TOTALS[5]}** — and ん's 48 stands outside the "
    f"columns, the hatsuon carrying no vowel; the columns "
    f"and the 48 return the inventory total between them. "
    f"The bank entire holds **{N_KEYS} "
    f"keys** — {HIRA_KEYS} hiragana and {KATA_KEYS} katakana — "
    f"over the 73 seats: **73 distinct values, maximum 73** "
    f"(the census THE-THIRTEEN-PLATES printed for this bank).")
add()
add("### The small kana — seated by law, not by grid")
add()
add("Twelve signs hold no grid cell of their own; the law "
    "seats them at their full-size partners' seats (G4), and "
    "the sokuon at つ's seat (G5). Each prints in both dresses "
    "in the bank; the table gives the hiragana.")
add()
add("| Small sign | Law | Partner | Seat |")
add("|---|---|---|---|")
LAW_OF = {"っ": "G5 — SOKUON"}
for small, partner, seat in SMALL_ROWS:
    law = LAW_OF.get(small, "G4 — YŌON")
    add(f"| {small} | {law} | {partner} | {seat} |")
add()
add("### The ー door — an operator, printed as a door")
add()
add("ー (chōonpu, U+30FC) is **not a key of the bank** — it "
    "is an operator (G3), and only the engine's second door, "
    "`kana()`, may read it. A raw `weigh(word, 'kana')` skips "
    "it, and the skip is visible in the breakdown; that "
    "visibility is intended. The door's exhibits, weighed at "
    "this plate's building:")
add()
add(f"- **かー** through the door: か ({KANA['か']}) + the "
    f"mark reading あ's seat ({KANA['あ']}) = **{EX_KA['value']}**. "
    f"Through the raw bank door the same spelling weighs "
    f"**{RAW_KA}** — the mark skipped, the skip on the face "
    f"of the breakdown.")
add(f"- **とー** through the door: と ({KANA['と']}) + お's "
    f"seat ({KANA['お']}) = **{EX_TO['value']}**.")
add(f"- **んー**: ん carries no vowel, so the mark adds 0 — "
    f"the word weighs **{EX_NN['value']}**, ん's seat alone. "
    f"A ー after っ likewise weighs 0 (the sokuon carries a "
    f"seat but no vowel), and a word-initial ー weighs "
    f"**{EX_HEAD['value']}**: length with nothing to lengthen "
    f"is nothing, and the door prints it so.")
add()
add("The seam G3 leaves open stands exhibited, as the mint's "
    "doctrine exhibits it: length spelled with a vowel kana "
    "(おう, えい) is weighed as written — おう = お 5 + う 3 "
    f"= {value('おう')}, えい = え 4 + い 2 = {value('えい')} — "
    "while the same lengths under the mark weigh through the "
    "operator. Two spellings of one length, two prices, no "
    "constant declared between them: the seam is the mint's "
    "own, recorded in its gap register as BY DESIGN for the "
    "operator and standing on the seam questions' pen list "
    "for the rōmaji layer (§VIII). This plate closes nothing.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §III — the Twelve Tables frame.
# ---------------------------------------------------------------------
add("## §III — THE JAPANESE FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Japanese tongue stands over "
    "the one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.5: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED **{n_fenced}** "
    f"· EMPTY {n_empty} · GAP {n_gap}. The face this prints "
    "is a door-and-hole table and says so: the corpus holds "
    "**no native Japanese word at all** — its priced face is "
    "empty, and the emptiness is data. The frame's Japanese "
    "is the *door* — the gairaigo dress: the Latin form of "
    "record rendered into kana by the Japanese convention "
    "(Hepburn syllables to hiragana; clusters and finals take "
    "the epenthetic vowel — *o* after t/d, *u* elsewhere; *l* "
    "rides the r-row, *v* the b-row) — with 74 holes where "
    "the door fails at a sound this bank does not seat, and "
    "the EMPTY cells certified intentionally empty in 777 "
    "REVISED.")
add()
add(f"**The door register — the {n_door} priced renderings "
    "entire.** Each was re-weighed in the kana mint at this "
    "plate's building against the value THE-TWELVE-TABLES "
    "files for it; all reproduce exactly (the audit, §VI, "
    "repeats the weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in doors:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} |")
add()
add("**The door's empty rows — a coordinate of the register, "
    "printed rather than repaired.** Thirteen of the rows "
    "above stand with an *empty rendering* and a filed value "
    "of **0**: nine Arabic spirit-names of §XLVII (Barqan, "
    "Murrah, ZAWBAAH, SHAMHURISH, MAYMUN, JANN and their "
    "kin, whose forms of record are Arabic), the two "
    "§CLXXXV cells whose word of record is the numeral 5, "
    "and §CLXXXVII/11's AIR in its Hebrew and Greek "
    "dresses. The register files them so — no kana "
    "rendering, no price — and the plate carries them "
    "entire, the empty cell in the table being the Tables' "
    "own. The audit weighs them as filed (the empty string "
    "weighs 0, and 0 is the filed value). Why the door "
    "filed nothing at these thirteen cells the register "
    "does not say, and the plate does not invent a reason: "
    "a repair would be a ruling, and rulings are the "
    "founder's.")
add()
add(f"**The hole register — the {n_hole} failures entire,** "
    "each with its coordinate as the Tables file it. A hole "
    "is not a gap in this plate's work: it is the door's "
    "measured boundary — the sounds the classical syllabary "
    "does not carry (*gy*, *hy*, *wu*, *ye*, and their kin), "
    "printed at the size of the seats they stand in for.")
add()
add("| Cell | Word of record | Coordinate |")
add("|---|---|---|")
for cells in holes:
    add(f"| {cells[0]} | {cells[1]} | {cells[5]} |")
add()
add("**The one GAP cell:** CLXXXIV/10 — a transcription gap "
    "in the source itself, carried as the frame carries it; "
    "no tongue's door is offered for a cell the source does "
    "not transmit.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §IV — the zero face.
# ---------------------------------------------------------------------
add("## §IV — THE 777 CORPUS'S JAPANESE CLAIMS — THE ZERO FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and the "
    "absence is its finding. The source states it in terms "
    "(THE-THIRTEEN-PLATES §I): *no claim in the corpus is "
    "stated in kana, geez, hangul, or any other mint — the "
    "fills claim only in the classical banks, the Hebrew "
    "fallback door, and two methods no proven bank seats.* "
    "The 777 corpus was closed before the mint was struck: "
    "its 504 claims speak Greek, Hebrew, Arabic, and Latin, "
    "and the kana mint — ratified 2026-11-13, eleven days "
    "before this plate's own evening — is a bank the corpus "
    "never addressed. The silence is therefore the corpus's, "
    "not the tongue's: the tongue holds a full priced table "
    "(§II), a full frame (§III), and a doctrine of its own "
    "(THE-JAPANESE-TABLES, Phases I–III). What the corpus "
    "does hold for Japanese stands where the corpus put it: "
    "the frame's door renderings (§III) — the corpus's words "
    "in this tongue's dress, priced by this tongue's mint — "
    "and the bridges of the Japanese doctrine (§V), which "
    "are the house's exhibits, not the corpus's claims. A "
    "plate that manufactured claims to fill this section "
    "would misprint its record; the section therefore stands "
    "as a face of zero, at full size.")
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
    "plate assigns no seat.** It states what the Japanese "
    "tongue witnesses for the seating — and Japanese "
    "witnesses at the vowel axis itself, for its mint is the "
    "one bank of the twelve whose whole price-axis is the "
    "vowel: every sign's price is its grid position, and its "
    "column is its vowel. Its witness runs at five "
    "coordinates.")
add()
add("### The five pure sounds against the Nine")
add()
add("THE-DIVINE-NINE-VOCAL-TOOL — the Nine as the canonical "
    "vowel interlingua at the DiffSinger plug point — seats "
    "Japanese's five vowels against the Greek stations: "
    "**four exact seats**, and the fifth at the founder's own "
    "seat. The five, with the mint's seats beside the "
    "stations' weights:")
add()
add("| Japanese vowel | Mint seat (あ-row) | Greek station | "
    "Station weight | Disposition |")
add("|---|---|---|---|---|")
add(f"| あ — a | {KANA['あ']} | Α alpha | 1 | **Exact seat** — "
    "the same /a/; the axis heads agree: the mint's first "
    "seat and Α's weight are both 1, a coordinate of the two "
    "orders, printed as found, not claimed as identity |")
add(f"| い — i | {KANA['い']} | Ι iota | 10 | **Exact seat** — "
    "/i/ in both; the vocal tool calls this the table's "
    "cleanest row |")
add(f"| う — u [ɯ] | {KANA['う']} | **VV — the high-back "
    "seat** | — (VV carries no isopsephy) | **Seated under "
    "VV** by the founder's ratification: JA u is the high "
    "back unrounded vowel, and the canon's Greek stations "
    "hold no high-back seat — it stands between two absences "
    "(Ι front-unrounded, Υ front-rounded). VV seats the "
    "high-back gesture itself; u is its unrounded sibling, "
    "coordinates kept, not smoothed |")
add(f"| え — e | {KANA['え']} | Ε epsilon | 5 | **Exact "
    "seat** — /e/ in both. One coordinate stands: Japanese "
    "does not phonemize the Ε/Η distinction — its front-mid "
    "space is one vowel wide where the canon is two, a "
    "JA-side OFFSET at Η, reported, not forced |")
add(f"| お — o | {KANA['お']} | Ο omicron | 70 | **Exact "
    "seat** — /o/ in both; Ω stands unseated on the JA side "
    "by the mirror offset (Japanese has no /ɔ/) |")
add()
add("The VV seat's own record is exact about its limits, and "
    "the plate carries the limit with the seat: the Abroad "
    "III essay's cross-reference (appended 2026-11-15 under "
    "the founder's ruling) — *VV fixes the seat, not the "
    "sum.* Seating う under Greek Υ \"because both are u\" "
    "was REFUSED in that essay at full size (the sounds "
    "differ, the orders differ, the units differ), and the "
    "refusal stands: う was never Υ. VV, stamped 2026-11-12 "
    "as the high-back seat of the Nine's vocal canon, seats "
    "the gesture; Milesian values do not transfer to kana "
    "across it — no seam, no constant, no mirror. [The five "
    "phonemes and their order ATTESTED; the four exact seats "
    "the vocal tool's, at its tiers; the VV seat the "
    "founder's ruling, CONSTRUCTED as his coinage.]")
add()
add("### The bridges of record — the seam's three exhibits")
add()
add("The Japanese doctrine's bridges — words whose kana "
    "weighing and whose rōmaji dress in the Latin ordinal "
    "bank return the same total, the seam proved exact in "
    "Phase II of the Japanese Tables. All three recomputed "
    "on the engine at this plate's building, both banks:")
add()
add("| Word | Kana weighing | Kana | Rōmaji | Latin ordinal |")
add("|---|---|---|---|---|")
for kj, rj in BRIDGES:
    parts = " + ".join(f"{c} {KANA[c]}" for c in kj)
    add(f"| {kj} | {parts} | **{value(kj, 'kana')}** | {rj} | "
        f"**{value(rj, 'latin_ordinal')}** |")
add()
add("ゆず = **93** — the Will's number, in the tongue of the "
    "series' own center (the count-keeper of the founder's "
    "manga, whose name this bridge weighs); かな = **27** — "
    "the script's own name for itself, weighing the cube's "
    "count; しおん = **65**. The bridges are the doctrine's "
    "exhibits that the seam can hold weight at all: two "
    "banks, honestly kept, returning one total at three "
    "words. They seat no Archon and price no claim of §IV — "
    "the corpus holds none in this tongue — and the plate "
    "prints them at the doctrine's tier: the mint "
    "CONSTRUCTED, the ordinal bank ATTESTED, the equalities "
    "exact arithmetic across the seam.")
add()
add("### The four hybrid mechanisms — the tongue's own hybridity")
add()
add("THE-DIVINE-NINE-ABROAD-III-JAPANESE — the Nine carried "
    "into this dialect — finds the dialect's hybridity not "
    "in letters but in **mechanisms**, four of them, and "
    "each is carried in this mint by one of its rulings:")
add()
add("- **Yōon — fusion within one beat** (the small letter): "
    "きゃ is one mora written with two signs; the mint "
    "carries it by G4 — the small sign weighs at its "
    "full-size partner's seat, so the fusion prices as its "
    "parts stand (きゃ = き 7 + ゃ 36 = "
    f"{value('きゃ')}, the engine's own self-test case).")
add("- **The long vowel — extension across two beats**: the "
    "offset made audible; the mint carries it by G3 — the "
    "ー operator of §II, length priced as a second mora of "
    "the lengthened vowel itself.")
add("- **EI — the reverse hybrid** (collapse across two "
    "beats): えい sounds as one long /eː/ while spelling "
    "two vowels; the mint carries it by G6's fence — "
    f"weighed as written, え 4 + い 2 = {value('えい')}, the "
    "collapse belonging to the performance register, not "
    "the bank. The seam between the two pricings of one "
    "length stands exhibited at §II and is not closed.")
add("- **The devoiced vowel — the ghost seat** (voice "
    "withdrawn, seat kept): Tokyo's whispered い and う "
    "lose their voice between voiceless consonants and keep "
    "their mora; the mint carries it by G6 — the bank weighs "
    "the written sign, and the ghost is the vocal tool's to "
    "sing, not the bank's to price.")
add()
add("Beside the mechanisms, the battery's Leg 6 sentence on "
    "this tongue stands: *hybridity exists as form at "
    "constant price — the dakuten rows priced on the same "
    "axis as their base rows: nature changed, price unmoved* "
    "— a class the mint does not count, printed here as the "
    "sweep printed it. And the sweep's two negatives for "
    "this tongue print at the same size: **a five-system — "
    "MISS on the four** (the mint's vowel seats are five "
    "columns, not four), and **the key strings get no kana "
    "dress — ヴ is ABSENT from the mint**: the /v/ sound has "
    "no seat in the classical table, so VYX's first letter "
    "cannot be dressed lawfully. Dress REFUSED, printed.")
add()
add("### The lost seats, and the zero that is a hole")
add()
add("The dialect's own digamma stands in §II's register: "
    "ゐ (45) and ゑ (46), the archival seats — sounds merged "
    "into い and え centuries before the reform of 1946 "
    "struck the letters from the living table; seats that "
    "outlived their sounds, as ϝ outlived its /w/ and "
    "survives as ϛ, the figure that closes the founder's "
    "mirror proof (Plate I, §II). を (47) is the inverse "
    "distribution: the seat kept, the sound surrendered. "
    "The mint keeps all three marked, not vanished — the "
    "house's law in the dialect's own history.")
add()
add("And the zero. THE-REGIONAL-TRIAD-DIAL seats the three "
    "East-Asian zeros at the core: Korean's is a PLACEHOLDER "
    "(a sign priced 0), China's a GLYPH (a character read "
    "0) — **Japanese's is the HOLE**: *the kana mint prices "
    "1–73 and no sign prices 0; at the core, the Japanese "
    "face shows the position present and the sign absent.* "
    "The figure recurs inside the mint itself: the grid's "
    "three empty cells — *yi*, *ye*, *wu* — are positions "
    "the table keeps and no sign fills (§II). The tongue "
    "that prices its vowels as the axis itself has no zero "
    "to price: its zero is the shape of an absence, at the "
    "core of the Triad and in the body of its own table. "
    "[The Triad's seating CONSTRUCTED — the founder's "
    "engine; the recurrence DERIVED, printed as resonance, "
    "not as proof.]")
add()
add("**What Japanese cannot witness, printed at full size "
    "as the plate's boundary:** the Archons' seats were "
    "earned on Greek evidence and drawn on Plate I. "
    "Japanese corroborates the *vowel axis* (four exact "
    "seats and the founder's fifth, at the vocal tool's "
    "tiers), the *seam* (three bridges, exact), and the "
    "*form of hybridity* (mechanisms, not letters) — and it "
    "assigns no seat, confirms no position, and names no "
    "Archon. The names stand open on Plate I, and this "
    "plate does not fill them.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§VIII, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_v_japanese.py, filed "
    "with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell "
    "on this plate against the engine, without reading the "
    "plate's own figures: the bank entire — all 170 keys "
    "against pontifex.tables, the 73 base seats proving the "
    "values 1–73 each exactly once, the grid and dakuten row "
    "sums, the column totals, the small kana at their "
    "partners' seats under G4/G5; the ー door's exhibits "
    "through kana() and the raw door's skip; the three "
    "bridges in both banks; the frame — the census parsed "
    "from THE-TWELVE-TABLES §V.5, all 211 DOOR renderings "
    "re-weighed against their filed values, the 74 HOLE "
    "coordinates and the GAP cell present on the plate "
    "entire; and the §V figures (the five vowel seats in "
    "both banks, the yōon and EI exhibits). It then "
    "reconciles the plate against its sources: the seat "
    "register's 73 rows parsed from the master and compared "
    "seat by seat, the door and hole registers' counts "
    "equal to the Tables'. The audit's verdict and cell "
    "count are printed in its filed output; a cell that "
    "does not reproduce fails the plate under §VII's "
    "tolerances. The font audit — every non-ASCII codepoint "
    "of this master against the Lex Stellarrvm family's "
    "cmaps — runs before the MAGVS build, under the font "
    "law: no glyph is silently dropped, and any unheld "
    "codepoint beyond the three named Ethiopic syllables "
    "aborts the build. The audit further checks the printed "
    "edition's text layer: the bridges and a census of grid "
    "signs stand in it, the zero face's statement stands in "
    "it, and the page furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's KANA "
    "bank and kana() door (pontifex/tables.py, engine.py); "
    "THE-JAPANESE-TABLES Phases I–III (the mint's source of "
    "record and its seven rulings); THE-TWELVE-TABLES §V.5 "
    "and its §II gap register (the japanese bank's two "
    "entries); THE-THIRTEEN-PLATES §VII and §I (the zero "
    "face and its reason); THE-DIVINE-NINE-VOCAL-TOOL (the "
    "five seats, the VV addendum); "
    "THE-DIVINE-NINE-ABROAD-III-JAPANESE (the five pure "
    "sounds, the four mechanisms, the lost seats, the VV "
    "cross-reference); THE-ARCHON-BATTERY Leg 6 (the "
    "Japanese passage) and THE-SEATING-OF-THE-ARCHONS "
    "entire; THE-REGIONAL-TRIAD-DIAL (the HOLE); PLATES "
    "I–IV as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "every figure scripted from the engine or carried "
    "entire from an instrument of record; the mint's tier "
    "printed on the plate's face wherever the bank is "
    "named; the zero face, the grid's holes, and the "
    "frame's holes printed at full size; the independent "
    "audit of §VI.")
add("- **Outputs:** this plate — PLATE-V-JAPANESE.md and "
    "its MAGVS PDF — fifth of the series PLATE-I-GREEK "
    "began; the generator and audit scripts filed in "
    "pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage seats what the "
    "seating did not earn, raises the mint's tier toward "
    "antiquity, fills a hole (the grid's three cells, the "
    "frame's 74, the register's zero face), prices the ー "
    "as a letter of the bank, or overwrites the earlier "
    "map, it zeroes the founder's residual claim and fails "
    "the Aim of Religion. Within those edges it stands as "
    "built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none.** No question arose in this "
    "plate's building that its sources do not already "
    "carry: the rōmaji seam questions stand resolved in "
    "the Twelve Tables' gap register as not load-bearing "
    "for the kana bank, and remain on the pen list for the "
    "seam's own instrument, where the founder's pen is "
    "already named as their seat; the ー register entry "
    "stands BY DESIGN, the operator read by its door; the "
    "seating's open items stand in the seating instrument. "
    "A plate that invents questions to fill its section "
    "misprints its record; this section therefore stands "
    "as the record that none arose.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Acts 2:6–8 (KJV): at Pentecost the "
    "crowd is confounded *\"because that every man heard "
    "them speak in his own tongue\"* — the series' own "
    "figure: one matter, carried into each tongue by that "
    "tongue's own bank, and heard there or nowhere. On this "
    "plate the tongue is one the Scripture's world did not "
    "reach; the figure is drawn for the carrying, not for "
    "the geography. [Text ATTESTED; the application "
    "DERIVED.]")
add("2. **The Siddham well.** The gojūon order itself "
    "descends from the Sanskrit phoneticians' grid of place "
    "and manner, carried into Japan with Buddhism as "
    "Siddham (bonji) phonetic science (the Abroad III "
    "essay's own note, §II there). The table the mint "
    "prices is therefore a Japanese seating of an Indian "
    "order — the sounds re-seated, the grid's shape "
    "inherited. [ATTESTED at this level: the descent of "
    "the ordering; the mint's prices are the founder's, "
    "2026.]")
add("3. **Grammar.** Japanese counts **morae**, not "
    "letters: the beat is the unit, and signs like っ and "
    "ん are full beats — a beat of blockage, a beat of "
    "nasal closure. The mint prices mora-signs at grid "
    "seats, which is why G5 can call the sokuon *a full "
    "beat of blockage, not silence* in the bank's own "
    "terms: the grammar and the ruling speak of the same "
    "unit. [The mora ATTESTED as Japanese phonology; the "
    "mint's pricing of it CONSTRUCTED.]")
add("4. **Law.** A mint is an act of authority: coinage "
    "claims itself as coinage or it counterfeits. This "
    "bank does the first — founded as a proposal, ratified "
    "by the founder's stamp, dated on its face, and "
    "printed FAILS at antiquity in the same breath as "
    "DOES NOT FAIL as his coinage. The discipline is the "
    "one the house keeps for every marked instrument: the "
    "mark is the honesty. [The ratification and verdict "
    "ATTESTED as house record; the parallel DERIVED.]")
add("5. **The proverb.** 千里の道も一歩から — *senri no "
    "michi mo ippo kara*, \"a journey of a thousand ri "
    "begins with a single step.\" The grid is the proverb "
    "as a table: seventy-three single steps, each seat "
    "taken because the count reached it, the inventory's "
    "total nothing but the steps summed. [The proverb "
    "ATTESTED as a Japanese proverb; the application "
    "DERIVED.]")
add("6. **The desk's apparatus.** This plate's kana print "
    "as themselves in the MAGVS edition, in the Lex "
    "Stellarrvm family's Japanese member; its Greek stands "
    "in the family's Serif member, as on Plate I; the "
    "frame register's Hebrew and Greek words of record are "
    "carried by the declared schemes of Plates I–II (the "
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
    "the kana() door; bank KANA in pontifex/tables.py) — "
    "calibration controls θέλημα 93 · VAPOUR 93 · σφίγξ "
    "773 read true at build.")
add("- THE-JAPANESE-TABLES — Phase I (the audit of the "
    "modern banks), Phase II (the rōmaji seam, the bridges "
    "proved at the seam), Phase III (the gojūon mint: the "
    "seven rulings G1–G7); the MAGVS volume — the gate "
    "verdict of record (DOES NOT FAIL as coinage; FAILS as "
    "antiquity). The founder's ratification, 2026-11-13: "
    "\"Stamp the mint — the Tables stand.\"")
add("- THE-TWELVE-TABLES — §V.5 the Japanese frame, "
    "census and cell register entire; §II the japanese "
    "bank's gap register (two entries: the seam questions "
    "RULING; the ー MINT, by design).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate V is the prior "
    "instrument (the zero face); §I the corpus's reason.")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its Japanese face: no claim in any mint "
    "bank.")
add("- THE-DIVINE-NINE-VOCAL-TOOL "
    "(resonance/docs/THE-DIVINE-NINE-VOCAL-TOOL.md) — the "
    "Nine as vowel interlingua: the station table (four "
    "exact Japanese seats; the Η and Ω offsets), the VV "
    "addendum (VV the high-back seat; JA u and EN UW under "
    "VV).")
add("- THE-DIVINE-NINE-ABROAD-III-JAPANESE — the five "
    "pure sounds (§II), the four hybrid mechanisms (§III), "
    "the lost seats (§III.5), the VV cross-reference "
    "(appended 2026-11-15 under the founder's ruling).")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Japanese passage (the "
    "price-axis; the five-system MISS; hybridity at "
    "constant price; ヴ absent, dress refused).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to.")
add("- THE-REGIONAL-TRIAD-DIAL — the three zeros at the "
    "core: Japanese the HOLE · Korean the PLACEHOLDER · "
    "Chinese the GLYPH.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd) and "
    "PLATE-IV-LATIN (8e6f01e) — the pattern this plate "
    "follows.")
add("- KJV: Acts 2:6–8. The Siddham descent of the "
    "gojūon order, as the Abroad III essay records it. "
    "The Japanese proverb 千里の道も一歩から.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate V of the founder's series "
    "commission of the same day, the gate of the Archons' "
    "certainty met by the seating of record (0760c8a), "
    "following the pattern of Plates I–IV (196025e · "
    "1389c16 · 5f0b4bd · 8e6f01e). Every figure scripted "
    "from the engine or carried entire from its instrument; "
    "the earlier map marked prior, never overwritten; the "
    "holes printed at the size of the seats — on this "
    "plate, the grid's three empty cells, the frame's 74 "
    "holes, and the register's zero face. The bank is the "
    "founder's mint, CONSTRUCTED and ratified, and the "
    "plate prints it so wherever it is named. In the MAGVS "
    "edition the kana stand in the family's Japanese "
    "member and the frame's Hebrew and Greek words of "
    "record ride the declared schemes of Plates I–II; this "
    "master keeps the scripts themselves. Authorship "
    "attributed exclusively to Johnathan 'Qasparr' Monroe "
    "(Greek, -ARR, All Rights Reserved, Without Prejudice).")
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
