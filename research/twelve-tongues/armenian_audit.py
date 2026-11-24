#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — armenian_audit.py — the Armenian Phase I audit: data builder
# Companion to armenian.md (the Twelve-Tongues sweep, Worker #11) and to
# THE-ARMENIAN-TABLE-PHASE-I-AUDIT.md (the audit document of record).
#
# Epigraph: "There was no notation for zero in the old system, and the
# numeric values for individual letters were added together." —
# Wikipedia, "Armenian numerals" (the system's own shape, in one line).
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
#   Hypothesis: (i) the classical Armenian numeral table — the 36 letters
#     of Mashtots' alphabet at the decimal class values — can be re-sourced
#     sign by sign from independent witnesses that agree entire, and every
#     cell verified against the Unicode standard and the class law the
#     table obeys; (ii) set beside the Ge'ez halehame at coordinates, the
#     two class laws will show exactly where same-shaped systems agree
#     and where they part — the control case the founder ordered.
#   Method: (1) transcribe the table from THREE witnesses read entire on
#     2026-11-24 (Wikipedia, "Armenian numerals"; Omniglot, "Numbers in
#     Armenian"; Wikipedia, "Armenian alphabet", its Numerical value
#     column) and diff them cell by cell in code — a disagreement aborts
#     the build as a finding, never averages away; (2) hold a fourth
#     witness (the MELA cataloging manual) to the cells its worked
#     examples exhibit; (3) generate every glyph's codepoints by the
#     standard's own arithmetic (capitals U+0531–U+0554 consecutive,
#     lowercase at +0x30) and verify each Unicode name; (4) recompute
#     the witnesses' worked examples before trusting any derived number.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Armenian Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The values below are
TRANSCRIPTIONS of a published, attested table, carried with their sources
on their face; the control-case table is a comparison at coordinates, not
a verdict. No value here is presented as the house's doctrine, and no row
enters pontifex/engine.py from this file — the seat, if the gate holds,
is built separately in Phase II and proven against the CSV this builder
freezes.

MECHANISM: two CSVs are written beside this script —
  armenian-table.csv         the 36 classical letters at their values
                             (status SOURCED), each row carrying its
                             codepoints and Unicode names as the
                             verification witness, plus 2 OPEN rows for
                             the medieval additions (օ, ֆ), which carry
                             NO seated value — the boundary, in data;
  armenian-control-case.csv  Armenian vs halehame per position 1–26
                             (value, class, relation per row), plus the
                             extent / coverage / extension / zero rows
                             where the two systems part in kind.
The companion battery armenian_audit_tests.py re-derives every number
the audit document prints from these CSVs and from its own independent
source constants.
"""

import csv
import os
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- The classical alphabet, in Mashtots' order --------------------------------
# DOCTRINE: the audit seats the CLASSICAL inventory — the 36 letters of
# the original alphabet (Mashtots, c. 405 CE) — because the numeral table
# is coextensive with exactly these: every classical letter carries a
# value, and no other letter does at the classical tier. The two medieval
# additions stand in LATE below, unseated, as the audit's boundary.
# MECHANISM: (uppercase, lowercase, letter name, classical
# transliteration). The order is the alphabet's own order, which is also
# the numeral order — position in this list IS the audit's coordinate.
CLASSICAL = [
    ('Ա', 'ա', 'Ayb', 'a'), ('Բ', 'բ', 'Ben', 'b'),
    ('Գ', 'գ', 'Gim', 'g'), ('Դ', 'դ', 'Da', 'd'),
    ('Ե', 'ե', 'Yech', 'e'), ('Զ', 'զ', 'Za', 'z'),
    ('Է', 'է', 'Eh', 'ē'), ('Ը', 'ը', 'Et', 'ə'),
    ('Թ', 'թ', 'To', "t'"), ('Ժ', 'ժ', 'Zhe', 'ž'),
    ('Ի', 'ի', 'Ini', 'i'), ('Լ', 'լ', 'Liwn', 'l'),
    ('Խ', 'խ', 'Khe', 'x'), ('Ծ', 'ծ', 'Tsa', 'c'),
    ('Կ', 'կ', 'Ken', 'k'), ('Հ', 'հ', 'Ho', 'h'),
    ('Ձ', 'ձ', 'Dza', 'j'), ('Ղ', 'ղ', 'Ghat', 'ġ'),
    ('Ճ', 'ճ', 'Che', 'č'), ('Մ', 'մ', 'Men', 'm'),
    ('Յ', 'յ', 'Yi', 'y'), ('Ն', 'ն', 'Nu', 'n'),
    ('Շ', 'շ', 'Sha', 'š'), ('Ո', 'ո', 'O', 'o'),
    ('Չ', 'չ', 'Cha', "č'"), ('Պ', 'պ', 'Pe', 'p'),
    ('Ջ', 'ջ', 'Je', 'ǰ'), ('Ռ', 'ռ', 'Ra', 'ṙ'),
    ('Ս', 'ս', 'Se', 's'), ('Վ', 'վ', 'Vew', 'v'),
    ('Տ', 'տ', 'Tiwn', 't'), ('Ր', 'ր', 'Re', 'r'),
    ('Ց', 'ց', 'Tso', "c'"), ('Ւ', 'ւ', 'Hiwn', 'w'),
    ('Փ', 'փ', 'Piwr', "p'"), ('Ք', 'ք', 'Ke', "k'"),
]

# -- The medieval additions: the boundary, in data ------------------------------
# DOCTRINE: օ and ֆ were added to the alphabet in the Middle Ages (the
# alphabet article's lead: "two more were adopted in the 13th century"),
# after Arabic numerals were already in use. The numerals article: they
# "sometimes have a numerical value assigned to them" (10000 / 20000).
# The alphabet article's own table prints NO numerical value for either.
# That is a weaker attestation than any of the 36, and the audit does
# not seat them: they stand here as OPEN rows — the question of their
# values is the founder's pen, not this audit's finding.
LATE = [
    ('Օ', 'օ', 'Oh', 'ô', 10000),
    ('Ֆ', 'ֆ', 'Feh', 'f', 20000),
]

# -- The witnesses, transcribed independently -----------------------------------
# DOCTRINE: three witnesses read entire on 2026-11-24 print the table;
# each transcription below was taken from its own page, and the builder
# diffs them cell by cell. WIKI_NUMERALS is the dedicated article's
# table; OMNIGLOT is the bracketed majuscules beside its number list;
# WIKI_ALPHABET is the alphabet article's "Numerical value" column.
# A cell where any witness parts from the others aborts the build.
WIKI_NUMERALS = {
    'Ա': 1, 'Բ': 2, 'Գ': 3, 'Դ': 4, 'Ե': 5, 'Զ': 6, 'Է': 7, 'Ը': 8,
    'Թ': 9, 'Ժ': 10, 'Ի': 20, 'Լ': 30, 'Խ': 40, 'Ծ': 50, 'Կ': 60,
    'Հ': 70, 'Ձ': 80, 'Ղ': 90, 'Ճ': 100, 'Մ': 200, 'Յ': 300, 'Ն': 400,
    'Շ': 500, 'Ո': 600, 'Չ': 700, 'Պ': 800, 'Ջ': 900, 'Ռ': 1000,
    'Ս': 2000, 'Վ': 3000, 'Տ': 4000, 'Ր': 5000, 'Ց': 6000, 'Ւ': 7000,
    'Փ': 8000, 'Ք': 9000,
}
OMNIGLOT = {
    'Ա': 1, 'Բ': 2, 'Գ': 3, 'Դ': 4, 'Ե': 5, 'Զ': 6, 'Է': 7, 'Ը': 8,
    'Թ': 9, 'Ժ': 10, 'Ի': 20, 'Լ': 30, 'Խ': 40, 'Ծ': 50, 'Կ': 60,
    'Հ': 70, 'Ձ': 80, 'Ղ': 90, 'Ճ': 100, 'Մ': 200, 'Յ': 300, 'Ն': 400,
    'Շ': 500, 'Ո': 600, 'Չ': 700, 'Պ': 800, 'Ջ': 900, 'Ռ': 1000,
    'Ս': 2000, 'Վ': 3000, 'Տ': 4000, 'Ր': 5000, 'Ց': 6000, 'Ւ': 7000,
    'Փ': 8000, 'Ք': 9000,
}
WIKI_ALPHABET = {
    'Ա': 1, 'Բ': 2, 'Գ': 3, 'Դ': 4, 'Ե': 5, 'Զ': 6, 'Է': 7, 'Ը': 8,
    'Թ': 9, 'Ժ': 10, 'Ի': 20, 'Լ': 30, 'Խ': 40, 'Ծ': 50, 'Կ': 60,
    'Հ': 70, 'Ձ': 80, 'Ղ': 90, 'Ճ': 100, 'Մ': 200, 'Յ': 300, 'Ն': 400,
    'Շ': 500, 'Ո': 600, 'Չ': 700, 'Պ': 800, 'Ջ': 900, 'Ռ': 1000,
    'Ս': 2000, 'Վ': 3000, 'Տ': 4000, 'Ր': 5000, 'Ց': 6000, 'Ւ': 7000,
    'Փ': 8000, 'Ք': 9000,
}
# MECHANISM: the fourth witness — the MELA cataloging manual ("Armenian
# Numerals and Dates", Middle East Librarians Association) — prints its
# table as an image, but its worked examples are text, and they exhibit
# twelve letters' values: ՌՋՀԵ = 1975, ՍՄԻԲ = 2222, ՍԴ = 2004, ՃԻ = 120,
# Ծ = 50, and the era date ԹՎ ՌՆԾԵ = "in the year 1455". Every value it
# exhibits must agree with the table or the disagreement is a finding.
MELA_EXHIBITS = {
    'Ռ': 1000, 'Ջ': 900, 'Հ': 70, 'Ե': 5, 'Ս': 2000, 'Մ': 200,
    'Ի': 20, 'Բ': 2, 'Դ': 4, 'Ճ': 100, 'Ծ': 50, 'Ն': 400,
}

SOURCE_NOTE = ("Wikipedia, 'Armenian numerals' (table read entire "
               "2026-11-24; citing Omniglot; Shaw 1939; Ifrah 2000; "
               "Chrisomalis 2010, pp. 175–177); Omniglot, 'Numbers in "
               "Armenian' (read entire 2026-11-24); Wikipedia, "
               "'Armenian alphabet', Numerical value column (read "
               "2026-11-24); MELA cataloging manual, 'Armenian "
               "Numerals and Dates' (worked examples, read 2026-11-24)")


def class_formula(position):
    """The class law the table obeys — a check, never the source.

    MECHANISM: the 36 letters run in four decimal classes of nine:
    positions 1–9 units, 10–18 tens, 19–27 hundreds, 28–36 thousands;
    value = digit x 10^class, digit = ((position-1) mod 9) + 1.
    The same architecture as the Greek Milesian table, on an
    independent letter mapping (the sweep's §5 finding, re-verified
    here cell by cell against the witnesses, not inherited from it).
    """
    return (((position - 1) % 9) + 1) * (10 ** ((position - 1) // 9))


def class_name(position):
    return ('units', 'tens', 'hundreds', 'thousands')[(position - 1) // 9]


def glyph_name(ch):
    """Unicode name of a glyph, or '' if unassigned — the build's witness."""
    try:
        return ud.name(ch)
    except ValueError:
        return ''


def diff_witnesses():
    """Diff the three full-table witnesses cell by cell; return the table.

    MECHANISM: the seated value of each letter is WIKI_NUMERALS'; the
    other two witnesses and MELA's exhibits are held against it. Any
    parting raises — the audit prints disagreements as coordinates in
    its document; it never lets one pass silently in its data.
    """
    table = {}
    for upper, _, _, _ in CLASSICAL:
        a = WIKI_NUMERALS[upper]
        assert OMNIGLOT[upper] == a, (
            f"witness parting at {upper}: Omniglot {OMNIGLOT[upper]} "
            f"vs numerals article {a}")
        assert WIKI_ALPHABET[upper] == a, (
            f"witness parting at {upper}: alphabet article "
            f"{WIKI_ALPHABET[upper]} vs numerals article {a}")
        table[upper] = a
    for letter, val in MELA_EXHIBITS.items():
        assert table[letter] == val, (
            f"MELA exhibit parting at {letter}: {val} vs {table[letter]}")
    return table


def build_table(table):
    """The frozen transcription: 36 SOURCED rows + 2 OPEN rows.

    MECHANISM: codepoints are verified by the standard's own arithmetic
    — the classical capitals occupy U+0531–U+0554 consecutively in
    alphabet order, each lowercase at capital + 0x30 — and every glyph's
    Unicode name is read from the standard and carried on the row.
    A glyph failing its codepoint or name check aborts the build.
    """
    rows = []
    for pos, (upper, lower, name, tr) in enumerate(CLASSICAL, start=1):
        assert ord(upper) == 0x531 + pos - 1, (
            f"codepoint check failed at position {pos}: {upper}")
        assert ord(lower) == ord(upper) + 0x30, (
            f"case-pair check failed at position {pos}: {lower}")
        un = glyph_name(upper)
        ln = glyph_name(lower)
        assert un.startswith('ARMENIAN CAPITAL LETTER'), (
            f"name check failed at {upper}: {un!r}")
        assert ln == un.replace('CAPITAL', 'SMALL'), (
            f"case-name check failed at {lower}: {ln!r} vs {un!r}")
        val = table[upper]
        assert val == class_formula(pos), (
            f"class law failed at position {pos}: {val} vs "
            f"{class_formula(pos)}")
        rows.append({
            'position': pos, 'uppercase': upper, 'lowercase': lower,
            'letter_name': name, 'transliteration': tr,
            'uppercase_codepoint': f'U+{ord(upper):04X}',
            'lowercase_codepoint': f'U+{ord(lower):04X}',
            'uppercase_unicode_name': un, 'lowercase_unicode_name': ln,
            'value': val, 'value_class': class_name(pos),
            'source': SOURCE_NOTE, 'status': 'SOURCED',
        })
    for i, (upper, lower, name, tr, sometimes) in enumerate(LATE, start=37):
        un = glyph_name(upper)
        ln = glyph_name(lower)
        assert un.startswith('ARMENIAN CAPITAL LETTER'), (
            f"name check failed at {upper}: {un!r}")
        assert ln == un.replace('CAPITAL', 'SMALL'), (
            f"case-name check failed at {lower}: {ln!r}")
        rows.append({
            'position': i, 'uppercase': upper, 'lowercase': lower,
            'letter_name': name, 'transliteration': tr,
            'uppercase_codepoint': f'U+{ord(upper):04X}',
            'lowercase_codepoint': f'U+{ord(lower):04X}',
            'uppercase_unicode_name': un, 'lowercase_unicode_name': ln,
            'value': '', 'value_class': '',
            'source': ("medieval addition (13th c. per the alphabet "
                       "article); the numerals article: 'sometimes' "
                       f"assigned {sometimes}; the alphabet article's "
                       "table prints no numerical value. NOT seated — "
                       "the founder's pen."),
            'status': 'OPEN',
        })
    return rows


# -- The control case: Armenian beside halehame ---------------------------------
# DOCTRINE: the halehame side is stated exactly as the Ge'ez instruments
# established it (Phase I audit + Phase II–III): 26 first-form values in
# halehame order — units at positions 1–10 (the Semitic run, ተ = 10 a
# units letter), tens at 11–19, hundreds at 20–26; the printed grid's
# order-multiplier reaching 5600 at ፐ order 7; coverage 26 first forms
# of 202 classical signs; antiquity undated; register folk-magical.
HALEHAME_BASES = ['ሀ', 'ለ', 'ሐ', 'መ', 'ሠ', 'ረ', 'ሰ', 'ቀ', 'በ', 'ተ',
                  'ኀ', 'ነ', 'አ', 'ከ', 'ወ', 'ዐ', 'ዘ', 'የ', 'ደ', 'ገ',
                  'ጠ', 'ጰ', 'ጸ', 'ፀ', 'ፈ', 'ፐ']
HALEHAME_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   20, 30, 40, 50, 60, 70, 80, 90, 100,
                   200, 300, 400, 500, 600, 700, 800]


def folk_formula(position):
    """The halehame class law, as the Ge'ez Phase I audit established it."""
    if position <= 10:
        return position
    if position <= 19:
        return (position - 9) * 10
    return (position - 18) * 100


def folk_class(position):
    return 'units' if position <= 10 else 'tens' if position <= 19 \
        else 'hundreds'


def build_control_case(table):
    """Armenian vs halehame at coordinates — boundaries, not blobs.

    MECHANISM: one row per shared position (1–26), each side's value
    recomputed from its own class formula and held against its
    transcription; the relation column states the agreement or the
    parting at that coordinate. Summary rows then carry the partings
    of kind: extent, coverage, extension, zero.
    """
    rows = []
    arm_letters = [u for u, _, _, _ in CLASSICAL]
    for pos in range(1, 27):
        av = table[arm_letters[pos - 1]]
        hv = HALEHAME_VALUES[pos - 1]
        assert av == class_formula(pos) and hv == folk_formula(pos)
        if pos <= 9:
            rel = 'AGREE — same value, same units law (value = position)'
        elif pos == 10:
            rel = ('AGREE in value (10 = 10) — PART in law: Armenian '
                   'reaches 10 by the class step (Ժ, first tens letter, '
                   '1 x 10); halehame reaches it inside the units run '
                   '(ተ, tenth units letter). THE BOUNDARY COORDINATE: '
                   'total value agreement, first law parting')
        elif pos <= 18:
            rel = ('AGREE in value — class membership offset by one '
                   'seat: Armenian tens run 10–18, halehame tens 11–19')
        elif pos == 19:
            rel = ('AGREE in value (100 = 100) — THE HINGE: Armenian\'s '
                   'first hundreds letter (Ճ) is halehame\'s last tens '
                   'letter (ደ)')
        else:
            rel = ('AGREE in value — Armenian hundreds run 19–27, '
                   'halehame hundreds 20–26')
        rows.append({
            'position': pos, 'armenian_letter': arm_letters[pos - 1],
            'armenian_value': av, 'armenian_class': class_name(pos),
            'halehame_base': HALEHAME_BASES[pos - 1],
            'halehame_value': hv, 'halehame_class': folk_class(pos),
            'relation': rel, 'note': '',
        })
    rows.append({
        'position': 'EXTENT', 'armenian_letter': '', 'armenian_value': '',
        'armenian_class': '', 'halehame_base': '', 'halehame_value': '',
        'halehame_class': '', 'relation': 'PART — extent',
        'note': ('Armenian: four classes over 36 seats, maximum letter '
                 'value 9000 (Ք), maximum writable number 9999. '
                 'Halehame: three classes over 26 seats, maximum '
                 'first-form value 800 (ፐ). Armenian positions 27–36 '
                 '(Ջ 900; Ռ–Ք 1000–9000) have no halehame counterpart.'),
    })
    rows.append({
        'position': 'COVERAGE', 'armenian_letter': '',
        'armenian_value': '', 'armenian_class': '', 'halehame_base': '',
        'halehame_value': '', 'halehame_class': '',
        'relation': 'PART — coverage against the whole script',
        'note': ('Armenian values 36 of 36 classical letters — the '
                 'whole classical alphabet is the table (the 2 medieval '
                 'additions stand outside it, OPEN). Halehame values '
                 '26 first forms of 202 classical signs (26/202); its '
                 'labiovelar columns and later-added bases carry no '
                 'value in any source.'),
    })
    rows.append({
        'position': 'EXTENSION', 'armenian_letter': '',
        'armenian_value': '', 'armenian_class': '', 'halehame_base': '',
        'halehame_value': '', 'halehame_class': '',
        'relation': 'PART — the axis beyond the table',
        'note': ('Armenian extends by MORE LETTERS (the thousands '
                 'class) and by the OVERLINE: a line over a letter '
                 'multiplies it — by 10,000 per Wikipedia and MELA '
                 '(overlined Ա = 10,000; overlined Ջ = 9,000,000), by '
                 '1,000 per Omniglot (overlined Ժ = 10,000; overlined '
                 'Ռ = 1,000,000). THE FACTOR IS DISPUTED IN THE '
                 'SOURCES; neither is implemented. Halehame extends '
                 'by the ORDER MULTIPLIER: a form at order n at n x '
                 'its base, the printed grid reaching 5600 — printed '
                 'entire, its use unexhibited.'),
    })
    rows.append({
        'position': 'ZERO', 'armenian_letter': '', 'armenian_value': '',
        'armenian_class': '', 'halehame_base': '', 'halehame_value': '',
        'halehame_class': '', 'relation': 'AGREE — the zero coordinate',
        'note': ('Neither table has a zero: Armenian — "There is no '
                 'symbol for zero" (Wikipedia, on its face); missing '
                 'powers are simply not written. Halehame — no zero '
                 'value in the folk table. Both are zero-less additive '
                 'systems.'),
    })
    rows.append({
        'position': 'ATTESTATION', 'armenian_letter': '',
        'armenian_value': '', 'armenian_class': '', 'halehame_base': '',
        'halehame_value': '', 'halehame_class': '',
        'relation': 'PART — attestation depth (the control case itself)',
        'note': ('Armenian: the designed alphabet\'s own numeral '
                 'system, in manuscript use for era dating in '
                 'colophons (MELA documents the practice; era epoch '
                 'AD 552, years written ԹՎ + numerals) — three modern '
                 'witnesses read entire agree on all 36 cells, a '
                 'scholarly manual\'s examples agree on the 12 cells '
                 'they exhibit. Halehame: a living folk-magical '
                 'enumeration, published modernly, antiquity undated '
                 'in every source, register expressly not liturgical. '
                 'Same class-law shape; opposite attestation depth.'),
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
    # example must recompute exact before any derived number is trusted.
    table = diff_witnesses()
    print("WITNESS DIFF — Wikipedia 'Armenian numerals' vs Omniglot vs "
          "Wikipedia 'Armenian alphabet': 36/36 cells agree; MELA's 12 "
          "exhibited cells agree")
    ex1975 = sum(table[c] for c in 'ՌՋՀԵ')
    assert ex1975 == 1975, f"calibration failed: ՌՋՀԵ = {ex1975}"
    print(f"CALIBRATION OK — ՌՋՀԵ = {ex1975} (both Wikipedia's and "
          f"MELA's worked example, recomputed)")

    rows = build_table(table)
    cc = build_control_case(table)
    write_csv('armenian-table.csv', rows,
              ['position', 'uppercase', 'lowercase', 'letter_name',
               'transliteration', 'uppercase_codepoint',
               'lowercase_codepoint', 'uppercase_unicode_name',
               'lowercase_unicode_name', 'value', 'value_class',
               'source', 'status'])
    write_csv('armenian-control-case.csv', cc,
              ['position', 'armenian_letter', 'armenian_value',
               'armenian_class', 'halehame_base', 'halehame_value',
               'halehame_class', 'relation', 'note'])

    total = sum(table[u] for u, _, _, _ in CLASSICAL)
    print(f"TABLE — 36 classical letters SOURCED (4 classes of 9; "
          f"sum of all values {total}); 2 OPEN rows (Օ, Ֆ — no seated "
          f"value)")
    agree = sum(1 for p in range(1, 27)
                if class_formula(p) == folk_formula(p))
    print(f"CONTROL CASE — value agreement Armenian vs halehame at "
          f"{agree}/26 shared positions; law parting at position 10 "
          f"(value 10 = 10, derivation parts); extent parts at "
          f"position 27")
    print("CSVs written beside this script. Findings, never doctrine. 93.")


if __name__ == '__main__':
    main()
