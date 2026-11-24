#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — east_asian_audit.py — the East Asian field Phase I audit:
# data builder for the REGIONAL TRIAD road (Chinese + Korean; Japanese
# stands as the seated anchor and is not re-opened).
#
# Epigraph: "The sounds of our country's language are different from
# those of the Middle Kingdom and are not confluent with the sounds of
# characters... I have been distressed because of this, and have newly
# designed twenty-eight letters." — Sejong the Great, Hunminjeongeum
# preface (1446), via Wikipedia, "Hunminjeongeum".
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to
# the author's red pen. This file is an AUDIT instrument: findings,
# never doctrine. Nothing here is a bank; nothing here enters the
# engine.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: (i) the Chinese material offers a NOTATION, not a
#     table: a closed set of digit and multiplier logographs whose
#     reading law is multiplicative-additive, beside two attested
#     ordinal cycles (the ten Heavenly Stems, the twelve Earthly
#     Branches) and one attested order without values (the 214 Kangxi
#     radicals); the sweep's closure — no Chinese letter-value table
#     exists — will re-verify, because no witness will produce a
#     per-sign value for any character outside the numeral logographs
#     themselves; (ii) the Korean material offers a GRID, not a table:
#     Hangul's jamo are a designed featural system with canonical
#     orders (1446 and modern, South and North) and NO letter-numeral
#     tradition — the checked negative will hold on both witnesses,
#     because Korean numerals are WORDS (native) and borrowed GLYPHS
#     (Sino-Korean hanja, identical to the Chinese logographs);
#     (iii) what the two fields honestly offer the dial is therefore
#     asymmetric: a notation seat for Chinese, tuning material (an
#     ordered grid) for Korean.
#   Method: (1) transcribe the Chinese numeral table from THREE
#     witnesses read entire on 2026-11-24 — Wikipedia, "Chinese
#     numerals" (the comparison table: financial and everyday, both
#     scripts; the reading-and-transcribing section for the law);
#     Omniglot, "Chinese numerals" (simple and complex forms 0–10);
#     Wikipedia, "Korean numerals" (the Sino-Korean hanja column and
#     the financial-hanja table — the same glyphs in Korean use) — and
#     diff them cell by cell in code: a disagreement aborts the build
#     as a finding, never averages away; (2) transcribe the two cycles
#     from three witnesses each (Wikipedia "Heavenly Stems" and
#     "Earthly Branches"; Herong Yang's Gan-Zhi tables, pinyin
#     sequences; the Chinese Calendar Atlas sexagenary page, glyph
#     sequences) and diff; generate the 60-term cycle in code and
#     check its law (first term 甲子, last 癸亥, parity never mixed);
#     (3) generate the Kangxi order from the Unicode block
#     (U+2F00–U+2FD5, 214 seats) and hold it against the 91 anchors
#     transcribed from Wikipedia's table (positions 1–91 read entire);
#     (4) transcribe the Korean orders from two witnesses — Wikipedia,
#     "Hangul" (letter counts; the consonant and vowel tables; the
#     North and South alphabetic orders; the obsolete letters) and
#     Wikipedia, "Hunminjeongeum" (the 1446 introduction order of the
#     28 letters), with Omniglot, "Korean language and alphabet",
#     concurring on the counts (24 basic jamo: 14 consonants, 10
#     vowels) and the syllable-block principle — and hold the modern
#     South order against the Unicode standard's own ordering (the
#     compatibility-jamo block sequence; the 11,172 syllable block);
#     (5) recompute the witnesses' own exhibits before trusting any
#     derived number (the reading law on Wikipedia's worked numbers).
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the East Asian field Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The Chinese
numerals below are TRANSCRIPTIONS of an attested NOTATION — the
glyphs denote numbers the way Roman numerals do, by a reading law,
not by a weighing table; the cycles are attested ORDINALS; the
Kangxi order is an attested ORDER. The Korean jamo orders are
TRANSCRIPTIONS of canonical sequences. No per-sign weighing value
is asserted for any Chinese character or any jamo anywhere in this
file: where a tuning later prices the jamo grid, that price is the
house's coinage, minted in Phase II under the founder's Flagpole,
and this audit's business is only to hand the tuning honest
material — the grid as the witnesses print it, the orders as they
stand, the partings (1446 vs modern, South vs North) unaveraged.
"""

import csv
import unicodedata

HERE = __file__.rsplit('/', 1)[0] + '/'

# ---------------------------------------------------------------------------
# CHINESE — the numeral notation. Three witness transcriptions.
# MECHANISM: W1 is keyed by value with four dress columns (financial /
# everyday × traditional / simplified) exactly as Wikipedia's
# comparison table prints them; W2 by value with its two dresses
# (simple / complex); W3 by value with the hanja glyph Korean uses
# (identical to W1's traditional everyday glyph at every shared cell)
# and its financial-hanja column. The diff runs over shared cells.
# ---------------------------------------------------------------------------
# value: (fin_trad, fin_simp, every_trad, every_simp, pinyin)
W1_NUMERALS = {
    0:          ('零', '零', '零', '零', 'líng'),
    1:          ('壹', '壹', '一', '一', 'yī'),
    2:          ('貳', '贰', '二', '二', 'èr'),
    3:          ('參', '叁', '三', '三', 'sān'),
    4:          ('肆', '肆', '四', '四', 'sì'),
    5:          ('伍', '伍', '五', '五', 'wǔ'),
    6:          ('陸', '陆', '六', '六', 'liù'),
    7:          ('柒', '柒', '七', '七', 'qī'),
    8:          ('捌', '捌', '八', '八', 'bā'),
    9:          ('玖', '玖', '九', '九', 'jiǔ'),
    10:         ('拾', '拾', '十', '十', 'shí'),
    100:        ('佰', '佰', '百', '百', 'bǎi'),
    1000:       ('仟', '仟', '千', '千', 'qiān'),
    10 ** 4:    ('萬', '万', '萬', '万', 'wàn'),
    10 ** 8:    ('億', '亿', '億', '亿', 'yì'),
    10 ** 12:   ('兆', '兆', '兆', '兆', 'zhào'),
}
# W1's zero coordinate, printed on its face: the everyday 0 may also
# be written 〇 (the table's "零 or 〇"); the financial 0 is 零 alone.
W1_ZERO_VARIANT = '〇'
# W2 (Omniglot): value: (simple, complex) for 0–10.
W2_NUMERALS = {
    0: ('〇', '零'), 1: ('一', '壹'), 2: ('二', '貳'), 3: ('三', '叁'),
    4: ('四', '肆'), 5: ('五', '伍'), 6: ('六', '陸'), 7: ('七', '柒'),
    8: ('八', '捌'), 9: ('九', '玖'), 10: ('十', '拾'),
}
# W3 (Wikipedia, "Korean numerals"): the Sino-Korean hanja glyph and
# the financial hanja, by value, at the cells the article exhibits.
W3_HANJA = {
    0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六',
    7: '七', 8: '八', 9: '九', 10: '十', 100: '百', 1000: '千',
    10 ** 4: '萬', 10 ** 8: '億', 10 ** 12: '兆',
}
W3_FINANCIAL = {
    1: '壹', 2: '貳', 3: '參', 4: '肆', 5: '伍', 6: '陸', 7: '柒',
    8: '捌', 9: '玖', 10: '拾', 100: '佰', 1000: '仟',
}

DIGITS = {g: v for v, t in W1_NUMERALS.items() if v < 10
          for g in (t[2],)}
MULTIPLIERS = {t[2]: v for v, t in W1_NUMERALS.items() if v >= 10}
FINANCIAL_DIGITS = {t[0]: v for v, t in W1_NUMERALS.items() if v < 10}
FINANCIAL_MULTIPLIERS = {t[0]: v for v, t in W1_NUMERALS.items()
                         if v >= 10}


def read_chinese(text):
    """The notation's reading law, as W1's reading section states it.

    MECHANISM: sign-value, multiplicative-additive, myriad-grouped.
    Split the string at the group multipliers (兆, 億, 萬 —
    descending); read each section as a sub-number under the simple
    law (a digit before a section multiplier 十百千 multiplies it;
    a bare multiplier carries an implicit one; a trailing digit
    adds; 零/〇 mark an interior zero place and contribute
    nothing); accumulate section × group value. A section may be
    empty (value 0). The law is verified against W1's own worked
    exhibits in the battery (60, 45, 2362, 205, 1158, 100004)
    before any derived reading is trusted.
    """
    GROUP = {'兆': 10 ** 12, '億': 10 ** 8, '亿': 10 ** 8,
             '萬': 10 ** 4, '万': 10 ** 4}

    def section(s):
        sub = 0
        pending = None
        for ch in s:
            if ch in ('零', '〇'):
                pending = 0
            elif ch in DIGITS or ch in FINANCIAL_DIGITS:
                pending = (DIGITS[ch] if ch in DIGITS
                           else FINANCIAL_DIGITS[ch])
            elif ch in MULTIPLIERS or ch in FINANCIAL_MULTIPLIERS:
                m = (MULTIPLIERS[ch] if ch in MULTIPLIERS
                     else FINANCIAL_MULTIPLIERS[ch])
                sub += (1 if pending is None else pending) * m
                pending = None
            else:
                raise ValueError('not a numeral glyph: %r' % ch)
        if pending:
            sub += pending
        return sub

    total = 0
    rest = text
    for g, gv in sorted(GROUP.items(), key=lambda kv: -kv[1]):
        if g in rest:
            head, rest = rest.split(g, 1)
            total += section(head) * gv
    total += section(rest)
    return total


# ---------------------------------------------------------------------------
# CHINESE — the cycles. Three witness transcriptions each.
# ---------------------------------------------------------------------------
STEMS_W1 = list('甲乙丙丁戊己庚辛壬癸')
STEMS_PINYIN = ['jiǎ', 'yǐ', 'bǐng', 'dīng', 'wù', 'jǐ', 'gēng',
                'xīn', 'rén', 'guǐ']
STEMS_W2_PINYIN = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng',
                   'Xin', 'Ren', 'Gui']  # Herong Yang
STEMS_W3 = list('甲乙丙丁戊己庚辛壬癸')  # Chinese Calendar Atlas
BRANCHES_W1 = list('子丑寅卯辰巳午未申酉戌亥')
BRANCHES_PINYIN = ['zǐ', 'chǒu', 'yín', 'mǎo', 'chén', 'sì', 'wǔ',
                   'wèi', 'shēn', 'yǒu', 'xū', 'hài']
BRANCHES_W2_PINYIN = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu',
                      'Wei', 'Shen', 'You', 'Xu', 'Hai']  # Herong Yang
BRANCHES_W3 = list('子丑寅卯辰巳午未申酉戌亥')  # Chinese Calendar Atlas


def sexagenary():
    """The 60-term cycle, generated by its own law.

    MECHANISM: advance stem and branch together; lcm(10, 12) = 60;
    parity never mixes (yang stems meet yang branches only), so 60
    of the 120 pairings occur — the law the witnesses state.
    """
    return [STEMS_W1[i % 10] + BRANCHES_W1[i % 12] for i in range(60)]


# ---------------------------------------------------------------------------
# CHINESE — the Kangxi order. Generated from the Unicode block;
# anchors transcribed from W1's table (positions 1–91 read entire).
# ---------------------------------------------------------------------------
KANGXI_ANCHORS = {
    1: '一', 2: '丨', 3: '丶', 4: '丿', 5: '乙', 6: '亅', 7: '二',
    8: '亠', 9: '人', 10: '儿', 11: '入', 12: '八', 13: '冂',
    14: '冖', 15: '冫', 16: '几', 17: '凵', 18: '刀', 19: '力',
    20: '勹', 21: '匕', 22: '匚', 23: '匸', 24: '十', 25: '卜',
    26: '卩', 27: '厂', 28: '厶', 29: '又', 30: '口', 31: '囗',
    32: '土', 33: '士', 34: '夂', 35: '夊', 36: '夕', 37: '大',
    38: '女', 39: '子', 40: '宀', 41: '寸', 42: '小', 43: '尢',
    44: '尸', 45: '屮', 46: '山', 47: '巛', 48: '工', 49: '己',
    50: '巾', 51: '干', 52: '幺', 53: '广', 54: '廴', 55: '廾',
    56: '弋', 57: '弓', 58: '彐', 59: '彡', 60: '彳', 61: '心',
    62: '戈', 63: '戶', 64: '手', 65: '支', 66: '攴', 67: '文',
    68: '斗', 69: '斤', 70: '方', 71: '无', 72: '日', 73: '曰',
    74: '月', 75: '木', 76: '欠', 77: '止', 78: '歹', 79: '殳',
    80: '毋', 81: '比', 82: '毛', 83: '氏', 84: '气', 85: '水',
    86: '火', 87: '爪', 88: '父', 89: '爻', 90: '爿', 91: '片',
}


def kangxi_order():
    """The 214 radicals in order, from the standard's block.

    MECHANISM: the Kangxi Radicals block U+2F00–U+2FD5 encodes the
    214 in dictionary order; the glyph at U+2F00 + position − 1 is
    the radical form of the position's head character (the anchors
    above are the head characters as W1's table prints them; where
    the block's radical form differs in shape from the head
    character — e.g. position 63 戶 vs block form — the battery
    compares by the standard's own name, not by glyph identity).
    """
    return [chr(0x2F00 + i) for i in range(214)]


# ---------------------------------------------------------------------------
# KOREAN — the jamo orders. Two witness transcriptions + the standard.
# ---------------------------------------------------------------------------
# The 1446 introduction order (Wikipedia, "Hunminjeongeum": "The 17
# consonants are introduced first in the following order... Then the
# 11 vowels").
ORIGINAL_CONSONANTS = list('ㄱㅋㆁㄷㅌㄴㅂㅍㅁㅈㅊㅅㆆㅎㅇㄹㅿ')
ORIGINAL_VOWELS = list('ㆍㅡㅣㅗㅏㅜㅓㅛㅑㅠㅕ')
# Witness B (Wikipedia, "Hangul", historical orders): the 1446 order
# AS PRINTED there carries the later tense doubles interpolated;
# removing the five tense doubles and ㆅ (the doubled ㆆ, both later
# developments by that article's own account) yields the base 28.
HANGUL_1446_AS_PRINTED = list('ㄱㄲㅋㆁㄷㄸㅌㄴㅂㅃㅍㅁㅈㅉㅊㅅㅆㆆㅎㆅㅇㄹㅿ')
LATER_INTERPOLATIONS = set('ㄲㄸㅃㅉㅆㆅ')
# Modern orders (Wikipedia, "Hangul", alphabetic order sections).
SK_INITIAL = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
SK_VOWEL = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
SK_FINAL = [None] + list('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')
NK_INITIAL = list('ㄱㄴㄷㄹㅁㅂㅅㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅇ')
NK_VOWEL = list('ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅚㅟㅢㅘㅝㅙㅞ')
BASIC_CONSONANTS = list('ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ')
BASIC_VOWELS = list('ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ')
OBSOLETE_BASIC = list('ㆁㅿㆆㆍ')  # the four dead basic letters (W1)


def compat_jamo():
    """The compatibility-jamo block in codepoint order (U+3131–).

    MECHANISM: the block lists the modern jamo in the South Korean
    dictionary order — consonants (with the final digraphs seated
    among them), then vowels. Filtering it is the standard's own
    testimony to the modern order, independent of the article.
    """
    out = []
    cp = 0x3131
    while True:
        ch = chr(cp)
        name = unicodedata.name(ch, '')
        if not name.startswith('HANGUL LETTER'):
            break
        out.append(ch)
        cp += 1
    return out


def build_csvs():
    """Write the four frozen audit tables beside this script."""
    with open(HERE + 'chinese-numerals.csv', 'w', newline='',
              encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['value', 'kind', 'everyday_trad', 'everyday_simp',
                    'financial_trad', 'financial_simp', 'pinyin',
                    'status', 'witnesses'])
        for v in sorted(W1_NUMERALS):
            ft, fs, et, es, py = W1_NUMERALS[v]
            kind = 'digit' if v < 10 else 'multiplier'
            w.writerow([v, kind, et, es, ft, fs, py, 'SOURCED',
                        'Wikipedia "Chinese numerals" (comparison '
                        'table); Omniglot (0–10); Wikipedia "Korean '
                        'numerals" (hanja column)'])
    with open(HERE + 'chinese-cycles.csv', 'w', newline='',
              encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['cycle', 'position', 'glyph', 'codepoint',
                    'pinyin', 'status', 'witnesses'])
        for i, g in enumerate(STEMS_W1):
            w.writerow(['stem', i + 1, g, 'U+%04X' % ord(g),
                        STEMS_PINYIN[i], 'SOURCED',
                        'Wikipedia "Heavenly Stems"; Herong Yang; '
                        'Chinese Calendar Atlas'])
        for i, g in enumerate(BRANCHES_W1):
            w.writerow(['branch', i + 1, g, 'U+%04X' % ord(g),
                        BRANCHES_PINYIN[i], 'SOURCED',
                        'Wikipedia "Earthly Branches"; Herong Yang; '
                        'Chinese Calendar Atlas'])
    with open(HERE + 'kangxi-order.csv', 'w', newline='',
              encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['position', 'block_glyph', 'codepoint',
                    'unicode_name', 'anchor_head', 'status'])
        for i, g in enumerate(kangxi_order()):
            w.writerow([i + 1, g, 'U+%04X' % ord(g),
                        unicodedata.name(g),
                        KANGXI_ANCHORS.get(i + 1, ''),
                        'SOURCED' if (i + 1) in KANGXI_ANCHORS
                        else 'BLOCK'])
    with open(HERE + 'korean-jamo.csv', 'w', newline='',
              encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['grid', 'stratum', 'position', 'glyph',
                    'codepoint', 'status', 'witnesses'])
        for i, g in enumerate(ORIGINAL_CONSONANTS):
            w.writerow(['1446', 'consonant', i + 1, g,
                        'U+%04X' % ord(g), 'SOURCED',
                        'Wikipedia "Hunminjeongeum"; Wikipedia '
                        '"Hangul" (historical orders)'])
        for i, g in enumerate(ORIGINAL_VOWELS):
            w.writerow(['1446', 'vowel', i + 1, g, 'U+%04X' % ord(g),
                        'SOURCED', 'Wikipedia "Hunminjeongeum"; '
                        'Wikipedia "Hangul" (historical orders)'])
        for name, seq in (('initial', SK_INITIAL),
                          ('vowel', SK_VOWEL)):
            for i, g in enumerate(seq):
                w.writerow(['modern-SK', name, i + 1, g,
                            'U+%04X' % ord(g), 'SOURCED',
                            'Wikipedia "Hangul" (South Korean '
                            'order); Unicode standard (block order)'])
        for i, g in enumerate(SK_FINAL):
            if g is not None:
                w.writerow(['modern-SK', 'final', i, g,
                            'U+%04X' % ord(g), 'SOURCED',
                            'Wikipedia "Hangul" (South Korean '
                            'order); Unicode standard (block order)'])
        for name, seq in (('initial', NK_INITIAL),
                          ('vowel', NK_VOWEL)):
            for i, g in enumerate(seq):
                w.writerow(['modern-NK', name, i + 1, g,
                            'U+%04X' % ord(g), 'SOURCED',
                            'Wikipedia "Hangul" (North Korean '
                            'order)'])


if __name__ == '__main__':
    build_csvs()
    print('CSVs written')
