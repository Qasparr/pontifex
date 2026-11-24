#!/usr/bin/env python3
# ============================================================================
# 93
# THE COPTIC TABLE — PARITY OF THE ENGINE SEAT AGAINST THE PHASE I
# AUDIT'S FROZEN TRANSCRIPTION, AND THE DESCENT EXHIBITED AT BOTH
# SEATS
# A Scientific Illuminist proving of the Coptic bank in the main
# engine (pontifex/pontifex) against the independent seat the Phase I
# audit built from the sources (research/twelve-tongues:
# coptic-table.csv and coptic-descent.csv, transcribed from three
# full-table witnesses read entire — Wikipedia, "Coptic script";
# the fsymbols Coptic collection; the tooldune Coptic Alphabet
# Table, concurring with its derivation stated — with Satzinger's
# Coptic Course and Dr. Isaac's Institute page held against the
# seats they exhibit). The seat was built at the desk on 2026-11-24
# under the founder's three standing rules — the road rule, the
# proof-enough rule, and the end-goal rule, under which the seat's
# desk decisions (DERIVED over the sweep's ATTESTED; small-letter
# keys; the marks counted, never priced) were taken and are printed
# in the audit at §VIII.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes from the two living seats —
#   the engine's bank (a literal dict in tables.py, keyed in the
#   small letters) and the audit's CSVs (generated in coptic_audit.py
#   from the witnesses, with Unicode-name verification). Nothing is
#   hard-coded from memory except the doctrine's own printed numbers,
#   which are cited to their pages. The seats are compared as SETS
#   with per-sign values: key for key, value for value.
#
# DOCTRINE — THE CONTROLS: the engine's own control word (θέλημα
#   = 93) is weighed first; every pre-existing battery (engine,
#   greek, doubles, cubes, kana, geez, halehame, armenian) is run and
#   must pass untouched; and the Phase I audit's own battery (20
#   checks) is run as a subprocess — the audit instrument must still
#   hold before its data can witness anything.
#
# DOCTRINE — THE DESCENT, EXHIBITED: this road's ordered comparison
#   is the descent from the Greek bank — the key's first inheritance
#   test. The exhibit below weighs every Milesian seat at BOTH
#   engine banks: 27 of 27 values agree, and the three holder
#   partings (6, 90, 900) are proven in code at the seats. The
#   agreement is a property of two value sequences, printed as
#   coordinates — it is NOT corroboration: the Coptic values are
#   the Greek values received, single-sourced by descent, and no
#   bridge is claimed on the agreement.
# ============================================================================

import csv
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, coptic, SYSTEMS,
    engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks,
)
from pontifex.tables import COPTIC, GREEK
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks

AUDIT_DIR = HERE / 'research' / 'twelve-tongues'

RESULTS = []


def check(name, passed, got):
    RESULTS.append((name, bool(passed), got))
    print('%s — %s | %r' % ('PASS' if passed else 'FAIL', name, got))


# --- The controls -----------------------------------------------------------
check('control — θέλημα/greek == 93 [ENGINE]',
      weigh('θέλημα', 'greek')['value'] == 93,
      weigh('θέλημα', 'greek')['value'])
for label, fn in (('engine', engine_checks), ('greek', greek_checks),
                  ('doubles', doubles_checks), ('cubes', cubes_checks),
                  ('kana', kana_checks), ('geez', geez_checks),
                  ('halehame', halehame_checks),
                  ('armenian', armenian_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                               len(cs)))
cs = coptic_checks()
check('seat battery — coptic_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))
audit_battery = subprocess.run(
    [sys.executable, str(AUDIT_DIR / 'coptic_audit_tests.py')],
    cwd=str(AUDIT_DIR), capture_output=True, text=True)
check('witness — the Phase I audit battery still passes (20 checks)',
      audit_battery.returncode == 0,
      audit_battery.stdout.strip().splitlines()[-1]
      if audit_battery.stdout.strip() else audit_battery.returncode)

# --- The audit's data seat, read ---------------------------------------------
with open(AUDIT_DIR / 'coptic-table.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'coptic-descent.csv', encoding='utf-8') as fh:
    desc = list(csv.DictReader(fh))
with open(AUDIT_DIR / 'coptic-values.csv', encoding='utf-8') as fh:
    sweep = list(csv.DictReader(fh))
SOURCED = [r for r in rows if r['status'] == 'SOURCED']
NOVALUE = [r for r in rows if r['status'] == 'NO VALUE']
check('the frozen transcription stands in the data seat: 27 SOURCED '
      'rows + 7 NO VALUE rows',
      len(SOURCED) == 27 and len(NOVALUE) == 7
      and [r['uppercase'] for r in NOVALUE]
      == ['Ϣ', 'Ϧ', 'Ⳉ', 'Ϩ', 'Ϫ', 'Ϭ', 'Ϯ'],
      (len(SOURCED), len(NOVALUE)))

# --- Sign for sign: the engine seat against the audit seat -------------------
check('bank identity — engine COPTIC == the audit’s 27 SOURCED '
      'rows, key for key, value for value',
      COPTIC == {r['lowercase']: int(r['value']) for r in SOURCED},
      (len(COPTIC), len(SOURCED)))
bad = [(r['uppercase'], unicodedata.name(r['uppercase'], ''),
        r['uppercase_unicode_name']) for r in rows
       if unicodedata.name(r['uppercase'], '')
       != r['uppercase_unicode_name']
       or unicodedata.name(r['lowercase'], '')
       != r['lowercase_unicode_name']]
check('every glyph is the standard’s own: Unicode names at the '
      'engine seat == the audit CSV == unicodedata, both cases',
      not bad, bad or '34/34 verified')
check('the Milesian sequence at the engine seat, recomputed from '
      'the audit’s table: the valued signs sorted by value are '
      'the 27-seat sequence entire',
      sorted(COPTIC.values())
      == [d for d in range(1, 10)] + [d * 10 for d in range(1, 10)]
      + [d * 100 for d in range(1, 10)],
      '27 seats by the law')
check('the boundary in the data is the boundary at the seat: the '
      'NO VALUE rows’ letters are keys of NO case in the bank, and '
      'weigh silence',
      all(r['uppercase'] not in COPTIC and r['lowercase'] not in COPTIC
          for r in NOVALUE)
      and weigh('ϣϩϯ', 'coptic')['breakdown'] == []
      and weigh('ⳉ', 'coptic')['value'] == 0,
      [r['uppercase'] for r in NOVALUE])

# --- The witnesses' numbers at the engine's doors ------------------------------
r = weigh('ⲧⲝⲉ', 'coptic')
check('calibration at the seat: ⲧⲝⲉ == 365, breakdown exact; '
      'ⲫ == 500',
      r['value'] == 365 and r['breakdown'] == [('ⲧ', 300), ('ⲝ', 60),
                                               ('ⲉ', 5)]
      and weigh('ⲫ', 'coptic')['value'] == 500,
      (r['value'], r['breakdown']))
ex = (weigh('ⲓⲃ', 'coptic')['value'], weigh('ⲱⲡⲏ', 'coptic')['value'],
      weigh('ⳁϥⲑ', 'coptic')['value'], sum(COPTIC.values()))
check('the witnesses’ numbers at the seat: 12 (W2), 888 (W1’s '
      'letter part), 999 (the maximum), the 27 values sum to 4995',
      ex == (12, 888, 999, 4995), ex)

# --- The sweep's corpus through the engine -------------------------------------
bad = []
for row in sweep:
    form = row['script_form']
    got = weigh(form, 'coptic')
    if row['value'] == 'UNKNOWN':
        partial = {'HERU-RA-HA': 677, 'ABRAHADABRA': 213}[row['term']]
        if got['value'] != partial \
                or len(got['breakdown']) == len(form):
            bad.append((row['term'], got['value'], partial))
    elif got['value'] != int(row['value']):
        bad.append((row['term'], got['value'], int(row['value'])))
check('the sweep’s seventeen corpus rows reproduce through the '
      'engine: 15 valued exact (OZ 77, CELL 85, AXONEME 231 among '
      'them), 2 UNKNOWN failing closed at their partials (677, 213)',
      len(sweep) == 17 and not bad, bad or '17/17 agree')

# --- The descent, exhibited at both seats ---------------------------------------
seat_rows = [r for r in desc if r['value'].isdigit()]
agree = [r for r in seat_rows
         if weigh(r['greek_sign'], 'greek')['value'] == int(r['value'])
         == weigh(r['coptic_sign'], 'coptic')['value']]
check('DESCENT — the shared domain at both engine seats: the '
      'Greek sign == the Coptic sign at 27/27 Milesian values',
      len(seat_rows) == 27 and len(agree) == 27,
      '%d/%d agree' % (len(agree), len(seat_rows)))
check('DESCENT — the holder partings in code: at 6, ϛ == ⲋ '
      '(sign for sign); at 90, ϟ == ϥ == 90 (the lineage parting — '
      'the dead Greek letter and the living Demotic letter at one '
      'value); at 900, ϡ == ⳁ (the sampi descended)',
      GREEK['ϛ'] == COPTIC['ⲋ'] == 6
      and GREEK['ϟ'] == COPTIC['ϥ'] == 90
      and GREEK['ϡ'] == COPTIC['ⳁ'] == 900
      and next(r for r in seat_rows if r['value'] == '90')
      ['greek_sign'] == 'ϟ',
      (GREEK['ϟ'], COPTIC['ϥ']))
print('COORD — THE DESCENT: on the 27 Milesian seats the two banks '
      'carry one value sequence entire (27/27), inherited, not '
      'corroborated — the partings are of kind (6, 900: a numeral '
      'sign for a numeral sign), of lineage (90: ϟ out, ϥ in), and '
      'of form (200: σ/ς against the one ⲥ). The agreement is '
      'exhibited as a coordinate; no bridge is claimed on it.')

# --- Case and the manuscript door -------------------------------------------------
check('case at the seat: ⲀⲂⲄ == ⲁⲃⲅ == 6 (the seam casefolds '
      'to the small-letter bank); Ϥⲁ == 91',
      weigh('ⲀⲂⲄ', 'coptic')['value']
      == weigh('ⲁⲃⲅ', 'coptic')['value'] == 6
      and weigh('Ϥⲁ', 'coptic')['value'] == 91,
      (weigh('ⲀⲂⲄ', 'coptic')['value'], weigh('Ϥⲁ', 'coptic')['value']))
d = coptic('ⲧ' + '\u0305' + 'ⲝ' + '\u0305' + 'ⲉ' + '\u0305')
t1 = coptic('ⲁ' + '\u033f')
t2 = coptic('ⲁ' + '\u0375')
check('the manuscript door: coptic() counts the marks (3 '
      'overlines; 1 double overline; 1 numeral sign) and prices '
      'NONE — overlined ⲧⲝⲉ weighs 365 at face, ⲁ̿ and ⲁ͵ weigh 1',
      d['value'] == 365 and d['overline_marks'] == 3
      and t1['value'] == 1 and t1['double_overline_marks'] == 1
      and t2['value'] == 1 and t2['numeral_sign_marks'] == 1,
      (d['value'], d['overline_marks'], t1['value'], t2['value']))

# --- The fences ---------------------------------------------------------------------
p = SYSTEMS['coptic']['provenance']
check('the seat’s registry provenance carries its fence',
      p.startswith('DERIVED') and '27' in p and 'fai' in p
      and 'NO value' in p and 'ATTESTED' in p, p)
p = SYSTEMS['greek']['provenance']
check('the parent’s fence stands unaltered beside the new seat',
      p == 'ATTESTED', p)

failed = [r for r in RESULTS if not r[1]]
print()
print('COPTIC PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         '' if not failed else ' — FAILURES: %r' % (failed,)))
sys.exit(1 if failed else 0)

# ============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# ============================================================================
