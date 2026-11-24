#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — diplomatic_turns.py — the Diplomatic Key, extended:
# the Greek turn geometry at the half-turn and the quarter-turns.
#
# Epigraph: "Possibly rotating counterclockwise to the greek
# vowels" — the founder, 2026-11-24, of legend piece (ii), the
# rotation. This module is the measurement that clause demanded.
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
#   Hypothesis: that the Greek lowercase geometry, measured at
#     every turn, would either seat a counterclockwise landing on
#     the vowels (the legend's clause cashed at the glyph level)
#     or close the glyph seat of that clause by evidence.
#   Method: the prior instrument's own apparatus, extended — the
#     letter geometry DERIVED from the letterforms' design
#     figures, corroborated by bitmap rotation in DejaVu Sans
#     (220pt, 400-pixel canvas, bounding-box centring, ink
#     overlap; the full matrices frozen under
#     research/greek-turns/), now at three turns: 180°, 90°
#     clockwise, 90° counterclockwise — the quarter-turns seated
#     as DISTINCT operations, because direction is the legend's
#     own word and the measurement's heart. The verdict rule is
#     the prior instrument's, stated before the verdicts:
#     self-symmetry corroborated at self-score ≥ 0.60; a pair
#     corroborated when each letter is the other's best match,
#     or the other's best NON-SELF match with the coordinate
#     printed (the M ↔ W precedent); where the bitmap contradicts
#     the design seat, the coordinate prints and the seat is
#     decided on the figure with its reasoning stated (the Θ
#     precedent) — and where inspection kills a design seat, the
#     seat falls in the open (ξ and φ below).
#   Observation: the lowercase half-turn seats TWO pairs (δ ↔ ρ,
#     γ ↔ λ) and three self-symmetric letters (ο θ χ); the
#     quarter-turns seat no pair in either case and reach no
#     score of 0.60 anywhere; and no turn at any angle, in either
#     direction, in either case, carries any letter onto a vowel
#     it did not start on — the only vowel landings in the whole
#     measurement are vowels landing on themselves.
#   Result: the checker, the (empty) corpus register with its
#     planted exhibits, the vowel-landing tables, and the
#     capitals impossibility re-scoped over the full quarter-turn
#     family, below. The legend verdict the instrument draws is
#     printed in THE-GREEK-LOWERCASE-GEOMETRY.md: the glyph-turn
#     is alive as a relation in Greek lowercase, and the legend's
#     "counterclockwise to the Greek vowels" is not a glyph fact
#     at any seat measured — the clause belongs to the traversal.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Diplomatic Key, extended — the Greek turn geometry.

RELATION TO THE PRIOR INSTRUMENT (the fence this module stands
behind): pontifex/diplomatic.py stands UNALTERED. Its family
turns glyphs by the half-turn alone, and its Greek result — no
diplomatic pair can exist in Greek capitals under that family —
was PROVEN for that family and stands. This module is an
EXTENSION of the instrument, versioned and stated as such: it
adds the quarter-turns (90° clockwise and 90° counterclockwise
as distinct operations) and measures the two Greek geometries
the prior instrument left as residue in its §VIII — the Greek
lowercase geometry entire, and the Greek capitals again at the
quarter-turns, where the impossibility question reopens and is
answered fresh (§CAPITALS below).

THE SEATED DEFINITION is the prior instrument's, unchanged: a
DIPLOMATIC PAIR is two strings A, B and a stated transformation
T with T(A) = B exactly, while A and B weigh differently in at
least one named bank; a pair that interlocks but weighs the same
everywhere is excluded by the definition, and a pure permutation
is value-invariant in every additive bank (the anagram theorem),
so diplomacy requires a glyph to actually turn. The extension
widens only the family's turns: a turn now carries its angle,
and the word-turn (every glyph turned, the seat order reversed)
keeps the family's signature at every angle — a stated
convention of the extension, printed here: a physical
quarter-turn of a written strip stacks its glyphs vertically,
and the reversal is the family's word-turn mark, applied
uniformly rather than renegotiated per angle.

NORMALIZATION: the checker takes Greek as the bank takes it —
inputs are prepared by the engine's own _normalize_greek
(casefolded, breathings and accents stripped), because the
living Greek bank prices bare lowercase letters (α = 1 …
ω = 800, σ and ς both 200). The turn tables are keyed on those
bare letters, ς seated as a 25th form beside the 24 letters.

TIER: CONSTRUCTED — a house instrument, the extension of the
founder's coinage of 2026-11-24, built at his word the same day
(13:25 EST: "Measure the Greek lowercase geometry"). The
geometry is DERIVED (design figures) and MEASURED (the frozen
bitmaps), tiered as the prior instrument tiered its own.
"""

import unicodedata

from .engine import SYSTEMS, weigh, _normalize_greek
from .diplomatic import find_permutation

# ---------------------------------------------------------------------------
# §GEOMETRY — the Greek turn tables, derived and measured.
#
# THE MEASUREMENT (frozen under research/greek-turns/): every
# letter rendered in DejaVu Sans — the face verified entire
# against the font's cmap (all 25 lowercase forms and all 24
# capitals present; no substitution was needed) — turned at each
# angle and scored against every letter of its alphabet. The
# direction mapping of the bitmap turns was verified by probe (a
# lone pixel's landing), not trusted to a library's names.
#
# LOWERCASE AT THE HALF-TURN — two pairs, three symmetric seats:
#   δ ↔ ρ (mutual best turns, 0.590): the design figure is the
#     bowl-and-stem exchange — δ carries its bowl low with a
#     right ascender, ρ its bowl high with a left descender, and
#     each turned is the other's anatomy. The coordinate, printed
#     not smoothed: in the drawn face δ's ascender curves at its
#     top and ρ's stem is straight, so the turned figures are
#     nearest neighbours, not congruent — the same disposition
#     as the prior instrument's M ↔ W (seated on the figure at
#     0.438 as the typeface's nearest turn; this pair measures
#     stronger, 0.590, and mutual).
#   γ ↔ λ (mutual best turns, 0.611): the measurement's own
#     catch — the desk's derivation expected no seat here. In
#     DejaVu Sans γ is drawn as a straight-stroke fork (a stem
#     splitting into two diagonals), NOT the curved hook of the
#     serif letterform, and that fork turned is λ's figure (a
#     tall diagonal with its fellow), as λ turned is the fork.
#     The seat is therefore a seat OF THE SANS LETTERFORM
#     DESIGN, and its sensitivity is printed at full size: in a
#     face whose γ carries the curved hook, this pair weakens or
#     falls. It stands here because the measured face's figures
#     interlock exactly and the bitmaps are mutual best above
#     the 0.60 line — both layers agreeing, in this face.
#   Self-symmetric: ο (0.910, the circle), θ (0.810, the oval
#     with its centred bar), χ (0.928, the crossed diagonals).
#   REFUSED SEATS, printed with their reasons (the derivation
#     proposed; inspection and measurement disposed):
#     ξ — the derivation guessed the two opposed hooks near
#       point-symmetric; the drawn ξ is not (its top is a flat
#       bar with a hook, its bottom a descender hook — the turn
#       lands on a stacked figure no letter wears). Self-score
#       0.145. The seat falls in the open.
#     φ — the derivation guessed the bisected bowl symmetric;
#       the drawn φ's bowl leans on its stem (the arcs are not
#       rotational counterparts), and its turn leans the other
#       way. Self-score 0.327. The seat falls in the open.
#     ι — the bare-stem figure would be self-symmetric, but the
#       drawn iota carries a foot, and a footed stem turned is a
#       hooked stem: self-score 0.146, its turned figure
#       reaching no letter. The seat is refused as the prior
#       instrument refused Latin l — a seat is not taken on a
#       figure the letterform does not stably hold.
#   COORDINATES (reaches that are not seats): turned σ reaches
#     ο at 0.604 — one-way only (ο's turn is ο), and the short
#     top bar that parts them is σ's whole identity; η's turn
#     reaches η itself at 0.526 and π's at 0.578, ω's at 0.519 —
#     near-self reaches below the line, their descenders and
#     bars parting them from true symmetry; turned υ reaches ο
#     at 0.538 (its stems part it); turned ς reaches δ at 0.466;
#     turned α reaches ε at 0.414 — α in this face is
#     SINGLE-STORY (a circle with a right stem and a tail
#     flick); the double-story α of serif faces is a different
#     figure again, and its turn is likewise no letter, so the
#     absence is stable while the coordinate is face-specific.
#
# LOWERCASE AT THE QUARTER-TURNS — no pairs, two figure seats:
#   No score anywhere reaches 0.60 (the highest in either
#   direction is ο's self-reach, 0.525). The one mutual-best
#   pair the bitmaps name, θ ↔ ω at 0.406/0.414, is refused on
#   the figures outright (a turned oval-with-bar is not a
#   double bowl; the overlap is the wide-oval accident of two
#   broad glyphs) and printed as a coordinate. The design's
#   expected near-miss, θ → φ, does not appear in this face at
#   all (0.216): φ's stem extends beyond its bowl, θ's bar does
#   not, and the bitmaps part them further than the derivation
#   feared. Two letters are seated self-symmetric ON THEIR
#   FIGURES: ο (the circle is invariant at every angle) and χ
#   (the two diagonals are invariant as a figure set). Their
#   DejaVu coordinates print at full size: ο scores 0.525
#   against itself and χ 0.065 — the face draws both letters
#   wider than tall, so a quarter-turned bitmap, aspect-swapped,
#   cannot overlap its unturned self at fixed size; the scores
#   measure the face's proportions, and the seats stand on the
#   figures with the departure printed, as Θ's seat stood in
#   the prior instrument. The bitmap-only layer is printed too:
#   by scores alone, the quarter-turn seat would be EMPTY.
#
# CAPITALS AT THE QUARTER-TURNS (Task 2 — the control):
#   No pair: no score reaches 0.60 in either direction (the
#   highest is Φ's self-reach, 0.503), the one mutual-best pair
#   (Ζ ↔ Μ, 0.310) is refused on the figures, and the design
#   derivation concurs — no capital's quarter-turned figure is
#   another capital's figure. Θ → Φ, the derivation's expected
#   near-miss, measures 0.403 both ways and is not mutual-best
#   (Θ's best reach is Ο, 0.445; Φ's is itself, 0.503): a
#   coordinate, not a seat. Ο and Χ are seated self-symmetric on
#   their figures with their coordinates printed (0.495; 0.162)
#   — the same disposition as their lowercase kin.
#
# THE IMPOSSIBILITY, RE-SCOPED (printed exactly): no diplomatic
# pair can exist in Greek capitals under the half-turn family
# (PROVEN, the prior instrument), and none under the
# quarter-turns in either direction (MEASURED here, the design
# derivation concurring) — at every angle of the full
# quarter-turn family {90° CW, 90° CCW, 180°} the only seated
# images a capital carries are itself or nothing, so every
# admissible transformation changes no letter, and by the
# anagram theorem no value can part. The claim's scope is the
# family and the measured face; its falsification coordinate
# stands in the instrument.
# ---------------------------------------------------------------------------

GREEK_LOWER = 'αβγδεζηθικλμνξοπρςστυφχψω'
GREEK_CAPITAL = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
VOWELS = 'αεηιουω'
CAPITAL_VOWELS = 'ΑΕΗΙΟΥΩ'
ANGLES = ('180', 'cw90', 'ccw90')

LOWER_180_PAIRS = {'γ': 'λ', 'λ': 'γ', 'δ': 'ρ', 'ρ': 'δ'}
LOWER_180_SYMMETRIC = frozenset('οθχ')
LOWER_QUARTER_SYMMETRIC = frozenset('οχ')
CAPITAL_QUARTER_SYMMETRIC = frozenset('ΟΧ')

# The seated turn maps: {(case, angle): {letter: image}}.
# Self-symmetric letters enter as their own image; a letter
# absent from a map has NO image at that turn and blocks any
# transformation that would turn it.
TURN_MAPS = {
    ('lower', '180'): dict(LOWER_180_PAIRS,
                           **{c: c for c in LOWER_180_SYMMETRIC}),
    ('lower', 'cw90'): {c: c for c in LOWER_QUARTER_SYMMETRIC},
    ('lower', 'ccw90'): {c: c for c in LOWER_QUARTER_SYMMETRIC},
    ('capital', 'cw90'): {c: c for c in CAPITAL_QUARTER_SYMMETRIC},
    ('capital', 'ccw90'): {c: c for c in CAPITAL_QUARTER_SYMMETRIC},
}


def turn_tables():
    """The seated geometry, printed whole: for each case and
    angle, its pairs, its self-symmetric letters, and its
    absences — every letter accounted for."""
    out = {}
    alphabets = {'lower': GREEK_LOWER, 'capital': GREEK_CAPITAL}
    for (case, angle), m in sorted(TURN_MAPS.items()):
        pairs = sorted({tuple(sorted((a, b))) for a, b in m.items()
                        if a != b})
        symmetric = sorted(c for c, img in m.items() if c == img)
        absent = [c for c in alphabets[case] if c not in m]
        out['%s/%s' % (case, angle)] = {
            'pairs': pairs, 'symmetric': symmetric,
            'absent': absent}
    return out


# ---------------------------------------------------------------------------
# §TRANSFORMATIONS — the extended family, as functions.
#
# MECHANISM: a spec is a tuple whose head names the form; every
# turn carries its angle. ('permute', π) · ('turn_seats', seats,
# angle) · ('turn_all', angle) · ('turn_word', angle) — every
# glyph turned and the order reversed · ('compose', (T1, ...)).
# A turn demanded of a letter with no image at that angle blocks
# the transformation (None). The checker works on the lowercase
# maps; inputs are normalized by the bank's own preparation.
# ---------------------------------------------------------------------------

def _turn_char(ch, angle):
    img = TURN_MAPS[('lower', angle)].get(ch)
    if img is None:
        raise ValueError('no %s image: %r' % (angle, ch))
    return img


def apply_turn(word, spec):
    """Apply a stated transformation of the extended family to a
    normalized lowercase string; None if a demanded turn is
    blocked by a letter with no image at that angle."""
    kind = spec[0]
    try:
        if kind == 'permute':
            perm = spec[1]
            if sorted(perm) != list(range(len(word))):
                return None
            return ''.join(word[i] for i in perm)
        if kind == 'turn_seats':
            chars = list(word)
            for i in spec[1]:
                chars[i] = _turn_char(chars[i], spec[2])
            return ''.join(chars)
        if kind == 'turn_all':
            return ''.join(_turn_char(c, spec[1]) for c in word)
        if kind == 'turn_word':
            return ''.join(_turn_char(c, spec[1])
                           for c in reversed(word))
        if kind == 'compose':
            out = word
            for step in spec[1]:
                out = apply_turn(out, step)
                if out is None:
                    return None
            return out
    except (ValueError, IndexError):
        return None
    raise ValueError('unknown transformation form: %r' % (kind,))


# ---------------------------------------------------------------------------
# §THE CHECKER — the prior instrument's print, at the new turns.
#
# MECHANISM: the values are read from the living engine, every
# letter-table bank in SYSTEMS (the music weigher skipped, as in
# the prior checker — a pitch extraction, not a letter bank),
# with each weighing's coverage shown. The verdicts are the
# seated definition's three: DIPLOMATIC, VALUE-INVARIANT
# (excluded by the definition), DOES NOT APPLY.
# ---------------------------------------------------------------------------

def _values(word):
    """{bank: (value, letters_weighed)} — the prior checker's
    own mechanism, mirrored so the two prints are commensurable."""
    out = {}
    for name, spec in SYSTEMS.items():
        if 'weigher' in spec:
            continue
        r = weigh(word, name)
        cov = sum(len(letter) for letter, _v in r['breakdown'])
        if cov:
            out[name] = (r['value'], cov)
    return out


def turn_pair(a, b, spec):
    """Verify the diplomatic relation between Greek strings a
    and b under a stated transformation of the extended family,
    and return its full print as data (the prior checker's
    fields). Inputs are normalized by the bank's preparation;
    the print shows the normalized forms that were weighed."""
    a, b = _normalize_greek(a), _normalize_greek(b)
    transformed = apply_turn(a, spec)
    applies = transformed == b
    va, vb = _values(a), _values(b)
    banks = {}
    differing, invariant = [], []
    for name in sorted(set(va) | set(vb)):
        ea, eb = va.get(name), vb.get(name)
        banks[name] = {'a': ea, 'b': eb}
        if ea is not None and eb is not None:
            (differing if ea[0] != eb[0] else invariant).append(name)
    seats = [(i, ca, cb) for i, (ca, cb) in enumerate(zip(a, b))
             if ca != cb]
    if not applies:
        verdict = 'DOES NOT APPLY'
    elif differing:
        verdict = 'DIPLOMATIC'
    else:
        verdict = 'VALUE-INVARIANT — excluded by the definition'
    return {
        'a': a, 'b': b, 'spec': spec, 'applies': applies,
        'transformed': transformed, 'seats': seats,
        'banks': banks, 'differing_banks': differing,
        'invariant_banks': invariant, 'verdict': verdict,
        'tier': 'CONSTRUCTED — the relation is a house instrument '
                '(the founder\'s coinage, 2026-11-24), extended '
                'to the quarter-turns the same day',
    }


def render_turn_pair(result):
    """The pair's print, as lines — the prior checker's format."""
    lines = ['%s ⇄ %s' % (result['a'], result['b']),
             '  T = %r' % (result['spec'],),
             '  applies: %s (T(A) = %s)'
             % (result['applies'], result['transformed']),
             '  seats at which the strings differ: %s'
             % (', '.join('%d: %s→%s' % (i + 1, ca, cb)
                          for i, ca, cb in result['seats'])
                or 'none')]
    for name in sorted(result['banks']):
        e = result['banks'][name]
        fa = '%s (%d/%d letters)' % (e['a'][0], e['a'][1],
                                     len(result['a'])) if e['a'] \
            else '—'
        fb = '%s (%d/%d letters)' % (e['b'][0], e['b'][1],
                                     len(result['b'])) if e['b'] \
            else '—'
        mark = '  ≠' if name in result['differing_banks'] else ''
        lines.append('  %-14s A %-22s B %-22s%s' % (name, fa, fb,
                                                    mark))
    lines.append('  verdict: %s' % result['verdict'])
    return lines


# ---------------------------------------------------------------------------
# §THE CORPUS AND THE SWEEP.
#
# MECHANISM: the corpus is assembled from the house record and
# stated whole, in provenance groups, then normalized by the
# bank's preparation and deduplicated. Discovery tries the
# extended family's forms in order of simplicity — permutation;
# one seat turned, at each angle; all glyphs turned, at each
# angle; the word turned, at each angle; a seat turned then
# permuted; all glyphs turned then permuted — in both
# directions, recording the first form that carries one side to
# the other. A seat whose image is itself is never proposed as
# a carrying move.
# ---------------------------------------------------------------------------

CORPUS_RAW = [
    # the engine's Greek exhibits (pontifex/engine.py, greek_checks)
    'θέλημα', 'ἀλήθεια', 'πλοῖον', 'σκαμνόν', 'πειρατής', 'λόγος',
    'οζ',
    # the prior instrument's Greek corpus heads, lowered
    'ἀγαπη', 'βαβαλον',
    # house heads from the goal record: the Zero Point's word,
    # the MOMENTVVM head, and the Greek seam heads of the
    # twelve-tongues record (the Latin heads in Greek dress)
    'οὐδέν', 'ἀτμός', 'αξονεμε', 'κιρα', 'κελλ', 'λιβερτυ',
    'αβραηαδαβρα', 'ηερυραηα',
    # Greek heads of 777-REVISED and the day's essays
    'ζευς', 'θωθ', 'δελφοι', 'σεληνη', 'πνευμα', 'πυρ', 'νυξ',
    'καλος', 'τεχνη', 'σταυρος', 'σφιγξ', 'ηλιος', 'αρμονια',
    'ελευθερια', 'υιος', 'οινος', 'φωνηεντα', 'διφθογγος',
    # the Divine Nine vowel material: the seven vowels as single
    # letters, and the diphthong heads of the vowel record
    'α', 'ε', 'η', 'ι', 'ο', 'υ', 'ω',
    'αι', 'ει', 'οι', 'υι', 'αυ', 'ευ', 'ου', 'ηα', 'αε',
]

CORPUS = sorted({_normalize_greek(w) for w in CORPUS_RAW})


def _discover(a, b):
    """The simplest stated transformation of the extended family
    carrying a to b, or None — the prior discovery, widened over
    the three angles."""
    perm = find_permutation(a, b)
    if perm is not None:
        return ('permute', perm)
    singles = []
    for angle in ANGLES:
        m = TURN_MAPS[('lower', angle)]
        for i, ch in enumerate(a):
            img = m.get(ch)
            if img is not None and img != ch:
                turned = a[:i] + img + a[i + 1:]
                singles.append((angle, i, turned))
                if turned == b:
                    return ('turn_seats', (i,), angle)
        if apply_turn(a, ('turn_all', angle)) == b:
            return ('turn_all', angle)
        if apply_turn(a, ('turn_word', angle)) == b:
            return ('turn_word', angle)
    for angle, i, turned in singles:
        perm = find_permutation(turned, b)
        if perm is not None:
            return ('compose', (('turn_seats', (i,), angle),
                                ('permute', perm)))
    for angle in ANGLES:
        turned_all = apply_turn(a, ('turn_all', angle))
        if turned_all is not None:
            perm = find_permutation(turned_all, b)
            if perm is not None:
                return ('compose', (('turn_all', angle),
                                    ('permute', perm)))
    return None


def sweep_turns(corpus=None):
    """Sweep the corpus under the extended family. Returns
    (register, excluded) in the prior instrument's senses."""
    words = list(CORPUS if corpus is None else corpus)
    register, excluded = [], []
    for x in range(len(words)):
        for y in range(x + 1, len(words)):
            a, b = words[x], words[y]
            if len(a) != len(b) or a == b:
                continue
            spec = _discover(a, b) or _discover(b, a)
            if spec is None:
                continue
            src, dst = (a, b) if _discover(a, b) else (b, a)
            result = turn_pair(src, dst, spec)
            result['pair'] = (a, b)
            if result['verdict'] == 'DIPLOMATIC':
                register.append(result)
            else:
                excluded.append(result)
    return register, excluded


REGISTER, EXCLUDED = sweep_turns()

# The planted exhibits: strings planted to prove the lowercase
# hinges in the checker (the prior instrument's proving ground —
# its MO ⇄ OW and b ⇄ q were planted the same way). πυδ is a
# planted string, not a Greek word, and is labelled so wherever
# it prints.
PLANTED = [
    ('δ', 'ρ', ('turn_seats', (0,), '180')),
    ('γ', 'λ', ('turn_seats', (0,), '180')),
    ('πυρ', 'πυδ', ('turn_seats', (2,), '180')),
]


# ---------------------------------------------------------------------------
# §THE VOWEL-LANDING TABLES — the legend's clause, computed.
#
# MECHANISM: a letter LANDS ON A VOWEL when its seated image at
# that angle is a vowel letter. The tables are read straight off
# the seated maps, for both cases and every angle (the capitals'
# half-turn map is the prior instrument's symmetric set, restated
# here for the table's completeness). A landing is a CROSS
# landing when the letter landed from is not the vowel it lands
# on — the only landings the legend's clause could cash.
# ---------------------------------------------------------------------------

def vowel_landings():
    """{(case, angle): {'landings': [(letter, image)], 'cross':
    [(letter, image)]}} — every seated image that is a vowel,
    and the cross landings among them."""
    from .diplomatic import GREEK_CAPITAL_SYMMETRIC
    maps = dict(TURN_MAPS)
    maps[('capital', '180')] = {c: c for c in
                                GREEK_CAPITAL_SYMMETRIC}
    out = {}
    for (case, angle), m in sorted(maps.items()):
        vowels = VOWELS if case == 'lower' else CAPITAL_VOWELS
        landings = [(c, img) for c, img in sorted(m.items())
                    if img in vowels]
        out[(case, angle)] = {
            'landings': landings,
            'cross': [(c, img) for c, img in landings if c != img],
        }
    return out


# ---------------------------------------------------------------------------
# §CHECKS — the extension proves itself.
# ---------------------------------------------------------------------------

def diplomatic_turns_checks():
    """The check battery: the seated geometry's formal
    properties; the planted exhibits verified; the vowels'
    inertness; the exclusion clause at the new turns; the
    capitals impossibility restated over the extended family;
    the landing tables computed; the corpus register reproduced
    by a fresh sweep. Each entry: (name, passed, detail)."""
    checks = []

    # 1. THE GEOMETRY'S FORMAL PROPERTIES: the half-turn map is
    #    an involution; the quarter maps seat only fixed points
    #    (so CW and CCW agree seat for seat — direction has no
    #    glyph to bite on); the counts as derived and measured.
    m180 = TURN_MAPS[('lower', '180')]
    tables = turn_tables()
    counts = {k: (len(t['pairs']), len(t['symmetric']),
                  len(t['absent'])) for k, t in tables.items()}
    formal = (all(m180[m180[c]] == c for c in m180)
              and TURN_MAPS[('lower', 'cw90')]
              == TURN_MAPS[('lower', 'ccw90')]
              and TURN_MAPS[('capital', 'cw90')]
              == TURN_MAPS[('capital', 'ccw90')]
              and counts == {'lower/180': (2, 3, 18),
                             'lower/cw90': (0, 2, 23),
                             'lower/ccw90': (0, 2, 23),
                             'capital/cw90': (0, 2, 22),
                             'capital/ccw90': (0, 2, 22)})
    checks.append(('the geometry: the half-turn map an '
                   'involution; the quarter maps seat fixed '
                   'points only; counts — lowercase 180: 2 pairs '
                   '/ 3 symmetric / 18 absent (of 25); quarters: '
                   '0 / 2 / 23; capitals quarters: 0 / 2 / 22 '
                   '(of 24)', formal, counts))

    # 2. THE PLANTED EXHIBITS: both lowercase hinges and the
    #    planted word verify DIPLOMATIC, at the bank's own
    #    numbers (δ 4 ≠ ρ 100; γ 3 ≠ λ 30; πυρ 580 ≠ πυδ 484).
    planted = [turn_pair(a, b, spec) for a, b, spec in PLANTED]
    vals = [(r['banks']['greek']['a'][0], r['banks']['greek']['b'][0])
            for r in planted]
    checks.append(('planted exhibits: δ ⇄ ρ (4 ≠ 100), γ ⇄ λ '
                   '(3 ≠ 30), πυρ ⇄ πυδ (580 ≠ 484) — all '
                   'DIPLOMATIC under the half-turn',
                   all(r['verdict'] == 'DIPLOMATIC' for r in planted)
                   and vals == [(4, 100), (3, 30), (580, 484)],
                   [(r['a'], r['b'], r['verdict']) for r in planted]))

    # 3. THE VOWELS' INERTNESS: of the seven vowels, only ο has
    #    any image at any angle, and its only image is itself —
    #    no vowel turns onto another letter, and no consonant
    #    turns onto a vowel, anywhere in the seated maps.
    vowel_images = {v: {ang: TURN_MAPS[('lower', ang)].get(v)
                        for ang in ANGLES} for v in VOWELS}
    consonant_to_vowel = [(c, ang, img) for (case, ang), m in
                          TURN_MAPS.items() if case == 'lower'
                          for c, img in m.items()
                          if c not in VOWELS and img in VOWELS]
    checks.append(('the vowels\' inertness: only ο carries an '
                   'image (itself, at every angle); the other '
                   'six vowels are imageless at every angle; no '
                   'consonant\'s image is a vowel',
                   vowel_images['ο'] == {ang: 'ο' for ang in ANGLES}
                   and all(vowel_images[v][ang] is None
                           for v in VOWELS if v != 'ο'
                           for ang in ANGLES)
                   and not consonant_to_vowel,
                   vowel_images))

    # 4. THE EXCLUSION CLAUSE AT THE NEW TURNS: a pure
    #    permutation of Greek letters still interlocks and is
    #    still refused (αβ ⇄ βα, 3 = 3); and a turn of
    #    self-symmetric letters alone is a permutation in
    #    disguise (οχο turned whole is οχο, 670 = 670, refused).
    perm = find_permutation('αβ', 'βα')
    r1 = turn_pair('αβ', 'βα', ('permute', perm))
    r2 = turn_pair('οχο', 'οχο', ('turn_word', '180'))
    checks.append(('exclusion in code: αβ ⇄ βα by permutation '
                   'refused as value-invariant; οχο by the '
                   'word-turn of symmetric letters refused the '
                   'same way',
                   r1['applies']
                   and r1['verdict'].startswith('VALUE-INVARIANT')
                   and r2['applies']
                   and r2['verdict'].startswith('VALUE-INVARIANT'),
                   (r1['verdict'], r2['verdict'])))

    # 5. BLOCKED TURNS REFUSED: a turn demanded of an imageless
    #    letter does not apply (υ at any angle; α at the
    #    half-turn) — the absence is enforced, not skipped.
    r3 = turn_pair('α', 'ο', ('turn_seats', (0,), '180'))
    r4 = turn_pair('υ', 'υ', ('turn_all', 'cw90'))
    checks.append(('blocked turns refused: α has no half-turn '
                   'image and υ no quarter-turn image — both '
                   'transformations DO NOT APPLY',
                   r3['verdict'] == 'DOES NOT APPLY'
                   and r4['verdict'] == 'DOES NOT APPLY',
                   (r3['transformed'], r4['transformed'])))

    # 6. THE CAPITALS IMPOSSIBILITY, restated over the extended
    #    family: at every angle now seated, a capital's only
    #    image is itself or nothing — so no admissible
    #    transformation changes any capital letter, and by the
    #    anagram theorem no capital pair can part in value.
    from .diplomatic import GREEK_CAPITAL_SYMMETRIC
    cap_maps = {ang: TURN_MAPS[('capital', ang)]
                for ang in ('cw90', 'ccw90')}
    cap_maps['180'] = {c: c for c in GREEK_CAPITAL_SYMMETRIC}
    checks.append(('the capitals impossibility over the '
                   'extended family: at 180°, 90° CW and 90° '
                   'CCW every capital\'s seated image is itself '
                   'or nothing — no transformation changes a '
                   'letter, so no pair can be diplomatic',
                   all(img == c for m in cap_maps.values()
                       for c, img in m.items()),
                   {ang: sorted(m) for ang, m in cap_maps.items()}))

    # 7. THE LANDING TABLES: counterclockwise and clockwise
    #    land alike — the only landings on vowels, in either
    #    case at any angle, are vowels landing on themselves,
    #    and the cross-landing register is empty everywhere.
    land = vowel_landings()
    checks.append(('the vowel-landing tables: cross landings '
                   'EMPTY in both cases at every angle; the '
                   'only landings are ο on itself (lowercase, '
                   'all angles; capitals, all angles) and Η Ι '
                   'on themselves (capitals, half-turn) — CW and '
                   'CCW yields identical',
                   all(not e['cross'] for e in land.values())
                   and land[('lower', 'ccw90')]['landings']
                   == land[('lower', 'cw90')]['landings']
                   == [('ο', 'ο')]
                   and land[('lower', '180')]['landings']
                   == [('ο', 'ο')]
                   and land[('capital', '180')]['landings']
                   == [('Η', 'Η'), ('Ι', 'Ι'), ('Ο', 'Ο')],
                   {str(k): v['landings'] for k, v in land.items()}))

    # 8. THE CORPUS REGISTER REPRODUCED by a fresh sweep: the
    #    51 heads of the house corpus interlock NOWHERE under
    #    the extended family — no exhibits, and no exclusions
    #    either (the corpus holds no anagram pair and no
    #    self-turn interlock for the definition to refuse).
    fresh_reg, fresh_exc = sweep_turns()
    checks.append(('the corpus register reproduced: 51 heads '
                   'swept, 0 exhibits seated, 0 exclusions — the '
                   'hinges exist and no two house heads hang on '
                   'them',
                   len(fresh_reg) == 0 and len(fresh_exc) == 0
                   and len(CORPUS) == 51,
                   (len(CORPUS), len(fresh_reg), len(fresh_exc))))

    return checks


if __name__ == '__main__':
    print('THE DIPLOMATIC KEY, EXTENDED — the Greek turns')
    for key, t in turn_tables().items():
        print('\n%s: pairs %s · symmetric %s · absent %s'
              % (key, t['pairs'], ''.join(t['symmetric']),
                 ''.join(t['absent'])))
    print('\nPLANTED EXHIBITS')
    for a, b, spec in PLANTED:
        print('\n'.join(render_turn_pair(turn_pair(a, b, spec))))
        print()
    print('CORPUS REGISTER: %d exhibits, %d exclusions '
          '(51 heads swept)' % (len(REGISTER), len(EXCLUDED)))
    print('\nVOWEL LANDINGS')
    for key, e in vowel_landings().items():
        print(' ', key, 'landings', e['landings'],
              '· cross', e['cross'])
    print('\nCHECKS')
    for name, passed, detail in diplomatic_turns_checks():
        print(' ', 'PASS' if passed else 'FAIL', name)
        if not passed:
            print('   detail:', detail)


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
