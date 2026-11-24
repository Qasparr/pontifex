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

# -- Ge'ez: THE HALEHAME WITNESS and THE GE'EZ MINT (two banks, one builder) -
# ---------------------------------------------------------------------------
# PROVENANCE — TWO BANKS, TWO DIFFERENT HONESTIES. Read both fences
# before either bank's habit.
#
# THE WITNESS (HALEHAME) is a SOURCED FOLK TABLE: the Debtera
# (halehame) enumeration of the Ethiopian debtera, transcribed from
# geez.org, "Numerology" (read entire, 2026-11-24) and corroborated
# independently by Ayele Bekerie, Ethiopic, An African Writing
# System (1997), via Peter T. Daniels' H-Net review — endpoints
# h = 1 … p = 800, multiplier examples hu = 2, lu = 4, po = 5600.
# Its first-form values are SOURCED 26 of 26 and recompute exact
# against the class law (units 1–10, tens 11–19, hundreds 20–26);
# its worked example ክርስቶስ = 80 is the tradition's own. Three
# caveats ride on its face, at the same size as its values: (1) the
# multiplier grid (a form at order n worth n × its base) is
# PRINTED entire in the source but its use is UNEXHIBITED — both
# scholarly witnesses agree worked examples use first forms only;
# (2) the practice's antiquity is UNDATED in every source read —
# no manuscript exemplar was sourced; (3) its register is
# folk-magical, expressly NOT liturgical. By the founder's ruling
# of 2026-11-24 under his END-GOAL RULE ("do the best for the end
# goal always"), halehame stands as WITNESS beside the mint —
# calibration, not the bank: it values 26 first forms of 202
# classical signs, and its labiovelar columns carry no value in
# any source (the audit's GAP rows), so it cannot carry the
# engine's weighing surface. It is NOT the house's coinage, and
# the mint's arrival corrects NOTHING in it: the folk ×6 at
# order 6 stands in this bank unaltered, forever (seam rule S4).
#
# THE MINT (GEEZ) is a CONSTRUCTION — house coinage, minted at
# the desk on 2026-11-24 under the founder's HYBRID LAW of the
# same morning (the Divine Nine seats on the fidäl by the
# tongue's own fusion devices) and under his three standing
# rules: chart the road through where one exists; PROOF-ENOUGH
# (what passes its tests and the full tower audit stands
# approved by his word); and the END-GOAL RULE, under which
# every fork below was decided at the desk — marked DESK
# RULINGS, revisable by his pen, never his words. No stamp is
# claimed for this bank beyond that proof: it stands if its
# batteries pass, and it must not be cited as attested,
# traditional, or ancient — liturgical Ge'ez has no letter
# values, and this bank is dated 2026 on its face. Source of
# record: THE-GEEZ-TABLES-PHASE-I-AUDIT.md (the inventory, the
# halehame audit, the Nine seating design) and THE-GEEZ-TABLES-
# PHASE-II-III-THE-SEAM-AND-THE-MINT.md (the seam protocol,
# the axis law and its failed candidates, the calibration).
# Parity between this seat and the Phase I audit's data is
# proven by test_geez_parity.py at the repository root.
#
# DOCTRINE — THE MINT'S RULINGS (reasoning in full in the
# Phase II–III instrument; the Phase I audit's §VII questions
# are answered at M3 and M5):
#   M1 THE AXIS: value(sign) = first-form value of its base ×
#      m(order), where m(order) = the order's own number — the
#      folk multiplier, the tongue's only printed axis — with
#      ONE correction: m(6) = 0 (M3). The failed candidates
#      stand printed in the instrument: the pure folk axis
#      (fails M3's declaration), the positional axis (fails
#      M2's calibration), the additive constant (no derivation
#      holds — two attempts printed failing, on the kana G2
#      pattern), Greek-station multipliers and station
#      additives (a transfer of Milesian values into a foreign
#      bank, and a merger of the citation column into the
#      first-form column besides).
#   M2 CALIBRATION BY CONSTRUCTION: the mint's first-form
#      column IS halehame — the 26 first-form values seated
#      exactly as the folk table gives them, so the mint's
#      first-form reading of ክርስቶስ is 80 by identity, not
#      by approximation. The witness calibrates the mint at
#      its first column; everywhere else the mint reads by
#      its own axis and the deltas print (seam rule S3).
#   M3 THE ORDER-6 DECLARATION (Phase I Q3, settled by the
#      end-goal rule): the mint obeys the KEY's station
#      reading at order 6 — the Zero seat — not the folk
#      multiplier. Every order-6 sign weighs 0 in the mint
#      (30 signs: 26 grid + 4 labiovelar). The folk ×6 stands
#      unaltered in the witness; the coordinate (order 6:
#      key 0, folk ×6) is the seam's boundary, printed at
#      its head. A Ge'ez weighing must declare its bank
#      (seam rule S1) precisely because the banks part here.
#   M4 THE LABIOVELAR COLUMN: the 20 classical labiovelar
#      signs — the tongue's own fusion device, consonant + ʷ
#      in one glyph, carrying the Nine's ΟΥ station — are
#      seated in the mint at their orders {1,3,4,5,6} under
#      the same axis law (no u-form, no o-form exist: the
#      glide absorbs them). The witness seats NONE of them:
#      its GAP stands beside the mint's column, printed.
#   M5 THE ΕΙ COLUMN (Phase I Q2, settled by the end-goal
#      rule): ΕΙ seats at the grid's eighth slot, generalized
#      — the only candidate that is a COLUMN (25 of 26 bases;
#      the labiovelar i-forms reach 4 bases and already carry
#      order 3's Ι seat, and a sign holds one seat). ዐ alone
#      has no eighth glyph — the standard leaves its slot
#      unassigned — so ዐ's ΕΙ cell is a HOLE: no glyph, no
#      seat, printed as a hole (the kana yi/ye precedent).
#      m(8) = 8 by the axis law's own arithmetic: the folk
#      multipliers ARE the order numbers at every printed
#      coordinate, so the eighth order's multiplier is 8
#      without a new constant entering. The correction set
#      of the whole law is exactly {6}.
#   M6 THE NINE IN THE MINT: the Nine names STATIONS; the
#      axis law prices ORDERS; the registers do not convert.
#      Order 6 is the one coordinate where name and price
#      coincide (station ZERO, multiplier 0). Order 8's
#      station is ΕΙ (Milesian 15, a Greek value, living in
#      the Greek bank) while its price is ×8 (an order
#      number) — the mint weighs no sign at 15 for ΕΙ's sake.
#      Η and Ω take no seat in the mint either: the fidäl
#      marks no vowel length, and the mint does not invent
#      what the audit printed as a gap.
#   M7 REDUCTION AND SINGLENESS: totals stand raw; every
#      sign carries exactly ONE value — the bank is a plain
#      dict, so a dual value is not merely ruled out, it is
#      unrepresentable in the instrument (the kana gate's
#      form, carried over).
#
# MECHANISM: ONE builder seats both banks from one base list,
# so the seam between them is mechanical, not editorial: the
# banks share the inventory and the first-form column entire,
# and differ by exactly (a) the multiplier at order 6, (b)
# coverage — the witness seats the 182 grid signs only; the
# mint seats those, the 20 labiovelars, and the 25 eighth-slot
# glyphs of the ΕΙ column (227 keys). Glyphs are generated by
# codepoint arithmetic on the audit's verified frame: each
# classical series occupies consecutive codepoints (order n
# at base + n − 1, the eighth slot at base + 7); the
# labiovelar series sit at offsets {1:0, 3:2, 4:3, 5:4, 6:5}
# from their series heads — offset +1 is unassigned in the
# standard precisely because the u-form does not exist.
_GEEZ_BASES = [
    ('ሀ', 1), ('ለ', 2), ('ሐ', 3), ('መ', 4), ('ሠ', 5), ('ረ', 6),
    ('ሰ', 7), ('ቀ', 8), ('በ', 9), ('ተ', 10), ('ኀ', 20), ('ነ', 30),
    ('አ', 40), ('ከ', 50), ('ወ', 60), ('ዐ', 70), ('ዘ', 80), ('የ', 90),
    ('ደ', 100), ('ገ', 200), ('ጠ', 300), ('ጰ', 400), ('ጸ', 500),
    ('ፀ', 600), ('ፈ', 700), ('ፐ', 800),
]

# MECHANISM: the classical labiovelar series heads and the base
# consonant whose first-form value prices them. The two
# post-classical series Unicode encodes (of ቐ, of ኸ) are NOT
# seated: the audit's field is the classical inventory, and the
# post-classical signs stand inventoried in the audit's data,
# unseated here — marked, not vanished.
_GEEZ_LABIOVELAR_HEADS = [
    ('ቈ', 'ቀ'), ('ኈ', 'ኀ'), ('ኰ', 'ከ'), ('ጐ', 'ገ'),
]
_GEEZ_LABIOVELAR_OFFSETS = {1: 0, 3: 2, 4: 3, 5: 4, 6: 5}

# MECHANISM: ዐ (Ayin) is the one classical base whose eighth
# slot the standard leaves unassigned (U+12D7) — the audit
# verified 25 of 26 slots filled against the Unicode standard.
# The hole is named here so the builder prints a hole, not a
# guess; test_geez_parity.py holds the exception against
# unicodedata and the audit's inventory, sign by sign.
_GEEZ_EIGHTH_SLOT_HOLE = 'ዐ'


def _geez_mint_multiplier(order):
    """The mint's axis (M1/M3): the order's own number, corrected
    at order 6 to the Zero. The folk multiplier is the identity
    function on orders and needs no function of its own — the
    witness builder below multiplies by the order directly, so
    the two laws stand side by side in the code as they do in
    the seam: one shared axis, one named correction."""
    return 0 if order == 6 else order


def _build_geez_banks():
    """Seat the witness and the mint from the one base list.

    MECHANISM: the witness first — the 182 grid signs at
    first × order, the printed folk grid entire, ×6 standing —
    with its first-form map (each sign → its base's first-form
    value) for the practiced reading door. Then the mint: the
    same 182 at first × m(order), the 20 labiovelars at their
    orders, the 25 eighth-slot glyphs at first × 8, with its
    own first-form map (the calibration door: every seated
    sign → its base's first-form value, labiovelars to their
    base consonant's, eighth-slot glyphs to their base's).
    Returns (witness, witness_first, mint, mint_first,
    mint_seating_order) — the seating order exported so the
    batteries can prove the surface: 182 grid + 20 labiovelar
    + 25 eighth-slot = 227 seats, the classical 202 first.
    """
    folk_first = dict(_GEEZ_BASES)
    witness, witness_first = {}, {}
    mint, mint_first, seating = {}, {}, []
    for base, fv in _GEEZ_BASES:
        cp0 = ord(base)
        for order in range(1, 8):
            ch = chr(cp0 + order - 1)
            witness[ch] = fv * order
            witness_first[ch] = fv
            mint[ch] = fv * _geez_mint_multiplier(order)
            mint_first[ch] = fv
            seating.append(ch)
    for head, base in _GEEZ_LABIOVELAR_HEADS:
        fv = folk_first[base]
        cp0 = ord(head)
        for order, off in _GEEZ_LABIOVELAR_OFFSETS.items():
            ch = chr(cp0 + off)
            mint[ch] = fv * _geez_mint_multiplier(order)
            mint_first[ch] = fv
            seating.append(ch)
    for base, fv in _GEEZ_BASES:
        if base == _GEEZ_EIGHTH_SLOT_HOLE:
            continue  # M5: no glyph, no seat — the hole stands
        ch = chr(ord(base) + 7)
        mint[ch] = fv * _geez_mint_multiplier(8)
        mint_first[ch] = fv
        seating.append(ch)
    return witness, witness_first, mint, mint_first, seating


HALEHAME, HALEHAME_FIRST, GEEZ, GEEZ_FIRST, GEEZ_BASE = _build_geez_banks()
# DOCTRINE: the Ethiopic numerals (፩–፼) are keys of NEITHER bank —
# they are a separate glyph system for writing numbers and assign
# no values to fidäl letters (Phase I audit, both derivation
# parties agreeing on the operative point). A weighing that meets
# one skips it: silence, not false weight.

# -- Armenian: THE CLASSICAL TABLE (ATTESTED, complete) ----------------------
# ---------------------------------------------------------------------------
# PROVENANCE — A SOURCED TABLE AT THE FULL DEPTH, stated against its
# control case so the difference is never blurred. The classical
# Armenian numeral system is the designed alphabet's OWN table:
# created with the majuscules of Mashtots' alphabet (c. 405 CE), it
# values EVERY one of the 36 classical letters — units ա–թ = 1–9,
# tens ժ–ղ = 10–90, hundreds ճ–ջ = 100–900, thousands ռ–ք =
# 1000–9000 — and it stands in continuous manuscript use, era dates
# in colophons written ԹՎ + numerals (era epoch AD 552), a practice
# the MELA cataloging manual documents for working catalogers.
# Audited 2026-11-24 (THE-ARMENIAN-TABLE-PHASE-I-AUDIT.md): three
# witnesses read entire agree on all 36 cells (Wikipedia, "Armenian
# numerals"; Omniglot, "Numbers in Armenian"; Wikipedia, "Armenian
# alphabet", Numerical value column), a fourth (MELA) agrees on the
# 12 cells its worked examples exhibit; the class law holds at every
# cell; the witnesses' worked example ՌՋՀԵ = 1975 recomputes exact;
# parity of this seat against the audit's frozen transcription is
# proven by test_armenian_parity.py at the repository root.
#
# THE DIFFERENCE FROM HALEHAME, PLAINLY (the founder ordered the
# two read as a control case — same decimal class-law shape,
# opposite attestation depth): halehame is a FOLK table — it values
# 26 first forms of the fidäl's 202 classical signs, its antiquity
# is undated in every source, its register is folk-magical and
# expressly not liturgical, and its extension axis (the order
# multiplier) is printed but unexhibited in use. This bank is the
# opposite on every axis: complete (36 of 36 classical letters),
# liturgical in its manuscript life, and valued at the full
# four-class extent. Both are witness banks — sourced, not house
# coinage — and the fences keep their depths distinct: do not cite
# halehame at this bank's depth, nor this bank as a folk practice.
# On the shared domain the two laws agree in VALUE at all 26
# positions and part in DERIVATION at exactly position 10
# (Armenian reaches 10 by the class step — Ժ, first tens letter;
# halehame inside the units run — ተ, tenth units letter): the
# control case's boundary coordinate, printed in the audit.
#
# MECHANISM: the bank is keyed in the MAJUSCULES — the forms the
# system was created in ("created using the majuscules of the
# Armenian alphabet"). The minuscules are the same letters' case
# pairs (the alphabet's own table pairs them, form by form, at one
# value), and engine.weigh() folds Armenian input to capitals at
# its seam, so both cases weigh — the preparation happens at the
# door, never by duplicating the bank. Singleness AND uniqueness
# both hold here: 36 letters, 36 distinct values (the Ge'ez mint's
# honesty coordinate — 90 values over 227 seats — does not arise;
# this is a ciphered table, one letter one value, all different).
#
# THE BOUNDARY, AT THE SAME SIZE AS THE VALUES: the two medieval
# additions, Օ (U+0555) and Ֆ (U+0556), are NOT keys of this bank.
# They entered the alphabet in the Middle Ages (13th c. per the
# alphabet article), after Arabic numerals were already in use;
# the numerals article says they "sometimes have a numerical
# value assigned to them" (10000 / 20000), and the alphabet
# article's own table prints NO numerical value for either. That
# is a weaker attestation than any cell of the 36. As first
# seated, the additions stood unseated entirely — an open
# coordinate for the founder's pen (Phase I audit §VII Q1) — and
# a classical weighing that meets Օ or Ֆ still skips it: silence
# at this bank's boundary, printed here, never a smuggled 10000.
#
# RESOLUTION R1 (the founder's ruling, 2026-11-24: the Armenian
# questions decided "in order of Synergy not argument as
# previously ruled"): the additions are seated in the LATE ANNEX
# below (ARMENIAN_LATE), NOT in this bank. Synergy's reasoning:
# this bank's purity is load-bearing — its fence reads "complete
# 36, attested" and the halehame control case leans on it, so
# medieval values are not blended in; yet the "sometimes" values
# are SOURCED, and the house leaves no sourced value homeless;
# and 10000 / 20000 continue the class law's own pattern,
# opening the next class past the thousands. The annex stands a
# tier BELOW the classical 36 (medieval; "sometimes"; one
# article against another's silence) and is OPT-IN: it weighs
# only at the engine's armenian() door under the explicit late
# path, so օ inside an ordinary word still weighs nothing at
# the classical door.
#
# THE OVERLINE — RESOLUTION R2 (same ruling, same standard).
# As first seated, the door counted marks and applied NO
# factor: the sources agree a line over a letter multiplies it
# and parted on the factor — x10,000 (Wikipedia; MELA) against
# x1,000 (Omniglot). Synergy decides by the table's own law:
# this bank holds UNIQUENESS (36 letters, 36 distinct values).
# At x1,000 the overlined units (Ա–Թ -> 1000–9000) collide with
# the plain thousands class — nine collisions, the mark adding
# nothing there; at x10,000 every overlined value at every
# class lands in an empty seat (overlined Ա = 10,000; overlined
# Ջ = 9,000,000, MELA's own exhibit) — zero collisions across
# all 36. The factor that keeps the whole working together is
# x10,000, and it also carries the two stronger witnesses.
# Omniglot's x1,000 stands recorded as the parted source —
# marked, not vanished. The engine's armenian() door applies
# x10,000 per overline mark; armenian_checks() proves the
# collision sweep in code.
ARMENIAN = {
    'Ա': 1, 'Բ': 2, 'Գ': 3, 'Դ': 4, 'Ե': 5, 'Զ': 6, 'Է': 7, 'Ը': 8,
    'Թ': 9, 'Ժ': 10, 'Ի': 20, 'Լ': 30, 'Խ': 40, 'Ծ': 50, 'Կ': 60,
    'Հ': 70, 'Ձ': 80, 'Ղ': 90, 'Ճ': 100, 'Մ': 200, 'Յ': 300, 'Ն': 400,
    'Շ': 500, 'Ո': 600, 'Չ': 700, 'Պ': 800, 'Ջ': 900, 'Ռ': 1000,
    'Ս': 2000, 'Վ': 3000, 'Տ': 4000, 'Ր': 5000, 'Ց': 6000, 'Ւ': 7000,
    'Փ': 8000, 'Ք': 9000,
}

# -- Coptic: THE MILESIAN INHERITANCE (DERIVED — descent from Greek) --------
# ---------------------------------------------------------------------------
# PROVENANCE — A RECEIVED TABLE, stated against its parent so the
# descent is never blurred. The Coptic alphabetic numeral system is
# the Greek Milesian system inherited entire: the Coptic script is
# the uncial Greek alphabet augmented by Demotic letters, and its
# letters carry the Milesian values seat for seat — all 27 value
# seats (units 1–9, tens 10–90, hundreds 100–900) agree with the
# GREEK bank above, verified against the living bank by the Phase I
# audit's descent battery (THE-COPTIC-TABLE-PHASE-I-AUDIT.md,
# 2026-11-24): three full-table witnesses agree on every cell
# (Wikipedia, "Coptic script"; fsymbols; tooldune concurring, its
# derivation from the first stated on its face), with Satzinger's
# Coptic Course exhibiting 26 seats and Dr. Isaac's Institute page
# the practice, all concurring. Parity of this seat against the
# audit's frozen transcription is proven by test_coptic_parity.py
# at the repository root.
#
# WHAT DESCENT PRESERVED, AND WHAT IT ALTERED — the partings ride
# here at the same size as the values:
#   * THE VALUES: total agreement, 27/27 seats. The two banks'
#     value SETS are identical. No value parting exists.
#   * AT 6 AND 900, A PARTING OF KIND: the epissemon seats kept
#     numeral SIGNS on both banks — Greek ϛ (stigma) → Coptic ⲋ
#     (sou: "not used as a letter, but as a numeral whose value
#     is 6" — Isaac), and Greek ϡ (sampi) → Coptic Ⳁ (sampi),
#     the same sign descended into the Coptic block. Neither is
#     a living letter on either bank; sampi is not one of the
#     32 letters of the Coptic alphabet at all.
#   * AT 90, THE ONE PARTING OF LINEAGE: Greek's holder, ϟ
#     (koppa), was an archaic letter, dead in words; Coptic seats
#     ϥ (fai) there — a LIVING Demotic letter, /f/, at home in
#     ordinary words. Wikipedia marks the equivalence
#     "(numerical value)": the kinship is the seat, not the
#     glyph. The grid's one vacancy is the one seat a native
#     letter took.
#   * AT 200, A PARTING OF FORM: the Greek bank carries two
#     glyphs (σ and its word-final form ς); Coptic ⲥ is one
#     letter with no final-form split.
#
# THE BOUNDARY, AT THE SAME SIZE: the remaining Demotic letters —
# ϣ (shai), Ϧ (khai, Bohairic form), Ⳉ (khai, Akhmimic form),
# ϩ (hori), ϫ (gangia), Ϭ (shima), ϯ (dei) — are NOT keys of this
# bank. Every witness read prints a dash against their names: the
# Milesian grid arrived FULL (9/9/9 seats held), so the native
# letters Greek had no room for took no numeral seats. A weighing
# that meets one skips it — silence, printed here, never an
# invented value (the sweep's HERU-RA-HA and ABRAHADABRA fail
# closed on ϩ for exactly this reason, and the failure is data).
#
# MECHANISM: the bank is keyed in the SMALL letters — the parent
# Greek bank's habit, and the case of the witnesses' number
# sequences. The script was caseless (case distinctions are a
# modern convention — Wikipedia, on its face), and engine.weigh()
# casefolds Coptic input at its seam, so both cases weigh — the
# preparation happens at the door, never by duplicating the bank.
# Singleness AND uniqueness both hold: 27 signs, 27 distinct
# values, sum 4995.
#
# THE MARKS ARE NOT VALUES: beyond 900 the sources show devices,
# never letter values — the numeral sign ͵ (U+0375: ⲁ͵ = 1,000)
# and the double overline (U+033F: ⲁ̿ = 1,000), per the Unicode
# Standard §7.3 as Wikipedia reports it, with Satzinger printing
# a stauros sign at 1000 instead. The engine's coptic() door
# counts these marks and prices none of them; the plain overline
# (U+0305) is in every source a MARKER of numeral use, never a
# multiplier — descent kept the Greek mark a mark, where the
# Armenian road found its line grown into a factor.
COPTIC = {
    'ⲁ': 1, 'ⲃ': 2, 'ⲅ': 3, 'ⲇ': 4, 'ⲉ': 5, 'ⲋ': 6, 'ⲍ': 7,
    'ⲏ': 8, 'ⲑ': 9, 'ⲓ': 10, 'ⲕ': 20, 'ⲗ': 30, 'ⲙ': 40, 'ⲛ': 50,
    'ⲝ': 60, 'ⲟ': 70, 'ⲡ': 80, 'ϥ': 90, 'ⲣ': 100, 'ⲥ': 200,
    'ⲧ': 300, 'ⲩ': 400, 'ⲫ': 500, 'ⲭ': 600, 'ⲯ': 700, 'ⲱ': 800,
    'ⳁ': 900,
}

# -- Armenian: THE LATE ANNEX (the medieval additions, opt-in) ----------------
# ---------------------------------------------------------------------------
# PROVENANCE — A TIER BELOW THE CLASSICAL TABLE, stated at its own
# depth. Օ (U+0555) and Ֆ (U+0556) entered the alphabet in the
# Middle Ages (13th c. per the alphabet article), after Arabic
# numerals were already in use; the numerals article says they
# "sometimes have a numerical value assigned to them" — Օ 10000,
# Ֆ 20000 — and the alphabet article's own table prints no value
# for either. Seated here by RESOLUTION R1 under the founder's
# ruling of 2026-11-24 (the Armenian questions decided "in order
# of Synergy not argument as previously ruled"): the values are
# sourced, so they are not left homeless; they continue the
# class law's own pattern, opening the class past the thousands;
# and they stand in an ANNEX, not in the classical bank above,
# whose "complete 36, attested" purity is load-bearing. The
# annex pattern is the house's proven shape — the kana mint's
# derived seats, the Ge'ez mint's labiovelar column: a later
# stratum seated beside its bank, at its own tier, never blended
# into it.
#
# MECHANISM: keyed in BOTH cases — the annex is entered letter by
# letter at the door, and both forms are stored so that no case
# preparation decides anything. This dict is the table of NO
# system in the registry: weigh(word, 'armenian') never sees it.
# It weighs only through engine.armenian(word, late=True) — the
# explicit annex path. At weigh() and at the default door, Օ and
# Ֆ in either case still weigh nothing: օ is a living letter of
# ordinary words (օր, "day"), and the annex must never fire by
# accident.
ARMENIAN_LATE = {
    'Օ': 10000, 'օ': 10000,
    'Ֆ': 20000, 'ֆ': 20000,
}

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
