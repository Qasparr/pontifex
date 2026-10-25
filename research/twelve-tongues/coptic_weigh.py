#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — coptic_weigh.py — the Coptic bank of the Twelve Tongues
# v0.1 "The Fourth Span" — worker #8 of 12 (COPTIC)
#
# Epigraph: "Do not unto another that which you would not have him do unto
# you. Thou needest this law alone. It is the foundation of all the rest."
# — Confucius, Analects XV.24. (The Golden Rule holds the scribe to the
# same audit the scribe applies: nothing guessed, nothing smoothed.)
#
# Thelemic date: ☉ in 18° 47′ Libra, ☽ in 21° 03′ Capricorn, dies solis,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are not. This research
# decrees no bridge. All findings go to his red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   HYPOTHESIS: Coptic, the Greek uncial alphabet augmented by seven
#     Demotic-derived letters, carried the Milesian letter-numeral system
#     into the Coptic manuscript tradition — with its own numeral-only
#     letters (ⲋ = 6, ϥ = 90, Ⳁ = 900) and five Demotic letters that have
#     no numeral value at all.
#   METHOD: weigh the shared corpus in Coptic script under a stated
#     Latin→Coptic transliteration convention (COPT-TRANS-v1); weigh with
#     the attested Coptic numeral values sourced from Wikipedia's
#     "Coptic alphabet" letter table, Dr. Kamal Farid Isaac (Institute
#     of Coptic Studies, Cairo), and the Unicode character names;
#     mark any letter without a sourced value UNKNOWN, never guessed.
#   OBSERVATION: the 24 Greek-origin letters hold their Milesian values
#     exactly (shared descent, not independent evidence); the Demotic
#     letters ⲋ/ϥ/Ⳁ hold 6/90/900; ϣ ϧ Ϩ ϫ ϭ ϯ have no numeral value.
#     Two corpus terms (HERU-RA-HA, ABRAHADABRA) contain ϩ and are
#     therefore unweighable in full — reported at full weight as
#     negative results.
#   RESULT: the weighings below, every sum recomputed by machine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Coptic bank.

DOCTRINE: attested tables are recorded as the traditions hand them down;
the scribe does not "improve" them. The Latin->Coptic transliteration is
the scribe's own (COPT-TRANS-v1) and is therefore CONSTRUCTED; the table
of letter values is ATTESTED — the Coptic alphabetic numeral system is a
living manuscript tradition (letters used as numerals, numerical use
marked by a continuous overline, per Wikipedia's "Coptic alphabet"
"Numerals" section), whose values follow the Greek Milesian system by
documented descent ("The numerical value of the letters is based on
Greek numerals", ibid.), and whose Coptic-specific slots are confirmed
by Dr. Kamal Farid Isaac, Institute of Coptic Studies, Cairo
(coptic-cairo.com): "The sixth letter [ⲋ] is not used as a letter, but
as a numeral whose value is 6 though most Greek letters were also used
as numerals." The 900-slot is filled by Ⳁ, whose Unicode name is
COPTIC CAPITAL LETTER SAMPI (U+2CC0), with Greek equivalent Ϡ/ϡ marked
"(numerical value)" in the Wikipedia letter table. ϥ = 90 (Greek
equivalent Ϙ/ϙ, "(numerical value)") — the Coptic letter that took the
koppa slot. The remaining Demotic letters (ϣ ϧ Ϩ ϫ ϭ ϯ, plus Akhmimic
Ⳉ/ⳉ) are recorded "—" in the numeric-value column: valueless in the
attested system. The scribe marks them UNKNOWN (not guessed).

PROVENANCE TIER: ATTESTED (table) — a living manuscript tradition of
letter-numerals — with Greek descent documented, not hidden. Script-form
transliterations are CONSTRUCTED (COPT-TRANS-v1).
"""

import csv

# -- Coptic letter-numeral table (ATTESTED) ------------------------------------
# MECHANISM: the 24 Greek-origin letters keep Milesian values; the three
# epissemone slots are filled Coptic-style: ⲋ (SOU, numeral-only) = 6,
# ϥ (FEI) = 90 in the koppa slot, Ⳁ (SAMPI) = 900. The other Demotic
# letters carry no numeral value — they are absent from this dict, so any
# script form containing them fails closed to UNKNOWN.
# DOCTRINE: the scribe records the tradition's table, not a better one.
COPTIC = {
    'ⲁ': 1, 'ⲃ': 2, 'ⲅ': 3, 'ⲇ': 4, 'ⲉ': 5, 'ⲋ': 6, 'ⲍ': 7, 'ⲏ': 8,
    'ⲑ': 9, 'ⲓ': 10, 'ⲕ': 20, 'ⲗ': 30, 'ⲙ': 40, 'ⲛ': 50, 'ⲝ': 60,
    'ⲟ': 70, 'ⲡ': 80, 'ϥ': 90, 'ⲣ': 100, 'ⲥ': 200, 'ⲧ': 300,
    'ⲩ': 400, 'ⲫ': 500, 'ⲭ': 600, 'ⲯ': 700, 'ⲱ': 800, 'Ⳁ': 900,
}

# -- COPT-TRANS-v1: Latin -> Coptic transliteration (CONSTRUCTED) -------------
# MECHANISM: greedy digraphs first (TH->ⲑ, SH->ϣ, CH->ⲭ), then a plain
# letter map. Choices stated, never silent:
#   V->ⲃ (Latin V is the consonant b/v; ⲃ covers b~v~w across dialects;
#          the vowel reading U->ⲟⲩ is the digraph ⲟⲩ = /u/,/w/)
#   X->ⲝ (dedicated letter, /ks/ in Greek loanwords; our terms are foreign)
#   F->ϥ (dedicated Demotic letter — consequence: 90-slot letter in play)
#   H->ϩ (dedicated Demotic letter — consequence: ϩ is valueless, so any
#          term containing H fails closed to UNKNOWN, partial sum reported)
#   J->ϫ (dedicated letter), Q->ⲕ (no q letter; c/k/q merge), C->ⲕ,
#   Y->ⲓ (i-sound; Y->ⲩ weighed as variant), U/W->ⲟⲩ digraph.
# DOCTRINE: the map is mechanical and letter-level (like the Latin->Hebrew
# map in pontifex/tables.py); phonetic cleverness is not smuggled in.
DIGRAPHS = {'th': 'ⲑ', 'sh': 'ϣ', 'ch': 'ⲭ'}
LETTER_MAP = {
    'a': 'ⲁ', 'b': 'ⲃ', 'c': 'ⲕ', 'd': 'ⲇ', 'e': 'ⲉ', 'f': 'ϥ',
    'g': 'ⲅ', 'h': 'ϩ', 'i': 'ⲓ', 'j': 'ϫ', 'k': 'ⲕ', 'l': 'ⲗ',
    'm': 'ⲙ', 'n': 'ⲛ', 'o': 'ⲟ', 'p': 'ⲡ', 'q': 'ⲕ', 'r': 'ⲣ',
    's': 'ⲥ', 't': 'ⲧ', 'u': 'ⲟⲩ', 'v': 'ⲃ', 'w': 'ⲟⲩ', 'x': 'ⲝ',
    'y': 'ⲓ', 'z': 'ⲍ',
}


def transliterate(latin):
    # MECHANISM: lowercase, strip hyphens (separators, not letters — dropped,
    # not zeroed, per the Greek worker's convention), greedy digraph pass.
    s = latin.lower().replace('-', '')
    out, i = '', 0
    while i < len(s):
        dig = s[i:i + 2]
        if dig in DIGRAPHS:
            out += DIGRAPHS[dig]
            i += 2
        else:
            out += LETTER_MAP[s[i]]
            i += 1
    return out


def weigh(script_form):
    # MECHANISM: additive, Milesian-style. If ANY letter is valueless in
    # the attested table, the weighing fails closed: value UNKNOWN, with
    # the partial sum of the weighable letters reported for the record.
    # DOCTRINE: a letter whose value cannot be sourced is UNKNOWN, never
    # guessed — so a term carrying one is UNKNOWN, never smoothed.
    total, unknown, partial = 0, [], 0
    for ch in script_form:
        if ch in COPTIC:
            total += COPTIC[ch]
            partial += COPTIC[ch]
        else:
            unknown.append(ch)
    if unknown:
        return 'UNKNOWN', partial, unknown
    return total, None, []


# -- The weighings -------------------------------------------------------------
# Each row: (term, script_form_override_or_None, convention, mergers, notes)
# A None override means "mechanical COPT-TRANS-v1 transliteration".
CORPUS = [
    ('AXONEME', None, 'COPT-TRANS-v1',
     'X->xi chosen over chi; epsilon/mu/omicron/nu single renderings',
     'Primary weighing.'),
    ('OZ', None, 'COPT-TRANS-v1',
     'no mergers fired',
     'TARGET 77 hit.'),
    ('TRVVTH', None, 'COPT-TRANS-v1',
     'V->beta each (Latin V as consonant b/v); TH->theta absorbs th',
     'Primary weighing. V->ou (vowel) variant weighed separately (1349).'),
    ('THELEMA', None, 'COPT-TRANS-v1',
     'TH->theta; both Es as epsilon (epsilon/eta merger)',
     'Mechanical rendering: 90, NOT the classic 93. '
     'Greek-aware spelling (eta) weighed separately (93).'),
    ('AGAPE', None, 'COPT-TRANS-v1',
     'no mergers fired; final E as epsilon',
     'Mechanical rendering: 90. Greek-aware spelling (eta) weighed '
     'separately (93). COLLISION with mechanical THELEMA at 90.'),
    ('BABALON', None, 'COPT-TRANS-v1',
     'B->beta, O->omicron',
     'Weighed with omicron per the corpus spelling.'),
    ('HERU-RA-HA', None, 'COPT-TRANS-v1',
     'hyphen dropped, not zeroed; U->ou digraph',
     'NEGATIVE RESULT: contains ϩ (HORI), which has no numeral value in '
     'the attested system — the term is UNKNOWN. Partial sum of the '
     'weighable letters reported, not a total.'),
    ('ABRAHADABRA', None, 'COPT-TRANS-v1',
     'H->hori each',
     'NEGATIVE RESULT: contains ϩ (HORI), valueless — term UNKNOWN. '
     'The Hebrew 418 bridge does not cross on the Coptic bank. '
     'Partial sum reported, not a total.'),
    ('QIRA', None, 'COPT-TRANS-v1',
     'Q->kappa (merger: c/q/k collapse)',
     ''),
    ('LIBERTY', None, 'COPT-TRANS-v1',
     'Y->iota chosen (i-sound); B->beta',
     'Primary weighing. Y->upsilon variant weighed separately (847).'),
    ('CELL', None, 'COPT-TRANS-v1',
     'C->kappa (merger: c/k collapse)',
     'Coptic 85 vs canonical English-ordinal 32 — no bridge. '
     'Negative result, reported at full weight.'),
    # -- variants: alternative readings, honestly labelled ------------------
    ('AXONEME [X->chi variant]', 'ⲁⲭⲟⲛⲉⲙⲉ', 'COPT-TRANS-v1 variant',
     'X->chi instead of xi',
     'ANTI-HIT recorded: 771 is near 777 but IS NOT 777. '
     'Wish-reading flagged; the miss stands.'),
    ('TRVVTH [V->ou variant]', 'ⲧⲣⲟⲩⲟⲩⲑ', 'COPT-TRANS-v1 variant',
     'V->ou each (vowel reading; the Roman V-for-U)',
     'Alternate reading of the Roman V.'),
    ('THELEMA [Greek-aware]', 'ⲑⲉⲗⲏⲙⲁ', 'authentic Greek spelling',
     'TH->theta; second E is eta in the real word',
     'The authentic word-form: 93, the classic value — reached on the '
     'Coptic bank too. TARGET-adjacent (93 is a target number). '
     'COLLISION with Greek-aware AGAPE at 93.'),
    ('AGAPE [Greek-aware]', 'ⲁⲅⲁⲡⲏ', 'authentic Greek spelling',
     'final E is eta in the real word',
     'The authentic word-form. TARGET 93 hit. COLLISION with '
     'Greek-aware THELEMA at 93 (see log).'),
    ('LIBERTY [Y->upsilon variant]', 'ⲗⲓⲃⲉⲣⲧⲩ', 'COPT-TRANS-v1 variant',
     'Y->upsilon (Greek u-sound); B->beta',
     'Alternate reading of Y.'),
    ('עז [transliterated]', 'ⲟⲍ', 'transliteration of the Hebrew term',
     'ayin->omicron, zayin->zeta: the Phoenician-derived numeral order '
     'survives on both banks',
     'Cross-bank reference row (cf. the Greek worker): TARGET 77 hit. '
     'The canonical bridge AXONEME=77=עז holds on the Coptic bank because '
     '70=70 and 7=7 in the shared Milesian order — ATTESTED on ATTESTED.'),
]

TABLE_USED = ('ATTESTED Coptic alphabetic numerals '
              '(ⲁ=1…ⲱ=800; ⲋ=6 numeral-only; ϥ=90; Ⳁ=900) — sources: '
              'Wikipedia "Coptic alphabet" letter table; Dr. Kamal Farid '
              'Isaac, Institute of Coptic Studies, Cairo (coptic-cairo.com); '
              'Unicode U+2CC0 named COPTIC CAPITAL LETTER SAMPI')


def main():
    # MECHANISM: weigh every row, print the letter-by-letter sums for the
    # record, and emit the CSV the parent agent will synthesize.
    rows = []
    print('=== COPTIC BANK — letter-by-letter weighings ===')
    for term, override, conv, mergers, notes in CORPUS:
        form = override if override is not None else transliterate(term)
        value, partial, unknown = weigh(form)
        # the letter-by-letter record
        parts = []
        for ch in form:
            v = COPTIC.get(ch, 'UNKNOWN')
            parts.append('%s=%s' % (ch, v))
        print('%s  %s' % (term, form))
        print('   ' + ' + '.join(parts) + '  =>  ' + str(value)
              + ('' if value != 'UNKNOWN'
                 else '   [unweighable: %s; partial=%d]'
                 % (','.join(sorted(set(unknown))), partial)))
        if value == 'UNKNOWN':
            tier = ('ATTESTED (table); script-form CONSTRUCTED — '
                    'term contains unweighable letter(s)')
            val_cell = 'UNKNOWN'
            notes = notes + ' [partial sum of weighable letters: %d]' % partial
        else:
            tier = 'ATTESTED (table); script-form CONSTRUCTED'
            val_cell = str(value)
        rows.append({
            'term': term, 'language': 'Coptic', 'script_form': form,
            'transliteration_convention': conv, 'table_used': TABLE_USED,
            'provenance_tier': tier, 'value': val_cell,
            'mergers_or_loss': mergers, 'notes': notes,
        })
    out = '/home/hatch/workspace/pontifex/research/twelve-tongues/coptic-values.csv'
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('\nCSV written: %s (%d rows)' % (out, len(rows)))


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
