#!/usr/bin/env python3
# ===========================================================================
# 93
# THE DIPLOMATIC KEY, EXTENDED AGAIN — PARITY OF THE LATIN FOLD
# GEOMETRY AGAINST THE LIVING ENGINE, THE PRIOR INSTRUMENTS, AND
# THE FROZEN MEASUREMENT
# A Scientific Illuminist proving of the fold module
# (pontifex/pontifex/diplomatic_folds.py): the control word
# weighed first; every pre-existing battery run untouched,
# including both prior instruments' own parities; the fold
# tables re-derived from the frozen bitmap matrices
# (research/latin-folds/) rather than from the module's say-so;
# the fold mechanics restated by direct bitmap surgery; and the
# planted exhibits re-verdicted from the frozen numbers in the
# battery's own hand. Built 2026-11-26 at the founder's question
# — "Can we use it if we dont already?" (10:16 EST) — of the
# fold his sentences of that morning named.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXVI day of November, Dies Iovis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from living seats — the
#   engine's banks for the control, the prior instruments'
#   checkers for the controls, the fold module for the seats,
#   and the frozen CSV matrices (themselves the output of
#   research/latin-folds/measure_latin_folds.py, the module's
#   own apparatus in the house faces) for the geometry.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first; every pre-existing checks battery runs
#   untouched; and the batteries of record — the prior
#   instrument's parity (23 checks) and the turns extension's
#   parity — run as subprocesses, so the fold is proven beside
#   the whole standing house, not beside a corner of it.
#
# DOCTRINE — THE VERDICT RULE, restated so the battery can hold
#   it: a fold claim is CORROBORATED when the claimed letter is
#   the collapsed form's best match at ≥ 0.60; PARTED when it
#   stands best or second below the line; FAILS otherwise —
#   coordinates printed, never smoothed.
# ===========================================================================

import csv
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import weigh, engine_checks
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import diplomatic_checks
from pontifex.diplomatic_turns import diplomatic_turns_checks
from pontifex.diplomatic_folds import (
    ALPHABET, CREASES, FACES, corroborations, diplomatic_folds_checks,
    fold_exhibits, fold_ranking, fold_tables, fold_vertical,
    fold_horizontal,
)

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('doubles', doubles_checks),
                  ('cubes', cubes_checks),
                  ('diplomatic (prior instrument)', diplomatic_checks),
                  ('diplomatic_turns (turns extension)',
                   diplomatic_turns_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs),
          '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))
for script, tail in (('test_diplomatic_parity.py', '23/23'),
                     ('test_diplomatic_turns_parity.py', 'checks PASS')):
    sub = subprocess.run([sys.executable, str(HERE / script)],
                         cwd=str(HERE), capture_output=True, text=True)
    last = sub.stdout.strip().splitlines()[-1] \
        if sub.stdout.strip() else sub.returncode
    check('control — the %s battery still passes (%s)' % (script, tail),
          sub.returncode == 0 and tail in str(last), last)

# --- The seat battery ---------------------------------------------------------
cs = diplomatic_folds_checks()
check('seat battery — diplomatic_folds_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))

# --- The mechanics, restated by direct bitmap surgery -------------------------
# MECHANISM: the battery folds with its own hands — a synthetic
# bitmap whose ink sits at known coordinates, folded by the
# module's operations and read at the mirror coordinates the
# crease geometry dictates (column 300 → 99 across column 200;
# row 300 → 99 across row 200).
probe = np.zeros((400, 400), dtype=bool)
probe[10, 300] = True
probe[10, 50] = True
fv = fold_vertical(probe)
probe2 = np.zeros((400, 400), dtype=bool)
probe2[300, 10] = True
fh = fold_horizontal(probe2)
check('mechanics restated: fold_vertical mirrors column 300 to '
      '99 across the crease at 200 and keeps column 50 standing; '
      'fold_horizontal mirrors row 300 to 99; extents halve',
      fv.shape == (400, 200) and fh.shape == (200, 400)
      and fv[10, 99] and fv[10, 50] and int(fv.sum()) == 2
      and fh[99, 10] and int(fh.sum()) == 1
      and CREASES == {'vertical': ('column', 200),
                      'horizontal': ('row', 200)},
      (fv.shape, fh.shape, CREASES))

# --- The geometry, re-derived from the frozen measurement ---------------------
FROZEN = HERE / 'research' / 'latin-folds'


def _matrix(face, axis):
    rows = list(csv.reader(
        (FROZEN / ('latin_%s_fold_%s_matrix.csv'
                   % (face.lower(), axis))).open(encoding='utf-8')))
    head = rows[0][1:]
    return {r[0]: {h: float(v) for h, v in zip(head, r[1:])}
            for r in rows[1:]}


frozen = {(face, axis): _matrix(face, axis)
          for face in FACES for axis in ('vertical', 'horizontal')}
live = fold_tables()
check('geometry re-derived: the frozen matrices equal the '
      'living tables cell for cell (4 matrices × 26 × 26, at '
      'the frozen 4-decimal precision)',
      all(round(live[(f, a)][c][t], 4) == frozen[(f, a)][c][t]
          for (f, a) in frozen for c in ALPHABET for t in ALPHABET),
      {str(k): (len(v), len(v['A'])) for k, v in frozen.items()})


def _best(mat, ch):
    return max(mat[ch].items(), key=lambda kv: kv[1])


check('geometry re-derived: the vertical register\'s seats '
      'from the frozen numbers — Serif corroborations exactly '
      'B/E/F/L/P → I (0.614/0.760/0.808/0.851/0.736), Sans '
      'exactly J → I (0.690); horizontal seats none, peak 0.467',
      {c: round(_best(frozen[('Serif', 'vertical')], c)[1], 3)
       for c in 'BEFLP'}
      == {'B': 0.614, 'E': 0.760, 'F': 0.808, 'L': 0.851,
          'P': 0.736}
      and all(_best(frozen[('Serif', 'vertical')], c)[0] == 'I'
              for c in 'BEFLP')
      and _best(frozen[('Sans', 'vertical')], 'J')[0] == 'I'
      and round(_best(frozen[('Sans', 'vertical')], 'J')[1], 3)
      == 0.690
      and all(max(row.values()) < 0.60
              for mat in (frozen[(f, 'horizontal')] for f in FACES)
              for row in mat.values())
      and round(max(s for f in FACES
                    for row in frozen[(f, 'horizontal')].values()
                    for s in row.values()), 3) == 0.467,
      ({c: _best(frozen[('Serif', 'vertical')], c) for c in 'BEFLP'},
       _best(frozen[('Sans', 'vertical')], 'J')))

# --- The planted exhibits, re-verdicted from the frozen numbers ---------------
ex = fold_exhibits()
serif_v = sorted(frozen[('Serif', 'vertical')]['H'].items(),
                 key=lambda kv: -kv[1])
sans_v = sorted(frozen[('Sans', 'vertical')]['H'].items(),
                key=lambda kv: -kv[1])
check('Exhibit E1 re-verdicted from the frozen numbers: Serif '
      'fold(H) → T 0.396 at rank 2 behind I 0.478 (PARTED); '
      'Sans fold(H) → T 0.151 at rank 9, best F 0.282 (FAILS); '
      'the module\'s verdicts agree',
      round(dict(serif_v)['T'], 3) == 0.396
      and [t for t, _ in serif_v].index('T') == 1
      and serif_v[0][0] == 'I' and round(serif_v[0][1], 3) == 0.478
      and round(dict(sans_v)['T'], 3) == 0.151
      and [t for t, _ in sans_v].index('T') == 8
      and sans_v[0][0] == 'F' and round(sans_v[0][1], 3) == 0.282
      and ex['Serif']['E1']['verdict'] == 'PARTED'
      and ex['Sans']['E1']['verdict'] == 'FAILS',
      (serif_v[:3], sans_v[:3]))
check('Exhibits E2/E3 re-verdicted from the frozen numbers: '
      'fold_vertical(H) vs H 0.094/0.095 (FAILS, both faces); '
      'fold_horizontal(H) best H 0.296 in Serif, U 0.391 in '
      'Sans — NO CORROBORATION in either',
      round(frozen[('Serif', 'vertical')]['H']['H'], 3) == 0.094
      and round(frozen[('Sans', 'vertical')]['H']['H'], 3) == 0.095
      and _best(frozen[('Serif', 'horizontal')], 'H')[0] == 'H'
      and round(_best(frozen[('Serif', 'horizontal')], 'H')[1], 3)
      == 0.296
      and _best(frozen[('Sans', 'horizontal')], 'H')[0] == 'U'
      and abs(_best(frozen[('Sans', 'horizontal')], 'H')[1]
              - 0.391) <= 0.001
      and ex['Serif']['E2']['verdict'] == 'FAILS'
      and ex['Sans']['E2']['verdict'] == 'FAILS'
      and ex['Serif']['E3']['verdict'] == 'NO CORROBORATION'
      and ex['Sans']['E3']['verdict'] == 'NO CORROBORATION',
      (_best(frozen[('Serif', 'horizontal')], 'H'),
       _best(frozen[('Sans', 'horizontal')], 'H')))
check('the bar coordinate from the module\'s exhibits: H\'s '
      'bar at 0.42 (Serif) / 0.41 (Sans) of height, the folded '
      'H\'s bar unmoved, T\'s at 0.00 — the fold performs no '
      'twist, and the instrument says so in numbers',
      round(ex['Serif']['bar']['fold_vertical(H)'], 2) == 0.42
      and round(ex['Sans']['bar']['fold_vertical(H)'], 2) == 0.41
      and ex['Serif']['bar']['T'] == 0.0
      and ex['Sans']['bar']['T'] == 0.0,
      {f: ex[f]['bar'] for f in FACES})

# --- The register, held whole ---------------------------------------------------
check('the register stands whole: every letter folded on both '
      'axes in both faces has a printed best match, and the '
      'corroboration sets are exactly the seated ones',
      all(fold_ranking(f, a, c) for f in FACES
          for a in ('vertical', 'horizontal') for c in ALPHABET)
      and sorted(corroborations('Serif', 'vertical'))
      == [('B', 'I'), ('E', 'I'), ('F', 'I'), ('L', 'I'),
          ('P', 'I')]
      and sorted(corroborations('Sans', 'vertical')) == [('J', 'I')]
      and corroborations('Serif', 'horizontal') == {}
      and corroborations('Sans', 'horizontal') == {},
      {str((f, a)): sorted(corroborations(f, a))
       for f in FACES for a in ('vertical', 'horizontal')})

print()
failed = [n for n, p, _ in RESULTS if not p]
print('DIPLOMATIC FOLDS PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         ('; FAILING: ' + '; '.join(failed)) if failed else ''))
sys.exit(1 if failed else 0)
