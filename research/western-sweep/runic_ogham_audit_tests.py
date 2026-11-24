#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — runic_ogham_audit_tests.py — the Runic-and-Ogham audit
# battery. Companion to runic_ogham_audit.py and
# THE-RUNIC-AND-OGHAM-FIELD.md.
#
# 93. Authorship: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved,
# Without Prejudice. Method of Science, Aim of Religion.
#
# MECHANISM: every check re-derives a number the audit document
# prints, from the frozen CSVs and from this battery's own
# independent source constants (the witnesses' material restated
# here, not imported from the builder — a battery that imports its
# builder's constants proves nothing). Run:
# python3 runic_ogham_audit_tests.py — exit 0 = all pass.
# =============================================================================
"""The Leg A audit battery: the frozen western data, re-derived."""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed)))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def load(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


golden = load('golden-numbers.csv')
pentadic = load('pentadic-notation.csv')
ogham = load('ogham-letters.csv')
uthark = load('uthark-modern.csv')

# --- Stratum 1: the golden numbers -----------------------------------------
# Independent restatement: the Younger Futhark row in canonical
# order (the sixteen glyphs), then the three golden symbols.
YF = 'ᚠᚢᚦᚬᚱᚴᚼᚾᛁᛅᛋᛏᛒᛚᛘᛦ'
check('the golden table has 19 rows at values 1–19 in order',
      [int(r['golden_number']) for r in golden] == list(range(1, 20)),
      len(golden))
check('golden 1–16 are the Younger Futhark row entire, in order',
      ''.join(r['glyph'] for r in golden[:16]) == YF,
      ''.join(r['glyph'] for r in golden[:16]))
check('golden 17–19 are the standard\'s three golden symbols',
      [r['unicode_name'] for r in golden[16:]] ==
      ['RUNIC ARLAUG SYMBOL', 'RUNIC TVIMADUR SYMBOL',
       'RUNIC BELGTHOR SYMBOL'],
      [r['unicode_name'] for r in golden[16:]])
check('every golden glyph\'s frozen codepoint is its own',
      all(int(r['codepoint'][2:], 16) == ord(r['glyph'])
          for r in golden),
      '19/19')
# The closure coordinate: the labels are for a CLOSED cycle — the
# table's own extent is 19 and no row composes (no row's standing
# claims a letter value).
check('no golden row claims a composing letter value',
      all('NOT a letter value' in r['standing'] for r in golden),
      '19/19 rows fenced as labels')

# --- Stratum 2: the pentadic notation --------------------------------------
law = {r['sign']: r for r in pentadic}
check('the pentadic law freezes 7 sign rows + the positional row',
      len(pentadic) == 8, len(pentadic))
check('the five-sign is a single sign at 5, not five ticks',
      law['five-sign']['value'] == '5'
      and 'single sign' in law['five-sign']['standing'],
      law['five-sign']['value'])
check('the ten-sign is two opposing five-signs at 10',
      law['ten-sign']['value'] == '10'
      and 'opposing' in law['ten-sign']['form'],
      law['ten-sign']['form'])
check('the notation\'s stated ceiling is 20',
      law['two ten-signs']['value'] == '20',
      law['two ten-signs']['value'])
check('the positional stratum is recorded UNSEATED, dated 1885',
      'UNSEATED' in law['positional digit set']['standing']
      and '1885' in law['positional digit set']['standing'],
      law['positional digit set']['standing'][:60])

# --- Stratum 3: Ogham --------------------------------------------------------
check('the Ogham table has 26 rows at seats 1–26 in order',
      [int(r['seat']) for r in ogham] == list(range(1, 27)),
      len(ogham))
check('the Ogham glyphs are the Unicode block U+1681–U+169A in order',
      [ord(r['glyph']) for r in ogham] == list(range(0x1681, 0x169B)),
      'U+1681..U+169A')
check('every Ogham row\'s standard name matches the live standard',
      all(ud.name(r['glyph']) == r['unicode_name'] for r in ogham),
      '26/26')
check('the aicmi stand 5/5/5/5 over the primary twenty, forfeda 5',
      [r['aicme'] for r in ogham[:5]] == ['beithe'] * 5
      and [r['aicme'] for r in ogham[5:10]] == ['hÚatha'] * 5
      and [r['aicme'] for r in ogham[10:15]] == ['muine'] * 5
      and [r['aicme'] for r in ogham[15:20]] == ['ailme'] * 5
      and [r['aicme'] for r in ogham[20:25]] == ['forfeda'] * 5,
      '4 aicmi + forfeda')
check('no Ogham row carries a numeral value in any witness',
      all('no numeral value' in r['standing'] for r in ogham),
      '26/26 rows valueless')
parted = [int(r['seat']) for r in ogham if r['parting']]
check('the partings stand recorded at exactly 10 seats '
      '(9 transliteration + the standard\'s OR at 22)',
      parted == [3, 6, 9, 10, 12, 13, 14, 22, 24, 25], parted)
# The tract's one positional cipher, restated: Ogam Bricrenn (no.
# 14 in In Lebor Ogaim) writes B with 1 dot … I with 20 dots — the
# letter's SEAT as a dot-count. The battery pins the arithmetic of
# the claim: the primary twenty's seats run 1–20, B at 1, I at 20.
check('Ogam Bricrenn\'s dot-counts are the seats: B = 1 dot, I = 20',
      ogham[0]['name'] == 'beith' and ogham[19]['name'] == 'iodhadh'
      and int(ogham[0]['seat']) == 1 and int(ogham[19]['seat']) == 20,
      (ogham[0]['name'], ogham[19]['name']))

# --- Stratum 4: the modern fence ---------------------------------------------
check('the Uthark freezes 24 seats + the F parting row',
      len(uthark) == 25, len(uthark))
check('the Uthark row runs u = 1 … f = 24 (the shift, restated)',
      uthark[0]['rune'] == 'u' and uthark[0]['uthark_value'] == '1'
      and uthark[23]['rune'] == 'f'
      and uthark[23]['uthark_value'] == '24',
      (uthark[0]['rune'], uthark[23]['rune']))
check('every Uthark row is fenced MODERN and UNSEATED',
      all('MODERN' in r['standing'] and 'UNSEATED' in r['standing']
          for r in uthark[:24]),
      '24/24')

print()
failed = [n for n, p in RESULTS if not p]
print('RUNIC-OGHAM AUDIT BATTERY — %d/%d checks PASS'
      % (len(RESULTS) - len(failed), len(RESULTS)))
if failed:
    print('FAILURES:', failed)
    sys.exit(1)

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
