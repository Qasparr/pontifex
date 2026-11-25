#!/usr/bin/env python3
# =============================================================================
# 93 — build_class_walk_map.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXIV day of November, Dies Martis, Sol in Sagittarius,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: generates THE-CLASS-WALK-MAP.md, the MAGVS instrument
# that maps the twelve tongues by the CLASS-WALK — the stepping
# operation the founder named from the INRI · JHS audit (the
# Triple H / ΩΠΗ finding, pontifex d5250ac) and commissioned by
# his tap of 2026-11-24, 21:59 EST. Every step of every walk is
# taken from the engine's banks at build, controls first
# (θέλημα 93 · VAPOUR 93 · σφίγξ 773); a figure the engine does
# not return is not printed. The walks are recomputed here,
# never copied from the desk's Greek proof of concept — the
# proof is checked against the recomputation, not transcribed.
#
# DOCTRINE: a class-walk steps one digit (or the tongue's native
# stepping axis) through the tongue's classes; every step is
# graded ARCHON (the holder is a vowel seat of the Nine, as that
# tongue's plate files its vowels) · STRANGER (a consonant) ·
# HOLE (no letter stands there). Where a tongue's axis is not
# letter-classes, the grades translate as the tongue files them
# and the section prints its translation. Every walk's BREAK
# COORDINATE is printed — the zero-point method: the exact step
# where the vowel line ends. The map assigns no seat and makes
# no ruling; its register is observation, DERIVED over the
# banks, the pattern-reading CONSTRUCTED as all pattern-readings
# are.
#
# CONTENT TEST: Inputs — the engine's banks entire, the twelve
# plates and their filings, the Archon battery, the seating,
# the INRI · JHS audit. Processes — the walks computed per
# tongue on its own axis, graded, their breaks taken; the
# hybrids walked by components; the summary counted. Outputs —
# the Markdown master beside the plates. Tolerances — every
# printed step recomputed by the independent audit; a step
# that does not reproduce fails the map.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh, hangul
from pontifex.tables import (GREEK, COPTIC, CYRILLIC, GLAGOLITIC,
                             GEORGIAN, ARMENIAN, ARABIC_ABJAD,
                             HEBREW, LATIN_ORDINAL, AGRIPPA, KANA,
                             GEEZ, HALEHAME, HANGUL_INITIAL,
                             HANGUL_VOWEL, HANGUL_FINAL,
                             _GEEZ_BASES, _GEEZ_LABIOVELAR_HEADS,
                             _GEEZ_LABIOVELAR_OFFSETS,
                             _GEEZ_EIGHTH_SLOT_HOLE,
                             _HANGUL_SK_INITIAL, _HANGUL_SK_VOWEL,
                             _HANGUL_SK_FINAL, _HANGUL_DIGRAPH_FINALS,
                             _jamo_conjoining)
from pontifex.numerals import repeat_status

BASE = (Path.home() / "workspace/goals/"
        "cross-gematria-777-gap-filling/files")
MASTER = BASE / "THE-CLASS-WALK-MAP.md"


def W(word, bank):
    return weigh(word, bank)["value"]


def root_chain(n):
    chain = [n]
    while chain[-1] >= 10:
        chain.append(sum(int(d) for d in str(chain[-1])))
    return chain


# --- controls, before any figure is taken -------------------------
assert W("θέλημα", "greek") == 93
assert W("VAPOUR", "latin_ordinal") == 93
assert W("σφίγξ", "greek") == 773

# --- the founding coordinates (the INRI · JHS audit, d5250ac) -----
assert W("ΗΗΗ", "greek") == 24
assert W("HHH", "latin_ordinal") == 24
assert W("HHH", "agrippa") == 24
assert W("ΙΗΣΟΥΣ", "greek") == 888
assert root_chain(888) == [888, 24, 6]
assert W("ΩΠΗ", "greek") == 888 and W("Π", "greek") == 80

# =====================================================================
# The walk machinery for the classed banks. A walk is a list of
# steps; a step is a list of holders (letter, value, grade) — one
# holder, except at a fork. Grades: ARCHON / STRANGER / HOLE.
# =====================================================================

CLASS3 = ["units", "tens", "hundreds"]
CLASS4 = ["units", "tens", "hundreds", "thousands"]


def cell_text(step):
    """One step as it prints: holders joined, a star on archons."""
    if not step:
        return "— HOLE"
    parts = []
    for letter, value, grade in step:
        parts.append(f"{letter} {value}" +
                     (" ★" if grade == "ARCHON" else ""))
    return " + ".join(parts)


def step_grade(step):
    if not step:
        return "HOLE"
    if any(g == "ARCHON" for _l, _v, g in step):
        return "ARCHON"
    return "STRANGER"


def analyze(steps, classnames):
    """The walk's counts and its break coordinate, by the
    instrument's law: the break is the first non-archon step
    after the first archon step; a return is a later archon."""
    grades = [step_grade(s) for s in steps]
    archon_at = [i for i, g in enumerate(grades) if g == "ARCHON"]
    n_archon = sum(1 for s in steps for _l, _v, g in s
                   if g == "ARCHON")
    n_steps_archon = len(archon_at)
    both_ends = bool(grades) and grades[0] == "ARCHON" \
        and grades[-1] == "ARCHON"
    if not archon_at:
        brk = "no line — no archon stands on this walk"
    else:
        brk = None
        ret = None
        for i in range(archon_at[0] + 1, len(grades)):
            if grades[i] != "ARCHON":
                brk = i
                break
        if brk is None:
            if archon_at[0] == len(grades) - 1:
                brk = ("late-standing — the archon stands at the "
                       "final step; nothing follows it to break")
            elif archon_at[0] > 0:
                brk = (f"stands late at the "
                       f"{classnames[archon_at[0]]} step and runs "
                       f"unbroken to the final step")
            else:
                brk = "unbroken — the line runs to the final step"
        else:
            for j in range(brk + 1, len(grades)):
                if grades[j] == "ARCHON":
                    ret = j
                    break
            brk = (f"break at the {classnames[brk]} step "
                   f"({cell_text(steps[brk])})")
            if ret is not None:
                brk += (f" · return at the {classnames[ret]} step "
                        f"({cell_text(steps[ret])})")
    return {"grades": grades, "archon_holders": n_archon,
            "archon_steps": n_steps_archon, "both_ends": both_ends,
            "break": brk}


def milesian_walks(seats, vowels, bank, extra_seats=()):
    """The 27-seat Milesian walks: seats in received order
    (9 units, 9 tens, 9 hundreds); every seat's price asserted
    against the bank and against its class value."""
    assert len(seats) == 27
    classes = [seats[0:9], seats[9:18], seats[18:27]]
    walks = []
    for d in range(1, 10):
        steps = []
        for ci, cls in enumerate(classes):
            letter = cls[d - 1]
            value = d * (10 ** ci)
            assert bank[letter] == value, (letter, value)
            grade = "ARCHON" if letter in vowels else "STRANGER"
            steps.append([(letter, value, grade)])
        walks.append(steps)
    return walks


def walk_rows(walks, classnames):
    rows = []
    for d, steps in enumerate(walks, 1):
        a = analyze(steps, classnames)
        cells = [cell_text(s) for s in steps]
        rows.append((d, cells, a))
    return rows


def totals_line(name, rows):
    a_steps = sum(r[2]["archon_steps"] for r in rows)
    holders = sum(r[2]["archon_holders"] for r in rows)
    walks_with = sum(1 for r in rows if r[2]["archon_steps"])
    both = [str(r[0]) for r in rows if r[2]["both_ends"]]
    return (f"**{name} totals:** archon-steps {a_steps} "
            f"(archon holders {holders}) · walks carrying archons "
            f"{walks_with} of {len(rows)} · both-ends walks "
            f"{len(both)}" +
            (f" (walk {', '.join(both)})" if both else "") + ".",
            a_steps, walks_with, both)


def emit_walk_table(L, rows, classnames, extra_cols=()):
    head = "| Walk | " + " step | ".join(
        c.capitalize() for c in classnames) + " step | " + \
        " | ".join(extra_cols + ("Archon-steps", "Break coordinate")) \
        + " |"
    L.append(head)
    L.append("|" + "---|" * (len(classnames) + len(extra_cols) + 3))
    for d, cells, a in rows:
        L.append(f"| {d} | " + " | ".join(cells) +
                 f" | {a['archon_steps']} | {a['break']} |")
    L.append("")


# --- the seat orders, as the plates file them ----------------------
GREEK_SEATS = ["α", "β", "γ", "δ", "ε", "ϛ", "ζ", "η", "θ",
               "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ϟ",
               "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω", "ϡ"]
GREEK_VOWELS = {"α", "ε", "η", "ι", "ο", "υ", "ω"}
assert sum(GREEK[s] for s in GREEK_SEATS) == 4995
assert GREEK["ς"] == 200 and GREEK["στ"] == 6  # duplicate-price keys

COPTIC_SEATS = ["ⲁ", "ⲃ", "ⲅ", "ⲇ", "ⲉ", "ⲋ", "ⲍ", "ⲏ", "ⲑ",
                "ⲓ", "ⲕ", "ⲗ", "ⲙ", "ⲛ", "ⲝ", "ⲟ", "ⲡ", "ϥ",
                "ⲣ", "ⲥ", "ⲧ", "ⲩ", "ⲫ", "ⲭ", "ⲯ", "ⲱ", "ⳁ"]
COPTIC_VOWELS = {"ⲁ", "ⲉ", "ⲏ", "ⲓ", "ⲟ", "ⲩ", "ⲱ"}
COPTIC_FENCED = ["ϣ", "ϧ", "ⳉ", "ϩ", "ϫ", "ϭ", "ϯ"]
COPTIC_FENCED_NAMES = ["SHEI", "KHEI", "AKHMIMIC KHEI", "HORI",
                       "GANGIA", "SHIMA", "DEI"]
assert sum(COPTIC[s] for s in COPTIC_SEATS) == 4995
for ch in COPTIC_FENCED:
    assert ch not in COPTIC and W(ch, "coptic") == 0

CYR_SEATS = ["А", "В", "Г", "Д", "Е", "Ѕ", "З", "И", "Ѳ",
             "І", "К", "Л", "М", "Н", "Ѯ", "О", "П", "Ч",
             "Р", "С", "Т", "У", "Ф", "Х", "Ѱ", "Ѡ", "Ц"]
CYR_VOWELS = {"А", "Е", "И", "І", "О", "У", "Ѡ"}
CYR_VARIANTS = {400: ["Ѵ", "Ꙋ", "Ѹ"], 800: ["Ѿ", "Ꙍ"], 900: ["Ѧ"]}
assert sum(CYRILLIC[s] for s in CYR_SEATS) == 4995
assert sum(CYRILLIC.values()) == 8695
for v, forms in CYR_VARIANTS.items():
    for f in forms:
        assert CYRILLIC[f] == v

ARM_CLASSES = [["Ա", "Բ", "Գ", "Դ", "Ե", "Զ", "Է", "Ը", "Թ"],
               ["Ժ", "Ի", "Լ", "Խ", "Ծ", "Կ", "Հ", "Ձ", "Ղ"],
               ["Ճ", "Մ", "Յ", "Ն", "Շ", "Ո", "Չ", "Պ", "Ջ"],
               ["Ռ", "Ս", "Վ", "Տ", "Ր", "Ց", "Ւ", "Փ", "Ք"]]
ARM_VOWELS = {"Ա", "Ե", "Ը", "Ի", "Ո", "Ւ"}
assert sum(ARMENIAN.values()) == 49995

GEO_CLASSES = [["ა", "ბ", "გ", "დ", "ე", "ვ", "ზ", "ჱ", "თ"],
               ["ი", "კ", "ლ", "მ", "ნ", "ჲ", "ო", "პ", "ჟ"],
               ["რ", "ს", "ტ", None, "ფ", "ქ", "ღ", "ყ", "შ"],
               ["ჩ", "ც", "ძ", "წ", "ჭ", "ხ", "ჴ", "ჯ", "ჰ"]]
GEO_VOWELS = {"ა", "ე", "ი", "ო", "უ"}
GEO_FORK = [("ჳ", 400), ("უ", 400)]
assert sum(GEORGIAN.values()) == 60395
assert GEORGIAN["ჵ"] == 10000

ARA_CLASSES = [["ا", "ب", "ج", "د", "ه", "و", "ز", "ح", "ط"],
               ["ي", "ك", "ل", "م", "ن", "س", "ع", "ف", "ص"],
               ["ق", "ر", "ش", "ت", "ث", "خ", "ذ", "ض", "ظ"]]
ARA_MATRES = {"ا", "و", "ي"}
assert sum(ARABIC_ABJAD.values()) == 5995
assert ARABIC_ABJAD["غ"] == 1000 and W("ة", "arabic_abjad") == 0

GLA_CLASSES = [[("Ⰰ", 1), ("Ⰱ", 2), ("Ⰲ", 3), ("Ⰳ", 4), ("Ⰴ", 5),
                ("Ⰵ", 6), ("Ⰶ", 7), ("Ⰷ", 8), ("Ⰸ", 9)],
               [("Ⰹ", 10), ("Ⰻ", 20), ("Ⰼ", 30), ("Ⰽ", 40),
                ("Ⰾ", 50), ("Ⰿ", 60), ("Ⱀ", 70), ("Ⱁ", 80),
                ("Ⱂ", 90)],
               [("Ⱃ", 100), ("Ⱄ", 200), ("Ⱅ", 300), ("Ⱆ", 400),
                ("Ⱇ", 500), ("Ⱈ", 600), ("Ⱉ", 700), ("Ⱋ", 800),
                ("Ⱌ", 900)],
               [("Ⱍ", 1000), ("Ⱎ", 2000), ("Ⱏ", 3000),
                ("Ⱑ", 4000), ("Ⱓ", 5000), None, None, None,
                ("Ⱔ", 9000)]]
GLA_VOWELS = {"Ⰰ", "Ⰵ", "Ⰹ", "Ⰺ", "Ⰻ", "Ⱁ", "Ⱆ", "Ⱑ"}
GLA_ALT_10 = ("Ⰺ", 10)
GLA_RUN_HOLES = [("Ⱊ", "the hundreds run, between Ⱉ 700 and Ⱋ 800"),
                 ("Ⱐ", "the thousands run, between Ⱏ 3000 and "
                        "Ⱑ 4000"),
                 ("Ⱒ", "the thousands run, between Ⱑ 4000 and "
                        "Ⱓ 5000")]
assert sum(GLAGOLITIC.values()) == 29005
assert sum(v for v in GLAGOLITIC.values() if v <= 900) == 5005
for ch, _where in GLA_RUN_HOLES:
    assert ch not in GLAGOLITIC and W(ch, "glagolitic") == 0
assert GLAGOLITIC["Ⰷ"] == 8 and "Ⰷ" not in GLA_VOWELS

# =====================================================================
L = []
A = L.append
A("![The Doctrine's Logo — TVRRIS VERITATIS seal](~/workspace/templates/doctrine-logo.png)")
A("")
A("# THE TWELVE TONGUES — A MAP")
A("")
A("**THE CLASS-WALK MAP**")
A("")
A("*Subtitle:* A Scientific Illuminist treatment of the twelve tongues "
  "under one operation — the CLASS-WALK, the stepping of a digit "
  "through a tongue's classes, named by the founder from the "
  "INRI · JHS audit's Triple H finding and commissioned by his tap "
  "of 2026-11-24 (21:59 EST). Every step of every walk is graded "
  "ARCHON, STRANGER, or HOLE, and every walk's break coordinate is "
  "printed: where each tongue's vowel line stands, where it breaks, "
  "and where — in one walk of one family — it comes back.")
A("")
A("Authorship attributed exclusively to Johnathan 'Qasparr' Monroe "
  "(Greek, -ARR, All Rights Reserved, Without Prejudice)")
A("XXIV day of November, Dies Martis, Sol in Sagittarius, "
  "Anno V:xii e.n. (2026 e.v.)")
A("")
A("Classification: Enterprise • Educational • Research & Development")
A("Method of Science, Aim of Religion")
A("")
A("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, All "
  "Rights Reserved, Without Prejudice. Right of claim hereby reserved "
  "and coined under the authority of the Living Man.")
A("")
A("---")
A("")
A("## §I — THE INSTRUMENT")
A("")
A("**The commission.** At the close of the day the thirteen plates "
  "landed and the INRI · JHS audit was weighed against the engine, "
  "the founder put the question the audit had left standing in its "
  "§V — the 888 cypher and its numeral dress — in instrument form "
  "(2026-11-24, 21:57–21:59 EST): if Η written three times weighs "
  "24, and 888 written as a numeral is the same 8 stepped through "
  "its classes with a stranger at the center, *can the stepping "
  "itself be used to map the other hybrids, the tongues, and the "
  "dialects?* His tap answered it: *\"Build the Class-Walk Map — "
  "all twelve tongues, MAGVS, pushed and posted.\"* This map is "
  "that build.")
A("")
A("**The definition, printed on the map's face.** A CLASS-WALK steps "
  "one digit (or the tongue's native stepping axis) through the "
  "tongue's classes. Every step is graded:")
A("")
A("- **ARCHON** — the step's holder is a vowel seat of the Nine, as "
  "that tongue's plate files its vowels;")
A("- **STRANGER** — the step's holder is a consonant;")
A("- **HOLE** — no letter stands there: silence in the bank, an "
  "unassigned cell, or a step the tongue never cut;")
A("- **FENCED** — a letter stands there and the tradition itself "
  "leaves it unvalued (one tongue's species, §III).")
A("")
A("Every walk's **BREAK COORDINATE** is printed — the zero-point "
  "method the founder ruled for every comparison (2026-10-27): not "
  "a verdict blob but the exact step where the vowel line ends. A "
  "break is the first non-archon step after a walk's first archon "
  "step; a walk that breaks and stands again on an archon prints "
  "its **RETURN** coordinate as well; a walk carrying no archon has "
  "no line and therefore no break; a walk whose archon stands at "
  "its final step is **late-standing**. The counts on each face "
  "are counted from the walks, never estimated.")
A("")
A("**The grade translations.** Five of the twelve tongues step on "
  "axes that are not letter-classes — Hebrew on final forms, Latin "
  "between its two banks, Japanese down its vowel columns, Ge'ez "
  "through its orders, Korean across its strata. In those sections "
  "the grades translate as the tongue files them, the translation "
  "is printed at the section's head, and no grade is forced onto an "
  "axis that does not bear it. Whether the translations stand as "
  "the instrument's standing convention is the founder's pen "
  "(§XVIII) — the map prints them as its own working dress, marked.")
A("")
A("**The founding coordinates** (the INRI · JHS audit, pontifex "
  "d5250ac, re-weighed at this build): ΗΗΗ = 24 in the Greek bank, "
  "and HHH = 24 in *both* Latin banks — the tripled 8 weighs the "
  "same in three banks. ΙΗΣΟΥΣ = 888, and 888 reduces 888 → 24 → 6: "
  "the cypher resolves to the Triple H's weight, then to MIRROR's "
  "price. And 888's numeral dress, ΩΠΗ, is the Greek 8-walk read "
  "as a numeral — Η at the units step, Π the stranger at the tens, "
  "Ω the archon returned at the hundreds. This map is that one "
  "walk, walked through all twelve tongues.")
A("")
A("**What this map is not.** It assigns no seat, names no Archon, "
  "and rules nothing. The seating stands on its own instrument "
  "(THE-SEATING-OF-THE-ARCHONS, 0760c8a); the map's register is "
  "observation — DERIVED over the banks it walks, the "
  "pattern-readings CONSTRUCTED as all pattern-readings are, each "
  "summary claim carrying the evidence that would kill it (§XV).")
A("")
# =====================================================================
# §II — GREEK, the type walk
# =====================================================================
gr_walks = milesian_walks(GREEK_SEATS, GREEK_VOWELS, GREEK)
gr_rows = walk_rows(gr_walks, CLASS3)
gr_totals, GR_A, GR_W, GR_BOTH = totals_line("Greek", gr_rows)

A("## §II — GREEK: THE TYPE WALK")
A("")
A("The Milesian bank entire, as Plate I files it: 27 seats in the "
  "received order — nine units, nine tens, nine hundreds — the "
  "seven simple vowels of the Nine among them (Α Ε Η Ι Ο Υ Ω; the "
  "hybrids walk in §XIV). Two further keys of the bank are not "
  "seats and are not walked: final ς, a duplicate price at 200, and "
  "the στ digraph, a duplicate price at ϛ's seat — forms at their "
  "prices, as the plate files them, not steps. Each walk below "
  "steps one digit through the three classes; a ★ marks an archon "
  "step.")
A("")
emit_walk_table(L, gr_rows, CLASS3)
A(gr_totals)
A("")
A("**The readings.** Walk 1 stands on archons twice — Α at home, Ι "
  "at the tens — and breaks at the hundreds, where Ρ is a "
  "stranger: the line that opens the bank cannot finish it. Walks "
  "4 and 7 carry their archons late — Υ at the far end of walk 4, "
  "Ο at the middle of walk 7 — and print late-standing and "
  "mid-standing respectively, no break, because no archon stood "
  "before them to be broken from. Walk 5 breaks at the first step "
  "it takes: Ε is an archon at home and both its class-brothers "
  "are strangers. And walk 8 is the map's type specimen, the walk "
  "the founder named the instrument from: **Η at home, the break "
  "at Π in the tens, the return at Ω in the hundreds — the only "
  "both-ends walk in the Greek bank, and, its mirrors apart (the "
  "same walk in other dresses, §§III–IV), the only walk in any "
  "classed tongue whose line breaks and comes back.** Read as a "
  "numeral it is ΩΠΗ = 888, the cypher of the audit; read as a "
  "walk it is the shape of the whole map in one line. Walks 2, 3, "
  "6, and 9 carry no archon at all — walk 6's steps are the dial's "
  "own furniture (ϛ the MIRROR sign at home), printed as strangers "
  "because the grade is the letter's, not the station's.")
A("")

# =====================================================================
# §III — COPTIC, the first mirror
# =====================================================================
co_walks = milesian_walks(COPTIC_SEATS, COPTIC_VOWELS, COPTIC)
co_rows = walk_rows(co_walks, CLASS3)
co_totals, CO_A, CO_W, CO_BOTH = totals_line("Coptic", co_rows)
# the mirror identity, checked step for step against the Greek
for d in range(9):
    assert [step_grade(s) for s in co_walks[d]] == \
           [step_grade(s) for s in gr_walks[d]], d

A("## §III — COPTIC: THE FIRST MIRROR")
A("")
A("The daughter bank, as Plate VIII files it: the same 27 Milesian "
  "seats at the same prices, in Coptic holders — a DERIVED bank, "
  "its values inherited from the Greek entire. Its walks are "
  "therefore the Greek walks in another dress, and the audit of "
  "this map verifies the identity step for step rather than "
  "assuming it: **every grade on every Coptic walk equals the "
  "grade on the corresponding Greek walk.** What the mirror "
  "changes is not the grades but the holders' kinds, and the "
  "changes stand at three coordinates, all printed by the plate: "
  "at the 6-step, ⲋ is a letter of the alphabet where Greek's ϛ is "
  "a numeral sign pressed into service; at the 900-step, ⳁ is "
  "likewise a letter where ϡ is a sign; at the 200-step the change "
  "is of form only, ⲥ for σ. **The one changed step of lineage is "
  "the 90-step of walk 9: ϥ — fai, a living Demotic letter, at "
  "home in ordinary words — where Greek's ϟ, koppa, is a dead sign "
  "that survives only as a numeral.** The grade does not move "
  "(both are strangers); the lineage does, and the parting is "
  "printed at the size of the walk.")
A("")
emit_walk_table(L, co_rows, CLASS3)
A(co_totals)
A("")
A("**The fence.** Seven Demotic letters stand in the Coptic "
  "alphabet and the tradition itself leaves them unvalued — "
  "ϣ SHEI · ϧ KHEI · ⳉ AKHMIMIC KHEI · ϩ HORI · ϫ GANGIA · "
  "ϭ SHIMA · ϯ DEI. They are graded **FENCED** where they stand: "
  "not walked, because no class prices them; not holes, because "
  "the letters stand. The bank's silence on them is verified at "
  "build — each weighs 0 with an empty breakdown — and Plate "
  "VIII's frozen parity exhibit rides with them: *the marks are "
  "counted and priced none.* **The limit, printed as the plate "
  "prints it: a mirror is not a second witness.** The Coptic "
  "walks corroborate the Greek walks' shape the way a reflection "
  "corroborates a face — the descent is the explanation, and the "
  "map counts the mirror's agreement at mirror class in §XV.")
A("")

# =====================================================================
# §IV — CYRILLIC, the second mirror
# =====================================================================
cy_walks = milesian_walks(CYR_SEATS, CYR_VOWELS, CYRILLIC)
cy_rows = walk_rows(cy_walks, CLASS3)
cy_totals, CY_A, CY_W, CY_BOTH = totals_line("Cyrillic", cy_rows)
for d in range(9):
    assert [step_grade(s) for s in cy_walks[d]] == \
           [step_grade(s) for s in gr_walks[d]], d

A("## §IV — CYRILLIC: THE SECOND MIRROR")
A("")
A("The registry's second DERIVED bank, as Plate X files it: 27 "
  "canonical seats in the received Greek order at the Milesian "
  "prices — the canonical total is the Milesian sum itself, "
  "4,995 — with six variant forms standing at three seats, printed "
  "below the table as forms, not steps. The grades again verify "
  "identical to the Greek, step for step. The mirror's changed "
  "holders stand at two coordinates: **at the 6-step, Ѕ is a "
  "letter — dzelo, a living letter of the Slavonic alphabet — "
  "where Greek's ϛ is a sign; at the 90-step, Ч is a Slavonic "
  "letter where koppa had died before the alphabet was borrowed** "
  "(the western price of Ч, 60, is refused whole by the plate and "
  "is not walked). The changed holders are both strangers, as "
  "their Greek counterparts are; what changes is that the mirror "
  "staffs the numeral's dead seats with living letters.")
A("")
emit_walk_table(L, cy_rows, CLASS3)
A(cy_totals)
A("")
A("**The variant forms — printed as forms, not steps.** At the "
  "400-step of walk 4, У's seat carries three further forms: "
  "Ѵ · Ꙋ · Ѹ, each priced 400 by the bank. At the 800-step of "
  "walk 8, Ѡ's seat carries Ѿ · Ꙍ at 800. At the 900-step of walk "
  "9, Ц's seat carries Ѧ at 900. The bank's extent is therefore "
  "33 keys over 27 seats (total 8,695; the 3,700 of difference is "
  "exactly the variants' weight, counted openly by the plate). "
  "The walks step by seats; a form that shares a seat shares its "
  "step's grade and takes no step of its own. Two of the variant "
  "seats are archon seats — the 400 of walk 4 and the 800 of walk "
  "8 — so the mirror's archons travel with retinues the Greek "
  "original does not have; the retinue changes the census, not "
  "the walk. **The limit rides here as in §III: a mirror is not a "
  "second witness** — and Plate XI will show what the elder "
  "Slavonic alphabet does when it prices by its own order instead "
  "(§XII).")
A("")

# =====================================================================
# §V — ARMENIAN: THE FOUR-CLASS WALK
# =====================================================================
arm_walks = []
for d in range(1, 10):
    steps = []
    for ci, cls in enumerate(ARM_CLASSES):
        letter = cls[d - 1]
        value = d * (10 ** ci)
        assert ARMENIAN[letter] == value, (letter, value)
        grade = "ARCHON" if letter in ARM_VOWELS else "STRANGER"
        steps.append([(letter, value, grade)])
    arm_walks.append(steps)
arm_rows = walk_rows(arm_walks, CLASS4)
arm_totals, ARM_A, ARM_W, ARM_BOTH = totals_line("Armenian", arm_rows)

A("## §V — ARMENIAN: THE FOUR-CLASS WALK")
A("")
A("The classical bank entire, ATTESTED, as Plate VII files it: 36 "
  "letters in four classes — the Milesian three and a thousands "
  "class of its own — so the Armenian walk has four steps where "
  "the Greek has three. The tongue files six vowels: Ա 1 · Ե 5 · "
  "Ը 8 · Ի 20 · Ո 600 · Ւ 7000. Note their spread before the table "
  "is read: no two of the six stand on the same walk's home step, "
  "and they occupy four different class-depths — units (Ա, Ե, Ը), "
  "tens (Ի), hundreds (Ո), thousands (Ւ). The late annex — "
  "Օ 10,000 · Ֆ 20,000 — stands behind its own door at "
  "`armenian(word, late=True)` only, per the founder's synergy "
  "ruling R1, and is **not walked**: a door is not a class.")
A("")
emit_walk_table(L, arm_rows, CLASS4)
A(arm_totals)
A("")
A("**The readings.** Armenia is the widest-spread walk in the map: "
  "six archon-steps on six different walks, no walk carrying two. "
  "Walk 7 is its signature — Է Հ Չ are strangers for three steps "
  "and the archon stands at the *last* step, Ւ at 7,000, the only "
  "thousands-step archon in any classed tongue's walk, "
  "late-standing at the walk's far end. Walk 6 mirrors it one "
  "class shallower: the archon Ո stands at the hundreds step and "
  "the walk breaks at its thousands. Walk 2's archon Ի stands at "
  "the tens and breaks at the hundreds. The 8-walk is at home and "
  "breaks at once — Ը is one of the five tongues' witnesses at 8 "
  "(the five-tongue 8 of the battery's Leg 6; Plate VII §V), but "
  "its class-brothers Ձ Պ Փ are strangers, and no return stands "
  "at the "
  "thousands: **the both-ends shape the Greek 8-walk makes is not "
  "repeated here.** Against the Ge'ez control case the plate "
  "files — value agreement total, 26 of 26, the law parting at "
  "position 10 — the walk adds its own coordinate: where Ge'ez "
  "will price a vowel at every order (§XI), Armenia prices six "
  "vowels in four classes and lets thirty of its thirty-six "
  "steps stand stranger. Both are complete alphabets; the walks "
  "are how their completeness differs.")
A("")

# =====================================================================
# §VI — GEORGIAN: THE FORK
# =====================================================================
geo_walks = []
for d in range(1, 10):
    steps = []
    for ci, cls in enumerate(GEO_CLASSES):
        value = d * (10 ** ci)
        if ci == 2 and d == 4:
            steps.append([(g, v, "ARCHON" if g in GEO_VOWELS
                           else "STRANGER") for g, v in GEO_FORK])
            continue
        letter = cls[d - 1]
        assert GEORGIAN[letter] == value, (letter, value)
        if letter == "ჱ":
            # the archaic 8-witness: graded ARCHON, marked †
            steps.append([("ჱ†", value, "ARCHON")])
            continue
        grade = "ARCHON" if letter in GEO_VOWELS else "STRANGER"
        steps.append([(letter, value, grade)])
    # the fifth class: one letter at digit 1, holes elsewhere
    if d == 1:
        steps.append([("ჵ", 10000, "STRANGER")])
    else:
        steps.append([])
    geo_walks.append(steps)
GEO_CLASSES5 = CLASS4 + ["ten-thousands"]
geo_rows = walk_rows(geo_walks, GEO_CLASSES5)
geo_totals, GEO_A, GEO_W, GEO_BOTH = totals_line("Georgian", geo_rows)
GEO_ARCH_STEPS = sum(r[2]["archon_steps"] for r in geo_rows)

A("## §VI — GEORGIAN: THE FORK")
A("")
A("The designed bank, ATTESTED, as Plate IX files it: 38 letters — "
  "and the census number is the first thing the walk must honor, "
  "because 38 letters over four classes of nine is two letters "
  "too many, and the surplus stands at one coordinate. The tongue "
  "files five living vowels — ა 1 · ე 5 · ი 10 · ო 70 · უ 400, at "
  "Greek-mirror prices, with no 8 among them — and one archaic "
  "witness: ჱ, at 8, dropped in the reform of the 1860s, the only "
  "one of the five tongues' 8-witnesses that reaches its seat "
  "from the archaic row. ჱ is graded ARCHON in the table below "
  "and marked † wherever it stands; the summary separates it (§XV). "
  "Beyond the thousands stands a fifth class of a single letter — "
  "ჵ at 10,000, a letter and not a device — so every Georgian "
  "walk is printed with five steps, the last a HOLE on eight of "
  "the nine walks.")
A("")
emit_walk_table(L, geo_rows, GEO_CLASSES5)
A(geo_totals)
A("")
A("**The fork.** Walk 4's hundreds step holds **two letters at "
  "one price: ჳ (obsolete) and უ (living), both 400** — the "
  "hundreds class carries ten letters for nine digits, its sum "
  "is 4,900 and not 4,500, and the number 494 carries two lawful "
  "spellings (ჳჟდ = უჟდ). This is the map's one forked step: a "
  "step whose holders disagree in kind — ჳ a stranger, უ an "
  "archon, the tongue's living /u/ — so the walk passes through "
  "the fork on both branches at once, and the grade the step "
  "prints is the archon's, with the stranger standing beside it "
  "in the same cell. No other step in the twelve tongues is "
  "forked. **The readings.** Walk 1 repeats the Greek opening — "
  "two archons, ა and ი, then the break at the hundreds — and "
  "then walks on past the Greek walk's end into two more stranger "
  "steps and the fifth class's one letter, ჵ, a stranger at "
  "10,000: Georgia's first walk is the map's longest. The 8-walk "
  "stands on the archaic witness at home — ჱ† — and breaks at the "
  "tens, no return: the seat the five tongues share is held here "
  "by a letter the living alphabet no longer uses, and the walk "
  "prints that at the size of the step. The five obsolete letters "
  "(ჱ 8 · ჲ 60 · ჳ 400 · ჴ 7,000 · ჵ 10,000) walk as members of "
  "the bank, as the plate seats them — the mirror image of the "
  "Armenian annex: where Armenia keeps its late letters behind a "
  "door, Georgia seats its old ones in the open and lets them "
  "stand on the walks.")
A("")

# =====================================================================
# §VII — ARABIC: THE THREE MATRES
# =====================================================================
ara_walks = []
for d in range(1, 10):
    steps = []
    for ci, cls in enumerate(ARA_CLASSES):
        letter = cls[d - 1]
        value = d * (10 ** ci)
        assert ARABIC_ABJAD[letter] == value, (letter, value)
        grade = "ARCHON" if letter in ARA_MATRES else "STRANGER"
        steps.append([(letter, value, grade)])
    if d == 1:
        steps.append([("غ", 1000, "STRANGER")])
    else:
        steps.append([])
    ara_walks.append(steps)
ARA_CLASSES4 = CLASS3 + ["thousands"]
ara_rows = walk_rows(ara_walks, ARA_CLASSES4)
ara_totals, ARA_A, ARA_W, ARA_BOTH = totals_line("Arabic", ara_rows)

A("## §VII — ARABIC: THE THREE MATRES")
A("")
A("The abjad bank, as Plate III files it: 28 letters in the abjad "
  "order — units, tens, hundreds full, and a thousands class of "
  "exactly one letter, غ at 1,000. **The grade translation, "
  "printed per §I's law:** Arabic seats no vowel letters of the "
  "Milesian kind; its vowel-carriers are the matres lectionis, and "
  "they are **three — ا 1 · و 6 · ي 10** (the battery's four-count "
  "MISS, verified by Plate III: the sweep's other tongues count "
  "four hybrid/mater seats, Arabic counts three). The matres are "
  "graded ARCHON on this face, marked as matres in the reasoning: "
  "the grade is borne by the tongue's own vowel-carriers, since "
  "there are no others to bear it. Tāʾ marbūṭa ة — the hybrid "
  "form, hāʾ's body with tāʾ's dots — is fenced and unseated in "
  "the bank (it weighs 0, verified at build) and is **not "
  "walked**: it has no class to stand in.")
A("")
emit_walk_table(L, ara_rows, ARA_CLASSES4)
A(ara_totals)
A("")
A("**The readings.** The Arabic walk is the Greek walk's shape "
  "under a thinner sky. Walk 1 opens exactly as the Greek does — "
  "two vowel-carriers at the first two steps, ا at home and ي at "
  "the tens — breaks at the hundreds on ق, and then does "
  "something no Greek walk can do: it takes a fourth step, to "
  "غ at 1,000, a stranger standing alone in a class of one. "
  "Walk 6 carries the third mater, و, at home and breaks at the "
  "tens. Every other walk ends in the thousands HOLE: digits 2–9 "
  "have no fourth step at all, so eight of the nine walks "
  "terminate in emptiness — the map's most-holed classed walk. "
  "The 8-walk holds the sweep's counterweight: ح at home is a "
  "consonant, a stranger — **Arabic's 8 is not a vowel-carrier**, "
  "and the five-tongue 8 of §III–§VI has no Arabic term. The "
  "tongue that shares the Hebrew 22's sum to the digit (its first "
  "22 letters total 1,495) parts from the vowel architecture "
  "exactly here: three matres, two walks, and a thousands class "
  "with one letter in it.")
A("")
# =====================================================================
# §VIII — HEBREW: THE WALK THAT MOVES WITHOUT MOVING
# =====================================================================
SOFIT = [("כ", "ך"), ("מ", "ם"), ("נ", "ן"), ("פ", "ף"), ("צ", "ץ")]
GADOL = {"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900}
HEB_MATRES = ["א", "ה", "ו", "י"]
for m, f in SOFIT:
    assert HEBREW[m] == HEBREW[f]
assert sum(HEBREW[m] for m in HEB_MATRES) == 22
assert sum(HEBREW.values()) == 1775

A("## §VIII — HEBREW: THE WALK THAT MOVES WITHOUT MOVING")
A("")
A("Hebrew has no classes. Its bank, as Plate II files it, is one "
  "run of 22 letters and five final forms, and its native stepping "
  "axis is the **sofit axis**: the five letters that change their "
  "dress at a word's end. **The grade translation:** the sofit "
  "step is graded **DRESS-STEP** — the step changes the letter's "
  "form; what it does to the price is the section's whole matter, "
  "and it is printed per step, not graded over. The tongue's "
  "vowel-carriers, the matres lectionis, are four — א 1 · ה 5 · "
  "ו 6 · י 10, summing 22 — the four-count the sweep corroborated "
  "in this tongue; none of the four is final-capable, and none of "
  "the five final-capable letters is a mater. The two systems "
  "cross without touching, and the walk belongs to the finals.")
A("")
A("| Letter | Medial (price) | Final form (price, face value) | "
  "The step at face value | Under mispar gadol (unseated variant) |")
A("|---|---|---|---|---|")
for m, f in SOFIT:
    v = HEBREW[m]
    g = GADOL[f]
    A(f"| {m} | {v} | {f} — {HEBREW[f]} | the dress changes; the "
      f"price does not ({v} → {HEBREW[f]}) | {f} at {g} — uplift "
      f"+{g - v}; the step breaks the bank's 400 maximum |")
A("")
A("**The readings.** At face value — the bank's seated law — the "
  "sofit walk is the map's one walk with **no break coordinate in "
  "price at all**: five steps, and the price line never ends, "
  "because it never moves; the walk moves without moving. The "
  "break stands in the dress alone: the letter that closes a word "
  "wears another shape, and the bank prices the shape at the "
  "letter's own price. Under mispar gadol — the received variant "
  "reading, printed by Plate II as an unseated variant and "
  "standing unseated here — every step is priced, and every price "
  "breaks the bank's seat maximum of 400 at once: the gadol walk "
  "has no standing step after its first, which is exactly the "
  "fence the plate prints (*Gadol stands as an unseated variant "
  "reading; the face-value law stands*). The corpus's own gadol "
  "parting rides at this coordinate: מאדים claimed 655 against "
  "hechrechi 95, the delta exactly the ם uplift, +560. So the "
  "Hebrew section prints two walks on one axis — the seated walk "
  "that cannot break, and the unseated walk that cannot stand — "
  "and grades neither past its filing.")
A("")

# =====================================================================
# §IX — LATIN: THE BANK-STEP
# =====================================================================
BANK_STEP_LETTERS = ["A", "E", "I", "O", "U", "Y", "H", "W", "J"]
bank_rows = []
for ch in BANK_STEP_LETTERS:
    o = LATIN_ORDINAL[ch]
    a_ = AGRIPPA.get(ch)
    if a_ is None:
        species = "HOLE"
    elif a_ == o:
        species = "UNMOVED"
    else:
        species = "MOVED"
    bank_rows.append((ch, o, a_, species))
assert W("Y", "agrippa") == 400 and W("Υ", "greek") == 400
assert "W" not in AGRIPPA and LATIN_ORDINAL["W"] == 23
assert AGRIPPA["J"] == AGRIPPA["I"] == 9

A("## §IX — LATIN: THE BANK-STEP")
A("")
A("Latin has no classes either; it has two banks. Its native "
  "stepping axis is the **bank-step**: one letter stepped from "
  "the ordinal bank (the alphabet's own order, A = 1 … Z = 26) "
  "to the Agrippa bank (the Renaissance's priced Latin). **The "
  "grade translation:** a bank-step is graded **UNMOVED** (one "
  "price in both banks), **MOVED** (the price changes; the letter "
  "does not), or **HOLE** (no seat in the second bank). This is "
  "the exact inverse of the Hebrew step (§VIII): there the dress "
  "changed and the price stood; here the letter stands and the "
  "price moves. The founding coordinate rides at the table's "
  "heart: **H is 8 in both banks, so HHH = 24 in both** — the "
  "Triple H of the audit, Latin's own share of it.")
A("")
A("| Letter | Ordinal price | Agrippa price | The bank-step | "
  "Reasoning |")
A("|---|---|---|---|---|")
LAT_REASONS = {
    "A": "The first vowel stands at 1 in both banks — the "
         "ordinal's A-seat and Agrippa's agree entire.",
    "E": "Unmoved at 5 — the second vowel the banks hold in "
         "common.",
    "I": "Unmoved at 9 — and the seat the fold lands on (below).",
    "O": "The first vowel whose price moves: 15 → 50. Among "
         "vowels, the banks part here.",
    "U": "21 → 200. V steps to the same seat (22 → 200): the two "
         "dresses coincide in Agrippa, as the titulus's expansion "
         "showed in the audit.",
    "Y": "25 → 400 — and 400 is Υ's own Greek price, exact: the "
         "battery's dress-coordinate, the Latin letter landing on "
         "its Greek original's value (Plate IV §V). Y stands at "
         "its coordinate, as the founder's filing has it.",
    "H": "8 → 8, unmoved — the Triple H seat: HHH = 24 in the "
         "ordinal and in Agrippa alike.",
    "W": "Ordinal 23; in Agrippa, no seat stands — the HOLE of "
         "the Latin walk, printed by Plate IV as the bank's one "
         "unseated letter.",
    "J": "Not a vowel — the fold, printed because Agrippa seats "
         "it: ordinal 10 → Agrippa 9, stepping onto I's own price. "
         "The two banks part first at J (Plate IV), before any "
         "vowel moves.",
}
for ch, o, a_, species in bank_rows:
    a_txt = str(a_) if a_ is not None else "— no seat"
    if species == "UNMOVED":
        step = f"UNMOVED ({o} → {a_})"
    elif species == "MOVED":
        step = f"MOVED ({o} → {a_})"
    else:
        step = "HOLE — the step cannot be taken"
    A(f"| {ch} | {o} | {a_txt} | {step} | {LAT_REASONS[ch]} |")
A("")
A("**The readings.** Three vowels never move — A, E, I hold one "
  "price across the Renaissance's repricing of the alphabet — and "
  "the three that move, move far: O by 35, U by 179, Y by 375, "
  "each landing on a rounder seat than it left. The walk's break "
  "coordinate, in the bank-step's own terms, is **J**: the banks "
  "part first at the folded letter, a consonant seat, before the "
  "first vowel (O) moves — the Latin line breaks on a letter that "
  "is not on the vowel line at all, the same species of parting "
  "the Greek 8-walk prints at Π and the numeral ΩΠΗ wears at its "
  "center. And the walk has exactly one HOLE: W, the letter the "
  "Renaissance bank never seated, standing in the ordinal at 23 "
  "with no second price to step to.")
A("")

# =====================================================================
# §X — JAPANESE: THE COLUMN-WALKS
# =====================================================================
J_ROWS = [("a", ["あ", "い", "う", "え", "お"]),
          ("k", ["か", "き", "く", "け", "こ"]),
          ("s", ["さ", "し", "す", "せ", "そ"]),
          ("t", ["た", "ち", "つ", "て", "と"]),
          ("n", ["な", "に", "ぬ", "ね", "の"]),
          ("h", ["は", "ひ", "ふ", "へ", "ほ"]),
          ("m", ["ま", "み", "む", "め", "も"]),
          ("y", ["や", None, "ゆ", None, "よ"]),
          ("r", ["ら", "り", "る", "れ", "ろ"]),
          ("w", ["わ", "ゐ", None, "ゑ", "を"])]
J_DAKU = [("g", ["が", "ぎ", "ぐ", "げ", "ご"]),
          ("z", ["ざ", "じ", "ず", "ぜ", "ぞ"]),
          ("d", ["だ", "ぢ", "づ", "で", "ど"]),
          ("b", ["ば", "び", "ぶ", "べ", "ぼ"]),
          ("p", ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"])]
J_COLS = ["a", "i", "u", "e", "o"]
J_NINE = {"a": "Α — the head's seat (1) is Α's own weight, exact",
          "i": "Ι — the correspondence seat, as Plate V files it",
          "u": "VV — [ɯ] under VV, the founder's ratification "
               "(Plate V §V)",
          "e": "Ε — the correspondence seat, as Plate V files it",
          "o": "Ο — the correspondence seat, as Plate V files it"}
J_ARCHIVAL = {"ゐ", "ゑ"}
J_HOLE_NAMES = {(7, 1): "yi", (7, 3): "ye", (9, 2): "wu"}
# seat assertions: the grid's standing seats run 1..47 in order
_seat = 0
for ri, (_rn, cells) in enumerate(J_ROWS):
    for ci, kana in enumerate(cells):
        if kana is None:
            assert (ri, ci) in J_HOLE_NAMES
            continue
        _seat += 1
        assert KANA[kana] == _seat, (kana, _seat)
        kata = chr(ord(kana) + 0x60)
        assert KANA[kata] == _seat, (kata, _seat)
assert _seat == 47 and KANA["ん"] == 48
_dseat = 48
for _rn, cells in J_DAKU:
    for kana in cells:
        _dseat += 1
        assert KANA[kana] == _dseat, (kana, _dseat)
assert _dseat == 73

A("## §X — JAPANESE: THE COLUMN-WALKS")
A("")
A("The kana mint — CONSTRUCTED, the founder's coinage, ratified "
  "by his stamp of 2026-11-13 — prices the gojūon grid by seat, "
  "and in this mint the vowel is the price-axis itself (Plate V): "
  "every seat's syllable carries its column's vowel. The walk "
  "therefore runs **down each vowel column through the grid's "
  "rows**. **The grade translation:** the column's head — the "
  "pure vowel itself — is graded **ARCHON**, with its Nine "
  "coordinate printed; every standing row-step below it is graded "
  "**CARRIER** (the vowel borne by a consonant row); an empty grid "
  "cell is a **HOLE**. The two dresses (hiragana · katakana) are "
  "one bank in two dresses at the same seats — the walk that "
  "changes the dress and not the price, Hebrew's species (§VIII) "
  "— and the seats below print the hiragana; the katakana stands "
  "at the identical seat, verified at build for every cell.")
A("")
A("| Column | The head — its Nine coordinate | The walk, row by "
  "row | Standing | Break coordinate |")
A("|---|---|---|---|---|")
J_COL_STATS = {}
for ci, col in enumerate(J_COLS):
    steps = []
    standing = 0
    hole_at = None
    ret_at = None
    for ri, (rn, cells) in enumerate(J_ROWS):
        kana = cells[ci]
        if kana is None:
            steps.append(f"{J_HOLE_NAMES[(ri, ci)]} — HOLE")
            if hole_at is None:
                hole_at = rn
            continue
        standing += 1
        mark = " ★" if ri == 0 else ""
        arch = " (archival)" if kana in J_ARCHIVAL else ""
        steps.append(f"{kana} {KANA[kana]}{mark}{arch}")
        if hole_at is not None and ret_at is None:
            ret_at = (rn, kana, KANA[kana])
    if hole_at is None:
        brk = "unbroken — no hole stands on this column"
    elif ret_at is not None:
        brk = (f"break at the {hole_at}-row (the grid cell is "
               f"empty) · return at the {ret_at[0]}-row "
               f"({ret_at[1]} {ret_at[2]})")
    else:
        brk = (f"break at the {hole_at}-row (the grid cell is "
               f"empty) — the column ends in the hole; no return")
    J_COL_STATS[col] = (standing, brk)
    A(f"| {col} | {J_NINE[col]} | " + " · ".join(steps) +
      f" | {standing} of 10 rows | {brk} |")
A("")
A("**The dakuten coda.** Below the grid the mint seats the voiced "
  "block, seats 49–73 — five rows (g · z · d · b · p) in the same "
  "five columns, every cell standing, no heads and no holes: the "
  "columns' carriers continue for twenty-five more steps without "
  "a break anywhere. And one seat stands outside the columns "
  "entire: ん at 48, the moraic nasal, which carries no vowel and "
  "belongs to no column — the grid's one columnless seat, printed "
  "here because a map of the columns must name what the columns "
  "cannot hold.")
A("")
A("**The readings.** A Japanese column-walk can never meet a "
  "stranger: every standing step carries the column's vowel, so "
  "the line cannot break the way the Milesian line breaks — it "
  "can only fall through a hole in the grid. The three holes "
  "stand at filed coordinates: **yi and ye in the y-row** (the "
  "i- and e-columns break there and return at the r-row), and "
  "**wu in the w-row**, where the u-column ends in its hole with "
  "no return — the map's one terminal hole inside a walk. The a- "
  "and o-columns stand unbroken for all ten rows. The archival "
  "pair ゐ (i-column, seat 45) and ゑ (e-column, seat 46) stand "
  "as carriers in the w-row, marked archival as the plate files "
  "them: the columns' oldest letters stand nearest their ends.")
A("")

# =====================================================================
# §XI — GE'EZ: THE ORDER-WALKS
# =====================================================================
GEEZ_NAMES = ["ha", "le", "ḥa", "me", "śa", "re", "sa", "qa",
              "ba", "ta", "xa", "na", "ʾa", "ka", "wa", "ʿa",
              "za", "ya", "da", "ga", "ṭa", "p̣a", "ṣa", "ṣ́a",
              "fa", "pa"]
FIRST_SUM = sum(fv for _b, fv in _GEEZ_BASES)
assert FIRST_SUM == 4095


def mint_price(fv, order):
    return fv * (0 if order == 6 else order)


for b, fv in _GEEZ_BASES:
    for o in range(1, 8):
        g = chr(ord(b) + o - 1)
        assert GEEZ[g] == mint_price(fv, o), (g, o)
        assert HALEHAME[g] == fv * o, (g, o)
MINT_COL6 = sum(mint_price(fv, 6) for _b, fv in _GEEZ_BASES)
WIT_COL6 = sum(fv * 6 for _b, fv in _GEEZ_BASES)
assert WIT_COL6 == 24570 and MINT_COL6 == 0
EIGHTH_TOTAL = 0
for b, fv in _GEEZ_BASES:
    if b == _GEEZ_EIGHTH_SLOT_HOLE:
        hole_glyph = chr(ord(b) + 7)
        assert hole_glyph not in GEEZ
        try:
            unicodedata.name(hole_glyph)
            raise SystemExit("U+12D7 unexpectedly assigned")
        except ValueError:
            pass
    else:
        g8 = chr(ord(b) + 7)
        assert GEEZ[g8] == fv * 8, g8
        EIGHTH_TOTAL += fv * 8
assert EIGHTH_TOTAL == 32200
LAB_TOTAL = 0
LAB_ZERO = []
for head, base in _GEEZ_LABIOVELAR_HEADS:
    fv = dict(_GEEZ_BASES)[base]
    for order, off in sorted(_GEEZ_LABIOVELAR_OFFSETS.items()):
        g = chr(ord(head) + off)
        assert g in GEEZ and g not in HALEHAME
        LAB_TOTAL += GEEZ[g]
        if GEEZ[g] == 0:
            LAB_ZERO.append(g)
assert LAB_TOTAL == 3614 and len(LAB_ZERO) == 4
assert sum(1 for v in GEEZ.values() if v == 0) == 30

A("## §XI — GE'EZ: THE ORDER-WALKS")
A("")
A("Ge'ez has no classes; it has **orders**. Each of the 26 "
  "classical bases is a consonant series of seven orders, and the "
  "order *is* the vowel — the seven orders carry the vowel grades "
  "of the fidäl (ä · u · i · a · e · ə · o). **The grade "
  "translation:** every standing order-step is graded "
  "**VOWEL-STEP** — in this tongue the walk cannot meet a "
  "stranger, because stepping *is* vowel-changing. Its breaks are "
  "of the other kind, and both are column-shaped. The walked bank "
  "is the founder's **mint** (CONSTRUCTED, his coinage of "
  "2026-11-24), calibrated to the halehame **witness** at its "
  "first column; the witness stands beside the walk at the one "
  "column where they part. A distinction the section keeps at "
  "full size: **ZERO is not HOLE** — an order-6 glyph in the mint "
  "stands and weighs 0; the hole of the eighth slot does not "
  "stand at all.")
A("")
A("| Base | First form | Orders 1–7 in the mint (glyph · price) | "
  "Order 6 in the witness | The eighth slot |")
A("|---|---|---|---|---|")
for (b, fv), nm in zip(_GEEZ_BASES, GEEZ_NAMES):
    steps = " · ".join(f"{chr(ord(b) + o - 1)} {mint_price(fv, o)}"
                       for o in range(1, 8))
    if b == _GEEZ_EIGHTH_SLOT_HOLE:
        eighth = "**HOLE** — the cell is unassigned (U+12D7)"
    else:
        eighth = f"{chr(ord(b) + 7)} {fv * 8}"
    A(f"| {b} {nm} | {fv} | {steps} | {fv * 6} | {eighth} |")
A("")
A(f"**Break coordinate 1 — the sixth order, entire.** The mint "
  f"prices order 6 at 0 for every base: the column of twenty-six "
  f"standing glyphs weighs nothing, where the witness prices the "
  f"same column at first-form × 6. The parting is one column "
  f"deep and totals **{WIT_COL6:,}** — the witness's order-6 "
  f"column entire (first forms sum {FIRST_SUM:,}; × 6 = "
  f"{WIT_COL6:,}), which is also the whole difference between "
  f"the two grids (mint 90,090 · witness 114,660). Every base's "
  f"walk therefore breaks in price at its sixth step in the mint "
  f"and does not break in the witness: the same glyphs, the same "
  f"orders, and the line ends at a different place depending on "
  f"which bank walks — the founder's Debtera ruling (halehame "
  f"stands as witness beside the mint) is what keeps both "
  f"printings standing.")
A("")
A(f"**Break coordinate 2 — the eighth slot.** Twenty-five bases "
  f"step once more, to an eighth glyph priced first-form × 8 — "
  f"the ΕΙ column, {EIGHTH_TOTAL:,} in total. One base does not: "
  f"ዐ (ʿa, first form 70), whose eighth cell is a **HOLE** — the "
  f"codepoint U+12D7 is unassigned in the standard, no glyph "
  f"exists to stand there, verified at build. The battery filed "
  f"this coordinate before the mint existed: in Ge'ez, the 8 "
  f"stands as a named hole. The walk prints it as the tongue's "
  f"one true hole — not a zero (the glyphs at zero stand) but an "
  f"absence in the script itself.")
A("")
A(f"**The labiovelars.** Four bases carry labiovelar series — "
  f"ቈ (of ቀ) · ኈ (of ኀ) · ኰ (of ከ) · ጐ (of ገ) — five signs each "
  f"at the orders {{1, 3, 4, 5, 6}}, twenty signs in the mint "
  f"(total {LAB_TOTAL:,}) and **none in the witness**: the "
  f"witness's grid has a gap at every labiovelar row, the second "
  f"reason it stands as witness and not as bank. Their order-6 "
  f"signs (ቍ · ኍ · ኵ · ጕ) price 0 in the mint, completing the "
  f"mint's thirty zero signs — twenty-six of the grid and four of "
  f"the labiovelars, counted at build. The derived rows beyond "
  f"the classical bases stand fenced in both banks (Plate VI) "
  f"and are not walked.")
A("")
# =====================================================================
# §XII — GLAGOLITIC: THE ORDER-PRICED WALK
# =====================================================================
gla_walks = []
for d in range(1, 10):
    steps = []
    for ci in range(4):
        entry = GLA_CLASSES[ci][d - 1]
        if entry is None:
            steps.append([])
            continue
        letter, value = entry
        assert GLAGOLITIC[letter] == value, (letter, value)
        grade = "ARCHON" if letter in GLA_VOWELS else "STRANGER"
        holders = [(letter, value, grade)]
        if ci == 1 and d == 1:
            alt_l, alt_v = GLA_ALT_10
            assert GLAGOLITIC[alt_l] == alt_v
            holders.append((alt_l, alt_v,
                            "ARCHON" if alt_l in GLA_VOWELS
                            else "STRANGER"))
        steps.append(holders)
    gla_walks.append(steps)
gla_rows = walk_rows(gla_walks, CLASS4)
gla_totals, GLA_A, GLA_W, GLA_BOTH = totals_line("Glagolitic",
                                                gla_rows)

A("## §XII — GLAGOLITIC: THE ORDER-PRICED WALK")
A("")
A("The elder Slavonic alphabet prices by its own order, not by "
  "Greek values — ATTESTED as an order-priced bank, as Plate XI "
  "files it: the letters' values *are* their alphabet positions "
  "stepped through the classes. Its vowel row, as the plate files "
  "it, is Ⰰ 1 · Ⰵ 6 · Ⰹ 10 · Ⰺ 10 · Ⰻ 20 · Ⱁ 80 · Ⱆ 400 · "
  "Ⱑ 4000 (the last flagged by the plate: the thousands range "
  "stands under the witnesses' warning). The walk steps by value "
  "through the four classes. One seat carries two holders: the "
  "tens step of walk 1, where the witnesses print *Ⰺ or Ⰹ* — "
  "both seat at 10, the value undisputed (the plate's one "
  "duplication, a doubled price, distinguished in §XV from "
  "Georgia's forked step: two glyphs the witnesses give for one "
  "seat, not two letters at two positions).")
A("")
emit_walk_table(L, gla_rows, CLASS4)
A(gla_totals)
A("")
A("**The holes inside the valued span.** Three letters of the "
  "alphabet stand unvalued *inside* the runs the walk steps "
  "through, each verified silent at build: **Ⱊ**, in the "
  "hundreds run between Ⱉ 700 and Ⱋ 800; **Ⱐ** (yeri), in the "
  "thousands run between Ⱏ 3000 and Ⱑ 4000; **Ⱒ** (spidery ha), "
  "between Ⱑ 4000 and Ⱓ 5000. They are HOLE steps of the run "
  "species — the letters stand in the alphabet and weigh nothing "
  "— distinct from the walk's three digit-step holes: the "
  "thousands steps of walks 6, 7, and 8, where no letter was ever "
  "cut (the composite spellings for 6000 · 7000 · 8000 are "
  "spellings, not letters, and are refused as steps, as the plate "
  "files them).")
A("")
A("**The readings.** The order-priced bank matches the Milesian "
  "count by its own law — seven archon-steps, the Greek total, "
  "reached without a single Greek price. Walk 1 opens with two "
  "(Ⰰ at home, the doubled 10 at the tens, both holders vowels) "
  "and breaks at the hundreds. And the 8-walk carries the map's "
  "sharpest negative: **Ⰷ, dzelo, the letter at 8, is a "
  "consonant — the 8 fails at home.** The vowel row steps 6 → 10 "
  "over the value, and the seat the five tongues hold with a "
  "vowel is held here by a stranger; the walk's archon waits at "
  "the tens (Ⱁ 80) instead. The elder alphabet is the five-tongue "
  "set's Slavonic boundary, as Plate XI printed it: its younger "
  "sibling joins the set (§IV); it does not. Its thousands steps "
  "also carry the witnesses' own warning — values above 999 are "
  "uncertain in the tradition, 3000 and above questioned — and "
  "the map walks them as filed, warning attached, neither "
  "smoothing the range nor refusing it.")
A("")

# =====================================================================
# §XIII — KOREAN: THE STRATA WALKS
# =====================================================================
def sk_seat(glyph, kind, bank):
    return bank[_jamo_conjoining(glyph, kind)]


KOR_INIT = [(g, sk_seat(g, "CHOSEONG", HANGUL_INITIAL))
            for g in _HANGUL_SK_INITIAL]
KOR_VOW = [(g, sk_seat(g, "JUNGSEONG", HANGUL_VOWEL))
           for g in _HANGUL_SK_VOWEL]
KOR_FIN = [(g, sk_seat(g, "JONGSEONG", HANGUL_FINAL))
           for g in _HANGUL_SK_FINAL]
FIN_BY_GLYPH = dict(KOR_FIN)
KOR_BROKEN = [g for g, _s in KOR_INIT if g not in FIN_BY_GLYPH]
KOR_STANDING = [(g, s, FIN_BY_GLYPH[g]) for g, s in KOR_INIT
                if g in FIN_BY_GLYPH]
KOR_FINAL_ONLY = [(g, s) for g, s in KOR_FIN
                  if g in set(_HANGUL_DIGRAPH_FINALS)]
assert KOR_BROKEN == ["ㄸ", "ㅃ", "ㅉ"]
assert len(KOR_STANDING) == 16 and len(KOR_FINAL_ONLY) == 11
KOR_COMPOUND = list("ㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ")
assert len(KOR_COMPOUND) == 11
HINGE_I = dict(KOR_INIT)["ㅇ"]
HINGE_F = FIN_BY_GLYPH["ㅇ"]
assert (HINGE_I, HINGE_F) == (12, 21)
DOOR_A = hangul("아")
DOOR_AI = hangul("아이")
assert DOOR_A["value"] == 1 and DOOR_A["null_initials"] == 1
assert DOOR_AI["value"] == 22 and DOOR_AI["null_initials"] == 2
assert hangul("한글")["value"] == 52 and hangul("한국")["value"] == 40
YE = [x for x in KOR_VOW if x[0] == "ㅖ"][0]
assert YE[1] == 8 and "ㅖ" in KOR_COMPOUND

A("## §XIII — KOREAN: THE STRATA WALKS")
A("")
A("The hangul mint — CONSTRUCTED, the founder's coinage — prices "
  "the jamo by their canonical South Korean seats within three "
  "strata (initials 19 · vowels 21 · finals 27; bank total 799), "
  "as Plate XII files it. The walk steps a jamo **across the "
  "strata where a form exists in each**. **The grade "
  "translation:** the vowel stratum's seats are the tongue's "
  "ARCHON-class (its vowel seats, priced by seat, as the mint's "
  "law is); consonant seats are STRANGER-class; a missing form "
  "is a HOLE; and one jamo carries a grade of its own, printed "
  "below. No witness prices a jamo — the mint is walked as a "
  "mint, its tier on its face.")
A("")
A("### §XIII.1 — The consonant walks: initial to final")
A("")
A("| Jamo | Initial seat | Final seat | The walk |")
A("|---|---|---|---|")
for g, si, sf in KOR_STANDING:
    step = (f"standing — the walk crosses ({si} → {sf})"
            if g != "ㅇ" else
            f"**THE HINGE** — see §XIII.3 ({si} → {sf})")
    A(f"| {g} | {si} | {sf} | {step} |")
for g in KOR_BROKEN:
    si = dict(KOR_INIT)[g]
    A(f"| {g} | {si} | — | **break** — no final form stands: "
      f"HOLE at the final stratum |")
A("")
A(f"**The readings.** Sixteen of the nineteen initials cross to "
  f"a final form; the seats move as they cross (ㄴ 3 → 4 · ㄷ 4 → "
  f"7 · ㅁ 7 → 16 · ㅎ 19 → 27) because the final stratum seats "
  f"its own order, clusters included. Three walks break: "
  f"**ㄸ (5) · ㅃ (9) · ㅉ (14)** — the tense doubles — have no "
  f"final form; the syllable they open can never be closed by "
  f"them, and their walks end at the stratum's edge in a HOLE. "
  f"Eleven further forms stand at the final stratum only — the "
  f"digraph clusters, whose initial step is a HOLE (no initial "
  f"form stands; the modern initials refuse them their seats, as "
  f"Plate XII files the refusal):")
A("")
A("| Cluster | Final seat | The walk |")
A("|---|---|---|")
for g, s in KOR_FINAL_ONLY:
    A(f"| {g} | {s} | stands at the final stratum only — HOLE at "
      f"the initial stratum |")
A("")
A("### §XIII.2 — The vowel stratum")
A("")
A("| Seat | Jamo | Class | Seat | Jamo | Class |")
A("|---|---|---|---|---|---|")
_vow = KOR_VOW
for i in range(0, 21, 2):
    left = _vow[i]
    right = _vow[i + 1] if i + 1 < 21 else ("", "", "")
    def _cls(g):
        return "compound (fused)" if g in KOR_COMPOUND else "basic"
    r_txt = (f"{right[1]} | {right[0]} | {_cls(right[0])}"
             if right[0] else "— | — | —")
    A(f"| {left[1]} | {left[0]} | {_cls(left[0])} | {r_txt} |")
A("")
A(f"The vowel stratum walks within itself — twenty-one seats, "
  f"ten basic and **eleven compound (fused)**, the compound class "
  f"counted as Plate XII and the battery file it (the four-count "
  f"MISS of Leg 6 stands: the class counts eleven, not four). "
  f"At **seat 8 stands ㅖ — itself a fused sign**: in the five "
  f"classed tongues the 8-seat is a vowel letter's price; here "
  f"the seat priced 8 in the vowel stratum is a compound, two "
  f"vowel signs in one glyph — the distinction printed at the "
  f"size of the seat, as Plate XII prints it.")
A("")
A("### §XIII.3 — ㅇ THE HINGE, walked entire")
A("")
A(f"One jamo holds two offices, and its walk is the section's "
  f"reason for standing. As an **initial**, ㅇ stands at seat "
  f"{HINGE_I} in the raw bank — but at the `hangul()` door the "
  f"null law prices an initial ㅇ at **0 and counts it**: the "
  f"exhibits are the plate's own — 아 weighs 1 at the door with "
  f"1 null initial; 아이 weighs 22 with 2 nulls, against the raw "
  f"bank's 46; 한글 52 · 한국 40. As a **final**, ㅇ is a full "
  f"letter, /ŋ/, at seat {HINGE_F} — the only jamo whose final "
  f"seat is its own syllable-closing sound. The hinge is the "
  f"Korean zero as the Regional Triad filed it: **the "
  f"PLACEHOLDER** — Japanese the HOLE · Korean the PLACEHOLDER · "
  f"Chinese the GLYPH — a zero that stands in the seat and holds "
  f"it open, priced at nothing, counted always. Its grade on "
  f"this map is its own: **HINGE** — neither archon nor stranger "
  f"nor hole, but the seat that lets the strata meet.")
A("")
A("**The North order, as filed, not walked.** The North Korean "
  "orders part from the South order seated here (Plate XII prints "
  "the parting); whether a North annex is ever wanted is the "
  "founder's pen, already standing at his pen from the plate. "
  "This map walks the seated order only and raises the question "
  "no further.")
A("")

# =====================================================================
# §XIV — THE HYBRIDS WALK
# =====================================================================
AI_, EI_, OI_, OU_ = (W("ΑΙ", "greek"), W("ΕΙ", "greek"),
                      W("ΟΙ", "greek"), W("ΟΥ", "greek"))
assert (AI_, EI_, OI_, OU_) == (11, 15, 80, 470)
assert AI_ + EI_ + OI_ + OU_ == 576 == 24 ** 2
assert W("ⲟⲩ", "coptic") == 470
assert W("VV", "latin_ordinal") == 44 and W("VV", "agrippa") == 400
assert W("UU", "agrippa") == 400
assert repeat_status("V", 2) == "refused_hybrid"
LAT_HYBRIDS = ["EI", "AE", "OE", "VI"]
for h in LAT_HYBRIDS:
    assert W(h, "latin_ordinal") and W(h, "agrippa")


def greek_walk_str(d):
    steps = gr_walks[d - 1]
    return " · ".join(cell_text(s) for s in steps)


A("## §XIV — THE HYBRIDS WALK")
A("")
A("The hybrids have no classes of their own; they walk by their "
  "components. The two seated hybrids of the Nine first, then "
  "the two candidate branches outside the Nine, then the Latin "
  "four by their letters' bank-steps, then the hybrid whose walk "
  "is a refusal.")
A("")
A("| Hybrid | Price | First component — its walk or seat | "
  "Second component — its walk or seat | Reasoning |")
A("|---|---|---|---|---|")
A(f"| ΑΙ | {AI_} | Α — walk 1's home step (Α 1 ★) | Ι — walk 1's "
  f"tens step (Ι 10 ★) | The candidate branch whose components "
  f"never leave walk 1: both stand on the one walk that opens "
  f"standing. ΑΙ holds no seat in the Nine; it is printed as a "
  f"branch, not a member. |")
A(f"| ΕΙ | {EI_} | Ε — walk 5 entire: {greek_walk_str(5)} | Ι — "
  f"walk 1's tens step (Ι 10 ★) | A seated hybrid of the Nine. "
  f"Its first component's walk breaks at the tens; its second "
  f"component is the step walk 1 breaks *after*. The seating's "
  f"PAIR-mark rides as the battery filed it: ΕΙ ↔ 852, root 6 "
  f"against root 6, single-witness. |")
A(f"| ΟΙ | {OI_} | Ο — walk 7's tens step (Ο 70 ★) | Ι — walk 1's "
  f"tens step (Ι 10 ★) | The second candidate branch: both "
  f"components are tens-step archons, the two middle steps of "
  f"two different walks, joined at one price. Outside the Nine, "
  f"as filed. |")
A(f"| ΟΥ | {OU_} | Ο — walk 7's tens step (Ο 70 ★) | Υ — walk 4's "
  f"hundreds step (Υ 400 ★) | A seated hybrid of the Nine — and "
  f"the map's one hybrid with a mirror twin: in Coptic the same "
  f"compound weighs ⲟⲩ = {W('ⲟⲩ', 'coptic')}, identical across "
  f"banks (Plate VIII: not bank architecture but a finding). Its "
  f"components stand at the middle of walk 7 and the far end of "
  f"walk 4 — the two late archons, compounded. |")
A("")
A(f"**The four together.** ΑΙ {AI_} · ΕΙ {EI_} · ΟΙ {OI_} · "
  f"ΟΥ {OU_} sum to **576 = 24²** — the hybrid branches square "
  f"the Triple H's weight (ΗΗΗ = 24, §I). The battery filed the "
  f"square as a structure-mark of the diphthong field; the walk "
  f"adds where the branches stand: every component of every "
  f"diphthong is an archon step of its walk — there is no "
  f"diphthong of strangers in the field — and the two seated "
  f"hybrids part in shape: ΕΙ compounds a broken walk's home with "
  f"walk 1's second step; ΟΥ compounds the two late-standing "
  f"archons of walks 7 and 4.")
A("")
A("### §XIV.1 — The Latin hybrids, by bank-steps")
A("")
A("| Hybrid | Ordinal | Agrippa | Its letters' bank-steps (§IX) |")
A("|---|---|---|---|")
_lat_hyb_rows = {"EI": "E unmoved · I unmoved — the hybrid whose "
                       "letters never move",
                 "AE": "A unmoved · E unmoved",
                 "OE": "O moved (15 → 50) · E unmoved",
                 "VI": "V moved (22 → 200) · I unmoved"}
for h in LAT_HYBRIDS:
    A(f"| {h} | {W(h, 'latin_ordinal')} | {W(h, 'agrippa')} | "
      f"{_lat_hyb_rows[h]} |")
A("")
A("The four seated Latin hybrids of Plate IV's §V (of six "
  "candidates; the six sum 121 = 11² in the ordinal). Their "
  "walks are their letters' bank-steps read together: EI and AE "
  "cross between the banks without a single moved letter — the "
  "hybrids the repricing could not touch — while OE and VI each "
  "carry one moved letter, and VI's V lands on the 200 where U "
  "also stands.")
A("")
A("### §XIV.2 — VV: the walk that is a refusal")
A("")
A(f"VV prices {W('VV', 'latin_ordinal')} in the ordinal and "
  f"**{W('VV', 'agrippa')} in Agrippa** — Υ's own price, the "
  f"doubled letter landing on the Greek vowel's seat (UU == VV "
  f"== 400 on Agrippa's bank, U read as V). As a numeral it does "
  f"not walk at all: Rome refuses the double, exactly as LL and "
  f"DD are refused, and the Roman instrument returns its status "
  f"at this build — *refused_hybrid* — refused as a numeral, "
  f"seated as the Roman face's hybrid by the founder's word of "
  f"2026-11-24, on his ground, printed verbatim as the instrument "
  f"files it: *\"its both a double constanant and a double "
  f"vowel.\"* VV's walk is therefore the map's one walk of length "
  f"zero: the step is not broken, holed, or fenced — it is "
  f"refused, and the refusal is the seat. Beside it the hybrids' "
  f"relation to the founding coordinate stands as filed: the "
  f"diphthong four square the 24 (§XIV above); VV in Agrippa "
  f"*is* one of the Nine's prices carried by two Latin letters.")
A("")
# =====================================================================
# §XV — THE SUMMARY TABLE
# =====================================================================
A("## §XV — THE SUMMARY: TWELVE WALKS ON ONE FACE")
A("")
A("| Tongue | Axis | Archon-steps | Walks carrying archons | "
  "Both-ends | Headline breaks, holes, and forks |")
A("|---|---|---|---|---|---|")
A(f"| Greek | classes × 3 | {GR_A} | {GR_W} of 9 | walk 8 | walk 1 "
  f"breaks at the hundreds · walk 5 at the tens · walk 8 breaks "
  f"at the tens and returns at the hundreds |")
A(f"| Coptic | classes × 3 (mirror) | {CO_A} | {CO_W} of 9 | walk "
  f"8 | the Greek breaks entire, in Coptic holders · the changed "
  f"step at 90 (ϥ for ϟ) · seven letters FENCED |")
A(f"| Cyrillic | classes × 3 (mirror) | {CY_A} | {CY_W} of 9 | "
  f"walk 8 | the Greek breaks entire · changed holders at 6 (Ѕ) "
  f"and 90 (Ч) · six variant forms at three seats |")
A(f"| Armenian | classes × 4 | {ARM_A} | {ARM_W} of 9 | none | "
  f"six archons on six walks · walk 7's archon at the final step "
  f"(Ւ 7000) · the annex behind its door, unwalked |")
A(f"| Georgian | classes × 4 + a fifth of one | {GEO_A} (one by "
  f"the archaic †) | {GEO_W} of 9 | none | THE FORK at walk 4's "
  f"hundreds (ჳ + უ at 400) · eight HOLEs in the fifth class |")
A(f"| Arabic | abjad classes × 3 + thousands of one | {ARA_A} "
  f"(matres) | {ARA_W} of 9 | none | walk 1 opens as the Greek "
  f"does and takes a fourth step · eight walks end in the "
  f"thousands HOLE · ة fenced, unwalked |")
A("| Hebrew | the sofit axis | — (species) | 5 final-capable "
  "letters | — | no price break at face value — the walk that "
  "moves without moving · under gadol, every step breaks the "
  "400 fence |")
A("| Latin | the bank-step | — (species) | A · E · I · H unmoved | "
  "— | the banks part first at J (the fold) · O the first vowel "
  "to move · W the walk's one HOLE |")
A("| Japanese | the vowel columns | 5 heads · 67 carriers | all "
  "five columns | — | holes at yi · ye (returns stand) and wu "
  "(terminal) · ん columnless at 48 · the dakuten block unbroken |")
A("| Ge'ez | the orders × 7 | every step a vowel-step (182 grid "
  "steps) | all 26 bases | — | order 6: the mint's zero column "
  "against the witness's 24,570 · the eighth slot's HOLE at ዐ · "
  "the labiovelar gap in the witness |")
A(f"| Glagolitic | order-priced classes × 4 | {GLA_A} | {GLA_W} "
  f"of 9 | none | the 8 fails at home (Ⰷ a stranger) · three "
  f"holes inside the runs (Ⱊ · Ⱐ · Ⱒ) · thousands holes at "
  f"6000 · 7000 · 8000 |")
A("| Korean | the strata | 21 vowel seats (11 fused) | the vowel "
  "stratum entire | — | three consonant walks break at the final "
  "stratum (ㄸ · ㅃ · ㅉ) · eleven clusters stand at the final "
  "only · ㅇ THE HINGE (12 → 0 at the door → 21) |")
A("| The hybrids | by components | every component an archon "
  "step | walks 1 · 4 · 5 · 7 (Greek) | — | the four sum 576 = "
  "24² · VV's walk refused — the refusal is the seat |")
A("")
A("**The thesis, at the strength earned.** Read at the class the "
  "counts earn — observation over the banks, no seat assigned — "
  "the twelve tongues divide by what their walks do with a vowel "
  "line:")
A("")
A(f"- **One family returns home.** The both-ends walk — archon at "
  f"the first step and at the last — stands in exactly the three "
  f"Milesian banks (Greek, and its two mirrors at mirror class), "
  f"and in each it is the same walk: the 8-walk, breaking at the "
  f"tens and returning at the hundreds. *Killing evidence:* any "
  f"recomputation giving another tongue a both-ends walk, or "
  f"taking the 8-walk's return from any of the three.")
A(f"- **The widest spread is Armenian.** Six archon-steps on six "
  f"walks, at four class-depths, including the map's only "
  f"thousands-step archon. *Killing evidence:* a recount of the "
  f"six filed vowels (Ա Ե Ը Ի Ո Ւ) against the bank.")
A(f"- **The order-priced bank ties the Milesian count without a "
  f"Milesian price.** Glagolitic also counts seven archon-steps, "
  f"by alphabet order alone — and is the one tongue whose 8 is a "
  f"stranger at home. *Killing evidence:* a recount of Plate "
  f"XI's vowel row against the bank, or a Glagolitic price for "
  f"Ⰷ other than 8.")
A(f"- **The holes have addresses.** Every HOLE in the map stands "
  f"at a printed coordinate: Georgia's fifth class (eight), "
  f"Arabic's thousands (eight walks), Glagolitic's runs and "
  f"thousands (six), Japan's grid (three), Korea's final stratum "
  f"(three walks) and initial stratum (eleven clusters), Latin's "
  f"W (one), Ge'ez's eighth slot (one). *Killing evidence:* a "
  f"letter shown standing at any of those coordinates in its "
  f"bank.")
A(f"- **Two walks cannot break, for opposite reasons.** Hebrew's "
  f"sofit walk cannot break in price because its price never "
  f"moves; Ge'ez's order-walk cannot meet a stranger because its "
  f"steps are vowels by construction. Their breaks are of the "
  f"other kind — dress and price-zero — and stand printed in "
  f"their sections. *Killing evidence:* a final form priced "
  f"otherwise at face value, or a Ge'ez order-step that is not a "
  f"vowel grade.")
A(f"- **The hybrids stand on archons only.** Every component of "
  f"the diphthong four is an archon step of its walk, and the "
  f"four sum to the square of the Triple H's weight. "
  f"*Killing evidence:* a component shown a stranger on its "
  f"walk, or the sum recomputed from 576.")
A("")
A("Nothing in this section seats anything. The pattern is "
  "printed at observation class, under the presumption rule "
  "within its tier: the counts stand until challenged and "
  "disproven by evidence, and each claim above names its "
  "evidence.")
A("")
A("## §XVI — THE AUDIT")
A("")
A("Every step of every walk in §II–§XIV was taken from the "
  "engine's banks at build, controls first (θέλημα 93 · "
  "VAPOUR 93 · σφίγξ 773, all true). The independent audit "
  "recomputes every walk from the banks and the plates' seat "
  "orders, re-derives every count, break, and total, re-weighs "
  "the founding coordinates and the hybrids, and checks the PDF "
  "text layer for the walks, the totals, and the resolving "
  "footer. Its results file stands beside the builders in the "
  "research folder; the map is not done until the audit passes, "
  "per the standing law.")
A("")
A("## §XVII — THE FOUR ELEMENTS — THE CONTENT TEST")
A("")
A("- **Inputs:** the engine's banks entire (seventeen weigh() "
  "systems; the twelve walked here); the twelve plates and their "
  "filings of vowels, seats, fences, and doors; the Archon "
  "battery and the seating; the INRI · JHS audit and its founding "
  "coordinates; the Roman instrument for the refusal.")
A("- **Processes:** the class-walk computed per tongue on its own "
  "axis; grading of every step; break and return coordinates "
  "taken by the instrument's law; the hybrids walked by "
  "components; the summary counted from the walks, never "
  "estimated.")
A("- **Outputs:** this map — twelve tongue-sections, the "
  "hybrids' walk, and one summary face: archon-steps, breaks, "
  "returns, forks, and holes, each at its coordinate.")
A("- **Tolerances:** zero unrecomputed steps; zero grades "
  "printed above the tongue's own filing; zero seats taken. A "
  "step that fails recomputation zeroes its walk's count and is "
  "struck marked, never vanished.")
A("")
A("## §XVIII — QUESTIONS FOR HIS PEN")
A("")
A("One question genuinely arises from this build, and it is the "
  "founder's alone:")
A("")
A("1. **The grade translations.** The instrument's three grades "
  "were coined for letter-classes. Five sections of this map "
  "translate them onto axes that are not classes — Arabic's "
  "matres at ARCHON grade (§VII), Hebrew's DRESS-STEP (§VIII), "
  "Latin's UNMOVED / MOVED (§IX), Japanese's CARRIER (§X), "
  "Ge'ez's VOWEL-STEP and ZERO (§XI), Korean's HINGE (§XIII). "
  "The translations are printed as the map's working dress, each "
  "marked at its section's head. Whether they stand as the "
  "instrument's standing convention — so that future walks are "
  "graded by them without re-derivation — is an act of his pen, "
  "as the instrument itself is his coinage's child.")
A("")
A("No other question arises from this matter. The North Korean "
  "order (§XIII) already stands at his pen from Plate XII and is "
  "cited there, not raised anew; the seating's questions stand in "
  "their own instrument and are not re-asked here.")
A("")
A("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
A("")
A("1. *Scripture:* \"Let him that hath understanding count the "
  "number of the beast\" (Revelation 13:18) — the counting "
  "imperative this instrument obeys in form: a number is a thing "
  "to be counted, recomputed, and checked, not admired. The "
  "888 that founds the walk stands in the Sibylline witness, "
  "carried by the INRI · JHS audit.")
A("2. *The classical well:* the Milesian numerals are the Greeks' "
  "own — the letters priced by class in the inscriptions and the "
  "grammarians — and Agrippa's Latin (De occulta philosophia, "
  "1533) is the Renaissance's repricing of the same alphabet: "
  "the two banks of §IX are the two ends of one tradition's "
  "walk through time.")
A("3. *The founder's own well:* Liber Oz is LXXVII, and 1776 "
  "encodes 93 (17 + 76) and 777 (776 + 1) in his gnosis — the "
  "numbers this engine keeps meeting are met on his ground, "
  "under his Flagpole, and the map claims no other antiquity "
  "for them than the banks attest.")
A("4. *The house well:* the twelve plates for every seat order, "
  "vowel filing, fence, and door relied on; the Archon battery "
  "(656d667) for the Nine and the five-tongue 8; the seating "
  "(0760c8a) for what a seat is; the INRI · JHS audit (d5250ac) "
  "for the founding coordinates. The engine is the authority "
  "for every number herein.")
A("5. *The dry wells, stated:* no case in the law reports bears "
  "on the stepping of letters through their classes, and the "
  "oral tradition of hip-hop — this house's fourth well — "
  "offers no genuine line on the class-walk that the desk can "
  "cite without stretching it. Both wells are left dry rather "
  "than padded, per the format's law.")
A("")
A("## TABLE OF AUTHORITIES (condensed)")
A("")
A("| Authority | What it carries |")
A("|---|---|")
A("| The pontifex engine (weigh, hangul, numerals) | Every step, "
  "price, and refusal in §II–§XIV |")
A("| PLATES I–XII (196025e · 1389c16 · 5f0b4bd · 8e6f01e · "
  "8d6cd59 · 67d5acc · 5c03d88 · 645bcbb · 933f8fd · 052fd28 · "
  "b40abac · 2ef9ba9) | Each tongue's seat order, vowel filing, "
  "fences, doors, and tiers |")
A("| PLATE XIII — THE DIAL (dae88e0) | The stations the grades "
  "are not confused with |")
A("| THE-ARCHON-BATTERY (656d667) | The Nine, their roots, the "
  "five-tongue 8, the diphthong four |")
A("| THE-SEATING-OF-THE-ARCHONS (0760c8a) | The marks; what "
  "seating is, and is not done here |")
A("| THE-INRI-JHS-AUDIT (d5250ac) | The founding coordinates: "
  "ΗΗΗ = HHH = 24 · ΙΗΣΟΥΣ 888 · ΩΠΗ |")
A("| Revelation 13:18; the Sibylline witness | The counting "
  "imperative; the 888's antiquity |")
A("| Agrippa, De occulta philosophia (1533) | The second Latin "
  "bank of §IX |")
A("")
A("## COLOPHON")
A("")
A("Generated 2026-11-24 at the desk, from the engine and the "
  "plates named above; every step scripted, none hand-copied. "
  "Set in the Lex Stellarrvm family in its MAGVS seat; the print "
  "dress declared in the MAGVS colophon. Authorship attributed "
  "exclusively to Johnathan 'Qasparr' Monroe (Greek, -ARR, All "
  "Rights Reserved, Without Prejudice).")
A("")
A("Method of Science. Aim of Religion.")
A("")
A("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, "
  "All Rights Reserved, Without Prejudice. Right of claim hereby "
  "reserved and coined under the authority of the Living Man.")
A("")
A("93 — Live, Love, and let Love, Live.")

MASTER.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {MASTER} — {MASTER.stat().st_size} bytes")
print(f"archon-steps: Greek {GR_A} · Coptic {CO_A} · Cyrillic "
      f"{CY_A} · Armenian {ARM_A} · Georgian {GEO_A} · Arabic "
      f"{ARA_A} · Glagolitic {GLA_A}")
print(f"both-ends: Greek {GR_BOTH} · Coptic {CO_BOTH} · Cyrillic "
      f"{CY_BOTH} · Armenian {ARM_BOTH} · Georgian {GEO_BOTH} · "
      f"Arabic {ARA_BOTH} · Glagolitic {GLA_BOTH}")
