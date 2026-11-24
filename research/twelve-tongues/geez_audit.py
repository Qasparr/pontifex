#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — geez_audit.py — the Ge'ez Phase I audit: data builder + replay
# Companion to geez.md (the Twelve-Tongues sweep, Worker #10) and to
# THE-GEEZ-TABLES-PHASE-I-AUDIT.md (the audit document of record).
#
# Epigraph: "Seemingly as if the pre-syllabic Ge'ez was somehow more
# meaningful in the practice." — geez.org, "Numerology" (on the Debtera
# enumeration's first-form law).
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
#   Hypothesis: (i) the classical Ge'ez inventory is a closed grid — 26
#     halehame bases x 7 orders = 182 signs, extended by the tongue's own
#     fusion devices (4 labiovelar series x 5 = 20; an 8th slot) — and
#     every count can be recomputed from the Unicode standard rather than
#     trusted from prose; (ii) the Debtera (halehame) enumeration the sweep
#     reported can be re-sourced sign-for-sign from its published table
#     and its worked example recomputed exact.
#   Method: (1) transcribe the halehame bases and folk values from the
#     geez.org "Numerology" table as actually read (2026-11-24), checked
#     against the class formula the table itself obeys; (2) generate every
#     grid glyph by codepoint arithmetic from each base's first form and
#     verify each glyph's Unicode name carries the expected order token —
#     a glyph that fails its name is a finding, not a rounding; (3) emit
#     the inventory, the folk values, the Nine seating design and the
#     zero-point table as CSVs; (4) recompute the tradition's own worked
#     example (ክርስቶስ = 80) before trusting a single derived number.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Ge'ez Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The halehame values
below are a TRANSCRIPTION of a published folk table (geez.org, "Numerology",
Debtera (Halehame) Enumeration), carried with its source on its face; the
inventory is generated from the Unicode standard; the Nine seating is a
DESIGN, tiered row by row in geez-nine-seating.csv. No value here is
presented as the house's doctrine, and no row enters pontifex/engine.py.

MECHANISM: four CSVs are written beside this script —
  geez-fidal-inventory.csv   every seated/inventoried glyph at its grid
                             coordinate (base x order), with its codepoint
                             and Unicode name as the verification witness;
  geez-halehame-values.csv   the folk values per base, plus explicit GAP
                             rows for the classes the folk table does not
                             reach (labiovelars, later-added bases);
  geez-nine-seating.csv      the Divine Nine seated on the grid: 7 orders
                             by sound + 2 hybrid stations, reasoning and
                             tier on every row;
  geez-zero-point.csv        folk value vs grid position per base, with
                             the agreement/disagreement relation printed
                             per row — coordinates, not a verdict blob.
The companion battery geez_audit_tests.py re-derives every number the
audit document prints from these CSVs and from source constants.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))

# -- The halehame order: the 26 classical bases -------------------------------
# DOCTRINE: the audit seats the CLASSICAL Ge'ez inventory — the 26 bases in
# halehame order — because (a) the audit's subject is Ge'ez the liturgical
# tongue, not its Amharic heir; (b) the folk table under audit enumerates
# exactly these 26 and no others; (c) the count is triple-sourced (geez.org
# table rows; geezonline FAQ "26 common consonants"; Unicode guide "26 base
# consonants (the traditional Ge'ez set)"). The Amharic-extended counts are
# printed in the audit document as coordinates, not seated.
# MECHANISM: (first-form glyph, traditional letter name, transliteration).
HALEHAME_BASES = [
    ('ሀ', 'Hoy', 'h'), ('ለ', 'Lawi', 'l'), ('ሐ', 'Hawt', 'ḥ'),
    ('መ', 'May', 'm'), ('ሠ', 'Sewt', 'ś'), ('ረ', 'Ris', 'r'),
    ('ሰ', 'Sat', 's'), ('ቀ', 'Qaf', 'q'), ('በ', 'Bet', 'b'),
    ('ተ', 'Taw', 't'), ('ኀ', 'Harm', 'ḫ'), ('ነ', 'Nehas', 'n'),
    ('አ', 'Alef', 'ʾ'), ('ከ', 'Kaf', 'k'), ('ወ', 'Wewe', 'w'),
    ('ዐ', 'Ayin', 'ʿ'), ('ዘ', 'Zey', 'z'), ('የ', 'Yemen', 'y'),
    ('ደ', 'Dint', 'd'), ('ገ', 'Gemel', 'g'), ('ጠ', 'Teyt', 'ṭ'),
    ('ጰ', 'Peyt', 'ṗ'), ('ጸ', 'Sedey', 'ṣ'), ('ፀ', 'Sepa', 'ṣ́'),
    ('ፈ', 'Af', 'f'), ('ፐ', 'Psa', 'p'),
]

# -- The Debtera (halehame) folk values, TRANSCRIBED ---------------------------
# DOCTRINE: transcribed from geez.org, "Numerology", the Debtera (Halehame)
# Enumeration table as read 2026-11-24: the table prints each base's value
# in Ethiopic numerals; the values below are that table read off row by row
# (ሀ ፩=1 … ፐ ፰፻=800). Corroborated at its endpoints and its multiplier
# examples by Ayele Bekerie, "Ethiopic, An African Writing System" (1997),
# via Peter T. Daniels' H-Net review (h=1, l=2, …, p=800; hu=2, lu=4,
# po=5600). The class formula (units 1-10 / tens / hundreds by position)
# is NOT the source — it is a check the transcription must pass, run in
# folk_formula() below; a transcription that failed it would be a finding.
FOLK_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               20, 30, 40, 50, 60, 70, 80, 90, 100,
               200, 300, 400, 500, 600, 700, 800]


def folk_formula(position):
    """The class law the published table obeys — a check, never the source.

    MECHANISM: positions 1-10 carry their position (units, ተ=10 included);
    positions 11-19 carry (position-9) x 10 (ኀ=20 … ደ=100); positions
    20-26 carry (position-18) x 100 (ገ=200 … ፐ=800). The same law is
    stated in prose by esotericnumbers.com's practitioner calculator
    ("the first ten letters are 1 to 10, the next nine run in tens from
    ኀ at 20 to ደ at 100, and the last seven in hundreds up to ፐ at 800").
    """
    if position <= 10:
        return position
    if position <= 19:
        return (position - 9) * 10
    return (position - 18) * 100


# -- The seven orders -----------------------------------------------------------
# DOCTRINE: order names are the tradition's own (ግዕዝ ካዕብ ሣልስ ራብዕ ኃምስ
# ሳድስ ሳብዕ, the geez.org table's column heads). Vowel values follow the
# EEG (Encyclopaedia Aethiopica) romanization as summarized by the Unicode
# guide's order table: 1 ä, 2 u, 3 i, 4 a, 5 e, 6 ə (also consonant-alone),
# 7 o. Order 6's double duty (schwa / no vowel) is a printed seam of the
# audit, not a detail to smooth.
ORDERS = [
    (1, "Ge'ez (ግዕዝ)", 'ä'),
    (2, "Ka'eb (ካዕብ)", 'u'),
    (3, "Salis (ሣልስ)", 'i'),
    (4, "Rabe' (ራብዕ)", 'a'),
    (5, "Hamis (ኃምስ)", 'e'),
    (6, "Sadis (ሳድስ)", 'ə'),
    (7, "Sabe' (ሳብዕ)", 'o'),
]
# MECHANISM: in the Unicode Ethiopic block each classical series occupies
# consecutive codepoints, order n at base_cp + (n-1); the Unicode name of
# each glyph ends in a consonant+vowel token (HA, HU, HI, HAA, HEE, HE,
# HO). The check is a suffix law on that final token, longest match first
# (order 4's AA before order 1's A; order 5's EE before order 6's E).
# A glyph whose name fails its order's suffix aborts the build — the grid
# is verified, not assumed.
def order_token_ok(name, order):
    t = name.rsplit(' ', 1)[-1] if name else ''
    if order == 1:
        return t.endswith('A') and not t.endswith('AA')
    if order == 2:
        return t.endswith('U')
    if order == 3:
        return t.endswith('I')
    if order == 4:
        return t.endswith('AA')
    if order == 5:
        return t.endswith('EE')
    if order == 6:
        return t.endswith('E') and not t.endswith('EE')
    if order == 7:
        return t.endswith('O')
    return False

# -- The labiovelar series -------------------------------------------------------
# DOCTRINE: the script's own fusion device — consonant + ʷ glide fused in
# one glyph. Classical Ge'ez seats FOUR series (of ቀ ኀ ከ ገ); Unicode also
# encodes two post-classical series (of ቐ, a Tigrinya/Amharic base, and of
# ኸ, an Amharic base), inventoried separately and flagged. Each series has
# FIVE forms — for the orders 1, 3, 4, 5, 6 — and structurally cannot have
# an order-2 (u) or order-7 (o) form: the glide absorbs them ("Naturally
# there is no form with u also as vowel; nor … for o following (w)" —
# Hough, "Aspects of the Amharic Verb", on the classical syllabary).
# MECHANISM: (series first glyph, base glyph, classical?) — forms sit at
# codepoint offsets [0, 2, 3, 4, 5] from the series head; offset +1 is
# unassigned in the standard precisely because the u-form does not exist.
LABIOVELARS = [
    ('ቈ', 'ቀ', True), ('ኈ', 'ኀ', True), ('ኰ', 'ከ', True), ('ጐ', 'ገ', True),
    ('ቘ', 'ቐ', False), ('ዀ', 'ኸ', False),
]
LABIOVELAR_ORDERS = [1, 3, 4, 5, 6]  # ä, i, a, e, ə — no u, no o


def glyph_name(ch):
    """Unicode name of a glyph, or '' if unassigned — the build's witness."""
    try:
        return ud.name(ch)
    except ValueError:
        return ''


def build_inventory():
    """Every inventoried glyph at its grid coordinate, name-verified.

    MECHANISM: classical rows are generated by codepoint arithmetic from
    each base's first form and each glyph's Unicode name is checked
    against its order token; the 8th slot (base_cp + 7) is inventoried
    where the standard encodes a glyph there; labiovelar rows likewise
    from their series heads. Returns a list of row dicts for the CSV.
    """
    rows = []
    for pos, (base, name, tr) in enumerate(HALEHAME_BASES, start=1):
        cp0 = ord(base)
        for order, order_name, vowel in ORDERS:
            ch = chr(cp0 + order - 1)
            nm = glyph_name(ch)
            assert order_token_ok(nm, order), (
                f"name check failed at {base} order {order}: {nm!r}")
            rows.append({
                'series': 'classical', 'base': base, 'base_name': name,
                'base_position': pos, 'order': order,
                'order_name': order_name, 'vowel': vowel, 'glyph': ch,
                'codepoint': f'U+{ord(ch):04X}', 'unicode_name': nm,
            })
        # The 8th slot: base_cp + 7, where the standard fills it.
        ch8 = chr(cp0 + 7)
        nm8 = glyph_name(ch8)
        if 'SYLLABLE' in nm8:
            rows.append({
                'series': 'eighth-slot', 'base': base, 'base_name': name,
                'base_position': pos, 'order': 8,
                'order_name': "Eighth slot (wa-form / ኧ-type)",
                'vowel': 'wa/ä', 'glyph': ch8,
                'codepoint': f'U+{ord(ch8):04X}', 'unicode_name': nm8,
            })
    for head, base, classical in LABIOVELARS:
        cp0 = ord(head)
        for order in LABIOVELAR_ORDERS:
            # MECHANISM: offsets from the series head are [0,2,3,4,5] for
            # orders [1,3,4,5,6] — offset +1 (the u-form) is unassigned.
            ch = chr(cp0 + {1: 0, 3: 2, 4: 3, 5: 4, 6: 5}[order])
            nm = glyph_name(ch)
            assert 'SYLLABLE' in nm and 'W' in nm.rsplit(' ', 1)[-1], (
                f"labiovelar name check failed: {nm!r}")
            rows.append({
                'series': 'labiovelar-classical' if classical
                          else 'labiovelar-postclassical',
                'base': base, 'base_name': f'{base}-series (labiovelar)',
                'base_position': '', 'order': order,
                'order_name': dict((o, n) for o, n, _ in ORDERS)[order],
                'vowel': dict((o, v) for o, _, v in ORDERS)[order],
                'glyph': ch, 'codepoint': f'U+{ord(ch):04X}',
                'unicode_name': nm,
            })
    return rows


def build_halehame():
    """The folk values per base, with the GAP rows printed as gaps.

    DOCTRINE: coverage is stated against the whole inventoried field, not
    only against the 26 the table reaches: the labiovelar series and the
    later-added bases carry NO halehame value in any source read, and the
    audit prints them as GAP rows rather than passing over them in
    silence. (The practitioner calculator at esotericnumbers.com states
    the same boundary: later-added letters "carry no classical value and
    are skipped.")
    """
    rows = []
    for pos, ((base, name, tr), val) in enumerate(
            zip(HALEHAME_BASES, FOLK_VALUES), start=1):
        assert val == folk_formula(pos), (
            f"transcription fails the class law at position {pos}")
        rows.append({
            'base': base, 'base_name': name, 'transliteration': tr,
            'halehame_position': pos, 'folk_value_first_form': val,
            'value_class': ('units' if pos <= 10 else
                            'tens' if pos <= 19 else 'hundreds'),
            'source': "geez.org, Numerology, Debtera (Halehame) "
                      "Enumeration table (read 2026-11-24); endpoints + "
                      "multipliers corroborated by Bekerie (1997) via "
                      "Daniels, H-Net review",
            'status': 'SOURCED',
        })
    rows.append({
        'base': 'ቈ ኈ ኰ ጐ (+ቘ ዀ)', 'base_name': 'labiovelar series',
        'transliteration': 'qʷ ḫʷ kʷ gʷ (+q̱ʷ ḵʷ)',
        'halehame_position': '', 'folk_value_first_form': '',
        'value_class': '', 'source': 'no source read assigns a halehame '
        'value to any labiovelar; the only published enumeration valuing '
        'any (ኈ=900, ቈ=1000) is the geez.org Gematria (Abegede) overlay, '
        'a scholarly superimposition — tier CONSTRUCTED, not the folk '
        'table', 'status': 'GAP',
    })
    rows.append({
        'base': 'ሸ ቸ ኘ ዠ ጀ ኸ ዥ ቨ', 'base_name': 'later-added bases',
        'transliteration': 'š č ñ ž ǧ ḵ ǧ̌ v',
        'halehame_position': '', 'folk_value_first_form': '',
        'value_class': '', 'source': 'no source read assigns a halehame '
        'value to the Amharic-era bases; esotericnumbers.com states they '
        '"carry no classical value and are skipped"',
        'status': 'GAP',
    })
    return rows


def build_seating():
    """The Divine Nine seated on the grid — a DESIGN, tiered per row.

    DOCTRINE: the seating follows the founder's hybrid law (2026-11-24):
    the Seven seat on the seven orders by sound; the two hybrids (ΕΙ, ΟΥ)
    seat by the tongue's own fusion devices. Every row carries its
    reasoning (the standing correspondence rule) and its tier. Seams are
    rows of their own, never footnotes to a smooth table: the ä/a crowding
    at Α, the length gaps at Η and Ω, the zero at order 6.
    """
    return [
        {'station': 'Α (Alpha, 1)', 'seat': 'Order 4 (a)',
         'device': 'plain order',
         'reasoning': "Order 4 carries the full open /a/ — the exact sound "
                      "of Α; it is also the order Lambdin's romanization "
                      "writes with plain 'a'. The clean seat.",
         'tier': 'DESIGN — sound match exact'},
        {'station': 'Α — second claimant (seam)', 'seat': 'Order 1 (ä)',
         'device': 'plain order',
         'reasoning': "Order 1's vowel is ä, a centralized [ɐ] between /a/ "
                      "and /ə/; for the glottal and pharyngeal bases "
                      "(ሀ, አ, ዐ) it is pronounced as /a/ outright, so "
                      "orders 1 and 4 collide at Α for at least three "
                      "bases and crowd it for the rest. Order 1 is seated "
                      "as Α's reduced twin, flagged — not given a station "
                      "of its own, because Greek has no second a-station "
                      "to give it.",
         'tier': 'DESIGN — seam printed, not smoothed'},
        {'station': 'Ε (Epsilon, 5)', 'seat': 'Order 5 (e)',
         'device': 'plain order',
         'reasoning': "Order 5 carries short /e/, the exact sound of Ε. "
                      "Clean seat; the long-ē territory of Η folds here "
                      "(see the Η row).",
         'tier': 'DESIGN — sound match exact'},
        {'station': 'Η (Eta, 8)', 'seat': 'UNSEATED — length gap',
         'device': 'none in the grid',
         'reasoning': "Η is long ē. The fidäl marks no vowel length "
                      "anywhere — no order, no device, distinguishes ē "
                      "from e. Η therefore takes no seat; its territory "
                      "is folded into order 5 (Ε) and the gap is printed "
                      "as a gap. Any future seating of Η is a mint's "
                      "invention, not this audit's finding.",
         'tier': 'DESIGN — gap printed'},
        {'station': 'Ι (Iota, 10)', 'seat': 'Order 3 (i)',
         'device': 'plain order',
         'reasoning': "Order 3 carries /i/, the exact sound of Ι. Clean "
                      "seat.",
         'tier': 'DESIGN — sound match exact'},
        {'station': 'Ο (Omicron, 70)', 'seat': 'Order 7 (o)',
         'device': 'plain order',
         'reasoning': "Order 7 carries short /o/, the exact sound of Ο. "
                      "Clean seat; the long-ō territory of Ω folds here "
                      "(see the Ω row).",
         'tier': 'DESIGN — sound match exact'},
        {'station': 'Υ (Upsilon, 400)', 'seat': 'Order 2 (u)',
         'device': 'plain order',
         'reasoning': "Order 2 carries /u/, the grid's only u; Υ is the "
                      "Greek u-station (the house's Divine Nine likewise "
                      "seats the high-back /u/ family at the VV/Υ seat). "
                      "Clean seat.",
         'tier': 'DESIGN — sound match exact'},
        {'station': 'Ω (Omega, 800)', 'seat': 'UNSEATED — length gap',
         'device': 'none in the grid',
         'reasoning': "Ω is long ō; the fidäl marks no length, so Ω takes "
                      "no seat of its own — its territory folds into "
                      "order 7 (Ο). Printed coordinate, offered without "
                      "weight: the folk table's last value is ፐ = 800, "
                      "which is also Ω's Milesian value; the audit "
                      "records the coincidence of number and claims no "
                      "bridge on it.",
         'tier': 'DESIGN — gap printed'},
        {'station': 'the ZERO (order 6, ə)', 'seat': 'Order 6 (ə)',
         'device': 'plain order',
         'reasoning': "Order 6 is the reduced vowel /ə/ and does double "
                      "duty as the consonant-alone form — the grid's "
                      "vowel-zero. No Greek vowel station honestly takes "
                      "it: Greek has no schwa letter, and seating ə at Η "
                      "or Ω would be a forgery of sound. It is seated "
                      "as the ZERO station of the Nine's grid — the "
                      "unseated seat — in the house's standing pattern "
                      "(Ϻ's OPEN chair; WW's void on the doubles map).",
         'tier': 'DESIGN — zero printed as a seat'},
        {'station': 'ΕΙ (15) — hybrid', 'seat': 'The 8th slot (order 8)',
         'device': "the grid's eighth-slot extension",
         'reasoning': "ΕΙ is the front hybrid (e+i). The grid's own "
                      "second extension device is the 8th slot: encoded "
                      "for 25 of the 26 classical bases (ዐ alone lacks "
                      "one), its classical exemplar is ኧ, the glottal's "
                      "eighth form. ΕΙ seats as the eighth order "
                      "generalized from that attested slot. Coordinate "
                      "printed at full size: the slot's classical "
                      "attestation is thin (ኧ is the standard case; the "
                      "wa-forms flourish in Amharic), so this is the "
                      "thinnest device in the design. Alternative seat "
                      "printed for the record: the labiovelar i-forms "
                      "(Cʷi) — rejected as primary because they belong "
                      "to the rounded fusion that carries ΟΥ.",
         'tier': 'CONSTRUCTED — by the hybrid law'},
        {'station': 'ΟΥ (470) — hybrid', 'seat': 'The labiovelar order',
         'device': 'labiovelar fusion (consonant + ʷ)',
         'reasoning': "ΟΥ is the rounded hybrid (o+u); its second element "
                      "is the u-glide. The labiovelar series is the same "
                      "fusion in the tongue's own hand — consonant + ʷ "
                      "fused in one glyph, five forms, structurally "
                      "without u- or o-forms because the glide absorbs "
                      "them. ΟΥ seats as the labiovelar order: the grid's "
                      "native diphthong column.",
         'tier': 'CONSTRUCTED — by the hybrid law'},
    ]


def build_zero_point():
    """Folk value vs grid position, per base — coordinates, no blob.

    MECHANISM: the 'constructed seat' the key supplies at this phase is
    the base's grid position (its halehame coordinate); the folk value is
    the transcribed table. The relation column states, per base, whether
    the two agree (folk == position) or where they part, and by what law.
    """
    rows = []
    for pos, ((base, name, tr), val) in enumerate(
            zip(HALEHAME_BASES, FOLK_VALUES), start=1):
        if val == pos:
            rel = 'AGREE — folk value equals grid position'
        elif pos <= 19:
            rel = 'PART — tens law: folk = (position − 9) × 10'
        else:
            rel = 'PART — hundreds law: folk = (position − 18) × 100'
        rows.append({
            'base': base, 'base_name': name, 'grid_position': pos,
            'folk_value': val, 'relation': rel,
            'folk_multiplier_at_order_6': val * 6,
            'note': ('boundary: last agreement' if pos == 10 else
                     'boundary: first parting' if pos == 11 else
                     'boundary: tens/hundreds hinge (last tens value)'
                     if pos == 19 else
                     'boundary: first hundreds step' if pos == 20 else
                     'folk maximum' if pos == 26 else ''),
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
    # MECHANISM: calibration first — the tradition's own worked example
    # must recompute exact before any derived number is trusted
    # (ክርስቶስ: ከ50 + ረ6 + ሰ7 + ተ10 [ቶ counts as ተ] + ሰ7 = 80).
    base_value = {b: v for (b, _, _), v in zip(HALEHAME_BASES, FOLK_VALUES)}
    christos = sum(base_value[c] for c in 'ከረሰተሰ')
    assert christos == 80, f"calibration failed: ክርስቶስ = {christos}"
    print(f"CALIBRATION OK — ክርስቶስ = {christos} "
          f"(geez.org's worked example, recomputed)")

    inv = build_inventory()
    hal = build_halehame()
    seat = build_seating()
    zp = build_zero_point()

    write_csv('geez-fidal-inventory.csv', inv,
              ['series', 'base', 'base_name', 'base_position', 'order',
               'order_name', 'vowel', 'glyph', 'codepoint', 'unicode_name'])
    write_csv('geez-halehame-values.csv', hal,
              ['base', 'base_name', 'transliteration', 'halehame_position',
               'folk_value_first_form', 'value_class', 'source', 'status'])
    write_csv('geez-nine-seating.csv', seat,
              ['station', 'seat', 'device', 'reasoning', 'tier'])
    write_csv('geez-zero-point.csv', zp,
              ['base', 'base_name', 'grid_position', 'folk_value',
               'relation', 'folk_multiplier_at_order_6', 'note'])

    n_classical = sum(1 for r in inv if r['series'] == 'classical')
    n_eighth = sum(1 for r in inv if r['series'] == 'eighth-slot')
    n_lab_c = sum(1 for r in inv if r['series'] == 'labiovelar-classical')
    n_lab_p = sum(1 for r in inv
                  if r['series'] == 'labiovelar-postclassical')
    print(f"INVENTORY — classical {n_classical} "
          f"(26 bases x 7 orders); labiovelar classical {n_lab_c} "
          f"(4 x 5), post-classical {n_lab_p} (2 x 5); "
          f"eighth-slot {n_eighth} of 26 bases")
    print(f"HALEHAME — 26 of 26 classical bases SOURCED; "
          f"2 GAP rows printed (labiovelars, later-added bases)")
    print(f"SEATING — {len(seat)} rows (7 orders, 2 length gaps, "
          f"1 zero, 2 hybrids)")
    print(f"ZERO POINT — agreement at positions 1-10; "
          f"first parting at position 11 (ኀ: position 11, folk 20)")
    print("CSVs written beside this script. Findings, never doctrine. 93.")


if __name__ == '__main__':
    main()
