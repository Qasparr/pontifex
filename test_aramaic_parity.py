#!/usr/bin/env python3
# ============================================================================
# 93
# THE ARAMAIC SEAT — PARITY OF THE ENGINE SEAT AGAINST THE PHASE I
# AUDIT'S FROZEN TRANSCRIPTION AND AGAINST THE LIVING HEBREW BANK
# A Scientific Illuminist proving of the Aramaic bank in the main
# engine (pontifex/pontifex) against the independent seat the
# Phase I audit built from the sources (research/twelve-tongues:
# aramaic-table.csv and aramaic-identity.csv, transcribed from
# three witnesses read entire — Cherry's Imperial Aramaic chart,
# York University, 2007; Wikipedia, "Syriac alphabet", summary
# table; tooldune's Syriac table — with the Syriac practice held
# against Nöldeke's appendix via Hughes) and against the engine's
# own HEBREW bank, whose identity with this one is the audit's
# finding. The seat was built at the desk on 2026-11-24 under the
# founder's three standing rules — the road rule, the proof-enough
# rule, and the end-goal rule, under which the seat's desk
# decisions (two strata in one bank; the square script not
# re-keyed; the finals extension not imported; the marks counted,
# never priced) were taken and are printed in the audit.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes from the living seats —
#   the engine's banks (ARAMAIC and its strata; HEBREW) and the
#   audit's CSVs. Nothing is hard-coded from memory except the
#   doctrine's own printed numbers, cited to their pages.
#
# DOCTRINE — THE CONTROLS: the engine's own control word (θέλημα
#   = 93) is weighed first; every pre-existing battery (engine,
#   greek, doubles, cubes, kana, geez, halehame, armenian,
#   coptic) is run and must pass untouched; and the Phase I
#   audit's own battery (22 checks) is run as a subprocess — the
#   audit instrument must still hold before its data can witness
#   anything.
#
# DOCTRINE — THE IDENTITY, EXHIBITED AND DISCIPLINED: this
#   battery proves the identity in BOTH directions, as the task
#   orders — every Aramaic seat against its Hebrew twin, and
#   every Hebrew base letter against both Aramaic strata. The
#   proof's purpose is the discipline that rides on it: the two
#   banks are ONE fact, never two witnesses, and this battery is
#   where that discipline is enforced in code — it also proves
#   the two banks share NO glyph, so no weighing can wander
#   between them and count the fact twice by accident of script.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, aramaic, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
)
from pontifex.tables import (
    ARAMAIC, ARAMAIC_IMPERIAL, ARAMAIC_SYRIAC, HEBREW,
)
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks

AUDIT_DIR = HERE / 'research' / 'twelve-tongues'

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


def abjad_value(position):
    # MECHANISM: the abjad class law restated independently in
    # the battery: nine units, nine tens, four hundreds.
    return position if position <= 9 else (position - 9) * 10 \
        if position <= 18 else (position - 18) * 100


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks),
                  ('armenian', armenian_checks),
                  ('coptic', coptic_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = aramaic_checks()
check('seat battery — aramaic_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'aramaic_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes (22 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-2]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat, read ---------------------------------------------
with open(AUDIT_DIR / 'aramaic-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'aramaic-identity.csv', encoding='utf-8') as fh:
    ident = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'aramaic-values.csv', encoding='utf-8') as fh:
    sweep = list(csv.DictReader(fh))
IMP_ROWS = [r for r in rows if r['stratum'] == 'IMPERIAL']
SYR_ROWS = [r for r in rows if r['stratum'] == 'SYRIAC']
check('the frozen transcription stands in the data seat: 44 '
      'SOURCED rows (22 IMPERIAL + 22 SYRIAC) and the identity '
      'table at 22 IDENTICAL rows',
      len(rows) == 44 and len(IMP_ROWS) == 22 and len(SYR_ROWS) == 22
      and all(r['status'] == 'SOURCED' for r in rows)
      and len(ident) == 22
      and all(r['relation'] == 'IDENTICAL' for r in ident),
      (len(rows), len(ident)))

# --- Sign for sign: the engine seat against the audit seat -------------------
check('bank identity — engine ARAMAIC_IMPERIAL == the audit’s '
      'IMPERIAL rows, key for key, value for value',
      ARAMAIC_IMPERIAL == {r['glyph']: int(r['value'])
                           for r in IMP_ROWS},
      (len(ARAMAIC_IMPERIAL), len(IMP_ROWS)))
check('bank identity — engine ARAMAIC_SYRIAC == the audit’s '
      'SYRIAC rows, key for key, value for value',
      ARAMAIC_SYRIAC == {r['glyph']: int(r['value'])
                         for r in SYR_ROWS},
      (len(ARAMAIC_SYRIAC), len(SYR_ROWS)))
check('bank identity — the registry table is the two strata '
      'entire: ARAMAIC == IMPERIAL ∪ SYRIAC, 44 keys, no overlap',
      SYSTEMS['aramaic']['table'] == ARAMAIC
      and ARAMAIC == {**ARAMAIC_IMPERIAL, **ARAMAIC_SYRIAC}
      and len(ARAMAIC) == 44
      and set(ARAMAIC_IMPERIAL).isdisjoint(set(ARAMAIC_SYRIAC)),
      len(ARAMAIC))
bad = [(r['glyph'], unicodedata.name(r['glyph'], ''),
        r['unicode_name']) for r in rows
       if unicodedata.name(r['glyph'], '') != r['unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata, all 44',
      not bad, bad or '44/44 verified')
check('the abjad law at the engine seat, recomputed from the '
      'audit’s positions, both strata',
      all(ARAMAIC_IMPERIAL[r['glyph']]
          == abjad_value(int(r['position'])) for r in IMP_ROWS)
      and all(ARAMAIC_SYRIAC[r['glyph']]
              == abjad_value(int(r['position'])) for r in SYR_ROWS),
      '44/44 by the law')

# --- THE IDENTITY, in both directions, against the living Hebrew bank ---------
check('IDENTITY, Aramaic → Hebrew: at every position of the '
      'audit’s identity table, both engine strata carry the '
      'living HEBREW bank’s value for the twin letter',
      all(ARAMAIC_IMPERIAL[r['imperial_glyph']]
          == ARAMAIC_SYRIAC[r['syriac_glyph']]
          == HEBREW[r['hebrew_glyph']] == int(r['hebrew_value'])
          for r in ident), '22/22 positions')
HEBREW_BASE = [r['hebrew_glyph'] for r in ident]
check('IDENTITY, Hebrew → Aramaic: every base letter of the '
      'living HEBREW bank finds its value in both strata — the '
      '22 base letters, no more and no fewer',
      set(HEBREW_BASE) == {g for g in HEBREW
                           if g not in 'ךםןףץ'}
      and all(any(r['hebrew_glyph'] == h
                  and ARAMAIC_IMPERIAL[r['imperial_glyph']]
                  == HEBREW[h]
                  and ARAMAIC_SYRIAC[r['syriac_glyph']] == HEBREW[h]
                  for r in ident) for h in HEBREW_BASE),
      '22/22 letters')
check('IDENTITY, the discipline in code: the two banks share '
      'values entire and glyphs never — key sets disjoint, so '
      'the one fact cannot be counted at both doors by script',
      set(ARAMAIC).isdisjoint(set(HEBREW))
      and set(ARAMAIC.values()) == set(
          HEBREW[g] for g in HEBREW_BASE),
      (len(set(ARAMAIC) & set(HEBREW)),
       len(set(ARAMAIC.values()))))
print('COORD — THE IDENTITY: the Aramaic seat and the Hebrew '
      'seat are one table in two scripts (22/22 seats, both '
      'directions). The agreement is exhibited as a coordinate; '
      'it is ONE fact, never two witnesses, and no bridge is '
      'claimed on it beyond the one the house already holds.')

# --- The exhibits at the engine's doors -----------------------------------------
a = weigh('𐡏𐡆', 'aramaic')
b = weigh('ܥܙ', 'aramaic')
c = weigh('עז', 'hebrew')
check('the founding head at the doors: 𐡏𐡆 (aramaic) == ܥܙ '
      '(aramaic) == עז (hebrew) == 77, breakdowns exact',
      a['value'] == b['value'] == c['value'] == 77
      and a['breakdown'] == [('𐡏', 70), ('𐡆', 7)]
      and b['breakdown'] == [('ܥ', 70), ('ܙ', 7)]
      and c['breakdown'] == [('ע', 70), ('ז', 7)],
      (a['value'], b['value'], c['value']))
ex = (weigh('ܬܩ', 'aramaic')['value'], weigh('ܬܪ', 'aramaic')['value'],
      weigh('ܬܫ', 'aramaic')['value'], weigh('ܬܬ', 'aramaic')['value'],
      weigh('ܬܬܩ', 'aramaic')['value'],
      weigh('ܩܢܙ', 'aramaic')['value'],
      weigh('ܬܫܣܕ', 'aramaic')['value'])
check('the Syriac practice at the doors: the additive hundreds '
      '500–900 and Hughes’ examples 157, 764',
      ex == (500, 600, 700, 800, 900, 157, 764), ex)

# --- The sweep's corpus through the engine ---------------------------------------
syr_of = {r['hebrew_glyph']: r['syriac_glyph'] for r in ident}
FINALS_OF = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}


def to_syriac(s):
    return ''.join(syr_of.get(FINALS_OF.get(ch, ch),
                              FINALS_OF.get(ch, ch)) for ch in s)


bad = []
for r in sweep:
    form = r['script_form']
    want = int(r['value'])
    if any(ch in ARAMAIC_SYRIAC for ch in form):
        got = weigh(form, 'aramaic')['value']
    else:
        got = (weigh(form, 'hebrew')['value'],
               weigh(to_syriac(form), 'aramaic')['value'])
        if got != (want, want):
            bad.append((r['term'], got, want))
            continue
        continue
    if got != want:
        bad.append((r['term'], got, want))
check('the sweep’s thirteen rows reproduce through the engine '
      'in BOTH scripts: the square forms at the hebrew door and '
      'their Syriac renderings at the aramaic door (AXONEME 267, '
      'ABRAHADABRA 418, the two 77 rows among them)',
      len(sweep) == 13 and not bad, bad or '13/13 in both scripts')

# --- The boundaries in code ---------------------------------------------------------
check('the finals boundary in code: the mispar gadol glyphs '
      'weigh nothing at the aramaic door, and the Hebrew seat '
      'they are measured against holds them at base values '
      '(ך 20, ם 40, ן 50, ף 80, ץ 90 — hechrechi, not gadol)',
      weigh('ךםןףץ', 'aramaic')['value'] == 0
      and weigh('ךםןףץ', 'aramaic')['breakdown'] == []
      and [HEBREW[g] for g in 'ךםןףץ'] == [20, 40, 50, 80, 90]
      and not any(v in ARAMAIC.values() for v in (500, 600, 700,
                                                  800, 900)),
      [HEBREW[g] for g in 'ךםןףץ'])
signs = ''.join(chr(cp) for cp in range(0x10857, 0x10860))
check('the number-sign boundary in code: the Imperial section '
      'sign and its 8 number signs weigh nothing at the door',
      weigh(signs, 'aramaic')['value'] == 0
      and weigh(signs, 'aramaic')['breakdown'] == [],
      weigh(signs, 'aramaic')['value'])

# --- The manuscript door ----------------------------------------------------------------
d = aramaic('ܬ' + '\u0305' + 'ܩ' + '\u0305')
r = aramaic('ܣ' + '\u0307')
check('the manuscript door: aramaic() counts the marks and '
      'prices none — overlined ܬܩ == 500 at face under 2 marks; '
      'the raised point counted, ܣ at its face 60, not 600',
      d['value'] == 500 and d['overline_marks'] == 2
      and d['word'] == 'ܬ' + '\u0305' + 'ܩ' + '\u0305'
      and r['value'] == 60 and r['raised_point_marks'] == 1,
      (d['value'], d['overline_marks'], r['value'],
       r['raised_point_marks']))

# --- The fences ----------------------------------------------------------------------------
p = SYSTEMS['aramaic']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('ATTESTED') and 'Imperial' in p
      and 'Syriac' in p and 'never two witnesses' in p
      and 'mispar gadol' in p and 'prices none' in p, p)
p = SYSTEMS['hebrew']['provenance']
check('the twin’s fence stands unaltered beside the new seat',
      p == 'ATTESTED', p)

failed = [r for r in RESULTS if not r[1]]
print()
print('ARAMAIC PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
