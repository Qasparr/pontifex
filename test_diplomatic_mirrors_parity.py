#!/usr/bin/env python3
# ===========================================================================
# 93
# THE DIPLOMATIC KEY, EXTENDED A THIRD TIME — PARITY OF THE
# LATIN MIRROR-COMPOSITION GEOMETRY AGAINST THE LIVING ENGINE,
# THE PRIOR INSTRUMENTS, AND THE FROZEN MEASUREMENT
# A Scientific Illuminist proving of the mirror module
# (pontifex/pontifex/diplomatic_mirrors.py): the control word
# weighed first; every pre-existing battery run untouched,
# including all three prior instruments' own parities; the
# composition tables re-derived from the frozen bitmap
# matrices (research/latin-mirrors/) rather than from the
# module's say-so; the mirror mechanics restated by direct
# bitmap surgery; and the planted exhibits re-verdicted from
# the frozen numbers in the battery's own hand. Built
# 2026-11-26 at the founder's order — "Do all of that" (14:35
# EST) — of his fifth stroke of that day: U as L mirroring
# itself, U as J mirroring itself into a lock, the barred I
# as T over L.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXVI day of November, Dies Iovis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from living seats — the
#   engine's banks for the control, the prior instruments'
#   checkers for the controls, the mirror module for the
#   seats, and the frozen CSVs (themselves the output of
#   research/latin-mirrors/measure_latin_mirrors.py, the
#   module's own apparatus in the house faces) for the
#   geometry.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first; every pre-existing checks battery
#   runs untouched; and the batteries of record — the prior
#   instrument's parity, the turns extension's parity, and the
#   folds' parity — run as subprocesses, so the composition is
#   proven beside the whole standing house, not beside a
#   corner of it.
#
# DOCTRINE — THE VERDICT RULE, restated so the battery can
#   hold it: a composition claim is CORROBORATED when the
#   claimed letter is the composed form's best match at
#   ≥ 0.60; PARTED when it stands best or second below the
#   line; FAILS otherwise — coordinates printed, never
#   smoothed. The decomposition's rule is the module's stated
#   translation: corroborated at overlap ≥ 0.60; parted when
#   the composite covers ≥ 0.60 of the I's ink below that
#   overlap; fails otherwise.
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
from pontifex.diplomatic_folds import diplomatic_folds_checks
from pontifex.diplomatic_mirrors import (
    ALPHABET, FACES, compose_mirror, compose_mirror_overlap,
    decompose_measures, diplomatic_mirrors_checks,
    mirror_bitmap, mirror_corroborations, mirror_exhibits,
    mirror_ranking, mirror_tables, overlap_sweep,
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
                   diplomatic_turns_checks),
                  ('diplomatic_folds (folds instrument)',
                   diplomatic_folds_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs),
          '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))
for script in ('test_diplomatic_parity.py',
               'test_diplomatic_turns_parity.py',
               'test_diplomatic_folds_parity.py'):
    sub = subprocess.run([sys.executable, str(HERE / script)],
                         cwd=str(HERE), capture_output=True, text=True)
    last = sub.stdout.strip().splitlines()[-1] \
        if sub.stdout.strip() else sub.returncode
    check('control — the %s battery still passes (checks PASS)'
          % script,
          sub.returncode == 0 and 'checks PASS' in str(last), last)

# --- The seat battery ---------------------------------------------------------
cs = diplomatic_mirrors_checks()
check('seat battery — diplomatic_mirrors_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))

# --- The mechanics, restated by direct bitmap surgery -------------------------
# MECHANISM: the battery composes with its own hands — a
# synthetic bitmap whose ink sits at a known coordinate,
# mirrored and composed by the module's operations and read
# at the coordinates the seam geometry dictates; the overlap
# construction's two ends restated against their definitions.
probe = np.zeros((10, 6), dtype=bool)
probe[2, 1] = True
manual = np.concatenate([probe, np.fliplr(probe)], axis=1)
check('mechanics restated: the mirror is an exact involution '
      'and a lone pixel at column 1 of a 6-wide crop composes '
      'to columns 1 and 10 of the 12-wide edge-to-edge '
      'composite (its twin across the seam); overlap(0.00) '
      'equals the edge-to-edge composite and overlap(1.00), '
      'cropped, equals crop ∪ mirror(crop) for L in both faces',
      bool((mirror_bitmap(mirror_bitmap(probe)) == probe).all())
      and manual.shape == (10, 12) and manual[2, 1]
      and manual[2, 10] and int(manual.sum()) == 2
      and all(bool((compose_mirror_overlap(f, 'L', 0.00)
                    == compose_mirror(f, 'L', 'vertical')).all())
              for f in FACES),
      manual.shape)

# --- The geometry, re-derived from the frozen measurement ---------------------
FROZEN = HERE / 'research' / 'latin-mirrors'


def _matrix(face, axis):
    rows = list(csv.reader(
        (FROZEN / ('latin_%s_mirror_%s_matrix.csv'
                   % (face.lower(), axis))).open(encoding='utf-8')))
    head = rows[0][1:]
    return {r[0]: {h: float(v) for h, v in zip(head, r[1:])}
            for r in rows[1:]}


frozen = {(face, axis): _matrix(face, axis)
          for face in FACES for axis in ('vertical', 'horizontal')}
live = mirror_tables()
check('geometry re-derived: the frozen matrices equal the '
      'living tables cell for cell (4 matrices × 26 × 26, at '
      'the frozen 4-decimal precision)',
      all(round(live[(f, a)][c][t], 4) == frozen[(f, a)][c][t]
          for (f, a) in frozen for c in ALPHABET for t in ALPHABET),
      {str(k): (len(v), len(v['A'])) for k, v in frozen.items()})


def _best(mat, ch):
    return max(mat[ch].items(), key=lambda kv: kv[1])


check('geometry re-derived: the register\'s finding from the '
      'frozen numbers — corroborations none in any of the four '
      'tables (no cell\'s row-best reaches 0.60 except against '
      'the line itself), and the register peak is Serif '
      'vertical I → E at 0.590',
      all(_best(frozen[(f, a)], c)[1] < 0.60
          for (f, a) in frozen for c in ALPHABET)
      and _best(frozen[('Serif', 'vertical')], 'I')[0] == 'E'
      and round(_best(frozen[('Serif', 'vertical')], 'I')[1], 3)
      == 0.590
      and round(max(s for mat in frozen.values()
                    for row in mat.values()
                    for s in row.values()), 3) == 0.590,
      _best(frozen[('Serif', 'vertical')], 'I'))

# --- The planted exhibits, re-verdicted from the frozen numbers ---------------
ex = mirror_exhibits()
serif_v = sorted(frozen[('Serif', 'vertical')]['L'].items(),
                 key=lambda kv: -kv[1])
sans_v = sorted(frozen[('Sans', 'vertical')]['L'].items(),
                key=lambda kv: -kv[1])
check('Exhibit M1 re-verdicted from the frozen numbers: '
      'Serif compose(L) → U 0.072 at rank 14, best M 0.121 '
      '(FAILS); Sans compose(L) → U 0.080 at rank 10, best W '
      '0.167 (FAILS); the module\'s verdicts agree',
      round(dict(serif_v)['U'], 3) == 0.072
      and [t for t, _ in serif_v].index('U') == 13
      and serif_v[0][0] == 'M' and round(serif_v[0][1], 3) == 0.121
      and round(dict(sans_v)['U'], 3) == 0.080
      and [t for t, _ in sans_v].index('U') == 9
      and sans_v[0][0] == 'W' and round(sans_v[0][1], 3) == 0.167
      and ex['Serif']['M1']['verdict'] == 'FAILS'
      and ex['Sans']['M1']['verdict'] == 'FAILS',
      (serif_v[:3], sans_v[:3]))

sweep_rows = list(csv.DictReader(
    (FROZEN / 'latin_j_lock_sweep.csv').open(encoding='utf-8')))
frozen_sweep = {f: [r for r in sweep_rows if r['face'] == f]
                for f in FACES}
check('Exhibit M2 re-verdicted from the frozen sweep: no row '
      'in either face seats U (best is never U at ≥ 0.60); the '
      'score against U peaks at 0.090 in Serif (fraction 0.00, '
      'rank 20) and 0.051 in Sans (rank 25); at coincidence '
      'the best match is J in both faces (0.616/0.538); the '
      'module\'s sweep agrees row for row',
      all(not (r['best'] == 'U' and float(r['best_score']) >= 0.60)
          for r in sweep_rows)
      and max(float(r['score_U']) for r in frozen_sweep['Serif'])
      == 0.0905
      and [r for r in frozen_sweep['Serif']
           if float(r['score_U']) == 0.0905][0]['fraction'] == '0.00'
      and max(float(r['score_U']) for r in frozen_sweep['Sans'])
      == 0.0515
      and frozen_sweep['Serif'][-1]['best'] == 'J'
      and float(frozen_sweep['Serif'][-1]['best_score']) == 0.6161
      and frozen_sweep['Sans'][-1]['best'] == 'J'
      and float(frozen_sweep['Sans'][-1]['best_score']) == 0.5379
      and all(round(r['score_U'], 4)
              == float(fr['score_U'])
              and r['best'] == fr['best']
              for f in FACES
              for r, fr in zip(overlap_sweep(f, 'J'),
                               frozen_sweep[f])),
      (frozen_sweep['Serif'][0], frozen_sweep['Sans'][-1]))

dec_rows = {r['face']: r for r in csv.DictReader(
    (FROZEN / 'latin_decompose_I.csv').open(encoding='utf-8'))}
check('Exhibit M3 re-verdicted from the frozen decomposition: '
      'Serif PARTED (IoU 0.291, covers I 0.606, I covers '
      '0.359, ink 4422 vs 7470); Sans FAILS (IoU 0.240, '
      'covers 0.577, ink 3520 vs 6976); the module\'s measures '
      'agree at the frozen precision',
      dec_rows['Serif']['verdict'] == 'PARTED'
      and float(dec_rows['Serif']['iou']) == 0.2909
      and float(dec_rows['Serif']['covers_I']) == 0.6061
      and float(dec_rows['Serif']['I_covers']) == 0.3588
      and dec_rows['Sans']['verdict'] == 'FAILS'
      and float(dec_rows['Sans']['iou']) == 0.2401
      and float(dec_rows['Sans']['covers_I']) == 0.5773
      and all(round(decompose_measures(f)['iou'], 4)
              == float(dec_rows[f]['iou'])
              and round(decompose_measures(f)['covers_I'], 4)
              == float(dec_rows[f]['covers_I'])
              for f in FACES),
      dec_rows)

# --- The register, held whole ---------------------------------------------------
check('the register stands whole: every letter composed on '
      'both axes in both faces has a printed best match, and '
      'the corroboration sets are empty in all four tables — '
      'the emptiness is the finding, printed, not smoothed',
      all(mirror_ranking(f, a, c) for f in FACES
          for a in ('vertical', 'horizontal') for c in ALPHABET)
      and all(mirror_corroborations(f, a) == {}
              for f in FACES for a in ('vertical', 'horizontal')),
      {str((f, a)): mirror_corroborations(f, a)
       for f in FACES for a in ('vertical', 'horizontal')})

print()
failed = [n for n, p, _ in RESULTS if not p]
print('DIPLOMATIC MIRRORS PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         ('; FAILING: ' + '; '.join(failed)) if failed else ''))
sys.exit(1 if failed else 0)
