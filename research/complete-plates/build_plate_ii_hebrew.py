#!/usr/bin/env python3
# =============================================================================
# 93 — build_plate_ii_hebrew.py
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
# MECHANISM: generates PLATE-II-HEBREW.md — Plate II of THE
# THIRTEEN COMPLETE PLATES — in the gap-filling goal's files/,
# following the pattern PLATE-I-GREEK set (196025e). Every figure
# on the plate is scripted from the house engine (pontifex
# weigh()) or carried entire from an instrument of record:
#   * the priced table — the engine's HEBREW bank (27 keys: the
#     22 letters and the five final forms at face value), read
#     from pontifex.tables, each seat printed with its reasoning
#     and its declared transliteration dress (the MAGVS print
#     dress of §II);
#   * the claims register — the Hebrew plate's 146 claims read
#     from research/thirteen-plates/mapping_register.json, the
#     mapping of THE-777-VERIFICATION-TABVLA's register, verdicts
#     as audited there (93 VERIFIED · 11 PARTED · 42 NOT
#     VERIFIABLE), across the plate's three subseats (the seated
#     bank 111 · the mispar-gadol variant label 21 · the Hebrew
#     fallback door 14), Aramaic folded in by inheritance;
#   * the Twelve Tables' Hebrew frame — its census counts and
#     its 45 NATIVE cells with their Aramaic dresses, parsed
#     from THE-TWELVE-TABLES.md §V.2;
#   * the tongue's bearing on the seated Archons — the matres
#     lectionis, the founding head and the founder's HIS noting,
#     and the key's Hebrew dress, from THE-ARCHON-BATTERY and
#     THE-TWELVE-TABLES, at the tiers those instruments carry
#     them. The plate assigns no seat: the seating is
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
# one; the Markdown master keeps the scripts themselves.
#
# CONTENT TEST: Inputs — the engine bank and its fallback door,
# the mapping register, the Twelve Tables master, the battery
# and the seating. Processes — control calibration, scripted
# extraction, register-faithful emission in the Teacher's
# Edition manner. Outputs — PLATE-II-HEBREW.md beside the
# series' other masters. Tolerances — the audit
# (audit_plate_ii_hebrew.py) re-weighs every priced cell
# independently; a figure that does not reproduce fails the
# plate.
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
from pontifex import transliterate_latin_to_hebrew
from pontifex.tables import HEBREW  # the hechrechi bank, as seated

GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
REGISTER = (Path.home() / "workspace/pontifex/research/"
            "thirteen-plates/mapping_register.json")
TWELVE = GOAL_FILES / "THE-TWELVE-TABLES.md"
OUTPUT = GOAL_FILES / "PLATE-II-HEBREW.md"


def value(word, bank="hebrew"):
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
# The bank's seats, in alphabet order by class, each with its
# reasoning and its declared transliteration dress (the MAGVS
# print dress). Reasoning doctrine: the reasoning states the
# letter's name, its class and place, and what the tradition and
# the corpus say of the seat — the matres marked, the finals'
# law stated, the corpus's own coordinates cited where they
# stand. The finals print at their letters' own seats, as the
# digraph στ printed at ϛ's seat on Plate I.
# ---------------------------------------------------------------------
UNITS = [
    ("א", "Aleph", "ʾ",
     "The first letter and the unit: the letter is the numeral. "
     "A mater lectionis — a consonant that also carries a vowel, "
     "one of the four two-office letters (§V)."),
    ("ב", "Beth", "b",
     "Second letter, second unit; the units proceed in "
     "alphabet order."),
    ("ג", "Gimel", "g", "Third unit, in alphabet order."),
    ("ד", "Daleth", "d", "Fourth unit, in alphabet order."),
    ("ה", "He", "h",
     "Fifth unit. A mater lectionis — one of the four two-office "
     "letters (§V)."),
    ("ו", "Waw", "w",
     "Sixth unit. A mater lectionis; in the engine's Hebrew dress "
     "of Latin words it is the merger seat — W and V both fall "
     "to ו — the merger on which the key's Hebrew collapse rides "
     "(§V)."),
    ("ז", "Zayin", "z",
     "Seventh unit. Spelled in full, זין (ZIN) = 67 — a bridge "
     "claim of the register (§IV). With ע it spells the founding "
     "head (§V)."),
    ("ח", "Ḥeth", "ḥ",
     "Eighth unit — the bank's 8 is a pure consonant: no mater "
     "is priced 8, and this tongue seats no vowel at the fold's "
     "coordinate (the Battery's sweep, §V)."),
    ("ט", "Ṭeth", "ṭ", "Ninth unit; the units close."),
]
TENS = [
    ("י", "Yod", "y",
     "The smallest letter of the alphabet carrying the first "
     "decade. A mater lectionis — one of the four (§V)."),
    ("כ", "Kaph", "k",
     "Second decade, in alphabet order. One of the five letters "
     "with a final form."),
    ("ך", "Kaph, final form", "K",
     "The same letter in its word-final dress (sophith); the "
     "bank prices the dress at the letter's own value under the "
     "face-value law — the gadol uplift refused at this seat."),
    ("ל", "Lamed", "l",
     "Third decade. Spelled in full, למד (LMD) = 74 — a bridge "
     "claim of the register (§IV)."),
    ("מ", "Mem", "m",
     "Fourth decade. One of the five with a final form."),
    ("ם", "Mem, final form", "M",
     "The pivot of the bank's one parting of principle: priced "
     "40 at face value here; under mispar gadol this seat would "
     "carry 600, and מאדים (Madim) would weigh 655 — the "
     "corpus's sharpest Hebrew parting rides on this letter "
     "(§IV)."),
    ("נ", "Nun", "n",
     "Fifth decade. One of the five with a final form."),
    ("ן", "Nun, final form", "N",
     "The letter's final dress at face value, 50."),
    ("ס", "Samekh", "s", "Sixth decade, in alphabet order."),
    ("ע", "Ayin", "ʿ",
     "Seventh decade. With ז it spells the founding head: עז "
     "(Oz) = 77 — 77 in this script and in both Aramaic dresses "
     "(§V)."),
    ("פ", "Pe", "p",
     "Eighth decade. One of the five with a final form."),
    ("ף", "Pe, final form", "P",
     "The letter's final dress at face value, 80."),
    ("צ", "Ṣaddi", "ṣ",
     "Ninth decade. One of the five with a final form; the tens "
     "close."),
    ("ץ", "Ṣaddi, final form", "Ṣ",
     "The letter's final dress at face value, 90."),
]
HUNDREDS = [
    ("ק", "Qoph", "q", "First hundred, in alphabet order."),
    ("ר", "Resh", "r", "Second hundred, in alphabet order."),
    ("ש", "Shin", "š", "Third hundred, in alphabet order."),
    ("ת", "Taw", "t",
     "Fourth hundred and the bank's close: 400 is the engine's "
     "seat maximum — the fence the gadol variant breaks and "
     "this bank keeps."),
]

FINALS = ("ך", "ם", "ן", "ף", "ץ")
units_sum = sum(HEBREW[g] for g, _n, _d, _r in UNITS)
tens_letters = sum(HEBREW[g] for g, _n, _d, _r in TENS
                   if g not in FINALS)
hundreds_sum = sum(HEBREW[g] for g, _n, _d, _r in HUNDREDS)
finals_sum = sum(HEBREW[g] for g in FINALS)
letters_sum = units_sum + tens_letters + hundreds_sum
bank_all = letters_sum + finals_sum
assert len(HEBREW) == 27, len(HEBREW)
assert (units_sum, tens_letters, hundreds_sum) == (45, 450, 1000)
assert (letters_sum, finals_sum, bank_all) == (1495, 280, 1775)

# The matres, the founding head, the noting, the key's dress —
# every §V figure scripted here, before any of it is printed.
MATRES = ("א", "ה", "ו", "י")
matres = {g: HEBREW[g] for g in MATRES}
assert matres == {"א": 1, "ה": 5, "ו": 6, "י": 10}
matres_sum = sum(matres.values())
assert matres_sum == 22, matres_sum
oz = value("עז")
oz_imperial = value("𐡏𐡆", "aramaic")
oz_syriac = value("ܥܙ", "aramaic")
assert (oz, oz_imperial, oz_syriac) == (77, 77, 77)
his_ordinal = value("HIS", "latin_ordinal")
his_agrippa = value("HIS", "agrippa")
assert (his_ordinal, his_agrippa) == (36, 107)
KEY_DRESS = transliterate_latin_to_hebrew("WVII")[0]
assert transliterate_latin_to_hebrew("VVII")[0] == KEY_DRESS
assert [hex(ord(ch)) for ch in KEY_DRESS] == \
    ["0x5d5", "0x5d5", "0x5d9", "0x5d9"]  # ו ו י י, the one word
assert value(KEY_DRESS) == 32
assert value("WVII", "latin_ordinal") == 63
assert value("VVII", "latin_ordinal") == 62
assert value("VVII", "agrippa") == 418

# ---------------------------------------------------------------------
# The claims register — the Hebrew plate's 146, from the mapping.
# ---------------------------------------------------------------------
register = json.loads(REGISTER.read_text(encoding="utf-8"))
claims = [c for c in register["claims"] if c["plate"] == "Hebrew"]
assert len(claims) == 146, len(claims)
verdicts = {}
for c in claims:
    verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
assert verdicts == {"VERIFIED": 93, "PARTED": 11,
                    "NOT VERIFIABLE": 42}, verdicts
sections = {c["section_number"] for c in claims}
subseats = {}
for c in claims:
    sub = subseats.setdefault(c["bank_engine"], {})
    sub[c["verdict"]] = sub.get(c["verdict"], 0) + 1
assert subseats == {
    "hebrew": {"VERIFIED": 82, "NOT VERIFIABLE": 29},
    "hebrew_gadol": {"VERIFIED": 6, "PARTED": 2,
                     "NOT VERIFIABLE": 13},
    "hebrew_fallback": {"VERIFIED": 5, "PARTED": 9}}, subseats
bridges = [c for c in claims
           if c["bridge"] not in ("none.", "none", "")]
assert len(bridges) == 6, len(bridges)
for c in claims:  # no table cell may break the master's tables
    assert "|" not in c["proposal_raw"]
    assert "|" not in (c["weighed_word"] or "")

# ---------------------------------------------------------------------
# The Twelve Tables' Hebrew frame — census and NATIVE cells.
# ---------------------------------------------------------------------
twelve_text = TWELVE.read_text(encoding="utf-8")
hebrew_block = twelve_text.split("### §V.2 — The Hebrew Table")[1] \
    .split("### §V.3")[0]
counts_line = re.search(r"Counts: NATIVE \*\*(\d+)\*\* · DOOR "
                        r"\*\*(\d+)\*\* · HOLE \*\*(\d+)\*\* · "
                        r"FENCED \*\*(\d+)\*\* · EMPTY (\d+) · "
                        r"GAP (\d+)", hebrew_block)
n_native, n_door, n_hole, n_fenced, n_empty, n_gap = \
    (int(x) for x in counts_line.groups())
natives = []
for line in hebrew_block.splitlines():
    if "| NATIVE |" in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.search(r"Aramaic dresses: (\S+) · (\S+) = (\d+)\.",
                      cells[5])
        assert m, cells[0]
        natives.append((cells, m.group(1), m.group(2)))
        assert int(m.group(3)) == int(cells[4])
assert len(natives) == n_native == 45, len(natives)

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
add("**PLATE II — HEBREW**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the Hebrew "
    "tongue's complete 777 table — the hechrechi bank entire "
    "with the Aramaic dresses folded in by inheritance, the 777 "
    "corpus's Hebrew claims with their verification verdicts, "
    "and the tongue's witness to the seated Archons: the four "
    "matres, the founding head, and the key's collapse.")
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
add("## §I — PLATE II AND ITS COMMISSION")
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
    "PARTS at the axis). PLATE I — GREEK (pontifex 196025e) "
    "landed first and set the pattern; this plate follows it, "
    "second of the twelve tongues in the Twelve Tables' order.")
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
add("**Aramaic folds into this plate.** The census proved the "
    "inheritance — the Aramaic seat's values are Hebrew's "
    "values in two further dresses (Imperial and Syriac), one "
    "weighing in three scripts — so Aramaic holds no plate of "
    "its own: a separate plate would count one weighing as two "
    "witnesses. Its dresses ride this plate's frame (§III), and "
    "its claims ride this plate's register (§IV), exactly as "
    "the earlier map folded them.")
add()
add("**The relation to the earlier map.** THE-THIRTEEN-PLATES "
    "(pontifex 6afe470, struck earlier this day) mapped the "
    "TABVLA's 504 claims into the twelve tongues as thirteen "
    "plates of *mapping* — each plate a face of verdict counts, "
    "its claims indexed to the Core. This series *fulfills* "
    "that map: where the map counted the Hebrew claims, this "
    "plate prints them entire, with the tongue's priced table "
    "beneath them and its witness to the Archons stated above "
    "them. The earlier work stands as the prior instrument of "
    "the same name's family — marked prior, never overwritten; "
    "its Hebrew face (146 claims · 93 verified · 11 parted · 42 "
    "not verifiable, over three subseats) is this plate's §IV "
    "register, carried entire.")
add()
add("**How the plate is read.** §II is the bank: the hechrechi "
    "letters at their prices, each with its reasoning and its "
    "declared print dress. §III is the tongue's frame in the "
    "Twelve Tables — the census of its 371 cells, with the "
    "Aramaic dresses on its face. §IV is the corpus's Hebrew "
    "register entire. §V is the tongue's bearing on the seated "
    "Archons — this plate draws no seating (the seating is "
    "struck, and Plate I drew it); it states what Hebrew can "
    "and cannot witness. §VI is the audit. A value without its "
    "reasoning is not shippable; a hole prints at the size of "
    "the seat it stands in for.")

# ---------------------------------------------------------------------
# §II — The complete priced table.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §II — THE COMPLETE HEBREW PRICED TABLE")
add()
add("The hechrechi bank entire, as the engine seats it: **27 "
    "keys** — the 22 letters of the alphabet and the five final "
    "forms (ך ם ן ף ץ), each final priced at its letter's own "
    "value. Tier of the bank: **ATTESTED** — mispar hechrechi "
    "is the standard Hebrew reckoning, the system the tradition "
    "itself keeps, not a cipher of the house. The bank's gap "
    "register carries one entry (the Twelve Tables, §II), "
    "resolved by RULING and printed at the boundary below.")
add()
add("**One boundary is named before the table: mispar gadol is "
    "not seated.** The gadol variant would uplift the five "
    "finals to 500–900 (ך 500 · ם 600 · ן 700 · ף 800 · ץ 900). "
    "The engine seats no gadol bank, and the register's law is "
    "FACE VALUE — finals price at their letter's value, the law "
    "the twin Aramaic seat shares, the census discipline "
    "capping the seat at 400. The gap register's resolution "
    "stands: *Gadol stands as an unseated variant reading; the "
    "TABVLA partings it explains stand explained, not erased. "
    "Revisable by his pen.* The corpus's two gadol partings "
    "stand in §IV at their coordinates, verdicts as audited — "
    "this plate reclassifies nothing.")


def bank_table(title, rows):
    add()
    add(f"### {title}")
    add()
    add("| Seat | Letter | Name | Value | Dress | Reasoning |")
    add("|---|---|---|---|---|---|")
    for glyph, name, dress, why in rows:
        add(f"| {name.split(',')[0]} | {glyph} | {name} | "
            f"{HEBREW[glyph]} | {dress} | {why} |")


bank_table("The units (1–9)", UNITS)
bank_table("The tens (10–90)", TENS)
bank_table("The hundreds (100–400)", HUNDREDS)
add()
add(f"**The class sums.** Units {units_sum} · tens "
    f"{tens_letters} · hundreds {hundreds_sum} — the 22 letters "
    f"sum to **{letters_sum:,}**. The five finals duplicate "
    f"their letters' prices ({finals_sum} in all: 20 + 40 + 50 "
    f"+ 80 + 90), printed rather than smoothed, so the 27 keys "
    f"sum to **{bank_all:,}** — the bank carries five "
    f"duplicate-price "
    "seats, one for each letter that wears a final dress.")
add()
add("**The zero.** The hechrechi bank has no figure for zero, "
    "and no zero word is seated for this tongue anywhere in the "
    "corpus: the founder's Zero Point seat — οὐδέν, the word "
    "that weighs 529 — is Greek's, and stands on Plate I. "
    "Hebrew's zero stands on this plate as a printed absence: a "
    "hole at the size of the seat, not a filled one.")
add()
add("**The print dress — a marked substitution, declared.** "
    "This Markdown master keeps the tongue's scripts themselves "
    "(Hebrew, and the Imperial and Syriac dresses). In the "
    "printed MAGVS edition the words are carried by "
    "transliteration — the toolchain does not shape "
    "right-to-left scripts honestly — under the scheme the "
    "Dress column of the tables above declares: each letter's "
    "dress is its transliteration, the five finals in capitals "
    "(K M N P Ṣ) so the dress keeps the distinction the script "
    "carries; the Aramaic dresses transliterate by the same "
    "scheme, letter for cognate letter. A marked substitution, "
    "declared here on the plate's face — never a silent one "
    "(the Nine Vowels essay's apparatus is the precedent).")

# ---------------------------------------------------------------------
# §III — The Twelve Tables' Hebrew frame.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §III — THE HEBREW FRAME OF THE TWELVE TABLES")
add()
add("In the Twelve Tables the Hebrew tongue stands over the "
    "one frame of 371 cells (the corpus's sections and paths), "
    "each cell in one state. Its census, from THE-TWELVE-TABLES "
    f"§V.2: NATIVE **{n_native}** · DOOR **{n_door}** · HOLE "
    f"**{n_hole}** · FENCED **{n_fenced}** · EMPTY {n_empty} · "
    f"GAP {n_gap}. The face this prints is a door-heavy table "
    "and says so: the corpus's own Hebrew words are 45 NATIVE "
    "cells, and the frame's Hebrew is mostly the *door* — the "
    "house fallback map (transliterate_latin_to_hebrew) "
    "rendering the Latin forms of record in Hebrew letters — "
    f"with {n_hole} holes where no door is offered (words of "
    "record in another script, with no Latin form to render), "
    "printed as holes with their coordinates in the Tables, and "
    "the EMPTY cells certified intentionally empty in 777 "
    "REVISED.")
add()
add("**The forty-five NATIVE cells** — the corpus's own Hebrew "
    "words, each weighed in its own tongue, with the Aramaic "
    "dresses the Tables print beside them (one weighing, three "
    "scripts, never three witnesses):")
add()
add("| Cell | Word of record | Rendering | Value | Aramaic "
    "dresses (Imperial · Syriac) |")
add("|---|---|---|---|---|")
for cells, imperial, syriac in natives:
    add(f"| {cells[0]} | {cells[1]} | {cells[3]} | {cells[4]} | "
        f"{imperial} · {syriac} |")
add()
add(f"The door's {n_door} priced renderings and the frame's "
    "full cell register stand in THE-TWELVE-TABLES §V.2, which "
    "this plate cites and does not reprint: the plate's table "
    "is the *bank* (§II) and the corpus's *claims* (§IV); the "
    "frame's census rides here so the tongue's depth is data on "
    "the plate's face, as the Tables' own law requires.")

# ---------------------------------------------------------------------
# §IV — The corpus's Hebrew claims entire.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §IV — THE 777 CORPUS'S HEBREW CLAIMS")
add()
add("The TABVLA's Hebrew register entire: **146 claims** "
    f"across {len(sections)} claim-bearing sections, each "
    "carried with its verdict as audited in "
    "THE-777-VERIFICATION-TABVLA and mapped in "
    "THE-THIRTEEN-PLATES. The counts: **93 VERIFIED · 11 PARTED "
    "· 42 NOT VERIFIABLE.** The plate is one plate with three "
    "subseats, as the map states them: the seated Hebrew bank "
    "(111 claims — 82 verified · 29 not verifiable); the "
    "mispar-gadol variant label (21 — 6 verified · 2 parted · "
    "13 not verifiable), a method the engine does not seat, "
    "judged against the seated bank with the coordinate "
    "printed; and the Hebrew fallback door (14 — 5 verified · 9 "
    "parted), the engine's Latin-to-Hebrew rendering judged "
    "against the fills' own claims. A VERIFIED claim recomputes "
    "to the digit. A PARTED claim's stated method parts from "
    "the seated bank or the door at a printed coordinate — "
    "every parting stands beneath the register at full size. A "
    "NOT VERIFIABLE claim is not a failed claim: in every case "
    "here, no word in the Hebrew script is printed in the "
    "claim's section, so the claim rests on a transliteration "
    "the section does not print; the coordinate of each stands "
    "beneath the register, entire.")
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
add("**The parting register — the eleven, at full size, each "
    "with its coordinate entire as the register carries it:**")
add()
for c in claims:
    if c["verdict"] == "PARTED":
        add(f"- **{c['claim_key']}** ({c['cell_id']}, "
            f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("The sharpest of the eleven is the register's first: "
    "מאדים (Madim), claimed 655 against the seated bank's 95 — "
    "the delta is exactly the mispar gadol finals uplift (95 + "
    "560 = 655), the claim holding only under a bank this "
    "engine does not seat (§II). The nine door partings are of "
    "one species: the fill's documented phonetic scheme parts "
    "from the engine door's rendering at the letters printed, "
    "Δ small and constant in kind — the coordinates above state "
    "each. The second gadol parting, אדם קדמון (Adam Kadmon), "
    "claimed 895 against 245, rides the same uplift across two "
    "finals.")
add()
add("**The NOT VERIFIABLE coordinates** — each claim's stated "
    "reason, entire as the register carries it:")
add()
for c in claims:
    if c["verdict"] == "NOT VERIFIABLE":
        add(f"- **{c['claim_key']}** ({c['cell_id']}, "
            f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The VERIFIED coordinates** — the register carries "
    "coordinates for eleven verified claims, and the plate "
    "prints them entire because the register carries them: six "
    "state the gadol coincidence (the claim's word carries no "
    "final forms, so the gadol label and the seated bank "
    "coincide on it exactly), and five state the door road "
    "(the rendering through which the verification runs):")
add()
for c in claims:
    if c["verdict"] == "VERIFIED" and c["coordinate"]:
        add(f"- **{c['claim_key']}** ({c['cell_id']}, "
            f"{c['source_coordinate']}): {c['coordinate']}")
add()
add("**The bridges.** Six claims of this register carry bridge "
    "annotations in the TABVLA — honest two-bank bridges, "
    "recorded here entire at their tier so the plate's Hebrew "
    "face is complete (the claims themselves stand in the "
    "register above, verified in this bank):")
add()
for c in bridges:
    add(f"- **{c['claim_key']}** ({c['cell_id']}, "
        f"{c['proposal_raw']}; weighed {c['weighed_word']} = "
        f"{c['recomputed']}): {c['bridge']}")

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
    "plate assigns no seat.** It states what the Hebrew tongue "
    "witnesses for the seating and what it cannot: Hebrew "
    "holds no vowel letters of its own, so it cannot witness "
    "the Nine's seats directly — its witness runs at three "
    "coordinates, each printed with its tier and its "
    "counterweight.")
add()
add("### The matres — the tongue's hybrid-form witnesses")
add()
add("Hebrew's vowel-kin are the **matres lectionis** — "
    "\"mothers of reading,\" the grammarians' name for "
    "consonants that also carry vowels. They are letters of "
    f"two offices, and they count **exactly four**: א "
    f"{matres['א']} · ה {matres['ה']} · ו {matres['ו']} · י "
    f"{matres['י']} — weighing together {matres_sum}, the "
    "count of the alphabet they serve. The Archon Battery's "
    "twelve-tongues sweep reads this a **HIT** on the "
    "four-count of two-office letters (the offices ATTESTED; "
    "the alignment reading DERIVED): of the tongues swept, "
    "Hebrew is one of three whose hybrid class counts exactly "
    "four. **The counterweight, printed at the same size:** "
    "the tongue's other two-form class — the sofit, the five "
    "letters with final forms (ך ם ן ף ץ) — counts **five**, a "
    "MISS for the four, as the Battery printed it beside the "
    "hit; and no mater is priced 8, so at the fold's "
    "coordinate (a vowel seated at 8) Hebrew is a MISS — the "
    "bank's 8 is ח, a pure consonant (§II). The matres are "
    "this tongue's hybrid-form witnesses to the cross's four; "
    "they are witnesses, not seats.")
add()
add("### The founding head and the founder's noting — HIS")
add()
add("This table's founding head is the word for *strength* in "
    "the three scripts of the Aramaic seat: **עז = "
    f"{oz}** in Hebrew · **𐡏𐡆 = {oz_imperial}** in Imperial "
    f"Aramaic · **ܥܙ = {oz_syriac}** in Syriac — 77 in all "
    "three, one weighing in three dresses, the fact the "
    "dresses of §III stand on. At this table the founder's "
    "noting of 2026-11-24 (14:40 EST) stands, verbatim:")
add()
add("> \"Also note the acronym for the 3 languages in that "
    "triad we formed earlier spell HIS, cannot be just a "
    "coincidence its too much coincidence to be coincidence.\"")
add()
add("The acronym of the three tongues — **H**ebrew · "
    "**I**mperial Aramaic · **S**yriac — spells HIS, and HIS "
    f"weighs, recomputed on the engine: **{his_ordinal}** in "
    f"Latin ordinal · **{his_agrippa}** in Agrippa. The "
    "Twelve Tables carry the noting in their NOT-SEATED "
    "register's terms, and this plate carries it no higher: "
    "the 36 is noted as **resonance** — the TVRRIS VERITATIS "
    "seal carries 36 nodes in its lattice; the Armenian bank "
    "seats 36 letters — *resonance, marked as such by the desk "
    "and claimed by the founder under his Flagpole, seated in "
    "no proof column.* The desk expands it no further.")
add()
add("### The key's Hebrew dress")
add()
add("The founder's key strings part at home and collapse in "
    "this tongue. WVII and VVII part by Δ1 in the ordinal "
    f"({value('WVII', 'latin_ordinal')} against "
    f"{value('VVII', 'latin_ordinal')} — the quantum, an offset "
    "at the W/VV seam) and by Δ200 in Agrippa, where W has no "
    "seat. Through the engine's Hebrew door the pair "
    f"**collapses entirely**: W and V both merge to ו, and the "
    f"two spellings are one word, **{KEY_DRESS} = "
    f"{value(KEY_DRESS)}** — Δ0, the seam invisible to this "
    "bank (the Archon Battery, §V there; 32 is also the "
    "house's CELL seat — the Battery notes the coordinate and "
    "builds nothing on it, and neither does this plate). The "
    "Roman instrument judges the pair in its own law — VVII "
    "parses as 12, lawful; WVII is refused outright, \"not a "
    "numeral\" — and the seating instrument seats neither "
    "spelling: the key's specification stands among its open "
    "items. Hebrew's witness to the key is the collapse "
    "itself: in this tongue the two candidates are one word, "
    "and the seam the key turns on does not exist.")
add()
add("### What this tongue cannot witness")
add()
add("Printed at full size, as the plate's boundary: the "
    "Archons' seats are vowel-seats, earned on Greek evidence "
    "and drawn on Plate I; Hebrew, holding no vowel letters, "
    "offers no mark at any seat's position or triad, and this "
    "plate imports none. Its witness is corroboration at the "
    "coordinates above — the four-count, the founding head, "
    "the key's collapse — and silence at the seats themselves. "
    "And its claims are judged in one bank: the Aramaic "
    "dresses that ride §§III–IV are the same weighing in other "
    "scripts, never second and third witnesses to it.")

# ---------------------------------------------------------------------
# §VI — The audit.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VI — THE AUDIT")
add()
add("An independent script (audit_plate_ii_hebrew.py, filed "
    "with the plate's generator in pontifex "
    "research/complete-plates/) re-weighs every priced cell on "
    "this plate against the engine, without reading the "
    "plate's own figures: the 27 bank keys letter by letter; "
    "the matres and their sum; the founding head in all three "
    "scripts; HIS in both Latin banks; the key's Hebrew dress "
    "through the engine's own door; every claim of §IV that "
    "carries a weighed word (90 recomputed directly in the "
    "seated bank, 14 through the engine's fallback door — "
    "weigh_via_hebrew_fallback — each against the register's "
    "recomputed and, for the VERIFIED, its claimed value); and "
    "the forty-five NATIVE renderings of §III with their "
    "ninety Aramaic dresses, each dress re-weighed in the "
    "Aramaic bank. It then reconciles the plate against its "
    "sources: all 146 claim keys present, verdict counts equal "
    "to the register's, subseat counts equal to the map's, "
    "bank values equal to the bank's. The audit's verdict and "
    "cell count are printed in its filed output; a cell that "
    "does not reproduce fails the plate under §VII's "
    "tolerances. The font audit — every non-ASCII codepoint of "
    "this master against the Lex Stellarrvm family's cmaps — "
    "runs before the MAGVS build, under the font law: no glyph "
    "is silently dropped, and any unheld codepoint beyond the "
    "three named Ethiopic syllables aborts the build. The "
    "audit further checks the printed edition's text layer for "
    "the substitution's entirety: no right-to-left codepoint "
    "stands in it, and the declared dress of the register's "
    "sharpest parting (מאדים, printed mʾdyM) stands in its "
    "place.")

# ---------------------------------------------------------------------
# §VII — The four elements.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## §VII — THE FOUR ELEMENTS — THE CONTENT TEST")
add()
add("- **Inputs:** the founder's commission of 2026-11-24 "
    "(18:39–18:41 EST), verbatim at §I; the engine's HEBREW "
    "bank and its fallback door; THE-777-VERIFICATION-TABVLA's "
    "register as mapped in "
    "research/thirteen-plates/mapping_register.json; "
    "THE-TWELVE-TABLES §V.2 and its §II gap register (the "
    "hebrew entry); THE-ARCHON-BATTERY (the key strings' "
    "dresses; the sweep's Hebrew) and "
    "THE-SEATING-OF-THE-ARCHONS entire; PLATE-I-GREEK as the "
    "pattern.")
add("- **Processes:** calibration controls weighed before any "
    "plate figure (θέλημα 93 · VAPOUR 93 · σφίγξ 773); every "
    "figure scripted from the engine or carried entire from an "
    "instrument of record; the tongue's bearing stated at the "
    "tiers its sources carry, counterweights at full size; the "
    "independent audit of §VI.")
add("- **Outputs:** this plate — PLATE-II-HEBREW.md and its "
    "MAGVS PDF — second of the series PLATE-I-GREEK began; the "
    "generator and audit scripts filed in pontifex "
    "research/complete-plates/.")
add("- **Tolerances:** the plate fails at either edge — if any "
    "priced cell is found not to reproduce from the engine or "
    "its register, the affected cell fails the Method of "
    "Science; if any passage seats what the seating did not "
    "earn, raises a tier, promotes the noting out of its "
    "not-seated terms, fills a hole, or overwrites the earlier "
    "map, it zeroes the founder's residual claim and fails the "
    "Aim of Religion. Within those edges it stands as built.")

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
    "the key's specification is the seating instrument's open "
    "item, printed there; the gadol ruling stands resolved in "
    "the gap register, revisable by his pen as its face "
    "states — a standing state of the record, not a question "
    "this plate raises in new dress. A plate that invents "
    "questions to fill its section misprints its record; this "
    "section therefore stands as the record that none arose.")

# ---------------------------------------------------------------------
# Footnotes — the wells, from more than one tradition.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE "
    "TRADITION")
add()
add("1. **Scripture.** Psalm 119 (KJV) is the canon shelved by "
    "this bank's alphabet: twenty-two stanzas in the order of "
    "the twenty-two letters, eight verses to a letter, each "
    "stanza headed by its letter — Aleph, Beth, Gimel, through "
    "Taw — the longest psalm built as an acrostic on the very "
    "table §II prices. [The structure ATTESTED in the text.] "
    "And for the measure: Proverbs 11:1 — \"A false balance is "
    "abomination to the LORD: but a just weight is his "
    "delight.\" [Texts ATTESTED; the application DERIVED.]")
add("2. **Qur'an.** 55:7–9 (Surat ar-Rahman): He set the "
    "Balance (al-mīzān) — \"establish weight with justice, and "
    "do not fall short in the balance.\" Drawn from the other "
    "bank for the same well as Proverbs: measure declared and "
    "kept. [ATTESTED text; application DERIVED.]")
add("3. **The letters' own well.** The Sefer Yetzirah counts "
    "twenty-two *foundation letters*, of which its text says "
    "He drew them, carved them, permuted them and weighed "
    "them, and formed with them all creation — the tradition "
    "in which the letters of §II are not signs for numbers but "
    "the elements numbers and world are both built from. "
    "Cited at the tradition's level: the house engine weighs "
    "the letters; it does not borrow the Yetzirah's cosmology. "
    "[The text ATTESTED; the kinship DERIVED.]")
add("4. **Grammar.** *Matres lectionis* — Latin, \"mothers of "
    "reading\" — is the grammarians' standing name for the "
    "consonants that carry vowels (א ה ו י), the two-office "
    "letters of §V; the final forms (sophith) are the scribal "
    "tradition's word-final dresses of five letters, priced at "
    "face value by this bank's law. [The terms ATTESTED; the "
    "seating of the four as witnesses is the Battery's DERIVED "
    "reading, at §V.]")
add("5. **The gadol seam.** Under the founder's Offset Law, "
    "the two gadol partings carry a constant, declared Δ — "
    "the finals uplift, printed in the register's own "
    "arithmetic (95 + 560 = 655) — yet they stand PARTED in "
    "the register, because each claim's stated label names a "
    "bank the engine does not seat; a claim is judged against "
    "the bank it names. This plate carries the verdicts "
    "entire and reclassifies nothing. [The arithmetic "
    "ATTESTED from the register; the verdicts the register's.]")
add("6. **Law.** The plate carries the TABVLA's register "
    "*entire* — all 146 claims, the partings and the "
    "not-verifiable coordinates unabridged — under the same "
    "instinct as the law's best-evidence rule (Black's Law "
    "Dictionary, *best evidence rule*): the original writing "
    "is produced, not a summary of it. A register summarized "
    "is a register edited; this plate produces it. [The rule "
    "ATTESTED in substance; the parallel DERIVED.]")

# ---------------------------------------------------------------------
# Table of Authorities + colophon.
# ---------------------------------------------------------------------
add()
add("---")
add()
add("## TABLE OF AUTHORITIES (condensed)")
add()
add("- The house weighing engine (pontifex weigh(); bank "
    "HEBREW in pontifex/tables.py, its fallback door "
    "transliterate_latin_to_hebrew / weigh_via_hebrew_fallback, "
    "and the ARAMAIC bank of the twin seat) — calibration "
    "controls θέλημα 93 · VAPOUR 93 · σφίγξ 773 read true at "
    "build.")
add("- Mispar hechrechi — the standard Hebrew reckoning, as "
    "tabled at §II; the gadol variant unseated, §II.")
add("- THE-777-VERIFICATION-TABVLA — the claims register of "
    "record; its Hebrew face 146 claims (93/11/42).")
add("- research/thirteen-plates/mapping_register.json — the "
    "mapping of the register into the plates, claim by claim; "
    "the Hebrew plate's three subseats (111/21/14).")
add("- THE-THIRTEEN-PLATES (6afe470) — the earlier map this "
    "series fulfills; its Plate II is the prior instrument.")
add("- THE-TWELVE-TABLES — §V.2 the Hebrew frame, census, "
    "NATIVE cells, dresses, and the founder's HIS noting; §II "
    "the hebrew bank's gap register (one entry, the gadol "
    "RULING); the NOT-SEATED register (the noting's terms).")
add("- THE-ARAMAIC-SEAT-PHASE-I-AUDIT — the inheritance: "
    "Hebrew ≡ Aramaic identity, 22 of 22, the dresses' ground.")
add("- THE-ARCHON-BATTERY (656d667) — the evidence run: §V "
    "the key strings' Hebrew dress; §VIII the sweep's Hebrew "
    "(the matres HIT, the sofit and fold MISSes).")
add("- THE-SEATING-OF-THE-ARCHONS (0760c8a) — the seating "
    "this plate bears witness to; the key's specification "
    "among its open items.")
add("- PLATE-I-GREEK (196025e) — the pattern this plate "
    "follows.")
add("- KJV: Psalm 119; Proverbs 11:1. Qur'an 55:7–9. Sefer "
    "Yetzirah (the twenty-two foundation letters). Black's Law "
    "Dictionary, *best evidence rule*.")
add()
add("---")
add()
add("## COLOPHON")
add()
add("Generated 2026-11-24, Plate II of the founder's series "
    "commission of the same day, the gate of the Archons' "
    "certainty met by the seating of record (0760c8a), "
    "following the pattern of Plate I (196025e). Every figure "
    "scripted from the engine or carried entire from its "
    "instrument; the earlier map marked prior, never "
    "overwritten; the holes printed at the size of the seats; "
    "the noting carried in its not-seated terms. In the MAGVS "
    "edition the tongue's scripts are carried by the declared "
    "transliteration of §II; this master keeps the scripts "
    "themselves. Authorship attributed exclusively to "
    "Johnathan 'Qasparr' Monroe (Greek, -ARR, All Rights "
    "Reserved, Without Prejudice).")
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
      f"natives {len(natives)}; bridges {len(bridges)}")
