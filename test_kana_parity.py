#!/usr/bin/env python3
# ============================================================================
# 93
# THE GOJŪON MINT — PARITY OF THE TWO ENGINE SEATS
# A Scientific Illuminist proving of the kana seat in the main engine
# (pontifex/pontifex) against the mint's first seat (tools/ptk), the
# bank as ratified 2026-11-13 and seated in the main engine 2026-11-24.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes from the two living banks —
#   nothing is hard-coded from memory except the doctrine's own printed
#   calibration numbers, which are cited to their pages. The banks are
#   compared as dictionaries, through their weigh doors sign by sign,
#   and through the ー operator door word by word.
#
# DOCTRINE — THE CONTROL: the engine's own control word (θέλημα = 93)
#   is weighed first, and ptk's anchorage (calibrate) is run first.
#   A bank that fails its control proves nothing about any seat.
#
# DOCTRINE — THE HEADS (protocol P4): the mint prints its あくま
#   beside AKUMA 47 and its むげつ beside MUGETSU 106 at the head of
#   its calibration, AGREE OR NOT. The kana values are 40 and 103;
#   the deltas (−7, −3) are the seam's coordinates, exhibited below
#   at full size — they are data, not failures, and no seat moves to
#   close them. The bridges (P2) are exact only: かな 27 == KANA 27,
#   しおん 65 == SHION 65, ゆず 93 == YUZU 93.
#
# DOCTRINE — THE SEAM (G3/G6): ー is an operator, not a bank key, in
#   BOTH seats; length spelled with a vowel kana is weighed as
#   written. The とー/とう pair is printed below as the exhibited
#   seam. This test proves the two seats agree; it does not close
#   the seam and does not alter any value.
# ============================================================================

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))            # the pontifex package
sys.path.insert(0, str(HERE / 'tools'))  # the ptk tool

from pontifex.engine import weigh, kana as engine_kana, SYSTEMS
from pontifex.tables import KANA as ENGINE_KANA, KANA_VOWEL, KANA_BASE
import ptk.weigh as ptk

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
check('control — ptk calibrate() holds [PTK]', ptk.calibrate() is True, True)
check('witness — ptk kana_selftest() holds, untouched [PTK]',
      ptk.kana_selftest() is True, True)

# --- The banks as dictionaries ----------------------------------------------
check('bank identity — engine KANA == ptk KANA, key for key',
      ENGINE_KANA == ptk.KANA,
      (len(ENGINE_KANA), len(ptk.KANA)))
check('vowel map identity — engine KANA_VOWEL == ptk _KANA_VOWEL',
      KANA_VOWEL == ptk._KANA_VOWEL,
      (len(KANA_VOWEL), len(ptk._KANA_VOWEL)))
check('ー is a key of NEITHER bank (operator, G3)',
      'ー' not in ENGINE_KANA and 'ー' not in ptk.KANA, True)

# --- Sign for sign through the weigh doors -----------------------------------
mismatch = [c for c in ENGINE_KANA
            if weigh(c, 'kana')['value'] != ptk.weigh(c, ptk.KANA)]
check('all signs weigh identically through both weigh doors',
      not mismatch, '%d/%d agree' % (len(ENGINE_KANA) - len(mismatch),
                                     len(ENGINE_KANA)))

# --- The seated inventory: 73 signs, values 1–73 each exactly once -----------
# MECHANISM: ptk exports no base list; its seating order is rebuilt
# from its own grid data (grid, then ん, then the dakuten rows — the
# load-bearing order of G1/G2) so the two inventories compare as
# sequences, not just as sets.
ptk_base = ([c for row in ptk._KANA_GRID for c in row if c] + ['ん']
            + [c for row in ptk._KANA_DAKUTEN_ROWS for c in row])
check('the 73 base signs are the same signs in the same seating order',
      list(KANA_BASE) == ptk_base, (len(KANA_BASE), len(ptk_base)))
check('values 1–73 each used exactly once across the seated inventory',
      sorted(ENGINE_KANA[s] for s in KANA_BASE) == list(range(1, 74))
      and sorted(ptk.KANA[s] for s in ptk_base) == list(range(1, 74)),
      (ENGINE_KANA['あ'], ENGINE_KANA['を'], ENGINE_KANA['ん'],
       ENGINE_KANA['ぽ']))
check('no dual values — ん holds ONE seat, 48, in both engines '
      '(Fukada’s elected ン refused)',
      ENGINE_KANA['ん'] == ptk.KANA['ん'] == 48
      and ENGINE_KANA['ン'] == ptk.KANA['ン'] == 48,
      (ENGINE_KANA['ん'], ptk.KANA['ん']))

# --- One sign, two dresses -----------------------------------------------------
hira = [c for c in ENGINE_KANA if 'ぁ' <= c <= 'ゖ']
mirror_bad = [c for c in hira
              if ENGINE_KANA[chr(ord(c) + 0x60)] != ENGINE_KANA[c]
              or ptk.KANA[chr(ord(c) + 0x60)] != ptk.KANA[c]]
check('katakana mirrors hiragana sign-for-sign in both engines',
      len(hira) == 85 and not mirror_bad,
      '%d pairs, %d mismatched' % (len(hira), len(mirror_bad)))

# --- The calibration heads, printed as the protocol prints them (P4/P2) -------
HEADS = [
    # (kana word, kana value, seam twin, twin value, Δ) — MAGVS Part IV
    ('あくま', 40, 'AKUMA', 47, -7),
    ('むげつ', 103, 'MUGETSU', 106, -3),
    ('ゆず', 93, 'YUZU', 93, 0),
    ('かな', 27, 'KANA', 27, 0),
    ('しおん', 65, 'SHION', 65, 0),
]
for kw, kv, twin, tv, delta in HEADS:
    got = (weigh(kw, 'kana')['value'], ptk.kana(kw),
           weigh(twin, 'latin_ordinal')['value'])
    check('head — %s == %d beside %s %d (Δ %+d)' % (kw, kv, twin, tv, delta),
          got == (kv, kv, tv) and kv - tv == delta, got)

# --- The operator door, word for word ------------------------------------------
WORDS = ['ラーメン', 'かー', 'とー', 'んー', 'ー', 'あー', 'ずっと',
         'きゃく', 'ありがとう', 'カタカナ', 'かたかな']
op_bad = [w for w in WORDS if engine_kana(w)['value'] != ptk.kana(w)]
raw_bad = [w for w in WORDS
           if weigh(w, 'kana')['value'] != ptk.weigh(w, ptk.KANA)]
check('operator door parity — engine kana() == ptk kana() on %d words'
      % len(WORDS), not op_bad, op_bad or 'all agree')
check('raw door parity — engine weigh() == ptk weigh() on the same words '
      '(ー skipped at both)', not raw_bad, raw_bad or 'all agree')

# --- The exhibited seam (G3/G6), printed at full size ---------------------------
seam = (engine_kana('とー')['value'], engine_kana('とう')['value'],
        ptk.kana('とー'), ptk.kana('とう'))
check('seam pair agrees across engines — とー (operator) vs とう (spelled)',
      seam == (25, 23, 25, 23), seam)
print('COORD — THE SEAM STANDS OPEN: とー weighs 25 by the operator '
      '(G3: length is a second mora of お, 5) while とう weighs 23 as '
      'written (G6: と 20 + う 3). Both seats print both numbers; '
      'neither closes the difference.')

# --- The fence -------------------------------------------------------------------
p = SYSTEMS['kana']['provenance']
check('the registry provenance carries the fence',
      p.startswith('CONSTRUCTED') and '2026-11-13' in p
      and 'NOT attested' in p, p)

failed = [r for r in RESULTS if not r[1]]
print()
print('KANA PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
