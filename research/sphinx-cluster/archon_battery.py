#!/usr/bin/env python3
# =============================================================================
# 93 — ARCHON_BATTERY.PY
# THE ARCHON BATTERY — every computation behind THE-ARCHON-BATTERY.md,
# run in one scripted pass on the house engine (pontifex) and the house
# solfeggio file (resonance/resonance/core/notes.py). Nothing in the
# instrument is hand-copied: each figure below is printed by this script
# from the banks themselves, so the audit can be re-run digit for digit.
#
# Commissioned by the founder, 2026-11-24: "Run the reduction and
# triangulation battery" — with Leg 5 (the cross quarters, the key
# strings VYX · RRYYZZ · WVII/VVII, the founder's named claim and its
# killing coordinates, the 4→8 fold he named 'the crazy 88') and Leg 6
# (the twelve-tongues sweep) added at his word the same evening.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =============================================================================
"""THE ARCHON BATTERY — computation pass.

DOCTRINE: the battery computes CANDIDATES for the founder's pen. It
seats nothing. Every value is taken from the engine's banks at run
time (weigh()), never typed in as a literal, except the Nine's own
values — and those are asserted against the engine first (S0), so a
drift in either direction fails loudly here before it can drift in
the instrument.

MECHANISM: sections S0–S7 mirror the instrument's legs:
  S0 calibration + the Nine asserted against the Greek bank
  S1 LEG 1 — reduction chains, mod-9, decade factorization
  S2 LEG 2 — the Trinity weighing per vowel + the Cube check
  S3 LEG 3 — triangulation (sketch frame, class frame, solfeggio,
       tridecagram traversal, abc_notes)
  S4 LEG 4 — the corpus's archon controls (ἄρχων / ARCHON)
  S5 LEG 5 — hybrid-mark census, the cross test, the key strings
  S6 LEG 5x — the fold (the four, the eight, the eighty-eight)
  S7 LEG 6 — the twelve-tongues sweep
"""

import sys, os, json, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/workspace/pontifex'))
sys.path.insert(0, os.path.expanduser('~/workspace/resonance'))

from pontifex.engine import weigh, weigh_via_hebrew_fallback, SYSTEMS
from pontifex.tables import (GREEK, LATIN_ORDINAL, AGRIPPA, HEBREW,
                             ARABIC_ABJAD, ARMENIAN, COPTIC, GEORGIAN,
                             CYRILLIC, GLAGOLITIC, KANA, KANA_VOWEL,
                             GEEZ_FIRST, _GEEZ_EIGHTH_SLOT_HOLE,
                             HANGUL_VOWEL)
from pontifex.cubes import factorize
from pontifex.doubles import DOUBLES as LATIN_PAIRS
from pontifex.numerals import DOUBLES as ROMAN_DOUBLES, pair as roman_pair
from resonance.core.notes import SOLFEGGIO, SOLFEGGIO_FREQS

OUT = []

def emit(s=''):
    OUT.append(s)
    print(s)

def W(word, system):
    """weigh() unwrapped to the bare value, for table-building."""
    return weigh(word, system)['value']

def BD(word, system):
    """weigh() breakdown as a compact string, for audit display."""
    r = weigh(word, system)
    parts = '+'.join(f"{tok}={val}" for tok, val in r['breakdown'])
    return f"{r['value']} [{parts}]" if parts else f"{r['value']} [no letters weighed]"

def chain(n):
    """Iterative digit-sum reduction, printed in the founder's chain
    style (cf. 436→13→4→2→0): returns the list of stages."""
    stages = [n]
    while stages[-1] >= 10:
        stages.append(sum(int(d) for d in str(stages[-1])))
    return stages

def chainstr(n):
    return ' → '.join(str(s) for s in chain(n))

def root(n):
    return chain(n)[-1]

def decade(n):
    """Decade factorization of a Milesian-style value: (digit, class)
    for pure decade forms; None for compound values."""
    if n == 0:
        return None
    s = str(n)
    if len(s) == 1:
        return (n, 0)
    if s[1:] == '0' * (len(s) - 1):
        return (int(s[0]), len(s) - 1)
    return None

# =============================================================================
# S0 — CALIBRATION AND THE NINE ASSERTED AGAINST THE BANK
# =============================================================================
emit('=' * 78)
emit('S0 — CALIBRATION')
emit('=' * 78)
emit(f"θέλημα greek      = {BD('θέλημα', 'greek')}   (control: 93)")
emit(f"VAPOUR ordinal    = {BD('VAPOUR', 'latin_ordinal')}   (the register's bridge: 93)")
emit(f"σφίγξ greek       = {BD('σφίγξ', 'greek')}   (control: 773)")

# The Nine, canonical order (essay §II–III; vocal tool §I).
NINE = [
    ('Α',  'α',  1),
    ('Ε',  'ε',  5),
    ('Η',  'η',  8),
    ('Ι',  'ι',  10),
    ('Ο',  'ο',  70),
    ('Υ',  'υ',  400),
    ('Ω',  'ω',  800),
    ('ΕΙ', 'ει', 15),
    ('ΟΥ', 'ου', 470),
]
emit()
emit('The Nine asserted against the engine (Greek bank):')
ok = True
for glyph, low, want in NINE:
    got = W(low, 'greek')
    flag = 'OK' if got == want else f'MISMATCH want {want}'
    ok = ok and got == want
    emit(f"  {glyph:3s} weigh('{low}','greek') = {got:5d}  {flag}")
seven = sum(v for _, _, v in NINE[:7])
hyb = sum(v for _, _, v in NINE[7:])
emit(f"  seven = {seven} (1294) · hybrids = {hyb} (485) · nine = {seven + hyb} (1779)")
assert ok and seven == 1294 and hyb == 485 and seven + hyb == 1779
emit('  ASSERTION HOLDS.')

# =============================================================================
# S1 — LEG 1: REDUCTION
# =============================================================================
emit()
emit('=' * 78)
emit('S1 — LEG 1: REDUCTION (digit-sum chains; mod-9; decade factorization)')
emit('=' * 78)
roots = {}
for glyph, low, v in NINE:
    r = root(v)
    roots.setdefault(r, []).append(glyph)
    emit(f"  {glyph:3s} {v:5d} : {chainstr(v):22s} root {r} · mod9 {v % 9} · decade {decade(v)}")
emit()
emit(f"  root multiset: {sorted((r, g) for r, g in roots.items())}")
emit(f"  collisions: " + '; '.join(f"root {r} ×{len(g)} ({', '.join(g)})"
                                 for r, g in sorted(roots.items()) if len(g) > 1))
emit(f"  empty roots: {[r for r in range(1, 10) if r not in roots]}")
emit(f"  distinct roots for nine vowels: {len(roots)}")
emit()
for label, total in [('seven 1294', 1294), ('hybrids 485', 485), ('nine 1779', 1779),
                     ('ΟΥ 470', 470), ('ΕΙ 15', 15)]:
    emit(f"  {label:14s}: {chainstr(total)}")
emit()
emit('  Decade reading of the hybrids (the thesis grid: function × decade):')
emit(f"    ΕΙ 15 = ε(5 ×1) + ι(1 ×10); components' decades: units + tens")
emit(f"    ΟΥ 470 = ο(7 ×10) + υ(4 ×100); components' decades: tens + hundreds")
emit(f"    decade(15) = {decade(15)} · decade(470) = {decade(470)}"
     '  (neither hybrid is a pure decade form)')

# =============================================================================
# S2 — LEG 2: THE TRINITY WEIGHING + CUBE CHECK
# =============================================================================
emit()
emit('=' * 78)
emit('S2 — LEG 2: TRINITY PER VOWEL (Greek own tongue · Latin ordinal dress · Agrippa dress)')
emit('=' * 78)
# Dresses: stated transliteration choices. Η takes E (short) and EI (the
# archaic long-ē spelling, Latin essay §III); Υ takes Y and V (U weighed
# as the modern dress, labelled); Ω takes O only (Ō has no bank seat —
# weighed below to show the silence); ΕΙ takes EI (and I as sound-dress);
# ΟΥ takes OV (glide dress) and V (sound dress, /uː/).
DRESSES = [
    ('Α',  ['A']),
    ('Ε',  ['E']),
    ('Η',  ['E', 'EI']),
    ('Ι',  ['I']),
    ('Ο',  ['O']),
    ('Υ',  ['Y', 'V', 'U']),
    ('Ω',  ['O']),
    ('ΕΙ', ['EI', 'I']),
    ('ΟΥ', ['OV', 'V']),
]
PRIMARY = {'Α': 'A', 'Ε': 'E', 'Η': 'E', 'Ι': 'I', 'Ο': 'O',
           'Υ': 'V', 'Ω': 'O', 'ΕΙ': 'EI', 'ΟΥ': 'OV'}
trinity = {}
for glyph, dresses in DRESSES:
    g = W(dict((g, l) for g, l, _ in NINE)[glyph], 'greek')
    row = {'greek': g, 'dresses': {}}
    for d in dresses:
        row['dresses'][d] = (W(d, 'latin_ordinal'), W(d, 'agrippa'))
    trinity[glyph] = row
    dstr = ' · '.join(f"{d}: ord {v[0]} / agr {v[1]}" for d, v in row['dresses'].items())
    emit(f"  {glyph:3s} greek {g:5d} | {dstr}")
emit()
emit(f"  The macron dresses weighed: Ō ordinal = {W('Ō', 'latin_ordinal')}, "
     f"agrippa = {W('Ō', 'agrippa')} (silence in both banks — no seat); "
     f"Ē ordinal = {W('Ē', 'latin_ordinal')}, agrippa = {W('Ē', 'agrippa')}")
ord_total = sum(trinity[g]['dresses'][PRIMARY[g]][0] for g, _, _ in NINE)
agr_total = sum(trinity[g]['dresses'][PRIMARY[g]][1] for g, _, _ in NINE)
grk_total = sum(trinity[g]['greek'] for g, _, _ in NINE)
emit()
emit(f"  Primary-dress totals: Greek {grk_total} · Latin ordinal {ord_total} · Agrippa {agr_total}")
for label, t in [('Greek', grk_total), ('Ordinal', ord_total), ('Agrippa', agr_total)]:
    emit(f"    {label:8s} {t:5d}: digit chain {chainstr(t)} · prime factorization {factorize(t)}")
emit()
emit('  The assembled grid (9 vowels × 3 banks = 27 cells, row-major in')
emit('  canonical order × Trinity order); the hidden center is cell 14:')
cells = []
for glyph, _, _ in NINE:
    cells.append((glyph, 'greek', trinity[glyph]['greek']))
    cells.append((glyph, 'ordinal', trinity[glyph]['dresses'][PRIMARY[glyph]][0]))
    cells.append((glyph, 'agrippa', trinity[glyph]['dresses'][PRIMARY[glyph]][1]))
emit(f"    cell 14 = {cells[13]}")
emit(f"    grid sum = {sum(c[2] for c in cells)} · chain {chainstr(sum(c[2] for c in cells))}")
emit()
emit('  The 13-Gate (QVANTVM §3 form: digit-sum chains; passage through 13 noted):')
for glyph, _, v in NINE:
    st = chain(v)
    emit(f"    {glyph:3s} {v:5d}: {' → '.join(map(str, st))}"
         f"{'  · passes through 13' if 13 in st else ''}")
for label, t in [('1294', 1294), ('1779', 1779), ('485', 485)]:
    st = chain(t)
    emit(f"    sum {label}: {' → '.join(map(str, st))}"
         f"{'  · passes through 13' if 13 in st else ''}")

# =============================================================================
# S3 — LEG 3: TRIANGULATION
# =============================================================================
emit()
emit('=' * 78)
emit('S3 — LEG 3: TRIANGULATION')
emit('=' * 78)
order = [g for g, _, _ in NINE]
vals = {g: v for g, _, v in NINE}

emit('  (a) ORDER — Frame A: canonical order on the sketch nodes (angle')
emit('      −90° + 40°·i, i = 0..8), triads as coded: (0,3,6) (1,4,7) (2,5,8).')
frameA = {}
for tri_idx, tri in enumerate([(0, 3, 6), (1, 4, 7), (2, 5, 8)]):
    members = [order[i] for i in tri]
    for pos, m in enumerate(members):
        frameA[m] = (tri_idx, pos)
    s = sum(vals[m] for m in members)
    emit(f"    Triad A{tri_idx} {members}: sum {s} · chain {chainstr(s)}")

emit()
emit('  (b) CLASS — Frame B: decade classes. Three stated rules for the')
emit('      hybrids: value-class (digits of the sum), landing-class (the')
emit('      glide\'s second component), onset-class (first component).')
def class_of_value(v):
    return 0 if v < 10 else (1 if v < 100 else 2)
comp = {'ΕΙ': ('Ε', 'Ι'), 'ΟΥ': ('Ο', 'Υ')}
def class_frame(rule):
    fr = {}
    for g, _, v in NINE:
        if g in comp:
            if rule == 'value':
                fr[g] = class_of_value(v)
            elif rule == 'landing':
                fr[g] = class_of_value(vals[comp[g][1]])
            else:
                fr[g] = class_of_value(vals[comp[g][0]])
        else:
            fr[g] = class_of_value(v)
    return fr
framesB = {}
for rule in ('value', 'landing', 'onset'):
    fr = class_frame(rule)
    framesB[rule] = fr
    counts = [sum(1 for g in order if fr[g] == c) for c in range(3)]
    emit(f"    rule {rule:8s}: class sizes {counts} "
         f"{'— TILES 3-3-3' if counts == [3, 3, 3] else '— does not tile'}")
frB = framesB['value']
class_triads = {}
for c in range(3):
    members = sorted([g for g in order if frB[g] == c], key=lambda g: vals[g])
    class_triads[c] = members
    for pos, m in enumerate(members):
        pass
    s = sum(vals[m] for m in members)
    emit(f"    Class triad B{c} (by value) {members}: sum {s} · chain {chainstr(s)}")
frameB = {}
for c, members in class_triads.items():
    for pos, m in enumerate(members):
        frameB[m] = (c, pos)
emit()
emit('  Frame agreement (triad index; position within triad by the frame\'s')
emit('  own order — sketch: node order; class: value order):')
for g in order:
    a, b = frameA[g], frameB[g]
    agree = 'TRIAD AGREES' if a[0] == b[0] else 'triad parts'
    pos = ' · position agrees' if a == b else ''
    emit(f"    {g:3s} A{a} vs B{b} — {agree}{pos}")
emit(f"  Hybrid placement by triad index: ΕΙ A{frameA['ΕΙ'][0]}/B{frameB['ΕΙ'][0]} · "
     f"ΟΥ A{frameA['ΟΥ'][0]}/B{frameB['ΟΥ'][0]}")

emit()
emit('  (c) THE SOLFEGGIO NINE (resonance/core/notes.py, as filed):')
emit(f"    freqs: {list(SOLFEGGIO_FREQS)}")
emit(f"    names: {[SOLFEGGIO[f] for f in SOLFEGGIO_FREQS]}")
sol_roots = [root(f) for f in SOLFEGGIO_FREQS]
emit(f"    reductions: {[chainstr(f) for f in SOLFEGGIO_FREQS]}")
emit(f"    roots by position 1..9: {sol_roots}")
for r in (3, 6, 9):
    pos = [i + 1 for i, x in enumerate(sol_roots) if x == r]
    emit(f"    root {r}: positions {pos} · freqs {[SOLFEGGIO_FREQS[i - 1] for i in pos]}")
emit('    Order-pairing vowel k ↔ solfeggio k, roots compared:')
agree_pairs = []
for k, (glyph, _, v) in enumerate(NINE):
    f = SOLFEGGIO_FREQS[k]
    mark = 'ROOTS AGREE' if root(v) == sol_roots[k] else 'roots part'
    if root(v) == sol_roots[k]:
        agree_pairs.append((glyph, f))
    emit(f"    {glyph:3s} (root {root(v)}) ↔ {f} Hz {SOLFEGGIO[f]} (root {sol_roots[k]}) — {mark}")
emit(f"    root-agreeing pairs by order: {agree_pairs}")
emit(f"    vowel roots present: {sorted(roots)} · solfeggio roots present: {sorted(set(sol_roots))}"
     f" · shared roots: {sorted(set(roots) & set(sol_roots))}")

emit()
emit('  (d) FURTHER WITNESSES.')
emit('    The tridecagram (build_divine_nine_vowel_table.py): 13 stations at')
emit('    −90° + i·(360/13)°; labels in order: Α Ε Η Ι Ο Υ Ω ΕΙ ΟΥ · γʹ OFFSET ·')
emit('    ϛʹ MIRROR · κʹ REFUSAL · οὐδέν ZERO. Star step {13/5} traversal:')
stations = order + ['γʹ OFFSET', 'ϛʹ MIRROR', 'κʹ REFUSAL', 'οὐδέν ZERO']
trav, idx = [], 0
for _ in range(13):
    trav.append(stations[idx])
    idx = (idx + 5) % 13
emit(f"    {' → '.join(trav)}")
emit('    abc_notes seats for the Latin faces (engine, system abc_notes):')
for face in ['A', 'E', 'I', 'O', 'V', 'Y']:
    try:
        emit(f"    {face}: {BD(face, 'abc_notes')}")
    except Exception as e:
        emit(f"    {face}: engine refuses ({type(e).__name__}: {e})")

# =============================================================================
# S4 — LEG 4: THE CORPUS'S ARCHON CONTROLS
# =============================================================================
emit()
emit('=' * 78)
emit('S4 — LEG 4: ARCHON CONTROLS FROM THE CORPUS')
emit('=' * 78)
emit(f"  ἄρχων greek      = {BD('ἄρχων', 'greek')}  (ARCHONSTRATVMVXXX instrument: 1551)")
emit(f"  ARCHON ordinal   = {BD('ARCHON', 'latin_ordinal')}  (the instrument: 59)")
emit(f"  ARCHON agrippa   = {BD('ARCHON', 'agrippa')}")
emit(f"  ἀρχή greek       = {BD('ἀρχή', 'greek')}  (the root-word: beginning/rule)")

# =============================================================================
# S5 — LEG 5: THE CROSS AND THE KEY STRINGS
# =============================================================================
emit()
emit('=' * 78)
emit('S5 — LEG 5: HYBRID-MARK CENSUS, THE CROSS TEST, THE KEY STRINGS')
emit('=' * 78)
emit('  Hybridity marks in the corpus (documentary — citations in the instrument):')
emit('    WITHIN THE NINE, corpus-marked: ΕΙ (improper diphthong, grammarians\') ·')
emit('    ΟΥ (improper diphthong, grammarians\') · Υ (border-dweller: vowel that')
emit('    served as a consonant\'s kin, essay §II; /y/ = /i/ tongue + /u/ lips,')
emit('    vocal tool §II) → COUNT 3.')
emit('    Η by heta: the wider tradition attests Η began as the aspirate')
emit('    consonant heta; the founder\'s corpus NOWHERE marks it (searched).')
emit('    WIDER FIELD, corpus-marked: ϛ stigma (letter-born, numeral-bound,')
emit('    essay §VII) · VV (founder\'s clause, thesis §III: vowel or consonant')
emit('    decided by the reading tongue) · V Latin (the dialect\'s own hybrid')
emit('    letter, Latin essay §II) → wider count with the nine\'s three: 6 named')
emit('    marks; the four-count is reached only by stated selection.')
four = ['Η', 'Υ', 'ΕΙ', 'ΟΥ']
fvals = {g: vals[g] for g in four}
emit()
emit(f"  The candidate four (nine + heta admitted): {four} values {fvals}")
emit(f"    canonical positions: {[order.index(g) + 1 for g in four]}")
emit(f"    Frame A triads: {[frameA[g][0] for g in four]} · Frame B classes: {[frameB[g][0] for g in four]}")
emit(f"    sum {sum(fvals.values())} · chain {chainstr(sum(fvals.values()))}")
emit(f"    roots: {[root(fvals[g]) for g in four]} (set {sorted(root(fvals[g]) for g in four)})")
emit(f"    the non-hybrid five roots: {[root(vals[g]) for g in order if g not in four]}")
emit(f"    9-ring quarters: 9/4 = {9 / 4} — not integral; no exact cardinal")
emit('    cross seats on a nine-node ring. Nearest node sets to the quarters')
emit('    (0°, 90°, 180°, 270° from node 0 at −90°): nodes 0, 2, 4 or 5, 7 —')
emit('    approximations, printed as approximations.')
emit(f"    tridecagram stations of the four: {[order.index(g) + 1 for g in four]} of 13;"
     f" 13/4 = {13 / 4} — not integral either.")

emit()
emit('  THE KEY STRINGS (byte-exact as given; expansions unruled):')
STRINGS = ['VYX', 'RRYYZZ', 'WVII', 'VVII']
HOUSE = {93, 77, 1776, 1779, 1294, 485, 15, 470, 8}
for s in STRINGS:
    emit(f"    {s}: ordinal {BD(s, 'latin_ordinal')} · agrippa {BD(s, 'agrippa')}"
         f" · chains ord {chainstr(W(s, 'latin_ordinal'))} / agr {chainstr(W(s, 'agrippa'))}")
emit('  Components:')
for c in ['R', 'Y', 'Z', 'V', 'W', 'X', 'I', 'RR', 'YY', 'ZZ', 'VV', 'II', 'WW']:
    lp = LATIN_PAIRS.get(c)
    emit(f"    {c:3s}: ordinal {W(c, 'latin_ordinal'):4d} · agrippa {W(c, 'agrippa'):4d}"
         + (f" · doubles map ord {lp['ordinal']} / agr {lp['agrippa']}" if lp else ''))
emit('  Roman instrument (numerals.py) on the doubles:')
for p in ['II', 'VV', 'XX', 'CC', 'MM', 'LL', 'DD']:
    e = ROMAN_DOUBLES[p]
    emit(f"    {p}: status {e['status']} · value {e['value']} · promotion {e['promotion']}"
         f" · hybrid_seat {e['hybrid_seat']}")
emit(f"    roman_pair('VV') = {roman_pair('VV')} · roman_pair('II') = {roman_pair('II')}")
from pontifex.numerals import parse as roman_parse
try:
    emit(f"    roman_parse('VVII') = {roman_parse('VVII')}")
except Exception as e:
    emit(f"    roman_parse('VVII') refuses: {type(e).__name__}: {e}")
try:
    emit(f"    roman_parse('WVII') = {roman_parse('WVII')}")
except Exception as e:
    emit(f"    roman_parse('WVII') refuses: {type(e).__name__}: {e}")
emit('  Greek dresses (stated equivalences: V→Υ, Y→Υ, X→Ξ, R→Ρ, Z→Ζ, W→ΥΥ, I→Ι):')
for s, dress in [('VYX', 'υυξ'), ('RRYYZZ', 'ρρυυζζ'), ('WVII', 'υυυιι'), ('VVII', 'υυιι')]:
    emit(f"    {s} → {dress}: {BD(dress, 'greek')} · chain {chainstr(W(dress, 'greek'))}")
emit('  Hebrew fallback dresses (the engine\'s own door, weigh_via_hebrew_fallback):')
for s in STRINGS:
    r = weigh_via_hebrew_fallback(s)
    emit(f"    {s}: {r}")
emit('  Touch tests vs the hybrids\' seats {15, 470, 485, root 8} and the house')
emit('  numbers {93, 77, 1776, 1779, 1294}: equality / root-equality / Δ∈{1,3}:')
def touches(label, n):
    hits = []
    for h in sorted(HOUSE):
        if n == h:
            hits.append(f"EQUALS {h}")
        if root(n) == root(h) and h in (485, 15, 470, 8):
            hits.append(f"root {root(n)} = root of {h}")
        if abs(n - h) in (1, 3):
            hits.append(f"Δ{abs(n - h)} from {h}")
    emit(f"    {label:22s} {n:6d} root {root(n)}: {'; '.join(hits) if hits else 'no touch'}")
for s in STRINGS:
    touches(f"{s} ordinal", W(s, 'latin_ordinal'))
    touches(f"{s} agrippa", W(s, 'agrippa'))
for s, dress in [('VYX', 'υυξ'), ('RRYYZZ', 'ρρυυζζ'), ('WVII', 'υυυιι'), ('VVII', 'υυιι')]:
    touches(f"{s} greek dress", W(dress, 'greek'))
emit(f"  Dress-pair Δ (WVII vs VVII): ordinal Δ{abs(W('WVII', 'latin_ordinal') - W('VVII', 'latin_ordinal'))}"
     f" · agrippa Δ{abs(W('WVII', 'agrippa') - W('VVII', 'agrippa'))}")

# =============================================================================
# S6 — LEG 5x: THE FOLD (4 → 8, 'THE CRAZY 88')
# =============================================================================
emit()
emit('=' * 78)
emit('S6 — LEG 5 EXTENSION: THE FOLD')
emit('=' * 78)
prod = 1
for g in four:
    prod *= fvals[g]
rprod = 1
for g in four:
    rprod *= root(fvals[g])
emit(f"  The four {four}: values {list(fvals.values())}")
emit(f"    sum {sum(fvals.values())} · chain {chainstr(sum(fvals.values()))}")
emit(f"    product {prod} · chain {chainstr(prod)}")
emit(f"    roots {[root(fvals[g]) for g in four]} · root sum {sum(root(fvals[g]) for g in four)}"
     f" · root product {rprod} · chain {chainstr(rprod)}")
emit(f"  ΗΗ weighed: greek {BD('ηη', 'greek')} · the figure 88 in Greek dress:"
     f" πη {BD('πη', 'greek')} · chain {chainstr(88)}")
emit(f"  HH ordinal {BD('HH', 'latin_ordinal')} · 88 = 8 × 11; 88 in the record:"
     ' RGBXA88 (cited as coordinate only, unexpanded)')
emit(f"  The hybrids' own road to 8: 485 → {chainstr(485)} (essay §III)")

# =============================================================================
# S7 — LEG 6: THE TWELVE-TONGUES SWEEP
# =============================================================================
emit()
emit('=' * 78)
emit('S7 — LEG 6: THE TWELVE-TONGUES SWEEP (vowel seats from the tables)')
emit('=' * 78)
def letters(table, chars):
    return {c: table.get(c) for c in chars}
emit(f"  HEBREW matres (א ה ו י): {letters(HEBREW, ['א', 'ה', 'ו', 'י'])}")
emit(f"    sofit finals present: {[c for c in ['ך', 'ם', 'ן', 'ף', 'ץ'] if c in HEBREW]}")
emit(f"  ARABIC matres (ا و ي): {letters(ARABIC_ABJAD, ['ا', 'و', 'ي'])}")
emit(f"    tāʾ marbūṭa ة in table: {'ة' in ARABIC_ABJAD} · weigh = "
     f"{weigh('ة', 'arabic_abjad')['value']} (breakdown {weigh('ة', 'arabic_abjad')['breakdown']})")
emit(f"  LATIN vowels: ordinal {letters(LATIN_ORDINAL, list('AEIOV'))} ·"
     f" agrippa {letters(AGRIPPA, list('AEIOV'))}")
emit(f"  KANA vowel seats (KANA_VOWEL): {KANA_VOWEL}")
for c in ['ア', 'イ', 'ウ', 'エ', 'オ']:
    emit(f"    {c}: kana weigh = {W(c, 'kana')}")
emit(f"  GEEZ: first-form sample {dict(list(GEEZ_FIRST.items())[:5])} ·"
     f" eighth-slot hole sign: {_GEEZ_EIGHTH_SLOT_HOLE}")
emit(f"  ARMENIAN vowels: {letters(ARMENIAN, ['Ա', 'Ե', 'Ը', 'Ի', 'Ո', 'Ւ', 'Օ'])}")
emit(f"    digraph ՈՒ (ու): weigh = {W('ՈՒ', 'armenian')}")
emit(f"  COPTIC vowels: {letters(COPTIC, ['Ⲁ', 'Ⲉ', 'Ⲏ', 'Ⲓ', 'Ⲟ', 'Ⲩ', 'Ⲱ'])}")
emit(f"    digraph ⲞⲨ: weigh = {W('ⲞⲨ', 'coptic')}")
emit(f"  GEORGIAN vowels: {letters(GEORGIAN, ['ა', 'ე', 'ი', 'ო', 'უ', 'ჱ'])}")
emit(f"  CYRILLIC vowel candidates: {letters(CYRILLIC, ['А', 'Е', 'И', 'І', 'О', 'У', 'Ѹ', 'Ѡ', 'Ъ', 'Ь'])}")
emit(f"  GLAGOLITIC vowel candidates: {letters(GLAGOLITIC, ['ⰰ', 'ⰵ', 'ⰻ', 'ⰹ', 'ⰿ', 'Ⱐ', 'Ⱒ', 'Ⱊ'])}")
emit(f"  HANGUL vowel jamo (21): {HANGUL_VOWEL}")
for j in HANGUL_VOWEL:
    try:
        emit(f"    {j}: hangul weigh = {weigh(j, 'hangul')['value']}")
    except Exception as e:
        emit(f"    {j}: {type(e).__name__}: {e}")
emit('  Kana dress check for the key strings (signs present in KANA table?):')
for c in ['ヴ', 'ク', 'ス', 'ル', 'ズ']:
    emit(f"    {c}: {'present' if c in KANA else 'ABSENT'}")

emit()
emit('BATTERY COMPUTATION COMPLETE — all figures above are engine output.')

with open(os.path.join(HERE, 'archon_battery_output.txt'), 'w') as f:
    f.write('\n'.join(OUT) + '\n')

# 93 — Live, Love, and let Love, Live.
