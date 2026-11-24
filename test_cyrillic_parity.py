#!/usr/bin/env python3
# ============================================================================
# 93
# THE CYRILLIC TABLE — PARITY OF THE ENGINE SEAT AGAINST THE PHASE II
# AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the Cyrillic bank in the main
# engine (pontifex/pontifex) against the independent seat the Phase
# II audit built from the sources (research/caucasus-north:
# cyrillic-table.csv, transcribed from two witnesses read entire —
# Wikipedia, "Cyrillic numerals"; languagesandnumbers, "Old Church
# Slavonic numbers" — diffed cell by cell in the builder, and held
# against the living GREEK bank at the witnesses' own pairings).
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from the two living seats — the
#   engine's bank (a literal dict in tables.py, keyed in capitals)
#   and the audit's CSV. The inheritance is checked against the
#   LIVING parent bank, never against a transcription of it.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα = 93)
#   is weighed first; every pre-existing battery is run and must
#   pass untouched; and the Phase II audit's own battery is run as
#   a subprocess — the audit instrument must still hold before its
#   data can witness anything.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pontifex.engine import (
    weigh, cyrillic, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
    hangul_checks, georgian_checks, cyrillic_checks,
)
from pontifex.tables import CYRILLIC, GREEK
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import diplomatic_checks
from pontifex.chinese import chinese_checks
from pontifex.triad import triad_checks
from pontifex.katapayadi import katapayadi_checks, aryabhatiya_checks

AUDIT_DIR = HERE / 'research' / 'caucasus-north'
RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks),
                  ('armenian', armenian_checks),
                  ('coptic', coptic_checks),
                  ('aramaic', aramaic_checks),
                  ('hangul', hangul_checks),
                  ('georgian', georgian_checks),
                  ('diplomatic', diplomatic_checks),
                  ('chinese', chinese_checks), ('triad', triad_checks),
                  ('katapayadi', katapayadi_checks),
                  ('aryabhatiya', aryabhatiya_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = cyrillic_checks()
check('seat battery — cyrillic_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'slavonic_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase II audit battery still passes (17 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat ----------------------------------------------------
with open(AUDIT_DIR / 'cyrillic-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
SOURCED = [r for r in rows if r['status'] == 'SOURCED']
VARIANT = [r for r in rows if r['status'] == 'VARIANT']
REFUSED = [r for r in rows if r['status'] == 'REFUSED-WESTERN']
check('the frozen transcription stands in the data seat: 27 SOURCED '
      'seats, 6 VARIANT forms, the western pair REFUSED',
      (len(SOURCED), len(VARIANT), len(REFUSED)) == (27, 6, 2),
      (len(SOURCED), len(VARIANT), len(REFUSED)))
frozen = {r['letter']: int(r['value']) for r in SOURCED + VARIANT}
check('bank identity — engine CYRILLIC == the audit’s SOURCED + '
      'VARIANT rows, key for key, value for value',
      CYRILLIC == frozen, (len(CYRILLIC), len(frozen)))
bad = [(r['letter'], unicodedata.name(r['letter'], ''),
        r['unicode_name']) for r in SOURCED + VARIANT
       if unicodedata.name(r['letter'], '') != r['unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata',
      not bad, bad or '33/33 verified')

# --- The inheritance, at the seats ---------------------------------------------
check('THE INHERITANCE at the seats: every SOURCED row’s value == '
      'the living GREEK bank at its frozen Greek pairing (27/27)',
      all(GREEK[r['greek_pair'].lower()] == int(r['value'])
          for r in SOURCED), '27/27 == GREEK')
check('the value SETS are one set: the Cyrillic canonical values '
      '== the Greek bank’s 27-seat value set (the Milesian '
      'sequence entire, sum 4995)',
      {int(r['value']) for r in SOURCED}
      == {v for k, v in GREEK.items() if k not in ('στ', 'ς')}
      and sum(int(r['value']) for r in SOURCED) == 4995,
      sum(int(r['value']) for r in SOURCED))

# --- The witnesses' numbers at the engine's doors ------------------------------
ex = (weigh('ѰЗ', 'cyrillic')['value'],
      weigh('ЦЧѲ', 'cyrillic')['value'],
      weigh('РНГ', 'cyrillic')['value'])
check('calibration at the seat: ѰЗ 707, ЦЧѲ 999, РНГ 153',
      ex == (707, 999, 153), ex)
d = (cyrillic('҂Ѕ')['value'], cyrillic('҂Л҂В')['value'],
     cyrillic('҂АѰЕ')['value'], cyrillic('҂ЗРИІ')['value'])
check('the device at the door: ҂Ѕ 6000, ҂Л҂В 32000, ҂АѰЕ 1705, '
      '҂ЗРИІ 7118 — the thousands sign priced at x1000',
      d == (6000, 32000, 1705, 7118), d)
check('the boundary in the data is the boundary at the seat: the '
      'REFUSED rows’ Ҁ weighs silence, and Ч stands at its '
      'canonical 90 (never the western 60)',
      weigh('Ҁ', 'cyrillic')['breakdown'] == []
      and weigh('Ч', 'cyrillic')['value'] == 90,
      weigh('Ч', 'cyrillic')['value'])
check('the house corpus at this bank, printed as data: a Georgian '
      'or Greek head weighs silence here — the bank hears only its '
      'own tongue’s letters (and its parent’s values)',
      weigh('საქართველო', 'cyrillic')['value'] == 0
      and weigh('ΘΕΛΗΜΑ', 'cyrillic')['value'] == 0,
      weigh('ΘΕΛΗΜΑ', 'cyrillic')['value'])

# --- The fences ---------------------------------------------------------------------
p = SYSTEMS['cyrillic']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('DERIVED') and '27' in p and 'REFUSED' in p
      and 'greek' in p, p[:60])
p = SYSTEMS['greek']['provenance']
check('the parent’s fence stands unaltered beside the heir',
      p.startswith('ATTESTED'), p)

failed = [r for r in RESULTS if not r[1]]
print()
print('CYRILLIC PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
