#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — engine.py — the weighing engine and the bridge check
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
#   Hypothesis: that words in different tongues which weigh the same reveal
#     a bridge — a convergent point across languages.
#   Method: weigh each word in its own tongue's table (attested where the
#     tradition exists; derived by script-descent; constructed by canonical
#     ordinal where neither exists), every value carrying its provenance;
#     tongues with no table fall back to Hebrew transliteration (the
#     tradition's own move), with mergers documented; melodies are weighed
#     by the music bridge (pontifex/music.py).
#   Observation: run the weighing; record convergent and divergent points.
#   Result: convergent points on attested tables are candidate bridges;
#     convergent points touching constructed tables are hypotheses for the
#     red pen — never doctrine until they pass TRVVTH.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The weighing engine.

DOCTRINE: gematria's method is to weigh each word in its own tongue; its
purpose is the bridge — the match across tongues. The shared number is the
bridge, and a bridge needs two honest banks. (Settled with the author,
2026-10-07.)

DOCTRINE: a liber's number derives from its title's gematria (CELL=32 →
XXXII); rename or renumber must follow the name.

Provenance tiers (every value carries one):
  ATTESTED    — the tradition's own table; verifies against the tradition.
  DERIVED     — inherited by script-descent from a tabulated script.
  CONSTRUCTED — built by canonical ordinal where no path exists; a proposal,
                never a discovery. Convergent points touching this tier are
                hypotheses for the author's red pen, never doctrine.
"""

import unicodedata

from .tables import (
    HEBREW, GREEK, LATIN_ORDINAL, AGRIPPA, ARABIC_ABJAD, BRAILLE,
    LATIN_TO_HEBREW_DIGRAPHS, LATIN_TO_HEBREW, MERGERS,
)
from .music import weigh_melody

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
    # MECHANISM: report mergers honestly — the Hebrew letters in this output
    # that merged distinct Latin inputs.
    mergers = sorted(set(h for h in hebrew if h in MERGERS))
    return hebrew, mergers


def _normalize_greek(word):
    """Prepare a Greek word for the isopsephy table.

    MECHANISM: casefold, then NFD-decompose and drop every combining
    mark. Case carries no Milesian value (the tradition weighs letters,
    not their height), and neither do the breathings and accents —
    θέλημα and ΘΕΛΗΜΑ and θελημα are one word to the table. Before this
    normalization existed, weigh() looked the raw characters up and
    SILENTLY SKIPPED every accented letter and every capital: θέλημα
    weighed 88 (the έ never counted), πειρατής 696 (the ή gone), and
    ΘΕΛΗΜΑ weighed 0 with an empty breakdown. The defect was found by
    control weighings on 2026-11-16 and repaired the same night, at the
    founder's order; greek_checks() below pins the repair.

    DOCTRINE: what the eye reads as the letter is what gets weighed —
    the same rule transliterate_latin_to_hebrew() already applies to
    its own input. The table itself is NOT touched: it stands as the
    tradition hands it down, in bare lowercase letters; the preparation
    happens here, at the door, where a reader of the breakdown can see
    the normalized letters that were actually weighed. (A word-final
    capital Σ folds to σ in the breakdown; a lowercase ς the writer
    actually wrote is restored in final position — see below. σ and ς
    both carry 200 in the table, so no weight turns on the glyph.)
    """
    folded = word.casefold()
    out = ''.join(
        c for c in unicodedata.normalize('NFD', folded)
        if not unicodedata.combining(c)
    )
    # MECHANISM: casefold unifies all three sigma forms (Σ, σ, ς) to σ.
    # Where the input itself was written with a final ς, restore that
    # glyph in final position, so the breakdown shows the letter the
    # eye read on the page. Pure fidelity of the audit trail: σ and ς
    # carry the same 200, so the restoration moves no weight.
    bare = ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if not unicodedata.combining(c)
    )
    if bare.endswith('ς') and out.endswith('σ'):
        out = out[:-1] + 'ς'
    return out


def weigh(word, system):
    """Weigh a word in a system's table.

    MECHANISM: look up each character, sum the values. Unknown characters
    are skipped (silence, not false weight). Latin systems fold case.
    Greek input is normalized first (see _normalize_greek): casefolded
    and stripped of diacritics, because case and accents carry no
    Milesian value — the breakdown then shows the normalized letters
    that were actually weighed, while the result's 'word' field keeps
    the word exactly as it was given. Returns a dict: value, provenance,
    and the per-letter breakdown so any weighing can be audited by hand.

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
    # MECHANISM: Greek digraph 'στ' (stigma) is two codepoints with one
    # value — check the pair before the singles.
    # MECHANISM: each script is prepared at this one seam, so all three
    # doors (Python, CLI, HTTP) weigh the same letters: Latin folds to
    # capitals (its tables are keyed in capitals); Greek is casefolded
    # and stripped of diacritics (its table is keyed in bare lowercase,
    # and neither case nor accent carries Milesian value).
    if system in ('latin_ordinal', 'agrippa'):
        w = word.upper()
    elif system == 'greek':
        w = _normalize_greek(word)
    else:
        w = word
    i = 0
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


def to_jsonable(result):
    """Normalize an engine result for JSON output (scripts and the HTTP API).

    MECHANISM: breakdown tuples become {"token","value"} objects; every
    other field is already JSON-safe. The CLI --json flag and the server
    both go through here, so scripts see one shape.
    """
    out = dict(result)
    out['breakdown'] = [
        {'token': tok, 'value': val} for tok, val in result.get('breakdown', [])
    ]
    return out


def fmt_breakdown(breakdown):
    """Render "C(3)+E(5)+L(12)+L(12)" so the audit trail reads."""
    # MECHANISM: the human-readable twin of to_jsonable — same data, the
    # shape the eye audits by hand.
    return '+'.join('%s(%d)' % (tok, val) for tok, val in breakdown)


def engine_checks():
    """Self-checks for the weighing engine. Returns [(name, passed, got)]."""
    from .music import music_checks
    checks = []
    # 1. CELL in Latin ordinal must be 32 — why the book is Liber XXXII.
    r = weigh('CELL', 'latin_ordinal')
    checks.append(('CELL/latin_ordinal == 32', r['value'] == 32, r['value']))
    # 2. AXONEME in Latin ordinal must be 77.
    r = weigh('AXONEME', 'latin_ordinal')
    checks.append(('AXONEME/latin_ordinal == 77', r['value'] == 77, r['value']))
    # 3. עז in Hebrew must be 77 (70+7).
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
    # 6. Unknown systems fail loudly.
    try:
        weigh('x', 'nope')
        checks.append(('unknown system raises', False, 'no error'))
    except ValueError:
        checks.append(('unknown system raises', True, 'ValueError'))
    checks.extend(music_checks())
    return checks


def greek_checks():
    """Self-checks for the Greek normalization. Returns [(name, passed, got)].

    MECHANISM: these pin the repair of 2026-11-16 — before it, weigh()
    silently dropped accented Greek letters (θέλημα read 88, πειρατής
    696, πλοῖον 300) and read uppercase Greek as zero (ΘΕΛΗΜΑ, empty
    breakdown). The battery holds the three doors of the defect shut:
    accents, capitals, and the final sigma. Kept beside engine_checks()
    rather than inside it, so the established eleven checks stand
    untouched as the no-collateral witness; run both for the full suite.
    """
    checks = []
    # 1. The control word, accented as a man actually writes it: θέλημα
    #    must weigh 93 — the έ counts.
    r = weigh('θέλημα', 'greek')
    checks.append(('θέλημα/greek == 93 (accented)', r['value'] == 93, r['value']))
    # 2. The same word in capitals must not vanish: ΘΕΛΗΜΑ == 93, with a
    #    full breakdown (before the repair: 0, empty).
    r = weigh('ΘΕΛΗΜΑ', 'greek')
    checks.append(('ΘΕΛΗΜΑ/greek == 93 (uppercase)',
                   r['value'] == 93 and len(r['breakdown']) == 6,
                   (r['value'], len(r['breakdown']))))
    # 3. All three writings of the word agree — accented, capital, bare.
    vals = {weigh(w, 'greek')['value'] for w in ('θέλημα', 'ΘΕΛΗΜΑ', 'θελημα')}
    checks.append(('θέλημα in three writings agrees at 93',
                   vals == {93}, sorted(vals)))
    # 4. Breathing and accent together: ἀλήθεια == 64.
    r = weigh('ἀλήθεια', 'greek')
    checks.append(('ἀλήθεια/greek == 64', r['value'] == 64, r['value']))
    # 5. Capitals again, on the truth: ΑΛΗΘΕΙΑ == 64.
    r = weigh('ΑΛΗΘΕΙΑ', 'greek')
    checks.append(('ΑΛΗΘΕΙΑ/greek == 64', r['value'] == 64, r['value']))
    # 6. The perispomeni is a mark, not a letter: πλοῖον == 310 (before
    #    the repair the ῖ was skipped and the vessel read 300).
    r = weigh('πλοῖον', 'greek')
    checks.append(('πλοῖον/greek == 310', r['value'] == 310, r['value']))
    # 7. ΠΛΟΙΟΝ in capitals == 310.
    r = weigh('ΠΛΟΙΟΝ', 'greek')
    checks.append(('ΠΛΟΙΟΝ/greek == 310', r['value'] == 310, r['value']))
    # 8. σκαμνόν, accented on the omicron, == 431.
    r = weigh('σκαμνόν', 'greek')
    checks.append(('σκαμνόν/greek == 431', r['value'] == 431, r['value']))
    # 9. πειρατής == 704, and the breakdown closes on the final sigma —
    #    a lowercase ς in the input stays ς and carries its 200.
    r = weigh('πειρατής', 'greek')
    checks.append(('πειρατής/greek == 704, final sigma in breakdown',
                   r['value'] == 704 and r['breakdown'][-1] == ('ς', 200),
                   (r['value'], r['breakdown'][-1])))
    # 10. Final-sigma agreement across case: λόγος (accented, ends ς)
    #     and ΛΟΓΟΣ (capitals; the final Σ folds to σ) weigh the same —
    #     σ and ς are one weight in the table.
    a = weigh('λόγος', 'greek')['value']
    b = weigh('ΛΟΓΟΣ', 'greek')['value']
    checks.append(('λόγος == ΛΟΓΟΣ == 373 (final sigma across case)',
                   a == b == 373, (a, b)))
    # 11. The stigma digraph survives normalization, in either case:
    #     στ and ΣΤ both read as the pair, value 6.
    a = weigh('στ', 'greek')['value']
    b = weigh('ΣΤ', 'greek')['value']
    checks.append(('stigma digraph στ == ΣΤ == 6', a == b == 6, (a, b)))
    # 12. The breakdown shows the letters actually weighed — normalized:
    #     ΘΕΛΗΜΑ's audit trail spells θελημα.
    toks = ''.join(tok for tok, _ in weigh('ΘΕΛΗΜΑ', 'greek')['breakdown'])
    checks.append(('breakdown shows normalized letters (ΘΕΛΗΜΑ → θελημα)',
                   toks == 'θελημα', toks))
    return checks


def self_test():
    """Verify the engine against the author's established bridges.

    MECHANISM: the known convergent points must reproduce exactly, or the
    engine is wrong — TRVVTH gates the instrument before the instrument
    gates anything else.
    """
    ok = True
    for name, passed, got in engine_checks():
        mark = 'PASS' if passed else 'FAIL'
        print('[%s] %s (got %r)' % (mark, name, got))
        ok = ok and passed
    print('self-test: %s' % ('ALL PASS — the instrument holds' if ok else 'FAILURE — do not trust this engine'))
    return ok

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
