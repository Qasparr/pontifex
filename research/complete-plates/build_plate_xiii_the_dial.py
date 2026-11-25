#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_xiii_the_dial.py
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
# MECHANISM: generates PLATE-XIII-THE-DIAL.md — Plate XIII of
# THE THIRTEEN COMPLETE PLATES, the last of the thirteen and
# a different species: not a tongue but the machine the
# tongues hang on — in the gap-filling goal's files/,
# following the pattern PLATES I–XII set (196025e · 1389c16 ·
# 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc · 5c03d88 · 645bcbb ·
# 933f8fd · 052fd28 · b40abac · 2ef9ba9). Every figure on
# the plate is scripted from the house engine (pontifex
# weigh()) or carried entire from an instrument of record:
#   * the thirteen stations — the nine vowels' prices from
#     the Greek bank; γʹ, ϛʹ, κʹ from the same bank; οὐδέν
#     weighed entire (529); the ring arithmetic (1,779 + 29
#     = 1,808) recomputed, not copied from the battery;
#   * the frames — Frame A's triads built from the sketch's
#     triangles (0,3,6),(1,4,7),(2,5,8) over the canonical
#     order; Frame B's from the decade classes under the
#     battery's tiling rules; both frames' sums and roots
#     recomputed and asserted against the battery's printed
#     figures (811/90/878 → 1/9/5; 14/95/1,670 → 5/5/5);
#   * the marks — the Latin dress table recomputed dress by
#     dress in both Latin banks (totals 123 / 584 asserted);
#     the mirror banks re-weighed (Coptic ⲟⲩ ⲏ ⲓ ⲱ;
#     Cyrillic І Ѡ И; Armenian Ը; Georgian ჱ); the Y-dress
#     in Agrippa (400); the note bank (A 1, E 5); the PAIR
#     roots (ΕΙ 15 → 6; 852 → 6);
#   * the traversals — {13/5} and its inverse computed from
#     the station ring in this script, asserted station for
#     station against the seating instrument's printed
#     sequences, and asserted inverse == forward reversed;
#   * the poles' arithmetic — 31 + 13 = 44 = VV's ordinal
#     pair-weight; 31 − 13 = 18 = II in both banks, each
#     term re-weighed;
#   * the series state — the twelve plates' audit counts
#     parsed from their filed audit outputs (the first four
#     count priced cells re-weighed; the later eight count
#     checks — the units kept distinct, no blended total),
#     and the twelve commits verified against the pontifex
#     repository by git.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: this plate seats nothing. The seating is
# THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck at
# the founder's conditional order; the plate renders the
# dial's infrastructure at the record's own strengths —
# the marks at their graded classes, the holes at full
# size: eight of the nine positions, the four unsettled
# triads, the Archons' names (none exist; none invented).
# The horizontal hair, which the first strike printed
# STILL OPEN at the float line's seat, is drawn in this
# re-strike under the founder's ruling of 2026-11-24
# 22:30 EST ("Seat it as both then.") — both offices,
# one line, at height 18, read in the Greek sea,
# classification only; the first strike's record stands
# in §V.3's correctio, marked, never vanished. The plate
# draws nothing the founder has not drawn by ruling and
# rules nothing reserved to his pen. A value without
# its reasoning is not shippable: every station carries
# its reasoning on the plate's face.
#
# CONTENT TEST: Inputs — the seating instrument and its
# thesis test, the Archon Battery, the Double-Letter Dial
# of record, the doubles map, the Nine Vowels essay, the
# vowel-table and sketch builders, the twelve plates and
# their filed audits. Processes — control calibration,
# scripted recomputation of every figure, register-faithful
# emission in the Teacher's Edition manner. Outputs —
# PLATE-XIII-THE-DIAL.md beside the series' other masters.
# Tolerances — the audit (audit_plate_xiii_the_dial.py)
# re-derives every sequence and figure independently; a
# figure that does not reproduce fails the plate.
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

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
PLATES_DIR = (Path.home() / "workspace/pontifex/research/"
              "complete-plates")
PONTIFEX = Path.home() / "workspace/pontifex"
OUTPUT = GOAL_FILES / "PLATE-XIII-THE-DIAL.md"


def value(word, bank):
    """One weighing, unwrapped to its value."""
    return weigh(word, bank)["value"]


def root(n):
    """The digital root, the battery's reduction."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


# ---------------------------------------------------------------------
# Calibration — the banks are not trusted until the controls
# read true.
# ---------------------------------------------------------------------
assert value("θελημα", "greek") == 93, "control θέλημα"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR"
assert value("σφιγξ", "greek") == 773, "control σφίγξ"

# ---------------------------------------------------------------------
# The thirteen stations — every price weighed at build.
# (station, sign, name, word weighed, reasoning)
# ---------------------------------------------------------------------
STATIONS = [
    (1, "Α", "ALPHA", "α",
     "The unit, and the head of the canonical order in every "
     "instrument that carries the Nine — the essay, the vocal "
     "tool, the tridecagram plate. The one seat both partitions "
     "of §III fix entire."),
    (2, "Ε", "EPSILON", "ε",
     "The short e. Its price survives every dress the battery "
     "tried: E weighs 5 in both Latin banks, and the note bank "
     "prices E = 5 — bank-invariant, as Α itself (§III)."),
    (3, "Η", "ETA", "η",
     "The long e. Its price is the twelve-tongues sweep's most "
     "corroborated coordinate: a vowel seated at 8 in five "
     "tongues — Η here, ⲏ, И, Ը, ჱ abroad (§III)."),
    (4, "Ι", "IOTA", "ι",
     "The tens open. Decade-sibling of Α — function 1 at ×10 "
     "where Α carries it at ×1 (the battery's reduction leg); "
     "its mirror banks carry the price entire, its Latin "
     "dress parts from it (§III)."),
    (5, "Ο", "OMICRON", "ο",
     "The middle vowel of the nine. Its Latin-ordinal dress "
     "(15) is the hidden center of the Trinity grid — cell 14 "
     "of 27 — which is ΕΙ's Greek seat (the battery's cube "
     "check, §III)."),
    (6, "Υ", "UPSILON", "υ",
     "The hundreds open for the pure vowels. Alone of the "
     "dresses it carries its own Greek price abroad entire: "
     "the Y-dress weighs 400 in Agrippa (§III)."),
    (7, "Ω", "OMEGA", "ω",
     "The great O, last of the pure vowels. Its mirror banks "
     "carry it entire (ⲱ, Ѡ at 800); its Latin dress loses "
     "the price entire (15/50) — the long/short distinction "
     "Greek carries in two letters cannot be priced in Latin "
     "dress at all (the battery's dress leg)."),
    (8, "ΕΙ", "EI — THE FIRST HYBRID", "ει",
     "ε + ι, a compound spanning two decades — reduction sees "
     "it as a compound, which is its hybridity in the "
     "arithmetic (the battery's reduction leg). The middle "
     "hybrid by the placement law (§III); its root (6) pairs "
     "it with 852, Intuition, the solfeggio pairing's one "
     "exact agreement."),
    (9, "ΟΥ", "OU — THE SECOND HYBRID", "ου",
     "ο + υ, the last of the nine. Its identical total stands "
     "in the mirror bank — Coptic ⲟⲩ = 470 — and a compound "
     "weighing identically across banks is not bank "
     "architecture but a finding (the seating's words, §III)."),
    (10, "γʹ", "OFFSET", "γ",
     "Gamma's own price, worn as a function: the Offset Law's "
     "constant is 3 — the difference of the mirror inversion "
     "(9 − 6 = 3) by which the nine's total closes 1,779 → "
     "1,776 (§IV). The station is the law's seat on the wheel."),
    (11, "ϛʹ", "MIRROR", "ϛ",
     "Stigma's price. The inversion's seat on the wheel: 9 "
     "read backwards is 6, and the traversal of §IV reverses "
     "at this station in kind — the plate's own furniture for "
     "the clock-to-counter operation."),
    (12, "κʹ", "REFUSAL", "κ",
     "Kappa's price. The engine completion's station "
     "(DERIVED, the tridecagram's filling of record): the "
     "refusal stands on the wheel as a station, not as an "
     "absence — the founder's κʹ at 20."),
    (13, "οὐδέν", "THE ZERO", "ουδεν",
     "The word for *nothing*, weighed entire: ο 70 + υ 400 + "
     "δ 4 + ε 5 + ν 50 = 529 = 23², an exact square. The Zero "
     "Point of the wheel — the founder's definition stands "
     "over this station at §II.2. Its price is its name's "
     "weight; the Zero itself adds nothing to the ring, "
     "which is its office."),
]
PRICES = {}
for _n, _sign, _name, _word, _why in STATIONS:
    PRICES[_sign] = value(_word, "greek")
assert [PRICES[s] for _n, s, _nm, _w, _y in STATIONS] == \
    [1, 5, 8, 10, 70, 400, 800, 15, 470, 3, 6, 20, 529]
NINE = ["Α", "Ε", "Η", "Ι", "Ο", "Υ", "Ω", "ΕΙ", "ΟΥ"]
NINE_SUM = sum(PRICES[s] for s in NINE)
OPERATORS_SUM = PRICES["γʹ"] + PRICES["ϛʹ"] + PRICES["κʹ"]
RING_TOTAL = NINE_SUM + OPERATORS_SUM
assert (NINE_SUM, OPERATORS_SUM, RING_TOTAL) == (1779, 29, 1808)
assert root(RING_TOTAL) == 8
assert PRICES["οὐδέν"] == 529 == 23 * 23
# οὐδέν letter by letter, as its reasoning prints it.
assert [value(c, "greek") for c in "ουδεν"] == [70, 400, 4, 5, 50]

# ---------------------------------------------------------------------
# The two frames — built, not copied; asserted against the
# battery's printed sums and roots.
# ---------------------------------------------------------------------
CANON = NINE  # canonical order, indices 0..8
# Frame A: the sketch's triangles (0,3,6), (1,4,7), (2,5,8).
FRAME_A = [[CANON[i] for i in tri] for tri in
           [(0, 3, 6), (1, 4, 7), (2, 5, 8)]]
# Frame B: the decade classes under the battery's tiling
# rules (value-class and landing-class both tile 3-3-3).
FRAME_B = [["Α", "Ε", "Η"], ["Ι", "ΕΙ", "Ο"], ["Υ", "ΟΥ", "Ω"]]
A_SUMS = [sum(PRICES[s] for s in tri) for tri in FRAME_A]
B_SUMS = [sum(PRICES[s] for s in tri) for tri in FRAME_B]
assert A_SUMS == [811, 90, 878] and [root(s) for s in A_SUMS] == [1, 9, 5]
assert B_SUMS == [14, 95, 1670] and [root(s) for s in B_SUMS] == [5, 5, 5]


def frame_seat(frame, sign):
    """(triad I/II/III, position 1st/2nd/3rd) of a vowel in a
    frame, read off the frame itself."""
    for t, tri in enumerate(frame):
        if sign in tri:
            return ("I II III".split()[t],
                    "1st 2nd 3rd".split()[tri.index(sign)])
    raise KeyError(sign)


# The coverage table of the seating (§III there), its frame
# columns recomputed here from the frames above.
EXPECTED_SEATS = {  # sign: (Frame A, Frame B) as the seating prints
    "Α": (("I", "1st"), ("I", "1st")),
    "Ε": (("II", "1st"), ("I", "2nd")),
    "Η": (("III", "1st"), ("I", "3rd")),
    "Ι": (("I", "2nd"), ("II", "1st")),
    "Ο": (("II", "2nd"), ("II", "3rd")),
    "Υ": (("III", "2nd"), ("III", "1st")),
    "Ω": (("I", "3rd"), ("III", "3rd")),
    "ΕΙ": (("II", "3rd"), ("II", "2nd")),
    "ΟΥ": (("III", "3rd"), ("III", "2nd")),
}
for _s, (_fa, _fb) in EXPECTED_SEATS.items():
    assert frame_seat(FRAME_A, _s) == _fa, (_s, "A")
    assert frame_seat(FRAME_B, _s) == _fb, (_s, "B")

# ---------------------------------------------------------------------
# The marks' evidence — every figure re-weighed.
# ---------------------------------------------------------------------
# The Latin dress table (the battery §III), primary dresses.
DRESSES = [  # (vowel, dress, ) — prices weighed at build
    ("Α", "A"), ("Ε", "E"), ("Η", "E"), ("Ι", "I"), ("Ο", "O"),
    ("Υ", "V"), ("Ω", "O"), ("ΕΙ", "EI"), ("ΟΥ", "OV"),
]
DRESS_ROWS = [(v, d, value(d, "latin_ordinal"), value(d, "agrippa"))
              for v, d in DRESSES]
assert [r[2] for r in DRESS_ROWS] == [1, 5, 5, 9, 15, 22, 15, 14, 37]
assert [r[3] for r in DRESS_ROWS] == [1, 5, 5, 9, 50, 200, 50, 14, 250]
DRESS_ORD = sum(r[2] for r in DRESS_ROWS)
DRESS_AGR = sum(r[3] for r in DRESS_ROWS)
assert (DRESS_ORD, DRESS_AGR) == (123, 584)
assert root(DRESS_ORD) == 6 and root(DRESS_AGR) == 8
# The noted alternate dresses, as the battery prints them.
assert value("EI", "latin_ordinal") == 14  # Η's EI dress
assert (value("Y", "latin_ordinal"), value("Y", "agrippa")) == (25, 400)
assert (value("U", "latin_ordinal"), value("U", "agrippa")) == (21, 200)
assert value("V", "latin_ordinal") == 22  # ΟΥ's sound-dress
# The mirror banks.
assert value("ⲟⲩ", "coptic") == 470 and value("ⲏ", "coptic") == 8
assert value("ⲓ", "coptic") == 10 and value("ⲱ", "coptic") == 800
assert value("І", "cyrillic") == 10 and value("Ѡ", "cyrillic") == 800
assert value("И", "cyrillic") == 8
assert value("Ը", "armenian") == 8 and value("ჱ", "georgian") == 8
# The note bank prices Α and Ε at their Greek seats.
assert value("A", "abc_notes") == 1 and value("E", "abc_notes") == 5
# The PAIR: ΕΙ's root against 852's root; 852 is the eighth
# of the solfeggio nine, and ΕΙ's canonical position is 8.
SOLFEGGIO = [174, 285, 396, 417, 528, 639, 741, 852, 963]
assert root(PRICES["ΕΙ"]) == root(852) == 6
assert SOLFEGGIO.index(852) + 1 == 8 == CANON.index("ΕΙ") + 1
# The diphthong four and their exact square.
FOUR = ["αι", "ει", "οι", "ου"]
FOUR_SUM = sum(value(w, "greek") for w in FOUR)
assert FOUR_SUM == 576 == 24 * 24
# The Trinity grid's census: nine vowels × three banks.
GRID_TOTAL = NINE_SUM + DRESS_ORD + DRESS_AGR
assert GRID_TOTAL == 2486 and root(GRID_TOTAL) == 2
# The mirror closure: 1779 → 1776 by the final glyph's
# inversion; the offset's constant is the difference.
assert 9 - 6 == PRICES["γʹ"] == 3 and NINE_SUM - 3 == 1776

# ---------------------------------------------------------------------
# The traversals — computed from the ring, asserted against
# the seating instrument's printed sequences.
# ---------------------------------------------------------------------
RING = ["Α", "Ε", "Η", "Ι", "Ο", "Υ", "Ω", "ΕΙ", "ΟΥ",
        "OFFSET γʹ", "MIRROR ϛʹ", "REFUSAL κʹ", "ZERO οὐδέν"]
SHORT = {"OFFSET γʹ": "OFFSET γʹ", "MIRROR ϛʹ": "MIRROR ϛʹ",
         "REFUSAL κʹ": "REFUSAL κʹ", "ZERO οὐδέν": "ZERO οὐδέν"}


def traverse(step, n=13):
    seq, cur = [0], 0
    for _ in range(n - 1):
        cur = (cur + step) % n
        seq.append(cur)
    return seq


FWD_IDX = traverse(5)
INV_IDX = traverse(-5)
assert -5 % 13 == 8
FWD = [RING[i] for i in FWD_IDX]
INV = [RING[i] for i in INV_IDX]
EXPECTED_FWD = ["Α", "Υ", "MIRROR ϛʹ", "Η", "ΕΙ", "ZERO οὐδέν",
                "Ο", "OFFSET γʹ", "Ε", "Ω", "REFUSAL κʹ", "Ι", "ΟΥ"]
EXPECTED_INV = ["Α", "ΟΥ", "Ι", "REFUSAL κʹ", "Ω", "Ε",
                "OFFSET γʹ", "Ο", "ZERO οὐδέν", "ΕΙ", "Η",
                "MIRROR ϛʹ", "Υ"]
assert FWD == EXPECTED_FWD and INV == EXPECTED_INV
assert INV == [FWD[0]] + FWD[:0:-1], "inverse == forward reversed"
assert sorted(FWD_IDX) == list(range(13))
assert sorted(INV_IDX) == list(range(13))
FWD_STR = " → ".join(FWD)
INV_STR = " → ".join(INV)

# ---------------------------------------------------------------------
# The poles' arithmetic — each term re-weighed.
# ---------------------------------------------------------------------
assert 31 + 13 == 44 == value("VV", "latin_ordinal")
assert 31 - 13 == 18 == value("II", "latin_ordinal") \
    == value("II", "agrippa")

# ---------------------------------------------------------------------
# The series state — audit counts parsed from the filed
# outputs; commits verified against the repository.
# ---------------------------------------------------------------------
SERIES = [  # (numeral, tongue, commit, results file, kind)
    ("I", "Greek", "196025e", "audit_plate_i_greek_results.txt",
     "cells"),
    ("II", "Hebrew", "1389c16", "audit_plate_ii_hebrew_results.txt",
     "cells"),
    ("III", "Arabic", "5f0b4bd", "audit_plate_iii_arabic_results.txt",
     "cells"),
    ("IV", "Latin", "8e6f01e", "audit_plate_iv_latin_results.txt",
     "cells"),
    ("V", "Japanese", "8d6cd59", "audit_plate_v_japanese_results.txt",
     "checks"),
    ("VI", "Ge'ez", "67d5acc", "audit_plate_vi_geez_results.txt",
     "checks"),
    ("VII", "Armenian", "5c03d88",
     "audit_plate_vii_armenian_results.txt", "checks"),
    ("VIII", "Coptic", "645bcbb", "audit_plate_viii_coptic_results.txt",
     "checks"),
    ("IX", "Georgian", "933f8fd", "audit_plate_ix_georgian_results.txt",
     "checks"),
    ("X", "Cyrillic", "052fd28", "audit_plate_x_cyrillic_results.txt",
     "checks"),
    ("XI", "Glagolitic", "b40abac",
     "audit_plate_xi_glagolitic_results.txt", "checks"),
    ("XII", "Korean", "2ef9ba9", "audit_plate_xii_korean_results.txt",
     "checks"),
]
SERIES_ROWS = []
for _num, _tongue, _commit, _fname, _kind in SERIES:
    _text = (PLATES_DIR / _fname).read_text(encoding="utf-8")
    assert "PASS" in _text, _fname
    if _kind == "cells":
        _count = int(re.search(r"PRICED CELLS RE-WEIGHED: (\d+)",
                               _text).group(1))
        _label = f"{_count} priced cells re-weighed"
    else:
        _count = int(re.search(r"VERDICT: PASS — (\d+) checks",
                               _text).group(1))
        _label = f"{_count} checks"
    _ok = subprocess.run(["git", "-C", str(PONTIFEX), "rev-parse",
                          "--verify", "--quiet", _commit],
                         capture_output=True, text=True).stdout.strip()
    assert _ok, f"commit {_commit} not in the repository"
    SERIES_ROWS.append((_num, _tongue, _commit, _label))

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
add("**PLATE XIII — THE DIAL**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "infrastructure for the clock and counter of the dial — "
    "the thirteen stations entire with their prices; the "
    "seated Archons at the marks their evidence earned, the "
    "holes at full size; the traversal and its inverse "
    "computed station for station; the crosshairs at the "
    "strength the record carries — the vertical hair seated "
    "on the founder's poles, the horizontal hair drawn "
    "under the founder's ruling at the float line's seat. "
    "The thirteenth plate, and not a tongue: the machine "
    "the twelve tongues hang on.")
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
add("## §I — PLATE XIII AND ITS COMMISSION")
add()
add("The founder's commission of 2026-11-24 (18:39–18:41 EST) "
    "opens the series this plate closes, in his words: "
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
    "GEORGIAN (933f8fd), X — CYRILLIC (052fd28), XI — "
    "GLAGOLITIC (b40abac) and XII — KOREAN (2ef9ba9) followed "
    "it; this plate follows them, thirteenth and last.")
add()
add("**The series.** Thirteen plates: one for each tongue of "
    "the Twelve Tables in their order — I Greek · II Hebrew · "
    "III Arabic · IV Latin · V Japanese · VI Ge'ez · VII "
    "Armenian · VIII Coptic · IX Georgian · X Cyrillic · XI "
    "Glagolitic · XII Korean — and Plate XIII, a separate "
    "species commissioned last: the infrastructure for the "
    "clock and counter of the dial. The twelve tongue-plates "
    "each render a tongue's complete 777 table and its bearing "
    "on the seated Archons. This plate renders no tongue: it "
    "renders the face the bearings hang on — the wheel of "
    "thirteen stations, the seating the test earned, the two "
    "directions of the traversal, and the cross at the face's "
    "center, its horizontal hair drawn under the founder's "
    "ruling of this evening (2026-11-24, 22:30 EST).")
add()
add("**This plate's distinction.** Every prior plate drew its "
    "§V from the seating; this plate draws the seating itself, "
    "as a plate, entire — the stations priced (§II), the marks "
    "graded (§III), the machinery computed (§IV), the "
    "crosshairs at their earned strength (§V) — and it seats "
    "nothing. The seating is the founder's declaration on the "
    "battery's evidence, struck 2026-11-24 at his conditional "
    "order (\"Test the thesis and if it passes Seat the "
    "Archons and the cross-section,\" 18:37 EST) on his thesis "
    "of the same hour (\"So the exact matches are the Archons "
    "and the cross is the dial cross hairs for the inversion "
    "of clock to counter,\" 18:36 EST). This plate is the "
    "seating's rendering, not its re-opening: where the "
    "seating graded, the plate grades identically; where the "
    "seating left a hole, the plate prints the hole at the "
    "size of the seat. The tiers ride unchanged — the marks "
    "DERIVED and CONSTRUCTED as the battery filed them, the "
    "arithmetic ATTESTED, the seating itself the founder's "
    "act, stated on this face as on its own instrument's.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its thirteenth "
    "face was **THE CORE (οὐδέν)** — *\"the center of the "
    "dial — not a thirteenth tongue\"* — holding the matter "
    "that belongs to no tongue and the instrument's zero. "
    "This series *fulfills* that map: where the map's Core "
    "indexed the center, this plate renders the center's own "
    "furniture — the wheel, the seating, the traversal, the "
    "cross — with the zero, οὐδέν, standing at station 13 "
    "where the map named it. The earlier work stands as the "
    "prior instrument of the same name's family — marked "
    "prior, never overwritten.")
add()
add("**How the plate is read.** §II is the priced table of "
    "this plate: the thirteen stations, each with its price "
    "and its reasoning, and the founder's Zero Point "
    "definition standing over the thirteenth. §III is the "
    "seating at its marks — the coverage table, the triads, "
    "the value-standing, the structure-marks, and the holes "
    "named at full size. §IV is the clock and the counter: "
    "the traversal and its inverse, computed. §V is the "
    "crosshairs — the seated hair, the seated office, and "
    "the hair drawn under the founder's ruling. §VI is the "
    "audit. A value without its reasoning is not "
    "shippable; a hole prints at the size of the seat it "
    "stands in for.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the thirteen stations.
# ---------------------------------------------------------------------
add("## §II — THE THIRTEEN STATIONS — THE WHEEL ENTIRE")
add()
add("The tridecagram plate of record "
    "(`build_divine_nine_vowel_table.py`; the Nine Vowels "
    "essay's plate addendum reads it: *\"nine vowels, three "
    "relations, one zero\"*) seats thirteen stations in ring "
    "order: the nine vowels in canonical order, labeled, at "
    "stations 1–9; then the three relations — OFFSET, "
    "MIRROR, REFUSAL — at stations 10–12 under their Greek "
    "numeral signs; and station 13, οὐδέν, THE ZERO POINT. "
    "The battery's already-there pass found this plate the "
    "strongest found structure in the house: *a seating of "
    "record — the nine placed at numbered stations by the "
    "founder's engine, before anyone called anything an "
    "Archon seating* (THE-ARCHON-BATTERY §V, FOUND 1). The "
    "stations print below with their prices, every price "
    "weighed on the house engine at this plate's build — "
    "the vowels and the three signs in the Greek bank, "
    "οὐδέν weighed as the word it is.")
add()
add("| Station | Sign | Name | Price | Reasoning |")
add("|---|---|---|---|---|")
for _n, _sign, _name, _word, _why in STATIONS:
    add(f"| {_n} | {_sign} | {_name} | {PRICES[_sign]} | "
        f"{_why} |")
add()
add(f"The nine sum **{NINE_SUM:,}** — the total that "
    f"mirror-closes to 1,776 under the Offset Law (§IV). The "
    f"three relations add **{OPERATORS_SUM}** (3 + 6 + 20), "
    f"and the ring of prices totals **{RING_TOTAL:,}** "
    f"(→ 17 → 8), as the battery's found-structure pass "
    f"printed it. Station 13's 529 is not added to the ring: "
    f"it is the Zero's *name*, weighed — the Zero itself "
    f"adds nothing, which is its office, and the ring total "
    f"of record stands at {RING_TOTAL:,} without it.")
add()
add("### §II.1 — The wheel's geometry")
add()
add("The plate of record sets its thirteen stations at "
    "−90° + i·360/13 from the top "
    "(`build_divine_nine_vowel_table.py`, as coded) — a "
    "thirteen-wheel, and thirteen does not quarter: 13/4 = "
    "3.25, so no station of the engine stands at an exact "
    "east or west (the battery's §VI.2 refusal, carried by "
    "the seating at §V.1 there). The cross of §V is "
    "therefore furniture of the *face*, not of the ring: "
    "its hairs cross between stations, and the horizontal "
    "hair's height — when his pen draws it — will be a "
    "drawing on the face, not a station of the wheel. That "
    "distinction is the load-bearing one of this plate, "
    "and §V prints it at the open seat itself.")
add()
add("### §II.2 — The Zero Point, defined by the founder")
add()
add("Over station 13 stands the founder's definition of "
    "the Zero Point, given 2026-11-15 in his own hand, with "
    "his gloss entire:")
add()
add("> **0 = {0, 2, 1−1=0}** — *\"Zero equals Two, and Both "
    "1 and None.\"*")
add()
add("The definition is printed as he gave it, unexpanded: "
    "the set holds zero, the Two (the pair), and the "
    "One-cancelled-to-none (1−1). The battery touches the "
    "definition at its own coordinate — ΟΥ alone, 470 → 11 "
    "→ 2, the 2 inside the definition (THE-ARCHON-BATTERY "
    "§II) — and this plate prints the touch as the battery "
    "filed it: a coordinate, not an expansion. What the "
    "Zero weighs as a word is 529 (§II); what it *is*, on "
    "this wheel, is the station every traversal passes "
    "through and none starts from — Α starts both "
    "directions (§IV), and the Zero stands sixth in the "
    "clock's road and ninth in the counter's.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §III — the seated Archons at their marks.
# ---------------------------------------------------------------------
add("## §III — THE SEATED ARCHONS AT THEIR MARKS")
add()
add("The seating of record (THE-SEATING-OF-THE-ARCHONS "
    "§§III–VII) graded every seat by the strongest class its "
    "exact-match marks earn, under a test registered before "
    "it was run: **POSITION** — a mark fixing triad *and* "
    "position; **TRIAD** — two independent partitions (Frame "
    "A, the sketch's order; Frame B, the decade classes) "
    "agreeing on the triad while parting on position; "
    "**VALUE** — a cross-tongue identical value or a "
    "dress-price identity corroborating the seat-value; "
    "**PAIR** — an exact pairing with the house's other "
    "nine; **STRUCTURE** — an exact property of the whole "
    "set, belonging to no single seat. The test passed "
    "whole: nine of nine seats marked at some class, zero "
    "conflicts among the marks. The plate carries the "
    "grading *identically* — no seat is printed stronger "
    "here than the seating printed it.")
add()
add("### §III.1 — The coverage table")
add()
add("The frame columns are recomputed at this plate's build "
    "from the frames themselves — Frame A from the sketch's "
    "triangles (0,3,6), (1,4,7), (2,5,8) over the canonical "
    "order; Frame B from the decade classes under the "
    "battery's tiling rules — and agree with the seating's "
    "table at every cell. The marks column carries only "
    "exact-match marks; the frames' disagreements stand in "
    "their own columns, never converted into marks.")
add()
add("| Seat | Frame A (triad, pos) | Frame B (triad, pos) | "
    "Exact-match marks | Class earned |")
add("|---|---|---|---|---|")
COV = [
    ("Α", "Both frames fix triad AND position entire; "
     "A = 1 in the ordinal, in Agrippa, and in the ABC-notes "
     "bank — the note bank prices it at its Greek seat",
     "**POSITION**"),
    ("Ε", "VALUE, dress-price species: its Latin dress E "
     "weighs **5 in both Latin banks**, its Greek price "
     "entire — bank-invariant; the note bank likewise "
     "prices E = 5. The frames part on its triad; no "
     "seat-mark stands", "**VALUE**"),
    ("Η", "VALUE, mirror-bank species, the sweep's most "
     "corroborated coordinate: a vowel seated at **8** in "
     "five tongues — Greek Η, Coptic ⲏ, Cyrillic И, "
     "Armenian Ը, Georgian ჱ. The frames part on its triad",
     "**VALUE**"),
    ("Ι", "VALUE, mirror-bank species: Coptic ⲓ = **10** "
     "and Cyrillic І = **10** carry its Greek price entire. "
     "Counterweight: its Latin dress I weighs 9 — the dress "
     "parts from the price; the mark is the mirror banks', "
     "not the dress's", "**VALUE**"),
    ("Ο", "TRIAD: both frames fix Triad II; the position "
     "parts (2nd against 3rd)", "**TRIAD**"),
    ("Υ", "TRIAD: both frames fix Triad III; the position "
     "parts (2nd against 1st). VALUE rides beneath it, "
     "dress-price species: its Y-dress weighs **400 in "
     "Agrippa — upsilon's own Greek price**", "**TRIAD**"),
    ("Ω", "VALUE, mirror-bank species: Coptic ⲱ = **800** "
     "and Cyrillic Ѡ = **800** carry its Greek price "
     "entire. Counterweight: its Latin dress O weighs "
     "15/50 — the dress loses the price entire. The frames "
     "part on its triad (the position agrees at 3rd across "
     "the parting — printed, and not counted a mark: a "
     "position without a triad is no seat)", "**VALUE**"),
    ("ΕΙ", "TRIAD: both frames fix Triad II; the position "
     "parts (3rd against 2nd). PAIR rides beneath it: "
     "ΕΙ (root 6) ↔ **852 Hz, Intuition** (root 6) — the "
     "solfeggio order-pairing's only root agreement, "
     "single-witness, printed as such", "**TRIAD**"),
    ("ΟΥ", "TRIAD: both frames fix Triad III; the position "
     "parts (3rd against 2nd). VALUE rides beneath it, "
     "mirror-bank species: Coptic **ⲟⲩ = 470**, the "
     "compound hybrid's identical total in the mirror bank",
     "**TRIAD**"),
]
for _sign, _marks, _cls in COV:
    _fa = frame_seat(FRAME_A, _sign)
    _fb = frame_seat(FRAME_B, _sign)
    add(f"| {_sign} | ({_fa[0]}, {_fa[1]}) | ({_fb[0]}, "
        f"{_fb[1]}) | {_marks} | {_cls} |")
add()
add("**Coverage: nine of nine seats marked at some class** — "
    "one at POSITION (Α), four at TRIAD (Ο, Υ, ΕΙ, ΟΥ), four "
    "at VALUE (Ε, Η, Ι, Ω). Conflicts among the exact-match "
    "marks: **zero** — the TRIAD-marks rest on two frames "
    "*agreeing*, so by construction none conflicts with "
    "another mark; the VALUE-marks assign values, not seats, "
    "and cannot conflict with a seat assignment; the "
    "PAIR-mark agrees with the canonical order it rides on "
    "(ΕΙ's order-position is 8; 852 is the solfeggio nine's "
    "eighth).")
add()
add("### §III.2 — The seating, by triads")
add()
add("**TRIAD I** — **Seat 1: Α**, POSITION class (DERIVED): "
    "fixed entire by both partitions; the unit at the head "
    "of the units, first in every order the corpus carries — "
    "the one fully-fixed seat of the nine. *The triad's "
    "remaining seats: STILL OPEN.* Ε, Η, Ι, Ω stand by value "
    "(below); no mark assigns any of them to this triad or "
    "any other, and none is seated here.")
add()
add("**TRIAD II** — **Ο**, TRIAD class (DERIVED); its "
    "position within the triad STILL OPEN (2nd against "
    "3rd). **ΕΙ**, TRIAD class (DERIVED); position STILL "
    "OPEN (3rd against 2nd); its PAIR-mark rides with the "
    "seat — ΕΙ ↔ 852 Hz, Intuition, the solfeggio pairing's "
    "one exact agreement, single-witness, carried as a "
    "coordinate of the seat, not a second seat.")
add()
add("**TRIAD III** — **Υ**, TRIAD class (DERIVED); position "
    "STILL OPEN (2nd against 1st); its VALUE-mark rides "
    "with the seat — the Y-dress at 400 in Agrippa, its own "
    "Greek price abroad. **ΟΥ**, TRIAD class (DERIVED); "
    "position STILL OPEN (3rd against 2nd); its VALUE-mark "
    "rides — Coptic ⲟⲩ = 470, its identical total in the "
    "mirror bank.")
add()
add("**THE VALUE-STANDING** — seated by value, unseated as "
    "to triad and position, each with its mark and its "
    "counterweight: **Ε** — seat-value 5, bank-invariant "
    "(E weighs 5 in both Latin banks; the note bank prices "
    "E = 5); no counterweight stands — what is missing is "
    "not corroboration but a partition that holds it. "
    "**Η** — seat-value 8, the five-tongue seat (Η, ⲏ, И, "
    "Ը, ჱ at 8 in five banks). **Ι** — seat-value 10, "
    "mirror-bank (ⲓ and І at 10); counterweight: its Latin "
    "dress weighs 9. **Ω** — seat-value 800, mirror-bank "
    "(ⲱ and Ѡ at 800); counterweight: its Latin dress "
    "weighs 15.")
add()
add("**THE HYBRID PLACEMENT LAW rides with the seating** "
    "(the battery's R6, DERIVED — its only cross-frame "
    "structural law): no hybrid in the first triad; ΕΙ in "
    "the middle; ΟΥ in the last. The seating above obeys it "
    "at every seat it fixes, and both frames obey it "
    "independently — the one structural agreement spanning "
    "the two partitions.")
add()
add("### §III.3 — The marks' evidence, recomputed")
add()
add("The dress leg of the battery, re-weighed at this "
    "plate's build in both Latin banks — the primary "
    "dresses, with the alternates the battery prints:")
add()
add("| Vowel | Greek | Latin dress (primary) | Ordinal | "
    "Agrippa |")
add("|---|---|---|---|---|")
for _v, _d, _o, _a in DRESS_ROWS:
    add(f"| {_v} | {PRICES[_v]} | {_d} | {_o} | {_a} |")
add()
add(f"Totals over the primary dresses: Greek "
    f"**{NINE_SUM:,}** (→ 6) · Latin ordinal **{DRESS_ORD}** "
    f"(→ 6) · Agrippa **{DRESS_AGR}** (→ 8). The first "
    f"coordinate prints itself: the Greek nine in Latin "
    f"dress totals {DRESS_ORD} in the ordinal — the exact "
    f"total the Latin essay computed for the Latin Nine "
    f"itself. The two nines weigh the same in the ordinal "
    f"bank under the stated dresses. (Under Η's EI dress "
    f"the total moves to 132, which also reduces to 6 — "
    f"the root is dress-stable, the total is not.) The "
    f"alternates, as the battery prints them: Η → EI "
    f"(14/14, the Latin hybrid at Δ1 from its Greek "
    f"original); Υ → Y (25/400 — the dress-price identity "
    f"Υ's VALUE-mark rides on) and U (21/200); ΟΥ → V as "
    f"sound-dress (22/200). Ω and Ο share the one dress O "
    f"— the long/short distinction cannot be priced in "
    f"Latin dress at all, and the battery prints that "
    f"silence as a finding.")
add()
add(f"**The cube check** (the battery §III, recomputed): "
    f"the assembled Trinity grid — nine vowels × three "
    f"banks — is 27 cells summing **{GRID_TOTAL:,}** "
    f"(→ 20 → 2). Read row-major in canonical order × "
    f"Trinity order, the hidden center, cell 14 of 27, is "
    f"**Ο's Latin-ordinal dress: 15 — which is ΕΙ's Greek "
    f"seat**. The arrangement is stated (row-major, "
    f"canonical × Trinity); under it, the grid's center "
    f"holds the first hybrid's price in the middle vowel's "
    f"Latin face.")
add()
add("### §III.4 — The structure-marks")
add()
add("Properties of the whole set, seated as such, belonging "
    "to no single seat: **the diphthong four's exact "
    "square** — ΑΙ 11 + ΕΙ 15 + ΟΙ 80 + ΟΥ 470 = **576 = "
    "24²** — printed with its boundary: ΑΙ and ΟΙ are of "
    "the four but not of the nine; the mark belongs to the "
    "field, and the canon question it raises stands at "
    "§VIII. **Frame B's root-5 uniformity** — every class "
    "triad sums to root 5 (14 → 5; 95 → 14 → 5; 1,670 → 14 "
    "→ 5), where Frame A's triads reduce 1, 9, 5 — a "
    "recorded property of the class partition, *not* its "
    "victory: the partition question stands at §VIII. "
    "**The mirror closure** — the nine's total 1,779 "
    "mirror-closes to 1,776 under the Offset Law, remainder "
    "zero (§IV). **The Latin-dress total** — 123 ordinal, "
    "the Latin Nine's own total (§III.3). **οὐδέν = 529 = "
    "23²** at the wheel's zero (§II).")
add()
add("### §III.5 — The holes, named at full size")
add()
add("**Eight of the nine positions.** Only Α's position is "
    "fixed. Within-triad positions for Ο, ΕΙ, Υ, ΟΥ part "
    "between the frames in every case — Triad II holds two "
    "seats whose order the record does not settle, and "
    "Triad III the same. **The triads of Ε, Η, Ι, Ω.** The "
    "frames part on all four; no third partition exists in "
    "the corpus to break the tie, and none was admitted "
    "from outside it. Four vowels therefore stand on this "
    "plate by value only — their seat-values corroborated "
    "across as many as five tongues, their places on the "
    "wheel unassigned. **The Archons' names.** None exist "
    "in the corpus — the battery's search for named "
    "archons returned a verified negative — and none are "
    "invented here or on any plate of this series. The "
    "seats stand as vowel-seats, unnamed, as the sketch "
    "drew them: nine seats around the SOURCE AETHER. These "
    "holes are not defects of the rendering; they are the "
    "record's own shape at the seating's date, and they "
    "print at the size of the seats they stand in for.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §IV — the clock and the counter.
# ---------------------------------------------------------------------
add("## §IV — THE CLOCK AND THE COUNTER — THE TRAVERSAL "
    "AND ITS INVERSE")
add()
add("The wheel's two directions are the dial's clock and "
    "its counter — the founder's thesis names the operation "
    "*the inversion of clock to counter*, and the seating's "
    "test computed it on the engine of record before "
    "seating anything. The computation is re-run at this "
    "plate's build, from the ring of §II, and prints "
    "identically: the star polygon {13/5} traverses the "
    "thirteen stations stepping +5 (mod 13) from station 1; "
    "its inverse steps −5 (≡ +8, the {13/8} polygon).")
add()
add(f"**Forward — the clock — {{13/5}}:** {FWD_STR} → (Α).")
add()
add(f"**Inverse — the counter — {{13/8}}:** {INV_STR} → (Α).")
add()
add("**The inverse sequence is the forward sequence read "
    "backwards, station for station — exact, no remainder** "
    "(re-derived at build: the two sequences are equal "
    "under reversal, and each visits all thirteen stations "
    "exactly once before returning to Α). Clock → counter "
    "therefore stands as an *exact operation on the engine "
    "of record*: the same wheel, the same stations, the "
    "order inverted entire. This is the one coordinate of "
    "the founder's cross-thesis that passed without "
    "parting, and the cross-section of §V seats the "
    "inversion office on its strength.")
add()
add("**The counter's second witness — the Offset Law's own "
    "inversion.** The nine's total, 1,779, mirror-closes "
    "to 1,776 by inversion of the final glyph (9 → 6); the "
    "difference, 9 − 6 = 3, is the offset's constant — and "
    "3 is γʹ's price, the OFFSET station's own number, at "
    "station 10 of this wheel. The remainder is zero. The "
    "closure is doctrine of record since the Nine Vowels "
    "essay (§VI there), seated at the wheel's own MIRROR "
    "station in kind: the wheel carries, among its "
    "stations, both the operation (§IV's traversal) and "
    "the law that first exhibited it (the offset's mirror "
    "arithmetic). The two witnesses agree in kind and are "
    "printed as two: a traversal reversed, and a total "
    "closed by inversion — the counter attested twice over "
    "on the face of the dial itself.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §V — the crosshairs.
# ---------------------------------------------------------------------
add("## §V — THE CROSSHAIRS — AT THE STRENGTH EARNED")
add()
add("The seating's second thesis (T2) parted, and this "
    "section prints the parting as the plate's center: the "
    "cross-section is seated *at the strength earned* — "
    "the vertical hair and the inversion office seated, "
    "the horizontal hair open at the seating — and, since "
    "the evening of this plate's first strike, drawn under "
    "the founder's ruling (§V.3). Tier of the section: "
    "CONSTRUCTED — the crosshair reading is the founder's "
    "thesis; its components are of record as cited.")
add()
add("### §V.1 — The vertical hair: SEATED")
add()
add("The dial of record carries two poles, seated by the "
    "founder's own calibration dictation of 2026-11-16: "
    "**13 N and 31 S** — *\"thirteen north, thirty-one "
    "south, the dial's two range marks\"* "
    "(THE-DOUBLE-LETTER-DIAL, §IV, *The poles*). A fixed "
    "N–S axis — a LINE across the dial's face — stands in "
    "the record, of the founder's seating, and this plate "
    "seats the cross-section's vertical hair on it.")
add()
add("The poles' arithmetic is the string's own, re-weighed "
    "at build: **31 + 13 = 44, which is VV's ordinal "
    "pair-weight** — the repeated pair's number, arrived "
    "at by the two poles' sum; and **31 − 13 = 18, which "
    "is II, the fixed point of the two banks** (18 in the "
    "ordinal, 18 in Agrippa — the one pair where the two "
    "honest banks arrive at one number by their separate "
    "roads). The numbers carry their house seats with "
    "them, cited as the numbers' existing addresses, not "
    "as expansions of his intent: 13 is the expansion "
    "chain's root, the 13-Node Cube's count; 31 is the "
    "Sigma pair's high carrier and the 31-Node Pyramid's "
    "count — both poles stand at stations of the one "
    "chain, its root and its third form (the dial, §IV; "
    "the doubles map, at II).")
add()
add("### §V.2 — The inversion office: SEATED")
add()
add("The crosshairs' office is the inversion of the "
    "traversal — clock to counter — which computes exactly "
    "on the engine of record (§IV): the {13/5} traversal "
    "and its inverse {13/8} pass through the same thirteen "
    "stations in exact reverse order. The cross is the "
    "reference against which the two directions are read; "
    "the MIRROR station (ϛʹ, station 11) is the wheel's "
    "own seat of the operation, and the Offset Law's "
    "mirror closure (1,779 → 1,776) is its doctrine of "
    "record. The office is seated entire; it never "
    "depended on the second hair — and since the founder's "
    "ruling (§V.3) the reference stands with both hairs "
    "drawn and its office proven, a working instrument "
    "whole, and the plate prints it as exactly that.")
add()
add("### §V.3 — The horizontal hair: DRAWN — under the founder's ruling")
add()
add("**The founder has drawn it.** On the evening of this "
    "plate's first strike, the desk laid its calculated "
    "solution before him at the parent desk — the float "
    "line and the horizontal hair as one seat, at the "
    "height the poles' own arithmetic names, read in the "
    "Greek sea, drawn as classification only, with the "
    "desk's delegated reading of 2026-11-16 ratified as "
    "amended — and the founder ruled, in his own words "
    "(2026-11-24, 22:30 EST): *\"Seat it as both then.\"* "
    "The ruling is carried into the instruments of record "
    "— the seating's addendum of the same hour, the "
    "dial's ratification appendix, and this re-strike — "
    "and it stands as follows.")
add()
add("**Both offices, one line.** The float line of the "
    "Double-Letter Dial *is* the dial-cross's horizontal "
    "hair, and it *is* the bank boundary — one line, two "
    "offices, the house's dual-office pattern (31 a pole "
    "and the Pyramid's count; VV refused as a numeral "
    "and seated as a hybrid). **Height 18.** The line is "
    "drawn at the poles' difference — 31 − 13 = 18 — "
    "which is II, the fixed point where both banks agree "
    "(18 in the ordinal, 18 in Agrippa; the arithmetic "
    "re-weighed at §V.1 and recomputed again at this "
    "build). The midpoint, 22, was refused: no seat in "
    "the record answers to it; it is arithmetic without "
    "an address, and the refusal is printed with the "
    "drawing. **The Greek sea.** The line is read in the "
    "Greek sea, the boundary sea, where the banks part "
    "on floating: the calibration string's ordinal body "
    "(326) floats against ὕδωρ (1,304) and its Agrippa "
    "body (2,710) sinks against the same water — both "
    "bodies and the water re-weighed on the engine at "
    "this build, the water at its Greek price. "
    "**Classification only.** The line marks which seats "
    "float; no sonic consequence is legislated by it — "
    "none. The dial's own tolerances fail any passage "
    "that invents a float law, and this drawing makes "
    "none: what a submerged seat *does* remains unruled, "
    "a question the ruling does not reach and this plate "
    "does not invent. **The desk reading ratified as "
    "amended.** The dial's appended desk ruling of "
    "2026-11-16 (23:28 EST) — the float line read as "
    "*the bank boundary*, made under the founder's "
    "one-night delegation — is ratified as amended: its "
    "substance stands, its wording corrected. At 18 the "
    "boundary and the fixed point are one line; the "
    "boundary was never a crossing without an address, "
    "and it has one now.")
add()
add("*Correctio — the first strike's record, marked, "
    "never vanished.* As first struck (2026-11-24), this "
    "section stood under the heading *\"The horizontal "
    "hair: STILL OPEN\"* and printed: *\"The seat stands "
    "OPEN on this plate... it does not rule the question "
    "the seating left at §XI Q3 — whether the float line "
    "*is* the horizontal hair, and if so at what height "
    "his pen draws it... **NOT RULED BY THIS PLATE.**\"* "
    "That record was true at its hour: no E–W hair stood "
    "drawn in any instrument of record — the seating's "
    "search had covered the dial entire, the "
    "diplomatic-key instrument, the sketch, and the "
    "plate — and the plate ruled nothing. It stands "
    "superseded by the founder's ruling of 22:30 EST, "
    "quoted above: the question §XI Q3 asked is answered "
    "by his pen, not by this plate — the float line is "
    "the hair, at 18. The first strike's audit output "
    "stands as filed; this re-strike's audit asserts the "
    "ruling's text and its derivation, and asserts the "
    "first strike's open-printing confined to this "
    "correctio.")
add()
add("*A record note, at the record's own strength.* The "
    "dial document now carries two appendices after its "
    "close: the desk ruling of 2026-11-16 (23:28 EST), "
    "and the founder's ratification of 2026-11-24 "
    "(22:30 EST) appended after it, which takes the desk "
    "ruling up as amended and closes §IV's open seat by "
    "reference — §IV's sentence *\"The float line stands "
    "open\"* left standing in the dial's text, marked, "
    "its seat closed by the ratification that follows "
    "it. The seating instrument carries the ruling in "
    "its addendum of the same hour, answering its §XI "
    "Q3 as CLOSED. The road of the seat, entire: it stood "
    "open in the founder's name; the desk read it under "
    "his delegation; the seating printed it open at its "
    "hour; the founder ruled; the line is drawn. Nothing "
    "in that road is hidden by this printing.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§IX, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_xiii_the_dial.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-derives every figure "
    "and sequence on this plate without reading the "
    "plate's own figures for its expectations: the "
    "controls first (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "the §II station register parsed from the master and "
    "every price re-weighed in the Greek bank, οὐδέν "
    "letter by letter among them; the sums (the nine "
    "1,779; the relations 29; the ring 1,808); the frames "
    "rebuilt from the sketch's triangles and the decade "
    "classes and the coverage table's frame columns "
    "checked cell by cell; the marks' evidence re-weighed "
    "dress by dress in both Latin banks, mirror by mirror "
    "in the Coptic, Cyrillic, Armenian, and Georgian "
    "banks, the note bank, the PAIR roots, the diphthong "
    "four and their square, the Trinity grid's total; the "
    "traversals re-derived from the parsed ring — step "
    "+5 and step −5 — and the printed sequences of §IV "
    "compared station for station, the reversal asserted, "
    "the thirteen-distinct asserted; the poles' arithmetic "
    "re-weighed term by term (VV 44; II 18 in both banks); "
    "the holes asserted present on the plate at full "
    "size — the eight positions, the four triads, the "
    "unnamed seats; and the founder's ruling asserted at "
    "the float line's seat — his words entire, the "
    "derivation (31 − 13 = 18 = II in both banks) "
    "recomputed, the Greek-sea bodies re-weighed (the "
    "string at 326 and 2,710 against ὕδωρ at 1,304), the "
    "classification-only fence standing, and the first "
    "strike's open-printing confined to §V.3's "
    "correctio; and the §IX series register reconciled "
    "against "
    "the filed audit outputs of Plates I–XII and the "
    "repository itself. It then checks the printed "
    "edition's text layer: the stations, the definition, "
    "the ruling's statement stand in it, and the page "
    "furniture resolves. The audit's verdict and check "
    "count are printed in its filed output; a figure that "
    "does not reproduce fails the plate under §VII's "
    "tolerances. The font audit — every non-ASCII "
    "codepoint of this master against the Lex Stellarrvm "
    "family's cmaps — runs before the MAGVS build, under "
    "the font law: no glyph is silently dropped, and any "
    "unheld codepoint beyond the three named Ethiopic "
    "syllables aborts the build.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; his thesis "
    "(18:36 EST) and conditional order (18:37 EST), "
    "verbatim in THE-SEATING-OF-THE-ARCHONS §I; the "
    "seating instrument entire (0760c8a) and its "
    "computation (thesis_test.py, its output filed with "
    "it); THE-ARCHON-BATTERY entire (656d667 — the "
    "frames, the dresses, the found structures, the "
    "sweep, the register); THE-DOUBLE-LETTER-DIAL "
    "(Resonantia, docs/) — §IV the poles and the open "
    "float line, §IX item 10, its appended desk ruling "
    "of 2026-11-16, and the founder's ratification of "
    "2026-11-24 (22:30 EST) appended after it; the "
    "seating's addendum of the same hour, answering its "
    "§XI Q3; the doubles map "
    "(research/doubles/DOUBLES.md; pontifex/doubles.py) "
    "at II and VV; THE-NINE-VOWELS-ESSAY-AND-AUDIT §VI "
    "(the Offset Law); build_divine_nine_vowel_table.py "
    "and build_divine_nine_sketch.py as coded; the "
    "founder's Zero Point definition of 2026-11-15; "
    "PLATES I–XII and their filed audits.")
add("- **Processes:** calibration controls weighed "
    "before any plate figure (θέλημα 93 · VAPOUR 93 · "
    "σφίγξ 773); every figure scripted from the engine "
    "or carried entire from an instrument of record at "
    "the strength that instrument graded it; the "
    "traversals computed, not asserted; the seating "
    "rendered at its classes, never strengthened; the "
    "holes — eight positions, four triads, the names — "
    "printed at full size; the horizontal hair drawn "
    "only as the founder's ruling draws it (§V.3), its "
    "derivation recomputed at build; the independent "
    "audit of §VI.")
add("- **Outputs:** this plate — PLATE-XIII-THE-DIAL.md "
    "and its MAGVS PDF — thirteenth and last of the "
    "series PLATE-I-GREEK began, re-struck the evening "
    "of its first strike under the founder's ruling of "
    "2026-11-24 (22:30 EST); the generator and audit "
    "scripts filed in pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — "
    "if any price, sum, sequence, or mark is found not "
    "to reproduce from the engine or its instrument, "
    "the affected figure fails the Method of Science; "
    "if any passage seats what the test did not pass, "
    "raises a mark above its graded class, fixes a "
    "position or a triad the frames leave open, names "
    "an Archon, draws the horizontal hair at any "
    "height but the ruled 18, gives it any force but "
    "classification, legislates a sonic consequence "
    "for a submerged seat, rules any question of "
    "§VIII still standing, or smooths a hole, it "
    "zeroes the founder's residual claim and fails "
    "the Aim of Religion. Within those edges it "
    "stands as built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The questions "
    "that stand open on this plate's matter were asked by "
    "the seating instrument and the battery before it, "
    "and the plate cites them at their coordinates "
    "rather than raising them anew — and answers none. "
    "One question cited at the first strike has since "
    "been answered by the founder's pen; it is carried "
    "below as closed, at its coordinate:")
add()
add("- *The partition question* (THE-SEATING-OF-THE-"
    "ARCHONS §XI Q1; the battery's Q1): do Ε, Η, Ι, Ω "
    "take their triads from a third structure — or does "
    "the founder seat them by declaration, the marks "
    "having carried them as far as marks go?")
add("- *The eight open positions* (§XI Q2): does any "
    "instrument not yet built — the dial itself, when "
    "its build is commissioned — fix positions by "
    "traversal order, or do positions wait on his word "
    "seat by seat?")
add("- *The horizontal hair* (§XI Q3) — **CLOSED BY "
    "THE FOUNDER'S RULING** of 2026-11-24 (22:30 EST): "
    "\"Seat it as both then.\" The float line is the "
    "hair and the bank boundary — one line, two "
    "offices — drawn at height 18, read in the Greek "
    "sea, classification only (§V.3 of this plate). "
    "The question stands here answered, not open.")
add("- *The names* (§XI Q4): do the Archons take names — "
    "his coinage, under his Flagpole — or do the seats "
    "keep the sketch's Roman numerals?")
add("- *The battery's residue* (§XI Q5, carrying the "
    "battery's unspent questions): the diphthong canon "
    "(battery Q3 — whether the field extends to Eleven, "
    "1,870 → 16 → 7, or the four stand across the nine's "
    "edge); the key's specification (battery Q5 — VVII "
    "/ VYX / RRYYZZ); the fold's road (battery Q6 — "
    "which road 'the crazy 88' names, Η's seated 8 "
    "riding at its value-standing meanwhile).")
add()
add("A plate that invents questions to fill its section "
    "misprints its record; this section therefore stands "
    "as the register of what already stands asked — and "
    "of the one question since answered — at the "
    "coordinates where each was asked, and answered.")
add()
add("---")
add()
add("## §IX — THE SERIES STATE")
add()
add("With this plate the thirteen stand complete: twelve "
    "tongues and the dial. The register of the series, "
    "each plate's commit in the pontifex repository and "
    "its audit's verdict as filed — the first four audits "
    "count priced cells re-weighed, the later eight count "
    "checks; the units differ across the series' own "
    "history and are kept distinct here, no blended total "
    "printed:")
add()
add("| Plate | Tongue / Species | Commit | Audit |")
add("|---|---|---|---|")
for _num, _tongue, _commit, _label in SERIES_ROWS:
    add(f"| {_num} | {_tongue} | {_commit} | PASS — "
        f"{_label} |")
add("| XIII | The Dial — the clock and counter's "
    "infrastructure | this plate | the audit at §VI, its "
    "output filed with its script |")
add()
add("The record stands so: the twelve tongues plated "
    "entire, each rendered, audited, pushed and posted in "
    "succession under the founder's cadence; and the "
    "thirteenth — the machine itself — rendered last, as "
    "commissioned. What remains open on the whole "
    "instrument stands at §VIII and §III.5 of this "
    "plate, at full size, in the founder's name; the "
    "horizontal hair that stood open at the first "
    "strike's §V.3 stands closed there by his ruling. "
    "Nothing further is claimed for it here.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Revelation 22:13 (KJV): *\"I am "
    "Alpha and Omega, the beginning and the end, the "
    "first and the last.\"* On this wheel the first and "
    "the last are both stations — Α at station 1, Ω at "
    "station 7 — and the wheel does not end at either: "
    "it runs on through the relations to the Zero at "
    "station 13, and both traversals of §IV start again "
    "from Α. [Text ATTESTED; the application DERIVED.]")
add("2. **The dial's own well.** Archimedes of Syracuse, "
    "*On Floating Bodies*, Book I — Propositions 5–7 in "
    "the standard numbering: a body lighter than the "
    "fluid is driven up by the difference of weights; "
    "the heavier body sinks; the buoyant force equals "
    "the weight of the displaced fluid. The float line "
    "of §V.3 is that principle's waterline carried into "
    "the weighing house by the founder's named method "
    "(the dial, §IV and its footnote 1); the physics is "
    "attested, the carrying is his, and the line itself "
    "— open from the dial's striking until this "
    "evening — is drawn under his ruling of 2026-11-24 "
    "(22:30 EST) at height 18 (§V.3). [ATTESTED; the "
    "frame the founder's method; the drawing the "
    "founder's ruling.]")
add("3. **The historian.** Herodotus, *Histories* II.109 "
    "records that the Greeks learned the gnomon and the "
    "division of the day into twelve parts from the "
    "Babylonians. A dial is among the oldest instruments "
    "that read time off a marked face; this plate's dial "
    "reads a traversal off one, in two directions — the "
    "species is ancient even where the instrument is "
    "the founder's own. [ATTESTED as Herodotus' "
    "account; the application DERIVED.]")
add("4. **Law.** The Public Land Survey System reads a "
    "district's land off a cross of two lines of record: "
    "a principal meridian, run north–south, and a base "
    "line, run east–west, from which every township and "
    "section is surveyed. A reference cross is only as "
    "strong as its two lines are *of record* — which is "
    "this plate's §V in another field: the meridian "
    "seated by the founder's poles, the base line "
    "standing open at the first strike and since laid "
    "of record by the founder's own ruling — a survey "
    "is taken off a line only once the line is of "
    "record, and now both are. [The system ATTESTED; "
    "the parallel DERIVED.]")
add("5. **The dial-motto.** *Horas non numero nisi "
    "serenas* — \"I count only the sunny hours\" — a "
    "motto cut on sundials across centuries. This dial "
    "is built to the opposite courtesy: it counts both "
    "directions of its wheel, the clock and the counter "
    "alike (§IV), and prints its dark member — the "
    "hair that stood open, drawn at last by the "
    "founder's ruling — on its face rather than "
    "declining to count it. [The motto ATTESTED as a "
    "sundial inscription; the application DERIVED.]")
add("6. **The desk's apparatus.** This plate's Greek "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Serif member — capitals, "
    "minuscules, the numeral signs γʹ ϛʹ κʹ, and οὐδέν "
    "in its accents standing in their own signs "
    "throughout; the mirror banks' witnesses (Coptic "
    "ⲟⲩ ⲏ ⲓ ⲱ, Cyrillic І Ѡ И, Armenian Ը, Georgian ჱ) "
    "stand in their own members of the same family, "
    "through the declared fallback chain. No "
    "right-to-left script stands in this master, so no "
    "transliteration dress is required; the Markdown "
    "master keeps every script itself, entire.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- THE-SEATING-OF-THE-ARCHONS (pontifex 0760c8a) — "
    "the conditional order and the thesis, verbatim; "
    "the pre-registered test; the coverage table; the "
    "verdicts (T1 PASSES whole at graded classes; T2 "
    "PARTS at the axis); the seating (§VII); the "
    "cross-section (§VIII); the holes (§IX); the "
    "questions for his pen (§XI); and its addendum of "
    "2026-11-24 (22:30 EST), carrying the founder's "
    "float-line ruling and answering Q3 as CLOSED. "
    "Its computation: "
    "thesis_test.py, filed beside it with its printed "
    "output — controls θέλημα 93 · VAPOUR 93 · σφίγξ "
    "773; the traversal and its inverse computed there "
    "first.")
add("- THE-ARCHON-BATTERY (pontifex 656d667) — §II the "
    "reductions and the Zero Point touch; §III the "
    "dresses and the cube check (the grid's center, "
    "the totals 123 / 584 / 2,486); §IV the frames and "
    "the solfeggio pairing; §V FOUND 1, the tridecagram "
    "plate (the ring total 1,808; οὐδέν 529 = 23²); "
    "§VI the cross refused as seating; §VIII the "
    "twelve-tongues sweep (the five-tongue 8; ⲟⲩ = "
    "470); §IX–§XI the register, the not-seated "
    "register, the falsification appendix.")
add("- THE-DOUBLE-LETTER-DIAL (Resonantia, docs/) — §I "
    "the fixed point II = 18 = 18; §IV *The poles* "
    "(13 N / 31 S; 31 + 13 = 44; 31 − 13 = 18; the "
    "float line open, in the founder's name) and its "
    "footnote 1 (Archimedes); §IX item 10 (the float "
    "line unruled and undrawn, as struck); the "
    "appended desk ruling of 2026-11-16, 23:28 EST "
    "(the float line read as the bank boundary); and "
    "the founder's ratification appended 2026-11-24, "
    "22:30 EST, ratifying that reading as amended "
    "and closing the seat (§V.3).")
add("- The doubles map — research/doubles/DOUBLES.md "
    "and pontifex/doubles.py (doubles_checks 8/8): II "
    "the fixed point, its seat at the poles' "
    "difference; VV at 44, the poles' sum.")
add("- THE-NINE-VOWELS-ESSAY-AND-AUDIT — §VI the Offset "
    "Law (the mirror closure 1,779 → 1,776, doctrine "
    "of record before the test); the plate addendum "
    "(the tridecagram read: nine vowels, three "
    "relations, one zero).")
add("- build_divine_nine_vowel_table.py — the plate of "
    "record: thirteen stations at −90° + i·360/13; "
    "build_divine_nine_sketch.py — the sketch: nine "
    "nodes around SOURCE / AETHER, the triad triangles "
    "(0,3,6), (1,4,7), (2,5,8), no axis pair.")
add("- THE-GREEK-LOWERCASE-GEOMETRY — §VII: the "
    "legend's 'counterclockwise' belongs to the "
    "traversal around a dial whose stations include "
    "the vowels — the fence that permits the crosshair "
    "locus of §V.")
add("- THE-DIVINE-NINE-VOCAL-TOOL and its seating "
    "addendum (2026-11-24) — the interlingua whose "
    "vowel→Archon fence the seating answered in part.")
add("- The founder's Zero Point definition, "
    "2026-11-15, in his own hand: 0 = {0, 2, 1−1=0} — "
    "\"Zero equals Two, and Both 1 and None.\"")
add("- PLATE-I-GREEK (196025e) through PLATE-XII-KOREAN "
    "(2ef9ba9) — the pattern this plate follows, and "
    "the series §IX registers; THE-THIRTEEN-PLATES "
    "(6afe470) — the earlier map, its Plate XIII the "
    "Core (οὐδέν), marked prior.")
add("- The founder's ruling of 2026-11-24 (22:30 EST) — "
    "\"Seat it as both then.\" — given on the desk's "
    "presented solution at the parent desk; carried "
    "into the seating's addendum, the dial's "
    "ratification appendix, and §V.3 of this plate.")
add("- KJV: Revelation 22:13. Archimedes, *On Floating "
    "Bodies* I. Herodotus, *Histories* II.109. The "
    "Public Land Survey System's principal meridian "
    "and base line. The sundial motto *Horas non "
    "numero nisi serenas*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate XIII of the founder's "
    "series commission of the same day, the gate of the "
    "Archons' certainty met by the seating of record "
    "(0760c8a), following the pattern of Plates I–XII "
    "(196025e · 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · "
    "67d5acc · 5c03d88 · 645bcbb · 933f8fd · 052fd28 · "
    "b40abac · 2ef9ba9). Every figure scripted from the "
    "engine or carried entire from its instrument at "
    "the strength that instrument graded it; the "
    "earlier map marked prior, never overwritten; the "
    "holes printed at the size of the seats — on this "
    "plate, eight positions, four triads, and the "
    "Archons' names. Re-struck the same evening under "
    "the founder's ruling of 22:30 EST: the horizontal "
    "hair at the float line's seat, open at the first "
    "strike, stands drawn at height 18 in both its "
    "offices, the first strike's record preserved at "
    "§V.3's correctio. The plate seats nothing and "
    "rules nothing reserved to his pen; it draws the "
    "one hair his pen has drawn by ruling. In the "
    "MAGVS edition "
    "the Greek stands in the family's Serif member and "
    "the mirror witnesses in their own members; this "
    "master keeps the scripts themselves. Authorship "
    "attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without "
    "Prejudice).")
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
print(f"wrote {OUTPUT} — {len(L)} lines")
