#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — aramaic_audit_tests.py — the Aramaic Phase I audit
# verification battery. Companion to aramaic_audit.py and
# THE-ARAMAIC-SEAT-PHASE-I-AUDIT.md.
#
# Epigraph: "Syriac numerals are traditionally written with the
# letters of the alphabet. The system is very similar to the
# alphabetic numerals traditionally used in Hebrew, Arabic (the
# abjadi numerals), Armenian, Greek and Cyrillic." — Hughes, "A
# guide to numerals in Syriac", after Nöldeke. Similar, says the
# grammarian; this battery measures exactly how similar, and where
# the similarity stops.
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's.
# This battery is an AUDIT instrument: findings, never doctrine.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: every number the audit document prints can be
#     recomputed from the audit's data files and from constants
#     transcribed directly from the named sources — so the audit's
#     pass is a script's verdict, not prose.
#   Method: read ONLY the CSVs aramaic_audit.py emits, the sweep's
#     aramaic-values.csv (Worker #7, 2026-10-11), plus the source
#     constants below (transcribed independently from the witnesses
#     as read 2026-11-24, and from the Unicode standard via
#     unicodedata); assert each printed number; report PASS/FAIL
#     per check with a summary and a nonzero exit on any failure.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Recompute every number the Aramaic Phase I audit prints.

DOCTRINE: this battery settles by test everything a test can
settle — the two strata's cells, the identity against Hebrew in
both directions, the exhibits, and the boundaries (the finals;
the Imperial number signs). What no test can decide (the tier's
exact depth for the Imperial stratum; a reading law for the
raised point) is not asserted here; both stand in the audit
document at §VI/§VII with their evidence, for the founder's pen
or the desk's printed reasoning.

MECHANISM: checks are grouped INVENTORY / TABLE / IDENTITY /
EXHIBITS / BOUNDARY. Each check prints one line; the run ends
with a count and exits 0 only if every check passed.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- Source constants -----------------------------------------------------------
# DOCTRINE: SOURCE_VALUES is the battery's OWN transcription of the
# abjad sequence (Cherry's Imperial chart, Numerical Value column,
# read 2026-11-24; held against the Wikipedia Syriac summary table
# and tooldune in the builder — transcribed here independently so
# the battery holds the CSV to the source, not to the builder).
SOURCE_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 20, 30, 40, 50, 60, 70, 80, 90,
                 100, 200, 300, 400]
HEBREW_ORDER = 'אבגדהוזחטיכלמנסעפצקרשת'
# MECHANISM: mispar hechrechi entire, finals at their letter's
# value — the Hebrew side exactly as the engine seats it, stated
# here as constants so the identity is held against the method the
# seat claims, and the finals coordinate can be measured.
HEBREW_HECHRECHI = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8,
    'ט': 9, 'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40,
    'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90,
    'ץ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
}
# MECHANISM: mispar gadol's finals — the extension that exists in
# Hebrew's record (Wikipedia, "Gematria": "In mispar gadol, the
# five final letters are given their own values, ranging from 500
# to 900") and in NO Aramaic witness read. The boundary checks
# hold the Aramaic table clear of it.
MISPAR_GADOL_FINALS = {'ך': 500, 'ם': 600, 'ן': 700, 'ף': 800, 'ץ': 900}
SYRIAC_CPS = [0x0710, 0x0712, 0x0713, 0x0715, 0x0717, 0x0718,
              0x0719, 0x071A, 0x071B, 0x071D, 0x071F, 0x0720,
              0x0721, 0x0722, 0x0723, 0x0725, 0x0726, 0x0728,
              0x0729, 0x072A, 0x072B, 0x072C]

RESULTS = []


def check(group, label, ok, detail=''):
    RESULTS.append((group, label, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {group} — {label}"
          + (f" ({detail})" if detail else ''))


def read_csv(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def abjad_value(pos):
    return pos if pos <= 9 else (pos - 9) * 10 if pos <= 18 \
        else (pos - 18) * 100


def main():
    tbl = read_csv('aramaic-table.csv')
    ident = read_csv('aramaic-identity.csv')
    imp = {r['glyph']: int(r['value'])
           for r in tbl if r['stratum'] == 'IMPERIAL'}
    syr = {r['glyph']: int(r['value'])
           for r in tbl if r['stratum'] == 'SYRIAC'}

    def weigh_imp(s):
        return sum(imp[c] for c in s)

    def weigh_syr(s):
        return sum(syr[c] for c in s)

    # --- INVENTORY -----------------------------------------------------
    letters = [chr(cp) for cp in range(0x10840, 0x10860)
               if ud.name(chr(cp), '').startswith(
                   'IMPERIAL ARAMAIC LETTER')]
    check('INVENTORY', 'the Imperial block encodes exactly 22 '
          'letters, U+10840–U+10855 consecutive',
          letters == [chr(0x10840 + i) for i in range(22)],
          '%d letters' % len(letters))
    check('INVENTORY', 'no Imperial letter name carries FINAL — '
          'the block encodes no final forms',
          all('FINAL' not in ud.name(chr(0x10840 + i), '')
              for i in range(22)), '22/22 formless of finals')
    signs = {cp: ud.name(chr(cp), '')
             for cp in range(0x10858, 0x10860)}
    check('INVENTORY', 'the block\'s other notation stands beside '
          'the letters: 8 dedicated NUMBER signs (ONE, TWO, THREE, '
          'TEN, TWENTY, ONE HUNDRED, ONE THOUSAND, TEN THOUSAND) '
          'and one SECTION SIGN at U+10857',
          len(signs) == 8
          and all('NUMBER' in n for n in signs.values())
          and ud.name(chr(0x10857), '')
          == 'IMPERIAL ARAMAIC SECTION SIGN',
          sorted(signs.values())[:2])
    check('INVENTORY', 'the Syriac stratum\'s 22 seats are the '
          'standard\'s own letters, no FINAL in any name',
          all(ud.name(chr(cp), '').startswith('SYRIAC LETTER')
              and 'FINAL' not in ud.name(chr(cp), '')
              for cp in SYRIAC_CPS), '22/22 verified')
    check('INVENTORY', 'the frozen transcription stands: 44 '
          'SOURCED rows, 22 per stratum, positions 1–22 each',
          len(tbl) == 44
          and all(r['status'] == 'SOURCED' for r in tbl)
          and sorted(int(r['position']) for r in tbl
                     if r['stratum'] == 'IMPERIAL')
          == list(range(1, 23))
          and sorted(int(r['position']) for r in tbl
                     if r['stratum'] == 'SYRIAC')
          == list(range(1, 23)), '44 rows')

    # --- TABLE -----------------------------------------------------------
    check('TABLE', 'the Imperial stratum == the source sequence, '
          'glyph for glyph in block order',
          [imp[chr(0x10840 + i)] for i in range(22)]
          == SOURCE_VALUES, '22/22')
    check('TABLE', 'the Syriac stratum == the source sequence, '
          'glyph for glyph at the standard\'s seats',
          [syr[chr(cp)] for cp in SYRIAC_CPS] == SOURCE_VALUES,
          '22/22')
    check('TABLE', 'the abjad class law holds at every cell of '
          'both strata (nine units, nine tens, four hundreds, '
          'recomputed from position)',
          all(imp[chr(0x10840 + i)] == abjad_value(i + 1)
              and syr[chr(SYRIAC_CPS[i])] == abjad_value(i + 1)
              for i in range(22)), '44/44 by the law')
    check('TABLE', 'singleness AND uniqueness in each stratum: '
          '22 letters, 22 distinct values, sum 1495',
          len(set(imp.values())) == 22 and sum(imp.values()) == 1495
          and len(set(syr.values())) == 22
          and sum(syr.values()) == 1495,
          (sum(imp.values()), sum(syr.values())))
    check('TABLE', 'Unicode names at the data seat == unicodedata, '
          'all 44 rows',
          all(ud.name(r['glyph'], '') == r['unicode_name']
              for r in tbl), '44/44 verified')

    # --- IDENTITY ---------------------------------------------------------
    check('IDENTITY', 'the identity table stands in data: 22 rows, '
          'relation IDENTICAL at every position',
          len(ident) == 22
          and all(r['relation'] == 'IDENTICAL' for r in ident),
          '22 rows')
    check('IDENTITY', 'value-for-value, Aramaic → Hebrew: at every '
          'position both strata carry the Hebrew base letter\'s '
          'hechrechi value',
          all(int(r['imperial_value'])
              == int(r['syriac_value'])
              == HEBREW_HECHRECHI[r['hebrew_glyph']]
              for r in ident), '22/22 positions')
    check('IDENTITY', 'value-for-value, Hebrew → Aramaic: every '
          'one of the 22 Hebrew base letters finds its value in '
          'both strata (the correspondence is the CSV\'s own '
          'hebrew_equivalent column)',
          all(any(r['hebrew_glyph'] == h
                  and int(r['imperial_value']) == v
                  and int(r['syriac_value']) == v
                  for r in ident)
              for h, v in HEBREW_HECHRECHI.items()
              if h in HEBREW_ORDER), '22/22 letters')
    check('IDENTITY', 'the correspondence itself is the witnesses\': '
          'each row\'s Hebrew glyph is the abjad-order twin the '
          'tables print (Wikipedia\'s equivalent columns; Cherry\'s '
          'pairing)',
          [r['hebrew_glyph'] for r in ident] == list(HEBREW_ORDER)
          and [r['imperial_glyph'] for r in ident]
          == [chr(0x10840 + i) for i in range(22)]
          and [r['syriac_glyph'] for r in ident]
          == [chr(cp) for cp in SYRIAC_CPS], '22/22 rows')

    # --- EXHIBITS -----------------------------------------------------------
    check('EXHIBITS', 'the founding head in three scripts: '
          'Imperial 𐡏𐡆 == Syriac ܥܙ == 77 from the frozen table '
          '(Hebrew עז = 70 + 7 by the constants)',
          weigh_imp('𐡏𐡆') == 77 and weigh_syr('ܥܙ') == 77
          and HEBREW_HECHRECHI['ע'] + HEBREW_HECHRECHI['ז'] == 77,
          (weigh_imp('𐡏𐡆'), weigh_syr('ܥܙ')))
    add = {s: weigh_syr(s)
           for s in ('ܬܩ', 'ܬܪ', 'ܬܫ', 'ܬܬ', 'ܬܬܩ')}
    check('EXHIBITS', 'the Syriac additive hundreds of Nöldeke\'s '
          'appendix recompute from the table: ܬܩ 500, ܬܪ 600, '
          'ܬܫ 700, ܬܬ 800, ܬܬܩ 900 — past 400 by ADDITION, '
          'no extended letter values',
          add == {'ܬܩ': 500, 'ܬܪ': 600, 'ܬܫ': 700, 'ܬܬ': 800,
                  'ܬܬܩ': 900}, add)
    ex = {s: weigh_syr(s) for s in ('ܝܒ', 'ܠܘ', 'ܩܢܙ', 'ܬܫܣܕ')}
    check('EXHIBITS', 'Hughes\' worked examples recompute: 12 '
          '(ܝܒ), 36 (ܠܘ), 157 (ܩܢܙ), 764 (ܬܫܣܕ)',
          ex == {'ܝܒ': 12, 'ܠܘ': 36, 'ܩܢܙ': 157, 'ܬܫܣܕ': 764}, ex)
    sweep = read_csv('aramaic-values.csv')
    syr_of = {r['hebrew_glyph']: r['syriac_glyph'] for r in ident}
    finals_of = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}

    def to_syriac(s):
        out = ''
        for c in s:
            c = finals_of.get(c, c)
            out += syr_of.get(c, c)
        return out

    bad = []
    for r in sweep:
        form = r['script_form']
        if any(c in syr for c in form):
            got = weigh_syr(form)
        else:
            got = weigh_syr(to_syriac(form))
        if got != int(r['value']):
            bad.append((r['term'], got, r['value']))
    check('EXHIBITS', 'the sweep\'s thirteen rows reproduce at '
          'the Syriac stratum through the seat correspondence '
          '(the eleven corpus weighings + the two 77 rows)',
          len(sweep) == 13 and not bad, bad or '13/13 agree')

    # --- BOUNDARY -----------------------------------------------------------
    check('BOUNDARY', 'the finals coordinate: NO final-form glyph '
          'is a key of either stratum, and no stratum value enters '
          '500–900 — the mispar gadol extension is not imported',
          all(g not in imp and g not in syr
              for g in MISPAR_GADOL_FINALS)
          and max(imp.values()) == 400
          and max(syr.values()) == 400,
          (max(imp.values()), max(syr.values())))
    check('BOUNDARY', 'the Hebrew seat the identity is measured '
          'against is hechrechi, not gadol: its finals stand at '
          'their letters\' values (ך 20, ם 40, ן 50, ף 80, ץ 90) '
          'in the constants, so no 500–900 enters the comparison '
          'from either side',
          all(HEBREW_HECHRECHI[f] == HEBREW_HECHRECHI[b]
              for f, b in finals_of.items()), '5/5 finals at base')
    check('BOUNDARY', 'the Imperial number signs are NOT letters '
          'of the table: none of U+10858–U+1085F is a key of the '
          'Imperial stratum, nor is the section sign',
          all(chr(cp) not in imp for cp in range(0x10857, 0x10860)),
          '9 signs unseated')
    check('BOUNDARY', 'the square script is not re-keyed in the '
          'data: no Hebrew-block glyph appears as a glyph of '
          'either stratum (its seat is the correspondence column, '
          'not a third stratum)',
          all(r['glyph'] not in HEBREW_HECHRECHI for r in tbl),
          '0 Hebrew glyphs among 44')

    failed = [r for r in RESULTS if not r[2]]
    print()
    print('ARAMAIC PHASE I AUDIT BATTERY — %d/%d PASS%s'
          % (len(RESULTS) - len(failed), len(RESULTS),
             '' if not failed else ' — FAILURES: %r' % (failed,)))
    print('BATTERY VERDICT: %s' % ('PASS' if not failed else 'FAIL'))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
