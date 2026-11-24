#!/usr/bin/env python3
# ============================================================================
# 93
# THE REGIONAL TRIAD DIAL — PARITY OF THE DIAL AGAINST ALL THREE
# STRATA'S FROZEN SOURCES
# A Scientific Illuminist proving of the dial (pontifex/triad.py)
# against the seats it reads: the kana mint's own doctrine
# exhibits, the Korean audit's frozen orders
# (research/twelve-tongues/korean-jamo.csv), and the Chinese
# audit's frozen tables (chinese-numerals.csv, chinese-cycles.csv)
# — the dial proven to read its strata as they were frozen,
# stratum by stratum, and to keep the notation's readings out of
# the weight. Built 2026-11-24 under the founder's three standing
# rules and his dial spec (a zero point at the same place for
# every tongue — a position, not a value).
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# DOCTRINE — THE CONTROLS: the control word (θέλημα = 93) first;
#   every pre-existing battery untouched, the two Phase II
#   parities included; the Phase I audit battery (12) as a
#   subprocess.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# ============================================================================

import csv
import subprocess
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])

from pontifex.engine import (  # noqa: E402
    weigh, engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks,
    aramaic_checks, hangul_checks)
from pontifex.chinese import chinese_checks  # noqa: E402
from pontifex.doubles import doubles_checks  # noqa: E402
from pontifex.cubes import cubes_checks  # noqa: E402
from pontifex.diplomatic import diplomatic_checks  # noqa: E402
from pontifex.triad import triad_weigh, triad_zero, triad_checks  # noqa: E402

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
                  ('chinese', chinese_checks),
                  ('triad', triad_checks)):
    cs = fn()
    check('control battery: %s %d/%d' % (label, len(cs), len(cs)),
          all(c[1] for c in cs), [c[0] for c in cs if not c[1]])
for script in ('test_korean_parity.py', 'test_chinese_parity.py',
               'research/twelve-tongues/east_asian_audit_tests.py'):
    run = subprocess.run([sys.executable, HERE + '/' + script],
                         capture_output=True, text=True)
    check('control battery: %s passes' % script,
          run.returncode == 0,
          run.stdout.strip().splitlines()[-1]
          if run.stdout.strip() else run.stderr[-200:])

# --- The Japanese stratum against the mint's own exhibits -------------------
check("the anchor's bridges on the dial: ゆず 93, かな 27, "
      'しおん 65 — each entirely in the Japanese stratum',
      all(triad_weigh(w)['weight'] == n
          and triad_weigh(w)['strata']['japanese'] == n
          and triad_weigh(w)['strata']['korean'] == 0
          for w, n in (('ゆず', 93), ('かな', 27), ('しおん', 65))),
      [(w, triad_weigh(w)['weight']) for w in ('ゆず', 'かな',
                                               'しおん')])

# --- The Korean stratum against the frozen orders ---------------------------
rows = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/korean-jamo.csv',
         encoding='utf-8')))
sk_initials = [r['glyph'] for r in rows
               if r['grid'] == 'modern-SK'
               and r['stratum'] == 'initial']
# every frozen initial, standing alone at the door, weighs its
# seat — except the hinge ㅇ, which the null law prices 0: the
# parting is the check's own exhibit, not an exception smuggled.
bad = []
for r in rows:
    if r['grid'] != 'modern-SK' or r['stratum'] != 'initial':
        continue
    got = triad_weigh(r['glyph'])['weight']
    want = 0 if r['glyph'] == 'ㅇ' else int(r['position'])
    if got != want:
        bad.append((r['glyph'], r['position'], got))
check('the Korean stratum on the dial: all 19 frozen initials '
      'weigh their seats, the hinge ㅇ weighing 0 by the null '
      'law', not bad and len(sk_initials) == 19,
      bad or '19/19 (18 seats + the null)')

# --- The Chinese stratum against the frozen tables --------------------------
nrows = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/chinese-numerals.csv',
         encoding='utf-8')))
bad = []
for row in nrows:
    if row['kind'] != 'digit':
        continue  # multipliers read under a head — proven in
        # test_chinese_parity.py and at scale below
    r = triad_weigh(row['everyday_trad'])
    if not ([x['value'] for x in r['readings']]
            == [int(row['value'])] and r['weight'] == 0):
        bad.append((row['everyday_trad'], row['value']))
check('the Chinese stratum on the dial: every frozen digit '
      'READS its value and weighs nothing', not bad,
      bad or 'digits 10/10 read, weight 0')
r = triad_weigh('一億二千三百四十五萬六千七百八十九')
check('the notation at scale on the dial: the myriad exhibit '
      'reads 123456789, weight still 0',
      [x['value'] for x in r['readings']] == [123456789]
      and r['weight'] == 0, r['readings'][0]['value'])
cyc = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/chinese-cycles.csv',
         encoding='utf-8')))
bad = []
for row in cyc:
    r = triad_weigh(row['glyph'])
    want = [(row['glyph'], row['cycle'], int(row['position']))]
    if r['cycles'] != want or r['weight'] != 0:
        bad.append((row['glyph'], r['cycles']))
check('the cycles on the dial: all 22 frozen glyphs report '
      'their attested ordinals as weightless coordinates',
      not bad and len(cyc) == 22, bad or '22/22')

# --- The zero, against the spec ----------------------------------------------
z = triad_zero()
check("the zero point: the founder's definition on the dial's "
      'face, the three faces computed (HOLE / PLACEHOLDER / '
      'GLYPH)',
      z['definition'] == '0 = {0, 2, 1−1=0}'
      and z['faces']['japanese'].startswith('HOLE')
      and z['faces']['korean'].startswith('PLACEHOLDER')
      and z['faces']['chinese'].startswith('GLYPH'),
      (z['faces']['japanese'][:12], z['faces']['korean'][:12],
       z['faces']['chinese'][:12]))

print()
print('TRIAD PARITY — %d/%d checks PASS' % (sum(CHECKS),
                                            len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
