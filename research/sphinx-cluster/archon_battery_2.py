#!/usr/bin/env python3
# =============================================================================
# 93 — ARCHON_BATTERY_2.PY
# THE ARCHON BATTERY, SECOND PASS — the founder's two mid-battery
# additions of 2026-11-24 18:26–18:27 EST:
#   (1) THE ALREADY-THERE PASS — "i think well find them where they are
#       already we just didnt knkw to mark them": the nine-seat
#       structures the house already drew, extracted as FOUND
#       structures (the tridecagram plate first), never constructed here.
#   (2) THE FOUR DIPHTHONGS — his candidate list "Ae Ei ai oo oi?":
#       ΑΙ and ΟΙ (the proper pair) beside ΕΙ and ΟΥ (the improper
#       pair, his seated hybrids), weighed entire, with the structural
#       consequence printed unsmoothed.
# Plus the weigh()-based vowel seats for the banks whose tables are
# keyed by minuscule (Coptic, Glagolitic), which the first pass's raw
# dict probe missed.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =============================================================================
"""Second pass: S8 the diphthong four · S9 the already-there pass ·
S10 the minuscule-keyed banks weighed through the engine."""

import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/workspace/pontifex'))

from pontifex.engine import weigh

OUT = []

def emit(s=''):
    OUT.append(s)
    print(s)

def W(word, system):
    return weigh(word, system)['value']

def BD(word, system):
    r = weigh(word, system)
    parts = '+'.join(f"{tok}={val}" for tok, val in r['breakdown'])
    return f"{r['value']} [{parts}]" if parts else f"{r['value']} [no letters weighed]"

def chain(n):
    stages = [n]
    while stages[-1] >= 10:
        stages.append(sum(int(d) for d in str(stages[-1])))
    return stages

def chainstr(n):
    return ' → '.join(str(s) for s in chain(n))

def root(n):
    return chain(n)[-1]

# =============================================================================
# S8 — THE FOUR DIPHTHONGS (the founder's list: "Ae Ei ai oo oi?")
# =============================================================================
emit('=' * 78)
emit('S8 — THE FOUR DIPHTHONGS')
emit('=' * 78)
DIPH = [('ΑΙ', 'αι', 'proper'), ('ΕΙ', 'ει', 'improper'),
        ('ΟΙ', 'οι', 'proper'), ('ΟΥ', 'ου', 'improper')]
dvals = {}
for glyph, low, kind in DIPH:
    v = W(low, 'greek')
    dvals[glyph] = v
    emit(f"  {glyph} ({kind}): {BD(low, 'greek')} · chain {chainstr(v)} · root {root(v)}")
tot = sum(dvals.values())
proper = dvals['ΑΙ'] + dvals['ΟΙ']
improper = dvals['ΕΙ'] + dvals['ΟΥ']
emit(f"  proper pair   ΑΙ+ΟΙ = {proper} · chain {chainstr(proper)}")
emit(f"  improper pair ΕΙ+ΟΥ = {improper} · chain {chainstr(improper)} (the seated hybrids)")
emit(f"  cross pairs: ΑΙ+ΟΥ = {dvals['ΑΙ'] + dvals['ΟΥ']} · chain {chainstr(dvals['ΑΙ'] + dvals['ΟΥ'])}"
     f" · ΕΙ+ΟΙ = {dvals['ΕΙ'] + dvals['ΟΙ']} · chain {chainstr(dvals['ΕΙ'] + dvals['ΟΙ'])}")
emit(f"  THE FOUR SUM = {tot} · chain {chainstr(tot)} · root {root(tot)}")
import math
sq = math.isqrt(tot)
emit(f"  square test: isqrt({tot}) = {sq}, {sq}² = {sq * sq} — "
     f"{'EXACT SQUARE' if sq * sq == tot else 'not a square'}")
emit(f"  product of the four = {dvals['ΑΙ'] * dvals['ΕΙ'] * dvals['ΟΙ'] * dvals['ΟΥ']}"
     f" · chain {chainstr(dvals['ΑΙ'] * dvals['ΕΙ'] * dvals['ΟΙ'] * dvals['ΟΥ'])}")
emit(f"  roots of the four: {[root(dvals[g]) for g, _, _ in DIPH]}")
emit()
emit('  The Latin witness and the dress (stated as dress only):')
emit(f"    AE (Latin heir of ΑΙ): ordinal {BD('AE', 'latin_ordinal')} · agrippa {BD('AE', 'agrippa')}")
emit(f"    'oo' (transliteration dress of ΟΥ's sound): ordinal {BD('OO', 'latin_ordinal')}"
     f" · agrippa {BD('OO', 'agrippa')}")
emit(f"    'OU' (schoolbook dress): ordinal {BD('OU', 'latin_ordinal')} · agrippa {BD('OU', 'agrippa')}")
emit()
emit('  Structural consequence — the Eleven:')
eleven = ['Α', 'ΑΙ', 'Ε', 'ΕΙ', 'Η', 'Ι', 'Ο', 'ΟΙ', 'ΟΥ', 'Υ', 'Ω']
base = {'Α': 1, 'Ε': 5, 'Η': 8, 'Ι': 10, 'Ο': 70, 'Υ': 400, 'Ω': 800,
        'ΕΙ': 15, 'ΟΥ': 470}
base.update(dvals)
esum = sum(base[g] for g in eleven)
emit(f"    the nine extended by the proper pair: {eleven}")
emit(f"    eleven sum = {esum} · chain {chainstr(esum)} (the nine's 1779 + the proper pair's {proper})")
emit(f"    seats of the four inside the nine: ΕΙ = seat 8, ΟΥ = seat 9;"
     ' ΑΙ and ΟΙ hold NO seat in the nine — the four straddle its edge.')

# =============================================================================
# S9 — THE ALREADY-THERE PASS (found structures, provenance stated)
# =============================================================================
emit()
emit('=' * 78)
emit('S9 — THE ALREADY-THERE PASS')
emit('=' * 78)
emit('  FOUND 1 — THE TRIDECAGRAM PLATE (build_divine_nine_vowel_table.py,')
emit('  the founder\'s engine, drawn 2026-11-09/24; essay plate addendum:')
emit('  "nine vowels, three relations, one zero"). The plate seats, in')
emit('  ring order: stations 1–9 the nine vowels in canonical order;')
emit('  station 10 γʹ OFFSET (3) · 11 ϛʹ MIRROR (6) · 12 κʹ REFUSAL (20) ·')
emit('  13 οὐδέν THE ZERO POINT. Operator values weighed:')
for w, label in [('γ', 'OFFSET γʹ'), ('ϛ', 'MIRROR ϛʹ (stigma)'), ('κ', 'REFUSAL κʹ')]:
    emit(f"    {label}: {BD(w, 'greek')}")
emit(f"    οὐδέν: {BD('οὐδέν', 'greek')} (the zero station's name weighed)")
emit(f"    ring total: vowels 1779 + operators {3 + 6 + 20} = {1779 + 29}"
     f" · chain {chainstr(1779 + 29)}")
emit('  FOUND 2 — THE SKETCH (build_divine_nine_sketch.py): nine nodes at')
emit('  −90° + 40°·i around SOURCE / AETHER, labeled Roman I–IX only;')
emit('  triads drawn (0,3,6) (1,4,7) (2,5,8). The geometry is FOUND; the')
emit('  vowels\' assignment to nodes is by canonical order (stated reading).')
emit('  FOUND 3 — THE SOLFEGGIO ORDER (notes.py, as filed): the nine')
emit('  frequencies in ascending order with their filed names; its')
emit('  reduction structure (3-6-9 over the mod-3 position classes) is')
emit('  computed in the first pass, S3(c).')
emit('  FOUND 4 — THE THESIS GRID (THE-DIVINE-NINE-THESIS §II): nine')
emit('  FUNCTIONS × three decades = the 27-slot grid; it seats functions')
emit('  1–9, not vowels and not archons — a found nine-seat STRUCTURE')
emit('  whose seats are numbers.')
emit('  FOUND 5 — THE VOCAL TOOL ORDER (THE-DIVINE-NINE-VOCAL-TOOL §I–II):')
emit('  the canonical order with acoustic seats (/a/ /e/ /ɛː/ /i/ /o/ /y/')
emit('  /ɔː/) and VV seated over the /u/ family — a found seating of the')
emit('  nine as SOUNDS, drawn for the engine, never named an archon seating.')
emit('  FOUND 6 — THE DIAL (THE-DOUBLE-LETTER-DIAL): seats the PAIRS on a')
emit('  pitch wheel under two traversals (POM/MOP); it does not seat the')
emit('  nine vowels — searched for the pass, NOT a nine-seat structure.')

# =============================================================================
# S10 — THE MINUSCULE-KEYED BANKS, WEIGHED THROUGH THE ENGINE
# =============================================================================
emit()
emit('=' * 78)
emit('S10 — COPTIC / GLAGOLITIC / ARMENIAN VOWEL SEATS VIA weigh()')
emit('=' * 78)
emit('  COPTIC (the bank folds case; singles weighed):')
for c in ['ⲁ', 'ⲉ', 'ⲏ', 'ⲓ', 'ⲟ', 'ⲩ', 'ⲱ']:
    emit(f"    {c}: {BD(c, 'coptic')}")
emit(f"    digraph ⲟⲩ: {BD('ⲟⲩ', 'coptic')}")
emit('  GLAGOLITIC (singles weighed):')
for c in ['ⰰ', 'ⰵ', 'ⰻ', 'ⰹ', 'ⰿ', 'Ⱐ', 'Ⱒ']:
    emit(f"    {c}: {BD(c, 'glagolitic')}")
emit('  ARMENIAN Օ/օ (the later ō letter) weighed:')
emit(f"    Օ: {BD('Օ', 'armenian')} · օ: {BD('օ', 'armenian')}")
emit('  GEORGIAN ჱ weighed (the archaic e-family letter):')
emit(f"    ჱ: {BD('ჱ', 'georgian')}")
emit('  CYRILLIC yers weighed (Ъ/Ь in the numeral bank):')
emit(f"    Ъ: {BD('Ъ', 'cyrillic')} · Ь: {BD('Ь', 'cyrillic')}")

emit()
emit('SECOND PASS COMPLETE.')

with open(os.path.join(HERE, 'archon_battery_2_output.txt'), 'w') as f:
    f.write('\n'.join(OUT) + '\n')

# 93 — Live, Love, and let Love, Live.
