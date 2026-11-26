#!/usr/bin/env python3
# =============================================================================
# 93 — build_branch_offsets.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXVI day of November, Dies Iovis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: THE BRANCH-OFFSET REGISTER's computation. Every branch
# script in the house is weighed against its parent tongue, letter by
# letter, at alignments that already exist in the house — the census
# CSVs, the descent table, the Phoenician map, the engine's own banks.
# Offset = branch value − parent value, at each aligned seat. Nothing
# is fitted: no alignment is adjusted to manufacture a pattern; where
# an alignment is absent or disputed, the row prints the gap.
#
# DOCTRINE — THE OFFSET: the founder's exemplar governs the reading.
# In the Latin bank the refused double VV parts from X by exactly 20,
# and 20 in Rome's own hand is XX, the lawful double — the offset
# landed signed in the branch's own root system. A parting is data;
# an offset that lands on a seat of the branch's own grid is printed
# as a SIGNED offset, with the seat named.
#
# DOCTRINE — TIERS: values ATTESTED (the tradition's own tables, as
# the engine seats them and the audits froze them); patterns DERIVED
# (laws fit to the computed offsets, each with its killing evidence);
# readings CONSTRUCTED (the signed-offset readings, labelled).
#
# CONTENT TEST: Inputs — pontifex/tables.py (the living banks);
#   research/caucasus-north/{cyrillic-table,glagolitic-table,
#   slavonic-parting,georgian-table}.csv; research/twelve-tongues/
#   {aramaic-table,armenian-table,coptic-descent}.csv;
#   maps/phoenician-cypher-glyph-map/phoenician-cypher-glyph-map.csv.
#   Processes — the seven branch computations below. Outputs —
#   branch_offsets.csv (every row), branch_offsets_summary.json
#   (counts, histograms, pattern fits), and this report on stdout.
#   Tolerances — every value recomputed from the living bank at run
#   time and cross-checked against its frozen CSV cell; a mismatch
#   aborts the build and names the cell.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO))

from pontifex.tables import (
    GREEK, CYRILLIC, GLAGOLITIC, COPTIC, ARABIC_ABJAD,
    LATIN_ORDINAL, AGRIPPA, HEBREW, ARMENIAN, GEORGIAN,
)
from pontifex.engine import weigh

CAUCASUS = REPO / 'research' / 'caucasus-north'
TWELVE = REPO / 'research' / 'twelve-tongues'
PHOENICIAN_CSV = (REPO / 'maps' / 'phoenician-cypher-glyph-map'
                  / 'phoenician-cypher-glyph-map.csv')

ROWS = []          # the register's every row
SUMMARY = {}       # per-branch counts, histograms, patterns


def read_csv(path):
    with open(path, encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def add(branch, seat, parent_letter, parent_value, branch_letter,
        branch_value, status, pairing, reasoning):
    offset = None
    if parent_value is not None and branch_value is not None:
        offset = branch_value - parent_value
        if status == 'COMPUTED':
            status = 'AGREE' if offset == 0 else 'OFFSET'
    ROWS.append({
        'branch': branch, 'seat': seat, 'parent_letter': parent_letter,
        'parent_value': parent_value, 'branch_letter': branch_letter,
        'branch_value': branch_value, 'offset': offset,
        'status': status, 'pairing': pairing, 'reasoning': reasoning,
    })


def summarise(branch, extra=None):
    rows = [r for r in ROWS if r['branch'] == branch]
    computed = [r for r in rows if r['offset'] is not None
                and r['status'] in ('AGREE', 'OFFSET')]
    hist = Counter(r['offset'] for r in computed)
    s = {
        'rows': len(rows),
        'computed': len(computed),
        'agree': sum(1 for r in computed if r['offset'] == 0),
        'offset': sum(1 for r in computed if r['offset'] != 0),
        'histogram': {str(k): hist[k] for k in sorted(hist)},
        'statuses': dict(Counter(r['status'] for r in rows)),
    }
    if extra:
        s.update(extra)
    SUMMARY[branch] = s
    return s


# Greek capital (as the census CSVs print pairs) -> the engine's key.
GREEK_PAIR_KEY = {'Ϛ': 'ϛ', 'Ϟ': 'ϟ', 'Ϡ': 'ϡ'}


def greek_value(pair_glyph):
    key = GREEK_PAIR_KEY.get(pair_glyph, pair_glyph.lower())
    return GREEK[key]


# =============================================================================
# BRANCH 1 — GREEK -> CYRILLIC. Alignment: cyrillic-table.csv's own
# greek_pair column (the census's sourced seats). Expectation is NOT
# assumed: every cell is recomputed from the living GREEK bank.
# =============================================================================
def branch_cyrillic():
    B = 'greek-cyrillic'
    for row in read_csv(CAUCASUS / 'cyrillic-table.csv'):
        letter, pair, val = row['letter'], row['greek_pair'], row['value']
        status = row['status']
        if status == 'SOURCED':
            pv = greek_value(pair)
            bv = int(val)
            assert CYRILLIC[letter] == bv, f'Cyrillic cell mismatch {letter}'
            add(B, row['seat'], pair, pv, letter, bv, 'COMPUTED', 'sound',
                'the census seat: the Cyrillic letter at its Greek pair, '
                'both values recomputed from the living banks')
        elif status == 'VARIANT':
            # Variants duplicate a held seat; pair by the letter's own
            # identity as the parting table states it.
            seat_pairs = {'Ѵ': ('Υ', 400), 'Ꙋ': ('Υ', 400), 'Ѹ': ('Υ', 400),
                          'Ѿ': ('Ω', 800), 'Ꙍ': ('Ω', 800), 'Ѧ': ('Ϡ', 900)}
            pair, pv = seat_pairs[letter]
            add(B, 'variant', pair, pv, letter, int(val), 'VARIANT', 'seat',
                'a variant glyph at a seat already held; printed in the '
                'annex, never in the main count')
        elif status == 'REFUSED-WESTERN':
            add(B, 'refused', pair or '', None, letter,
                int(val) if val else None, 'REFUSED', 'seat',
                'a western witness reading the house refuses; printed '
                'refused, never offset')
    summarise(B)


# =============================================================================
# BRANCH 2 — GREEK -> GLAGOLITIC. Alignment CHAINED from two in-house
# alignments and no other: Greek -> Cyrillic (greek_pair), then
# Cyrillic -> Glagolitic (slavonic-parting PAIRS, keyed by the
# Cyrillic letter). Seat-pairings flagged where the chain runs on a
# numeral seat rather than a sound (the epissemon seats).
# =============================================================================
def branch_glagolitic():
    B = 'greek-glagolitic'
    parting = {r['cyrillic_letter']: r for r in
               read_csv(CAUCASUS / 'slavonic-parting.csv')}
    # Greek seat -> Cyrillic heirs (from cyrillic-table SOURCED rows,
    # plus the b-row: Cyrillic Б, unseated in the numeral table but
    # seated in the parting as beta's b-heir).
    heirs = {}
    for row in read_csv(CAUCASUS / 'cyrillic-table.csv'):
        if row['status'] == 'SOURCED':
            heirs.setdefault(row['greek_pair'], []).append(row['letter'])
    heirs.setdefault('Β', []).append('Б')
    heirs.setdefault('Υ', []).append('Ѵ')   # izhitsa, the variant heir
    seat_flag = {'Ϛ': 'seat — the dz sound has no Greek letter; Cyrillic '
                       'seats Ѕ at the stigma seat, and the chain follows '
                       'the seat',
                 'Ϟ': 'seat — the ch sound has no Greek letter; Cyrillic '
                       'seats Ч at the koppa seat, and the chain follows '
                       'the seat',
                 'Ϡ': 'seat — the ts sound has no Greek letter; Cyrillic '
                       'seats Ц at the sampi seat, and the chain follows '
                       'the seat'}
    greek_order = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ϛ', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ',
                   'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ϟ', 'Ρ', 'Σ', 'Τ', 'Υ',
                   'Φ', 'Χ', 'Ψ', 'Ω', 'Ϡ']
    reached_glag = set()
    for g in greek_order:
        pv = greek_value(g)
        for cyr in heirs.get(g, []):
            prow = parting.get(cyr)
            if prow is None:
                add(B, g, g, pv, cyr, CYRILLIC.get(cyr), 'NO-PARTING-ROW',
                    'sound', 'the Cyrillic heir stands outside the '
                             'parting table; the chain ends, printed')
                continue
            glag = prow['glagolitic_letter']
            gv = GLAGOLITIC.get(glag)
            reached_glag.add(glag)
            pairing = 'seat' if g in seat_flag else 'sound'
            why = seat_flag.get(g, 'the chained sound: Greek pair to '
                                   'Cyrillic heir to Glagolitic letter, '
                                   'both alignments the census\u2019s own')
            if cyr == 'Ѵ':
                why = ('the variant heir: izhitsa, Cyrillic’s '
                       'second upsilon letter, chained through the '
                       'parting’s izhitsa row')
            if glag == '':
                add(B, g, g, pv, '', None, 'BRANCH-ABSENT', pairing, why)
            elif gv is None:
                add(B, g, g, pv, glag, None, 'BRANCH-UNSEATED', pairing,
                    why + '; the Glagolitic letter stands in the alphabet '
                          'and seats no value in the sourced table')
            else:
                add(B, g, g, pv, glag, gv, 'COMPUTED', pairing, why)
    # Branch-only seats: Glagolitic letters the chain never reaches.
    native = {'Ⰶ': 'zh — a Slavic sound with no Greek letter',
              'Ⱋ': 'sht — a Slavic cluster with no Greek letter',
              'Ⱎ': 'sh — a Slavic sound with no Greek letter',
              'Ⱏ': 'yeru — a Slavic vowel with no Greek letter',
              'Ⱑ': 'yati — a Slavic vowel with no Greek letter',
              'Ⱓ': 'yu — a Slavic sound with no Greek letter',
              'Ⱔ': 'small yus — a nasal vowel with no Greek letter'}
    for glag, why in native.items():
        if glag not in reached_glag:
            add(B, 'native', '', None, glag, GLAGOLITIC[glag],
                'GAP-NO-PARENT', 'none', why + '; the branch\u2019s own '
                'seat, printed with no parent and no offset')
    for hole in ('Ⱊ', 'Ⱐ', 'Ⱒ'):
        add(B, 'hole', '', None, hole, None, 'BRANCH-UNSEATED', 'none',
            'a letter of the alphabet no witness seats (the Plate XI '
            'holes); printed as a hole, never offset')
    summarise(B)


# =============================================================================
# BRANCH 3 — GREEK -> COPTIC. Alignment: coptic-descent.csv, the
# Phase I descent table, seat for seat. The Demotic seven are FENCED:
# printed unvalued, never offset. Fai (ϥ) is Demotic by birth and
# valued by seat — printed apart from the fence.
# =============================================================================
def branch_coptic():
    B = 'greek-coptic'
    for row in read_csv(TWELVE / 'coptic-descent.csv'):
        if not row['value'].isdigit():
            continue
        pv = int(row['value'])
        csign = row['coptic_sign']
        cv = COPTIC[csign.lower()] if csign.lower() in COPTIC else None
        assert cv == pv, f'Coptic descent cell mismatch at {pv}'
        note = row['relation']
        kind = 'sound'
        if pv == 90:
            kind = 'seat'
            why = ('the one parting of lineage: Greek\u2019s holder ϟ '
                   '(koppa) was a dead letter; Coptic seats ϥ (fai), a '
                   'living Demotic letter, at the seat — kinship of '
                   'seat, not of glyph')
        elif pv in (6, 900):
            why = ('a parting of kind: an epissemon sign on both banks, '
                   'numeral-only in both tongues; the value descends '
                   'entire')
        elif pv == 200:
            why = ('a parting of form: Greek carries two glyphs (σ and '
                   'final ς) at this seat; Coptic ⲥ is one letter')
        else:
            why = ('descent preserved the seat entire — the Coptic '
                   'sign is the Greek letter\u2019s own heir')
        add(B, str(pv), row['greek_sign'], pv, csign, cv, 'COMPUTED',
            kind, why + f' [descent table: {note[:60]}…]' if len(note) > 60
            else why)
    for ch, name in (('ϣ', 'shai'), ('ϧ', 'khai (Bohairic)'),
                     ('ⳉ', 'khai (Akhmimic)'), ('ϩ', 'hori'),
                     ('ϫ', 'gangia'), ('ϭ', 'shima'), ('ϯ', 'dei')):
        assert ch not in COPTIC and weigh(ch, 'coptic')['value'] == 0
        add(B, 'fenced', '', None, ch, None, 'FENCED', 'none',
            f'{name} — a Demotic letter the attested system leaves '
            'valueless; the Milesian grid arrived full and no witness '
            'seats it. Fenced: printed, never offset')
    summarise(B)


# =============================================================================
# BRANCH 4 — ARAMAIC -> HEBREW and ARAMAIC -> ARABIC. The parent is
# the 22-letter abjad the aramaic-table froze (Imperial and Syriac
# strata). Hebrew alignment: the table's own hebrew_equivalent
# column. Arabic alignment: the shared abjad order — Aramaic
# position n against the n-th letter of the ARABIC_ABJAD bank, whose
# header states the traditional abjadī order.
# =============================================================================
def branch_aramaic():
    rows = read_csv(TWELVE / 'aramaic-table.csv')
    by_pos = {}
    for r in rows:
        by_pos.setdefault(int(r['position']), {})[r['stratum']] = r
    # The two strata must agree in value at every position.
    for pos, strata in by_pos.items():
        vals = {s: int(r['value']) for s, r in strata.items()}
        assert len(set(vals.values())) == 1, f'Aramaic strata part at {pos}'
    abjad = list(ARABIC_ABJAD.items())   # dict order = abjadī order
    for pos in sorted(by_pos):
        imp = by_pos[pos]['IMPERIAL']
        av = int(imp['value'])
        he = imp['hebrew_equivalent']
        hv = HEBREW[he]
        add('aramaic-hebrew', str(pos), imp['glyph'], av, he, hv,
            'COMPUTED', 'sound',
            'the table\u2019s own Hebrew equivalent; both strata of '
            'the parent agree in value at this seat')
        if pos <= len(abjad):
            alett, aval = abjad[pos - 1]
            add('aramaic-arabic', str(pos), imp['glyph'], av, alett,
                aval, 'COMPUTED', 'order',
                'the shared abjad order: Aramaic seat n against the '
                'n-th letter of the Arabic abjad bank')
    for i in range(22, len(abjad)):
        alett, aval = abjad[i]
        add('aramaic-arabic', 'extension', '', None, alett, aval,
            'EXTENSION', 'none',
            'an Arabic letter beyond the 22 of the shared order — '
            'the branch\u2019s own extension (the letters of the '
            'Arabic sounds the parent stock had no seats for)')
    head = {s: weigh(w, s)['value'] for w, s in
            (('עז', 'hebrew'), ('ܥܙ', 'aramaic'), ('عز', 'arabic_abjad'))}
    summarise('aramaic-hebrew', {'head_77': head})
    summarise('aramaic-arabic', {'head_77': head})


# =============================================================================
# BRANCH 5 — GREEK -> LATIN. Alignment: the Phoenician map's 22
# rows — the shared line, each Phoenician letter's Greek heir
# against its Latin heir. Parent: Milesian (the map's greek_value,
# cross-checked against the living GREEK bank). Branch banks:
# latin_ordinal (the map's own Latin bank) and Agrippa (Latin's
# second bank), printed as two offset columns of one branch.
# =============================================================================
def branch_latin():
    B = 'greek-latin'
    for row in read_csv(PHOENICIAN_CSV):
        gname, lname = row['greek_name'], row['latin']
        gv_raw, lv_raw = row['greek_value'], row['latin_value']
        if gv_raw == '':
            add(B, row['n'], row['greek'], None, lname or '', None,
                'GAP-NO-PARENT', 'sound',
                f'{gname} carries no Milesian value (san, the '
                'Phoenician ṣādē\u2019s Greek heir, stands outside '
                'the numeral grid); no parent value, no offset')
            continue
        gv = int(gv_raw)
        if lname == '' or lv_raw == '':
            add(B, row['n'], row['greek'], gv, lname or 'TH', None,
                'GAP-NO-BRANCH', 'sound',
                'no single Latin letter carries this sound (the map '
                'files the digraph TH unpriced, and the ṣādē row '
                'stands empty); the gap prints, no offset')
            continue
        lo = LATIN_ORDINAL[lname]
        assert lo == int(lv_raw)
        add(B, row['n'], row['greek'], gv, lname, lo, 'COMPUTED',
            'sound', 'the map\u2019s row: Milesian parent against '
                     'the Latin ordinal heir')
        ag = AGRIPPA[lname]
        add('greek-latin-agrippa', row['n'], row['greek'], gv, lname,
            ag, 'COMPUTED', 'sound',
            'the same row on Latin\u2019s second bank: Agrippa\u2019s '
            'published values against the Milesian parent')
    summarise(B)
    summarise('greek-latin-agrippa')


# =============================================================================
# BRANCH 6 — ARMENIAN and GEORGIAN: TESTIMONY, never a verdict.
# Parentage is disputed in the literature (a Greek line and an
# Aramaic line are both claimed). The register computes the offset
# signature against BOTH candidate parents under printed sound
# alignments — every pair carries its reasoning, every absence a
# gap — and lets the two signatures stand side by side.
# Discipline: a pair whose BRANCH value exceeds the parent grid's
# cap (Milesian 900, Hebrew 400) is flagged EXTENSION and excluded
# from the agreement counts: beyond the cap the branch is counting
# its own alphabet, and the offset measures the extension, not the
# descent.
# =============================================================================
# pair maps: transliteration -> (parent letter, parent value,
# pairing kind, reasoning). Parent values are read from the living
# banks in testimony() — the literals here are letters and reasons.
ARM_GREEK = {
    'a': ('α', 'sound', 'the head of both alphabets'),
    'b': ('β', 'sound', 'the shared second seat'),
    'g': ('γ', 'sound', 'the shared third seat'),
    'd': ('δ', 'sound', 'the shared fourth seat'),
    'e': ('ε', 'sound', 'the shared fifth seat'),
    'z': ('ζ', 'sound', 'Armenian seats z sixth in its own order; '
                         'Greek seats ζ seventh, after the epissemon'),
    'ē': ('η', 'sound', 'the long-e vowel; Greek seats η eighth, '
                        'after the epissemon'),
    "t'": ('θ', 'sound', 'the aspirated t; both grids seat it ninth'),
    'i': ('ι', 'sound', 'Armenian\u2019s tens open with ž (a native '
                        'letter) at 10, so its i stands at 20 against '
                        'iota\u2019s 10'),
    'l': ('λ', 'sound', 'the shared l'),
    'x': ('χ', 'sound', 'Armenian x is the velar fricative /x/; its '
                        'Greek sound-heir is χ, seated at the hundreds '
                        'tail of the Milesian grid'),
    'k': ('κ', 'sound', 'the shared k'),
    'm': ('μ', 'sound', 'the shared m'),
    'n': ('ν', 'sound', 'the shared n'),
    'o': ('ο', 'sound', 'the shared o vowel'),
    'p': ('π', 'sound', 'the shared p'),
    'ṙ': ('ρ', 'sound', 'the trilled r against rho'),
    'r': ('ρ', 'doublet', 'Armenian\u2019s second r letter against '
                          'the same rho — a doublet, printed as such'),
    's': ('σ', 'sound', 'the plain s against sigma — seated in '
                        'Armenian\u2019s thousands extension, so the '
                        'row prints as EXTENSION'),
    't': ('τ', 'sound', 'the plain t against tau — seated in '
                        'Armenian\u2019s thousands extension, so the '
                        'row prints as EXTENSION'),
    'v': ('Ϝ', 'sound', 'the w-line: Armenian v descends from /w/; '
                        'Greek\u2019s w letter is the digamma, priced '
                        '6 by the Phoenician map (the living GREEK '
                        'bank seats the stigma at that value)'),
}
ARM_GREEK_GAPS = {
    'ə': 'the schwa — Greek has no letter for it',
    'ž': 'no Greek letter for /ʒ/',
    'c': 'no Greek letter for /ts/',
    'h': 'Greek seats no /h/ letter in the numeral grid (the rough '
         'breathing is a mark, not a letter)',
    'j': 'no Greek letter for /dz/',
    'ġ': 'no Greek letter for /ʁ/',
    'č': 'no Greek letter for /tʃ/',
    'y': 'Armenian y is /h/ — no Greek letter',
    'š': 'no Greek letter for /ʃ/',
    "č'": 'no Greek letter for the aspirated affricate',
    'ǰ': 'no Greek letter for /dʒ/',
    "c'": 'no second Greek ts letter',
    'w': 'a second w-line letter; the digamma seat is already '
         'claimed by v in this alignment',
    "p'": 'the aspirated p — Greek\u2019s aspirate seat is φ, '
          'already the pair of plain p\u2019s line in the Latin '
          'tradition; printed as a gap rather than a second claim',
    "k'": 'the aspirated k — no second Greek k letter',
}
ARM_HEBREW = {
    'a': ('א', 'sound', 'the head of the abjad'),
    'b': ('ב', 'sound', 'the shared second seat'),
    'g': ('ג', 'sound', 'the shared third seat'),
    'd': ('ד', 'sound', 'the shared fourth seat'),
    'e': ('ה', 'seat', 'the abjad\u2019s fifth seat; the SOUND '
                       'parts (Armenian e is a vowel, ה is /h/) — '
                       'a seat pair, printed as such'),
    'z': ('ז', 'sound', 'the shared zayin sound'),
    "t'": ('ט', 'sound', 'the t line: Armenian aspirate against '
                         'the abjad\u2019s plain t, both ninth'),
    'i': ('י', 'sound', 'the yod sound; Armenian\u2019s i stands '
                        'at 20 (its tens open with ž) against '
                        'yod\u2019s 10'),
    'l': ('ל', 'sound', 'the shared lamed'),
    'x': ('ח', 'sound', 'the Semitic back fricative: Armenian /x/ '
                        'against ħet /ħ/'),
    'c': ('צ', 'sound', 'the ts line: Armenian /ts/ against ṣadē'),
    'k': ('כ', 'sound', 'the shared kap'),
    'h': ('ה', 'sound', 'the /h/ letter against he'),
    'm': ('מ', 'sound', 'the shared mem'),
    'n': ('נ', 'sound', 'the shared nun'),
    'š': ('ש', 'sound', 'the shin sound'),
    'o': (None, 'gap', 'the o vowel — the abjad has no o letter; '
                       'some traditions pair o with ʿayin by seat, '
                       'printed here as a sound gap, not a pair'),
    'p': ('פ', 'sound', 'the shared pe'),
    'ṙ': ('ר', 'sound', 'the trilled r against resh'),
    's': ('ס', 'sound', 'the plain /s/ against samekh'),
    'v': ('ו', 'sound', 'the waw line: /w/ seated as v'),
    't': ('ת', 'sound', 'the plain t against taw'),
    'r': ('ר', 'doublet', 'the second r against the same resh'),
    "c'": ('צ', 'doublet', 'the aspirated ts against the same ṣadē'),
    'w': ('ו', 'doublet', 'the second w-line letter against waw'),
    "p'": ('פ', 'doublet', 'the aspirated p against the same pe'),
    "k'": ('ק', 'sound', 'the back k against qof — the abjad\u2019s '
                          'own k/q distinction'),
}
ARM_HEBREW_GAPS = {
    'ē': 'no Hebrew letter for the long e',
    'ə': 'no Hebrew letter for the schwa',
    'ž': 'no Hebrew letter for /ʒ/',
    'j': 'no Hebrew letter for /dz/',
    'ġ': 'no Hebrew letter for /ʁ/',
    'č': 'no Hebrew letter for /tʃ/',
    'y': 'Armenian y is /h/; the he seat is claimed by h in this '
         'alignment — printed as a gap, not a third claim',
    "č'": 'no Hebrew letter for the aspirated affricate',
    'ǰ': 'no Hebrew letter for /dʒ/',
}
GEO_GREEK = {
    'an': ('α', 'sound', 'the head of both alphabets'),
    'ban': ('β', 'sound', 'the shared second seat'),
    'gan': ('γ', 'sound', 'the shared third seat'),
    'don': ('δ', 'sound', 'the shared fourth seat'),
    'en': ('ε', 'sound', 'the shared fifth seat'),
    'vin': ('Ϝ', 'sound', 'the w-line: Georgian v against the '
                          'digamma, priced 6 by the Phoenician map'),
    'zen': ('ζ', 'sound', 'the shared z'),
    'he': ('η', 'sound', 'the obsolete long-e letter against eta'),
    'tan': ('θ', 'sound', 'the aspirated t, ninth in both'),
    'in': ('ι', 'sound', 'the shared i'),
    "k'an": ('κ', 'sound', 'Georgian k’an is the ejective k; '
                           'against kappa, the plain k of the '
                           'parent grid'),
    'las': ('λ', 'sound', 'the shared l'),
    'man': ('μ', 'sound', 'the shared m'),
    'nar': ('ν', 'sound', 'the shared n'),
    'on': ('ο', 'sound', 'the shared o'),
    "p'ar": ('π', 'sound', 'Georgian p’ar is the ejective p; '
                           'against pi, the plain p of the parent '
                           'grid'),
    'rae': ('ρ', 'sound', 'the shared r'),
    'san': ('σ', 'sound', 'the shared s'),
    "t'ar": ('τ', 'sound', 'the aspirated t against tau'),
    'vie': ('υ', 'seat', 'the obsolete w-letter at upsilon’s '
                         'seat — a seat pair: the sound parts (w '
                         'against u), the seat is the tradition’s '
                         'own (the Plate IX doubled seat)'),
    'un': ('υ', 'sound', 'the u vowel against upsilon — the second '
                         'holder of the doubled 400 seat'),
    'par': ('φ', 'sound', 'the aspirated p (par) against phi — in '
                           'the classical parent φ was itself /pʰ/'),
    'kan': ('χ', 'sound', 'the aspirated k (kan) against chi — in '
                            'the classical parent χ was itself /kʰ/'),
}
GEO_GREEK_GAPS = {
    'yad': 'the obsolete yad letter: it HOLDS the 60 seat of the '
           'grid with no Greek sound pair (Greek’s 60 is ξ, '
           '/ks/) — a seat filled natively, printed as a gap',
    'zhan': 'a native letter at the 90 seat: Greek’s 90 is the '
            'koppa sign; no sound pair — a seat filled natively',
    'ghan': 'no Greek letter for /ʁ/',
    "q'ar": 'no Greek letter for the ejective q',
    'shin': 'no Greek letter for /ʃ/',
    'chin': 'no Greek letter for /tʃ/',
    'tsan': 'no Greek letter for /ts/',
    'dzil': 'no Greek letter for /dz/',
    "ts'il": 'no Greek letter for the aspirated ts',
    "ch'ar": 'no Greek letter for the aspirated affricate',
    'khan': 'the /x/ letter (khan): Greek’s fricative seat is '
            'already claimed by kan (the classical aspirate pair); '
            'printed as a gap, not a second claim',
    'khar': 'the obsolete khar letter (7000): no Greek pair stands '
            'in the shared grid',
    'jan': 'no Greek letter for /dʒ/',
    'hae': 'Greek seats no /h/ letter in the numeral grid',
    'hoe': 'the obsolete long-o letter (hoe, 10000): its sound '
           'pair would be ω, beyond the shared grid — printed in '
           'the extension block of the testimony',
}
GEO_HEBREW = {
    'an': ('א', 'sound', 'the head of the abjad'),
    'ban': ('ב', 'sound', 'the shared second seat'),
    'gan': ('ג', 'sound', 'the shared third seat'),
    'don': ('ד', 'sound', 'the shared fourth seat'),
    'en': ('ה', 'seat', 'the abjad’s fifth seat; the sound '
                        'parts (a vowel against /h/) — a seat pair'),
    'vin': ('ו', 'sound', 'the waw line: /w/ seated as v'),
    'zen': ('ז', 'sound', 'the shared zayin sound'),
    'tan': ('ט', 'sound', 'the t line, ninth in both'),
    'in': ('י', 'sound', 'the yod sound'),
    "k'an": ('כ', 'sound', 'the k line against kap'),
    'las': ('ל', 'sound', 'the shared lamed'),
    'man': ('מ', 'sound', 'the shared mem'),
    'nar': ('נ', 'sound', 'the shared nun'),
    'on': (None, 'gap', 'the o vowel — the abjad has no o letter; '
                        'its value 70 coincides with ʿayin’s '
                        'seat, printed as a coincidence, not a pair'),
    "p'ar": ('פ', 'sound', 'the p line against pe'),
    'rae': ('ר', 'sound', 'the r against resh'),
    'san': ('ס', 'sound', 'the plain /s/ against samekh (the '
                           'tradition’s other s, ש, is /ʃ/ '
                           'and is not this letter’s pair)'),
    "t'ar": ('ת', 'sound', 'the t line against taw'),
    'par': ('פ', 'doublet', 'the aspirated p against the same pe'),
    'kan': ('ק', 'sound', 'the back k against qof'),
    'khan': ('ח', 'sound', 'the /x/ fricative against ħet'),
    'hae': ('ה', 'doublet', 'the /h/ letter against the same he'),
}
GEO_HEBREW_GAPS = {
    'he': 'no Hebrew letter for the long e',
    'yad': 'no Hebrew letter for the yad letter',
    'zhan': 'no Hebrew letter for /ʒ/',
    'vie': 'the obsolete w-letter: the waw seat is claimed by vin '
           'in this alignment — printed as a gap',
    'un': 'the abjad has no u vowel letter',
    'ghan': 'no Hebrew letter for /ʁ/',
    "q'ar": 'the ejective q: the qof seat is claimed by kan in '
            'this alignment — printed as a gap',
    'shin': 'no Hebrew letter for /ʃ/ (shin is /ʃ/ in its later '
            'reading but stands in the tradition as the sh of the '
            'abjad’s own s-line; printed as a gap rather '
            'than a contested claim)',
    'chin': 'no Hebrew letter for /tʃ/',
    'tsan': 'the ts sound: its abjad pair would be ṣadē, whose '
            'Georgian sound-heir by the fricative line is not '
            'this letter — printed as a gap',
    'dzil': 'no Hebrew letter for /dz/',
    "ts'il": 'no Hebrew letter for the aspirated ts',
    "ch'ar": 'no Hebrew letter for the aspirated affricate',
    'khar': 'the obsolete khar letter: no Hebrew pair',
    'jan': 'no Hebrew letter for /dʒ/',
    'hoe': 'the obsolete long-o letter: no Hebrew pair',
}


def testimony(branch, table_rows, key_field, pairs, gaps, parent_bank,
              parent_cap, parent_name):
    """Compute one testimony signature. table_rows: the script's own
    frozen table (CSV rows); key_field: the transliteration/name
    column; pairs/gaps: the alignment above; parent_bank: the living
    dict; parent_cap: the parent grid's maximum."""
    greek_special = {'Ϝ': 6}   # digamma: priced by the Phoenician map
    ext = 0
    for row in table_rows:
        key = row[key_field]
        letter = row.get('letter') or row.get('uppercase')
        val_raw = row.get('value', '')
        if val_raw == '' or val_raw is None:
            continue                      # the late annex — not classical
        bv = int(val_raw)
        if key in pairs:
            pl, kind, why = pairs[key]
            if pl is None:
                add(branch, key, '', None, letter, bv, 'GAP-NO-PARENT',
                    kind, why)
                continue
            pv = parent_bank.get(pl, greek_special.get(pl))
            assert pv is not None, f'{branch}: no parent value for {pl}'
            if bv > parent_cap:
                ext += 1
                add(branch, key, pl, pv, letter, bv, 'EXTENSION', kind,
                    why + f' — beyond the {parent_name} grid\u2019s cap '
                          f'({parent_cap}): the branch counts its own '
                          'alphabet here; printed, excluded from the '
                          'agreement count')
            else:
                add(branch, key, pl, pv, letter, bv, 'COMPUTED', kind,
                    why)
        elif key in gaps:
            add(branch, key, '', None, letter, bv, 'GAP-NO-PARENT',
                'none', gaps[key])
    covered = sum(1 for r in ROWS if r['branch'] == branch)
    valued = sum(1 for row in table_rows
                 if row.get('value') not in ('', None))
    assert covered == valued, (f'{branch}: {covered} register rows '
                               f'against {valued} valued letters — '
                               'a letter fell out of the alignment')
    s = summarise(branch)
    s['extension_rows'] = ext
    # in-grid agreement statistics (EXTENSION rows excluded by status)
    ingrid = [r for r in ROWS if r['branch'] == branch
              and r['status'] in ('AGREE', 'OFFSET')]
    s['ingrid_pairs'] = len(ingrid)
    s['ingrid_agree'] = sum(1 for r in ingrid if r['offset'] == 0)
    s['ingrid_delta1'] = sum(1 for r in ingrid if abs(r['offset']) == 1)
    return s


def branch_testimony():
    arm_rows = read_csv(TWELVE / 'armenian-table.csv')
    geo_rows = read_csv(CAUCASUS / 'georgian-table.csv')
    testimony('armenian-vs-greek', arm_rows, 'transliteration',
              ARM_GREEK, ARM_GREEK_GAPS, GREEK, 900, 'Milesian')
    testimony('armenian-vs-hebrew', arm_rows, 'transliteration',
              ARM_HEBREW, ARM_HEBREW_GAPS, HEBREW, 400, 'Hebrew')
    testimony('georgian-vs-greek', geo_rows, 'name',
              GEO_GREEK, GEO_GREEK_GAPS, GREEK, 900, 'Milesian')
    testimony('georgian-vs-hebrew', geo_rows, 'name',
              GEO_HEBREW, GEO_HEBREW_GAPS, HEBREW, 400, 'Hebrew')


# =============================================================================
# BRANCH 7 — THE LIMIT CASES. No offsets are computed: each prints
# the reason at the register's boundary, at full size.
# =============================================================================
def branch_limits():
    B = 'limit-cases'
    add(B, 'kana', '', None, '', None, 'NO-PARENT-BANK', 'none',
        'kana is a notation seat: its letters descend from Chinese '
        'characters, and the house seats Chinese as a reader only — '
        'no Chinese value bank stands in the engine, so there is no '
        'parent value for an offset to part from. The kana mint\u2019s '
        'own values are the branch\u2019s internal affair.')
    add(B, 'hangul', '', None, '', None, 'NO-PARENT-BANK', 'none',
        'hangul is a featural invention (1443/46): designed, not '
        'descended. Its jamo values are its own mint\u2019s law. A '
        'script with no parent has no offset — it is its own root.')
    add(B, 'geez-halehame', '', None, '', None, 'NO-PARENT-BANK',
        'none', 'the Ge\u2019ez line\u2019s parent is the South '
        'Arabian (Musnad) stock, which stands in no in-house bank; '
        'the gap prints. (The halehame witness against the Ge\u2019ez '
        'mint is one tongue\u2019s internal affair — a witness '
        'relation, not a branch offset — and is not computed here.)')
    summarise(B)


# =============================================================================
# PATTERNS — fit AFTER the offsets exist; every law states the
# residuals it was fit against, and its killing evidence rides in
# the register text. Signed offsets: an offset whose magnitude is
# itself a seat value of the branch's own grid.
# =============================================================================
ROMAN_SEATS = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
               500: 'D', 1000: 'M'}


def signed_offsets():
    out = []
    for r in ROWS:
        if r['offset'] in (None, 0):
            continue
        mag = abs(r['offset'])
        seat = None
        if r['branch'] in ('greek-latin', 'greek-latin-agrippa'):
            seat = ROMAN_SEATS.get(mag)
            grid = 'the Roman numeral seats'
        elif r['branch'] == 'greek-glagolitic':
            if mag in set(GLAGOLITIC.values()):
                seat = f'the Glagolitic seat of value {mag}'
                grid = 'the branch\u2019s own grid'
        elif r['branch'].startswith(('armenian', 'georgian')):
            # The testimony grids hold every class value, so a
            # magnitude that merely coincides with a seat proves
            # nothing there. Only the unit is signed in testimony:
            # the founder's delta-1 species, the offset that is the
            # branch's own first seat.
            if mag == 1:
                seat = 'the unit — the branch\u2019s own first seat'
                grid = 'the branch\u2019s own grid'
        if seat:
            out.append({'branch': r['branch'], 'seat': r['seat'],
                        'offset': r['offset'], 'signed_as': seat,
                        'grid': grid})
    return out


def patterns():
    P = {}
    # Greek -> Latin (ordinal): the tens law and the hundreds law.
    lat = {r['seat']: r for r in ROWS if r['branch'] == 'greek-latin'
           and r['offset'] is not None}
    phoen = {r['n']: r for r in read_csv(PHOENICIAN_CSV)}
    tens = [('11', 1), ('12', 2), ('13', 3), ('14', 4)]   # κ λ μ ν rows
    P['latin_tens_law'] = {
        'law': 'offset = -9j at the j-th inherited tens seat',
        'residuals': {n: lat[n]['offset'] + 9 * j for n, j in tens},
    }
    hunds = [('20', 1), ('21', 2), ('22', 3)]             # ρ σ τ rows
    P['latin_hundreds_law'] = {
        'law': 'offset = 17 - 99j at the j-th inherited hundreds seat',
        'residuals': {n: lat[n]['offset'] - (17 - 99 * j)
                      for n, j in hunds},
    }
    ag = [r for r in ROWS if r['branch'] == 'greek-latin-agrippa'
          and r['offset'] is not None]
    tens_ag = [r['offset'] for r in ag if r['seat'] in
               ('11', '12', '13', '14')]
    P['agrippa_tens_constant'] = {
        'law': 'a constant offset at the four inherited tens seats',
        'values': tens_ag,
        'constant': tens_ag[0] if len(set(tens_ag)) == 1 else None,
    }
    # Glagolitic units staircase against the insertion count.
    gla = [r for r in ROWS if r['branch'] == 'greek-glagolitic'
           and r['offset'] is not None]
    P['glagolitic_units'] = {
        'rows': [(r['seat'], r['offset']) for r in gla],
    }
    return P


def main():
    branch_cyrillic()
    branch_glagolitic()
    branch_coptic()
    branch_aramaic()
    branch_latin()
    branch_testimony()
    branch_limits()
    SUMMARY['_patterns'] = patterns()
    SUMMARY['_signed_offsets'] = signed_offsets()
    with open(HERE / 'branch_offsets.csv', 'w', encoding='utf-8',
              newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(ROWS[0].keys()))
        w.writeheader()
        w.writerows(ROWS)
    with open(HERE / 'branch_offsets_summary.json', 'w',
              encoding='utf-8') as fh:
        json.dump(SUMMARY, fh, ensure_ascii=False, indent=1)
    for b, s in SUMMARY.items():
        if b.startswith('_'):
            continue
        print(f"{b:22s} rows={s['rows']:3d} computed={s['computed']:3d} "
              f"agree={s['agree']:3d} offset={s['offset']:3d} "
              f"hist={s['histogram']}")
    print('\nPATTERNS:', json.dumps(SUMMARY['_patterns'],
                                   ensure_ascii=False))
    print('\nSIGNED OFFSETS:')
    for so in SUMMARY['_signed_offsets']:
        print(' ', so)


if __name__ == '__main__':
    main()
