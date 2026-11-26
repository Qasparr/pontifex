#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — research/latin-folds/measure_latin_folds.py
# The bitmap measurement of the Latin fold geometry: every Latin
# capital, in the house's two text faces (Lex Stellarrvm Serif
# and Sans), folded on the vertical and horizontal creases by
# pontifex/diplomatic_folds.py, its collapsed form scored against
# every capital of its face by ink overlap. The frozen CSVs this
# builder writes are the measurement the fold instrument stands
# on — the greek-turns builder's office, for the new operation.
#
# Epigraph: "A T is also the H but folded and twisted unto
# itself" — the founder, 2026-11-26.
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
#     (pontifex/diplomatic_folds.py): the planted exhibit —
#     fold_vertical(H) read as T — would corroborate under the
#     turns family's verdict rule or part at printed coordinates;
#     the killing evidence was stated before the run.
#   Method: the instrument's own apparatus and operations,
#     imported, not re-implemented — 220pt render, bounding-box
#     centring on a 400-pixel canvas, ink at grey 96, ink
#     overlap; the fold at the canvas-centre crease (column 200,
#     row 200), mirror identification, ink union; the collapsed
#     form centred, not rescaled, and scored against the whole
#     alphabet of its face.
#   Observation: printed by this builder to the frozen CSVs; the
#     instrument quotes them, and the parity battery re-derives
#     its tables from them. Headline: fold_vertical(H) → T 0.396
#     in Serif (second, behind I 0.478 — PARTED) and 0.151 in
#     Sans (ninth, best F 0.282 — FAILS); the vertical register's
#     corroborations land on I (Serif B/E/F/L/P, Sans J); the
#     horizontal register corroborates nothing (peak 0.467).
#   Result: latin_{serif,sans}_fold_{vertical,horizontal}_
#     matrix.csv (26×26 each) and latin_fold_summary.csv (per
#     face, axis and letter: best match, best score, runner-up,
#     margin, and the letter's score against itself).
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Latin fold measurement — builder and freezer.

MECHANISM: import the instrument's tables (computed from the
living faces by its own apparatus), write the full matrices and
a summary. Nothing here re-implements a fold or a score: the
frozen CSVs are the instrument's numbers, set in rows.

DOCTRINE: the frozen matrices are the measurement of record; the
parity battery re-derives the instrument's seats from them, so
the module never stands on its own say-so.
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))  # the pontifex repo

from pontifex.diplomatic_folds import ALPHABET, FACES, fold_tables


def main():
    tables = fold_tables()
    summary = []
    for face in FACES:
        for axis in ('vertical', 'horizontal'):
            mat = tables[(face, axis)]
            path = HERE / ('latin_%s_fold_%s_matrix.csv'
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
    with (HERE / 'latin_fold_summary.csv').open(
            'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'face', 'axis', 'letter', 'best', 'best_score',
            'self_score', 'runner_up', 'runner_up_score', 'margin'])
        w.writeheader()
        w.writerows(summary)
    print('summary frozen: latin_fold_summary.csv (%d rows)'
          % len(summary))


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
