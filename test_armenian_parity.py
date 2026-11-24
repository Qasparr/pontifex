#!/usr/bin/env python3
# ============================================================================
# 93
# THE ARMENIAN TABLE — PARITY OF THE ENGINE SEAT AGAINST THE PHASE I
# AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the Armenian bank in the main
# engine (pontifex/pontifex) against the independent seat the Phase I
# audit built from the sources (research/twelve-tongues:
# armenian-table.csv and armenian-control-case.csv, transcribed from
# three witnesses read entire — Wikipedia, "Armenian numerals";
# Omniglot, "Numbers in Armenian"; Wikipedia, "Armenian alphabet" —
# with the MELA cataloging manual's worked examples held against the
# cells they exhibit). The seat was built at the desk on 2026-11-24
# under the founder's three standing rules — the road rule, the
# proof-enough rule, and the end-goal rule, under which the seat's
# one desk decision (the classical 36 only; the medieval additions
# unseated) was taken and is printed in the audit at §VII Q1.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes from the two living seats —
#   the engine's bank (a literal dict in tables.py, keyed in the
#   majuscules) and the audit's CSVs (generated in armenian_audit.py
#   from the witnesses, with Unicode-name verification). Nothing is
#   hard-coded from memory except the doctrine's own printed numbers,
#   which are cited to their pages. The seats are compared as SETS
#   with per-sign values: key for key, value for value.
#
# DOCTRINE — THE CONTROLS: the engine's own control word (θέλημα
#   = 93) is weighed first; every pre-existing battery (engine,
#   greek, doubles, cubes, kana, geez, halehame) is run and must
#   pass untouched; and the Phase I audit's own battery (24 checks)
#   is run as a subprocess — the audit instrument must still hold
#   before its data can witness anything.
#
# DOCTRINE — THE CONTROL CASE, EXHIBITED: the founder ordered this
#   table read beside the halehame witness — same decimal class-law
#   shape, opposite attestation depth. The exhibit below weighs the
#   shared domain at BOTH engine seats: the Armenian letter and the
#   halehame base at each position 1–26 carry the same value, 26 of
#   26, while their laws part at position 10 (Armenian's Ժ is its
#   first tens letter; halehame's ተ is its tenth units letter).
#   The agreement is a property of two attested value sequences,
#   printed as a coordinate — it is NOT a bridge: no word is weighed
#   on both banks here, and none is claimed.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, armenian, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks,
)
from pontifex.tables import ARMENIAN, HALEHAME_FIRST
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks

AUDIT_DIR = HERE / 'research' / 'twelve-tongues'

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def class_formula(position):
    # MECHANISM: the class law restated independently in the battery:
    # four classes of nine, value = digit x 10^class by position.
    # The battery holds the seat to the LAW as the audit states it,
    # not to the builder's private copy of it.
    return (((position - 1) % 9) + 1) * (10 ** ((position - 1) // 9))


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = armenian_checks()
check('seat battery — armenian_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'armenian_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes (24 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat, read ---------------------------------------------
with open(AUDIT_DIR / 'armenian-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'armenian-control-case.csv', encoding='utf-8') as fh:
    cc = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'armenian-values.csv', encoding='utf-8') as fh:
    sweep = list(csv.DictReader(fh))
SOURCED = [r for r in rows if r['status'] == 'SOURCED']
OPENED = [r for r in rows if r['status'] == 'OPEN']
check('the frozen transcription stands in the data seat: 36 SOURCED '
      'rows + 2 OPEN rows',
      len(SOURCED) == 36 and len(OPENED) == 2
      and [r['uppercase'] for r in OPENED] == ['Օ', 'Ֆ'],
      (len(SOURCED), len(OPENED)))

# --- Sign for sign: the engine seat against the audit seat -------------------
check('bank identity — engine ARMENIAN == the audit’s 36 SOURCED '
      'rows, key for key, value for value',
      ARMENIAN == {r['uppercase']: int(r['value']) for r in SOURCED},
      (len(ARMENIAN), len(SOURCED)))
bad = [(r['uppercase'], unicodedata.name(r['uppercase'], ''),
        r['uppercase_unicode_name']) for r in SOURCED
       if unicodedata.name(r['uppercase'], '')
       != r['uppercase_unicode_name']
       or unicodedata.name(r['lowercase'], '')
       != r['lowercase_unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata, both cases',
      not bad, bad or '36/36 verified')
check('the class law at the engine seat, recomputed from the '
      'audit’s positions: value == digit x 10^class at all 36',
      all(ARMENIAN[r['uppercase']]
          == class_formula(int(r['position'])) for r in SOURCED),
      '36/36 by the law')
check('the boundary in the data is the boundary at the seat: the '
      'OPEN rows’ letters are keys of NO case in the bank, and '
      'weigh silence',
      all(r['uppercase'] not in ARMENIAN for r in OPENED)
      and weigh('Օ', 'armenian')['breakdown'] == []
      and weigh('ֆ', 'armenian')['value'] == 0,
      [r['uppercase'] for r in OPENED])

# --- The witnesses' numbers at the engine's doors ------------------------------
r = weigh('ՌՋՀԵ', 'armenian')
check('calibration at the seat: ՌՋՀԵ == 1975, breakdown exact',
      r['value'] == 1975 and r['breakdown'] == [('Ռ', 1000), ('Ջ', 900),
                                                ('Հ', 70), ('Ե', 5)],
      (r['value'], r['breakdown']))
ex = (weigh('ՍՄԻԲ', 'armenian')['value'], weigh('ՍԴ', 'armenian')['value'],
      weigh('ՃԻ', 'armenian')['value'], weigh('Ծ', 'armenian')['value'],
      weigh('ՌՆԾԵ', 'armenian')['value'])
check('the witnesses’ examples at the seat: 2222, 2004, 120, 50, '
      'and MELA’s era date 1455', ex == (2222, 2004, 120, 50, 1455), ex)
check('the system’s arithmetic at the seat: ՔՋՂԹ == 9999 (maximum '
      'without the overline); the 36 values sum to 49995',
      weigh('ՔՋՂԹ', 'armenian')['value'] == 9999
      and sum(ARMENIAN.values()) == 49995,
      (weigh('ՔՋՂԹ', 'armenian')['value'], sum(ARMENIAN.values())))

# --- The sweep's corpus through the engine -------------------------------------
bad = [(r['term'], weigh(r['script_form'], 'armenian')['value'],
        int(r['value'])) for r in sweep
       if weigh(r['script_form'], 'armenian')['value'] != int(r['value'])]
check('the sweep’s eleven corpus weighings reproduce through the '
      'engine, minuscule script forms and all (AXONEME 1251, '
      'THELEMA 250, CELL 125 among them)',
      len(sweep) == 11 and not bad, bad or '11/11 agree')

# --- The control case, exhibited at both seats ----------------------------------
posrows = [r for r in cc if r['position'].isdigit()]
agree = [r for r in posrows
         if ARMENIAN[r['armenian_letter']] == int(r['armenian_value'])
         and HALEHAME_FIRST[r['halehame_base']] == int(r['halehame_value'])
         and int(r['armenian_value']) == int(r['halehame_value'])]
check('CONTROL CASE — the shared domain at both engine seats: '
      'Armenian letter == halehame first form at 26/26 positions',
      len(posrows) == 26 and len(agree) == 26,
      '%d/%d agree' % (len(agree), len(posrows)))
check('CONTROL CASE — the boundary coordinate in code: position 10 '
      'weighs 10 at both seats — Ժ (Armenian’s first tens letter) '
      'and ተ (halehame’s tenth units letter)',
      ARMENIAN['Ժ'] == HALEHAME_FIRST['ተ'] == 10
      and next(r for r in posrows if r['position'] == '10')
      ['armenian_class'] == 'tens'
      and next(r for r in posrows if r['position'] == '10')
      ['halehame_class'] == 'units',
      (ARMENIAN['Ժ'], HALEHAME_FIRST['ተ']))
print('COORD — THE CONTROL CASE: on positions 1–26 the two banks '
      'carry one value sequence entire (26/26), reached by laws that '
      'part at position 10 and held at opposite attestation depths — '
      'Armenian complete and liturgical (36/36 letters), halehame '
      'folk and partial (26 first forms of 202 signs). The agreement '
      'is exhibited as a coordinate; no bridge is claimed on it.')

# --- Case and the manuscript door -------------------------------------------------
check('case at the seat: աբգ == ԱԲԳ == 6 (the seam folds to the '
      'majuscule bank)',
      weigh('աբգ', 'armenian')['value']
      == weigh('ԱԲԳ', 'armenian')['value'] == 6,
      (weigh('աբգ', 'armenian')['value'], weigh('ԱԲԳ', 'armenian')['value']))
d = armenian('Ռ' + '\u0305' + 'ՋՀԵ')
check('the manuscript door: armenian() counts the overline (1) and '
      'applies NO factor — overlined ՌՋՀԵ weighs 1975 at face',
      d['value'] == 1975 and d['overline_marks'] == 1
      and d['word'] == 'Ռ' + '\u0305' + 'ՋՀԵ',
      (d['value'], d['overline_marks']))

# --- The fences ---------------------------------------------------------------------
p = SYSTEMS['armenian']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('ATTESTED') and '36' in p and 'halehame' in p
      and 'NOT seated' in p, p)
p = SYSTEMS['halehame']['provenance']
check('the witness’s fence stands unaltered beside the new seat',
      p.startswith('FOLK TABLE') and 'WITNESS' in p
      and 'UNDATED' in p and 'UNEXHIBITED' in p, p)

failed = [r for r in RESULTS if not r[1]]
print()
print('ARMENIAN PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
