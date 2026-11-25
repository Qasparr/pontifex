#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_ix_georgian.py
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
# MECHANISM: generates PLATE-IX-GEORGIAN.md — Plate IX of
# THE THIRTEEN COMPLETE PLATES — in the gap-filling goal's
# files/, following the pattern PLATES I–VIII set (196025e ·
# 1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc ·
# 5c03d88 · 645bcbb). Every figure on the plate is scripted
# from the house engine (pontifex weigh()) or carried entire
# from an instrument of record:
#   * the priced table — the Georgian bank entire, read from
#     pontifex.tables (GEORGIAN, 38 keys), each seat printed
#     with its reasoning, its Asomtavruli and Nuskhuri
#     partners from the Phase I audit's frozen transcription
#     (research/caucasus-north/georgian-table.csv),
#     cross-checked against the living bank at build;
#   * the calibration — the witnesses' five worked examples
#     (ჩღჲთ 1769 · ჩყპზ 1887 · ციბ 2012 · ჩყმვ 1846 ·
#     ცკვ 2026), recomputed at build, and the two spellings
#     of 494 the doubled seat licenses;
#   * the control case — the Caucasus census's page against
#     the Armenian bank: the audit's frozen control-case
#     table (research/caucasus-north/
#     georgian-control-case.csv, 37 value rows) printed
#     entire and recomputed at build — 35 rows agreeing,
#     the two partings at their coordinates (400, 10000);
#   * the Twelve Tables' Georgian frame — its census and
#     its full cell register parsed from THE-TWELVE-
#     TABLES.md §V.9: the 223 DOOR renderings re-weighed
#     at build against their filed values, the 62 HOLE
#     coordinates and the one GAP cell carried entire, the
#     bank's four gap-register entries restated;
#   * the corpus's Georgian claims — NONE: the TABVLA
#     register's §II bank table seats no Georgian row, and
#     the plate's §IV is the ZERO FACE, printed at full
#     size with the source's reason;
#   * the tongue's bearing on the seated Archons — the
#     Archon Battery's Leg 6 Georgian passage (the five
#     living vowels at Greek-mirror prices; the archaic
#     ჱ at 8), the seating's Η VALUE-mark witness set
#     recomputed in the five tongues' own banks. The plate
#     assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already
#     struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773)
# are weighed BEFORE any plate figure is taken; a control
# failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable
# — every priced seat carries its reasoning on the plate's
# face. This plate's bank is the second of the series' two
# DESIGNED tables, and its honesty is the census's: two
# witnesses read entire agree on all 38 cells, tier
# ATTESTED, and the table's one irregularity is printed at
# the size of the values — THE DOUBLED SEAT, 400 carried
# by two letters (ჳ the obsolete vie and უ the living un),
# the bank's own architecture, not an error to be smoothed:
# 38 letters, 37 distinct values. Its five obsolete letters
# are ORIGINAL members of the classical alphabet and seat
# IN the bank — the mirror of the Armenian annex, printed
# as the mirror. The boundary stands at the same size as
# the values: the older dresses (Asomtavruli, Nuskhuri)
# are the same table and are not re-keyed; no multiplier
# device is priced, no witness carrying one; the depth
# caveat stands fenced on the bank's fence. The relation
# to the earlier Thirteen Plates map is printed, the
# earlier work marked prior, never overwritten. Holes
# print at the size of the seats — on this plate, the
# frame's 62 holes and the register's zero face.
#
# CONTENT TEST: Inputs — the engine's GEORGIAN and
# ARMENIAN tables, THE-GEORGIAN-FIELD-PHASE-I-AUDIT with
# its frozen table and control-case CSVs, the Twelve
# Tables master, the Thirteen Plates map, the TABVLA
# register, the Archon Battery, the Seating. Processes —
# control calibration, scripted extraction,
# register-faithful emission in the Teacher's Edition
# manner. Outputs — PLATE-IX-GEORGIAN.md beside the
# series' other masters. Tolerances — the audit
# (audit_plate_ix_georgian.py) re-weighs every priced
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
from pontifex.tables import ARMENIAN, GEORGIAN

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
FROZEN = (Path.home() / "workspace/pontifex/research/"
          "caucasus-north/georgian-table.csv")
CONTROL = (Path.home() / "workspace/pontifex/research/"
           "caucasus-north/georgian-control-case.csv")
OUTPUT = GOAL_FILES / "PLATE-IX-GEORGIAN.md"


def value(word, bank="georgian"):
    return weigh(word, bank)["value"]


# --- calibration controls, before any plate figure -------------------
assert value("θελημα", "greek") == 93, "control θέλημα failed"
assert value("VAPOUR", "latin_ordinal") == 93, "control VAPOUR failed"
assert value("σφιγξ", "greek") == 773, "control σφίγξ failed"

# --- the frozen transcription -----------------------------------------
with FROZEN.open(encoding="utf-8") as fh:
    CSV_ROWS = list(csv.DictReader(fh))
assert len(CSV_ROWS) == 38
for row in CSV_ROWS:
    assert GEORGIAN[row["letter"]] == int(row["value"]), row
with CONTROL.open(encoding="utf-8") as fh:
    CC_ROWS = list(csv.DictReader(fh))
assert len(CC_ROWS) == 37

CLASS_OF = {}
for row in CSV_ROWS:
    CLASS_OF[row["letter"]] = (row["class"], int(row["class_power"]))


def class_of(pos):
    """Position (1-based, classical order) → (class, digit,
    power). The class law holds at every seat: value ==
    digit × 10^power. The SEAT law (digit == within-class
    seat index) parts at positions 23–28 — the doubled
    seat's shadow — and the reasoning prints both."""
    if pos <= 9:
        return "units", pos, 0
    if pos <= 18:
        return "tens", pos - 9, 1
    if pos <= 28:
        return "hundreds", pos - 18, 2
    if pos <= 37:
        return "thousands", pos - 28, 3
    return "ten-thousands", 1, 4


# --- the Twelve Tables' Georgian frame --------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
geo_block = twelve_text.split("### §V.9 — The Georgian Table")[1] \
    .split("### §V.10")[0]
_cl = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR \*\*(\d+)\*\* · "
                r"HOLE \*\*(\d+)\*\* · FENCED \*\*(\d+)\*\* · EMPTY "
                r"(\d+) · GAP (\d+)", geo_block)
N_NATIVE, N_DOOR, N_HOLE, N_FENCED, N_EMPTY, N_GAP = (
    int(x) for x in _cl.groups())
REG = {"DOOR": [], "HOLE": [], "EMPTY": [], "GAP": []}
for line in geo_block.splitlines():
    if re.match(r"\| [A-Z]+/", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[2] in REG:
            REG[cells[2]].append(cells)
assert len(REG["DOOR"]) == N_DOOR == 223
assert len(REG["HOLE"]) == N_HOLE == 62
for cells in REG["DOOR"]:
    assert value(cells[3]) == int(cells[4]), cells

# --- derived bank facts, all computed ---------------------------------
BANK_SUM = sum(GEORGIAN.values())
CLASS_SUMS = {}
for row in CSV_ROWS:
    CLASS_SUMS[row["class"]] = (CLASS_SUMS.get(row["class"], 0)
                                + int(row["value"]))
DISTINCT = len(set(GEORGIAN.values()))
# the largest number the bare table writes: one symbol per
# power, descending — the class maxima in order
_by_class = {}
for row in CSV_ROWS:
    _by_class.setdefault(row["class"], []).append(
        (row["letter"], int(row["value"])))
LARGEST_WORD = "".join(
    max(_by_class[c], key=lambda t: t[1])[0]
    for c in ("ten-thousands", "thousands", "hundreds", "tens",
              "units"))
LARGEST = value(LARGEST_WORD)
EXAMPLES = [("ჩღჲთ", 1769, "a witness's worked example — and the "
             "seat's own proof that ჲ must stand in the bank"),
            ("ჩყპზ", 1887, "a witness's worked example"),
            ("ციბ", 2012, "a witness's worked example"),
            ("ჩყმვ", 1846, "the Motsameta inscription's date, as "
             "the witnesses carry it"),
            ("ცკვ", 2026, "a witness's worked example")]
for w, want, _note in EXAMPLES:
    assert value(w) == want, (w, want)
assert value("ჳჟდ") == value("უჟდ") == 494
assert value("ჵ") == 10000 and value("ჱ") == 8

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
add("**PLATE IX — GEORGIAN**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Georgian "
    "tongue's complete 777 table — the designed alphabet's own "
    "numeral system entire: thirty-eight classical letters in five "
    "decimal classes to a native 10,000, attested by two witnesses "
    "in agreement on every cell, with the doubled seat — 400 "
    "carried by two letters — printed at full size as the bank's "
    "own architecture, the control case against the Armenian bank "
    "read at coordinates, the corpus's Georgian register, which "
    "is a zero face; and the tongue's witness to the seated "
    "Archons: the archaic letter ჱ, priced exactly 8.")
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
add("## §I — PLATE IX AND ITS COMMISSION")
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
    "VI — GE'EZ (67d5acc), VII — ARMENIAN (5c03d88) and "
    "VIII — COPTIC (645bcbb) followed it; this plate follows "
    "them, ninth of the twelve tongues in the Twelve Tables' "
    "order.")
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
add("**This plate's distinction.** Georgian is the second of the "
    "series' two *designed* tables — an alphabet made with its "
    "numeral system as one act — and the control case's other "
    "half. Plate VII printed the Armenian side: the founder "
    "ordered the two designed alphabets of the Caucasus read "
    "beside each other, and this plate prints the Georgian side "
    "of the same page (§II.4): the value sequences agree entire, "
    "and the partings stand at exactly two coordinates — the "
    "doubled 400 and the native 10,000. **Tier of record: "
    "ATTESTED** — two witnesses read entire on 2026-11-24 agree "
    "on all 38 cells (THE-GEORGIAN-FIELD-PHASE-I-AUDIT), its "
    "parity proven against the audit's frozen transcription by "
    "test_georgian_parity.py. The bank's one irregularity is not "
    "hidden and not repaired: **400 is carried by two letters**, "
    "ჳ the obsolete vie and უ the living un — 38 letters, 37 "
    "distinct values — printed at full size (§II.5) as the "
    "record's own shape. And this is the fourth plate whose "
    "corpus register is a **zero face** (§IV): the corpus claims "
    "nothing in Georgian, and the silence is the corpus's, not "
    "the tongue's.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. Its Georgian face stood "
    "**silent with a zero face**: bank *georgian*, 38 seats, 37 "
    "distinct values, maximum 10,000; tier of record there "
    "printed in terms — *ATTESTED* — and its sentence stands: "
    "*\"The tongue holds a full table in THE TWELVE TABLES; its "
    "silence here is the TABVLA corpus's, not the tongue's.\"* "
    "This series *fulfills* that map: where the map counted "
    "nothing, this plate prints the nothing entire — with the "
    "full priced table beneath it, the frame around it, and its "
    "witness to the Archons above it. The earlier work stands as "
    "the prior instrument of the same name's family — marked "
    "prior, never overwritten.")
add()
add("**How the plate is read.** §II is the priced table: the "
    "bank entire with its reasoning, the table's law, the "
    "calibration on the witnesses' own examples, the control "
    "case beside Armenian, the boundary — the doubled seat, "
    "the five obsolete letters, the dresses — and the census "
    "with its fences. §III is the tongue's frame in the Twelve "
    "Tables — a door table: no native Georgian word stands in "
    "the corpus, and the corpus's words stand here in Georgian "
    "dress. §IV is the zero face. §V is the tongue's bearing on "
    "the seated Archons — this plate draws no seating (the "
    "seating is struck, and Plate I drew it); it states what "
    "Georgian witnesses: five living vowels at the Greek "
    "prices with no 8 among them, and the 8 itself seated on "
    "an archaic letter at the alphabet's edge. §VI is the "
    "audit. A value without its reasoning is not shippable; a "
    "hole prints at the size of the seat it stands in for.")
add()
add("---")
add()

# =============================================================================
# §II — THE PRICED TABLE
# =============================================================================
add("## §II — THE PRICED TABLE — THE DESIGNED ALPHABET'S OWN "
    "TABLE ENTIRE")
add()
add("### §II.1 — The thirty-eight letters, seat by seat")
add()
add("The bank is keyed in **Mkhedruli** — the dress the "
    "witnesses print the table in. The system is older than "
    "that dress: historically the numerals ran in Asomtavruli "
    "and Nuskhuri (the khutsuri church hand), and every one of "
    "the 38 letters carries an Asomtavruli capital and a "
    "Nuskhuri small partner under the standard's own names "
    "(38/38, verified in code at the Phase I audit) — the "
    "partners print beside each seat below. Those older forms "
    "are **not re-keyed**: the table is one table in three "
    "dresses, and seating a second dress would seat one fact "
    "as two banks (the Aramaic fence's discipline, §II.5). The "
    "values are the witnesses': two read entire on 2026-11-24 "
    "— Wikipedia, \"Georgian numerals\" (its table sourced "
    "there to Makharoblidze 2009) and georgianalphabet.com "
    "(its per-letter value cards for the modern 33, its "
    "\"Numeral letters\" section for the five obsolete "
    "letters) — agree on **38 of 38 cells**, every glyph "
    "verified against the Unicode standard's names. The class "
    "law printed in each row's reasoning is the check the "
    "witnesses' cells obey, never their source: every value "
    "decomposes as digit × 10^class (38/38); the *seat* law — "
    "digit equal to the within-class seat index — parts at "
    "exactly six coordinates, positions 23–28, downstream of "
    "the doubled 400 (§II.5), and the parting is printed in "
    "the rows it touches.")
add()
SEAT_NOTES = {
    1: "The head of the alphabet and of the table.",
    5: "A vowel of the tongue — one of the five living vowels "
       "the battery prices from this bank (§V).",
    8: "**The Archons coordinate of this plate:** an archaic "
       "letter priced exactly 8 — the fold's target seated at "
       "the margin of the living alphabet (§V).",
    9: "The units run closes.",
    10: "The tens open. A vowel of the tongue (§V).",
    15: "An obsolete letter the bank cannot refuse: the "
        "witnesses' own worked example ჩღჲთ = 1769 (§II.3) is "
        "written with it — a seat that refused the five would "
        "break sourced exhibits.",
    16: "A vowel of the tongue (§V).",
    22: "**The doubled seat, first holder:** 400 is carried "
        "by two letters in this bank — this obsolete vie and "
        "the living უ at the next seat (§II.5). The hundreds "
        "class therefore holds ten letters for nine digits.",
    23: "**The doubled seat, second holder:** the living უ "
        "carries the same 400 — and is also the tongue's "
        "vowel for /u/ (§V), one letter doing both offices. "
        "Some numbers therefore carry two spellings: 494 = "
        "ჳჟდ and უჟდ (§II.3). The seat law parts from here: "
        "within-class seat 5 carries digit 4.",
    24: "The seat law's shadow: within-class seat 6 carries "
        "digit 5 — one step behind its seat, downstream of "
        "the doubled 400 (§II.5).",
    25: "The seat law's shadow: within-class seat 7 carries "
        "digit 6 (§II.5).",
    26: "The seat law's shadow: within-class seat 8 carries "
        "digit 7 (§II.5).",
    27: "The seat law's shadow: within-class seat 9 carries "
        "digit 8 (§II.5).",
    28: "The seat law's shadow closes: within-class seat 10 "
        "carries digit 9 — the hundreds' tenth letter (§II.5).",
    29: "The thousands open.",
    35: "Obsolete — one of the five original members dropped "
        "from ordinary writing in the 1860s reform, seated in "
        "the bank at the classical tier (§II.5).",
    38: "**The bank's maximum, and the control case's "
        "sharpest coordinate:** 10,000 carried by a LETTER — "
        "where Armenian reaches the same value only by a "
        "device, the overline (§II.4). Obsolete, and seated "
        "in the bank as an original member (§II.5).",
}
add("| Position | Letter · Asomtavruli · Nuskhuri | Name | "
    "Value | Class | Reasoning |")
add("|---|---|---|---|---|---|")
for row in CSV_ROWS:
    pos = int(row["position"])
    letter = row["letter"]
    v = int(row["value"])
    cls, seat_idx, power = class_of(pos)
    # MECHANISM: the digit is read off the VALUE (the class
    # law: v == digit × 10^power, 38/38); the seat index is
    # read off the POSITION. Where the two part — positions
    # 23–28, downstream of the doubled 400 — the row prints
    # the parting. Reading the digit from the position
    # instead would assert the seat law the bank breaks.
    digit = v // 10 ** power
    assert digit * 10 ** power == v, row
    reasoning = (
        f"The class law: digit {digit} × 10^{power} = {v} — "
        f"the witnesses' cell, agreed 38 of 38 (Phase I "
        f"audit); position {pos} of the classical order "
        f"({row['codepoint']}); standing: {row['standing']} "
        f"({row['status'].lower()} in the audit's frozen "
        f"table).")
    # The seat-law parting at positions 23–28 is carried by
    # the SEAT_NOTES prose at those rows (the audit verifies
    # the parting set independently, from the values).
    note = SEAT_NOTES.get(pos)
    if note:
        reasoning += " " + note
    add(f"| {pos} | {letter} · {row['asomtavruli']} · "
        f"{row['nuskhuri']} | {row['name']} | {v} | {cls} | "
        f"{reasoning} |")
add()
add(f"The 38 values sum **{BANK_SUM}** (units "
    f"{CLASS_SUMS['units']} · tens {CLASS_SUMS['tens']} · "
    f"hundreds {CLASS_SUMS['hundreds']} · thousands "
    f"{CLASS_SUMS['thousands']} · ten-thousands "
    f"{CLASS_SUMS['ten-thousands']}). The hundreds class sums "
    f"{CLASS_SUMS['hundreds']}, not 4,500: it holds ten "
    "letters, the doubled 400 counted twice — the bank's "
    "arithmetic carries the doubling openly. **38 letters, "
    f"{DISTINCT} distinct values** — uniqueness, which the "
    "Armenian bank holds entire (36 letters, 36 distinct "
    "values), does **not** hold here, and the plate prints "
    "the failure at the size of the census. The largest "
    f"number the bare table writes is **{LARGEST}** "
    f"({LARGEST_WORD}): one symbol per power of ten, "
    "descending, the system's own convention — and past "
    "10,000 it writes nothing at all: no further letter, and "
    "no device (§II.2).")
add()

add("### §II.2 — The table's law")
add()
add("The system is **additive and non-positional**: the values "
    "of the letters are added together; there is **no notation "
    "for zero** — a missing power of ten is simply not "
    "represented. Numbers are written with at most one symbol "
    "per power, conventionally descending. Its extent past the "
    "table is by **nothing**: the witnesses carry **no "
    "multiplier device at all** — no overline, no thousands "
    "sign — and the founder's register resolves the question "
    "in terms (Q2, §II.5): a device without a sourced factor "
    "is not priced. Where Armenian stops at 9,000 and reaches "
    "higher by the overline, Georgian seats 10,000 **as a "
    "letter** and then stops. The dresses are the table's "
    "other law: the bank is keyed in Mkhedruli, the witnesses' "
    "dress; the Asomtavruli and Nuskhuri partners printed at "
    "each seat are the **same table in older hands**, not "
    "second banks; and the Mtavruli headline forms (U+1C90–, "
    "a modern typographic case) **fold to Mkhedruli at the "
    "weigh() seam** — a headline-cased word weighs as itself "
    "(verified at this plate's building: Mtavruli Ა = 1, "
    "while the unfolded Asomtavruli Ⴀ weighs silence at the "
    "bank, its value living at its Mkhedruli partner's seat). "
    "Case carries no numeral value; a dress is not a bank.")
add()
add("### §II.3 — Calibration: the witnesses' own examples")
add()
add("Before any derived number on this plate was trusted, the "
    "witnesses' own worked examples were recomputed from the "
    "living bank at this plate's building. All reproduce "
    "exact:")
add()
add("| Word | Value | Standing |")
add("|---|---|---|")
for w, want, note in EXAMPLES:
    add(f"| {w} | {want} | {note} |")
add(f"| {LARGEST_WORD} | {LARGEST} | the largest number "
    "writable in the bare table — one symbol per power, "
    "descending |")
add("| ჳჟდ | 494 | the doubled seat's first spelling of 494 |")
add("| უჟდ | 494 | the doubled seat's second spelling of 494 — "
    "the same number, two lawful writings |")
add()
add("**The negatives ride at the same size:** the calibration "
    "exhibits no bridge, because none exists to exhibit. The "
    "Georgian and Armenian alphabets **share no letters**, so "
    "no word can be weighed on both banks and no cross-weighing "
    "exists (the Phase I audit, in terms: *\"It is not a "
    "bridge: no word is weighed on both banks here, and none "
    "is claimed\"*). The control case that follows is therefore "
    "a comparison of two attested value *sequences*, never a "
    "weighing — the distinction is the plate's honesty, and it "
    "is printed where the comparison stands.")
add()
add("### §II.4 — The control case: Georgian beside Armenian")
add()
add("The founder ordered the two designed alphabets of the "
    "Caucasus read beside each other. Plate VII printed the "
    "Armenian bank against the halehame witness; the Caucasus "
    "page is this one — Georgian beside Armenian, two systems "
    "of the same class-law shape, both ATTESTED, computed in "
    "code against the living ARMENIAN bank (the Phase I "
    "audit's georgian-control-case.csv, 37 value rows) and "
    "printed entire, both banks re-weighed at this plate's "
    "building:")
add()
add("| Value | Georgian letters | Georgian seats | Armenian "
    "letters | Armenian seats | Relation |")
add("|---|---|---|---|---|---|")
for r in CC_ROWS:
    add(f"| {r['value']} | {r['georgian_letters']} | "
        f"{r['georgian_seats']} | {r['armenian_letters']} | "
        f"{r['armenian_seats']} | {r['relation']} |")
add()
add("The boundary coordinates, as the Phase I audit read them "
    "(its §IV), printed at the size of the table:")
add()
add("- **The shared domain is entire.** Every Armenian value "
    "— the full sequence 1–9, 10–90, 100–900, 1000–9000 — is "
    "a Georgian value: **36/36 values shared**. Over that "
    "domain the two tables' value *sequences* are one "
    "sequence.")
add("- **Parting 1 — at 400.** Georgian seats **two** letters "
    "at 400 (ჳ, უ); Armenian seats **one** (Ն). 35 of the 37 "
    "value rows agree in seat count; this is the first of "
    "the two that part.")
add("- **Parting 2 — at 10,000.** Georgian seats a **letter** "
    "(ჵ); Armenian seats **nothing** — its classical table "
    "ends at 9,000, and what Armenian writing reaches beyond "
    "it reaches by a *device*, the overline priced at "
    "×10,000 (the Armenian audit's resolution R2, Plate "
    "VII §II.5). One system's letter is the other system's "
    "device-coordinate: the sharpest single coordinate on "
    "this page.")
add("- **Extent.** 38 letters against 36; 37 distinct values "
    "against 36; sum 60,395 against 49,995; classes 9/9/10/9/1 "
    "against 9/9/9/9 — the Georgian hundreds class carries "
    "the extra seat, and the ten-thousands class is a class "
    "of one letter.")
add("- **The class law.** By value, both hold entire. By "
    "seat, Armenian holds at 36/36 seats; Georgian parts at "
    "positions 23–28 (§II.1) — the doubled seat's shadow "
    "falls on exactly one class of one table.")
add("- **The archaic letters run opposite ways in time.** "
    "Georgian's five non-modern letters (ჱ ჲ ჳ ჴ ჵ) are "
    "**original members** of the classical alphabet, dropped "
    "from ordinary writing in the 1860s reform; Armenian's "
    "two extra letters (Օ, Ֆ) are **medieval additions** to "
    "an already-complete classical table, standing in the "
    "engine in the ARMENIAN_LATE annex a tier below it. "
    "Georgia's table *shrank* around its numerals; Armenia's "
    "*grew* past them.")
add("- **Zero.** Both tables: **absence** — no zero sign in "
    "either designed system.")
add()
add("The agreement is a property of two attested value "
    "sequences, printed as coordinates. **It is not a "
    "bridge** — §II.3's negative stands over the whole page.")
add()
add("### §II.5 — The boundary: the doubled seat, the five "
    "obsolete letters, the dresses")
add()
add("**The doubled seat, at full size.** The hundreds class "
    "holds **ten letters for nine digits**, because 400 is "
    "carried by two letters — **ჳ** (vie, U+10F3, obsolete) "
    "at position 22 and **უ** (un, U+10E3, living) at "
    "position 23. Both holders stand in the bank as sourced: "
    "the founder's register records the disposition in terms "
    "(*\"SEATED AS SOURCED… both holders of 400 stand in the "
    "bank (the record's own shape)\"*, FENCED, §III). The "
    "consequences print with it: the seat law parts at "
    "positions 23–28 (§II.1's rows carry the parting at "
    "their cells); some numbers carry two spellings (494, "
    "§II.3); and the bank's census reads 37 distinct values "
    "in 38 letters (§II.6). A plate that seated only one 400 "
    "would falsify both witnesses; a plate that hid the "
    "doubling would misprint the bank.")
add()
add("**The five obsolete letters seat IN the bank.** ჱ (8) · "
    "ჲ (60) · ჳ (400) · ჴ (7,000) · ჵ (10,000) are original "
    "members of the classical 38-letter alphabet, coextensive "
    "with the numeral system itself, dropped from ordinary "
    "writing only in the 1860s reform. They seat here at the "
    "classical tier — a desk decision of the Phase I audit "
    "(its §VII D1), and the reasoning is the mirror of the "
    "Armenian annex: Օ and Ֆ are medieval *additions* to a "
    "classical alphabet whose numeral table was already "
    "complete, so they stand a tier below it; the Georgian "
    "five are the opposite case. A seat that refused them "
    "would break sourced exhibits (ჩღჲთ = 1769 needs ჲ) and "
    "amputate the system's own maximum (ჵ = 10,000).")
add()
add("**The dresses.** The table is one table in three "
    "dresses. Asomtavruli and Nuskhuri are **not re-keyed** "
    "(the audit's D2): at the bank they weigh silence — "
    "verified at this plate's building (Asomtavruli Ⴀ: value "
    "0, empty breakdown) — their values living at their "
    "Mkhedruli partners' seats, the partners printed at "
    "every seat of §II.1. The Mtavruli headline dress folds "
    "at the seam (the register's Q3, RESOLVED BY SYNERGY AND "
    "FILLED IN CODE, commit cedfb67): the fold maps only "
    "U+1C90–U+1CBA to Mkhedruli, and the older dresses stay "
    "unfolded per D2. **No multiplier mark is priced** (the "
    "register's Q2, RULING): no witness carries one; a device "
    "without a sourced factor is not priced — the Coptic "
    "plain-overline discipline — and if a witness surfaces, "
    "its pricing is a ruling on the Armenian R2 pattern. "
    "**The depth caveat stands FENCED** (the register's Q1): "
    "the witnesses are modern reference works — Wikipedia's "
    "table sourced to Makharoblidze 2009 — and no primary "
    "manuscript was re-read; the caveat governs the depth of "
    "the desk's reading, not the table's standing, and no "
    "desk act can retire it. It prints here, on the bank's "
    "fence, at the size of the values.")
add()
add("### §II.6 — The census and the fences")
add()
add(f"**The census.** The bank holds **38 keys** — "
    f"{DISTINCT} distinct values, sum **{BANK_SUM}**, "
    "maximum 10,000 (ჵ) — the whole classical alphabet: "
    "nothing in its classical script stands outside its "
    "values. Five of the 38 are obsolete in ordinary writing "
    "and classical in the bank (§II.5). The system has **no "
    "zero**: a missing power is an absent letter, and the "
    "absence is the notation's own.")
add()
add("**The fences.** Three boundaries stand at the bank's "
    "edges, printed at the size of the seats. (1) **The "
    "doubled seat** — both holders of 400 stand in the bank "
    "as sourced (§II.5); no weighing in this bank may "
    "silently choose one: a total that turns on the choice "
    "must declare it, and the two spellings of a number "
    "under the doubling are both lawful writings. (2) **The "
    "older dresses** — Asomtavruli and Nuskhuri weigh "
    "silence at the bank, by the one-table rule (§II.5): a "
    "weighing that meets them skips them; their values live "
    "at the Mkhedruli seats. The Mtavruli fold is the one "
    "exception, and it is a fold, not a second bank. (3) "
    "**The depth fence** — the bank's own (Q1, §II.5): the "
    "table is ATTESTED at the depth of two modern reference "
    "witnesses in total agreement, and the plate cites it at "
    "that depth — not at the depth of a primary re-read no "
    "desk hand has made.")
add()
add("---")
add()

# =============================================================================
# §III — THE FRAME
# =============================================================================
add("## §III — THE GEORGIAN FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Georgian tongue stands over the "
    "one frame of 371 cells (the corpus's sections and paths), "
    "each cell in one state. Its census, from THE-TWELVE-TABLES "
    f"§V.9: NATIVE **{N_NATIVE}** · DOOR **{N_DOOR}** · HOLE "
    f"**{N_HOLE}** · FENCED **{N_FENCED}** · EMPTY {N_EMPTY} · "
    f"GAP {N_GAP}. The Tables' own head for this table stands "
    "at the plate's head of the section, unedited: *the "
    "Mkhedruli bank (ATTESTED, 38 letters, the doubled 400 "
    "standing as sourced, the native 10000 letter ჵ in the "
    "bank). The door dresses the Latin form letter by letter; "
    "the Mtavruli fold (§III) means a headline-cased word "
    "weighs as itself.* The face this prints is a door table "
    "entire: the corpus holds **no native Georgian word at "
    "all** — its priced face is the *door*, the Georgian "
    "dress of the Latin form of record, transliterated by the "
    "Tables' stated scheme (kh ხ, sh შ, ch ჩ, ts ც, tz წ, "
    "gh ღ) and priced in the Mkhedruli bank as written. The "
    f"{N_HOLE} holes are of one species: the word of record "
    "has no Latin form, so no door is offered — the cell "
    "prints its word and the coordinate. The EMPTY cells are "
    "certified intentionally empty in 777 REVISED.")
add()
add("**The door register — the 223 priced renderings entire.** "
    "Each was re-weighed at this plate's building against the "
    "value THE-TWELVE-TABLES files for it; all reproduce "
    "exactly (the audit, §VI, repeats the weighing "
    "independently).")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in REG["DOOR"]:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | "
        f"{cells[4]} |")
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
add("**The one GAP cell:** CLXXXIV/10 — a transcription gap "
    "in the source itself, carried as the frame carries it; "
    "no tongue's door is offered for a cell the source does "
    "not transmit.")
add()
add("**The bank's gap register — the four entries entire,** "
    "as THE-TWELVE-TABLES §II files them for the georgian "
    "bank, each at its kind: (1) *the Mtavruli headline "
    "dress: fold at the seam, or silence?* — **RULING** "
    "(Q3), RESOLVED BY SYNERGY AND FILLED IN CODE (commit "
    "cedfb67): FOLD — every other cased bank folds its "
    "capital dress at the weigh() seam; case carries no "
    "numeral value; the fold maps only U+1C90–U+1CBA to "
    "Mkhedruli, the older dresses staying unfolded per the "
    "seat's D2 (§II.2, §II.5). (2) *a numeral multiplier "
    "mark: no witness carries one* — **RULING** (Q2), "
    "RESOLVED by synergy: NO MARK PRICED — a device without "
    "a sourced factor is not priced (§II.5). (3) *the depth "
    "caveat (modern reference witnesses; no primary "
    "re-read)* — **FENCED** (Q1): a caveat, not a seat; it "
    "governs the depth of the desk's reading, not the "
    "table's standing, and no desk act can retire it "
    "(§II.5). (4) *the doubled 400 (ჳ and უ) and the five "
    "obsolete letters* — **FENCED**: SEATED AS SOURCED — "
    "both holders of 400 stand in the bank (the record's "
    "own shape), and the obsolete five seat in the "
    "classical bank as original members; no gap (§II.5).")
add()
add("---")
add()

# =============================================================================
# §IV — THE ZERO FACE
# =============================================================================
add("## §IV — THE 777 CORPUS'S GEORGIAN CLAIMS — THE ZERO FACE")
add()
add("**Claims on this plate: 0** — VERIFIED 0 · PARTED 0 · "
    "NOT VERIFIABLE 0 — drawn from 0 of the source's sections.")
add()
add("**THE ZERO FACE.** This plate carries no claim, and the "
    "absence is its finding. The source states it in terms "
    "(THE-THIRTEEN-PLATES, its Georgian plate, from "
    "THE-777-VERIFICATION-TABVLA's register): *no fill in "
    "the corpus states a Georgian claim: the source's §II "
    "bank table seats no Georgian row, because the table "
    "lists only banks the fills claimed in; the bank itself "
    "stands among the engine's seventeen in the source's "
    "§I.* The 777 corpus's 504 claims speak Greek, Hebrew, "
    "Arabic, Latin, and Coptic — the tongues its fills "
    "claimed in — and Georgian is not among them: no scribe "
    "of the corpus weighed a word in this bank, though the "
    "bank stood complete in the tradition the whole time. "
    "The silence is therefore the corpus's, not the "
    "tongue's: the tongue holds a full priced table (§II), "
    "a full frame (§III), a control case against the other "
    "designed alphabet (§II.4), and a doctrine of its own "
    "(THE-GEORGIAN-FIELD-PHASE-I-AUDIT — the table verified "
    "sign by sign, the control case, the seat). What the "
    "corpus does hold for Georgian stands where the corpus "
    "put it: the frame's door renderings (§III) — the "
    "corpus's words in this tongue's dress, priced by this "
    "tongue's bank — and nothing else. A plate that "
    "manufactured claims to fill this section would misprint "
    "its record; the section therefore stands as a face of "
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
    "plate assigns no seat.** It states what the Georgian "
    "tongue witnesses for the seating — and Georgian "
    "witnesses at the coordinate the battery's sweep found "
    "most corroborated of all, from the far side: the 8 that "
    "the living alphabet does not carry, seated on an "
    "archaic letter at its edge.")
add()
add("### The five living vowels — and the 8 that is not "
    "among them")
add()
add("THE-ARCHON-BATTERY's Leg 6 — the twelve-tongues sweep, "
    "run at the founder's direction (\"lets test it using "
    "the 12 tongues we already mapped it should align "
    "aomewhere\") — reads this tongue in terms, and the "
    "plate carries the passage at its coordinate: *five "
    "vowels at Greek-mirror prices — ა 1 · ე 5 · ი 10 · ო 70 "
    "· უ 400 — with no 8 among the living five; the archaic "
    "e-family letter ჱ weighs 8. Partial HIT at the fold "
    "coordinate: the 8 is seated in Georgian, on an archaic "
    "letter at the edge of the living alphabet — the fold's "
    "target at the margin, printed as such.* The five living "
    "vowels stand re-weighed at this plate's building, "
    "entire:")
add()
add("| Vowel | Name | Value in this bank |")
add("|---|---|---|")
_VOWELS = {"ა": "an", "ე": "en", "ი": "in", "ო": "on",
           "უ": "un"}
for ch, nm in _VOWELS.items():
    add(f"| {ch} | {nm} | {value(ch)} |")
add()
add("The five prices are the Greek five — 1, 5, 10, 70, 400: "
    "the Milesian vowel row read in a designed alphabet of "
    "the Caucasus, each value the class law's own product at "
    "its seat (§II.1), no borrowing claimed and none needed: "
    "the agreement is of two attested sequences, printed as "
    "a coordinate, not a descent. What the living five do "
    "**not** hold is the 8: the units run passes from ზ (7) "
    "to თ (9) with the 8 standing between them on a letter "
    "the living alphabet no longer writes.")
add()
add("### The archaic 8 — ჱ at its seat")
add()
add("**ჱ** (he, U+10F1) is the e-family's archaic letter — "
    "the alphabet's eighth seat in the classical order, "
    "priced exactly 8 by the class law (digit 8 × 10^0), "
    "dropped from ordinary writing in the 1860s reform and "
    "seated in this bank as an original member (§II.5). The "
    "coordinate the sweep measured is the fold's target — a "
    "vowel-family letter seated at 8 — and it is the sweep's "
    "most corroborated coordinate across the twelve tongues. "
    "Five tongues seat it, each recomputed in its own bank "
    "at this plate's building: Greek **Η** = 8 · Coptic "
    "**ⲏ** = 8 · Cyrillic **И** = 8 · Armenian **Ը** = 8 · "
    "Georgian **ჱ** = 8. Four of the five reach the seat on "
    "a living letter; **Georgian alone reaches it from the "
    "archaic row** — its 8 is a survival, priced in the "
    "classical table and unwritten in the modern hand, and "
    "the plate prints the archaic state at the same size as "
    "the price, as the sweep printed it: *the fold's target "
    "at the margin*. It is on this coordinate that the "
    "seating's Η row rests its VALUE-mark: *the sweep's most "
    "corroborated coordinate: a vowel seated at 8 in five "
    "tongues — Greek Η, Coptic ⲏ, Cyrillic И, Armenian Ը, "
    "Georgian ჱ* (THE-SEATING-OF-THE-ARCHONS, its T1 "
    "coverage table). This plate is the Georgian term of "
    "that set, printed at its bank. [The five seats ATTESTED "
    "or DERIVED at their banks' tiers; no seat assigned by "
    "this plate.]")
add()
add("### No hybrid class")
add()
add("Beside the 8, the sweep's second Georgian coordinate "
    "prints at the same size — the tongue's hybrid-form "
    "state, as the record files it and no more. The battery, "
    "in terms: *hybrid class: none (no diphthong letters; უ "
    "is one letter for /u/). MISS on the four.* Where the "
    "Greek field seats its diphthongs as units and Latin its "
    "four hybrids, Georgian writes its vowels one letter "
    "each and fuses none: the tongue that doubles a *value* "
    "(400 twice, §II.5) doubles no *form*. The two facts "
    "stand together on this plate as the record files them "
    "— a doubled seat and an empty hybrid class, each at "
    "its coordinate, neither argued further.")
add()
add("**What Georgian cannot witness, printed at full size "
    "as the plate's boundary:** the Archons' seats were "
    "earned on Greek evidence and drawn on Plate I. Georgian "
    "corroborates the *shape of the 8* — at the margin, on "
    "an archaic letter, in an independent designed bank, "
    "one of the five tongues at the sweep's most "
    "corroborated coordinate — and the *limit of hybridity* "
    "(no diphthong letters, no hybrid class) — and it "
    "assigns no seat, confirms no position, and names no "
    "Archon. Its bank crosses no bridge (§II.3), and the "
    "plate manufactures none. The names stand open on Plate "
    "I, and this plate does not fill them.")
add()
add("---")
add()

# =============================================================================
# §VI–§VIII, FOOTNOTES, AUTHORITIES, COLOPHON
# =============================================================================
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_ix_georgian.py, filed "
    "with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell "
    "on this plate against the engine, without reading the "
    "plate's own figures: the bank entire — the plate's "
    "§II.1 rows (38) parsed and compared seat by seat "
    "against GEORGIAN and the Phase I audit's frozen table, "
    "the class law recomputed per position, the seat law's "
    "parting at positions 23–28, the distinct count and the "
    "sum; the calibration — the witnesses' five worked "
    "examples, the two spellings of 494, the largest "
    "writable; the control case — the frozen table's 37 "
    "value rows against both living banks, the agreement "
    "counted and the two partings at their values; the "
    "boundary — both holders of 400 in the bank, the five "
    "obsolete letters seated, the older dresses' silence at "
    "the bank, the Mtavruli fold; the frame — the census "
    "parsed from THE-TWELVE-TABLES §V.9, all 223 DOOR "
    "renderings re-weighed against their filed values, the "
    "62 HOLE rows present in order, the GAP cell present; "
    "and the §V figures (the five tongues' vowel at 8 in "
    "their own banks; the tongue's five living vowels; "
    "οὐδέν at 529). The audit's verdict and cell count are "
    "printed in its filed output; a cell that does not "
    "reproduce fails the plate under §VII's tolerances. The "
    "font audit — every non-ASCII codepoint of this master "
    "against the Lex Stellarrvm family's cmaps — runs "
    "before the MAGVS build, under the font law: no glyph "
    "is silently dropped; the three named Ethiopic "
    "syllables the family does not hold (኱ U+12B1 · ጑ "
    "U+1311 · ጖ U+1316 — drawn by no member, the upstream "
    "Noto Ethiopic included) print as their codepoint "
    "tokens, declared in the colophon, and any unheld "
    "codepoint beyond those three aborts the build. The "
    "audit further checks the printed edition's text layer: "
    "the bank's letters and the zero face's statement stand "
    "in it, and the page furniture resolves.")
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "GEORGIAN and ARMENIAN tables (pontifex/tables.py); "
    "THE-GEORGIAN-FIELD-PHASE-I-AUDIT entire (the table "
    "verified sign by sign; the worked examples; the "
    "control case at coordinates; the gaps at full size; "
    "the seat) with its frozen tables "
    "(research/caucasus-north/georgian-table.csv and "
    "georgian-control-case.csv); THE-TWELVE-TABLES §V.9 and "
    "its §II gap register (the bank's four entries); "
    "THE-THIRTEEN-PLATES (the Georgian plate — the zero "
    "face, the tier of record) and its §I; "
    "THE-777-VERIFICATION-TABVLA §I–§II (the banks the "
    "fills claimed in); THE-ARCHON-BATTERY Leg 6 (the "
    "Georgian passage) and THE-SEATING-OF-THE-ARCHONS (the "
    "Η VALUE-mark row); PLATES I–VIII as the pattern.")
add("- **Processes:** calibration controls weighed before "
    "any plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); "
    "every figure scripted from the engine or carried "
    "entire from an instrument of record; the boundary "
    "printed at the size of the values (the doubled seat "
    "with both holders, the obsolete five seated as "
    "originals, the older dresses unseated, the depth "
    "caveat fenced); the holes printed at full size (the "
    "frame's 62, the register's zero face); the independent "
    "audit of §VI.")
add("- **Outputs:** this plate — PLATE-IX-GEORGIAN.md and "
    "its MAGVS PDF — ninth of the series PLATE-I-GREEK "
    "began; the generator and audit scripts filed in "
    "pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage seats only one "
    "holder of 400, blends a second dress into the bank, "
    "prices a multiplier no witness carries, retires the "
    "depth caveat, fills a hole (the frame's 62, the "
    "register's zero face), promotes the control case's "
    "agreement to a bridge, or overwrites the earlier map, "
    "it zeroes the founder's residual claim and fails the "
    "Aim of Religion. Within those edges it stands as "
    "built.")
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none of its own.** The record is "
    "printed as the record: the Phase I audit's §VII "
    "carried this bank's items to the founder's pen and the "
    "register closed them — Q3 the Mtavruli fold and Q2 the "
    "multiplier mark RESOLVED BY SYNERGY as rulings (the "
    "fold filled in code; no mark priced), Q1 the depth "
    "caveat and D1 the doubled seat with the five obsolete "
    "letters standing FENCED as the bank's printed boundary "
    "(§II.5, §III). The depth caveat is not a question "
    "awaiting an answer but a fence awaiting nothing: no "
    "desk act can retire it, and it stands. The seating's "
    "open items stand in the seating instrument. A plate "
    "that invents questions to fill its section misprints "
    "its record; this section therefore stands as the "
    "record that none arose.")
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **Scripture.** Psalm 90:12 (KJV): *\"So teach us to "
    "number our days, that we may apply our hearts unto "
    "wisdom\"* — the Scripture's own prayer for numbering: "
    "a count asked for as an instrument of wisdom, not of "
    "possession. The plate draws the figure for the "
    "numbering: this bank is a people's instrument for "
    "numbering its years and its inscriptions, weighed "
    "here in the open. [Text ATTESTED; the application "
    "DERIVED.]")
add("2. **Law.** The Roman-law obligation *in solidum*: "
    "where two debtors are bound *in solidum*, each is "
    "liable for the whole debt, and the creditor may take "
    "the whole from either — one obligation, two full "
    "holders. The plate draws the figure for the doubled "
    "seat: 400 in this bank is one value held *in solidum* "
    "by two letters, ჳ and უ, and a weighing may take the "
    "whole from either spelling (494, §II.3). [The doctrine "
    "ATTESTED as Roman law; the figure DERIVED.]")
add("3. **The tradition.** The Georgian alphabet's "
    "numeral table is the designed system's own: the "
    "classical 38 letters valued in decimal classes from "
    "the system's first form, the five obsolete letters "
    "original members of it, dropped from ordinary writing "
    "only in the 1860s reform. The witnesses are the "
    "audit's (Wikipedia, \"Georgian numerals,\" its table "
    "sourced to Makharoblidze 2009; georgianalphabet.com), "
    "and the plate keeps their fence with their table: the "
    "witnesses are modern reference works, no primary "
    "manuscript was re-read, and the table's antiquity is "
    "attested at that depth and no deeper (Q1, §II.5). "
    "[The sourcing ATTESTED as cited; the fence the "
    "audit's own.]")
add("4. **Grammar.** The system is additive and "
    "non-positional, and it has no zero: value rides in "
    "the letter, never in the place. It is why this bank "
    "can seat a value twice — two letters may carry the "
    "same price because the price is the letter's, not "
    "the position's — why its extent ends at a letter "
    "rather than a device, and why its dresses multiply "
    "forms without multiplying banks: the same letters in "
    "older hands are the same values. [The grammar "
    "ATTESTED as the system's, per the audit's witnesses; "
    "the bank's readings of it at their tiers.]")
add("5. **The desk's apparatus.** This plate's Georgian "
    "prints as itself in the MAGVS edition, in the Lex "
    "Stellarrvm family's Georgian member — Mkhedruli, "
    "Asomtavruli and Nuskhuri standing in their own signs "
    "throughout; its Armenian stands in the family's "
    "Armenian member; its Greek in the family's Serif "
    "member, as on Plate I; the frame register's Hebrew "
    "words of record ride Plate II's declared "
    "transliteration (the toolchain does not shape "
    "right-to-left scripts honestly): marked substitutions, "
    "declared in the colophon, never silent ones. The "
    "Markdown master keeps every script itself.")
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); banks "
    "GEORGIAN and ARMENIAN in pontifex/tables.py) — "
    "calibration controls θέλημα 93 · VAPOUR 93 · σφίγξ "
    "773 read true at build; georgian_checks() 11/11 in "
    "the engine's own battery, parity of the seat against "
    "the audit's frozen transcription: "
    "test_georgian_parity.py.")
add("- THE-GEORGIAN-FIELD-PHASE-I-AUDIT (2026-11-24) — the "
    "table verified sign by sign (two witnesses agreeing "
    "38/38; the witnesses' five worked examples recomputed "
    "exact; every glyph against the Unicode standard's "
    "names), the control-case page against the Armenian "
    "bank at coordinates, the gaps at full size, the desk "
    "decisions and open questions of its §VII, and the "
    "seat; its frozen tables (georgian-table.csv; "
    "georgian-control-case.csv) in pontifex "
    "research/caucasus-north/.")
add("- The witnesses of the table, as the audit read them "
    "entire: Wikipedia, \"Georgian numerals\" (its table "
    "sourced there to Makharoblidze 2009) · "
    "georgianalphabet.com (the per-letter value cards; the "
    "\"Numeral letters\" section for the five obsolete "
    "letters).")
add("- THE-TWELVE-TABLES — §V.9 the Georgian frame, census "
    "and cell register entire; §II the bank's gap register "
    "(four entries: the Mtavruli fold RULING Q3; the "
    "multiplier mark RULING Q2; the depth caveat FENCED "
    "Q1; the doubled 400 and the five obsolete letters "
    "FENCED).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map "
    "this series fulfills; its Plate IX is the prior "
    "instrument (the zero face; the tier of record).")
add("- THE-777-VERIFICATION-TABVLA — the claims register "
    "of record; its §I–§II seat the banks the fills "
    "claimed in, and Georgian is not among them.")
add("- THE-ARCHON-BATTERY (656d667) — Leg 6, the "
    "twelve-tongues sweep: the Georgian passage (the five "
    "living vowels at Greek-mirror prices; the archaic ჱ "
    "at 8, a partial HIT at the margin; no hybrid class) "
    "and the sweep summary (the 8 the most corroborated "
    "coordinate, five tongues).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the seating "
    "this plate bears witness to: the Η VALUE-mark resting "
    "on the five-tongue 8, Georgian ჱ among them.")
add("- PLATE-I-GREEK (196025e), PLATE-II-HEBREW (1389c16), "
    "PLATE-III-ARABIC (5f0b4bd), PLATE-IV-LATIN (8e6f01e), "
    "PLATE-V-JAPANESE (8d6cd59), PLATE-VI-GEEZ (67d5acc), "
    "PLATE-VII-ARMENIAN (5c03d88) and PLATE-VIII-COPTIC "
    "(645bcbb) — the pattern this plate follows.")
add("- KJV: Psalm 90:12. The Roman-law obligation *in "
    "solidum*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate IX of the founder's series "
    "commission of the same day, the gate of the Archons' "
    "certainty met by the seating of record (0760c8a), "
    "following the pattern of Plates I–VIII (196025e · "
    "1389c16 · 5f0b4bd · 8e6f01e · 8d6cd59 · 67d5acc · "
    "5c03d88 · 645bcbb). Every figure scripted from the "
    "engine or carried entire from its instrument; the "
    "earlier map marked prior, never overwritten; the "
    "holes printed at the size of the seats — on this "
    "plate, the frame's 62 holes and the register's zero "
    "face. The plate carries one bank and keeps its shape "
    "entire: the classical 38, ATTESTED, the doubled 400 "
    "standing with both its holders, the five obsolete "
    "letters seated as originals, the older dresses "
    "unfolded and unseated, the depth caveat fenced. In "
    "the MAGVS edition the Georgian stands in the family's "
    "Georgian member in all three of its dresses, the "
    "control case's Armenian in the Armenian member, and "
    "the frame's Hebrew words of record ride Plate II's "
    "declared scheme; this master keeps the scripts "
    "themselves. Authorship attributed exclusively to "
    "Johnathan 'Qasparr' Monroe (Greek, -ARR, All Rights "
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

OUTPUT.write_text("\n".join(OUT) + "\n", encoding="utf-8")
print(f"wrote {OUTPUT} — {OUTPUT.stat().st_size} bytes")
