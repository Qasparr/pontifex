#!/usr/bin/env python3
# =============================================================================
# "Weigh the tongue that has no tongue." — the scribe
#
# Thelemic date: Wed 2026-10-14 (dies mercurii), Anno V:xii e.n.
#
# 93.
#
# weigh_thirteen.py — the Thirteenth Tongue: a gematria system for computer
# programming languages, weighed in unison with the traditional methods.
#
# Johnathan's order (2026-10-14, his words): "we should pioneer that too."
# Research stage. This script is the calculated design: it does not decree
# anything. Every finding below is CONSTRUCTED tier — hypothesis, never
# doctrine — and waits on his red pen.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): hypothesis -> method -> observation ->
# result. The hypothesis: a programming language's name can be weighed like
# any word, in its own tongue where it has one and by honest fallback where
# it has none. The method: four banks, one audit, one watch-list. The
# observation: the tables below. The result: bridges and convergences,
# flagged CONSTRUCTED, for the red pen.
#
# MECHANISM: ptk supplies the ATTESTED banks (Hebrew mispar hechrechi,
# Greek isopsephy, English ordinal, Agrippa, Arabic abjad) and the honest
# weigh() engine. The scribe contributes only the transliteration schemes
# below — his own construction, documented letter by letter — and the
# corpus of language names. The engine sums; the scribe does not hand-tune.
#
# DOCTRINE: (1) English ordinal is the NATIVE bank here — programming
# language names are coined in Latin script, so the plain ordinal is the
# word weighed in its own tongue. (2) Hebrew, Greek, Arabic are FALLBACK
# banks via constructed transliteration; Hebrew is the proper fallback for
# a tongue with no table (his standing ruling). (3) Three-tier provenance:
# the banks are ATTESTED, the transliterations and this whole application
# are CONSTRUCTED — every bridge found here is a hypothesis, never doctrine.
# (4) The purpose is the bridge: a number shared across two honest banks
# for the same word (cf. AXONEME=77 English = עז=77 Hebrew). (5) A weighing
# is only honest if its skips are visible: unknown() audits every dropped
# character (digits, +, #, -).
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import sys

sys.path.insert(0, "/home/hatch/workspace/pontifex/tools")
from ptk import weigh as W

# ---------------------------------------------------------------------------
# DOCTRINE: the transliteration schemes. CONSTRUCTED by the scribe —
# consistent, documented, and revisable by the red pen. Each maps one Latin
# letter to one letter of the fallback tongue; the choice is phonetic where
# the tongues agree and conventional where they do not. The notes below are
# the whole honesty of the scheme: nothing hidden, nothing "obvious."
# ---------------------------------------------------------------------------

# -- English -> Hebrew (mispar hechrechi bank) --------------------------------
# MECHANISM: C=/k/ rides כ (documented); P stays פ; Q takes ק; V/W/U all ride
# ו as the waw-family; X collapses כס to ס (documented simplification —
# the red pen may rule כס instead, which would add 80+60=140 per X).
EN_TO_HE = {
    'A': 'א', 'B': 'ב', 'C': 'כ', 'D': 'ד', 'E': 'ה', 'F': 'פ', 'G': 'ג',
    'H': 'ה', 'I': 'י', 'J': 'י', 'K': 'כ', 'L': 'ל', 'M': 'מ', 'N': 'נ',
    'O': 'ו', 'P': 'פ', 'Q': 'ק', 'R': 'ר', 'S': 'ס', 'T': 'ת', 'U': 'ו',
    'V': 'ו', 'W': 'ו', 'X': 'ס', 'Y': 'י', 'Z': 'ז',
}

# -- English -> Greek (Milesian isopsephy bank) ------------------------------
# MECHANISM: C=/k/ rides κ; F takes φ (the aspirate); H takes η (the rough
# vowel); Q rides κ; W takes ω (documented convention — υ would be the
# phonetic choice, but ω keeps W distinct from U/V; red-pen revisable).
EN_TO_GR = {
    'A': 'α', 'B': 'β', 'C': 'κ', 'D': 'δ', 'E': 'ε', 'F': 'φ', 'G': 'γ',
    'H': 'η', 'I': 'ι', 'J': 'ι', 'K': 'κ', 'L': 'λ', 'M': 'μ', 'N': 'ν',
    'O': 'ο', 'P': 'π', 'Q': 'κ', 'R': 'ρ', 'S': 'σ', 'T': 'τ', 'U': 'υ',
    'V': 'υ', 'W': 'ω', 'X': 'ξ', 'Y': 'υ', 'Z': 'ζ',
}

# -- English -> Arabic (abjad bank, Eastern order) ----------------------------
# MECHANISM: P has no Arabic letter — ب (ba) is the documented closest
# (documented, not hidden); V takes ف; W/U/O ride و as the waw-family;
# X collapses to س (documented, as with the Hebrew scheme).
EN_TO_AR = {
    'A': 'ا', 'B': 'ب', 'C': 'ك', 'D': 'د', 'E': 'ه', 'F': 'ف', 'G': 'ج',
    'H': 'ح', 'I': 'ي', 'J': 'ي', 'K': 'ك', 'L': 'ل', 'M': 'م', 'N': 'ن',
    'O': 'و', 'P': 'ب', 'Q': 'ق', 'R': 'ر', 'S': 'س', 'T': 'ت', 'U': 'و',
    'V': 'ف', 'W': 'و', 'X': 'س', 'Y': 'ي', 'Z': 'ز',
}

# -- The watched numbers ------------------------------------------------------
# DOCTRINE: guides, never claims. The chart draws them as lines; the report
# flags hits. A hit is a coincidence wearing a costume until the red pen
# says otherwise.
WATCHED = [13, 26, 32, 77, 93, 418, 666, 777]


def transliterate(name, scheme):
    """MECHANISM: map each Latin letter through the scheme; drop the rest.

    DOCTRINE: what drops is not lost — dropped() returns it, and the
    report prints the skips beside every weighing. C++, C#, Objective-C,
    F# all shed their symbols here, visibly.
    """
    out, dropped = [], []
    for ch in name.upper():
        if ch in scheme:
            out.append(scheme[ch])
        else:
            dropped.append(ch)
    return "".join(out), dropped


def theo_reduce(n):
    """MECHANISM: theosophical reduction — digital root, 9 stays 9."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


# -- The corpus ----------------------------------------------------------------
# DOCTRINE: canonical names, uppercase, spanning 1957 (FORTRAN) to 2023
# (MOJO). No cherry-picking: the list was fixed before any weighing. Symbols
# (+, #, -) are kept in the name so the audit shows them dropping.
CORPUS = [
    "FORTRAN", "COBOL", "BASIC", "LISP", "ALGOL", "APL", "FORTH", "PASCAL",
    "ADA", "SMALLTALK", "PROLOG", "ASSEMBLY", "SQL", "C", "C++", "C#",
    "F#", "AWK", "SCHEME", "ML", "D", "OBJECTIVE-C", "GROOVY", "ERLANG",
    "HASKELL", "PERL", "PYTHON", "RUBY", "JAVA", "LUA", "JAVASCRIPT", "PHP",
    "MATLAB", "SCALA", "CLOJURE", "GO", "RUST", "SWIFT", "KOTLIN",
    "TYPESCRIPT", "DART", "JULIA", "ZIG", "MOJO", "ELIXIR", "OCAML",
    "POWERSHELL", "R", "HTML",
]


def weigh_all():
    """MECHANISM: one pass per language, four banks, one audit line each."""
    rows = []
    for name in CORPUS:
        letters = "".join(ch for ch in name.upper() if ch.isalpha())
        eng = W.weigh(name.upper(), W.LATIN_ORDINAL)
        agr = W.weigh(name.upper(), W.AGRIPPA)
        he_word, he_drop = transliterate(name, EN_TO_HE)
        gr_word, gr_drop = transliterate(name, EN_TO_GR)
        ar_word, ar_drop = transliterate(name, EN_TO_AR)
        heb = W.weigh(he_word, W.HEBREW)
        grk = W.weigh(gr_word, W.GREEK)
        arb = W.weigh(ar_word, W.ARABIC_ABJAD)
        dropped = sorted(set(he_drop) & set(gr_drop) & set(ar_drop))
        rows.append({
            "name": name, "letters": letters,
            "ENG": eng, "AGRIPPA": agr, "HEB": heb, "GRK": grk, "ARB": arb,
            "dropped": "".join(dropped) or "-",
            "he_word": he_word, "gr_word": gr_word, "ar_word": ar_word,
        })
    return rows


def find_bridges(rows):
    """MECHANISM: a bridge = one word, one number, two honest banks.

    DOCTRINE: this is the whole purpose of the exercise — the shared number
    across two banks (AXONEME=77/עז=77 is the model). CONSTRUCTED tier:
    a bridge here is a hypothesis wearing work clothes, never doctrine.
    """
    banks = ["ENG", "AGRIPPA", "HEB", "GRK", "ARB"]
    bridges = []
    for r in rows:
        seen = {}
        for b in banks:
            v = r[b]
            seen.setdefault(v, []).append(b)
        for v, bs in seen.items():
            if len(bs) >= 2:
                bridges.append((r["name"], v, bs))
    return bridges


def find_watched(rows):
    """MECHANISM: flag every weighing that lands on a watched number."""
    hits = []
    for r in rows:
        for b in ["ENG", "AGRIPPA", "HEB", "GRK", "ARB"]:
            if r[b] in WATCHED:
                hits.append((r["name"], b, r[b]))
    return hits


def find_shared(rows):
    """MECHANISM: two languages sharing one number in one bank — the
    correspondence-table shape (two words, one cell)."""
    shared = {}
    for r in rows:
        for b in ["ENG", "AGRIPPA", "HEB", "GRK", "ARB"]:
            shared.setdefault((b, r[b]), []).append(r["name"])
    return {k: v for k, v in shared.items() if len(v) >= 2}


def main():
    rows = weigh_all()

    # -- 1. The full table -----------------------------------------------------
    print("=" * 100)
    print("THE THIRTEENTH TONGUE — full weighing table (CONSTRUCTED tier)")
    print("=" * 100)
    print(f"{'LANGUAGE':<12}{'ENG':>6}{'AGRP':>6}{'HEB':>6}{'GRK':>6}{'ARB':>6}  "
          f"{'red':>3}  dropped")
    for r in rows:
        red = theo_reduce(r["ENG"])
        print(f"{r['name']:<12}{r['ENG']:>6}{r['AGRIPPA']:>6}{r['HEB']:>6}"
              f"{r['GRK']:>6}{r['ARB']:>6}  {red:>3}  {r['dropped']}")

    # -- 2. Bridges ------------------------------------------------------------
    print()
    print("=" * 100)
    print("BRIDGES — one word, one number, two honest banks")
    print("=" * 100)
    bridges = find_bridges(rows)
    if bridges:
        for name, v, bs in bridges:
            print(f"  {name:<12} = {v:<5} across {', '.join(bs)}")
    else:
        print("  (none — no two banks agree on any one word)")

    # -- 3. Watched-number hits -------------------------------------------------
    print()
    print("=" * 100)
    print("WATCHED HITS — 13 26 32 77 93 418 666 777 (guides, never claims)")
    print("=" * 100)
    hits = find_watched(rows)
    if hits:
        for name, b, v in hits:
            print(f"  {name:<12} [{b:<7}] = {v}")
    else:
        print("  (none)")

    # -- 4. Shared cells --------------------------------------------------------
    print()
    print("=" * 100)
    print("SHARED CELLS — two languages, one number, one bank")
    print("=" * 100)
    shared = find_shared(rows)
    if shared:
        for (b, v), names in sorted(shared.items(), key=lambda x: (x[0][0], x[0][1])):
            print(f"  [{b:<7}] {v:<5} <- {', '.join(names)}")
    else:
        print("  (none)")

    # -- 5. CSV for the record ---------------------------------------------------
    out = "/home/hatch/workspace/pontifex/research/thirteen-tongues/weighings.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "ENG", "AGRIPPA", "HEB", "GRK", "ARB",
                    "theo_reduce_ENG", "dropped", "he_word", "gr_word", "ar_word"])
        for r in rows:
            w.writerow([r["name"], r["ENG"], r["AGRIPPA"], r["HEB"], r["GRK"],
                        r["ARB"], theo_reduce(r["ENG"]), r["dropped"],
                        r["he_word"], r["gr_word"], r["ar_word"]])
    print()
    print(f"CSV written: {out}")
    print()
    print("Live, Love, and let Love, Live. — 93.")


if __name__ == "__main__":
    main()
