#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_xii_korean.py
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
# MECHANISM: generates PLATE-XII-KOREAN.md — Plate XII of THE
# THIRTEEN COMPLETE PLATES, the last of the twelve tongues —
# in the gap-filling goal's files/, following the pattern
# PLATES I–XI set (196025e · 1389c16 · 5f0b4bd · 8e6f01e ·
# 8d6cd59 · 67d5acc · 5c03d88 · 645bcbb · 933f8fd · 052fd28 ·
# b40abac). Every figure on the plate is scripted from the
# house engine (pontifex weigh(), the hangul() door, and
# hangul_checks()) or carried entire from an instrument of
# record:
#   * the priced table — the HANGUL MINT entire, read from
#     pontifex.tables (HANGUL_INITIAL 19 · HANGUL_VOWEL 21 ·
#     HANGUL_FINAL 27; the merged bank 67 keys), each seat
#     printed with its reasoning — in a positional mint the
#     reasoning is the coordinate: stratum, seat, and the
#     law that seats it;
#   * THE HINGE at full size — ㅇ: its raw-bank initial seat
#     (12), its door price under the null law (0, counted),
#     and its final seat (21, a full letter), all three
#     weighed or read at build;
#   * the hangul() door's exhibits — 한글 52 · 한국 40 ·
#     아이 22 with two nulls against the raw bank's 46 ·
#     강 23 · 아 1 · ㄳ 3 · ㆍ unseated — read through
#     engine.hangul() at build;
#   * the 1446 ANNEX entire (HANGUL_1446_*: 17/11/17),
#     reached only through hangul(hist=True), its exhibits
#     read at build (ㆁㆍ 4 · ㅇ 15 · ㆍ 1 · ㄲ refused);
#   * the Twelve Tables' Korean frame — its census and its
#     full cell register parsed from THE-TWELVE-TABLES.md
#     §V.12: the 223 DOOR renderings re-weighed through the
#     hangul() door at build against their filed values, the
#     62 HOLE coordinates and the one GAP cell carried
#     entire (the register's thirteen empty-rendering door
#     rows carried entire, as on Plate V);
#   * the corpus's Korean claims — none: the register's
#     ZERO FACE, carried from THE-THIRTEEN-PLATES §XIV with
#     the TABVLA's reason stated at §I there;
#   * the tongue's bearing on the seated Archons — the
#     Regional Triad's three zeros printed entire (Japanese
#     the HOLE · Korean the PLACEHOLDER · Chinese the
#     GLYPH), ㅇ's dual office as the placeholder's
#     mechanism, the Archon Battery's Leg 6 Korean passage
#     (the 21 vowel jamo by seat; the compound class eleven,
#     a MISS on the four; ㅖ at seat 8, itself a fused sign),
#     and the five tongues' 8s recomputed in their own
#     banks. The plate assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's
# face. This plate's bank is a MINT: CONSTRUCTED, the
# founder's coinage struck on the Regional Triad road, and
# the plate prints that tier on its face wherever the bank
# is named — it DOES NOT FAIL as his coinage and FAILS as
# any claim of antiquity, in the same breath: the Phase I
# audit verified the negative from the witnesses — no
# witness prices a jamo; Korean numerals are words and
# borrowed glyphs. The relation to the earlier Thirteen
# Plates map is printed, the earlier work marked prior,
# never overwritten. Holes print at the size of the seats —
# on this plate, the frame's 62 holes, the register's zero
# face, and the refused seats of the modern grid.
#
# CONTENT TEST: Inputs — the engine's HANGUL banks and
# hangul() door, the Twelve Tables master, the Thirteen
# Plates map, the East Asian Phase I audit, the Regional
# Triad dial, the Archon Battery. Processes — control
# calibration, scripted extraction, register-faithful
# emission in the Teacher's Edition manner. Outputs —
# PLATE-XII-KOREAN.md beside the series' other masters.
# Tolerances — the audit (audit_plate_xii_korean.py)
# re-weighs every priced cell independently; a figure that
# does not reproduce fails the plate.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
import sys
import unicodedata as ud
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

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-XII-KOREAN.md"


def value(word, bank="hangul"):
    """One weighing at the raw bank door, unwrapped."""
    return weigh(word, bank)["value"]


# ---------------------------------------------------------------------
# Calibration — the banks are not trusted until the controls read
# true, and the mint's own seal stands green.
# ---------------------------------------------------------------------
assert value("θελημα", "greek") == 93, "control θέλημα"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR"
assert value("σφιγξ", "greek") == 773, "control σφίγξ"
assert all(ok for _n, ok, _d in hangul_checks()), "hangul_checks"

# ---------------------------------------------------------------------
# The mint's census — every count below is taken from the bank
# itself, never typed.
# ---------------------------------------------------------------------
N_INIT, N_VOW, N_FIN = (len(HANGUL_INITIAL), len(HANGUL_VOWEL),
                        len(HANGUL_FINAL))
assert (N_INIT, N_VOW, N_FIN) == (19, 21, 27)
assert len(HANGUL) == 67
SUM_INIT = sum(HANGUL_INITIAL.values())          # 190
SUM_VOW = sum(HANGUL_VOWEL.values())             # 231
SUM_FIN = sum(HANGUL_FINAL.values())             # 378
BANK_TOTAL = sum(HANGUL.values())                # 799
assert (SUM_INIT, SUM_VOW, SUM_FIN, BANK_TOTAL) == (190, 231, 378, 799)
assert sorted(HANGUL_INITIAL.values()) == list(range(1, 20))
assert sorted(HANGUL_VOWEL.values()) == list(range(1, 22))
assert sorted(HANGUL_FINAL.values()) == list(range(1, 28))
DISTINCT = len(set(HANGUL.values()))
assert DISTINCT == 27 and max(HANGUL.values()) == 27

A_INIT, A_VOW, A_FIN = (len(HANGUL_1446_INITIAL),
                        len(HANGUL_1446_VOWEL),
                        len(HANGUL_1446_FINAL))
assert (A_INIT, A_VOW, A_FIN) == (17, 11, 17)
assert len(HANGUL_1446) == 45
A_SUMS = (sum(HANGUL_1446_INITIAL.values()),
          sum(HANGUL_1446_VOWEL.values()),
          sum(HANGUL_1446_FINAL.values()))
assert A_SUMS == (153, 66, 153)


def name_of(compat):
    """The letter's name from the standard: HANGUL LETTER
    KIYEOK -> KIYEOK."""
    return ud.name(compat).replace("HANGUL LETTER ", "", 1)


def seat_rows(compat_seq, bank, kind):
    """(seat, compat sign, name, price) for one stratum, the
    compatibility sequence resolved to its conjoining seat."""
    rows = []
    for i, g in enumerate(compat_seq):
        conj = _jamo_conjoining(g, kind)
        rows.append((i + 1, g, name_of(g), bank[conj]))
    return rows


INIT_ROWS = seat_rows(_HANGUL_SK_INITIAL, HANGUL_INITIAL, "CHOSEONG")
VOW_ROWS = seat_rows(_HANGUL_SK_VOWEL, HANGUL_VOWEL, "JUNGSEONG")
FIN_ROWS = seat_rows(_HANGUL_SK_FINAL, HANGUL_FINAL, "JONGSEONG")
A_INIT_ROWS = seat_rows(_HANGUL_1446_CONSONANTS, HANGUL_1446_INITIAL,
                        "CHOSEONG")
A_VOW_ROWS = seat_rows(_HANGUL_1446_VOWELS, HANGUL_1446_VOWEL,
                       "JUNGSEONG")
A_FIN_ROWS = seat_rows(_HANGUL_1446_CONSONANTS, HANGUL_1446_FINAL,
                       "JONGSEONG")
for rows, bank, kind in ((INIT_ROWS, HANGUL_INITIAL, "CHOSEONG"),
                         (VOW_ROWS, HANGUL_VOWEL, "JUNGSEONG"),
                         (FIN_ROWS, HANGUL_FINAL, "JONGSEONG")):
    assert [r[3] for r in rows] == list(range(1, len(rows) + 1))

# The compound (fused) vowels — two vowel signs in one glyph.
COMPOUND = list("ㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ")
BASIC_VOWELS = [g for g in _HANGUL_SK_VOWEL if g not in COMPOUND]
assert len(COMPOUND) == 11 and len(BASIC_VOWELS) == 10

# The teeth, recomputed: the doubles' prices against doublings.
INIT_PRICE = {g: p for _s, g, _n, p in INIT_ROWS}
DOUBLES = [("ㄲ", "ㄱ"), ("ㄸ", "ㄷ"), ("ㅃ", "ㅂ"), ("ㅆ", "ㅅ"),
           ("ㅉ", "ㅈ")]
DOUBLE_FACTS = [(d, b, INIT_PRICE[d], INIT_PRICE[b],
                 INIT_PRICE[d] == 2 * INIT_PRICE[b])
                for d, b in DOUBLES]
assert [f[4] for f in DOUBLE_FACTS] == [True, False, False, False,
                                        False]
# The digraphs' refusal coordinate: four keep only archaic
# choseong namesakes; seven have no choseong form at all.
ARCHAIC_NAMESAKES = []
NO_CHOSEONG = []
for g in _HANGUL_DIGRAPH_FINALS:
    try:
        conj = _jamo_conjoining(g, "CHOSEONG")
        assert conj not in HANGUL_INITIAL
        ARCHAIC_NAMESAKES.append(g)
    except ValueError:
        NO_CHOSEONG.append(g)
assert ARCHAIC_NAMESAKES == list("ㄵㄶㅀㅄ"), ARCHAIC_NAMESAKES
assert len(NO_CHOSEONG) == 7

# The hinge's three facts.
HINGE_RAW_SEAT = HANGUL_INITIAL[HANGUL_NULL_INITIAL]     # 12
HINGE_FINAL_SEAT = FIN_ROWS[20][3]                       # ㅇ final: 21
assert HINGE_RAW_SEAT == 12 and HINGE_FINAL_SEAT == 21
assert _HANGUL_SK_FINAL[20] == "ㅇ"

# The door's exhibits, read through hangul() at build.
EX_HANGEUL = hangul_door("한글")          # 52; strata 20/20/12
EX_HANGUK = hangul_door("한국")           # 40
EX_AI = hangul_door("아이")               # 22, two nulls
EX_A = hangul_door("아")                  # 1, one null
EX_GANG = hangul_door("강")               # 23, no null
EX_DIGRAPH = hangul_door("ㄳ")            # 3, at its final seat
EX_AUAE = hangul_door("ㆍ")               # modern: 0, unseated 1
RAW_AI = value("아이")  # the raw bank's spelling of 아이
assert (EX_HANGEUL["value"], EX_HANGEUL["initial_subtotal"],
        EX_HANGEUL["vowel_subtotal"],
        EX_HANGEUL["final_subtotal"]) == (52, 20, 20, 12)
assert EX_HANGUK["value"] == 40
assert (EX_AI["value"], EX_AI["null_initials"], RAW_AI) == (22, 2, 46)
assert (EX_A["value"], EX_A["null_initials"]) == (1, 1)
assert (EX_GANG["value"], EX_GANG["final_subtotal"],
        EX_GANG["null_initials"]) == (23, 21, 0)
assert (EX_DIGRAPH["value"], EX_DIGRAPH["final_subtotal"]) == (3, 3)
assert (EX_AUAE["value"], EX_AUAE["unseated"]) == (0, 1)
# The annex's exhibits, through the hist door only.
HX_PAIR = hangul_door("ㆁㆍ", hist=True)   # 3 + 1 = 4
HX_IEUNG = hangul_door("ㅇ", hist=True)    # 15 — no null in 1446
HX_AUAE = hangul_door("ㆍ", hist=True)     # 1 — vowel seat 1
HX_DOUBLE = hangul_door("ㄲ", hist=True)   # refused: unseated 1
assert (HX_PAIR["value"], HX_IEUNG["value"], HX_AUAE["value"],
        HX_DOUBLE["unseated"]) == (4, 15, 1, 1)

# The five tongues' 8s, recomputed in their own banks for §V.
EIGHTS = [("Η", "greek"), ("ⲏ", "coptic"), ("И", "cyrillic"),
          ("Ը", "armenian"), ("ჱ", "georgian")]
assert all(value(g, b) == 8 for g, b in EIGHTS)
YE_SEAT = VOW_ROWS[7]
assert YE_SEAT[1] == "ㅖ" and YE_SEAT[3] == 8 and "ㅖ" in COMPOUND

# ---------------------------------------------------------------------
# The Twelve Tables' Korean frame — census and cell register.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
korean_block = twelve_text.split("### §V.12 — The Korean Table")[1] \
    .split("## §VI")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", korean_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
doors, holes, gaps = [], [], []
for line in korean_block.splitlines():
    if re.match(r"\| [A-Z]+/", line) and " | " in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            continue
        state = cells[2]
        if state == "DOOR":
            assert hangul_door(cells[3])["value"] == int(cells[4]), \
                cells
            doors.append(cells)
        elif state == "HOLE":
            holes.append(cells)
        elif state == "GAP":
            gaps.append(cells)
assert (len(doors), len(holes), len(gaps)) == (n_door, n_hole, n_gap)
assert (n_native, n_door, n_hole, n_fenced, n_empty, n_gap) == \
    (0, 223, 62, 0, 85, 1)
assert gaps[0][0] == "CLXXXIV/10"
# Thirteen door rows stand in the register with an EMPTY
# rendering and a filed value of 0 — the same thirteen cells
# the Japanese frame carries (Plate V, §III): nine Arabic
# spirit-names of §XLVII, two §CLXXXV cells whose word of
# record is the numeral 5, and §CLXXXVII/11's AIR in two
# dresses. The plate carries them entire.
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
add("**PLATE XII — KOREAN**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Korean tongue's complete 777 table — the hangul mint "
    "entire, the founder's coinage on the designed grid, "
    "priced stratum by stratum; the hinge ㅇ printed at full "
    "size; the 1446 annex behind its door; the corpus's "
    "Korean register, which is a zero face; and the "
    "tongue's witness to the seated Archons: the zero that "
    "is a placeholder, and the fused sign at the vowel "
    "row's eighth seat. The last of the twelve tongues.")
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
add("## §I — PLATE XII AND ITS COMMISSION")
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
    "(8e6f01e), V — JAPANESE (8d6cd59), VI — GE'EZ (67d5acc), "
    "VII — ARMENIAN (5c03d88), VIII — COPTIC (645bcbb), IX — "
    "GEORGIAN (933f8fd), X — CYRILLIC (052fd28) and XI — "
    "GLAGOLITIC (b40abac) followed it; this plate follows "
    "them, twelfth and last of the twelve tongues in the "
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
add("**This plate's distinction.** Korean is the second "
    "plate of the series whose bank is a **mint** — and the "
    "only one whose material is a *designed grid*: Hangul, "
    "the featural alphabet Sejong's court devised in 1443 "
    "and promulgated in 1446, the one field of the whole "
    "sweep whose letterforms are a theory. The Phase I audit "
    "of the East Asian field verified the negative from the "
    "witnesses before anything was seated: **no witness "
    "prices a jamo** — Korean numerals are *words* (the "
    "native system) and *borrowed glyphs* (the Sino-Korean "
    "hanja, identical to the Chinese logographs). What the "
    "field offers is the grid itself, and the hangul mint "
    "prices that grid by its seats. Its tier is therefore "
    "printed on this plate's face wherever the bank is "
    "named: **CONSTRUCTED** — the founder's coinage under "
    "his Flagpole, struck on the Regional Triad road "
    "(2026-11-24), and not attested, traditional, or "
    "ancient at any coordinate. It is also a plate whose "
    "corpus register is a **zero face** (§IV): the 777 "
    "corpus judges no claim in this tongue, and the plate "
    "prints that silence as its finding rather than filling "
    "it. And its bearing on the seated Archons (§V) runs at "
    "the zero itself: this is the tongue whose zero is a "
    "sign — the placeholder ㅇ — and whose vowel row seats a "
    "fused sign at the fold's coordinate, 8.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its Korean "
    "face stood **silent with a zero face**: bank *hangul*, "
    "67 seats, 27 distinct values, maximum 27; tier of "
    "record *CONSTRUCTED — the hangul mint*; and its "
    "sentence stands: *\"The hangul mint stands seated in "
    "the engine and holds a full table in THE TWELVE "
    "TABLES; its silence here is the TABVLA corpus's, not "
    "the tongue's.\"* This series *fulfills* that map: where "
    "the map counted nothing, this plate prints the nothing "
    "entire — with the tongue's priced table beneath it, "
    "the frame around it, and its witness to the Archons "
    "above it. The earlier work stands as the prior "
    "instrument of the same name's family — marked prior, "
    "never overwritten.")
add()
add("**How the plate is read.** §II is the mint: the three "
    "strata priced seat by seat, each seat with its "
    "reasoning — in a positional mint the reasoning is the "
    "coordinate, and the plate prints it so — then the "
    "teeth, the hinge at full size, the door and its "
    "exhibits, and the 1446 annex behind its own door. §III "
    "is the tongue's frame in the Twelve Tables — a face of "
    "door and hole, its register restated entire. §IV is "
    "the zero face. §V is the tongue's bearing on the "
    "seated Archons — this plate draws no seating (the "
    "seating is struck, and Plate I drew it); it states "
    "what Korean witnesses. §VI is the audit. §IX states "
    "the series state this plate closes. A value without "
    "its reasoning is not shippable; a hole prints at the "
    "size of the seat it stands in for.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the mint entire.
# ---------------------------------------------------------------------
add("## §II — THE HANGUL MINT — THE COMPLETE PRICED TABLE")
add()
add("The bank is the **hangul mint**: the jamo of the modern "
    "South Korean grid priced by their seats within their "
    "strata. **Tier of record: CONSTRUCTED** — a house "
    "coinage on a designed grid, struck under the founder's "
    "Flagpole on the Regional Triad road (Phase II seats, "
    "pontifex a0efdf1; the mint's seal, `hangul_checks()`, "
    "stands 11/11 and its parity battery 18/18). Hangul has "
    "NO letter-numeral tradition: the Phase I audit "
    "(THE-EAST-ASIAN-FIELD-PHASE-I-AUDIT, 2026-11-24) "
    "verified the negative from the witnesses — Korean "
    "numerals are words (하나 둘 셋 …, the native system) "
    "and borrowed glyphs (the Sino-Korean hanja, identical "
    "to the Chinese logographs); no witness prices a jamo. "
    "What the field offers is the grid itself: a designed "
    "featural alphabet (Sejong, 1443; promulgated 1446) "
    "with canonical orders, audited from two witnesses and "
    "the Unicode standard's own block order (the audit's "
    "battery 12/12). This mint prices that grid by its "
    "seats. The gate of record stands over the whole plate: "
    "**the mint DOES NOT FAIL as the founder's coinage; it "
    "FAILS as any claim of antiquity, at the same size, in "
    "the same breath.** It must never be cited as attested, "
    "traditional, or ancient.")
add()
add("**The face-law seating** (the mint's founding law, "
    "from the tables' header): the tongue's signs occupy "
    "their seats as **strata** — the script's own three "
    "positional strata, initial (choseong), vowel "
    "(jungseong), final (jongseong) — and a sign's price is "
    "its seat *within its stratum*, the strata never "
    "blended: an initial ㄱ and a final ㄱ are two seats "
    "that happen to share a price (1), and ㅅ initial (10) "
    "and ㅅ final (19) share nothing but the letter. The "
    "bank is keyed in the standard's *conjoining* jamo "
    "blocks (choseong U+1100 + seat − 1, and so for the "
    "other strata), because the conjoining blocks are the "
    "only keying under which initial and final seats cannot "
    "collide; the plate prints each sign in its "
    "compatibility dress (ㄱ ㄲ ㄴ …), the dress the audit's "
    "frozen transcriptions carry, resolved to its "
    "conjoining seat by Unicode name — the audit's order, "
    "the standard's names, and the block seats are three "
    "testimonies held to one sequence.")
add()
add("**The parting, printed.** The North Korean orders "
    "differ — the doubles seated last, ㅇ last among "
    "initials, the basic vowels first among vowels. They "
    "are NOT seated: the South order is the standard's "
    "block order and the audit's. The parting stands here "
    "so no reader mistakes the mint for the peninsula's "
    "one voice; whether a North annex is ever wanted is "
    "the founder's pen.")

INIT_REASON = {
    1: "The head of the stratum and of the grid: the "
       "tongue-root shape, first of the treatise's five "
       "basic consonant forms.",
    2: "**A lawful double** (the teeth, below): the tense "
       "double of ㄱ, seated directly after its base in "
       "the South order. Its price is its seat, 2 — the "
       "one double that coincides with twice its base "
       "(2 = 2×1), a coincidence of the head seats, "
       "printed as such.",
    5: "**A lawful double**: the tense double of ㄷ. Its "
       "price is its seat, 5 — NOT twice its base (8): "
       "the teeth part from the Roman arithmetic here, "
       "and the parting is printed, not smoothed.",
    9: "**A lawful double**: the tense double of ㅂ — "
       "seat 9, not twice its base (16).",
    11: "**A lawful double**: the tense double of ㅅ — "
        "seat 11, not twice its base (20).",
    12: "**THE HINGE** — printed at full size below: the "
        "raw bank holds this seat (12); at the door the "
        "null law prices an initial ㅇ at 0 and counts "
        "it. The letter's consonantal life is final "
        "(final stratum, seat 21).",
    14: "**A lawful double**: the tense double of ㅈ — "
        "seat 14, not twice its base (26).",
    19: "The stratum's close: the last initial seat of "
        "the modern grid.",
}
add()
add("### The initial stratum — choseong (seats 1–19)")
add()
add("The syllable-initial consonants in the South order. "
    "Nineteen seats, prices 1–19 each exactly once; the "
    "stratum sums **190**.")
add()
add("| Seat | Sign | Name | Price | Coordinate |")
add("|---|---|---|---|---|")
for seat, g, nm, p in INIT_ROWS:
    reason = INIT_REASON.get(
        seat, "Seated by the South order: the count of "
              "initials standing before it in the canonical "
              "sequence, plus one — in this mint the count "
              "IS the reasoning.")
    add(f"| {seat} | {g} | {nm} | {p} | {reason} |")
add()
add("### The vowel stratum — jungseong (seats 1–21)")
add()
add("The vowels in the South order: ten basic signs and "
    "eleven fused (compound) signs — two vowel signs in "
    "one glyph — the compound class counted at its "
    "coordinate below. Twenty-one seats, prices 1–21 each "
    "exactly once; the stratum sums **231**.")
add()
add("| Seat | Sign | Name | Price | Coordinate |")
add("|---|---|---|---|---|")
VOW_REASON = {
    1: "The head of the vowel stratum: a basic vowel.",
    8: "**The fold coordinate of this plate** (the "
       "bearing, §V): the seat priced 8 — and ㅖ is "
       "itself a fused sign (ㅕ with ㅣ), a hybrid by "
       "construction at the eighth seat.",
    19: "A basic vowel: the earth line of the Haerye's "
        "three fundamentals (ㆍ heaven, ㅡ earth, ㅣ man); "
        "also the door's epenthetic vowel — a bare onset "
        "in the Korean foreign dress takes ㅡ.",
    20: "A fused sign — the compound class.",
    21: "The stratum's close: a basic vowel, the man "
        "stroke of the three fundamentals.",
}
for seat, g, nm, p in VOW_ROWS:
    if g in COMPOUND:
        base = ("A fused sign — two vowel signs in one "
                "glyph: one of the compound class of "
                "eleven.")
    else:
        base = ("A basic vowel: one of the ten the modern "
                "grid keeps from the 1446 eleven's line.")
    reason = VOW_REASON.get(seat, base)
    add(f"| {seat} | {g} | {nm} | {p} | {reason} |")
add()
add(f"The compound class counted: **{len(COMPOUND)}** of "
    f"the 21 vowel jamo are fused signs ({' '.join(COMPOUND)}), "
    f"against {len(BASIC_VOWELS)} basic "
    f"({' '.join(BASIC_VOWELS)}). The count stands here "
    "because the Archon Battery's sweep counts it (§V): a "
    "hybrid class of eleven — a MISS on the four, printed "
    "as filed.")
add()
add("### The final stratum — jongseong (seats 1–27)")
add()
add("The syllable-final consonants in the South order, "
    "the 28 final slots of the syllable-block law less the "
    "empty slot. Twenty-seven seats, prices 1–27 each "
    "exactly once; the stratum sums **378**. The stratum "
    "carries the eleven heterogenous digraphs at their "
    "block seats — the block law seats them there, and a "
    "syllable's decomposition names them as units — while "
    "the modern grid refuses them initial seats entire "
    "(the teeth, below).")
add()
add("| Seat | Sign | Name | Price | Coordinate |")
add("|---|---|---|---|---|")
FIN_REASON = {
    1: "The stratum's head: a final ㄱ is a seat of its "
       "own — it shares its price (1) with the initial ㄱ "
       "and nothing else; the strata are never blended.",
    2: "The tense double at its final seat: initial ㄲ "
       "is also 2 — a shared price between two seats, "
       "not one seat in two places.",
    21: "**The hinge's other office**: ㅇ as a final is a "
        "full letter, /ŋ/ — the letter's consonantal "
        "life. The door's exhibit 강 weighs it at this "
        "seat with no null counted (below).",
    27: "The stratum's close, and the bank's maximum: "
        "every price in the mint is a seat of some "
        "stratum, and no seat runs past 27.",
}
DIGRAPH_NOTE = {
    "ㄵ": "one of the four whose choseong namesake "
          "survives only as an archaic Middle Korean "
          "cluster form, unseated in the modern stratum.",
    "ㄶ": "one of the four whose choseong namesake "
          "survives only as an archaic Middle Korean "
          "cluster form, unseated in the modern stratum.",
    "ㅀ": "one of the four whose choseong namesake "
          "survives only as an archaic Middle Korean "
          "cluster form, unseated in the modern stratum.",
    "ㅄ": "one of the four whose choseong namesake "
          "survives only as an archaic Middle Korean "
          "cluster form, unseated in the modern stratum.",
}
for seat, g, nm, p in FIN_ROWS:
    if g in _HANGUL_DIGRAPH_FINALS:
        reason = ("A heterogenous digraph, seated here by "
                  "the syllable-block law — and REFUSED an "
                  "initial seat in the modern grid, so a "
                  "digraph can never open a modern "
                  "syllable: refused a promotion, in the "
                  "Roman shape. " + DIGRAPH_NOTE.get(
                      g, "It has no choseong form at all."))
    else:
        reason = FIN_REASON.get(
            seat, "Seated by the South order within the "
                  "final stratum: its seat in the block "
                  "sequence is its price.")
    add(f"| {seat} | {g} | {nm} | {p} | {reason} |")
add()
add(f"**The bank's totals.** The merged bank holds **67 "
    f"keys** — 19 initials, 21 vowels, 27 finals — over "
    f"the three strata; the strata sum 190 + 231 + 378 = "
    f"**{BANK_TOTAL}**. Because the strata are priced "
    f"independently, the bank carries **27 distinct "
    f"values** (1–27), its maximum 27 — the census "
    f"THE-THIRTEEN-PLATES printed for this bank (67 seats "
    f"· 27 distinct · max 27). A price in this mint is "
    f"never a value in the Milesian sense: it is a seat, "
    f"and the stratum is part of the price's name.")
add()
add("### The teeth — the Roman shape in this material")
add()
add("The mint's blueprint is the Roman double-letter "
    "shape, as the tables' header states it — lawful "
    "doubles, refused signs, a hybrid hinge — and the "
    "teeth are stated from the material, the partings "
    "printed:")
add()
add("- **LAWFUL DOUBLES — the five tense doubles** ㄲ ㄸ "
    "ㅃ ㅆ ㅉ: the script's own derived signs, seated "
    "directly after their bases in the South order. "
    "Their prices are their SEATS', not doublings:")
add()
add("| Double | Base | Double's seat | Twice the base | "
    "Verdict |")
add("|---|---|---|---|---|")
for d, b, pd_, pb, coincides in DOUBLE_FACTS:
    add(f"| {d} | {b} | {pd_} | {2 * pb} | "
        f"{'coincides — the head-seat accident, printed as such' if coincides else 'PARTS — priced by seat, not by doubling'} |")
add()
add("  The teeth-law's shape transfers (named lawful "
    "doubles); its Roman arithmetic (a double promotes) "
    "does not, and the parting is printed, not smoothed.")
add("- **REFUSED — the eleven heterogenous final "
    "digraphs** (ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ) are refused "
    "INITIAL seats in the modern grid, so a digraph can "
    "never open a modern syllable: refused a promotion, "
    "in the Roman shape. The refusal's exact coordinate: "
    f"seven ({' '.join(NO_CHOSEONG)}) have no choseong "
    f"form at all; four ({' '.join(ARCHAIC_NAMESAKES)}) "
    "keep only ARCHAIC Middle Korean cluster forms in "
    "the standard's block (U+115C, U+115D, U+111A, "
    "U+1121), which the modern stratum does not seat — "
    "the refusal is the modern grid's, and the archaic "
    "forms stand in the block as its witnesses. As "
    "finals the digraphs stand at their block seats "
    "(§II, the final stratum), because the seat law and "
    "the block law agree there.")
add("- **REFUSED — the four obsolete basic letters** ㆁ "
    "ㅿ ㆆ ㆍ are refused a modern seat entire: their seat "
    "is the 1446 annex below. A fifth sign, ㆅ, stands "
    "in one witness's 1446 list (the Phase I audit's "
    "note: its testimony rests on that witness alone) "
    "and in no seat of the engine — recorded, not "
    "seated, marked not vanished.")
add()
add("### THE HINGE — ㅇ at full size")
add()
add("One sign, two natures, decided by position — the "
    "mint's hybrid hinge, as the Triad files it. The "
    "plate prints its three facts at the size of the "
    "seat:")
add()
add(f"1. **At the raw bank**, the initial ㅇ holds its "
    f"seat: **{HINGE_RAW_SEAT}** of the initial stratum. "
    f"`weigh()` reads the bank as keyed and shows the "
    f"seat.")
add(f"2. **At the door**, the null law prices a "
    f"syllable-initial ㅇ at **0** — the script's own "
    f"zero, the silent placeholder every vowel-initial "
    f"syllable carries — and counts it in the weighing's "
    f"`null_initials`, so the zero is visible in the "
    f"audit trail, never silent. In modern Korean the "
    f"law is phonologically exact: an initial ㅇ is "
    f"always the placeholder.")
add(f"3. **As a final**, ㅇ is a full letter, /ŋ/, at "
    f"seat **{HINGE_FINAL_SEAT}** of the final stratum — "
    f"the letter's consonantal life is final, and the "
    f"door prices it there in full.")
add()
add("The two doors' parting is by design, and the engine "
    "prints it in the door's own doctrine: the null law "
    "binds the door, the way the kana ー operator binds "
    "kana() and not weigh() (Plate V). §V takes up what "
    "the hinge is at the dial's core: the PLACEHOLDER.")
add()
add("### The hangul() door — syllable dress, and its exhibits")
add()
add("The mint's reading door is `hangul()`: text as it is "
    "written — syllable blocks — NFD-decomposed by the "
    "standard's own law (block = (initial × 21 + vowel) "
    "× 28 + final, in the South order), each jamo priced "
    "at its seat in its stratum, the null law applied, "
    "the strata subtotals and the null count carried in "
    "the result. A bare compatibility jamo resolves by "
    "Unicode name — a vowel to its vowel seat, a "
    "consonant to its initial seat, a digraph (which has "
    "no initial form) to its final seat, the only seat it "
    "holds. The door's exhibits, read at this plate's "
    "building:")
add()
add(f"- **한글** — the witnesses' own syllable example: "
    f"한 = ㅎ 19 + ㅏ 1 + ㄴ 4 = 24; 글 = ㄱ 1 + ㅡ 19 + "
    f"ㄹ 8 = 28; the word weighs **{EX_HANGEUL['value']}**, "
    f"strata subtotals {EX_HANGEUL['initial_subtotal']}/"
    f"{EX_HANGEUL['vowel_subtotal']}/"
    f"{EX_HANGEUL['final_subtotal']}.")
add(f"- **한국** weighs **{EX_HANGUK['value']}** (한 24 + "
    f"국 16 = ㄱ 1 + ㅜ 14 + ㄱ 1).")
add(f"- **아이** at the door weighs **{EX_AI['value']}** "
    f"with **{EX_AI['null_initials']} null initials "
    f"counted** — two placeholders priced 0, their count "
    f"on the face of the weighing. At the raw bank its "
    f"conjoining spelling shows the seats (12+1 + 12+21) "
    f"= **{RAW_AI}**: the two doors part at the zero, by "
    f"design, and the parting is the hinge's proof.")
add(f"- **아** weighs **{EX_A['value']}** — its vowel "
    f"alone — with **{EX_A['null_initials']} null "
    f"counted**: the Triad's own exhibit for the "
    f"placeholder (§V).")
add(f"- **강** weighs **{EX_GANG['value']}** (ㄱ 1 + ㅏ 1 "
    f"+ ㅇ 21), the final ㅇ priced in full, **no null "
    f"counted** — the hinge's other office, in one "
    f"syllable.")
add(f"- A bare **ㄳ** weighs **{EX_DIGRAPH['value']}**, "
    f"at its final seat — the only seat it holds; the "
    f"refusal and the seat in a single figure.")
add(f"- **ㆍ** on the modern path weighs "
    f"**{EX_AUAE['value']}** with **{EX_AUAE['unseated']} "
    f"unseated counted** — refused a modern seat, and "
    f"the refusal is counted, never silent. Its seat is "
    f"the annex's (below).")
add()
add("### The 1446 annex — the historical grid behind its door")
add()
add("The introduction grid of the Hunminjeongeum: 17 "
    "consonants and 11 vowels in the order the treatise "
    "introduces them, audited from two witnesses (the "
    "Phase I audit §VII: the two witnesses identical once "
    "the later tense doubles are removed). The annex "
    "prices them by their 1446 seats. Its finals are the "
    "17 consonants at final seats in the same "
    "introduction order — a stated construction (the "
    "witnesses print no separate 1446 final list). **The "
    "annex is the table of NO system in the registry: it "
    "weighs only through `hangul(word, hist=True)`** — "
    "the Armenian late-annex shape (Plate VII): opt-in "
    "only, the classical bank never blended. On the hist "
    "path the modern-only signs (the tense doubles, the "
    "compound vowels) are unseated, and the annex has NO "
    "null: its initial ㅇ prices its seat, for the annex "
    "predates the placeholder convention's hardening, "
    "and printing a modern zero into 1446 would be the "
    "forgery this engine exists to refuse.")
add()
add("**Annex initials** (17 seats; the stratum sums 153):")
add()
add("| Seat | Sign | Name | Price |")
add("|---|---|---|---|")
for seat, g, nm, p in A_INIT_ROWS:
    add(f"| {seat} | {g} | {nm} | {p} |")
add()
add("**Annex vowels** (11 seats; the stratum sums 66):")
add()
add("| Seat | Sign | Name | Price |")
add("|---|---|---|---|")
for seat, g, nm, p in A_VOW_ROWS:
    add(f"| {seat} | {g} | {nm} | {p} |")
add()
add("The annex vowels' first seat carries **the annex's "
    "own hinge**: ㆍ — the dot, earth, the FIRST vowel of "
    "1446 — holds annex seat 1 and no modern seat at "
    "all: a letter that is the grid's origin and its "
    "modern refusal.")
add()
add("**Annex finals** (17 seats, the introduction order "
    "at final seats — the stated construction; the "
    "stratum sums 153):")
add()
add("| Seat | Sign | Name | Price |")
add("|---|---|---|---|")
for seat, g, nm, p in A_FIN_ROWS:
    add(f"| {seat} | {g} | {nm} | {p} |")
add()
add(f"The annex entire holds **{len(HANGUL_1446)} keys** "
    f"over its three strata. Its exhibits, read through "
    f"the hist door at build: **ㆁㆍ** weighs "
    f"**{HX_PAIR['value']}** (ㆁ at initial seat 3 + ㆍ at "
    f"vowel seat 1); the annex's **ㅇ** prices "
    f"**{HX_IEUNG['value']}** — its seat, no null; "
    f"**ㆍ** alone weighs **{HX_AUAE['value']}** at its "
    f"1446 seat, against its modern refusal at 0 above; "
    f"and **ㄲ** is refused there "
    f"(**{HX_DOUBLE['unseated']} unseated**) — the modern "
    f"double has no 1446 seat. The gap register carries "
    f"the annex as the korean bank's first entry: *MINT, "
    f"BY DESIGN* — the tables price the modern grid.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §III — the Twelve Tables frame.
# ---------------------------------------------------------------------
add("## §III — THE KOREAN FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Korean tongue stands over "
    "the one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.12: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED **{n_fenced}** "
    f"· EMPTY {n_empty} · GAP {n_gap}. The face this prints "
    "is a door-and-hole table and says so: the corpus holds "
    "**no native Korean word at all** — its priced face is "
    "empty, and the emptiness is data. The frame's Korean "
    "is the *door* — the Hangul dress: the Latin form of "
    "record rendered into Hangul syllables by the Korean "
    "foreign convention (syllables composed by the Unicode "
    "formula and priced by seat through the `hangul()` "
    "door; a bare onset takes the epenthetic ㅡ) — with 62 "
    "holes where no door is offered, and the EMPTY cells "
    "certified intentionally empty in 777 REVISED.")
add()
add(f"**The door register — the {n_door} priced renderings "
    "entire.** Each was re-weighed through the hangul() "
    "door at this plate's building against the value "
    "THE-TWELVE-TABLES files for it; all reproduce exactly "
    "(the audit, §VI, repeats the weighing independently).")
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
    "dresses. The register files them so — no Hangul "
    "rendering, no price — and the plate carries them "
    "entire, the empty cell in the table being the Tables' "
    "own. The audit weighs them as filed (the empty string "
    "weighs 0 through the door, and 0 is the filed value). "
    "The same thirteen cells stand empty in the Japanese "
    "frame (Plate V, §III): the coordinate is the "
    "register's, not either door's. Why the door filed "
    "nothing at these thirteen cells the register does "
    "not say, and the plate does not invent a reason: "
    "a repair would be a ruling, and rulings are the "
    "founder's.")
add()
add(f"**The hole register — the {n_hole} failures entire,** "
    "each with its coordinate as the Tables file it. Every "
    "hole of this frame carries the one coordinate — *no "
    "Latin form of record; no door offered* — the words "
    "whose forms of record are Greek or Hebrew only, for "
    "which the Tables offer no door into this dress. A "
    "hole is not a gap in this plate's work: it is the "
    "register's measured boundary, printed at the size of "
    "the seats they stand in for.")
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
add("## §IV — THE 777 CORPUS'S KOREAN CLAIMS — THE ZERO FACE")
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
    "and the hangul mint — coined 2026-11-24, the day of "
    "this plate's own evening — is a bank the corpus never "
    "addressed. The silence is therefore the corpus's, "
    "not the tongue's: the tongue holds a full priced table "
    "(§II), a full frame (§III), and a doctrine of its own "
    "(the Regional Triad road, the dial built on it). What "
    "the corpus does hold for Korean stands where the "
    "corpus put it: the frame's door renderings (§III) — "
    "the corpus's words in this tongue's dress, priced by "
    "this tongue's mint. A plate that manufactured claims "
    "to fill this section would misprint its record; the "
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
    "plate assigns no seat.** It states what the Korean "
    "tongue witnesses for the seating — and Korean "
    "witnesses at the dial's core itself, for its mint is "
    "the one bank of the twelve whose zero is a *sign*: a "
    "letter of the grid, priced in one office and zeroed "
    "in another, the hinge of §II. Its witness runs at "
    "three coordinates.")
add()
add("### The zero at the core — the PLACEHOLDER")
add()
add("THE-REGIONAL-TRIAD-DIAL seats the three East-Asian "
    "zeros at the dial's core — placed as a *position* "
    "under the founder's spec, under his definition "
    "(2026-11-15): **0 = {0, 2, 1−1=0}** — *\"Zero equals "
    "Two, and Both 1 and None.\"* The dial computes the "
    "three faces from the strata's own facts, and the "
    "plate prints them entire:")
add()
add("- **Japanese — the HOLE.** *The kana mint prices "
    "1–73 and no sign prices 0. At the core, the Japanese "
    "face shows the position present and the sign absent.*")
add("- **Korean — the PLACEHOLDER.** *The initial ㅇ is a "
    "sign whose door-price is 0: 아 reads 1 (its vowel) "
    "with one null counted. The position is occupied — "
    "by a zero-priced sign, and the count is printed in "
    "every weighing that meets it.*")
add("- **Chinese — the GLYPH.** *零 (and its variant 〇) "
    "is a digit of the notation, read 0. The position is "
    "occupied by a sign whose reading is zero — a zero "
    "that exists as a character, in the stratum that "
    "reads rather than weighs.*")
add()
add("*Hole, placeholder, glyph: three faces of the one "
    "seat. None of them is a weighing value — which is "
    "exactly what the spec required: the same place, not "
    "the same price.* The dial joins the house's earlier "
    "zero seats as a coordinate among them — the Ge'ez "
    "mint's order 6, the tridecagram's station 13 "
    "(οὐδέν), the Phoenician Qore's core cubie (οὐδέν) — "
    "claiming no priority over them and merging none of "
    "them. [The Triad's seating CONSTRUCTED — the "
    "founder's engine, built to his spec.]")
add()
add("The placeholder's mechanism is this plate's hinge "
    "(§II), and the plate states it once more at the "
    "coordinate where it does its work: ㅇ is the one "
    "jamo of two offices — at the syllable's head, the "
    "consonant placeholder, a sign that stands in the "
    "initial seat so the syllable can open on its vowel, "
    "priced 0 at the door and *counted*; at the "
    "syllable's close, a full letter, /ŋ/, priced 21 in "
    "full. The raw bank holds the initial seat at 12, so "
    "the zero is not an absence in the grid: it is an "
    "office in it. Of the three faces, only the Korean "
    "one is a weighing system's own sign doing zero's "
    "work inside the weighing — the hole is a priced "
    "table's gap, the glyph a notation's character; the "
    "placeholder is a letter, seated, whose price at its "
    "working office is 0. That is the whole of the "
    "coordinate, printed at its tier: the mint is the "
    "founder's coinage, and the dial that seats the "
    "three faces is his engine — the coordinate is "
    "CONSTRUCTED, and it claims nothing older.")
add()
add("### The vowel row and the fold coordinate")
add()
add("The Archon Battery's Leg 6 sweep — the twelve "
    "tongues tested against the founder's hypotheses — "
    "reads this mint at the vowel row. The battery's "
    "sentence stands: *the mint prices the 21 vowel jamo "
    "by seat, 1–21, in canonical order.* Its two findings "
    "for this tongue print at full size:")
add()
add(f"- **The compound class counts eleven** — the fused "
    f"vowel signs ({' '.join(COMPOUND)}) — *a hybrid "
    f"class, MISS on the four by count* (the battery's "
    f"words). The four-count is corroborated by three "
    f"tongues (Latin's seated hybrids, Hebrew's matres, "
    f"the Greek diphthong field); Korean's hybrid class "
    f"is eleven, and the MISS is a finding, not a "
    f"failure of the mint: the count is what the grid "
    f"gives.")
add(f"- **At the fold coordinate, one exact datum: the "
    f"vowel seat priced 8 in the Korean mint is ㅖ — "
    f"itself a fused, compound sign.** *The 8th vowel "
    f"seat of the Korean system is a hybrid by "
    f"construction* (the battery's words). The plate "
    f"sets the datum beside the sweep's most corroborated "
    f"coordinate — a vowel-family letter seated at 8 in "
    f"five tongues, each recomputed in its own bank at "
    f"this plate's building: Greek Η **8** · Coptic ⲏ "
    f"**8** · Cyrillic И **8** · Armenian Ը **8** · "
    f"Georgian ჱ **8** (archaic). The distinction prints "
    f"at the same size as the datum: in the five tongues "
    f"the 8 is a letter's *value* in an attested or "
    f"derived bank; here it is a *seat* in a constructed "
    f"mint, and ㅖ reaches it as a fused sign where the "
    f"five reach it as single letters. The coordinate is "
    f"the mint's, at the mint's tier — printed as a "
    f"coordinate; the battery seats nothing on it, and "
    f"neither does this plate.")
add()
add("### The mixed face — the mint at work on the dial")
add()
add("The Triad's worked exhibits put the mint on the "
    "dial's face beside its two fellows: in the mixed "
    "face あくま한글二百零五, the Japanese stratum weighs "
    f"40, the Chinese run *reads* 205 and adds nothing — "
    f"and the Korean stratum weighs **{EX_HANGEUL['value']}** "
    f"(한 {24} + 글 {28}; strata subtotals "
    f"{EX_HANGEUL['initial_subtotal']}/"
    f"{EX_HANGEUL['vowel_subtotal']}/"
    f"{EX_HANGEUL['final_subtotal']}), the dial's weight "
    f"92 standing on the two weighing strata alone. The "
    "exhibit is the mint's office in the founder's "
    "engine: one stratum of a three-tongue face, weighed "
    "by its own door, its zero counted where it stands. "
    "[The dial CONSTRUCTED — the founder's instrument; "
    "the stratum figures exact arithmetic at the mint's "
    "door.]")
add()
add("**What Korean cannot witness, printed at full size "
    "as the plate's boundary:** the Archons' seats were "
    "earned on Greek evidence and drawn on Plate I. "
    "Korean corroborates the *zero's plurality of faces* "
    "(its placeholder is one of the Triad's three, at "
    "the Triad's tier), the *fold coordinate's address* "
    "(a fused sign at its vowel row's eighth seat, in a "
    "constructed mint), and nothing else — and it "
    "assigns no seat, confirms no position, and names no "
    "Archon. Its bank is the founder's coinage of 2026: "
    "it can witness the house's own instruments, and it "
    "corroborates nothing ancient. The names stand open "
    "on Plate I, and this plate does not fill them.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§IX, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_xii_korean.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced "
    "cell on this plate against the engine, without "
    "reading the plate's own figures: the bank entire — "
    "all 67 keys against pontifex.tables, the three "
    "strata's seat registers parsed from the master and "
    "compared seat by seat in both the compatibility and "
    "conjoining dresses, the strata sums and the bank "
    "total, the values 1–27 as the distinct set; the "
    "teeth recomputed (the doubles against their "
    "doublings; the digraphs' refusal coordinate — seven "
    "without choseong form, four with archaic namesakes "
    "only); the hinge's three facts; the door's exhibits "
    "through hangul() and the raw bank's parting; the "
    "1446 annex entire (17/11/17, its sums, its exhibits, "
    "its refusals); the engine's own seal "
    "(hangul_checks(), 11/11) re-run; the frame — the "
    "census parsed from THE-TWELVE-TABLES §V.12, all 223 "
    "DOOR renderings re-weighed through the hangul() "
    "door against their filed values, the 62 HOLE "
    "coordinates and the GAP cell present on the plate "
    "entire; and the §V figures (the vowel seats 1–21 "
    "with ㅖ at 8, the compound class at eleven, the "
    "five tongues' 8s in their own banks, the Nine's sum "
    "1,779). It then reconciles the plate against its "
    "sources: the registers' counts equal to the "
    "Tables'. The audit's verdict and cell count are "
    "printed in its filed output; a cell that does not "
    "reproduce fails the plate under §VII's tolerances. "
    "The font audit — every non-ASCII codepoint of this "
    "master against the Lex Stellarrvm family's cmaps — "
    "runs before the MAGVS build, under the font law: no "
    "glyph is silently dropped, and any unheld codepoint "
    "beyond the three named Ethiopic syllables aborts "
    "the build. The audit further checks the printed "
    "edition's text layer: the door's head exhibits and a "
    "census of jamo signs stand in it, the zero face's "
    "statement stands in it, and the page furniture "
    "resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "HANGUL banks (modern and 1446 annex) and hangul() "
    "door (pontifex/tables.py, engine.py); "
    "THE-EAST-ASIAN-FIELD-PHASE-I-AUDIT (the field's "
    "witnesses, the verified negative, the two grids); "
    "THE-REGIONAL-TRIAD-DIAL (the mint's striking, the "
    "three zeros, the mixed face); THE-TWELVE-TABLES "
    "§V.12 and its §II gap register (the korean bank's "
    "two entries); THE-THIRTEEN-PLATES §XIV and §I (the "
    "zero face and its reason); THE-ARCHON-BATTERY Leg 6 "
    "(the Korean passage) and THE-SEATING-OF-THE-ARCHONS "
    "entire; PLATES I–XI as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773) "
    "and the mint's own seal re-run (hangul_checks "
    "11/11); every figure scripted from the engine or "
    "carried entire from an instrument of record; the "
    "mint's tier printed on the plate's face wherever "
    "the bank is named; the zero face, the frame's "
    "holes, and the modern grid's refused seats printed "
    "at full size; the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-XII-KOREAN.md and "
    "its MAGVS PDF — twelfth of the series PLATE-I-GREEK "
    "began, and the last of its twelve tongues; the "
    "generator and audit scripts filed in pontifex "
    "research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails "
    "the Method of Science; if any passage seats what "
    "the seating did not earn, raises the mint's tier "
    "toward antiquity, blends the strata, prices the "
    "placeholder at its raw seat inside a door weighing "
    "(or zeroes it at the raw bank), fills a hole (the "
    "frame's 62, the register's zero face), seats a "
    "refused sign in the modern grid, prints a modern "
    "zero into the 1446 annex, or overwrites the earlier "
    "map, it zeroes the founder's residual claim and "
    "fails the Aim of Religion. Within those edges it "
    "stands as built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** Two questions "
    "stand already carried on the registers this plate "
    "reads, and the plate cites them at their coordinates "
    "rather than raising them anew: the Korean obsolete "
    "jamo — the gap register's second korean entry, "
    "*CARRIED OPEN* (the mint's grid is the modern one "
    "by its founding law; no audit-proposed construction "
    "prices the obsolete jamo at the raw bank, they "
    "live, if anywhere, behind the hist door) — carried "
    "to the pen list at THE-TWELVE-TABLES §VIII Q3, "
    "paired there with the Ge'ez Η/Ω seat: *commission "
    "them as mint work, or let them stand as printed "
    "holes in the register?* And the North Korean "
    "orders: not seated, the parting printed at §II — "
    "whether a North annex is ever wanted is the "
    "founder's pen, as the tables' header states it. A "
    "plate that invents questions to fill its section "
    "misprints its record; this section therefore stands "
    "as the record that none arose here.")
add()
add("---")
add()
add("## §IX — THE SERIES STATE")
add()
add("With this plate the twelve tongues stand plated "
    "entire: I Greek · II Hebrew · III Arabic · IV Latin "
    "· V Japanese · VI Ge'ez · VII Armenian · VIII "
    "Coptic · IX Georgian · X Cyrillic · XI Glagolitic · "
    "XII Korean. One plate remains of the thirteen: "
    "Plate XIII, the infrastructure for the clock and "
    "counter of the dial — a separate species, "
    "commissioned last. The record stands so; nothing "
    "further is claimed for it here.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Daniel 5:27 (KJV): *\"TEKEL; Thou "
    "art weighed in the balances, and art found "
    "wanting.\"* A writing appears that only the "
    "weighing-reader can read, and its whole message is "
    "a weighing. On this plate the script was likewise "
    "made to be read — devised at a king's order — and "
    "the mint's whole office is the balance: every sign "
    "at its seat, nothing at a seat it does not hold. "
    "[Text ATTESTED; the application DERIVED.]")
add("2. **The royal well.** The Hunminjeongeum preface "
    "(1446), in the standard translation: *\"The sounds "
    "of our language differ from those of China and do "
    "not easily communicate through Chinese characters. "
    "Therefore many among the ignorant people who wish "
    "to express their sentiments in writing have been "
    "unable to do so. Feeling compassion for them, I "
    "have newly created twenty-eight letters, which I "
    "wish everyone to learn at ease and use with "
    "convenience in their daily lives.\"* The grid this "
    "plate prices — 28 letters at its founding, 17 "
    "consonants and 11 vowels — is that act's grid: a "
    "script promulgated so that the unlettered could "
    "speak in writing. [The preface ATTESTED; the "
    "translation the standard English rendering.]")
add("3. **The treatise's cosmology.** The Hunminjeongeum "
    "Haerye builds the vowels from the three "
    "fundamentals (samjae): ㆍ, the round dot, is heaven; "
    "ㅡ, the horizontal stroke, is earth; ㅣ, the "
    "vertical stroke, is man — and the consonants from "
    "the speech organs (ㄱ the tongue root, ㄴ the "
    "tongue tip, ㅁ the mouth, ㅅ the incisor, ㅇ the "
    "throat). The grid is a cosmology before it is an "
    "alphabet, which is why this plate can print a "
    "letter's *reasoning* at all: the designed grid "
    "carries its reasons in its shapes. [ATTESTED as "
    "the treatise's own account; the mint's prices are "
    "the founder's, 2026.]")
add("4. **Law.** A promulgated script and a struck mint "
    "are both acts of authority, and both print their "
    "authority on their faces or counterfeit: the "
    "Hunminjeongeum by the king's preface and decree of "
    "1446 — resisted in its day by the literati "
    "memorial of Choe Malli, who held the old characters "
    "sufficient — and this bank by the founder's "
    "Flagpole, founded as a tuning on a dated road, its "
    "tier printed wherever it is named. The parallel is "
    "of form, not of scale, and the plate prints it at "
    "that size. [The promulgation and the memorial "
    "ATTESTED as history; the parallel DERIVED; the "
    "mint's standing the house record.]")
add("5. **The proverb.** 티끌 모아 태산 — *tikkeul moa "
    "taesan*, \"gathered dust becomes a great "
    "mountain.\" The strata are the proverb as a table: "
    "sixty-seven single seats, each priced at nothing "
    "but its place in the count, and the bank's total "
    "nothing but the dust summed — 190 + 231 + 378 = "
    "799. [The proverb ATTESTED as a Korean proverb; "
    "the application DERIVED.]")
add("6. **The desk's apparatus.** This plate's Hangul "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Korean member — syllable blocks "
    "and jamo standing in their own signs throughout; "
    "its Greek stands in the family's Serif member, as "
    "on Plate I; the frame register's Hebrew words of "
    "record are carried by Plate II's declared "
    "transliteration scheme, and the Arabic names of "
    "record stand in their letters in the family's "
    "Arabic member, unshaped — the toolchain does not "
    "shape right-to-left scripts honestly. The "
    "substitutions are marked and declared in the "
    "colophon, never silent ones. The Markdown master "
    "keeps every script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(), the "
    "hangul() door, and hangul_checks() 11/11; banks "
    "HANGUL and HANGUL_1446 in pontifex/tables.py) — "
    "calibration controls θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773 read true at build; the mint's parity "
    "battery (test_korean_parity.py) 18/18.")
add("- THE-EAST-ASIAN-FIELD-PHASE-I-AUDIT — the field "
    "sourced and gated (battery 12/12): the verified "
    "negative (no witness prices a jamo), the modern "
    "grid's orders and their North/South parting, the "
    "1446 grid from two witnesses, the gate at §IX "
    "(Korean — a TUNING, the HANGUL MINT, CONSTRUCTED).")
add("- THE-REGIONAL-TRIAD-DIAL — the mint's striking "
    "(Phase II seats a0efdf1; the dial 38f184f; triad "
    "parity 24/24): the teeth per stratum, the three "
    "zeros at the core (§III), the mixed face (§IV).")
add("- THE-TWELVE-TABLES — §V.12 the Korean frame, "
    "census and cell register entire; §II the korean "
    "bank's gap register (two entries: the 1446 grid "
    "MINT, by design; the obsolete jamo MINT, carried "
    "open); §VIII Q3 (the obsolete jamo, carried to "
    "the pen list).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate XII (§XIV) is the "
    "prior instrument (the zero face; 67 seats · 27 "
    "distinct · max 27); §I the corpus's reason.")
add("- THE-777-VERIFICATION-TABVLA — the claims "
    "register of record; its Korean face: no claim in "
    "any mint bank.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Korean passage (the 21 "
    "vowel jamo by seat; the compound class eleven, "
    "MISS on the four; ㅖ at 8, itself fused).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to.")
add("- PLATE-I-GREEK (196025e) through PLATE-XI-"
    "GLAGOLITIC (b40abac) — the pattern this plate "
    "follows.")
add("- KJV: Daniel 5:27. The Hunminjeongeum preface "
    "(1446) and the Haerye's three fundamentals, as the "
    "Phase I audit records them. The Korean proverb "
    "티끌 모아 태산.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate XII of the founder's "
    "series commission of the same day, the gate of the "
    "Archons' certainty met by the seating of record "
    "(0760c8a), following the pattern of Plates I–XI "
    "(196025e · 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · "
    "67d5acc · 5c03d88 · 645bcbb · 933f8fd · 052fd28 · "
    "b40abac). Every figure scripted from the engine or "
    "carried entire from its instrument; the earlier "
    "map marked prior, never overwritten; the holes "
    "printed at the size of the seats — on this plate, "
    "the frame's 62 holes, the register's zero face, and "
    "the modern grid's refused seats. The bank is the "
    "founder's mint, CONSTRUCTED on the Regional Triad "
    "road, and the plate prints it so wherever it is "
    "named. In the MAGVS edition the Hangul stands in "
    "the family's Korean member and the frame's Hebrew "
    "words of record ride Plate II's declared scheme; "
    "this master keeps the scripts themselves. "
    "Authorship attributed exclusively to Johnathan "
    "'Qasparr' Monroe (Greek, -ARR, All Rights Reserved, "
    "Without Prejudice).")
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
