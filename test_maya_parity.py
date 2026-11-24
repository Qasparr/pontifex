#!/usr/bin/env python3
# ============================================================================
# 93
# THE MAYA NOTATION SEAT — PARITY OF THE READER AGAINST THE
# AUDIT'S FROZEN INVENTORY, AND NO WEIGH() SYSTEM, PROVEN IN CODE
# A Scientific Illuminist proving of the notation seat
# (pontifex/maya.py) against the audit's frozen inventory
# (research/western-sweep/maya-numerals.csv, transcribed
# 2026-11-24 from witnesses read entire — Wikipedia, "Maya
# numerals"; MacTutor, "Mayan mathematics"; the head-variant
# witness). The seat is a READER under two laws, fenced by mode:
# the pure vigesimal law of the notation's shape, and the
# calendrical law of the Long Count, whose third place is
# 18 x 20 = 360 — the x18 coordinate exhibited at the door, not
# smoothed. No weighing system answers to the notation's name:
# the notation prices no letters, and the registry's silence is
# proven here in code.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: the controls first (the control word; every
#   pre-existing battery untouched, the census battery and both
#   western audit batteries among them as subprocesses); then the
#   reader against the frozen inventory; then the registry's
#   silence proven in code.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# ============================================================================

import csv
import os
import subprocess
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
HERE = __file__.rsplit('/', 1)[0]

from pontifex.engine import (  # noqa: E402
    SYSTEMS, weigh, engine_checks, greek_checks, kana_checks,
    geez_checks, halehame_checks, armenian_checks, coptic_checks,
    aramaic_checks, hangul_checks, georgian_checks, cyrillic_checks,
    glagolitic_checks)
from pontifex.doubles import doubles_checks  # noqa: E402
from pontifex.cubes import cubes_checks  # noqa: E402
from pontifex.diplomatic import diplomatic_checks  # noqa: E402
from pontifex.chinese import chinese_checks  # noqa: E402
from pontifex.triad import triad_checks  # noqa: E402
from pontifex.katapayadi import (  # noqa: E402
    katapayadi_checks, aryabhatiya_checks)
from pontifex.pentadic import pentadic_checks  # noqa: E402
from pontifex.maya import read_maya_numerals, maya_checks  # noqa: E402

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
                  ('georgian', georgian_checks),
                  ('cyrillic', cyrillic_checks),
                  ('glagolitic', glagolitic_checks),
                  ('chinese', chinese_checks),
                  ('triad', triad_checks),
                  ('katapayadi', katapayadi_checks),
                  ('aryabhatiya', aryabhatiya_checks),
                  ('pentadic', pentadic_checks),
                  ('maya', maya_checks)):
    cs = fn()
    check('control battery: %s %d/%d' % (label, len(cs), len(cs)),
          all(c[1] for c in cs), [c[0] for c in cs if not c[1]])
for battery in ('research/western-sweep/maya_audit_tests.py',
                'research/western-sweep/runic_ogham_audit_tests.py',
                'test_census_parity.py'):
    out = subprocess.run([sys.executable, os.path.join(HERE, battery)],
                         capture_output=True, text=True)
    tail = (out.stdout.strip().splitlines() or [''])[-1]
    check('subprocess battery: %s' % battery, out.returncode == 0,
          tail)

# --- The reader against the frozen inventory ---------------------------------
with open(os.path.join(HERE, 'research/western-sweep',
                       'maya-numerals.csv'), encoding='utf-8') as fh:
    inventory = list(csv.DictReader(fh))
frozen_ok = all(
    read_maya_numerals(r['glyph'])['value'] == int(r['digit'])
    and read_maya_numerals(r['glyph'])['digits'] == [int(r['digit'])]
    for r in inventory)
check('every frozen glyph reads itself at the door: 20/20 digit '
      'signs, shell included', frozen_ok, len(inventory))
check('the frozen law holds at the door: digit == 5*bars + dots '
      'for every row',
      all(int(r['digit']) == 5 * int(r['bars']) + int(r['dots'])
          for r in inventory),
      '20/20')
check('the shell reads 0 and HOLDS ITS PLACE: [1, 0, 0] differs '
      'from [1] by the place law in both modes',
      read_maya_numerals([1, 0, 0])['value'] == 400
      and read_maya_numerals([1, 0, 0], 'long_count')['value'] == 360
      and read_maya_numerals([1])['value'] == 1,
      (read_maya_numerals([1, 0, 0])['value'],
       read_maya_numerals([1, 0, 0], 'long_count')['value']))

# --- The registry's silence, proven in code ----------------------------------
absent = [name for name in ('maya', 'mayan', 'long_count')
          if name not in SYSTEMS]
check('no weighing system answers to the notation: maya, mayan, '
      'long_count all absent from the registry', len(absent) == 3,
      absent)

print()
print('MAYA PARITY — %d/%d checks PASS' % (sum(CHECKS), len(CHECKS)))
if not all(CHECKS):
    sys.exit(1)

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
