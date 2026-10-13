#!/usr/bin/env python3
# =============================================================================
# ARAMAIC BANK — worker #7 of 12, the PONTIFEX twelve-tongues research
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: ☉ in 18° Libra, ☽ in 12° Scorpio, dies solis,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   HYPOTHESIS: Aramaic's 22-letter abjad order carries the same values as
#     Hebrew mispar hechrechi (the shared Northwest Semitic tradition), so
#     weighing the corpus in Aramaic letters reproduces the Hebrew bank —
#     and any agreement between the two banks is ARITHMETIC IDENTITY, not
#     an independent bridge (the English↔Latin anti-finding, repeated).
#   METHOD: transliterate each Latin term into Jewish Aramaic square script
#     with the repo's documented LATIN_TO_HEBREW map (CONSTRUCTED), weigh
#     with the 22-letter values (ATTESTED for Aramaic — see aramaic.md for
#     the tier justification), report mergers fired, collisions, target hits.
#   OBSERVATION: the script's letter-by-letter sums below.
#   RESULT: calibration ܥܙ/עז = 77 holds; ABRAHADABRA = 418 in Aramaic
#     letters exactly as in Hebrew; no 666/777/93/11 hits among the corpus.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the shared corpus in Aramaic letters.

DOCTRINE: the scribe invents no table. The 22 values are the tradition's own
(ܐ/א=1 … ܬ/ת=400); the transliteration map is the repo's documented one, and
every merger it forces is reported, never hidden. Where the Aramaic weighing
agrees with the Hebrew worker's, the report marks it ARITHMETIC IDENTITY.
"""

import csv
import os

# -- The 22 values: shared Northwest Semitic tradition (ATTESTED) --------------
# MECHANISM: byte-identical to pontifex.tables.HEBREW; recorded here so the
# Aramaic bank stands on its own feet and the Hebrew-identity comparison is
# checkable letter by letter. Jewish square script = the script of Biblical
# Aramaic (Ezra, Daniel) and the Talmud, where letter-number weighing is
# actually practiced on Aramaic text.
ARAMAIC = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
    'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
}

# -- Transliteration map: Latin → Aramaic square letters (CONSTRUCTED) --------
# MECHANISM: greedy digraphs first (ch→ח, sh→ש, th→ת), then single letters,
# identical to pontifex.tables.LATIN_TO_HEBREW. DOCTRINE: this map is the
# scribe's construction — every merger is a documented loss, listed below.
DIGRAPHS = {'ch': 'ח', 'sh': 'ש', 'th': 'ת'}
SINGLES = {
    'a': 'א', 'b': 'ב', 'c': 'ק', 'd': 'ד', 'e': 'ה', 'f': 'פ', 'g': 'ג',
    'h': 'ה', 'i': 'י', 'j': 'י', 'k': 'כ', 'l': 'ל', 'm': 'מ', 'n': 'נ',
    'o': 'ו', 'p': 'פ', 'q': 'ק', 'r': 'ר', 's': 'ס', 't': 'ת', 'u': 'ו',
    'v': 'ו', 'w': 'ו', 'x': 'קס', 'y': 'י', 'z': 'ז',
}
# MECHANISM: the mergers, stated plainly — two Latin letters, one Aramaic
# letter, distinction lost in the weighing.
MERGERS = {
    'ה': ['e', 'h'], 'י': ['i', 'j', 'y'], 'ו': ['o', 'u', 'v', 'w'],
    'ק': ['c', 'q'], 'פ': ['f', 'p'],
}

# -- The shared corpus ---------------------------------------------------------
CORPUS = ["AXONEME", "OZ", "TRVVTH", "THELEMA", "AGAPE", "BABALON",
          "HERU-RA-HA", "ABRAHADABRA", "QIRA", "LIBERTY", "CELL"]
TARGETS = {418, 666, 777, 93, 77, 11}


def transliterate(term):
    """Render a Latin term in Aramaic square letters.

    MECHANISM: hyphen is a separator and is dropped, not weighed (stated
    choice); the double V of TRVVTH is two letters and weighed twice (stated
    choice — no elision); digraphs fire greedily left to right.
    """
    src = term.lower().replace('-', '')
    out, i = [], 0
    while i < len(src):
        pair = src[i:i + 2]
        if pair in DIGRAPHS:
            out.append(DIGRAPHS[pair]); i += 2
        else:
            out.append(SINGLES[src[i]]); i += 1
    return ''.join(out)


def weigh(spelling):
    """Letter-by-letter sum; returns (total, [(letter, value), ...])."""
    parts = [(ch, ARAMAIC[ch]) for ch in spelling]
    return sum(v for _, v in parts), parts


def mergers_fired(term):
    """Which documented mergers fired in this term's transliteration."""
    fired = []
    low = term.lower()
    for letter, lats in MERGERS.items():
        hit = sorted({c for c in lats if c in low})
        if len(hit) > 1:
            fired.append(f"{letter}←{'/'.join(hit)}")
    if 'x' in low:
        fired.append("קס←x (one letter rendered as two: value split, not merged)")
    for dg, letter in DIGRAPHS.items():
        if dg in low:
            fired.append(f"{letter}←{dg} (digraph fired greedily)")
    return fired


def main():
    rows = []
    for term in CORPUS:
        spelling = transliterate(term)
        total, parts = weigh(spelling)
        detail = '+'.join(f"{ch}={v}" for ch, v in parts)
        fired = mergers_fired(term)
        hits = sorted(t for t in TARGETS if t == total)
        rows.append({
            'term': term,
            'language': 'Aramaic',
            'script_form': spelling,
            'transliteration_convention':
                'PONTIFEX-LATIN-TO-ARAMAIC v1: greedy digraphs ch→ח sh→ש th→ת; '
                'a→א b→ב c→ק d→ד e→ה f→פ g→ג h→ה i/j/y→י k→כ l→ל m→מ n→נ '
                'o/u/v/w→ו p→פ q→ק r→ר s→ס t→ת x→קס z→ז; hyphen dropped; '
                'double-V weighed twice (no elision)',
            'table_used': 'Aramaic 22-letter abjad, א=1…ת=400 (values identical to Hebrew mispar hechrechi)',
            'provenance_tier': 'CONSTRUCTED — attested table, constructed transliteration',
            'value': total,
            'mergers_or_loss': '; '.join(fired) if fired else 'none',
            'notes': (f"letter-by-letter: {detail} = {total}. "
                      + (f"TARGET HIT: {hits}. " if hits else "no target-number hit. ")
                      + "Numerical agreement with the Hebrew bank (same map, same values) "
                        "is ARITHMETIC IDENTITY, not independent evidence."),
        })
        print(f"{term:12s} {spelling:12s} {detail} = {total}"
              + (f"  <-- TARGET {hits}" if hits else ""))

    # -- Calibration rows: the עז bridge, weighed natively, then script-swapped
    # MECHANISM: עז is an attested Aramaic/Hebrew word; its value in its own
    # tradition's numbers is the anchor. ܥܙ shows the same number in Syriac
    # Estrangela letterforms — values are script-invariant.
    for term, spelling, tier, note in [
        ('עז-equivalent', 'עז', 'ATTESTED — attested word in its own tradition’s numbers',
         'calibration anchor: ע=70 + ז=7 = 77. The canonical bridge AXONEME=77=עז is English-ordinal-side; in Aramaic letters AXONEME=267.'),
        ('ܥܙ (script-invariance demo)', 'ܥܙ', 'DERIVED — same tradition, Syriac script-descent letterforms',
         'ܥ=70 + ܙ=7 = 77 in Estrangela: values do not change across scripts, only letterforms.'),
    ]:
        rows.append({
            'term': term, 'language': 'Aramaic', 'script_form': spelling,
            'transliteration_convention': 'n/a — native spelling, no transliteration',
            'table_used': 'Aramaic 22-letter abjad, א=1…ת=400',
            'provenance_tier': tier, 'value': 77,
            'mergers_or_loss': 'none',
            'notes': note,
        })
    print("עז-equivalent עז ע=70+ז=7 = 77  <-- TARGET [77] (calibration, not corpus)")

    # -- Collisions and targets --------------------------------------------------
    vals = {}
    for r in rows:
        vals.setdefault(r['value'], []).append(r['term'])
    collisions = {v: ts for v, ts in vals.items() if len(ts) > 1}
    print("\nCOLLISIONS (same number, different terms):",
          collisions if collisions else "none among weighed terms")

    out = os.path.expanduser('~/workspace/pontifex/research/twelve-tongues/aramaic-values.csv')
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['term', 'language', 'script_form',
                                          'transliteration_convention', 'table_used',
                                          'provenance_tier', 'value',
                                          'mergers_or_loss', 'notes'])
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {out} ({len(rows)} rows)")


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
