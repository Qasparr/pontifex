#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — slavonic_audit.py — the Slavonic Pair Phase II audit: builder
# Companion to THE-SLAVONIC-PAIR.md (the audit document of record) and
# Phase II of the Caucasus-and-the-North road.
#
# Epigraph: "values assigned according to the native alphabetic order
# of the Glagolitic alphabet" — Wikipedia, "Glagolitic numerals" (the
# one sentence in which the two systems of this pair part).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to
# the author's red pen. This file is an AUDIT instrument: findings,
# never doctrine. Nothing here is a bank; nothing here enters the engine.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: (i) the Cyrillic table is the Milesian table received —
#     its 27 seats will agree seat for seat with the living GREEK bank
#     under the witnesses' own Greek pairings; (ii) the Glagolitic
#     table is priced by its own alphabet's order — its values will
#     follow the class law down the block order of its valued letters,
#     parting only where the record itself parts (the doubled 10, the
#     hundreds hole, the questioned thousands tail); (iii) read by
#     shared sound, the two laws will agree across the middle band of
#     sounds and part at the head and the tail — the region's control
#     case proper.
#   Method: (1) transcribe both tables from witnesses read entire on
#     2026-11-24 and diff them in code where they overlap — Cyrillic:
#     Wikipedia, "Cyrillic numerals" (W1) against languagesandnumbers,
#     "Old Church Slavonic numbers" (W2, its lists sourced there to
#     Krause & Slocum's Old Church Slavonic Online); Glagolitic:
#     Wikipedia, "Glagolitic numerals" (W1) against the same W2's
#     Glagolitic list (printed in smalls; diffed through the case
#     map); an earlier edition of W1's Cyrillic article (W1b, 2017
#     oldid) is recorded as the same witness's earlier state, never
#     counted as independent; (2) hold Cyrillic against the living
#     GREEK bank under W1's printed Greek pairings; (3) hold
#     Glagolitic against its own order law in code; (4) compute the
#     parting table by shared sound; (5) recompute the witnesses'
#     worked examples before trusting any derived number.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Slavonic Pair audit data.

DOCTRINE: this script builds AUDIT data, not banks. The values below
are TRANSCRIPTIONS of published tables, carried with their sources on
their face; the parting table is a comparison at coordinates, not a
verdict. No row enters pontifex/engine.py from this file — the seats,
if the gate holds, are built separately and proven against the CSVs
this builder freezes.

MECHANISM: three CSVs are written beside this script —
  cyrillic-table.csv     the 27 canonical seats (status SOURCED), the
                         variant letterforms at their seats (status
                         VARIANT), and the refused western pair
                         (status REFUSED — printed, never seated);
  glagolitic-table.csv   the seated letters in block order (status
                         SOURCED, with the questioned thousands range
                         flagged in its own column), the unvalued
                         holes inside the valued runs (status HOLE),
                         and the refused composite spellings (status
                         REFUSED);
  slavonic-parting.csv   the two laws read by shared sound: the
                         Cyrillic seat, the Glagolitic seat, and the
                         computed relation per row.
The companion battery slavonic_audit_tests.py re-derives every number
the audit document prints from these CSVs and from its own independent
source constants.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from pontifex.tables import GREEK  # the parent bank, living

# -- Cyrillic W1: Wikipedia, "Cyrillic numerals" (read entire 2026-11-24) ----
# The table of values, canonical letter per seat, with W1's printed
# Greek counterpart per seat (the inheritance, on the witness's face).
CYR_W1 = [
    ('А', 'Α', 1), ('В', 'Β', 2), ('Г', 'Γ', 3), ('Д', 'Δ', 4),
    ('Е', 'Ε', 5), ('Ѕ', 'Ϛ', 6), ('З', 'Ζ', 7), ('И', 'Η', 8),
    ('Ѳ', 'Θ', 9),
    ('І', 'Ι', 10), ('К', 'Κ', 20), ('Л', 'Λ', 30), ('М', 'Μ', 40),
    ('Н', 'Ν', 50), ('Ѯ', 'Ξ', 60), ('О', 'Ο', 70), ('П', 'Π', 80),
    ('Ч', 'Ϟ', 90),
    ('Р', 'Ρ', 100), ('С', 'Σ', 200), ('Т', 'Τ', 300), ('У', 'Υ', 400),
    ('Ф', 'Φ', 500), ('Х', 'Χ', 600), ('Ѱ', 'Ψ', 700), ('Ѡ', 'Ω', 800),
    ('Ц', 'Ϡ', 900),
]
# W1's printed variants: alternative letterforms at a seat.
CYR_VARIANTS = {'Ѵ': 400, 'Ꙋ': 400, 'Ѹ': 400,  # the uk seat's forms
                'Ѿ': 800, 'Ꙍ': 800,              # the omega seat's forms
                'Ѧ': 900}                        # the sampi seat's form
# W1's printed western pair (its dagger note): in some Western
# varieties Ч carried 60 and Ҁ carried 90. Ҁ's 90 duplicates the
# canonical Ч seat; Ч's 60 contradicts it. The pair is REFUSED whole.
CYR_WESTERN = {'Ч@west': 60, 'Ҁ': 90}
CYR_W1_EXAMPLES = {'ѰЗ': 707, 'ЦЧѲ': 999}
CYR_W1_DEVICE_EXAMPLES = {'҂Ѕ': 6000, '҂Л҂В': 32000,
                          '҂АѰЕ': 1705, '҂АѰЅ': 1706, '҂ЗРИІ': 7118}

# -- Cyrillic W2: languagesandnumbers, "Old Church Slavonic numbers" --------
# (read entire 2026-11-24; its source line cites Krause & Slocum, Old
# Church Slavonic Online, UT Austin). Printed in smalls; transcribed
# here in capitals through the case map. Its 400 glyph is ѹ, the small
# of Ѹ — the uk digraph, a form of the 400 seat (a variant, below).
CYR_W2 = {
    'А': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ѕ': 6, 'З': 7, 'И': 8,
    'Ѳ': 9, 'І': 10, 'К': 20, 'Л': 30, 'М': 40, 'Н': 50, 'Ѯ': 60,
    'О': 70, 'П': 80, 'Ч': 90, 'Р': 100, 'С': 200, 'Т': 300,
    'Ф': 500, 'Х': 600, 'Ѱ': 700, 'Ѡ': 800, 'Ц': 900,
}
CYR_W2_VARIANT = {'Ѹ': 400}
CYR_W2_EXAMPLES = {'РНГ': 153, 'КЗ': 27, 'ОВ': 72}

# -- Glagolitic W1: Wikipedia, "Glagolitic numerals" (read entire) -----------
# The table of values as printed (capitals). The thousands range is
# printed under the witness's own warning, carried in the CSV's flag
# column: "the letters associated with number values greater than 999
# are uncertain" and "the validity of 3000 and greater is questioned".
GLA_W1 = {
    'Ⰰ': 1, 'Ⰱ': 2, 'Ⰲ': 3, 'Ⰳ': 4, 'Ⰴ': 5, 'Ⰵ': 6, 'Ⰶ': 7, 'Ⰷ': 8,
    'Ⰸ': 9,
    'Ⰺ': 10, 'Ⰻ': 20, 'Ⰼ': 30, 'Ⰽ': 40, 'Ⰾ': 50, 'Ⰿ': 60, 'Ⱀ': 70,
    'Ⱁ': 80, 'Ⱂ': 90,
    'Ⱃ': 100, 'Ⱄ': 200, 'Ⱅ': 300, 'Ⱆ': 400, 'Ⱇ': 500, 'Ⱈ': 600,
    'Ⱉ': 700, 'Ⱋ': 800, 'Ⱌ': 900,
    'Ⱍ': 1000, 'Ⱎ': 2000, 'Ⱏ': 3000, 'Ⱑ': 4000, 'Ⱓ': 5000,
    'Ⱔ': 9000,
}
# W1 prints the 10-seat as "Ⰺ or Ⰹ" — the holder disputed between the
# two adjacent letters. Both are carried here; the diff and the seat
# treat them together (the audit's D1).
GLA_W1_TEN_HOLDERS = ['Ⰺ', 'Ⰹ']
# W1's refused material: the composite spellings printed for
# 6000–8000 (spellings, not letters), recorded whole, never seated.
GLA_W1_COMPOSITES = {6000: 'ⰵ҃ⱍ҃', 7000: 'ⰶ҃ⱍ҃', 8000: 'ⰸ҃ⱍ҃'}
# W1b (the 2017 edition of the Cyrillic article, its Glagolitic
# thousands list) records variant readings of the same witness family:
# 3000 as "Ⱏ or Ⱐ", 6000 as the single letter Ⱗ. Printed, not seated.
GLA_W1B_VARIANTS = {'Ⱐ': 3000, 'Ⱗ': 6000}
GLA_W1_EXAMPLES = {'ⰗⰑⰂ': 583, 'ⰅⰊ': 16, 'ⰝⰔⰑ': 1280}

# -- Glagolitic W2: languagesandnumbers (the same page's Glagolitic list) ----
# Printed in SMALLS in its counting list; transcribed here through the
# case map (small -> capital). Its text list covers 1–100 and 1000;
# its 200–900 and 2000–5000 glyphs are images, not text (the gap is
# printed in the instrument).
GLA_W2 = {
    'Ⰰ': 1, 'Ⰱ': 2, 'Ⰲ': 3, 'Ⰳ': 4, 'Ⰴ': 5, 'Ⰵ': 6, 'Ⰶ': 7, 'Ⰷ': 8,
    'Ⰸ': 9, 'Ⰺ': 10, 'Ⰻ': 20, 'Ⰼ': 30, 'Ⰽ': 40, 'Ⰾ': 50, 'Ⰿ': 60,
    'Ⱀ': 70, 'Ⱁ': 80, 'Ⱂ': 90, 'Ⱃ': 100, 'Ⱍ': 1000,
}


def main():
    # ================= CYRILLIC =================
    w1 = {ch: v for ch, _, v in CYR_W1}
    assert len(w1) == 27
    partings = [(ch, w1[ch], CYR_W2[ch]) for ch in CYR_W2
                if CYR_W2[ch] != w1.get(ch)]
    assert not partings, 'CYRILLIC WITNESS PARTING: %r' % (partings,)
    # W2 prints 26 seats in canonical letters; the 27th seat (400)
    # arrives in W2 only as the uk digraph ѹ/Ѹ — a FORM of the seat,
    # carried below as a variant. The set coordinate is exact:
    assert set(CYR_W2) == set(w1) - {'У'} \
        and CYR_W2_VARIANT == {'Ѹ': w1['У']}, \
        'CYRILLIC WITNESS SET PARTING'
    print('CYRILLIC DIFF — W1 vs W2: 27/27 seats AGREE on value '
          '(26 in canonical letters; the 400-seat arrives in W2 as '
          'the uk digraph ѹ/Ѹ, a form of the seat, carried as a '
          'variant)')

    # The inheritance, against the living parent bank. (The bank is
    # keyed in small letters — its own seam folds case — so the
    # witnesses' printed capitals are folded here, epissemons and
    # all: Ϛ->ϛ, Ϟ->ϟ, Ϡ->ϡ are the standard's own case pairs.)
    bad = [(cyr, gr, v, GREEK.get(gr.lower())) for cyr, gr, v in CYR_W1
           if GREEK.get(gr.lower()) != v]
    assert not bad, 'INHERITANCE PARTING vs the GREEK bank: %r' % (bad,)
    print('INHERITANCE — all 27 Cyrillic seats == the living GREEK '
          'bank at the witnesses\' own Greek pairings (27/27)')

    table = dict(w1)
    for ch, v in CYR_VARIANTS.items():
        assert table.get(ch, v) == v
        table[ch] = v
    for word, expect in list(CYR_W1_EXAMPLES.items()) \
            + list(CYR_W2_EXAMPLES.items()):
        got = sum(table[ch] for ch in word)
        assert got == expect, 'EXAMPLE FAILS %s: %d != %d' % (word, got,
                                                              expect)
    print('CYRILLIC EXAMPLES — ѰЗ 707, ЦЧѲ 999, РНГ 153, КЗ 27, '
          'ОВ 72 recompute exact')

    rows = []
    for i, (ch, gr, v) in enumerate(CYR_W1, start=1):
        rows.append({'seat': i, 'letter': ch,
                     'codepoint': 'U+%04X' % ord(ch),
                     'unicode_name': ud.name(ch), 'greek_pair': gr,
                     'value': v, 'status': 'SOURCED'})
    for ch, v in sorted(CYR_VARIANTS.items(), key=lambda kv: kv[1]):
        rows.append({'seat': '', 'letter': ch,
                     'codepoint': 'U+%04X' % ord(ch),
                     'unicode_name': ud.name(ch), 'greek_pair': '',
                     'value': v, 'status': 'VARIANT'})
    for ch, v in CYR_WESTERN.items():
        letter = ch.split('@')[0]
        rows.append({'seat': '', 'letter': letter,
                     'codepoint': 'U+%04X' % ord(letter),
                     'unicode_name': ud.name(letter), 'greek_pair': '',
                     'value': v, 'status': 'REFUSED-WESTERN'})
    with open(os.path.join(HERE, 'cyrillic-table.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('CYRILLIC EXTENT — 27 canonical seats + %d variant forms '
          'seated; the western pair REFUSED whole (Ч@60 contradicts '
          'the canonical 90; Ҁ@90 travels with it)'
          % len(CYR_VARIANTS))

    # ================= GLAGOLITIC =================
    shared = set(GLA_W1) & set(GLA_W2)
    partings = [(ch, GLA_W1[ch], GLA_W2[ch]) for ch in shared
                if GLA_W1[ch] != GLA_W2[ch]]
    assert not partings, 'GLAGOLITIC WITNESS PARTING: %r' % (partings,)
    print('GLAGOLITIC DIFF — W1 vs W2 on the %d cells W2 prints in '
          'text: TOTAL AGREEMENT (incl. the 10-seat: W2 seats Ⰺ, '
          'one of W1\'s two printed holders)' % len(shared))

    gla = dict(GLA_W1)
    gla['Ⰹ'] = 10  # the 10-seat's second printed holder (D1)
    for word, expect in GLA_W1_EXAMPLES.items():
        got = sum(gla[ch] for ch in word)
        assert got == expect, 'EXAMPLE FAILS %s: %d != %d' % (word, got,
                                                              expect)
    print('GLAGOLITIC EXAMPLES — ⰗⰑⰂ 583, ⰅⰊ 16 (the teens '
          'reversal, on the Ⰺ holder), the Vinodol ⰝⰔⰑ 1280 '
          'recompute exact')

    # The order law over the valued letters, in block order: classes
    # run 9 / 10 / 9 / 6 valued letters; digits should run 1..9 per
    # class. Print every coordinate where they do not.
    block = [chr(cp) for cp in range(0x2C00, 0x2C2F)]
    valued = [ch for ch in block if ch in gla]
    law_breaks = []
    idx = {}
    for ch in valued:
        v = gla[ch]
        power = 0 if v < 10 else 1 if v < 100 else 2 if v < 1000 else 3
        idx[power] = idx.get(power, 0) + 1
        if v // (10 ** power) != idx[power]:
            law_breaks.append((ch, 'U+%04X' % ord(ch), idx[power],
                               v // (10 ** power), v))
    holes = [ch for ch in block
             if ch not in gla and 'Ⰰ' <= ch <= 'Ⱔ']
    print('GLAGOLITIC ORDER LAW — %d valued letters in block order; '
          'the digit law parts at %r; unvalued holes inside the '
          'valued span: %r' % (len(valued), law_breaks, holes))

    rows = []
    for ch in block:
        if ch in gla:
            v = gla[ch]
            rows.append({'block_seat': ord(ch) - 0x2C00 + 1,
                         'letter': ch,
                         'codepoint': 'U+%04X' % ord(ch),
                         'unicode_name': ud.name(ch), 'value': v,
                         'range_flag': ('QUESTIONED — W1: validity '
                                        'of 3000 and greater '
                                        'questioned'
                                        if v >= 3000 else
                                        'QUESTIONED — W1: values '
                                        'greater than 999 uncertain'
                                        if v >= 1000 else ''),
                         'status': 'SOURCED'})
        elif ch <= 'Ⱔ':
            rows.append({'block_seat': ord(ch) - 0x2C00 + 1,
                         'letter': ch,
                         'codepoint': 'U+%04X' % ord(ch),
                         'unicode_name': ud.name(ch), 'value': '',
                         'range_flag': '', 'status': 'HOLE'})
    for val, spelling in sorted(GLA_W1_COMPOSITES.items()):
        rows.append({'block_seat': '', 'letter': spelling,
                     'codepoint': '', 'unicode_name': '', 'value': val,
                     'range_flag': 'composite spelling in W1',
                     'status': 'REFUSED-COMPOSITE'})
    for ch, v in GLA_W1B_VARIANTS.items():
        rows.append({'block_seat': ord(ch) - 0x2C00 + 1, 'letter': ch,
                     'codepoint': 'U+%04X' % ord(ch),
                     'unicode_name': ud.name(ch), 'value': v,
                     'range_flag': 'W1b (2017 ed.) variant reading',
                     'status': 'REFUSED-VARIANT'})
    with open(os.path.join(HERE, 'glagolitic-table.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('GLAGOLITIC EXTENT — %d seated letters, %d distinct '
          'values, sum %d' % (len(gla), len(set(gla.values())),
                              sum(gla.values())))

    # ================= THE PARTING TABLE =================
    # The two laws read by shared sound. Each pair carries its
    # reasoning: the shared Slavic phoneme (or letter-name tradition)
    # that makes the pair one sound in two scripts.
    cyr_full = dict(table)  # canonical + variants
    PAIRS = [
        ('a', 'А', 'Ⰰ', 'az — the opening letter of both alphabets'),
        ('b', 'Б', 'Ⰱ', 'buky — Cyrillic Б descends from the same '
         'letter; the Cyrillic numeral table seats no Б'),
        ('v', 'В', 'Ⰲ', 'vede — one sound, two seats of two laws'),
        ('g', 'Г', 'Ⰳ', 'glagoli'),
        ('d', 'Д', 'Ⰴ', 'dobro'),
        ('e', 'Е', 'Ⰵ', 'yest'),
        ('zh', 'Ж', 'Ⰶ', 'zhivete — Cyrillic Ж seats nothing'),
        ('dz', 'Ѕ', 'Ⰷ', 'dzelo'),
        ('z', 'З', 'Ⰸ', 'zemlja'),
        ('i (from eta)', 'И', 'Ⰹ', 'izhe — the 10-seat\'s disputed '
         'holder on the Glagolitic side'),
        ('i (from iota)', 'І', 'Ⰺ', 'i — the 10-seat\'s other holder'),
        ('k', 'К', 'Ⰻ', 'kako'),
        ('l', 'Л', 'Ⰼ', 'ljudie'),
        ('m', 'М', 'Ⰽ', 'myslite'),
        ('n', 'Н', 'Ⰾ', 'nash'),
        ('o', 'О', 'Ⱀ', 'on'),
        ('p', 'П', 'Ⱁ', 'pokoj'),
        ('r', 'Р', 'Ⱃ', 'rьci'),
        ('s', 'С', 'Ⱄ', 'slovo'),
        ('t', 'Т', 'Ⱅ', 'tvrьdo'),
        ('u', 'У', 'Ⱆ', 'ukъ'),
        ('f', 'Ф', 'Ⱇ', 'frьtъ'),
        ('kh', 'Х', 'Ⱈ', 'xěrъ'),
        ('omega/ot', 'Ѡ', 'Ⱉ', 'the long-o seat: Cyrillic omega, '
         'Glagolitic otъ'),
        ('ts', 'Ц', 'Ⱌ', 'ci'),
        ('ch', 'Ч', 'Ⱍ', 'chrьvъ — the sharpest parting on the page'),
        ('sh', 'Ш', 'Ⱎ', 'sha — Cyrillic Ш seats nothing'),
        ('sht', 'Щ', 'Ⱋ', 'shta — Cyrillic Щ seats nothing'),
        ('small yus', 'Ѧ', 'Ⱔ', 'the yus seat: a Cyrillic variant at '
         '900, a Glagolitic thousands letter at 9000 (questioned '
         'range)'),
        ('fita/theta', 'Ѳ', 'Ⱚ', 'fita — Glagolitic Ⱚ seats nothing '
         'in W1\'s table'),
        ('izhitsa', 'Ѵ', 'Ⱛ', 'izhitsa — a Cyrillic variant at 400; '
         'Glagolitic Ⱛ seats nothing'),
        ('ksi', 'Ѯ', None, 'a Greek-borrowed seat: Cyrillic only'),
        ('psi', 'Ѱ', None, 'a Greek-borrowed seat: Cyrillic only'),
    ]
    prows = []
    for sound, c, g, why in PAIRS:
        cv = cyr_full.get(c) if c else None
        gv = gla.get(g) if g else None
        if cv is not None and gv is not None:
            rel = 'AGREE' if cv == gv else 'PART'
        elif cv is None and gv is not None:
            rel = 'PART — Cyrillic unseated'
        elif cv is not None and gv is None:
            rel = 'PART — Glagolitic unseated'
        else:
            rel = 'PART — both unseated'
        prows.append({'sound': sound, 'cyrillic_letter': c or '',
                      'cyrillic_value': cv if cv is not None else '',
                      'glagolitic_letter': g or '',
                      'glagolitic_value': gv if gv is not None else '',
                      'relation': rel, 'reasoning': why})
    with open(os.path.join(HERE, 'slavonic-parting.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(prows[0].keys()))
        w.writeheader()
        w.writerows(prows)
    agree = [r for r in prows if r['relation'] == 'AGREE']
    print('PARTING TABLE — %d sound rows: %d AGREE, %d PART'
          % (len(prows), len(agree), len(prows) - len(agree)))
    print('BUILT — cyrillic-table.csv, glagolitic-table.csv, '
          'slavonic-parting.csv')


if __name__ == '__main__':
    main()
