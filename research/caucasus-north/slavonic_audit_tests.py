#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — slavonic_audit_tests.py — the Slavonic Pair audit battery
# Companion to slavonic_audit.py and THE-SLAVONIC-PAIR.md.
#
# 93. Authorship: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved,
# Without Prejudice. Method of Science, Aim of Religion.
#
# MECHANISM: every check re-derives a number the audit document
# prints, from the frozen CSVs and from this battery's own independent
# source constants (the witnesses' tables restated here, not imported
# from the builder). Run: python3 slavonic_audit_tests.py.
# =============================================================================
"""The Phase II audit battery: the frozen Slavonic data, re-derived."""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from pontifex.tables import GREEK

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed)))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# The witnesses' tables restated independently (Wikipedia, "Cyrillic
# numerals" and "Glagolitic numerals", read entire 2026-11-24;
# languagesandnumbers concurring on every shared cell).
CYR = {
    'А': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ѕ': 6, 'З': 7, 'И': 8,
    'Ѳ': 9, 'І': 10, 'К': 20, 'Л': 30, 'М': 40, 'Н': 50, 'Ѯ': 60,
    'О': 70, 'П': 80, 'Ч': 90, 'Р': 100, 'С': 200, 'Т': 300,
    'У': 400, 'Ф': 500, 'Х': 600, 'Ѱ': 700, 'Ѡ': 800, 'Ц': 900,
}
CYR_VAR = {'Ѵ': 400, 'Ꙋ': 400, 'Ѹ': 400, 'Ѿ': 800, 'Ꙍ': 800,
           'Ѧ': 900}
GLA = {
    'Ⰰ': 1, 'Ⰱ': 2, 'Ⰲ': 3, 'Ⰳ': 4, 'Ⰴ': 5, 'Ⰵ': 6, 'Ⰶ': 7,
    'Ⰷ': 8, 'Ⰸ': 9, 'Ⰹ': 10, 'Ⰺ': 10, 'Ⰻ': 20, 'Ⰼ': 30, 'Ⰽ': 40,
    'Ⰾ': 50, 'Ⰿ': 60, 'Ⱀ': 70, 'Ⱁ': 80, 'Ⱂ': 90, 'Ⱃ': 100,
    'Ⱄ': 200, 'Ⱅ': 300, 'Ⱆ': 400, 'Ⱇ': 500, 'Ⱈ': 600, 'Ⱉ': 700,
    'Ⱋ': 800, 'Ⱌ': 900, 'Ⱍ': 1000, 'Ⱎ': 2000, 'Ⱏ': 3000,
    'Ⱑ': 4000, 'Ⱓ': 5000, 'Ⱔ': 9000,
}

with open(os.path.join(HERE, 'cyrillic-table.csv'), encoding='utf-8') as fh:
    cyr_rows = list(csv.DictReader(fh))
with open(os.path.join(HERE, 'glagolitic-table.csv'),
          encoding='utf-8') as fh:
    gla_rows = list(csv.DictReader(fh))
with open(os.path.join(HERE, 'slavonic-parting.csv'),
          encoding='utf-8') as fh:
    part = list(csv.DictReader(fh))

cyr = {r['letter']: int(r['value']) for r in cyr_rows
       if r['status'] == 'SOURCED'}
cyr_var = {r['letter']: int(r['value']) for r in cyr_rows
           if r['status'] == 'VARIANT'}
check('CYRILLIC — the frozen table stands: 27 SOURCED seats and 6 '
      'VARIANT forms, letter for letter against the witnesses as '
      'restated', cyr == CYR and cyr_var == CYR_VAR,
      (len(cyr), len(cyr_var)))
check('CYRILLIC — the refused western pair stands in the data as '
      'REFUSED, at its printed values (Ч@60, Ҁ@90), and Ҁ is no '
      'seat of the table',
      [(r['letter'], int(r['value'])) for r in cyr_rows
       if r['status'] == 'REFUSED-WESTERN'] == [('Ч', 60), ('Ҁ', 90)]
      and 'Ҁ' not in cyr and 'Ҁ' not in cyr_var,
      [(r['letter'], r['value']) for r in cyr_rows
       if r['status'] == 'REFUSED-WESTERN'])
check('CYRILLIC — every glyph is the standard\'s own: the CSV\'s '
      'Unicode names == unicodedata at every seated row',
      all(ud.name(r['letter']) == r['unicode_name'] for r in cyr_rows
          if r['status'] in ('SOURCED', 'VARIANT')),
      '33/33 verified')
check('CYRILLIC — THE INHERITANCE, re-derived: all 27 seats equal '
      'the living GREEK bank at the witnesses\' printed Greek '
      'pairings (the parent bank, not a transcription)',
      all(GREEK[r['greek_pair'].lower()] == int(r['value'])
          for r in cyr_rows if r['status'] == 'SOURCED'),
      '27/27 == GREEK')
full_cyr = dict(cyr)
full_cyr.update(cyr_var)
check('CYRILLIC — the witnesses\' examples recompute: ѰЗ 707, '
      'ЦЧѲ 999, РНГ 153, КЗ 27, ОВ 72',
      (sum(full_cyr[c] for c in 'ѰЗ'), sum(full_cyr[c] for c in 'ЦЧѲ'),
       sum(full_cyr[c] for c in 'РНГ'), sum(full_cyr[c] for c in 'КЗ'),
       sum(full_cyr[c] for c in 'ОВ')) == (707, 999, 153, 27, 72),
      sum(full_cyr[c] for c in 'ѰЗ'))
check('CYRILLIC — extent: 27 seats, 27 distinct canonical values, '
      'canonical sum 4995 (the Milesian sum itself); with variants '
      '33 letters, sum 8695',
      len(cyr) == 27 and len(set(cyr.values())) == 27
      and sum(cyr.values()) == 4995 and len(full_cyr) == 33
      and sum(full_cyr.values()) == 8695,
      (sum(cyr.values()), sum(full_cyr.values())))

gla = {r['letter']: int(r['value']) for r in gla_rows
       if r['status'] == 'SOURCED'}
check('GLAGOLITIC — the frozen table stands: 34 SOURCED letters, '
      'letter for letter against W1 as restated (with the 10-seat\'s '
      'second holder Ⰹ seated beside Ⰺ)',
      gla == GLA, (len(gla), gla == GLA))
check('GLAGOLITIC — the holes stand in the data as HOLE at their '
      'block seats: Ⱊ (27), Ⱐ (33), Ⱒ (35) — unvalued letters '
      'inside the valued span',
      [(r['letter'], int(r['block_seat'])) for r in gla_rows
       if r['status'] == 'HOLE'] == [('Ⱊ', 27), ('Ⱐ', 33), ('Ⱒ', 35)],
      [(r['letter'], r['block_seat']) for r in gla_rows
       if r['status'] == 'HOLE'])
check('GLAGOLITIC — the refused material stands refused: the three '
      'composite spellings (6000–8000) and W1b\'s two variant '
      'readings (Ⱐ@3000, Ⱗ@6000) carry no seat',
      sum(1 for r in gla_rows if r['status'] == 'REFUSED-COMPOSITE')
      == 3
      and [(r['letter'], int(r['value'])) for r in gla_rows
           if r['status'] == 'REFUSED-VARIANT']
      == [('Ⱐ', 3000), ('Ⱗ', 6000)]
      and 'Ⱗ' not in gla and gla.get('Ⱐ') is None,
      [r['status'] for r in gla_rows if r['status'].startswith('REFUSED')])
check('GLAGOLITIC — every glyph is the standard\'s own: Unicode '
      'names == unicodedata at the seated and hole rows',
      all(ud.name(r['letter']) == r['unicode_name'] for r in gla_rows
          if r['unicode_name']), '37/37 verified')
check('GLAGOLITIC — the witnesses\' examples recompute: ⰗⰑⰂ 583, '
      'ⰅⰊ 16, the Vinodol ⰝⰔⰑ 1280',
      (sum(gla[c] for c in 'ⰗⰑⰂ'), sum(gla[c] for c in 'ⰅⰊ'),
       sum(gla[c] for c in 'ⰝⰔⰑ')) == (583, 16, 1280),
      sum(gla[c] for c in 'ⰝⰔⰑ'))
# The order law restated independently: valued letters in block
# order, digits by class run.
valued = [r for r in gla_rows if r['status'] == 'SOURCED']
valued.sort(key=lambda r: int(r['block_seat']))
breaks, idx = [], {}
for r in valued:
    v = int(r['value'])
    p = 0 if v < 10 else 1 if v < 100 else 2 if v < 1000 else 3
    idx[p] = idx.get(p, 0) + 1
    if v // (10 ** p) != idx[p]:
        breaks.append(r['letter'])
check('GLAGOLITIC — THE ORDER LAW, re-derived: the digit law parts '
      'at exactly ten letters — the whole tens tail Ⰺ–Ⱂ downstream '
      'of the doubled 10, and Ⱔ at the thousands tail (digit 9 at '
      'run-index 6: the 6000–8000 seats are missing as letters)',
      breaks == ['Ⰺ', 'Ⰻ', 'Ⰼ', 'Ⰽ', 'Ⰾ', 'Ⰿ', 'Ⱀ', 'Ⱁ', 'Ⱂ', 'Ⱔ'],
      breaks)
check('GLAGOLITIC — extent: 34 letters, 33 distinct values, sum '
      '29005; the questioned range flagged in the data at every '
      'seat >= 1000',
      len(gla) == 34 and len(set(gla.values())) == 33
      and sum(gla.values()) == 29005
      and all(r['range_flag'] for r in valued
              if int(r['value']) >= 1000),
      (len(set(gla.values())), sum(gla.values())))

# -- The parting table ---------------------------------------------------------
check('PARTING — the frozen comparison stands: 33 sound rows, 15 '
      'AGREE, 18 PART',
      len(part) == 33
      and sum(1 for r in part if r['relation'] == 'AGREE') == 15,
      (len(part), sum(1 for r in part if r['relation'] == 'AGREE')))
check('PARTING — the agreement band exact: /a/, iota-/i/, and the '
      'run /k/ through /ts/ at 20,30,40,50,70,80,100,200,300,400,'
      '500,600,900 — and NO agreement inside the units class but /a/',
      [r['sound'] for r in part if r['relation'] == 'AGREE']
      == ['a', 'i (from iota)', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
          's', 't', 'u', 'f', 'kh', 'ts'],
      [r['sound'] for r in part if r['relation'] == 'AGREE'])
check('PARTING — the sharpest coordinates: /ch/ 90 against 1000; '
      'the omega seat 800 against 700 (the one parting inside the '
      'hundreds); the small yus 900 against 9000',
      [(r['cyrillic_value'], r['glagolitic_value']) for r in part
       if r['sound'] in ('ch', 'omega/ot', 'small yus')]
      == [('800', '700'), ('90', '1000'), ('900', '9000')],
      [(r['sound'], r['cyrillic_value'], r['glagolitic_value'])
       for r in part if r['sound'] in ('ch', 'omega/ot', 'small yus')])
check('PARTING — every row\'s printed values are the two frozen '
      'tables\' own (no third numbers enter the comparison)',
      all((not r['cyrillic_value']
           or full_cyr.get(r['cyrillic_letter'])
           == int(r['cyrillic_value']))
          and (not r['glagolitic_value']
               or gla.get(r['glagolitic_letter'])
               == int(r['glagolitic_value'])) for r in part),
      '33/33 rows held to the tables')

failed = [n for n, p in RESULTS if not p]
print()
print('SLAVONIC AUDIT BATTERY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)
