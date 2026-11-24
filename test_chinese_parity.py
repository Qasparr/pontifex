#!/usr/bin/env python3
# ============================================================================
# 93
# THE CHINESE NOTATION SEAT — PARITY OF THE READER AGAINST THE
# PHASE I AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the notation seat
# (pontifex/chinese.py) against the audit's frozen tables
# (research/twelve-tongues/chinese-numerals.csv and
# chinese-cycles.csv, transcribed 2026-11-24 from three witnesses
# read entire — Wikipedia, "Chinese numerals"; Omniglot;
# Wikipedia, "Korean numerals"; and for the cycles Wikipedia's
# "Heavenly Stems" and "Earthly Branches", Herong Yang, and the
# Chinese Calendar Atlas). The seat is a READER, not a bank: the
# audit's closure — no Chinese letter-value table exists — was
# re-verified, and this battery proves both halves of the gate:
# the reader reads the notation exactly as frozen, and no
# weighing system answers to the notation's name.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from the frozen CSVs and the
#   living reader. A digit glyph alone reads its value; a
#   multiplier reads its value under an explicit one (一十, 一萬)
#   in either dress; the two dresses of every cell read one
#   number — the face-law's local instance, proven per cell.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) first; every pre-existing battery untouched; the Phase I
#   audit battery (12 checks) as a subprocess.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# ============================================================================

import csv
import subprocess
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])

from pontifex.engine import (  # noqa: E402
    SYSTEMS, weigh, engine_checks, greek_checks, kana_checks,
    geez_checks, halehame_checks, armenian_checks, coptic_checks,
    aramaic_checks, hangul_checks)
from pontifex.chinese import read_chinese_numerals, chinese_checks  # noqa: E402
from pontifex.doubles import doubles_checks  # noqa: E402
from pontifex.cubes import cubes_checks  # noqa: E402
from pontifex.diplomatic import diplomatic_checks  # noqa: E402

HERE = __file__.rsplit('/', 1)[0]
CHECKS = []


def check(name, passed, got):
    CHECKS.append(bool(passed))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls -----------------------------------------------------------
check("the control word: weigh('θέλημα', 'greek') == 93",
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks),
                  ('armenian', armenian_checks),
                  ('coptic', coptic_checks),
                  ('aramaic', aramaic_checks),
                  ('diplomatic', diplomatic_checks),
                  ('hangul', hangul_checks),
                  ('chinese', chinese_checks)):
    cs = fn()
    check('control battery: %s %d/%d' % (label, len(cs), len(cs)),
          all(c[1] for c in cs), [c[0] for c in cs if not c[1]])

audit = subprocess.run(
    [sys.executable, HERE + '/research/twelve-tongues/'
     'east_asian_audit_tests.py'],
    capture_output=True, text=True)
check('control battery: the Phase I audit battery passes (12/12)',
      audit.returncode == 0 and '12/12 PASS' in audit.stdout,
      audit.stdout.strip().splitlines()[-1]
      if audit.stdout.strip() else audit.stderr[-200:])

# --- Parity against the frozen numeral table --------------------------------
rows = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/chinese-numerals.csv',
         encoding='utf-8')))
bad = []
for row in rows:
    value = int(row['value'])
    if row['kind'] == 'digit':
        for dress in ('everyday_trad', 'financial_trad'):
            got = read_chinese_numerals(row[dress])['value']
            if got != value:
                bad.append((row[dress], value, got))
    else:
        # a multiplier reads its value under an explicit one,
        # in either dress: 一十, 壹拾, 一萬, 壹萬 …
        for one, glyph in (('一', row['everyday_trad']),
                           ('壹', row['financial_trad'])):
            got = read_chinese_numerals(one + glyph)['value']
            if got != value:
                bad.append((one + glyph, value, got))
check('parity: all 16 frozen cells read their values in both '
      'dresses (digits at face; multipliers under an explicit '
      'one)', not bad and len(rows) == 16, bad or '16/16 cells')

# The face-law's local instance, per cell: the two dresses of the
# composed reading agree (二十 == 貳拾; 一百 == 壹佰; 一千 == 壹仟).
pairs = [('二十', '貳拾', 20), ('一百', '壹佰', 100),
         ('一千', '壹仟', 1000), ('一萬', '壹萬', 10000)]
bad = [(a, b) for a, b, n in pairs
       if read_chinese_numerals(a)['value'] != n
       or read_chinese_numerals(b)['value'] != n]
check('parity: the dresses agree per composed reading (one '
      'value sequence, two dresses, values unmoved)',
      not bad, bad or pairs)

# --- Parity against the frozen cycles ---------------------------------------
cyc = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/chinese-cycles.csv',
         encoding='utf-8')))
sys.path.insert(0, HERE + '/research/twelve-tongues')
import east_asian_audit as A  # noqa: E402
stems = [r['glyph'] for r in cyc if r['cycle'] == 'stem']
branches = [r['glyph'] for r in cyc if r['cycle'] == 'branch']
check('parity: the frozen cycles are the audit\'s cycles '
      '(stems 10, branches 12); the sexagenary law regenerates '
      'from them (甲子 first, 癸亥 last)',
      stems == A.STEMS_W1 and branches == A.BRANCHES_W1
      and A.sexagenary()[0] == '甲子'
      and A.sexagenary()[-1] == '癸亥',
      (len(stems), len(branches)))

# --- The gate's other half: NOT a bank ---------------------------------------
not_a_bank = ('chinese' not in SYSTEMS
              and 'chinese_numerals' not in SYSTEMS)
try:
    weigh('一', 'chinese')
    raised = False
except ValueError:
    raised = True
check('the gate: no weighing system answers to the notation '
      '(the reader is not a bank, and weigh() refuses the name)',
      not_a_bank and raised, (not_a_bank, raised))

print()
print('CHINESE PARITY — %d/%d checks PASS'
      % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
