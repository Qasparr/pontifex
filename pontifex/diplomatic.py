#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — diplomatic.py — the Diplomatic Key
# (the relation instrument: equality of letters under a stated
# transformation, inequality of values on its face)
#
# Epigraph: "Could be a key itself though. A diplomatic key."
# — the founder, 2026-11-24, of the found exhibit ROMAN ⇄ NOWAR.
#
# Thelemic date: XXIV day of November, dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The name PONTIFEX ("bridge-builder") was proposed by the scribe and approved
# by the author's red pen, 2026-10-07. The doctrine is the author's; the
# mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: that beside the bridge (a shared number across two
#     honest banks) there stands a second relation-kind: two strings
#     that interlock EXACTLY under a stated letter-transformation —
#     a half-turn of glyphs, a permutation of seats, or their
#     composition — while weighing DIFFERENTLY, neither side's
#     values surrendered, neither side's letters altered beyond the
#     stated turn. The founder named it a diplomatic key, and
#     glossed its posture the same minute: "Like the Stalemate
#     strategy by defense of G4" — the position arranged so exactly
#     that the stronger party cannot convert it.
#   Method: state the transformation family and the definition
#     formally, with its exclusion clause; derive the half-turn
#     letter geometry of the Latin and Greek capital alphabets
#     (and the Latin lowercase) from the letterforms' design
#     geometry, corroborated by bitmap rotation in a named
#     typeface with the typeface's deviations printed; build a
#     checker that verifies a declared transformation and prints
#     both sides' values across every bank; sweep the house corpus
#     for pairs and seat what the definition admits.
#   Observation: the corpus yields exactly two diplomatic pairs,
#     both hanging on the one capital hinge Latin carries, M ↔ W;
#     one further pair interlocks by permutation alone and is
#     excluded by the definition itself, as the theorem requires —
#     a pure permutation is value-invariant in every additive bank,
#     so diplomacy requires geometry: at least one glyph must
#     actually turn.
#   Result: the checker and the register below. The relation is
#     tier CONSTRUCTED — a house instrument, the founder's coinage
#     of 2026-11-24 — with its exhibits individually sourced. It
#     builds ONE exhibit-class of legend piece (ii), the rotation:
#     the half-turn. It does not build the rotation itself, whose
#     stated direction (counterclockwise, to the Greek vowels) a
#     half-turn cannot exhibit, being direction-indifferent. That
#     boundary is printed in the instrument at full size.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Diplomatic Key — the relation instrument.

DOCTRINE: the house knows the bridge — two words weighing the
same across two honest banks. The founder's coinage of 2026-11-24
names a second relation. A DIPLOMATIC PAIR is two strings A, B
and a stated letter-transformation T, drawn from the family below,
such that T(A) = B exactly, while A and B weigh DIFFERENTLY in at
least one named bank. Neither side's values change; neither side
concedes a point; the relation is the key. The founder's gloss,
verbatim: "Like the Stalemate strategy by defense of G4" — the
position arranged so exactly that the stronger party cannot
convert it; no value surrendered, no victory claimed. ("Defense
of G4" is his reference; its expansion is his to give and stands
unexpanded here.)

THE TRANSFORMATION FAMILY. A transformation is built from two
moves and their composition:
  ROTATION — a letter is replaced by its half-turn image under
    the letter geometry of §GEOMETRY below (M → W; a self-
    symmetric letter — N, O, S — is its own image). A letter with
    no image blocks any transformation that would turn it.
  PERMUTATION — the seats are reordered by a stated permutation.
The named forms: ('permute', π) · ('rotate_seats', seats) ·
('rotate_all',) · ('rotate_word',) — every glyph turned and the
order reversed, the physical half-turn of a written word — and
('compose', (T1, T2, ...)), the forms applied in sequence.

THE EXCLUSION CLAUSE (the definition's teeth). If T(A) = B but A
and B weigh the same in every bank where both weigh, the pair is
NOT diplomatic: it is a bridge-candidate or a triviality, and the
register excludes it, printing the exclusion. The clause has a
theorem behind it: every bank this engine holds is an additive
letter bank — a word's value is a function of its letter
multiset — so a PURE PERMUTATION never changes any value, in any
bank, ever. Diplomacy therefore requires geometry: at least one
glyph must actually turn, changing the multiset (M out, W in),
before two strings can interlock without weighing the same.

TIER: the relation is CONSTRUCTED — a house instrument, coined
2026-11-24. Its exhibits are individually sourced: Exhibit 1 was
found by the founder himself and verified at the desk the same
morning ("unrelated to my knowledge or intention but
ROMAN==NOWAR", 10:45 EST — the claim as written fails in both
Latin banks, and the relation underneath it is exact).
"""

from .engine import SYSTEMS, weigh

# ---------------------------------------------------------------------------
# §GEOMETRY — the half-turn letter tables.
#
# MECHANISM: the tables below are DERIVED from the letterforms'
# design geometry — the stroke figure of each letter, read under a
# half-turn (180° rotation). A letter is SELF-SYMMETRIC when its
# figure is invariant under the turn (H: two stems and a bar,
# each landing on itself; S and Z: the two-stroke zigzag figures
# with point symmetry; Ν, Ο, Χ, Ζ and kin in Greek). Two letters
# form a PAIR when one's figure, turned, is the other's (M and W:
# the same four-stroke figure, vertex down and vertex up). A
# letter whose turned figure is no letter of its alphabet has NO
# IMAGE, and the absence is data: it is printed in the instrument
# and it blocks transformations in the checker.
#
# CORROBORATION (a measurement, printed in the instrument with
# its coordinates): the seated seats were checked by bitmap
# rotation in DejaVu Sans (glyphs centred by bounding box, turned
# 180°, ink-overlap scored against every letter of the alphabet).
# The lowercase pairs score 0.94–0.99 and the self-symmetric
# letters 0.61–0.97 — the typeface agrees with the design
# geometry. Two typeface coordinates stand against naive reading
# and are printed, not smoothed: (1) DejaVu Sans draws M with a
# half-depth vertex and W with a full-height peak, so its bitmaps
# score the M ↔ W turn at only 0.436 — yet W is still rotated-M's
# best NON-SELF match and M is rotated-W's best match outright:
# the pair is the typeface's nearest turn, and the design figure
# (four strokes, vertex down ↔ vertex up) is exact; (2) DejaVu's
# Θ carries its bar a hair off centre, so turned-Θ scores 0.835
# against Ο and 0.823 against Θ itself — the bar penalises the
# self-match twice; Θ is seated self-symmetric on its figure
# (oval and centred bar), the coordinate printed beside it.
# Two lowercase absences the measurement sharpened: m and w are
# NOT a pair (m carries a stem, w carries none — the figures
# differ, and the bitmaps agree: no match), and l is not seated
# self-symmetric (its foot breaks the figure in the general
# letterform, though DejaVu's nearly bare stem scores 0.929
# against itself — a typeface coordinate, not a seat).
#
# THE GREEK ABSENCE THAT MATTERS: Greek capitals carry NO pair at
# all. Μ's turned figure would be a W-form, and Greek has no such
# letter. The founder's found exhibit turns on M ↔ W — a hinge
# only Latin carries. Cross-script diplomacy by rotation is
# therefore impossible where the partner seat does not exist in
# the target script, and within Greek capitals every admissible
# transformation is value-invariant (self-symmetric turns change
# no letter; permutations change no multiset): no diplomatic
# pair can exist in Greek capitals under this family. Latin
# capitals hang their whole diplomacy on the one hinge, M ↔ W;
# the lowercase widens the hinge set to b ↔ q, d ↔ p, n ↔ u.
# ---------------------------------------------------------------------------

LATIN_CAPITAL_PAIRS = {'M': 'W', 'W': 'M'}
LATIN_CAPITAL_SYMMETRIC = frozenset('HINOSXZ')
LATIN_LOWER_PAIRS = {'b': 'q', 'q': 'b', 'd': 'p', 'p': 'd',
                     'n': 'u', 'u': 'n'}
LATIN_LOWER_SYMMETRIC = frozenset('osxz')
GREEK_CAPITAL_PAIRS = {}
GREEK_CAPITAL_SYMMETRIC = frozenset('ΖΗΘΙΝΞΟΦΧ')

_ALPHABETS = (
    ('Latin capitals', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
     LATIN_CAPITAL_PAIRS, LATIN_CAPITAL_SYMMETRIC),
    ('Latin lowercase', 'abcdefghijklmnopqrstuvwxyz',
     LATIN_LOWER_PAIRS, LATIN_LOWER_SYMMETRIC),
    ('Greek capitals', 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',
     GREEK_CAPITAL_PAIRS, GREEK_CAPITAL_SYMMETRIC),
)


def _build_rotate():
    """Assemble the one rotation map from the per-alphabet tables.

    MECHANISM: pairs enter in both directions (the map is an
    involution by construction); self-symmetric letters enter as
    their own image. The alphabets are disjoint in codepoints, so
    the union cannot collide.
    """
    rot = {}
    for _name, _letters, pairs, symmetric in _ALPHABETS:
        for a, b in pairs.items():
            rot[a] = b
        for ch in symmetric:
            rot[ch] = ch
    return rot


ROTATE = _build_rotate()


def rotate_letter(ch):
    """The half-turn image of one letter, or None where the
    letter's turned figure is no letter of its alphabet."""
    return ROTATE.get(ch)


def geometry_tables():
    """The derived geometry, printed whole: for each alphabet,
    its pairs, its self-symmetric letters, and its absences —
    the letters with no rotation partner, named, not skipped."""
    out = {}
    for name, letters, pairs, symmetric in _ALPHABETS:
        pair_letters = set(pairs)
        absent = [c for c in letters
                  if c not in pair_letters and c not in symmetric]
        out[name] = {
            'pairs': sorted(set(tuple(sorted(p)) for p in
                                pairs.items())),
            'symmetric': sorted(symmetric),
            'absent': absent,
        }
    return out


# ---------------------------------------------------------------------------
# §TRANSFORMATIONS — the family, as functions.
#
# MECHANISM: a transformation spec is a tuple whose head names
# the form. apply_transform returns the transformed string, or
# None when a rotation the spec demands is blocked by a letter
# with no image. A spec that changes nothing is not a
# transformation of anything: rotate_seats on a self-symmetric
# seat is a no-op at that seat and the discovery below never
# proposes it as a pair's carrying move.
# ---------------------------------------------------------------------------

def _rotate_char(ch):
    img = ROTATE.get(ch)
    if img is None:
        raise ValueError('no half-turn image: %r' % ch)
    return img


def apply_transform(word, spec):
    """Apply a stated transformation; None if a demanded turn is
    blocked by a letter with no half-turn image."""
    kind = spec[0]
    try:
        if kind == 'permute':
            perm = spec[1]
            if sorted(perm) != list(range(len(word))):
                return None
            return ''.join(word[i] for i in perm)
        if kind == 'rotate_seats':
            chars = list(word)
            for i in spec[1]:
                chars[i] = _rotate_char(chars[i])
            return ''.join(chars)
        if kind == 'rotate_all':
            return ''.join(_rotate_char(c) for c in word)
        if kind == 'rotate_word':
            return ''.join(_rotate_char(c) for c in reversed(word))
        if kind == 'compose':
            out = word
            for step in spec[1]:
                out = apply_transform(out, step)
                if out is None:
                    return None
            return out
    except (ValueError, IndexError):
        return None
    raise ValueError('unknown transformation form: %r' % (kind,))


def find_permutation(a, b):
    """The stable left-to-right permutation carrying a to b, or
    None when b is not an anagram of a. Stable: each letter of b
    takes the leftmost still-unused matching seat of a, so the
    stated permutation is reproducible by hand."""
    if len(a) != len(b) or sorted(a) != sorted(b):
        return None
    used = [False] * len(a)
    perm = []
    for ch in b:
        for i, ca in enumerate(a):
            if not used[i] and ca == ch:
                used[i] = True
                perm.append(i)
                break
    return tuple(perm)


# ---------------------------------------------------------------------------
# §THE CHECKER — verify a declared pair and print both sides.
#
# MECHANISM: the values are read from the living engine, every
# letter-table bank in SYSTEMS (the music weigher is skipped: it
# is a pitch extraction, not a letter bank, and diplomacy is a
# letter relation). Coverage counts the letters a bank actually
# weighed — a bank may weigh a word partially (W is silent in
# Agrippa), and the print shows the coverage rather than letting
# a partial sum pose as a total.
# ---------------------------------------------------------------------------

def _values(word):
    """{bank: (value, letters_weighed)} for every letter bank
    that weighs at least one letter of the word."""
    out = {}
    for name, spec in SYSTEMS.items():
        if 'weigher' in spec:
            continue
        r = weigh(word, name)
        cov = sum(len(letter) for letter, _v in r['breakdown'])
        if cov:
            out[name] = (r['value'], cov)
    return out


def diplomatic_pair(a, b, spec):
    """Verify the diplomatic relation between a and b under the
    stated transformation, and return its full print as data:
    whether the transformation applies, the seats it touches,
    both sides' values across the banks with their coverage, the
    banks where the values differ, and the verdict under the
    definition — DIPLOMATIC, VALUE-INVARIANT (the exclusion
    clause), or DOES NOT APPLY."""
    transformed = apply_transform(a, spec)
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
                '(the founder\'s coinage, 2026-11-24); exhibits '
                'individually sourced',
    }


def render_pair(result):
    """The pair's print, as lines: the transformation, the seats,
    both sides' values bank by bank with coverage, the verdict."""
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
# §THE SWEEP — the corpus and the discovery of pairs.
#
# MECHANISM: the corpus is the house's own word-hoard, stated
# whole: the shared corpus heads of the twelve-tongues sweep
# (HERU-RA-HA's hyphen dropped, the house convention — a
# separator, not a letter), the day's exhibits, and the head
# words of the day's instruments and roads. Discovery tries the
# family's forms in order of simplicity — permutation; one seat
# turned; every glyph turned; the physical word-turn; then the
# two compositions — in both directions, and records the first
# form that carries one side to the other. A pair the definition
# admits enters the REGISTER; a pair that interlocks but weighs
# the same everywhere enters EXCLUDED, printed with its reason —
# the exclusion count is part of the yield, not a footnote.
# ---------------------------------------------------------------------------

CORPUS = [
    # the shared corpus heads (twelve-tongues sweep)
    'AXONEME', 'OZ', 'TRVVTH', 'THELEMA', 'AGAPE', 'BABALON',
    'HERURAHA', 'ABRAHADABRA', 'QIRA', 'LIBERTY', 'CELL',
    # the day's exhibits (2026-11-24)
    'ROMAN', 'NOWAR', 'ROWAN',
    # the instruments' and roads' head words
    'VESTIGATOR', 'TABVLA', 'DIPLOMATIC', 'PONTIFEX', 'MAGVS',
    'SPHINX', 'MEDVSA', 'COPTIC', 'ARAMAIC', 'ARMENIAN',
    'HALEHAME', 'GEEZ', 'SANSKRIT', 'PHOENICIAN', 'STALEMATE',
    'LIBER',
    # the Greek heads, in the capitals the geometry reads
    'ΘΕΛΗΜΑ', 'ΑΓΑΠΗ', 'ΒΑΒΑΛΟΝ', 'ΟΖ',
]


def _discover(a, b):
    """The simplest stated transformation carrying a to b, or
    None. Forms in order: permutation; one seat turned; all
    glyphs turned; the word turned whole; a seat turned then
    permuted; all glyphs turned then permuted. A seat whose
    image is itself is never proposed as a carrying move — it
    changes nothing, and a transformation that changes nothing
    carries nothing."""
    perm = find_permutation(a, b)
    if perm is not None:
        return ('permute', perm)
    singles = []
    for i, ch in enumerate(a):
        img = ROTATE.get(ch)
        if img is not None and img != ch:
            turned = a[:i] + img + a[i + 1:]
            singles.append((i, turned))
            if turned == b:
                return ('rotate_seats', (i,))
    if apply_transform(a, ('rotate_all',)) == b:
        return ('rotate_all',)
    if apply_transform(a, ('rotate_word',)) == b:
        return ('rotate_word',)
    for i, turned in singles:
        perm = find_permutation(turned, b)
        if perm is not None:
            return ('compose', (('rotate_seats', (i,)),
                                ('permute', perm)))
    turned_all = apply_transform(a, ('rotate_all',))
    if turned_all is not None:
        perm = find_permutation(turned_all, b)
        if perm is not None:
            return ('compose', (('rotate_all',),
                                ('permute', perm)))
    return None


def sweep(corpus=None):
    """Sweep the corpus for diplomatic pairs. Returns
    (register, excluded): the pairs the definition admits, and
    the pairs that interlock under a stated transformation but
    weigh the same in every bank — excluded by the definition,
    printed, counted."""
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
            result = diplomatic_pair(src, dst, spec)
            result['pair'] = (a, b)
            if result['verdict'] == 'DIPLOMATIC':
                register.append(result)
            else:
                excluded.append(result)
    return register, excluded


def _seat_register():
    """Seat the register with Exhibit 1 designated: ROMAN ⇄ NOWAR
    is the founder's found exhibit, seated first by his coinage —
    not by discovery order (its own halves, ROMAN ⇄ ROWAN, were
    found by the same sweep and stand as Exhibit 2)."""
    register, excluded = sweep()

    def key(entry):
        pair = set(entry['pair'])
        return 0 if pair == {'ROMAN', 'NOWAR'} else 1

    register.sort(key=key)
    for n, entry in enumerate(register, 1):
        entry['exhibit'] = n
    return register, excluded


REGISTER, EXCLUDED = _seat_register()

# Exhibit 1's transformation, stated once, in the direction the
# founder found it: ROMAN, turned at its centre seat (M → W, the
# half-turn pair), then permuted, reads NOWAR.
EXHIBIT_1_SPEC = ('compose', (('rotate_seats', (2,)),
                              ('permute', (4, 1, 2, 3, 0))))


# ---------------------------------------------------------------------------
# §CHECKS — the instrument proves itself.
# ---------------------------------------------------------------------------

def diplomatic_checks():
    """The check battery: the found exhibit recomputed; the
    geometry's formal properties; Exhibit 1 verified under its
    stated transformation; planted pairs passing; planted
    non-pairs and planted value-invariant pairs refused by the
    definition in code; the register reproduced by a fresh sweep.
    Each entry: (name, passed, detail)."""
    checks = []

    # 1. THE FOUND EXHIBIT RECOMPUTED: the founder's claim as
    #    written (ROMAN == NOWAR) fails in both Latin banks; the
    #    numbers are the desk's of 10:45 EST, recomputed here.
    ex = (weigh('ROMAN', 'latin_ordinal')['value'],
          weigh('ROMAN', 'agrippa')['value'],
          weigh('NOWAR', 'latin_ordinal')['value'],
          weigh('NOWAR', 'agrippa')['value'],
          weigh('ROWAN', 'latin_ordinal')['value'],
          weigh('ROWAN', 'agrippa')['value'])
    checks.append(('the found exhibit recomputed: ROMAN 61/201, '
                   'NOWAR 71/171, ROWAN 71/171 — the claim as '
                   'written fails, the relation underneath exact',
                   ex == (61, 201, 71, 171, 71, 171), ex))

    # 2. THE GEOMETRY'S FORMAL PROPERTIES: the rotation map is
    #    an involution; self-symmetric letters are its fixed
    #    points; pairs and symmetric seats are disjoint; the
    #    counts per alphabet as derived.
    geo = geometry_tables()
    counts = {name: (len(t['pairs']), len(t['symmetric']),
                     len(t['absent']))
              for name, t in geo.items()}
    formal = (all(ROTATE[ROTATE[c]] == c for c in ROTATE)
              and all(ROTATE[c] == c
                      for t in geo.values() for c in t['symmetric'])
              and counts == {'Latin capitals': (1, 7, 17),
                             'Latin lowercase': (3, 4, 16),
                             'Greek capitals': (0, 9, 15)})
    checks.append(('the geometry: an involution with the derived '
                   'counts (Latin capitals 1 pair / 7 symmetric / '
                   '17 absent; lowercase 3 / 4 / 16; Greek 0 / 9 '
                   '/ 15)', formal, counts))

    # 3. THE HINGE AND THE GREEK ABSENCE: M ↔ W seated both ways;
    #    Μ has no image; no Greek capital has a partner.
    hinge = (ROTATE.get('M') == 'W' and ROTATE.get('W') == 'M'
             and rotate_letter('Μ') is None
             and not GREEK_CAPITAL_PAIRS)
    checks.append(('the hinge M ↔ W seated; Μ imageless; Greek '
                   'capitals carry no pair', hinge,
                   (ROTATE.get('M'), ROTATE.get('W'),
                    rotate_letter('Μ'))))

    # 4. EXHIBIT 1 VERIFIED under its stated transformation:
    #    centre seat, half-turn, then permutation; values differ
    #    in both Latin banks (+10 ordinal, −30 Agrippa).
    r1 = diplomatic_pair('ROMAN', 'NOWAR', EXHIBIT_1_SPEC)
    deltas = (r1['banks']['latin_ordinal']['b'][0]
              - r1['banks']['latin_ordinal']['a'][0],
              r1['banks']['agrippa']['b'][0]
              - r1['banks']['agrippa']['a'][0])
    mid = apply_transform('ROMAN', EXHIBIT_1_SPEC[1][0])
    mid_seats = [(i, ca, cb) for i, (ca, cb)
                 in enumerate(zip('ROMAN', mid)) if ca != cb]
    checks.append(('Exhibit 1: ROMAN ⇄ NOWAR verifies under '
                   'compose(turn seat 3, permute) — the turn '
                   'lands on ROWAN at the one seat (3: M→W), '
                   'deltas +10 ordinal / −30 Agrippa, verdict '
                   'DIPLOMATIC',
                   r1['verdict'] == 'DIPLOMATIC'
                   and mid == 'ROWAN'
                   and mid_seats == [(2, 'M', 'W')]
                   and deltas == (10, -30),
                   (r1['verdict'], mid, mid_seats, deltas)))

    # 5. PLANTED PAIR, the physical word-turn: MO turned whole
    #    reads OW, and the turn changes the multiset (M out,
    #    W in), so the values part (28 → 38 ordinal).
    r2 = diplomatic_pair('MO', 'OW', ('rotate_word',))
    checks.append(('planted pair: MO ⇄ OW by the word-turn, '
                   'DIPLOMATIC (28 ≠ 38 ordinal)',
                   r2['verdict'] == 'DIPLOMATIC'
                   and r2['banks']['latin_ordinal']['a'][0] == 28
                   and r2['banks']['latin_ordinal']['b'][0] == 38,
                   (r2['verdict'], r2['transformed'])))

    # 6. PLANTED PAIR, the lowercase hinge: b turned is q, and
    #    the single letters weigh apart (2 ≠ 17 ordinal).
    r3 = diplomatic_pair('b', 'q', ('rotate_seats', (0,)))
    checks.append(('planted pair: b ⇄ q by the seat-turn, '
                   'DIPLOMATIC (2 ≠ 17 ordinal)',
                   r3['verdict'] == 'DIPLOMATIC',
                   (r3['verdict'], r3['transformed'])))

    # 7. THE EXCLUSION CLAUSE IN CODE, first form: a pure
    #    permutation applies exactly and is still refused —
    #    ROWAN ⇄ NOWAR weighs the same in every bank, as the
    #    anagram theorem requires.
    perm = find_permutation('ROWAN', 'NOWAR')
    r4 = diplomatic_pair('ROWAN', 'NOWAR', ('permute', perm))
    checks.append(('exclusion in code: ROWAN ⇄ NOWAR applies by '
                   'permutation and is refused — value-invariant '
                   'in every bank',
                   r4['applies'] and not r4['differing_banks']
                   and r4['verdict'].startswith('VALUE-INVARIANT'),
                   (r4['applies'], r4['verdict'])))

    # 8. THE EXCLUSION CLAUSE, second form: the word-turn on
    #    self-symmetric letters alone is a permutation in
    #    disguise — NO turned whole is ON, and 29 = 29 refuses it.
    r5 = diplomatic_pair('NO', 'ON', ('rotate_word',))
    checks.append(('exclusion in code: NO ⇄ ON by the word-turn '
                   'of self-symmetric letters — applies, weighs '
                   '29 = 29, refused',
                   r5['applies']
                   and r5['verdict'].startswith('VALUE-INVARIANT'),
                   (r5['applies'], r5['verdict'])))

    # 9. PLANTED NON-PAIRS REFUSED: ROMAN is no anagram of
    #    NOWAR (the permutation the pair would need does not
    #    exist, and the stated one lands on NOMAR); an identity
    #    is no diplomacy.
    r6 = diplomatic_pair('ROMAN', 'NOWAR',
                         ('permute', (4, 1, 2, 3, 0)))
    r7 = diplomatic_pair('CELL', 'CELL', ('permute', (0, 1, 2, 3)))
    checks.append(('planted non-pairs refused: ROMAN under '
                   'permutation alone does not reach NOWAR; '
                   'CELL ⇄ CELL is a triviality, not a pair',
                   r6['verdict'] == 'DOES NOT APPLY'
                   and r6['transformed'] == 'NOMAR'
                   and r7['verdict'].startswith('VALUE-INVARIANT'),
                   (r6['transformed'], r7['verdict'])))

    # 10. THE REGISTER REPRODUCED by a fresh sweep of the
    #     corpus: exactly the two seated pairs, Exhibit 1
    #     designated, and exactly one exclusion.
    fresh_reg, fresh_exc = sweep()
    seated = [(e['a'], e['b']) for e in REGISTER]
    checks.append(('the register reproduced: 2 pairs seated '
                   '(Exhibit 1 ROMAN ⇄ NOWAR; Exhibit 2 ROMAN ⇄ '
                   'ROWAN), 1 exclusion (the pair NOWAR ⇄ ROWAN, '
                   'found in corpus order, refused as '
                   'value-invariant)',
                   len(fresh_reg) == 2 and len(fresh_exc) == 1
                   and seated == [('ROMAN', 'NOWAR'),
                                  ('ROMAN', 'ROWAN')]
                   and [(e['a'], e['b']) for e in fresh_exc]
                   == [('NOWAR', 'ROWAN')],
                   (seated, [(e['a'], e['b']) for e in fresh_exc])))

    return checks


if __name__ == '__main__':
    print('THE DIPLOMATIC KEY — the register as swept')
    for entry in REGISTER:
        print('\nEXHIBIT %d' % entry['exhibit'])
        print('\n'.join(render_pair(entry)))
    for entry in EXCLUDED:
        print('\nEXCLUDED BY THE DEFINITION')
        print('\n'.join(render_pair(entry)))
    print('\nCHECKS')
    for name, passed, detail in diplomatic_checks():
        print(' ', 'PASS' if passed else 'FAIL', name)
        if not passed:
            print('   detail:', detail)


# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
