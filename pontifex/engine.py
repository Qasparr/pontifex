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
    KANA, KANA_VOWEL, KANA_BASE,
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
    # DOCTRINE: the GOJŪON MINT is the registry's one RATIFIED
    # construction — house coinage, founded 2026-11-12, stamped by
    # the founder 2026-11-13 ("Stamp the mint — the Tables stand").
    # Its tier stays CONSTRUCTED because that is what it is: the
    # ratification makes it the founder's doctrine, never the
    # tradition's antiquity. The full fence stands at the bank in
    # tables.py; it must not be cited as attested, traditional, or
    # ancient. The ー operator is read by kana() below, not by
    # weigh() — weigh() is the raw bank door, as in ptk.
    'kana':          {'table': KANA,
                      'provenance': 'CONSTRUCTED — the GOJŪON MINT: house '
                                    'coinage ratified by the founder\'s '
                                    'stamp 2026-11-13; NOT attested, '
                                    'traditional, or ancient'},
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


def kana(word):
    """Weigh a Japanese word in the GOJŪON MINT, reading the ー operator.

    MECHANISM: this is the mint's second door, ported from
    tools/ptk/weigh.py's kana()/kana_breakdown() — the same account in
    the engine's dress (a result dict, like weigh()). Sum the seated
    signs (hiragana and katakana share seats); the mark ー is read
    as an operator (G3): it adds the seat value of the vowel of the
    sign it follows (とー weighs ト 20 + お 5). A ー with no vowel
    before it (word-initial, or after ん/っ, which carry no vowel)
    adds 0. Characters the bank does not know are skipped — and reset
    the ー's memory, so length never reaches across a separator.
    The breakdown shows ー with the value it actually contributed,
    so the operator's work is auditable, never silent.

    DOCTRINE: weigh(word, 'kana') is the raw bank door and skips ー,
    exactly as ptk's raw weigh(word, KANA) does — ー is not a key of
    the bank. This function is the only door that reads it. The bank
    weighs the WRITTEN sign (G6); devoicing is not modelled. Totals
    stand raw (G7).
    """
    total = 0
    breakdown = []
    prev_vowel = None
    for ch in word:
        if ch == 'ー':
            v = prev_vowel if prev_vowel is not None else 0
            breakdown.append((ch, v))
            total += v
            continue
        if ch in KANA:
            v = KANA[ch]
            breakdown.append((ch, v))
            total += v
            prev_vowel = KANA_VOWEL.get(ch)
        else:
            # MECHANISM: an unknown character is silence, and it
            # resets the operator's memory (ptk's exact behavior).
            prev_vowel = None
    return {
        'word': word,
        'system': 'kana',
        'value': total,
        'provenance': SYSTEMS['kana']['provenance'],
        'breakdown': breakdown,
    }


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


def kana_checks():
    """Self-checks for the GOJŪON MINT seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against the doctrine's own printed
    numbers (THE-JAPANESE-TABLES-MAGVS.md, Part IV and the Phase III
    calibration), the way greek_checks() pins the Greek repair.
    Sign-for-sign parity against the mint's first engine seat
    (tools/ptk) is a relation between two codebases and lives in
    test_kana_parity.py at the repository root; this battery holds
    the seat to the doctrine itself. Kept beside engine_checks()
    rather than inside it, so the established checks stand untouched
    as the no-collateral witness; run both for the full suite.

    DOCTRINE — THE HEADS, PRINTED AS THE PROTOCOL PRINTS THEM (P4):
    the mint's あくま and むげつ stand BESIDE their rōmaji seam twins
    AKUMA 47 and MUGETSU 106, agreeing or not. The kana values are
    40 and 103; the deltas (−7, −3) are coordinates of the seam,
    exhibited — not failures, and never to be "repaired" by moving
    a seat. The bridges (P2) are entered one by one, exact only:
    かな 27 == KANA 27, しおん 65 == SHION 65, ゆず 93 == YUZU 93.
    """
    checks = []
    # 1. The axis itself (G1): あいうえお = 1+2+3+4+5 = 15.
    r = weigh('あいうえお', 'kana')
    checks.append(('あいうえお/kana == 15 (G1 axis)', r['value'] == 15, r['value']))
    # 2. The inventory: 73 seated signs, values 1–73 each exactly
    #    once, を holding its grid seat at 47, ん at 48 — ONE value
    #    (the elected dual refused).
    vals = sorted(KANA[s] for s in KANA_BASE)
    checks.append(('73 seats, values 1–73 each used exactly once',
                   len(KANA_BASE) == 73 and vals == list(range(1, 74)),
                   (len(KANA_BASE), vals[:3], vals[-3:])))
    checks.append(('を == 47 (grid seat kept), ん == 48 (one value)',
                   KANA['を'] == 47 and KANA['ん'] == 48 and KANA['ン'] == 48,
                   (KANA['を'], KANA['ん'], KANA['ン'])))
    # 3. The P4 heads at the raw bank door, beside their seam twins —
    #    the deltas printed as coordinates (P3), at full size.
    a = weigh('あくま', 'kana')['value']
    a_twin = weigh('AKUMA', 'latin_ordinal')['value']
    checks.append(('あくま == 40 beside AKUMA 47 (Δ −7, exhibited)',
                   a == 40 and a_twin == 47 and a - a_twin == -7,
                   (a, a_twin, a - a_twin)))
    m = weigh('むげつ', 'kana')['value']
    m_twin = weigh('MUGETSU', 'latin_ordinal')['value']
    checks.append(('むげつ == 103 beside MUGETSU 106 (Δ −3, exhibited)',
                   m == 103 and m_twin == 106 and m - m_twin == -3,
                   (m, m_twin, m - m_twin)))
    # 4. The three bridges, exact (P2): kana total == seam twin.
    for kw, twin, want in (('かな', 'KANA', 27), ('しおん', 'SHION', 65),
                           ('ゆず', 'YUZU', 93)):
        kv = weigh(kw, 'kana')['value']
        tv = weigh(twin, 'latin_ordinal')['value']
        checks.append(('%s == %d == %s (bridge)' % (kw, want, twin),
                       kv == tv == want, (kv, tv)))
    # 5. The dakuten continuation (G2): が at 49, on the mint's own
    #    axis after the base inventory entire.
    r = weigh('ありがとう', 'kana')
    checks.append(('ありがとう == 113, が == 49 (G2)',
                   r['value'] == 113 and KANA['が'] == 49,
                   (r['value'], KANA['が'])))
    # 6. Yōon at the full-size seat (G4) and sokuon at ツ's seat (G5).
    checks.append(('きゃ == 43 (G4: ゃ at や’s seat 36)',
                   weigh('きゃ', 'kana')['value'] == 43
                   and KANA['ゃ'] == KANA['や'] == 36,
                   (weigh('きゃ', 'kana')['value'], KANA['ゃ'])))
    checks.append(('ずっと == 94 (G5: っ at つ’s seat 18)',
                   weigh('ずっと', 'kana')['value'] == 94
                   and KANA['っ'] == KANA['つ'] == 18,
                   (weigh('ずっと', 'kana')['value'], KANA['っ'])))
    # 7. One sign, two dresses: every hiragana seat is its katakana
    #    twin's seat, sign for sign, across the whole bank. (The
    #    hiragana block runs ぁ U+3041 to ゖ U+3096 — ゕ・ゖ sit
    #    above ん, and a range ending at ん would skip them unseen.)
    hira = [(c, v) for c, v in KANA.items() if 'ぁ' <= c <= 'ゖ']
    mirror = all(KANA[chr(ord(c) + 0x60)] == v for c, v in hira)
    checks.append(('katakana mirrors hiragana, sign for sign (85 pairs)',
                   len(hira) == 85 and mirror
                   and weigh('かたかな', 'kana')['value']
                   == weigh('カタカナ', 'kana')['value'] == 49,
                   (len(hira), mirror, weigh('カタカナ', 'kana')['value'])))
    # 8. The ー seam, exhibited at both doors (G3): the raw bank door
    #    skips the operator (121, breakdown silent on it); the kana()
    #    door reads it (122 = 39 + 1 + 34 + 48, the ー lengthening a).
    raw = weigh('ラーメン', 'kana')
    op = kana('ラーメン')
    checks.append(('ラーメン: raw door 121 (ー skipped) / kana() door 122 (G3)',
                   raw['value'] == 121
                   and all(tok != 'ー' for tok, _ in raw['breakdown'])
                   and op['value'] == 122
                   and ('ー', 1) in op['breakdown'],
                   (raw['value'], op['value'], op['breakdown'])))
    # 9. The operator's edges: after ん (no vowel) and word-initial,
    #    ー weighs 0 — length with nothing to lengthen.
    checks.append(('んー == 48 and ー alone == 0 (operator edges)',
                   kana('んー')['value'] == 48 and kana('ー')['value'] == 0,
                   (kana('んー')['value'], kana('ー')['value'])))
    # 10. The fence rides with every weighing: the provenance names
    #     the coinage and refuses the antiquity claim on its face.
    p = SYSTEMS['kana']['provenance']
    checks.append(('kana provenance carries the fence (CONSTRUCTED, ratified '
                   '2026-11-13, NOT attested)',
                   p.startswith('CONSTRUCTED') and '2026-11-13' in p
                   and 'NOT attested' in p, p))
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
