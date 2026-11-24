#!/usr/bin/env python3
# ============================================================================
# 93
# THE GEORGIAN TABLE — PARITY OF THE ENGINE SEAT AGAINST THE PHASE I
# AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the Georgian bank in the main
# engine (pontifex/pontifex) against the independent seat the Phase I
# audit built from the sources (research/caucasus-north:
# georgian-table.csv and georgian-control-case.csv, transcribed from
# two witnesses read entire — Wikipedia, "Georgian numerals", its
# table sourced there to Makharoblidze 2009; georgianalphabet.com,
# its per-letter value cards and "Numeral letters" section — and
# diffed cell by cell in the builder, which aborts on any parting).
# The seat was built at the desk on 2026-11-24 as Phase I of the
# Caucasus-and-the-North road, under the founder's standing rules.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from the two living seats — the
#   engine's bank (a literal dict in tables.py, keyed in Mkhedruli)
#   and the audit's CSVs (generated in georgian_audit.py from the
#   witnesses, with Unicode-name verification and the dress partners
#   matched by the standard's names). Nothing is hard-coded from
#   memory except the doctrine's own printed numbers, cited to
#   their pages.
#
# DOCTRINE — THE CONTROLS: the engine's own control word (θέλημα
#   = 93) is weighed first; every pre-existing battery is run and
#   must pass untouched; and the Phase I audit's own battery (15
#   checks) is run as a subprocess — the audit instrument must
#   still hold before its data can witness anything.
#
# DOCTRINE — THE CONTROL CASE, EXHIBITED: the founder ordered this
#   table read beside the Armenian — the two designed alphabets of
#   the Caucasus under one decimal class law. The exhibit below
#   holds the shared domain at BOTH engine seats: every Armenian
#   value 1–9000 is a Georgian value (36/36), and the two banks
#   part at exactly two value coordinates — 400 (two Georgian
#   seats, one Armenian) and 10000 (a Georgian letter, no Armenian
#   seat — a device instead). The agreement is a property of two
#   attested value sequences, printed as coordinates — it is NOT a
#   bridge: no word is weighed on both banks here, and none is
#   claimed.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
    hangul_checks, georgian_checks,
)
from pontifex.tables import GEORGIAN, ARMENIAN
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


def power(pos):
    # MECHANISM: the class law restated independently in the battery:
    # classes by seat — units 1–9, tens 10–18, hundreds 19–28,
    # thousands 29–37, ten-thousands 38 — value's digit x 10^power.
    return 0 if pos <= 9 else 1 if pos <= 18 else 2 if pos <= 28 \
        else 3 if pos <= 37 else 4


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
                  ('diplomatic', diplomatic_checks),
                  ('chinese', chinese_checks), ('triad', triad_checks),
                  ('katapayadi', katapayadi_checks),
                  ('aryabhatiya', aryabhatiya_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = georgian_checks()
check('seat battery — georgian_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'georgian_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes (15 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat, read ---------------------------------------------
with open(AUDIT_DIR / 'georgian-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'georgian-control-case.csv', encoding='utf-8') as fh:
    cc = list(csv.DictReader(fh))
SOURCED = [r for r in rows if r['status'] == 'SOURCED']
check('the frozen transcription stands in the data seat: 38 SOURCED '
      'rows, none open',
      len(SOURCED) == 38 and len(rows) == 38, len(SOURCED))

# --- Sign for sign: the engine seat against the audit seat -------------------
check('bank identity — engine GEORGIAN == the audit’s 38 SOURCED '
      'rows, key for key, value for value',
      GEORGIAN == {r['letter']: int(r['value']) for r in SOURCED},
      (len(GEORGIAN), len(SOURCED)))
bad = [(r['letter'], unicodedata.name(r['letter'], ''),
        r['unicode_name']) for r in SOURCED
       if unicodedata.name(r['letter'], '') != r['unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata',
      not bad, bad or '38/38 verified')
check('the dress coordinate in the data: every frozen row carries '
      'its Asomtavruli and Nuskhuri partners, matched by name',
      all(r['asomtavruli'] and r['nuskhuri'] for r in SOURCED),
      '38/38 dressed')
check('the class law by value at the engine seat, recomputed from '
      'the audit’s positions: digit x 10^class at all 38',
      all(GEORGIAN[r['letter']]
          == (GEORGIAN[r['letter']] // (10 ** power(int(r['position']))))
          * (10 ** power(int(r['position'])))
          and 1 <= GEORGIAN[r['letter']]
          // (10 ** power(int(r['position']))) <= 9 for r in SOURCED),
      '38/38 by the law')
fails = []
counters = {}
for r in SOURCED:
    p = int(r['position'])
    counters[power(p)] = counters.get(power(p), 0) + 1
    if int(r['value']) // (10 ** power(p)) != counters[power(p)]:
        fails.append(p)
check('the seat law’s parting at the engine seat, at the audit’s '
      'coordinates: positions 23–28 exactly',
      fails == [23, 24, 25, 26, 27, 28], fails)

# --- The witnesses' numbers at the engine's doors ------------------------------
r = weigh('ჩყმვ', 'georgian')
check('calibration at the seat: ჩყმვ == 1846 (the Motsameta '
      'inscription’s date), breakdown exact',
      r['value'] == 1846 and r['breakdown'] == [('ჩ', 1000), ('ყ', 800),
                                                ('მ', 40), ('ვ', 6)],
      (r['value'], r['breakdown']))
ex = (weigh('ჩღჲთ', 'georgian')['value'],
      weigh('ჩყპზ', 'georgian')['value'],
      weigh('ციბ', 'georgian')['value'],
      weigh('ცკვ', 'georgian')['value'])
check('the witnesses’ examples at the seat: 1769, 1887, 2012, 2026',
      ex == (1769, 1887, 2012, 2026), ex)
check('the system’s arithmetic at the seat: the 38 values sum to '
      '60395; 37 distinct; the maximum letter ჵ == 10000',
      sum(GEORGIAN.values()) == 60395
      and len(set(GEORGIAN.values())) == 37
      and GEORGIAN['ჵ'] == 10000,
      (sum(GEORGIAN.values()), len(set(GEORGIAN.values()))))
check('the duplicate’s consequence at the seat: ჳჟდ == უჟდ == 494 '
      '(two spellings, one number)',
      weigh('ჳჟდ', 'georgian')['value']
      == weigh('უჟდ', 'georgian')['value'] == 494,
      weigh('უჟდ', 'georgian')['value'])
check('the house corpus at this bank, printed as data: the '
      'Georgian-script exhibits (ანბანი 114, თბილისი 271, '
      'საქართველო 1022); a Latin-script head weighs silence — the '
      'bank hears only its own tongue',
      (weigh('ანბანი', 'georgian')['value'],
       weigh('თბილისი', 'georgian')['value'],
       weigh('საქართველო', 'georgian')['value']) == (114, 271, 1022)
      and weigh('THELEMA', 'georgian')['value'] == 0
      and weigh('THELEMA', 'georgian')['breakdown'] == [],
      weigh('საქართველო', 'georgian')['value'])

# --- The control case, exhibited at both seats ----------------------------------
agree = [r for r in cc if r['relation'] == 'AGREE']
part = [(int(r['value']), int(r['georgian_seats']),
         int(r['armenian_seats'])) for r in cc if r['relation'] == 'PART']
check('CONTROL CASE — the frozen comparison at both engine seats: '
      '37 value rows, 35 AGREE, partings at 400 (2 vs 1) and 10000 '
      '(1 vs 0)',
      len(cc) == 37 and len(agree) == 35
      and part == [(400, 2, 1), (10000, 1, 0)]
      and all(ARMENIAN[r['armenian_letters']] == int(r['value'])
              for r in cc if r['armenian_letters'])
      and all(GEORGIAN[r['georgian_letters'][0]] == int(r['value'])
              for r in cc if r['georgian_letters']),
      part)
check('CONTROL CASE — the shared domain entire at the seats: every '
      'Armenian value is a Georgian value (36/36), and Georgian '
      'adds exactly one value beyond the shared domain: 10000',
      set(ARMENIAN.values()) <= set(GEORGIAN.values())
      and set(GEORGIAN.values()) - set(ARMENIAN.values()) == {10000},
      sorted(set(GEORGIAN.values()) - set(ARMENIAN.values())))
print('COORD — THE CONTROL CASE: the two designed alphabets carry '
      'one value sequence over 1–9000 entire (36/36 values shared), '
      'reached under one class law, and part at exactly two value '
      'coordinates — the doubled 400 (Georgian seats two letters '
      'there, Armenian one) and 10000 (Georgian a letter, ჵ; '
      'Armenian no seat, its overline device instead). Extent parts '
      'too: 38 letters against 36, 37 distinct values against 36, '
      'and the archaic letters run opposite ways in time — '
      'Georgian’s five are classical members dropped from modern '
      'writing; Armenian’s two are medieval additions standing in '
      'an annex. The agreement is exhibited as coordinates; no '
      'bridge is claimed on it.')

# --- The fences ---------------------------------------------------------------------
p = SYSTEMS['georgian']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('ATTESTED') and '38' in p and '400' in p
      and '10000' in p and 'Mkhedruli' in p, p[:60])
p = SYSTEMS['armenian']['provenance']
check('the neighbour’s fence stands unaltered beside the new seat',
      p.startswith('ATTESTED') and '36' in p and 'ARMENIAN_LATE' in p, p[:60])

failed = [r for r in RESULTS if not r[1]]
print()
print('GEORGIAN PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
