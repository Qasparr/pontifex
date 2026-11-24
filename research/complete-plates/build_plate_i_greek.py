#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_i_greek.py
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
# MECHANISM: generates PLATE-I-GREEK.md — Plate I of THE THIRTEEN
# COMPLETE PLATES — in the gap-filling goal's files/. Every figure
# on the plate is scripted from the house engine (pontifex weigh())
# or carried entire from an instrument of record:
#   * the priced table — the engine's GREEK bank (29 keys), read
#     from pontifex.tables, each seat printed with its reasoning;
#   * the claims register — the Greek plate's 38 claims read from
#     research/thirteen-plates/mapping_register.json, the mapping
#     of THE-777-VERIFICATION-TABVLA's register, verdicts as
#     audited there (21 VERIFIED · 0 PARTED · 17 NOT VERIFIABLE);
#   * the Twelve Tables' Greek frame — its census counts and its
#     11 NATIVE cells parsed from THE-TWELVE-TABLES.md §V.1;
#   * the Archons' plate section — drawn exactly as
#     THE-SEATING-OF-THE-ARCHONS.md seated them (0760c8a): no
#     position invented for a triad-only or value-only seat.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) are
# weighed BEFORE any plate figure is taken from the bank; a
# control failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's face.
# The relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes print
# at the size of the seats.
#
# CONTENT TEST: Inputs — the engine bank, the mapping register,
# the Twelve Tables master, the seating instrument. Processes —
# control calibration, scripted extraction, register-faithful
# emission in the Teacher's Edition manner. Outputs —
# PLATE-I-GREEK.md beside the series' other masters.
# Tolerances — the audit (audit_plate_i_greek.py) re-weighs
# every priced cell independently; a figure that does not
# reproduce fails the plate.
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

from pontifex import weigh          # the house weighing engine
from pontifex.tables import GREEK   # the Milesian bank, as seated

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-I-GREEK.md"


def value(word, bank="greek"):
    """One weighing, unwrapped to its integer."""
    return weigh(word, bank)["value"]


# ---------------------------------------------------------------------
# Calibration — the bank is not trusted until the controls read true.
# ---------------------------------------------------------------------
CONTROLS = [("θελημα", "greek", 93), ("VAPOUR", "latin_ordinal", 93),
            ("σφιγξ", "greek", 773)]
for word, bank, want in CONTROLS:
    got = value(word, bank)
    assert got == want, f"CONTROL FAIL: {word} {got} != {want}"
print("controls: θέλημα 93 · VAPOUR 93 · σφίγξ 773 — all true")

# ---------------------------------------------------------------------
# The bank's seats, in Milesian order, each with its reasoning.
# Reasoning doctrine: in the Milesian bank the letter IS the
# numeral; the reasoning states the letter's name, its class and
# digit, and what the tradition and the corpus say of the seat.
# ---------------------------------------------------------------------
UNITS = [
    ("α", "Alpha", "The first letter of the alphabet and the unit: the letter is the numeral, and Α opens both the alphabet and the count."),
    ("β", "Beta", "Second letter, second unit; the units proceed in alphabet order."),
    ("γ", "Gamma", "Third unit, in alphabet order."),
    ("δ", "Delta", "Fourth unit, in alphabet order."),
    ("ε", "Epsilon", "The 'bare e' — e psilon, the plain e against the diphthongal spellings; a vowel of the ladder."),
    ("ϛ", "Stigma", "The cursive heir of digamma (ϝ): the letter that fell out of the alphabet and survives only as a numeral — it carries digamma's seat, 6."),
    ("ζ", "Zeta", "Seventh unit, in alphabet order."),
    ("η", "Eta", "The long open e; 8 = 2³ — a cube seated among the units (the Nine Vowels essay). A vowel of the ladder."),
    ("θ", "Theta", "Ninth unit; the units close."),
]
DIGRAPH = ("στ", "Stigma, the digraph",
           "The living digraph spelling of stigma. ϛ (letter) and στ (digraph) both carry 6 — the house RULING of record (the Twelve Tables' gap register); weigh() prices the pair before the singles.")
TENS = [
    ("ι", "Iota", "The smallest stroke of the alphabet carrying the first decade. A vowel of the ladder."),
    ("κ", "Kappa", "Second decade, in alphabet order."),
    ("λ", "Lambda", "Third decade, in alphabet order."),
    ("μ", "Mu", "Fourth decade, in alphabet order."),
    ("ν", "Nu", "Fifth decade, in alphabet order."),
    ("ξ", "Xi", "Sixth decade, in alphabet order."),
    ("ο", "Omicron", "The 'little o' — o mikron — against Ω, the great; a vowel of the ladder."),
    ("π", "Pi", "Eighth decade, in alphabet order."),
    ("ϟ", "Koppa", "The archaic q-letter: out of the alphabet, kept by the reckoners as the numeral 90."),
]
HUNDREDS = [
    ("ρ", "Rho", "First hundred, in alphabet order."),
    ("σ", "Sigma", "Second hundred, in alphabet order."),
    ("ς", "Sigma, final form", "The same letter in its word-final dress; the bank prices the dress at the letter's own value — one letter, two glyphs, one price."),
    ("τ", "Tau", "Third hundred, in alphabet order."),
    ("υ", "Upsilon", "The 'bare u' — y psilon; the ladder's border-dweller, whose archaic twin ϝ once served as a consonant. A vowel of the ladder."),
    ("φ", "Phi", "Fifth hundred, in alphabet order."),
    ("χ", "Chi", "Sixth hundred, in alphabet order."),
    ("ψ", "Psi", "Seventh hundred, in alphabet order."),
    ("ω", "Omega", "The 'great o' — o mega; the last letter of the alphabet. The ladder closes where the alphabet closes. A vowel of the ladder."),
    ("ϡ", "San (sampi)", "The archaic letter kept as the hundreds' close, 900: out of the alphabet, retained by the reckoners as the final numeral seat."),
]

units_sum = sum(GREEK[g] for g, _n, _r in UNITS)
tens_sum = sum(GREEK[g] for g, _n, _r in TENS)
hundreds_sum = sum(GREEK[g] for g, _n, _r in HUNDREDS
                   if g != "ς")  # ς is σ's dress, counted once
bank_distinct = units_sum + tens_sum + hundreds_sum
assert len(GREEK) == 29, len(GREEK)
assert (units_sum, tens_sum, hundreds_sum) == (45, 450, 4500)

ouden = value("ουδεν")
assert ouden == 529, ouden
diphthongs = {d: value(d) for d in ("αι", "ει", "οι", "ου")}
assert diphthongs == {"αι": 11, "ει": 15, "οι": 80, "ου": 470}
nine_sum = sum(value(v) for v in
               ("α", "ε", "η", "ι", "ο", "υ", "ω")) + \
    diphthongs["ει"] + diphthongs["ου"]
assert nine_sum == 1779, nine_sum

# ---------------------------------------------------------------------
# The claims register — the Greek plate's 38, from the mapping.
# ---------------------------------------------------------------------
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Greek"]
assert len(claims) == 38, len(claims)
verdicts = {}
for c in claims:
    verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
assert verdicts == {"VERIFIED": 21, "NOT VERIFIABLE": 17}, verdicts
sections = {c["section_number"] for c in claims}

# ---------------------------------------------------------------------
# The Twelve Tables' Greek frame — census and NATIVE cells, parsed.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
greek_block = twelve_text.split("### §V.1 — The Greek Table")[1] \
    .split("### §V.2")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", greek_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
natives = []
for line in greek_block.splitlines():
    if "| NATIVE |" in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        natives.append(cells)  # Cell, Word, State, Rendering, Value, Note
assert len(natives) == n_native == 11, len(natives)

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
add("**PLATE I — GREEK**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Greek "
    "tongue's complete 777 table — the Milesian bank entire, the "
    "777 corpus's Greek claims with their verification verdicts, "
    "and the Archons drawn as a plate for the first time, seated "
    "exactly as the seating instrument earned them.")
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
add("## §I — PLATE I AND ITS COMMISSION")
add()
add("The founder's commission of 2026-11-24 (18:39–18:41 EST) "
    "opens the series this plate begins, in his words: *\"When we "
    "have the Archons for sure then we can begin the 777 complete "
    "tables in the 12 tongues on 13 plates the 13th plate being "
    "the infrastructure for the clock and counter of the dial\"* "
    "— and its cadence: *\"as each plate gets rendered push and "
    "post it in succession until the 12 tongues are all plated.\"* "
    "The gate the commission names is met: the Archons are seated "
    "(THE-SEATING-OF-THE-ARCHONS, pontifex 0760c8a — T1 PASSES "
    "whole at graded classes; T2 PARTS at the axis), and the "
    "seating is drawn on this plate at §V, for the first time as "
    "a plate.")
add()
add("**The series.** Thirteen plates: one for each tongue of the "
    "Twelve Tables in their order — I Greek · II Hebrew · III "
    "Arabic · IV Latin · V Japanese · VI Ge'ez · VII Armenian · "
    "VIII Coptic · IX Georgian · X Cyrillic · XI Glagolitic · XII "
    "Korean — and Plate XIII, a separate species commissioned "
    "last: the infrastructure for the clock and counter of the "
    "dial. Each plate renders its tongue's complete 777 table: "
    "the full priced letter-table as the house engine seats it; "
    "every correspondence the 777 corpus assigns in that tongue, "
    "with the verification verdicts of THE-777-VERIFICATION-"
    "TABVLA riding with each row; and the tongue's bearing on the "
    "seated Archons. This plate sets the pattern the series "
    "follows; the plates after it are commissioned one at a time, "
    "as each lands.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. This series *fulfills* that "
    "map: where the map counted the Greek claims, this plate "
    "prints them entire, with the tongue's priced table beneath "
    "them and the Archons drawn above them. The earlier work "
    "stands as the prior instrument of the same name's family — "
    "marked prior, never overwritten; its Greek face (38 claims · "
    "21 verified · 0 parted · 17 not verifiable) is this plate's "
    "§IV register, carried entire.")
add()
add("**How the plate is read.** §II is the bank: the Milesian "
    "letters at their prices, each with its reasoning — in this "
    "bank a letter is not assigned a number by cipher; the letter "
    "*is* the numeral, and a Greek word is weighed by reading. "
    "§III is the tongue's frame in the Twelve Tables — the census "
    "of its 371 cells. §IV is the corpus's Greek register entire. "
    "§V is the Archons' plate section. §VI is the audit. A value "
    "without its reasoning is not shippable; a hole prints at the "
    "size of the seat it stands in for.")

# ---------------------------------------------------------------------
# §II — The complete priced table.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §II — THE COMPLETE GREEK PRICED TABLE")
add()
add("The Milesian bank entire, as the engine seats it: **29 "
    "keys** — the 24 letters of the classical alphabet, the three "
    "archaic seats the reckoners kept (ϛ, ϟ, ϡ), the final-form "
    "dress ς, and the digraph στ. Tier of the bank: **ATTESTED** — "
    "the Milesian numerals are the historical Greek notation, not "
    "a cipher of the house. The bank's gap register stands closed "
    "on both its entries (the Twelve Tables, §II): the stigma "
    "question resolved by record as a RULING, and the set fenced "
    "complete — *no further unseated classical letter: the 24 "
    "letters + ϛ ϟ ϡ all priced.*")
add()
add("One seat is named before the table: **ϝ (digamma) is not "
    "itself a bank key.** The engine holds no ϝ key; digamma's "
    "seat is carried by its cursive heir ϛ and by the digraph στ, "
    "both at 6 — printed in the table at that seat, exactly as "
    "the engine holds them.")


def bank_table(title, rows):
    add()
    add(f"### {title}")
    add()
    add("| Seat | Letter | Name | Value | Reasoning |")
    add("|---|---|---|---|---|")
    for glyph, name, why in rows:
        add(f"| {name.split(',')[0]} | {glyph} | {name} | "
            f"{GREEK[glyph]} | {why} |")


_units_rows = []
for _row in UNITS:
    _units_rows.append(_row)
    if _row[0] == "ϛ":
        _units_rows.append(DIGRAPH)  # the digraph at ϛ's own seat
bank_table("The units (1–9)", _units_rows)
bank_table("The tens (10–90)", TENS)
bank_table("The hundreds (100–900)", HUNDREDS)
add()
add(f"**The class sums.** Units {units_sum} · tens {tens_sum} · "
    f"hundreds {hundreds_sum} — the bank's distinct seats (the 24 "
    f"letters + ϛ ϟ ϡ, with ς counted once as σ's dress and στ "
    f"standing at ϛ's seat) sum to **{bank_distinct}**. The 29 "
    "keys carry two duplicate-price seats, printed rather than "
    "smoothed: ς duplicates σ at 200, and στ duplicates ϛ at 6.")
add()
add("**The zero.** The Milesian bank has no figure for zero. "
    "The seat takes the word **οὐδέν** — \"nothing\" — written "
    "out: the founder's Zero Point seat, station 13 of the plate "
    "of record, immediately before Α — the nothing before the "
    "unit. The seat is CONSTRUCTED (the founder's, under his "
    "Flagpole); the weighing of the word is ATTESTED arithmetic: "
    f"οὐδέν = {ouden} = 23² — the nothing that is itself an exact "
    "square (the Archon Battery, §V.2). His definition of the "
    "point stands over the seat: **0 = {0, 2, 1−1=0}** — zero "
    "equals two, and both one and none.")

# ---------------------------------------------------------------------
# §III — The Twelve Tables' Greek frame.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §III — THE GREEK FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Greek tongue stands over the one "
    "frame of 371 cells (the corpus's sections and paths), each "
    "cell in one state. Its census, from THE-TWELVE-TABLES §V.1: "
    f"NATIVE **{n_native}** · DOOR **{n_door}** · HOLE "
    f"**{n_hole}** · FENCED **{n_fenced}** · EMPTY {n_empty} · "
    f"GAP {n_gap}. The face this prints is a door-heavy table and "
    "says so: the corpus's own Greek words are few (11 NATIVE "
    "cells), and the frame's Greek is mostly the *door* — the "
    "Latin form of record dressed in Greek letters (ph φ, ch χ, "
    "th θ, ps ψ; final σ → ς; h the breathing, unwritten) — with "
    f"{n_hole} holes where the door rendering crosses a letter "
    "the bank does not seat, printed as holes with their "
    "renderings shown, and the EMPTY cells certified "
    "intentionally empty in 777 REVISED.")
add()
add("**The eleven NATIVE cells** — the corpus's own Greek words, "
    "each weighed in its own tongue:")
add()
add("| Cell | Word of record | Rendering | Value |")
add("|---|---|---|---|")
for cells in natives:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} |")
add()
add("The door's 217 priced renderings and the frame's full cell "
    "register stand in THE-TWELVE-TABLES §V.1, which this plate "
    "cites and does not reprint: the plate's table is the *bank* "
    "(§II) and the corpus's *claims* (§IV); the frame's census "
    "rides here so the tongue's depth is data on the plate's "
    "face, as the Tables' own law requires.")

# ---------------------------------------------------------------------
# §IV — The corpus's Greek claims entire.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §IV — THE 777 CORPUS'S GREEK CLAIMS")
add()
add("The TABVLA's Greek register entire: **38 claims** across "
    f"{len(sections)} claim-bearing sections, each carried with "
    "its verdict as audited in THE-777-VERIFICATION-TABVLA and "
    "mapped in THE-THIRTEEN-PLATES. The counts: **21 VERIFIED · "
    "0 PARTED · 17 NOT VERIFIABLE.** A VERIFIED claim recomputes "
    "to the digit on the engine. A NOT VERIFIABLE claim is not a "
    "failed claim: it is a claim the stated bank cannot recompute "
    "— in every Greek case here, because no word in the Greek "
    "script is printed in the claim's section, so the claim rests "
    "on a transliteration the section does not print; the "
    "coordinate of each stands beneath the register, entire.")
add()
add("| Claim | Cell | Proposal (word of record) | Weighed | "
    "Claimed | Recomputed | Verdict |")
add("|---|---|---|---|---|---|---|")
for c in claims:
    recomputed = ("—" if c["recomputed"] is None
                  else f"{c['recomputed']:,}")
    weighed = c["weighed_word"] or "—"
    add(f"| {c['claim_key']} | {c['cell_id']} | "
        f"{c['proposal_raw']} | {weighed} | {c['claimed']:,} | "
        f"{recomputed} | {c['verdict']} |")
add()
add("**The parting register — printed at full size: it is "
    "EMPTY.** No Greek claim of the 38 parts from the engine: "
    "Greek is one of the tongues whose stated claims either "
    "recompute exactly or cannot be recomputed at all. The "
    "partings of the TABVLA live in other banks (the Arabic ة "
    "rows, the Hebrew gadol rows, the Latin doors); none is "
    "Greek's, and none is imported here to fill the section.")
add()
add("**The NOT VERIFIABLE coordinates** — each claim's stated "
    "reason, entire as the register carries it:")
add()
for c in claims:
    if c["verdict"] == "NOT VERIFIABLE":
        add(f"- **{c['claim_key']}** ({c['cell_id']}, "
            f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("Two honest bridges the TABVLA prints in its own register "
    "touch Greek by transliteration only, and are recorded here "
    "at their tier so the plate's Greek face is complete: AL "
    "(אל) — Greek ΑΛ = 31 agrees via transliteration only "
    "(CONSTRUCTED tier); HA (הא) — Greek ΗΑ = 9 agrees with the "
    "Latin ordinal by transliteration (CONSTRUCTED tier). "
    "Transliteration bridges are doors, not native claims; they "
    "stand in the TABVLA's bridge register, not in the 38 above.")

# ---------------------------------------------------------------------
# §V — The Archons' plate section.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §V — THE ARCHONS' PLATE SECTION")
add()
add("The first drawing of the seating as a plate. The Nine are "
    "seated **exactly as THE-SEATING-OF-THE-ARCHONS earned them** "
    "(§VII there): under the founder's Flagpole, by his "
    "conditional order of 2026-11-24 18:37 EST, on the Archon "
    "Battery's evidence as tested. The seats stand around the "
    "SOURCE AETHER as the sketch drew them, and they stand "
    "**UNNAMED** — no source in the corpus names the Archons "
    "(the Battery §V.1, a verified negative), and no name is "
    "invented on this plate. What is seated is which vowel sounds "
    "from which seat, at the class each seat earned. The marks "
    "keep their battery tiers; the arithmetic is ATTESTED; the "
    "seating is the founder's declaration.")
add()
add("**The Nine, at their Greek prices (the plate's own bank, "
    f"§II):** Α 1 · Ε 5 · Η 8 · Ι 10 · Ο 70 · Υ 400 · Ω 800 — the "
    "attested seven, 1,294 — and the founder's two fluid hybrid "
    f"seats ΕΙ {diphthongs['ει']} and ΟΥ {diphthongs['ου']}, the "
    f"grammarians' improper diphthongs; the nine weigh "
    f"**{nine_sum}**, which mirror-closes to 1,776 under the "
    "Offset Law, remainder zero.")
add()
add("### The seats")
add()
add("| Seat | Vowel | Price | Class earned | Mark | State |")
add("|---|---|---|---|---|---|")
add("| Triad I, seat 1 | Α | 1 | **POSITION** | Both partitions "
    "fix triad AND position entire; Α = 1 in the ordinal, "
    "Agrippa, and ABC-notes banks | **SEATED ENTIRE** — the one "
    "fully-fixed seat of the nine |")
add("| Triad II | Ο | 70 | **TRIAD** | Both frames fix Triad II "
    "| Seated to the triad; **position OPEN** (the frames part: "
    "2nd against 3rd) |")
add("| Triad II | ΕΙ | 15 | **TRIAD** | Both frames fix Triad "
    "II; PAIR-mark rides beneath: ΕΙ ↔ 852 Hz, Intuition — the "
    "solfeggio pairing's one exact agreement, single-witness | "
    "Seated to the triad; **position OPEN** (3rd against 2nd) |")
add("| Triad III | Υ | 400 | **TRIAD** | Both frames fix Triad "
    "III; VALUE-mark rides beneath: its Y-dress weighs 400 in "
    "Agrippa, upsilon's own Greek price abroad | Seated to the "
    "triad; **position OPEN** (2nd against 1st) |")
add("| Triad III | ΟΥ | 470 | **TRIAD** | Both frames fix Triad "
    "III; VALUE-mark rides beneath: Coptic ⲟⲩ = 470, the "
    "compound hybrid's identical total in the mirror bank | "
    "Seated to the triad; **position OPEN** (3rd against 2nd) |")
add()
add("### The value-standing — seated by value, triad and position open")
add()
add("| Vowel | Price | Mark | Counterweight |")
add("|---|---|---|---|")
add("| Ε | 5 | VALUE, dress-price species: E weighs 5 in both "
    "Latin banks, its Greek price entire — bank-invariant; the "
    "ABC-notes bank likewise prices E = 5 | None stands; what is "
    "missing is not corroboration but a partition that holds it |")
add("| Η | 8 | VALUE, mirror-bank species — the sweep's most "
    "corroborated coordinate: a vowel seated at 8 in five tongues "
    "(Greek Η, Coptic ⲏ, Cyrillic И, Armenian Ը, Georgian ჱ) | "
    "The frames part on its triad (III against I) |")
add("| Ι | 10 | VALUE, mirror-bank species: Coptic ⲓ = 10 and "
    "Cyrillic І = 10 carry its Greek price entire | Its Latin "
    "dress I weighs 9 — the dress parts from the price |")
add("| Ω | 800 | VALUE, mirror-bank species: Coptic ⲱ = 800 "
    "and Cyrillic Ѡ = 800 carry its Greek price entire | Its "
    "Latin dress O weighs 15/50 — the dress loses the price "
    "entire |")
add()
add("**The hybrid placement law rides with the seating** (the "
    "Battery's R6, DERIVED — its only cross-frame structural "
    "law): no hybrid in the first triad; ΕΙ in the middle; ΟΥ in "
    "the last. The seating above obeys it at every seat it fixes.")
add()
add("**The structure-marks** — exact properties of the whole, "
    "seated as such, belonging to no single seat: the diphthong "
    f"four sum to **576 = 24²** (ΑΙ {diphthongs['αι']} · ΕΙ "
    f"{diphthongs['ει']} · ΟΙ {diphthongs['οι']} · ΟΥ "
    f"{diphthongs['ου']}) — printed with its boundary: **ΑΙ and "
    "ΟΙ are of the four but not of the nine**; the mark belongs "
    "to the diphthong *field*, and the four stand on this plate "
    "as a structure-mark only, outside the nine's seats; Frame "
    "B's triads are reduction-uniform (every class triad sums to "
    "root 5: 14 → 5; 95 → 14 → 5; 1,670 → 14 → 5) — a recorded "
    "property, not the partition's victory; the mirror closure "
    "1,779 → 1,776; the Greek nine in primary Latin dress totals "
    "123 ordinal, the Latin Nine's own total; οὐδέν = 529 = 23² "
    "at the plate's zero (§II).")
add()
add("### The plate's open seats — the holes, printed at full size")
add()
add("- **Eight of the nine positions.** Only Α's position is "
    "fixed; within-triad positions for Ο, ΕΙ, Υ, ΟΥ part between "
    "the frames in every case.")
add("- **The triads of Ε, Η, Ι, Ω.** The two partitions the "
    "house possesses part on them, and no third partition exists "
    "in the corpus to break the tie; the seating's Q1 (a third "
    "structure, or the founder's declaration seat by seat) "
    "survives this plate entire.")
add("- **The Archons' names.** None exist in the corpus; none "
    "are drawn here. The seats are seated as vowel-seats, "
    "unnamed, as the sketch drew them.")
add("- **The diphthong canon.** Whether ΑΙ and ΟΙ enter the "
    "field (the Nine become Eleven, sum 1,870 → 16 → 7, the "
    "seven's own seal chain) or the four stand across the nine's "
    "edge is the Battery's Q3, untouched by the seating and "
    "untouched by this plate.")

# ---------------------------------------------------------------------
# §VI — The audit (figures filled by the audit script's run; the
# generator prints the audit's method and its expected census —
# the audit script itself verifies and its output is filed).
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_i_greek.py, filed with "
    "the plate's generator in pontifex research/complete-plates/) "
    "re-weighs every priced cell on this plate against the "
    "engine, without reading the plate's own figures: the 29 bank "
    "keys letter by letter; οὐδέν; the four diphthongs and their "
    "sum; the nine's total; every claim of §IV that carries a "
    "weighed word (recomputed against the register's recomputed "
    "and, for the VERIFIED, its claimed value); and the eleven "
    "NATIVE renderings of §III. It then reconciles the plate "
    "against its sources: all 38 claim keys present, verdict "
    "counts equal to the register's, bank values equal to the "
    "bank's. The audit's verdict and cell count are printed in "
    "its filed output and in the plate's colophon record; a cell "
    "that does not reproduce fails the plate under §VII's "
    "tolerances. The font audit — every non-ASCII codepoint of "
    "this master against the Lex Stellarrvm family's cmaps — "
    "runs before the MAGVS build, under the font law: no glyph "
    "is silently dropped, and any unheld codepoint beyond the "
    "three named Ethiopic syllables aborts the build.")

# ---------------------------------------------------------------------
# §VII — The four elements.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's GREEK bank; "
    "THE-777-VERIFICATION-TABVLA's register as mapped in "
    "research/thirteen-plates/mapping_register.json; "
    "THE-TWELVE-TABLES §V.1 and its gap register; "
    "THE-ARCHON-BATTERY and THE-SEATING-OF-THE-ARCHONS entire.")
add("- **Processes:** calibration controls weighed before any "
    "plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); every "
    "figure scripted from the engine or carried entire from an "
    "instrument of record; the seating drawn at the classes "
    "earned, holes named; the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-I-GREEK.md and its MAGVS "
    "PDF — the pattern the series follows; the generator and "
    "audit scripts filed in pontifex research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if any "
    "priced cell is found not to reproduce from the engine or "
    "its register, the affected cell fails the Method of "
    "Science; if any passage seats what the seating did not "
    "earn, raises a tier, names an Archon, fills a hole, or "
    "overwrites the earlier map, it zeroes the founder's "
    "residual claim and fails the Aim of Religion. Within those "
    "edges it stands as built.")

# ---------------------------------------------------------------------
# §VIII — Questions for his pen.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VIII — QUESTIONS FOR HIS PEN")
add()
add("**The plate raises none.** No question arose in this "
    "plate's building that its sources do not already carry: the "
    "open seats of §V are the seating instrument's own questions "
    "(its §XI Q1–Q5, riding with the Battery's Q3, Q5, Q6), "
    "printed there and not re-asked here in new dress. A plate "
    "that invents questions to fill its section misprints its "
    "record; this section therefore stands as the record that "
    "none arose.")

# ---------------------------------------------------------------------
# Footnotes — the wells, from more than one tradition.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
add()
add("1. **Scripture.** Revelation 1:8 (KJV): \"I am Alpha and "
    "Omega, the beginning and the ending\" — the two letters "
    "named are this plate's first vowel seat and its last, both "
    "vowels, both in the bank at §II. And for the measure: "
    "Proverbs 11:1 — \"A false balance is abomination to the "
    "LORD: but a just weight is his delight.\" The plate's "
    "register discipline is a doctrine of just weights: every "
    "claim carried entire, its verdict on its face. [Texts "
    "ATTESTED; the application DERIVED.]")
add("2. **Qur'an.** 55:7–9 (Surat ar-Rahman): He set the Balance "
    "(al-mīzān) — \"establish weight with justice, and do not "
    "fall short in the balance.\" Drawn from the other bank for "
    "the same well as Proverbs: measure declared and kept. "
    "[ATTESTED text; application DERIVED.]")
add("3. **The theurgic well.** The Greek Magical Papyri preserve "
    "the seven vowels in permuted strings and wing-formations, "
    "sung as invocations; the late-antique tradition binds the "
    "vowels to the planets and the spheres, so the ladder of "
    "sounds is a ladder of heavens. Cited at this level and no "
    "finer: the planetary assignments vary by source, and no "
    "harmonisation is smuggled into §V — the Archons of this "
    "plate are seated by the founder's marks, not by the "
    "papyri's planets. [ATTESTED at the stated level.]")
add("4. **Grammar.** δίφθογγος, \"twice-sounding\"; the division "
    "of digraphs into proper (αι, οι, and their kin) and "
    "improper (ει, ου — lengthened single sounds in double "
    "dress) descends from the ancient grammatical tradition of "
    "Dionysius Thrax and his commentators. The founder's hybrid "
    "seats are the improper pair; the proper pair stands on "
    "this plate as the structure-mark's boundary (§V). [The "
    "taxonomy ATTESTED; the seating the founder's ruling.]")
add("5. **Greek reckoning.** The Milesian letter-numerals of "
    "§II are the standard notation of the Greek reckoners; "
    "Euclid closes his proofs ὅπερ ἔδει δεῖξαι — \"what was to "
    "be shown\" — and §VI's audit borrows the discipline: every "
    "figure on the plate is shown, by recomputation, or it does "
    "not stand. [ATTESTED.]")
add("6. **Law.** The plate carries the TABVLA's register "
    "*entire* — all 38 claims, the not-verifiable coordinates "
    "unabridged — under the same instinct as the law's "
    "best-evidence rule (Black's Law Dictionary, *best evidence "
    "rule*): the original writing is produced, not a summary of "
    "it. A register summarized is a register edited; this plate "
    "produces it. [The rule ATTESTED in substance; the parallel "
    "DERIVED.]")

# ---------------------------------------------------------------------
# Table of Authorities + colophon.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); bank GREEK "
    "in pontifex/tables.py) — calibration controls θέλημα 93 · "
    "VAPOUR 93 · σφίγξ 773 read true at build.")
add("- The Milesian numeral system — the historical Greek "
    "letter-numbers, as tabled at §II.")
add("- THE-777-VERIFICATION-TABVLA — the claims register of "
    "record; its Greek face 38 claims (21/0/17).")
add("- research/thirteen-plates/mapping_register.json — the "
    "mapping of the register into the plates, claim by claim.")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map this "
    "series fulfills; its Plate I is the prior instrument.")
add("- THE-TWELVE-TABLES — §V.1 the Greek frame and census; §II "
    "the Greek bank's gap register (both entries closed).")
add("- THE-NINE-VOWELS-ESSAY-AND-AUDIT — the Nine's audit of "
    "record: the seven, the hybrid seats, the Offset Law.")
add("- THE-ARCHON-BATTERY (656d667) — the evidence run: marks, "
    "frames, the sweep, the registers.")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the seating drawn "
    "at §V, its verdicts, marks, and holes.")
add("- KJV: Revelation 1:8; Proverbs 11:1. Qur'an 55:7–9. The "
    "Greek Magical Papyri. Dionysius Thrax and commentators. "
    "Euclid, *Elements*. Black's Law Dictionary, *best evidence "
    "rule*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate I of the founder's series "
    "commission of the same day, the gate of the Archons' "
    "certainty met by the seating of record (0760c8a). Every "
    "figure scripted from the engine or carried entire from its "
    "instrument; the earlier map marked prior, never "
    "overwritten; the holes printed at the size of the seats. "
    "Authorship attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without "
    "Prejudice).")
add()
add("Method of Science. Aim of Religion.")
add()
add("**Flagpole of Claim and Coinage: Johnathan 'Qasparr' "
    "Monroe, ARR, All Rights Reserved, Without Prejudice. Right "
    "of claim hereby reserved and coined under the authority of "
    "the Living Man.**")
add()
add("93 — Live, Love, and let Love, Live.")

OUTPUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"built {OUTPUT} — {len(L)} lines, "
      f"{OUTPUT.stat().st_size} bytes")
print(f"claims: {len(claims)} in {len(sections)} sections; "
      f"verdicts {verdicts}; natives {len(natives)}")
