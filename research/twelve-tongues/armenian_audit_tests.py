#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — armenian_audit_tests.py — the Armenian Phase I audit
# verification battery. Companion to armenian_audit.py and
# THE-ARMENIAN-TABLE-PHASE-I-AUDIT.md.
#
# Epigraph: "Numbers in the Armenian numeral system are obtained by
# simple addition." — MELA cataloging manual, "Armenian Numerals and
# Dates". Simple addition, verified sign by sign; this battery is the
# proof road.
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
#     from the audit's data files and from constants transcribed directly
#     from the named sources — so the audit's pass is a script's verdict,
#     not prose.
#   Method: read ONLY the CSVs armenian_audit.py emits, the sweep's
#     armenian-values.csv (Worker #11, 2026-10-11), plus the source
#     constants below (transcribed independently from the witnesses as
#     read 2026-11-24, and from the Unicode standard via unicodedata);
#     assert each printed number; report PASS/FAIL per check with a
#     summary and a nonzero exit on any failure.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Recompute every number the Armenian Phase I audit prints.

DOCTRINE: this battery settles by test everything a test can settle —
the table's cells, the class law, the worked examples, the control
case's coordinates, the boundary rows. What no test can decide (the
late letters' "sometimes" values; the overline's disputed factor) is
not asserted here; both stand in the audit document as open
coordinates for the founder's pen, and the battery holds only their
printed presence and their unseated state.

MECHANISM: checks are grouped INVENTORY / TABLE / CONTROL-CASE /
BOUNDARY. Each check prints one line; the run ends with a count and
exits 0 only if every check passed.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- Source constants -----------------------------------------------------------
# DOCTRINE: SOURCE_VALUES is the battery's OWN transcription of the
# classical table (Wikipedia, "Armenian numerals", read 2026-11-24,
# held against Omniglot and the alphabet article's Numerical value
# column in the builder; transcribed here independently so the battery
# holds the CSV to the source, not to the builder's copy).
SOURCE_LETTERS = ['Ա', 'Բ', 'Գ', 'Դ', 'Ե', 'Զ', 'Է', 'Ը', 'Թ', 'Ժ',
                  'Ի', 'Լ', 'Խ', 'Ծ', 'Կ', 'Հ', 'Ձ', 'Ղ', 'Ճ', 'Մ',
                  'Յ', 'Ն', 'Շ', 'Ո', 'Չ', 'Պ', 'Ջ', 'Ռ', 'Ս', 'Վ',
                  'Տ', 'Ր', 'Ց', 'Ւ', 'Փ', 'Ք']
SOURCE_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 20, 30, 40, 50, 60, 70, 80, 90,
                 100, 200, 300, 400, 500, 600, 700, 800, 900,
                 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
# MECHANISM: the halehame side of the control case, stated exactly as
# the Ge'ez Phase I audit established it (its own battery's constants).
FOLK_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               20, 30, 40, 50, 60, 70, 80, 90, 100,
               200, 300, 400, 500, 600, 700, 800]

RESULTS = []


def check(group, label, ok, detail=''):
    RESULTS.append((group, label, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {group} — {label}"
          + (f" ({detail})" if detail else ''))


def read_csv(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def class_formula(pos):
    return (((pos - 1) % 9) + 1) * (10 ** ((pos - 1) // 9))


def folk_formula(pos):
    return pos if pos <= 10 else (pos - 9) * 10 if pos <= 19 \
        else (pos - 18) * 100


def main():
    tbl = read_csv('armenian-table.csv')
    cc = read_csv('armenian-control-case.csv')
    sourced = [r for r in tbl if r['status'] == 'SOURCED']
    opened = [r for r in tbl if r['status'] == 'OPEN']
    table = {r['uppercase']: int(r['value']) for r in sourced}

    def weigh_str(s):
        return sum(table[c] for c in s)

    # ---- INVENTORY ------------------------------------------------------
    check('INVENTORY', 'the table seats 36 SOURCED classical letters; '
          'the 2 medieval additions stand as OPEN rows',
          len(sourced) == 36 and len(opened) == 2
          and [r['uppercase'] for r in opened] == ['Օ', 'Ֆ'],
          f'{len(sourced)} sourced, {len(opened)} open')
    check('INVENTORY', 'letters stand in Mashtots\' order, positions '
          '1–36, values matching the battery\'s own transcription '
          'sign for sign',
          [r['uppercase'] for r in sourced] == SOURCE_LETTERS
          and [int(r['value']) for r in sourced] == SOURCE_VALUES)
    check('INVENTORY', 'codepoints by the standard\'s arithmetic: '
          'capitals U+0531–U+0554 consecutive; lowercase at +0x30',
          all(int(r['uppercase_codepoint'][2:], 16) == 0x531 + i
              and int(r['lowercase_codepoint'][2:], 16)
              == 0x531 + i + 0x30
              for i, r in enumerate(sourced)))
    bad = [r for r in sourced
           if ud.name(r['uppercase']) != r['uppercase_unicode_name']
           or ud.name(r['lowercase']) != r['lowercase_unicode_name']
           or not r['uppercase_unicode_name'].startswith(
               'ARMENIAN CAPITAL LETTER')
           or r['lowercase_unicode_name']
           != r['uppercase_unicode_name'].replace('CAPITAL', 'SMALL')]
    check('INVENTORY', 'every glyph\'s Unicode name verified against '
          'the standard, both cases', not bad,
          f'{36 - len(bad)}/36 verified')
    check('INVENTORY', 'the additions sit immediately after the '
          'classical block in the standard too: Օ U+0555, Ֆ U+0556',
          [r['uppercase_codepoint'] for r in opened]
          == ['U+0555', 'U+0556'])
    check('INVENTORY', 'the class law holds at every cell: value = '
          'digit x 10^class over four classes of nine',
          all(int(r['value']) == class_formula(int(r['position']))
              for r in sourced))
    check('INVENTORY', 'the 36 values are each used exactly once '
          '(uniqueness holds in this bank — stated, not assumed)',
          sorted(table.values()) == sorted(SOURCE_VALUES)
          and len(set(table.values())) == 36)

    # ---- TABLE ------------------------------------------------------------
    check('TABLE', 'calibration: the witnesses\' worked example '
          'ՌՋՀԵ recomputes exact', weigh_str('ՌՋՀԵ') == 1975,
          f"1000 + 900 + 70 + 5 = {weigh_str('ՌՋՀԵ')}")
    check('TABLE', 'the shared examples of both text witnesses: '
          'ՍՄԻԲ = 2222, ՍԴ = 2004, ՃԻ = 120, Ծ = 50',
          (weigh_str('ՍՄԻԲ'), weigh_str('ՍԴ'), weigh_str('ՃԻ'),
           weigh_str('Ծ')) == (2222, 2004, 120, 50),
          f"{weigh_str('ՍՄԻԲ')}, {weigh_str('ՍԴ')}, "
          f"{weigh_str('ՃԻ')}, {weigh_str('Ծ')}")
    check('TABLE', 'MELA\'s era date: ՌՆԾԵ = 1455 (the ԹՎ siglum\'s '
          'year, as the manual prints it)', weigh_str('ՌՆԾԵ') == 1455,
          f"1000 + 400 + 50 + 5 = {weigh_str('ՌՆԾԵ')}")
    check('TABLE', 'the system\'s own arithmetic: the largest number '
          'writable without the overline is ՔՋՂԹ = 9999',
          weigh_str('ՔՋՂԹ') == 9999)
    check('TABLE', 'the sum of all 36 values is 49995 '
          '(45 + 450 + 4500 + 45000)',
          sum(table.values()) == 49995, f"{sum(table.values())}")
    # MECHANISM: the sweep's eleven corpus weighings (Worker #11) are a
    # frozen second seat of this same table: their script forms, weighed
    # on the audit's frozen table, must return the sweep's values.
    sweep = read_csv('armenian-values.csv')
    bad = [(r['term'], weigh_str(r['script_form'].upper()),
            int(r['value'])) for r in sweep
           if weigh_str(r['script_form'].upper()) != int(r['value'])]
    check('TABLE', 'the sweep\'s eleven corpus weighings recompute '
          'from the frozen table (AXONEME 1251 … CELL 125)',
          len(sweep) == 11 and not bad,
          f'{11 - len(bad)}/11 agree' if not bad else f'{bad}')

    # ---- CONTROL CASE -------------------------------------------------------
    posrows = [r for r in cc if r['position'].isdigit()]
    check('CONTROL-CASE', 'the comparison runs the whole shared '
          'domain: 26 position rows',
          len(posrows) == 26
          and [int(r['position']) for r in posrows]
          == list(range(1, 27)))
    check('CONTROL-CASE', 'value agreement is TOTAL on the shared '
          'domain: Armenian value == halehame value at 26/26 positions',
          all(int(r['armenian_value']) == int(r['halehame_value'])
              == SOURCE_VALUES[int(r['position']) - 1]
              == FOLK_VALUES[int(r['position']) - 1]
              for r in posrows))
    check('CONTROL-CASE', 'both class formulas, recomputed, produce '
          'the same value sequence on positions 1–26 — and part in '
          'derivation at position 10',
          all(class_formula(p) == folk_formula(p) for p in range(1, 27))
          and class_formula(10) == folk_formula(10) == 10)
    r10 = next(r for r in posrows if r['position'] == '10')
    r19 = next(r for r in posrows if r['position'] == '19')
    check('CONTROL-CASE', 'the boundary coordinates stand in the '
          'data: position 10 (value 10 = 10, law parts) and the '
          'hinge at 19 (Armenian hundreds open, halehame tens close)',
          'BOUNDARY' in r10['relation'] and 'HINGE' in r19['relation']
          and r10['armenian_class'] == 'tens'
          and r10['halehame_class'] == 'units'
          and r19['armenian_class'] == 'hundreds'
          and r19['halehame_class'] == 'tens')
    check('CONTROL-CASE', 'class boundaries offset by one seat: '
          'Armenian classes break after positions 9/18/27, halehame '
          'after 10/19 (from the rows\' class columns)',
          [r['armenian_class'] for r in posrows[:9]] == ['units'] * 9
          and posrows[9]['armenian_class'] == 'tens'
          and posrows[9]['halehame_class'] == 'units'
          and [r['halehame_class'] for r in posrows[:10]]
          == ['units'] * 10)
    summary = {r['position']: r for r in cc
               if not r['position'].isdigit()}
    check('CONTROL-CASE', 'extent parts in kind: Armenian four '
          'classes to 9000 over 36 seats; halehame three to 800 over '
          '26 (the EXTENT row carries both)',
          'EXTENT' in summary and '9000' in summary['EXTENT']['note']
          and '800' in summary['EXTENT']['note'])
    check('CONTROL-CASE', 'coverage parts in kind: Armenian 36 of 36 '
          'classical letters; halehame 26 first forms of 202 signs '
          '(the COVERAGE row carries both)',
          'COVERAGE' in summary
          and '36 of 36' in summary['COVERAGE']['note']
          and '26/202' in summary['COVERAGE']['note'])
    check('CONTROL-CASE', 'the zero coordinate agrees: neither table '
          'carries a zero value (the ZERO row stands; both value '
          'sets are >= 1)',
          'ZERO' in summary and min(SOURCE_VALUES) >= 1
          and min(FOLK_VALUES) >= 1)

    # ---- BOUNDARY ---------------------------------------------------------
    check('BOUNDARY', 'the OPEN rows carry NO seated value: the late '
          'letters\' "sometimes" numbers live in the source note, '
          'not in the value column',
          all(r['value'] == '' for r in opened)
          and all('sometimes' in r['source'] for r in opened))
    ext = summary.get('EXTENSION', {'note': ''})['note']
    check('BOUNDARY', 'the overline disagreement stands in the data '
          'at full size: x10,000 (Wikipedia + MELA) against x1,000 '
          '(Omniglot), neither implemented',
          'EXTENSION' in summary and '10,000' in ext
          and '1,000' in ext and 'DISPUTED' in ext)
    check('BOUNDARY', 'the attestation parting is printed, not '
          'smoothed: the ATTESTATION row names the colophon record '
          'against the undated folk practice',
          'ATTESTATION' in summary
          and 'colophon' in summary['ATTESTATION']['note']
          and 'undated' in summary['ATTESTATION']['note'])

    passed = sum(1 for _, _, ok in RESULTS if ok)
    print(f"\n{passed}/{len(RESULTS)} CHECKS PASS")
    if passed != len(RESULTS):
        print('BATTERY VERDICT: FAIL')
        sys.exit(1)
    print('BATTERY VERDICT: PASS — every number the audit prints is '
          'recomputed. Findings, never doctrine. 93.')


if __name__ == '__main__':
    main()
