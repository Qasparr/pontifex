#!/usr/bin/env python3
# ============================================================================
# 93
# THE GLAGOLITIC TABLE — PARITY OF THE ENGINE SEAT AGAINST THE PHASE
# II AUDIT'S FROZEN TRANSCRIPTION
# A Scientific Illuminist proving of the Glagolitic bank in the main
# engine (pontifex/pontifex) against the independent seat the Phase
# II audit built from the sources (research/caucasus-north:
# glagolitic-table.csv and slavonic-parting.csv, transcribed from
# Wikipedia, "Glagolitic numerals", read entire, and diffed on the
# 20 cells the second witness — languagesandnumbers, "Old Church
# Slavonic numbers" — prints in text).
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from the two living seats — the
#   engine's bank (a literal dict in tables.py, keyed in capitals)
#   and the audit's CSVs. The order law is recomputed from the
#   block seats frozen in the CSV, never from the dict's shape.
#
# DOCTRINE — THE CONTROLS: as the pair's other battery — the
#   control word first, every pre-existing battery untouched, the
#   Phase II audit battery as a subprocess.
#
# DOCTRINE — THE PARTING, EXHIBITED: the founder ordered the pair
#   read against each other — the region's control case proper.
#   The exhibit below holds the frozen parting table at BOTH engine
#   seats: 33 sound rows, 15 AGREE, 18 PART, the agreement band and
#   the sharpest coordinates recomputed from the living banks.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pontifex.engine import (
    weigh, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
    hangul_checks, georgian_checks, cyrillic_checks,
    glagolitic_checks,
)
from pontifex.tables import GLAGOLITIC, CYRILLIC
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
                  ('cyrillic', cyrillic_checks),
                  ('diplomatic', diplomatic_checks),
                  ('chinese', chinese_checks), ('triad', triad_checks),
                  ('katapayadi', katapayadi_checks),
                  ('aryabhatiya', aryabhatiya_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = glagolitic_checks()
check('seat battery — glagolitic_checks() passes',
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
with open(AUDIT_DIR / 'glagolitic-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'slavonic-parting.csv', encoding='utf-8') as fh:
    part = list(csv.DictReader(fh))
SOURCED = [r for r in rows if r['status'] == 'SOURCED']
HOLES = [r for r in rows if r['status'] == 'HOLE']
check('the frozen transcription stands in the data seat: 34 '
      'SOURCED letters, 3 HOLE rows, the refused material refused',
      (len(SOURCED), len(HOLES)) == (34, 3)
      and sum(1 for r in rows if r['status'].startswith('REFUSED'))
      == 5,
      (len(SOURCED), len(HOLES)))
check('bank identity — engine GLAGOLITIC == the audit’s 34 '
      'SOURCED rows, key for key, value for value',
      GLAGOLITIC == {r['letter']: int(r['value']) for r in SOURCED},
      (len(GLAGOLITIC), len(SOURCED)))
bad = [(r['letter'], unicodedata.name(r['letter'], ''),
        r['unicode_name']) for r in SOURCED + HOLES
       if unicodedata.name(r['letter'], '') != r['unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata',
      not bad, bad or '37/37 verified')
check('the boundary in the data is the boundary at the seat: the '
      'HOLE letters (Ⱊ Ⱐ Ⱒ) weigh silence, and the questioned '
      'range stands flagged in the frozen data at every seat '
      '>= 1000',
      all(weigh(r['letter'], 'glagolitic')['breakdown'] == []
          for r in HOLES)
      and all(r['range_flag'] for r in SOURCED
              if int(r['value']) >= 1000),
      [r['letter'] for r in HOLES])

# --- The order law at the seat --------------------------------------------------
valued = sorted(SOURCED, key=lambda r: int(r['block_seat']))
breaks, idx = [], {}
for r in valued:
    v = int(r['value'])
    p = 0 if v < 10 else 1 if v < 100 else 2 if v < 1000 else 3
    idx[p] = idx.get(p, 0) + 1
    if v // (10 ** p) != idx[p]:
        breaks.append(r['letter'])
check('the order law at the engine seat, recomputed from the '
      'audit’s block seats: the digit law parts at exactly the '
      'ten frozen letters',
      breaks == ['Ⰺ', 'Ⰻ', 'Ⰼ', 'Ⰽ', 'Ⰾ', 'Ⰿ', 'Ⱀ', 'Ⱁ', 'Ⱂ', 'Ⱔ']
      and all(GLAGOLITIC[r['letter']] == int(r['value'])
              for r in valued), breaks)

# --- The witnesses' numbers at the engine's doors ------------------------------
ex = (weigh('ⰗⰑⰂ', 'glagolitic')['value'],
      weigh('ⰅⰊ', 'glagolitic')['value'],
      weigh('ⰝⰔⰑ', 'glagolitic')['value'])
check('calibration at the seat: ⰗⰑⰂ 583, ⰅⰊ 16, the Vinodol '
      'ⰝⰔⰑ 1280', ex == (583, 16, 1280), ex)
check('the system’s arithmetic at the seat: 34 letters, 33 '
      'distinct values, sum 29005',
      len(GLAGOLITIC) == 34
      and len(set(GLAGOLITIC.values())) == 33
      and sum(GLAGOLITIC.values()) == 29005,
      sum(GLAGOLITIC.values()))

# --- The parting, exhibited at both seats ---------------------------------------
agree = [r for r in part if r['relation'] == 'AGREE']
check('THE PARTING at both engine seats: the frozen table’s 33 '
      'sound rows recompute from the living banks — 15 AGREE, '
      '18 PART, no third numbers',
      len(part) == 33 and len(agree) == 15
      and all((not r['cyrillic_value']
               or CYRILLIC.get(r['cyrillic_letter'])
               == int(r['cyrillic_value']))
              and (not r['glagolitic_value']
                   or GLAGOLITIC.get(r['glagolitic_letter'])
                   == int(r['glagolitic_value'])) for r in part),
      (len(part), len(agree)))
check('THE PARTING — the sharpest coordinates at the seats: /ch/ '
      'Ч 90 against Ⱍ 1000; omega Ѡ 800 against Ⱉ 700; the small '
      'yus Ѧ 900 against Ⱔ 9000',
      (CYRILLIC['Ч'], GLAGOLITIC['Ⱍ'], CYRILLIC['Ѡ'],
       GLAGOLITIC['Ⱉ'], CYRILLIC['Ѧ'], GLAGOLITIC['Ⱔ'])
      == (90, 1000, 800, 700, 900, 9000),
      (CYRILLIC['Ч'], GLAGOLITIC['Ⱍ']))
print('COORD — THE PARTING: the two laws agree at /a/, at '
      'iota-/i/, and across the whole middle band of sounds '
      '(/k/–/ts/: 20, 30, 40, 50, 70, 80, 100, 200, 300, 400, 500, '
      '600, 900), because from /k/ onward Glagolitic’s own order '
      'tracks the Greek-shaped sequence of sounds its sibling '
      'inherited. They part at every units seat but /a/ (the head: '
      'two alphabet orders pricing the same first sounds '
      'differently), at the omega seat inside the hundreds (800 '
      'against 700), and at the tail, where Glagolitic’s extra '
      'letters take thousands seats or none (/ch/: a tens letter '
      'at 90 in the inherited law, a thousands letter at 1000 in '
      'the order law). Printed as coordinates; the comparison is '
      'of two laws over shared sounds, not a bridge.')

# --- The fences ---------------------------------------------------------------------
p = SYSTEMS['glagolitic']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('ATTESTED') and '34' in p
      and 'QUESTIONED' in p and 'HOLE' in p, p[:60])
p = SYSTEMS['cyrillic']['provenance']
check('the sibling’s fence stands unaltered beside the new seat',
      p.startswith('DERIVED') and '27' in p, p[:60])

failed = [r for r in RESULTS if not r[1]]
print()
print('GLAGOLITIC PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
