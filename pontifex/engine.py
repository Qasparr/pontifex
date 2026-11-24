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
    HALEHAME, HALEHAME_FIRST, GEEZ, GEEZ_FIRST, GEEZ_BASE,
    ARMENIAN, ARMENIAN_LATE,
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
    # DOCTRINE: the HALEHAME WITNESS is a sourced folk table, not
    # a house coinage — the Debtera enumeration as published,
    # audited 2026-11-24. Its fence carries its three caveats
    # (multiplier printed but unexhibited in use; antiquity
    # undated; register folk-magical, not liturgical) into every
    # weighing. It stands as WITNESS beside the Ge'ez mint by
    # the founder's end-goal ruling of 2026-11-24 — calibration,
    # not the bank. weigh() reads its printed grid as written;
    # halehame() below reads its practiced first-form law.
    'halehame':      {'table': HALEHAME,
                      'provenance': 'FOLK TABLE — WITNESS: the Debtera '
                                    '(halehame) enumeration as published '
                                    '(geez.org, read 2026-11-24), audited '
                                    '2026-11-24 — first-form values '
                                    'sourced 26/26; the multiplier grid '
                                    'as printed, its use UNEXHIBITED; '
                                    'antiquity UNDATED; register '
                                    'folk-magical, not liturgical. '
                                    'Stands as witness beside the '
                                    'Ge\'ez mint (the founder\'s '
                                    'end-goal ruling, 2026-11-24); '
                                    'NOT the house\'s coinage'},
    # DOCTRINE: the GE'EZ MINT is the registry's second house
    # coinage — minted at the desk 2026-11-24 under the
    # founder's hybrid law and his three standing rules (the
    # road rule, the proof-enough rule, the end-goal rule);
    # its fork decisions are desk rulings under the end-goal
    # rule, revisable by his pen. NO stamp is claimed beyond
    # that proof. Its axis is the folk multiplier corrected at
    # order 6 to the Zero (M3) — so a Ge'ez total is ambiguous
    # unless it declares its bank (seam rule S1). weigh()
    # reads signs as written; geez() below reads the mint's
    # first-form (calibration) door. The full fence stands at
    # the banks in tables.py.
    'geez':          {'table': GEEZ,
                      'provenance': 'CONSTRUCTED — the GE\'EZ MINT: '
                                    'house coinage minted at the desk '
                                    '2026-11-24 under the founder\'s '
                                    'hybrid law and end-goal rule, '
                                    'calibrated by construction to the '
                                    'halehame witness (first-form '
                                    'column identical, 26/26); NOT '
                                    'attested, traditional, or ancient'},
    # DOCTRINE: the ARMENIAN bank is a sourced table at the full
    # depth — the designed alphabet's own numeral system, complete
    # at 36 of 36 classical letters, in liturgical manuscript use
    # for era dating; audited 2026-11-24, three witnesses agreeing
    # on every cell. Its fence states the difference from the
    # halehame witness plainly, because the founder ordered the
    # two read as a control case: halehame is a folk enumeration
    # (26 first forms of 202 signs, undated, multiplier
    # unexhibited); this is a complete liturgical table. The
    # medieval additions (Օ, Ֆ) are NOT seated in this bank: by
    # the founder's ruling of 2026-11-24 (the Armenian questions
    # decided in order of synergy, not argument) they stand in
    # the ARMENIAN_LATE annex at their "sometimes" values, a tier
    # below the classical 36, weighing only at the armenian()
    # door's explicit late path. The bank is keyed in majuscules;
    # weigh() folds Armenian input to capitals at its seam.
    # armenian() below is the manuscript-dress door: it prices
    # the overline at x10,000 per mark — the factor the table's
    # own uniqueness law selects (resolution R2).
    'armenian':      {'table': ARMENIAN,
                      'provenance': 'ATTESTED — the classical Armenian '
                                    'numeral table: the designed '
                                    'alphabet\'s own system (Mashtots, '
                                    'c. 405 CE), all 36 classical '
                                    'letters valued in four decimal '
                                    'classes to 9000, audited '
                                    '2026-11-24 (three witnesses agree '
                                    'on all 36 cells; MELA\'s colophon '
                                    'examples concur). A complete '
                                    'liturgical table — NOT the '
                                    'halehame witness\'s case: that '
                                    'bank is a folk enumeration valuing '
                                    '26 first forms of 202 signs, '
                                    'antiquity undated, its multiplier '
                                    'unexhibited. The medieval '
                                    'additions (Օ, Ֆ) are NOT seated '
                                    'in this bank: by the founder\'s '
                                    'ruling of 2026-11-24 (the Armenian '
                                    'questions decided in order of '
                                    'synergy, not argument) they stand '
                                    'in the ARMENIAN_LATE annex at '
                                    'their "sometimes" values '
                                    '(10000 / 20000), a tier below the '
                                    'classical 36, weighing only at '
                                    'the armenian() door\'s explicit '
                                    'late path. The overline '
                                    'multiplies by 10,000 — the factor '
                                    'the table\'s own uniqueness law '
                                    'selects; Omniglot\'s x1,000 '
                                    'stands recorded as the parted '
                                    'source'},
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
    # capitals (its tables are keyed in capitals); Armenian folds the
    # same way (its table is keyed in the majuscules the system was
    # created in, and case carries no numeral value — the alphabet's
    # own table pairs the cases at one value); Greek is casefolded
    # and stripped of diacritics (its table is keyed in bare lowercase,
    # and neither case nor accent carries Milesian value).
    if system in ('latin_ordinal', 'agrippa', 'armenian'):
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


def geez(word):
    """Weigh a Ge'ez word in the GE'EZ MINT's first-form reading.

    MECHANISM: the mint's calibration door. Every seated sign is
    read at its BASE's first-form value — the sign's order is set
    aside and the base speaks (ክ weighs what ከ weighs, 50).
    Signs the mint does not seat (the post-classical inventory,
    the Ethiopic numerals, anything foreign) are skipped —
    silence, not false weight. The breakdown shows each written
    sign with the value it actually contributed, so the reading
    is auditable sign by sign.

    DOCTRINE: weigh(word, 'geez') is the mint's protocol door —
    signs as written, each at its order's seat under the axis
    law (seam rule S1's mint side). This door exists for one
    purpose: CALIBRATION (M2). The mint's first-form column IS
    halehame, so this reading of any word over the 182 grid
    signs returns exactly the witness's practiced total —
    ክርስቶስ = 80 here, as in halehame() below — by identity of
    construction, not by approximation, and the seam records
    that agreement as calibration, never as a bridge (the two
    banks are calibrated, not independent, at this door). Over
    the signs only the mint seats — the labiovelars, the ΕΙ
    column — this door reads each at its base's value where
    the witness is silent: the coverage coordinate, printed in
    the seam, not hidden by the door.
    """
    total = 0
    breakdown = []
    for ch in word:
        if ch in GEEZ_FIRST:
            v = GEEZ_FIRST[ch]
            breakdown.append((ch, v))
            total += v
        # else: silence, not false weight (see above).
    return {
        'word': word,
        'system': 'geez',
        'value': total,
        'provenance': SYSTEMS['geez']['provenance'],
        'breakdown': breakdown,
    }


def halehame(word):
    """Weigh a Ge'ez word in the HALEHAME WITNESS's practiced reading.

    MECHANISM: the witness's reading door — the first-form law
    the debtera actually practice. Every grid sign is read at
    its base's first-form value (the source's own statement:
    example usage "invariably uses the letters of a word in the
    first form only"). Signs the folk table does not reach —
    the labiovelar series, the eighth-slot glyphs, the
    later-added bases — are skipped: the folk table assigns
    them no value, and the door reports silence where the
    table is silent (the audit's GAP rows, at the door). The
    breakdown shows each written sign with the value it
    contributed.

    DOCTRINE: weigh(word, 'halehame') is the witness's raw
    door — the PRINTED grid, a form at order n at n × its base,
    ×6 standing at order 6 unaltered (seam rule S4: the mint
    corrects its own axis, never the witness's). The printed
    grid's use is unexhibited in every worked example the
    sources carry; THIS door is the practiced law, and the
    seam's protocol (S1) requires every witness total to name
    its door, because the two doors part — ክርስቶስ reads 80
    here and 490 at the raw door, and both numbers are the
    witness's own, at different doors, with the caveat riding
    on the printed one.
    """
    total = 0
    breakdown = []
    for ch in word:
        if ch in HALEHAME_FIRST:
            v = HALEHAME_FIRST[ch]
            breakdown.append((ch, v))
            total += v
        # else: silence — the folk table's gap, reported as such.
    return {
        'word': word,
        'system': 'halehame',
        'value': total,
        'provenance': SYSTEMS['halehame']['provenance'],
        'breakdown': breakdown,
    }


def armenian(word, late=False):
    """Weigh an Armenian word in the classical table, manuscript dress.

    MECHANISM: the bank's reading door for text as manuscripts and
    colophons write it. The combining overline (U+0305) FOLLOWS the
    letter it multiplies, so the door walks the word letter by
    letter, groups each letter with the marks riding on it, and
    prices that letter at its face value x 10,000 per mark.
    Letters are folded per letter to the majuscules the bank is
    keyed in — the seam's preparation, done here because the marks
    must be read before any fold could scatter them. The result
    carries weigh()'s shape (word as given, system, value,
    provenance, breakdown) plus the dress made auditable:
    'overline_marks' (every mark seen, including any orphan mark
    that prices nothing), 'overline_factor' (10000), and
    'late_annex' (whether the annex path stood open). The
    breakdown shows each letter's PRICED contribution, so its
    entries sum to the value — the audit trail shows the
    multiplication, never hides it. On unmarked classical text
    this door and weigh(word, 'armenian') agree exactly.

    DOCTRINE — THE OVERLINE, RESOLVED (R2): the overline is a
    MULTIPLIER in the sources, and the sources parted on its
    factor — x10,000 (Wikipedia, "Armenian numerals"; MELA: an
    overlined Ա is 10,000, an overlined Ջ is 9,000,000) against
    x1,000 (Omniglot: an overlined Ժ is 10,000, an overlined Ռ is
    1,000,000). As first seated, this door counted marks and
    applied NO factor, the choice standing open for the founder's
    pen (Phase I audit §VII Q2). His ruling of 2026-11-24 decided
    the Armenian questions "in order of Synergy not argument as
    previously ruled", and synergy reads the table's own law: the
    classical bank holds UNIQUENESS — 36 letters, 36 distinct
    values. Priced at x1,000, the overlined units (Ա–Թ ->
    1000–9000) collide with the plain thousands class — nine
    collisions, the mark adding nothing there. Priced at
    x10,000, every overlined value at every class lands in an
    empty seat — zero collisions across all 36 — and the factor
    also carries the two stronger witnesses. So this door
    multiplies by 10,000 per mark. Omniglot's x1,000 stands
    recorded here as the parted source — marked, not vanished.
    armenian_checks() proves the collision sweep in code.

    DOCTRINE — THE LATE ANNEX, RESOLVED (R1, same ruling): the
    medieval additions Օ/Ֆ carry "sometimes" values (10000 /
    20000) a tier below the classical 36. They are seated in
    tables.ARMENIAN_LATE and weigh ONLY when the caller opens the
    annex path (late=True): the classical bank is never blended,
    and օ — a living letter of ordinary words (օր, "day") —
    still weighs nothing on the default path, so the annex can
    never fire by accident. weigh(word, 'armenian') is the raw
    bank door: it never sees the annex or the factor at all.
    There is no second reading to declare: the system is additive
    as written, one letter one value, and the door exists for the
    mark and the annex, not for a rival law.
    """
    marks_total = word.count('\u0305')  # every combining overline
    # MECHANISM: first pass — group each letter with the marks
    # that ride on it. A mark with no letter before it is counted
    # in overline_marks (above) and prices nothing.
    letters = []
    for ch in word:
        if ch == '\u0305':
            if letters:
                letters[-1][1] += 1
            continue
        letters.append([ch, 0])
    total = 0
    breakdown = []
    for ch, marks in letters:
        folded = ch.upper()
        if folded in ARMENIAN:
            base = ARMENIAN[folded]
        elif late and (ch in ARMENIAN_LATE
                       or folded in ARMENIAN_LATE):
            # MECHANISM: the annex is keyed in both cases; the raw
            # letter is tried first, the fold second — same seat.
            base = ARMENIAN_LATE.get(ch, ARMENIAN_LATE.get(folded))
        else:
            continue  # silence, not false weight
        priced = base * (10000 ** marks) if marks else base
        breakdown.append((folded, priced))
        total += priced
    return {
        'word': word,
        'system': 'armenian',
        'value': total,
        'provenance': SYSTEMS['armenian']['provenance'],
        'breakdown': breakdown,
        'overline_marks': marks_total,
        'overline_factor': 10000,
        'late_annex': bool(late),
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


# MECHANISM: the folk first-form values, transcribed from geez.org's
# published Debtera table (read 2026-11-24) — the doctrine's own
# printed numbers for the Ge'ez seats, held here so both Ge'ez
# batteries pin the banks to the source, not to each other. The
# Phase I audit battery holds an independent transcription of the
# same table; test_geez_parity.py runs it as a control.
_GEEZ_FOLK_FIRST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    20, 30, 40, 50, 60, 70, 80, 90, 100,
                    200, 300, 400, 500, 600, 700, 800]


def geez_checks():
    """Self-checks for the GE'EZ MINT seat. Returns [(name, passed, got)].

    MECHANISM: these pin the mint against its own instrument of
    record (THE-GEEZ-TABLES-PHASE-II-III: the axis law M1, the
    calibration M2, the order-6 declaration M3, the columns M4/M5)
    and against the witness it was calibrated to. Sign-for-sign
    parity against the Phase I audit's independent data seat
    (the inventory and values CSVs) is a relation between two
    seats and lives in test_geez_parity.py at the repository
    root; this battery holds the seat to the doctrine itself.
    Kept beside kana_checks() rather than inside engine_checks(),
    so the established checks stand untouched as the
    no-collateral witness; run all for the full suite.

    DOCTRINE — THE HEADS, PRINTED AS THE SEAM PRINTS THEM (S3):
    the mint's ክርስቶስ stands at the head of its calibration
    beside the witness's 80 — agreeing at the first-form doors
    BY CONSTRUCTION (calibration, not a bridge) and parting at
    the protocol doors by exactly the order-6 correction:
    70 as written, Δ −10, the delta being three order-6 signs
    the folk practice reduces to their bases and the mint
    reads at the Zero. The delta is a coordinate, exhibited —
    not a failure, and never to be "repaired" by moving a seat.
    """
    checks = []
    # 1. The axis itself (M1) on the first base's row: ሀ (first
    #    form 1) prices its orders at the order numbers, with
    #    the single correction standing in the row: 1,2,3,4,5,0,7.
    row = [GEEZ[chr(ord('ሀ') + o)] for o in range(7)]
    checks.append(('ሀ row prices the axis (M1): 1,2,3,4,5,0,7 — '
                   'the correction inside the row',
                   row == [1, 2, 3, 4, 5, 0, 7], row))
    # 2. The surface: 227 seats in seating order — the classical
    #    202 first (182 grid + 20 labiovelar), then the 25 of
    #    the ΕΙ column; every seated sign a key, no duplicates.
    strata = (len(GEEZ_BASE[:182]), len(GEEZ_BASE[182:202]),
              len(GEEZ_BASE[202:]))
    checks.append(('227 seats: 182 grid + 20 labiovelar (the classical '
                   '202) + 25 of the ΕΙ column, each exactly once',
                   strata == (182, 20, 25) and len(GEEZ) == 227
                   and len(set(GEEZ_BASE)) == 227
                   and all(s in GEEZ for s in GEEZ_BASE),
                   (strata, len(GEEZ))))
    # 3. Calibration by construction (M2): the mint's first-form
    #    column IS the folk table — all 26 first forms identical
    #    to the transcribed source values, in both banks.
    firsts = [GEEZ_BASE[i * 7] for i in range(26)]
    checks.append(('first-form column == the folk table, 26/26 (M2)',
                   [GEEZ[g] for g in firsts] == _GEEZ_FOLK_FIRST
                   and [HALEHAME[g] for g in firsts] == _GEEZ_FOLK_FIRST
                   and [GEEZ_FIRST[g] for g in firsts] == _GEEZ_FOLK_FIRST,
                   [GEEZ[g] for g in firsts]))
    # 4. The head, at all four doors (S1/S3): ክርስቶስ — the
    #    tradition's own worked example. Practiced readings 80
    #    and 80 (identity); protocol doors part: mint as written
    #    70 (Δ −10, the order-6 correction at work), the
    #    witness's printed grid 490 (the caveat's number).
    mw = weigh('ክርስቶስ', 'geez')['value']
    mf = geez('ክርስቶስ')['value']
    wf = halehame('ክርስቶስ')['value']
    wp = weigh('ክርስቶስ', 'halehame')['value']
    checks.append(('ክርስቶስ: mint-written 70 / mint first-form 80 / '
                   'witness practiced 80 / witness printed 490',
                   (mw, mf, wf, wp) == (70, 80, 80, 490),
                   (mw, mf, wf, wp)))
    # 5. The corroborated multiplier exhibits (Bekerie via
    #    Daniels) hold in the mint as written — the mint's axis
    #    IS the folk axis at every exhibited coordinate but one:
    #    hu = 2, lu = 4, to = 70, po = 5600.
    ex = (weigh('ሁ', 'geez')['value'], weigh('ሉ', 'geez')['value'],
          weigh('ቶ', 'geez')['value'], weigh('ፖ', 'geez')['value'])
    checks.append(('multiplier exhibits hold as written: ሁ 2, ሉ 4, '
                   'ቶ 70, ፖ 5600 (Bekerie)',
                   ex == (2, 4, 70, 5600), ex))
    # 6. The order-6 declaration (M3), proven in code: the mint
    #    reads the Zero law — ል = 0, ፕ = 0, and exactly 30 signs
    #    weigh 0 (26 grid + 4 labiovelar) — while the witness's
    #    printed grid reads ×6 unaltered at the same signs.
    zeros = sum(1 for v in GEEZ.values() if v == 0)
    checks.append(('order 6 (M3): mint ል/ፕ == 0 with exactly 30 zero '
                   'signs; witness printed ል 12, ፕ 4800 (×6 stands)',
                   GEEZ['ል'] == 0 and GEEZ['ፕ'] == 0 and zeros == 30
                   and HALEHAME['ል'] == 12 and HALEHAME['ፕ'] == 4800,
                   (GEEZ['ል'], GEEZ['ፕ'], zeros,
                    HALEHAME['ል'], HALEHAME['ፕ'])))
    # 7. The labiovelar column (M4): seated in the mint at the
    #    axis's prices, the Zero reaching into the column (ቍ);
    #    the witness seats none of the twenty — its GAP at the
    #    door, not a silent zero of ours.
    lab = GEEZ_BASE[182:202]
    checks.append(('labiovelars (M4): ቈ == 8, ቍ == 0 in the mint; '
                   'none of the 20 in the witness',
                   GEEZ['ቈ'] == 8 and GEEZ['ቍ'] == 0
                   and all(s not in HALEHAME for s in lab),
                   (GEEZ['ቈ'], GEEZ['ቍ'],
                    sum(1 for s in lab if s in HALEHAME))))
    # 8. The ΕΙ column (M5): the eighth slot priced at ×8 —
    #    ሇ == 8, ኧ == 320 — and ዐ's cell a HOLE: the glyph the
    #    standard does not encode is a key of neither bank.
    hole = chr(ord('ዐ') + 7)
    checks.append(('the ΕΙ column (M5): ሇ == 8, ኧ == 320 at ×8; '
                   'ዐ’s slot a hole in both banks',
                   GEEZ['ሇ'] == 8 and GEEZ['አ'] * 8 == GEEZ['ኧ'] == 320
                   and hole not in GEEZ and hole not in HALEHAME,
                   (GEEZ['ሇ'], GEEZ['ኧ'], hole in GEEZ)))
    # 9. The honesty coordinate, printed not smoothed: the mint
    #    is NOT a unique-value bank. Its axis is a calibrated
    #    class axis, and its 227 seats return 90 distinct
    #    values — collisions inherited from the folk class
    #    structure (ሁ weighs 2, which is also ለ's first form).
    #    What the law claims is singleness — one value per
    #    sign, no duals — never uniqueness.
    checks.append(('90 distinct values over 227 seats (collisions '
                   'printed; singleness claimed, uniqueness not)',
                   len(set(GEEZ.values())) == 90
                   and GEEZ['ሁ'] == GEEZ['ለ'] == 2,
                   (len(set(GEEZ.values())), GEEZ['ሁ'])))
    # 10. The desk exhibit word, all four doors (ሰላም, "peace" —
    #     weighed first in the Phase II–III instrument, at
    #     [CONSTRUCTED] exhibit tier): the readings part exactly
    #     at ም, the word's one order-6 sign.
    sw = (weigh('ሰላም', 'geez')['value'], geez('ሰላም')['value'],
          halehame('ሰላም')['value'], weigh('ሰላም', 'halehame')['value'])
    checks.append(('ሰላም at four doors: 15 / 13 / 13 / 39 (the '
                   'parting at ም, its order-6 sign)',
                   sw == (15, 13, 13, 39), sw))
    # 11. The fence rides with every weighing.
    p = SYSTEMS['geez']['provenance']
    checks.append(('geez provenance carries the fence (CONSTRUCTED, '
                   'minted 2026-11-24, NOT attested)',
                   p.startswith('CONSTRUCTED') and '2026-11-24' in p
                   and 'NOT attested' in p, p))
    return checks


def halehame_checks():
    """Self-checks for the HALEHAME WITNESS seat. [(name, passed, got)].

    MECHANISM: these pin the witness to its sources — the
    transcribed folk table, Bekerie's corroborated exhibits,
    the tradition's own worked example — and to its fences:
    the coverage boundary (the 182 grid signs, no more), the
    unaltered ×6 (S4), and the practiced door's law. Parity
    against the Phase I audit's data seat lives in
    test_geez_parity.py; the audit's own battery is run there
    as a control. Kept beside geez_checks(); the witness is
    audited, never corrected, by the mint's arrival.
    """
    checks = []
    # 1. Coverage, exactly the folk table's reach: the 182 grid
    #    signs — and NOT the labiovelars, NOT the eighth slot,
    #    NOT the post-classical series. The gaps are the folk
    #    table's own boundaries, printed in the audit's GAP
    #    rows; a witness key beyond the 182 would be a forgery
    #    of coverage.
    lab = GEEZ_BASE[182:202]
    eighth = GEEZ_BASE[202:]
    checks.append(('coverage: exactly the 182 grid signs; no '
                   'labiovelar, no eighth-slot key',
                   len(HALEHAME) == 182
                   and all(s not in HALEHAME for s in lab)
                   and all(s not in HALEHAME for s in eighth),
                   (len(HALEHAME),
                    sum(1 for s in lab + eighth if s in HALEHAME))))
    # 2. The first-form values are the transcribed table's,
    #    sign for sign, class law and all.
    firsts = [GEEZ_BASE[i * 7] for i in range(26)]
    checks.append(('first-form values == the published table, 26/26',
                   [HALEHAME[g] for g in firsts] == _GEEZ_FOLK_FIRST,
                   [HALEHAME[g] for g in firsts]))
    # 3. The printed grid entire at its corroborated exhibits:
    #    Bekerie's multipliers (hu = 2, lu = 4, po = 5600) and
    #    the audit battery's spot checks (ተ at order 7 = 70;
    #    ኀ at order 5 = 100 — ኄ, the grid form).
    ex = (weigh('ሁ', 'halehame')['value'], weigh('ሉ', 'halehame')['value'],
          weigh('ቶ', 'halehame')['value'], weigh('ኄ', 'halehame')['value'],
          weigh('ፖ', 'halehame')['value'])
    checks.append(('printed grid at its exhibits: ሁ 2, ሉ 4, ቶ 70, '
                   'ኄ 100, ፖ 5600',
                   ex == (2, 4, 70, 100, 5600), ex))
    # 4. The tradition's worked example at the practiced door:
    #    ክርስቶስ = 80, exact — the calibration the audit ran
    #    before trusting any derived number, run here at the
    #    engine's door.
    r = halehame('ክርስቶስ')
    checks.append(('ክርስቶስ == 80 at the practiced door (the '
                   'tradition’s own example)',
                   r['value'] == 80
                   and r['breakdown'] == [('ክ', 50), ('ር', 6), ('ስ', 7),
                                          ('ቶ', 10), ('ስ', 7)],
                   (r['value'], r['breakdown'])))
    # 5. The ×6 stands (S4): the mint's correction is the
    #    mint's; the witness's printed order-6 column is the
    #    folk law's, unaltered — ፕ at 4800, the folk maximum's
    #    heaviest printed form.
    checks.append(('the folk ×6 stands unaltered: ፕ == 4800 printed',
                   weigh('ፕ', 'halehame')['value'] == 4800
                   and HALEHAME_FIRST['ፕ'] == 800,
                   (HALEHAME['ፕ'], HALEHAME_FIRST['ፕ'])))
    # 6. The practiced door's silence at the gaps: a labiovelar
    #    weighs NOTHING at this door — skipped, not zeroed by
    #    us — while the same glyph speaks in the mint. The
    #    asymmetry is the coverage coordinate, at the doors.
    checks.append(('practiced door silent on labiovelars (ቈ skipped); '
                   'the mint reads it 8',
                   halehame('ቈ')['value'] == 0
                   and halehame('ቈ')['breakdown'] == []
                   and weigh('ቈ', 'geez')['value'] == 8,
                   (halehame('ቈ')['value'], weigh('ቈ', 'geez')['value'])))
    # 7. The fence: folk table, witness standing, caveats named.
    p = SYSTEMS['halehame']['provenance']
    checks.append(('halehame provenance carries the fence (FOLK '
                   'TABLE — WITNESS, UNDATED, UNEXHIBITED multiplier)',
                   p.startswith('FOLK TABLE') and 'WITNESS' in p
                   and 'UNDATED' in p and 'UNEXHIBITED' in p, p))
    return checks


# MECHANISM: the classical letters in Mashtots' order — the audit's
# coordinate for the seat. The class law is recomputed from position
# in armenian_checks() below, never trusted from the dict's shape.
_ARMENIAN_ORDER = 'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔ'


def armenian_checks():
    """Self-checks for the ARMENIAN seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-ARMENIAN-TABLE-PHASE-I-AUDIT.md): the class law recomputed
    from position, the witnesses' worked examples, MELA's era date,
    the boundary at the medieval additions, and — since the
    founder's resolutions of 2026-11-24 (the audit's RESOLUTIONS
    section) — the late annex's exact values and opt-in silence,
    the overline priced at x10,000, and the collision sweep that
    is the factor's synergy proof. Sign-for-sign parity against
    the audit's frozen transcription
    (research/twelve-tongues/armenian-table.csv) is a relation
    between two seats and lives in test_armenian_parity.py at the
    repository root; this battery holds the seat to the doctrine
    itself. Kept beside halehame_checks() rather than inside
    engine_checks(), so the established checks stand untouched as
    the no-collateral witness; run all for the full suite.

    DOCTRINE — THE CONTROL CASE, AT THE SEAT: this bank and the
    halehame witness carry the same value sequence over their
    shared domain (positions 1–26 identical), reached by laws that
    part at position 10 and held at opposite attestation depths.
    The checks below pin THIS bank's side: complete, unique-valued,
    liturgical. The comparison itself is the audit's page and the
    parity battery's exhibit, not a weighing either bank performs.
    """
    checks = []
    # 1. The class law entire, recomputed from position: four
    #    classes of nine, value = digit x 10^class, at all 36 seats.
    def cls(pos):
        return (((pos - 1) % 9) + 1) * (10 ** ((pos - 1) // 9))
    law = [ARMENIAN[ch] for ch in _ARMENIAN_ORDER]
    checks.append(('the class law at all 36 seats (four classes of '
                   'nine, recomputed from position)',
                   law == [cls(p) for p in range(1, 37)]
                   and len(ARMENIAN) == 36, law[:4] + law[-2:]))
    # 2. Uniqueness, printed against the mint's coordinate: 36
    #    letters, 36 distinct values — a ciphered table, not a
    #    class axis with collisions.
    checks.append(('36 letters, 36 distinct values (uniqueness '
                   'holds; singleness and uniqueness both)',
                   len(set(ARMENIAN.values())) == 36
                   and sum(ARMENIAN.values()) == 49995,
                   (len(set(ARMENIAN.values())), sum(ARMENIAN.values()))))
    # 3. Calibration: the witnesses' own worked example, exact —
    #    the number the audit trusted before any derived number.
    r = weigh('ՌՋՀԵ', 'armenian')
    checks.append(('ՌՋՀԵ == 1975 (the witnesses\' worked example)',
                   r['value'] == 1975
                   and r['breakdown'] == [('Ռ', 1000), ('Ջ', 900),
                                          ('Հ', 70), ('Ե', 5)],
                   (r['value'], r['breakdown'])))
    # 4. The examples both text witnesses share: 2222, 2004, 120, 50.
    ex = (weigh('ՍՄԻԲ', 'armenian')['value'],
          weigh('ՍԴ', 'armenian')['value'],
          weigh('ՃԻ', 'armenian')['value'],
          weigh('Ծ', 'armenian')['value'])
    checks.append(('shared examples: ՍՄԻԲ 2222, ՍԴ 2004, ՃԻ 120, '
                   'Ծ 50', ex == (2222, 2004, 120, 50), ex))
    # 5. MELA's era date at the door of practice: ՌՆԾԵ = 1455, the
    #    year the manual's colophon writes after the ԹՎ siglum.
    checks.append(('ՌՆԾԵ == 1455 (MELA\'s era date)',
                   weigh('ՌՆԾԵ', 'armenian')['value'] == 1455,
                   weigh('ՌՆԾԵ', 'armenian')['value']))
    # 6. The system's own arithmetic: the largest number writable
    #    without the overline — one letter per class, descending.
    checks.append(('ՔՋՂԹ == 9999 (the maximum without the overline)',
                   weigh('ՔՋՂԹ', 'armenian')['value'] == 9999,
                   weigh('ՔՋՂԹ', 'armenian')['value']))
    # 7. Case: the seam folds minuscules to the majuscule bank —
    #    աբգ and ԱԲԳ are one weighing, and the sweep's corpus head
    #    crosses at its recorded value through the fold.
    a = weigh('աբգ', 'armenian')['value']
    b = weigh('ԱԲԳ', 'armenian')['value']
    x = weigh('ախոնեմե', 'armenian')['value']
    checks.append(('case folds at the seam: աբգ == ԱԲԳ == 6; the '
                   'corpus head ախոնեմե == 1251',
                   a == b == 6 and x == 1251, (a, b, x)))
    # 8. The boundary at the classical door (R1 keeps it): the
    #    medieval additions are not keys of the bank — through
    #    weigh() and through the DEFAULT door a weighing that
    #    meets one hears silence, in either case, and the
    #    "sometimes" 10000 never fires by accident: օր ("day")
    #    weighs its Ր alone, 5000, the օ silent.
    checks.append(('the boundary at the classical door: Օ, Ֆ, օ, '
                   'ֆ weigh nothing through weigh() or the default '
                   'door (annex opt-in; no accidental 10000)',
                   'Օ' not in ARMENIAN and 'Ֆ' not in ARMENIAN
                   and weigh('Օ', 'armenian')['value'] == 0
                   and weigh('Օ', 'armenian')['breakdown'] == []
                   and weigh('ֆ', 'armenian')['value'] == 0
                   and armenian('Օ')['value'] == 0
                   and armenian('օր')['value'] == 5000,
                   (weigh('Օ', 'armenian')['value'],
                    armenian('օր')['value'])))
    # 9. The overline door, priced (R2): an overlined Ռ weighs
    #    1000 x 10,000 beside its letters at face — 10,000,975,
    #    one mark counted; the unmarked word is untouched.
    d = armenian('Ռ' + '\u0305' + 'ՋՀԵ')
    checks.append(('armenian() prices the overline at x10,000: '
                   'overlined ՌՋՀԵ == 10000975, 1 mark; the '
                   'unmarked word weighs 1975, 0 marks',
                   d['value'] == 10000975 and d['overline_marks'] == 1
                   and d['overline_factor'] == 10000
                   and armenian('ՌՋՀԵ')['value'] == 1975
                   and armenian('ՌՋՀԵ')['overline_marks'] == 0,
                   (d['value'], d['overline_marks'])))
    # 10. The witnesses' overline exhibits at the resolved factor:
    #     overlined Ա = 10,000 (Wikipedia; MELA) and overlined
    #     Ջ = 9,000,000 (MELA) — the numbers the factor was
    #     chosen among, reproduced at the door.
    checks.append(('the overline exhibits: overlined Ա == 10000; '
                   'overlined Ջ == 9000000 (MELA)',
                   armenian('Ա' + '\u0305')['value'] == 10000
                   and armenian('Ջ' + '\u0305')['value'] == 9000000,
                   (armenian('Ա' + '\u0305')['value'],
                    armenian('Ջ' + '\u0305')['value'])))
    # 11. THE SYNERGY PROOF, in code: the classical bank's
    #     uniqueness law is the factor's judge. At x10,000 the 36
    #     overlined values are 36 distinct seats, disjoint from
    #     the 36 plain values — zero collisions. At x1,000 the
    #     overlined set strikes the plain thousands class in
    #     exactly nine seats. The factor that keeps the whole
    #     working together is the one this door applies.
    plain = set(ARMENIAN.values())
    over10k = {v * 10000 for v in plain}
    over1k = {v * 1000 for v in plain}
    checks.append(('the synergy sweep: x10,000 collides nowhere '
                   '(36 distinct overlined values, disjoint from '
                   'the plain 36); x1,000 collides in exactly 9',
                   len(over10k) == 36 and over10k.isdisjoint(plain)
                   and len(over1k & plain) == 9,
                   (len(over10k & plain), len(over1k & plain))))
    # 12. The late annex (R1): seated apart, exact at both cases,
    #     reachable only on the explicit path — օր weighs 15000
    #     with the annex open (օ 10000 + Ր 5000) against 5000
    #     shut (check 8); the classical bank stands unblended
    #     at 36 keys, the annex at its four.
    checks.append(('the late annex: ARMENIAN_LATE exact '
                   '(Օ/օ 10000, Ֆ/ֆ 20000); the late path weighs '
                   'օր == 15000; the classical bank unblended',
                   ARMENIAN_LATE == {'Օ': 10000, 'օ': 10000,
                                     'Ֆ': 20000, 'ֆ': 20000}
                   and armenian('Օ', late=True)['value'] == 10000
                   and armenian('օ', late=True)['value'] == 10000
                   and armenian('Ֆ', late=True)['value'] == 20000
                   and armenian('ֆ', late=True)['value'] == 20000
                   and armenian('օր', late=True)['value'] == 15000
                   and armenian('օր', late=True)['late_annex'] is True
                   and len(ARMENIAN) == 36,
                   (armenian('Օ', late=True)['value'],
                    armenian('օր', late=True)['value'])))
    # 13. The fence: attested, complete, the difference from the
    #     folk witness named, the annex and the resolved factor
    #     on its face.
    p = SYSTEMS['armenian']['provenance']
    checks.append(('armenian provenance carries the fence '
                   '(ATTESTED, complete 36, NOT halehame\'s case, '
                   'ARMENIAN_LATE annex and the x10,000 factor '
                   'stated)',
                   p.startswith('ATTESTED') and '36' in p
                   and 'halehame' in p and 'ARMENIAN_LATE' in p
                   and '10,000' in p, p))
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
