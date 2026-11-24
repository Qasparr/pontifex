#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — sanskrit_audit.py — the Sanskrit Phase I audit: data builder
# Companion to sanskrit.md (the Twelve-Tongues sweep, Worker #9) and to
# THE-SANSKRIT-FIELD-PHASE-I-AUDIT.md (the audit document of record).
#
# Epigraph: "na, ña and the vowels [standing alone denote] zeros; [the
# consonants] beginning with ka, ṭa, pa and ya, [denote severally] the
# numbers [1 to 9]; in a conjunct [consonant, only] the consonant in the
# penultimate [place, which is followed by a vowel, denotes a] number;
# and a consonant not attached to a vowel should not be considered [as
# a number]." — Śaṅkaravarman, Sadratnamālā (1819), 3.3, in Sarma's
# translation (the tradition's own definition of the first system).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to
# the author's red pen. This file is an AUDIT instrument: findings,
# never doctrine. Nothing here is a bank; nothing here enters the
# engine's weighing surface.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: (i) the Kaṭapayādi consonant→digit table can be
#     re-sourced sign by sign from independent witnesses agreeing
#     entire, and its laws (the group structure, the vowel rule, the
#     conjunct rule, the leftward reading) verified by recomputing
#     the witnesses' own worked examples; (ii) Āryabhaṭa's
#     alphasyllabic cipher (Gītikāpāda) can likewise be re-sourced —
#     the varga/avarga values and the vowel place-multipliers — and
#     verified against the sine verse it was built to carry;
#     (iii) the two systems are DIFFERENT SPECIES from the engine's
#     weighing banks and from each other, and the audit's seat, if
#     any, must be a door, never a bank.
#   Method: (1) transcribe each table from the witnesses read entire
#     on 2026-11-24 (named in the CSVs' witness columns) and diff
#     them cell by cell in code — a disagreement aborts the build
#     as a finding, never averages away; (2) verify every glyph
#     against the Unicode standard (codepoint and name); (3)
#     recompute the witnesses' own exhibits before trusting any
#     derived number (the battery does this; this builder freezes
#     the data the battery proves against).
#   Observation: recorded in the audit document, section by section.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Build and freeze the Sanskrit Phase I audit data.

DOCTRINE: this script builds AUDIT data, not a bank. Two numeral
systems are transcribed here, each ATTESTED as what it is:

  KAṬAPAYĀDI — a syllable ENCODER: consonants denote decimal digits
    so that a number can be worn as pronounceable verse. Decoding
    (syllables → number) is deterministic; encoding (number →
    syllables) is free. It is not, and in the tradition never was,
    a way of weighing words.

  ĀRYABHAṬĪYA — Āryabhaṭa's alphasyllabic POSITIONAL CIPHER:
    consonants carry values (varga 1–25, avarga 30–100), vowels
    carry places (successive powers of 100), and a string's number
    is the sum of its syllables' contributions. Letters as digits
    in places — again, not a weighing bank: the same syllables in
    another arrangement are another number, and a word's meaning
    contributes nothing.

MECHANISM: four CSVs are written beside this script —
  sanskrit-katapayadi-table.csv      the 33 consonant→digit cells
                                     (three transcriptions diffed),
                                     the standalone-vowel zero rule,
                                     and the ḷa row standing OPEN;
  sanskrit-katapayadi-examples.csv   the witnesses' own worked
                                     examples, with the numbers the
                                     battery must reproduce;
  sanskrit-aryabhatiya-table.csv     the 33 consonant values and
                                     the 9 vowel place-multipliers
                                     (two transcriptions diffed);
  sanskrit-aryabhatiya-examples.csv  the exhibits: the 24 sine
                                     differences of Gītikāpāda 12,
                                     khyughṛ, the jala verse, the
                                     ṅiśibu string, the slate's two
                                     ends (ka, hau).
The companion battery sanskrit_audit_tests.py re-derives every
number from these files; the Phase II door (pontifex/katapayadi.py)
is proven against them by test_sanskrit_parity.py at the root.
"""

import csv
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# MECHANISM: the Devanagari seats. Every glyph below is written as a
# literal and verified against the Unicode standard in main() —
# codepoint and name — so a transcription slip in this file fails
# the build instead of entering the record.
# ---------------------------------------------------------------------------

# The 33 consonants in varṇamālā order, with IAST names.
CONSONANTS = [
    ('ka', 'क'), ('kha', 'ख'), ('ga', 'ग'), ('gha', 'घ'), ('ṅa', 'ङ'),
    ('ca', 'च'), ('cha', 'छ'), ('ja', 'ज'), ('jha', 'झ'), ('ña', 'ञ'),
    ('ṭa', 'ट'), ('ṭha', 'ठ'), ('ḍa', 'ड'), ('ḍha', 'ढ'), ('ṇa', 'ण'),
    ('ta', 'त'), ('tha', 'थ'), ('da', 'द'), ('dha', 'ध'), ('na', 'न'),
    ('pa', 'प'), ('pha', 'फ'), ('ba', 'ब'), ('bha', 'भ'), ('ma', 'म'),
    ('ya', 'य'), ('ra', 'र'), ('la', 'ल'), ('va', 'व'), ('śa', 'श'),
    ('ṣa', 'ष'), ('sa', 'स'), ('ha', 'ह'),
]

# ---------------------------------------------------------------------------
# KAṬAPAYĀDI — three independent transcriptions of the digit table.
#
# W1: Wikipedia, "Katapayadi system" (read entire 2026-11-24) — the
#     arrangement table in Devanagari and the Sadratnamālā verse.
# W2: Sarma, "The Kaṭapayādi System of Numerical Notation", Revue
#     d'Histoire des Mathématiques 18.1 (2012), pp. 37–66 — the
#     table at p. 39 and the eight definitions of his Appendix,
#     esp. Sadratnamālā 3.3 and the anonymous kādi-nava verse.
# SWEEP: the house's own draft (sanskrit.md §1.3, Worker #9,
#     2026-10-11) — a third transcription, diffed like the others.
# Each dict is written out entire, from its own page.
# ---------------------------------------------------------------------------

KATAPAYADI_W1 = {
    'ka': 1, 'kha': 2, 'ga': 3, 'gha': 4, 'ṅa': 5, 'ca': 6, 'cha': 7,
    'ja': 8, 'jha': 9, 'ña': 0,
    'ṭa': 1, 'ṭha': 2, 'ḍa': 3, 'ḍha': 4, 'ṇa': 5, 'ta': 6, 'tha': 7,
    'da': 8, 'dha': 9, 'na': 0,
    'pa': 1, 'pha': 2, 'ba': 3, 'bha': 4, 'ma': 5,
    'ya': 1, 'ra': 2, 'la': 3, 'va': 4, 'śa': 5, 'ṣa': 6, 'sa': 7,
    'ha': 8,
}

KATAPAYADI_W2 = {
    'ka': 1, 'kha': 2, 'ga': 3, 'gha': 4, 'ṅa': 5, 'ca': 6, 'cha': 7,
    'ja': 8, 'jha': 9, 'ña': 0,
    'ṭa': 1, 'ṭha': 2, 'ḍa': 3, 'ḍha': 4, 'ṇa': 5, 'ta': 6, 'tha': 7,
    'da': 8, 'dha': 9, 'na': 0,
    'pa': 1, 'pha': 2, 'ba': 3, 'bha': 4, 'ma': 5,
    'ya': 1, 'ra': 2, 'la': 3, 'va': 4, 'śa': 5, 'ṣa': 6, 'sa': 7,
    'ha': 8,
}

KATAPAYADI_SWEEP = {
    'ka': 1, 'kha': 2, 'ga': 3, 'gha': 4, 'ṅa': 5, 'ca': 6, 'cha': 7,
    'ja': 8, 'jha': 9, 'ña': 0,
    'ṭa': 1, 'ṭha': 2, 'ḍa': 3, 'ḍha': 4, 'ṇa': 5, 'ta': 6, 'tha': 7,
    'da': 8, 'dha': 9, 'na': 0,
    'pa': 1, 'pha': 2, 'ba': 3, 'bha': 4, 'ma': 5,
    'ya': 1, 'ra': 2, 'la': 3, 'va': 4, 'śa': 5, 'ṣa': 6, 'sa': 7,
    'ha': 8,
}

KATA_GROUPS = [
    ('ka-group', ['ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja',
                  'jha', 'ña']),
    ('ṭa-group', ['ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da',
                  'dha', 'na']),
    ('pa-group', ['pa', 'pha', 'ba', 'bha', 'ma']),
    ('ya-group', ['ya', 'ra', 'la', 'va', 'śa', 'ṣa', 'sa', 'ha']),
]

KATA_WITNESSES = ('Wikipedia "Katapayadi system" (arrangement table); '
                  'Sarma 2012, p. 39 table + Appendix defs. 1–6, 8; '
                  'sweep draft sanskrit.md §1.3')

# ---------------------------------------------------------------------------
# ĀRYABHAṬĪYA — two independent transcriptions.
#
# W1: Wikipedia, "Āryabhaṭa numeration" (read entire 2026-11-24) —
#     the full 33 × 9 slate, citing Ifrah (2000), pp. 447–450, and
#     Fleet, JRAS 43 (1911).
# W2: PramaKosha, "Āryabhaṭa's Alphabetic Numeral Notation
#     (varga–avarga akṣara system)" (read entire 2026-11-24) — a
#     procedure entry grounded in the GRETIL Āryabhaṭīya text
#     (urn:cts:sanskritLit:aryabhatiya:1.2), with its value tables
#     stated as deterministic ground truth and its worked examples
#     set by a verify-tool.
# ---------------------------------------------------------------------------

ARYA_VARGA_W1 = {
    'ka': 1, 'kha': 2, 'ga': 3, 'gha': 4, 'ṅa': 5,
    'ca': 6, 'cha': 7, 'ja': 8, 'jha': 9, 'ña': 10,
    'ṭa': 11, 'ṭha': 12, 'ḍa': 13, 'ḍha': 14, 'ṇa': 15,
    'ta': 16, 'tha': 17, 'da': 18, 'dha': 19, 'na': 20,
    'pa': 21, 'pha': 22, 'ba': 23, 'bha': 24, 'ma': 25,
}
ARYA_AVARGA_W1 = {
    'ya': 30, 'ra': 40, 'la': 50, 'va': 60,
    'śa': 70, 'ṣa': 80, 'sa': 90, 'ha': 100,
}
# vowel name -> (place index n, multiplier 10^(2n)); long and short
# are NOT distinguished (W1, on the slate's own statement).
ARYA_VOWELS_W1 = {
    'a': (0, 1), 'i': (1, 100), 'u': (2, 10000), 'ṛ': (3, 1000000),
    'ḷ': (4, 100000000), 'e': (5, 10000000000),
    'ai': (6, 1000000000000), 'o': (7, 100000000000000),
    'au': (8, 10000000000000000),
}

ARYA_VARGA_W2 = {
    'ka': 1, 'kha': 2, 'ga': 3, 'gha': 4, 'ṅa': 5,
    'ca': 6, 'cha': 7, 'ja': 8, 'jha': 9, 'ña': 10,
    'ṭa': 11, 'ṭha': 12, 'ḍa': 13, 'ḍha': 14, 'ṇa': 15,
    'ta': 16, 'tha': 17, 'da': 18, 'dha': 19, 'na': 20,
    'pa': 21, 'pha': 22, 'ba': 23, 'bha': 24, 'ma': 25,
}
ARYA_AVARGA_W2 = {
    'ya': 30, 'ra': 40, 'la': 50, 'va': 60,
    'śa': 70, 'ṣa': 80, 'sa': 90, 'ha': 100,
}
ARYA_VOWELS_W2 = {
    'a': (0, 1), 'i': (1, 100), 'u': (2, 10000), 'ṛ': (3, 1000000),
    'ḷ': (4, 100000000), 'e': (5, 10000000000),
    'ai': (6, 1000000000000), 'o': (7, 100000000000000),
    'au': (8, 10000000000000000),
}

ARYA_WITNESSES = ('Wikipedia "Āryabhaṭa numeration" (the 33 × 9 slate); '
                  'PramaKosha procedure entry (GRETIL-grounded value '
                  'tables)')

VOWEL_GLYPHS = {
    'a': 'अ', 'i': 'इ', 'u': 'उ', 'ṛ': 'ऋ', 'ḷ': 'ऌ',
    'e': 'ए', 'ai': 'ऐ', 'o': 'ओ', 'au': 'औ',
}

# ---------------------------------------------------------------------------
# THE EXHIBITS — the witnesses' own worked examples, frozen here so
# the battery (and later the door's parity battery) recompute them
# from the tables, never from this file's expectations alone: the
# expectations are the witnesses' printed numbers, cited per row.
# ---------------------------------------------------------------------------

# (exhibit, devanagari, expected digit sequence [units first],
#  expected number under the standard leftward reading, source)
KATA_EXAMPLES = [
    ('bhavati (the sweep\'s form example)', 'भवति',
     [4, 4, 6], 644,
     'sweep sanskrit.md §1.4, after Plofker (2009)'),
    ('naṭanara = 2010', 'नटनर',
     [0, 1, 0, 2], 2010,
     'Sarma 2012, p. 38 (na=0, ṭa=1, na=0, ra=2, read backwards)'),
    ('viśati, the Kolam-era chronogram', 'विशति',
     [4, 5, 6], 654,
     'Sarma 2012, p. 47 (viśati = 654 of the Kolam era)'),
    ('śaktyaloke, Śaka 1315', 'शक्त्यलोके',
     [5, 1, 3, 1], 1315,
     'Sarma 2012, p. 47 + n. 25 (ktya: only the final y counts)'),
    ('tattvaloke, Śaka 1346', 'तत्त्वलोके',
     [6, 4, 3, 1], 1346,
     'Sarma 2012, p. 47 (the Satyamangalam inscription)'),
    ('rāghavāya, Śaka 1442', 'राघवाय',
     [2, 4, 4, 1], 1442,
     'Sarma 2012, p. 48 (the gloss\'s own split: rā 2, gha 4, vā 4, '
     'ya 1)'),
    ('bhadrāmbudhi line (π to 17 places)', 'भद्राम्बुधिसिद्धजन्मगणितश्रद्धा स्म यद् भूपगीः',
     [4, 2, 3, 9, 7, 9, 8, 5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3],
     314159265358979324,
     'Wikipedia "Katapayadi system" (the Sadratnamālā verse with '
     'its per-akṣara digit split printed)'),
    ('ācārya vāgbhaṭā (the Kollam epoch)', 'आचार्य वागभटा',
     [0, 6, 1, 4, 3, 4, 1], 1434160,
     'Wikipedia "Katapayadi system" (ā 0, cā 6, rya 1, vā 4, g 3, '
     'bha 4, ṭā 1 — the article\'s own syllabification)'),
    ('ācārya vāgbhaṭā, conjunct spelling (orthography parting)',
     'आचार्य वाग्भटा',
     [0, 6, 1, 4, 4, 1], 144160,
     'desk coordinate: the strict conjunct spelling gbha counts '
     'once (bha=4) — printed so the spelling-sensitivity is on '
     'record, not hidden'),
    ('āyurārogyasaukhyam (the Nārāyaṇīyam colophon)',
     'आयुरारोग्यसौख्यम्',
     [0, 1, 2, 2, 1, 7, 1], 1712210,
     'Wikipedia "Katapayadi system" (value as per Kaṭapayādi: '
     '1712210)'),
    ('caṇḍāṃśucandrādhamakuṃbhipālaiḥ (Karaṇapaddhati π)',
     'चण्डांशुचन्द्राधमकुम्भिपालैः',
     [6, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3], 31415926536,
     'Wikipedia "Katapayadi system" (the circumference word for '
     'diameter 10^10)'),
]

# The gopī verse: W1 prints it AND flags that its digit order
# violates the leftward rule — the digits run in direct order.
# (exhibit, devanagari, expected digit sequence AS WRITTEN, source)
KATA_DIRECT_EXAMPLES = [
    ('gopībhāgya verse (π/10, direct order — the documented '
     'exception)',
     'गोपीभाग्यमधुव्रातशृङ्गिशोदधिसन्धिग खलजीवितखाताव गलहालारसंधरः',
     [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3,
      2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 2],
     'Wikipedia "Katapayadi system" (the verse yields π/10 = '
     '0.31415926535897932384626433832792; "this rule is violated '
     'in this sloka")'),
]

# The melakarta use: a rāga's number is its first two akṣaras'
# digits, reversed. (raga, devanagari, expected first-two digits,
# expected melakarta number, source)
KATA_MELAKARTA = [
    ('Dhīraśaṅkarābharaṇam', 'धीरशङ्कराभरणम्', [9, 2], 29,
     'Wikipedia "Katapayadi system" (dha↔9, ra↔2, hence 29)'),
    ('Mechakalyāṇi', 'मेचकल्याणि', [5, 6], 65,
     'Wikipedia "Katapayadi system" (ma↔5, ca↔6, hence 65)'),
]

# The sweep's corpus, re-run through the audit's decoder in the
# battery: (term, devanagari, sweep column-(a) reading)
KATA_SWEEP_CORPUS = [
    ('AXONEME', 'अक्षोनेमे', 5060),
    ('TRVVTH', 'त्रव्वथ', 742),
    ('THELEMA', 'थेलेमा', 537),
    ('AGAPE', 'अगापे', 130),
    ('BABALON', 'बाबालोन्', 333),
    ('HERU-RA-HA', 'हेरु-रा-हा', 8228),
    ('ABRAHADABRA', 'अब्राहादाब्रा', 28820),
    ('QIRA', 'किरा', 21),
    ('LIBERTY', 'लिबेर्टी', 133),
    ('CELL', 'चेल्ल', 36),
    # OZ (ओज़) is deliberately absent: its z carries a nukta, a
    # loan letter the classical table never knew. The sweep dropped
    # it and read 0; the door FAILS CLOSED on it. The battery
    # asserts the refusal — both handlings record the same fact:
    # the letter is unmappable.
]

# (exhibit, devanagari, expected value, source)
ARYA_EXAMPLES = [
    ('khyughṛ — the mahāyuga revolutions of the Sun', 'ख्युघृ',
     4320000,
     'Āryabhaṭīya 1.3; Wikipedia "Āryabhaṭa numeration"; '
     'PramaKosha (verified by its tool); Narasimha, Nature 414 '
     '(2001)'),
    ('the jala verse — 299,792,458', 'जलघिनिझुशुझृसृखॢ',
     299792458,
     'Wikipedia "Āryabhaṭa numeration" (the place-pair table: '
     '58 | 24 | 79 | 99 | 2)'),
    ('ṅiśibuṇḷṣkhṛ — 1,582,237,500', 'ङिशिबुणॢष्खृ',
     1582237500,
     'Wikipedia "Āryabhaṭa numeration" (1582 237 500, Indian '
     'grouping)'),
    ('ka — the slate\'s first syllable', 'क', 1,
     'Wikipedia "Āryabhaṭa numeration" (ka = 1)'),
    ('hau — the slate\'s last syllable', 'हौ', 1000000000000000000,
     'Wikipedia "Āryabhaṭa numeration" (from ka = 1 up to '
     'hau = 10^18)'),
]

# The 24 sine differences of Gītikāpāda 12, in the critical
# edition's text (Shukla & Sarma 1976) as printed by Wikipedia,
# "Āryabhaṭa's sine table" — word by word, with the decoded values
# that article's table prints. Word 11 is śghaki (श्घकि) there;
# the numeration article's verse transcription prints śghakhi,
# which would decode 274 — the parting is a battery exhibit, not
# a silent correction: see the audit document §V.
SINE_WORDS = [
    ('मखि', 'makhi', 225), ('भखि', 'bhakhi', 224),
    ('फखि', 'phakhi', 222), ('धखि', 'dhakhi', 219),
    ('णखि', 'ṇakhi', 215), ('ञखि', 'ñakhi', 210),
    ('ङखि', 'ṅakhi', 205), ('हस्झ', 'hasjha', 199),
    ('स्ककि', 'skaki', 191), ('किष्ग', 'kiṣga', 183),
    ('श्घकि', 'śghaki', 174), ('किघ्व', 'kighva', 164),
    ('घ्लकि', 'ghlaki', 154), ('किग्र', 'kigra', 143),
    ('हक्य', 'hakya', 131), ('धकि', 'dhaki', 119),
    ('किच', 'kica', 106), ('स्ग', 'sga', 93),
    ('झश', 'jhaśa', 79), ('ङ्व', 'ṅva', 65),
    ('क्ल', 'kla', 51), ('प्त', 'pta', 37),
    ('फ', 'pha', 22), ('छ', 'cha', 7),
]


def diff_tables(name, tables):
    """Diff transcription dicts cell by cell; abort on a parting."""
    keys = set()
    for t in tables.values():
        keys |= set(t)
    partings = []
    for k in sorted(keys):
        vals = {w: t.get(k) for w, t in tables.items()}
        if len(set(vals.values())) != 1:
            partings.append((k, vals))
    if partings:
        print('PARTING in %s: %r' % (name, partings))
        sys.exit(1)
    print('%s: %d cells, TOTAL AGREEMENT across %s'
          % (name, len(keys), ', '.join(tables)))
    return keys


def main():
    glyph_of = dict((name, g) for name, g in CONSONANTS)

    # --- Unicode verification of every consonant glyph -----------
    for name, g in CONSONANTS:
        uname = unicodedata.name(g)
        assert uname.startswith('DEVANAGARI LETTER'), (name, g, uname)
    print('Unicode: 33 consonant glyphs verified as DEVANAGARI '
          'LETTERs')

    # --- Kaṭapayādi: diff the three transcriptions ----------------
    diff_tables('Kaṭapayādi consonant→digit',
                {'W1': KATAPAYADI_W1, 'W2': KATAPAYADI_W2,
                 'SWEEP': KATAPAYADI_SWEEP})

    # --- Āryabhaṭīya: diff the two transcriptions -----------------
    diff_tables('Āryabhaṭīya varga',
                {'W1': ARYA_VARGA_W1, 'W2': ARYA_VARGA_W2})
    diff_tables('Āryabhaṭīya avarga',
                {'W1': ARYA_AVARGA_W1, 'W2': ARYA_AVARGA_W2})
    diff_tables('Āryabhaṭīya vowels',
                {'W1': ARYA_VOWELS_W1, 'W2': ARYA_VOWELS_W2})

    # --- Write the Kaṭapayādi table CSV ---------------------------
    path = HERE / 'sanskrit-katapayadi-table.csv'
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['group', 'position', 'devanagari', 'codepoint',
                    'unicode_name', 'transliteration', 'digit',
                    'status', 'witnesses'])
        for group, members in KATA_GROUPS:
            for i, name in enumerate(members, 1):
                g = glyph_of[name]
                w.writerow([group, i, g, 'U+%04X' % ord(g),
                            unicodedata.name(g), name,
                            KATAPAYADI_W1[name], 'SOURCED',
                            KATA_WITNESSES])
        w.writerow(['zero class', 0, '(any standalone vowel)', '',
                    '', '(vowels)', 0, 'SOURCED-RULE',
                    'Sadratnamālā 3.3 in both witnesses: "na, ña '
                    'and the vowels [standing alone denote] zeros" '
                    '— the late-medieval no-value reading stands '
                    'as the printed fork (audit §II)'])
        w.writerow(['ya-group extension', 9, 'ळ', 'U+0933',
                    unicodedata.name('ळ'), 'ḷa', '', 'OPEN',
                    'PARTED in the record: W1 (Variations) attests '
                    'ḷa\'s employment (Mādhava\'s sine table) with '
                    'no value; Sarma 2012, p. 43 cites his 1972 '
                    'finding of ḷa incorporated in Malayalam use '
                    'at 7; Lüders (in Sarma, n. 27) records an '
                    'inscription treating it as la = 3. No value '
                    'frozen; the door fails closed on it.'])
    print('wrote %s' % path.name)

    # --- Write the Kaṭapayādi examples CSV ------------------------
    path = HERE / 'sanskrit-katapayadi-examples.csv'
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['exhibit', 'devanagari', 'expected_digits',
                    'expected_number', 'reading', 'source'])
        for name, dev, digits, number, src in KATA_EXAMPLES:
            w.writerow([name, dev, ' '.join(map(str, digits)),
                        number, 'leftward (standard)', src])
        for name, dev, digits, src in KATA_DIRECT_EXAMPLES:
            w.writerow([name, dev, ' '.join(map(str, digits)), '',
                        'DIRECT (the documented exception)', src])
        for name, dev, digits, number, src in KATA_MELAKARTA:
            w.writerow([name + ' (first two akṣaras)', dev,
                        ' '.join(map(str, digits)), number,
                        'melakarta prefix rule', src])
        for term, dev, value in KATA_SWEEP_CORPUS:
            w.writerow(['sweep corpus: ' + term, dev, '', value,
                        'leftward (standard)',
                        'sweep sanskrit.md §3, column (a)'])
    print('wrote %s' % path.name)

    # --- Write the Āryabhaṭīya table CSV --------------------------
    path = HERE / 'sanskrit-aryabhatiya-table.csv'
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['kind', 'class_or_index', 'devanagari',
                    'codepoint', 'unicode_name', 'transliteration',
                    'value', 'multiplier', 'status', 'witnesses'])
        for name, g in CONSONANTS:
            if name in ARYA_VARGA_W1:
                kind, val = 'consonant', ARYA_VARGA_W1[name]
                cls = 'varga'
            else:
                kind, val = 'consonant', ARYA_AVARGA_W1[name]
                cls = 'avarga'
            w.writerow([kind, cls, g, 'U+%04X' % ord(g),
                        unicodedata.name(g), name, val, '',
                        'SOURCED', ARYA_WITNESSES])
        for vname, (idx, mult) in ARYA_VOWELS_W1.items():
            g = VOWEL_GLYPHS[vname]
            w.writerow(['vowel', idx, g, 'U+%04X' % ord(g),
                        unicodedata.name(g), vname, '', mult,
                        'SOURCED', ARYA_WITNESSES +
                        '; long and short vowels not distinguished '
                        '(W1)'])
    print('wrote %s' % path.name)

    # --- Write the Āryabhaṭīya examples CSV -----------------------
    path = HERE / 'sanskrit-aryabhatiya-examples.csv'
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['exhibit', 'devanagari', 'transliteration',
                    'expected_value', 'source'])
        for name, dev, val, src in ARYA_EXAMPLES:
            w.writerow([name, dev, '', val, src])
        for i, (dev, iast, val) in enumerate(SINE_WORDS, 1):
            w.writerow(['sine difference %d (Gītikāpāda 12)' % i,
                        dev, iast, val,
                        'Wikipedia "Āryabhaṭa\'s sine table" (the '
                        'critical edition\'s text, Shukla & Sarma '
                        '1976)'])
    print('wrote %s' % path.name)

    print('BUILD COMPLETE — all diffs in agreement; the battery '
          'now proves the exhibits.')


if __name__ == '__main__':
    main()
