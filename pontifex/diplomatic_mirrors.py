#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — diplomatic_mirrors.py — the Diplomatic Key, extended
# a third time: MIRROR-COMPOSITION — a letter unioned with its
# own mirror image, the construction the founder's fifth stroke
# named on the afternoon of 2026-11-26.
#
# Epigraph: "Ok I with the top and bottom bars is also T and L
# just as U is L mirroring itself horizontally and U is also J
# mirroring itself but with them overlapping slightly forming
# a 'lock.' (In terms of magnetism)" — the founder, 2026-11-26.
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
#   Hypothesis: that the fold instrument built the same morning
#     (pontifex/diplomatic_folds.py) carries the mirror as its
#     half-operation — every fold mirrors one half onto the
#     other — but nowhere COMPOSES a letter with its own mirror
#     image, which is the construction the founder's fifth
#     stroke states three times: U as L mirroring itself, U as
#     J mirroring itself with a slight overlap (a "lock"), and
#     the barred I as T over L on one stem; and that each claim
#     would either corroborate under the family's own verdict
#     rule or part at printed coordinates. The founder's order,
#     verbatim (14:35 EST): "Do all of that."
#   Method: the folds apparatus, imported, not re-implemented —
#     220pt render, bounding-box centring, ink at grey 96, ink
#     overlap — in the house's two text faces, Lex Stellarrvm
#     Serif and Sans. THREE operations, defined mechanically:
#     compose_mirror places a glyph's bounding-box crop beside
#     its own mirror image, edge-to-edge, no overlap (vertical
#     axis: the crop and its left-right mirror side by side,
#     feet meeting at the seam; horizontal axis: stacked).
#     compose_mirror_overlap sweeps the mirrored copy from that
#     edge-to-edge placement (fraction 0.00) to box-coincidence
#     (fraction 1.00) in twentieths, unioning the ink at each
#     offset and scoring each against the alphabet — the lock,
#     if any, is the offset of maximum score against the
#     claimed letter. decompose builds the barred I's claimed
#     parts: T top-aligned and L bottom-aligned on a canvas of
#     the I's own height, their stem columns (each crop's
#     ink-heaviest column) made coincident, the ink unioned.
#     A composite is wider than the 400-pixel canvas the folds
#     score on, so scoring FRAMES both forms: each is cropped
#     to its bounding box and centred — centred, NOT rescaled —
#     on the smallest square canvas that holds both, and the
#     ink overlap is taken there. Wherever a form fits the
#     folds' canvas the framed score is the folds' score
#     exactly; the checker proves the identity on the folds'
#     own headline measurement before any composite is read.
#     THE VERDICT RULE is the family's, inherited: for the
#     composition claims (M1, M2) the folds' translation stands
#     — CORROBORATED when the claimed letter is the composite's
#     best match at ≥ 0.60; PARTED when it stands best or
#     second below the line; FAILS otherwise, rank and score
#     printed. For the decomposition (M3) the rule is stated
#     once, here, before its numbers: CORROBORATED when the
#     composite's overlap with the I is ≥ 0.60; PARTED when the
#     overlap stands below the line but the composite still
#     covers ≥ 0.60 of the I's ink (the parts explain the
#     letter; the whole is not the letter); FAILS otherwise.
#     THE KILLING EVIDENCE, stated before the run: M1 fails if
#     U is not the L-composite's best match at the line; M2
#     fails if no offset in the sweep makes U the J-composite's
#     best match at the line — no lock in these faces; M3 fails
#     as stated if the T-over-L composite covers less than
#     0.60 of the barred I's ink.
#   Observation: M1 FAILS in both faces — the edge-to-edge
#     L-composite reads M in Serif (0.121) and W in Sans
#     (0.167), with U fourteenth (0.072) and tenth (0.080); the
#     parting coordinate is width: the composite stands 258
#     pixels wide against U's 166 in Serif, 202 against 123 in
#     Sans — feet meeting tip-to-tip, the figure runs half
#     again as wide as any letter it could be. M2 finds NO
#     LOCK: against U the sweep peaks at its separated end in
#     Serif (0.090 at fraction 0.00, U ranked 20th) and on a
#     low plateau in Sans (0.051, U ranked 25th), and U is
#     never the composite's best match at any offset in either
#     face; as the copies close, the figure converges not onto
#     U but onto the stem family — J itself in Serif (0.616 at
#     coincidence), I mid-sweep in Sans (0.670 at fraction
#     0.50) — because the house's J is narrow and its two stems
#     meet at the centre, where U is hollow. M3 PARTS in Serif
#     and FAILS in Sans: the T-over-L composite covers 0.606 of
#     the barred I's ink in Serif (the parts do explain the
#     letter) at an overlap of 0.291 (the whole is not the
#     letter — the composite carries both full stems and L's
#     one-sided foot, 7,470 ink against the I's 4,422); in
#     Sans, whose I wears no bars, coverage falls to 0.577,
#     under the stated line. The register (M4) seats NOTHING:
#     no letter's edge-to-edge mirror composite, on either
#     axis, in either face, reaches the 0.60 line against any
#     letter; the nearest approach in the whole register is
#     Serif's doubled barred I reading E at 0.590. The
#     apparatus controls hold: mirroring is an exact involution
#     on the bitmaps, and the near-symmetric letters return
#     themselves under the mirror (Serif H 0.948, I 0.939,
#     O 0.967; Sans H and I exact at 1.000, O 0.988) — X parts
#     (0.632 / 0.876): the drawn X's diagonals are not mirror
#     twins, and the instrument prints it.
#   Result: the mirror-composition instrument below — the
#     three operations, the full composition tables (26
#     capitals × 2 axes × 2 faces), the J lock sweep, the
#     decomposition, the planted exhibits with their verdicts,
#     and the checker. The founder's claims stand filed as his
#     claims; the instrument's numbers stand beside them. The
#     composition seats no diplomatic pair and decides no
#     doctrine; what it adds to the house is a measured answer,
#     in the house's own faces, to a construction the founder
#     stated — and the register's emptiness is its finding,
#     printed whole.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Diplomatic Key, extended a third time — mirror-composition.

RELATION TO THE PRIOR INSTRUMENTS (the fence this module stands
behind): pontifex/diplomatic.py, pontifex/diplomatic_turns.py
and pontifex/diplomatic_folds.py stand UNALTERED. The folds
mirror a glyph's half onto its other half and read the
collapsed form; this module COMPOSES — a whole glyph unioned
with its own whole mirror image — and reads the composed form.
Composition is not a fold and not a turn: it doubles a glyph's
extent instead of halving it, which is why its scores are taken
on the framed canvas (§APPARATUS) and why no composed form
enters a diplomatic pair. The apparatus — render, centring,
binarisation, ink overlap, verdict line — is the folds' own,
imported from pontifex.diplomatic_folds, so a score here and a
score there are one measure wherever both can be taken.

WHAT A COMPOSITION CLAIM IS, in the instrument's terms: a
composed form, scored against the alphabet of its own face, is
read as a letter — a claim seated only under the verdict rule
stated in the header. The register this module keeps is a
register of composed forms and their nearest letters, with
every coordinate printed, the empty seats printed as empty.

TIER: CONSTRUCTED — a house instrument, built 2026-11-26 at
the founder's order of the same afternoon. The geometry is
MEASURED (the frozen matrices under research/latin-mirrors/),
in the house's own faces, by the folds apparatus.
"""

import numpy as np

# ---------------------------------------------------------------------------
# §APPARATUS — the folds measurement, imported whole.
#
# MECHANISM: _canvas renders and centres a glyph; _iou is the
# ink overlap; _verdict is the folds' translation of the family
# rule. The one extension is the FRAME: a composed form can be
# wider than the 400-pixel canvas, and clipping its ink to fit
# would corrupt every score it touches, so _framed_iou crops
# both forms to their bounding boxes and centres them — the
# apparatus's own centring, unrescaled — on the smallest square
# canvas holding both. The folds' canvas is the special case:
# where both forms fit 400, the framed score equals the folds'
# score to the last decimal (checker, first entry).
# ---------------------------------------------------------------------------

from pontifex.diplomatic_folds import (
    ALPHABET, FACES, _canvas, _centre, _iou, _verdict,
    fold_vertical,
)

_C = 400


def _crop(a):
    """A bitmap cropped to its ink's bounding box."""
    ys, xs = np.nonzero(a)
    return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def _place(c, size):
    """A cropped form centred — NOT rescaled — on a square
    canvas of the given size."""
    out = np.zeros((size, size), dtype=bool)
    y0 = (size - c.shape[0]) // 2
    x0 = (size - c.shape[1]) // 2
    out[y0:y0 + c.shape[0], x0:x0 + c.shape[1]] = c
    return out


def _framed_iou(a, b):
    """Ink overlap of two forms, each cropped to its bounding
    box and centred on the smallest square canvas holding
    both (never smaller than the folds' 400). Identical to the
    folds' centred score wherever both forms fit the 400
    canvas."""
    ca, cb = _crop(a), _crop(b)
    size = max(_C, ca.shape[0], ca.shape[1],
               cb.shape[0], cb.shape[1])
    return _iou(_place(ca, size), _place(cb, size))


def _framed_pair(a, b):
    """Both forms framed on one canvas, for coverage measures:
    returns the two placed bitmaps."""
    ca, cb = _crop(a), _crop(b)
    size = max(_C, ca.shape[0], ca.shape[1],
               cb.shape[0], cb.shape[1])
    return _place(ca, size), _place(cb, size)


# ---------------------------------------------------------------------------
# §THE OPERATIONS — mirror, composition, the lock sweep, the
# decomposition, each defined mechanically.
#
# MECHANISM: mirror_bitmap reflects a bitmap across the named
# axis (vertical = left-right, the mirror the founder's stroke
# names; horizontal = top-bottom). compose_mirror concatenates
# a glyph's crop with its mirror, edge-to-edge, no overlap —
# vertical: [crop | mirror(crop)], the feet meeting at the
# seam; horizontal: the crop stacked on its mirror.
# compose_mirror_overlap builds on a canvas twice the crop's
# width: the crop stands at the left; the mirrored copy is
# placed at offset fraction f of the crop's width from the
# edge-to-edge position — f = 0.00 is compose_mirror itself,
# f = 1.00 is box-coincidence, the two copies' boxes one box —
# and the ink is unioned. decompose builds T over L: T's crop
# top-aligned, L's crop bottom-aligned, on a canvas of the
# barred I's crop height, the two stem columns (each crop's
# ink-heaviest column) made coincident.
# ---------------------------------------------------------------------------

def mirror_bitmap(a, axis='vertical'):
    """A bitmap reflected across the named axis: 'vertical'
    flips left-right, 'horizontal' flips top-bottom."""
    if axis == 'vertical':
        return np.fliplr(a)
    if axis == 'horizontal':
        return np.flipud(a)
    raise ValueError('axis must be vertical or horizontal')


def compose_mirror(face, letter, axis='vertical'):
    """The letter's crop concatenated with its own mirror
    image, edge-to-edge, no overlap. Returns the composed
    form's bitmap (uncropped extent)."""
    c = _crop(_canvas(face, letter))
    m = mirror_bitmap(c, axis)
    if axis == 'vertical':
        return np.concatenate([c, m], axis=1)
    return np.concatenate([c, m], axis=0)


def compose_mirror_overlap(face, letter, fraction):
    """The letter unioned with its mirror image at an overlap
    fraction: 0.00 = edge-to-edge (compose_mirror on the
    vertical axis), 1.00 = the copies' boxes coincident.
    Vertical axis only — the lock the founder named is a
    horizontal closing."""
    c = _crop(_canvas(face, letter))
    w = c.shape[1]
    canvas = np.zeros((c.shape[0], 2 * w), dtype=bool)
    canvas[:, :w] |= c
    x0 = w - int(round(fraction * w))
    canvas[:, x0:x0 + w] |= np.fliplr(c)
    return canvas


def _stem_column(c):
    """A crop's stem column: its ink-heaviest column — the
    column the decomposition aligns on."""
    return int(np.argmax(c.sum(axis=0)))


def decompose_bars(face):
    """The barred I decomposed as T over L: T top-aligned and
    L bottom-aligned on a canvas of the I's crop height, stem
    columns coincident, ink unioned. Returns the composite
    bitmap (uncropped extent)."""
    gi = _crop(_canvas(face, 'I'))
    gt = _crop(_canvas(face, 'T'))
    gl = _crop(_canvas(face, 'L'))
    height = gi.shape[0]
    off = _stem_column(gt) - _stem_column(gl)
    width = max(gt.shape[1], gl.shape[1] + abs(off)) + 40
    canvas = np.zeros((height, width), dtype=bool)
    stem = _stem_column(gt) + 20
    canvas[0:gt.shape[0],
           stem - _stem_column(gt):
           stem - _stem_column(gt) + gt.shape[1]] |= gt
    y0 = height - gl.shape[0]
    canvas[y0:y0 + gl.shape[0],
           stem - _stem_column(gl):
           stem - _stem_column(gl) + gl.shape[1]] |= gl
    return canvas


# ---------------------------------------------------------------------------
# §THE TABLES — every capital composed, both axes, both faces;
# the lock sweep; the decomposition's measures.
#
# MECHANISM: each letter rendered once per face by the folds
# apparatus; each composition built once; the composed form
# scored against every capital of the same face on the framed
# canvas. The full matrices are frozen under
# research/latin-mirrors/ by that folder's builder; the tables
# below are recomputed from the living faces, and the parity
# battery holds the two to each other.
# ---------------------------------------------------------------------------

_TABLES = None
SWEEP_STEPS = 20   # twentieths: fractions 0.00, 0.05, …, 1.00


def mirror_tables():
    """{(face, axis): {letter: {target: score}}} — the full
    composition register, computed from the living faces."""
    global _TABLES
    if _TABLES is not None:
        return _TABLES
    out = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in ALPHABET}
        for axis in ('vertical', 'horizontal'):
            mat = {}
            for c in ALPHABET:
                comp = compose_mirror(face, c, axis)
                mat[c] = {t: _framed_iou(comp, glyphs[t])
                          for t in ALPHABET}
            out[(face, axis)] = mat
    _TABLES = out
    return out


def mirror_ranking(face, axis, letter):
    """The composed form's matches, best first: [(target,
    score)] over the whole alphabet of its face."""
    row = mirror_tables()[(face, axis)][letter]
    return sorted(row.items(), key=lambda kv: -kv[1])


def mirror_corroborations(face, axis):
    """The register's seats on one face and axis: the letters
    whose composed form's best match stands at or above the
    0.60 line — {(letter, best_target): score}."""
    out = {}
    for c in ALPHABET:
        best, score = mirror_ranking(face, axis, c)[0]
        if score >= 0.60:
            out[(c, best)] = score
    return out


def overlap_sweep(face, letter='J'):
    """The lock sweep for one letter: at each overlap fraction
    (twentieths from 0.00 to 1.00), the composed form's score
    against U, U's rank, and the best match — the sweep the
    founder's 'overlapping slightly' names, run whole."""
    glyphs = {c: _canvas(face, c) for c in ALPHABET}
    rows = []
    for i in range(SWEEP_STEPS + 1):
        frac = i / SWEEP_STEPS
        comp = compose_mirror_overlap(face, letter, frac)
        row = {t: _framed_iou(comp, glyphs[t]) for t in ALPHABET}
        ranking = sorted(row.items(), key=lambda kv: -kv[1])
        rows.append({'fraction': frac,
                     'score_U': row['U'],
                     'rank_U': [t for t, _s in ranking].index('U') + 1,
                     'best': ranking[0][0],
                     'best_score': ranking[0][1]})
    return rows


def decompose_measures(face):
    """The decomposition's numbers: the T-over-L composite
    against the face's I — ink overlap, the fraction of the
    I's ink the composite covers, the fraction of the
    composite's ink the I covers, and both ink counts."""
    comp, target = _framed_pair(decompose_bars(face),
                                _canvas(face, 'I'))
    inter = int((comp & target).sum())
    return {'iou': _iou(comp, target),
            'covers_I': inter / int(target.sum()),
            'I_covers': inter / int(comp.sum()),
            'I_ink': int(target.sum()),
            'composite_ink': int(comp.sum())}


def _decompose_verdict(m):
    """The decomposition rule, stated in the header:
    CORROBORATED at overlap ≥ 0.60; PARTED when the overlap
    stands below the line but the composite covers ≥ 0.60 of
    the I's ink; FAILS otherwise."""
    if m['iou'] >= 0.60:
        return 'CORROBORATED'
    if m['covers_I'] >= 0.60:
        return 'PARTED'
    return 'FAILS'


# ---------------------------------------------------------------------------
# §THE PLANTED EXHIBITS — the founder's fifth stroke, verdicted.
#
# The exhibits were planted by the founder's sentence of
# 2026-11-26 14:34 EST and are verdicted by the inherited
# rule, per face, never merged across faces:
#   M1 — U is L mirroring itself: the edge-to-edge composite
#        of L, read against U.
#   M2 — U is J mirroring itself with a slight overlap: the
#        lock sweep — the offset of maximum score against U,
#        verdicted at that offset; whether any offset seats U
#        at all.
#   M3 — the barred I is T over L: the decomposition's
#        overlap and coverages, verdicted by its stated rule.
#   M4 — the register entire (mirror_tables): which letters,
#        if any, are mirror-composites of others.
# ---------------------------------------------------------------------------

def mirror_exhibits():
    """The planted exhibits, verdicted per face, with every
    coordinate the verdicts rest on."""
    out = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in ALPHABET}
        m1_rank = mirror_ranking(face, 'vertical', 'L')
        sweep = overlap_sweep(face, 'J')
        lock_i = max(range(len(sweep)),
                     key=lambda i: sweep[i]['score_U'])
        lock = sweep[lock_i]
        lock_ranking = sorted(
            {t: _framed_iou(
                compose_mirror_overlap(face, 'J', lock['fraction']),
                glyphs[t]) for t in ALPHABET}.items(),
            key=lambda kv: -kv[1])
        m3 = decompose_measures(face)
        out[face] = {
            'M1': _verdict(m1_rank, 'U'),
            'M1_top5': m1_rank[:5],
            'M1_widths': {
                'composite': int(compose_mirror(
                    face, 'L', 'vertical').shape[1]),
                'U': int(_crop(glyphs['U']).shape[1])},
            'M2': {'lock_fraction': lock['fraction'],
                   'lock_score_U': lock['score_U'],
                   'lock_rank_U': lock['rank_U'],
                   'verdict': _verdict(lock_ranking, 'U')['verdict'],
                   'any_seat': any(
                       r['best'] == 'U' and r['best_score'] >= 0.60
                       for r in sweep),
                   'coincident_best': sweep[-1]['best'],
                   'coincident_best_score': sweep[-1]['best_score'],
                   'sweep': sweep},
            'M3': dict(m3, verdict=_decompose_verdict(m3)),
        }
    return out


def mirror_controls():
    """The apparatus controls: the mirror as an exact
    involution, and the near-symmetric letters read against
    themselves under the mirror and at the coincident end of
    the overlap construction."""
    out = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in ALPHABET}
        out[face] = {
            'involution_exact': all(
                bool((mirror_bitmap(
                    mirror_bitmap(_crop(glyphs[c]))) == _crop(
                        glyphs[c])).all())
                for c in ALPHABET),
            'mirror_self': {c: _framed_iou(
                mirror_bitmap(glyphs[c]), glyphs[c])
                for c in 'HIOX'},
            'coincident_self': {c: _framed_iou(
                compose_mirror_overlap(face, c, 1.00), glyphs[c])
                for c in 'HIOX'},
        }
    return out


# ---------------------------------------------------------------------------
# §CHECKS — the instrument proves itself.
# ---------------------------------------------------------------------------

def diplomatic_mirrors_checks():
    """The check battery: the framed road proven identical to
    the folds' road on the folds' own headline measurement;
    the mirror mechanics on synthetic bitmaps; the apparatus
    controls; the tables complete; the planted exhibits
    restated at their measured coordinates; the register's
    emptiness stated as its finding. Each entry: (name,
    passed, detail)."""
    checks = []
    tables = mirror_tables()
    ex = mirror_exhibits()
    ctl = mirror_controls()

    # 1. THE FRAMED ROAD IS THE FOLDS' ROAD: fold_vertical(H)
    #    against T, recomputed on the framed canvas, equals
    #    the folds' centred score to the printed precision in
    #    both faces (Serif 0.396, Sans 0.151) — the frame
    #    enlarges the canvas and touches nothing else.
    equiv = {}
    for face in FACES:
        glyphs = {c: _canvas(face, c) for c in 'HT'}
        folded = fold_vertical(glyphs['H'])
        equiv[face] = (round(_iou(_centre(folded), glyphs['T']), 3),
                       round(_framed_iou(folded, glyphs['T']), 3))
    checks.append(('framed road = folds road: fold_vertical(H) '
                   'vs T scores identical on both roads (Serif '
                   '0.396, Sans 0.151) — the frame only enlarges '
                   'the canvas, never rescales',
                   equiv == {'Serif': (0.396, 0.396),
                             'Sans': (0.151, 0.151)}, equiv))

    # 2. THE MIRROR MECHANICS, on synthetic bitmaps: the
    #    mirror is an exact involution on every capital's crop
    #    in both faces; a lone ink pixel composes to itself and
    #    its twin at the seam; the overlap construction at
    #    fraction 1.00 is the crop unioned with its mirror in
    #    one box, and at 0.00 is compose_mirror itself.
    probe = np.zeros((10, 6), dtype=bool)
    probe[2, 1] = True
    comp = np.concatenate([probe, np.fliplr(probe)], axis=1)
    checks.append(('mirror mechanics: involution exact on all '
                   '26 crops in both faces; a lone pixel at '
                   'column 1 composes to columns 1 and 10 of a '
                   '12-wide composite (its twin across the '
                   'seam); overlap(0.00) = compose_mirror and '
                   'overlap(1.00) = crop ∪ mirror(crop)',
                   all(ctl[f]['involution_exact'] for f in FACES)
                   and comp.shape == (10, 12) and comp[2, 1]
                   and comp[2, 10] and int(comp.sum()) == 2
                   and all(
                       bool((compose_mirror_overlap(f, 'L', 0.00)
                             == compose_mirror(f, 'L', 'vertical')
                             ).all())
                       and bool((_crop(compose_mirror_overlap(
                                     f, 'L', 1.00))
                                 == _crop(_canvas(f, 'L'))
                                 | np.fliplr(_crop(_canvas(f, 'L')))
                                 ).all())
                       for f in FACES),
                   {f: ctl[f]['involution_exact'] for f in FACES}))

    # 3. THE APPARATUS CONTROLS: the near-symmetric letters
    #    return themselves under the mirror — Serif H 0.948,
    #    I 0.939, O 0.967; Sans H 1.000, I 1.000, O 0.988 —
    #    and X parts in both faces (0.632 / 0.876): the drawn
    #    X's diagonals are not mirror twins. At the coincident
    #    end of the overlap construction H returns itself at
    #    0.974 (Serif) and 1.000 (Sans).
    ms = {f: {c: round(ctl[f]['mirror_self'][c], 3)
              for c in 'HIOX'} for f in FACES}
    cs = {f: round(ctl[f]['coincident_self']['H'], 3)
          for f in FACES}
    checks.append(('apparatus controls: mirror(H/I/O) against '
                   'themselves ≥ 0.93 in Serif (0.948/0.939/'
                   '0.967) and ≥ 0.98 in Sans (1.000/1.000/'
                   '0.988); X parts (0.632/0.876); coincident '
                   'compose of H vs H 0.974/1.000',
                   ms == {'Serif': {'H': 0.948, 'I': 0.939,
                                    'O': 0.967, 'X': 0.632},
                          'Sans': {'H': 1.000, 'I': 1.000,
                                   'O': 0.988, 'X': 0.876}}
                   and cs == {'Serif': 0.974, 'Sans': 1.000},
                   (ms, cs)))

    # 4. THE TABLES COMPLETE: both faces, both axes, all 26
    #    letters composed and scored against all 26 targets,
    #    every score a proportion.
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
    checks.append(('the composition tables complete: 2 faces '
                   '× 2 axes × 26 letters × 26 targets, every '
                   'score in [0, 1]', complete,
                   {str(k): len(v) for k, v in tables.items()}))

    # 5. EXHIBIT M1 RESTATED: compose_mirror(L) against U —
    #    FAILS in both faces (Serif: U 14th at 0.072, best M
    #    0.121; Sans: U 10th at 0.080, best W 0.167); the
    #    parting coordinate is width (composite 258 vs U 166
    #    in Serif; 202 vs 123 in Sans).
    m1 = {f: (ex[f]['M1']['verdict'], ex[f]['M1']['rank'],
              round(ex[f]['M1']['score'], 3), ex[f]['M1']['best'],
              round(ex[f]['M1']['best_score'], 3),
              ex[f]['M1_widths']['composite'],
              ex[f]['M1_widths']['U']) for f in FACES}
    checks.append(('Exhibit M1 restated: compose_mirror(L) vs '
                   'U — FAILS in both faces (Serif rank 14, '
                   '0.072, best M 0.121, widths 258 vs 166; '
                   'Sans rank 10, 0.080, best W 0.167, widths '
                   '202 vs 123): edge-to-edge, the figure runs '
                   'half again as wide as its claimed letter',
                   m1 == {'Serif': ('FAILS', 14, 0.072, 'M', 0.121,
                                    258, 166),
                          'Sans': ('FAILS', 10, 0.080, 'W', 0.167,
                                   202, 123)}, m1))

    # 6. EXHIBIT M2 RESTATED: the J lock sweep — no offset
    #    seats U in either face (any_seat false); the score
    #    against U peaks at fraction 0.00 in Serif (0.090, U
    #    ranked 20th — FAILS) and at 0.051 on the low plateau
    #    in Sans (U ranked 25th — FAILS); at coincidence the
    #    composite reads J in both faces (0.616 / 0.538), not
    #    U: the closing pair converges onto the stem family.
    m2 = {f: (ex[f]['M2']['lock_fraction'],
              round(ex[f]['M2']['lock_score_U'], 3),
              ex[f]['M2']['lock_rank_U'],
              ex[f]['M2']['verdict'], ex[f]['M2']['any_seat'],
              ex[f]['M2']['coincident_best'],
              round(ex[f]['M2']['coincident_best_score'], 3))
          for f in FACES}
    checks.append(('Exhibit M2 restated: the J lock sweep — '
                   'no lock in either face: Serif peaks at '
                   'fraction 0.00 (0.090 vs U, rank 20, FAILS), '
                   'Sans at 0.051 (rank 25, FAILS), any_seat '
                   'false in both; at coincidence the pair '
                   'reads J (0.616/0.538), never U',
                   m2['Serif'][1:] == (0.090, 20, 'FAILS', False,
                                       'J', 0.616)
                   and m2['Sans'][1] == 0.051
                   and m2['Sans'][2] == 25
                   and m2['Sans'][3:] == ('FAILS', False, 'J',
                                          0.538), m2))

    # 7. EXHIBIT M3 RESTATED: the barred I as T over L —
    #    PARTED in Serif (overlap 0.291; the composite covers
    #    0.606 of the I's ink, the I covers 0.359 of the
    #    composite's; ink 4,422 against 7,470); FAILS in Sans
    #    (overlap 0.240; coverage 0.577, under the stated
    #    line — the Sans I wears no bars for the parts to
    #    explain).
    m3 = {f: (ex[f]['M3']['verdict'],
              round(ex[f]['M3']['iou'], 3),
              round(ex[f]['M3']['covers_I'], 3),
              round(ex[f]['M3']['I_covers'], 3),
              ex[f]['M3']['I_ink'], ex[f]['M3']['composite_ink'])
          for f in FACES}
    checks.append(('Exhibit M3 restated: decompose(I) as T '
                   'over L — PARTED in Serif (IoU 0.291, '
                   'covers I 0.606, I covers composite 0.359, '
                   'ink 4422 vs 7470); FAILS in Sans (IoU '
                   '0.240, covers 0.577 — under the line)',
                   m3 == {'Serif': ('PARTED', 0.291, 0.606, 0.359,
                                    4422, 7470),
                          'Sans': ('FAILS', 0.240, 0.577, 0.291,
                                   3520, 6976)}, m3))

    # 8. THE REGISTER'S FINDING: the composition register
    #    seats nothing — corroborations empty on both axes in
    #    both faces — and its nearest approach in the whole
    #    register is Serif's doubled barred I reading E at
    #    0.590, under the line, printed as the peak.
    seats = {(f, a): mirror_corroborations(f, a)
             for f in FACES for a in ('vertical', 'horizontal')}
    peak = max((s, f, a, c, t) for (f, a), mat in tables.items()
               for c, row in mat.items() for t, s in row.items())
    checks.append(('the register\'s finding: mirror-'
                   'composition corroborates nothing — seats '
                   'empty on both axes in both faces; the '
                   'register peak is Serif vertical I → E at '
                   '0.590, below the line',
                   all(v == {} for v in seats.values())
                   and (round(peak[0], 3), peak[1], peak[2],
                        peak[3], peak[4])
                   == (0.590, 'Serif', 'vertical', 'I', 'E'),
                   {str(k): v for k, v in seats.items()}))

    return checks


if __name__ == '__main__':
    print('THE DIPLOMATIC KEY, EXTENDED A THIRD TIME — '
          'mirror-composition')
    for face in FACES:
        for axis in ('vertical', 'horizontal'):
            print('\n%s · %s composition — best matches'
                  % (face, axis))
            for c in ALPHABET:
                best, score = mirror_ranking(face, axis, c)[0]
                print('  compose(%s) → %s  %.3f' % (c, best, score))
    print('\nPLANTED EXHIBITS')
    for face, e in mirror_exhibits().items():
        print(' %s M1 compose_mirror(L) vs U: %s (rank %d, %.3f; '
              'best %s %.3f; widths %d vs %d)'
              % (face, e['M1']['verdict'], e['M1']['rank'],
                 e['M1']['score'], e['M1']['best'],
                 e['M1']['best_score'],
                 e['M1_widths']['composite'], e['M1_widths']['U']))
        print(' %s M2 J lock sweep: peak vs U %.3f at fraction '
              '%.2f (rank %d) — %s; any seat: %s; at '
              'coincidence best %s %.3f'
              % (face, e['M2']['lock_score_U'],
                 e['M2']['lock_fraction'], e['M2']['lock_rank_U'],
                 e['M2']['verdict'], e['M2']['any_seat'],
                 e['M2']['coincident_best'],
                 e['M2']['coincident_best_score']))
        print(' %s M3 decompose(I) as T over L: %s (IoU %.3f; '
              'covers I %.3f; I covers composite %.3f)'
              % (face, e['M3']['verdict'], e['M3']['iou'],
                 e['M3']['covers_I'], e['M3']['I_covers']))
    print('\nCHECKS')
    for name, passed, detail in diplomatic_mirrors_checks():
        print(' ', 'PASS' if passed else 'FAIL', name)
        if not passed:
            print('   detail:', detail)


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
