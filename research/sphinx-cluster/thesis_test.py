# =====================================================================
# THESIS TEST — the computation pass for the conditional seating
# =====================================================================
# [epigraph] "Test the thesis and if it passes Seat the Archons and
#   the cross-section." — the founder's conditional order, 2026-11-24
#   18:37 EST. The desk tests first; it seats only what passes.
#
# Date: XXIV day of November, Dies Martis, Anno V:xii e.n. (2026 e.v.)
# 93
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM / DOCTRINE
#   This script computes the two things in the thesis test that are
#   computations rather than citations:
#     (1) T2(b) THE INVERSION — the tridecagram's {13/5} traversal
#         (the star polygon of the plate of record) and its inverse
#         (step -5, i.e. step +8 mod 13): does the inverse pass
#         through the same stations in EXACT reverse order? Clock
#         to counter as an exact operation on the engine of record.
#     (2) The second witness the brief names: the Offset Law's own
#         inversion machinery (the 9<->6 mirror closure, 1779 ->
#         1776) re-run as arithmetic.
#   It also re-verifies, from the house engine, the value inputs the
#   T1 coverage table rests on (the Nine; the Coptic mirror; the
#   dresses the battery flagged), so the seating instrument's marks
#   answer to the bank and not to the battery's prose alone.
#   Nothing here seats anything. The script measures; the
#   instrument (THE-SEATING-OF-THE-ARCHONS.md) reports; the seating
#   is the founder's declaration on the evidence, at his order.
# =====================================================================

import sys, site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, '/home/hatch/workspace/pontifex')
from pontifex import weigh  # noqa: E402  (the house engine)


def V(word, bank):
    """DOCTRINE: one weighing, unwrapped to its value. The engine
    returns a record; the test needs the number and nothing else."""
    r = weigh(word, bank)
    return r['value'] if isinstance(r, dict) else r


# ---------------------------------------------------------------------
# Controls — the bank must read true before anything is believed.
# ---------------------------------------------------------------------
print('CONTROLS')
print('  thelema greek   =', V('θελημα', 'greek'), '(expect 93)')
print('  VAPOUR ordinal  =', V('VAPOUR', 'latin_ordinal'), '(expect 93)')
print('  sphinx greek    =', V('σφιγξ', 'greek'), '(expect 773)')

# ---------------------------------------------------------------------
# T2(b) — THE INVERSION, computed on the plate of record.
# MECHANISM: the plate seats thirteen stations in ring order:
#   1 Α · 2 Ε · 3 Η · 4 Ι · 5 Ο · 6 Υ · 7 Ω · 8 ΕΙ · 9 ΟΥ ·
#   10 OFFSET γ' · 11 MIRROR ϛ' · 12 REFUSAL κ' · 13 ZERO οὐδέν
# (build_divine_nine_vowel_table.py; the battery, Found 1).
# The star polygon {13/5} steps +5 stations (mod 13) from station 1.
# The inverse traversal steps -5 (mod 13). The test: the inverse
# sequence, read from the same start, must be the forward sequence
# read backwards — station for station, no remainder.
# ---------------------------------------------------------------------
STATIONS = ['Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', 'ΕΙ', 'ΟΥ',
            'OFFSET γʹ', 'MIRROR ϛʹ', 'REFUSAL κʹ', 'ZERO οὐδέν']


def traverse(start, step, n=13):
    """DOCTRINE: one full circuit of the {13/k} star from `start`
    (0-based index), stepping `step` stations at a time, mod 13.
    Returns the visited station indices in visit order."""
    seq, cur = [start], start
    for _ in range(n - 1):
        cur = (cur + step) % n
        seq.append(cur)
    return seq


fwd = traverse(0, 5)          # the {13/5} path, from station 1 (Α)
inv = traverse(0, -5)         # its inverse: step -5 == step +8 (mod 13)
print('\nT2(b) THE TRAVERSAL AND ITS INVERSE')
print('  forward {13/5} :', ' → '.join(STATIONS[i] for i in fwd))
print('  inverse {-5}   :', ' → '.join(STATIONS[i] for i in inv))
rev = [fwd[0]] + fwd[:0:-1]   # forward read backwards, same start
print('  inverse == forward reversed, station for station:',
      inv == rev)
print('  inverse visits all 13 stations exactly once:',
      sorted(inv) == list(range(13)))
print('  step check: -5 mod 13 =', -5 % 13, '(the {13/8} polygon)')

# Second witness — the Offset Law's inversion machinery (essay §VI):
# the mirror closure 1779 -> 1776 by inversion of the final glyph
# (9 -> 6), the offset's constant (3) being exactly 9 - 6.
print('\nT2(b) SECOND WITNESS — THE OFFSET LAW INVERSION')
print('  1779 final digit 9, inverted 6; 9 - 6 =', 9 - 6,
      '; 1779 - 3 =', 1779 - 3, '(the closure is exact, remainder 0)')

# ---------------------------------------------------------------------
# T1 — the value inputs under the coverage table, re-weighed.
# ---------------------------------------------------------------------
print('\nT1 VALUE INPUTS (re-weighed from the engine)')
nine = {'Α': 1, 'Ε': 5, 'Η': 8, 'Ι': 10, 'Ο': 70, 'Υ': 400, 'Ω': 800,
        'ΕΙ': 15, 'ΟΥ': 470}
for w, expect in nine.items():
    got = V(w.lower(), 'greek')
    print(f'  greek {w} = {got} (battery {expect})', 'OK' if got == expect else 'PART')
print('  coptic ⲟⲩ =', V('ⲟⲩ', 'coptic'), '(battery 470 — ΟΥ value-mark)')
print('  coptic ⲏ  =', V('ⲏ', 'coptic'), '(battery 8 — five-tongue 8)')
print('  coptic ⲓ  =', V('ⲓ', 'coptic'), '(battery 10 — Ι mirror value)')
print('  coptic ⲱ  =', V('ⲱ', 'coptic'), '(battery 800 — Ω mirror value)')
print('  upsilon Y-dress, Agrippa =', V('Y', 'agrippa'),
      '(battery 400 — Υ carries its own Greek price abroad)')
print('  epsilon dress E: ordinal', V('E', 'latin_ordinal'),
      '/ Agrippa', V('E', 'agrippa'),
      '(battery 5/5 — Ε bank-invariant, like Α)')
print('  iota dress I: ordinal', V('I', 'latin_ordinal'),
      '(battery 9 — Ι dress PARTS from its Greek price 10)')
print('  omega dress O: ordinal', V('O', 'latin_ordinal'),
      '(battery 15 — Ω dress PARTS from its Greek price 800)')
print('  diphthong four: ΑΙ', V('αι', 'greek'), '+ ΕΙ', V('ει', 'greek'),
      '+ ΟΙ', V('οι', 'greek'), '+ ΟΥ', V('ου', 'greek'), '=',
      V('αι', 'greek') + V('ει', 'greek') + V('οι', 'greek') + V('ου', 'greek'),
      '(576 = 24^2:', 24 * 24 == 576, ')')
print('  οὐδέν =', V('ουδεν', 'greek'), '(529 = 23^2:', 23 * 23 == 529, ')')

print('\n93 — Live, Love, and let Love, Live.')
