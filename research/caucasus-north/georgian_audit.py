#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — georgian_audit.py — the Georgian Phase I audit: data builder
# Companion to THE-GEORGIAN-FIELD-PHASE-I-AUDIT.md (the audit document of
# record) and the first phase of the Caucasus-and-the-North road.
#
# Epigraph: "There is no zero: values are added from largest to smallest."
# — georgianalphabet.com, "Numeral letters" (the system's own shape, in
# one line).
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
#   Hypothesis: (i) the traditional Georgian letter-numeral table — the
#     classical 38-letter alphabet at decimal class values running to a
#     native 10,000 seat — can be re-sourced sign by sign from independent
#     witnesses that agree entire, every cell verified against the Unicode
#     standard and against the class law the table obeys; (ii) the class
#     law will be found to part from the clean digit x 10^class seat law
#     at exactly one coordinate, the doubled 400; (iii) set beside the
#     Armenian bank at coordinates, the two designed alphabets of the
#     Caucasus will show where same-shaped systems agree and where they
#     part — the control case the founder ordered for this region.
#   Method: (1) transcribe the table from TWO witnesses read entire on
#     2026-11-24 (Wikipedia, "Georgian numerals", its "Numeric values of
#     letters" table, sourced there to Makharoblidze 2009; and
#     georgianalphabet.com, its per-letter value cards for the modern 33
#     and its "Numeral letters" section for the five obsolete letters)
#     and diff them cell by cell in code — a disagreement aborts the
#     build as a finding, never averages away; (2) verify every glyph
#     against the Unicode standard's names; (3) verify the dress
#     coordinate — the older scripts' blocks (Asomtavruli capitals,
#     Nuskhuri smalls) matched to the seated Mkhedruli letters by the
#     standard's own letter names; (4) recompute the witnesses' worked
#     examples before trusting any derived number; (5) compute the
#     control case against the living ARMENIAN bank in code.
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and replay the Georgian Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. The values below are
TRANSCRIPTIONS of a published, attested table, carried with their sources
on their face; the control-case table is a comparison at coordinates, not
a verdict. No value here is presented as the house's doctrine, and no row
enters pontifex/engine.py from this file — the seat, if the gate holds,
is built separately and proven against the CSV this builder freezes.

MECHANISM: two CSVs are written beside this script —
  georgian-table.csv         the 38 classical letters at their values
                             (status SOURCED), each row carrying its
                             Mkhedruli codepoint and Unicode name, its
                             Asomtavruli and Nuskhuri partners as the
                             standard names them, its class, and its
                             standing (living / obsolete);
  georgian-control-case.csv  Georgian vs Armenian per shared class
                             value (36 rows), plus the boundary rows
                             where the two systems part in kind.
The companion battery georgian_audit_tests.py re-derives every number
the audit document prints from these CSVs and from its own independent
source constants.
"""

import csv
import os
import sys
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from pontifex.tables import ARMENIAN  # the control case's living bank

# -- Witness 1: Wikipedia, "Georgian numerals" (read entire 2026-11-24) ------
# The "Numeric values of letters" table, in the OLD alphabet's order as
# printed there (the obsolete letters interleaved at their classical
# seats). Transcribed as (letter, value) pairs in printed order.
W1 = [
    ('ა', 1), ('ბ', 2), ('გ', 3), ('დ', 4), ('ე', 5), ('ვ', 6), ('ზ', 7),
    ('ჱ', 8), ('თ', 9),
    ('ი', 10), ('კ', 20), ('ლ', 30), ('მ', 40), ('ნ', 50), ('ჲ', 60),
    ('ო', 70), ('პ', 80), ('ჟ', 90),
    ('რ', 100), ('ს', 200), ('ტ', 300), ('ჳ', 400), ('უ', 400),
    ('ფ', 500), ('ქ', 600), ('ღ', 700), ('ყ', 800), ('შ', 900),
    ('ჩ', 1000), ('ც', 2000), ('ძ', 3000), ('წ', 4000), ('ჭ', 5000),
    ('ხ', 6000), ('ჴ', 7000), ('ჯ', 8000), ('ჰ', 9000),
    ('ჵ', 10000),
]
# W1's own worked examples, as printed: the running text's three and the
# Motsameta inscription caption's one.
W1_EXAMPLES = {'ჩღჲთ': 1769, 'ჩყპზ': 1887, 'ციბ': 2012, 'ჩყმვ': 1846}
# W1's unvalued tail, as printed: "These letters have no numerical value."
W1_UNVALUED = ['ჶ', 'ჷ', 'ჸ', 'ჹ', 'ჺ', 'ჼ', '჻']

# -- Witness 2: georgianalphabet.com (read entire 2026-11-24) -----------------
# The per-letter cards give the MODERN 33 in modern order (the obsolete
# five absent from the sequence); the "Numeral letters" section and the
# FAQ give the five obsolete letters at their values, and state that ჳ's
# 400 is "shared with უ". Transcribed as a letter -> value map.
W2 = {
    'ა': 1, 'ბ': 2, 'გ': 3, 'დ': 4, 'ე': 5, 'ვ': 6, 'ზ': 7, 'თ': 9,
    'ი': 10, 'კ': 20, 'ლ': 30, 'მ': 40, 'ნ': 50, 'ო': 70, 'პ': 80,
    'ჟ': 90, 'რ': 100, 'ს': 200, 'ტ': 300, 'უ': 400, 'ფ': 500,
    'ქ': 600, 'ღ': 700, 'ყ': 800, 'შ': 900, 'ჩ': 1000, 'ც': 2000,
    'ძ': 3000, 'წ': 4000, 'ჭ': 5000, 'ხ': 6000, 'ჯ': 8000, 'ჰ': 9000,
    'ჱ': 8, 'ჲ': 60, 'ჳ': 400, 'ჴ': 7000, 'ჵ': 10000,
}
# W2's own worked example, as printed (its numeral converter):
# "2026, ცკვ, 2,000 ც, + 20 კ, + 6 ვ".
W2_EXAMPLES = {'ცკვ': 2026}

OBSOLETE = {'ჱ', 'ჲ', 'ჳ', 'ჴ', 'ჵ'}  # dropped in the 1860s reform (W2)

# Transliterated letter names, for the record's readability; the Unicode
# standard's names are frozen beside them in the CSV as the verification
# witness, and the battery holds the two together.
NAMES = {
    'ა': 'an', 'ბ': 'ban', 'გ': 'gan', 'დ': 'don', 'ე': 'en', 'ვ': 'vin',
    'ზ': 'zen', 'ჱ': 'he', 'თ': 'tan', 'ი': 'in', 'კ': "k'an", 'ლ': 'las',
    'მ': 'man', 'ნ': 'nar', 'ჲ': 'yad', 'ო': 'on', 'პ': "p'ar", 'ჟ': 'zhan',
    'რ': 'rae', 'ს': 'san', 'ტ': "t'ar", 'ჳ': 'vie', 'უ': 'un', 'ფ': 'par',
    'ქ': 'kan', 'ღ': 'ghan', 'ყ': "q'ar", 'შ': 'shin', 'ჩ': 'chin',
    'ც': 'tsan', 'ძ': 'dzil', 'წ': "ts'il", 'ჭ': "ch'ar", 'ხ': 'khan',
    'ჴ': 'khar', 'ჯ': 'jan', 'ჰ': 'hae', 'ჵ': 'hoe',
}


def weigh(table, word):
    return sum(table[ch] for ch in word)


def main():
    # -- The diff: the two witnesses, cell by cell -------------------------
    w1 = dict(W1)
    assert len(W1) == 38 and len(w1) == 38, 'W1 must carry 38 seats'
    assert set(w1) == set(W2), (
        'WITNESS PARTING — letter sets differ: %r vs %r'
        % (sorted(set(w1) - set(W2)), sorted(set(W2) - set(w1))))
    partings = [(ch, w1[ch], W2[ch]) for ch in w1 if w1[ch] != W2[ch]]
    assert not partings, 'WITNESS PARTING — values differ: %r' % (partings,)
    print('WITNESS DIFF — W1 (Wikipedia) vs W2 (georgianalphabet.com): '
          '38/38 letters, 38/38 values AGREE')

    table = w1  # the agreed table, in W1's classical order below

    # -- The witnesses' examples, recomputed before anything derived ------
    for word, expect in list(W1_EXAMPLES.items()) + list(W2_EXAMPLES.items()):
        got = weigh(table, word)
        assert got == expect, 'EXAMPLE FAILS: %s %d != %d' % (word, got, expect)
    print('EXAMPLES — the witnesses\' five worked numbers recompute '
          'exact (1769, 1887, 2012, 1846, 2026)')

    # -- Unicode verification + the dress coordinate -----------------------
    # MECHANISM: the standard names the Mkhedruli letters GEORGIAN LETTER
    # X, the Asomtavruli GEORGIAN CAPITAL LETTER X, the Nuskhuri GEORGIAN
    # SMALL LETTER X. The dress partners are matched by that name suffix,
    # in code — the correspondence is the standard's, not the scribe's.
    caps = {}
    smalls = {}
    for cp in range(0x10A0, 0x10C6):
        n = ud.name(chr(cp), '')
        if n.startswith('GEORGIAN CAPITAL LETTER '):
            caps[n[len('GEORGIAN CAPITAL LETTER '):]] = chr(cp)
    for cp in range(0x2D00, 0x2D26):
        n = ud.name(chr(cp), '')
        if n.startswith('GEORGIAN SMALL LETTER '):
            smalls[n[len('GEORGIAN SMALL LETTER '):]] = chr(cp)
    rows = []
    order = [ch for ch, _ in W1]
    for pos, ch in enumerate(order, start=1):
        name = ud.name(ch)
        assert name.startswith('GEORGIAN LETTER '), (ch, name)
        suffix = name[len('GEORGIAN LETTER '):]
        asom = caps.get(suffix, '')
        nusk = smalls.get(suffix, '')
        if pos <= 9:
            klass, power = 'units', 0
        elif pos <= 18:
            klass, power = 'tens', 1
        elif pos <= 28:
            klass, power = 'hundreds', 2
        elif pos <= 37:
            klass, power = 'thousands', 3
        else:
            klass, power = 'ten-thousands', 4
        rows.append({
            'position': pos, 'letter': ch,
            'codepoint': 'U+%04X' % ord(ch), 'unicode_name': name,
            'asomtavruli': asom,
            'asomtavruli_codepoint': ('U+%04X' % ord(asom)) if asom else '',
            'nuskhuri': nusk,
            'nuskhuri_codepoint': ('U+%04X' % ord(nusk)) if nusk else '',
            'name': NAMES[ch], 'value': table[ch],
            'class': klass, 'class_power': power,
            'standing': 'obsolete' if ch in OBSOLETE else 'living',
            'status': 'SOURCED',
        })
    dressed = sum(1 for r in rows if r['asomtavruli'] and r['nuskhuri'])
    print('DRESS — Unicode names verified 38/38; Asomtavruli + Nuskhuri '
          'partners matched by the standard\'s names at %d/38 seats'
          % dressed)

    # -- The class law, both formulations ----------------------------------
    # (a) every value decomposes as digit x 10^class, digit 1..9;
    # (b) the seat law: digit == within-class seat index.
    decomp = all(1 <= r['value'] // (10 ** r['class_power']) <= 9
                 and r['value'] % (10 ** r['class_power']) == 0
                 for r in rows)
    seat_law_fail = []
    counters = {}
    for r in rows:
        counters[r['class']] = counters.get(r['class'], 0) + 1
        digit = r['value'] // (10 ** r['class_power'])
        if digit != counters[r['class']]:
            seat_law_fail.append((r['position'], r['letter'],
                                  counters[r['class']], digit, r['value']))
    print('CLASS LAW — decomposition (a): %s at 38/38; seat law (b): '
          'parts at %r' % ('HOLDS' if decomp else 'FAILS', seat_law_fail))
    distinct = len(set(table.values()))
    print('EXTENT — 38 letters, %d distinct values, sum %d, '
          'maximum letter %d' % (distinct, sum(table.values()),
                                 max(table.values())))

    with open(os.path.join(HERE, 'georgian-table.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # -- The control case against Armenian, computed ------------------------
    arm_by_value = {}
    for ch, v in ARMENIAN.items():
        arm_by_value.setdefault(v, []).append(ch)
    geo_by_value = {}
    for ch, v in table.items():
        geo_by_value.setdefault(v, []).append(ch)
    cc = []
    for v in sorted(set(arm_by_value) | set(geo_by_value)):
        cc.append({
            'value': v,
            'georgian_letters': ''.join(geo_by_value.get(v, [])),
            'georgian_seats': len(geo_by_value.get(v, [])),
            'armenian_letters': ''.join(arm_by_value.get(v, [])),
            'armenian_seats': len(arm_by_value.get(v, [])),
            'relation': ('AGREE' if v in arm_by_value and v in geo_by_value
                         and len(geo_by_value[v]) == len(arm_by_value[v])
                         else 'PART'),
        })
    with open(os.path.join(HERE, 'georgian-control-case.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(cc[0].keys()))
        w.writeheader()
        w.writerows(cc)
    shared = [r for r in cc if r['relation'] == 'AGREE']
    print('CONTROL CASE — value seats shared with Armenian: %d AGREE, '
          'partings at %r' % (len(shared),
                              [(r['value'], r['georgian_seats'],
                                r['armenian_seats']) for r in cc
                               if r['relation'] == 'PART']))
    print('BUILT — georgian-table.csv (38 rows), '
          'georgian-control-case.csv (%d rows)' % len(cc))


if __name__ == '__main__':
    main()
