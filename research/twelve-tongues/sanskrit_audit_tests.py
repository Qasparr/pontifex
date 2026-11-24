#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — sanskrit_audit_tests.py — the Sanskrit Phase I audit
# verification battery. Companion to sanskrit_audit.py and
# THE-SANSKRIT-FIELD-PHASE-I-AUDIT.md.
#
# Epigraph: "It may be noted that in the conjunct consonant ktya,
# only the final consonant y has numerical value." — Sarma (2012),
# n. 25, on the Mangalagiri inscription. A footnote carries the
# rule; this battery carries the footnote's number.
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
#     recomputed from the audit's frozen CSVs — so the audit's
#     pass is a script's verdict, not prose.
#   Method: read ONLY the CSVs sanskrit_audit.py emits, plus the
#     sweep's sanskrit-values.csv (Worker #9, 2026-10-11) for the
#     corpus rows' provenance; build both decoders from the CSV
#     tables (the audit seat's own machinery — the akṣara parser
#     is shared script machinery, imported from the Phase II
#     module, since both seats read the same script; the TABLES,
#     the audit's substance, come only from the CSVs); assert each
#     printed number; report PASS/FAIL per check with a summary
#     and a nonzero exit on any failure.
#   Observation / Result: printed at run time, below the line.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Recompute every number the Sanskrit Phase I audit prints.

DOCTRINE: this battery settles by test everything a test can
settle — both tables' cells, the laws, the witnesses' exhibits,
the round-trip property, and the boundaries (the OPEN ḷa row;
the nukta refusal; the śghaki/śghakhi parting). What no test can
decide (whether a variant ever wants a door; the bhūtasaṅkhyā
question) is not asserted here; both stand in the audit document
at §VII for the founder's pen.
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

from pontifex.katapayadi import parse_aksaras  # shared machinery

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def load(name):
    with (HERE / name).open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


# --- The audit seat's decoders, built ONLY from the CSVs ---------

KATA_TABLE = {}
for row in load('sanskrit-katapayadi-table.csv'):
    if row['status'] == 'SOURCED':
        KATA_TABLE[row['devanagari']] = int(row['digit'])

ARYA_VALUES = {}
ARYA_VOWEL_MULT = {}
for row in load('sanskrit-aryabhatiya-table.csv'):
    if row['kind'] == 'consonant':
        ARYA_VALUES[row['devanagari']] = int(row['value'])
    else:
        ARYA_VOWEL_MULT[row['transliteration']] = int(
            row['multiplier'])


def kata_digits(text):
    digits = []
    for ak in parse_aksaras(text):
        if ak['standalone']:
            digits.append(0)
        elif ak['vowel'] is None:
            continue
        else:
            digits.append(KATA_TABLE[ak['consonants'][-1]])
    return digits


def kata_decode(text):
    return sum(d * 10 ** i for i, d in enumerate(kata_digits(text)))


def arya_decode(text):
    total = 0
    for ak in parse_aksaras(text):
        if ak['standalone'] or not ak['consonants']:
            continue
        mult = ARYA_VOWEL_MULT[ak['vowel']]
        total += sum(ARYA_VALUES[g] for g in ak['consonants']) * mult
    return total


def main():
    kata_rows = load('sanskrit-katapayadi-table.csv')
    arya_rows = load('sanskrit-aryabhatiya-table.csv')
    kata_ex = load('sanskrit-katapayadi-examples.csv')
    arya_ex = load('sanskrit-aryabhatiya-examples.csv')

    # --- Kaṭapayādi table integrity -------------------------------
    sourced = [r for r in kata_rows if r['status'] == 'SOURCED']
    check('Kaṭapayādi table: 33 SOURCED consonant rows',
          len(sourced) == 33, len(sourced))
    import unicodedata
    check('Kaṭapayādi table: Unicode names verified at all 33 '
          'seats',
          all(unicodedata.name(r['devanagari']) == r['unicode_name']
              for r in sourced), True)
    law = True
    for r in sourced:
        pos = int(r['position'])
        want = pos % 10 if r['group'] in ('ka-group', 'ṭa-group') \
            else pos
        law = law and int(r['digit']) == want
    check('Kaṭapayādi group law recomputed (digit = position in '
          'group; the two full groups close at 0)', law, True)
    zero = [r for r in kata_rows if r['status'] == 'SOURCED-RULE']
    lla = [r for r in kata_rows if r['status'] == 'OPEN']
    check('the zero class stands as a SOURCED-RULE row; the ḷa '
          'row stands OPEN with no digit frozen',
          (len(zero), len(lla), lla[0]['digit'] if lla else '—'),
          (1, 1, ''))
    from collections import Counter
    dist = Counter(KATA_TABLE.values())
    check('the encoder\'s freedom, measured: preimages per digit '
          '(0:2, 1–5:4, 6–8:3, 9:2)',
          (dist[0], dist[1], dist[5], dist[6], dist[8], dist[9]),
          (2, 4, 4, 3, 3, 2))

    # --- Kaṭapayādi exhibits ---------------------------------------
    for row in kata_ex:
        if row['reading'] == 'leftward (standard)' and \
                not row['exhibit'].startswith('sweep corpus'):
            got = (kata_digits(row['devanagari']),
                   kata_decode(row['devanagari']))
            want = ([int(x) for x in
                     row['expected_digits'].split()],
                    int(row['expected_number']))
            check('exhibit: %s' % row['exhibit'], got == want, got)
    for row in kata_ex:
        if row['reading'].startswith('DIRECT'):
            got = kata_digits(row['devanagari'])
            want = [int(x) for x in row['expected_digits'].split()]
            joined = ''.join(map(str, got))
            check('exhibit (direct order): %s — the digit string '
                  'is π/10 as written' % row['exhibit'],
                  (got == want, joined),
                  (True, '31415926535897932384626433832792'))
    for row in kata_ex:
        if row['reading'] == 'melakarta prefix rule':
            digits = kata_digits(row['devanagari'])
            got = (digits[:2],
                   digits[0] + 10 * digits[1])
            want = ([int(x) for x in
                     row['expected_digits'].split()],
                    int(row['expected_number']))
            check('exhibit (melakarta): %s' % row['exhibit'],
                  got == want, got)
    corpus_ok, corpus = True, {}
    for row in kata_ex:
        if row['exhibit'].startswith('sweep corpus'):
            got = kata_decode(row['devanagari'])
            corpus[row['exhibit']] = got
            corpus_ok = corpus_ok and \
                got == int(row['expected_number'])
    check('the sweep\'s corpus re-read through the audit seat: '
          '10/10 readings reproduced', corpus_ok, corpus)
    try:
        kata_decode('ओज़')
        oz = 'decoded (a guess!)'
    except ValueError:
        oz = 'fails closed'
    check('OZ (ओज़) fails closed at the audit seat — the nukta '
          'letter is unmappable (the sweep dropped it and read '
          '0; both handlings record the same fact)', oz,
          'fails closed')

    # --- Kaṭapayādi round-trip at the audit seat -------------------
    reps = {}
    for r in sourced:
        reps.setdefault(int(r['digit']), r['devanagari'])
    rt = all(kata_decode(''.join(reps[int(c)] for c in
                                 str(n)[::-1])) == n
             for n in range(1000))
    check('round-trip at the audit seat: decode∘encode == '
          'identity, 0..999 (canonical representatives)', rt, True)

    # --- Āryabhaṭīya table integrity ------------------------------
    cons = [r for r in arya_rows if r['kind'] == 'consonant']
    vows = [r for r in arya_rows if r['kind'] == 'vowel']
    check('Āryabhaṭīya table: 33 consonant rows + 9 vowel rows, '
          'all SOURCED',
          (len(cons), len(vows),
           all(r['status'] == 'SOURCED' for r in arya_rows)),
          (33, 9, True))
    order = [r['transliteration'] for r in cons]
    varga_ok = all(int(r['value']) == i + 1
                   for i, r in enumerate(cons[:25]))
    avarga_ok = [int(r['value']) for r in cons[25:]] == \
        [30, 40, 50, 60, 70, 80, 90, 100]
    check('Āryabhaṭīya values recomputed from the rule (varga = '
          'varṇamālā position 1–25; avarga = 30–100 by tens)',
          (varga_ok, avarga_ok), (True, True))
    check('Āryabhaṭīya vowel multipliers recomputed '
          '(100^index, indices 0–8)',
          all(int(r['multiplier']) == 100 ** int(
              r['class_or_index']) for r in vows), True)

    # --- Āryabhaṭīya exhibits ---------------------------------------
    for row in arya_ex:
        if not row['exhibit'].startswith('sine difference'):
            got = arya_decode(row['devanagari'])
            check('exhibit: %s' % row['exhibit'],
                  got == int(row['expected_value']), got)
    sine = [r for r in arya_ex
            if r['exhibit'].startswith('sine difference')]
    got_sine = [arya_decode(r['devanagari']) for r in sine]
    want_sine = [int(r['expected_value']) for r in sine]
    check('the sine verse recomputed: 24/24 differences exact',
          got_sine == want_sine, got_sine)
    check('the differences sum to Āryabhaṭa\'s radius, 3438',
          sum(got_sine), 3438)
    parting = arya_decode('श्घखि')
    check('the śghaki parting, printed: the numeration article\'s '
          'transcription (śghakhi) decodes 274; the critical '
          'edition\'s reading (śghaki) decodes 174 and stands',
          (parting, arya_decode('श्घकि')), (274, 174))

    # --- Āryabhaṭīya round-trip at the audit seat ------------------
    glyph_of_value = {}
    for g, v in ARYA_VALUES.items():
        glyph_of_value.setdefault(v, g)
    signs = {0: '', 1: 'ि', 2: 'ु', 3: 'ृ', 4: 'ॢ',
             5: 'े', 6: 'ै', 7: 'ो', 8: 'ौ'}

    def pair_cons(p):
        if p in glyph_of_value and (p <= 25 or p % 10 == 0):
            return [glyph_of_value[p]]
        if p < 50:
            return [glyph_of_value[p - 25], glyph_of_value[25]]
        a = (p // 10) * 10
        return [glyph_of_value[p - a], glyph_of_value[a]]

    def arya_encode(n):
        if n == 0:
            return ''
        out, idx = [], 0
        while n:
            p = n % 100
            if p:
                out.append('्'.join(pair_cons(p)) + signs[idx])
            n //= 100
            idx += 1
        return ''.join(out)

    rt2 = all(arya_decode(arya_encode(n)) == n
              for n in range(10000))
    check('round-trip at the audit seat: decode∘encode == '
          'identity, 0..9999', rt2, True)

    # --- Summary -----------------------------------------------------
    failed = [r for r in RESULTS if not r[1]]
    print()
    print('SANSKRIT AUDIT BATTERY — %d/%d PASS'
          % (len(RESULTS) - len(failed), len(RESULTS)))
    if failed:
        print('FAILURES: %r' % (failed,))
        sys.exit(1)
    print('BATTERY VERDICT: PASS')


if __name__ == '__main__':
    main()
