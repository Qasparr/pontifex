#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — chinese.py — THE CHINESE NOTATION SEAT: a reader for the
# attested logographic numeral notation. NOT a weighing bank.
#
# Epigraph: "Chinese numerals are words and phrases used to denote
# numbers... The writing of Chinese numerals was one of the three
# earliest developments of Chinese civilization." — Wikipedia,
# "Chinese numerals" (read entire, 2026-11-24).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to the
# author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis (the Phase I audit's gate, THE-EAST-ASIAN-FIELD-
#     PHASE-I-AUDIT.md §IX): the Chinese field offers a NOTATION,
#     not a table — a closed set of digit and multiplier logographs
#     whose glyphs DENOTE numbers under a reading law, the same
#     species as the Imperial Aramaic number signs the Aramaic
#     seat counted and did not seat as letters. A reader door is
#     therefore the honest seat: it parses the notation and
#     returns the number; it must never register as a weigh()
#     system, because no Chinese weighing table exists (the
#     closure re-verified by the audit, battery 12/12).
#   Method: the sign set and the law are the audit's, transcribed
#     from three witnesses (Wikipedia, "Chinese numerals";
#     Omniglot; Wikipedia, "Korean numerals") and frozen in
#     research/twelve-tongues/chinese-numerals.csv; the law is
#     verified against the witnesses' own worked exhibits in
#     chinese_checks() below, and parity against the frozen CSV
#     is proven by test_chinese_parity.py at the repository root.
#   Observation: recorded in the audit document and the triad
#     instrument (THE-REGIONAL-TRIAD-DIAL.md).
#   Result: a reader, fenced as a reader.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Read Chinese numerals in the attested notation.

DOCTRINE — WHAT THIS SEAT IS AND IS NOT: this module READS the
logographic decimal notation — the glyphs 一 through 兆 and their
financial dress — and returns the number the notation denotes.
It is not a gematria bank: the glyphs are not letters with values,
they are digits and multipliers in a sign-value notation, and no
weigh() system is registered here. A text that is not a numeral
is refused with an error, never silently misread — a reader that
guesses is a forger.

THE TWO DRESSES (the Aramaic shape): the everyday dress （一二三
四五六七八九十百千萬億兆） and the financial dress （壹貳參肆伍陸
柒捌玖拾佰仟萬億兆）, the anti-fraud stratum of Wu Zetian's decree
and the Hongwu case, carry ONE value sequence — the dresses are
interchangeable in a reading and the reader accepts both, plus
the simplified forms （万亿， and the financial 贰叁陆） and the zero
variant 〇. What parted in the audit is printed on the seat: at
the zero the dresses' primaries part (everyday 零 with 〇 as its
variant; financial 零 alone), and Omniglot's complex 3 （叁） is
the simplified financial form where its fellows are traditional.

NOT SEATED: the Suzhou numerals （花碼）, a positional cipher of
the Song era — a separate notation species, named in the audit,
awaiting its own audit if ever wanted. The Heavenly Stems and
Earthly Branches are attested ORDINALS, not this notation; they
stand in the audit's frozen table and are not read here.
"""

# MECHANISM: the sign set, by role. Digits denote 1–9 in any
# dress; section multipliers （十百千 and financial 拾佰仟） scale a
# digit inside a myriad section; group multipliers （萬億兆 and
# simplified 万亿） close a section and scale it. 零 and 〇 are the
# zero: a place marker inside a section, the number itself alone.
_DIGITS = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7,
    '八': 8, '九': 9,
    '壹': 1, '貳': 2, '參': 3, '肆': 4, '伍': 5, '陸': 6, '柒': 7,
    '捌': 8, '玖': 9,
    '贰': 2, '叁': 3, '陆': 6,  # the simplified financial forms
}
_SECTION_MULTIPLIERS = {
    '十': 10, '百': 100, '千': 1000,
    '拾': 10, '佰': 100, '仟': 1000,
}
_GROUP_MULTIPLIERS = {
    '萬': 10 ** 4, '万': 10 ** 4,
    '億': 10 ** 8, '亿': 10 ** 8,
    '兆': 10 ** 12,
}
_ZERO_GLYPHS = ('零', '〇')
_SIGNS = (set(_DIGITS) | set(_SECTION_MULTIPLIERS)
          | set(_GROUP_MULTIPLIERS) | set(_ZERO_GLYPHS))


def _read_section(section):
    """One myriad section under the simple law.

    MECHANISM: a digit before a section multiplier multiplies it;
    a bare multiplier carries an implicit one （十 = 10, 十五 =
    15); a trailing digit adds; a zero glyph marks an empty place
    and contributes nothing (its presence is the notation's own
    — 二百零五 writes the empty tens place, it does not add)."""
    subtotal = 0
    pending = None
    for ch in section:
        if ch in _ZERO_GLYPHS:
            pending = 0
        elif ch in _DIGITS:
            pending = _DIGITS[ch]
        elif ch in _SECTION_MULTIPLIERS:
            subtotal += (1 if pending is None else pending) \
                * _SECTION_MULTIPLIERS[ch]
            pending = None
        else:
            raise ValueError('not a numeral glyph: %r' % ch)
    if pending:
        subtotal += pending
    return subtotal


def read_chinese_numerals(text):
    """Read a Chinese numeral in the attested notation.

    MECHANISM: split the text at the group multipliers,
    descending （兆， then 億， then 萬） — each head is a section
    read under the simple law and scaled by its group; the tail
    is the units section. Returns a result dict: the text as
    given, the number, the per-sign breakdown (glyph and role),
    and 'dress' — the dresses the reading actually wore
    ('everyday', 'financial', or 'mixed'), so a reading's dress
    is auditable, never assumed. A glyph outside the sign set
    raises ValueError: the reader refuses what it cannot read.

    DOCTRINE: the result is a READING, not a weighing — it
    carries no provenance tier because it asserts no table; the
    notation is attested and the law is the witnesses' own,
    verified on their exhibits in chinese_checks().
    """
    for ch in text:
        if ch not in _SIGNS:
            raise ValueError('not a numeral glyph: %r' % ch)
    breakdown = []
    for ch in text:
        if ch in _ZERO_GLYPHS:
            role = 'zero'
        elif ch in _GROUP_MULTIPLIERS:
            role = 'group_multiplier'
        elif ch in _SECTION_MULTIPLIERS:
            role = 'section_multiplier'
        else:
            role = 'digit'
        breakdown.append((ch, role))
    financial = any(ch in '壹貳參肆伍陸柒捌玖拾佰仟贰叁陆'
                    for ch in text)
    everyday = any(ch in '一二三四五六七八九十百千' for ch in text)
    dress = ('mixed' if financial and everyday
             else 'financial' if financial else 'everyday')
    total = 0
    rest = text
    for glyph, group_value in sorted(_GROUP_MULTIPLIERS.items(),
                                     key=lambda kv: -kv[1]):
        if glyph in rest:
            head, rest = rest.split(glyph, 1)
            total += _read_section(head) * group_value
    total += _read_section(rest)
    return {
        'text': text,
        'value': total,
        'breakdown': breakdown,
        'dress': dress,
        'notation': 'chinese_numerals',
    }


def chinese_checks():
    """Verify the notation seat against the witnesses' exhibits.

    MECHANISM: the audit's worked numbers recomputed (Wikipedia's
    reading exhibits, both dresses), the dress equivalence (one
    value sequence under two dresses — the face-law's local
    instance), the zero's two glyphs, and the refusal: a
    non-numeral text raises, it does not misread. Parity against
    the frozen CSV is proven separately by
    test_chinese_parity.py.
    """
    checks = []
    exhibits = {'六十': 60, '四十五': 45, '二千三百六十二': 2362,
                '二百零五': 205, '一千一百五十八': 1158,
                '十萬零四': 100004, '一百一十四': 114}
    bad = [(t, read_chinese_numerals(t)['value'], n)
           for t, n in exhibits.items()
           if read_chinese_numerals(t)['value'] != n]
    checks.append(("the witnesses' exhibits recompute (60, 45, "
                   '2362, 205, 1158, 100004, 114)',
                   not bad, bad or '7/7 exact'))
    fin = read_chinese_numerals('壹佰壹拾肆')
    checks.append(('the financial dress reads the same sequence: '
                   '壹佰壹拾肆 == 114, dress financial; 貳拾 == 20',
                   fin['value'] == 114
                   and fin['dress'] == 'financial'
                   and read_chinese_numerals('貳拾')['value'] == 20,
                   (fin['value'], fin['dress'])))
    checks.append(('the zero\'s two glyphs read one place: '
                   '二百〇五 == 二百零五 == 205; 零 alone == 0',
                   read_chinese_numerals('二百〇五')['value'] == 205
                   and read_chinese_numerals('零')['value'] == 0,
                   read_chinese_numerals('二百〇五')['value']))
    checks.append(('the myriad scale: 一億二千三百四十五萬六千七百'
                   '八十九 == 123456789',
                   read_chinese_numerals(
                       '一億二千三百四十五萬六千七百八十九')['value']
                   == 123456789,
                   read_chinese_numerals(
                       '一億二千三百四十五萬六千七百八十九')['value']))
    refused = False
    try:
        read_chinese_numerals('猫')
    except ValueError:
        refused = True
    checks.append(('the refusal: a non-numeral glyph raises '
                   'ValueError — the reader never misreads',
                   refused, refused))
    return checks

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
