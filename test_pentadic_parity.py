#!/usr/bin/env python3
# ============================================================================
# 93
# THE PENTADIC NOTATION SEAT — PARITY OF THE READER AGAINST THE
# FIELD AUDIT'S FROZEN TRANSCRIPTIONS, AND THE CHECKED NEGATIVE
# PROVEN IN CODE
# A Scientific Illuminist proving of the notation seat
# (pontifex/pentadic.py) against the audit's frozen tables
# (research/western-sweep/pentadic-notation.csv and
# golden-numbers.csv, transcribed 2026-11-24 from witnesses read
# entire — Wikipedia, "Pentadic numerals"; Wikipedia, "Runic
# calendar"; Wikipedia, "Ogham"; Wikipedia, "In Lebor Ogaim";
# Wikipedia, "Cipher runes"; Wikipedia, "Uthark theory"; the
# Viking Answer Lady's Rundata survey). The seat is a READER, not
# a bank: the audit's closure — no runic or Ogham letter-value
# table exists — was proven stratum by stratum, and this battery
# proves both halves of the gate: the reader reads the notation
# exactly as frozen, and no weighing system answers to the name
# of the runes, of Ogham, of the pentadic notation, or of the
# modern Uthark.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: the controls first (the control word; every
#   pre-existing battery untouched, the census battery among them
#   as a subprocess); then the reader against the frozen law; then
#   the closure proven in code against the living registry.
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
from pontifex.pentadic import read_pentadic, pentadic_checks  # noqa: E402

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
                  ('pentadic', pentadic_checks)):
    cs = fn()
    check('control battery: %s %d/%d' % (label, len(cs), len(cs)),
          all(c[1] for c in cs), [c[0] for c in cs if not c[1]])
for battery in ('research/western-sweep/runic_ogham_audit_tests.py',
                'test_census_parity.py'):
    out = subprocess.run([sys.executable, os.path.join(HERE, battery)],
                         capture_output=True, text=True)
    tail = (out.stdout.strip().splitlines() or [''])[-1]
    check('subprocess battery: %s' % battery, out.returncode == 0,
          tail)

# --- The reader against the frozen law --------------------------------------
with open(os.path.join(HERE, 'research/western-sweep',
                       'pentadic-notation.csv'), encoding='utf-8') as fh:
    law = {r['sign']: r for r in csv.DictReader(fh)}
check("the frozen five-sign reads 5 at the door",
      read_pentadic('u')['value'] == int(law['five-sign']['value']),
      read_pentadic('u')['value'])
check("the frozen ten-sign reads 10 at the door",
      read_pentadic('uu')['value'] == int(law['ten-sign']['value']),
      read_pentadic('uu')['value'])
check('the frozen ceiling reads 20 at the door, and 21 is refused',
      read_pentadic('uuuu')['value']
      == int(law['two ten-signs']['value']),
      read_pentadic('uuuu')['value'])

# --- The closure, proven in code ---------------------------------------------
absent = [name for name in ('pentadic', 'runic', 'ogham', 'uthark',
                            'futhark', 'golden')
          if name not in SYSTEMS]
check('no weighing system answers to the western field: '
      'pentadic, runic, ogham, uthark, futhark, golden all absent '
      'from the registry', len(absent) == 6, absent)
with open(os.path.join(HERE, 'research/western-sweep',
                       'golden-numbers.csv'), encoding='utf-8') as fh:
    golden = list(csv.DictReader(fh))
check('the golden labels stand frozen as coordinates: 19 rows, '
      'none a letter value',
      len(golden) == 19
      and all('NOT a letter value' in r['standing'] for r in golden),
      len(golden))

print()
print('PENTADIC PARITY — %d/%d checks PASS'
      % (sum(CHECKS), len(CHECKS)))
if not all(CHECKS):
    sys.exit(1)

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
