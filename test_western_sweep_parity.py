#!/usr/bin/env python3
# ============================================================================
# 93
# THE WESTERN SWEEP — THE INTEGRATION BATTERY
# A Scientific Illuminist proving that the sweep's two seats (the
# pentadic reader, pontifex/pentadic.py; the Maya reader,
# pontifex/maya.py) landed without moving anything the engine
# already held: the control word first, then every pre-existing
# checks battery run untouched, then every battery of the sweep
# itself — both field audits, both leg parities, and the WORLD
# CENSUS battery (38/38) — as subprocesses, and the registry's
# silence for the whole western field proven in code: no weighing
# system answers to pentadic, runic, ogham, uthark, futhark,
# golden, maya, mayan, or long_count.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# ============================================================================

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
from pontifex.maya import maya_checks  # noqa: E402

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

# --- Every battery of record, as subprocesses --------------------------------
for battery in ('research/western-sweep/runic_ogham_audit_tests.py',
                'research/western-sweep/maya_audit_tests.py',
                'test_pentadic_parity.py',
                'test_maya_parity.py',
                'test_census_parity.py'):
    out = subprocess.run([sys.executable, os.path.join(HERE, battery)],
                         capture_output=True, text=True)
    tail = (out.stdout.strip().splitlines() or [''])[-1]
    check('subprocess battery: %s' % battery, out.returncode == 0,
          tail)

# --- The registry's silence for the whole western field -----------------------
absent = [name for name in ('pentadic', 'runic', 'ogham', 'uthark',
                            'futhark', 'golden', 'maya', 'mayan',
                            'long_count')
          if name not in SYSTEMS]
check('no weighing system answers to the western field: all nine '
      'names absent from the registry', len(absent) == 9, absent)
check('the registry still holds exactly the census\'s 17 systems',
      len(SYSTEMS) == 17, len(SYSTEMS))

print()
print('WESTERN SWEEP PARITY — %d/%d checks PASS'
      % (sum(CHECKS), len(CHECKS)))
if not all(CHECKS):
    sys.exit(1)

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
