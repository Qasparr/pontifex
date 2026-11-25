#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_viii_coptic.py
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
# MECHANISM: generates PLATE-VIII-COPTIC.md — Plate VIII of
# THE THIRTEEN COMPLETE PLATES — in the gap-filling goal's
# files/, following the pattern PLATES I–VII set (196025e ·
# 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc ·
# 5c03d88). Every figure on the plate is scripted from the
# house engine (pontifex weigh() and the coptic() manuscript
# door) or carried entire from an instrument of record:
#   * the priced table — the Coptic bank entire, read from
#     pontifex.tables (COPTIC, 27 keys), each seat printed
#     with its Greek parent and its reasoning — in this
#     tongue the reasoning is the descent: the Milesian
#     seat, the parent sign at the same value on Plate I's
#     bank, the witnesses' agreement at the cell;
#   * the letter names, the Greek equivalents and the
#     NO VALUE rows — the Phase I audit's frozen
#     transcription (research/twelve-tongues/
#     coptic-table.csv), cross-checked against the living
#     banks at build;
#   * the calibration corpus — the witnesses' worked
#     examples and the sweep's seventeen rows in the
#     sweep's own dresses (research/twelve-tongues/
#     coptic.md), recomputed at build, the two UNKNOWNs
#     verified as fence-crossings, not merely as sums;
#   * the manuscript door's exhibits — the marks counted
#     and none priced, at the door and at the raw bank;
#   * the Twelve Tables' Coptic frame — its census and
#     its full cell register parsed from THE-TWELVE-
#     TABLES.md §V.8: the 183 DOOR renderings re-weighed
#     at build against their filed values, the 40 FENCED
#     renderings verified to cross a fenced letter, the
#     62 HOLE coordinates and the one GAP cell carried
#     entire, the bank's four gap-register entries
#     restated;
#   * the corpus's Coptic claims — exactly ONE: the
#     TABVLA register's S155-P0-C0 (§III.156, LI/32 bis,
#     weighed on ⲧ), reproduced entire with its verdict,
#     its Hebrew companion at its coordinate, and the
#     three Coptic-named sections the corpus leaves empty;
#   * the tongue's bearing on the seated Archons — the
#     Archon Battery's Leg 6 Coptic passage (the seven
#     vowels at exactly the Greek prices; ⲟⲩ at 470),
#     the seating's Η and ΟΥ rows with their mirror-bank
#     species stated, and the Ι and Ω witnesses at their
#     coordinates. The plate assigns no seat: the seating
#     is THE-SEATING-OF-THE-ARCHONS' (0760c8a), already
#     struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable
# — every priced seat carries its reasoning on the plate's
# face. This plate's bank is the series' one INHERITANCE:
# neither made at the desk (the mints) nor found whole in
# the wild (the attested tables), but RECEIVED — the Greek
# Milesian grid entire, in the Egyptian hand. Its honesty
# is therefore the opposite of corroboration: the daughter
# bank carries the parent's prices BY ARCHITECTURE, the
# tier reads DERIVED, and agreement between the two banks
# is continuity, single-sourced — one fact in two scripts,
# never two witnesses. The boundary stands at the same
# size as the values: the seven Demotic letters the
# tradition itself leaves unvalued stand FENCED, their
# dash a positive statement of the sources; the marks are
# counted and priced NONE, under a frozen parity exhibit
# that stopped a fill in the open; the thousands question
# stands carried open for the founder's pen, unruled by
# this plate. The relation to the earlier Thirteen Plates
# map is printed, the earlier work marked prior, never
# overwritten. Holes print at the size of the seats — on
# this plate, the frame's 62 holes and its 40 fences.
#
# CONTENT TEST: Inputs — the engine's COPTIC and GREEK
# tables and the coptic() door, THE-COPTIC-TABLE-PHASE-I-
# AUDIT with its frozen CSV, the sweep's Coptic account,
# the Twelve Tables master, the Thirteen Plates map, the
# TABVLA register, the Archon Battery, the Seating.
# Processes — control calibration, scripted extraction,
# register-faithful emission in the Teacher's Edition
# manner. Outputs — PLATE-VIII-COPTIC.md beside the
# series' other masters. Tolerances — the audit
# (audit_plate_viii_coptic.py) re-weighs every priced
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
from pontifex.engine import _COPTIC_ORDER, coptic as coptic_door
from pontifex.tables import COPTIC, GREEK

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "twelve-tongues/coptic-table.csv")
OUTPUT = GOAL_FILES / "PLATE-VIII-COPTIC.md"


def value(word, bank="coptic"):
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
# The frozen transcription — the audit's 34 rows: names, Greek
# equivalents, origins, values, statuses. The bank's seats are
# read against it at every step below.
# ---------------------------------------------------------------------
with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
assert len(CSV_ROWS) == 34
BY_SMALL = {r["lowercase"]: r for r in CSV_ROWS}
VALUED = [r for r in CSV_ROWS if r["status"] == "SOURCED"]
UNVALUED = [r for r in CSV_ROWS if r["status"] == "NO VALUE"]
assert len(VALUED) == 27 and len(UNVALUED) == 7
for r in VALUED:
    assert COPTIC[r["lowercase"]] == int(r["value"]), r
for r in UNVALUED:
    assert r["lowercase"] not in COPTIC, r

# The Milesian seat order — the engine's own sequence, checked
# against the bank and the frozen values.
SEATS = list(_COPTIC_ORDER)
assert len(SEATS) == 27 and set(SEATS) == set(COPTIC)
MILESIAN = ([d for d in range(1, 10)] + [d * 10 for d in range(1, 10)]
            + [d * 100 for d in range(1, 10)])
for pos, ch in enumerate(SEATS, 1):
    assert COPTIC[ch] == MILESIAN[pos - 1], (pos, ch)
BANK_SUM = sum(COPTIC.values())                    # 4,995
assert BANK_SUM == 4995 == sum(GREEK[g] for g in GREEK
                               if g != "στ") - 200  # see below
# The Greek bank sums 5,201 over its 29 keys: the 27-seat grid
# (4,995) + the final form ς at 200 + the στ digraph at 6 —
# stated exactly in §II.4's prose from these computed parts:
GREEK_KEYS = {g: GREEK[g] for g in GREEK}
assert sum(GREEK_KEYS.values()) == 5201
assert GREEK_KEYS["ς"] == 200 and GREEK_KEYS["στ"] == 6
assert len(set(COPTIC.values())) == 27             # uniqueness
assert max(COPTIC.values()) == 900
CLASS_SUMS = {"units": 45, "tens": 450, "hundreds": 4500}
for pos, ch in enumerate(SEATS, 1):
    cls = "units" if pos <= 9 else "tens" if pos <= 18 \
        else "hundreds"
    assert COPTIC[ch] == MILESIAN[pos - 1]


def class_of(pos):
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    return "hundreds", pos - 18, 2


def greek_parent(val):
    """The parent bank's holder at a value — from the frozen
    CSV's equivalent column, cross-checked against the living
    GREEK bank: some sign of the parent carries the value."""
    assert val in set(GREEK.values()), val
    row = next(r for r in VALUED if int(r["value"]) == val)
    return row["greek_equivalent"]


LETTER_NOTES = {
    "ⲁ": "The devices' letter: the sources' thousands "
         "examples ride on this sign (ⲁ͵ and ⲁ̿ each write "
         "1,000) — devices of notation, counted at the door "
         "and priced none (§II.5).",
    "ⲋ": "**A parting of kind.** The stigma seat's heir: a "
         "numeral sign on both banks, a living letter on "
         "neither. Isaac, expressly: the sixth letter \"is "
         "not used as a letter, but as a numeral whose value "
         "is 6\"; Satzinger marks the seat \"Number only.\" "
         "Descent preserved the seat's numeral-only nature "
         "with its value (§II.4).",
    "ⲏ": "**The Archons coordinate of this plate:** a vowel "
         "at exactly 8 — the fold's target in a third tongue, "
         "and one of the seating's mirror-bank witnesses "
         "(§V).",
    "ⲓ": "The seating's Ι witness stands on this letter: "
         "ⲓ = 10 carries its Greek price entire in the "
         "mirror bank (§V).",
    "ϥ": "**The descent's one parting of lineage.** This "
         "living Demotic letter — /f/, at home in ordinary "
         "words (ϥ̀ⲧⲟⲟⲩ, \"four,\" among fsymbols' number "
         "words) — holds the seat Greek's archaic ϟ (koppa) "
         "held dead. Its place in the letter inventory is "
         "27th, after the Greek run; its Milesian seat is "
         "the tens' last. Wikipedia marks its equivalence "
         "\"(numerical value)\": the kinship is the seat, "
         "not the glyph (§II.4).",
    "ⲥ": "**A parting of form.** The Greek bank carries two "
         "glyphs at this seat (σ and its word-final ς); "
         "Coptic carries one letter with no final-form "
         "split. The value descends entire; the form "
         "distinction does not (§II.4).",
    "ⲧ": "**The corpus's one Coptic claim weighs this "
         "sign** — S155-P0-C0, claimed 300, VERIFIED "
         "(§IV).",
    "ⲩ": "The ⲟⲩ compound's second sign: ⲟ + ⲩ = 70 + "
         "400 = 470, the seated hybrid's identical total "
         "in this bank (§V).",
    "ⲱ": "The seating's Ω witness stands on this letter: "
         "ⲱ = 800 carries its Greek price entire in the "
         "mirror bank (§V).",
    "ⳁ": "A valued sign, not a letter: sampi stands "
         "outside the 32-letter inventory altogether "
         "(the audit's D5), descended into the Coptic "
         "block from Greek ϡ — a sign for a sign, one "
         "class up from sou. Satzinger's course does not "
         "exhibit it; the three full-table witnesses seat "
         "it, and the Unicode standard names it.",
}

# ---------------------------------------------------------------------
# Calibration — the witnesses' worked examples, recomputed; the
# sweep's corpus in the sweep's own dresses, re-verified.
# ---------------------------------------------------------------------
EXAMPLES = [("ⲫ", 500, "Wikipedia's §Numerals example — "
             "\"such as ⲫ for 500\""),
            ("ⲓⲃ", 12, "fsymbols' composite, \"highest "
             "first\""),
            ("ⲧⲝⲉ", 365, "fsymbols' composite — the letter "
             "part the door's overline exhibit also carries "
             "(§II.5)"),
            ("ⲱⲡⲏ", 888, "the letter part of Wikipedia's "
             "thousands example ⲁ͵ⲱ̅ⲡ̅ⲏ̅ = 1,888 — the ⲁ͵ "
             "device is reported at §II.5, never priced "
             "into the letters"),
            ("ⳁϥⲑ", 999, "the largest number writable in "
             "letters alone — one sign per class, "
             "descending")]
for w, want, _n in EXAMPLES:
    assert value(w) == want, (w, value(w), want)
assert value("ⲀⲂⲄ") == value("ⲁⲃⲅ") == 6         # the case fold
assert value("Ϥⲁ") == 91                            # fai's fold
assert value("Ⳁ") == 900                             # sampi's fold

# The sweep's corpus (Worker #8, 2026-10-11), its dresses and
# verdicts as the Phase I audit re-verified them 17 of 17.
CORPUS = [("AXONEME", "ⲁⲝⲟⲛⲉⲙⲉ", 231, "weighed"),
          ("OZ", "ⲟⲍ", 77, "weighed — the bridge's OZ half "
           "holds, as continuity (§II.3)"),
          ("TRVVTH", "ⲧⲣⲃⲃⲑ", 413, "weighed — the "
           "sweep's dress renders V by its sound, ⲃ"),
          ("THELEMA", "ⲑⲉⲗⲉⲙⲁ", 90, "mechanical dress; "
           "the epsilon/eta merger is the transliteration's "
           "loss, not the table's"),
          ("AGAPE", "ⲁⲅⲁⲡⲉ", 90, "mechanical dress — the "
           "collision with THELEMA at 90"),
          ("THELEMA (Greek-aware)", "ⲑⲉⲗⲏⲙⲁ", 93,
           "authentic Greek spelling — 93 stands"),
          ("AGAPE (Greek-aware)", "ⲁⲅⲁⲡⲏ", 93,
           "authentic Greek spelling — 93 stands; the "
           "collision with THELEMA at 93"),
          ("BABALON", "ⲃⲁⲃⲁⲗⲟⲛ", 156, "weighed"),
          ("QIRA", "ⲕⲓⲣⲁ", 131, "weighed"),
          ("LIBERTY", "ⲗⲓⲃⲉⲣⲧⲓ", 457, "weighed — the "
           "sweep's dress renders Y as ⲓ; its Y→ⲩ variant "
           "reads 847"),
          ("CELL", "ⲕⲉⲗⲗ", 85, "weighed — not 32: the "
           "English-ordinal bridge does not cross"),
          ("AXONEME (X→ⲭ)", "ⲁⲭⲟⲛⲉⲙⲉ", 771, "the "
           "anti-hit: near 777, is not 777"),
          ("HERU-RA-HA", "ϩⲉⲣⲟⲩⲣⲁϩⲁ", 677, "UNKNOWN — "
           "ϩ valueless; the figure is the partial sum of "
           "the weighable letters"),
          ("ABRAHADABRA", "ⲁⲃⲣⲁϩⲁⲇⲁⲃⲣⲁ", 213, "UNKNOWN "
           "— ϩ valueless; the Hebrew 418 bridge does not "
           "cross")]
for _name, dress, want, _note in CORPUS:
    got = value(dress)
    assert got == want, (_name, got, want)
    if "UNKNOWN" in _note:
        # The UNKNOWN is a fence-crossing, verified as one:
        # the dress contains a letter the bank does not hold,
        # and that letter is absent from the breakdown.
        r = weigh(dress, "coptic")
        assert any(ch not in COPTIC for ch in dress), _name
        assert all(ch in COPTIC for ch, _v in r["breakdown"])
assert value("ⲟⲍ") == value("οζ", "greek") == 77   # the descent

# ---------------------------------------------------------------------
# The descent, in code: the value sets identical; the holders
# parting at exactly the seats the audit names.
# ---------------------------------------------------------------------
assert set(COPTIC.values()) == set(GREEK.values())
assert GREEK["ϛ"] == COPTIC["ⲋ"] == 6               # kind
assert GREEK["ϟ"] == 90 and COPTIC["ϥ"] == 90        # lineage
assert GREEK["ϡ"] == COPTIC["ⳁ"] == 900              # kind
assert GREEK["σ"] == GREEK["ς"] == COPTIC["ⲥ"] == 200  # form

# ---------------------------------------------------------------------
# The boundary: the seven unvalued, silent in both cases; the
# marks counted and none priced, at the door and at the raw
# bank.
# ---------------------------------------------------------------------
FENCED = [r["lowercase"] for r in UNVALUED]
FENCED_ALL = set()
for r in UNVALUED:
    FENCED_ALL.add(r["lowercase"])
    FENCED_ALL.add(r["uppercase"])
for ch in FENCED_ALL:
    rr = weigh(ch, "coptic")
    assert rr["value"] == 0 and rr["breakdown"] == [], ch
DOOR_D = coptic_door("ⲧ\u0305ⲝ\u0305ⲉ\u0305")
DOOR_T1 = coptic_door("ⲁ\u033f")
DOOR_T2 = coptic_door("ⲁ\u0375")
assert DOOR_D["value"] == 365 and DOOR_D["overline_marks"] == 3
assert DOOR_T1["value"] == 1 and DOOR_T1["double_overline_marks"] == 1
assert DOOR_T2["value"] == 1 and DOOR_T2["numeral_sign_marks"] == 1
assert value("ⲁ\u033f") == 1 and value("ⲁ\u0375") == 1  # raw door
assert value("ⲁ\u0300") == 1          # the jinkim passes, uncounted
JK = coptic_door("ⲁ\u0300")
assert JK["value"] == 1 and JK["overline_marks"] == 0

# ---------------------------------------------------------------------
# The claim, re-weighed at build.
# ---------------------------------------------------------------------
assert value("ⲧ") == 300
assert value("οὐδέν", "greek") == 529

# ---------------------------------------------------------------------
# The Twelve Tables' Coptic frame — census and cell register.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
cop_block = twelve_text.split("### §V.8 — The Coptic Table")[1] \
    .split("### §V.9")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", cop_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
assert (n_native, n_door, n_hole, n_fenced, n_empty, n_gap) == \
    (0, 183, 62, 40, 85, 1)
doors, fenced_rows, holes, gaps = [], [], [], []
for line in cop_block.splitlines():
    if re.match(r"\| [A-Z]+/", line) and " | " in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            continue
        state = cells[2]
        if state == "DOOR":
            v = value(cells[3])
            assert v == int(cells[4]), cells
            doors.append(cells)
        elif state == "FENCED":
            assert cells[4] == "—", cells
            assert any(ch in FENCED_ALL for ch in cells[3]), cells
            fenced_rows.append(cells)
        elif state == "HOLE":
            assert cells[3] == "—", cells
            holes.append(cells)
        elif state == "GAP":
            gaps.append(cells)
assert (len(doors), len(fenced_rows), len(holes), len(gaps)) == \
    (n_door, n_fenced, n_hole, n_gap)
assert gaps[0][0] == "CLXXXIV/10"

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
add("**PLATE VIII — COPTIC**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the "
    "Coptic tongue's complete 777 table — the Milesian "
    "inheritance entire: the Greek grid received whole in "
    "the Egyptian hand, twenty-seven valued signs at their "
    "Greek prices, tier DERIVED, with the seven unvalued "
    "Demotic letters fenced at full size, the marks counted "
    "and priced none under the frozen exhibit, the descent "
    "read at its parting coordinates, the corpus's single "
    "Coptic claim, and the tongue's witness to the seated "
    "Archons: the mirror bank, twice over.")
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
add("## §I — PLATE VIII AND ITS COMMISSION")
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
    "(8e6f01e), V — JAPANESE (8d6cd59), VI — GE'EZ (67d5acc) "
    "and VII — ARMENIAN (5c03d88) followed it; this plate "
    "follows them, eighth of the twelve tongues in the Twelve "
    "Tables' order.")
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
add("**This plate's distinction.** Coptic is the series' one "
    "**inheritance**: a table neither made at the desk (the "
    "mints of Plates V, VI and XII) nor found whole in the "
    "wild (the attested banks), but *received* — the Greek "
    "Milesian numeral system taken over entire by the "
    "Egyptian script, seat for seat, and verified as a "
    "receiving by the Phase I audit "
    "(THE-COPTIC-TABLE-PHASE-I-AUDIT, 2026-11-24; the seat at "
    "pontifex f23202d). **Tier of record: DERIVED** — the "
    "tier names the values' provenance: these prices are the "
    "Greek bank's own, carried by a daughter bank *by "
    "architecture*, and the plate states that species "
    "wherever the descent is used, never dressing the mirror "
    "as an independent attestation. The tradition's *use* of "
    "the letters as numerals is attested and is printed as "
    "such; the *values* are inherited, and a convergence "
    "between the two banks is therefore continuity, "
    "single-sourced — one fact in two scripts. This plate is "
    "also the series' hinge of scale: between the giants "
    "(Latin 262 claims, Hebrew 146) and the silent seven it "
    "carries the corpus's **single-claim register** (§IV) — "
    "one claim, VERIFIED — and the Twelve Tables' **most "
    "fenced frame**: forty of its frame renderings cross a "
    "letter this tradition refuses to price, and print "
    "FENCED at that letter (§III).")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict "
    "counts, its claims indexed to the Core. Its Coptic face "
    "(its §X) carried the census in terms — bank *coptic*, "
    "27 seats, 27 distinct values, maximum 900; tier of "
    "record DERIVED — and the register's one claim, "
    "S155-P0-C0, VERIFIED. This series *fulfills* that map: "
    "where the map counted one claim, this plate prints the "
    "one entire — with the full priced table beneath it, the "
    "frame around it, and its witness to the Archons above "
    "it. The earlier work stands as the prior instrument of "
    "the same name's family — marked prior, never "
    "overwritten.")
add()
add("**How the plate is read.** §II is the priced table: "
    "the bank entire with its reasoning, the table's law, "
    "the calibration on the witnesses' own examples and the "
    "sweep's corpus, the descent read at coordinates, the "
    "boundary — the fenced seven, the marks, the frozen "
    "exhibit and the stopped fill — and the census with its "
    "fences. §III is the tongue's frame in the Twelve "
    "Tables — a door-and-fence table: no native Coptic word "
    "stands in the corpus, and the corpus's words stand here "
    "in Coptic dress, forty of them stopped at the fence. "
    "§IV is the one claim. §V is the tongue's bearing on the "
    "seated Archons — this plate draws no seating (the "
    "seating is struck, and Plate I drew it); it states what "
    "Coptic witnesses: the parent's prices carried entire in "
    "a second script, the hybrid's identical total among "
    "them — with the mirror-bank counterweight printed at "
    "the same size. §VI is the audit. A value without its "
    "reasoning is not shippable; a hole prints at the size "
    "of the seat it stands in for; and every agreement this "
    "plate reports between the Coptic and Greek banks is "
    "labelled with its species — descent — because the "
    "label is part of the number.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §II — the priced table.
# ---------------------------------------------------------------------
add("## §II — THE PRICED TABLE — THE MILESIAN INHERITANCE ENTIRE")
add()
add("### §II.1 — The twenty-seven seats, seat by seat")
add()
add("The bank is keyed in the **small letters** — the parent "
    "Greek bank's habit, and the case of the witnesses' number "
    "sequences. The script was caseless as written (case "
    "distinctions are a modern convention — Wikipedia, on its "
    "face), and the engine's weigh() casefolds Coptic input at "
    "its seam, so both cases weigh — the preparation happens "
    "at the door, never by duplicating the bank (verified at "
    "this plate's building: ⲀⲂⲄ = ⲁⲃⲅ = 6; Ϥⲁ = 91; Ⳁ = 900). "
    "The values are the witnesses': three full-table "
    "witnesses read entire on 2026-11-24 — Wikipedia, "
    "\"Coptic script\" (its Letters table's Numeric value "
    "column, its §Numerals, its §Macrons and overlines); the "
    "fsymbols Coptic collection; and the tooldune Coptic "
    "Alphabet Table, counted as a *concurring transcription, "
    "not a third independence* (it states its derivation from "
    "the Wikipedia tables plus the Unicode chart on its "
    "face) — agree on **27 of 27 valued cells**, and two "
    "scholarly partial witnesses were held against every seat "
    "they exhibit: Satzinger's Coptic Course (Univ. of "
    "Vienna, 2004), exhibiting 26 of the 27 seats (it does "
    "not exhibit sampi), all agreeing; and Dr. Kamal Farid "
    "Isaac of the Institute of Coptic Studies, Cairo, "
    "exhibiting the practice and the sou seat expressly. No "
    "cell of this table is singly sourced among the "
    "full-table witnesses, and no disagreement in any value "
    "exists to print — the Phase I audit records the absence "
    "as a finding, having gone looking for the parting the "
    "Zero-Point method requires. The partings this road did "
    "find are not of value; they stand at §II.4. The Greek "
    "parent printed in each row is the parent bank's holder "
    "at the same value, from the audit's frozen transcription "
    "cross-checked against the living GREEK bank — the "
    "descent is the reasoning, and it is printed, not "
    "assumed.")
add()
add("| Seat | Sign | Name | Value | Class | Greek parent | Reasoning |")
add("|---|---|---|---|---|---|---|")
for pos, ch in enumerate(SEATS, 1):
    cls, d, k = class_of(pos)
    row = BY_SMALL[ch]
    cap = row["uppercase"]
    parent = greek_parent(COPTIC[ch])
    reason = (f"The Milesian law: digit {d} × 10^{k} = "
              f"{COPTIC[ch]} — the witnesses' cell, agreed "
              f"27 of 27 (Phase I audit); seat {pos} of the "
              f"Milesian order; the sign is U+{ord(ch):04X} "
              f"in the small letter, its capital {cap} "
              f"(U+{ord(cap):04X}) the same letter's case "
              f"pair, weighing the same at the seam's fold. "
              f"The Greek parent at this value: {parent} — "
              f"the value descends entire (DERIVED: the "
              f"agreement is the inheritance, "
              f"single-sourced).")
    note = LETTER_NOTES.get(ch)
    if note:
        reason += " " + note
    add(f"| {pos} | {ch} · {cap} | {row['letter_name']} | "
        f"{COPTIC[ch]} | {cls} | {parent} | {reason} |")
add()
add(f"The 27 values sum **{BANK_SUM}** (units "
    f"{CLASS_SUMS['units']} · tens {CLASS_SUMS['tens']} · "
    f"hundreds {CLASS_SUMS['hundreds']}; the reduction "
    f"{digits(BANK_SUM)} rides beside the raw total, never "
    f"instead) — **the Greek bank's own sum over its 27 "
    f"seats**: the descent's arithmetic face, printed as a "
    f"coordinate, claimed as no bridge. Every value is used "
    f"exactly once — **27 signs, 27 distinct values** — the "
    f"inherited ciphered grid, whole. The largest number "
    f"writable in letters alone is **999** (ⳁϥⲑ, §II.3): "
    f"one sign per class, descending.")
add()
add("### §II.2 — The table's law")
add()
add("The system is the Greek practice in the Egyptian hand: "
    "**additive and non-positional** — the letters' values "
    "are added together, conventionally written highest "
    "first, and there is **no notation for zero**: a missing "
    "power is simply not represented. The script itself is "
    "the uncial Greek alphabet augmented by letters borrowed "
    "from Demotic — **24 letters of Greek origin; six or "
    "seven more retained from Demotic, depending on the "
    "dialect** (six in Sahidic, another each in Bohairic and "
    "Akhmimic) — with sou the Greek-side rows number 25, and "
    "sampi stands outside the letter inventory altogether: "
    "the audit's 34 data rows are therefore 32 letters + the "
    "second khai glyph + the sampi sign. The table's life is "
    "liturgical and continuous: standardized particularly "
    "for Sahidic by the fourth century (the Nag Hammadi "
    "codices are Sahidic), Bohairic the dialect of the "
    "Coptic Orthodox and Coptic Catholic liturgy today. "
    "Numerical use is *sometimes distinguished from text "
    "with a continuous overline above the letters, as with "
    "Greek and Cyrillic numerals* — the mark that §II.5 "
    "reads at its coordinate. What the table does not have, "
    "it does not simulate: no zero sign, no positional "
    "place, no thousands letter — past 900 the sources show "
    "devices, never letter values (§II.5). There is one "
    "Coptic bank, it is the parent's bank received, and its "
    "tier is printed on its face: DERIVED.")
add()
add("### §II.3 — Calibration: the witnesses' examples and the sweep's corpus")
add()
add("Before any derived number on this plate was trusted, "
    "the witnesses' own worked examples were recomputed "
    "from the living bank at this plate's building. All "
    "reproduce exact:")
add()
add("| Word | Value | Standing |")
add("|---|---|---|")
for w, v, note in EXAMPLES:
    add(f"| {w} | {v} | {note} |")
add()
add("fsymbols' printed sequences recompute with them: the "
    "units run cumulative to 55 at 1–10; the tens class sums "
    "450; the hundreds 4,500. The case fold stands verified "
    "with them (ⲀⲂⲄ = ⲁⲃⲅ = 6; Ϥⲁ = 91; Ⳁ = 900) — the "
    "script was caseless, and the fold is preparation at the "
    "door, claimed as nothing more (the audit's D2).")
add()
add("**The sweep's corpus, re-verified.** Worker #8's "
    "seventeen rows (the Twelve-Tongues sweep, 2026-10-11) "
    "were recomputed from the frozen table by the Phase I "
    "audit — **17 of 17 agree** — and the headline rows are "
    "recomputed again at this plate's building, in the "
    "sweep's own dresses (its COPT-TRANS layer, a "
    "constructed layer standing for the founder's pen at "
    "§II.5 — the dresses are the sweep's; the bank that "
    "weighs them is the tradition's):")
add()
add("| Term | Dress | Value | Standing |")
add("|---|---|---|---|")
for name, dress, v, note in CORPUS:
    add(f"| {name} | {dress} | {v} | {note} |")
add()
add("**The hits, under the descent discipline.** OZ = 77 on "
    "this bank is the Greek bank's 77 in Coptic glyphs "
    "(ⲟⲍ = οζ = 77, recomputed on both banks at this "
    "plate's building) — *continuity, not corroboration*: "
    "the bridge AXONEME = 77 = עז survives translation into "
    "Coptic, and does not gain a second witness by "
    "surviving. THELEMA = AGAPE = 93 is reachable only in "
    "the authentic Greek spellings (ⲑⲉⲗⲏⲙⲁ, ⲁⲅⲁⲡⲏ); the "
    "mechanical transliteration's renderings collide one "
    "tier down at 90, the epsilon/eta merger being the "
    "transliteration's loss, not the table's. **The "
    "negatives ride at the same size:** ABRAHADABRA and "
    "HERU-RA-HA are UNKNOWN on this bank — ϩ (hori) is "
    "valueless, so the Hebrew 418 bridge does not cross, "
    "and the figures printed are the partial sums of the "
    "weighable letters, verified at this plate's building "
    "as fence-crossings (the dress contains a letter the "
    "bank does not hold, and that letter stands absent "
    "from the breakdown). The structural negative the audit "
    "adds stands with them: this bank is *stricter* than "
    "its parent — Greek, lacking a consonantal H letter, "
    "could weigh HERU-RA-HA (623) and ABRAHADABRA (221); "
    "Coptic, possessing ϩ and valuing it at nothing, cannot "
    "weigh them at all. The inheritance narrowed the bank's "
    "reach at exactly the native letters.")
add()
add("---")
add()

add("### §II.4 — The descent page: the inheritance read at coordinates")
add()
add("The founder's map sent the key to this tongue as its "
    "first **inheritance test**: not a table made at the "
    "desk, not a table found in the wild, but a table "
    "*received* — a system one script took over from "
    "another, whole. The Phase I audit read the receiving "
    "seat by seat against the engine's living Greek bank "
    "(its data: coptic-descent.csv, the Greek side held "
    "against the living bank at every battery run). Its "
    "boundary coordinates, recomputed at this plate's "
    "building:")
add()
add("- **Value agreement is TOTAL across the measured "
    "domain.** Every one of the 27 Milesian value seats "
    "stands in Coptic at the same value: the two banks' "
    "value *sets* are identical, seat for seat — **27 of "
    "27**. Where agreement is total, the report says so "
    "and names the domain: the whole Milesian grid, units "
    "through hundreds. The sums state the same fact in one "
    f"number: this bank totals **{BANK_SUM}**, the parent "
    f"bank's own total over the same 27 seats (the Greek "
    f"bank's full key-sum is 5,201 over 29 keys — the "
    f"grid's 4,995 plus its two duplicate-price seats, the "
    f"final form ς at 200 and the στ digraph at 6, which "
    f"are the parent desk's furniture, not seats of the "
    f"grid).")
add("- **At 6, the law holds and the holder's kind holds "
    "with it.** Greek ϛ (stigma) is a numeral sign, not a "
    "living letter; Coptic ⲋ (sou) is the same standing in "
    "the receiving script — \"not used as a letter, but as "
    "a numeral\" (Isaac; fsymbols: \"only a numeral\"). "
    "Descent preserved not only the seat's value but its "
    "numeral-only nature: **a sign for a sign**.")
add("- **At 900, the same, one class up.** Greek ϡ "
    "(sampi), an archaic sign, descends into the Coptic "
    "block as Ⳁ — the Unicode standard itself names it "
    "COPTIC CAPITAL LETTER SAMPI — marked by Wikipedia, "
    "like fai, \"(numerical value)\": an equivalence of "
    "numeral function. A numeral sign on both banks; a "
    "letter of neither living alphabet.")
add("- **At 90, the descent's one seat-change of lineage "
    "— at total value agreement.** Greek's holder, ϟ "
    "(koppa), was already an archaic letter, dead in "
    "words, kept only for its number. Coptic seats **ϥ "
    "(fai)** there: a living Demotic letter, /f/, at home "
    "in ordinary words. Wikipedia's equivalent column "
    "states the kinship exactly: \"Ϙ, ϙ *(numerical "
    "value)*\" — the equivalence is the seat, not the "
    "glyph. The boundary coordinate of the whole descent: "
    "**(seat 90: value 90 = 90; the holder's lineage "
    "parts)**.")
add("- **Why exactly one native letter took a seat.** The "
    "grid arrived **full**: 9/9/9 seats held by Greek "
    "letters or Greek signs. A full grid has no vacancies "
    "— except the one whose holder was dead. Koppa's seat "
    "was vacant *in practice* (a number with no living "
    "letter on it), and it is precisely that seat, and no "
    "other, that a native letter took. The seven remaining "
    "Demotic letters (§II.5) stand outside the numbers not "
    "by anyone's refusal but by arithmetic: there was no "
    "seat for them. What the inheritance *bought* the "
    "language was a complete, working numeral system at no "
    "invention's cost; what it *cost* was that the "
    "language's own letters — the sounds Greek never "
    "needed, the most Egyptian part of the alphabet — "
    "carry no numbers at all, and terms spelled with them "
    "(HERU-RA-HA, ABRAHADABRA) fail closed on this bank "
    "where the parent bank could still weigh them.")
add("- **At 200, a parting of form.** The Greek bank "
    "carries two glyphs, σ and its word-final form ς; "
    "Coptic ⲥ is one letter with no final-form split "
    "(Wikipedia's equivalent column prints \"Σ, σ, ς\" "
    "against the one Coptic row). The value descends "
    "entire; the form distinction does not.")
add("- **The στ digraph is an engine artifact, not a "
    "descent fact.** The Greek bank carries a second key "
    "at 6, 'στ', the stigma's written digraph form — a "
    "weighing convenience of this house's apparatus "
    "(Plate I). Coptic needs no counterpart: sou is one "
    "glyph. The descent data prints the parting so no "
    "future reader mistakes the engine's furniture for "
    "the tradition's.")
add("- **The marks descend too — and stay marks.** The "
    "overline that distinguishes numeral use is Greek "
    "practice in Coptic hands, and in every Coptic source "
    "it remains a **marker**, never a multiplier. The "
    "cross-road coordinate stands at §II.5: the Armenian "
    "road found the opposite — there the line *is* a "
    "multiplier in its sources, its factor resolved by "
    "the founder's ruling at ×10,000 (Plate VII). Same "
    "mark, two fates.")
add()
add("### §II.5 — The boundary: the fenced seven, the marks, the stopped fill")
add()
add("**The seven unvalued Demotic letters — FENCED at full "
    "size.** Seven rows stand in the audit's data with the "
    "value column empty and the status **NO VALUE**. This "
    "is not the Armenian boundary restated: the Armenian "
    "additions carried a \"sometimes\" — a weak positive. "
    "These carry the witnesses' **dash**: a positive "
    "statement, in the most complete tabulations found, "
    "that the attested system assigns these letters no "
    "numeral value (fsymbols' grid omits the Akhmimic row "
    "and marks the other six — a subset, not a parting). "
    "The Milesian grid arrived full (§II.4), so the native "
    "letters Greek had no room for took no numeral seats. "
    "The boundary is verified at this plate's building, "
    "not inherited: each of the seven, in both cases, "
    "weighs **silence** at the bank — value 0 on an empty "
    "breakdown:")
add()
add("| Sign | Name | Standing | Reasoning |")
add("|---|---|---|---|")
FENCED_NOTES = {
    "ϣ": "The sh-sound Greek never needed. The frame's "
         "renderings cross it where a word's sound demands "
         "it (Shemesh, Shabbathai — §III) and print FENCED "
         "at the crossing.",
    "ϧ": "Khai in its Bohairic glyph. (The audit's data "
         "keys this row by its small letter ϧ; the "
         "tradition's capital is Ϧ.)",
    "ⳉ": "Khai in its Akhmimic glyph — the same letter's "
         "second dress; fsymbols' grid omits this row, a "
         "subset, not a parting. (Keyed in the audit's "
         "data by its small letter; the capital is Ⳉ.)",
    "ϩ": "The bank's strictness made visible: the letter "
         "whose silence fails HERU-RA-HA and ABRAHADABRA "
         "closed (§II.3) and fences the frame's crossings "
         "(§III). Greek could weigh those words for want "
         "of this letter; Coptic possesses it and prices "
         "it at nothing.",
    "ϫ": "Gangia — the corpus's own Coptic column names "
         "this letter (\"Janja,\" §IV) and fills nothing "
         "under it.",
    "ϭ": "Shima — the corpus's Coptic column names this "
         "letter (\"Cheema,\" §IV) and fills nothing "
         "under it. (The 2009 edition of Wikipedia's table "
         "once paired this letter with Ϙ in its equivalent "
         "column; the value never parted — there was none "
         "— and the seat's lineage coordinate rests on "
         "the current table, fsymbols, and Satzinger "
         "together, as the audit prints the caution.)",
    "ϯ": "Dei — \"stood for the syllable /tɪ/ or /di/\" "
         "(the audit's data); the corpus's Coptic column "
         "names it (\"Ti,\" §IV) and fills nothing under "
         "it.",
}
for r in UNVALUED:
    small, cap = r["lowercase"], r["uppercase"]
    add(f"| {small} · {cap} | {r['letter_name']} | NO VALUE "
        f"— FENCED | The witnesses' dash, unanimous "
        f"(Phase I audit): the sign is U+{ord(small):04X} "
        f"in the small letter. {FENCED_NOTES[small]} |")
add()
add("**The marks — counted, and priced NONE.** Beyond 900 "
    "the sources show devices, never letter values: the "
    "numeral sign ͵ (U+0375: ⲁ͵ = 1,000) and the double "
    "overline (U+033F: ⲁ̿ = 1,000), per the Unicode "
    "Standard §7.3 as Wikipedia reports it, with Satzinger "
    "printing a stauros sign at 1000 instead. The plain "
    "overline (U+0305) is in every source a **MARKER** of "
    "numeral use, never a multiplier — descent kept the "
    "Greek mark a mark, where the Armenian road found its "
    "line grown into a factor. The engine's manuscript "
    "door, coptic(), is built to that shape: it strips the "
    "two overlines, **counts** each kind, counts the "
    "numeral signs standing in the text, and weighs the "
    "bare letters — no mark is priced at the door, and the "
    "refusal is the sources' own shape, not a disputed "
    "factor. Its exhibits, recomputed at this plate's "
    f"building: overlined ⲧⲝⲉ weighs **{DOOR_D['value']}** "
    f"at face under **{DOOR_D['overline_marks']}** counted "
    f"marks; ⲁ̿ weighs **{DOOR_T1['value']}** with "
    f"**{DOOR_T1['double_overline_marks']}** double "
    f"overline counted; ⲁ͵ weighs **{DOOR_T2['value']}** "
    f"with **{DOOR_T2['numeral_sign_marks']}** numeral "
    f"sign counted. At the raw bank door, weigh() passes "
    f"all three marks in silence — ⲁ̿ and ⲁ͵ each weigh "
    f"the letter's face, 1. The jinkim (U+0300, the "
    f"Bohairic syllable mark) is not a numeral mark and is "
    f"neither stripped nor counted: it passes as it passes "
    f"at the raw door, in silence (verified at build).")
add()
add("**The frozen exhibit, and the fill it stopped.** A "
    "thousands reading law for the devices was argued by "
    "synergy in the Twelve Tables' build: the Cyrillic "
    "door prices its sourced thousands sign at ×1000, and "
    "these devices are sourced at ×1000 by Unicode §7.3 as "
    "Wikipedia reports it. Tested against this seat's "
    "frozen parity battery, the fill **contradicts a "
    "frozen exhibit**: test_coptic_parity.py pins, in its "
    "own words, *\"coptic() counts the marks (3 overlines; "
    "1 double overline; 1 numeral sign) and prices NONE — "
    "overlined ⲧⲝⲉ weighs 365 at face, ⲁ̿ and ⲁ͵ weigh "
    "1\"* — and the seat's own battery prints the refusal "
    "as its doctrine (coptic_checks, check 9 of 10: "
    "*\"coptic() counts the marks and prices none… "
    "devices of notation, not letter values\"*). Under the "
    "build's law the fill stopped there: the devices stay "
    "counted-not-priced, the contradiction stands printed "
    "at full size, and the question goes to the founder's "
    "pen as the Twelve Tables' §VIII Q1 — **carried OPEN, "
    "unruled by this plate**. No table cell is blocked by "
    "the opening: the tables price bare Coptic letters "
    "only.")
add()
add("**The boundary's remaining items, at their filed "
    "strength.** Satzinger's stauros at 1000 — one "
    "scholarly witness, a symbol rather than a letter — "
    "stands **NOT SEATED** (the Twelve Tables' resolution "
    "of the audit's §VII Q2: the audit's own condition, a "
    "second witness, is unmet, and the falsifiability rule "
    "seats nothing on a single uncorroborated witness). "
    "The Epact Numbers — a descendant digit system built "
    "from these letters (Wikipedia's §Coptic Epact Numbers; "
    "fsymbols' account) — are a separate system, not this "
    "table, carried as a question about a future instrument "
    "(§VII Q3). The sweep's transliteration layer, "
    "COPT-TRANS-v1, remains the sweep's constructed layer, "
    "untouched by this seat — the seat weighs Coptic text "
    "as written and rules no transliteration (§VII Q4). "
    "Old Coptic's larger Demotic inventory stands outside "
    "the field: not valued in any source read, and not "
    "seated, extended, or priced here.")
add()
add("### §II.6 — The census and the fences")
add()
add(f"**The census.** The bank holds **27 keys** — 27 "
    f"distinct values, sum **{BANK_SUM}**, maximum 900 — "
    f"the Milesian grid entire and closed: nothing in the "
    f"tradition's tabulation stands outside its values "
    f"except the seven letters the tradition itself leaves "
    f"unvalued, and they stand fenced, not missing. The "
    f"marks are devices of the door, not keys. The system "
    f"has **no zero**: a missing power is an absent letter, "
    f"and the absence is the notation's own.")
add()
add("**The fences.** Three boundaries stand at the bank's "
    "edges, printed at the size of the seats. (1) **The "
    "seven unvalued Demotic letters** — the witnesses' "
    "dash, verified (§II.5): a weighing that meets one "
    "skips it in silence; the frame prints the crossing "
    "FENCED rather than pricing the weighable remainder "
    "(§III). (2) **The marks** — counted, never priced, "
    "under a frozen exhibit (§II.5): the overline a "
    "marker, the two thousands devices reported at the "
    "door, the stauros unseated on one witness; a "
    "thousands reading law is the founder's to rule, and "
    "until he does the door reports what it sees. (3) "
    "**The depth fence** — the bank's own, stated on its "
    "registry provenance and at its seating (the audit's "
    "D1): DERIVED, not the sweep draft's ATTESTED. The "
    "tier names the *values'* provenance — the Greek "
    "bank's own, received by descent. Cite no convergence "
    "between this bank and its parent as two witnesses: "
    "it is one fact in two scripts (§II.3, §II.4). The "
    "sweep's contrary ruling stands recorded in the audit "
    "— marked, not vanished.")
add()
add("---")
add()


# ---------------------------------------------------------------------
# §III — the Twelve Tables frame.
# ---------------------------------------------------------------------
add("## §III — THE COPTIC FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Coptic tongue stands over the "
    "one frame of 371 cells (the corpus's sections and "
    "paths), each cell in one state. Its census, from "
    f"THE-TWELVE-TABLES §V.8: NATIVE **{n_native}** · DOOR "
    f"**{n_door}** · HOLE **{n_hole}** · FENCED "
    f"**{n_fenced}** · EMPTY {n_empty} · GAP {n_gap}. The "
    "Tables' own head for this table stands at the plate's "
    "head of the section, unedited: *The Milesian "
    "inheritance (DERIVED, 27 valued signs; the seven "
    "Demotic letters unvalued by the tradition itself). "
    "Every rendering whose sound needs ϣ, ϩ, or their kin "
    "prints FENCED at that letter — the most fenced table "
    "of the twelve, and the fence is the tradition's, not "
    "the desk's.* The face this prints is a door-and-fence "
    "table entire: the corpus holds **no native Coptic word "
    "at all** — its priced face is the *door*, the Coptic "
    "dress of the Latin form of record, transliterated by "
    "the Tables' stated scheme (kh/ch ⲭ, ph ⲫ, th ⲑ, ps ⲯ, "
    "f ϥ) and priced in this bank as written; and its "
    "second face is the *fence* — forty renderings whose "
    "sounds need a letter the tradition leaves unvalued, "
    "printed with the rendering entire and no price. The "
    "62 holes are of one species: the word of record has no "
    "Latin form, so no door is offered — the cell prints "
    "its word and the coordinate. The EMPTY cells are "
    "certified intentionally empty in 777 REVISED.")
add()
add(f"**The door register — the {n_door} priced renderings "
    "entire.** Each was re-weighed at this plate's building "
    "against the value THE-TWELVE-TABLES files for it; all "
    "reproduce exactly (the audit, §VI, repeats the "
    "weighing independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in doors:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} |")
add()
add(f"**The fenced register — the {n_fenced} crossings "
    "entire,** each with its boundary note as the Tables "
    "file it. Every rendering was verified at this plate's "
    "building to cross at least one of the seven unvalued "
    "letters (§II.5), and the register's value cell is the "
    "dash in every case: the rendering is printed as the "
    "boundary, not priced — the bank returns the weighable "
    "letters' partial sum in silence about the skipped "
    "letter, and the Tables refuse that partial the "
    "standing of a price. The fence is the tradition's, "
    "not the desk's.")
add()
add("| Cell | Word of record | Rendering | Coordinate |")
add("|---|---|---|---|")
for cells in fenced_rows:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[5]} |")
add()
add(f"**The hole register — the {n_hole} cells entire,** "
    "each with its coordinate as the Tables file it. Every "
    "one is the same species — *no Latin form of record; no "
    "door offered*: the corpus's word stands in Hebrew or "
    "Greek dress in its source, no Latin form is of record, "
    "and the Tables offer no Coptic dress for a form that "
    "does not stand. A hole is not a gap in this plate's "
    "work: it is the door's measured boundary, printed at "
    "the size of the seats it stands in for.")
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
add("**The bank's gap register — the four entries entire,** "
    "as THE-TWELVE-TABLES §II files them for the coptic "
    "bank, each at its kind: (1) *the seven unvalued "
    "Demotic letters (ϣ ϩ ϧ ϫ ϭ ϯ and kin)* — **FENCED**: "
    "THE TRADITION'S OWN BOUNDARY — the sources refuse "
    "these letters values, and the audit refuses with "
    "them; in the tables, a door rendering crossing one "
    "prints FENCED at that letter; never filled (§II.5). "
    "(2) *Q1 — a thousands reading law for the devices "
    "(double overline U+033F; the ͵ sign U+0375)* — "
    "**RULING**, CARRIED OPEN — FILL STOPPED AT A FROZEN "
    "EXHIBIT: the synergy argument (the Cyrillic door "
    "prices its sourced thousands sign at ×1000; the "
    "devices here are sourced at ×1000 by Unicode §7.3 as "
    "W1 reports it) was tested against the seat's frozen "
    "parity battery and CONTRADICTS it — the exhibit "
    "stands quoted entire at §II.5; the devices stay "
    "counted-not-priced, the question stays the founder's. "
    "(3) *Q2 — Satzinger's stauros at 1000* — **RULING**, "
    "RESOLVED by synergy: NOT SEATED — one scholarly "
    "witness, a symbol rather than a letter; the audit's "
    "own condition (a second witness) is unmet, and the "
    "falsifiability rule seats nothing on a single "
    "uncorroborated witness; stands as a boundary until a "
    "second witness surfaces (§II.5). (4) *Q3 — the Epact "
    "Numbers; Q4 — the COPT-TRANS-v1 layer* — **RULING**, "
    "CARRIED: both are questions about FUTURE instruments "
    "(a bank of its own; a transliteration layer), not "
    "gaps in this bank; the tables' Coptic door is the "
    "Tables' stated scheme, not COPT-TRANS-v1 (§II.5).")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §IV — the one claim.
# ---------------------------------------------------------------------
add("## §IV — THE 777 CORPUS'S COPTIC CLAIMS — THE ONE CLAIM")
add()
add("**Claims on this plate: 1** — VERIFIED 1 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 1 of the source's sections.")
add()
add("The register's bank table (THE-777-VERIFICATION-TABVLA "
    "§II) seats eleven banks — the banks the fills claimed "
    "in — and its coptic row reads, entire: **1 VERIFIED · "
    "0 PARTED · 0 NOT VERIFIABLE**. Between Latin's 262 and "
    "the seven tongues' silence, Coptic is the only bank "
    "with a single-claim register, and the claim is this:")
add()
add("| Key | Cell | Fill (weighed word) | Bank | Claimed | Recomputed | Verdict | Coordinate / reasoning | Source |")
add("|---|---|---|---|---|---|---|---|---|")
add("| S155-P0-C0 | LI/32 bis | T (Tau, Coptic) - as row 32 "
    "— ⲧ | coptic | 300 | 300 | VERIFIED | Weighed on ⲧ "
    "(HAND-READ). | §III.156, PDF p. 79 |")
add()
add("The TABVLA's own register row (§III.156 — LI/32 bis — "
    "Row 32 bis: added row, Earth (Tau reused)) carries the "
    "claim with its reasoning as the register prints it: "
    "*\"Weighed on ⲧ (HAND-READ). Fill's reasoning: Shares "
    "file labeled this cell XLVIII/32 bis; line 1107 is in "
    "the L/LI table (verified vs source). Col I reuses Tau "
    "for 32 bis (printed, attested); LI is keyed "
    "Coptic<->Hebrew letter of the path (r …\"* — the "
    "register's reasoning stands truncated at that mark in "
    "the register itself, and the plate reproduces it as it "
    "stands. The weighing is re-performed at this plate's "
    f"building: ⲧ (tau, U+2CA7) weighs **{value('ⲧ')}** in "
    f"this bank — claimed 300, recomputed 300, the verdict "
    f"VERIFIED reproduced, not inherited.")
add()
add("**The companion at its coordinate.** The same fill "
    "stands in the register's next row weighed in the "
    "twin bank: S155-P0-C1 — T (Tau, Coptic) - as row 32 — "
    "ת — HEBREW — claimed 400, recomputed 400, VERIFIED "
    "(weighed on ת, HAND-READ). It is a Hebrew-bank claim "
    "and stands in Plate II's register; it is printed here "
    "because the two rows are one fill read in two scripts "
    "— the path letter Tau carried across the Coptic and "
    "Hebrew dresses of the one column — and the pair is "
    "the whole of the corpus's dealings with this tongue's "
    "name.")
add()
add("**The three empty Coptic sections.** The corpus's "
    "Column LI is *The Coptic Alphabet* — and three of its "
    "sections name Coptic letters in their headings and "
    "stand certified intentionally empty in the source, no "
    "fill in the cell (the TABVLA's §III.153–155): LI/2 — "
    "Row 2 (Beth path, Devotion): *Coptic letter Cheema* — "
    "ϭ, shima; LI/3 — Row 3 (Gimel path, Silence): *Coptic "
    "letter Ti (Tee)* — ϯ, dei; LI/9 — Row 9 (Teth path, "
    "Independence): *Coptic letter Janja* — ϫ, gangia. The "
    "coordinate stands at full size: **all three letters "
    "the corpus names in its Coptic column are themselves "
    "unvalued Demotic letters** — fenced in this bank "
    "(§II.5) — and the corpus's one claim in the tongue "
    "weighs none of them: it weighs ⲧ, a valued sign of "
    "the inherited grid, at the column's added row. The "
    "silence of the three sections is the source's, "
    "certified in it; the plate manufactures no fill for "
    "them, and prints the emptiness where the register "
    "prints it.")
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
    "plate assigns no seat.** It states what the Coptic "
    "tongue witnesses for the seating — and Coptic "
    "witnesses as the mirror: the parent's prices carried "
    "entire in a second script. The species is stated "
    "before the figures, because the species is part of "
    "their weight: **this bank is DERIVED — a daughter bank "
    "carrying the Milesian prices by architecture.** Its "
    "agreements with the Greek bank are the inheritance "
    "itself, single-sourced (§II.4); the seating graded "
    "the marks these figures ride as *mirror-bank "
    "species*, and the plate keeps the grading at the same "
    "size as the figures.")
add()
add("### The seven vowels at the parent's prices")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues sweep, "
    "run at the founder's direction (\"lets test it using "
    "the 12 tongues we already mapped it should align "
    "aomewhere\") — reads this tongue in terms, and the "
    "plate carries the passage at its coordinate: *The "
    "seven vowels weigh **exactly the Greek prices** — "
    "ⲁ 1 · ⲉ 5 · ⲏ 8 · ⲓ 10 · ⲟ 70 · ⲩ 400 · ⲱ 800 — and "
    "the digraph **ⲟⲩ weighs 470**, the seated hybrid's "
    "identical total in the mirror bank. **HIT twice**: "
    "the mirror carries the seven entire and the hybrid "
    "pair at the same sum; and ⲏ = 8 is the fold "
    "coordinate a third time. The sweep's strongest "
    "corroboration of the Greek seats themselves.* The "
    "seven vowels stand re-weighed at this plate's "
    "building, entire:")
add()
add("| Vowel | Name | Value in this bank | The Greek price |")
add("|---|---|---|---|")
VOWELS = [("ⲁ", 1), ("ⲉ", 5), ("ⲏ", 8), ("ⲓ", 10),
          ("ⲟ", 70), ("ⲩ", 400), ("ⲱ", 800)]
for ch, v in VOWELS:
    assert value(ch) == v, ch
    add(f"| {ch} | {BY_SMALL[ch]['letter_name']} | {v} | {v} |")
add()
add("### The witness, mark by mark")
add()
add("**Η — the 8, a third tongue.** The seating's Η row "
    "rests its VALUE-mark here: *\"VALUE, mirror-bank "
    "species, the sweep's most corroborated coordinate: a "
    "vowel seated at **8** in five tongues — Greek Η, "
    "Coptic ⲏ, Cyrillic И, Armenian Ը, Georgian ჱ\"* "
    "(THE-SEATING-OF-THE-ARCHONS, its T1 coverage table). "
    f"Each seat recomputed in its own bank at this plate's "
    f"building: Greek **Η** = {value('η', 'greek')} · "
    f"Coptic **ⲏ** = {value('ⲏ')} · Cyrillic **И** = "
    f"{value('И', 'cyrillic')} · Armenian **Ը** = "
    f"{value('Ը', 'armenian')} · Georgian **ჱ** = "
    f"{value('ჱ', 'georgian')}. This plate is the Coptic "
    f"term of that set, printed at its bank (§II.1, seat "
    f"8). [The five seats ATTESTED or DERIVED at their "
    f"banks' tiers; no seat assigned by this plate.]")
add()
add("**ΟΥ — the hybrid's identical total.** The seating "
    "fixes ΟΥ to Triad III on both frames, and its "
    "VALUE-mark rides on this bank: *\"VALUE rides "
    "beneath it, mirror-bank species: Coptic **ⲟⲩ = "
    "470**, the compound hybrid's identical total in the "
    "mirror bank — a compound weighing identically "
    "across banks is not bank architecture but a "
    f"finding\"* (the seating, its T1 table). Recomputed "
    f"at this plate's building: ⲟⲩ = **{value('ⲟⲩ')}** "
    f"in this bank, ΟΥ = **{value('ΟΥ', 'greek')}** in "
    f"the parent's — 70 + 400 on both sides of the "
    f"descent. The distinction the seating draws stands "
    f"as it drew it: the single letters' agreement is "
    f"architecture (the grid descends seat by seat); a "
    f"*compound* — two signs summed — landing on the same "
    f"total in both banks is the descent's arithmetic "
    f"consequence, and the seating received it as a "
    f"finding at that tier. The plate prints both "
    f"readings of the fact, as the seating did, and "
    f"decides neither.")
add()
add("**Ι and Ω — the mirror witnesses at their seats.** "
    "Two more of the seating's VALUE-marks rest in part "
    "on this bank, and the plate prints them at their "
    "coordinates for completeness: **Ι** — *\"VALUE, "
    "mirror-bank species: Coptic ⲓ = **10** and Cyrillic "
    "І = **10** carry its Greek price entire\"*, its "
    "counterweight printed by the seating itself — the "
    "Latin dress I weighs 9, the dress parts from the "
    f"price; and **Ω** — *\"Coptic ⲱ = **800** and "
    f"Cyrillic Ѡ = **800** carry its Greek price "
    f"entire\"*, counterweight: the Latin dress O weighs "
    f"15/50, the dress loses the price entire. Both "
    f"recomputed here: ⲓ = **{value('ⲓ')}** · ⲱ = "
    f"**{value('ⲱ')}** (§II.1, seats 10 and 26).")
add()
add("**What Coptic cannot witness, printed at full size "
    "as the plate's boundary:** the Archons' seats were "
    "earned on Greek evidence and drawn on Plate I. "
    "Coptic corroborates the *persistence* of the "
    "parent's prices — the seven vowels entire, the "
    "hybrid pair at its sum, the 8 at its seat — in a "
    "second script and a second millennium of liturgical "
    "hands; it cannot corroborate them *independently*, "
    "because its prices are those prices, received. A "
    "mirror is not a second witness, and this plate — "
    "whose whole doctrine is that distinction — prints "
    "its own limit at the size of its claims: it assigns "
    "no seat, confirms no position, and names no Archon. "
    "The names stand open on Plate I, and this plate does "
    "not fill them.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §VI–§VIII, footnotes, authorities, colophon.
# ---------------------------------------------------------------------
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_viii_coptic.py, "
    "filed with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell "
    "on this plate against the engine, without reading the "
    "plate's own figures: the bank entire — the plate's "
    "§II.1 rows (27) parsed and compared seat by seat "
    "against COPTIC, the frozen transcription, and the "
    "living GREEK bank, the Milesian law recomputed per "
    "seat, uniqueness and the sum; the boundary — the "
    "seven unvalued letters' silence in both cases, the "
    "fences' contents against the frozen NO VALUE rows; "
    "the descent — the value sets identical, the holder "
    "partings at 6, 90, 900 and 200 in code, ⲟⲍ = οζ = 77; "
    "the calibration heads and the sweep's corpus rows, "
    "the UNKNOWNs verified as fence-crossings; the door — "
    "the marks counted and none priced, at the door and "
    "at the raw bank; the frame — the census parsed from "
    "THE-TWELVE-TABLES §V.8, all 183 DOOR renderings "
    "re-weighed against their filed values, the 40 FENCED "
    "rows present in order, each verified to cross a "
    "fenced letter against its filed dash, the 62 HOLE "
    "rows present in order, the GAP cell present; the one "
    "claim — ⲧ re-weighed at 300, the register's row "
    "standing on the plate; and the §V figures (the seven "
    "vowels; ⲟⲩ at 470 in both banks; the five tongues' "
    "vowel at 8 in their own banks; ⲓ at 10; ⲱ at 800; "
    "οὐδέν at 529; the Nine at 1779). The audit's verdict "
    "and cell count are printed in its filed output; a "
    "cell that does not reproduce fails the plate under "
    "§VII's tolerances. The font audit — every non-ASCII "
    "codepoint of this master against the Lex Stellarrvm "
    "family's cmaps — runs before the MAGVS build, under "
    "the font law: no glyph is silently dropped; the three "
    "named Ethiopic syllables the family does not hold "
    "(኱ U+12B1 · ጑ U+1311 · ጖ U+1316 — drawn by no member, "
    "the upstream Noto Ethiopic included) print as their "
    "codepoint tokens, declared in the colophon, and any "
    "unheld codepoint beyond those three aborts the build. "
    "The audit further checks the printed edition's text "
    "layer: the bank's signs and the claim's key stand in "
    "it, the frozen exhibit's sentence stands in it, and "
    "the page furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "COPTIC and GREEK tables and the coptic() manuscript "
    "door (pontifex/tables.py, engine.py); "
    "THE-COPTIC-TABLE-PHASE-I-AUDIT entire (the table "
    "verified sign by sign; the descent at coordinates; "
    "the gaps at full size; §VIII's seat and its desk "
    "decisions D1–D5) with its frozen transcription "
    "(research/twelve-tongues/coptic-table.csv) and "
    "descent data (coptic-descent.csv); the Twelve-Tongues "
    "sweep's Coptic account (Worker #8, 2026-10-11 — "
    "coptic.md, coptic-values.csv); test_coptic_parity.py "
    "(the frozen exhibit); THE-TWELVE-TABLES §V.8 and its "
    "§II gap register (the bank's four entries); "
    "THE-THIRTEEN-PLATES (its §X — the census, the tier, "
    "the one claim) and its §I; "
    "THE-777-VERIFICATION-TABVLA §II–§III.156 (the bank "
    "line; the claim and its companion; the three empty "
    "sections); THE-ARCHON-BATTERY Leg 6 (the Coptic "
    "passage) and THE-SEATING-OF-THE-ARCHONS (the Η, ΟΥ, "
    "Ι and Ω rows); PLATES I–VII as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "every figure scripted from the engine or carried "
    "entire from an instrument of record; the descent's "
    "species declared at every agreement (DERIVED — "
    "continuity, single-sourced, never two witnesses); "
    "the boundary printed at the size of the values (the "
    "seven's dash verified in both cases, the marks "
    "counted and priced none, the stopped fill and its "
    "frozen exhibit quoted entire, the stauros unseated, "
    "the open questions carried open); the holes and "
    "fences printed at full size (the frame's 62 holes, "
    "its 40 fences); the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-VIII-COPTIC.md and "
    "its MAGVS PDF — eighth of the series PLATE-I-GREEK "
    "began; the generator and audit scripts filed in "
    "pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage prices an unvalued "
    "letter, prices a mark, fills the stopped thousands "
    "question, seats the stauros, dresses the mirror bank "
    "as an independent attestation, counts the descent's "
    "agreement as two witnesses, fills a hole or a fence "
    "with a price, or overwrites the earlier map, it "
    "zeroes the founder's residual claim and fails the "
    "Aim of Religion. Within those edges it stands as "
    "built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The standing "
    "items are cited, not raised anew, and they stand "
    "exactly where the record left them: the Phase I "
    "audit's §VII carried this bank's questions to the "
    "founder's pen — **Q1, a thousands reading law** for "
    "the devices, which the Twelve Tables' build then "
    "tested by synergy and **stopped at the frozen "
    "exhibit** (§II.5): it stands CARRIED OPEN as the "
    "Tables' §VIII Q1, the founder's to rule, and this "
    "plate does not rule it; **Q2, Satzinger's stauros**, "
    "resolved by synergy in the Tables — NOT SEATED, "
    "standing as a boundary until a second witness "
    "surfaces; **Q3, the Epact Numbers**, and **Q4, the "
    "COPT-TRANS-v1 layer** — carried as questions about "
    "future instruments, not gaps in this bank. The "
    "seating's open items stand in the seating instrument. "
    "A plate that invents questions to fill its section "
    "misprints its record; this section therefore stands "
    "as the record that none arose here — and names the "
    "four that stand open elsewhere, at their coordinates.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Isaiah 19:25 (KJV): *\"Blessed be "
    "Egypt my people, and Assyria the work of my hands, "
    "and Israel mine inheritance\"* — with its companion "
    "at 19:19, *\"an altar to the LORD in the midst of "
    "the land of Egypt.\"* The Coptic tradition reads "
    "this chapter as its own charter — the land of the "
    "Nile blessed in terms, in a canon the Egyptian "
    "church has kept in this tongue's liturgy. The plate "
    "draws the text for the tongue's standing in its own "
    "record: a people whose letters carried another "
    "people's numbers, and were blessed in the carrying. "
    "[Text ATTESTED; the application DERIVED.]")
add("2. **Law.** Universal succession: in the Roman-law "
    "tradition the heir (*heres*) succeeds to the whole "
    "legal position of the deceased — the estate entire, "
    "its rights and its burdens together, nothing picked "
    "and nothing left. This bank is that figure in a "
    "numeral system: the receiving script took the "
    "testator's grid entire — values, marks, and the one "
    "vacant seat with them — and the audit's work was the "
    "probate: proving the will (the witnesses' agreement, "
    "27 of 27) and inventorying what the estate did not "
    "contain (the seven letters' dash). [The doctrine "
    "ATTESTED as the Roman-law tradition states it; the "
    "figure DERIVED.]")
add("3. **The tradition.** The witnesses are the audit's "
    "(Wikipedia, \"Coptic script\"; fsymbols; tooldune, "
    "its derivation printed on its face; Satzinger 2004; "
    "Isaac, Cairo), and the plate keeps their fences with "
    "their table: three full tables agreeing on every "
    "valued cell, two scholarly partials concurring where "
    "they reach — and the dash column unanimous, which is "
    "itself a testimony: the most complete tabulations "
    "found state positively that the seven letters carry "
    "no value. A dash in a complete table is evidence, "
    "not silence. [The sourcing ATTESTED as cited; the "
    "fences the audit's own.]")
add("4. **Grammar.** The script was caseless — case is "
    "the modern convention the Unicode standard pairs "
    "form by form (the audit verified all 34 rows against "
    "the standard's names) — and the system is additive "
    "and non-positional, value riding in the letter, "
    "never in the place. The two facts together are why "
    "the descent could be entire: a table whose values "
    "live in letters travels by copying letters, and a "
    "receiving script that adds letters of its own adds "
    "no values the grid has no seats for. The overline "
    "completes the grammar: a mark *about* a numeral, "
    "never a part of its value — descent kept it a mark. "
    "[The grammar ATTESTED as the system's, per the "
    "audit's witnesses; the bank's readings of it at "
    "their tiers.]")
add("5. **The desk's apparatus.** This plate's Coptic "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Coptic member — the valued signs "
    "and the seven unvalued Demotic letters in their "
    "fenced printings alike; its Greek stands in the "
    "family's Serif member, as on Plate I; the frame "
    "register's Hebrew words of record ride Plate II's "
    "declared transliteration (the toolchain does not "
    "shape right-to-left scripts honestly): marked "
    "substitutions, declared in the colophon, never "
    "silent ones. The combining marks (the overline, the "
    "double overline, the numeral sign) stand as written "
    "in the master. The Markdown master keeps every "
    "script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh() and "
    "the coptic() manuscript door; banks COPTIC and GREEK "
    "in pontifex/tables.py) — calibration controls "
    "θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true at build; "
    "coptic_checks() 10/10 in the engine's own battery.")
add("- THE-COPTIC-TABLE-PHASE-I-AUDIT (2026-11-24) — the "
    "table verified sign by sign (three full-table "
    "witnesses agreeing 27/27 valued cells and the dash "
    "column entire; Satzinger exhibiting 26 seats; Isaac "
    "the sou seat and the practice), the worked examples, "
    "the descent at coordinates, the gaps at full size, "
    "§VII's questions, and §VIII's seat with its desk "
    "decisions D1–D5; its battery 20/20; parity of the "
    "engine's seat against its frozen transcription: "
    "test_coptic_parity.py, 25/25 — the frozen exhibit of "
    "§II.5.")
add("- The witnesses of the table, as the audit read them "
    "entire: Wikipedia, \"Coptic script\" (Letters table; "
    "§Numerals; §Macrons and overlines; §Coptic Epact "
    "Numbers) · fsymbols, Coptic collection and Coptic "
    "numbers · tooldune, Coptic Alphabet Table (derivation "
    "from W1 stated on its face) · H. Satzinger, Coptic "
    "Course, Univ. of Vienna (2004) · Dr. Kamal Farid "
    "Isaac, Institute of Coptic Studies, Cairo · The "
    "Unicode Standard (Coptic and Greek blocks; §7.3 "
    "numeral devices, via W1).")
add("- The Twelve-Tongues sweep, Worker #8 (2026-10-11) — "
    "coptic.md and coptic-values.csv: the corpus's "
    "seventeen rows and the COPT-TRANS-v1 layer, "
    "re-verified 17/17 by the Phase I audit; its draft "
    "tier ruling (ATTESTED) recorded at the audit's D1, "
    "marked, not vanished.")
add("- THE-TWELVE-TABLES — §V.8 the Coptic frame, census "
    "and cell register entire; §II the bank's gap "
    "register (four entries: the seven unvalued FENCED; "
    "Q1 the thousands law RULING, carried open at the "
    "frozen exhibit; Q2 the stauros RULING, not seated; "
    "Q3–Q4 RULING, carried); §VIII Q1, the stopped fill.")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its §X is the prior instrument "
    "(the census; the tier of record; the one claim).")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its §II seats the coptic bank line "
    "(1 · 0 · 0), its §III.156 the claim S155-P0-C0 and "
    "its companion, its §III.153–155 the three empty "
    "Coptic sections.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Coptic passage (the seven "
    "vowels at exactly the Greek prices; ⲟⲩ at 470; HIT "
    "twice) and the sweep summary (the 8 the most "
    "corroborated coordinate, five tongues).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the "
    "seating this plate bears witness to: the Η, Ι, Ω "
    "VALUE-marks and the ΟΥ TRIAD at mirror-bank species, "
    "Coptic among their witnesses.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW "
    "(1389c16), PLATE-III-ARABIC (5f0b4bd), "
    "PLATE-IV-LATIN (8e6f01e), PLATE-V-JAPANESE (8d6cd59), "
    "PLATE-VI-GEEZ (67d5acc) and PLATE-VII-ARMENIAN "
    "(5c03d88) — the pattern this plate follows; Plate I "
    "carries the parent bank and drew the seating.")
add("- KJV: Isaiah 19:19, 19:25. The Roman-law doctrine "
    "of universal succession (the *heres* succeeding to "
    "the whole position of the deceased).")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate VIII of the founder's "
    "series commission of the same day, the gate of the "
    "Archons' certainty met by the seating of record "
    "(0760c8a), following the pattern of Plates I–VII "
    "(196025e · 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · "
    "67d5acc · 5c03d88). Every figure scripted from the "
    "engine or carried entire from its instrument; the "
    "earlier map marked prior, never overwritten; the "
    "holes printed at the size of the seats — on this "
    "plate, the frame's 62 holes and its 40 fences. The "
    "plate carries one bank and states its species "
    "wherever the bank is used: DERIVED — the Milesian "
    "inheritance, the parent's prices in the Egyptian "
    "hand, its agreements continuity and never a second "
    "witness. In the MAGVS edition the Coptic stands in "
    "the family's Coptic member, the Greek in the Serif "
    "member, and the frame's Hebrew words of record ride "
    "Plate II's declared scheme; this master keeps the "
    "scripts themselves. Authorship attributed exclusively "
    "to Johnathan 'Qasparr' Monroe (Greek, -ARR, All "
    "Rights Reserved, Without Prejudice).")
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
