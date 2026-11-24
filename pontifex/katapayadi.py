#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — katapayadi.py — the Sanskrit doors: the Kaṭapayādi
# encoder and the Āryabhaṭīya positional cipher.
#
# Epigraph: "na, ña and the vowels [standing alone denote] zeros;
# [the consonants] beginning with ka, ṭa, pa and ya, [denote
# severally] the numbers [1 to 9]; in a conjunct [consonant, only]
# the consonant in the penultimate [place, which is followed by a
# vowel, denotes a] number; and a consonant not attached to a vowel
# should not be considered [as a number]." — Śaṅkaravarman,
# Sadratnamālā (1819), 3.3, in Sarma's translation.
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n. (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open
# to the author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the Sanskrit field holds no weighing bank, but it
#     holds two honest instruments — an encoder and a positional
#     cipher — and the engine can serve both as DOORS (decode and
#     encode) without ever seating them as banks.
#   Method: the tables are seated here exactly as the Phase I audit
#     froze them (research/twelve-tongues/sanskrit-*-table.csv,
#     transcribed from the witnesses named in the audit and diffed
#     cell by cell); one akṣara parser serves both decoders, since
#     both systems read the same script; every claim the module
#     makes is proven by test_sanskrit_parity.py against the
#     audit's frozen data.
#   Observation / Result: in the audit document of record,
#     THE-SANSKRIT-FIELD-PHASE-I-AUDIT.md.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""The Sanskrit doors — decode and encode, never weigh.

SPECIES FENCE (load-bearing): this module is NOT a weighing
system, and it registers nothing in engine.SYSTEMS. The house's
weighing banks answer the question "what does this word weigh?"
Neither Sanskrit system asks that question:

  KAṬAPAYĀDI answers "what number does this syllable-string
    ENCODE?" — consonants denote decimal digits (ka-group,
    ṭa-group, pa-group, ya-group), a standalone vowel denotes 0,
    a conjunct counts only its last consonant, a consonant with
    no vowel counts nothing, and the digits are read leftward
    (aṅkānāṃ vāmatō gatiḥ: the first akṣara is the units digit).
    Decoding is a function; encoding is a freedom — many strings
    encode one number, and the tradition's art was choosing the
    meaningful one. katapayadi_decode / katapayadi_encode are the
    two directions of that door.

  ĀRYABHAṬĪYA answers "what number does this syllable-string
    STATE?" — Āryabhaṭa's cipher (Gītikāpāda 2): varga consonants
    carry 1–25, avarga consonants 30–100, and the vowel of each
    syllable multiplies by a power of 100 (a ×1, i ×100, u ×10⁴,
    ṛ ×10⁶, ḷ ×10⁸, e ×10¹⁰, ai ×10¹², o ×10¹⁴, au ×10¹⁶; long
    and short vowels are not distinguished). The number is the
    SUM of the syllables' contributions. aryabhatiya_decode /
    aryabhatiya_encode are its two directions.

FAIL-CLOSED DOCTRINE (the Coptic bank's habit, carried here):
  - a nukta consonant (a Perso-Arabic loan letter, e.g. ज़) is
    unmappable in both systems and raises ValueError;
  - ḷa (ळ, U+0933) raises ValueError at the Kaṭapayādi door: the
    record PARTS on its value (7 in Sarma's Malayalam finding;
    treated as la = 3 in an inscription Lüders records) and W1
    attests its employment with no value — the audit froze the
    row OPEN, and an open row is a refusal, not a guess;
  - a vowelless (halant-final) cluster raises ValueError at the
    Āryabhaṭīya door (his syllables all bear vowels; the cipher
    has no seat for a bare consonant), while the Kaṭapayādi door
    ignores it, exactly as Sadratnamālā rules;
  - any character outside the two systems' script raises
    ValueError. Silence would be a false weight; a refusal is a
    reading.
"""

import unicodedata

# ---------------------------------------------------------------------------
# MECHANISM: the script's seats. Consonant glyphs are generated from
# the consonant list by name; the batteries verify every glyph's
# Unicode name against the standard, so a seat cannot drift.
# ---------------------------------------------------------------------------

_CONSONANT_NAMES = [
    'ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja', 'jha', 'ña',
    'ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da', 'dha', 'na',
    'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'śa',
    'ṣa', 'sa', 'ha',
]
_CONSONANT_GLYPHS = [
    'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
    'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
    'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
    'ष', 'स', 'ह',
]
GLYPH_OF = dict(zip(_CONSONANT_NAMES, _CONSONANT_GLYPHS))
NAME_OF = dict(zip(_CONSONANT_GLYPHS, _CONSONANT_NAMES))

LLA = 'ळ'  # U+0933 DEVANAGARI LETTER LLA — the OPEN row (see fence)

# ---------------------------------------------------------------------------
# THE KAṬAPAYĀDI TABLE — consonant glyph -> digit, exactly as the
# Phase I audit froze it (three transcriptions in total agreement:
# Wikipedia's arrangement table; Sarma 2012, p. 39 + Appendix;
# the sweep draft). Provenance: ATTESTED (the tradition's own
# table, Sadratnamālā 3.3 and the anonymous rule-verses).
# ---------------------------------------------------------------------------

KATAPAYADI_DIGITS = {
    'क': 1, 'ख': 2, 'ग': 3, 'घ': 4, 'ङ': 5, 'च': 6, 'छ': 7,
    'ज': 8, 'झ': 9, 'ञ': 0,
    'ट': 1, 'ठ': 2, 'ड': 3, 'ढ': 4, 'ण': 5, 'त': 6, 'थ': 7,
    'द': 8, 'ध': 9, 'न': 0,
    'प': 1, 'फ': 2, 'ब': 3, 'भ': 4, 'म': 5,
    'य': 1, 'र': 2, 'ल': 3, 'व': 4, 'श': 5, 'ष': 6, 'स': 7,
    'ह': 8,
}

# ---------------------------------------------------------------------------
# THE ĀRYABHAṬĪYA TABLES — consonant glyph -> value; vowel -> place
# index (the multiplier is 100**index). As frozen by the audit
# (two transcriptions in total agreement: Wikipedia's 33 × 9
# slate; the PramaKosha procedure entry, GRETIL-grounded).
# Provenance: ATTESTED (Āryabhaṭīya, Gītikāpāda 2).
# ---------------------------------------------------------------------------

ARYABHATIYA_VALUES = {
    'क': 1, 'ख': 2, 'ग': 3, 'घ': 4, 'ङ': 5, 'च': 6, 'छ': 7,
    'ज': 8, 'झ': 9, 'ञ': 10,
    'ट': 11, 'ठ': 12, 'ड': 13, 'ढ': 14, 'ण': 15, 'त': 16,
    'थ': 17, 'द': 18, 'ध': 19, 'न': 20,
    'प': 21, 'फ': 22, 'ब': 23, 'भ': 24, 'म': 25,
    'य': 30, 'र': 40, 'ल': 50, 'व': 60, 'श': 70, 'ष': 80,
    'स': 90, 'ह': 100,
}

# Vowel seats: independent forms and dependent signs both fold to
# the place index; long and short are NOT distinguished (the
# slate's own rule).
_VOWEL_INDEX = {
    'a': 0, 'i': 1, 'u': 2, 'ṛ': 3, 'ḷ': 4,
    'e': 5, 'ai': 6, 'o': 7, 'au': 8,
}
_INDEPENDENT_VOWELS = {
    'अ': 'a', 'आ': 'a', 'इ': 'i', 'ई': 'i', 'उ': 'u', 'ऊ': 'u',
    'ऋ': 'ṛ', 'ॠ': 'ṛ', 'ऌ': 'ḷ', 'ॡ': 'ḷ',
    'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
}
_DEPENDENT_SIGNS = {
    'ा': 'a', 'ि': 'i', 'ी': 'i', 'ु': 'u', 'ू': 'u',
    'ृ': 'ṛ', 'ॄ': 'ṛ', 'ॢ': 'ḷ', 'ॣ': 'ḷ',
    'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',
}
_SIGN_OF_INDEX = {
    0: '', 1: 'ि', 2: 'ु', 3: 'ृ', 4: 'ॢ',
    5: 'े', 6: 'ै', 7: 'ो', 8: 'ौ',
}

_VIRAMA = '्'
_ANUSVARA = 'ं'
_VISARGA = 'ः'
_CANDRABINDU = 'ँ'
_NUKTA = '़'
_MARKS = {_ANUSVARA, _VISARGA, _CANDRABINDU}
_SEPARATORS = set(' \t\n\r-—–|।॥,;:()·')

_CONSONANT_SET = set(_CONSONANT_GLYPHS) | {LLA}


def parse_aksaras(text):
    """Split a Devanagari string into akṣaras.

    MECHANISM: an akṣara is either a standalone vowel or a
    consonant cluster (consonants joined by virāma) bearing one
    vowel — a dependent sign, the inherent 'a', or None when the
    cluster is halant-final (vowelless). Anusvāra, visarga and
    candrabindu are marks: they ride on an akṣara and carry no
    value in either system, so the parser notes and sets them
    aside. Separators (spaces, daṇḍas, hyphens, punctuation) are
    skipped. Anything else — a nukta loan letter above all —
    raises ValueError: the doors fail closed.

    Returns a list of dicts: {consonants: [glyphs], vowel: key or
    None, standalone: bool}.
    """
    aksaras = []
    chars = list(text)
    i, n = 0, len(chars)
    while i < n:
        ch = chars[i]
        if ch in _SEPARATORS:
            i += 1
            continue
        if ch in _MARKS:
            i += 1  # a mark with no value in either system
            continue
        if ch in _INDEPENDENT_VOWELS:
            aksaras.append({'consonants': [],
                            'vowel': _INDEPENDENT_VOWELS[ch],
                            'standalone': True})
            i += 1
            continue
        if ch in _CONSONANT_SET:
            cluster = [ch]
            i += 1
            if i < n and chars[i] == _NUKTA:
                raise ValueError(
                    'nukta loan letter %s़ is unmappable in the '
                    'classical tables' % ch)
            while (i + 1 < n and chars[i] == _VIRAMA
                   and chars[i + 1] in _CONSONANT_SET):
                cluster.append(chars[i + 1])
                i += 2
                if i < n and chars[i] == _NUKTA:
                    raise ValueError(
                        'nukta loan letter is unmappable in the '
                        'classical tables')
            if i < n and chars[i] in _DEPENDENT_SIGNS:
                vowel = _DEPENDENT_SIGNS[chars[i]]
                i += 1
            elif i < n and chars[i] == _VIRAMA:
                vowel = None  # halant-final: no vowel bears it
                i += 1
            else:
                vowel = 'a'  # the inherent vowel
            aksaras.append({'consonants': cluster, 'vowel': vowel,
                            'standalone': False})
            continue
        raise ValueError('character %r (U+%04X %s) is outside the '
                         'two systems\' script'
                         % (ch, ord(ch), unicodedata.name(ch, '?')))
    return aksaras


# ---------------------------------------------------------------------------
# KAṬAPAYĀDI — the encoder's two directions.
# ---------------------------------------------------------------------------

def katapayadi_digits(text):
    """The digit sequence of a Kaṭapayādi string, units first.

    DOCTRINE (Sadratnamālā 3.3): a standalone vowel denotes 0; a
    consonant cluster denotes the digit of its LAST consonant;
    a vowelless (halant) consonant denotes nothing and is
    skipped. ḷa raises ValueError — its row stands OPEN in the
    audit (the record parts on its value), and an open row is a
    refusal, not a guess.
    """
    digits = []
    for ak in parse_aksaras(text):
        if ak['standalone']:
            digits.append(0)
            continue
        if ak['vowel'] is None:
            continue  # halant: "not to be considered"
        last = ak['consonants'][-1]
        if last == LLA:
            raise ValueError(
                'ḷa (ळ) stands OPEN in the audit — the record '
                'parts on its value (7 in Sarma\'s Malayalam '
                'finding; la = 3 in the inscription Lüders '
                'records); the door fails closed')
        digits.append(KATAPAYADI_DIGITS[last])
    return digits


def katapayadi_decode(text):
    """Decode a Kaṭapayādi string to its number.

    The digits are read leftward (aṅkānāṃ vāmatō gatiḥ): the
    first akṣara is the units digit. Deterministic — the same
    string always yields the same number.
    """
    value = 0
    for i, d in enumerate(katapayadi_digits(text)):
        value += d * (10 ** i)
    return value


# Canonical representatives per digit, one set per group — the
# encoder's freedom made visible: any set serves, because the
# decoder reads digits, not letters.
_KATA_REPS = {
    'ka': {0: 'ञ', 1: 'क', 2: 'ख', 3: 'ग', 4: 'घ', 5: 'ङ',
           6: 'च', 7: 'छ', 8: 'ज', 9: 'झ'},
    'ta': {0: 'न', 1: 'ट', 2: 'ठ', 3: 'ड', 4: 'ढ', 5: 'ण',
           6: 'त', 7: 'थ', 8: 'द', 9: 'ध'},
    'ya': {0: 'ञ', 1: 'य', 2: 'र', 3: 'ल', 4: 'व', 5: 'श',
           6: 'ष', 7: 'स', 8: 'ह', 9: 'झ'},
}


def katapayadi_encode(number, variant='ka'):
    """Encode a non-negative integer as a Kaṭapayādi string.

    MECHANISM: the number's decimal digits, units first, each
    wearing the chosen group's representative consonant with the
    inherent vowel 'a'. The result is a CANONICAL encoding, not
    a verse: the tradition's encoders chose freely among the
    representatives (and all vowels) to make meaning; this door
    proves the freedom by offering three representative sets,
    all decoding back to the same number.
    """
    if number < 0:
        raise ValueError('Kaṭapayādi encodes non-negative '
                         'integers; there is no sign in the system')
    reps = _KATA_REPS[variant]
    digits = [int(c) for c in str(number)][::-1]
    return ''.join(reps[d] for d in digits)


# ---------------------------------------------------------------------------
# ĀRYABHAṬĪYA — the cipher's two directions.
# ---------------------------------------------------------------------------

def aryabhatiya_decode(text):
    """Decode an Āryabhaṭīya syllable string to its number.

    DOCTRINE (Gītikāpāda 2): every consonant of a syllable counts
    (a cluster shares its vowel — the opposite of Kaṭapayādi's
    last-only rule); each contributes its value × 100^(vowel
    index); the number is the sum. A standalone vowel contributes
    nothing (the cipher's syllables are consonant-born). A
    vowelless cluster fails closed: his syllables bear vowels.
    """
    total = 0
    for ak in parse_aksaras(text):
        if ak['standalone'] or not ak['consonants']:
            continue
        if ak['vowel'] is None:
            raise ValueError(
                'a vowelless cluster has no seat in the '
                'Āryabhaṭīya cipher (his syllables bear vowels)')
        mult = 100 ** _VOWEL_INDEX[ak['vowel']]
        for g in ak['consonants']:
            if g == LLA or g not in ARYABHATIYA_VALUES:
                raise ValueError(
                    '%s has no value in the Āryabhaṭīya table'
                    % g)
            total += ARYABHATIYA_VALUES[g] * mult
    return total


_VARGA_GLYPH = {v: g for g, v in ARYABHATIYA_VALUES.items()
                if v <= 25}
_AVARGA_GLYPH = {v: g for g, v in ARYABHATIYA_VALUES.items()
                 if v > 25}


def _pair_consonants(p):
    """Decompose a place-pair value (1–100) into consonant glyphs.

    MECHANISM: one consonant where the slate offers one (a varga
    value 1–25, an avarga value 30–100 by tens); otherwise two —
    two vargas for 26–49 (25 + remainder), an avarga and a varga
    for the rest (the jala order: varga first, avarga after, as
    in W1's own example ja-la = 8 + 50). Every pair 1–100
    decomposes; the parity battery proves it by round-trip.
    """
    if p in _VARGA_GLYPH:
        return [_VARGA_GLYPH[p]]
    if p in _AVARGA_GLYPH:
        return [_AVARGA_GLYPH[p]]
    if p < 50:
        return [_VARGA_GLYPH[p - 25], _VARGA_GLYPH[25]]
    a = (p // 10) * 10
    return [_VARGA_GLYPH[p - a], _AVARGA_GLYPH[a]]


def aryabhatiya_encode(number):
    """Encode a non-negative integer in the Āryabhaṭīya cipher.

    MECHANISM: the number is split into place-pairs (hundreds);
    each nonzero pair becomes one syllable — its consonants (the
    decomposition above) sharing the pair's vowel — written, as
    Āryabhaṭa writes, from the lowest pair upward. Zero is the
    empty string: the cipher has no zero syllable, and absence
    is its zero — a species trait, printed here rather than
    repaired. The slate's ceiling is hau = 10^18; a number
    needing a tenth pair raises ValueError.
    """
    if number < 0:
        raise ValueError('the Āryabhaṭīya cipher states '
                         'non-negative integers')
    if number == 0:
        return ''
    pairs = []
    n, idx = number, 0
    while n:
        pairs.append((idx, n % 100))
        n //= 100
        idx += 1
    if pairs[-1][0] > 8:
        # The one boundary case: 10^18 itself, which the slate
        # states as hau — the pair 100 at the ninth vowel (index
        # 8) — not as 1 at a tenth place that does not exist.
        if number == 10 ** 18:
            pairs = [(8, 100)]
        else:
            raise ValueError('beyond the slate: the ninth vowel '
                             '(au) is the last place '
                             '(hau = 10^18)')
    out = []
    for idx, p in pairs:
        if p == 0:
            continue
        cons = _pair_consonants(p)
        out.append(_VIRAMA.join(cons) + _SIGN_OF_INDEX[idx])
    return ''.join(out)


# ---------------------------------------------------------------------------
# THE CHECKS — the module proves itself on the doctrine's printed
# exhibits. The full proof (against the audit's frozen CSVs, the
# other batteries untouched) is test_sanskrit_parity.py.
# ---------------------------------------------------------------------------

def _run(checks):
    return checks


def katapayadi_checks():
    """The Kaṭapayādi door's self-proof, on printed exhibits."""
    out = []

    def chk(name, fn, expected):
        try:
            got = fn()
            out.append((name, got == expected, got))
        except Exception as exc:  # a refusal where a value was due
            out.append((name, False, 'raised %r' % (exc,)))

    chk('bhavati == 644 (the form example)',
        lambda: katapayadi_decode('भवति'), 644)
    chk('naṭanara == 2010 (Sarma\'s example)',
        lambda: katapayadi_decode('नटनर'), 2010)
    chk('the bhadrāmbudhi line == π to 17 places',
        lambda: katapayadi_decode(
            'भद्राम्बुधिसिद्धजन्मगणितश्रद्धा स्म यद् भूपगीः'),
        314159265358979324)
    chk('āyurārogyasaukhyam == 1712210 (the colophon)',
        lambda: katapayadi_decode('आयुरारोग्यसौख्यम्'), 1712210)
    chk('round-trip: decode∘encode == identity, 0..999, '
        'three representative sets',
        lambda: all(
            katapayadi_decode(katapayadi_encode(n, v)) == n
            for v in ('ka', 'ta', 'ya') for n in range(1000)),
        True)
    chk('encoding is free: three distinct strings, one number '
        '(2010)',
        lambda: (len({katapayadi_encode(2010, v)
                       for v in ('ka', 'ta', 'ya')}),
                 {katapayadi_decode(katapayadi_encode(2010, v))
                  for v in ('ka', 'ta', 'ya')}),
        (3, {2010}))
    chk('the conjunct rule: ktya counts only y (digit 1)',
        lambda: katapayadi_digits('क्त्य'), [1])
    chk('the halant rule: a vowelless consonant counts nothing '
        '(BABALON\'s final n)',
        lambda: katapayadi_decode('बाबालोन्'), 333)

    def _lla():
        try:
            katapayadi_decode('ळ')
            return 'decoded (a guess!)'
        except ValueError:
            return 'fails closed'
    chk('ḷa fails closed (its row stands OPEN in the audit)',
        _lla, 'fails closed')

    def _nukta():
        try:
            katapayadi_decode('ओज़')
            return 'decoded (a guess!)'
        except ValueError:
            return 'fails closed'
    chk('a nukta loan letter fails closed (OZ is unmappable)',
        _nukta, 'fails closed')
    return _run(out)


def aryabhatiya_checks():
    """The Āryabhaṭīya door's self-proof, on printed exhibits."""
    out = []

    def chk(name, fn, expected):
        try:
            got = fn()
            out.append((name, got == expected, got))
        except Exception as exc:
            out.append((name, False, 'raised %r' % (exc,)))

    chk('khyughṛ == 4,320,000 (the mahāyuga)',
        lambda: aryabhatiya_decode('ख्युघृ'), 4320000)
    chk('makhi == 225 (the first sine difference)',
        lambda: aryabhatiya_decode('मखि'), 225)
    chk('hau == 10^18 (the slate\'s last syllable)',
        lambda: aryabhatiya_decode('हौ'), 10 ** 18)
    chk('the jala verse == 299,792,458',
        lambda: aryabhatiya_decode('जलघिनिझुशुझृसृखॢ'),
        299792458)
    chk('round-trip: decode∘encode == identity, 0..9999',
        lambda: all(
            aryabhatiya_decode(aryabhatiya_encode(n)) == n
            for n in range(10000)),
        True)
    chk('round-trip on the exhibits (4,320,000; 299,792,458; '
        '1,582,237,500; 10^18)',
        lambda: all(
            aryabhatiya_decode(aryabhatiya_encode(n)) == n
            for n in (4320000, 299792458, 1582237500, 10 ** 18)),
        True)
    chk('encoding is free: pair 29 takes two decompositions '
        '(na+jha, gha+ma), both decoding to 29',
        lambda: (aryabhatiya_decode('न्झ') == 29
                 and aryabhatiya_decode('घ्म') == 29),
        True)
    chk('zero is absence: encode(0) is the empty string and '
        'decodes to 0',
        lambda: (aryabhatiya_encode(0),
                 aryabhatiya_decode('')),
        ('', 0))
    return _run(out)


__all__ = [
    'KATAPAYADI_DIGITS', 'ARYABHATIYA_VALUES',
    'parse_aksaras',
    'katapayadi_digits', 'katapayadi_decode', 'katapayadi_encode',
    'aryabhatiya_decode', 'aryabhatiya_encode',
    'katapayadi_checks', 'aryabhatiya_checks',
]
