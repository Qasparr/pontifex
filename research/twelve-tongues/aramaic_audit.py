#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — aramaic_audit.py — the Aramaic Phase I audit: data builder
# Companion to aramaic.md (the Twelve-Tongues sweep, Worker #7) and to
# THE-ARAMAIC-SEAT-PHASE-I-AUDIT.md (the audit document of record).
#
# Epigraph: "In addition to the sounds of the language, the letters of
# the Syriac alphabet can be used to represent numbers in a system
# similar to Hebrew and Greek numerals." — Wikipedia, "Syriac alphabet"
# (the practice, stated on the tradition's own page).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to the
# author's red pen. This file is an AUDIT instrument: findings, never
# doctrine. Nothing here is a bank; nothing here enters the engine.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: (i) the Aramaic letter-values — the abjad bank entire,
#     1–400 over the 22 letters — can be re-sourced in Aramaic's OWN
#     record, in two scripts at once: the Imperial Aramaic glyphs
#     (U+10840–U+10855) tabulated with their numerical values by
#     Cherry (York University), and the Syriac letters, whose own
#     numeral practice the grammatical tradition (Nöldeke's appendix,
#     via Hughes) documents; (ii) held against the engine's living
#     HEBREW bank, the identity the sweep asserted (Hebrew≡Aramaic)
#     will prove cell by cell, in both directions — and where the two
#     traditions genuinely part (the finals), the parting will print
#     at an exact coordinate instead of dissolving into the identity.
#   Method: (1) transcribe the values from THREE witnesses read entire
#     on 2026-11-24 — Cherry, "Imperial Aramaic Script (700 B.C.E.–
#     200 B.C.E.) with West-Syriac Reading" (the Imperial glyphs with
#     a Numerical Value column); Wikipedia, "Syriac alphabet" (the
#     summary table: Syriac glyph, Imperial equivalent, Hebrew
#     equivalent, Numerical Value); tooldune, "Syriac Alphabet Table"
#     (the Syriac values, following Wikipedia and the Unicode chart) —
#     and diff them cell by cell in code: a disagreement aborts the
#     build as a finding, never averages away; (2) generate every
#     glyph from its codepoint (the Imperial block consecutive,
#     U+10840 + position − 1; the Syriac letters at their standard's
#     own seats) and verify each Unicode name; (3) hold the table
#     against the living HEBREW bank's values as transcribed here,
#     seat by seat — the identity battery; (4) recompute the
#     tradition's own exhibits (the 77 head in three scripts; the
#     Syriac additive hundreds of Nöldeke's appendix) before trusting
#     any derived number.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Aramaic Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The values below
are TRANSCRIPTIONS of a published, attested table — the shared
Northwest Semitic abjad values as Aramaic's own record carries them —
with their sources on their face. No value here is the house's
coinage, and no row enters pontifex/engine.py from this file: the
seat, if the gate holds, is built separately in Phase II and proven
against the CSVs this builder freezes.

MECHANISM: two CSVs are written beside this script —
  aramaic-table.csv      the 22 letters in TWO strata (IMPERIAL,
                         the classical Imperial Aramaic glyphs;
                         SYRIAC, the letters of Aramaic's living
                         descendant script), each row SOURCED,
                         carrying its codepoint and Unicode name
                         as the verification witness;
  aramaic-identity.csv   the identity battery in data: per position,
                         the Imperial glyph, the Syriac glyph, the
                         Hebrew glyph, and the three values — the
                         relation the audit exists to prove, row by
                         row, so the parity battery can re-prove it
                         against the living banks.
The companion battery aramaic_audit_tests.py re-derives every number
the audit document prints from these CSVs and from its own
independent source constants.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- The abjad order -------------------------------------------------------------
# DOCTRINE: the audit seats the SHARED ABJAD — the 22 letters in the
# order the whole Northwest Semitic tradition carries (ʾālep̄ … taw),
# which is simultaneously the Imperial Aramaic inventory, the Syriac
# inventory, and the Hebrew inventory. Position in this list IS the
# audit's coordinate: every comparison in this build is made at a
# position, never at a glyph guessed across scripts.
# MECHANISM: (letter name as the Aramaic tradition gives it,
# transliteration, the Unicode name-token of the Imperial letter,
# the Unicode name-token of the Syriac letter).
LETTERS = [
    ('Ālap̄',  'ʾ', 'ALEPH',  'ALAPH'),
    ('Bēṯ',    'b', 'BETH',   'BETH'),
    ('Gāmal',  'g', 'GIMEL',  'GAMAL'),
    ('Dālaṯ',  'd', 'DALETH', 'DALATH'),
    ('Hē',     'h', 'HE',     'HE'),
    ('Waw',    'w', 'WAW',    'WAW'),
    ('Zayn',   'z', 'ZAYIN',  'ZAIN'),
    ('Ḥēṯ',    'ḥ', 'HETH',   'HETH'),
    ('Ṭēṯ',    'ṭ', 'TETH',   'TETH'),
    ('Yōḏ',    'y', 'YODH',   'YUDH'),
    ('Kāp̄',    'k', 'KAPH',   'KAPH'),
    ('Lāmaḏ',  'l', 'LAMEDH', 'LAMADH'),
    ('Mīm',    'm', 'MEM',    'MIM'),
    ('Nūn',    'n', 'NUN',    'NUN'),
    ('Semkaṯ', 's', 'SAMEKH', 'SEMKATH'),
    ('ʿĒ',     'ʿ', 'AYIN',   'E'),
    ('Pē',     'p', 'PE',     'PE'),
    ('Ṣāḏē',   'ṣ', 'SADHE',  'SADHE'),
    ('Qōp̄',    'q', 'QOPH',   'QAPH'),
    ('Rēš',    'r', 'RESH',   'RISH'),
    ('Šīn',    'š', 'SHIN',   'SHIN'),
    ('Taw',    't', 'TAW',    'TAW'),
]

# MECHANISM: the Syriac letters are NOT consecutive in their block
# (vowel points and later additions stand between them), so their
# codepoints are stated seat by seat — each verified against the
# standard's name below, so a wrong seat aborts the build.
SYRIAC_CPS = [0x0710, 0x0712, 0x0713, 0x0715, 0x0717, 0x0718,
              0x0719, 0x071A, 0x071B, 0x071D, 0x071F, 0x0720,
              0x0721, 0x0722, 0x0723, 0x0725, 0x0726, 0x0728,
              0x0729, 0x072A, 0x072B, 0x072C]

# MECHANISM: the Hebrew side of the identity, in abjad order — the
# base letters only. The five final forms (ךםןףץ) are NOT positions
# of the abjad; they are the finals coordinate, handled in the
# battery, and their absence from this list is the audit's point.
HEBREW_ORDER = 'אבגדהוזחטיכלמנסעפצקרשת'

# -- The witnesses, transcribed independently -------------------------------------
# DOCTRINE: three transcriptions of the one table, made separately so
# the diff between them is evidence. CHERRY carries the values paired
# with the IMPERIAL glyphs themselves (his chart's columns: Imperial
# Aramaic Script / West-Syriac Reading / Transliteration / Numerical
# Value; references Diringer 1968, Healey 1990, Hetzron 1997, Rogers
# 2005). WIKIPEDIA carries the values in the Syriac summary table,
# whose rows ALSO pair each Syriac glyph with its Imperial Aramaic
# equivalent — so this witness testifies to both strata and to the
# correspondence between them. TOOLDUNE carries the Syriac values
# again, its page stating it follows the Wikipedia tables and the
# Unicode chart (a concurrence, counted as such, not a third
# independence at full weight).
WITNESS_CHERRY = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                  10, 20, 30, 40, 50, 60, 70, 80, 90,
                  100, 200, 300, 400]
WITNESS_WIKIPEDIA = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 20, 30, 40, 50, 60, 70, 80, 90,
                     100, 200, 300, 400]
WITNESS_TOOLDUNE = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    10, 20, 30, 40, 50, 60, 70, 80, 90,
                    100, 200, 300, 400]

# MECHANISM: the Hebrew bank's values as the engine seats them
# (mispar hechrechi, base letters in abjad order) — transcribed here
# so the AUDIT holds the identity against a constant; the parity
# battery at the repository root re-proves it against the LIVING
# bank, so a drift in either seat would be caught by one of the two.
HEBREW_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 20, 30, 40, 50, 60, 70, 80, 90,
                 100, 200, 300, 400]


def abjad_value(position):
    """The abjad class law, restated as law (never as source).

    MECHANISM: nine units (positions 1–9, value = position), nine
    tens (10–18, value = (position − 9) × 10), four hundreds
    (19–22, value = (position − 18) × 100). The battery holds the
    transcribed cells to this law; the law itself is checked
    against the witnesses, never the other way round.
    """
    if position <= 9:
        return position
    if position <= 18:
        return (position - 9) * 10
    return (position - 18) * 100


def main():
    # -- The witness diff: a parting aborts the build -------------------
    witnesses = {'cherry': WITNESS_CHERRY,
                 'wikipedia': WITNESS_WIKIPEDIA,
                 'tooldune': WITNESS_TOOLDUNE}
    for name, vals in witnesses.items():
        if len(vals) != 22:
            print('ABORT — witness %s carries %d values, not 22'
                  % (name, len(vals)))
            return 1
    partings = [(i + 1, {n: v[i] for n, v in witnesses.items()})
                for i in range(22)
                if len({v[i] for v in witnesses.values()}) != 1]
    if partings:
        print('ABORT — the witnesses PART at %r; a parting is a '
              'finding, never averaged away' % (partings,))
        return 1
    values = WITNESS_CHERRY
    print('WITNESS DIFF — three transcriptions agree on all 22 '
          'cells (Cherry for the Imperial stratum; Wikipedia and '
          'tooldune for the Syriac)')

    # -- Generate the glyphs; verify every name --------------------------
    rows = []
    identity = []
    for i, (name, tr, imp_token, syr_token) in enumerate(LETTERS):
        pos = i + 1
        imp = chr(0x10840 + i)
        syr = chr(SYRIAC_CPS[i])
        heb = HEBREW_ORDER[i]
        imp_name = ud.name(imp, '')
        syr_name = ud.name(syr, '')
        if imp_name != 'IMPERIAL ARAMAIC LETTER ' + imp_token:
            print('ABORT — U+%05X is named %r, not the Imperial '
                  'letter %s' % (0x10840 + i, imp_name, imp_token))
            return 1
        if syr_name != 'SYRIAC LETTER ' + syr_token:
            print('ABORT — U+%04X is named %r, not the Syriac '
                  'letter %s' % (SYRIAC_CPS[i], syr_name, syr_token))
            return 1
        v = values[i]
        if v != abjad_value(pos) or v != HEBREW_VALUES[i]:
            print('ABORT — position %d: witness value %d breaks '
                  'the law or the identity' % (pos, v))
            return 1
        rows.append({
            'position': pos, 'stratum': 'IMPERIAL', 'glyph': imp,
            'codepoint': 'U+%05X' % (0x10840 + i),
            'unicode_name': imp_name, 'letter_name': name,
            'transliteration': tr, 'hebrew_equivalent': heb,
            'value': v, 'status': 'SOURCED',
            'witnesses': 'Cherry (Imperial chart, Numerical Value '
                         'column); Wikipedia "Syriac alphabet" '
                         '(Imperial Aramaic Equivalent column)',
        })
        rows.append({
            'position': pos, 'stratum': 'SYRIAC', 'glyph': syr,
            'codepoint': 'U+%04X' % SYRIAC_CPS[i],
            'unicode_name': syr_name, 'letter_name': name,
            'transliteration': tr, 'hebrew_equivalent': heb,
            'value': v, 'status': 'SOURCED',
            'witnesses': 'Wikipedia "Syriac alphabet" (Numerical '
                         'Value column); tooldune (Num. column); '
                         'Hughes after Nöldeke (the practice)',
        })
        identity.append({
            'position': pos, 'letter_name': name,
            'imperial_glyph': imp, 'syriac_glyph': syr,
            'hebrew_glyph': heb, 'imperial_value': v,
            'syriac_value': v, 'hebrew_value': HEBREW_VALUES[i],
            'relation': 'IDENTICAL',
        })
    print('GLYPHS — 44 signs generated from their codepoints; '
          'Unicode names verified 44/44 (22 Imperial, consecutive '
          'U+10840–U+10855; 22 Syriac at the standard\'s seats)')

    # -- Write the frozen transcription ----------------------------------
    with open(os.path.join(HERE, 'aramaic-table.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'position', 'stratum', 'glyph', 'codepoint',
            'unicode_name', 'letter_name', 'transliteration',
            'hebrew_equivalent', 'value', 'status', 'witnesses'])
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(HERE, 'aramaic-identity.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=[
            'position', 'letter_name', 'imperial_glyph',
            'syriac_glyph', 'hebrew_glyph', 'imperial_value',
            'syriac_value', 'hebrew_value', 'relation'])
        w.writeheader()
        w.writerows(identity)
    print('WROTE aramaic-table.csv (44 SOURCED rows: 22 IMPERIAL '
          '+ 22 SYRIAC) and aramaic-identity.csv (22 rows, '
          'relation IDENTICAL at every position)')

    # -- The exhibits, recomputed from the built table --------------------
    table = {(r['stratum'], r['glyph']): r['value'] for r in rows}

    def weigh(stratum, s):
        return sum(table[(stratum, c)] for c in s)

    oz_i = weigh('IMPERIAL', '𐡏𐡆')
    oz_s = weigh('SYRIAC', 'ܥܙ')
    print('EXHIBIT — the founding head in three scripts: Imperial '
          '𐡏𐡆 = %d; Syriac ܥܙ = %d; (Hebrew עז = 77 at the living '
          'bank, re-proven by the parity battery)' % (oz_i, oz_s))
    # MECHANISM: the Syriac additive hundreds of Nöldeke's appendix
    # (via Hughes): past 400 the tradition writes taw-prefixed
    # hundreds — no new values, the bank's own letters added.
    add = {s: weigh('SYRIAC', s)
           for s in ('ܬܩ', 'ܬܪ', 'ܬܫ', 'ܬܬ', 'ܬܬܩ')}
    print('EXHIBIT — the Syriac additive hundreds (Nöldeke via '
          'Hughes): %r' % (add,))
    ex = {s: weigh('SYRIAC', s) for s in ('ܝܒ', 'ܠܘ', 'ܩܢܙ', 'ܬܫܣܕ')}
    print('EXHIBIT — Hughes\' worked examples: %r' % (ex,))
    print('SUMS — each stratum: 22 distinct values, sum %d'
          % sum(values))
    return 0


if __name__ == '__main__':
    sys.exit(main())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
