#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — maya_audit.py — the Maya notation audit builder, Leg B of
# the Western Sweep (the founder's commission of 2026-11-24, 11:51
# EST: both legs in Synergy not Argumentation).
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
#   Hypothesis (the commission's, to be tested not assumed): the
#     Maya numerals are a NOTATION species — bar-and-dot signs
#     (dot 1, bar 5, shell zero) under a positional vigesimal
#     reading, with head-variant glyphs as a second dress of the
#     same digits, and a calendrical modification of the law at
#     the third position (x18, the 360-day tun).
#   Method: two independent witnesses read entire (W1 Wikipedia
#     'Maya numerals'; W2 the MacTutor History of Mathematics
#     archive's 'Mayan mathematics', University of St Andrews),
#     transcribed independently below; a third witness for the
#     head-variant dress (planetarchaeology's 'Maya Number
#     System'). The sign inventory is verified against the
#     Unicode standard in code (U+1D2E0–U+1D2F3, the Mayan
#     Numerals block, twenty digit signs in order). Every exhibit
#     the witnesses print is recomputed from the transcribed laws
#     in code — the builder asserts each recomputation and ABORTS
#     on a parting; partings of framing are recorded as partings,
#     never averaged.
#   Observation: the inventory and both laws agree entire; the
#     witnesses' worked exhibits recompute exact (33, 429, 409,
#     5125; the Long Count of La Mojarra Stela 1, 1,193,947;
#     MacTutor's two day-counts, 1,253,912 and 1,357,100); the
#     x18 coordinate is exact — under pure vigesimal law [1,0,0]
#     reads 400, under the calendrical law it reads 360, and
#     MacTutor's own non-property (20 x 67,873 != 1,357,100)
#     exhibits the parting in arithmetic. The witnesses part in
#     FRAMING only: W1 seats the pure vigesimal system as the
#     presumed general system with the modified as its calendar
#     variation; W2 treats the modified as THE attested written
#     system. The arithmetic does not part anywhere.
#   Result: maya-numerals.csv frozen here; the reader seated at
#     pontifex/maya.py under both laws, fenced by mode; NO
#     weigh() system registered — the species is a notation,
#     proven in the parity battery.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Freeze the Maya numeral inventory and reading laws (Leg B).

MECHANISM: DIGITS is the bar-and-dot decomposition of the twenty
digits, derived from the two witnesses' stated law (each digit is
0–4 dots and 0–3 bars; digit = 5*bars + dots) and verified
against the Unicode standard's block: the glyph at U+1D2E0+n must
be named for digit n. EXHIBITS carries the witnesses' own worked
examples with their sources; main() recomputes every one under
the stated law and asserts equality, then writes the CSV.
"""

import csv
import os
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# --- The sign inventory (W1 and W2, agreeing) -------------------------------
# W1: "Maya numerals are a base-20 (vigesimal) system" built from
# three symbols: zero (a shell), one (a dot), five (a bar); "Each
# of the twenty vigesimal digits" is written from them. W2: "The
# Mayan system used three symbols" — a dot for one, a line/bar
# for five, a shell for zero — and a positional writing. The
# decomposition is the law's own: digit = 5 bars' worth + dots.
DIGITS = []  # (digit, bars, dots)
for d in range(20):
    DIGITS.append((d, d // 5, d % 5))


def vigesimal(digits):
    """Pure positional law: places 20^k, highest position first."""
    return sum(d * 20 ** i for i, d in enumerate(reversed(digits)))


def long_count(digits):
    """The calendrical law: places 1, 20, 360, 7200, 144000, ...

    MECHANISM: the second place (winal) runs in twenties; the
    third place (tun) is 18 x 20 = 360, not 20 x 20 = 400; every
    place above the tun multiplies by 20 again. The second digit
    from the bottom is therefore bounded at 17 — 18 winals close
    the tun — and the law refuses a larger winal digit."""
    if len(digits) >= 2 and digits[-2] > 17:
        raise ValueError('winal digit above 17: %r' % (digits,))
    places = [1, 20]
    for _ in range(2, len(digits)):
        places.append(places[-1] * (18 if len(places) == 2 else 20))
    return sum(d * p for d, p in zip(reversed(digits), places))


# --- The witnesses' exhibits, recomputed -------------------------------------
# (digits top-first, expected value, law, source as printed)
EXHIBITS = [
    ([1, 13], 33, 'vigesimal',
     'W1: "33 = (1 x 20) + 13"'),
    ([1, 1, 9], 429, 'vigesimal',
     'W1: "429 = (1 x 20^2) + (1 x 20^1) + 9"'),
    ([0, 1, 13], 33, 'vigesimal',
     'W1 header table: the column of 0, 1, 13 totals 33'),
    ([1, 0, 9], 409, 'vigesimal',
     'W1 header table: the column of 1, 0, 9 totals 409'),
    ([12, 16, 5], 5125, 'vigesimal',
     'W1 header table: the column of 12, 16, 5 totals 5125 — the '
     'printed total pins the middle digit at 16'),
    ([1, 0, 0], 360, 'long_count',
     'W1: "one dot over two zeros signifies 360" — the x18 '
     'coordinate itself'),
    ([1, 0, 0], 400, 'vigesimal',
     'the same column under the pure law: 400 — the parting '
     'exhibited, not smoothed'),
    ([8, 5, 16, 9, 7], 1193947, 'long_count',
     'W1: La Mojarra Stela 1, Long Count 8.5.16.9.7 (= 156 CE by '
     'the correlation W1 prints)'),
    ([8, 14, 3, 1, 12], 1253912, 'long_count',
     'W2: "[8;14;3;1;12] counts 1,253,912 days" (Tikal)'),
    ([9, 8, 9, 13, 0], 1357100, 'long_count',
     'W2: "[9;8;9;13;0] = 1,357,100 days" (Palenque)'),
    ([9, 8, 9, 13], 67873, 'long_count',
     "W2's own intermediate: [9;8;9;13] = 67,873"),
]

LAWS = {'vigesimal': vigesimal, 'long_count': long_count}


def main():
    # 1. The inventory against the standard, in code.
    for d, bars, dots in DIGITS:
        glyph = chr(0x1D2E0 + d)
        name = ud.name(glyph)
        expect = 'MAYAN NUMERAL %s' % (
            'ZERO' if d == 0 else
            {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',
             6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN',
             11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN',
             14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN',
             17: 'SEVENTEEN', 18: 'EIGHTEEN',
             19: 'NINETEEN'}[d])
        assert name == expect, (d, name, expect)
        assert 5 * bars + dots == d
    print('the standard: 20/20 digit signs in order, '
          'U+1D2E0–U+1D2F3; the law digit = 5*bars + dots holds '
          '20/20')

    # 2. Every exhibit recomputed under its law.
    for digits, expected, law, _src in EXHIBITS:
        got = LAWS[law](digits)
        assert got == expected, (digits, law, got, expected)
    # W2's non-property, the parting in arithmetic: extending the
    # Palenque column by one zero does NOT multiply by 20.
    assert 20 * long_count([9, 8, 9, 13]) != long_count([9, 8, 9, 13, 0])
    print('the exhibits: %d/%d recompute exact under their laws; '
          'the shift non-property holds (20 x 67,873 = 1,357,460 '
          '!= 1,357,100 — the parting is exactly 360)'
          % (len(EXHIBITS), len(EXHIBITS)))

    # 3. Freeze the inventory.
    with open(os.path.join(HERE, 'maya-numerals.csv'), 'w',
              newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['digit', 'bars', 'dots', 'glyph', 'codepoint',
                    'unicode_name', 'standing'])
        for d, bars, dots in DIGITS:
            glyph = chr(0x1D2E0 + d)
            w.writerow([d, bars, dots, glyph,
                        'U+%05X' % (0x1D2E0 + d), ud.name(glyph),
                        'SOURCED — a digit sign of a NOTATION; '
                        'the shell at 0 is a zero GLYPH in a '
                        'positional law, not a letter value'])
    print('CSV frozen: maya-numerals (20 digits)')


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
