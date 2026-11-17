#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — doubles.py — the double-letter map (the dial's weighing face)
# v0.3.0 "The Third Span"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: XVI day of November, dies lunae, Sol in Scorpio,
# Anno V:xii e.n. (2026 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The name PONTIFEX ("bridge-builder") was proposed by the scribe and approved
# by the author's red pen, 2026-10-07. The doctrine is the author's; the
# mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: that the doubled letters of the Latin alphabet — the pairs
#     AA through ZZ — form a map of their own, with laws a single letter
#     cannot state: a ladder, a void, and a fixed point.
#   Method: weigh every pair on the two attested Latin banks (the ordinal
#     and Agrippa's table) and read the pattern the two banks draw together.
#   Observation: the ordinal bank draws an unbroken ladder of even numbers;
#     Agrippa's bank, drawn from the classical alphabet, leaves one pair
#     weightless and folds two pairs into their neighbours.
#   Result: the map below, DERIVED from the two attested banks — a theorem
#     of the tables, not a third table. The dial built on it (Resonantia,
#     docs/THE-DOUBLE-LETTER-DIAL.md) is the author's doctrine; this module
#     is only its weighing face.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The double-letter map.

DOCTRINE: the pairs are weighed in the two attested Latin banks and the
results recorded as DERIVED — the map adds no values of its own. Every
number here is twice a value the tradition already hands down, or zero
where the tradition hands down nothing. The reasoning for each
load-bearing pair stands in research/doubles/DOUBLES.md; the pitch
methods that seat these weights on the tuning dial stand in Resonantia's
THE-DOUBLE-LETTER-DIAL.md.
"""

from .tables import LATIN_ORDINAL, AGRIPPA

# -- The map, computed — never frozen ---------------------------------------
# MECHANISM: a pair's weight is derived from tables.py at import, not
# copied into a literal. If an attested bank were ever corrected, the map
# would follow the bank; doubles_checks() pins the derivation against the
# engine's weigh() on all 26 pairs in both banks, so any divergence
# between the derivation and the instrument fails loudly instead of
# drifting in silence.
#
# MECHANISM (the three irregularities, all Agrippa's, all attested):
#   * W has no seat in AGRIPPA — the classical alphabet Agrippa worked in
#     has no W — so .get(ch, 0) yields 0 and WW weighs 0: THE VOID.
#   * J stands in AGRIPPA at 9, read as I, so JJ weighs 18, exactly II.
#   * U and V both stand at 200 (U read as V), so UU == VV == 400.
DOUBLES = {
    ch * 2: {
        'ordinal': 2 * LATIN_ORDINAL[ch],
        'agrippa': 2 * AGRIPPA.get(ch, 0),
    }
    for ch in (chr(ord('A') + i) for i in range(26))
}


def pair(pair_word):
    """One pair's seat on the map: {'ordinal': n, 'agrippa': n}.

    MECHANISM: a plain lookup in DOUBLES; the pair is upper-cased first,
    as weigh() folds Latin input the same way.
    """
    return DOUBLES[pair_word.upper()]


def doubles_checks():
    """Self-checks for the double-letter map. Returns [(name, passed, got)].

    MECHANISM: kept beside engine_checks() rather than inside it, on the
    greek_checks() precedent of 2026-11-16 — the established self-test
    stands untouched as the no-collateral witness; run both for the full
    suite. The engine is imported here, inside the function, so the
    modules stay one-directional (doubles → tables at import; the engine
    is consulted only when the checks run), as music.py does.
    """
    from .engine import weigh
    checks = []

    # 1. THE LADDER LAW: in the ordinal bank every pair weighs twice its
    #    letter's position — the unbroken even numbers 2, 4, …, 52.
    bad = [(p, DOUBLES[p]['ordinal']) for i, p in enumerate(
        (chr(ord('A') + k) * 2 for k in range(26)))
        if DOUBLES[p]['ordinal'] != 2 * (i + 1)]
    checks.append(('ladder law: every pair ordinal == 2 × position (2..52)',
                   not bad, bad or 'all 26 on the ladder'))

    # 2. Corollary of the ladder: no pair can weigh odd in the ordinal
    #    bank — 31, 77 and 93 are unreachable by any pair there. (A pair
    #    that weighed odd would break check 1 first; this states the
    #    boundary the dial is built against, in so many words.)
    odds = [p for p in DOUBLES if DOUBLES[p]['ordinal'] % 2]
    checks.append(('no pair weighs odd in the ordinal bank',
                   not odds, odds or 'all 26 even'))

    # 3. The derivation agrees with the instrument: the engine's weigh()
    #    on all 26 pairs, in both banks, returns the map's numbers.
    bad = [(p, sys) for p in DOUBLES for sys in ('latin_ordinal', 'agrippa')
           if weigh(p, sys)['value'] != DOUBLES[p][
               'ordinal' if sys == 'latin_ordinal' else 'agrippa']]
    checks.append(('map == engine weigh() on all 26 pairs, both banks',
                   not bad, bad or '52/52 agree'))

    # 4. THE VOID: WW weighs 46 in the ordinal bank and 0 in Agrippa —
    #    present in the younger bank, absent from the older, because the
    #    classical alphabet has no W to seat.
    checks.append(('WW the void: ordinal 46, agrippa 0',
                   DOUBLES['WW'] == {'ordinal': 46, 'agrippa': 0},
                   DOUBLES['WW']))

    # 5. THE FIXED POINT: II weighs 18 in both banks — the one pair where
    #    the two banks agree exactly.
    checks.append(('II the fixed point: 18 in both banks',
                   DOUBLES['II'] == {'ordinal': 18, 'agrippa': 18},
                   DOUBLES['II']))

    # 6. JJ folds into II in Agrippa (J read as I, 9+9=18) while the
    #    ordinal bank keeps them apart (20 vs 18) — the banks part
    #    exactly here, and the map prints both readings.
    checks.append(('JJ == II in Agrippa (18), apart in ordinal (20 vs 18)',
                   DOUBLES['JJ']['agrippa'] == DOUBLES['II']['agrippa'] == 18
                   and DOUBLES['JJ']['ordinal'] == 20
                   and DOUBLES['II']['ordinal'] == 18,
                   (DOUBLES['JJ'], DOUBLES['II'])))

    # 7. UU == VV in Agrippa (U read as V, 200+200=400) — the identity
    #    the founder's orthography (V for U) rides on.
    checks.append(('UU == VV in Agrippa (400)',
                   DOUBLES['UU']['agrippa'] == DOUBLES['VV']['agrippa'] == 400,
                   (DOUBLES['UU']['agrippa'], DOUBLES['VV']['agrippa'])))

    # 8. The load-bearing seats, weighed on the engine: OO at the
    #    TEE/MAP seat (30), TT at the HOLE seat (40), LL at 24 (the Sigma
    #    low carrier's number), VV at the POM/MOP seat (44), RR at KY's
    #    seat (36), XX at the REFS seat (48).
    seats = [('OO', 'TEE', 30), ('OO', 'MAP', 30), ('TT', 'HOLE', 40),
             ('VV', 'POM', 44), ('VV', 'MOP', 44), ('RR', 'KY', 36),
             ('XX', 'REFS', 48)]
    bad = [(p, w) for p, w, n in seats
           if weigh(p, 'latin_ordinal')['value'] != n
           or weigh(w, 'latin_ordinal')['value'] != n]
    ll = weigh('LL', 'latin_ordinal')['value']
    checks.append(('load-bearing seats: OO 30, TT 40, LL 24, VV 44, '
                   'RR 36, XX 48 — each with its witness word',
                   not bad and ll == 24, bad or ('LL', ll)))
    return checks


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
