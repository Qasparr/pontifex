#!/usr/bin/env python3
# ============================================================================
# 93
# THE HANGUL MINT — PARITY OF THE ENGINE SEAT AGAINST THE PHASE I
# AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the Korean seat in the main
# engine (pontifex/pontifex: tables.HANGUL* and engine.hangul)
# against the independent audit the Phase I road built from the
# witnesses (research/twelve-tongues/korean-jamo.csv, transcribed
# 2026-11-24 from Wikipedia, "Hangul" and "Hunminjeongeum", with
# the Unicode standard's block order as the standard's own
# testimony). The mint was built at the desk on 2026-11-24 under
# the founder's three standing rules and his Flagpole: a house
# coinage on a designed grid — the audit established the checked
# negative (no Korean letter-numeral tradition exists) and froze
# the grid's orders; this battery proves the engine's seats ARE
# the frozen orders, seat for seat, in both grids.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from the two living seats —
#   the engine's banks (keyed in conjoining jamo, generated from
#   the standard's blocks by name resolution) and the audit's CSV
#   (keyed in the compatibility glyphs the witnesses print). The
#   bridge between the encodings is the Unicode name, resolved
#   mechanically in both directions; nothing is hard-coded from
#   memory except the doctrine's own printed exhibits.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first; every pre-existing battery is run and
#   must pass untouched; and the Phase I audit's own battery (12
#   checks) is run as a subprocess — the audit instrument must
#   still hold before its data can witness anything.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# ============================================================================

import csv
import subprocess
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
sys.path.insert(0, __file__.rsplit('/', 1)[0]
                + '/research/twelve-tongues')

from pontifex.engine import (  # noqa: E402
    SYSTEMS, weigh, hangul, engine_checks, greek_checks,
    kana_checks, geez_checks, halehame_checks, armenian_checks,
    coptic_checks, aramaic_checks, hangul_checks)
from pontifex.tables import (  # noqa: E402
    HANGUL_INITIAL, HANGUL_VOWEL, HANGUL_FINAL,
    HANGUL_1446_INITIAL, HANGUL_1446_VOWEL, HANGUL_1446_FINAL,
    _jamo_conjoining)
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
                  ('hangul', hangul_checks)):
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

# --- Parity against the frozen transcription --------------------------------
rows = list(csv.DictReader(
    open(HERE + '/research/twelve-tongues/korean-jamo.csv',
         encoding='utf-8')))
KIND = {'initial': 'CHOSEONG', 'vowel': 'JUNGSEONG',
        'final': 'JONGSEONG', 'consonant': 'CHOSEONG'}
MODERN = {'initial': HANGUL_INITIAL, 'vowel': HANGUL_VOWEL,
          'final': HANGUL_FINAL}
ANNEX = {'consonant': HANGUL_1446_INITIAL, 'vowel': HANGUL_1446_VOWEL}

bad = []
counts = {}
for row in rows:
    grid, stratum = row['grid'], row['stratum']
    if grid == 'modern-NK':
        continue  # the parting is checked below, not seated
    bank = (MODERN if grid == 'modern-SK' else ANNEX)[stratum]
    conj = _jamo_conjoining(row['glyph'], KIND[stratum])
    if bank.get(conj) != int(row['position']):
        bad.append((grid, stratum, row['glyph'], row['position'],
                    bank.get(conj)))
    counts[grid] = counts.get(grid, 0) + 1
check('parity: every frozen seat is the engine seat (modern-SK '
      '67, 1446 consonants+vowels 28 — the annex finals are the '
      'audit-stated construction, proven in hangul_checks)',
      not bad and counts == {'modern-SK': 67, '1446': 28},
      bad or counts)

# The annex finals, stated construction: the 17 consonants at
# final seats in introduction order — recomputed from the CSV's
# 1446 consonant rows.
bad = []
for row in rows:
    if row['grid'] == '1446' and row['stratum'] == 'consonant':
        conj = _jamo_conjoining(row['glyph'], 'JONGSEONG')
        if HANGUL_1446_FINAL.get(conj) != int(row['position']):
            bad.append((row['glyph'], row['position']))
check('parity: the annex finals stand at the introduction '
      'order\'s seats (17/17)', not bad, bad or '17/17')

# The North parting, as frozen: the NK initial order is NOT the
# SK order (the doubles and ㅇ move to the end).
nk = [r['glyph'] for r in rows
      if r['grid'] == 'modern-NK' and r['stratum'] == 'initial']
sk = [r['glyph'] for r in rows
      if r['grid'] == 'modern-SK' and r['stratum'] == 'initial']
check('the parting as frozen: the North initial order differs '
      'from the South (same 19 letters, other seats)',
      nk != sk and sorted(nk) == sorted(sk) and len(nk) == 19,
      (nk[:5], sk[:5]))

# The door exhibits against the frozen grid.
r = hangul('한글')
check('the door on the frozen grid: 한글 == 52, 한국 == 40, '
      '아이 == 22 with 2 nulls',
      r['value'] == 52 and hangul('한국')['value'] == 40
      and hangul('아이')['value'] == 22
      and hangul('아이')['null_initials'] == 2,
      (r['value'], hangul('한국')['value'],
       hangul('아이')['value']))

print()
print('KOREAN PARITY — %d/%d checks PASS'
      % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
