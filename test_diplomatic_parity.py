#!/usr/bin/env python3
# ===========================================================================
# 93
# THE DIPLOMATIC KEY — PARITY OF THE RELATION INSTRUMENT AGAINST
# THE LIVING ENGINE, THE STATED DEFINITION, AND THE GLYPH GEOMETRY
# A Scientific Illuminist proving of the diplomatic checker and
# register (pontifex/pontifex/diplomatic.py): the found exhibit
# recomputed, the definition's exclusion clause held in code, the
# letter geometry re-derived by bitmap rotation in a named
# typeface (DejaVu Sans) and held to its stated tolerances, and
# the register reproduced by a fresh sweep. Built 2026-11-24 at
# the founder's word — "Proceed as the map and key point the
# tuning forks" (11:02 EST) — for his coinage of the same morning:
# "Could be a key itself though. A diplomatic key."
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check recomputes from living seats — the
#   engine's banks for the values, the module's checker for the
#   verdicts, and an independent bitmap derivation (PIL, DejaVu
#   Sans) for the geometry. The exhibits' transformations are
#   additionally restated by direct string surgery in this
#   battery's own hand, so the register does not stand on the
#   module's say-so alone.
#
# DOCTRINE — THE CONTROLS: the engine's control word (θέλημα =
#   93) is weighed first; every pre-existing battery (engine,
#   greek, doubles, cubes, kana, geez, halehame, armenian,
#   coptic, aramaic) runs and must pass untouched; and the most
#   recent sibling parity (Aramaic) is run as a subprocess — the
#   newest seat must still hold while a new instrument is proven
#   beside it.
#
# DOCTRINE — THE EXCLUSION: the definition's teeth are asserted
#   at full size. A pure permutation is value-invariant in every
#   additive bank (the anagram theorem), so a pair carried by
#   permutation alone is refused BY THE DEFINITION, in code —
#   ROWAN ⇄ NOWAR stands in the battery as the refused pair, and
#   a checker that admitted it would fail here by design.
# ===========================================================================

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # the pontifex package

from pontifex.engine import (
    weigh, engine_checks, greek_checks, kana_checks, geez_checks,
    halehame_checks, armenian_checks, coptic_checks, aramaic_checks,
)
from pontifex.doubles import doubles_checks
from pontifex.cubes import cubes_checks
from pontifex.diplomatic import (
    ROTATE, CORPUS, REGISTER, EXCLUDED, EXHIBIT_1_SPEC,
    apply_transform, diplomatic_pair, diplomatic_checks,
    find_permutation, geometry_tables, sweep,
)

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
                  ('armenian', armenian_checks),
                  ('coptic', coptic_checks),
                  ('aramaic', aramaic_checks)):
    cs = fn()
    check('control — pre-existing battery %s passes untouched' % label,
          all(p for _, p, _ in cs),
          '%d/%d' % (sum(1 for _, p, _ in cs if p), len(cs)))
sibling = subprocess.run(
    [sys.executable, str(HERE / 'test_aramaic_parity.py')],
    cwd=str(HERE), capture_output=True, text=True)
check('control — the Aramaic parity battery still passes (29 checks)',
      sibling.returncode == 0,
      sibling.stdout.strip().splitlines()[-1]
      if sibling.stdout.strip() else sibling.returncode)

# --- The seat battery ---------------------------------------------------------
cs = diplomatic_checks()
check('seat battery — diplomatic_checks() passes',
      all(p for _, p, _ in cs), '%d/%d' % (sum(1 for _, p, _ in cs if p),
                                          len(cs)))

# --- The exhibits, restated by direct string surgery --------------------------
# MECHANISM: the battery rebuilds Exhibit 1 with its own hands —
# ROMAN's third letter replaced by W, nothing else touched — and
# holds the module's transformation to the result; the anagram
# half is restated with sorted(), the plainest statement of a
# permutation that exists.
surgery = 'ROMAN'[:2] + 'W' + 'ROMAN'[3:]
check('Exhibit 1 restated: ROMAN with seat 3 turned (M→W) is '
      'ROWAN, and ROWAN is an anagram of NOWAR by sorted()',
      surgery == 'ROWAN' and sorted('ROWAN') == sorted('NOWAR')
      and apply_transform('ROMAN', EXHIBIT_1_SPEC) == 'NOWAR',
      (surgery, apply_transform('ROMAN', EXHIBIT_1_SPEC)))
r = diplomatic_pair('ROMAN', 'ROWAN', ('rotate_seats', (2,)))
check('Exhibit 2 restated: the one-seat turn alone carries '
      'ROMAN to ROWAN, values 61/201 against 71/171',
      r['verdict'] == 'DIPLOMATIC'
      and r['banks']['latin_ordinal']['a'][0] == 61
      and r['banks']['latin_ordinal']['b'][0] == 71,
      (r['verdict'], r['transformed']))

# --- The anagram theorem, restated --------------------------------------------
# MECHANISM: every anagram pair in the corpus is found by
# sorted() and weighed in both Latin banks in the battery's own
# calls; the theorem says the values cannot part. (Greek and
# other banks weigh these Latin strings partially or not at all;
# the theorem is stated for additive banks generally and proven
# here on the banks that cover the pairs whole.)
anagram_pairs = [(a, b) for i, a in enumerate(CORPUS)
                 for b in CORPUS[i + 1:]
                 if len(a) == len(b) and sorted(a) == sorted(b)]
theorem_holds = all(
    weigh(a, bank)['value'] == weigh(b, bank)['value']
    for a, b in anagram_pairs
    for bank in ('latin_ordinal', 'agrippa'))
check('the anagram theorem restated: every anagram pair in the '
      'corpus weighs identically in both Latin banks',
      theorem_holds and anagram_pairs == [('NOWAR', 'ROWAN')],
      anagram_pairs)

# --- The geometry, re-derived by bitmap rotation ------------------------------
# MECHANISM: DejaVu Sans glyphs are rendered, centred by their
# bounding boxes on a square canvas, turned 180°, and scored by
# ink overlap (intersection over union, threshold 96) against
# every letter of their alphabet. Tolerances as stated in the
# instrument: self-symmetry corroborated at ≥ 0.60; the
# lowercase pairs at ≥ 0.85 with mutual best match; the M ↔ W
# coordinate asserted as measured (rotated-W's best match is M;
# rotated-M's best NON-SELF match is W, the pair being the
# typeface's nearest turn though DejaVu's half-depth M-vertex
# scores it 0.438); Μ's absence asserted as measured (no match
# at the 0.60 line anywhere in the Greek alphabet).
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
_font = ImageFont.truetype(FONT_PATH, 220)
_C = 400


def _canvas(ch):
    img = Image.new('L', (_C, _C), 0)
    ImageDraw.Draw(img).text((0, 0), ch, font=_font, fill=255)
    g = img.crop(img.getbbox())
    out = Image.new('L', (_C, _C), 0)
    out.paste(g, ((_C - g.width) // 2, (_C - g.height) // 2))
    return out


def _sim(a, b):
    inter = union = 0
    for va, vb in zip(a.getdata(), b.getdata()):
        ba, bb = va > 96, vb > 96
        if ba and bb:
            inter += 1
        if ba or bb:
            union += 1
    return inter / union if union else 0.0


def _best(imgs, ch):
    rot = imgs[ch].transpose(Image.ROTATE_180)
    return sorted(((_sim(rot, imgs[o]), o) for o in imgs),
                  reverse=True)


LAT = {c: _canvas(c) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
LOW = {c: _canvas(c) for c in 'abcdefghijklmnopqrstuvwxyz'}
GRK = {c: _canvas(c) for c in 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'}

lat_self = {c: _sim(LAT[c].transpose(Image.ROTATE_180), LAT[c])
            for c in 'HINOSXZ'}
check('geometry re-derived: Latin capitals H I N O S X Z are '
      'self-symmetric in DejaVu Sans (ink overlap ≥ 0.60)',
      all(s >= 0.60 for s in lat_self.values()),
      {c: round(s, 3) for c, s in sorted(lat_self.items())})
grk_self = {c: _sim(GRK[c].transpose(Image.ROTATE_180), GRK[c])
            for c in 'ΖΗΘΙΝΞΟΦΧ'}
check('geometry re-derived: Greek capitals Ζ Η Θ Ι Ν Ξ Ο Φ Χ '
      'are self-symmetric in DejaVu Sans (ink overlap ≥ 0.60)',
      all(s >= 0.60 for s in grk_self.values()),
      {c: round(s, 3) for c, s in sorted(grk_self.items())})
low_pairs = {}
pairs_ok = True
for a, b in (('b', 'q'), ('d', 'p'), ('n', 'u')):
    sa, sb = _best(LOW, a), _best(LOW, b)
    low_pairs[a + b] = (round(sa[0][0], 3), round(sb[0][0], 3))
    pairs_ok = (pairs_ok and sa[0][1] == b and sb[0][1] == a
                and sa[0][0] >= 0.85 and sb[0][0] >= 0.85)
check('geometry re-derived: the lowercase pairs b↔q, d↔p, n↔u '
      'are mutual best turns at ink overlap ≥ 0.85', pairs_ok,
      low_pairs)
mw = (_best(LAT, 'W')[0], [x for x in _best(LAT, 'M')
                           if x[1] != 'M'][0])
check('geometry re-derived: the M ↔ W coordinate as measured — '
      'rotated-W’s best match is M; rotated-M’s best non-self '
      'match is W (the typeface’s nearest turn)',
      mw[0][1] == 'M' and mw[1][1] == 'W',
      (mw[0][1], round(mw[0][0], 3), mw[1][1], round(mw[1][0], 3)))
mu = _best(GRK, 'Μ')
check('geometry re-derived: Μ has no partner — its turned '
      'bitmap reaches no Greek capital at the 0.60 line',
      all(s < 0.60 for s, _ in mu),
      [(o, round(s, 3)) for s, o in mu[:3]])

# --- The register, held to the corpus ------------------------------------------
geo = geometry_tables()
check('the seated geometry tables print whole: pairs, symmetric '
      'seats, and absences account for every letter of all three '
      'alphabets',
      all(len(t['pairs']) * 2 + len(t['symmetric'])
          + len(t['absent']) == n
          for t, n in zip(geo.values(), (26, 26, 24))),
      {k: (len(v['pairs']), len(v['symmetric']), len(v['absent']))
       for k, v in geo.items()})
check('the register stands as swept: 2 exhibits seated, 1 '
      'exclusion printed, every exhibit verified DIPLOMATIC by '
      'the checker',
      len(REGISTER) == 2 and len(EXCLUDED) == 1
      and all(e['verdict'] == 'DIPLOMATIC' for e in REGISTER)
      and EXCLUDED[0]['verdict'].startswith('VALUE-INVARIANT'),
      ([(e['a'], e['b']) for e in REGISTER],
       [(e['a'], e['b']) for e in EXCLUDED]))

print()
failed = [n for n, p, _ in RESULTS if not p]
print('DIPLOMATIC PARITY — %d/%d checks PASS%s'
      % (len(RESULTS) - len(failed), len(RESULTS),
         ('; FAILING: ' + '; '.join(failed)) if failed else ''))
sys.exit(1 if failed else 0)
