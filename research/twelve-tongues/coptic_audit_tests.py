#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — coptic_audit_tests.py — the Coptic Phase I audit
# verification battery. Companion to coptic_audit.py and
# THE-COPTIC-TABLE-PHASE-I-AUDIT.md.
#
# Epigraph: "Coptic counts with letters, the way Greek did: a letter
# with a stroke above it is a number." — fsymbols, "Coptic numbers
# 1–10 and the epact numerals" (the inheritance, in the witness's
# own words).
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
#   Hypothesis: every number the audit document prints can be recomputed
#     from the audit's data files, from constants transcribed directly
#     from the named sources, and from the engine's living Greek bank —
#     so the audit's pass is a script's verdict, not prose.
#   Method: read ONLY the CSVs coptic_audit.py emits, the sweep's
#     coptic-values.csv (Worker #8, 2026-10-11), the source constants
#     below (transcribed independently from the witnesses as read
#     2026-11-24, and from the Unicode standard via unicodedata), and
#     pontifex.tables.GREEK imported fresh; assert each printed number;
#     report PASS/FAIL per check with a summary and a nonzero exit on
#     any failure.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Recompute every number the Coptic Phase I audit prints.

DOCTRINE: this battery settles by test everything a test can settle —
the table's cells, the witnesses' examples, the descent's coordinates
against the living Greek bank, the boundary rows. What no test can
decide (the stauros thousands sign's seating; the epact system's
future bank) is not asserted here; both stand in the audit document
as open coordinates for the founder's pen, and the battery holds
only their printed presence and their unseated state.

MECHANISM: checks are grouped INVENTORY / TABLE / DESCENT /
BOUNDARY. Each check prints one line; the run ends with a count and
exits 0 only if every check passed.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))  # the pontifex package
from pontifex.tables import GREEK  # noqa: E402 — the living parent bank

# -- Source constants -----------------------------------------------------------
# DOCTRINE: the battery's OWN transcription of the witnesses' table
# (Wikipedia, "Coptic script", Letters table, read 2026-11-24, held
# against fsymbols and tooldune in the builder; transcribed here
# independently so the battery holds the CSV to the source, not to
# the builder's copy). None marks the witnesses' dash.
SOURCE_ROWS = [
    ('Ⲁ', 1), ('Ⲃ', 2), ('Ⲅ', 3), ('Ⲇ', 4), ('Ⲉ', 5), ('Ⲋ', 6),
    ('Ⲍ', 7), ('Ⲏ', 8), ('Ⲑ', 9), ('Ⲓ', 10), ('Ⲕ', 20), ('Ⲗ', 30),
    ('Ⲙ', 40), ('Ⲛ', 50), ('Ⲝ', 60), ('Ⲟ', 70), ('Ⲡ', 80),
    ('Ⲣ', 100), ('Ⲥ', 200), ('Ⲧ', 300), ('Ⲩ', 400), ('Ⲫ', 500),
    ('Ⲭ', 600), ('Ⲯ', 700), ('Ⲱ', 800),
    ('Ϣ', None), ('Ϥ', 90), ('Ϧ', None), ('Ⳉ', None), ('Ϩ', None),
    ('Ϫ', None), ('Ϭ', None), ('Ϯ', None), ('Ⳁ', 900),
]
MILESIAN = [1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 20, 30, 40, 50, 60, 70, 80, 90,
            100, 200, 300, 400, 500, 600, 700, 800, 900]
NO_VALUE_CAPS = ['Ϣ', 'Ϧ', 'Ⳉ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ']
# MECHANISM: the sweep's two fail-closed partials, transcribed from
# coptic.md §1.5 (HERU-RA-HA 677; ABRAHADABRA 213).
SWEEP_PARTIALS = {'HERU-RA-HA': 677, 'ABRAHADABRA': 213}

RESULTS = []


def check(group, label, ok, detail=''):
    RESULTS.append((group, label, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {group} — {label}"
          + (f" ({detail})" if detail else ''))


def read_csv(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def main():
    tbl = read_csv('coptic-table.csv')
    desc = read_csv('coptic-descent.csv')
    sourced = [r for r in tbl if r['status'] == 'SOURCED']
    novalue = [r for r in tbl if r['status'] == 'NO VALUE']
    table = {r['lowercase']: int(r['value']) for r in sourced}

    def weigh_str(s):
        return sum(table[c] for c in s)

    # ---- INVENTORY ------------------------------------------------------
    check('INVENTORY', 'the table seats 27 SOURCED signs; the 7 '
          'Demotic rows beyond fai stand as NO VALUE rows',
          len(sourced) == 27 and len(novalue) == 7
          and [r['uppercase'] for r in novalue] == NO_VALUE_CAPS,
          f'{len(sourced)} sourced, {len(novalue)} no-value')
    check('INVENTORY', 'rows stand in the witnesses\' order, values '
          'matching the battery\'s own transcription sign for sign',
          [(r['uppercase'], int(r['value']) if r['value'] else None)
           for r in tbl] == SOURCE_ROWS)
    greek_rows = tbl[:25]
    demotic_block = ['Ϣ', 'Ϥ', 'Ϧ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ']
    check('INVENTORY', 'codepoints by the standard\'s arithmetic: '
          'the Greek-side rows at U+2C80 + 2k consecutive; the '
          'Demotic pairs in the Greek block at U+03E2 + 2k; Ⳉ at '
          'U+2CC8; Ⳁ at U+2CC0; the small at capital + 1 at all 34',
          all(int(r['uppercase_codepoint'][2:], 16) == 0x2C80 + 2 * i
              for i, r in enumerate(greek_rows))
          and all(int(next(r for r in tbl
                           if r['uppercase'] == cap)
                      ['uppercase_codepoint'][2:], 16) == 0x03E2 + 2 * i
                  for i, cap in enumerate(demotic_block))
          and next(r for r in tbl if r['uppercase'] == 'Ⳉ')
              ['uppercase_codepoint'] == 'U+2CC8'
          and next(r for r in tbl if r['uppercase'] == 'Ⳁ')
              ['uppercase_codepoint'] == 'U+2CC0'
          and all(int(r['lowercase_codepoint'][2:], 16)
                  == int(r['uppercase_codepoint'][2:], 16) + 1
                  for r in tbl))
    bad = [r for r in tbl
           if ud.name(r['uppercase']) != r['uppercase_unicode_name']
           or ud.name(r['lowercase']) != r['lowercase_unicode_name']
           or not r['uppercase_unicode_name'].startswith(
               'COPTIC CAPITAL LETTER')
           or r['lowercase_unicode_name']
           != r['uppercase_unicode_name'].replace('CAPITAL', 'SMALL')]
    check('INVENTORY', 'every glyph\'s Unicode name verified against '
          'the standard, both cases', not bad,
          f'{34 - len(bad)}/34 verified')
    check('INVENTORY', 'the valued signs carry exactly the Milesian '
          'sequence: three classes of nine, 1–9 / 10–90 / 100–900',
          sorted(table.values()) == MILESIAN
          and [sum(1 for v in table.values() if v in cls) for cls in
               (range(1, 10), range(10, 100, 10),
                range(100, 1000, 100))] == [9, 9, 9])
    check('INVENTORY', 'the 27 values are each used exactly once '
          '(uniqueness holds — stated, not assumed); sum 4995',
          len(set(table.values())) == 27
          and sum(table.values()) == 4995, f"{sum(table.values())}")

    # ---- TABLE ------------------------------------------------------------
    check('TABLE', 'calibration: the witnesses\' worked examples '
          'recompute exact — ⲫ = 500 (W1); ⲓⲃ = 12, ⲧⲝⲉ = 365 (W2)',
          (weigh_str('ⲫ'), weigh_str('ⲓⲃ'), weigh_str('ⲧⲝⲉ'))
          == (500, 12, 365),
          f"{weigh_str('ⲫ')}, {weigh_str('ⲓⲃ')}, {weigh_str('ⲧⲝⲉ')}")
    check('TABLE', 'W1\'s thousands example, letter part: ⲱⲡⲏ = 888 '
          '(of ⲁ͵ⲱ̅ⲡ̅ⲏ̅ = 1,888 — the ⲁ͵ device reported, not priced)',
          weigh_str('ⲱⲡⲏ') == 888, f"800 + 80 + 8 = {weigh_str('ⲱⲡⲏ')}")
    # MECHANISM: W2 prints ⲓ̅ at the end of its 1–10 run and opens
    # its tens run at ⲕ̅ (20–90, summing 440); the tens CLASS entire
    # (ⲓ through ϥ, 10–90) sums 450. The check weighs the class.
    check('TABLE', 'the sequences W2 prints: 1–10 cumulative 55; '
          'the tens class (10–90) sums 450; the hundreds sum 4500',
          weigh_str('ⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓ') == 55
          and weigh_str('ⲓⲕⲗⲙⲛⲝⲟⲡϥ') == 450
          and weigh_str('ⲣⲥⲧⲩⲫⲭⲯⲱⳁ') == 4500,
          f"{weigh_str('ⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓ')}, "
          f"{weigh_str('ⲓⲕⲗⲙⲛⲝⲟⲡϥ')}, "
          f"{weigh_str('ⲣⲥⲧⲩⲫⲭⲯⲱⳁ')}")
    check('TABLE', 'the system\'s own arithmetic: the largest number '
          'writable in letters alone is ⳁϥⲑ = 999',
          weigh_str('ⳁϥⲑ') == 999)
    # MECHANISM: the sweep's corpus (Worker #8) is a frozen second
    # seat of this same table: its valued rows must recompute from
    # the audit's frozen table, and its two UNKNOWN rows must fail
    # closed — a letter outside the table present, the weighable
    # partial exactly the sweep's printed partial.
    sweep = read_csv('coptic-values.csv')
    bad = []
    for r in sweep:
        form = r['script_form']
        if r['value'] == 'UNKNOWN':
            partial = sum(table.get(c, 0) for c in form)
            outside = [c for c in form if c not in table]
            if not outside or partial != SWEEP_PARTIALS[r['term']]:
                bad.append((r['term'], partial, outside))
        elif sum(table.get(c, 0) for c in form) != int(r['value']) \
                or any(c not in table for c in form):
            bad.append((r['term'], r['value']))
    check('TABLE', 'the sweep\'s seventeen corpus rows recompute '
          'from the frozen table: 15 valued exact, 2 UNKNOWN failing '
          'closed at their printed partials (677, 213)',
          len(sweep) == 17 and not bad,
          f'{17 - len(bad)}/17 agree' if not bad else f'{bad}')

    # ---- DESCENT ----------------------------------------------------------
    seat_rows = [r for r in desc if r['value'].isdigit()]
    check('DESCENT', 'the descent runs the whole Milesian domain: '
          '27 seat rows, values 1–900',
          len(seat_rows) == 27
          and [int(r['value']) for r in seat_rows] == MILESIAN)
    check('DESCENT', 'VALUE AGREEMENT IS TOTAL: the living Greek '
          'bank\'s value set == the Coptic table\'s value set, '
          '27 seats, seat for seat',
          set(GREEK.values()) == set(table.values())
          and all(GREEK[r['greek_sign']] == int(r['value'])
                  == table[r['coptic_sign']] for r in seat_rows),
          '27/27 seats agree')
    check('DESCENT', 'every seat relation opens AGREE — the '
          'partings are of kind, lineage, and form, never of value',
          all(r['relation'].startswith('AGREE') for r in seat_rows))
    parts = {int(r['value']): r['relation'] for r in seat_rows
             if 'PART' in r['relation']}
    check('DESCENT', 'the parting coordinates stand in the data: '
          'kind at 6 and 900, lineage at 90, form at 200 — and '
          'nowhere else',
          set(parts) == {6, 90, 900, 200}
          and 'PART in kind' in parts[6]
          and 'PART IN LINEAGE' in parts[90]
          and 'PART in kind' in parts[900]
          and 'PART in form' in parts[200],
          f'{sorted(parts)}')
    extra = set(GREEK) - {r['greek_sign'] for r in seat_rows}
    check('DESCENT', 'the Greek bank\'s two extra keys are exactly '
          'ς (200, the final form) and στ (6, the digraph) — form '
          'and apparatus, with no Coptic counterpart key',
          extra == {'ς', 'στ'} and GREEK['ς'] == 200
          and GREEK['στ'] == 6, f'{sorted(extra)}')
    summary = {r['value']: r for r in desc
               if not r['value'].isdigit()}
    native = summary.get('NATIVE', {'coptic_sign': ''})
    check('DESCENT', 'the NATIVE row names exactly the unseated: '
          'the 7 NO VALUE smalls, keys of neither bank',
          set(native['coptic_sign'].split())
          == {r['lowercase'] for r in novalue}
          and all(r['lowercase'] not in table for r in novalue)
          and all(r['lowercase'] not in GREEK for r in novalue))

    # ---- BOUNDARY ---------------------------------------------------------
    check('BOUNDARY', 'the NO VALUE rows carry NO seated value: the '
          'dash lives in the status column, the value column empty',
          all(r['value'] == '' for r in novalue)
          and all(r['status'] == 'NO VALUE' for r in novalue))
    thou = summary.get('THOUSANDS', {'note': ''})['note']
    check('BOUNDARY', 'the thousands parting stands in the data at '
          'full size: the mark devices (U+0375; double overline) '
          'and Satzinger\'s stauros, neither seated; no letter '
          'value exceeds 900',
          'THOUSANDS' in summary and 'U+0375' in thou
          and 'stauros' in thou and max(table.values()) == 900)
    sampi = next(r for r in tbl if r['uppercase'] == 'Ⳁ')
    check('BOUNDARY', 'sampi\'s standing is printed, not smoothed: '
          'row 34, SOURCED at 900, its origin naming it a sign '
          'outside the 32-letter alphabet (34 rows = 32 letters + '
          'the second khai glyph + sampi)',
          sampi['status'] == 'SOURCED' and sampi['value'] == '900'
          and 'sampi sign' in sampi['origin'] and len(tbl) == 34)

    passed = sum(1 for _, _, ok in RESULTS if ok)
    print(f"\n{passed}/{len(RESULTS)} CHECKS PASS")
    if passed != len(RESULTS):
        print('BATTERY VERDICT: FAIL')
        sys.exit(1)
    print('BATTERY VERDICT: PASS — every number the audit prints is '
          'recomputed. Findings, never doctrine. 93.')


if __name__ == '__main__':
    main()
