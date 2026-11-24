#!/usr/bin/env python3
# ============================================================================
# 93
# THE GE'EZ MINT AND THE HALEHAME WITNESS — PARITY OF THE ENGINE SEAT
# AGAINST THE PHASE I AUDIT'S DATA SEAT
# A Scientific Illuminist proving of the two Ge'ez banks in the main
# engine (pontifex/pontifex) against the independent seat the Phase I
# audit built from the sources (research/twelve-tongues: the inventory
# and values CSVs, generated from the Unicode standard and the
# published Debtera table). The mint and the witness were minted at
# the desk on 2026-11-24 under the founder's hybrid law and his three
# standing rules — the road rule, the proof-enough rule, and the
# end-goal rule, under which halehame stands as WITNESS beside the
# mint (Phase I §VII Q1, settled at the desk, revisable by his pen).
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes from the two living seats —
#   the engine's banks (generated in tables.py by codepoint
#   arithmetic) and the audit's CSVs (generated independently in
#   geez_audit.py from the same sources, with Unicode-name
#   verification). Nothing is hard-coded from memory except the
#   doctrine's own printed numbers, which are cited to their pages.
#   The seats are compared as SETS with per-sign values, not as
#   sequences: the audit's CSV interleaves the eighth slot with its
#   base's row, the engine seats strata in blocks — two declared
#   traversals of one inventory, and set parity is the honest claim.
#
# DOCTRINE — THE CONTROLS: the engine's own control word (θέλημα
#   = 93) is weighed first; every pre-existing battery (engine,
#   greek, doubles, cubes, kana) is run and must pass untouched;
#   and the Phase I audit's own battery (25 checks) is run as a
#   subprocess — the witness instrument must still hold before its
#   data can witness anything.
#
# DOCTRINE — THE SEAM (S1/S3): every Ge'ez total names its bank
#   and its door. The head of the calibration, ክርስቶስ, is printed
#   at all four doors below: the practiced readings agree at 80 BY
#   CONSTRUCTION (the mint's first-form column IS halehame —
#   calibration, recorded as calibration, never as a bridge: the
#   two banks are calibrated, not independent, at that door), and
#   the protocol doors part at 70 against 490 across the order-6
#   boundary — the mint reading the Zero where the folk grid
#   prints ×6, the printed grid standing unaltered in the witness
#   (S4). The deltas are coordinates, exhibited at full size.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, geez, halehame, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks, halehame_checks,
)
from pontifex.tables import (
    GEEZ, GEEZ_FIRST, GEEZ_BASE, HALEHAME, HALEHAME_FIRST,
)
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks

AUDIT_DIR = HERE / 'research' / 'twelve-tongues'

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def mint_mult(order):
    # MECHANISM: the axis law restated independently in the battery
    # (M1/M3): the order's own number, corrected at order 6 to the
    # Zero. The battery holds the bank to the LAW as the instrument
    # states it, not to the builder's private copy of it.
    return 0 if order == 6 else order


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label
          if label not in ('geez', 'halehame') else
          'seat battery — %s_checks() passes' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'geez_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes (25 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat, read ---------------------------------------------
with open(AUDIT_DIR / 'geez-fidal-inventory.csv', encoding='utf-8') as fh:
    inventory = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'geez-halehame-values.csv', encoding='utf-8') as fh:
    folk_rows = list(csv.DictReader(fh))
FOLK = {r['base']: int(r['folk_value_first_form'])
        for r in folk_rows if r['status'] == 'SOURCED'}
check('the folk transcription stands in the data seat: 26 SOURCED rows',
      len(FOLK) == 26, len(FOLK))

strata = {}
for r in inventory:
    strata.setdefault(r['series'], []).append(r)
check('inventory strata as audited: 182 classical + 20 labiovelar-'
      'classical + 25 eighth-slot + 10 labiovelar-postclassical',
      {k: len(v) for k, v in strata.items()} ==
      {'classical': 182, 'labiovelar-classical': 20,
       'eighth-slot': 25, 'labiovelar-postclassical': 10},
      {k: len(v) for k, v in strata.items()})

# --- Sign for sign: the engine seat against the audit seat -------------------
bad = []
for r in strata['classical']:
    g, base, order = r['glyph'], r['base'], int(r['order'])
    fv = FOLK[base]
    if GEEZ.get(g) != fv * mint_mult(order):
        bad.append((g, 'mint', GEEZ.get(g), fv * mint_mult(order)))
    if HALEHAME.get(g) != fv * order:
        bad.append((g, 'witness', HALEHAME.get(g), fv * order))
    if GEEZ_FIRST.get(g) != fv or HALEHAME_FIRST.get(g) != fv:
        bad.append((g, 'first-form maps'))
    if unicodedata.name(g, '') != r['unicode_name']:
        bad.append((g, 'unicode name', unicodedata.name(g, ''),
                    r['unicode_name']))
check('all 182 grid signs: mint at first × m(order), witness at '
      'first × order, first-form maps at the folk value, glyphs the '
      'standard’s own', not bad, bad or '182/182 agree at both seats')

bad = []
for r in strata['labiovelar-classical']:
    g, base, order = r['glyph'], r['base'], int(r['order'])
    if GEEZ.get(g) != FOLK[base] * mint_mult(order):
        bad.append((g, 'mint', GEEZ.get(g)))
    if g in HALEHAME or g in HALEHAME_FIRST:
        bad.append((g, 'witness seats a labiovelar — GAP violated'))
check('all 20 classical labiovelars: seated in the mint under the '
      'axis; the witness’s GAP holds at both its maps', not bad,
      bad or '20/20 seated, 0 witnessed')

bad = []
for r in strata['eighth-slot']:
    g, base = r['glyph'], r['base']
    if GEEZ.get(g) != FOLK[base] * 8:
        bad.append((g, 'mint ΕΙ column', GEEZ.get(g), FOLK[base] * 8))
    if g in HALEHAME:
        bad.append((g, 'witness seats an eighth-slot glyph'))
check('all 25 eighth-slot glyphs: the mint’s ΕΙ column at first × 8; '
      'none in the witness', not bad, bad or '25/25 at ×8')

bad = [r['glyph'] for r in strata['labiovelar-postclassical']
       if r['glyph'] in GEEZ or r['glyph'] in HALEHAME]
check('the 10 post-classical labiovelars: seated in NEITHER bank '
      '(inventoried in the audit, unseated here)', not bad,
      bad or '0 seated')

seated_csv = {r['glyph'] for k in ('classical', 'labiovelar-classical',
                                   'eighth-slot') for r in strata[k]}
check('bank identity — engine GEEZ keys == the audit’s seated glyphs, '
      'key for key; GEEZ_BASE is that set in seating order',
      set(GEEZ) == seated_csv and set(GEEZ_BASE) == seated_csv
      and len(GEEZ_BASE) == 227,
      (len(GEEZ), len(seated_csv), len(GEEZ_BASE)))
check('bank identity — engine HALEHAME keys == the audit’s 182 grid '
      'glyphs, key for key',
      set(HALEHAME) == {r['glyph'] for r in strata['classical']},
      len(HALEHAME))
check('the classical surface: GEEZ_BASE’s first 202 seats are exactly '
      'the grid + labiovelar glyphs (the ΕΙ column rides after)',
      set(GEEZ_BASE[:202]) ==
      {r['glyph'] for k in ('classical', 'labiovelar-classical')
       for r in strata[k]},
      len(GEEZ_BASE[:202]))

# --- Calibration by construction: the first-form column ----------------------
firsts = [GEEZ_BASE[i * 7] for i in range(26)]
folk_list = [FOLK[g] for g in
             ['ሀ', 'ለ', 'ሐ', 'መ', 'ሠ', 'ረ', 'ሰ', 'ቀ', 'በ', 'ተ', 'ኀ', 'ነ',
              'አ', 'ከ', 'ወ', 'ዐ', 'ዘ', 'የ', 'ደ', 'ገ', 'ጠ', 'ጰ', 'ጸ', 'ፀ',
              'ፈ', 'ፐ']]
check('first-form identity — mint column == witness column == the '
      'published table, 26/26',
      [GEEZ[g] for g in firsts] == folk_list
      and [HALEHAME[g] for g in firsts] == folk_list,
      folk_list)

# --- The calibration heads, printed as the seam prints them (S3) -------------
HEADS = [
    # (word, mint-written, mint first-form, witness practiced,
    #  witness printed) — Phase II–III §III, the seam's table
    ('ክርስቶስ', 70, 80, 80, 490),
    ('ሰላም', 15, 13, 13, 39),
]
for w, mw, mf, wf, wp in HEADS:
    got = (weigh(w, 'geez')['value'], geez(w)['value'],
           halehame(w)['value'], weigh(w, 'halehame')['value'])
    check('head — %s at four doors: %d / %d / %d / %d' % (w, mw, mf, wf, wp),
          got == (mw, mf, wf, wp), got)
print('COORD — THE HEAD: ክርስቶስ agrees at the first-form doors at 80 '
      'BY CONSTRUCTION (calibration, not a bridge) and parts at the '
      'protocol doors — mint 70 as written (Δ −10 against the practiced '
      '80: its three order-6 signs read at the Zero), witness 490 as '
      'printed (the unexhibited multiplier’s arithmetic). Both deltas '
      'are the order-6 boundary, measured from two sides.')

# --- The corroborated exhibits ------------------------------------------------
EXHIBITS = [
    # (sign, mint-written, witness printed) — Bekerie via Daniels, and
    # the audit battery's spot checks; the axis agreement exhibits
    ('ሁ', 2, 2), ('ሉ', 4, 4), ('ቶ', 70, 70), ('ኄ', 100, 100),
    ('ፖ', 5600, 5600),
]
bad = [(s, weigh(s, 'geez')['value'], weigh(s, 'halehame')['value'])
       for s, mw, wp in EXHIBITS
       if weigh(s, 'geez')['value'] != mw
       or weigh(s, 'halehame')['value'] != wp]
check('multiplier exhibits: mint-written == witness-printed at ሁ, ሉ, '
      'ቶ, ኄ, ፖ (the axis agrees at every exhibited coordinate but one)',
      not bad, bad or '5/5 agree')

# --- The boundary, proven in code (M3/S3) --------------------------------------
check('THE BOUNDARY — order 6 in code: mint (ል, ፕ) == (0, 0); witness '
      'printed (12, 4800); both practiced doors read the bases (2, 800)',
      (GEEZ['ል'], GEEZ['ፕ'], HALEHAME['ል'], HALEHAME['ፕ'],
       geez('ል')['value'], halehame('ፕ')['value'])
      == (0, 0, 12, 4800, 2, 800),
      (GEEZ['ል'], GEEZ['ፕ'], HALEHAME['ል'], HALEHAME['ፕ']))
grid = [r['glyph'] for r in strata['classical']]
agree_printed = sum(1 for g in grid if GEEZ[g] == HALEHAME[g])
agree_practiced = sum(1 for g in grid if GEEZ[g] == HALEHAME_FIRST[g])
check('agreement counts on the 182: mint-written == witness-printed '
      'at 156 (all but order 6); == witness-practiced at exactly the '
      '26 first forms',
      (agree_printed, agree_practiced) == (156, 26),
      (agree_printed, agree_practiced))
print('COORD — THE BOUNDARY STANDS AT (order 6: key 0, folk ×6): of '
      'the 182 grid signs the two protocol readings agree at 156 and '
      'part at the 26 order-6 signs, nowhere else. The mint did not '
      'tune this: the parting is the single correction, and the '
      'witness’s side of it stands unaltered (S4).')

# --- The coverage coordinate ----------------------------------------------------
check('coverage — ኌ (labiovelar, order 5) prices 100 in the mint, '
      'ኄ’s price on the other device; the witness seats ኄ at 100 '
      'and ኌ not at all',
      GEEZ['ኌ'] == 100 and HALEHAME['ኄ'] == 100 and 'ኌ' not in HALEHAME,
      (GEEZ['ኌ'], HALEHAME['ኄ'], 'ኌ' in HALEHAME))

# --- The fences -------------------------------------------------------------------
p = SYSTEMS['geez']['provenance']
check('the mint’s registry provenance carries its fence',
      p.startswith('CONSTRUCTED') and '2026-11-24' in p
      and 'NOT attested' in p, p)
p = SYSTEMS['halehame']['provenance']
check('the witness’s registry provenance carries its fence',
      p.startswith('FOLK TABLE') and 'WITNESS' in p
      and 'UNDATED' in p and 'UNEXHIBITED' in p, p)

failed = [r for r in RESULTS if not r[1]]
print()
print('GE\'EZ PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
