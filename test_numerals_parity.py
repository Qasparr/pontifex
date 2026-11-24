#!/usr/bin/env python3
# ============================================================================
# 93
# THE ROMAN NUMERAL DOUBLE-LETTER SYSTEM — PARITY OF THE MAP AGAINST
# THE ATTESTED GIVENS AND THE LATIN DOUBLES MAP
# A Scientific Illuminist proving of the numeral core (pontifex/
# pontifex/numerals.py) against the two seats it must answer to: the
# tradition's own standard form (the seven values, the repetition
# law, the six subtractive seats — as read in the "Roman numerals"
# article, Wikipedia, 2026-11-24) and the house's Latin doubles map
# (pontifex/doubles.py), inside whose twenty-six pairs the seven
# numeral pairs sit. Built 2026-11-24 at the founder's word —
# "what's the halt? Build" — as piece (i) of his Codex Legend
# theory: the Roman numeral double-letter system, the first-named
# and last-unbuilt of the legend's three pieces.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from living seats — the numeral
#   map as generated from its seven givens, the Latin doubles map
#   as generated from the Latin banks, and the law restated
#   independently below. Nothing is trusted from the module's own
#   say-so: the battery restates the classification arithmetic and
#   the promotion search in its own hand and holds the map to them.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα = 93)
#   is weighed first; every pre-existing battery (engine, greek,
#   doubles, cubes, kana, geez, halehame) is run and must pass
#   untouched; and the Ge'ez Phase I audit battery is run as a
#   subprocess — the house's most recent witness instrument must
#   still hold while a new seat is proven beside it.
#
# DOCTRINE — VV: the hinge is asserted at full size. Rome refuses
#   VV as a numeral and promotes it to X; the founder seats it as
#   the Roman face's HYBRID (his word, 2026-11-24), on his ground
#   that it is both a double consonant and a double vowel. The
#   battery pins the status as DISTINCT — refused_hybrid, neither
#   flattened into the refused class nor promoted into the lawful
#   — and pins LL and DD as refused with NO hybrid seat: their
#   candidacy is an open coordinate for his pen, and a battery
#   that let the desk extend his ruling would fail here by design.
# ============================================================================

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks,
)
from pontifex.doubles import DOUBLES as LATIN_PAIRS, doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.numerals import (
    NUMERAL_VALUES, DOUBLES, TRIPLES, SUBTRACTIVES,
    repeat_status, parse, numerals_checks,
)

AUDIT_DIR = HERE / 'research' / 'twelve-tongues'

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def law_status(letter, count):
    # MECHANISM: the repetition law restated independently in the
    # battery — classify by the value's arithmetic (a power is
    # 10^k; a five is 5·10^k), license powers to three, refuse the
    # fives, refuse four of anything, and seat V's double as the
    # founder's hybrid. The battery holds the map to the LAW as
    # stated, not to the builder's private copy of it.
    v = NUMERAL_VALUES[letter]
    while v > 1 and v % 10 == 0:
        v //= 10
    if count == 1:
        return 'single'
    if count > 3:
        return 'refused'
    if v == 1:
        return 'lawful'
    return 'refused_hybrid' if letter == 'V' and count == 2 else 'refused'


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'geez_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('control — the Ge’ez Phase I audit battery still passes (25 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The seat battery ---------------------------------------------------------
cs = numerals_checks()
check('seat battery — numerals_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))

# --- The law, restated --------------------------------------------------------
bad = [(ch, n) for ch in NUMERAL_VALUES for n in (2, 3, 4)
       if repeat_status(ch, n) != law_status(ch, n)]
check('the law restated: repeat_status agrees with the independent '
      'restatement at every letter and count (2, 3, 4)',
      not bad, bad or '21/21 agree')
bad = [(p, e['status']) for p, e in list(DOUBLES.items())
       + list(TRIPLES.items())
       if e['status'] != law_status(e['letter'], e['repeat'])]
check('every seat in both repeat maps carries the status the law '
      'assigns it — the refused three fall out of the arithmetic',
      not bad, bad or '14/14 statuses lawful under the restated law')

# --- The givens and the map ---------------------------------------------------
check('the seven givens stand as attested, in descending seat order '
      'M D C L X V I',
      NUMERAL_VALUES == {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                         'D': 500, 'M': 1000}
      and set(DOUBLES) == {c * 2 for c in NUMERAL_VALUES}
      and set(TRIPLES) == {c * 3 for c in NUMERAL_VALUES},
      sorted(DOUBLES))
check('lawful doubles and triples weigh by repetition: '
      'II 2, XX 20, CC 200, MM 2000; III 3, XXX 30, CCC 300, MMM 3000',
      [DOUBLES[p]['value'] for p in ('II', 'XX', 'CC', 'MM')]
      == [2, 20, 200, 2000]
      and [TRIPLES[p]['value'] for p in ('III', 'XXX', 'CCC', 'MMM')]
      == [3, 30, 300, 3000],
      ([DOUBLES[p]['value'] for p in ('II', 'XX', 'CC', 'MM')],
       [TRIPLES[p]['value'] for p in ('III', 'XXX', 'CCC', 'MMM')]))
check('promotions: each refused double points at the sign of exactly '
      'twice its value (VV→X, LL→C, DD→M), found by search',
      all(DOUBLES[p]['promotion_value'] == 2 * NUMERAL_VALUES[p[0]]
          and NUMERAL_VALUES[DOUBLES[p]['promotion']] ==
          DOUBLES[p]['promotion_value']
          for p in ('VV', 'LL', 'DD')),
      {p: DOUBLES[p]['promotion'] for p in ('VV', 'LL', 'DD')})
check('subtractives: the six generated seats, each greater − lesser, '
      'and the evaluator reads each back at its seat value',
      SUBTRACTIVES == {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                       'CD': 400, 'CM': 900}
      and all(parse(s) == v for s, v in SUBTRACTIVES.items()),
      SUBTRACTIVES)
check('no zero: the system seats no zero sign and N (nulla) is not '
      'a numeral letter',
      0 not in NUMERAL_VALUES.values() and 'N' not in NUMERAL_VALUES
      and all(e['value'] is None or e['value'] > 0
              for e in list(DOUBLES.values()) + list(TRIPLES.values())),
      'no zero seat')

# --- The joins against the Latin doubles map ----------------------------------
joins = {p: (DOUBLES[p]['value'], LATIN_PAIRS[p]['ordinal'],
             LATIN_PAIRS[p]['agrippa'])
         for p in ('II', 'VV', 'XX', 'LL', 'CC', 'DD', 'MM')}
check('the seven pairs cross-weighed against the living Latin map: '
      'II (2|18|18), VV (—|44|400), XX (20|48|600), LL (—|24|40), '
      'CC (200|6|6), DD (—|8|8), MM (2000|26|60)',
      joins == {'II': (2, 18, 18), 'VV': (None, 44, 400),
                'XX': (20, 48, 600), 'LL': (None, 24, 40),
                'CC': (200, 6, 6), 'DD': (None, 8, 8),
                'MM': (2000, 26, 60)}, joins)
check('the partings are total on values: no lawful numeral double '
      'equals either Latin pair-weight, and the Latin banks agree '
      'with each other at exactly II, CC, DD',
      all(n is None or (n != o and n != a) for n, o, a in joins.values())
      and {p for p, (_, o, a) in joins.items() if o == a}
      == {'II', 'CC', 'DD'},
      {p: (o, a) for p, (_, o, a) in joins.items() if o == a})
print('COORD — THE ZERO-POINT PAGE OF THE TWO SYSTEMS: the numeral '
      'doubles and the Latin pair-weights share the seven letters '
      'and no value. The Latin banks part from the numerals at II '
      'by +16 in both banks (18 against 2), at XX by +28/+580, at '
      'CC by −194 in both, at MM by −1974/−1940; at the refused '
      'three the numeral side of the page is a refusal with a '
      'promotion (X 10, C 100, M 1000) against Latin weights '
      '44/400, 24/40, 8/8. The boundary is everywhere, and it is '
      'printed, not smoothed.')

# --- VV, the hinge --------------------------------------------------------------
vv = DOUBLES['VV']
check('VV the hinge: status refused_hybrid — distinct from both the '
      'lawful and the refused class — valueless as a numeral, '
      'promotion X, hybrid seat carried in the data',
      vv['status'] == 'refused_hybrid' and vv['value'] is None
      and vv['promotion'] == 'X' and vv['promotion_value'] == 10
      and vv['hybrid_seat'] is True, vv)
check('the founder’s ground as a coordinate of the existing map: '
      'UU == VV == 400 in Agrippa (U read as V) — the double that '
      'is a double consonant and a double vowel in the same glyphs',
      LATIN_PAIRS['UU']['agrippa'] == LATIN_PAIRS['VV']['agrippa'] == 400
      and LATIN_PAIRS['VV']['ordinal'] == 44,
      (LATIN_PAIRS['UU'], LATIN_PAIRS['VV']))
check('LL and DD: refused with promotion, NO hybrid seat — their '
      'hybrid candidacy stands open for the founder’s pen, and the '
      'desk does not extend his ruling',
      DOUBLES['LL']['status'] == DOUBLES['DD']['status'] == 'refused'
      and DOUBLES['LL']['hybrid_seat'] is False
      and DOUBLES['DD']['hybrid_seat'] is False
      and (DOUBLES['LL']['promotion'], DOUBLES['DD']['promotion'])
      == ('C', 'M'),
      (DOUBLES['LL'], DOUBLES['DD']))

# --- The evaluator exhibits -----------------------------------------------------
check('evaluator exhibits: LXXVII == 77 (two lawful doubles around '
      'V), XCIII == 93 (a subtractive seat carrying a lawful '
      'triple), MDCCLXXVI == 1776, MMXXVI == 2026',
      (parse('LXXVII'), parse('XCIII'), parse('MDCCLXXVI'),
       parse('MMXXVI')) == (77, 93, 1776, 2026),
      (parse('LXXVII'), parse('XCIII'), parse('MDCCLXXVI'),
       parse('MMXXVI')))

failed = [r for r in RESULTS if not r[1]]
print()
print('NUMERALS PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
