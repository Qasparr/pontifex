#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — tables.py — the value tables and the transliteration maps
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
#   (The full statement stands in pontifex/engine.py; this module carries the
#   tables the method weighs with, recorded as the traditions hand them down.)
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The value tables.

DOCTRINE: attested tables are recorded as the traditions hand them down;
the scribe does not "improve" them. Anything the scribe builds is marked
CONSTRUCTED where it is registered (see pontifex/engine.py).
"""

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


def _braille_table():
    # MECHANISM: build programmatically — the Unicode order IS the table.
    # DOCTRINE: constructed — transparent and consistent, never a discovery.
    # Its purpose is as a lossless *carrier*: 64 patterns swallow most
    # alphabets whole, so transliteration into braille preserves distinctions
    # that Hebrew's 22 letters would merge. Charted because the tool's purpose
    # is precisely universal charting.
    # NOTE: patterns 1..26 correspond to a-z in standard braille by design.
    return {chr(0x2800 + i): i + 1 for i in range(64)}


# -- Braille, 64 dot-patterns (CONSTRUCTED) ---------------------------------
BRAILLE = _braille_table()

# -- Hebrew fallback: Latin → Hebrew transliteration (CONSTRUCTED map) ------
# MECHANISM: the default map for tongues with no table of their own (academic
# style, greedy digraphs). Every merger is documented in MERGERS so the loss
# is visible, never hidden.
# DOCTRINE: Hebrew is the proper fallback because the correspondence engine
# is Hebrew-rooted — bridges must land in the system where the
# correspondences live. (Settled with the author, 2026-10-07.)
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

# -- Japanese kana, THE GOJŪON MINT (CONSTRUCTED — house coinage, RATIFIED) --
# ---------------------------------------------------------------------------
# PROVENANCE — READ BEFORE EVERY OTHER BANK'S HABIT. Every bank above is
# an ATTESTED copy, recorded as the tradition hands it down; the scribe
# records and does not revise. THIS BANK IS NOT. It is a CONSTRUCTION,
# coined at the desk under the founder's commission for the project
# Complete the Tables in Japanese (Phase III: the gojūon mint), founded
# as a proposal on 2026-11-12 (XII day of November, Dies Jovis, Anno
# V:xii e.n.) and RATIFIED by the founder's stamp on 2026-11-13 (XIII
# day of November, Dies Veneris): "Stamp the mint — the Tables stand."
# From that ratification it is doctrine — the founder's mint, 2026 —
# and it must not be cited as attested, traditional, or ancient: no
# kana letter-value bank is attested before the 21st century, and this
# one is dated 2026 on its face. (The gate verdict of record, THE
# JAPANESE TABLES (MAGVS): the mint DOES NOT FAIL as the founder's
# coinage; it FAILS as any claim of antiquity, at the same size, in
# the same breath.) Source of record: THE-JAPANESE-TABLES-MAGVS.md —
# Phase I (audit of the modern banks), Phase II (the rōmaji seam),
# Phase III (the mint). The seat below is generated from the same grid
# data, by the same construction, as the mint's first engine seat in
# tools/ptk/weigh.py; parity between the two seats is proven by
# test_kana_parity.py at the repository root, not asserted here.
#
# DOCTRINE — THE SEVEN RULINGS (reasoning in full in the Phase III
# instrument and the MAGVS volume; the gap numbers are Phase I §VI's):
#   G1 THE AXIS: gojūon positional, row-major in the spoken column
#      order a-i-u-e-o (あ=1, い=2, う=3, え=4, お=5, か=6 …). The grid
#      seats 47 (the や row's yi/ye cells and the わ row's wu cell are
#      holes — no kana, no seat); ゐ・ゑ hold their grid seats (45, 46)
#      as ARCHIVAL seats; を=47; ん, the hatsuon outside the fifty,
#      takes the next seat, 48 — ONE value. Dual values are refused
#      bank-wide (against Fukada's ン 1-or-10: a sign with two values
#      is a fork in every sum it enters).
#   G2 DAKUTEN LAW: continuation ON THE MINT'S OWN AXIS. No derived
#      diacritic constant holds, and a constant chosen anyway would
#      be invented, not derived — so the voiced rows take the next
#      seats after the base inventory entire, in the grid's printed
#      dakuten order: が行 49–53, ざ行 54–58, だ行 59–63, ば行 64–68,
#      ぱ行 69–73. Subtraction (Yoshino) is refused: it drives totals
#      negative, which no house bank admits.
#   G3 CHŌON LAW: the mark ー is an operator, not a sign: it weighs
#      the seat value of the vowel it lengthens (かー → あ's 1;
#      とー → お's 5). Length is a second mora OF THAT VOWEL, against
#      Yoshino's ー=0, which erases what the spelling declares. Length
#      spelled with a vowel kana (おう, えい) is weighed as written
#      (G6's fence); the seam that opens is exhibited in the Phase III
#      instrument, not hidden — and not closed here.
#   G4 YŌON LAW: a small kana weighs at its full-size form's seat
#      (ゃ=ヤ 36, ゅ=ユ 37, ょ=ヨ 38; small vowels likewise; ゎ, ゕ,
#      ゖ by the same law).
#   G5 SOKUON LAW: っ/ッ weighs at つ/ツ's seat, 18 — its full-size
#      form. The geminate mora is a full beat of blockage, not
#      silence.
#   G6 DEVOICING: the bank weighs the WRITTEN sign. Devoicing is
#      phonology and belongs to the performance register (the Divine
#      Nine vocal tool); it has no mechanic here, and the fence is
#      declared, not silent.
#   G7 REDUCTION: totals stand raw; digit-reduction rides beside,
#      never instead.
#
# MECHANISM: the bank is generated from the grid rows below so the
# table printed in the doctrine and the table in this engine are one
# object, not two copies that can drift. Columns run a-i-u-e-o; a
# sign's value is its sequence position; its column gives the vowel a
# following ー weighs. Katakana is generated from hiragana by the
# Unicode block offset (+0x60): one sign, two dresses — あ and ア
# share a seat by construction.
_KANA_GRID = [
    ('あ', 'い', 'う', 'え', 'お'),
    ('か', 'き', 'く', 'け', 'こ'),
    ('さ', 'し', 'す', 'せ', 'そ'),
    ('た', 'ち', 'つ', 'て', 'と'),
    ('な', 'に', 'ぬ', 'ね', 'の'),
    ('は', 'ひ', 'ふ', 'へ', 'ほ'),
    ('ま', 'み', 'む', 'め', 'も'),
    ('や', None, 'ゆ', None, 'よ'),   # holes: yi, ye — no kana, no seat
    ('ら', 'り', 'る', 'れ', 'ろ'),
    ('わ', 'ゐ', None, 'ゑ', 'を'),   # hole: wu; ゐ・ゑ ARCHIVAL seats
]

_KANA_DAKUTEN_ROWS = [
    ('が', 'ぎ', 'ぐ', 'げ', 'ご'),
    ('ざ', 'じ', 'ず', 'ぜ', 'ぞ'),
    ('だ', 'ぢ', 'づ', 'で', 'ど'),
    ('ば', 'び', 'ぶ', 'べ', 'ぼ'),
    ('ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'),
]

# MECHANISM: small kana seated by law, at their full-size partners'
# seats — ゃゅょ and the small vowels by G4, ゎ・ゕ・ゖ by G4's same
# law extended to the small forms the modern script still writes,
# っ by G5 (the sokuon is listed here because its seat is a law,
# not a grid position).
_KANA_SMALL_PARTNER = {
    'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お',
    'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ',
    'ゎ': 'わ', 'ゕ': 'か', 'ゖ': 'け',
    'っ': 'つ',
}


def _build_kana():
    """MECHANISM: seat the grid row-major (a-i-u-e-o), then ん, then
    the dakuten block; record each sign's column-vowel seat value for
    the ー operator (G3); seat the small kana at their partners
    (G4/G5); mirror every seat into katakana by the block offset.
    Returns (bank, vowel_map, base_signs) — base_signs is the seated
    inventory in seating order (the 73), exported so the audit can
    prove values 1–73 are each used exactly once across it. ん and
    っ have no vowel: a ー after them weighs 0."""
    bank, vowel, base = {}, {}, []
    n = 0

    def seat(rows):
        nonlocal n
        for row in rows:
            for col, ch in enumerate(row):
                if ch is None:
                    continue
                n += 1
                bank[ch] = n
                vowel[ch] = col + 1  # あ=1 い=2 う=3 え=4 お=5 by column
                base.append(ch)

    # MECHANISM: seating order is the rulings' order — the grid (G1),
    # then ん at the next seat (G1), then the dakuten block after the
    # base inventory entire (G2). The order is load-bearing: seat
    # the dakuten rows before ん and every voiced value shifts by
    # one — the kana self-test's むげつ case guards exactly this.
    seat(_KANA_GRID)
    n += 1
    bank['ん'] = n  # G1: the hatsuon after the grid — seat 48
    base.append('ん')
    seat(_KANA_DAKUTEN_ROWS)
    for small, partner in _KANA_SMALL_PARTNER.items():
        bank[small] = bank[partner]
        vowel[small] = vowel[partner]
    # MECHANISM: the sokuon carries a seat (G5) but no vowel — its
    # partner's vowel is not inherited, so a ー after っ weighs 0.
    vowel.pop('っ', None)
    for ch in list(bank):
        kata = chr(ord(ch) + 0x60)
        bank[kata] = bank[ch]
        if ch in vowel:
            vowel[kata] = vowel[ch]
    return bank, vowel, base


KANA, KANA_VOWEL, KANA_BASE = _build_kana()
# DOCTRINE: ー (U+30FC) is deliberately NOT a key of KANA — it is an
# operator (G3) and only engine.kana() may read it. A raw
# weigh(word, 'kana') therefore skips it, and the skip is visible in
# the breakdown; that visibility is intended. The long-vowel seam
# (G3/G6) stands exhibited in the doctrine; this seat does not close
# it and does not alter any value.

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
