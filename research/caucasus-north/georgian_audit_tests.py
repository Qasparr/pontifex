#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — georgian_audit_tests.py — the Georgian Phase I audit battery
# Companion to georgian_audit.py and THE-GEORGIAN-FIELD-PHASE-I-AUDIT.md.
#
# 93. Authorship: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved,
# Without Prejudice. Method of Science, Aim of Religion.
#
# MECHANISM: every check re-derives a number the audit document prints,
# from the frozen CSVs and from this battery's own independent source
# constants (the witnesses' tables restated here, not imported from the
# builder — a battery that imports its builder's constants proves
# nothing). Run: python3 georgian_audit_tests.py — exit 0 = all pass.
# =============================================================================
"""The Phase I audit battery: the frozen Georgian data, re-derived."""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from pontifex.tables import ARMENIAN

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed)))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# The witnesses' table restated independently (Wikipedia, "Georgian
# numerals", read entire 2026-11-24; georgianalphabet.com concurring on
# every cell — the builder holds the diff; this battery holds the data).
EXPECTED = {
    'ა': 1, 'ბ': 2, 'გ': 3, 'დ': 4, 'ე': 5, 'ვ': 6, 'ზ': 7, 'ჱ': 8,
    'თ': 9, 'ი': 10, 'კ': 20, 'ლ': 30, 'მ': 40, 'ნ': 50, 'ჲ': 60,
    'ო': 70, 'პ': 80, 'ჟ': 90, 'რ': 100, 'ს': 200, 'ტ': 300, 'ჳ': 400,
    'უ': 400, 'ფ': 500, 'ქ': 600, 'ღ': 700, 'ყ': 800, 'შ': 900,
    'ჩ': 1000, 'ც': 2000, 'ძ': 3000, 'წ': 4000, 'ჭ': 5000, 'ხ': 6000,
    'ჴ': 7000, 'ჯ': 8000, 'ჰ': 9000, 'ჵ': 10000,
}

with open(os.path.join(HERE, 'georgian-table.csv'), encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(os.path.join(HERE, 'georgian-control-case.csv'),
          encoding='utf-8') as fh:
    cc = list(csv.DictReader(fh))

table = {r['letter']: int(r['value']) for r in rows}
check('the frozen table stands: 38 SOURCED rows, letter for letter '
      'and value for value against the witnesses as restated',
      len(rows) == 38 and table == EXPECTED
      and all(r['status'] == 'SOURCED' for r in rows),
      (len(rows), table == EXPECTED))
check('every glyph is the standard\'s own: the CSV\'s Unicode names '
      '== unicodedata, and the codepoints match',
      all(ud.name(r['letter']) == r['unicode_name']
          and 'U+%04X' % ord(r['letter']) == r['codepoint'] for r in rows),
      '38/38 verified')
check('the dress coordinate in the data: every seat carries an '
      'Asomtavruli capital and a Nuskhuri small partner, matched by '
      'the standard\'s names',
      all(r['asomtavruli'] and r['nuskhuri']
          and ud.name(r['asomtavruli'])
          == 'GEORGIAN CAPITAL LETTER '
          + r['unicode_name'][len('GEORGIAN LETTER '):]
          and ud.name(r['nuskhuri'])
          == 'GEORGIAN SMALL LETTER '
          + r['unicode_name'][len('GEORGIAN LETTER '):] for r in rows),
      '38/38 dressed')
check('the standing coordinate: exactly five obsolete letters '
      '(ჱ ჲ ჳ ჴ ჵ), the classical letters dropped in the 1860s',
      sorted(r['letter'] for r in rows if r['standing'] == 'obsolete')
      == sorted(['ჱ', 'ჲ', 'ჳ', 'ჴ', 'ჵ']),
      [r['letter'] for r in rows if r['standing'] == 'obsolete'])

def weigh(word):
    return sum(table[ch] for ch in word)

check('the witnesses\' worked examples recompute from the frozen '
      'data: ჩღჲთ 1769, ჩყპზ 1887, ციბ 2012, ჩყმვ 1846, ცკვ 2026',
      (weigh('ჩღჲთ'), weigh('ჩყპზ'), weigh('ციბ'), weigh('ჩყმვ'),
       weigh('ცკვ')) == (1769, 1887, 2012, 1846, 2026),
      (weigh('ჩღჲთ'), weigh('ჩყპზ'), weigh('ციბ'), weigh('ჩყმვ'),
       weigh('ცკვ')))
check('the class law by value: every value decomposes as digit x '
      '10^class with digit 1..9 — 38/38',
      all(1 <= int(r['value']) // (10 ** int(r['class_power'])) <= 9
          and int(r['value']) % (10 ** int(r['class_power'])) == 0
          for r in rows), '38/38')
# The seat law restated independently: within each class, the digit
# should equal the seat's index in the class. It parts at exactly the
# hundreds tail — the doubled 400's shadow, positions 23-28.
fails = []
counters = {}
for r in rows:
    counters[r['class']] = counters.get(r['class'], 0) + 1
    if int(r['value']) // (10 ** int(r['class_power'])) \
            != counters[r['class']]:
        fails.append(int(r['position']))
check('the seat law parts at exactly six coordinates — positions '
      '23–28, the whole hundreds tail downstream of the doubled 400 '
      '(root seat: position 23, უ, seat-index 5 carrying digit 4)',
      fails == [23, 24, 25, 26, 27, 28], fails)
check('the doubled seat itself: 400 is the one value carried by two '
      'letters (ჳ vie and უ un); every other value has exactly one',
      sorted(ch for ch, v in table.items() if v == 400) == ['უ', 'ჳ']
      and all(sum(1 for v in table.values() if v == x) == 1
              for x in set(table.values()) if x != 400),
      [ch for ch, v in table.items() if v == 400])
check('extent: 38 letters, 37 distinct values, sum 60395, the '
      'maximum letter ჵ at 10000 — a native ten-thousands seat',
      len(table) == 38 and len(set(table.values())) == 37
      and sum(table.values()) == 60395
      and max(table, key=table.get) == 'ჵ' and table['ჵ'] == 10000,
      (len(set(table.values())), sum(table.values())))
check('the classes by seat count: units 9, tens 9, hundreds 10, '
      'thousands 9, ten-thousands 1',
      [sum(1 for r in rows if r['class'] == c) for c in
       ('units', 'tens', 'hundreds', 'thousands', 'ten-thousands')]
      == [9, 9, 10, 9, 1],
      {c: sum(1 for r in rows if r['class'] == c) for c in
       ('units', 'tens', 'hundreds', 'thousands', 'ten-thousands')})
check('no zero: no letter carries 0, and the witnesses\' unvalued '
      'tail (ჶ ჷ ჸ ჹ ჺ ჼ ჻) stands outside the table entire',
      0 not in table.values()
      and all(ch not in table for ch in 'ჶჷჸჹჺჼ჻'),
      'absence, not a seat')
check('computed data exhibits (marked as computation, not '
      'attestation): ანბანი 114, თბილისი 271, საქართველო 1022; and '
      '494 carries TWO spellings by the doubled seat (ჳჟდ, უჟდ)',
      (weigh('ანბანი'), weigh('თბილისი'), weigh('საქართველო'),
       weigh('ჳჟდ'), weigh('უჟდ')) == (114, 271, 1022, 494, 494),
      (weigh('ანბანი'), weigh('თბილისი'), weigh('საქართველო')))

# -- The control case ---------------------------------------------------------
check('CONTROL CASE — the frozen comparison stands: 37 value rows, '
      '35 AGREE, partings at exactly 400 (2 seats vs 1) and 10000 '
      '(1 seat vs 0)',
      len(cc) == 37
      and sum(1 for r in cc if r['relation'] == 'AGREE') == 35
      and [(int(r['value']), int(r['georgian_seats']),
            int(r['armenian_seats'])) for r in cc
           if r['relation'] == 'PART'] == [(400, 2, 1), (10000, 1, 0)],
      [(r['value'], r['relation']) for r in cc if r['relation'] == 'PART'])
check('CONTROL CASE — the shared domain entire: every Armenian value '
      '1..9000 is a Georgian value, and the Armenian bank\'s letters '
      'at those values stand as the CSV prints them',
      all(int(r['value']) in table.values() for r in cc
          if int(r['value']) <= 9000)
      and all(ARMENIAN[r['armenian_letters']] == int(r['value'])
              for r in cc if r['armenian_letters']),
      '36/36 Armenian values shared')
check('CONTROL CASE — extent coordinates: Armenian 36 letters / 36 '
      'distinct / sum 49995 / max 9000 against Georgian 38 / 37 / '
      '60395 / 10000',
      (len(ARMENIAN), len(set(ARMENIAN.values())),
       sum(ARMENIAN.values()), max(ARMENIAN.values()))
      == (36, 36, 49995, 9000),
      (len(ARMENIAN), sum(ARMENIAN.values())))

failed = [n for n, p in RESULTS if not p]
print()
print('GEORGIAN AUDIT BATTERY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)
