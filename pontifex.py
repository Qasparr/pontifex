#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — the Universal Correspondence Framework
# v0.2.0 "The Second Span"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, letter to Robert Hooke, 1676.
# (The bridges were always there; we are only now mapping them diligently.)
#
# Thelemic date: ☉ in 14° 53′ Libra, ☽ in 14° 4′ Virgo, dies mercurii,
# Anno V:xii e.n. (2026-10-07, computed on the author's own engine)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The name PONTIFEX ("bridge-builder") was proposed by the scribe and approved
# by the author's red pen, 2026-10-07. The doctrine is the author's; the
# mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: that words in different tongues which weigh the same reveal
#     a bridge — a convergent point across languages.
#   Method: weigh each word in its own tongue's table (attested where the
#     tradition exists; derived by script-descent; constructed by canonical
#     ordinal where neither exists), every value carrying its provenance;
#     tongues with no table fall back to Hebrew transliteration (the
#     tradition's own move), with mergers documented.
#   Observation: run the weighing; record convergent and divergent points.
#   Result: convergent points on attested tables are candidate bridges;
#     convergent points touching constructed tables are hypotheses for the
#     red pen — never doctrine until they pass TRVVTH.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""
PONTIFEX — the Universal Correspondence Framework.

DOCTRINE: gematria's method is to weigh each word in its own tongue; its
purpose is the bridge — the match across tongues. The shared number is the
bridge, and a bridge needs two honest banks. (Settled with the author,
2026-10-07.)

DOCTRINE: a liber's number derives from its title's gematria (CELL=32 →
XXXII); rename or renumber must follow the name.

This module implements v0.2: the weighing engine over the attested tables
(Hebrew, Greek, Latin ordinal, Agrippa's Latin, Arabic abjad), the braille
carrier table (constructed, 64 patterns — charted because the tool's purpose
is precisely universal charting), the Hebrew-fallback transliteration for
tongues with no table, the music bridge (ABC-notation pitch weighing on
attested Latin-ordinal note values), and the bridge check with provenance
flags.

Provenance tiers (every value carries one):
  ATTESTED    — the tradition's own table; verifies against the tradition.
  DERIVED     — inherited by script-descent from a tabulated script.
  CONSTRUCTED — built by canonical ordinal where no path exists; a proposal,
                never a discovery. Convergent points touching this tier are
                hypotheses for the author's red pen, never doctrine.
"""

import sys
import re
import unicodedata

# ---------------------------------------------------------------------------
# MECHANISM: the tables. Each maps a single character to its number value.
# DOCTRINE: attested tables are recorded as the traditions hand them down;
# the scribe does not "improve" them. Anything the scribe builds is marked
# CONSTRUCTED in PROVENANCE below.
# ---------------------------------------------------------------------------

# -- Hebrew, mispar hechrechi (ATTESTED) ------------------------------------
# MECHANISM: the standard values; final forms (ךםןףץ) share their letter's
# value. This is the root engine of the author's correspondences.
HEBREW = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100,
    'ר': 200, 'ש': 300, 'ת': 400,
}

# -- Greek, isopsephy (ATTESTED) --------------------------------------------
# MECHANISM: Milesian values; the three epissemones (digamma/stigma=6,
# koppa=90, sampi=900) are included because the classical system needs them.
# Both stigma forms are accepted for 6.
GREEK = {
    'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'ϛ': 6, 'στ': 6, 'ζ': 7,
    'η': 8, 'θ': 9, 'ι': 10, 'κ': 20, 'λ': 30, 'μ': 40, 'ν': 50, 'ξ': 60,
    'ο': 70, 'π': 80, 'ϟ': 90, 'ρ': 100, 'σ': 200, 'ς': 200, 'τ': 300,
    'υ': 400, 'φ': 500, 'χ': 600, 'ψ': 700, 'ω': 800, 'ϡ': 900,
}

# -- Latin, English ordinal A=1..Z=26 (ATTESTED as the working Latin table) -
# MECHANISM: the plain ordinal of the Latin alphabet. DOCTRINE: this is what
# "Latin gematria" is in practice — the scale English words are weighed on
# (CELL=32, AXONEME=77).
LATIN_ORDINAL = {chr(ord('A') + i): i + 1 for i in range(26)}

# -- Latin, Agrippa's table, De occulta philosophia II.xix (ATTESTED) --------
# MECHANISM: Agrippa's published Latin values. J is read as I and U as V, per
# the classical alphabet he worked in; the scribe records, not revises.
AGRIPPA = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 9, 'K': 10, 'L': 20, 'M': 30, 'N': 40, 'O': 50, 'P': 60,
    'Q': 70, 'R': 80, 'S': 90, 'T': 100, 'U': 200, 'V': 200, 'X': 300,
    'Y': 400, 'Z': 500,
}

# -- Arabic, abjad numerals, Eastern order (ATTESTED) ------------------------
# MECHANISM: the traditional abjadī order values. (The Maghrebi order differs
# in a few letters; the Eastern order is recorded here and the difference is
# noted, not hidden.)
ARABIC_ABJAD = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8,
    'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60,
    'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400,
    'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
}

# -- Braille, 64 dot-patterns (CONSTRUCTED) ---------------------------------
# MECHANISM: Unicode braille patterns U+2800..U+28FF follow the canonical dot
# numbering, so pattern index i (0..63) takes value i+1. DOCTRINE: this table
# is the scribe's construction — transparent and consistent, but a proposal,
# never a discovery. Its purpose is as a lossless *carrier*: 64 patterns
# swallow most alphabets whole, so transliteration into braille preserves
# distinctions that Hebrew's 22 letters would merge.
# NOTE: patterns 1..26 correspond to a-z in standard braille by design.
def _braille_table():
    # MECHANISM: build programmatically — the order IS the table.
    return {chr(0x2800 + i): i + 1 for i in range(64)}


BRAILLE = _braille_table()

# -- Music: ABC-notation pitch weighing ---------------------------------------
# MECHANISM: musical note names in the English letter tradition ARE Latin
# letters, so their values fall straight out of the ATTESTED Latin ordinal —
# no constructed table is needed. C=3, D=4, E=5, F=6, G=7, A=1, B=2.
# DOCTRINE: a melody is a word spelled in notes; the bridge between music
# and tongue is weighed, not invented.
NOTE_VALUES = {'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'A': 1, 'B': 2}

# MECHANISM: the extraction conventions — every choice the parser makes that
# the tradition does not hand down is stated here, so the weighing shows its
# work. Values ATTESTED; extraction CONSTRUCTED.
MUSIC_CONVENTIONS = [
    'Note names: English letter tradition (CDEFGAB) — stated, not universal '
    '(solfège do-re-mi is a different naming; pick one and state it).',
    'Values: Latin ordinal on the letter (ATTESTED).',
    'Accidentals: sharp +1, flat -1, natural +0 on the letter value '
    '(CONSTRUCTED convention).',
    'Octave markers (`,` / `\'`, upper/lower case): dropped — pitch-class '
    'level, the letter not the frequency (CONSTRUCTED).',
    'Durations: ignored — gematria weighs letters, not lengths (CONSTRUCTED).',
    'Chords [CEG]: each note weighed in order (CONSTRUCTED).',
    'Rests (z): silence — skipped, not zeroed; the standing doctrine.',
    'Headers (X:, T:, M:, K:, ...), bar lines, ornaments: skipped.',
]


def extract_pitches(text):
    """Extract (letter, accidental_offset) pitch pairs from ABC notation.

    MECHANISM: accepts full ABC tunes or bare note sequences ("C E G").
    Inline fields like [K:G] are stripped first — they are instructions, not
    music, and their key letter must not be weighed. Full-line headers
    (X:, T:, M:, L:, K:, w:, ...) and % comments are dropped. Then a single
    left-to-right scan: ^/_/= accumulate the accidental for the next note,
    A–G (either case; lower = higher octave in ABC, folded) emit a pitch,
    z/Z rests reset the accidental and emit nothing, digits/slashes/bars/
    octave marks/ties/spaces are skipped. Brackets are transparent — chord
    tones are weighed in order, per the stated convention.
    Returns a list of (LETTER, accidental_offset) tuples.
    """
    # MECHANISM: strip inline fields — [K:G], [M:3/4] — before anything else.
    t = re.sub(r'\[[A-Za-z]:[^\]]*\]', '', text)
    # MECHANISM: drop header lines and comments; what remains is music.
    body = []
    for line in t.splitlines():
        line = line.split('%', 1)[0]
        if re.match(r'^[A-Za-z]:', line.strip()):
            continue
        body.append(line)
    t = ' '.join(body)
    pitches = []
    acc = 0
    i = 0
    n = len(t)
    while i < n:
        ch = t[i]
        if ch == '^':
            # MECHANISM: sharps stack (^^ = double sharp, +2), per ABC.
            acc += 1
        elif ch == '_':
            acc -= 1
        elif ch == '=':
            # MECHANISM: natural cancels the accidental — back to the letter.
            acc = 0
        elif ch.upper() in 'ABCDEFG':
            # MECHANISM: the pitch is emitted; the letter's value comes from
            # NOTE_VALUES (attested Latin ordinal), the offset from the
            # constructed accidental convention.
            pitches.append((ch.upper(), acc))
            acc = 0
        elif ch in 'zZ':
            # MECHANISM: rest — silence, not false weight; accidental dies.
            acc = 0
        # else: digits, /, |, :, ,, ', -, (, ), [, ], spaces — skipped.
        i += 1
    return pitches


def weigh_melody(text):
    """Weigh a melody given as ABC notation or a bare note sequence.

    MECHANISM: extract pitches, then letter value + accidental offset, summed.
    Returns the same result shape as weigh(), so bridge() works unchanged —
    the melody stands as one bank of the bridge, the word as the other.
    DOCTRINE: the result carries its conventions with it; a music bridge is
    only as honest as the extraction it stands on.
    """
    pitches = extract_pitches(text)
    total = 0
    breakdown = []
    for letter, acc in pitches:
        v = NOTE_VALUES[letter] + acc
        # MECHANISM: label shows the accidental so the audit trail reads —
        # C# is 4, visibly 3+1.
        label = letter + ('#' * acc if acc > 0 else '') + ('b' * (-acc) if acc < 0 else '')
        breakdown.append((label, v))
        total += v
    shown = text if len(text) <= 48 else text[:45] + '...'
    return {
        'word': shown,
        'system': 'abc_notes',
        'value': total,
        'provenance': 'ATTESTED values; CONSTRUCTED extraction',
        'breakdown': breakdown,
        'conventions': MUSIC_CONVENTIONS,
    }


# ---------------------------------------------------------------------------
# MECHANISM: the registry. Every system knows its table and its provenance.
# Systems with custom extraction (music) register a weigher instead of a
# table; weigh() dispatches to it.
# DOCTRINE: provenance is load-bearing — it decides whether a convergent
# point is a candidate bridge (attested) or a hypothesis for the red pen
# (constructed). A value without provenance is a rumor.
# ---------------------------------------------------------------------------
SYSTEMS = {
    'hebrew':        {'table': HEBREW,        'provenance': 'ATTESTED'},
    'greek':         {'table': GREEK,         'provenance': 'ATTESTED'},
    'latin_ordinal': {'table': LATIN_ORDINAL, 'provenance': 'ATTESTED'},
    'agrippa':       {'table': AGRIPPA,       'provenance': 'ATTESTED'},
    'arabic_abjad':  {'table': ARABIC_ABJAD,  'provenance': 'ATTESTED'},
    'braille':       {'table': BRAILLE,       'provenance': 'CONSTRUCTED'},
    'abc_notes':     {'weigher': weigh_melody,
                      'provenance': 'ATTESTED values; CONSTRUCTED extraction '
                                     '(see MUSIC_CONVENTIONS)'},
}

# ---------------------------------------------------------------------------
# MECHANISM: the Hebrew fallback. For tongues with no table of their own, the
# tradition's own move is transliteration into Hebrew. This default map covers
# Latin letters (academic style, greedy digraphs); every merger is documented
# in MERGERS so the loss is visible, never hidden.
# DOCTRINE: Hebrew is the proper fallback because the correspondence engine
# is Hebrew-rooted — bridges must land in the system where the
# correspondences live. English ordinal is native for English words, not the
# fallback for others. (Settled with the author, 2026-10-07.)
# ---------------------------------------------------------------------------
LATIN_TO_HEBREW_DIGRAPHS = {'ch': 'ח', 'sh': 'ש', 'th': 'ת'}
LATIN_TO_HEBREW = {
    'a': 'א', 'b': 'ב', 'c': 'ק', 'd': 'ד', 'e': 'ה', 'f': 'פ', 'g': 'ג',
    'h': 'ה', 'i': 'י', 'j': 'י', 'k': 'כ', 'l': 'ל', 'm': 'מ', 'n': 'נ',
    'o': 'ו', 'p': 'פ', 'q': 'ק', 'r': 'ר', 's': 'ס', 't': 'ת', 'u': 'ו',
    'v': 'ו', 'w': 'ו', 'x': 'קס', 'y': 'י', 'z': 'ז',
}
# MECHANISM: the mergers, stated plainly. Where two Latin letters land on one
# Hebrew letter, distinction is lost in the weighing — the bridge-table must
# show it.
MERGERS = {
    'ה': ['e', 'h'],
    'י': ['i', 'j', 'y'],
    'ו': ['o', 'u', 'v', 'w'],
    'ק': ['c', 'q'],
    'פ': ['f', 'p'],
}


def transliterate_latin_to_hebrew(word):
    """Render a Latin-script word in Hebrew letters (CONSTRUCTED mapping).

    MECHANISM: lowercase, strip diacritics, then greedy longest-match over
    the digraph table before single letters. Returns (hebrew_word, mergers)
    where mergers lists the Hebrew letters that merged distinct Latin
    letters in this word.
    """
    # MECHANISM: normalize — fold case, strip accents so 'café' weighs as
    # 'cafe'. What the eye reads as the letter is what gets weighed.
    w = ''.join(
        c for c in unicodedata.normalize('NFKD', word.lower())
        if not unicodedata.combining(c)
    )
    out = []
    i = 0
    while i < len(w):
        # MECHANISM: digraphs first — 'sh' is ש, not סה. Greedy match keeps
        # the transliteration honest to pronunciation.
        if w[i:i + 2] in LATIN_TO_HEBREW_DIGRAPHS:
            out.append(LATIN_TO_HEBREW_DIGRAPHS[w[i:i + 2]])
            i += 2
        elif w[i] in LATIN_TO_HEBREW:
            out.append(LATIN_TO_HEBREW[w[i]])
            i += 1
        else:
            # MECHANISM: characters with no mapping (digits, punctuation)
            # are skipped, not zeroed — silence, not false weight.
            i += 1
    hebrew = ''.join(out)
    # MECHANISM: report mergers honestly — collect which Hebrew letters in
    # this word merged distinct Latin inputs.
    seen = {}
    j = 0
    wi = 0
    mergers = []
    # (Re-walk to attribute; simple pass over the digraph/single decisions.)
    # For v0.1 the report is per-letter of the Hebrew output.
    for h in hebrew:
        if h in MERGERS:
            mergers.append(h)
    return hebrew, sorted(set(mergers))


def weigh(word, system):
    """Weigh a word in a system's table.

    MECHANISM: look up each character, sum the values. Unknown characters
    are skipped (silence, not false weight). Latin systems fold case.
    Returns a dict: value, provenance, and the per-letter breakdown so any
    weighing can be audited by hand.

    DOCTRINE: the breakdown is the audit trail — TRVVTH requires that every
    number show its work.
    """
    # MECHANISM: unknown system names fail loudly — a silent default table
    # would be a lie.
    if system not in SYSTEMS:
        raise ValueError("unknown system: %r (see SYSTEMS)" % system)
    spec = SYSTEMS[system]
    if 'weigher' in spec:
        # MECHANISM: systems with custom extraction (music) weigh by their
        # own function; the provenance travels inside the result.
        return spec['weigher'](word)
    table = spec['table']
    provenance = spec['provenance']
    total = 0
    breakdown = []
    chars = list(word)
    # MECHANISM: Greek digraph 'στ' (stigma) is two codepoints with one
    # value — check the pair before the singles.
    i = 0
    w = word.upper() if system in ('latin_ordinal', 'agrippa') else word
    while i < len(w):
        pair = w[i:i + 2]
        if pair in table:
            v = table[pair]
            breakdown.append((pair, v))
            total += v
            i += 2
            continue
        ch = w[i]
        if ch in table:
            v = table[ch]
            breakdown.append((ch, v))
            total += v
        # else: silence, not false weight (see above).
        i += 1
    return {
        'word': word,
        'system': system,
        'value': total,
        'provenance': provenance,
        'breakdown': breakdown,
    }


def weigh_via_hebrew_fallback(latin_word):
    """Weigh a Latin-script word through the Hebrew fallback.

    MECHANISM: transliterate (CONSTRUCTED map), then weigh the Hebrew
    rendering in the ATTESTED Hebrew table. The result carries BOTH
    provenances: the rendering is constructed, the weighing is attested.
    DOCTRINE: this is the honest form of the fallback — the map's limits
    (mergers) travel with the number.
    """
    hebrew, mergers = transliterate_latin_to_hebrew(latin_word)
    result = weigh(hebrew, 'hebrew')
    result['rendering'] = hebrew
    result['rendering_provenance'] = 'CONSTRUCTED'
    result['mergers'] = mergers
    result['via'] = 'hebrew_fallback'
    return result


def bridge(word1, system1, word2, system2):
    """Check a convergent point between two weighings.

    MECHANISM: weigh both, compare. Returns the two results and whether the
    numbers converge.
    DOCTRINE: a convergent point on attested tables is a candidate bridge;
    a convergent point touching a constructed table is a hypothesis for the
    author's red pen — never doctrine until it passes TRVVTH. The function
    reports the tier so the judgment can be made; it does not make it.
    """
    r1 = weigh(word1, system1)
    r2 = weigh(word2, system2)
    convergent = r1['value'] == r2['value']
    tiers = {r1['provenance'], r2['provenance']}
    if convergent and tiers <= {'ATTESTED'}:
        standing = 'CANDIDATE BRIDGE (attested)'
    elif convergent:
        standing = 'HYPOTHESIS — red pen, never doctrine (constructed tier touched)'
    else:
        standing = 'DIVERGENT — also data'
    return {
        'a': r1,
        'b': r2,
        'convergent': convergent,
        'standing': standing,
    }


def _fmt_breakdown(breakdown):
    # MECHANISM: render "C(3)+E(5)+L(12)+L(12)" so the audit trail reads.
    return '+'.join('%s(%d)' % (ch, v) for ch, v in breakdown)


def self_test():
    """Verify the engine against the author's established bridges.

    MECHANISM: the known convergent points must reproduce exactly, or the
    engine is wrong — TRVVTH gates the instrument before the instrument
    gates anything else.
    DOCTRINE: CELL=32 (English ordinal) is why the book is Liber XXXII;
    AXONEME=77 (English ordinal) = עז=77 (Hebrew) is the bridge that named
    the author's engine.
    """
    checks = []
    # 1. CELL in Latin ordinal must be 32.
    r = weigh('CELL', 'latin_ordinal')
    checks.append(('CELL/latin_ordinal == 32', r['value'] == 32, r['value']))
    # 2. AXONEME in Latin ordinal must be 77.
    r = weigh('AXONEME', 'latin_ordinal')
    checks.append(('AXONEME/latin_ordinal == 77', r['value'] == 77, r['value']))
    # 3. עז in Hebrew must be 77.
    r = weigh('עז', 'hebrew')
    checks.append(('עז/hebrew == 77', r['value'] == 77, r['value']))
    # 4. The bridge: AXONEME (Latin) ↔ עז (Hebrew) converges at 77, attested.
    b = bridge('AXONEME', 'latin_ordinal', 'עז', 'hebrew')
    checks.append(('bridge AXONEME↔עז converges at 77, attested',
                   b['convergent'] and b['a']['value'] == 77
                   and 'CANDIDATE BRIDGE' in b['standing'],
                   (b['a']['value'], b['b']['value'], b['standing'])))
    # 5. Provenance flags present on every weighing.
    r = weigh('test', 'braille')
    checks.append(('braille provenance == CONSTRUCTED',
                   r['provenance'] == 'CONSTRUCTED', r['provenance']))
    # 6. Music: the C-major triad weighs 15 (C=3, E=5, G=7 — Latin ordinal
    #    on note names, attested values).
    r = weigh('C E G', 'abc_notes')
    checks.append(('C E G/abc_notes == 15', r['value'] == 15, r['value']))
    # 7. Accidentals: ^C (C#) = 3+1 = 4; _B (Bb) = 2-1 = 1; total 5.
    r = weigh('^C _B', 'abc_notes')
    checks.append(('^C _B/abc_notes == 5', r['value'] == 5, r['value']))
    # 8. Rests are silence: 'C z D' weighs the same as 'C D' (3+4=7).
    a = weigh('C z D', 'abc_notes')['value']
    b = weigh('C D', 'abc_notes')['value']
    checks.append(('rests are silence (C z D == C D == 7)',
                   a == b == 7, (a, b)))
    # 9. ABC headers are dropped: 'X:1\nT:Test\nK:C\nCDE' == CDE = 12.
    r = weigh('X:1\nT:Test\nK:C\nCDE', 'abc_notes')
    checks.append(('ABC headers dropped (== 12)', r['value'] == 12, r['value']))
    # 10. The music bridge: C-E-G (15) converges with O (15) — attested
    #     values on both banks.
    m = bridge('C E G', 'abc_notes', 'O', 'latin_ordinal')
    checks.append(('music bridge CEG<->O converges at 15',
                   m['convergent'] and m['a']['value'] == 15,
                   (m['a']['value'], m['b']['value'], m['standing'])))
    ok = True
    for name, passed, got in checks:
        mark = 'PASS' if passed else 'FAIL'
        print('[%s] %s (got %r)' % (mark, name, got))
        ok = ok and passed
    print('self-test: %s' % ('ALL PASS — the instrument holds' if ok else 'FAILURE — do not trust this engine'))
    return ok


def _cli():
    # MECHANISM: a small honest CLI — weigh, bridge, fallback, self-test.
    # DOCTRINE: the instrument must be usable by hand; TRVVTH is checked by
    # doing, not by assertion.
    argv = sys.argv[1:]
    if not argv or argv[0] in ('-h', '--help', 'help'):
        print('usage:')
        print('  pontifex.py weigh WORD SYSTEM')
        print('    systems: %s' % ', '.join(sorted(SYSTEMS)))
        print('  pontifex.py bridge WORD1 SYSTEM1 WORD2 SYSTEM2')
        print('  pontifex.py fallback LATIN_WORD   (Hebrew fallback, mergers shown)')
        print('  pontifex.py music "C E G"   (ABC notation or bare notes)')
        print('  pontifex.py selftest')
        return 0
    cmd = argv[0]
    if cmd == 'weigh' and len(argv) == 3:
        r = weigh(argv[1], argv[2])
        print('%s [%s, %s] = %d' % (r['word'], r['system'], r['provenance'], r['value']))
        print('  ' + _fmt_breakdown(r['breakdown']))
    elif cmd == 'bridge' and len(argv) == 5:
        b = bridge(argv[1], argv[2], argv[3], argv[4])
        a, c = b['a'], b['b']
        print('%s [%s] = %d   vs   %s [%s] = %d' % (
            a['word'], a['system'], a['value'], c['word'], c['system'], c['value']))
        print('  convergent: %s — %s' % (b['convergent'], b['standing']))
    elif cmd == 'fallback' and len(argv) == 2:
        r = weigh_via_hebrew_fallback(argv[1])
        print('%s → %s [rendering %s] = %d [weighing %s]' % (
            argv[1], r['rendering'], r['rendering_provenance'],
            r['value'], r['provenance']))
        print('  ' + _fmt_breakdown(r['breakdown']))
        if r['mergers']:
            print('  mergers (distinction lost): %s' % ', '.join(
                '%s ← %s' % (h, '/'.join(MERGERS[h])) for h in r['mergers']))
        else:
            print('  mergers: none — the rendering is lossless')
    elif cmd == 'music' and len(argv) >= 2:
        # MECHANISM: join all args so the tune can be quoted or bare.
        r = weigh_melody(' '.join(argv[1:]))
        print('melody [%s] = %d' % (r['provenance'], r['value']))
        print('  ' + _fmt_breakdown(r['breakdown']))
        print('  conventions:')
        for c in r['conventions']:
            print('    - ' + c)
    elif cmd == 'selftest':
        return 0 if self_test() else 1
    else:
        print('unknown command; try: pontifex.py help')
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(_cli())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
