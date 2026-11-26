#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — research/latin-mirrors/measure_latin_mirrors.py
# The bitmap measurement of the Latin mirror-composition
# geometry: every Latin capital, in the house's two text faces
# (Lex Stellarrvm Serif and Sans), composed with its own mirror
# image edge-to-edge by pontifex/diplomatic_mirrors.py, the
# composed form scored against every capital of its face by ink
# overlap; the J lock sweep at every overlap twentieth; and the
# barred I's decomposition as T over L. The frozen CSVs this
# builder writes are the measurement the mirror instrument
# stands on — the latin-folds builder's office, for the new
# operation.
#
# Epigraph: "U is L mirroring itself horizontally and U is
# also J mirroring itself but with them overlapping slightly
# forming a 'lock.'" — the founder, 2026-11-26.
#
# Thelemic date: XXVI day of November, Dies Iovis, Sol in
# Sagittario, Anno V:xii e.n. (2026 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: as stated in the instrument
#     (pontifex/diplomatic_mirrors.py): the planted exhibits —
#     U as L mirroring itself, U as J mirroring itself with a
#     slight overlap, the barred I as T over L — would
#     corroborate under the family's verdict rule or part at
#     printed coordinates; the killing evidence was stated
#     before the run.
#   Method: the instrument's own apparatus and operations,
#     imported, not re-implemented — the folds' 220pt render,
#     bounding-box centring, ink at grey 96, ink overlap;
#     compositions edge-to-edge; the lock sweep in twentieths
#     from edge-to-edge to box-coincidence; scores taken on
#     the framed canvas (centred, never rescaled), which the
#     instrument's checker proves identical to the folds' road
#     wherever the folds' canvas holds the form.
#   Observation: printed by this builder to the frozen CSVs;
#     the instrument quotes them, and the parity battery
#     re-derives its tables from them. Headline: M1 FAILS in
#     both faces (U 14th at 0.072 in Serif, 10th at 0.080 in
#     Sans); M2 finds no lock (the sweep against U peaks at
#     0.090 / 0.051, U never the best match at any offset);
#     M3 PARTS in Serif (covers 0.606 of the I's ink, overlap
#     0.291) and FAILS in Sans (0.577); the composition
#     register corroborates nothing (peak: Serif's doubled
#     barred I → E at 0.590).
#   Result: latin_{serif,sans}_mirror_{vertical,horizontal}_
#     matrix.csv (26×26 each), latin_mirror_summary.csv (per
#     face, axis and letter: best match, best score, runner-up,
#     margin, and the letter's score against itself),
#     latin_j_lock_sweep.csv (per face and fraction: the score
#     against U, U's rank, the best match), and
#     latin_decompose_I.csv (the decomposition's measures and
#     verdict, per face).
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Latin mirror-composition measurement — builder and freezer.

MECHANISM: import the instrument's tables, sweep and
decomposition (computed from the living faces by the folds
apparatus), write the full matrices, the summary, the sweep
and the decomposition. Nothing here re-implements a mirror, a
composition or a score: the frozen CSVs are the instrument's
numbers, set in rows.

DOCTRINE: the frozen matrices are the measurement of record;
the parity battery re-derives the instrument's seats from
them, so the module never stands on its own say-so.
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))  # the pontifex repo

from pontifex.diplomatic_mirrors import (
    ALPHABET, FACES, decompose_measures, mirror_exhibits,
    mirror_tables, overlap_sweep,
)


def main():
    tables = mirror_tables()
    summary = []
    for face in FACES:
        for axis in ('vertical', 'horizontal'):
            mat = tables[(face, axis)]
            path = HERE / ('latin_%s_mirror_%s_matrix.csv'
                           % (face.lower(), axis))
            with path.open('w', newline='', encoding='utf-8') as fh:
                w = csv.writer(fh)
                w.writerow(['letter'] + list(ALPHABET))
                for ch in ALPHABET:
                    w.writerow([ch] + ['%.4f' % mat[ch][o]
                                        for o in ALPHABET])
            for ch in ALPHABET:
                row = sorted(mat[ch].items(), key=lambda kv: -kv[1])
                best, best_score = row[0]
                runner, runner_score = row[1]
                summary.append({
                    'face': face, 'axis': axis, 'letter': ch,
                    'best': best, 'best_score': '%.4f' % best_score,
                    'self_score': '%.4f' % mat[ch][ch],
                    'runner_up': runner,
                    'runner_up_score': '%.4f' % runner_score,
                    'margin': '%.4f' % (best_score - runner_score),
                })
            print('%s %s frozen: %s' % (face, axis, path.name))
    with (HERE / 'latin_mirror_summary.csv').open(
            'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'face', 'axis', 'letter', 'best', 'best_score',
            'self_score', 'runner_up', 'runner_up_score', 'margin'])
        w.writeheader()
        w.writerows(summary)
    print('summary frozen: latin_mirror_summary.csv (%d rows)'
          % len(summary))

    sweep_rows = []
    for face in FACES:
        for r in overlap_sweep(face, 'J'):
            sweep_rows.append({
                'face': face, 'fraction': '%.2f' % r['fraction'],
                'score_U': '%.4f' % r['score_U'],
                'rank_U': r['rank_U'], 'best': r['best'],
                'best_score': '%.4f' % r['best_score']})
    with (HERE / 'latin_j_lock_sweep.csv').open(
            'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'face', 'fraction', 'score_U', 'rank_U', 'best',
            'best_score'])
        w.writeheader()
        w.writerows(sweep_rows)
    print('sweep frozen: latin_j_lock_sweep.csv (%d rows)'
          % len(sweep_rows))

    ex = mirror_exhibits()
    with (HERE / 'latin_decompose_I.csv').open(
            'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'face', 'iou', 'covers_I', 'I_covers', 'I_ink',
            'composite_ink', 'verdict'])
        w.writeheader()
        for face in FACES:
            m = ex[face]['M3']
            w.writerow({
                'face': face, 'iou': '%.4f' % m['iou'],
                'covers_I': '%.4f' % m['covers_I'],
                'I_covers': '%.4f' % m['I_covers'],
                'I_ink': m['I_ink'],
                'composite_ink': m['composite_ink'],
                'verdict': m['verdict']})
    print('decomposition frozen: latin_decompose_I.csv')


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
