#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — numerals.py — the Roman numeral double-letter system
# (the missing link of the Codex Legend, legend piece i)
# v0.3.0 "The Third Span"
#
# Epigraph: "If there is a missing piece to the codex legend its going
# to be the roman numeral double letter system." — the founder,
# 2026-11-24, stating the theory this module builds.
#
# Thelemic date: XXIV day of November, dies Martis, Sol in Sagittario,
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
#   Hypothesis: that inside the double-letter map's twenty-six pairs
#     there sits a smaller, older system — the seven pairs of the
#     Roman numeral letters — governed not by the Latin banks but by
#     the numeral law itself: repetition as arithmetic, licensed to
#     three for the powers, refused for the five-signs, and inverted
#     in the subtractive seats.
#   Method: take the seven attested values as the tradition's givens
#     and compute everything else — doubles, triples, promotions,
#     subtractives — from a stated law function, never from a frozen
#     list; then weigh the seven pairs against the Latin doubles map
#     and print the partings at coordinates.
#   Observation: the two systems share the seven letters and no
#     value at all; the Latin banks agree with each other at II, CC
#     and DD and part from the numerals everywhere; and VV — refused
#     by Rome, promoted to X — is seated by the founder as the Roman
#     face's HYBRID, on his ground that it is both a double consonant
#     and a double vowel in the same glyphs.
#   Result: the map below, DERIVED from the attested numerals — a
#     theorem of the system, not a new table. The founder's hybrid
#     seat at VV is his ruling, recorded as his, tier FOUNDER; it is
#     no part of Roman practice and claims to be none.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Roman numeral double-letter system.

DOCTRINE: the seven values are ATTESTED — the tradition's givens,
stated in every standard reference on Roman numerals (the values
and the standard form are as read in the "Roman numerals" article,
Wikipedia, read 2026-11-24; the sign origins in its Etruscan and
early-Roman sections). Everything else in this module is DERIVED:
computed from the seven by the repetition law stated below, the
doubles.py discipline — computed, never frozen. The one exception
is marked where it stands: the HYBRID seat at VV is the founder's
ruling of 2026-11-24 (tier FOUNDER, his coinage under his
Flagpole), seated in the legend's system against Rome's refusal,
on his stated ground. It changes no numeral value; it names a seat.

THE LAW (Roman practice, standard form): a numeral is written by
concatenating signs of fixed value and summing them. Repetition is
the system's arithmetic. The signs divide by their own values into
the POWERS (1, 10, 100, 1000 — I, X, C, M) and the FIVES (5, 50,
500 — V, L, D, each five times a power). A power may repeat, up to
three in standard form. A five may never repeat: its double is
written as the next power instead — the PROMOTION (VV is not a
numeral; 10 is X). Four of a power is likewise outside the
standard form (the historical additive IIII of clocks and of the
Colosseum gates is a variant the sources record; the standard
form's answer to four is the subtractive seat, IV). Six
SUBTRACTIVE seats invert the order — a power before the five or
the power above it weighs the difference: IV, IX, XL, XC, CD, CM.
The system has no zero sign (the medieval nulla, N, is a word's
initial doing a zero's work, not a numeral sign).
"""

# -- The givens -------------------------------------------------------------
# MECHANISM: the seven attested values are the only literals in this
# module. They are not derived because they are not derivable: they
# are what the tradition hands down, and every other number here is
# computed from them by the law functions below. If a source ever
# corrected a value, the whole map would follow it.
NUMERAL_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

# The seven in the system's own descending order of weight — the
# order a numeral is written in, and the order the subtractive
# generation below walks.
NUMERAL_ORDER = ('M', 'D', 'C', 'L', 'X', 'V', 'I')

# The repetition cap of the standard form.
MAX_REPEAT = 3


def _kind(value):
    """Classify a sign by its value's own arithmetic: 'power' or 'five'.

    MECHANISM: a power of ten (1, 10, 100, 1000) is a power; five
    times a power of ten (5, 50, 500) is a five. The classification
    is computed from the value, not looked up per letter, so the
    law below is a function of the numbers themselves — the same
    division the system itself draws (its signs are the powers of
    ten and their halves-by-five, which is why the fives are the
    ones that may not repeat: two fives make the next power whole).
    """
    v = value
    while v > 1 and v % 10 == 0:
        v //= 10
    if v == 1:
        return 'power'
    if v == 5:
        return 'five'
    raise ValueError('not a Roman sign value: %r' % (value,))


def repeat_status(letter, count):
    """The repetition law: the status of `letter` written `count` times.

    MECHANISM: derived from the letter's kind at every call —
    nothing here is a frozen list of statuses.
      * count 1 is the single itself: 'single'.
      * A POWER at count 2 or 3 (up to MAX_REPEAT): 'lawful' — the
        double and triple are numerals (II, III, XX, XXX, ...).
      * A FIVE at count 2 or 3: 'refused' — the system promotes
        instead (see DOUBLES below for the promotion each refusal
        points to).
      * V at count 2 is the founder's exception, and it is a seat,
        not a value: 'refused_hybrid' — refused as a numeral by
        Rome's law exactly as LL and DD are, and seated as the
        Roman face's HYBRID by the founder's word of 2026-11-24,
        on his ground: "its both a double constanant and a double
        vowel" — V is the one classical letter that carries both
        natures (vocalic U and consonantal V are one letter; the
        Latin doubles map prints UU == VV == 400 on Agrippa's
        bank, U read as V), so its double is a double consonant
        and a double vowel in the same glyphs, a hybrid across the
        consonant/vowel line itself. The seat is the founder's;
        the refusal is Rome's; the map prints both, flattened into
        neither.
      * Any letter at count 4 or more: 'refused' — outside the
        standard form for powers and fives alike.
    """
    if letter not in NUMERAL_VALUES:
        raise ValueError('not a numeral letter: %r' % (letter,))
    if count < 1:
        raise ValueError('a repetition count starts at 1: %r' % (count,))
    if count == 1:
        return 'single'
    if count > MAX_REPEAT:
        return 'refused'
    if _kind(NUMERAL_VALUES[letter]) == 'power':
        return 'lawful'
    if letter == 'V' and count == 2:
        return 'refused_hybrid'
    return 'refused'


def _promotion(letter):
    """The sign a refused double points to: the sign of twice its value.

    MECHANISM: computed by searching the seven for the value 2v.
    For the three fives the search always lands — 2·5 = 10 (X),
    2·50 = 100 (C), 2·500 = 1000 (M) — because the fives are the
    powers' halves, so a doubled five is the next power whole.
    That is the whole mechanics of the refusal: Rome does not
    forbid the value, it forbids the spelling, and writes the
    value with the promoted sign.
    """
    twice = 2 * NUMERAL_VALUES[letter]
    for ch, v in NUMERAL_VALUES.items():
        if v == twice:
            return ch
    return None


def _repeat_map(count):
    """Compute the map of every letter written `count` times.

    MECHANISM: one builder for doubles and triples, so the two
    maps cannot drift apart. Each entry carries its status from
    the law function, its numeral value where the law licenses
    one (None where refused — a refusal is a seat, not a zero),
    its promotion where refused, and its hybrid seat where the
    founder has seated one (VV alone, at count 2).
    """
    out = {}
    for ch in NUMERAL_ORDER:
        status = repeat_status(ch, count)
        entry = {
            'letter': ch,
            'repeat': count,
            'status': status,
            'value': (NUMERAL_VALUES[ch] * count
                      if status == 'lawful' else None),
            'promotion': (_promotion(ch)
                          if status in ('refused', 'refused_hybrid')
                          and count == 2 else None),
            'hybrid_seat': status == 'refused_hybrid',
        }
        if entry['promotion'] is not None:
            entry['promotion_value'] = NUMERAL_VALUES[entry['promotion']]
        out[ch * count] = entry
    return out


# -- The map, computed — never frozen ---------------------------------------
# MECHANISM: derived from the seven givens at import by the law
# functions above, on the doubles.py discipline. numerals_checks()
# pins the derivation by restating the law independently, so any
# divergence between the law and the map fails loudly.
DOUBLES = _repeat_map(2)
TRIPLES = _repeat_map(3)

# -- The subtractive seats, computed -----------------------------------------
# MECHANISM: generated by the standard rule, not listed. Walk the
# powers I, X, C in ascending order; each takes the two signs above
# it — its own five and the next power — subtractively: I before V
# and X; X before L and C; C before D and M. Six seats, each
# weighing greater − lesser. M has no sign above it in the seven,
# so the generation stops at C — the system's negative face is
# exactly as large as its ladder allows, and no larger.
def _build_subtractives():
    ascending = tuple(reversed(NUMERAL_ORDER))  # I, V, X, L, C, D, M
    out = {}
    for i, ch in enumerate(ascending):
        if _kind(NUMERAL_VALUES[ch]) != 'power' or ch == 'M':
            continue
        for greater in (ascending[i + 1], ascending[i + 2]):
            out[ch + greater] = NUMERAL_VALUES[greater] - NUMERAL_VALUES[ch]
    return out


SUBTRACTIVES = _build_subtractives()


def pair(pair_word):
    """One double's seat on the numeral map (see DOUBLES).

    MECHANISM: a plain lookup; the pair is upper-cased first, as
    the Latin doors fold their input the same way.
    """
    return DOUBLES[pair_word.upper()]


def parse(numeral):
    """Evaluate a standard-form numeral string by the system's own law.

    MECHANISM: the additive principle with the subtractive seats —
    scan the signs; a sign worth less than the sign after it is
    subtracted, every other sign is added. This is the reading the
    tradition itself states ("a number is written by concatenating
    individual symbols... when a smaller numeral symbol precedes a
    larger one, subtraction is implied"). It exists so the checks
    can weigh whole numerals — LXXVII, XCIII — against the map's
    seats instead of trusting them.
    """
    s = numeral.upper()
    if not s or any(ch not in NUMERAL_VALUES for ch in s):
        raise ValueError('not a numeral: %r' % (numeral,))
    total = 0
    for i, ch in enumerate(s):
        v = NUMERAL_VALUES[ch]
        if i + 1 < len(s) and NUMERAL_VALUES[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total


def numerals_checks():
    """Self-checks for the Roman numeral double-letter system.

    Returns [(name, passed, got)].

    MECHANISM: kept beside doubles_checks() rather than inside
    engine_checks(), on the greek_checks()/doubles_checks()
    precedent — the established self-test stands untouched as the
    no-collateral witness; run all for the full suite. The Latin
    doubles map is imported here, inside the function, so the
    modules stay one-directional (numerals → the seven givens at
    import; the Latin map is consulted only when the checks run).
    The law is restated independently inside the checks (the
    classification arithmetic written out again), so the battery
    holds the map to the LAW, not to the builder's copy of it.
    """
    from .doubles import DOUBLES as LATIN_PAIRS
    checks = []

    # 1. THE GIVENS: exactly the seven attested letters at the
    #    attested values — no eighth sign, and no zero among them
    #    (the system has no zero sign; the medieval N of nulla is
    #    not a numeral letter and is not seated here).
    checks.append(('the seven givens: I 1, V 5, X 10, L 50, C 100, '
                   'D 500, M 1000 — and no zero sign among them',
                   NUMERAL_VALUES == {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                                      'C': 100, 'D': 500, 'M': 1000}
                   and 0 not in NUMERAL_VALUES.values()
                   and 'N' not in NUMERAL_VALUES,
                   NUMERAL_VALUES))

    # 2. THE LAW, RESTATED: classify every letter by its value's
    #    arithmetic, written out again here — a power is 10^k, a
    #    five is 5·10^k — and recompute every double's status from
    #    the classification. The refused set must fall out of the
    #    arithmetic as exactly {VV, LL, DD}, the lawful doubles as
    #    exactly {II, XX, CC, MM}, and the hybrid seat as VV alone.
    def kind_of(v):
        while v > 1 and v % 10 == 0:
            v //= 10
        return 'power' if v == 1 else 'five'
    lawful, refused, hybrid = set(), set(), set()
    for ch, v in NUMERAL_VALUES.items():
        st = DOUBLES[ch * 2]['status']
        want = ('lawful' if kind_of(v) == 'power'
                else 'refused_hybrid' if ch == 'V' else 'refused')
        (lawful if st == 'lawful' else
         hybrid if st == 'refused_hybrid' else refused).add(ch * 2)
        if st != want:
            lawful.add('MISMATCH:' + ch * 2)
    checks.append(('the law derived, not frozen: statuses recomputed '
                   'from the values give lawful {II, XX, CC, MM}, '
                   'refused {LL, DD}, refused-hybrid {VV}',
                   lawful == {'II', 'XX', 'CC', 'MM'}
                   and refused == {'LL', 'DD'} and hybrid == {'VV'},
                   (sorted(lawful), sorted(refused), sorted(hybrid))))

    # 3. THE LAWFUL DOUBLES weigh twice their sign — repetition is
    #    the arithmetic: II 2, XX 20, CC 200, MM 2000.
    got = {p: DOUBLES[p]['value'] for p in ('II', 'XX', 'CC', 'MM')}
    checks.append(('lawful doubles weigh 2×: II 2, XX 20, CC 200, MM 2000',
                   got == {'II': 2, 'XX': 20, 'CC': 200, 'MM': 2000}, got))

    # 4. THE PROMOTIONS: each refused double carries no numeral
    #    value and points at the sign of exactly twice its letter's
    #    value — VV → X (10), LL → C (100), DD → M (1000) — the
    #    promotion found by search, and the promoted sign worth
    #    exactly the doubled value the spelling was refused for.
    prom = {p: (DOUBLES[p]['value'], DOUBLES[p]['promotion'],
                DOUBLES[p]['promotion_value'])
            for p in ('VV', 'LL', 'DD')}
    checks.append(('promotions exact: VV→X 10, LL→C 100, DD→M 1000, '
                   'each refused double valueless as spelled',
                   prom == {'VV': (None, 'X', 10), 'LL': (None, 'C', 100),
                            'DD': (None, 'M', 1000)}, prom))

    # 5. THE CAP AND THE TRIPLES: repetition is licensed to three
    #    for the powers and not at all for the fives, and four is
    #    refused for every letter in the standard form.
    trip = {p: TRIPLES[p]['value'] for p in ('III', 'XXX', 'CCC', 'MMM')}
    checks.append(('triples lawful for the powers (III 3, XXX 30, '
                   'CCC 300, MMM 3000), refused for the fives, and '
                   'four of anything refused',
                   trip == {'III': 3, 'XXX': 30, 'CCC': 300, 'MMM': 3000}
                   and all(TRIPLES[p]['status'] == 'refused'
                           for p in ('VVV', 'LLL', 'DDD'))
                   and all(repeat_status(ch, 4) == 'refused'
                           for ch in NUMERAL_VALUES),
                   trip))

    # 6. THE SUBTRACTIVE SEATS: exactly six, generated by the
    #    rule, each weighing greater − lesser: IV 4, IX 9, XL 40,
    #    XC 90, CD 400, CM 900.
    checks.append(('subtractives: exactly six, each greater − lesser '
                   '(IV 4, IX 9, XL 40, XC 90, CD 400, CM 900)',
                   SUBTRACTIVES == {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                                    'CD': 400, 'CM': 900}
                   and all(SUBTRACTIVES[a + b] ==
                           NUMERAL_VALUES[b] - NUMERAL_VALUES[a]
                           for a, b in SUBTRACTIVES),
                   SUBTRACTIVES))

    # 7. VV — THE HINGE: refused as a numeral, promoted to X, and
    #    seated as the hybrid — the only hybrid seat on the map.
    #    Against the Latin doubles map the same glyphs weigh 44 in
    #    the ordinal bank and 400 in Agrippa, where UU == VV (U
    #    read as V) — the founder's stated ground (a double
    #    consonant and a double vowel in the same glyphs) printed
    #    as a coordinate of the existing map. LL and DD carry no
    #    hybrid seat: their candidacy stands open for his pen,
    #    and the map does not extend his ruling for him.
    vv = DOUBLES['VV']
    checks.append(('VV the hinge: refused-hybrid, promotion X, the '
                   'map’s only hybrid seat; Latin banks 44 / 400 with '
                   'UU == VV in Agrippa; LL and DD unseated as hybrids',
                   vv['status'] == 'refused_hybrid' and vv['hybrid_seat']
                   and vv['promotion'] == 'X' and vv['value'] is None
                   and LATIN_PAIRS['VV'] == {'ordinal': 44, 'agrippa': 400}
                   and LATIN_PAIRS['UU']['agrippa']
                   == LATIN_PAIRS['VV']['agrippa'] == 400
                   and not DOUBLES['LL']['hybrid_seat']
                   and not DOUBLES['DD']['hybrid_seat'],
                   (vv, LATIN_PAIRS['VV'])))

    # 8. THE JOINS PAGE: the seven numeral pairs inside the
    #    twenty-six, cross-weighed against the Latin doubles map's
    #    own output. The two Latin banks agree at II (18/18), CC
    #    (6/6) and DD (8/8); the numeral doubles (where lawful)
    #    agree with neither bank anywhere — the systems share the
    #    letters and no value.
    joins = {p: (DOUBLES[p]['value'], LATIN_PAIRS[p]['ordinal'],
                 LATIN_PAIRS[p]['agrippa'])
             for p in ('II', 'VV', 'XX', 'LL', 'CC', 'DD', 'MM')}
    pinned = {'II': (2, 18, 18), 'VV': (None, 44, 400),
              'XX': (20, 48, 600), 'LL': (None, 24, 40),
              'CC': (200, 6, 6), 'DD': (None, 8, 8),
              'MM': (2000, 26, 60)}
    checks.append(('the seven pairs cross-weighed: numeral | ordinal | '
                   'Agrippa, the Latin banks agreeing at II, CC, DD '
                   'and the numeral agreeing with neither anywhere',
                   joins == pinned
                   and all(n is None or (n != o and n != a)
                           for n, o, a in joins.values()),
                   joins))

    # 9. THE EVALUATOR EXHIBITS: whole numerals weighed by the
    #    system's own reading — LXXVII = 77, the house's number,
    #    itself built of two lawful doubles (XX and II) around V;
    #    XCIII = 93, a subtractive seat carrying a lawful triple;
    #    MDCCLXXVI = 1776 (the date on the Statue of Liberty's
    #    book, as the source article records); MMXXVI = 2026.
    ex = (parse('LXXVII'), parse('XCIII'), parse('MDCCLXXVI'),
          parse('MMXXVI'))
    checks.append(('evaluator exhibits: LXXVII 77, XCIII 93, '
                   'MDCCLXXVI 1776, MMXXVI 2026',
                   ex == (77, 93, 1776, 2026), ex))
    return checks


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
