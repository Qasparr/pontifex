#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — runic_ogham_audit.py — the Runic and Ogham field audit:
# data builder. Companion to THE-RUNIC-AND-OGHAM-FIELD.md (the audit
# document of record) and Leg A of the Western Sweep.
#
# Epigraph: "Most runic texts, including the Viking age runestones use
# no number system, instead numbers are simply spelled out." —
# Wikipedia, "Pentadic numerals" (read entire, 2026-11-24).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open
# to the author's red pen. This file is an AUDIT instrument: findings,
# never doctrine. Nothing here is a bank; nothing here enters the
# engine.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis (the commission's, to be tested not assumed): neither
#     the runes nor the Ogham letters carry an attested letter-numeral
#     TABLE — a checked negative like Korean's — with attested
#     notation and cipher species standing beside the empty seat.
#   Method: the field worked in its actual strata, each sourced and
#     fenced separately: (1) runes as numerals in medieval practice
#     (the calendar golden numbers; the inscriptional abbreviation
#     practice); (2) the pentadic notation of the Scandinavian
#     calendars, and its 1885 positional offshoot; (3) the Ogham
#     letters, their order, and the tract's numerical material; (4)
#     the modern rune-value systems, fenced MODERN. Each stratum
#     transcribed from at least two witnesses read entire on
#     2026-11-24 and diffed in code — a disagreement inside a
#     stratum's diffed domain aborts the build as a finding, never
#     averages away; partings of convention (transliteration, a
#     manuscript's date) are recorded as partings, at coordinates.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Runic-and-Ogham field audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The tables
below are TRANSCRIPTIONS of published material, carried with their
sources on their face. No value here is presented as the house's
doctrine, and no row enters pontifex/engine.py from this file —
the one seat the gate holds (the pentadic notation reader) is
built separately in pontifex/pentadic.py and proven against the
CSV this builder freezes.

MECHANISM: four CSVs are written beside this script —
  golden-numbers.csv   the calendar assignment: the Younger
                       Futhark's sixteen letters at golden numbers
                       1–16 and the three improvised runes at
                       17–19 (an ordinal label set for a closed
                       cycle — coordinates, not a bank);
  pentadic-notation.csv  the pentadic notation's sign law, as the
                       witnesses state it (the calendar stave
                       stratum), with the 1885 positional stratum
                       recorded beneath it, unseated;
  ogham-letters.csv    the Ogham letters in their canonical order
                       (20 primary + 5 forfeda + peith), two
                       witnesses' transliterations side by side,
                       the Unicode standard's names as the code
                       witness — an ORDER, carrying no values;
  uthark-modern.csv    the modern stratum's named system (Agrell,
                       1932), fenced MODERN and UNSEATED.
The companion battery runic_ogham_audit_tests.py re-derives every
number the audit document prints from these CSVs and from its own
independent source constants.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# STRATUM 1 — THE GOLDEN NUMBERS (runes as calendar labels, 1–19)
# ===========================================================================
# Witness 1: Wikipedia, "Runic calendar" (read entire 2026-11-24),
# the Marks table: Arabic 1–19 against the golden-number signs, in
# order. Transcribed as (glyph, name) in printed order.
W1_GOLDEN = [
    ('ᚠ', 'fehu'), ('ᚢ', 'uruz'), ('ᚦ', 'thurisaz'), ('ᚬ', 'oss'),
    ('ᚱ', 'raidu'), ('ᚴ', 'kaun'), ('ᚼ', 'hagall'), ('ᚾ', 'naudr'),
    ('ᛁ', 'iss'), ('ᛅ', 'ar'), ('ᛋ', 'sol'), ('ᛏ', 'tyr'),
    ('ᛒ', 'bjarkan'), ('ᛚ', 'logr'), ('ᛘ', 'madr'), ('ᛦ', 'yr'),
    ('ᛮ', 'arlaug'), ('ᛯ', 'tvimadur'), ('ᛰ', 'belgthor'),
]
# Witness 2: Wikipedia, "Pentadic numerals" (read entire 2026-11-24),
# History: "the 16 letters of Younger Futhark represented the numbers
# from 1 to 16 with three special runes used for the numbers 17 to
# 19", the Computus Runicus manuscript (dated 1343 in this state of
# the article; a second crawl state of the same article prints 1328
# — the parting is recorded in the audit, §III, and the build takes
# no side), collected and published by Ole Worm in the 17th century.
# W2 states the LAW and the EXTENT; the glyph-by-glyph check runs
# against the Unicode standard below.
W2_GOLDEN_LAW = {'letters_1_to': 16, 'special_17_to': 19,
                 'documented_by': 'Ole Worm, 1636 (W1, ref. 1: '
                 'Runir seu Danica literatura antiquissima, ch. '
                 'XVIII, pp. 102–103)'}
# The canonical Younger Futhark row, as the Unicode standard's names
# fix it — the code witness for W1's first sixteen glyphs: each
# glyph's standard name must carry the row's name at its seat.
YF_ROW_NAMES = ['FEHU', 'URUZ', 'THURISAZ', 'OSS', 'RAID', 'KAUN',
                'HAGALL', 'NAUD', 'IS', 'AR', 'SOL', 'TYR', 'BJARKAN',
                'LOGR', 'MADR', 'YR']
YF_ROW_NAME_PARTS = [
    ('FEHU',), ('URUZ',), ('THURISAZ',), ('LONG-BRANCH-OSS',),
    ('RAIDO', 'RAD'), ('KAUN',), ('LONG-BRANCH-HAGALL',),
    ('NAUDIZ', 'NAUD'), ('ISAZ', 'ISS'), ('LONG-BRANCH-AR',),
    ('LONG-BRANCH-SOL', 'SIGEL'), ('TIWAZ', 'TYR'),
    ('BERKANAN', 'BJARKAN'), ('LAUKAZ', 'LOGR'),
    ('LONG-BRANCH-MADR',), ('LONG-BRANCH-YR',),
]
GOLDEN_SPECIAL_NAMES = {17: 'ARLAUG', 18: 'TVIMADUR', 19: 'BELGTHOR'}


def diff_golden():
    """Diff stratum 1: W1's table against W2's law and the standard.

    MECHANISM: (i) W1's table has exactly 19 rows, values 1–19 in
    order; (ii) its first sixteen glyphs are the Younger Futhark
    row in canonical order — each glyph's Unicode name carries the
    row name at its seat; (iii) its last three glyphs are the
    standard's three RUNIC ... SYMBOL signs, named for the three
    improvised runes; (iv) W2's law (16 letters → 1–16, three
    special → 17–19) matches the table's shape exactly. Any
    failure aborts the build as a finding.
    """
    assert len(W1_GOLDEN) == 19, 'W1 golden table extent'
    for i, (glyph, name) in enumerate(W1_GOLDEN[:16], start=1):
        uname = ud.name(glyph)
        assert any(p in uname for p in YF_ROW_NAME_PARTS[i - 1]), \
            'seat %d: %s not the YF row letter %s' % (i, uname, name)
    for value in (17, 18, 19):
        glyph = W1_GOLDEN[value - 1][0]
        uname = ud.name(glyph)
        assert 'SYMBOL' in uname and \
            GOLDEN_SPECIAL_NAMES[value] in uname, \
            'golden %d: %s' % (value, uname)
    assert W2_GOLDEN_LAW['letters_1_to'] == 16
    assert W2_GOLDEN_LAW['special_17_to'] == 19
    return 'W1 table == W2 law == the standard: 19/19 seats'


# ===========================================================================
# STRATUM 2 — THE PENTADIC NOTATION (a notation, not a table)
# ===========================================================================
# Witness 1: Wikipedia, "Pentadic numerals" (read entire): the ticks
# are placed vertically on a stem or stav; 4 = four horizontal lines
# on the stem; 5 = what looks like an inverted letter U; 10 = two
# U's opposing each other; numbers up to 19, or even 20, by
# combination of I's and U's; widest use the golden numbers 1–19 on
# runic calendars (clogs); numbers commonly found in Modern Age and
# possibly Early Modern Age calendars; medieval use unknown.
# Witness 2: Wikipedia, "Runic calendar" (read entire): "Later
# calendars used Pentadic numerals for the values 1–19."
# The sign law frozen as rows: (sign, form, value, standing).
PENTADIC_LAW = [
    ('unit tick', 'one horizontal line on the stem', 1,
     'the additive unit — n ticks read n, to four'),
    ('four ticks', 'four horizontal lines on the stem', 4,
     'the largest tick group the witnesses describe'),
    ('five-sign', 'what looks like an inverted letter U', 5,
     'a single sign, not five ticks (W1)'),
    ('five-sign + ticks', 'the five-sign with n ticks added', '5+n',
     '6–9, n to four (the witnesses\' shape; cf. the positional '
     'stratum\'s "additional branches" for 6–9)'),
    ('ten-sign', 'two U\'s opposing each other', 10,
     'a single sign (W1)'),
    ('ten-sign + unit', 'the ten-sign with a unit sign', '10+n',
     '11–19 — the golden-number extent'),
    ('two ten-signs', 'two ten-signs', 20,
     '"up to 19, or even 20" (W1) — the notation\'s stated ceiling'),
]
# The positional stratum (recorded, UNSEATED): Edward Larsson's
# notes of 1885 — the oldest AUTHENTICATED use of pentadic runes as
# a base-ten positional digit set (W1, Positional notation). The
# two North American stone groups that use it (Kensington, 1898;
# Spirit Pond, 1971) are modern hoaxes in the runological consensus
# both witnesses print. The per-digit shapes of this stratum live
# in the witnesses' images and in prose descriptions that part
# (a vertical line with a circle on top for 0, in one account; an
# O placed at the top "for 0 and 10" in another) — no digit table
# is frozen, and the reader in pontifex/pentadic.py does not seat
# this stratum. See the audit, §IV.
POSITIONAL_STRATUM = {
    'oldest_authenticated': 'Edward Larsson\'s notes, 1885 (W1)',
    'standing': 'MODERN (19th century); the North American stones '
                'are hoaxes (W1, refs. 1–3)',
    'seated': False,
}


# ===========================================================================
# STRATUM 3 — OGHAM (an order; the tract's ciphers and tallies)
# ===========================================================================
# Witness 1: Wikipedia, "Ogham" (read entire 2026-11-24), the
# Letters table: (glyph, name, transliteration) in printed order —
# 20 primary letters, then the forfeda, then peith.
W1_OGHAM = [
    ('ᚁ', 'beith', 'b'), ('ᚂ', 'luis', 'l'), ('ᚃ', 'fearn', 'f'),
    ('ᚄ', 'sail', 's'), ('ᚅ', 'nion', 'n'),
    ('ᚆ', 'uath', 'h'), ('ᚇ', 'dair', 'd'), ('ᚈ', 'tinne', 't'),
    ('ᚉ', 'coll', 'c'), ('ᚊ', 'ceirt', 'q'),
    ('ᚋ', 'muin', 'm'), ('ᚌ', 'gort', 'g'), ('ᚍ', 'ngéadal', 'ng'),
    ('ᚎ', 'straif', 'st'), ('ᚏ', 'ruis', 'r'),
    ('ᚐ', 'ailm', 'a'), ('ᚑ', 'onn', 'o'), ('ᚒ', 'úr', 'u'),
    ('ᚓ', 'eadhadh', 'e'), ('ᚔ', 'iodhadh', 'i'),
    ('ᚕ', 'éabhadh', 'ea'), ('ᚖ', 'óir', 'oi'),
    ('ᚗ', 'uilleann', 'ui'), ('ᚘ', 'pín/ifín', 'p/io'),
    ('ᚙ', 'eamhancholl', 'ch/x/ae'),
    ('ᚚ', 'peith', 'p'),
]
# Witness 2: Wikipedia, "Template:Table Oghamletters" (read entire
# 2026-11-24): the same letters grouped by aicme, transliterations
# in the Primitive Irish convention. Transcribed as name ->
# transliteration, in the template's order.
W2_OGHAM = [
    ('beith', 'b'), ('luis', 'l'), ('fearn', 'w'), ('sail', 's'),
    ('nion', 'n'),
    ('uath', 'j'), ('dair', 'd'), ('tinne', 't'), ('coll', 'k'),
    ('ceirt', 'kʷ'),
    ('muin', 'm'), ('gort', 'ɡ'), ('ngéadal', 'ɡʷ'),
    ('straif', 'st/ts/sw'), ('ruis', 'r'),
    ('ailm', 'a'), ('onn', 'o'), ('úr', 'u'), ('eadhadh', 'e'),
    ('iodhadh', 'i'),
    ('éabhadh', 'ea'), ('óir', 'oi'), ('uilleann', 'ui'),
    ('ifín', 'ia'), ('eamhancholl', 'x/ai'),
    ('peith', 'p'),
]
# The transliteration partings between the witnesses — conventions,
# not order or name partings — recorded at their seats (the audit,
# §V): W1 prints the later/manuscript values, W2 the Primitive
# Irish values, for the letters whose sound changed.
OGHAM_TRANSLIT_PARTINGS = {
    3: 'fearn: W1 f (later) / W2 w (Primitive Irish [w])',
    6: 'uath: W1 h / W2 j — the letter\'s value is uncertain in '
       'both witnesses (W1 prints [j] and [h] side by side)',
    9: 'coll: W1 c / W2 k — one sound, two conventions',
    10: 'ceirt: W1 q / W2 kʷ — one sound, two conventions',
    12: 'gort: W1 g / W2 ɡ — one sound, two conventions',
    13: 'ngéadal: W1 ng / W2 ɡʷ — the manuscript value against the '
        'etymological value (W1\'s own text: "probably GW")',
    14: 'straif: W1 st / W2 st, ts, sw — the range stated wider',
    24: 'ifín: W1 p/io (name pín, later ifín) / W2 ia — the '
        'forfeda\'s reassignment, both witnesses record it',
    25: 'eamhancholl: W1 ch/x/ae / W2 x/ai — the reassignment, '
        'as at 24',
}
# The one seat where the STANDARD's name parts from both witnesses':
# U+1696 is OGHAM LETTER OR; W1 and W2 both print the name Óir.
# Recorded, not smoothed — the glyph and the seat are not in doubt.
OGHAM_STD_NAME_PARTINGS = {
    22: 'the standard shortens the name to OR; both witnesses '
        'print Óir',
}
AICMI = [(1, 'beithe', 1, 5), (2, 'hÚatha', 6, 10),
         (3, 'muine', 11, 15), (4, 'ailme', 16, 20),
         (5, 'forfeda', 21, 25)]


def diff_ogham():
    """Diff stratum 3: W1 against W2 against the standard.

    MECHANISM: (i) both witnesses carry 26 rows in the same order
    (peith last, a manuscript letter standing outside the five
    aicmi in both); (ii) the NAMES agree at every seat, modulo the
    one recorded renaming (pín → ifín at seat 24, which W1 prints
    as a double name and W2 under the later name); (iii) every
    glyph is the Unicode block's letter of that name at that seat
    — the block U+1681–U+169A is the canonical order itself;
    (iv) transliterations part only at the recorded seats, and
    only as conventions. Any other failure aborts the build.
    """
    def plain(s):
        # the standard's names carry no diacritics; the witnesses'
        # Irish names do (ngéadal, úr, óir, éabhadh) — compare with
        # the accents folded, and say so: accent is orthography,
        # not a name parting.
        return ''.join(c for c in ud.normalize('NFKD', s)
                       if not ud.combining(c)).lower()

    assert len(W1_OGHAM) == len(W2_OGHAM) == 26
    for seat, ((glyph, name1, _t1), (name2, _t2)) in enumerate(
            zip(W1_OGHAM, W2_OGHAM), start=1):
        uname = ud.name(glyph)
        assert 'OGHAM LETTER' in uname, (seat, uname)
        # the standard's name for the glyph at this seat:
        std = plain(uname.replace('OGHAM LETTER ', ''))
        w1_names = [plain(n) for n in name1.split('/')]
        assert std in w1_names or std == plain(name2) \
            or seat in OGHAM_STD_NAME_PARTINGS, \
            'seat %d: standard %s vs W1 %s / W2 %s' % (
                seat, std, name1, name2)
        assert plain(name2) in w1_names or plain(name2) == std, \
            'seat %d name parting: W1 %s / W2 %s' % (seat, name1, name2)
        # the block is sequential: seat n is U+1680+n
        assert ord(glyph) == 0x1680 + seat, (seat, hex(ord(glyph)))
    return 'W1 == W2 == the standard: 26/26 seats, names entire; ' \
           'transliterations part at 9 recorded seats, as conventions'


# ===========================================================================
# STRATUM 4 — THE MODERN SYSTEMS (fenced MODERN, unseated)
# ===========================================================================
# The Uthark: Sigurd Agrell's 1932 reordering (Die spätantike
# Alphabet-Mystik und die Runenreihe) — the futhark row read as a
# cipher: F moved last, every rune valued by its position in the
# shifted row (U = 1 … F = 24). Witness 1: Wikipedia, "Uthark
# theory" (read entire 2026-11-24): "no support in historical
# sources and was never accepted in mainstream runic studies".
# Witness 2: the rune-numerology reference table (read 2026-11-24),
# which prints the uthark numbers seat by seat — and presents F at
# BOTH 0 and 24 (the parting recorded: the cycle's outside against
# the cycle's completion; the values of the other 23 agree).
UTHARK_ORDER = ['u', 'þ', 'a', 'r', 'k', 'g', 'w', 'h', 'n', 'i',
                'j', 'ï', 'p', 'z', 's', 't', 'b', 'e', 'm', 'l',
                'ŋ', 'd', 'o', 'f']
UTHARK_F_PARTING = 'F at 24 (W2\'s seat table; the Everand ' \
    'excerpt of Karlsson 2002: "Fehu as the 24th") against F at ' \
    '0 (W2\'s significance table: "the unmanifest source") — a ' \
    'presentation parting inside the modern stratum, recorded, ' \
    'not resolved: the system is unseated either way.'


def main():
    print(diff_golden())
    print(diff_ogham())
    # --- golden-numbers.csv -------------------------------------------------
    with open(os.path.join(HERE, 'golden-numbers.csv'), 'w',
              newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['golden_number', 'glyph', 'codepoint',
                    'unicode_name', 'rune_name', 'stratum',
                    'standing', 'source'])
        for value, (glyph, name) in enumerate(W1_GOLDEN, start=1):
            w.writerow([value, glyph, 'U+%04X' % ord(glyph),
                        ud.name(glyph), name,
                        'calendar label (Younger Futhark row)'
                        if value <= 16 else
                        'calendar label (improvised rune)',
                        'SOURCED — an ordinal label for a closed '
                        'cycle of 19; NOT a letter value: the '
                        'labels do not compose',
                        'Wikipedia, "Runic calendar" (table); '
                        'Wikipedia, "Pentadic numerals" (the law); '
                        'Unicode standard (the glyphs\' names)'])
    # --- pentadic-notation.csv ----------------------------------------------
    with open(os.path.join(HERE, 'pentadic-notation.csv'), 'w',
              newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['sign', 'form', 'value', 'standing', 'source'])
        for sign, form, value, standing in PENTADIC_LAW:
            w.writerow([sign, form, value, standing,
                        'Wikipedia, "Pentadic numerals"; Wikipedia, '
                        '"Runic calendar" ("Later calendars used '
                        'Pentadic numerals for the values 1–19")'])
        w.writerow(['positional digit set', 'ten distinct digit '
                    'signs on stems, base-ten positional',
                    '0–9 per position',
                    'RECORDED, UNSEATED — ' +
                    POSITIONAL_STRATUM['standing'] +
                    '; oldest authenticated use: ' +
                    POSITIONAL_STRATUM['oldest_authenticated'],
                    'Wikipedia, "Pentadic numerals" (Positional '
                    'notation)'])
    # --- ogham-letters.csv ----------------------------------------------------
    with open(os.path.join(HERE, 'ogham-letters.csv'), 'w',
              newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['seat', 'aicme', 'glyph', 'codepoint',
                    'unicode_name', 'name', 'transliteration_w1',
                    'transliteration_w2', 'parting', 'standing'])
        for seat, ((glyph, name1, t1), (name2, t2)) in enumerate(
                zip(W1_OGHAM, W2_OGHAM), start=1):
            aicme = next((a[1] for a in AICMI if a[2] <= seat <= a[3]),
                         '— (peith: manuscript letter, outside the '
                         'five aicmi in both witnesses)')
            parting = '; '.join(p for p in (
                OGHAM_TRANSLIT_PARTINGS.get(seat, ''),
                OGHAM_STD_NAME_PARTINGS.get(seat, '')) if p)
            w.writerow([seat, aicme, glyph, 'U+%04X' % ord(glyph),
                        ud.name(glyph), name1, t1, t2, parting,
                        'SOURCED — a seat in an ORDER; the letter '
                        'carries no numeral value in any witness'])
    # --- uthark-modern.csv ----------------------------------------------------
    with open(os.path.join(HERE, 'uthark-modern.csv'), 'w',
              newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['uthark_value', 'rune', 'standing', 'source'])
        for value, rune in enumerate(UTHARK_ORDER, start=1):
            w.writerow([value, rune,
                        'MODERN (Agrell, 1932) — a scholarly '
                        'hypothesis rejected by mainstream runic '
                        'studies (W1); UNSEATED in this engine',
                        'Wikipedia, "Uthark theory"; the '
                        'rune-numerology reference table'])
        w.writerow([0, 'f (alternative presentation)',
                    'PARTING recorded: ' + UTHARK_F_PARTING,
                    'the rune-numerology reference table'])
    print('CSVs frozen: golden-numbers (19), pentadic-notation '
          '(%d), ogham-letters (26), uthark-modern (24+1)'
          % (len(PENTADIC_LAW) + 1))


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
