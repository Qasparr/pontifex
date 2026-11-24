#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — test_sanskrit_parity.py — the Sanskrit doors' parity
# battery: the Phase II module against the Phase I audit's frozen
# data, controls first.
#
# Epigraph: "the digits are to be read from left to right in the
# ordinary way" — the gopībhāgya verse's documented exception,
# which this battery asserts as an exception and the doors do not
# implement. What the record marks as a violation, the engine
# leaves unbuilt; what it marks as law, the engine proves.
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the module pontifex/katapayadi.py is the audit's
#     frozen tables wearing doors — identical cells, the witnesses'
#     exhibits exact through the module, the round-trip property
#     holding at the engine seat, the refusals holding — and
#     nothing else in the engine moved.
#   Method: controls first (the calibration weighing; every
#     pre-existing check battery, the diplomatic key's included;
#     the Phase I audit battery as a subprocess), then the module
#     diffed cell by cell against the audit's CSVs, the exhibits
#     re-run through the module, the round-trips widened, the
#     fail-closed boundaries asserted, and the species fence
#     proven in code: no 'sanskrit' weighing system exists.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Parity: the Sanskrit doors against the audit's frozen data.

DOCTRINE: the module's tables are not trusted because they were
typed carefully; they are proven identical to the CSVs the audit
froze from the witnesses. The doors are not trusted because their
checks pass; they are proven on the witnesses' own exhibits, at
wider round-trip ranges than the audit seat used, and at the
boundaries — the OPEN ḷa row, the nukta refusal, the slate's
ceiling at hau — where a careless seat would guess.
"""

import csv
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pontifex.engine import (
    SYSTEMS, weigh, engine_checks, greek_checks, kana_checks,
    geez_checks, halehame_checks, armenian_checks, coptic_checks,
    aramaic_checks)
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import diplomatic_checks
from pontifex.katapayadi import (
    KATAPAYADI_DIGITS, ARYABHATIYA_VALUES, _VOWEL_INDEX,
    katapayadi_digits, katapayadi_decode, katapayadi_encode,
    aryabhatiya_decode, aryabhatiya_encode,
    katapayadi_checks, aryabhatiya_checks)

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed)))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def load(name):
    path = HERE / 'research' / 'twelve-tongues' / name
    with path.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


# --- Controls: the house stands as it stood ------------------------

check('control — θέλημα weighs 93 in the Greek bank',
      weigh('θελημα', 'greek'), 93)
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks),
                  ('armenian', armenian_checks),
                  ('coptic', coptic_checks),
                  ('aramaic', aramaic_checks),
                  ('diplomatic', diplomatic_checks)):
    cs = fn()
    check('control — %s_checks() passes untouched (%d)'
          % (label, len(cs)), all(p for _, p, _ in cs), len(cs))

audit_battery = subprocess.run(
    [sys.executable, 'research/twelve-tongues/sanskrit_audit_tests.py'],
    cwd=str(HERE), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes '
      '(34 checks)', audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-2]
      if audit_battery.stdout else audit_battery.stderr[-200:])

# --- The module's own batteries ------------------------------------

for label, fn in (('katapayadi', katapayadi_checks),
                  ('aryabhatiya', aryabhatiya_checks)):
    cs = fn()
    check('seat battery — %s_checks() passes (%d)'
          % (label, len(cs)), all(p for _, p, _ in cs), len(cs))

# --- Table parity: module == frozen CSVs, cell by cell --------------

kata_rows = load('sanskrit-katapayadi-table.csv')
csv_kata = {r['devanagari']: int(r['digit']) for r in kata_rows
            if r['status'] == 'SOURCED'}
check('Kaṭapayādi parity: module table == frozen CSV, 33/33 cells',
      KATAPAYADI_DIGITS == csv_kata,
      (len(KATAPAYADI_DIGITS), len(csv_kata)))

arya_rows = load('sanskrit-aryabhatiya-table.csv')
csv_arya = {r['devanagari']: int(r['value']) for r in arya_rows
            if r['kind'] == 'consonant'}
check('Āryabhaṭīya parity: module values == frozen CSV, 33/33 '
      'cells', ARYABHATIYA_VALUES == csv_arya,
      (len(ARYABHATIYA_VALUES), len(csv_arya)))
csv_vowels = {r['transliteration']: int(r['multiplier'])
              for r in arya_rows if r['kind'] == 'vowel'}
check('Āryabhaṭīya parity: module vowel multipliers == frozen '
      'CSV, 9/9 cells',
      {k: 100 ** v for k, v in _VOWEL_INDEX.items()} == csv_vowels,
      len(csv_vowels))

# --- Exhibits through the module -------------------------------------

kata_ex = load('sanskrit-katapayadi-examples.csv')
bad = []
for row in kata_ex:
    if row['reading'] == 'leftward (standard)':
        if katapayadi_decode(row['devanagari']) != \
                int(row['expected_number']):
            bad.append(row['exhibit'])
    elif row['reading'].startswith('DIRECT'):
        if katapayadi_digits(row['devanagari']) != \
                [int(x) for x in row['expected_digits'].split()]:
            bad.append(row['exhibit'])
    elif row['reading'] == 'melakarta prefix rule':
        d = katapayadi_digits(row['devanagari'])
        if d[0] + 10 * d[1] != int(row['expected_number']):
            bad.append(row['exhibit'])
check('exhibits: every Kaṭapayādi row of the audit (21) exact '
      'through the module', bad == [], bad or '21/21')

arya_ex = load('sanskrit-aryabhatiya-examples.csv')
bad = []
for row in arya_ex:
    if aryabhatiya_decode(row['devanagari']) != \
            int(row['expected_value']):
        bad.append(row['exhibit'])
check('exhibits: every Āryabhaṭīya row of the audit (29) exact '
      'through the module', bad == [], bad or '29/29')

# --- Round-trips, widened past the audit seat -------------------------

check('round-trip (engine seat): Kaṭapayādi decode∘encode == '
      'identity, 0..9999',
      all(katapayadi_decode(katapayadi_encode(n)) == n
          for n in range(10000)), True)
check('round-trip (engine seat): Āryabhaṭīya decode∘encode == '
      'identity, 0..20000 + the boundary exhibits',
      all(aryabhatiya_decode(aryabhatiya_encode(n)) == n
          for n in list(range(20001)) +
          [4320000, 299792458, 1582237500, 10 ** 16, 10 ** 18]),
      True)

# --- The boundaries ----------------------------------------------------

def raises(fn):
    try:
        fn()
        return False
    except ValueError:
        return True

check('boundary: ḷa fails closed at the Kaṭapayādi door '
      '(the row stands OPEN)',
      raises(lambda: katapayadi_decode('ळ')), True)
check('boundary: a nukta loan letter fails closed at both doors',
      (raises(lambda: katapayadi_decode('ओज़')),
       raises(lambda: aryabhatiya_decode('ज़'))), (True, True))
check('boundary: a vowelless cluster fails closed at the '
      'Āryabhaṭīya door, and is ignored (as ruled) at the '
      'Kaṭapayādi door',
      (raises(lambda: aryabhatiya_decode('यद्')),
       katapayadi_decode('यद्')), (True, 1))
check('boundary: the slate\'s ceiling — encode(10^18) is hau; '
      '10^18 + 1 raises',
      (aryabhatiya_encode(10 ** 18),
       raises(lambda: aryabhatiya_encode(10 ** 18 + 1))),
      ('हौ', True))
check('boundary: negative numbers raise at both encoders',
      (raises(lambda: katapayadi_encode(-1)),
       raises(lambda: aryabhatiya_encode(-1))), (True, True))

# --- The species fence, proven in code ---------------------------------

_registered = [s for s in ('sanskrit', 'katapayadi', 'aryabhatiya')
               if s in SYSTEMS]
check('SPECIES FENCE: no weighing system is registered for '
      'Sanskrit under any name',
      _registered == [], _registered)
check('SPECIES FENCE: weigh() refuses the category error',
      raises(lambda: weigh('क', 'sanskrit')), True)
check('the species boundary, at coordinates: one string, two '
      'doors, two numbers — मखि reads 25 at the encoder (ma = 5, '
      'khi\'s kha = 2, read leftward) and 225 at the cipher '
      '(ma 25 × 1 + kha 2 × 100)',
      (katapayadi_decode('मखि'), aryabhatiya_decode('मखि')),
      (25, 225))

print()
failed = [n for n, p in RESULTS if not p]
print('SANSKRIT PARITY — %d/%d PASS'
      % (len(RESULTS) - len(failed), len(RESULTS)))
if failed:
    print('FAILURES: %r' % (failed,))
    sys.exit(1)
print('BATTERY VERDICT: PASS')
