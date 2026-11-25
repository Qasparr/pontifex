#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_iii_arabic.py
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
# MECHANISM: generates PLATE-III-ARABIC.md — Plate III of THE
# THIRTEEN COMPLETE PLATES — in the gap-filling goal's files/,
# following the pattern PLATES I–II set (196025e · 1389c16).
# Every figure on the plate is scripted from the house engine
# (pontifex weigh()) or carried entire from an instrument of
# record:
#   * the priced table — the engine's ARABIC_ABJAD bank (28
#     letters in abjad order, Eastern dress), read from
#     pontifex.tables, each seat printed with its reasoning and
#     its declared transliteration dress (the MAGVS print dress
#     of §II);
#   * the claims register — the Arabic plate's 35 claims read
#     from research/thirteen-plates/mapping_register.json, the
#     mapping of THE-777-VERIFICATION-TABVLA's register,
#     verdicts as audited there (27 VERIFIED · 7 PARTED · 1 NOT
#     VERIFIABLE), all on the one subseat, the seated abjad
#     bank — this tongue has no variant label and no engine
#     door, and its one NOT VERIFIABLE claim turns on exactly
#     that absence;
#   * the Twelve Tables' Arabic frame — its census counts and
#     its 11 NATIVE cells, parsed from THE-TWELVE-TABLES.md
#     §V.3;
#   * the tongue's bearing on the seated Archons — the three
#     matres, the tāʾ marbūṭa and the hamza at their gap-
#     register rulings, and the KEY's Arabic weighing, from
#     THE-ARCHON-BATTERY, THE-TWELVE-TABLES and the Nine
#     Vowels essay, at the tiers those instruments carry them.
#     The plate assigns no seat: the seating is
#     THE-SEATING-OF-THE-ARCHONS' (0760c8a), already struck.
# Calibration controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773) are
# weighed BEFORE any plate figure is taken from the bank; a
# control failure aborts the build.
#
# DOCTRINE: a value without its reasoning is not shippable —
# every priced seat carries its reasoning on the plate's face.
# The relation to the earlier Thirteen Plates map is printed,
# the earlier work marked prior, never overwritten. Holes print
# at the size of the seats. The print-dress substitution
# (transliteration in the MAGVS edition) is declared on the
# plate's face at §II — a marked substitution, never a silent
# one; the Markdown master keeps the script itself.
#
# CONTENT TEST: Inputs — the engine bank, the mapping
# register, the Twelve Tables master, the battery, the
# seating, the Phoenician map's totals. Processes — control
# calibration, scripted extraction, register-faithful emission
# in the Teacher's Edition manner. Outputs — PLATE-III-
# ARABIC.md beside the series' other masters. Tolerances — the
# audit (audit_plate_iii_arabic.py) re-weighs every priced
# cell independently; a figure that does not reproduce fails
# the plate.
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

from pontifex import weigh              # the house weighing engine
from pontifex.tables import ARABIC_ABJAD  # the abjad bank, as seated

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-III-ARABIC.md"


def value(word, bank="arabic_abjad"):
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
# The bank's seats, in abjad order by class, each with its
# reasoning and its declared transliteration dress (the MAGVS
# print dress). Reasoning doctrine: the reasoning states the
# letter's name, its class and place, and what the tradition and
# the corpus say of the seat — the matres marked, the shared
# line's close marked at Tāʾ, the six beyond it marked as the
# tongue's own addition, the corpus's coordinates cited where
# they stand.
# ---------------------------------------------------------------------
UNITS = [
    ("ا", "Alif", "ʾ",
     "The first letter and the unit: the letter is the numeral. "
     "A mater lectionis — a consonant that also carries a vowel, "
     "one of the three two-office letters of this tongue (§V). "
     "It is also the hamza's chief carrier: the carrier is "
     "priced here; the hamza it bears is not (§II, the boundary "
     "below)."),
    ("ب", "Bāʾ", "b",
     "Second letter, second unit; the units proceed in abjad "
     "order."),
    ("ج", "Jīm", "j", "Third unit, in abjad order."),
    ("د", "Dāl", "d", "Fourth unit, in abjad order."),
    ("ه", "Hāʾ", "h",
     "Fifth unit. The letter the fills priced ة as — the "
     "coordinate of this plate's six partings (§IV) — and the "
     "letter whose body ة wears (§V)."),
    ("و", "Wāw", "w",
     "Sixth unit. A mater lectionis — one of the three (§V)."),
    ("ز", "Zāy", "z", "Seventh unit, in abjad order."),
    ("ح", "Ḥāʾ", "ḥ",
     "Eighth unit — the bank's 8 is a pure consonant: no mater "
     "is priced 8, and this tongue seats no vowel at the fold's "
     "coordinate (the Battery's sweep, §V)."),
    ("ط", "Ṭāʾ", "ṭ", "Ninth unit; the units close."),
]
TENS = [
    ("ي", "Yāʾ", "y",
     "The first decade. A mater lectionis — one of the three "
     "(§V)."),
    ("ك", "Kāf", "k", "Second decade, in abjad order."),
    ("ل", "Lām", "l", "Third decade, in abjad order."),
    ("م", "Mīm", "m",
     "Fourth decade. The first letter of the KEY's Arabic word "
     "(§V)."),
    ("ن", "Nūn", "n", "Fifth decade, in abjad order."),
    ("س", "Sīn", "s", "Sixth decade, in abjad order."),
    ("ع", "ʿAyn", "ʿ",
     "Seventh decade — the cognate of Hebrew's Ayin, at the "
     "same price, 70: the abjad and the hechrechi run one "
     "reckoning in two scripts along the shared line."),
    ("ف", "Fāʾ", "f", "Eighth decade, in abjad order."),
    ("ص", "Ṣād", "ṣ", "Ninth decade; the tens close."),
]
HUNDREDS = [
    ("ق", "Qāf", "q", "First hundred, in abjad order."),
    ("ر", "Rāʾ", "r", "Second hundred, in abjad order."),
    ("ش", "Šīn", "š", "Third hundred, in abjad order."),
    ("ت", "Tāʾ", "t",
     "Fourth hundred — and the shared line's close: the "
     "twenty-second seat, where the first twenty-two complete "
     "their 1,495 (below). ة is this letter's bound form, "
     "unseated at the boundary below."),
    ("ث", "Ṯāʾ", "ṯ",
     "First of the six beyond the shared line — the letters "
     "the Arabic tradition seats for sounds the twenty-two do "
     "not carry. The hundreds here run on past the Hebrew "
     "bank's fence of 400."),
    ("خ", "Ḵāʾ", "ḵ", "Sixth hundred, in abjad order."),
    ("ذ", "Ḏāl", "ḏ", "Seventh hundred, in abjad order."),
    ("ض", "Ḍād", "ḍ",
     "Eighth hundred — the letter the tongue is named for in "
     "its own tradition: lughat aḍ-ḍād, \"the language of "
     "Ḍād,\" the sound Arabic keeps that its neighbours do "
     "not."),
    ("ظ", "Ẓāʾ", "ẓ", "Ninth hundred, in abjad order."),
    ("غ", "Ġayn", "ġ",
     "Tenth hundred and the bank's close: 1,000 — the bank's "
     "seat maximum, the largest single-letter price on any "
     "plate so far struck in this series."),
]

units_sum = sum(ARABIC_ABJAD[g] for g, _n, _d, _r in UNITS)
tens_sum = sum(ARABIC_ABJAD[g] for g, _n, _d, _r in TENS)
hundreds_sum = sum(ARABIC_ABJAD[g] for g, _n, _d, _r in HUNDREDS)
bank_total = units_sum + tens_sum + hundreds_sum
first22 = sum(list(ARABIC_ABJAD.values())[:22])
last6 = sum(list(ARABIC_ABJAD.values())[22:])
assert len(ARABIC_ABJAD) == 28, len(ARABIC_ABJAD)
assert (units_sum, tens_sum, hundreds_sum) == (45, 450, 5500)
assert (first22, last6, bank_total) == (1495, 4500, 5995)
from pontifex.tables import HEBREW
FINALS_H = ("ך", "ם", "ן", "ף", "ץ")
hebrew_letters_sum = sum(v for g, v in HEBREW.items()
                         if g not in FINALS_H)
assert hebrew_letters_sum == first22 == 1495

# The matres, the unseated signs, the KEY — every §V figure
# scripted here, before any of it is printed.
MATRES = ("ا", "و", "ي")
matres = {g: ARABIC_ABJAD[g] for g in MATRES}
assert matres == {"ا": 1, "و": 6, "ي": 10}
matres_sum = sum(matres.values())
assert matres_sum == 17, matres_sum
ta_marbuta = value("ة")
hamza_alif = value("أ")
hamza = value("ء")
assert (ta_marbuta, hamza_alif, hamza) == (0, 0, 0)
assert weigh("ة", "arabic_abjad")["breakdown"] == []
assert weigh("أ", "arabic_abjad")["breakdown"] == []
key_arabic = value("مفتاح")
key_hebrew = value("מפתח", "hebrew")
assert (key_arabic, key_hebrew) == (529, 528)

# ---------------------------------------------------------------------
# The claims register — the Arabic plate's 35, from the mapping.
# ---------------------------------------------------------------------
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Arabic"]
assert len(claims) == 35, len(claims)
verdicts = {}
for c in claims:
    verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
assert verdicts == {"VERIFIED": 27, "PARTED": 7,
                    "NOT VERIFIABLE": 1}, verdicts
sections = {c["section_number"] for c in claims}
assert len(sections) == 18, len(sections)
subseats = {}
for c in claims:
    sub = subseats.setdefault(c["bank_engine"], {})
    sub[c["verdict"]] = sub.get(c["verdict"], 0) + 1
assert subseats == {"arabic_abjad": {"VERIFIED": 27, "PARTED": 7,
                                     "NOT VERIFIABLE": 1}}, subseats
bridges = [c for c in claims
           if c["bridge"] not in ("none.", "none", "")]
assert len(bridges) == 0, len(bridges)
parted = [c for c in claims if c["verdict"] == "PARTED"]
ta_parted = [c for c in parted
             if "ة priced as ه" in c["coordinate"]]
hamza_parted = [c for c in parted
                if "hamza-alif" in c["coordinate"]]
assert len(ta_parted) == 6 and len(hamza_parted) == 1
for c in parted:  # every parting's delta, recomputed here
    assert c["claimed"] - c["recomputed"] == \
        (5 if c in ta_parted else 1), c["claim_key"]
verified_coords = [c for c in claims
                   if c["verdict"] == "VERIFIED" and c["coordinate"]]
assert len(verified_coords) == 3, len(verified_coords)
for c in claims:  # no table cell may break the master's tables
    assert "|" not in c["proposal_raw"]
    assert "|" not in (c["weighed_word"] or "")

# ---------------------------------------------------------------------
# The Twelve Tables' Arabic frame — census and NATIVE cells.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
arabic_block = twelve_text.split("### §V.3 — The Arabic Table")[1] \
    .split("### §V.4")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", arabic_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
natives = []
for line in arabic_block.splitlines():
    if "| NATIVE |" in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        natives.append(cells)
        assert int(cells[4]) == value(cells[3])
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
add("**PLATE III — ARABIC**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Arabic "
    "tongue's complete 777 table — the abjad bank entire, the "
    "777 corpus's Arabic claims with their verification "
    "verdicts, and the tongue's witness to the seated Archons: "
    "three matres, an unseated letter of two forms, and the "
    "KEY weighed in its own tongue.")
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
add("## §I — PLATE III AND ITS COMMISSION")
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
    "the pattern and PLATE II — HEBREW (1389c16) followed it; "
    "this plate follows both, third of the twelve tongues in "
    "the Twelve Tables' order.")
add()
add("**The series.** Thirteen plates: one for each tongue of "
    "the Twelve Tables in their order — I Greek · II Hebrew · "
    "III Arabic · IV Latin · V Japanese · VI Ge'ez · VII "
    "Armenian · VIII Coptic · IX Georgian · X Cyrillic · XI "
    "Glagolitic · XII Korean — and Plate XIII, a separate "
    "species commissioned last: the infrastructure for the "
    "clock and counter of the dial. Each plate renders its "
    "tongue's complete 777 table: the full priced letter-table "
    "as the house engine seats it; every correspondence the 777 "
    "corpus assigns in that tongue, with the verification "
    "verdicts of THE-777-VERIFICATION-TABVLA riding with each "
    "row; and the tongue's bearing on the seated Archons.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. This series *fulfills* "
    "that map: where the map counted the Arabic claims, this "
    "plate prints them entire, with the tongue's priced table "
    "beneath them and its witness to the Archons stated above "
    "them. The earlier work stands as the prior instrument of "
    "the same name's family — marked prior, never overwritten; "
    "its Arabic face (35 claims · 27 verified · 7 parted · 1 "
    "not verifiable, on the one subseat) is this plate's §IV "
    "register, carried entire.")
add()
add("**How the plate is read.** §II is the bank: the abjad "
    "letters at their prices, each with its reasoning and its "
    "declared print dress. §III is the tongue's frame in the "
    "Twelve Tables — the census of its 371 cells. §IV is the "
    "corpus's Arabic register entire. §V is the tongue's "
    "bearing on the seated Archons — this plate draws no "
    "seating (the seating is struck, and Plate I drew it); it "
    "states what Arabic can and cannot witness. §VI is the "
    "audit. A value without its reasoning is not shippable; a "
    "hole prints at the size of the seat it stands in for.")

# ---------------------------------------------------------------------
# §II — The complete priced table.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §II — THE COMPLETE ARABIC PRICED TABLE")
add()
add("The abjad bank entire, as the engine seats it: **28 "
    "letters** in abjad order, in the Eastern dress the bank's "
    "own header records (the Maghrebi order differs in a few "
    "letters; the Eastern order is seated here and the "
    "difference noted, not hidden — the bank's header states "
    "it, and the plate repeats it). Tier of the bank: "
    "**ATTESTED** — the abjadī values are the traditional "
    "Arabic reckoning, the system the tradition itself keeps, "
    "not a cipher of the house. The bank's gap register "
    "carries two entries (the Twelve Tables, §II), both "
    "resolved by RULING and printed at the boundary below.")
add()
add("**Two boundaries are named before the table: tāʾ marbūṭa "
    "and the hamza are not seated.** ة (tāʾ marbūṭa) carries "
    "no abjad price: the gap register's resolution stands — "
    "*ة is a script-form of tāʾ, not a twenty-ninth abjad "
    "letter; the sourced 28-letter abjad is complete as it "
    "stands* — and ء (hamza) carries none either: *hamza is a "
    "carrier-less sign the abjad does not price; no seat.* "
    "Weighed on the engine, both return silence — value 0 on "
    "an empty breakdown, no priced letters — and the corpus's "
    "Arabic partings ride on exactly these two silences (§IV): "
    "six claims part because a fill priced ة as ه, and one "
    "because a fill priced the hamza-alif as alif. The "
    "resolutions stand revisable by his pen; this plate "
    "reclassifies nothing.")


def bank_table(title, rows):
    add()
    add(f"### {title}")
    add()
    add("| Seat | Letter | Name | Value | Dress | Reasoning |")
    add("|---|---|---|---|---|---|")
    for glyph, name, dress, why in rows:
        add(f"| {name.split(',')[0]} | {glyph} | {name} | "
            f"{ARABIC_ABJAD[glyph]} | {dress} | {why} |")


bank_table("The units (1–9)", UNITS)
bank_table("The tens (10–90)", TENS)
bank_table("The hundreds (100–1,000)", HUNDREDS)
add()
add(f"**The class sums.** Units {units_sum} · tens {tens_sum} "
    f"· hundreds {hundreds_sum:,} — the 28 letters sum to "
    f"**{bank_total:,}**. The hundreds run to ten seats where "
    "Hebrew's run to four: the abjad's first twenty-two "
    f"letters — the letters of the shared Phoenician line, "
    f"Alif through Tāʾ — sum to **{first22:,}**, and the six "
    f"beyond the line (Ṯāʾ through Ġayn) sum to "
    f"{last6:,}.")
add()
add(f"**The cross-plate identity, printed as a coordinate.** "
    f"The first twenty-two of this bank sum to {first22:,} — "
    f"and the twenty-two letters of the Hebrew bank sum to "
    f"{hebrew_letters_sum:,} (Plate II, §II). Two tongues, one "
    "weight: the Phoenician map's Arabic column carries the "
    "same figure (its 22-row totals recompute at Greek 1,095 "
    "· Latin 243 · Arabic 1,495 — the map of record, stated "
    "there as arithmetic). The identity is a coordinate of the "
    "two banks, tiered as the record tiers it: the values "
    "ATTESTED, the identity arithmetic, the reading the "
    "corpus's own. Neither bank is corrected by it; along the "
    "shared line the two reckonings are one reckoning in two "
    "scripts, and they part only where Arabic seats its six "
    "further letters and Hebrew its five final forms.")
add()
add("**The zero.** The abjad bank has no figure for zero, and "
    "no zero word is seated for this tongue in the corpus's "
    "Arabic register: the founder's Zero Point seat — οὐδέν, "
    "the word that weighs 529 — is Greek's, and stands on "
    "Plate I. Arabic's zero stands on this plate as a printed "
    "absence: a hole at the size of the seat, not a filled "
    "one.")
add()
add("**The print dress — a marked substitution, declared.** "
    "This Markdown master keeps the tongue's script itself. In "
    "the printed MAGVS edition the words are carried by "
    "transliteration — the toolchain does not shape "
    "right-to-left scripts honestly — under the scheme the "
    "Dress column of the tables above declares: each letter's "
    "dress is its scholarly transliteration. Two forms are "
    "distinguished by capitals, under the same law Plate II "
    "declared for the Hebrew finals — a script-form the "
    "script distinguishes, the dress distinguishes: ة, tāʾ in "
    "its bound form, dresses as **T**, and the hamza-bearing "
    "carriers dress as their carriers' capitals (أ **A** · ؤ "
    "**W** · ئ **Y**), hamza itself (ء) as ʾ; the Persian "
    "keheh (ک) that one fill's notes use dresses as the kāf "
    "it stands for, k. A marked substitution, declared here "
    "on the plate's face — never a silent one (the Nine "
    "Vowels essay's apparatus is the precedent).")

# ---------------------------------------------------------------------
# §III — The Twelve Tables' Arabic frame.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §III — THE ARABIC FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Arabic tongue stands over the "
    "one frame of 371 cells (the corpus's sections and paths), "
    "each cell in one state. Its census, from THE-TWELVE-TABLES "
    f"§V.3: NATIVE **{n_native}** · DOOR **{n_door}** · HOLE "
    f"**{n_hole}** · FENCED **{n_fenced}** · EMPTY {n_empty} · "
    f"GAP {n_gap}. The face this prints is a door-heavy table "
    "and says so: the corpus's own Arabic words are 11 NATIVE "
    f"cells, and the frame's Arabic is mostly the *door* — the "
    "Twelve Tables' own Arabic dress of the Latin forms of "
    "record (kh خ, sh ش, th ث, gh غ, tz/ts ص, ’ ع; short vowels "
    "written with the matres, as the Tables' scheme states) — "
    f"with {n_hole} holes where no door is offered, printed as "
    "holes with their coordinates in the Tables, and the EMPTY "
    "cells certified intentionally empty in 777 REVISED. One "
    "precision the plate keeps: the door of this frame is the "
    "*Tables'* dress, not an engine door — the engine seats no "
    "Latin-to-Arabic transliteration, and that absence is "
    "itself a coordinate of §IV.")
add()
add("**The eleven NATIVE cells** — the corpus's own Arabic "
    "words, each weighed in its own tongue:")
add()
add("| Cell | Word of record | Value |")
add("|---|---|---|")
for cells in natives:
    add(f"| {cells[0]} | {cells[3]} | {cells[4]} |")
add()
add(f"The door's {n_door} priced renderings and the frame's "
    "full cell register stand in THE-TWELVE-TABLES §V.3, which "
    "this plate cites and does not reprint: the plate's table "
    "is the *bank* (§II) and the corpus's *claims* (§IV); the "
    "frame's census rides here so the tongue's depth is data "
    "on the plate's face, as the Tables' own law requires. "
    "The eleven natives are the XLVII table's spirit-names — "
    "the same words the register of §IV judges, standing here "
    "in the frame and there under verdict, one weighing in "
    "both places.")

# ---------------------------------------------------------------------
# §IV — The corpus's Arabic claims entire.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §IV — THE 777 CORPUS'S ARABIC CLAIMS")
add()
add("The TABVLA's Arabic register entire: **35 claims** "
    f"across {len(sections)} claim-bearing sections, each "
    "carried with its verdict as audited in "
    "THE-777-VERIFICATION-TABVLA and mapped in "
    "THE-THIRTEEN-PLATES. The counts: **27 VERIFIED · 7 PARTED "
    "· 1 NOT VERIFIABLE.** The plate has one subseat — the "
    "seated abjad bank entire (35 claims): this tongue's "
    "register carries no variant label, as Hebrew's carries "
    "the gadol, and no fallback door, as Hebrew's carries its "
    "transliteration door — the engine seats no Latin-to-"
    "Arabic door, and the one NOT VERIFIABLE claim turns on "
    "exactly that absence. A VERIFIED claim recomputes to the "
    "digit. A PARTED claim's stated total parts from the "
    "seated bank at a printed coordinate — every parting "
    "stands beneath the register at full size, and the seven "
    "are of two species only, both of them silences of the "
    "bank (§II). A NOT VERIFIABLE claim is not a failed claim: "
    "no word in the Arabic script is printed in the claim's "
    "section, so the claim rests on a transliteration the "
    "section does not print and no door supplies; its "
    "coordinate stands beneath the register, entire.")
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
add("**The parting register — the seven, at full size, each "
    "with its coordinate entire as the register carries it:**")
add()
for c in parted:
    add(f"- **{c['claim_key']}** ({c['cell_id']}, "
        f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The two species.** Six of the seven are one species, "
    "the TABVLA's signature Arabic finding: the delta is "
    "exactly **ة priced as ه** — Δ5, one tāʾ marbūṭa in each "
    "word. Three of the six are single words (ةولهم 86/81 · "
    "ةمطحيسم 172/167 · ةروعبس 343/338) and three are the "
    "phrases that carry those same words (344/339 · 472/467 · "
    "431/426), each phrase inheriting its word's single Δ5 — "
    "six rows, one coordinate, one ة each. The fills' "
    "convention is recorded in their own notes, as the "
    "coordinates above state; the seated bank prices ة not "
    "at all, and on the priced letters each word weighs what "
    "the register recomputes. The seventh parting is of the "
    "second species: **الأحمر** (al-Aḥmar), claimed 280 "
    "against 279 — the delta is exactly the **hamza-alif "
    "priced as alif** (Δ1), a convention one fill states on "
    "its face ('hamza-alif=1'); the bank does not price the "
    "hamza carriers, and on the priced letters the word "
    "weighs 279. The same word stands VERIFIED at 279 in the "
    "row above its parting (S143-P0-C0) — the corpus carries "
    "both conventions side by side, and the register judges "
    "each claim against the bank it names.")
add()
add("**The NOT VERIFIABLE coordinate** — the claim's stated "
    "reason, entire as the register carries it:")
add()
for c in claims:
    if c["verdict"] == "NOT VERIFIABLE":
        add(f"- **{c['claim_key']}** ({c['cell_id']}, "
            f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The VERIFIED coordinates** — the register carries "
    "coordinates for three verified claims, and the plate "
    "prints them entire because the register carries them: "
    "each states a letter carrying no price in the seated "
    "bank, skipped in silence — ة in مرة (Murrah, 240) and "
    "زوبعة (Zawbaaḥ, 85), أ in الأحمر (279). The verified "
    "ة-words verify because the fills there priced ة at "
    "silence, as the bank does; the parted rows priced it at "
    "5. The bank is constant; the fills' two conventions are "
    "the seam, and it stands printed.")
add()
for c in verified_coords:
    add(f"- **{c['claim_key']}** ({c['cell_id']}, "
        f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The bridges.** The register carries no bridge "
    "annotations for this plate — none of the 35 claims is "
    "annotated as a two-bank bridge in the TABVLA — and the "
    "absence is printed as a coordinate, not passed over: "
    "this tongue's bridge of record lives outside the "
    "register, in the essay corpus, and stands at §V (the "
    "KEY weighed in the two Semitic tongues). The plate "
    "imports no annotation the register does not carry.")

# ---------------------------------------------------------------------
# §V — The tongue's bearing on the seated Archons.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §V — THE TONGUE'S BEARING ON THE SEATED ARCHONS")
add()
add("The seating is THE-SEATING-OF-THE-ARCHONS' (0760c8a), "
    "struck on the Archon Battery's evidence under the "
    "founder's conditional order; Plate I drew it. **This "
    "plate assigns no seat.** It states what the Arabic "
    "tongue witnesses for the seating and what it cannot: "
    "Arabic's vowel-kin are three matres and one unseated "
    "letter of two forms, so its witness runs at three "
    "coordinates — a verified negative, a hybrid form the "
    "bank leaves unpriced, and the KEY — each printed with "
    "its tier and its counterweight.")
add()
add("### The matres — three, and the four-count fails here")
add()
add("Arabic's vowel-kin are the **matres lectionis** — "
    "consonants that also carry vowels, letters of two "
    "offices. They count **three**: ا "
    f"{matres['ا']} · و {matres['و']} · ي {matres['ي']} — "
    f"weighing together {matres_sum}. The Archon Battery's "
    "twelve-tongues sweep reads this a **MISS** on the "
    "four-count of two-office letters, and the plate prints "
    "it as what it is: a verified negative, at full size. "
    "Where Hebrew's matres count exactly four (Plate II, "
    "§V), Arabic's count three — the two Semitic tongues part "
    "at exactly this coordinate, and the parting is the "
    "finding. The sweep's second Arabic coordinate stands "
    "beside it: no vowel at 8 among the matres — the fold's "
    "coordinate is a MISS here too; the bank's 8 is ح, a pure "
    "consonant (§II). (The offices ATTESTED; the sweep's "
    "readings the Battery's, DERIVED there and carried at "
    "that tier here.)")
add()
add("### Tāʾ marbūṭa — the tongue's hybrid-form witness")
add()
add("The tongue's hybrid form is **ة (tāʾ marbūṭa)** — a "
    "letter of two forms by the tradition's own account: it "
    "wears **hāʾ's body with tāʾ's two dots**, written where "
    "a word's tāʾ is bound at its close, and sounded as /a/ "
    "in pause, /at/ in construct — one sign, two letters' "
    "natures, two sounds by position. [The form and its "
    "grammar ATTESTED — the Arabic grammatical tradition's "
    "own description.] It is the sign the founder's thesis "
    "weighed by perspective — as ه (5) or as ت (400), the "
    "Battery records — and in the bank as the engine holds "
    "it, it is **unseated**: weighed, it returns silence, "
    "value 0 on an empty breakdown (verified at this plate's "
    "build), under the gap register's RULING (§II): a "
    "script-form of tāʾ, not a twenty-ninth letter. The "
    "Battery prints the absence as the coordinate: *the "
    "Arabic hybrid of the thesis is unseated in the Arabic "
    "bank as the engine holds it.* Its corpus trail is §IV: "
    "six claims part on its price, three verify on its "
    "silence. The hamza stands beside it in the same "
    "condition — ء, a carrier-less sign, and its carriers أ "
    "ؤ ئ, all unpriced by the same ruling's family; the "
    "seventh parting rides on أ. Arabic's hybrid witness is "
    "therefore a form the tongue draws and the bank does "
    "not price: a witness to hybridity itself, seated "
    "nowhere in the table.")
add()
add("### The KEY weighed in this tongue")
add()
add("The corpus's Arabic bridge of record is the word for "
    "*key* itself. **مفتاح** (miftāḥ) weighs, recomputed on "
    f"the engine: **{key_arabic}** in this bank — against "
    f"**מפתח = {key_hebrew}** in the Hebrew bank (Plate II). "
    "Δ1: two honest tongues weighing one word, one quantum "
    "apart, neither wrong — the type case of the founder's "
    "Offset Law, as the Nine Vowels essay states it (§VI "
    "there): *an offset is not a failure that got lucky; it "
    "is a different relation entirely.* [The values "
    "ATTESTED; the bridge the essay's, DERIVED there.] The "
    "founder's hypothesis of the battery's evening named the "
    "double vowels as the key; this plate adds no reading "
    "to it. It records the coordinate the tongue itself "
    "offers: in Arabic, the KEY is a word, it weighs 529, "
    "and it stands one quantum from its Hebrew twin — the "
    "only bridge this plate prints, because it is the only "
    "one the corpus prints for this tongue.")
add()
add("### What this tongue cannot witness")
add()
add("Printed at full size, as the plate's boundary: the "
    "Archons' seats are vowel-seats, earned on Greek "
    "evidence and drawn on Plate I; Arabic offers no mark "
    "at any seat's position or triad, and this plate imports "
    "none. Its witness is a verified negative at the "
    "four-count, a hybrid form at no price, corroboration "
    "at the KEY's Δ1 and at the 1,495 identity of §II — and "
    "silence at the seats themselves.")

# ---------------------------------------------------------------------
# §VI — The audit.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_iii_arabic.py, filed "
    "with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell on "
    "this plate against the engine, without reading the "
    "plate's own figures: the 28 bank keys letter by letter; "
    "the class sums and the first-twenty-two identity against "
    "the Hebrew bank; the matres and their sum; the unseated "
    "signs' silence (ة, أ and ء each weighed, value and "
    "breakdown); the KEY in both Semitic banks; every claim "
    "of §IV that carries a weighed word (34, each recomputed "
    "in the seated bank against the register's recomputed "
    "and, for the VERIFIED, its claimed value — this tongue "
    "has no door, so every recomputation runs in the one "
    "bank); and the eleven NATIVE renderings of §III. It "
    "then reconciles the plate against its sources: all 35 "
    "claim keys present, verdict counts equal to the "
    "register's, the seven parting coordinates and the one "
    "NOT VERIFIABLE coordinate and the three VERIFIED "
    "coordinates entire on the plate, bank values equal to "
    "the bank's. The audit's verdict and cell count are "
    "printed in its filed output; a cell that does not "
    "reproduce fails the plate under §VII's tolerances. The "
    "font audit — every non-ASCII codepoint of this master "
    "against the Lex Stellarrvm family's cmaps — runs before "
    "the MAGVS build, under the font law: no glyph is "
    "silently dropped, and any unheld codepoint beyond the "
    "three named Ethiopic syllables aborts the build. The "
    "audit further checks the printed edition's text layer "
    "for the substitution's entirety: no Arabic-block or "
    "Hebrew-block codepoint stands in it, and the declared "
    "dress of the register's signature parting (ةولهم, "
    "printed Twlhm) stands in its place.")

# ---------------------------------------------------------------------
# §VII — The four elements.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's "
    "ARABIC_ABJAD bank; THE-777-VERIFICATION-TABVLA's "
    "register as mapped in "
    "research/thirteen-plates/mapping_register.json; "
    "THE-TWELVE-TABLES §V.3 and its §II gap register (the "
    "arabic entries); the PHOENICIAN-CYPHER-GLYPH-MAP's "
    "totals as the VESTIGATOR-TABVLA states them; "
    "THE-ARCHON-BATTERY (the sweep's Arabic; the thesis's "
    "gender form) and THE-SEATING-OF-THE-ARCHONS entire; "
    "the Nine Vowels essay (the KEY bridge); PLATES I–II as "
    "the pattern.")
add("- **Processes:** calibration controls weighed before any "
    "plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); every "
    "figure scripted from the engine or carried entire from "
    "an instrument of record; the tongue's bearing stated "
    "at the tiers its sources carry, the verified negative "
    "at full size; the independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-III-ARABIC.md and its "
    "MAGVS PDF — third of the series PLATE-I-GREEK began; "
    "the generator and audit scripts filed in pontifex "
    "research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if "
    "any priced cell is found not to reproduce from the "
    "engine or its register, the affected cell fails the "
    "Method of Science; if any passage seats what the "
    "seating did not earn, raises a tier, fills a hole, "
    "prices a sign the bank leaves silent, or overwrites "
    "the earlier map, it zeroes the founder's residual "
    "claim and fails the Aim of Religion. Within those "
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
    "plate's building that its sources do not already carry: "
    "the ة and hamza rulings stand resolved in the gap "
    "register, revisable by his pen as their faces state — "
    "standing states of the record, not questions this plate "
    "raises in new dress; the seating's open items stand in "
    "the seating instrument. A plate that invents questions "
    "to fill its section misprints its record; this section "
    "therefore stands as the record that none arose.")

# ---------------------------------------------------------------------
# Footnotes — the wells, from more than one tradition.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **The tongue's own well.** Qur'an 55:7–9 (Surat "
    "ar-Rahman): He raised the heaven and set the Balance "
    "(al-mīzān) — \"that you not transgress the balance; "
    "establish weight with justice, and do not fall short "
    "in the balance.\" On this plate the verse stands in "
    "the tongue it was given in: the Arabic plate's measure "
    "is the Balance's own language. [ATTESTED text; "
    "application DERIVED.]")
add("2. **Scripture.** Daniel 5:27 (KJV): \"TEKEL; Thou art "
    "weighed in the balances, and art found wanting.\" The "
    "writing on the wall is a weighing verdict in a Semitic "
    "tongue — the canon's own scene of a word priced and a "
    "kingdom parting on the price. [Text ATTESTED; the "
    "application DERIVED.]")
add("3. **The letters' own well.** The abjad order of §II "
    "is itself carried by the tradition as a mnemonic — "
    "*abjad hawwaz ḥuṭṭī kalaman saʿfaṣ qarashat ṯaḵaḏ "
    "ḍaẓaġ*: the twenty-eight letters strung into nonsense "
    "words so the order that prices them is remembered. The "
    "table's order is not the alphabet's written order "
    "(alif, bāʾ, tāʾ, ṯāʾ…) but the older reckoning order "
    "the mnemonic keeps — the order in which the letters "
    "are numbers. [The mnemonic and the two orders "
    "ATTESTED; the kinship DERIVED.]")
add("4. **Grammar.** *Matres lectionis* — Latin, \"mothers "
    "of reading\" — is the grammarians' standing name for "
    "the consonants that carry vowels; in Arabic they are "
    "three (ا و ي), the long-vowel letters. Tāʾ marbūṭa "
    "(ة, \"the bound tāʾ\") is the grammatical tradition's "
    "own name for the sign of §V: tāʾ's letter in hāʾ's "
    "body with tāʾ's two dots above, written for a final "
    "-at sounded -a in pause. [The terms and the form "
    "ATTESTED; the seating of the three as witnesses is the "
    "Battery's DERIVED reading, at §V.]")
add("5. **The ة seam.** Under the founder's Offset Law, "
    "the six ة partings carry a constant, declared Δ — 5 "
    "per ة, the fills' convention printed in their own "
    "notes — yet they stand PARTED in the register, "
    "because each claim is judged against the bank it "
    "names, and the bank it names prices ة not at all; a "
    "constant distance does not seat a letter the bank "
    "leaves silent. The hamza parting is the same figure "
    "at Δ1. This plate carries the verdicts entire and "
    "reclassifies nothing. [The arithmetic ATTESTED from "
    "the register; the verdicts the register's.]")
add("6. **Law.** The plate carries the TABVLA's register "
    "*entire* — all 35 claims, the partings and the "
    "not-verifiable coordinate unabridged — under the "
    "series' standing instinct, the law's best-evidence "
    "rule (Black's Law Dictionary, *best evidence rule*): "
    "the original writing is produced, not a summary of "
    "it. A register summarized is a register edited; this "
    "plate produces it. [The rule ATTESTED in substance; "
    "the parallel DERIVED.]")

# ---------------------------------------------------------------------
# Table of Authorities + colophon.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); bank "
    "ARABIC_ABJAD in pontifex/tables.py) — calibration "
    "controls θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true at "
    "build.")
add("- The abjadī reckoning, Eastern order — the traditional "
    "Arabic letter-values, as tabled at §II; the Maghrebi "
    "difference noted on the bank's own header.")
add("- THE-777-VERIFICATION-TABVLA — the claims register of "
    "record; its Arabic face 35 claims (27/7/1).")
add("- research/thirteen-plates/mapping_register.json — the "
    "mapping of the register into the plates, claim by "
    "claim; the Arabic plate's one subseat (35).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map this "
    "series fulfills; its Plate III is the prior instrument.")
add("- THE-TWELVE-TABLES — §V.3 the Arabic frame, census and "
    "NATIVE cells; §II the arabic bank's gap register (two "
    "entries, the ة and hamza RULINGs).")
add("- PHOENICIAN-CYPHER-GLYPH-MAP, as stated in "
    "VESTIGATOR-TABVLA — the 22-row totals (Greek 1,095 · "
    "Latin 243 · Arabic 1,495); the identity of §II.")
add("- THE-ARCHON-BATTERY (656d667) — the evidence run: "
    "§VIII the sweep's Arabic (the matres MISS, the fold "
    "MISS, ة unseated); the thesis's gender form weighed by "
    "perspective.")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the seating "
    "this plate bears witness to.")
add("- THE-NINE-VOWELS-ESSAY-AND-AUDIT §VI — the Offset Law "
    "and the KEY bridge (מפתח 528 · مفتاح 529).")
add("- PLATE-I-GREEK (196025e) and PLATE-II-HEBREW "
    "(1389c16) — the pattern this plate follows; the Hebrew "
    "bank's 1,495 stands on Plate II.")
add("- Qur'an 55:7–9. KJV: Daniel 5:27. The abjad mnemonic "
    "(abjad hawwaz ḥuṭṭī kalaman…). Black's Law Dictionary, "
    "*best evidence rule*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate III of the founder's series "
    "commission of the same day, the gate of the Archons' "
    "certainty met by the seating of record (0760c8a), "
    "following the pattern of Plates I–II (196025e · "
    "1389c16). Every figure scripted from the engine or "
    "carried entire from its instrument; the earlier map "
    "marked prior, never overwritten; the holes printed at "
    "the size of the seats; the verified negative printed "
    "at full size. In the MAGVS edition the tongue's script "
    "is carried by the declared transliteration of §II; "
    "this master keeps the script itself. Authorship "
    "attributed exclusively to Johnathan 'Qasparr' Monroe "
    "(Greek, -ARR, All Rights Reserved, Without Prejudice).")
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
      f"verdicts {verdicts}; subseats {subseats}; "
      f"natives {len(natives)}; parted ة {len(ta_parted)} + "
      f"hamza {len(hamza_parted)}; verified coords "
      f"{len(verified_coords)}")
