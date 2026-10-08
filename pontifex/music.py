#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — music.py — the music bridge (ABC-notation pitch weighing)
# v0.3.0 "The Third Span"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: ☉ in 14° 54′ Libra, ☽ in 14° 12′ Virgo, dies jovis,
# Anno V:xii e.n. (2026-10-08)
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
#   Hypothesis: that a melody weighed in its note-names converges with a word
#     weighed in its tongue — a bridge between music and language.
#   Method: note names in the English letter tradition ARE Latin letters, so
#     their values come from the attested Latin ordinal; ABC notation is
#     parsed to a pitch sequence under stated, constructed conventions.
#   Observation: weigh the melody; check the convergent point.
#   Result: convergent points are hypotheses for the red pen — the extraction
#     tier is constructed, so the instrument flags them honestly.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The music bridge.

DOCTRINE: a melody is a word spelled in notes. The note *values* are attested
(Latin ordinal on the letter names); the *extraction* (ABC → pitch sequence)
is constructed, and every choice is stated in MUSIC_CONVENTIONS.
"""

import re

# -- Note values: Latin ordinal on the English letter names (ATTESTED) -------
# MECHANISM: no new table is needed — CDEFGAB are Latin letters, and the
# working Latin table weighs them. DOCTRINE: this is what makes the music
# bridge cleaner than a constructed table: the values are discovered, the
# extraction alone is built.
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
    Returns the same result shape as engine.weigh(), so engine.bridge() works
    unchanged — the melody stands as one bank of the bridge, the word as the
    other.
    DOCTRINE: the result carries its conventions with it; a music bridge is
    only as honest as the extraction it stands on.
    """
    pitches = extract_pitches(text)
    total = 0
    breakdown = []
    for letter, acc in pitches:
        v = NOTE_VALUES[letter] + acc
        # MECHANISM: the label shows the accidental so the audit trail reads —
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


def music_checks():
    """Self-checks for the music bridge. Returns [(name, passed, got)]."""
    # MECHANISM: import here so music.py never depends on engine.py at import
    # time — the modules stay one-directional (engine → music).
    from .engine import weigh, bridge
    checks = []
    # 1. The C-major triad weighs 15 (C=3, E=5, G=7 — Latin ordinal).
    r = weigh('C E G', 'abc_notes')
    checks.append(('C E G/abc_notes == 15', r['value'] == 15, r['value']))
    # 2. Accidentals: ^C (C#) = 3+1 = 4; _B (Bb) = 2-1 = 1; total 5.
    r = weigh('^C _B', 'abc_notes')
    checks.append(('^C _B/abc_notes == 5', r['value'] == 5, r['value']))
    # 3. Rests are silence: 'C z D' weighs the same as 'C D' (3+4=7).
    a = weigh('C z D', 'abc_notes')['value']
    b = weigh('C D', 'abc_notes')['value']
    checks.append(('rests are silence (C z D == C D == 7)',
                   a == b == 7, (a, b)))
    # 4. ABC headers are dropped: 'X:1\nT:Test\nK:C\nCDE' == CDE = 12.
    r = weigh('X:1\nT:Test\nK:C\nCDE', 'abc_notes')
    checks.append(('ABC headers dropped (== 12)', r['value'] == 12, r['value']))
    # 5. The first music bridge: C-E-G (15) converges with O (15) — attested
    #    values on both banks, constructed extraction, so the standing is
    #    honestly HYPOTHESIS.
    m = bridge('C E G', 'abc_notes', 'O', 'latin_ordinal')
    checks.append(('music bridge CEG<->O converges at 15',
                   m['convergent'] and m['a']['value'] == 15,
                   (m['a']['value'], m['b']['value'], m['standing'])))
    return checks

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
