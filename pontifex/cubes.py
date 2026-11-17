#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — cubes.py — the parallel cubes (77³ beside 93³)
#
# Epigraph: "Do what thou wilt shall be the whole of the Law."
# — Liber AL vel Legis I:40.
#
# Thelemic date: XVII day of November, dies Martis, Sol in Scorpio,
# Anno V:xii e.n. (2026 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: that the house's two cubes — 77³, the Enclave Sphere
#     of the Pyramidasphere instrument, and 93³, ordered by the founder
#     2026-11-17 ("Apply or Parallel with Lex Stellarrvm 93^3") — form
#     a parallel the engine should carry as DERIVED arithmetic, on the
#     doubles.py precedent: computed from the integers, never frozen.
#   Method: cube each base by multiplication; factor each cube by
#     trial division; take each threefold sum; and pin the Greek seats
#     (ΚΥ, θέλημα) against the engine's own weigh() at check time.
#   Observation: 77³ = 456,533 = 7³ × 11³ and 93³ = 804,357 = 3³ × 31³
#     — the second cube seats the 31 of the founder's pyramid under
#     the Cube (27), and the first cube's 11³ is the very number
#     Plate II of 2026-11-17 prints on its face (1331).
#   Result: the parallel below, DERIVED — a theorem of arithmetic and
#     of the attested Greek bank, not a new bank. The doctrine that
#     seats these cubes (the instruments, the plates, the synergy
#     circuit) stands in research/cubes/CUBES.md; this module is only
#     its weighing face.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The parallel cubes.

DOCTRINE: the cubes are computed from their bases at import — square,
cube, prime factorization, and threefold — never copied in as
literals. If a base were ever corrected, the record would follow it;
cubes_checks() pins every figure against independent recomputation
and against the engine's weigh() for the Greek seats, so a divergence
fails loudly instead of drifting in silence.

REASONING (why these two bases, and no others):
  * 77 is the house's bridge number — AXONEME in the English ordinal
    bank, עז in the Hebrew bank — and 77³ = 456,533 is the Enclave
    Sphere of the stamped Pyramidasphere instrument (2026-11-17),
    the Trinity's field size (3 × 456,533 = 1,369,599).
  * 93 is θέλημα in the Greek bank — the Will — and the founder
    ordered its cube in parallel (2026-11-17). 93 = 3 × 31 seats the
    pyramid's own 31 (the 31-node frame of the Pyramidasphere scene)
    under the Cube 3³ = 27 of the house weighing order.
  * The Greek pair stands beside the cubes because the founder's
    proof rule seats claims in Greek: ΚΥ = 420 (κ 20 + υ 400,
    ATTESTED) is the KY measure proven in the Pyramidasphere
    instrument; θέλημα = 93 is the control and the 93-cube's base.
"""


def factorize(n):
    """The prime factorization of n as {prime: exponent}. Pure.

    MECHANISM: trial division by increasing integers; n is small
    (the cubes are under a million), so the naive road is the honest
    one — no sieve, no cache, nothing to drift.
    """
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _cube_record(base):
    """One base's derived record: square, cube, factorization, fold.

    MECHANISM: every figure is computed from `base` here — the cube
    by multiplication, the factorization by factorize() on the cube
    (not on the base, so the record proves the cube's own factors),
    the threefold as 3 × cube (the house's 3 Fold: three fields).
    """
    cube = base ** 3
    return {
        'base': base,
        'square': base ** 2,
        'cube': cube,
        'factorization': factorize(cube),
        'threefold': 3 * cube,
    }


# -- The parallel, computed — never frozen ---------------------------------
# MECHANISM: derived from the two bases at import, on the doubles.py
# precedent (the map there is derived from the attested banks; the
# record here is derived from the integers themselves).
CUBES = {base: _cube_record(base) for base in (77, 93)}

# The Greek seats, recorded as MEASURED values with their reasoning;
# cubes_checks() pins both against the engine's weigh() so the record
# cannot drift from the bank it cites.
GREEK_SEATS = {
    'ΚΥ': {
        'value': 420,
        'reasoning': "κ 20 + υ 400 in the attested Greek bank — the "
                     "KY measure proven in the Pyramidasphere "
                     "instrument; KY's expansion is the founder's "
                     "alone and is not recorded here.",
    },
    'θέλημα': {
        'value': 93,
        'reasoning': "the Will, in the attested Greek bank — the "
                     "control of the Greek register and the base of "
                     "the 93-cube itself.",
    },
}

# The founder's declared equation (the Pyramidasphere visualization's
# inscription, 2026-11-17), recorded as a DECLARATION with the desk's
# arithmetic beside it — both figures, neither smoothed, per the
# house law for declared equations.
DECLARED_EQUATION = {
    'inscription': '31^3 = 93',
    'kind': "the founder's declared equation",
    'by_multiplication': 31 ** 3,          # 29,791
    'by_threefold_sum': 31 + 31 + 31,      # 93
}


def cubes_checks():
    """Self-checks for the parallel cubes. Returns [(name, passed, got)].

    MECHANISM: kept beside engine_checks() rather than inside it, on
    the doubles_checks()/greek_checks() precedent — the established
    self-test stands untouched as the no-collateral witness; run all
    for the full suite. The engine is imported here, inside the
    function, so the modules stay one-directional (cubes → integers
    at import; the engine is consulted only when the checks run).
    """
    from .engine import weigh
    from .doubles import DOUBLES
    checks = []

    # 1. THE 77 CUBE: by multiplication, and its factors recomputed
    #    from the cube itself — 7³ × 11³ and nothing else.
    c77 = CUBES[77]
    prod = 1
    for p, e in c77['factorization'].items():
        prod *= p ** e
    checks.append(('77^3 == 456,533 by multiplication; factors 7^3 × 11^3',
                   c77['cube'] == 456533 and prod == 456533
                   and c77['factorization'] == {7: 3, 11: 3},
                   (c77['cube'], c77['factorization'])))

    # 2. THE 93 CUBE: by multiplication, and its factors — 3³ × 31³:
    #    the pyramid's 31 under the Cube 27.
    c93 = CUBES[93]
    prod = 1
    for p, e in c93['factorization'].items():
        prod *= p ** e
    checks.append(('93^3 == 804,357 by multiplication; factors 3^3 × 31^3',
                   c93['cube'] == 804357 and prod == 804357
                   and c93['factorization'] == {3: 3, 31: 3},
                   (c93['cube'], c93['factorization'])))

    # 3. THE SQUARES, printed because the parallel reads cleaner with
    #    them pinned: 77² = 5,929 and 93² = 8,649.
    checks.append(('squares: 77^2 == 5,929 and 93^2 == 8,649',
                   c77['square'] == 5929 and c93['square'] == 8649,
                   (c77['square'], c93['square'])))

    # 4. THE 3 FOLDS: three fields of each cube — 1,369,599 beside
    #    2,413,071.
    checks.append(('3 folds: 3 × 456,533 == 1,369,599; 3 × 804,357 == 2,413,071',
                   c77['threefold'] == 1369599
                   and c93['threefold'] == 2413071,
                   (c77['threefold'], c93['threefold'])))

    # 5. THE GREEK SEATS, pinned against the engine's own weigh() —
    #    the record answers to the bank, not to itself.
    bad = [(w, GREEK_SEATS[w]['value'], weigh(w, 'greek')['value'])
           for w in GREEK_SEATS
           if weigh(w, 'greek')['value'] != GREEK_SEATS[w]['value']]
    checks.append(('Greek seats == engine weigh(): ΚΥ 420, θέλημα 93',
                   not bad, bad or 'both seats agree with the bank'))

    # 6. THE KY COORDINATE IN THE YOUNGER BANKS: KY ordinal 36 — the
    #    RR pair's own seat on the double-letter map (doubles.py) —
    #    printed so the Greek 420 never floats without its coordinate.
    ky_ord = weigh('KY', 'latin_ordinal')['value']
    checks.append(('KY ordinal == 36 == RR pair ordinal (the coordinate)',
                   ky_ord == 36 and DOUBLES['RR']['ordinal'] == 36,
                   (ky_ord, DOUBLES['RR']['ordinal'])))

    # 7. THE DECLARED EQUATION'S BOUNDARY: the inscription stands as
    #    the founder's declaration; the arithmetic beside it reads
    #    29,791 by multiplication and 93 by the threefold sum — the
    #    check asserts BOTH figures, so neither can swallow the other.
    de = DECLARED_EQUATION
    checks.append(('declared 31^3 = 93: arithmetic 29,791; threefold sum 93',
                   de['by_multiplication'] == 29791
                   and de['by_threefold_sum'] == 93,
                   (de['by_multiplication'], de['by_threefold_sum'])))
    return checks


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
