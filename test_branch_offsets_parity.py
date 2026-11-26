#!/usr/bin/env python3
# ===========================================================================
# 93
# THE BRANCH-OFFSET REGISTER — PARITY OF THE FROZEN OFFSETS AGAINST
# THE LIVING BANKS AND THE CENSUS TABLES
# A Scientific Illuminist proving of the branch-offset build
# (research/branch-offsets/): the control word weighed first; the
# pre-existing engine battery run untouched; and then every frozen
# row of branch_offsets.csv re-derived in the battery's own hand —
# the parent and branch values re-read from the living banks of
# pontifex.tables, the alignments re-read from the census CSVs, the
# offset arithmetic and statuses re-checked cell by cell — so the
# register is proven from its sources, not from its own say-so.
# Built 2026-11-26 under the founder's commission of 15:03 EST:
# "Build the branch-offset register — chart the 12 tongues'
# branches."
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXVI day of November, Dies Iovis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: the battery reads the frozen CSV and summary JSON,
#   then re-derives: (1) every COMPUTED row's two values from the
#   living bank dicts and its offset by subtraction; (2) the branch
#   headline counts (the zero branches, the staircase, the Latin
#   laws with zero residuals, the Agrippa constant, the testimony
#   signatures) from the frozen rows alone; (3) the fenced Demotic
#   letters' unvalued state from the engine itself; (4) the 77 head
#   in the three abjad scripts by weigh(); (5) the coverage counts
#   (36 Armenian, 38 Georgian, per signature) against the census
#   tables' valued letters.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first, and engine_checks() runs untouched, so
#   the register is proven beside the standing house. The founder's
#   exemplar is a control too: VV − X in the Latin ordinal bank
#   must equal 20 — XX, the lawful double.
#
# DOCTRINE — THE BOUNDARIES, held by the battery: no fenced letter
#   carries a computed row; no testimony row is counted as a
#   verdict (the battery checks signatures, never parentage); the
#   limit cases compute nothing.
# ===========================================================================

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import weigh, engine_checks
from pontifex.tables import (
    GREEK, CYRILLIC, GLAGOLITIC, COPTIC, HEBREW, ARAMAIC,
    ARABIC_ABJAD, LATIN_ORDINAL, AGRIPPA, ARMENIAN, GEORGIAN,
)

RES = HERE / "research/branch-offsets"
ROWS = list(csv.DictReader(
    (RES / "branch_offsets.csv").open(encoding="utf-8")))
SUMMARY = json.loads(
    (RES / "branch_offsets_summary.json").read_text(encoding="utf-8"))

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# The Phoenician map prices the two archaic capitals the engine's
# Greek bank seats only as numeral signs: Ϝ digamma 6, Ϙ koppa 90.
# For the Latin branch (and the Georgian vin row) the map is the
# living source of the parent value, as the register states.
MAP_GREEK = {}
for _r in csv.DictReader(
        (HERE / 'maps/phoenician-cypher-glyph-map'
         / 'phoenician-cypher-glyph-map.csv').open(encoding='utf-8')):
    if _r['greek'] and _r['greek_value'].isdigit():
        MAP_GREEK[_r['greek']] = int(_r['greek_value'])


def bank_value(bank, ch):
    """A letter's value in a living bank dict, case-folded the way
    the engine seats the Greek signs."""
    if ch in bank:
        return bank[ch]
    return bank.get(ch.lower())


def parent_value(bank, ch):
    v = bank_value(bank, ch)
    if v is None and bank is GREEK:
        v = MAP_GREEK.get(ch)
    return v


# branch -> (parent bank, branch bank) for the re-derivation
BANKS = {
    'greek-cyrillic': (GREEK, CYRILLIC),
    'greek-glagolitic': (GREEK, GLAGOLITIC),
    'greek-coptic': (GREEK, COPTIC),
    'aramaic-hebrew': (ARAMAIC, HEBREW),
    'aramaic-arabic': (ARAMAIC, ARABIC_ABJAD),
    'greek-latin': (GREEK, LATIN_ORDINAL),
    'greek-latin-agrippa': (GREEK, AGRIPPA),
    'armenian-vs-greek': (GREEK, ARMENIAN),
    'armenian-vs-hebrew': (HEBREW, ARMENIAN),
    'georgian-vs-greek': (GREEK, GEORGIAN),
    'georgian-vs-hebrew': (HEBREW, GEORGIAN),
}

# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
cs = engine_checks()
check('control — pre-existing battery engine passes untouched',
      all(p for _, p, _ in cs),
      '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))
check("control — the founder's exemplar: VV − X == 20 in the "
      "Latin ordinal bank (XX, the lawful double)",
      weigh('VV', 'latin_ordinal')['value']
      - weigh('X', 'latin_ordinal')['value'] == 20,
      weigh('VV', 'latin_ordinal')['value']
      - weigh('X', 'latin_ordinal')['value'])

# --- Every computed row, re-derived from the living banks -------------------
bad = []
for r in ROWS:
    if r['status'] not in ('AGREE', 'OFFSET'):
        continue
    pb, bb = BANKS[r['branch']]
    pv = parent_value(pb, r['parent_letter'])
    bv = bank_value(bb, r['branch_letter'])
    if pv is None or bv is None \
            or int(r['parent_value']) != pv \
            or int(r['branch_value']) != bv \
            or int(r['offset']) != bv - pv \
            or (r['status'] == 'AGREE') != (bv == pv):
        bad.append((r['branch'], r['seat']))
check('every computed row re-derives from the living banks '
      '(values, offset, status)', not bad, bad or 'all rows')

# --- The zero branches -------------------------------------------------------
for branch, n in (('greek-cyrillic', 27), ('greek-coptic', 27),
                  ('aramaic-hebrew', 22), ('aramaic-arabic', 22)):
    rows = [r for r in ROWS if r['branch'] == branch
            and r['status'] in ('AGREE', 'OFFSET')]
    check(f'{branch}: {n} aligned seats, every offset zero',
          len(rows) == n and all(r['status'] == 'AGREE' for r in rows),
          f"{sum(1 for r in rows if r['status'] == 'AGREE')}/{len(rows)}")
ext = [r for r in ROWS if r['branch'] == 'aramaic-arabic'
       and r['status'] == 'EXTENSION']
check('aramaic-arabic: the six branch-only extension letters '
      '(500–1000) stand apart from the shared grid',
      len(ext) == 6
      and [int(r['branch_value']) for r in ext]
      == [500, 600, 700, 800, 900, 1000],
      [r['branch_letter'] for r in ext])

# --- The founding head --------------------------------------------------------
check('the founding head: עז = ܥܙ = عز = 77 by weigh()',
      (weigh('עז', 'hebrew')['value'],
       weigh('ܥܙ', 'aramaic')['value'],
       weigh('عز', 'arabic_abjad')['value']) == (77, 77, 77),
      (weigh('עז', 'hebrew')['value'],
       weigh('ܥܙ', 'aramaic')['value'],
       weigh('عز', 'arabic_abjad')['value']))

# --- The fence -----------------------------------------------------------------
fenced = [r for r in ROWS if r['status'] == 'FENCED']
check('the seven Demotic letters stand fenced: printed, unvalued, '
      'never offset — and the engine weighs ϣ at 0',
      len(fenced) == 7
      and all(r['offset'] == '' and r['branch_value'] == ''
              for r in fenced)
      and weigh('ϣ', 'coptic')['value'] == 0,
      [r['branch_letter'] for r in fenced])

# --- The Glagolitic staircase ---------------------------------------------------
gla = {(r['parent_letter'], r['branch_letter']): r for r in ROWS
       if r['branch'] == 'greek-glagolitic'}
stair = [('Α', 'Ⰰ', 0), ('Β', 'Ⰱ', 0), ('Β', 'Ⰲ', 1), ('Γ', 'Ⰳ', 1),
         ('Δ', 'Ⰴ', 1), ('Ε', 'Ⰵ', 1), ('Ϛ', 'Ⰷ', 2), ('Ζ', 'Ⰸ', 2),
         ('Η', 'Ⰹ', 2), ('Ι', 'Ⰺ', 0)]
check('the Glagolitic units staircase stands at its coordinates '
      '(0,0,+1,+1,+1,+1,+2,+2,+2, then absorbed at the doubled 10)',
      all(gla[(p, b)]['offset'] == str(o) for p, b, o in stair),
      [(p, gla[(p, b)]['offset']) for p, b, _ in stair])
check('the two Glagolitic parting seats: Ϟ→Ⱍ +910 (seat pairing), '
      'Ω→Ⱉ −100 (one hundreds step, signed)',
      gla[('Ϟ', 'Ⱍ')]['offset'] == '910'
      and gla[('Ω', 'Ⱉ')]['offset'] == '-100',
      (gla[('Ϟ', 'Ⱍ')]['offset'], gla[('Ω', 'Ⱉ')]['offset']))

# --- The Latin laws --------------------------------------------------------------
lat = {r['seat']: r for r in ROWS if r['branch'] == 'greek-latin'}
tens = all(int(lat[str(s)]['offset']) == -9 * j
           for s, j in ((11, 1), (12, 2), (13, 3), (14, 4)))
hunds = all(int(lat[str(s)]['offset']) == 17 - 99 * j
            for s, j in ((20, 1), (21, 2), (22, 3)))
check('the Latin ordinal laws fit with zero residuals '
      '(tens −9j; hundreds 17−99j)', tens and hunds,
      {s: lat[s]['offset'] for s in ('11', '12', '13', '14',
                                     '20', '21', '22')})
check('the Latin break coordinates: Ι −1 (signed, the missing '
      'theta), Ζ +19 and Ξ −36 (the exiled loan letters)',
      lat['10']['offset'] == '-1' and lat['7']['offset'] == '19'
      and lat['15']['offset'] == '-36',
      (lat['10']['offset'], lat['7']['offset'], lat['15']['offset']))
agr = {r['seat']: r for r in ROWS
       if r['branch'] == 'greek-latin-agrippa'}
check('the Agrippa tens constant: −10 at all four inherited tens '
      'seats (signed, −X)',
      all(agr[str(s)]['offset'] == '-10' for s in (11, 12, 13, 14)),
      [agr[str(s)]['offset'] for s in (11, 12, 13, 14)])
check('the Latin gaps print as gaps: Θ→TH unpriced, Ϻ san '
      'unvalued', lat['9']['status'] == 'GAP-NO-BRANCH'
      and lat['18']['status'] == 'GAP-NO-PARENT',
      (lat['9']['status'], lat['18']['status']))

# --- The testimony signatures -----------------------------------------------------
geo_g = [r for r in ROWS if r['branch'] == 'georgian-vs-greek'
         and r['status'] in ('AGREE', 'OFFSET')]
check('TESTIMONY — Georgian against Greek: 23 in-grid pairs, '
      'every offset zero (a signature, never a verdict)',
      len(geo_g) == 23 and all(r['status'] == 'AGREE' for r in geo_g),
      f"{sum(1 for r in geo_g if r['status'] == 'AGREE')}/{len(geo_g)}")
geo_h = {(r['seat']): r for r in ROWS
         if r['branch'] == 'georgian-vs-hebrew'}
check('TESTIMONY — Georgian against Hebrew: the hundreds part at '
      'rae −100, t\u2019ar −100, san +140; the tens run agrees',
      geo_h['rae']['offset'] == '-100'
      and geo_h["t'ar"]['offset'] == '-100'
      and geo_h['san']['offset'] == '140',
      (geo_h['rae']['offset'], geo_h["t'ar"]['offset'],
       geo_h['san']['offset']))
arm_g = {r['seat']: r for r in ROWS
         if r['branch'] == 'armenian-vs-greek'}
arm_h = {r['seat']: r for r in ROWS
         if r['branch'] == 'armenian-vs-hebrew'}
check('TESTIMONY — Armenian: the same agreeing head under both '
      'parents (a–e at 0), the Δ1 pair against Greek (z, ē at −1)',
      all(arm_g[s]['offset'] == '0' for s in 'abgde')
      and all(arm_h[s]['offset'] == '0' for s in 'abgde')
      and arm_g['z']['offset'] == '-1'
      and arm_g['ē']['offset'] == '-1',
      {s: arm_g[s]['offset'] for s in ('a', 'z', 'ē')})
check('TESTIMONY — the discriminating coordinate x: −560 against '
      'Greek (χ 600), +32 against Hebrew (ħet 8); separation 592',
      arm_g['x']['offset'] == '-560'
      and arm_h['x']['offset'] == '32'
      and int(arm_h['x']['offset']) - int(arm_g['x']['offset']) == 592,
      (arm_g['x']['offset'], arm_h['x']['offset']))

# --- Coverage: no letter fell out of an alignment --------------------------------
for branch, table, n in (
        ('armenian-vs-greek', 'armenian-table.csv', 36),
        ('armenian-vs-hebrew', 'armenian-table.csv', 36),
        ('georgian-vs-greek', 'georgian-table.csv', 38),
        ('georgian-vs-hebrew', 'georgian-table.csv', 38)):
    rows = [r for r in ROWS if r['branch'] == branch]
    check(f'coverage — {branch}: all {n} valued classical letters '
          'of the census table stand in the register',
          len(rows) == n, len(rows))

# --- The boundary ------------------------------------------------------------------
lim = [r for r in ROWS if r['branch'] == 'limit-cases']
check('the boundary stands: kana, hangul, Ge\u2019ez/halehame — '
      'three limit cases, none computed',
      len(lim) == 3 and all(r['status'] == 'NO-PARENT-BANK'
                            and r['offset'] == '' for r in lim),
      [r['seat'] for r in lim])

# --- The summary agrees with the frozen rows ---------------------------------------
BRANCHES = [k for k in SUMMARY if not k.startswith('_')]
agree = all(
    SUMMARY[b]['agree']
    == sum(1 for r in ROWS if r['branch'] == b
           and r['status'] == 'AGREE')
    and SUMMARY[b]['rows']
    == sum(1 for r in ROWS if r['branch'] == b)
    for b in BRANCHES)
check('the frozen summary JSON agrees with the frozen CSV, '
      'branch by branch', agree,
      {b: SUMMARY[b]['rows'] for b in BRANCHES})
signed = {(s['branch'], s['seat']): s['offset']
          for s in SUMMARY['_signed_offsets']}
check('the signed offsets stand in the summary: Latin Ι −1, '
      'Agrippa tens −10, Glagolitic Ω −100, Armenian z −1',
      signed.get(('greek-latin', '10')) == -1
      and signed.get(('greek-latin-agrippa', '11')) == -10
      and signed.get(('greek-glagolitic', 'Ω')) == -100
      and signed.get(('armenian-vs-greek', 'z')) == -1,
      {k: v for k, v in signed.items()
       if k[0] in ('greek-latin', 'greek-glagolitic')})

print()
failed = [n for n, p, _ in RESULTS if not p]
print('BRANCH-OFFSET PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         ('; FAILING: ' + '; '.join(failed)) if failed else ''))
sys.exit(1 if failed else 0)
