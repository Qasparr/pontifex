#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — maya.py — THE MAYA NOTATION SEAT: a reader for the
# bar-and-dot positional notation. NOT a weighing bank — the
# notation prices no letters; it reads columns of digit signs
# (THE-MAYA-NOTATION.md).
#
# Epigraph: "In the second position, only the digits up to 17 are
# used, and the place value of the third position is not
# 20 x 20 = 400, as might be expected, but 18 x 20 = 360 so that
# one dot over two zeros signifies 360." — Wikipedia, "Maya
# numerals" (read entire, 2026-11-24).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's,
# open to the author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis (the field audit's gate, THE-MAYA-NOTATION.md §IX):
#     the Maya numerals are a NOTATION — three signs (dot 1, bar 5,
#     shell zero) composing twenty digits, read positionally —
#     which two witnesses state identically, whose exhibits
#     recompute exact, and which therefore takes a reader's seat
#     on the Chinese precedent. It must never register as a
#     weigh() system: the notation has no letters to price.
#   Method: the inventory and both reading laws are the audit's,
#     transcribed from two witnesses (Wikipedia, 'Maya numerals';
#     MacTutor, 'Mayan mathematics') and frozen in
#     research/western-sweep/maya-numerals.csv; the laws are
#     verified against the witnesses' exhibits in maya_checks()
#     below, and parity against the frozen CSV is proven by
#     test_maya_parity.py at the repository root.
#   Observation: recorded in the audit document.
#   Result: a reader under both laws, fenced by mode.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Read Maya numerals under the pure and the calendrical laws.

DOCTRINE — THE SPECIES: the Maya numeral system is a NOTATION,
not a letter table. Its signs are three — a dot (1), a bar (5),
and the shell (0) — composed into twenty digit signs, and its
numbers are COLUMNS of digits read positionally, highest place
first as the column is written. This module reads such a column
and returns the number with every position audited. It registers
no weigh() system: there are no letters here, and nothing to
weigh.

THE TWO LAWS, AND THE COORDINATE WHERE THEY PART: under the PURE
vigesimal law the places run 20^k — 1, 20, 400, 8000, … Under the
CALENDRICAL law — the Long Count, the system of every dated
monument the witnesses exhibit — the third place is not
20 x 20 = 400 but 18 x 20 = 360, the tun of roughly a year,
because the second place (the winal, the 20-day month) runs only
to 17: eighteen winals close the tun. Above the tun the places
multiply by 20 again: 1, 20, 360, 7200, 144000, … The parting is
exact and it is exhibited, not smoothed: the column [1, 0, 0]
reads 360 under the calendrical law and 400 under the pure law,
and MacTutor's own arithmetic shows the seam — [9;8;9;13] reads
67,873, and twenty times that is 1,357,460, NOT the 1,357,100 of
the full count [9;8;9;13;0]; the difference is exactly 360, the
tun itself. WHICH law the witnesses seat where is printed in the
audit: the written, dated record is the calendrical system; the
pure system stands as the presumed general arithmetic (W1) — "it
is reasonable to assume, but not proven by any evidence" — and
Ifrah's pure merchants' system, which W2 reports, has left no
trace at all. The reader therefore takes the law as an explicit
mode and defaults to the pure law of the notation's own shape;
it never blends the two.

THE INPUT CONVENTION (stated on the seat): a column is given
either as a string of the Unicode Mayan numeral signs
U+1D2E0–U+1D2F3 (the block the standard assigns to exactly these
twenty digits, verified against the standard in the audit), or
as a sequence of integers 0–19 — in both cases highest position
first, as the column is written on the stone. Anything else —
a digit above 19, a foreign character, an empty column, a winal
digit above 17 in Long Count mode — is refused with an error:
a reader that guesses is a forger.

THE SECOND DRESS: the same twenty digits were also written as
HEAD-VARIANT glyphs — portrait heads of the deities of the
numbers, the digits 13–19 wearing the jaw-attribute of 10, as
the Yucatec number words compose them. The dress is verified
across the witnesses (W1; the head-variant witness of the audit)
but it is NOT parsed here: the head variants have no per-glyph
standard encoding the audit could freeze, and a reader seats
only what it can verify sign by sign. The dress stands recorded
in the instrument; the door reads the bar-and-dot dress and the
standard's digit signs.
"""

_MODES = ('vigesimal', 'long_count')


def _places(count, mode):
    """The place values, lowest first, for a column of `count`.

    MECHANISM: pure law — 20^k. Calendrical law — 1, 20, then
    18 x 20 = 360 at the third place, then x20 upward: the x18
    binds exactly once, between the second and third places,
    because the winal is the calendar's twenty-day month and
    eighteen of them close the tun."""
    places = []
    for k in range(count):
        if mode == 'vigesimal':
            places.append(20 ** k)
        elif k == 0:
            places.append(1)
        elif k == 1:
            places.append(20)
        elif k == 2:
            places.append(360)
        else:
            places.append(places[-1] * 20)
    return places


def _digits_of(text):
    """Normalize the input convention to a list of digit ints.

    MECHANISM: a string must consist wholly of the Mayan numeral
    signs U+1D2E0–U+1D2F3, each read as its block offset; a
    sequence must consist of ints in 0–19. Anything else raises
    ValueError — the reader refuses what it cannot read."""
    if isinstance(text, str):
        if not text:
            raise ValueError('empty Maya column')
        digits = []
        for ch in text:
            code = ord(ch)
            if not 0x1D2E0 <= code <= 0x1D2F3:
                raise ValueError('not a Maya numeral sign: %r' % ch)
            digits.append(code - 0x1D2E0)
        return digits
    try:
        digits = list(text)
    except TypeError:
        raise ValueError('not a Maya column: %r' % (text,))
    if not digits:
        raise ValueError('empty Maya column')
    for d in digits:
        if not isinstance(d, int) or isinstance(d, bool) \
                or not 0 <= d <= 19:
            raise ValueError('not a Maya digit: %r' % (d,))
    return digits


def read_maya_numerals(text, mode='vigesimal'):
    """Read a Maya numeral column under the stated law.

    MECHANISM: normalize the column (highest position first),
    take the mode's place values, and in Long Count mode enforce
    the winal ceiling — the second digit from the bottom at most
    17, since eighteen winals close the tun. Returns a result
    dict: the input as given, the digits, the number, the
    per-position breakdown (digit, place value, product — highest
    first), and the mode.
    """
    if mode not in _MODES:
        raise ValueError('unknown Maya reading mode: %r' % (mode,))
    digits = _digits_of(text)
    if mode == 'long_count' and len(digits) >= 2 and digits[-2] > 17:
        raise ValueError('winal digit above 17 in Long Count mode: '
                         '%r' % (digits,))
    places = _places(len(digits), mode)
    breakdown = [(d, p, d * p)
                 for d, p in zip(digits, reversed(places))]
    return {
        'text': text,
        'digits': digits,
        'value': sum(product for _d, _p, product in breakdown),
        'breakdown': breakdown,
        'mode': mode,
        'notation': 'maya',
    }


def maya_checks():
    """Verify the notation seat against the witnesses' exhibits.

    MECHANISM: the inventory's law recomputed at its coordinates
    (digit = 5 bars + dots across the standard's block), the
    witnesses' worked examples under both laws, the x18 parting
    exhibited at its exact coordinate, MacTutor's non-property
    (the seam in arithmetic), the winal ceiling enforced, and the
    refusals. Parity against the frozen CSV is proven separately
    by test_maya_parity.py.
    """
    checks = []
    block = all(
        read_maya_numerals([d])['value'] == d for d in range(20))
    checks.append(('the twenty digit signs read themselves: every '
                   'digit 0–19 at a single position', block,
                   '20/20'))
    checks.append(("W1's exhibits under the pure law: 33 and 429",
                   read_maya_numerals([1, 13])['value'] == 33
                   and read_maya_numerals([1, 1, 9])['value'] == 429,
                   (read_maya_numerals([1, 13])['value'],
                    read_maya_numerals([1, 1, 9])['value'])))
    checks.append(('the x18 coordinate: [1,0,0] reads 360 under '
                   'the calendrical law, 400 under the pure law — '
                   'the parting exhibited, not smoothed',
                   read_maya_numerals([1, 0, 0],
                                      'long_count')['value'] == 360
                   and read_maya_numerals([1, 0, 0])['value'] == 400,
                   (read_maya_numerals([1, 0, 0],
                                       'long_count')['value'],
                    read_maya_numerals([1, 0, 0])['value'])))
    checks.append(("W1's La Mojarra Long Count 8.5.16.9.7 reads "
                   '1,193,947 under the calendrical law',
                   read_maya_numerals([8, 5, 16, 9, 7],
                                      'long_count')['value']
                   == 1193947,
                   read_maya_numerals([8, 5, 16, 9, 7],
                                      'long_count')['value']))
    checks.append(("W2's two day-counts read exact: 1,253,912 and "
                   '1,357,100',
                   read_maya_numerals([8, 14, 3, 1, 12],
                                      'long_count')['value']
                   == 1253912
                   and read_maya_numerals([9, 8, 9, 13, 0],
                                          'long_count')['value']
                   == 1357100,
                   (read_maya_numerals([8, 14, 3, 1, 12],
                                       'long_count')['value'],
                    read_maya_numerals([9, 8, 9, 13, 0],
                                       'long_count')['value'])))
    seam = 20 * read_maya_numerals([9, 8, 9, 13],
                                   'long_count')['value'] \
        - read_maya_numerals([9, 8, 9, 13, 0],
                             'long_count')['value']
    checks.append(("W2's non-property: extending a Long Count by "
                   'one zero does NOT multiply by 20 — the seam '
                   'is exactly 360, the tun', seam == 360, seam))
    signs = ''.join(chr(0x1D2E0 + d) for d in (12, 16, 5))
    glyphs = read_maya_numerals(signs)
    checks.append(("the standard's digit signs parse as a column: "
                   'the signs for 12, 16, 5 read [12,16,5] == 5125, '
                   "W1's header total",
                   glyphs['digits'] == [12, 16, 5]
                   and glyphs['value'] == 5125,
                   (glyphs['digits'], glyphs['value'])))
    refused = []
    for bad, mode in (([1, 18, 0], 'long_count'), ([20], 'vigesimal'),
                      ('abc', 'vigesimal'), ([], 'vigesimal'),
                      ([1, 2], 'sideways')):
        try:
            read_maya_numerals(bad, mode)
        except ValueError:
            refused.append((bad, mode))
    checks.append(('the refusals: a winal above 17, a digit above '
                   '19, foreign glyphs, the empty column, an '
                   'unknown mode — all raise ValueError',
                   len(refused) == 5, refused))
    return checks

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
