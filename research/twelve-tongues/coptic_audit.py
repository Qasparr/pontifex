#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — coptic_audit.py — the Coptic Phase I audit: data builder
# Companion to coptic.md (the Twelve-Tongues sweep, Worker #8) and to
# THE-COPTIC-TABLE-PHASE-I-AUDIT.md (the audit document of record).
#
# Epigraph: "The numerical value of the letters is based on Greek
# numerals." — Wikipedia, "Coptic script", §Numerals (the descent,
# stated by the witness itself, in one line).
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
#   Hypothesis: (i) the Coptic alphabetic numeral table can be re-sourced
#     sign by sign from independent witnesses that agree entire — the
#     Greek-derived letters at their Milesian values, and the numeral
#     status of every Demotic-derived letter settled exactly as the
#     sources show it; (ii) read against the engine's living Greek
#     Milesian bank, the descent will show precisely what inheritance
#     preserved, what it altered, and at which seats — the key's first
#     inheritance test: a table received, not made or found.
#   Method: (1) transcribe the table from THREE full-table witnesses
#     read entire on 2026-11-24 (Wikipedia, "Coptic script", Letters
#     table + §Numerals; the fsymbols Coptic collection; the tooldune
#     Coptic Alphabet Table — the last stating its derivation from the
#     first on its face, counted as a concurring transcription, not a
#     third independence) and diff them cell by cell in code — a
#     disagreement aborts the build as a finding, never averages away;
#   (2) hold two scholarly partial witnesses (Satzinger's Coptic
#     Course, Univ. of Vienna; Dr. Kamal Farid Isaac, Institute of
#     Coptic Studies, Cairo) to every seat they exhibit; (3) generate
#     every glyph's codepoints and verify each Unicode name; (4)
#     recompute the witnesses' worked examples before trusting any
#     derived number; (5) read the verified table against the Greek
#     bank's seat map, value seat by value seat.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Coptic Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The values below
are TRANSCRIPTIONS of a published table, carried with their sources on
their face; the descent table is a comparison at coordinates against
the Greek Milesian bank, not a verdict. No value here is presented as
the house's doctrine, and no row enters pontifex/engine.py from this
file — the seat, if the gate holds, is built separately in Phase II
and proven against the CSV this builder freezes.

MECHANISM: two CSVs are written beside this script —
  coptic-table.csv    the witnesses' alphabet table entire: 27 rows
                      carrying a value (status SOURCED) and 7 rows
                      carrying none (status NO VALUE — a sourced
                      emptiness, the witnesses' own dash, not a gap
                      in this audit's reading);
  coptic-descent.csv  the descent read seat by seat: one row per
                      Milesian value (27), the Greek bank's sign
                      beside the Coptic sign at the same value, the
                      relation at that seat, plus the summary rows
                      where the partings of kind live (the 200 form,
                      the στ digraph, the unseated natives, the
                      thousands devices, the total).
The companion battery coptic_audit_tests.py re-derives every number
the audit document prints from these CSVs, from its own independent
source constants, and from the living Greek bank itself.
"""

import csv
import os
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- The witnesses' table, in the witnesses' own row order ----------------------
# DOCTRINE: the audit's field is the alphabet table as the witnesses
# print it: the 25 Greek-side rows (the 24 living letters + sou, the
# stigma's heir), the 8 Demotic rows (the seven letters — khai wearing
# two dialectal glyphs, Ϧ Bohairic and Ⳉ Akhmimic — counted once as a
# letter, twice as a row), and sampi, which stands outside the
# 32-letter alphabet as a numeral sign. 34 rows; 27 carry values.
# MECHANISM: (capital, small, transliteration, Greek equivalent as
# W1 prints it, origin). Position in this list IS the audit's
# coordinate — the row order of Wikipedia's Letters table, which
# fsymbols' Bohairic order and tooldune's table follow.
ROWS = [
    ('Ⲁ', 'ⲁ', 'A', 'Α, α', 'Greek'),
    ('Ⲃ', 'ⲃ', 'B', 'Β, β', 'Greek'),
    ('Ⲅ', 'ⲅ', 'G', 'Γ, γ', 'Greek'),
    ('Ⲇ', 'ⲇ', 'D', 'Δ, δ', 'Greek'),
    ('Ⲉ', 'ⲉ', 'E', 'Ε, ε', 'Greek'),
    ('Ⲋ', 'ⲋ', '(none)', 'Ϛ, ϛ', 'Greek — the stigma seat'),
    ('Ⲍ', 'ⲍ', 'Z', 'Ζ, ζ', 'Greek'),
    ('Ⲏ', 'ⲏ', 'Ē', 'Η, η', 'Greek'),
    ('Ⲑ', 'ⲑ', 'Th', 'Θ, θ', 'Greek'),
    ('Ⲓ', 'ⲓ', 'I', 'Ι, ι', 'Greek'),
    ('Ⲕ', 'ⲕ', 'K', 'Κ, κ', 'Greek'),
    ('Ⲗ', 'ⲗ', 'L', 'Λ, λ', 'Greek'),
    ('Ⲙ', 'ⲙ', 'M', 'Μ, μ', 'Greek'),
    ('Ⲛ', 'ⲛ', 'N', 'Ν, ν', 'Greek'),
    ('Ⲝ', 'ⲝ', 'Ks', 'Ξ, ξ', 'Greek'),
    ('Ⲟ', 'ⲟ', 'O', 'Ο, ο', 'Greek'),
    ('Ⲡ', 'ⲡ', 'P', 'Π, π', 'Greek'),
    ('Ⲣ', 'ⲣ', 'R', 'Ρ, ρ', 'Greek'),
    ('Ⲥ', 'ⲥ', 'S', 'Σ, σ, ς', 'Greek'),
    ('Ⲧ', 'ⲧ', 'T', 'Τ, τ', 'Greek'),
    ('Ⲩ', 'ⲩ', 'U', 'Υ, υ', 'Greek'),
    ('Ⲫ', 'ⲫ', 'Ph', 'Φ, φ', 'Greek'),
    ('Ⲭ', 'ⲭ', 'Kh', 'Χ, χ', 'Greek'),
    ('Ⲯ', 'ⲯ', 'Ps', 'Ψ, ψ', 'Greek'),
    ('Ⲱ', 'ⲱ', 'Ō', 'Ω, ω', 'Greek'),
    ('Ϣ', 'ϣ', 'Š', '(none)', 'Demotic'),
    ('Ϥ', 'ϥ', 'F', 'Ϙ, ϙ (numerical value)', 'Demotic'),
    ('Ϧ', 'ϧ', 'X', '(none)', 'Demotic — khai, Bohairic form'),
    ('Ⳉ', 'ⳉ', '(none)', '(none)', 'Demotic — khai, Akhmimic form'),
    ('Ϩ', 'ϩ', 'H', '(none)', 'Demotic'),
    ('Ϫ', 'ϫ', 'J', '(none)', 'Demotic'),
    ('Ϭ', 'ϭ', 'C', '(none)', 'Demotic'),
    ('Ϯ', 'ϯ', 'Ti', 'Τι, τι', 'Demotic'),
    ('Ⳁ', 'ⳁ', '(none)', 'Ϡ, ϡ (numerical value)',
     'Greek — the sampi sign'),
]

# -- The witnesses, transcribed independently -----------------------------------
# DOCTRINE: three full-table witnesses read entire on 2026-11-24 print
# the values; each transcription below was taken from its own page,
# and the builder diffs them cell by cell. WIKI is Wikipedia, "Coptic
# script" (Letters table, Numeric value column); FSYMBOLS is the
# fsymbols Coptic collection (its letter grid + §"Coptic numbers");
# TOOLDUNE is the tooldune Coptic Alphabet Table, which states on its
# face that its values "follow the Wikipedia Coptic script tables" —
# a concurring transcription, its derivation flagged, never counted
# as a third independence. A cell where any witness parts from the
# others aborts the build.
WIKI = {
    'Ⲁ': 1, 'Ⲃ': 2, 'Ⲅ': 3, 'Ⲇ': 4, 'Ⲉ': 5, 'Ⲋ': 6, 'Ⲍ': 7,
    'Ⲏ': 8, 'Ⲑ': 9, 'Ⲓ': 10, 'Ⲕ': 20, 'Ⲗ': 30, 'Ⲙ': 40, 'Ⲛ': 50,
    'Ⲝ': 60, 'Ⲟ': 70, 'Ⲡ': 80, 'Ⲣ': 100, 'Ⲥ': 200, 'Ⲧ': 300,
    'Ⲩ': 400, 'Ⲫ': 500, 'Ⲭ': 600, 'Ⲯ': 700, 'Ⲱ': 800,
    'Ϥ': 90, 'Ⳁ': 900,
}
WIKI_NONE = {'Ϣ', 'Ϧ', 'Ⳉ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ'}
FSYMBOLS = {
    'Ⲁ': 1, 'Ⲃ': 2, 'Ⲅ': 3, 'Ⲇ': 4, 'Ⲉ': 5, 'Ⲋ': 6, 'Ⲍ': 7,
    'Ⲏ': 8, 'Ⲑ': 9, 'Ⲓ': 10, 'Ⲕ': 20, 'Ⲗ': 30, 'Ⲙ': 40, 'Ⲛ': 50,
    'Ⲝ': 60, 'Ⲟ': 70, 'Ⲡ': 80, 'Ⲣ': 100, 'Ⲥ': 200, 'Ⲧ': 300,
    'Ⲩ': 400, 'Ⲫ': 500, 'Ⲭ': 600, 'Ⲯ': 700, 'Ⲱ': 800,
    'Ϥ': 90, 'Ⳁ': 900,
}
# MECHANISM: fsymbols' Demotic grid lists six unvalued letters and
# does not carry the Akhmimic Ⳉ row at all — absence from its grid is
# not a parting; its unvalued set must be a subset of WIKI's.
FSYMBOLS_NONE = {'Ϣ', 'Ϧ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ'}
TOOLDUNE = {
    'Ⲁ': 1, 'Ⲃ': 2, 'Ⲅ': 3, 'Ⲇ': 4, 'Ⲉ': 5, 'Ⲋ': 6, 'Ⲍ': 7,
    'Ⲏ': 8, 'Ⲑ': 9, 'Ⲓ': 10, 'Ⲕ': 20, 'Ⲗ': 30, 'Ⲙ': 40, 'Ⲛ': 50,
    'Ⲝ': 60, 'Ⲟ': 70, 'Ⲡ': 80, 'Ⲣ': 100, 'Ⲥ': 200, 'Ⲧ': 300,
    'Ⲩ': 400, 'Ⲫ': 500, 'Ⲭ': 600, 'Ⲯ': 700, 'Ⲱ': 800,
    'Ϥ': 90, 'Ⳁ': 900,
}
TOOLDUNE_NONE = {'Ϣ', 'Ϧ', 'Ⳉ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ'}
# MECHANISM: the scholarly partial witnesses, held to the seats they
# exhibit. SATZINGER (Helmut Satzinger, Coptic Course, Univ. of
# Vienna, Belgrade 2004): his alphabet table's Numerical value column
# exhibits 26 of the 27 seats — the whole Greek run and fai at
# koppa's 90 ("koppa = fai"), sou marked "Number only" — and does
# not exhibit sampi; beyond the table he prints a further seat this
# audit does NOT seat: "+ stauros — 1000, Number only" (a symbol,
# carried in the descent CSV's THOUSANDS row, not in the table).
SATZINGER_EXHIBITS = {
    'Ⲁ': 1, 'Ⲃ': 2, 'Ⲅ': 3, 'Ⲇ': 4, 'Ⲉ': 5, 'Ⲋ': 6, 'Ⲍ': 7,
    'Ⲏ': 8, 'Ⲑ': 9, 'Ⲓ': 10, 'Ⲕ': 20, 'Ⲗ': 30, 'Ⲙ': 40, 'Ⲛ': 50,
    'Ⲝ': 60, 'Ⲟ': 70, 'Ⲡ': 80, 'Ⲣ': 100, 'Ⲥ': 200, 'Ⲧ': 300,
    'Ⲩ': 400, 'Ⲫ': 500, 'Ⲭ': 600, 'Ⲯ': 700, 'Ⲱ': 800,
    'Ϥ': 90,
}
# MECHANISM: ISAAC (Dr. Kamal Farid Isaac, Institute of Coptic
# Studies, Cairo — coptic-cairo.com): exhibits one seat expressly —
# "The sixth letter is not used as a letter, but as a numeral whose
# value is 6" (sou) — and the practice in general: "most Greek
# letters were also used as numerals". His alphabet list counts 31
# letters (24 Greek + 7 Demotic) and does not count sampi among
# them — the sign's standing outside the letter inventory, from a
# Coptic institute's own page.
ISAAC_EXHIBITS = {'Ⲋ': 6}

SOURCE_NOTE = ("Wikipedia, 'Coptic script' (Letters table, Numeric "
               "value column; §Numerals; §Macrons and overlines — "
               "read entire 2026-11-24); fsymbols, Coptic collection "
               "(letter grid + 'Coptic numbers' — read entire "
               "2026-11-24); tooldune, 'Coptic Alphabet Table' "
               "(read entire 2026-11-24; states its derivation from "
               "the Wikipedia tables + the Unicode chart on its "
               "face); Satzinger, Coptic Course (Univ. of Vienna, "
               "2004), alphabet table's Numerical value column "
               "(partial witness, 26 seats exhibited); Isaac, "
               "Institute of Coptic Studies, Cairo (partial witness: "
               "sou + the practice)")


def glyph_name(ch):
    """Unicode name of a glyph, or '' if unassigned — the build's witness."""
    try:
        return ud.name(ch)
    except ValueError:
        return ''


def value_class(value):
    return 'units' if value < 10 else 'tens' if value < 100 \
        else 'hundreds'


def diff_witnesses():
    """Diff the full-table witnesses cell by cell; return the table.

    MECHANISM: the seated value of each sign is WIKI's; FSYMBOLS and
    TOOLDUNE are held against it cell for cell, their unvalued sets
    against WIKI's dash column; SATZINGER and ISAAC are held against
    every seat they exhibit. Any parting raises — the audit prints
    disagreements as coordinates in its document; it never lets one
    pass silently in its data.
    """
    for name, wit in (('fsymbols', FSYMBOLS), ('tooldune', TOOLDUNE)):
        assert wit == WIKI, (
            f"witness parting: {name}'s valued table differs from "
            f"Wikipedia's at "
            f"{[k for k in set(wit) | set(WIKI) if wit.get(k) != WIKI.get(k)]}")
    assert TOOLDUNE_NONE == WIKI_NONE, (
        f"witness parting in the dash column: tooldune "
        f"{sorted(TOOLDUNE_NONE)} vs Wikipedia {sorted(WIKI_NONE)}")
    assert FSYMBOLS_NONE <= WIKI_NONE, (
        f"witness parting in the dash column: fsymbols marks "
        f"{sorted(FSYMBOLS_NONE - WIKI_NONE)} valueless where "
        f"Wikipedia seats a value")
    for name, exhibits in (('Satzinger', SATZINGER_EXHIBITS),
                           ('Isaac', ISAAC_EXHIBITS)):
        for letter, val in exhibits.items():
            assert WIKI[letter] == val, (
                f"{name} exhibit parting at {letter}: {val} vs "
                f"{WIKI[letter]}")
    table = {}
    for upper, _, _, _, _ in ROWS:
        table[upper] = WIKI.get(upper)  # None where the dash stands
    return table


def build_table(table):
    """The frozen transcription: 27 SOURCED rows + 7 NO VALUE rows.

    MECHANISM: every glyph pair is verified against the Unicode
    standard: the small letter stands at capital + 1 at every row
    (the Coptic block's pairs, the Greek block's Demotic pairs, and
    sampi's pair alike — the standard's own arithmetic for this
    script), and every Unicode name is read from the standard and
    carried on the row, the small's name the capital's with SMALL
    for CAPITAL. A glyph failing its codepoint or name check aborts
    the build.
    """
    rows = []
    for pos, (upper, lower, tr, geq, origin) in enumerate(ROWS, start=1):
        assert ord(lower) == ord(upper) + 1, (
            f"case-pair check failed at row {pos}: {upper} {lower}")
        un = glyph_name(upper)
        ln = glyph_name(lower)
        assert un.startswith('COPTIC CAPITAL LETTER'), (
            f"name check failed at {upper}: {un!r}")
        assert ln == un.replace('CAPITAL', 'SMALL'), (
            f"case-name check failed at {lower}: {ln!r} vs {un!r}")
        val = table[upper]
        rows.append({
            'position': pos, 'uppercase': upper, 'lowercase': lower,
            'letter_name': un.replace('COPTIC CAPITAL LETTER ', ''),
            'transliteration': tr, 'greek_equivalent': geq,
            'origin': origin,
            'uppercase_codepoint': f'U+{ord(upper):04X}',
            'lowercase_codepoint': f'U+{ord(lower):04X}',
            'uppercase_unicode_name': un, 'lowercase_unicode_name': ln,
            'value': '' if val is None else val,
            'value_class': '' if val is None else value_class(val),
            'source': SOURCE_NOTE,
            'status': 'NO VALUE' if val is None else 'SOURCED',
        })
    return rows


# -- The descent: the verified table read against the Greek bank ----------------
# DOCTRINE: the Greek side is transcribed here from the engine's
# living GREEK bank (pontifex/tables.py, read at build time): value
# seat → the bank's sign(s) at that value. The companion battery
# holds this transcription against the living bank imported fresh,
# so the descent page can never drift from the engine it describes.
# The bank carries 28 keys at 27 values: σ and ς share 200 (one
# letter, two forms), and 'στ' shares 6 with ϛ (a digraph key — the
# engine's weighing convenience for the stigma's written form).
GREEK_SEATS = {
    1: 'α', 2: 'β', 3: 'γ', 4: 'δ', 5: 'ε', 6: 'ϛ', 7: 'ζ', 8: 'η',
    9: 'θ', 10: 'ι', 20: 'κ', 30: 'λ', 40: 'μ', 50: 'ν', 60: 'ξ',
    70: 'ο', 80: 'π', 90: 'ϟ', 100: 'ρ', 200: 'σ', 300: 'τ',
    400: 'υ', 500: 'φ', 600: 'χ', 700: 'ψ', 800: 'ω', 900: 'ϡ',
}
# MECHANISM: the Coptic seat at each value (small letters — the
# citation case of the witnesses' number sequences).
COPTIC_SEATS = {
    1: 'ⲁ', 2: 'ⲃ', 3: 'ⲅ', 4: 'ⲇ', 5: 'ⲉ', 6: 'ⲋ', 7: 'ⲍ', 8: 'ⲏ',
    9: 'ⲑ', 10: 'ⲓ', 20: 'ⲕ', 30: 'ⲗ', 40: 'ⲙ', 50: 'ⲛ', 60: 'ⲝ',
    70: 'ⲟ', 80: 'ⲡ', 90: 'ϥ', 100: 'ⲣ', 200: 'ⲥ', 300: 'ⲧ',
    400: 'ⲩ', 500: 'ⲫ', 600: 'ⲭ', 700: 'ⲯ', 800: 'ⲱ', 900: 'ⳁ',
}

AGREE = ('AGREE — same value, and the Coptic sign is the Greek '
         'letter\'s own heir: descent preserved the seat entire')
SPECIAL = {
    6: ('AGREE in value — PART in kind: the epissemon seat. Greek '
        'ϛ (stigma) is a numeral sign, not a living letter; Coptic '
        'ⲋ (sou) is likewise "not used as a letter, but as a '
        'numeral" (Isaac). The seat kept a SIGN on both banks — '
        'descent preserved even the seat\'s numeral-only standing.'),
    90: ('AGREE in value — PART IN LINEAGE, the descent\'s one '
         'seat-change: Greek ϟ (koppa) is an archaic letter, dead '
         'in words; Coptic seats ϥ (fai), a LIVING Demotic letter '
         '(/f/, in ordinary words), at koppa\'s value. W1 marks '
         'the equivalence "(numerical value)" — the kinship is '
         'the seat, not the glyph. The grid\'s one vacancy (a '
         'holder dead as a letter) is the one seat a native '
         'letter took.'),
    900: ('AGREE in value — PART in kind: Greek ϡ (sampi) is an '
          'archaic numeral sign; Coptic Ⳁ is the same sign '
          'descended into the Coptic block (Unicode name: COPTIC '
          'CAPITAL LETTER SAMPI), marked "(numerical value)" by '
          'W1. A numeral sign on both banks; a letter of neither '
          'living alphabet — Isaac\'s 31-letter list does not '
          'count it.'),
    200: ('AGREE in value — PART in form: the Greek bank carries '
          'two glyphs at this seat, σ and its word-final form ς; '
          'Coptic ⲥ is one letter with no final-form split (W1\'s '
          'equivalent column prints "Σ, σ, ς" against the one '
          'Coptic row). The value descends entire; the form '
          'distinction does not.'),
}


def build_descent(table):
    """The descent read seat by seat — boundaries, not blobs.

    MECHANISM: one row per Milesian value (27): the Greek bank's
    sign, the Coptic sign, both verified against their seats (the
    Coptic side against this build's verified table); the relation
    column states the agreement or the parting at that seat.
    Summary rows then carry the partings of kind: the digraph, the
    unseated natives, the thousands devices, the total.
    """
    by_small = {}
    for upper, lower, _, _, _ in ROWS:
        if table[upper] is not None:
            by_small[lower] = table[upper]
    rows = []
    for value in sorted(GREEK_SEATS):
        g = GREEK_SEATS[value]
        c = COPTIC_SEATS[value]
        assert by_small[c] == value, (
            f"descent seat mismatch at {value}: Coptic {c} weighs "
            f"{by_small.get(c)} in the verified table")
        rows.append({
            'value': value, 'greek_sign': g,
            'greek_name': glyph_name(g), 'coptic_sign': c,
            'coptic_name': glyph_name(c),
            'relation': SPECIAL.get(value, AGREE), 'note': '',
        })
    rows.append({
        'value': 'DIGRAPH', 'greek_sign': 'στ', 'greek_name': '',
        'coptic_sign': '', 'coptic_name': '',
        'relation': 'PART — an engine artifact, not a descent fact',
        'note': ('The Greek bank carries a second key at 6: \'στ\', '
                 'the stigma\'s written digraph form, a weighing '
                 'convenience of the engine. Coptic has no '
                 'counterpart key and needs none — sou is one '
                 'glyph. The parting is between the engine\'s '
                 'Greek apparatus and the Coptic seat, not between '
                 'the traditions.'),
    })
    rows.append({
        'value': 'NATIVE', 'greek_sign': '', 'greek_name': '',
        'coptic_sign': 'ϣ ϧ ⳉ ϩ ϫ ϭ ϯ', 'coptic_name': '',
        'relation': 'NO SEAT — the letters descent could not seat',
        'note': ('The Demotic letters beyond fai — shai, khai (both '
                 'dialectal glyphs), hori, djanja, shima, ti — '
                 'carry NO value in any witness read: the witnesses\' '
                 'dash is unanimous. The Milesian grid arrived '
                 'FULL (9/9/9 seats held); there was no vacant seat '
                 'for a native letter to take except the one whose '
                 'holder was dead (90). What the inheritance bought '
                 'the language — a complete numeral system — is '
                 'exactly what its own letters could not enter.'),
    })
    rows.append({
        'value': 'THOUSANDS', 'greek_sign': '', 'greek_name': '',
        'coptic_sign': '', 'coptic_name': '',
        'relation': 'PART of practice — devices, never letter values',
        'note': ('Beyond 900 the witnesses show MARKS, not values: '
                 'W1 (§Macrons and overlines, citing the Unicode '
                 'Standard §7.3): ⲁ͵ = 1,000 (the numeral sign '
                 'U+0375, Greek practice inherited) and the double '
                 'overline U+033F (ⲁ̿ = 1,000), with the worked '
                 'example ⲁ͵ⲱ̅ⲡ̅ⲏ̅ = 1,888. Satzinger prints a '
                 'different device: a stauros sign at 1000, '
                 '"Number only". Two devices in the record, both '
                 'marks or symbols; no letter carries a thousands '
                 'value in any source. Neither is seated; the '
                 'engine\'s door counts marks and prices none.'),
    })
    rows.append({
        'value': 'TOTAL', 'greek_sign': '', 'greek_name': '',
        'coptic_sign': '', 'coptic_name': '',
        'relation': 'VALUE AGREEMENT TOTAL on the measured domain',
        'note': ('All 27 Milesian value seats stand in Coptic at '
                 'the same values: the value SETS of the two banks '
                 'are identical, seat for seat. The partings are '
                 'never of value — they are of kind (6, 900: sign '
                 'for sign), of lineage (90: a living native '
                 'letter for a dead Greek one), and of form (200: '
                 'two glyphs for one). Descent preserved the '
                 'numbers entire and altered the holders at '
                 'exactly three seats.'),
    })
    return rows


def write_csv(filename, rows, fieldnames):
    path = os.path.join(HERE, filename)
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    return path


def main():
    # MECHANISM: witness diff first — the table exists only if the
    # witnesses agree; then calibration: the witnesses' own worked
    # examples must recompute exact before any derived number is
    # trusted (W1's ⲫ = 500; W2's 12 and 365; the letter part of
    # W1's 1,888).
    table = diff_witnesses()
    print("WITNESS DIFF — Wikipedia 'Coptic script' vs fsymbols vs "
          "tooldune: 27/27 valued cells agree; the dash column "
          "agrees (7 signs, tooldune == Wikipedia; fsymbols' 6 a "
          "subset); Satzinger's 26 exhibited seats and Isaac's 1 "
          "agree")
    by_small = {lower: table[upper] for upper, lower, _, _, _ in ROWS
                if table[upper] is not None}

    def weigh_str(s):
        return sum(by_small[c] for c in s)

    assert weigh_str('ⲫ') == 500, "calibration failed: ⲫ"
    assert weigh_str('ⲓⲃ') == 12, "calibration failed: ⲓⲃ"
    assert weigh_str('ⲧⲝⲉ') == 365, "calibration failed: ⲧⲝⲉ"
    assert weigh_str('ⲱⲡⲏ') == 888, "calibration failed: ⲱⲡⲏ"
    print("CALIBRATION OK — ⲫ = 500 (W1's example); ⲓⲃ = 12 and "
          "ⲧⲝⲉ = 365 (W2's examples); ⲱⲡⲏ = 888 (the letter part "
          "of W1's 1,888, recomputed)")

    rows = build_table(table)
    descent = build_descent(table)
    write_csv('coptic-table.csv', rows,
              ['position', 'uppercase', 'lowercase', 'letter_name',
               'transliteration', 'greek_equivalent', 'origin',
               'uppercase_codepoint', 'lowercase_codepoint',
               'uppercase_unicode_name', 'lowercase_unicode_name',
               'value', 'value_class', 'source', 'status'])
    write_csv('coptic-descent.csv', descent,
              ['value', 'greek_sign', 'greek_name', 'coptic_sign',
               'coptic_name', 'relation', 'note'])

    total = sum(v for v in table.values() if v is not None)
    print(f"TABLE — 27 signs SOURCED with values (three classes of "
          f"nine; sum of all values {total}); 7 rows NO VALUE "
          f"(Ϣ Ϧ Ⳉ Ϩ Ϫ Ϭ Ϯ — the witnesses' dash, unanimous)")
    print("DESCENT — value agreement vs the Greek Milesian bank "
          "TOTAL at 27/27 seats; partings of kind at 6 and 900, "
          "of lineage at 90, of form at 200 — coordinates in "
          "coptic-descent.csv")
    print("CSVs written beside this script. Findings, never doctrine. 93.")


if __name__ == '__main__':
    main()
