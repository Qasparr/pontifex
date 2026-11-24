#!/usr/bin/env python3
# ============================================================================
# 93
# THE WORLD CENSUS — THE ENGINE ENUMERATED, BY SPECIES, WITH THE
# DEVICES AND THE ZEROS COUNTED IN CODE
# A Scientific Illuminist census of the whole pontifex engine as it
# stands after Phase II of the Caucasus-and-the-North road: every
# system the engine holds, classified by species; every thousands /
# multiplier / marking device, priced or price-refused at its door;
# every face of zero, computed bank by bank. The census is the
# evidence the Phase III instrument (THE-CAUCASUS-AND-THE-NORTH.md)
# states its pattern from — nothing in the instrument's proof column
# is asserted that is not recomputed here.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: the census reads the living registry (SYSTEMS) and the
#   living banks, and calls the living doors. The species table is
#   stated here as data (each entry's tier read off its own
#   registry fence); the devices are exercised, not described; the
#   zeros are counted, not remembered.
#
# DOCTRINE — THE CONTROLS: the control word first; EVERY battery
#   the engine carries is run and must pass untouched — the census
#   is only a census of a whole engine.
#
# DOCTRINE — THE FALSIFIABILITY RULE (the founder's, 2026-11-24
#   11:31 EST): this battery is itself a falsification coordinate
#   for the instrument's census claims — any count printed here
#   that fails in a later run kills the claim it witnessed.
# ============================================================================

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import pontifex.engine as E
from pontifex.engine import (
    weigh, SYSTEMS, armenian, cyrillic, coptic, aramaic,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
    hangul_checks, georgian_checks, cyrillic_checks,
    glagolitic_checks,
)
from pontifex import tables
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import diplomatic_checks
from pontifex.chinese import chinese_checks, read_chinese_numerals
from pontifex.triad import triad_checks, triad_weigh
from pontifex.katapayadi import (
    katapayadi_checks, aryabhatiya_checks, katapayadi_decode,
    aryabhatiya_encode,
)

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls: the whole engine, untouched -------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
ALL_BATTERIES = (
    ('engine', engine_checks), ('greek', greek_checks),
    ('doubles', doubles_checks), ('cubes', cubes_checks),
    ('kana', kana_checks), ('geez', geez_checks),
    ('halehame', halehame_checks), ('armenian', armenian_checks),
    ('coptic', coptic_checks), ('aramaic', aramaic_checks),
    ('hangul', hangul_checks), ('georgian', georgian_checks),
    ('cyrillic', cyrillic_checks), ('glagolitic', glagolitic_checks),
    ('diplomatic', diplomatic_checks), ('chinese', chinese_checks),
    ('triad', triad_checks), ('katapayadi', katapayadi_checks),
    ('aryabhatiya', aryabhatiya_checks),
)
for label, fn in ALL_BATTERIES:
    cs = fn()
    check('control — battery %s passes untouched' % label,
          all(p for _, p, _ in cs),
          '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))

# --- The census of systems, by species -----------------------------------------
SPECIES = {
    'attested banks': ['hebrew', 'greek', 'latin_ordinal', 'agrippa',
                       'arabic_abjad', 'armenian', 'georgian',
                       'glagolitic', 'aramaic'],
    'derived banks': ['coptic', 'cyrillic'],
    'constructed mints': ['kana', 'geez', 'hangul'],
    'constructed other': ['braille'],
    'witnesses': ['halehame'],
    'notation weighers': ['abc_notes'],
}
flat = [s for v in SPECIES.values() for s in v]
check('THE CENSUS — the registry holds exactly the species table: '
      '17 weigh() systems (9 attested banks, 2 derived, 3 mints, '
      '1 constructed other, 1 witness, 1 notation weigher)',
      set(SYSTEMS) == set(flat) and len(SYSTEMS) == 17,
      {k: len(v) for k, v in SPECIES.items()})
tier_ok = all(
    SYSTEMS[s]['provenance'].startswith(tier)
    for tier, names in (('ATTESTED', SPECIES['attested banks']),
                        ('DERIVED', SPECIES['derived banks']),
                        ('CONSTRUCTED', SPECIES['constructed mints']
                         + SPECIES['constructed other']))
    for s in names)
check('THE CENSUS — every bank’s registry fence opens with the '
      'tier its species claims (the tier names the values’ '
      'provenance, read off the fences themselves)',
      tier_ok, 'fences read at the registry')
check('THE CENSUS — the doors beyond weigh(): katapayadi the '
      'ENCODER, aryabhatiya the CIPHER, the Chinese NOTATION '
      'reader, the Roman NOTATION (numerals.py), the DIPLOMATIC '
      'relation, the DOUBLES map, the CUBES, the TRIAD assembly — '
      'eight instruments, none of them a weigh() system',
      all(not hasattr(E, n) or n not in SYSTEMS
          for n in ('katapayadi', 'aryabhatiya', 'chinese'))
      and 'katapayadi' not in SYSTEMS and 'sanskrit' not in SYSTEMS
      and 'aryabhatiya' not in SYSTEMS and 'chinese' not in SYSTEMS
      and 'roman' not in SYSTEMS and 'diplomatic' not in SYSTEMS,
      sorted(SYSTEMS))

# --- The class law, across the letter-tables -----------------------------------
CLASS_BANKS = ('GREEK', 'HEBREW', 'ARABIC_ABJAD', 'ARMENIAN',
               'GEORGIAN', 'COPTIC', 'CYRILLIC', 'GLAGOLITIC',
               'ARAMAIC')


def class_form(v):
    return any(v == d * (10 ** k) for d in range(1, 10)
               for k in range(0, 5))


off = {n: [v for v in getattr(tables, n).values() if not class_form(v)]
       for n in CLASS_BANKS}
check('THE CLASS LAW at census scale: every value in the nine '
      'letter-tables (Greek, Hebrew, Arabic, Armenian, Georgian, '
      'Coptic, Cyrillic, Glagolitic, Aramaic) is digit x 10^class '
      '— no value off the decimal grid',
      all(not v for v in off.values()),
      {n: len(v) for n, v in off.items()})

# --- The devices census, exercised at the doors ---------------------------------
d1 = armenian('Ե' + '̅')
check('DEVICE — the Armenian overline: PRICED x10,000 at its door '
      '(Ե + overline = 50,000)',
      d1['value'] == 50000, d1['value'])
d2 = cyrillic('҂Ѕ')
check('DEVICE — the Cyrillic thousands sign: PRICED x1000 at its '
      'door (҂Ѕ = 6,000)',
      d2['value'] == 6000, d2['value'])
d3 = cyrillic('⃝А')
check('DEVICE — the Cyrillic higher encircling signs: COUNTED, '
      'NOT PRICED (the Lesser and Greater scales part; the door '
      'refuses the choice)',
      d3['value'] == 1 and d3['higher_marks'] == 1,
      (d3['value'], d3['higher_marks']))
d4 = cyrillic('А' + '҃')
check('DEVICE — the Cyrillic titlo: a MARK, counted, never priced',
      d4['value'] == 1 and d4['titlo_marks'] == 1,
      (d4['value'], d4['titlo_marks']))
d5 = coptic('ⲁ' + '̅')
check('DEVICE — the Coptic overline: a MARKER, counted, never '
      'priced (the descent kept the Greek mark a mark)',
      d5['value'] == 1 and d5['overline_marks'] == 1,
      (d5['value'], d5['overline_marks']))
d6 = aramaic('ܬ' + '̅' + 'ܩ' + '̅')
d7 = aramaic('ܣ' + '̇')
check('DEVICE — the Aramaic overlines and raised point: marks '
      'COUNTED, never priced, at their door',
      d6['value'] == 500 and d7['value'] == 60,
      (d6['value'], d7['value']))
check('DEVICE — Greek’s own thousands device (the lower keraia) '
      'is NOT SEATED in this engine: no greek() door exists; the '
      'epissemon signs stand in the bank as ordinary letters '
      '(ϛ 6, ϟ 90, ϡ 900). A printed gap, not a silence.',
      not hasattr(E, 'greek')
      and weigh('ϛϟϡ', 'greek')['value'] == 996,
      weigh('ϛϟϡ', 'greek')['value'])
check('DEVICE — Georgian seats NO device (its 10,000 is the '
      'letter ჵ in the bank); Glagolitic’s thousands sign is '
      'attested as evidence but unseated (no door prices it)',
      weigh('ჵ', 'georgian')['value'] == 10000
      and not hasattr(E, 'glagolitic_door'), weigh('ჵ', 'georgian'))

# --- The zeros census, computed ---------------------------------------------------
banks = {n: getattr(tables, n) for n in
         ('GREEK', 'HEBREW', 'ARABIC_ABJAD', 'ARMENIAN', 'GEORGIAN',
          'COPTIC', 'CYRILLIC', 'GLAGOLITIC', 'ARAMAIC',
          'LATIN_ORDINAL', 'AGRIPPA', 'HALEHAME', 'BRAILLE',
          'KANA', 'HANGUL')}
zero_keys = {n: sum(1 for v in b.values() if v == 0)
             for n, b in banks.items()}
check('THE ZEROS — ABSENCE: no attested or derived weighing bank '
      'carries a zero-valued letter (counted: 0 zero keys in each '
      'of Greek, Hebrew, Arabic, Armenian, Georgian, Coptic, '
      'Cyrillic, Glagolitic, Aramaic, Latin ordinal, Agrippa)',
      all(zero_keys[n] == 0 for n in
          ('GREEK', 'HEBREW', 'ARABIC_ABJAD', 'ARMENIAN', 'GEORGIAN',
           'COPTIC', 'CYRILLIC', 'GLAGOLITIC', 'ARAMAIC',
           'LATIN_ORDINAL', 'AGRIPPA')), zero_keys)
geez_zero = sum(1 for v in tables.GEEZ.values() if v == 0)
check('THE ZEROS — THE MINT’S PRICE: in the Ge’ez mint zero is a '
      'price — the non-axis forms and the order-6 axis seat price '
      '0 (counted in code)',
      geez_zero > 0, geez_zero)
t = triad_weigh('아')
check('THE ZEROS — THE PLACEHOLDER: the Hangul mint’s ㅇ initial '
      'is priced 0 at the door and counted as a null initial (the '
      'script’s own zero, at its seat)',
      t['null_initials'] == 1, t['null_initials'])
check('THE ZEROS — THE GLYPH: the Chinese notation reads its zero '
      'glyphs as the number 0 （零 and 〇）, inside a notation, '
      'never as letters of a bank',
      read_chinese_numerals('零')['value'] == 0
      and read_chinese_numerals('〇')['value'] == 0
      and 'chinese' not in SYSTEMS, 'glyph, not letter')
check('THE ZEROS — THE ENCODER’S DIGIT: Katapayadi prices signs '
      'at 0 (ञ decodes 0); the Aryabhatiya cipher’s zero is '
      'ABSENCE (encode(0) is the empty string)',
      katapayadi_decode('ञ') == 0
      and aryabhatiya_encode(0) == '',
      (katapayadi_decode('ञ'), repr(aryabhatiya_encode(0))))
check('THE ZEROS — THE HOLE: Glagolitic’s unvalued letters (Ⱊ Ⱐ '
      'Ⱒ) are holes inside a valued span — letters present, values '
      'absent — a different face from a zero sign (counted: 3, '
      'and the bank holds no 0)',
      zero_keys['GLAGOLITIC'] == 0
      and all(weigh(c, 'glagolitic')['breakdown'] == []
              for c in 'ⰚⰠⰢ'), '3 holes, no zero key')

failed = [r for r in RESULTS if not r[1]]
print()
print('WORLD CENSUS — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
