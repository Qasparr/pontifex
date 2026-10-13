#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — twelve tongues: ARMENIAN bank — the weighing script
# Worker #11 (ARMENIAN), 2026-10-11
#
# Epigraph: "Measure what is measurable, and make measurable what is not
# so." — attributed to Galileo Galilei.
#
# Thelemic date: dies Solis, ☉ in Libra, ☽ in Capricorn, Anno V:xii e.n.
# (2026-10-11 e.v.)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's.
# Transliteration map: CONSTRUCTED by the scribe — proposal for the red pen.
# Numeric table: ATTESTED, the tradition's own (see provenance note in
# armenian.md). A value built on an attested table through a constructed map
# is reported as ATTESTED-table/CONSTRUCTED-map.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   HYPOTHESIS: Classical Armenian letters carry alphabetic numeral values in
#   the Mashtots order, usable to weigh the shared corpus.
#   METHOD: weigh each corpus term through the ATTESTED table via the scribe's
#   stated transliteration map; record every merger, loss, and alternative.
#   OBSERVATION: letter-by-letter sums below (printed verbatim by this script).
#   RESULT: none of the eleven terms land on a target number; the Greek
#   scheme is an analogy, not a parallel table (see armenian.md).
#   The scribe reports, never decrees. Findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The Armenian bank: weigh the shared corpus in classical Armenian letters.

DOCTRINE: the table is recorded as the tradition hands it down; the scribe
does not "improve" it. The transliteration map is the scribe's construction,
stated in full, and every judgment call is flagged.
"""

# -- Armenian alphabetic numerals (ATTESTED) --------------------------------
# MECHANISM: the table as handed down — Wikipedia "Armenian numerals" (citing
# omniglot, Shaw 1939, Ifrah 2000, Chrisomalis 2010 CUP), cross-checked
# against the Armenian alphabet article and the MELA cataloging manual
# (manuscript era-dating use, e.g. ՌՋՀԵ = 1975). Values 1..9000 over the
# 36 classical letters; Օ=10000 and Ֆ=20000 are late additions (13th c.,
# "sometimes have a numerical value assigned" per Wikipedia) — recorded with
# that caveat, marked (late) below.
# DOCTRINE: this system is the tradition's own, used in Armenian manuscript
# colophons — ATTESTED, not derived. Its letter mapping is independent of
# Greek (see armenian.md §5), even though the ciphered-additive principle is
# the same as in the Greek and Hebrew systems (Wikipedia, Armenian numerals).
ARMENIAN = {
    'ա': 1, 'բ': 2, 'գ': 3, 'դ': 4, 'ե': 5, 'զ': 6, 'է': 7, 'ը': 8, 'թ': 9,
    'ժ': 10, 'ի': 20, 'լ': 30, 'խ': 40, 'ծ': 50, 'կ': 60, 'հ': 70,
    'ձ': 80, 'ղ': 90,
    'ճ': 100, 'մ': 200, 'յ': 300, 'ն': 400, 'շ': 500, 'ո': 600,
    'չ': 700, 'պ': 800, 'ջ': 900,
    'ռ': 1000, 'ս': 2000, 'վ': 3000, 'տ': 4000, 'ր': 5000, 'ց': 6000,
    'ւ': 7000, 'փ': 8000, 'ք': 9000,
    'օ': 10000,  # (late) — 13th-century addition, "sometimes assigned"
    'ֆ': 20000,  # (late) — 13th-century addition, "sometimes assigned"
}

# -- Scribe's transliteration map (CONSTRUCTED) ------------------------------
# MECHANISM: graphemic (letter-for-letter), classical letters preferred.
# Every judgment call is numbered and explained in armenian.md §3.
#   T1: TH -> թ (the aspirated-t letter; parallel to the Greek bank's θ).
#   T2: O  -> ո (classical; the later օ=10000 is NOT used — a 10000-valued
#       letter in every O would drown the weighing; alternative recorded).
#   T3: U  -> ու digraph (600+7000; classical Armenian writes /u/ so; heavy).
#   T4: V  -> վ (graphemic; V in TRVVTH stands for U — phonemic alt. ու noted).
#   T5: X  -> խ (single letter; the /ks/ is collapsed — loss recorded).
#   T6: C  -> կ (k-origin; /s/ before e/i merged — loss recorded).
#   T7: K  -> կ (merges with C — loss recorded).
#   T8: Q  -> ք (alternative ղ noted).
#   T9: W  -> ւ (the /w/ letter).
#   T10: J -> ջ. CH -> չ, SH -> շ, PH -> փ (digraphs where English has them).
#   T11: hyphens dropped; word read straight through.
MAP = {
    'A': 'ա', 'B': 'բ', 'C': 'կ', 'D': 'դ', 'E': 'ե', 'F': 'ֆ', 'G': 'գ',
    'H': 'հ', 'I': 'ի', 'J': 'ջ', 'K': 'կ', 'L': 'լ', 'M': 'մ', 'N': 'ն',
    'O': 'ո', 'P': 'պ', 'Q': 'ք', 'R': 'ր', 'S': 'ս', 'T': 'տ', 'U': 'ու',
    'V': 'վ', 'W': 'ւ', 'X': 'խ', 'Y': 'յ', 'Z': 'զ',
    'TH': 'թ', 'CH': 'չ', 'SH': 'շ', 'PH': 'փ',
}


def transliterate(term):
    # MECHANISM: greedy digraphs (TH/CH/SH/PH) first, then single letters;
    # hyphens are separators, dropped per T11.
    # DOCTRINE: the map is stated, not smuggled — the reader can replay it.
    out, i, t = [], 0, term.upper().replace('-', '')
    while i < len(t):
        if t[i:i + 2] in ('TH', 'CH', 'SH', 'PH'):
            out.append(MAP[t[i:i + 2]])
            i += 2
        else:
            out.append(MAP[t[i]])
            i += 1
    return ''.join(out)


def weigh(term):
    # MECHANISM: sum the ATTESTED value of each transliterated letter.
    # Raises KeyError rather than guessing if a letter is missing —
    # an unsourced letter is UNKNOWN, never invented.
    script = transliterate(term)
    parts = [(ch, ARMENIAN[ch]) for ch in script]
    return script, parts, sum(v for _, v in parts)


CORPUS = ['AXONEME', 'OZ', 'TRVVTH', 'THELEMA', 'AGAPE', 'BABALON',
          'HERU-RA-HA', 'ABRAHADABRA', 'QIRA', 'LIBERTY', 'CELL']
TARGETS = (418, 666, 777, 93, 77, 11)


def main():
    print('ARMENIAN BANK — letter-by-letter weighings')
    print('(table ATTESTED / transliteration map CONSTRUCTED)')
    print('=' * 64)
    hits = []
    for term in CORPUS:
        script, parts, total = weigh(term)
        detail = ' + '.join(f'{ch}={v}' for ch, v in parts)
        print(f'{term:12s} {script}')
        print(f'{"":12s} {detail} = {total}')
        if total in TARGETS:
            hits.append((term, total))
        print('-' * 64)
    print('TARGET-NUMBER HITS:', hits if hits else 'NONE — negative result, '
          'reported with the same weight as a positive.')


if __name__ == '__main__':
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
