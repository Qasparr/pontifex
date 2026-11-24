#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — research/greek-turns/measure_greek_turns.py
# The bitmap measurement of the Greek turn geometry: every Greek
# letter, lowercase (with final sigma as a 25th form) and capital,
# rendered in DejaVu Sans, turned at 180°, 90° clockwise and 90°
# counterclockwise, and scored against every letter of its own
# alphabet by ink overlap. The frozen CSVs this builder writes are
# the measurement the instrument THE-GREEK-LOWERCASE-GEOMETRY.md
# stands on.
#
# Epigraph: "Possibly rotating counterclockwise to the greek
# vowels" — the founder, 2026-11-24, of legend piece (ii).
#
# Thelemic date: XXIV day of November, dies Martis, Sol in
# Sagittario, Anno V:xii e.n. (2026 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis (the DESIGN DERIVATION, stated before the bitmaps
#     were run, and printed in the instrument beside the scores):
#     lowercase at 180° seats one pair (δ ↔ ρ — bowl low with a
#     right ascender against bowl high with a left descender, each
#     the other's figure turned) and six self-symmetric letters
#     (ο the circle, ι the bare stem, θ the oval with its centred
#     bar, φ the bowl bisected by a stem extending both ways, χ
#     the crossed diagonals, ξ the two opposed hooks about a
#     centre); at the quarter-turns it seats no pair and two
#     self-symmetric letters (ο, χ); the capitals at the
#     quarter-turns seat no pair and two self-symmetric letters
#     (Ο, Χ). θ at 90° and Θ at 90° approach φ / Φ (the bar turned
#     vertical inside the oval) but the bar does not extend beyond
#     the bowl as the stem does — a near-miss coordinate, not a
#     seat, is the expectation.
#   Method: the prior instrument's own apparatus, unchanged —
#     DejaVu Sans at 220pt on a 400-pixel canvas, glyphs centred
#     by bounding box, ink binarised at grey 96, a turn scored as
#     intersection-over-union of the turned bitmap against every
#     letter of the alphabet. The verdict rule is stated before
#     the verdicts (see the module pontifex/diplomatic_turns.py):
#     self-symmetry corroborated at self-score ≥ 0.60; a pair
#     corroborated when each letter is the other's best match, or
#     the other's best NON-SELF match with the self coordinate
#     printed (the M ↔ W precedent of the prior instrument);
#     where the bitmap's best match at ≥ 0.60 contradicts the
#     design seat, the coordinate prints and the seat is decided
#     on the figure with its reasoning stated (the Θ precedent).
#   Observation: printed by this builder to the frozen CSVs; the
#     instrument reads them, and the report to the founder quotes
#     them. No number in the instrument is quoted from memory —
#     every score is recomputed here.
#   Result: greek_lower_matrix_{180,cw90,ccw90}.csv (the full
#     25×25 score matrices), greek_capital_matrix_{cw90,ccw90}.csv
#     (24×24), and greek_turn_summary.csv (per letter, per angle:
#     best match, best score, self score, runner-up, margin).
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Greek turn measurement — builder and freezer.

MECHANISM: render each letter once (the prior battery's canvas:
220pt DejaVu Sans, bounding-box crop, centred on a 400×400
canvas), turn the canvas with PIL transposes (ROTATE_180,
ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE — exact pixel
permutations on a square canvas, no resampling), and score ink
overlap (IoU over pixels greyer than 96) against every letter of
the same alphabet. Freeze the full matrices and a summary.

DOCTRINE: the bitmap is the CORROBORATION, not the seat — the
seats are derived from the letterforms' design geometry, and the
scores print beside them with their coordinates, exactly as the
prior instrument printed M ↔ W at 0.438 and Θ's off-centre bar.
A score the design derivation did not predict is printed, never
smoothed.
"""

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
_font = ImageFont.truetype(FONT_PATH, 220)
_C = 400

LOWER = 'αβγδεζηθικλμνξοπρςστυφχψω'   # 24 letters + final sigma ς
CAPITAL = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'  # 24 letters

# MECHANISM: Pillow ≥ 10 spells the transposes under
# Image.Transpose (the prior battery's Image.ROTATE_180 alias is
# the same operation); the transposes are exact pixel
# permutations either way, so the two instruments' scores stay
# commensurable. The direction mapping was verified by probe,
# not by the names (Pillow's ROTATE_90 turns counterclockwise):
# a lone ink pixel at (1, 0) of a 5×5 canvas lands at (0, 3)
# under ROTATE_90 (the left side — a counterclockwise turn) and
# at (4, 1) under ROTATE_270 (the right side — clockwise). So
# clockwise is ROTATE_270 and counterclockwise is ROTATE_90, and
# the builder's labels below follow the probe.
_T = Image.Transpose
_TURNS = {
    '180': _T.ROTATE_180,
    'cw90': _T.ROTATE_270,
    'ccw90': _T.ROTATE_90,
}


def _canvas(ch):
    """One glyph, centred by its bounding box on the square
    canvas — the prior battery's exact apparatus, so the scores
    of the two instruments are commensurable."""
    img = Image.new('L', (_C, _C), 0)
    ImageDraw.Draw(img).text((0, 0), ch, font=_font, fill=255)
    g = img.crop(img.getbbox())
    out = Image.new('L', (_C, _C), 0)
    out.paste(g, ((_C - g.width) // 2, (_C - g.height) // 2))
    return out


def _sim(a, b):
    """Ink overlap: intersection over union of the binarised
    bitmaps (threshold 96, the prior battery's line)."""
    inter = union = 0
    for va, vb in zip(a.getdata(), b.getdata()):
        ba, bb = va > 96, vb > 96
        if ba and bb:
            inter += 1
        if ba or bb:
            union += 1
    return inter / union if union else 0.0


def measure(alphabet):
    """{angle: {letter: {target: score}}} — the full matrices."""
    imgs = {c: _canvas(c) for c in alphabet}
    out = {}
    for angle, op in _TURNS.items():
        mat = {}
        for ch in alphabet:
            rot = imgs[ch].transpose(op)
            mat[ch] = {o: _sim(rot, imgs[o]) for o in alphabet}
        out[angle] = mat
    return out


def main():
    summary = []
    for label, alphabet in (('lower', LOWER), ('capital', CAPITAL)):
        mats = measure(alphabet)
        for angle, mat in mats.items():
            path = HERE / ('greek_%s_matrix_%s.csv' % (label, angle))
            with path.open('w', newline='', encoding='utf-8') as fh:
                w = csv.writer(fh)
                w.writerow(['letter'] + list(alphabet))
                for ch in alphabet:
                    w.writerow([ch] + ['%.4f' % mat[ch][o]
                                        for o in alphabet])
            for ch in alphabet:
                row = sorted(mat[ch].items(), key=lambda kv: -kv[1])
                best, best_score = row[0]
                runner, runner_score = row[1]
                summary.append({
                    'case': label, 'letter': ch, 'angle': angle,
                    'best': best, 'best_score': '%.4f' % best_score,
                    'self_score': '%.4f' % mat[ch][ch],
                    'runner_up': runner,
                    'runner_up_score': '%.4f' % runner_score,
                    'margin': '%.4f' % (best_score - runner_score),
                })
            print('%s %s frozen: %s' % (label, angle, path.name))
    with (HERE / 'greek_turn_summary.csv').open('w', newline='',
                                                encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'case', 'letter', 'angle', 'best', 'best_score',
            'self_score', 'runner_up', 'runner_up_score', 'margin'])
        w.writeheader()
        w.writerows(summary)
    print('summary frozen: greek_turn_summary.csv (%d rows)'
          % len(summary))


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
