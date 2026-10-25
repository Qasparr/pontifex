#!/usr/bin/env python3
# =============================================================================
# PONTIFEX research — greek_weigh.py — worker #2 of 12 (GREEK)
# The Greek bank of the Twelve Tongues gematria bridge research.
#
# Epigraph: "Weigh each word in its own tongue, and let the bridge be the
# shared number across two honest banks."
# — the author's doctrine, recorded by the scribe.
#
# Date: 2026-10-11 (Sol in 18° Libra, Anno V:xii e.n.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, and the
# scribe reports findings, never doctrine. All findings go to the red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   HYPOTHESIS: the shared corpus, transliterated into Greek by a stated
#     convention, can be weighed in the attested Milesian table; the
#     weighings that land on the author's target numbers (418, 666, 777,
#     93, 77, 11) and the collisions between distinct terms are findings
#     for the red pen, and the misses are findings of equal weight.
#   METHOD: transliterate each corpus term with the stated CONSTRUCTED
#     convention (see TRANSLITERATION_CONVENTION); weigh the Greek form
#     with the repo's ATTESTED GREEK table via pontifex.engine.weigh —
#     the scribe never invents a table silently.
#   OBSERVATION: per-letter breakdowns, printed and written to CSV, so
#     every number shows its work (the engine's own doctrine).
#   RESULT: the CSV greek-values.csv and the findings in the final report.
#     This research decrees no bridge.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the shared Twelve Tongues corpus in Greek isopsephy.

DOCTRINE (the author's, not amended here):
- Each word is weighed in its own tongue. The Greek table is the attested
  Milesian isopsephy (alpha=1 ... omega=800, with the epissemones
  stigma=6, koppa=90, sampi=900), recorded in pontifex/tables.py.
- Every value carries a provenance tier: ATTESTED / DERIVED / CONSTRUCTED.
  Constructed = hypothesis, never doctrine.
- The table is ATTESTED; the Latin->Greek transliteration convention below
  is CONSTRUCTED and stated in full. Where a term IS an authentic Greek
  word, its attested Greek spelling is weighed instead and marked as such.
"""

import csv
import os
import sys

# MECHANISM: reuse the repo's attested engine so no table is invented here.
# The script lives inside the repo tree, so a plain import is honest.
sys.path.insert(0, os.path.expanduser('~/workspace/pontifex'))
from pontifex.engine import weigh  # noqa: E402

# ---------------------------------------------------------------------------
# TRANSLITERATION_CONVENTION — "GR-TRANS-v1" (CONSTRUCTED, research convention)
# ---------------------------------------------------------------------------
# MECHANISM: Latin-script corpus terms are rendered into Greek letters by
# the map below. Greedy digraphs are tried first; hyphens are dropped
# (Greek has no hyphen value; the engine would skip them as silence anyway).
# Every choice is stated because the choice IS part of the finding.
#
# DOCTRINE of the choices:
#   TH -> theta      (the conventional single-letter rendering; NOT tau+eta)
#   OO -> ou         (the diphthong, two letters: omicron+upsilon)
#   V  -> upsilon    (the corpus spells TRVVTH in Roman epigraphic style,
#                     where V stands for U; variant V->beta is weighed as
#                     an alternate because classical Latin V ~ Greek w/b)
#   H  -> eta        (Greek has no /h/; rough breathing leaves no letter.
#                     Variant H->chi is weighed as an alternate for the
#                     headline terms.)
#   X  -> xi         (classical Latin X -> Greek xi, e.g. Xerxes = Xerxes;
#                     variant X->chi is weighed as an alternate)
#   Y  -> upsilon    (Greek has no Latin Y; variant Y->iota weighed)
#   Q  -> kappa      (Greek has no Q; classical Q -> kappa)
#   C  -> kappa      (classical C -> kappa)
#   J  -> iota       (not fired by this corpus; recorded for completeness)
#   W  -> ou         (not fired by this corpus; recorded for completeness)
#   E/O-> epsilon/omicron by default, EXCEPT where the term is an authentic
#                     Greek word: THELEMA -> thelema (theta epsilon lambda
#                     ETA mu alpha, the word's real spelling) and
#                     AGAPE -> agape (alpha gamma alpha pi ETA, the real
#                     spelling). The authentic spellings are weighed as
#                     attested forms; the mechanical renderings are weighed
#                     as variants, because the 90-vs-93 split is itself a
#                     finding (see the log).
# MERGERS that fire (information loss, stated plainly):
#   theta absorbs th (distinction between theta and tau+eta unrecoverable)
#   upsilon absorbs v, u, y (the v/beta and y/iota ambiguities are variants)
#   eta absorbs h (the /h/ distinction is lost; rough-breathing words are
#     silently smooth in the Greek column)
#   kappa absorbs c, q, k (the three Latin letters collapse to one)
#   xi absorbs x (x/chi choice is a variant)
#   hyphen: dropped, not zeroed.

DIGRAPHS = {'th': 'θ', 'ph': 'φ', 'ch': 'χ', 'oo': 'ου'}

SINGLES = {
    'a': 'α', 'b': 'β', 'c': 'κ', 'd': 'δ', 'e': 'ε', 'f': 'φ', 'g': 'γ',
    'h': 'η', 'i': 'ι', 'j': 'ι', 'k': 'κ', 'l': 'λ', 'm': 'μ', 'n': 'ν',
    'o': 'ο', 'p': 'π', 'q': 'κ', 'r': 'ρ', 's': 'σ', 't': 'τ', 'u': 'υ',
    'v': 'υ', 'w': 'ου', 'x': 'ξ', 'y': 'υ', 'z': 'ζ',
}


def transliterate(latin):
    """Render a Latin-script term in Greek letters per GR-TRANS-v1.

    MECHANISM: greedy digraphs first, then singles; hyphens dropped.
    Returns the Greek string.
    """
    out = []
    i = 0
    w = latin.lower()
    while i < len(w):
        if w[i] == '-':
            i += 1  # MECHANISM: dropped, not zeroed — recorded in the log.
            continue
        pair = w[i:i + 2]
        if pair in DIGRAPHS:
            out.append(DIGRAPHS[pair])
            i += 2
            continue
        ch = w[i]
        if ch in SINGLES:
            out.append(SINGLES[ch])
        # else: silence — unknown characters are never given false weight.
        i += 1
    return ''.join(out)


# ---------------------------------------------------------------------------
# THE CORPUS — (term, greek_form, convention_label, provenance_note,
#                mergers_or_loss, notes)
# ---------------------------------------------------------------------------
# MECHANISM: script forms come from transliterate() above (marked
# CONSTRUCTED) or are authentic Greek spellings (marked as such). The
# values are always weighed in the repo's ATTESTED table.
CORPUS = [
    # -- headline: the canonical 77 bridge, both banks --------------------
    ('AXONEME', 'αξονεμε', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'X->xi chosen over chi; upsilon absorbs nothing here; '
     'epsilon/mu/omicron/nu single renderings',
     'Primary weighing. X->chi variant weighed separately (771, not 777).'),
    ('OZ', 'οζ', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'no mergers fired',
     'TARGET 77 hit.'),
    ('TRVVTH', 'τρυυθ', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'V->upsilon each (Roman epigraphic V-for-U); TH->theta absorbs th',
     'Primary weighing. V->beta variant weighed separately (413).'),
    # -- the calibration term: authentic Greek spelling -------------------
    ('THELEMA', 'θελημα', 'authentic Greek spelling',
     'ATTESTED (table); authentic Greek word-form',
     'no mergers fired; second E is eta in the real word',
     'CALIBRATION: classic 93 confirmed letter by letter. '
     'Mechanical θελεμα variant weighed separately (90).'),
    ('AGAPE', 'αγαπη', 'authentic Greek spelling',
     'ATTESTED (table); authentic Greek word-form',
     'no mergers fired; final E is eta in the real word',
     'TARGET 93 hit. COLLISION with THELEMA at 93 (see log).'),
    ('BABALON', 'βαβαλον', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'B->beta, O->omicron; kappa absorbs nothing here',
     'Weighed with omicron per the corpus spelling.'),
    ('HERU-RA-HA', 'ηερυραηα', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'H->eta each (the /h/ is lost); hyphen dropped, not zeroed',
     'Primary weighing. H->chi variant weighed separately (1807).'),
    ('ABRAHADABRA', 'αβραηαδαβρα', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'H->eta; kappa absorbs nothing here',
     'Greek value is NOT 418 — the Hebrew bridge does not cross. '
     'Negative result, reported at full weight.'),
    ('QIRA', 'κιρα', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'Q->kappa (merger: c/q/k collapse)',
     ''),
    ('LIBERTY', 'λιβερτυ', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'Y->upsilon chosen; B->beta; final sigma form not fired '
     '(word ends in upsilon); upsilon absorbs y/u/v ambiguity',
     'Primary weighing. Y->iota variant weighed separately (457).'),
    ('CELL', 'κελλ', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'C->kappa (merger: c/k collapse)',
     'Greek 85 vs canonical English-ordinal 32 — no bridge. '
     'Negative result, reported at full weight.'),
    # -- the Hebrew reference term, weighed in Greek -----------------------
    ('עז', 'οζ', 'transliteration of the Hebrew term',
     'ATTESTED (table); transliterated Hebrew term',
     'ayin->omicron, zayin->zeta: the Phoenician-derived numeral order '
     'survives on both banks',
     'TARGET 77 hit. The canonical bridge AXONEME=77=עז holds on the '
     'Greek bank because 70=70 and 7=7 in both systems — ATTESTED on '
     'ATTESTED.'),
    # -- variants (alternate convention choices, weighed and recorded) -----
    ('AXONEME [X->chi variant]', 'αχονεμε', 'GR-TRANS-v1 variant',
     'ATTESTED (table); script-form CONSTRUCTED',
     'X->chi instead of xi',
     'ANTI-HIT recorded: 771 is near 777 but IS NOT 777. Wish-reading '
     'flagged; the miss stands.'),
    ('TRVVTH [V->beta variant]', 'τρββθ', 'GR-TRANS-v1 variant',
     'ATTESTED (table); script-form CONSTRUCTED',
     'V->beta for BOTH Vs (classical Latin V); TH->theta',
     'Alternate reading of the Roman V. The scribe\'s first hand entry '
     'wrote τρυβθ (one beta, 811) — the engine\'s verification caught it; '
     'the true all-beta form is τρυββθ = 413. Logged as a caught error.'),
    ('THELEMA [mechanical variant]', 'θελεμα', 'GR-TRANS-v1',
     'ATTESTED (table); script-form CONSTRUCTED',
     'TH->theta; both Es as epsilon',
     'The naive rendering: 90, NOT the classic 93. This dead end taught '
     'the convention that authentic Greek spellings must be weighed.'),
    ('HERU-RA-HA [H->chi variant]', 'χερυραχα', 'GR-TRANS-v1 variant',
     'ATTESTED (table); script-form CONSTRUCTED',
     'H->chi (consonantal /h/); hyphen dropped',
     'Alternate reading of initial H.'),
    ('LIBERTY [Y->iota variant]', 'λιβερτι', 'GR-TRANS-v1 variant',
     'ATTESTED (table); script-form CONSTRUCTED',
     'Y->iota (Greek i-sound); B->beta',
     'Alternate reading of Y.'),
]

TARGETS = (418, 666, 777, 93, 77, 11)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_csv = os.path.join(here, 'greek-values.csv')

    rows = []
    print('PONTIFEX — Greek bank (worker #2 of 12) — weighings')
    print('=' * 70)
    for (term, greek, convention, provenance,
         mergers, notes) in CORPUS:
        r = weigh(greek, 'greek')
        value = r['value']
        # MECHANISM: the audit trail — every number shows its work.
        parts = ' + '.join('%s=%d' % (ch, v) for ch, v in r['breakdown'])
        print('\n%s  ->  %s' % (term, greek))
        print('    %s = %d' % (parts, value))
        hits = [t for t in TARGETS if t == value]
        if hits:
            print('    *** TARGET HIT: %s ***' % ', '.join(map(str, hits)))
        rows.append({
            'term': term,
            'language': 'Greek',
            'script_form': greek,
            'transliteration_convention': convention,
            'table_used': 'ATTESTED Milesian isopsephy '
                          '(pontifex/tables.py GREEK)',
            'provenance_tier': provenance,
            'value': value,
            'mergers_or_loss': mergers,
            'notes': notes,
        })

    # MECHANISM: the CSV is the machine-readable ledger for the parent's
    # synthesis. The ultra-verbose narrative lives in greek.md.
    fieldnames = ['term', 'language', 'script_form',
                  'transliteration_convention', 'table_used',
                  'provenance_tier', 'value', 'mergers_or_loss', 'notes']
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print('\n' + '=' * 70)
    print('wrote %s (%d rows)' % (out_csv, len(rows)))

    # MECHANISM: cross-check the hand computations of the scribe — the
    # machine re-weighs from the same attested table, so agreement is the
    # verification and disagreement would be a TRVVTH failure.
    expected = {
        'AXONEME': 231, 'OZ': 77, 'TRVVTH': 1209, 'THELEMA': 93,
        'AGAPE': 93, 'BABALON': 156, 'HERU-RA-HA': 623,
        'ABRAHADABRA': 221, 'QIRA': 131, 'LIBERTY': 847, 'CELL': 85,
        'עז': 77,
        'AXONEME [X->chi variant]': 771,
        'TRVVTH [V->beta variant]': 413,
        'THELEMA [mechanical variant]': 90,
        'HERU-RA-HA [H->chi variant]': 1807,
        'LIBERTY [Y->iota variant]': 457,
    }
    got = {row['term']: row['value'] for row in rows}
    bad = [(t, expected[t], got.get(t)) for t in expected
           if got.get(t) != expected[t]]
    if bad:
        print('TRVVTH FAILURE — mismatches:', bad)
        sys.exit(1)
    print('all %d hand computations verified against the attested table'
          % len(expected))

    # MECHANISM: report the target-number landscape and collisions — the
    # parent needs these for synthesis, and the scribe names them plainly.
    print('\n--- target-number landscape ---')
    for t in TARGETS:
        landed = [row['term'] for row in rows if row['value'] == t
                  and 'variant' not in row['term'].lower()
                  and 'variant]' not in row['term']]
        print('%d: %s' % (t, landed if landed else 'no corpus term lands'))
    print('\n--- collisions (distinct terms, same value) ---')
    by_value = {}
    for row in rows:
        if 'variant]' in row['term']:
            continue
        by_value.setdefault(row['value'], []).append(row['term'])
    for v, terms in sorted(by_value.items()):
        if len(terms) > 1:
            print('%d: %s' % (v, terms))


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
