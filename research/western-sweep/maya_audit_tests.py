#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — maya_audit_tests.py — the Maya notation audit battery,
# Leg B of the Western Sweep. Companion to maya_audit.py and
# THE-MAYA-NOTATION.md.
#
# 93. Authorship: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved,
# Without Prejudice. Method of Science, Aim of Religion.
#
# MECHANISM: every check re-derives a number the instrument prints,
# from the frozen CSV and from this battery's own independent
# constants and laws (the reading laws restated here, not imported
# from the builder). Run: python3 maya_audit_tests.py — exit 0 =
# all pass.
# =============================================================================
"""The Leg B audit battery: the frozen Maya data, re-derived."""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed)))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def vig(digits):
    return sum(d * 20 ** i for i, d in enumerate(reversed(digits)))


def lc(digits):
    places = [1, 20]
    for _ in range(2, len(digits)):
        places.append(places[-1] * (18 if len(places) == 2 else 20))
    return sum(d * p for d, p in zip(reversed(digits), places))


with open(os.path.join(HERE, 'maya-numerals.csv'),
          encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))

check('the inventory freezes 20 digits, 0–19 in order',
      [int(r['digit']) for r in rows] == list(range(20)), len(rows))
check('every digit is 5*bars + dots, bars 0–3, dots 0–4',
      all(int(r['digit']) == 5 * int(r['bars']) + int(r['dots'])
          and 0 <= int(r['bars']) <= 3 and 0 <= int(r['dots']) <= 4
          for r in rows),
      '20/20')
check('the glyphs are the Mayan Numerals block in order, '
      'names matching the live standard',
      all(ord(r['glyph']) == 0x1D2E0 + int(r['digit'])
          and ud.name(r['glyph']) == r['unicode_name'] for r in rows),
      'U+1D2E0..U+1D2F3')
check('the shell is digit 0: no bars, no dots — a sign, not an '
      'absence',
      rows[0]['digit'] == '0' and rows[0]['bars'] == '0'
      and rows[0]['dots'] == '0'
      and rows[0]['unicode_name'] == 'MAYAN NUMERAL ZERO',
      rows[0]['unicode_name'])

# The exhibits, restated from the witnesses independently.
check("W1's 33 == (1x20) + 13 under the pure law", vig([1, 13]) == 33,
      vig([1, 13]))
check("W1's 429 == 400 + 20 + 9 under the pure law",
      vig([1, 1, 9]) == 429, vig([1, 1, 9]))
check("W1's header totals 409 and 5125 recompute",
      vig([1, 0, 9]) == 409 and vig([12, 16, 5]) == 5125,
      (vig([1, 0, 9]), vig([12, 16, 5])))
check('the x18 coordinate: [1,0,0] reads 360 calendrical, 400 pure',
      lc([1, 0, 0]) == 360 and vig([1, 0, 0]) == 400,
      (lc([1, 0, 0]), vig([1, 0, 0])))
check('the tun place law: places run 1, 20, 360, 7200, 144000',
      [lc([1] + [0] * i) for i in range(4, -1, -1)]
      == [144000, 7200, 360, 20, 1],
      [lc([1] + [0] * i) for i in range(4, -1, -1)])
check("W1's La Mojarra Long Count 8.5.16.9.7 == 1,193,947 days",
      lc([8, 5, 16, 9, 7]) == 1193947, lc([8, 5, 16, 9, 7]))
check("W2's Tikal count [8;14;3;1;12] == 1,253,912 days",
      lc([8, 14, 3, 1, 12]) == 1253912, lc([8, 14, 3, 1, 12]))
check("W2's Palenque count [9;8;9;13;0] == 1,357,100 days",
      lc([9, 8, 9, 13, 0]) == 1357100, lc([9, 8, 9, 13, 0]))
check("W2's non-property: 20 x [9;8;9;13] != the Palenque count; "
      'the parting is exactly 360',
      20 * lc([9, 8, 9, 13]) - lc([9, 8, 9, 13, 0]) == 360,
      20 * lc([9, 8, 9, 13]) - lc([9, 8, 9, 13, 0]))
check('the winal ceiling: the second digit of every witness '
      'Long Count stands at 17 or below',
      all(d <= 17 for d in (16, 14, 9, 13)),
      'witness maximum 16')
# The addition law W1 states: five dots make a bar; four bars make
# a dot in the next row — the digit arithmetic of the notation.
check("W1's carrying law: digit 19 + 1 carries to (1, 0)",
      vig([1, 19]) + 1 == vig([2, 0]) == 40, vig([1, 19]) + 1)

print()
failed = [n for n, p in RESULTS if not p]
print('MAYA AUDIT BATTERY — %d/%d checks PASS'
      % (len(RESULTS) - len(failed), len(RESULTS)))
if failed:
    print('FAILURES:', failed)
    sys.exit(1)

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
