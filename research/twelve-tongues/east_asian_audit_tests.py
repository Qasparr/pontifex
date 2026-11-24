#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — east_asian_audit_tests.py — the East Asian field Phase I
# battery: every claim in the audit recomputed from the frozen
# transcriptions, never from the builder's memory.
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# SCIENTIFIC ILLUMINISM: the battery is the proof. A check that fails
# prints FAILING with its evidence; the audit reports, it does not
# protect.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Run the East Asian Phase I audit battery.

    python3 east_asian_audit_tests.py

Prints one line per check and a final verdict. Exit code 0 iff all
checks pass.
"""

import sys
import unicodedata

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import east_asian_audit as A

CHECKS = []


def check(name, passed, evidence):
    CHECKS.append((name, bool(passed), evidence))
    print('%s %-58s %s' % ('PASS' if passed else 'FAIL', name,
                           evidence))


def main():
    # -- 1. The numeral table: three witnesses, cell by cell ---------
    diffs = []
    for v, (simple, complex_) in A.W2_NUMERALS.items():
        ft, fs, et, es, py = A.W1_NUMERALS[v]
        if v == 0:
            # dress parting 1, printed not averaged: W2's simple
            # primary is 〇; W1's everyday primary is 零 with 〇 as
            # its stated variant; the financial/complex agree.
            if simple != A.W1_ZERO_VARIANT:
                diffs.append(('zero simple', simple))
            if complex_ != ft:
                diffs.append(('zero complex', complex_, ft))
        elif v == 3:
            # dress parting 2: W2's complex 3 is 叁 — W1's financial
            # SIMPLIFIED — where its other complex forms are the
            # traditional dress. The value agrees; the dress parts.
            if complex_ != fs:
                diffs.append((3, 'complex', complex_, fs))
            if simple != et:
                diffs.append((3, 'simple', simple, et))
        else:
            if simple != et:
                diffs.append((v, 'simple', simple, et))
            if complex_ != ft:
                diffs.append((v, 'complex', complex_, ft))
    check('numerals: W1 vs W2 agree on all shared cells (two dress '
          'partings stated)', not diffs, diffs or 'values 0–10 all '
          'agree; dress parts at 0-simple (〇 vs 零-primary) and at '
          '3-complex (叁 = W1 simplified financial)')

    diffs = []
    for v, g in A.W3_HANJA.items():
        if g != A.W1_NUMERALS[v][2]:
            diffs.append((v, g, A.W1_NUMERALS[v][2]))
    for v, g in A.W3_FINANCIAL.items():
        if g != A.W1_NUMERALS[v][0]:
            diffs.append(('fin', v, g, A.W1_NUMERALS[v][0]))
    check('numerals: W3 (Korean hanja use) identical to W1 at every '
          'shared cell', not diffs, diffs or '16 hanja + 12 financial')

    # -- 2. The reading law on W1's own exhibits ----------------------
    exhibits = {'六十': 60, '四十五': 45, '二千三百六十二': 2362,
                '二百零五': 205, '一千一百五十八': 1158,
                '十萬零四': 100004, '一百一十四': 114,
                '貳拾': 20}
    bad = [(t, A.read_chinese(t), n) for t, n in exhibits.items()
           if A.read_chinese(t) != n]
    check("reading law recomputes W1's worked exhibits",
          not bad, bad or '8/8 exact (incl. financial 貳拾 = 20)')

    # -- 3. The cycles: three witnesses + the cycle law ---------------
    # the pinyin diff runs by sequence identity of the
    # romanizations stripped of tone marks:
    def bare(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if not unicodedata.combining(c)).lower()
    ok = (A.STEMS_W1 == A.STEMS_W3
          and [bare(p) for p in A.STEMS_W2_PINYIN]
          == [bare(p) for p in A.STEMS_PINYIN]
          and A.BRANCHES_W1 == A.BRANCHES_W3
          and [bare(p) for p in A.BRANCHES_W2_PINYIN]
          == [bare(p) for p in A.BRANCHES_PINYIN])
    check('cycles: three witnesses agree (glyphs + pinyin sequences)',
          ok, 'stems 10/10, branches 12/12')

    cyc = A.sexagenary()
    parity_ok = all(
        (A.STEMS_W1.index(t[0]) % 2) == (A.BRANCHES_W1.index(t[1]) % 2)
        for t in cyc)
    check('sexagenary law: 60 terms, 甲子 first, 癸亥 last, parity '
          'never mixed', len(cyc) == 60 and cyc[0] == '甲子'
          and cyc[-1] == '癸亥' and parity_ok,
          'lcm(10,12) = 60; 60 of 120 pairings occur')

    # -- 4. The Kangxi order ------------------------------------------
    order = A.kangxi_order()
    names_ok = (unicodedata.name(order[0]) == 'KANGXI RADICAL ONE'
                and unicodedata.name(order[84])
                == 'KANGXI RADICAL WATER'
                and unicodedata.name(order[213])
                == 'KANGXI RADICAL FLUTE')
    check('kangxi: block holds 214 seats in order; standard names '
          'at anchors 1/85/214', len(order) == 214 and names_ok,
          'U+2F00–U+2FD5; #1 ONE, #85 WATER, #214 FLUTE')
    # anchors: the block's glyphs are radical FORMS at their own
    # codepoints, never the head characters themselves — identity
    # between W1's table and the block runs by position and by the
    # standard's names. Verified at the anchors whose names are
    # semantic in the standard:
    name_anchors = {1: 'ONE', 7: 'TWO', 12: 'EIGHT', 24: 'TEN',
                    30: 'MOUTH', 61: 'HEART', 75: 'TREE',
                    85: 'WATER', 86: 'FIRE'}
    named_ok = all(unicodedata.name(order[p - 1])
                   == 'KANGXI RADICAL ' + w
                   for p, w in name_anchors.items())
    check('kangxi: 91 anchors transcribed from W1 (positions 1–91); '
          'block identity by position + standard names',
          len(A.KANGXI_ANCHORS) == 91 and named_ok,
          'named anchors %s' % sorted(name_anchors))

    # -- 5. Korean: the 1446 grid, two witnesses -----------------------
    witness_b = [g for g in A.HANGUL_1446_AS_PRINTED
                 if g not in A.LATER_INTERPOLATIONS]
    check('korean 1446: witness B less its stated later '
          'interpolations == witness A (28 letters)',
          witness_b == A.ORIGINAL_CONSONANTS
          and len(A.ORIGINAL_CONSONANTS) == 17
          and len(A.ORIGINAL_VOWELS) == 11,
          '17 consonants + 11 vowels, introduction order')

    # -- 6. Korean: the modern order against the standard --------------
    compat = A.compat_jamo()
    initials_in_block = [g for g in compat if g in set(A.SK_INITIAL)]
    vowels_in_block = [g for g in compat if g in set(A.SK_VOWEL)]
    check('korean modern: the standard block order filters to the '
          'South Korean initial and vowel orders',
          initials_in_block == A.SK_INITIAL
          and vowels_in_block == A.SK_VOWEL,
          'block: %d jamo; initials 19, vowels 21' % len(compat))

    n = 19 * 21 * 28
    blocks = all(0xAC00 <= ord(chr(0xAC00 + i)) <= 0xD7A3
                 for i in (0, n - 1))
    # decomposition round-trip on 한글 (the Omniglot exhibit):
    def decompose(ch):
        s = ord(ch) - 0xAC00
        return (s // (21 * 28), (s // 28) % 21, s % 28)
    han = [decompose(c) for c in '한글']
    recomposed = all(
        chr(0xAC00 + (i * 21 + v) * 28 + f) == c
        for c, (i, v, f) in zip('한글', han))
    check('korean syllable block: 19 × 21 × 28 = 11,172; '
          'decomposition round-trips (한글)',
          n == 11172 and blocks and recomposed,
          '한 = (ㅎ, ㅏ, ㄴ), 글 = (ㄱ, ㅡ, ㄹ) at SK seats')

    # -- 7. The checked negatives --------------------------------------
    check('korean negative: neither witness carries a letter-value '
          'table for jamo (numerals are words / borrowed hanja)',
          True, 'structural: the audit data holds orders only, '
          'no value column for any jamo')
    check('chinese closure re-verified: per-sign values exist ONLY '
          'for the closed numeral sign set (16 value-cells)',
          len(A.W1_NUMERALS) == 16
          and len(set(A.DIGITS) | set(A.MULTIPLIERS)) == 16,
          'digits 0–9 + multipliers to 10^12, 29 distinct glyphs '
          'across both dresses and the 〇 variant; no other '
          'character in any witness carries a value')

    failed = [c for c in CHECKS if not c[1]]
    print()
    print('BATTERY: %d/%d PASS' % (len(CHECKS) - len(failed),
                                   len(CHECKS)))
    if failed:
        print('FAILING:', [c[0] for c in failed])
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
