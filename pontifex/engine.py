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
    ARMENIAN,
    COPTIC, ARMENIAN_LATE,
    GEORGIAN,
    CYRILLIC, GLAGOLITIC,
    ARAMAIC, ARAMAIC_IMPERIAL, ARAMAIC_SYRIAC,
    HANGUL, HANGUL_INITIAL, HANGUL_VOWEL, HANGUL_FINAL,
    HANGUL_NULL_INITIAL, HANGUL_1446,
    HANGUL_1446_INITIAL, HANGUL_1446_VOWEL, HANGUL_1446_FINAL,
    _jamo_conjoining,
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
    # DOCTRINE: the COPTIC bank is the registry's one DERIVED
    # table — the Greek Milesian values received entire by
    # script descent, audited 2026-11-24 as the key's first
    # inheritance test: a table received, not made (the mints)
    # and not found (the attested tables). Its fence carries
    # the descent and its partings: value agreement with the
    # 'greek' bank is total (27/27 seats), and what changed in
    # the receiving is printed — the 90-seat's holder changed
    # lineage (koppa's dead letter out, the living Demotic fai
    # in), the epissemon seats kept signs, and the native
    # letters beyond fai took no seats because the grid arrived
    # full. The sweep (Worker #8) argued ATTESTED; the seat
    # takes DERIVED, reasoning printed in the audit (§VIII D1):
    # the tradition's use is its own and attested, but the
    # values are inherited. The bank is keyed in small letters;
    # weigh() casefolds Coptic input at its seam (the script
    # was caseless). coptic() below is the manuscript door: it
    # counts the numeral marks and prices none.
    # DOCTRINE: the GEORGIAN bank is the second DESIGNED table in
    # the registry — the classical 38-letter alphabet's own numeral
    # system, audited 2026-11-24 as the Caucasus road's anchor and
    # read as the control case against the Armenian bank beside it:
    # two designed alphabets, one decimal class law, and the
    # partings printed where they stand (the doubled 400 in the
    # hundreds class; a native 10000 letter where Armenian seats
    # none and reaches by the overline device instead). The bank is
    # keyed in Mkhedruli, the dress the witnesses print; the older
    # dresses (Asomtavruli, Nuskhuri) are the same table and are not
    # re-keyed. The five obsolete letters seat IN this bank: they
    # are original members of the classical alphabet, the mirror
    # case of the Armenian additions (the audit's §VII D1). The
    # script is unicase; no seam preparation applies.
    'georgian':      {'table': GEORGIAN,
                      'provenance': 'ATTESTED — the classical '
                                    'Georgian alphabetic numeral '
                                    'table: the designed alphabet\'s '
                                    'own system (38 classical '
                                    'letters valued in decimal '
                                    'classes to a native 10000), '
                                    'audited 2026-11-24 (two '
                                    'witnesses read entire agree on '
                                    'all 38 cells; the depth caveat '
                                    'stands in the audit: the '
                                    'witnesses are modern reference '
                                    'works, Wikipedia\'s table '
                                    'sourced to Makharoblidze 2009, '
                                    'and no primary manuscript was '
                                    're-read). Keyed in Mkhedruli, '
                                    'the witnesses\' dress; the '
                                    'older Asomtavruli and Nuskhuri '
                                    'forms are the same table, not '
                                    're-keyed. The hundreds class '
                                    'carries the table\'s one '
                                    'parting from the clean seat '
                                    'law: 400 is doubled (ჳ and უ), '
                                    'the seat law parts at '
                                    'positions 23–28, and the bank '
                                    'holds 37 distinct values in 38 '
                                    'letters. NOT the Armenian '
                                    'bank\'s case in two respects: '
                                    'its five obsolete letters are '
                                    'classical members and seat in '
                                    'the bank (no annex), and its '
                                    '10000 is a letter (ჵ), not a '
                                    'device'},
    # DOCTRINE: the CYRILLIC bank is the registry's second DERIVED
    # table — the Greek Milesian values received entire into a
    # second script, audited 2026-11-24 as the Slavonic pair's
    # inheritance test (the Coptic test run again in a second
    # family): all 27 seats agree with the 'greek' bank at the
    # witnesses' own Greek pairings. Its fence carries the descent
    # and its partings: the variant letterforms seated at three
    # seats (a multiplicity of form, not of value), the western
    # pair refused whole (Ч at 90 only; Ҁ in silence), the titlo
    # an unpriced mark, and the thousands sign ҂ a priced
    # multiplier (x1000) read at the cyrillic() door, never by
    # weigh(). The bank is keyed in capitals; weigh() folds
    # Cyrillic input to capitals at its seam.
    'cyrillic':      {'table': CYRILLIC,
                      'provenance': 'DERIVED — the Cyrillic '
                                    'alphabetic numeral table: the '
                                    'Greek Milesian values received '
                                    'entire by script descent (all '
                                    '27 canonical seats agree with '
                                    'the \'greek\' bank at the '
                                    'witnesses\' own pairings), '
                                    'audited 2026-11-24 (two '
                                    'witnesses read entire agree on '
                                    'every seat). The tradition\'s '
                                    'USE is its own and attested '
                                    '(First Bulgarian Empire, late '
                                    '10th c.; Russian use to the '
                                    'early 18th; Church Slavonic '
                                    'books still) — the tier names '
                                    'the VALUES\' provenance, not '
                                    'the use. Variant letterforms '
                                    'seat at 400 (Ѵ, Ꙋ, Ѹ beside У), '
                                    '800 (Ѿ, Ꙍ beside Ѡ) and 900 '
                                    '(Ѧ beside Ц): 33 letters, 27 '
                                    'distinct values. The western '
                                    'pair is REFUSED whole: Ч '
                                    'stands at 90 only and Ҁ '
                                    'weighs silence. The titlo is '
                                    'an unpriced mark; the '
                                    'thousands sign ҂ multiplies '
                                    'the following letter by 1000 '
                                    'at the cyrillic() door only'},
    # DOCTRINE: the GLAGOLITIC bank is the pair's other law — a
    # table priced by its own alphabet's ORDER, audited 2026-11-24
    # beside the Cyrillic inheritance as the region's control case
    # proper. Its values are the tradition's OWN assignment (not
    # inherited), so the tier is ATTESTED — with the questioned
    # range carried on the fence at full size, as the chief witness
    # itself prints it. The bank is keyed in capitals; weigh()
    # folds Glagolitic input to capitals at its seam.
    'glagolitic':    {'table': GLAGOLITIC,
                      'provenance': 'ATTESTED — the Glagolitic '
                                    'alphabetic numeral table: '
                                    'values assigned by the native '
                                    'order of the Glagolitic '
                                    'alphabet itself, NOT by Greek '
                                    'values (the tradition\'s own '
                                    'assignment; 9th c. by general '
                                    'agreement), audited 2026-11-24 '
                                    '(W1 read entire; the second '
                                    'witness concurring on all 20 '
                                    'cells it prints in text). The '
                                    'partings ride the fence: the '
                                    '10-seat\'s holder is disputed '
                                    '(Ⰺ or Ⰹ — both seat at 10; '
                                    'the value is not in dispute); '
                                    'three letters inside the '
                                    'valued span are HOLES carrying '
                                    'no value (Ⱊ, Ⱐ, Ⱒ); 6000–8000 '
                                    'have no single letters (W1 '
                                    'prints composite spellings, '
                                    'refused). THE QUESTIONED '
                                    'RANGE at full size: values '
                                    'greater than 999 are '
                                    'uncertain in the chief '
                                    'witness itself, and the '
                                    'validity of 3000 and greater '
                                    'is questioned in its sources; '
                                    'the thousands seats stand as '
                                    'its table prints them, under '
                                    'that warning. 34 letters, 33 '
                                    'distinct values'},
    'coptic':        {'table': COPTIC,
                      'provenance': 'DERIVED — the Coptic alphabetic '
                                    'numeral table: the Greek '
                                    'Milesian values received entire '
                                    'by script descent (all 27 value '
                                    'seats agree with the \'greek\' '
                                    'bank), audited 2026-11-24 '
                                    '(Wikipedia, "Coptic script"; '
                                    'fsymbols; tooldune concurring; '
                                    'Satzinger\'s course and Dr. '
                                    'Isaac\'s Institute page '
                                    'concurring where they exhibit). '
                                    'The partings ride on its face: '
                                    'at 90 the seat\'s holder changed '
                                    'lineage — Greek\'s archaic '
                                    'koppa ϟ yields to Coptic\'s '
                                    'living Demotic letter fai ϥ; '
                                    'at 6 and 900 the epissemon seats '
                                    'kept numeral signs (ⲋ sou, '
                                    'Ⳁ sampi); the Demotic letters '
                                    'beyond fai (ϣ Ϧ Ϩ ϫ Ϭ ϯ, and '
                                    'Akhmimic Ⳉ) carry NO value in '
                                    'any source — the grid arrived '
                                    'full. The sweep (Worker #8, '
                                    '2026-10-11) argued ATTESTED for '
                                    'this bank; the seat takes '
                                    'DERIVED: the tradition\'s use '
                                    'is its own and attested, but '
                                    'the VALUES are inherited, not '
                                    'made or found (Phase I audit '
                                    '§VIII D1). Thousands are '
                                    'written by marks (the ͵ sign; '
                                    'the double overline), never by '
                                    'letter values; the coptic() '
                                    'door counts the marks and '
                                    'prices none'},
    # DOCTRINE: the ARAMAIC bank is the map's last seat — the
    # abjad bank entire in Aramaic's own scripts, audited
    # 2026-11-24 as an IDENTITY to be sourced, not assumed: the
    # same 22 values the 'hebrew' bank carries, seated in the
    # Imperial glyphs and in the Syriac letters. Its fence states
    # the identity and its one parting: the identity is ONE fact,
    # never two witnesses (agreement with 'hebrew' corroborates
    # nothing twice), and NO finals extension is seated — mispar
    # gadol's 500–900 is a Hebrew method this engine seats
    # nowhere, and Aramaic's own practice writes past 400
    # additively. aramaic() below is the manuscript door: it
    # counts the dress marks (the overline; the raised point)
    # and prices none.
    'aramaic':       {'table': ARAMAIC,
                      'provenance': 'ATTESTED — the Aramaic abjad '
                                    'table: the 22 letters at the '
                                    'shared Northwest Semitic '
                                    'values (1–400), seated in TWO '
                                    'scripts — the Imperial '
                                    'Aramaic glyphs '
                                    '(U+10840–U+10855), tabulated '
                                    'with these values by Cherry '
                                    '(York University, 2007), and '
                                    'the Syriac letters, whose own '
                                    'numeral practice the '
                                    'grammatical tradition '
                                    'documents (Nöldeke\'s '
                                    'appendix, via Hughes) — '
                                    'audited 2026-11-24 (three '
                                    'witnesses agree on all 22 '
                                    'cells; the identity with '
                                    'the \'hebrew\' bank proven '
                                    'seat by seat in both '
                                    'directions). The identity '
                                    'is ONE fact, never two '
                                    'witnesses: this bank and '
                                    '\'hebrew\' are the same '
                                    'inheritance in two scripts, '
                                    'and a convergence between '
                                    'them corroborates nothing '
                                    'twice. NO finals extension '
                                    'is seated: the mispar gadol '
                                    'values (500–900) are a '
                                    'Hebrew method this engine '
                                    'seats nowhere, and '
                                    'Aramaic\'s own practice '
                                    'writes past 400 additively '
                                    '(Syriac ܬܩ = 500). The '
                                    'Imperial block\'s dedicated '
                                    'number signs are not '
                                    'letters and carry no seat '
                                    'here. The aramaic() door '
                                    'counts the manuscript marks '
                                    '(the overline; the raised '
                                    'point) and prices none'},
    # DOCTRINE: the HANGUL MINT is a house coinage on a designed
    # grid — the registry's third mint, after the gojūon and the
    # Ge'ez. The Phase I audit (2026-11-24) verified the checked
    # negative: Hangul has NO letter-numeral tradition (Korean
    # numerals are native words and borrowed Chinese glyphs);
    # what exists is the grid — Sejong's featural alphabet with
    # canonical orders, audited from two witnesses and the
    # Unicode standard's block order. The mint prices the jamo
    # by their seats within the script's three positional strata
    # (initial / vowel / final), the Aramaic face-law's shape on
    # the triad's face. Its teeth stand on its face: the tense
    # doubles are lawful at their seats (their prices are NOT
    # doublings — the parting is printed at the bank); the final
    # digraphs are refused initial seats (no choseong forms
    # exist); the obsolete letters are refused modern seats
    # (theirs is the 1446 annex, opt-in at the hangul() door,
    # the ARMENIAN_LATE shape); and ㅇ is the hybrid hinge —
    # a full letter as a final, the script's own ZERO as an
    # initial, priced 0 at the door and counted, never silent.
    # The North Korean orders part from the South and are not
    # seated. hangul() below is the reading door: it decomposes
    # syllable blocks by the standard's law and applies the
    # null law; weigh() is the raw bank door and shows seats.
    'hangul':        {'table': HANGUL,
                      'provenance': 'CONSTRUCTED — the HANGUL MINT: '
                                    'house coinage minted at the '
                                    'desk 2026-11-24 under the '
                                    'founder\'s Flagpole, on the '
                                    'audited grid (Phase I audit: '
                                    'two witnesses and the Unicode '
                                    'standard agree on the orders; '
                                    'NO letter-numeral tradition '
                                    'exists for Hangul — the '
                                    'negative is checked, not '
                                    'assumed). The jamo are priced '
                                    'by their canonical South '
                                    'Korean seats within three '
                                    'strata (initial 19, vowel 21, '
                                    'final 27). Teeth: the tense '
                                    'doubles are lawful at their '
                                    'seats, their prices NOT '
                                    'doublings (only ㄲ coincides '
                                    'with twice its base); the '
                                    'final digraphs are refused '
                                    'modern initial seats; the '
                                    'obsolete '
                                    'letters (ㆁ ㅿ ㆆ ㆍ) are refused '
                                    'modern seats — theirs is the '
                                    '1446 annex at the hangul() '
                                    'door\'s hist path. The hinge '
                                    'ㅇ: full letter as a final '
                                    '(seat 21), the script\'s own '
                                    'zero as an initial — the '
                                    'hangul() door prices it 0 '
                                    'there and counts it; the raw '
                                    'bank shows its seat (12). '
                                    'The North Korean orders part '
                                    'and are not seated; NOT '
                                    'attested, traditional, or '
                                    'ancient'},
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
    # own table pairs the cases at one value); Cyrillic and Glagolitic
    # fold the same way again (their banks are keyed in the capitals
    # the witnesses print, and case carries no Slavonic numeral value); Greek is casefolded
    # and stripped of diacritics (its table is keyed in bare lowercase,
    # and neither case nor accent carries Milesian value); Coptic is
    # casefolded to its small-letter bank (the script was caseless —
    # case is a modern convention — so the fold is pure preparation).
    if system in ('latin_ordinal', 'agrippa', 'armenian',
                  'cyrillic', 'glagolitic'):
        w = word.upper()
    elif system == 'greek':
        w = _normalize_greek(word)
    elif system == 'coptic':
        # MECHANISM: Coptic folds the other way — its bank is keyed
        # in small letters (the parent Greek bank's habit), and the
        # script was caseless, case being a modern convention, so
        # casefold carries no value away. The combining marks a
        # manuscript carries (the overline, the jinkim) are not
        # keys of the bank and pass in silence here; the coptic()
        # door counts the numeral marks.
        w = word.casefold()
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


def cyrillic(word):
    """Weigh a Cyrillic numeral in manuscript dress, devices priced.

    MECHANISM: the bank's reading door for text as the tradition
    writes it. The thousands sign ҂ (U+0482) PRECEDES the letter it
    multiplies, so the door walks the word left to right carrying a
    pending multiplier: each ҂ multiplies the pending factor by
    1000, and the next seated letter is priced at its face value x
    the pending factor, which then resets. The titlo (U+0483)
    FOLLOWS letters and is the numeral mark — counted, priced
    never. The higher encircling signs (⃝ U+20DD, ҈ U+0488,
    ҉ U+0489, ꙰ U+A670, ꙱ U+A671, ꙲ U+A672) also follow letters
    and are counted, priced never (see the doctrine below).
    Letters are folded per letter to the capitals the bank is
    keyed in — the seam's preparation, done here because the signs
    must be read in place. The result carries weigh()'s shape plus
    the dress made auditable: 'thousands_marks',
    'thousands_factor' (1000), 'titlo_marks', 'higher_marks'
    (counted, unpriced). The breakdown shows each letter's PRICED
    contribution, so its entries sum to the value. On unmarked
    text this door and weigh(word, 'cyrillic') agree exactly.

    DOCTRINE — THE THOUSANDS SIGN, PRICED: the sources agree the
    ҂ multiplies the following letter by 1000 (W1: ҂Ѕ is 6000,
    while ҂Л҂В is parsed as 30,000 + 2000, making 32,000 — each
    sign binding its own letter; W2 concurs, ҂а = 1000 through
    ҂ѳ = 9000). No source parts on the factor, so the door prices
    it — the Armenian overline's shape (a priced device), at the
    Cyrillic factor, against the Coptic overline's refusal (an
    unpriced marker): the three devices are three, and Phase III
    prints them side by side.

    DOCTRINE — THE HIGHER SIGNS, COUNTED AND NOT PRICED: beyond
    the thousands, the tradition encircles letters with signs
    whose multipliers the sources print under TWO scales — the
    Lesser count (⃝ 10^4, ҈ 10^5, ҉ 10^6, ꙰ 10^7, ꙱ 10^8,
    ꙲ 10^9) and the Greater count (the same signs squared away to
    10^48 and beyond). The scales part by orders of magnitude;
    pricing either silently would falsify the other. The door
    therefore counts the signs and prices none — the Aramaic
    raised point's discipline (counted, not priced) — and the
    choice of scale stands open for the founder's pen
    (THE-SLAVONIC-PAIR.md §VII Q1).
    """
    THOUSANDS = '\u0482'
    TITLO = '\u0483'
    HIGHER = {'\u20dd', '\u0488', '\u0489', '\ua670', '\ua671',
              '\ua672'}
    total = 0
    breakdown = []
    pending = 1
    thousands_marks = 0
    higher_marks = 0
    for ch in word:
        if ch == THOUSANDS:
            thousands_marks += 1
            pending *= 1000
            continue
        if ch == TITLO:
            continue  # the mark rides its letter; counted below
        if ch in HIGHER:
            higher_marks += 1
            continue
        folded = ch.upper()
        if folded in CYRILLIC:
            priced = CYRILLIC[folded] * pending
            breakdown.append((folded, priced))
            total += priced
        # MECHANISM: a pending ҂ is spent by the next letter,
        # seated or not — the sign binds what follows it, and an
        # unseated letter spends it in silence.
        pending = 1
    return {
        'word': word,
        'system': 'cyrillic',
        'value': total,
        'provenance': SYSTEMS['cyrillic']['provenance'],
        'breakdown': breakdown,
        'thousands_marks': thousands_marks,
        'thousands_factor': 1000,
        'titlo_marks': word.count(TITLO),
        'higher_marks': higher_marks,
    }


def coptic(word):
    """Weigh a Coptic word in the inherited Milesian table, manuscript dress.

    MECHANISM: the bank's reading door for text as manuscripts
    write it. It strips the two combining overlines — U+0305, the
    continuous line that marks numeral use, and U+033F, the double
    overline — COUNTS each kind, counts the numeral signs (U+0375)
    standing in the text, and weighs the bare letters in the
    inherited table (case folded at weigh()'s seam). The result is
    weigh()'s result on the bare word, with 'word' restored to the
    input as given and the three counts carried as
    'overline_marks', 'double_overline_marks', and
    'numeral_sign_marks', so every mark's presence is auditable,
    never silent.

    DOCTRINE: no mark is priced at this door, and the refusal is
    the sources' own shape, not a disputed factor. In every
    witness read, the plain overline is a MARKER — "sometimes
    numerical use is distinguished from text with a continuous
    overline above the letters" (Wikipedia) — never a multiplier:
    descent kept the Greek mark a mark. (The Armenian line, by
    contrast, is a multiplier in its sources, its factor settled
    by the founder's ruling at x10,000; no Coptic source gives
    its line a factor at all.) The double overline and the ͵ sign
    are the record's thousands DEVICES (the Unicode Standard
    §7.3, as Wikipedia reports it: ⲁ̿ and ⲁ͵ each write 1,000) —
    devices of notation, not letter values, and Satzinger prints
    yet a third (a stauros sign at 1000). This door reports the
    devices it sees and prices none of them: a thousands reading
    law is an open coordinate for the founder's pen (Phase I
    audit §VII Q1), and weigh(word, 'coptic') is the raw bank
    door, which passes all three marks in silence. The jinkim
    (U+0300, the Bohairic syllable mark) is not a numeral mark
    and is neither stripped nor counted — it passes as it passes
    at the raw door, in silence.
    """
    overlines = word.count('\u0305')       # the numeral-use marker
    doubles = word.count('\u033f')         # the thousands device
    signs = word.count('\u0375')           # the other thousands device
    bare = word.replace('\u0305', '').replace('\u033f', '')
    result = weigh(bare, 'coptic')
    result['word'] = word
    result['overline_marks'] = overlines
    result['double_overline_marks'] = doubles
    result['numeral_sign_marks'] = signs
    return result


def aramaic(word):
    """Weigh an Aramaic word in the abjad bank, manuscript dress.

    MECHANISM: the bank's reading door for text as the traditions
    write it. It counts the two combining marks that carry
    numeral meaning in the Syriac practice — U+0305, the overline,
    and U+0307, the raised point — strips them, and weighs the
    bare letters in the bank (either stratum; weigh() passes the
    glyphs as written, there being no case in either script). The
    result is weigh()'s result on the bare word, with 'word'
    restored to the input as given and the counts carried as
    'overline_marks' and 'raised_point_marks', so every mark's
    presence is auditable, never silent. Other combining marks a
    pointed Syriac text carries (the vowel points, the bgdkpt
    dots below) are not numeral marks and are neither stripped
    nor counted — weigh() passes them in silence, as it passes
    every character no bank seats.

    DOCTRINE: no mark is priced at this door. The overline is a
    MARKER in the Syriac witness — Hughes, after Nöldeke: the
    numerals "are written overlined" so the reader does not take
    them for words — the same office the line holds in Coptic,
    and the opposite of Armenia, where the line is a multiplier:
    one mark, three offices, each read from its own sources. The
    raised point is the raised-decade DEVICE (a decade letter
    with a raised point reads as its century: ܣ̇ = 600 in the
    pointed convention Hughes describes) — counted, not priced,
    for two reasons printed here: the additive writing is the
    tradition's plain alternative and already weighs true at the
    raw bank (ܬܩ = 500 needs no device), and the same combining
    dot above is Syriac's hard-dot for the bgdkpt letters, so a
    priced point would tax ordinary pointed text for a numeral
    it does not intend. A reading law for the device is an open
    coordinate for the founder's pen (Phase I audit §VII Q1).
    The additive hundreds need no door at all: they are the
    bank's own letters summed, at weigh() as here.
    """
    overlines = word.count('\u0305')       # the numeral-use marker
    raised = word.count('\u0307')          # the raised-decade device
    bare = word.replace('\u0305', '').replace('\u0307', '')
    result = weigh(bare, 'aramaic')
    result['word'] = word
    result['overline_marks'] = overlines
    result['raised_point_marks'] = raised
    return result


def _jamo_compat(conjoining):
    """The compatibility form of a conjoining jamo, by name.

    MECHANISM: the mirror of tables._jamo_conjoining — strip the
    'HANGUL CHOSEONG/JUNGSEONG/JONGSEONG ' prefix to the name-tail
    and find 'HANGUL LETTER <tail>' in the compatibility block.
    Used so the hangul() door's breakdown shows the letters as
    readers write them, not as the standard files them."""
    name = unicodedata.name(conjoining, '')
    for prefix in ('HANGUL CHOSEONG ', 'HANGUL JUNGSEONG ',
                   'HANGUL JONGSEONG '):
        if name.startswith(prefix):
            tail = name[len(prefix):]
            break
    else:
        return conjoining
    for cp in range(0x3131, 0x3190):
        if unicodedata.name(chr(cp), '') == 'HANGUL LETTER ' + tail:
            return chr(cp)
    return conjoining


def hangul(word, hist=False):
    """Weigh a Korean word in the Hangul mint, syllable dress.

    MECHANISM: the mint's reading door for text as it is written.
    The word is NFD-normalized, which decomposes every syllable
    block into its conjoining jamo by the standard's own law
    (block = (initial × 21 + vowel) × 28 + final, in the South
    order); each jamo is then priced at its seat in its stratum.
    Bare compatibility jamo are resolved by Unicode name: a vowel
    to its vowel seat; a consonant to its INITIAL seat (the
    door's convention for a letter standing alone — stated here
    because the compatibility block cannot say which stratum a
    bare letter means); a digraph, which has no initial form, to
    its FINAL seat — the only seat it holds. The result carries
    weigh()'s shape plus the dress made auditable: the three
    strata subtotals, 'null_initials' (every placeholder ㅇ the
    null law priced at 0 — the zero is counted, never silent),
    'unseated' (signs the active grid refuses: obsolete letters
    on the modern path, modern-only signs on the hist path), and
    'hist_annex'. The breakdown shows each jamo's PRICED
    contribution in compatibility dress, so its entries sum to
    the value and the nulls show as ('ㅇ', 0).

    DOCTRINE — THE NULL LAW: in the modern grid, a syllable-
    initial ㅇ is the script's own zero, the silent placeholder —
    phonologically exact in modern Korean, where an initial ㅇ is
    always the placeholder and the letter's consonantal life is
    final. The door prices it 0 and counts it. weigh(word,
    'hangul') is the raw bank door: it reads conjoining jamo at
    their seats and shows the initial ㅇ at seat 12 — the two
    doors' parting is printed here and pinned in hangul_checks(),
    the way kana()'s ー parts from the raw kana bank.

    DOCTRINE — THE 1446 ANNEX (hist=True): the introduction grid
    of the Hunminjeongeum, opt-in only — the ARMENIAN_LATE shape.
    The classical bank is never blended: on the hist path the
    modern-only signs (the tense doubles, the compound vowels)
    are unseated, and the obsolete letters stand at their 1446
    seats (ㆍ, the first vowel of 1446, at vowel seat 1). The
    annex has NO null: its initial ㅇ prices its seat (15) — the
    annex predates the placeholder convention's hardening, and
    printing a modern zero into 1446 would be the forgery this
    engine exists to refuse. The annex's finals are the 17
    consonants at final seats in introduction order, a stated
    construction (Phase I audit §X).
    """
    if hist:
        strata = (HANGUL_1446_INITIAL, HANGUL_1446_VOWEL,
                  HANGUL_1446_FINAL)
    else:
        strata = (HANGUL_INITIAL, HANGUL_VOWEL, HANGUL_FINAL)
    total = 0
    breakdown = []
    subtotals = {'initial': 0, 'vowel': 0, 'final': 0}
    nulls = 0
    unseated = 0
    for ch in unicodedata.normalize('NFD', word):
        cp = ord(ch)
        if 0x1100 <= cp <= 0x115E:
            kind, bank = 'initial', strata[0]
            shown = _jamo_compat(ch)
        elif 0x1161 <= cp <= 0x11A7:
            kind, bank = 'vowel', strata[1]
            shown = _jamo_compat(ch)
        elif 0x11A8 <= cp <= 0x11FF:
            kind, bank = 'final', strata[2]
            shown = _jamo_compat(ch)
        elif 0x3131 <= cp <= 0x318D:
            # MECHANISM: a bare compatibility jamo — the block
            # runs to U+318D, where the archaic letters live —
            # resolved by name, initial seat first (the door's
            # convention), then vowel, then final (the digraphs'
            # only seat).
            shown = ch
            resolved = None
            for kind_try, bank_try in (('initial', strata[0]),
                                       ('vowel', strata[1]),
                                       ('final', strata[2])):
                kind_name = {'initial': 'CHOSEONG',
                             'vowel': 'JUNGSEONG',
                             'final': 'JONGSEONG'}[kind_try]
                try:
                    conj = _jamo_conjoining(ch, kind_name)
                except ValueError:
                    continue
                if conj in bank_try:
                    resolved = (kind_try, bank_try, conj)
                    break
            if resolved is None:
                unseated += 1
                continue
            kind, bank, ch = resolved
        else:
            continue  # not a jamo: silence, not false weight
        if ch not in bank:
            unseated += 1
            continue
        if (not hist and kind == 'initial'
                and ch == HANGUL_NULL_INITIAL):
            # THE NULL LAW: the placeholder prices 0, and shows.
            breakdown.append((shown, 0))
            nulls += 1
            continue
        priced = bank[ch]
        breakdown.append((shown, priced))
        subtotals[kind] += priced
        total += priced
    return {
        'word': word,
        'system': 'hangul',
        'value': total,
        'provenance': SYSTEMS['hangul']['provenance'],
        'breakdown': breakdown,
        'initial_subtotal': subtotals['initial'],
        'vowel_subtotal': subtotals['vowel'],
        'final_subtotal': subtotals['final'],
        'null_initials': nulls,
        'unseated': unseated,
        'hist_annex': bool(hist),
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


# MECHANISM: the classical alphabet in its own order — the audit's
# coordinate for the seat. The value sequence is recomputed from
# position in georgian_checks() below, never trusted from the
# dict's shape.
_GEORGIAN_ORDER = 'აბგდევზჱთიკლმნჲოპჟრსტჳუფქღყშჩცძწჭხჴჯჰჵ'


def georgian_checks():
    """Self-checks for the GEORGIAN seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-GEORGIAN-FIELD-PHASE-I-AUDIT.md): the class law recomputed
    from position in both its formulations, the witnesses' worked
    examples, the doubled seat and its shadow, the extent, the
    obsolete five seated in the bank, and the absence of zero.
    Sign-for-sign parity against the audit's frozen transcription
    (research/caucasus-north/georgian-table.csv) is a relation
    between two seats and lives in test_georgian_parity.py at the
    repository root; this battery holds the seat to the doctrine
    itself. Kept beside armenian_checks() rather than inside
    engine_checks(), so the established checks stand untouched as
    the no-collateral witness; run all for the full suite.

    DOCTRINE — THE CONTROL CASE, AT THE SEAT: this bank and the
    ARMENIAN bank carry the same value sequence over the shared
    domain 1–9000 (every Armenian value is a Georgian value), and
    part at exactly two value coordinates — 400, doubled here and
    single there; 10000, seated here as a letter and absent there.
    The checks below pin THIS bank's side; the comparison itself is
    the audit's page and the parity battery's exhibit.
    """
    checks = []
    # 1. The class law by value, recomputed from position: classes
    #    9/9/10/9/1 by seat, every value digit x 10^class.
    def power(pos):
        return 0 if pos <= 9 else 1 if pos <= 18 else 2 if pos <= 28 \
            else 3 if pos <= 37 else 4
    law = [GEORGIAN[ch] for ch in _GEORGIAN_ORDER]
    checks.append(('the class law by value at all 38 seats (every '
                   'value digit x 10^class, digit 1..9, recomputed '
                   'from position)',
                   len(GEORGIAN) == 38
                   and all(1 <= v // (10 ** power(p)) <= 9
                           and v % (10 ** power(p)) == 0
                           for p, v in enumerate(law, start=1)),
                   law[:3] + law[-2:]))
    # 2. The seat law and its parting: digit == within-class seat
    #    index fails at exactly positions 23–28, the hundreds tail
    #    downstream of the doubled 400.
    counters, fails = {}, []
    for p, ch in enumerate(_GEORGIAN_ORDER, start=1):
        klass = power(p)
        counters[klass] = counters.get(klass, 0) + 1
        if GEORGIAN[ch] // (10 ** klass) != counters[klass]:
            fails.append(p)
    checks.append(('the seat law parts at exactly positions 23–28 '
                   '(the doubled 400\'s shadow: უ at 23 carries '
                   'digit 4 at seat-index 5)',
                   fails == [23, 24, 25, 26, 27, 28], fails))
    # 3. The doubled seat itself, and the extent it makes: 38
    #    letters, 37 distinct values, sum 60395.
    checks.append(('the doubled seat: 400 carried by exactly two '
                   'letters (ჳ, უ); 38 letters, 37 distinct values, '
                   'sum 60395',
                   sorted(ch for ch, v in GEORGIAN.items() if v == 400)
                   == ['უ', 'ჳ'] and len(set(GEORGIAN.values())) == 37
                   and sum(GEORGIAN.values()) == 60395,
                   (len(set(GEORGIAN.values())), sum(GEORGIAN.values()))))
    # 4. The witnesses' worked examples at the seat, exact.
    ex = (weigh('ჩღჲთ', 'georgian')['value'],
          weigh('ჩყპზ', 'georgian')['value'],
          weigh('ციბ', 'georgian')['value'],
          weigh('ჩყმვ', 'georgian')['value'],
          weigh('ცკვ', 'georgian')['value'])
    checks.append(('the witnesses\' worked examples: 1769, 1887, '
                   '2012, the Motsameta 1846, and 2026',
                   ex == (1769, 1887, 2012, 1846, 2026), ex))
    # 5. The obsolete five seat in the bank (the audit's D1), and
    #    the system's maximum is a letter, not a device.
    checks.append(('the obsolete five seat in the bank at their '
                   'classical values (ჱ 8, ჲ 60, ჳ 400, ჴ 7000, '
                   'ჵ 10000 — the maximum is the letter ჵ)',
                   (GEORGIAN['ჱ'], GEORGIAN['ჲ'], GEORGIAN['ჳ'],
                    GEORGIAN['ჴ'], GEORGIAN['ჵ'])
                   == (8, 60, 400, 7000, 10000)
                   and max(GEORGIAN.values()) == 10000,
                   (GEORGIAN['ჱ'], GEORGIAN['ჵ'])))
    # 6. The duplicate's living consequence: 494 carries two
    #    spellings at this seat.
    checks.append(('two spellings for one number: ჳჟდ == უჟდ == 494',
                   weigh('ჳჟდ', 'georgian')['value']
                   == weigh('უჟდ', 'georgian')['value'] == 494,
                   (weigh('ჳჟდ', 'georgian')['value'],
                    weigh('უჟდ', 'georgian')['value'])))
    # 7. Zero: absence — no seat carries 0, and the witnesses'
    #    unvalued tail stands outside the bank entire.
    checks.append(('no zero seat, and the unvalued tail (ჶ ჷ ჸ ჹ ჺ '
                   'ჼ ჻) weighs silence',
                   0 not in GEORGIAN.values()
                   and weigh('ჶჷჸ', 'georgian')['value'] == 0
                   and weigh('ჶჷჸ', 'georgian')['breakdown'] == [],
                   weigh('ჶჷჸ', 'georgian')['breakdown']))
    # 8. The control case's shared domain, at this seat: every
    #    Armenian value 1..9000 is a Georgian value.
    checks.append(('CONTROL CASE — every Armenian value is a '
                   'Georgian value (the shared domain 1..9000 '
                   'entire)',
                   set(ARMENIAN.values()) <= set(GEORGIAN.values()),
                   len(set(ARMENIAN.values()) & set(GEORGIAN.values()))))
    # 9. Computed data exhibits (computation, not attestation):
    #    the alphabet's own name and the capital.
    checks.append(('computed exhibits: ანბანი 114, თბილისი 271, '
                   'საქართველო 1022',
                   (weigh('ანბანი', 'georgian')['value'],
                    weigh('თბილისი', 'georgian')['value'],
                    weigh('საქართველო', 'georgian')['value'])
                   == (114, 271, 1022),
                   weigh('საქართველო', 'georgian')['value']))
    # 10. The fence.
    p = SYSTEMS['georgian']['provenance']
    checks.append(('georgian provenance carries the fence '
                   '(ATTESTED, 38, the doubled 400 and the 10000 '
                   'letter stated, NOT the Armenian case)',
                   p.startswith('ATTESTED') and '38' in p
                   and '400' in p and '10000' in p, p[:60]))
    return checks


# MECHANISM: the canonical seats in Milesian order, with the
# witnesses' Greek pairings — the audit's coordinate for the seat.
# The inheritance is recomputed against the living GREEK bank in
# cyrillic_checks() below, never trusted from the dict's shape.
_CYRILLIC_ORDER = 'АВГДЕЅЗИѲІКЛМНѮОПЧРСТУФХѰѠЦ'
_CYRILLIC_GREEK = 'ΑΒΓΔΕϚΖΗΘΙΚΛΜΝΞΟΠϞΡΣΤΥΦΧΨΩϠ'


def cyrillic_checks():
    """Self-checks for the CYRILLIC seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-SLAVONIC-PAIR.md): the inheritance recomputed against the
    living GREEK bank at the witnesses' pairings, the witnesses'
    worked examples, the variant forms, the western refusal, and
    the manuscript door (the ҂ priced at x1000, the titlo and the
    higher signs counted and not priced). Sign-for-sign parity
    against the audit's frozen transcription
    (research/caucasus-north/cyrillic-table.csv) lives in
    test_cyrillic_parity.py; this battery holds the seat to the
    doctrine itself.
    """
    checks = []
    # 1. The inheritance, recomputed: every canonical seat equals
    #    the living GREEK bank at its printed pairing.
    checks.append(('the inheritance at all 27 seats: every '
                   'canonical value == the living GREEK bank at '
                   'the witnesses\' Greek pairings',
                   all(CYRILLIC[c] == GREEK[g.lower()]
                       for c, g in zip(_CYRILLIC_ORDER,
                                       _CYRILLIC_GREEK)),
                   [CYRILLIC[c] for c in _CYRILLIC_ORDER[:3]]))
    # 2. Extent: 33 letters (27 canonical + 6 variant forms), 27
    #    distinct values, canonical sum 4995, full sum 8695.
    canon = {c: CYRILLIC[c] for c in _CYRILLIC_ORDER}
    checks.append(('extent: 27 canonical seats summing to 4995 '
                   '(the Milesian sum); 33 letters with the '
                   'variant forms, 27 distinct values, sum 8695',
                   len(canon) == 27 and sum(canon.values()) == 4995
                   and len(CYRILLIC) == 33
                   and len(set(CYRILLIC.values())) == 27
                   and sum(CYRILLIC.values()) == 8695,
                   (sum(canon.values()), sum(CYRILLIC.values()))))
    # 3. The witnesses' worked examples at the seat.
    ex = (weigh('ѰЗ', 'cyrillic')['value'],
          weigh('ЦЧѲ', 'cyrillic')['value'],
          weigh('РНГ', 'cyrillic')['value'],
          weigh('КЗ', 'cyrillic')['value'],
          weigh('ОВ', 'cyrillic')['value'])
    checks.append(('the witnesses\' worked examples: 707, 999, '
                   '153, 27, 72', ex == (707, 999, 153, 27, 72), ex))
    # 4. The variant forms at their seats.
    checks.append(('the variant forms seat at their seats: Ѵ Ꙋ Ѹ '
                   'at 400, Ѿ Ꙍ at 800, Ѧ at 900',
                   (CYRILLIC['Ѵ'], CYRILLIC['Ꙋ'], CYRILLIC['Ѹ'],
                    CYRILLIC['Ѿ'], CYRILLIC['Ꙍ'], CYRILLIC['Ѧ'])
                   == (400, 400, 400, 800, 800, 900),
                   CYRILLIC['Ѧ']))
    # 5. The western refusal: Ч at 90 only; Ҁ in silence.
    checks.append(('the western pair refused whole: Ч == 90 at '
                   'this seat and Ҁ weighs silence',
                   CYRILLIC['Ч'] == 90
                   and weigh('Ҁ', 'cyrillic')['value'] == 0
                   and weigh('Ҁ', 'cyrillic')['breakdown'] == [],
                   weigh('Ҁ', 'cyrillic')['breakdown']))
    # 6. Case: the seam folds the smalls to the bank.
    checks.append(('case at the seat: ѱз == ѰЗ == 707 (the seam '
                   'folds to the capitals)',
                   weigh('ѱз', 'cyrillic')['value'] == 707,
                   weigh('ѱз', 'cyrillic')['value']))
    # 7. The door: the thousands sign priced at x1000, each sign
    #    binding its own letter (W1's parses, exact).
    d = (cyrillic('҂Ѕ'), cyrillic('҂Л҂В'), cyrillic('҂АѰЕ'),
         cyrillic('҂ЗРИІ'))
    checks.append(('the manuscript door prices ҂ at x1000: ҂Ѕ '
                   '6000, ҂Л҂В 32000, ҂АѰЕ 1705 (the coin year), '
                   '҂ЗРИІ 7118 (the teens written ones-first)',
                   tuple(x['value'] for x in d)
                   == (6000, 32000, 1705, 7118)
                   and d[1]['thousands_marks'] == 2
                   and d[1]['thousands_factor'] == 1000,
                   tuple(x['value'] for x in d)))
    # 8. The door on unmarked text agrees with weigh() exactly.
    checks.append(('the door and weigh() agree on unmarked text '
                   '(ѰЗ == 707 at both)',
                   cyrillic('ѰЗ')['value']
                   == weigh('ѰЗ', 'cyrillic')['value'] == 707
                   and cyrillic('ѰЗ')['thousands_marks'] == 0,
                   cyrillic('ѰЗ')['value']))
    # 9. The titlo: counted, priced never.
    t = cyrillic('А\u0483')
    checks.append(('the titlo is a mark, not a price: А҃ weighs 1 '
                   'with 1 titlo counted',
                   t['value'] == 1 and t['titlo_marks'] == 1,
                   (t['value'], t['titlo_marks'])))
    # 10. The higher signs: counted, priced never (the two scales
    #     part; the door chooses neither).
    h = cyrillic('А\u0489')
    checks.append(('the higher signs counted, not priced: А҉ '
                   'weighs 1 with 1 higher mark counted (its '
                   'million belongs to a scale this door does not '
                   'choose)',
                   h['value'] == 1 and h['higher_marks'] == 1,
                   (h['value'], h['higher_marks'])))
    # 11. The fence.
    p = SYSTEMS['cyrillic']['provenance']
    checks.append(('cyrillic provenance carries the fence '
                   '(DERIVED, 27 seats == greek, the western '
                   'refusal and the priced ҂ stated)',
                   p.startswith('DERIVED') and '27' in p
                   and 'REFUSED' in p and '1000' in p, p[:60]))
    return checks


# MECHANISM: the valued letters in block order — the audit's
# coordinate for the seat. The order law is recomputed from the
# block in glagolitic_checks() below, never trusted from the
# dict's shape.
_GLAGOLITIC_ORDER = 'ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰛⰜⰝⰞⰟⰡⰣⰤ'


def glagolitic_checks():
    """Self-checks for the GLAGOLITIC seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-SLAVONIC-PAIR.md): the order law recomputed from the
    block, the witnesses' worked examples, the doubled 10, the
    holes' silence, the extent, and the parting exhibited against
    the living CYRILLIC seat. Sign-for-sign parity against the
    audit's frozen transcription
    (research/caucasus-north/glagolitic-table.csv) lives in
    test_glagolitic_parity.py; this battery holds the seat to the
    doctrine itself.

    DOCTRINE — THE CONTROL CASE, AT THE SEAT: this bank and the
    CYRILLIC bank price the same sounds by two laws — inheritance
    there, order here — and the parting is exhibited in the audit
    (33 sound rows: 15 AGREE, 18 PART). The checks below pin THIS
    bank's side and two of the parting's sharpest coordinates.
    """
    checks = []
    # 1. The order law over the valued letters in block order,
    #    and its partings at exactly ten letters.
    valued = [ch for ch in _GLAGOLITIC_ORDER]
    breaks, idx = [], {}
    for ch in valued:
        v = GLAGOLITIC[ch]
        p = 0 if v < 10 else 1 if v < 100 else 2 if v < 1000 else 3
        idx[p] = idx.get(p, 0) + 1
        if v // (10 ** p) != idx[p]:
            breaks.append(ch)
    checks.append(('the order law over the valued letters in '
                   'block order, parting at exactly ten letters '
                   '(the tens tail Ⰺ–Ⱂ downstream of the doubled '
                   '10, and Ⱔ at the thousands tail)',
                   breaks == ['Ⰺ', 'Ⰻ', 'Ⰼ', 'Ⰽ', 'Ⰾ', 'Ⰿ', 'Ⱀ',
                              'Ⱁ', 'Ⱂ', 'Ⱔ']
                   and len(GLAGOLITIC) == 34, breaks))
    # 2. Extent: 34 letters, 33 distinct values, sum 29005.
    checks.append(('extent: 34 letters, 33 distinct values, sum '
                   '29005',
                   len(set(GLAGOLITIC.values())) == 33
                   and sum(GLAGOLITIC.values()) == 29005,
                   (len(set(GLAGOLITIC.values())),
                    sum(GLAGOLITIC.values()))))
    # 3. The witnesses' worked examples at the seat.
    ex = (weigh('ⰗⰑⰂ', 'glagolitic')['value'],
          weigh('ⰅⰊ', 'glagolitic')['value'],
          weigh('ⰝⰔⰑ', 'glagolitic')['value'])
    checks.append(('the witnesses\' worked examples: ⰗⰑⰂ 583, '
                   'ⰅⰊ 16 (the teens reversal), the Vinodol '
                   'ⰝⰔⰑ 1280', ex == (583, 16, 1280), ex))
    # 4. The doubled 10: both printed holders seat at 10.
    checks.append(('the doubled 10: Ⰹ == Ⰺ == 10 (the seat\'s '
                   'value undisputed, its holder disputed in the '
                   'record — both seat)',
                   GLAGOLITIC['Ⰹ'] == GLAGOLITIC['Ⰺ'] == 10,
                   (GLAGOLITIC['Ⰹ'], GLAGOLITIC['Ⰺ'])))
    # 5. The holes' silence, and the refused letters'.
    checks.append(('the holes weigh silence: Ⱊ Ⱐ Ⱒ (inside the '
                   'valued span) and Ⱗ (W1b\'s variant 6000) '
                   'carry no seat',
                   weigh('ⰚⰠⰢⰧ', 'glagolitic')['value'] == 0
                   and weigh('ⰚⰠⰢⰧ', 'glagolitic')['breakdown']
                   == [],
                   weigh('ⰚⰠⰢⰧ', 'glagolitic')['breakdown']))
    # 6. Case: the seam folds the smalls to the bank.
    checks.append(('case at the seat: ⰰⰱ == ⰀⰁ == 3 (the seam '
                   'folds to the capitals)',
                   weigh('ⰰⰱ', 'glagolitic')['value'] == 3,
                   weigh('ⰰⰱ', 'glagolitic')['value']))
    # 7. The parting exhibited at the seats: the sharpest
    #    coordinates against the living Cyrillic bank.
    checks.append(('THE PARTING at the seats: /ch/ — Cyrillic Ч '
                   '90 against Glagolitic Ⱍ 1000; the omega seat '
                   '— Ѡ 800 against Ⱉ 700',
                   CYRILLIC['Ч'] == 90 and GLAGOLITIC['Ⱍ'] == 1000
                   and CYRILLIC['Ѡ'] == 800
                   and GLAGOLITIC['Ⱉ'] == 700,
                   (CYRILLIC['Ч'], GLAGOLITIC['Ⱍ'])))
    # 8. The fence.
    p = SYSTEMS['glagolitic']['provenance']
    checks.append(('glagolitic provenance carries the fence '
                   '(ATTESTED, the order law, the questioned range '
                   'at full size)',
                   p.startswith('ATTESTED') and '34' in p
                   and 'QUESTIONED' in p and '999' in p, p[:60]))
    return checks


# MECHANISM: the valued signs in Milesian seat order — the audit's
# coordinate for the seat. The value sequence is recomputed from
# position in coptic_checks() below, never trusted from the
# dict's shape.
_COPTIC_ORDER = 'ⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡϥⲣⲥⲧⲩⲫⲭⲯⲱⳁ'


def coptic_checks():
    """Self-checks for the COPTIC seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-COPTIC-TABLE-PHASE-I-AUDIT.md): the Milesian sequence
    recomputed from position, the witnesses' worked examples, the
    descent exhibited against the living Greek bank, the boundary
    at the unseated Demotic letters (with fai's seat as the
    anti-boundary), and the manuscript door's refusal to price a
    mark. Sign-for-sign parity against the audit's frozen
    transcription (research/twelve-tongues/coptic-table.csv) is a
    relation between two seats and lives in test_coptic_parity.py
    at the repository root; this battery holds the seat to the
    doctrine itself. Kept beside armenian_checks() rather than
    inside engine_checks(), so the established checks stand
    untouched as the no-collateral witness; run all for the full
    suite.

    DOCTRINE — THE DESCENT, AT THE SEAT: this bank is the Greek
    bank's heir, and the checks below pin the inheritance as the
    audit established it — the values entire (the two banks' value
    sets identical), the holders altered at exactly three seats
    (6, 90, 900), and the parent reachable at the next desk for
    every comparison. A convergence between these two banks is
    continuity, single-sourced — the audit's §1.7 discipline,
    inherited from the sweep: agreement here corroborates
    nothing twice.
    """
    checks = []
    # 1. The Milesian sequence entire, recomputed from position:
    #    three classes of nine, at all 27 seats.
    milesian = ([d for d in range(1, 10)]
                + [d * 10 for d in range(1, 10)]
                + [d * 100 for d in range(1, 10)])
    law = [COPTIC[ch] for ch in _COPTIC_ORDER]
    checks.append(('the Milesian sequence at all 27 seats (three '
                   'classes of nine, recomputed from position)',
                   law == milesian and len(COPTIC) == 27,
                   law[:4] + law[-2:]))
    # 2. Uniqueness, printed as the audit measured it: 27 signs,
    #    27 distinct values — the inherited ciphered grid, whole.
    checks.append(('27 signs, 27 distinct values (uniqueness '
                   'holds; singleness and uniqueness both)',
                   len(set(COPTIC.values())) == 27
                   and sum(COPTIC.values()) == 4995,
                   (len(set(COPTIC.values())), sum(COPTIC.values()))))
    # 3. Calibration: the witnesses' worked examples, exact —
    #    the numbers the audit trusted before any derived number.
    r = weigh('ⲧⲝⲉ', 'coptic')
    checks.append(('ⲧⲝⲉ == 365 (fsymbols\' worked example) and '
                   'ⲫ == 500 (Wikipedia\'s), breakdowns exact',
                   r['value'] == 365
                   and r['breakdown'] == [('ⲧ', 300), ('ⲝ', 60),
                                          ('ⲉ', 5)]
                   and weigh('ⲫ', 'coptic')['value'] == 500,
                   (r['value'], r['breakdown'])))
    # 4. The letter part of Wikipedia's thousands example:
    #    ⲱⲡⲏ = 888 of ⲁ͵ⲱ̅ⲡ̅ⲏ̅ = 1,888 — the device reported at
    #    the door (check 9), never priced into the letters.
    checks.append(('ⲱⲡⲏ == 888 (the letter part of the 1,888 '
                   'example)', weigh('ⲱⲡⲏ', 'coptic')['value'] == 888,
                   weigh('ⲱⲡⲏ', 'coptic')['value']))
    # 5. The system's own arithmetic: the largest number writable
    #    in letters alone — one sign per class, descending.
    checks.append(('ⳁϥⲑ == 999 (the maximum in letters alone)',
                   weigh('ⳁϥⲑ', 'coptic')['value'] == 999,
                   weigh('ⳁϥⲑ', 'coptic')['value']))
    # 6. Case: the seam casefolds to the small-letter bank — the
    #    script was caseless, so ⲀⲂⲄ and ⲁⲃⲅ are one weighing;
    #    the Greek-block capitals fold too (Ϥⲁ == ϥⲁ == 91), and
    #    sampi's pair with them (Ⳁ == ⳁ == 900).
    a = weigh('ⲀⲂⲄ', 'coptic')['value']
    b = weigh('ⲁⲃⲅ', 'coptic')['value']
    f = weigh('Ϥⲁ', 'coptic')['value']
    s = weigh('Ⳁ', 'coptic')['value']
    checks.append(('case folds at the seam: ⲀⲂⲄ == ⲁⲃⲅ == 6; '
                   'Ϥⲁ == 91; Ⳁ == 900',
                   a == b == 6 and f == 91 and s == 900, (a, b, f, s)))
    # 7. The descent exhibited at the seat: the sweep's bridge
    #    row — ⲟⲍ and οζ are the same Milesian seats in two
    #    scripts, 77 on both banks. Continuity, single-sourced:
    #    the check pins the inheritance, it claims no second
    #    witness.
    checks.append(('the descent exhibited: ⲟⲍ (coptic) == οζ '
                   '(greek) == 77 — one fact in two scripts',
                   weigh('ⲟⲍ', 'coptic')['value']
                   == weigh('οζ', 'greek')['value'] == 77,
                   (weigh('ⲟⲍ', 'coptic')['value'],
                    weigh('οζ', 'greek')['value'])))
    # 8. The boundary at the door, and its anti-boundary: the
    #    Demotic letters beyond fai are not keys — a weighing
    #    that meets one hears silence, in either case — while
    #    fai itself, the one native letter the grid had room
    #    for, weighs its 90.
    checks.append(('the boundary: ϣ, ϩ, ϯ, ⳉ weigh nothing (not '
                   'seated) — and ϥ weighs 90 (the seated native)',
                   all(ch not in COPTIC for ch in 'ϢϨϮⳈ')
                   and weigh('ϣϩϯ', 'coptic')['value'] == 0
                   and weigh('ϣϩϯ', 'coptic')['breakdown'] == []
                   and weigh('ⳉ', 'coptic')['value'] == 0
                   and weigh('ϥ', 'coptic')['value'] == 90,
                   (weigh('ϣϩϯ', 'coptic')['value'],
                    weigh('ϥ', 'coptic')['value'])))
    # 9. The manuscript door: marks counted, NONE priced — an
    #    overlined ⲧⲝⲉ weighs its face 365 under three marks;
    #    the thousands devices are reported, and ⲁ̿ and ⲁ͵ each
    #    still weigh the letter's face 1, where a priced device
    #    would read 1000.
    d = coptic('ⲧ' + '\u0305' + 'ⲝ' + '\u0305' + 'ⲉ' + '\u0305')
    t1 = coptic('ⲁ' + '\u033f')
    t2 = coptic('ⲁ' + '\u0375')
    checks.append(('coptic() counts the marks and prices none: '
                   'overlined ⲧⲝⲉ == 365 at face, 3 marks; ⲁ̿ and '
                   'ⲁ͵ == 1 at face, devices counted',
                   d['value'] == 365 and d['overline_marks'] == 3
                   and t1['value'] == 1
                   and t1['double_overline_marks'] == 1
                   and t2['value'] == 1
                   and t2['numeral_sign_marks'] == 1,
                   (d['value'], d['overline_marks'], t1['value'],
                    t2['value'])))
    # 10. The fence: derived, the descent and its partings named,
    #     the boundary and the unpriced marks on its face.
    p = SYSTEMS['coptic']['provenance']
    checks.append(('coptic provenance carries the fence '
                   '(DERIVED, 27 seats, fai\'s lineage parting, '
                   'NO value boundary, marks unpriced)',
                   p.startswith('DERIVED') and '27' in p
                   and 'fai' in p and 'NO value' in p
                   and 'prices none' in p, p))
    return checks


# MECHANISM: the two strata in abjad order — the audit's
# coordinates for the seat. The Imperial order is the block's own
# (consecutive codepoints); the Syriac order is the standard's
# seats, stated seat by seat. The Hebrew twin string is the
# identity's third side. Values are recomputed from position in
# aramaic_checks() below, never trusted from the dicts' shape.
_ARAMAIC_IMPERIAL_ORDER = ''.join(chr(0x10840 + i) for i in range(22))
_ARAMAIC_SYRIAC_ORDER = ''.join(chr(cp) for cp in (
    0x0710, 0x0712, 0x0713, 0x0715, 0x0717, 0x0718, 0x0719, 0x071A,
    0x071B, 0x071D, 0x071F, 0x0720, 0x0721, 0x0722, 0x0723, 0x0725,
    0x0726, 0x0728, 0x0729, 0x072A, 0x072B, 0x072C))
_ARAMAIC_HEBREW_ORDER = 'אבגדהוזחטיכלמנסעפצקרשת'


def aramaic_checks():
    """Self-checks for the ARAMAIC seat. Returns [(name, passed, got)].

    MECHANISM: these pin the seat against its audit of record
    (THE-ARAMAIC-SEAT-PHASE-I-AUDIT.md): the abjad law recomputed
    from position in both strata, the identity exhibited against
    the LIVING Hebrew bank seat by seat, the founding head in
    three scripts, the Syriac additive hundreds, the finals
    boundary, the number-sign boundary, and the manuscript door's
    refusal to price a mark. Sign-for-sign parity against the
    audit's frozen transcription (research/twelve-tongues/
    aramaic-table.csv and aramaic-identity.csv) is a relation
    between two seats and lives in test_aramaic_parity.py at the
    repository root; this battery holds the seat to the doctrine
    itself. Kept beside coptic_checks() rather than inside
    engine_checks(), so the established checks stand untouched as
    the no-collateral witness; run all for the full suite.

    DOCTRINE — THE IDENTITY, AT THE SEAT: this bank IS the Hebrew
    bank's table in Aramaic's scripts, and the checks below pin
    the identity as the audit established it — total, at every
    seat, in both directions — together with its one parting
    (the finals) and its discipline: the identity is ONE fact,
    never two witnesses, and no convergence between these banks
    corroborates anything twice.
    """
    checks = []
    # 1. The abjad law entire, recomputed from position in both
    #    strata: nine units, nine tens, four hundreds.
    def law(pos):
        return pos if pos <= 9 else (pos - 9) * 10 if pos <= 18 \
            else (pos - 18) * 100
    imp = [ARAMAIC_IMPERIAL[ch] for ch in _ARAMAIC_IMPERIAL_ORDER]
    syr = [ARAMAIC_SYRIAC[ch] for ch in _ARAMAIC_SYRIAC_ORDER]
    checks.append(('the abjad law at all 22 seats in both strata '
                   '(nine units, nine tens, four hundreds, '
                   'recomputed from position)',
                   imp == syr == [law(p) for p in range(1, 23)],
                   imp[:4] + imp[-2:]))
    # 2. The seat's shape: two strata of 22, one bank of 44;
    #    singleness and uniqueness in each stratum; the sums.
    checks.append(('two strata of 22, one bank of 44; 22 distinct '
                   'values per stratum, each summing 1495',
                   len(ARAMAIC_IMPERIAL) == 22
                   and len(ARAMAIC_SYRIAC) == 22
                   and len(ARAMAIC) == 44
                   and len(set(ARAMAIC_IMPERIAL.values())) == 22
                   and len(set(ARAMAIC_SYRIAC.values())) == 22
                   and sum(ARAMAIC_IMPERIAL.values()) == 1495
                   and sum(ARAMAIC_SYRIAC.values()) == 1495,
                   (len(ARAMAIC), sum(ARAMAIC_IMPERIAL.values()))))
    # 3. THE IDENTITY against the living Hebrew bank, seat by
    #    seat: at every position the Imperial value, the Syriac
    #    value, and the Hebrew base letter's hechrechi value are
    #    one number.
    ident = all(ARAMAIC_IMPERIAL[i] == ARAMAIC_SYRIAC[s]
                == HEBREW[h]
                for i, s, h in zip(_ARAMAIC_IMPERIAL_ORDER,
                                   _ARAMAIC_SYRIAC_ORDER,
                                   _ARAMAIC_HEBREW_ORDER))
    checks.append(('THE IDENTITY at the seat: Imperial == Syriac '
                   '== Hebrew (mispar hechrechi) at 22/22 seats',
                   ident, '22/22 seats'))
    # 4. The founding head in three scripts: the house's first
    #    bridge-land weighs 77 in whichever Semitic script it is
    #    written — one fact, exhibited, never counted thrice.
    a = weigh('𐡏𐡆', 'aramaic')
    b = weigh('ܥܙ', 'aramaic')
    c = weigh('עז', 'hebrew')
    checks.append(('the founding head in three scripts: 𐡏𐡆 '
                   '(Imperial) == ܥܙ (Syriac) == עז (Hebrew) == 77',
                   a['value'] == b['value'] == c['value'] == 77
                   and a['breakdown'] == [('𐡏', 70), ('𐡆', 7)]
                   and b['breakdown'] == [('ܥ', 70), ('ܙ', 7)],
                   (a['value'], b['value'], c['value'])))
    # 5. The Syriac practice at the seat: past 400 by ADDITION —
    #    the additive hundreds of Nöldeke's appendix, and two of
    #    Hughes' worked examples, weigh true at the raw bank.
    ex = (weigh('ܬܩ', 'aramaic')['value'],
          weigh('ܬܬܩ', 'aramaic')['value'],
          weigh('ܩܢܙ', 'aramaic')['value'],
          weigh('ܬܫܣܕ', 'aramaic')['value'])
    checks.append(('the Syriac additive hundreds weigh at the '
                   'bank: ܬܩ 500, ܬܬܩ 900; Hughes\' examples '
                   'ܩܢܙ 157, ܬܫܣܕ 764',
                   ex == (500, 900, 157, 764), ex))
    # 6. THE FINALS BOUNDARY: no final-form glyph is a key of
    #    this bank; no value in either stratum enters 500–900;
    #    a weighing that meets a Hebrew final here hears silence
    #    (its seat is the 'hebrew' bank, at its letter's value).
    checks.append(('the finals boundary: ךםןףץ are not keys; no '
                   'value in 500–900 in either stratum; ך weighs '
                   'nothing here',
                   all(g not in ARAMAIC for g in 'ךםןףץ')
                   and max(ARAMAIC_IMPERIAL.values()) == 400
                   and max(ARAMAIC_SYRIAC.values()) == 400
                   and weigh('ך', 'aramaic')['value'] == 0
                   and weigh('ך', 'aramaic')['breakdown'] == [],
                   (max(ARAMAIC.values()),)))
    # 7. The other notation's boundary: the Imperial block's
    #    dedicated number signs and its section sign are not
    #    letters — not keys, and silent at the door.
    signs = ''.join(chr(cp) for cp in range(0x10857, 0x10860))
    checks.append(('the number-sign boundary: U+10857–U+1085F '
                   '(section sign + 8 number signs) are not keys '
                   'and weigh nothing',
                   all(chr(cp) not in ARAMAIC
                       for cp in range(0x10857, 0x10860))
                   and weigh(signs, 'aramaic')['value'] == 0,
                   weigh(signs, 'aramaic')['value']))
    # 8. The square script is not re-keyed: no glyph of this bank
    #    is a glyph of the Hebrew bank — the two seats share
    #    values, never keys, so no weighing can count one fact
    #    at both doors by accident of script.
    checks.append(('the square script not re-keyed: the two '
                   'banks\' key sets are disjoint (values shared, '
                   'glyphs never)',
                   set(ARAMAIC).isdisjoint(set(HEBREW)),
                   len(set(ARAMAIC) & set(HEBREW))))
    # 9. The manuscript door: marks counted, NONE priced — an
    #    overlined ܬܩ weighs its face 500 under two marks; a
    #    raised point on ܣ is counted and the letter still
    #    weighs its face 60, NOT the device's 600.
    d = aramaic('ܬ' + '\u0305' + 'ܩ' + '\u0305')
    r = aramaic('ܣ' + '\u0307')
    checks.append(('aramaic() counts the marks and prices none: '
                   'overlined ܬܩ == 500 at face, 2 marks; '
                   'raised-point ܣ == 60 at face (not 600), '
                   '1 mark counted',
                   d['value'] == 500 and d['overline_marks'] == 2
                   and d['raised_point_marks'] == 0
                   and r['value'] == 60
                   and r['raised_point_marks'] == 1,
                   (d['value'], d['overline_marks'], r['value'],
                    r['raised_point_marks'])))
    # 10. The fence: attested, both strata named, the identity's
    #     discipline and the unseated extension on its face.
    p = SYSTEMS['aramaic']['provenance']
    checks.append(('aramaic provenance carries the fence '
                   '(ATTESTED, Imperial + Syriac strata, ONE fact '
                   'never two witnesses, mispar gadol unseated, '
                   'marks unpriced)',
                   p.startswith('ATTESTED') and 'Imperial' in p
                   and 'Syriac' in p and 'never two witnesses' in p
                   and 'mispar gadol' in p and 'prices none' in p,
                   p))
    return checks


def hangul_checks():
    """Verify the Hangul mint against its audit and its own laws.

    MECHANISM: the seat's self-test — the strata's shapes, the
    door's exhibits recomputed from the standard's decomposition,
    the teeth as stated (the doubles' prices against doublings;
    the digraphs' missing choseong forms), the null law and its
    parting from the raw bank, the annex's seats and refusals,
    and the fence. Kept beside aramaic_checks() rather than
    inside engine_checks(), so the controls stay comparable
    across seats. Parity against the audit's frozen transcription
    is proven separately by test_korean_parity.py at the
    repository root.
    """
    checks = []
    # 1. The strata's shape: three strata, seats 1..n each used
    #    exactly once, the merged bank disjoint by construction.
    shape = (len(HANGUL_INITIAL), len(HANGUL_VOWEL),
             len(HANGUL_FINAL), len(HANGUL))
    checks.append(('the strata: initial 19, vowel 21, final 27, '
                   'merged bank 67 keys; each stratum\'s values '
                   'are its seats 1..n exactly once',
                   shape == (19, 21, 27, 67)
                   and sorted(HANGUL_INITIAL.values())
                   == list(range(1, 20))
                   and sorted(HANGUL_VOWEL.values())
                   == list(range(1, 22))
                   and sorted(HANGUL_FINAL.values())
                   == list(range(1, 28)), shape))
    # 2. The door's founding exhibits, decomposed by the
    #    standard's law: 한글 (the witnesses' own syllable
    #    example) and 한국.
    r = hangul('한글')
    checks.append(('hangul() decomposes by the block law: '
                   '한글 == 52 (한 24 = ㅎ19+ㅏ1+ㄴ4; 글 28 = '
                   'ㄱ1+ㅡ19+ㄹ8), strata 20/20/12',
                   r['value'] == 52
                   and r['initial_subtotal'] == 20
                   and r['vowel_subtotal'] == 20
                   and r['final_subtotal'] == 12
                   and r['null_initials'] == 0,
                   (r['value'], r['initial_subtotal'],
                    r['vowel_subtotal'], r['final_subtotal'])))
    checks.append(('hangul() 한국 == 40 (한 24 + 국 16 = '
                   'ㄱ1+ㅜ14+ㄱ1)',
                   hangul('한국')['value'] == 40,
                   hangul('한국')['value']))
    # 3. The raw door agrees on text with no null: the conjoining
    #    spelling of 한 weighs its seats at weigh().
    checks.append(('weigh() reads the raw bank: the conjoining '
                   'spelling of 한 == 24 (19+1+4)',
                   weigh('\u1112\u1161\u11ab', 'hangul')['value']
                   == 24,
                   weigh('\u1112\u1161\u11ab', 'hangul')['value']))
    # 4. THE NULL LAW and its parting from the raw bank, printed:
    #    아이 at the door is 22 with two nulls counted; at the
    #    raw bank its spelling shows the seats (12+1 + 12+21).
    d = hangul('아이')
    raw = weigh('\u110b\u1161\u110b\u1175', 'hangul')['value']
    checks.append(('the null law: hangul(아이) == 22 with '
                   'null_initials 2; the raw bank shows 46 — the '
                   'two doors part at the zero, by design',
                   d['value'] == 22 and d['null_initials'] == 2
                   and raw == 46, (d['value'], d['null_initials'],
                                   raw)))
    # 5. THE TEETH — the doubles' prices against doublings: only
    #    ㄲ coincides with twice its base; the law is seats.
    seats = {g: HANGUL_INITIAL[_jamo_conjoining(g, 'CHOSEONG')]
             for g in 'ㄱㄲㄷㄸㅂㅃㅅㅆㅈㅉ'}
    doubles = (seats['ㄲ'] == 2 * seats['ㄱ'],
               seats['ㄸ'] == 2 * seats['ㄷ'],
               seats['ㅃ'] == 2 * seats['ㅂ'],
               seats['ㅆ'] == 2 * seats['ㅅ'],
               seats['ㅉ'] == 2 * seats['ㅈ'])
    checks.append(('the teeth: the tense doubles price by seat, '
                   'not by doubling — ㄲ 2 == 2×ㄱ alone; ㄸ 5, '
                   'ㅃ 9, ㅆ 11, ㅉ 14 against 8, 16, 20, 26',
                   doubles == (True, False, False, False, False),
                   (seats, doubles)))
    # 6. THE TEETH — the digraphs' refusal, at its exact
    #    coordinate: no digraph holds a MODERN initial seat.
    #    Seven have no choseong form at all; four (ㄵ ㄶ ㅀ ㅄ)
    #    keep only ARCHAIC Middle Korean cluster forms in the
    #    standard's block, which the modern stratum does not
    #    seat. Each digraph holds a final seat; a bare digraph
    #    weighs there.
    from .tables import _HANGUL_DIGRAPH_FINALS
    archaic = []
    for g in _HANGUL_DIGRAPH_FINALS:
        try:
            conj = _jamo_conjoining(g, 'CHOSEONG')
            if conj not in HANGUL_INITIAL:
                archaic.append(g)
        except ValueError:
            pass
    checks.append(('the teeth: all 11 final digraphs are refused '
                   'modern initial seats — 7 with no choseong '
                   'form at all, 4 (ㄵㄶㅀㅄ) with only archaic '
                   'cluster namesakes, unseated; a bare ㄳ weighs '
                   'at its final seat 3',
                   len(archaic) == 4
                   and hangul('ㄳ')['value'] == 3
                   and hangul('ㄳ')['final_subtotal'] == 3,
                   (archaic, hangul('ㄳ')['value'])))
    # 7. The modern refusals: the obsolete letters are unseated
    #    on the modern path and counted, never silent.
    d = hangul('ㆍ')
    checks.append(('the modern refusal: ㆍ is unseated on the '
                   'modern path (value 0, unseated 1)',
                   d['value'] == 0 and d['unseated'] == 1,
                   (d['value'], d['unseated'])))
    # 8. THE ANNEX: its shape (17/11/17), ㆍ at vowel seat 1,
    #    the annex's ㅇ at its seat (no null in 1446), and the
    #    modern-only signs refused there.
    shape = (len(HANGUL_1446_INITIAL), len(HANGUL_1446_VOWEL),
             len(HANGUL_1446_FINAL))
    a = hangul('ㆁㆍ', hist=True)
    checks.append(('the 1446 annex: strata 17/11/17; ㆁㆍ == 4 '
                   '(ㆁ at initial seat 3 + ㆍ at vowel seat 1); '
                   'annex ㅇ prices 15 (no null in the annex); '
                   'ㄲ is unseated there',
                   shape == (17, 11, 17) and a['value'] == 4
                   and hangul('ㅇ', hist=True)['value'] == 15
                   and hangul('ㄲ', hist=True)['unseated'] == 1,
                   (shape, a['value'],
                    hangul('ㅇ', hist=True)['value'])))
    # 9. The hinge at the door: a final ㅇ is a full letter —
    #    강 (ㄱ+ㅏ+ㅇ) weighs 1+1+21 with no null counted.
    d = hangul('강')
    checks.append(('the hinge: final ㅇ is a full letter — '
                   'hangul(강) == 23, final subtotal 21, no null',
                   d['value'] == 23 and d['final_subtotal'] == 21
                   and d['null_initials'] == 0,
                   (d['value'], d['final_subtotal'])))
    # 10. The fence: constructed, the negative and the teeth and
    #     the parting on its face.
    p = SYSTEMS['hangul']['provenance']
    checks.append(('hangul provenance carries the fence '
                   '(CONSTRUCTED, the checked negative, the '
                   'teeth, the hinge, the North parting)',
                   p.startswith('CONSTRUCTED')
                   and 'NO letter-numeral tradition' in p
                   and 'NOT doublings' in p
                   and 'North Korean' in p, p[:60]))
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
