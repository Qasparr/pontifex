#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — diplomatic_folds.py — the Diplomatic Key, extended
# again: the FOLD — the operation the turn family never carried.
#
# Epigraph: "A T is also the H but folded and twisted unto
# itself" — the founder, 2026-11-26, of the letter H; and of the
# fold's crease: "Its the point where convergence and divergence
# cross paths."
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
#   Hypothesis: that the house's turn family (pontifex/
#     diplomatic.py at the half-turn; pontifex/diplomatic_turns.py
#     at the quarter-turns) lacks the operation the founder named
#     on the morning of 2026-11-26 — the FOLD, a glyph collapsed
#     onto itself along a crease, the two halves identified as
#     paper identifies them — and that the founder's planted
#     exhibit, H folded is T, would either corroborate under the
#     family's own verdict rule or part at printed coordinates.
#     The founder's question, verbatim (10:16 EST): "Can we use
#     it if we dont already?" — the house did not already; the
#     grep of the tree finds "fold" only inside "casefolded".
#   Method: the turns apparatus, unchanged in every particular
#     that touches a score — glyphs rendered at 220pt, centred by
#     bounding box on a 400-pixel canvas, ink binarised at grey
#     96, ink overlap (intersection over union) as the measure —
#     in the house's own two text faces, Lex Stellarrvm Serif and
#     Sans (fonts/lex-stellarrvm/), each verified entire against
#     its cmap for the 26 Latin capitals. THE FOLD, defined
#     mechanically: fold_vertical splits the canvas at its
#     vertical centre axis (column 200 — the crease, whose
#     coordinate the instrument prints and glosses no further)
#     and collapses the right half onto the left by mirror
#     identification, ink-union; fold_horizontal likewise at row
#     200. The collapsed form is cropped to its bounding box and
#     centred on the canvas — centred, NOT rescaled; the
#     apparatus centres only, as it centred the quarter-turns
#     whose aspect departure the turns instrument printed. The
#     collapsed form is then scored against every capital of the
#     same face. THE VERDICT RULE is the turns instrument's,
#     inherited verbatim and translated once, in the open: a
#     fold claim (the collapsed form of X is the letter Y) is
#     CORROBORATED when Y is the collapsed form's best match at
#     a score ≥ 0.60 (the corroboration line; the mutual-best
#     clause has no fold analogue — a fold is not a letter's
#     turn — so best-match at the line is the fold's seat);
#     PARTED when Y stands best or second below the line (the
#     fold carries toward Y and parts, the coordinate printed);
#     FAILS otherwise, the best match and Y's rank and score
#     printed. The killing evidence for the planted exhibit was
#     stated before the run: if fold_vertical(H)'s best match is
#     not T, or its score against T stands below the line with
#     T not at its shoulder, the claim fails as a fold claim in
#     these faces. The instrument measures the FOLD ONLY: the
#     founder's sentence carries a second motion, "twisted",
#     which no fold performs, and the design notes it before any
#     number — the fold of H leaves H's bar where H wears it, at
#     mid-height (measured bar fraction 0.41–0.42 of the glyph's
#     height), while T wears its bar at the top (fraction 0.00);
#     whatever carries the bar from the middle to the top is
#     the twist, and it is not in this instrument.
#   Observation: fold_vertical(H) against T scores 0.396 in
#     Serif — T stands SECOND, behind I at 0.478 — and 0.151 in
#     Sans, ninth, behind F at 0.282: the exhibit PARTS in Serif
#     and FAILS in Sans, and corroborates in neither face.
#     fold_vertical(H) against H itself scores 0.094 / 0.095 —
#     the collapsed H is not H-like in either face.
#     fold_horizontal(H)'s best matches are H itself in Serif
#     (0.296) and U in Sans (0.391, H second at 0.365) — no
#     corroboration anywhere on the horizontal axis either; the
#     whole horizontal table's highest score is 0.467. The
#     register the tables do seat: the vertical fold has an
#     attractor, and it is I — in Serif the collapsed forms of
#     B (0.614), E (0.760), F (0.808), L (0.851) and P (0.736)
#     corroborate onto I (a stem with bars, halved, is a stem
#     with bars — the serifed I's own figure), and in Sans J's
#     collapsed form corroborates onto I at 0.690. The apparatus
#     control holds in the house faces: the half-turn of M
#     reaches W as its best non-self match in both (Serif 0.409,
#     W best outright; Sans 0.438 behind M's self-reach 0.504) —
#     the M ↔ W precedent, re-measured on the new ground.
#   Result: the fold instrument below — the two fold operations
#     with their crease coordinates, the full fold tables (26
#     capitals × 2 axes × 2 faces, every collapsed form's best
#     match and score against the whole alphabet), the planted
#     exhibits with their verdicts, and the checker. The
#     founder's claim stands filed as his claim; the
#     instrument's numbers stand beside it, which is the house's
#     way with both. The fold is now a house operation, usable
#     wherever a collapsed form is honestly in question; it
#     seats no diplomatic pair and decides no doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Diplomatic Key, extended again — the fold geometry.

RELATION TO THE PRIOR INSTRUMENTS (the fence this module stands
behind): pontifex/diplomatic.py and pontifex/diplomatic_turns.py
stand UNALTERED. Their family turns glyphs — by the half-turn,
then by the quarter-turns — and a turn is a rigid motion: every
point of the glyph keeps its distance from every other. A FOLD
is not a turn. A fold IDENTIFIES two halves of the glyph: the
right half is laid onto the left and the ink is unioned, so the
collapsed form is half the width (or half the height) and
carries both halves' ink in one figure. No composition of turns
performs it, and the grep of the house records the absence
exactly: before this module, "fold" appears in the tree only
inside "casefolded". This module is an EXTENSION of the
instrument, versioned and stated as such, as the turns module
was an extension of the Key.

WHAT A FOLD CLAIM IS, in the instrument's terms: the collapsed
form of a letter X, scored against the alphabet of its own face,
is read as a letter Y — a claim seated only under the verdict
rule stated in the header. A fold is not a transformation of
the diplomatic family: it changes a glyph's extent, not merely
its letters, so a folded form enters no diplomatic pair and the
checker of the prior instruments neither knows nor needs it.
The fold's register is a register of collapsed forms and their
nearest letters, with every coordinate printed.

THE CREASE: each fold reports its axis coordinate — column 200
for the vertical fold, row 200 for the horizontal, the canvas
centre the apparatus centred the glyph on. The founder's words
for the crease stand in the epigraph; the instrument prints the
axis and glosses it no further.

TIER: CONSTRUCTED — a house instrument, built 2026-11-26 at the
founder's question of the same morning. The geometry is
MEASURED (the frozen matrices under research/latin-folds/),
in the house's own faces, by the turns apparatus.
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# §APPARATUS — the turns measurement, restated on the house faces.
#
# MECHANISM: 220pt render, bounding-box crop, centred on a
# 400×400 canvas, ink at grey > 96 — the greek-turns builder's
# exact constants, so a score here and a score there are one
# measure. The faces are the house's: Lex Stellarrvm Serif and
# Sans, from the repo's own fonts/ directory, each verified
# entire for the 26 capitals before the run (no substitution).
# ---------------------------------------------------------------------------

_C = 400
CREASE_X = _C // 2   # the vertical fold's axis: canvas column 200
CREASE_Y = _C // 2   # the horizontal fold's axis: canvas row 200
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
FACES = ('Serif', 'Sans')
_FONT_DIR = Path(__file__).resolve().parent.parent / 'fonts' \
    / 'lex-stellarrvm'
_FONTS = {}


def _font(face):
    if face not in _FONTS:
        _FONTS[face] = ImageFont.truetype(
            str(_FONT_DIR / ('LexStellarrvm-%s.ttf' % face)), 220)
    return _FONTS[face]


def _canvas(face, ch):
    """One glyph, centred by its bounding box on the square
    canvas — the turns apparatus, unchanged."""
    img = Image.new('L', (_C, _C), 0)
    ImageDraw.Draw(img).text((0, 0), ch, font=_font(face),
                             fill=255)
    g = img.crop(img.getbbox())
    out = Image.new('L', (_C, _C), 0)
    out.paste(g, ((_C - g.width) // 2, (_C - g.height) // 2))
    return np.array(out) > 96


def _centre(a):
    """A bitmap cropped to its ink's bounding box and centred on
    the canvas — centred, NOT rescaled (the apparatus centres
    only; a collapsed form keeps its own proportions, and the
    departure that costs it is printed in its scores)."""
    ys, xs = np.nonzero(a)
    crop = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    out = np.zeros((_C, _C), dtype=bool)
    y0 = (_C - crop.shape[0]) // 2
    x0 = (_C - crop.shape[1]) // 2
    out[y0:y0 + crop.shape[0], x0:x0 + crop.shape[1]] = crop
    return out


def _iou(a, b):
    """Ink overlap: intersection over union of the binarised
    bitmaps — the turns measure."""
    union = int((a | b).sum())
    return int((a & b).sum()) / union if union else 0.0


# ---------------------------------------------------------------------------
# §THE FOLDS — the two operations, defined mechanically.
#
# MECHANISM: fold_vertical splits the canvas at the crease
# column: the left half stands; the right half is mirrored
# (column 200+k lands on column 199−k, the paper identification)
# and the ink is unioned. The result is a half-width bitmap,
# 400 tall × 200 wide. fold_horizontal is the same operation on
# the rows: the bottom half mirrored up onto the top, a
# half-height bitmap, 200 × 400. A fold is idempotent in extent
# only in the trivial sense — folding a collapsed form again
# halves it again; the instrument folds each glyph once, from
# its full form, and says so.
# ---------------------------------------------------------------------------

def fold_vertical(bitmap):
    """Collapse a canvas bitmap along the vertical crease
    (column 200): right half mirrored onto the left, ink
    unioned. Returns the half-width collapsed bitmap."""
    left = bitmap[:, :CREASE_X]
    right = bitmap[:, CREASE_X:][:, ::-1]
    return left | right


def fold_horizontal(bitmap):
    """Collapse a canvas bitmap along the horizontal crease
    (row 200): bottom half mirrored onto the top, ink unioned.
    Returns the half-height collapsed bitmap."""
    top = bitmap[:CREASE_Y, :]
    bottom = bitmap[CREASE_Y:, :][::-1, :]
    return top | bottom


FOLDS = {'vertical': fold_vertical, 'horizontal': fold_horizontal}
CREASES = {'vertical': ('column', CREASE_X),
           'horizontal': ('row', CREASE_Y)}


def bar_fraction(bitmap):
    """The glyph's bar coordinate: the ink-heaviest row, stated
    as a fraction of the glyph's ink height (0 = the top). The
    coordinate at which the H/T exhibit parts: H wears its bar
    mid-height, T at the top, and the fold moves no bar."""
    ys, _xs = np.nonzero(bitmap)
    row = int(np.argmax(bitmap.sum(axis=1)))
    span = max(1, int(ys.max() - ys.min()))
    return (row - int(ys.min())) / span


# ---------------------------------------------------------------------------
# §THE TABLES — every capital folded, both axes, both faces.
#
# MECHANISM: each letter rendered once per face; each fold
# applied once; the collapsed form centred and scored against
# every capital of the same face. The full matrices are frozen
# under research/latin-folds/ by that folder's builder; the
# tables below are recomputed from the living faces, and the
# parity battery holds the two to each other.
# ---------------------------------------------------------------------------

_TABLES = None


def fold_tables():
    """{(face, axis): {letter: {target: score}}} — the full
    fold register, computed from the living faces."""
    global _TABLES
    if _TABLES is not None:
        return _TABLES
    out = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in ALPHABET}
        for axis, fn in FOLDS.items():
            mat = {}
            for c in ALPHABET:
                collapsed = _centre(fn(glyphs[c]))
                mat[c] = {t: _iou(collapsed, glyphs[t])
                          for t in ALPHABET}
            out[(face, axis)] = mat
    _TABLES = out
    return out


def fold_ranking(face, axis, letter):
    """The collapsed form's matches, best first: [(target,
    score)] over the whole alphabet of its face."""
    row = fold_tables()[(face, axis)][letter]
    return sorted(row.items(), key=lambda kv: -kv[1])


def corroborations(face, axis):
    """The register's seats on one face and axis: the letters
    whose collapsed form's best match stands at or above the
    0.60 line — {(letter, best_target): score}."""
    out = {}
    for c in ALPHABET:
        best, score = fold_ranking(face, axis, c)[0]
        if score >= 0.60:
            out[(c, best)] = score
    return out


# ---------------------------------------------------------------------------
# §THE PLANTED EXHIBITS — the founder's claims, verdicted.
#
# The exhibits were planted by the founder's sentences of
# 2026-11-26 and are verdicted by the inherited rule, per face,
# never merged across faces:
#   E1 — fold_vertical(H) is T ("folded and twisted unto
#        itself"; the instrument measures the fold only, and
#        prints the bar coordinate where the twist's absence
#        shows).
#   E2 — fold_vertical(H) is H (the collapsed form read against
#        its own letter: is what survives the fold H-like?).
#   E3 — fold_horizontal(H), the other axis: its best matches,
#        printed as a table question, not a claim.
# ---------------------------------------------------------------------------

def _verdict(ranking, target):
    """The inherited rule, translated once (see the header):
    CORROBORATED — the target is the best match at ≥ 0.60;
    PARTED — the target stands best or second, below the line;
    FAILS — otherwise. The coordinates ride with the verdict."""
    names = [t for t, _s in ranking]
    rank = names.index(target) + 1
    score = dict(ranking)[target]
    best, best_score = ranking[0]
    if rank == 1 and score >= 0.60:
        verdict = 'CORROBORATED'
    elif rank <= 2:
        verdict = 'PARTED'
    else:
        verdict = 'FAILS'
    return {'target': target, 'rank': rank, 'score': score,
            'best': best, 'best_score': best_score,
            'verdict': verdict}


def fold_exhibits():
    """The planted exhibits, verdicted per face, with every
    coordinate the verdicts rest on."""
    out = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in 'HT'}
        v_rank = fold_ranking(face, 'vertical', 'H')
        h_rank = fold_ranking(face, 'horizontal', 'H')
        out[face] = {
            'E1': _verdict(v_rank, 'T'),
            'E2': _verdict(v_rank, 'H'),
            'E3': {'best': h_rank[0], 'second': h_rank[1],
                   'H': dict(h_rank)['H'],
                   'verdict': 'CORROBORATED'
                   if h_rank[0][1] >= 0.60 else 'NO CORROBORATION'},
            'bar': {'H': bar_fraction(glyphs['H']),
                    'fold_vertical(H)': bar_fraction(
                        fold_vertical(glyphs['H'])),
                    'T': bar_fraction(glyphs['T'])},
            'vertical_H_top5': v_rank[:5],
            'horizontal_H_top5': h_rank[:5],
        }
    return out


# ---------------------------------------------------------------------------
# §CHECKS — the instrument proves itself.
# ---------------------------------------------------------------------------

def diplomatic_folds_checks():
    """The check battery: the apparatus control re-measured in
    the house faces (the M ↔ W precedent); the fold mechanics on
    a synthetic bitmap; the crease coordinates; the tables
    complete; the planted exhibits restated at their measured
    coordinates; the register's corroborations as seated. Each
    entry: (name, passed, detail)."""
    checks = []
    tables = fold_tables()
    ex = fold_exhibits()

    # 1. THE APPARATUS CONTROL: in the house faces, under this
    #    apparatus, the half-turn of H reaches H at ≥ 0.60 (the
    #    self-symmetry line) and the half-turn of M reaches W as
    #    its best NON-SELF match — the prior instruments' hinge,
    #    re-measured on the new ground before any fold is read.
    control = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in ALPHABET}
        rot_h = _iou(np.rot90(glyphs['H'], 2), glyphs['H'])
        rot_m = sorted(
            ((t, _iou(np.rot90(glyphs['M'], 2), glyphs[t]))
             for t in ALPHABET if t != 'M'),
            key=lambda kv: -kv[1])
        control[face] = (round(rot_h, 3), rot_m[0],
                         round(rot_m[0][1], 3))
    checks.append(('apparatus control: half-turned H reaches H '
                   'at ≥ 0.60 in both faces (Serif 0.764, Sans '
                   '0.745); half-turned M\'s best non-self match '
                   'is W in both (Serif 0.409, Sans 0.438) — the '
                   'M ↔ W precedent holds in the house faces',
                   control['Serif'][0] == 0.764
                   and control['Sans'][0] == 0.745
                   and control['Serif'][1][0] == 'W'
                   and control['Serif'][2] == 0.409
                   and control['Sans'][1][0] == 'W'
                   and control['Sans'][2] == 0.438,
                   control))

    # 2. THE FOLD MECHANICS, on a synthetic bitmap: a lone ink
    #    pixel in the right half lands mirrored across the
    #    crease; a pixel in the bottom half likewise; ink
    #    already on the standing half is untouched; the
    #    collapsed extents are exactly half.
    probe = np.zeros((_C, _C), dtype=bool)
    probe[10, 300] = True    # right half: mirrors to column 99
    probe[10, 50] = True     # left half: stands
    fv = fold_vertical(probe)
    probe2 = np.zeros((_C, _C), dtype=bool)
    probe2[300, 10] = True   # bottom half: mirrors to row 99
    fh = fold_horizontal(probe2)
    checks.append(('fold mechanics: the right half mirrors '
                   'across the crease (column 300 → 99) and '
                   'unions with the standing half; the bottom '
                   'half likewise (row 300 → 99); collapsed '
                   'extents exactly half (400×200, 200×400)',
                   fv.shape == (400, 200) and fh.shape == (200, 400)
                   and fv[10, 99] and fv[10, 50]
                   and int(fv.sum()) == 2
                   and fh[99, 10] and int(fh.sum()) == 1,
                   (fv.shape, fh.shape)))

    # 3. THE CREASES, printed as coordinates and nothing more:
    #    column 200, row 200 — the canvas centre the apparatus
    #    centred every glyph on.
    checks.append(('the creases: vertical axis column 200, '
                   'horizontal axis row 200 — the crossing '
                   'coordinates, printed as axes',
                   CREASES == {'vertical': ('column', 200),
                               'horizontal': ('row', 200)},
                   CREASES))

    # 4. THE TABLES COMPLETE: both faces, both axes, all 26
    #    letters folded and scored against all 26 targets, every
    #    score a proportion.
    complete = (
        sorted(tables) == [('Sans', 'horizontal'),
                           ('Sans', 'vertical'),
                           ('Serif', 'horizontal'),
                           ('Serif', 'vertical')]
        and all(len(mat) == 26 and all(len(row) == 26
                for row in mat.values())
                for mat in tables.values())
        and all(0.0 <= s <= 1.0 for mat in tables.values()
                for row in mat.values() for s in row.values()))
    checks.append(('the fold tables complete: 2 faces × 2 axes '
                   '× 26 letters × 26 targets, every score in '
                   '[0, 1]', complete,
                   {str(k): len(v) for k, v in tables.items()}))

    # 5. EXHIBIT E1 RESTATED: fold_vertical(H) against T —
    #    Serif PARTED (T second at 0.396 behind I at 0.478);
    #    Sans FAILS (T ninth at 0.151; best F at 0.282); the bar
    #    coordinate parts them in both faces (folded H's bar at
    #    0.41–0.42 of height, T's at 0.00) — the fold measured,
    #    the twist not performed, the claim not seated.
    e1 = {f: (ex[f]['E1']['verdict'], ex[f]['E1']['rank'],
              round(ex[f]['E1']['score'], 3),
              ex[f]['E1']['best'],
              round(ex[f]['E1']['best_score'], 3)) for f in FACES}
    bars = {f: (round(ex[f]['bar']['H'], 2),
                round(ex[f]['bar']['fold_vertical(H)'], 2),
                round(ex[f]['bar']['T'], 2)) for f in FACES}
    checks.append(('Exhibit E1 restated: fold_vertical(H) vs T '
                   '— PARTED in Serif (rank 2, 0.396, behind I '
                   '0.478), FAILS in Sans (rank 9, 0.151, best F '
                   '0.282); bars: H 0.42/0.41, folded H unmoved, '
                   'T 0.00 in both faces',
                   e1 == {'Serif': ('PARTED', 2, 0.396, 'I', 0.478),
                          'Sans': ('FAILS', 9, 0.151, 'F', 0.282)}
                   and bars == {'Serif': (0.42, 0.42, 0.0),
                                'Sans': (0.41, 0.41, 0.0)},
                   (e1, bars)))

    # 6. EXHIBIT E2 RESTATED: the collapsed H against H itself —
    #    0.094 / 0.095, FAILS in both faces: what survives the
    #    vertical fold is not H-like.
    e2 = {f: (ex[f]['E2']['verdict'],
              round(ex[f]['E2']['score'], 3)) for f in FACES}
    checks.append(('Exhibit E2 restated: fold_vertical(H) vs H '
                   '— FAILS in both faces (0.094 Serif, 0.095 '
                   'Sans): the collapsed form is not H-like',
                   e2 == {'Serif': ('FAILS', 0.094),
                          'Sans': ('FAILS', 0.095)}, e2))

    # 7. EXHIBIT E3 RESTATED: the horizontal fold of H — best
    #    H itself in Serif (0.296), best U in Sans (0.391, H
    #    second 0.365); no corroboration on the axis in either
    #    face, and no score in either horizontal table reaches
    #    the line at all (the tables' maximum is Sans I → I,
    #    0.467).
    e3 = {f: (ex[f]['E3']['best'][0],
              round(ex[f]['E3']['best'][1], 3),
              ex[f]['E3']['verdict']) for f in FACES}
    hmax = max(s for (f, a), mat in tables.items()
               if a == 'horizontal' for row in mat.values()
               for s in row.values())
    checks.append(('Exhibit E3 restated: fold_horizontal(H) — '
                   'best H (0.296) in Serif, best U (0.391) in '
                   'Sans, NO CORROBORATION in either; the whole '
                   'horizontal register peaks at 0.467, below '
                   'the line',
                   e3 == {'Serif': ('H', 0.296, 'NO CORROBORATION'),
                          'Sans': ('U', 0.391, 'NO CORROBORATION')}
                   and round(hmax, 3) == 0.467,
                   (e3, round(hmax, 3))))

    # 8. THE REGISTER'S SEATS: the vertical fold's corroborations
    #    are exactly the I-attractor set — Serif {B, E, F, L, P}
    #    onto I; Sans {J} onto I — and the horizontal fold seats
    #    none, in either face.
    seats = {(f, a): sorted(corroborations(f, a))
             for f in FACES for a in FOLDS}
    checks.append(('the register\'s seats: vertical-fold '
                   'corroborations exactly Serif B/E/F/L/P → I '
                   'and Sans J → I (the I attractor); horizontal '
                   'corroborations none in either face',
                   seats[('Serif', 'vertical')]
                   == [('B', 'I'), ('E', 'I'), ('F', 'I'),
                       ('L', 'I'), ('P', 'I')]
                   and seats[('Sans', 'vertical')] == [('J', 'I')]
                   and seats[('Serif', 'horizontal')] == []
                   and seats[('Sans', 'horizontal')] == [],
                   {str(k): v for k, v in seats.items()}))

    return checks


if __name__ == '__main__':
    print('THE DIPLOMATIC KEY, EXTENDED AGAIN — the folds')
    for face in FACES:
        for axis in FOLDS:
            print('\n%s · %s fold (crease: %s %d) — best matches'
                  % (face, axis, CREASES[axis][0], CREASES[axis][1]))
            for c in ALPHABET:
                best, score = fold_ranking(face, axis, c)[0]
                print('  fold(%s) → %s  %.3f' % (c, best, score))
    print('\nPLANTED EXHIBITS')
    for face, e in fold_exhibits().items():
        print(' %s E1 fold_vertical(H) vs T: %s (rank %d, %.3f; '
              'best %s %.3f)' % (face, e['E1']['verdict'],
                                 e['E1']['rank'], e['E1']['score'],
                                 e['E1']['best'],
                                 e['E1']['best_score']))
        print(' %s E2 fold_vertical(H) vs H: %s (%.3f)'
              % (face, e['E2']['verdict'], e['E2']['score']))
        print(' %s E3 fold_horizontal(H): best %s %.3f — %s'
              % (face, e['E3']['best'][0], e['E3']['best'][1],
                 e['E3']['verdict']))
        print(' %s bars: H %.2f · folded H %.2f · T %.2f'
              % (face, e['bar']['H'], e['bar']['fold_vertical(H)'],
                 e['bar']['T']))
    print('\nCHECKS')
    for name, passed, detail in diplomatic_folds_checks():
        print(' ', 'PASS' if passed else 'FAIL', name)
        if not passed:
            print('   detail:', detail)


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
