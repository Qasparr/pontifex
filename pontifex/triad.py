#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — triad.py — THE REGIONAL TRIAD DIAL: one face, three
# tongues, a zero at the core.
#
# Epigraph: "The 3 together is the key to all the languages tuned
# like the sundial." — the founder, 2026-11-24 (the Codex Legend
# theory, spoken over the Phoenician map and the Roman doubles).
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
#   Hypothesis (the founder's dial spec, 2026-11-24 11:04 EST):
#     a dial can seat the region's three tongues on ONE face —
#     Japanese (the kana mint, the anchor), Korean (the hangul
#     mint), Chinese (the notation) — on the Aramaic face-law
#     (strata on one face, values unmoved between them) and the
#     Roman teeth-law, and can place a ZERO POINT AT THE SAME
#     PLACE for every tongue: not a value (the attested dials
#     mostly have no zero) but a POSITION — the shared core seat,
#     under the founder's definition 0 = {0, 2, 1−1=0}.
#   Method: the dial routes each character to its stratum by
#     script and reads it there with that stratum's own door —
#     kana() for Japanese, hangul() for Korean, the notation
#     reader for Chinese numerals — and reports the strata
#     SEPARATELY before any sum, so no value ever moves between
#     tongues. The zero is reported per stratum from the strata's
#     own facts, recomputed in triad_checks(): what each tongue
#     does at the core seat.
#   Observation: recorded in THE-REGIONAL-TRIAD-DIAL.md.
#   Result: a house instrument of 2026, fenced CONSTRUCTED.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Read the regional triad on one face.

DOCTRINE — THE FACE AND ITS STRATA: the dial seats three tongues
as three strata of one face, the Aramaic shape. A character is
read by the stratum its script belongs to, at that stratum's own
door, and the strata's subtotals are reported before the sum —
the face-law's discipline: values are never moved, blended, or
averaged between tongues. The strata:

  JAPANESE — the kana mint (ratified house coinage, 2026-11-13),
    read at the kana() door. The dial's anchor: the only seat
    that pre-exists this road.
  KOREAN — the hangul mint (house coinage, 2026-11-24), read at
    the hangul() door, the null law and all. The hist flag
    passes through to this stratum alone (the 1446 annex).
  CHINESE — the notation (ATTESTED), read at the notation
    reader. ITS NUMBERS ARE READINGS, NOT WEIGHTS: a numeral
    run contributes its reading to the report and NOTHING to
    the weight. The Chinese WEIGHING leg stands OPEN — the
    Phase I gate refused all four tuning seams with their
    reasons, and the dial prints the open leg rather than
    forcing it (§V of the audit). Stem and branch glyphs are
    read as CYCLE COORDINATES (their attested ordinals),
    likewise weightless.

DOCTRINE — THE ZERO AT THE CORE: the dial's center seat is the
zero point, placed as a POSITION under the founder's spec and
his definition — 0 = {0, 2, 1−1=0}, "Zero equals Two, and Both
1 and None" (his gloss, 2026-11-15). The seat is one; what each
tongue does there is its own, and the dial prints all three:
Japanese has NO zero sign (the mint prices 1–73; at the core
the Japanese face shows a HOLE — the position present, the
sign absent); Korean has the placeholder ㅇ (a sign whose
initial price is 0 — the position occupied by a zero-priced
sign, counted at the door); Chinese has the zero GLYPH 零/〇 (a
digit of the notation, read 0 — the position occupied by a
sign whose reading is zero). Hole, placeholder, glyph: three
faces of the one seat, none of them a weighing value — which is
what the spec required: the same PLACE, not the same price.
triad_zero() recomputes the three faces from the strata's own
facts; nothing in this paragraph is asserted without them.

BOUNDARY: the dial is a house instrument of 2026. Of its seats,
only the kana mint pre-exists it; the hangul mint was coined on
this road; the Chinese notation is attested but is read here,
not weighed. Nothing in the dial is attested, traditional, or
ancient as an ASSEMBLY, and a cross-stratum sum is the dial's
arithmetic, exhibited as arithmetic — never a bridge claim.
"""

import unicodedata

from .engine import kana, hangul
from .chinese import read_chinese_numerals, _SIGNS as _NUMERAL_SIGNS
from .tables import KANA

# The cycle glyphs and their attested ordinals (Phase I audit,
# frozen in research/twelve-tongues/chinese-cycles.csv; three
# witnesses agree). The dial reads them as coordinates only.
_STEMS = '甲乙丙丁戊己庚辛壬癸'
_BRANCHES = '子丑寅卯辰巳午未申酉戌亥'
_CYCLE = {}
for _i, _g in enumerate(_STEMS):
    _CYCLE[_g] = ('stem', _i + 1)
for _i, _g in enumerate(_BRANCHES):
    _CYCLE[_g] = ('branch', _i + 1)

_KANA_SET = set(KANA) | {'ー'}
_PROVENANCE = (
    'CONSTRUCTED — THE REGIONAL TRIAD DIAL: house instrument '
    'of 2026-11-24 under the founder\'s Flagpole and dial spec. '
    'Strata: Japanese at the kana mint (ratified coinage), '
    'Korean at the hangul mint (coinage of this road), Chinese '
    'at the attested notation (READ, never weighed — its '
    'weighing leg stands OPEN). The zero is a position at the '
    'core seat under the founder\'s definition '
    '0 = {0, 2, 1−1=0}; a cross-stratum sum is the dial\'s '
    'arithmetic, not a bridge claim; NOT attested, '
    'traditional, or ancient as an assembly')


def _is_hangul(ch):
    cp = ord(ch)
    return (0xAC00 <= cp <= 0xD7A3 or 0x1100 <= cp <= 0x11FF
            or 0x3131 <= cp <= 0x318D)


def triad_zero():
    """The dial's zero point, recomputed from the strata's facts.

    MECHANISM: nothing here is asserted — the Japanese face is
    the kana bank's own value set (does any sign price 0?), the
    Korean face is the hangul() door's null law on a vowel-
    initial syllable, the Chinese face is the notation reader
    on the zero glyphs. Returns the founder's definition, his
    gloss, the seat, and the three faces as computed.
    """
    kana_has_zero = 0 in set(KANA.values())
    door = hangul('아')
    return {
        'definition': '0 = {0, 2, 1−1=0}',
        'gloss': 'Zero equals Two, and Both 1 and None.',
        'seat': 'the core seat — one position, shared by every '
                'stratum of the face',
        'tier': 'CONSTRUCTED (the placement); the definition is '
                'the founder\'s (2026-11-15)',
        'faces': {
            'japanese': ('HOLE — no zero sign: the kana mint '
                         'prices %d–%d and no sign prices 0; the '
                         'position is present, the sign absent'
                         % (min(KANA.values()), max(KANA.values()))
                         if not kana_has_zero else
                         'a zero-valued sign exists (unexpected)'),
            'korean': ('PLACEHOLDER — initial ㅇ prices 0 at the '
                       'door (아 reads %d with %d null counted); '
                       'the position is occupied by a zero-priced '
                       'sign' % (door['value'],
                                 door['null_initials'])),
            'chinese': ('GLYPH — 零 and 〇 are digits of the '
                        'notation, read %d; the position is '
                        'occupied by a sign whose reading is zero'
                        % read_chinese_numerals('零')['value']),
        },
    }


def triad_weigh(text, hist=False):
    """Weigh a text on the triad dial.

    MECHANISM: the text is walked character by character and
    routed by script — kana to the Japanese stratum, Hangul
    (syllables, conjoining and compatibility jamo) to the
    Korean stratum, numeral glyphs to the Chinese notation,
    stem/branch glyphs to the cycle coordinates, everything
    else counted as unread. Consecutive characters of one
    stratum are read together at that stratum's own door, so
    each door sees whole words, never fragments. The result
    reports the strata separately — 'strata' subtotals for the
    two weighing strata, 'readings' for the notation's numbers,
    'cycles' for the coordinates — and the 'weight' is the sum
    of the WEIGHING strata only: a reading is never added into
    a weight, and a coordinate carries none.
    """
    runs = []  # (stratum, substring)
    for ch in text:
        if ch in _KANA_SET:
            stratum = 'japanese'
        elif _is_hangul(ch):
            stratum = 'korean'
        elif ch in _NUMERAL_SIGNS:
            stratum = 'chinese_numerals'
        elif ch in _CYCLE:
            stratum = 'cycles'
        else:
            stratum = 'unread'
        if runs and runs[-1][0] == stratum:
            runs[-1][1] += ch
        else:
            runs.append([stratum, ch])
    strata = {'japanese': 0, 'korean': 0}
    readings = []
    cycles = []
    unread = 0
    null_initials = 0
    for stratum, run in runs:
        if stratum == 'japanese':
            strata['japanese'] += kana(run)['value']
        elif stratum == 'korean':
            r = hangul(run, hist=hist)
            strata['korean'] += r['value']
            null_initials += r['null_initials']
        elif stratum == 'chinese_numerals':
            readings.append(read_chinese_numerals(run))
        elif stratum == 'cycles':
            for ch in run:
                kind, ordinal = _CYCLE[ch]
                cycles.append((ch, kind, ordinal))
        else:
            unread += len(run)
    return {
        'text': text,
        'weight': strata['japanese'] + strata['korean'],
        'strata': strata,
        'readings': readings,
        'cycles': cycles,
        'null_initials': null_initials,
        'unread': unread,
        'zero': triad_zero(),
        'provenance': _PROVENANCE,
        'hist_annex': bool(hist),
    }


def triad_checks():
    """Verify the dial against its strata and its spec.

    MECHANISM: the exhibits are recomputed through the strata's
    own doors (never re-priced here): the anchor's bridge in its
    stratum, a mixed string read stratum by stratum, the
    notation's readings kept OUT of the weight, the cycles as
    weightless coordinates, the zero's three faces as computed
    by triad_zero(), and the open Chinese leg proven — a Chinese
    character that is not a numeral is unread, never weighed.
    Parity against all three frozen audit tables is proven
    separately by test_triad_parity.py.
    """
    checks = []
    # 1. The anchor in its stratum: the kana mint's own bridge
    #    reads on the dial unchanged.
    r = triad_weigh('ゆず')
    checks.append(('the anchor stratum: ゆず reads 93 on the '
                   'dial, all of it Japanese stratum',
                   r['weight'] == 93
                   and r['strata'] == {'japanese': 93,
                                       'korean': 0},
                   (r['weight'], r['strata'])))
    # 2. A mixed face: あくま (kana bank's own head, 40) +
    #    한글 (52) + 二百零五 (a READING of 205, weightless).
    r = triad_weigh('あくま한글二百零五')
    checks.append(('the mixed face: weight 92 = Japanese 40 + '
                   'Korean 52; the Chinese run READS 205 and '
                   'adds nothing to the weight',
                   r['weight'] == 92
                   and r['strata'] == {'japanese': 40,
                                       'korean': 52}
                   and [x['value'] for x in r['readings']] == [205],
                   (r['weight'], r['strata'],
                    [x['value'] for x in r['readings']])))
    # 3. The cross-stratum sum, exhibited as arithmetic: あ
    #    (1) more makes 93 across two strata — printed as the
    #    dial's arithmetic, never a bridge.
    r = triad_weigh('ああくま한글')
    checks.append(('cross-stratum arithmetic, as arithmetic: '
                   'ああくま한글 == 93 (41 + 52)',
                   r['weight'] == 93
                   and r['strata'] == {'japanese': 41,
                                       'korean': 52},
                   (r['weight'], r['strata'])))
    # 4. The zero's three faces, computed.
    z = triad_zero()
    checks.append(('the zero at the core: Japanese HOLE (no '
                   'zero-valued kana), Korean PLACEHOLDER (아 '
                   'counts a null), Chinese GLYPH (零 reads 0)',
                   z['faces']['japanese'].startswith('HOLE')
                   and z['faces']['korean'].startswith('PLACEHOLDER')
                   and z['faces']['chinese'].startswith('GLYPH'),
                   (z['faces']['japanese'][:20],
                    z['faces']['korean'][:20],
                    z['faces']['chinese'][:20])))
    # 5. The cycles as weightless coordinates: 甲子 reports
    #    (stem 1, branch 1) and weighs nothing.
    r = triad_weigh('甲子')
    checks.append(('the cycles: 甲子 reports stem 1 + branch 1 '
                   'as coordinates and weighs 0',
                   r['weight'] == 0
                   and r['cycles'] == [('甲', 'stem', 1),
                                       ('子', 'branch', 1)],
                   (r['weight'], r['cycles'])))
    # 6. THE OPEN LEG, proven: a Chinese character that is not
    #    a numeral sign is unread on the dial — counted, never
    #    weighed, never misread as a number.
    r = triad_weigh('猫')
    checks.append(('the open leg: 猫 is unread (1), weight 0, '
                   'no reading issued — the Chinese weighing '
                   'leg stands open, not forced',
                   r['weight'] == 0 and r['unread'] == 1
                   and r['readings'] == [],
                   (r['weight'], r['unread'])))
    # 7. The hist flag reaches the Korean stratum alone: ㆍ is
    #    unseated on the modern face and seated (vowel 1) on
    #    the hist face, the Japanese stratum unmoved.
    modern = triad_weigh('ㆍ')
    annex = triad_weigh('ㆍ', hist=True)
    checks.append(('the annex on the dial: ㆍ weighs 0 modern, '
                   '1 with hist=True (its 1446 vowel seat)',
                   modern['weight'] == 0 and annex['weight'] == 1,
                   (modern['weight'], annex['weight'])))
    # 8. The fence.
    checks.append(('the dial\'s fence: CONSTRUCTED, the open '
                   'leg and the not-a-bridge clause on its face',
                   _PROVENANCE.startswith('CONSTRUCTED')
                   and 'OPEN' in _PROVENANCE
                   and 'not a bridge claim' in _PROVENANCE,
                   _PROVENANCE[:60]))
    return checks

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
