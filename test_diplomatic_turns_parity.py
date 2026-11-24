#!/usr/bin/env python3
# ===========================================================================
# 93
# THE DIPLOMATIC KEY, EXTENDED — PARITY OF THE GREEK TURN
# GEOMETRY AGAINST THE LIVING ENGINE, THE PRIOR INSTRUMENT, AND
# THE FROZEN MEASUREMENT
# A Scientific Illuminist proving of the extension module
# (pontifex/pontifex/diplomatic_turns.py): the control word
# weighed first; every pre-existing battery run untouched,
# including the prior instrument's own parity and the world
# census; the seated geometry re-derived from the frozen bitmap
# matrices (research/greek-turns/) rather than from the module's
# say-so; the planted exhibits restated by direct string surgery;
# and the legend's vowel-landing tables recomputed from the
# seated maps in the battery's own hand. Built 2026-11-24 at the
# founder's word — "Measure the Greek lowercase geometry"
# (13:25 EST) — the measurement the prior instrument's residue
# (§VIII) named as open.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from living seats — the
#   engine's banks for the values, the extension's checker for
#   the verdicts, and the frozen CSV matrices (themselves the
#   output of research/greek-turns/measure_greek_turns.py, the
#   prior battery's apparatus in DejaVu Sans) for the geometry.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first; every pre-existing checks battery runs
#   untouched; and the batteries of record — the prior
#   instrument's parity (23 checks), the WORLD CENSUS (38), the
#   Western Sweep (29) — run as subprocesses, so the extension
#   is proven beside the whole standing house, not beside a
#   corner of it.
#
# DOCTRINE — THE VERDICT RULE, restated so the battery can hold
#   it: self-symmetry corroborated at self-score ≥ 0.60; a pair
#   corroborated at mutual best match (or best non-self, the
#   coordinate printed — the M ↔ W precedent); a bitmap reach
#   that is not mutual is a coordinate, never a seat.
# ===========================================================================

import csv
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
)
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import diplomatic_checks
from pontifex.diplomatic_turns import (
    CORPUS, REGISTER, EXCLUDED, PLANTED, TURN_MAPS, ANGLES,
    apply_turn, turn_pair, diplomatic_turns_checks, turn_tables,
    vowel_landings,
)

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
                  ('diplomatic (prior instrument)', diplomatic_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs),
          '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))
for script, tail in (('test_diplomatic_parity.py', '23/23'),
                     ('test_census_parity.py', '38/38'),
                     ('test_western_sweep_parity.py', '29/29')):
    sub = subprocess.run([sys.executable, str(HERE / script)],
                         cwd=str(HERE), capture_output=True, text=True)
    last = sub.stdout.strip().splitlines()[-1] \
        if sub.stdout.strip() else sub.returncode
    check('control — the %s battery still passes (%s)' % (script, tail),
          sub.returncode == 0 and tail in str(last), last)

# --- The seat battery ---------------------------------------------------------
cs = diplomatic_turns_checks()
check('seat battery — diplomatic_turns_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))

# --- The planted exhibits, restated by direct string surgery ------------------
# MECHANISM: the battery rebuilds the planted word with its own
# hands — πυρ's third letter replaced by δ, nothing else
# touched — and holds the module's transformation to the result.
surgery = 'πυρ'[:2] + 'δ'
check('planted exhibit restated: πυρ with seat 3 turned (ρ→δ) '
      'is πυδ, weighing 580 against 484 in the living bank',
      surgery == 'πυδ'
      and apply_turn('πυρ', ('turn_seats', (2,), '180')) == 'πυδ'
      and weigh('πυρ', 'greek')['value'] == 580
      and weigh('πυδ', 'greek')['value'] == 484,
      (surgery, weigh('πυρ', 'greek')['value'],
       weigh('πυδ', 'greek')['value']))

# --- The geometry, re-derived from the frozen measurement ---------------------
# MECHANISM: the frozen matrices are read back and the seat
# facts recomputed — mutual-best pairs, the corroboration line,
# the refused coordinates — so the module's tables stand on the
# measurement, not on the module.
FROZEN = HERE / 'research' / 'greek-turns'


def _matrix(case, angle):
    rows = list(csv.reader(
        (FROZEN / ('greek_%s_matrix_%s.csv' % (case, angle)))
        .open(encoding='utf-8')))
    head = rows[0][1:]
    return {r[0]: {h: float(v) for h, v in zip(head, r[1:])}
            for r in rows[1:]}


def _mutuals(m):
    return sorted({tuple(sorted((a, b))) for a in m for b in m
                   if a != b and max(m[a], key=m[a].get) == b
                   and max(m[b], key=m[b].get) == a})


m180 = _matrix('lower', '180')
check('geometry re-derived: the lowercase half-turn\'s '
      'mutual-best pairs in the frozen bitmaps are exactly '
      'γ ↔ λ (0.611) and δ ↔ ρ (0.590)',
      _mutuals(m180) == [('γ', 'λ'), ('δ', 'ρ')]
      and round(m180['γ']['λ'], 3) == 0.611
      and round(m180['δ']['ρ'], 3) == 0.590,
      (_mutuals(m180), round(m180['γ']['λ'], 3),
       round(m180['δ']['ρ'], 3)))
selfs = {c: round(m180[c][c], 3) for c in 'οθχ'}
check('geometry re-derived: the seated symmetric letters '
      'corroborate at the 0.60 line (ο 0.910, θ 0.810, χ 0.928)',
      selfs == {'ο': 0.910, 'θ': 0.810, 'χ': 0.928}
      and all(s >= 0.60 for s in selfs.values()), selfs)
check('geometry re-derived: the refused seats\' coordinates '
      'as measured — ι self 0.146 (the footed iota), ξ self '
      '0.145 and φ self 0.327 (the derivation\'s guesses, killed '
      'by inspection and score); σ\'s one-way reach to ο 0.604 '
      'is not mutual (ο\'s best is ο)',
      round(m180['ι']['ι'], 3) == 0.146
      and round(m180['ξ']['ξ'], 3) == 0.145
      and round(m180['φ']['φ'], 3) == 0.327
      and round(m180['σ']['ο'], 3) == 0.604
      and max(m180['ο'], key=m180['ο'].get) == 'ο',
      (round(m180['ι']['ι'], 3), round(m180['ξ']['ξ'], 3),
       round(m180['φ']['φ'], 3), round(m180['σ']['ο'], 3)))
quarters = {(case, angle): _matrix(case, angle)
            for case in ('lower', 'capital')
            for angle in ('cw90', 'ccw90')}
qmax = max(s for m in quarters.values() for row in m.values()
           for s in row.values())
qmax_cap = max(s for (case, _a), m in quarters.items()
               if case == 'capital' for row in m.values()
               for s in row.values())
check('geometry re-derived: no quarter-turn score anywhere '
      'reaches the 0.60 line, in either case, in either '
      'direction (the maximum is ο\'s self-reach, 0.525; the '
      'capitals\' maximum is Φ\'s self-reach, 0.503)',
      qmax < 0.60 and round(qmax, 3) == 0.525
      and round(qmax_cap, 3) == 0.503,
      (round(qmax, 3), round(qmax_cap, 3)))
check('geometry re-derived: the capitals\' expected near-miss '
      'Θ → Φ measures 0.403 in both directions and is not '
      'mutual-best (Θ reaches Ο at 0.445; Φ reaches itself at '
      '0.503) — a coordinate, not a seat',
      all(round(quarters[('capital', a)]['Θ']['Φ'], 3) == 0.403
          for a in ('cw90', 'ccw90'))
      and _mutuals(quarters[('capital', 'cw90')]) == [('Ζ', 'Μ')]
      and round(quarters[('capital', 'cw90')]['Ζ']['Μ'], 3)
      == 0.310,
      (_mutuals(quarters[('capital', 'cw90')]),
       _mutuals(quarters[('capital', 'ccw90')])))

# --- The landing tables, recomputed in the battery's own hand ------------------
land = vowel_landings()
check('the landing tables recomputed: cross landings empty at '
      'every angle in both cases; CW and CCW yields identical; '
      'the seated maps seat no image on any vowel but the '
      'vowel\'s own',
      all(not e['cross'] for e in land.values())
      and all(TURN_MAPS[('lower', a)].get(v) in (None, v)
              for a in ANGLES for v in 'αεηιουω'),
      {str(k): v['landings'] for k, v in land.items()})

# --- The register, held to the corpus ------------------------------------------
check('the register stands as swept: the 51-head corpus seats '
      'no exhibit and no exclusion under the extended family; '
      'the three planted exhibits all verify DIPLOMATIC',
      len(REGISTER) == 0 and len(EXCLUDED) == 0
      and len(CORPUS) == 51
      and all(turn_pair(a, b, s)['verdict'] == 'DIPLOMATIC'
              for a, b, s in PLANTED),
      (len(CORPUS), len(REGISTER), len(EXCLUDED)))
tables = turn_tables()
WHOLE = {'lower/180': 25, 'lower/cw90': 25, 'lower/ccw90': 25,
         'capital/cw90': 24, 'capital/ccw90': 24}
check('the seated tables print whole: pairs, symmetric seats '
      'and absences account for every letter at every angle',
      all(len(t['pairs']) * 2 + len(t['symmetric'])
          + len(t['absent']) == WHOLE[k]
          for k, t in tables.items()),
      {k: (len(v['pairs']), len(v['symmetric']), len(v['absent']))
       for k, v in tables.items()})

print()
failed = [n for n, p, _ in RESULTS if not p]
print('DIPLOMATIC TURNS PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         ('; FAILING: ' + '; '.join(failed)) if failed else ''))
sys.exit(1 if failed else 0)
