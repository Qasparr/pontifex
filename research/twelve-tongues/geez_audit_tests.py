#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — geez_audit_tests.py — the Ge'ez Phase I audit verification
# battery. Companion to geez_audit.py and THE-GEEZ-TABLES-PHASE-I-AUDIT.md.
#
# Epigraph: "Proponents of the halehame enumeration testify to the better
# results it offers when applied as Gematria." — geez.org, "Numerology".
# Testimony is not proof; this battery is the proof road.
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
#   Method: read ONLY the four CSVs geez_audit.py emits, plus the source
#     constants below (transcribed from geez.org's published table as
#     read 2026-11-24, and from the Unicode standard via unicodedata);
#     assert each printed number; report PASS/FAIL per check with a
#     summary and a nonzero exit on any failure.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Recompute every number the Ge'ez Phase I audit prints.

DOCTRINE: this battery settles by test everything a test can settle —
inventory counts, halehame coverage, the seating coordinates, the
zero-point boundaries. What no test can decide (the Debtera table's tier
classification) is not asserted here; it stands in the audit document as
the founder's open question, with its evidence.

MECHANISM: checks are grouped INVENTORY / HALEHAME / SEATING /
ZERO-POINT. Each check prints one line; the run ends with a count and
exits 0 only if every check passed.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- Source constants -----------------------------------------------------------
# DOCTRINE: SOURCE_VALUES is the audit's transcription of geez.org,
# "Numerology", Debtera (Halehame) Enumeration — the first-form value of
# each base in halehame order, read off the published table (which prints
# values in Ethiopic numerals: ሀ ፩ … ፐ ፰፻). The battery holds the CSV to
# THIS, not to the builder's copy: builder and battery transcribing the
# same source independently is what makes the comparison a check.
SOURCE_BASES = ['ሀ', 'ለ', 'ሐ', 'መ', 'ሠ', 'ረ', 'ሰ', 'ቀ', 'በ', 'ተ',
                'ኀ', 'ነ', 'አ', 'ከ', 'ወ', 'ዐ', 'ዘ', 'የ', 'ደ', 'ገ',
                'ጠ', 'ጰ', 'ጸ', 'ፀ', 'ፈ', 'ፐ']
SOURCE_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
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


def order_token_ok(name, order):
    # MECHANISM: the same suffix law the builder enforces (see
    # geez_audit.py) — re-derived here so the battery does not import
    # the builder's word for it.
    t = name.rsplit(' ', 1)[-1] if name else ''
    return {
        1: t.endswith('A') and not t.endswith('AA'),
        2: t.endswith('U'),
        3: t.endswith('I'),
        4: t.endswith('AA'),
        5: t.endswith('EE'),
        6: t.endswith('E') and not t.endswith('EE'),
        7: t.endswith('O'),
    }[order]


def main():
    inv = read_csv('geez-fidal-inventory.csv')
    hal = read_csv('geez-halehame-values.csv')
    seat = read_csv('geez-nine-seating.csv')
    zp = read_csv('geez-zero-point.csv')

    # ---- INVENTORY ------------------------------------------------------
    classical = [r for r in inv if r['series'] == 'classical']
    bases = sorted({r['base'] for r in classical},
                   key=lambda b: int(next(r['base_position'] for r in
                                          classical if r['base'] == b)))
    check('INVENTORY', 'classical grid is 26 bases x 7 orders = 182',
          len(classical) == 182 and len(bases) == 26
          and all(sum(1 for r in classical if r['base'] == b) == 7
                  for b in bases),
          f'{len(bases)} bases, {len(classical)} glyphs')
    check('INVENTORY', 'classical bases stand in halehame order',
          bases == SOURCE_BASES)
    bad_names = [r for r in classical
                 if not order_token_ok(ud.name(r['glyph']),
                                       int(r['order']))]
    check('INVENTORY', 'every classical glyph passes its Unicode '
          'order-name check', not bad_names,
          f'{182 - len(bad_names)}/182 verified against the standard')
    lab_c = [r for r in inv if r['series'] == 'labiovelar-classical']
    lab_p = [r for r in inv if r['series'] == 'labiovelar-postclassical']
    lab_orders = sorted({int(r['order']) for r in lab_c})
    check('INVENTORY', 'classical labiovelars: 4 series x 5 forms = 20, '
          'orders {1,3,4,5,6} only (no u-form, no o-form)',
          len(lab_c) == 20 and lab_orders == [1, 3, 4, 5, 6],
          f'{len(lab_c)} glyphs, orders {lab_orders}')
    check('INVENTORY', 'post-classical labiovelars inventoried '
          'separately: 2 series x 5 = 10', len(lab_p) == 10)
    check('INVENTORY', 'classical total 182 + 20 = 202',
          len(classical) + len(lab_c) == 202)
    eighth = [r for r in inv if r['series'] == 'eighth-slot']
    eighth_bases = {r['base'] for r in eighth}
    missing = [b for b in SOURCE_BASES if b not in eighth_bases]
    check('INVENTORY', '8th slot encoded for 25 of 26 classical bases; '
          'ዐ (Ayin) alone lacks one',
          len(eighth) == 25 and missing == ['ዐ'],
          f'{len(eighth)} eighth forms; missing: {missing}')
    numerals = [cp for cp in range(0x1369, 0x137D)
                if 'ETHIOPIC' in (ud.name(chr(cp), ''))]
    check('INVENTORY', 'the Ethiopic numerals are a separate glyph '
          'system: 20 signs, U+1369–U+137C', len(numerals) == 20)

    # ---- HALEHAME ---------------------------------------------------------
    sourced = [r for r in hal if r['status'] == 'SOURCED']
    gaps = [r for r in hal if r['status'] == 'GAP']
    check('HALEHAME', 'coverage: 26 of 26 classical bases SOURCED; '
          'the unreached classes printed as 2 GAP rows',
          len(sourced) == 26 and len(gaps) == 2)
    vals = {r['base']: int(r['folk_value_first_form']) for r in sourced}
    check('HALEHAME', 'every sourced value matches the geez.org '
          'transcription, sign for sign',
          all(vals[b] == v for b, v in zip(SOURCE_BASES, SOURCE_VALUES)))
    def formula(pos):
        return pos if pos <= 10 else (pos - 9) * 10 if pos <= 19 \
            else (pos - 18) * 100
    check('HALEHAME', 'the transcription also satisfies the class law '
          '(units 1–10 / tens / hundreds by position)',
          all(int(r['folk_value_first_form']) ==
              formula(int(r['halehame_position'])) for r in sourced))
    christos = sum(vals[c] for c in 'ከረሰተሰ')
    check('HALEHAME', "calibration: the tradition's worked example "
          'ክርስቶስ recomputes exact', christos == 80,
          f'ከ50 + ረ6 + ሰ7 + ተ10 + ሰ7 = {christos}')
    # MECHANISM: multiplier spot checks against the published grid's own
    # numerals (geez.org table) and Bekerie's examples via Daniels:
    # ለ order 2 = 4 (ሉ ፬); ተ order 7 = 70 (ቶ ፸); ኀ order 5 = 100 (ኄ ፻);
    # ፐ order 7 = 5600 (ፖ ፶፮፻; Bekerie's "po = 5600").
    spots = [('ለ', 2, 4), ('ሀ', 2, 2), ('ተ', 7, 70), ('ኀ', 5, 100),
             ('ፐ', 7, 5600)]
    check('HALEHAME', 'order-multiplier spot checks reproduce the '
          'published grid (incl. Bekerie’s po = 5600)',
          all(vals[b] * o == want for b, o, want in spots))
    check('HALEHAME', 'no labiovelar or later-added base carries a '
          'sourced value (the gap is in the data, not the prose)',
          all(r['folk_value_first_form'] == '' for r in gaps))

    # ---- SEATING ----------------------------------------------------------
    stations = [r['station'] for r in seat]
    check('SEATING', '11 rows: the Seven, the Α seam, the zero, '
          'the two hybrids',
          len(seat) == 11 and any('ΕΙ' in s for s in stations)
          and any('ΟΥ' in s for s in stations)
          and any('ZERO' in s for s in stations))
    unseated = [r['station'] for r in seat if 'UNSEATED' in r['seat']]
    check('SEATING', 'Η and Ω stand UNSEATED (the length gap), '
          'printed, not filled',
          len(unseated) == 2 and any('Η' in s for s in unseated)
          and any('Ω' in s for s in unseated))
    hybrids = [r for r in seat if 'CONSTRUCTED' in r['tier']]
    check('SEATING', 'both hybrid stations are tiered CONSTRUCTED',
          len(hybrids) == 2)
    check('SEATING', 'every seating row carries its reasoning '
          '(the correspondence rule)',
          all(len(r['reasoning']) > 40 for r in seat))
    # MECHANISM: the hybrid devices must exist in the inventoried grid —
    # the labiovelar series (for ΟΥ) and the glottal eighth form ኧ (for ΕΙ).
    check('SEATING', "ΟΥ's device exists in the inventory "
          '(labiovelar rows present)',
          len(lab_c) == 20)
    check('SEATING', "ΕΙ's device exists in the inventory "
          '(ኧ, the glottal 8th form, is seated)',
          any(r['glyph'] == 'ኧ' for r in eighth))

    # ---- ZERO POINT ---------------------------------------------------------
    agree = [r for r in zp if r['relation'].startswith('AGREE')]
    check('ZERO-POINT', 'agreement (folk value = grid position) holds '
          'at exactly positions 1–10',
          [int(r['grid_position']) for r in agree] == list(range(1, 11)))
    first_part = min((r for r in zp if r['relation'].startswith('PART')),
                     key=lambda r: int(r['grid_position']))
    check('ZERO-POINT', 'the boundary coordinate: first parting at '
          'position 11 — ኀ, position 11, folk 20',
          int(first_part['grid_position']) == 11
          and first_part['base'] == 'ኀ'
          and int(first_part['folk_value']) == 20)
    hinge = next(r for r in zp if int(r['grid_position']) == 19)
    first_hundred = next(r for r in zp if int(r['grid_position']) == 20)
    check('ZERO-POINT', 'the tens/hundreds hinge: ደ (19) = 100 closes '
          'the tens; ገ (20) = 200 opens the hundreds',
          int(hinge['folk_value']) == 100
          and int(first_hundred['folk_value']) == 200)
    check('ZERO-POINT', 'the order-6 exhibit: the folk law weights the '
          "key's zero at x6 for every base (recomputed)",
          all(int(r['folk_multiplier_at_order_6']) ==
              int(r['folk_value']) * 6 for r in zp))
    check('ZERO-POINT', 'the printed coincidence, numbers only: the '
          "folk maximum ፐ = 800 equals Ω's Milesian 800",
          int(zp[-1]['folk_value']) == 800 and zp[-1]['base'] == 'ፐ')

    passed = sum(1 for _, _, ok in RESULTS if ok)
    print(f"\n{passed}/{len(RESULTS)} CHECKS PASS")
    if passed != len(RESULTS):
        print('BATTERY VERDICT: FAIL')
        sys.exit(1)
    print('BATTERY VERDICT: PASS — every number the audit prints is '
          'recomputed. Findings, never doctrine. 93.')


if __name__ == '__main__':
    main()
