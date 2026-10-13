# -*- coding: utf-8 -*-
"""
weigh_worker05.py — worker-05 weighing harness for PONTIFEX 777 gap-filling.

> "Every number is a fact; every fact is sacred." — the weighing is the
> sacrament, and the audit trail is the liturgy.

Date: 2026-10-13. 93.
Author line: proposed by worker-05 for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
Keeper of the Secret Treasure. All Rights Reserved, Without Prejudice.

MECHANISM: imports ~/workspace/pontifex/tools/ptk/weigh.py, runs calibrate()
(the anchorage — nothing is weighed until the engine proves itself), then
weighs worker-05's column-XXIV candidates (Pali/Sanskrit terms in IAST
transliteration) in LATIN_ORDINAL. DOCTRINE: no Sanskrit/Pali bank exists in
ptk, so these weighings are single-bank CONSTRUCTED values — hypotheses, not
doctrine. A second Hebrew-bank weighing of my own transliteration was
considered and REJECTED: my own mapping counted twice is not two honest banks.

Scientific Illuminism: hypothesis → method → observation → result is printed
per candidate, and unknown() is audited on every weighing (the gotcha: the
bank dict keys are uppercase, so normalize before auditing).
Closing: findings, never doctrine — the red pen rules. 93 93/93.
"""

import sys
import unicodedata

# MECHANISM: the weighing engine lives in the pontifex tools tree; never retype
# a letter table — import the single canonical copy.
sys.path.insert(0, '/home/hatch/workspace/pontifex/tools/ptk')
import weigh  # noqa: E402


def normalize(iast):
    """MECHANISM: strip macrons/diacritics (NFD decomposition, drop marks),
    drop spaces and hyphens, uppercase for the bank dict. DOCTRINE: the engine
    sees only what the bank knows; normalization is declared, not hidden."""
    s = unicodedata.normalize('NFD', iast)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace(' ', '').replace('-', '').upper()


# DOCTRINE: (cell, proposal, IAST spelling, term attestation). The TERM may be
# attested; the NUMBER is constructed. Never confuse the two.
CANDIDATES = [
    ('XXIV/2',  'Savikalpa-samadhi', 'Savikalpa-samādhi',
     'Crowley, Eight Lectures on Yoga — samprajnata, samadhi with seed'),
    ('XXIV/2',  'Mudita-samadhi',     'Muditā-samādhi',
     'Visuddhimagga brahmavihara framing; compound constructed'),
    ('XXIV/3',  'Mahakaruna',         'Mahākaruṇā',
     'Mahayana — the Great Compassion'),
    ('XXIV/3',  'Bodhicitta',         'Bodhicitta',
     'Mahayana — the awakening-mind'),
    ('XXIV/4',  'Brahmavihara',       'Brahmavihāra',
     'Pali canon — the four divine abidings'),
    ('XXIV/4',  'Metta-samadhi',      'Mettā-samādhi',
     'Visuddhimagga — metta-bhavana issues in jhana'),
    ('XXIV/5',  'Amata',              'Amata',
     'Pali canon — the Deathless = Nibbana'),
    ('XXIV/5',  'Samvega',            'Saṃvega',
     'Pali canon — spiritual urgency, fruit of maranasati'),
    ('XXIV/7',  'Sayujya',            'Sāyujya',
     'Hindu four muktis — union with the deity'),
    ('XXIV/7',  'Deva-darsana',       'Deva-darśana',
     'parallels Crowley darshana vocabulary, XXIV rows 1, 6, 13'),
    ('XXIV/8',  'Iddhi',              'Iddhi',
     'Pali canon — the supernormal powers'),
    ('XXIV/8',  'Vibhuti',            'Vibhūti',
     'Patanjali Yoga Sutra III — manifestations of power'),
    ('XXIV/9',  'Sotapatti',          'Sotāpatti',
     'Pali canon — stream-entry'),
    ('XXIV/9',  'Dhammacakkhu',       'Dhammacakkhu',
     'Pali canon — the Dhamma-eye at stream-entry'),
    ('XXIV/12', 'Patibhaga-nimitta',  'Paṭibhāga-nimitta',
     'Visuddhimagga — the counterpart sign of kasina practice'),
    ('XXIV/12', 'Appana',             'Appanā',
     'Visuddhimagga — absorption following the nimitta'),
]


def main():
    # METHOD: the anchorage first — calibrate() must pass before anything
    # is weighed.
    weigh.calibrate()
    print('calibrate: PASS\n')
    print('%-8s %-20s %-18s %6s %s' % ('cell', 'proposal', 'weighed_as', 'value', 'attestation'))
    for cell, proposal, iast, src in CANDIDATES:
        # OBSERVATION: normalize, weigh, then audit the skipped characters.
        w = normalize(iast)
        value = weigh.latin(w.lower())
        skipped = weigh.unknown(w, weigh.LATIN_ORDINAL)
        assert skipped == [], 'unknown() flagged %r on %s' % (skipped, w)
        # RESULT: one honest single-bank constructed weighing per candidate.
        print('%-8s %-20s %-18s %6d %s' % (cell, proposal, w, value, src))
    print('\n16 weighings, unknown()=[] on all. Findings, never doctrine.')


if __name__ == '__main__':
    main()
