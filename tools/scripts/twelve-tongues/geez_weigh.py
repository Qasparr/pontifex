#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — geez_weigh.py — the Ge'ez bank of the Twelve-Tongues survey
# Worker #10 of 12 (GE'EZ)
#
# Epigraph: "There are 22 heads of mankind from Adam to Jacob, and 22 works
# that were done until the seventh day." — Jubilees 2:23 (Ethiopian canon).
#
# Thelemic date: ☉ in Libra, dies solis, Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to the
# author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: Ge'ez has no living letter-number tradition of the abjad
#   kind — the ፩፪፫ glyphs are a borrowed numeral system, like Roman
#   numerals, not values of the fidel. But the debtera (unordained clergy:
#   astrologers, fortune-tellers) DO keep a native letter-number
#   enumeration — the halehame enumeration — for fortune-telling.
#   Method: (1) verify the negative and the positive against sources;
#   (2) weigh the corpus in the halehame bank via a documented,
#   uniform phonetic transliteration into first-form fidel (word-forms
#   CONSTRUCTED, table ATTESTED); (3) weigh the same forms through the
#   repo's Hebrew-fallback doctrine (values ATTESTED, map CONSTRUCTED);
#   (4) weigh them in a transparently scribe-built fidel ordinal
#   (CONSTRUCTED, labeled as construction, never discovery);
#   (5) self-check the halehame table against its published worked
#   example ክርስቶስ = 80 before trusting a single number.
#   Observation: recorded in the log below and in geez.md.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Weigh the Twelve-Tongues shared corpus in the Ge'ez bank.

DOCTRINE: the Ge'ez bank is NOT the Ethiopic numerals (፩፪፫…). Those are
separate glyphs, borrowed from the Greek numerals (via Coptic uncials with a
vinculum), used to WRITE numbers — Roman numerals, not letter values.
The native letter-number practice is the DEBTERA/HALEHAME enumeration:
the first-form fidel characters in the halehame order carry values
(ሀ=1 … ፐ=800), used by the debtera for fortune-telling (e.g. the mother's
name summed, mod 12, read against the stars). It is a specialized
magical practice, not mainstream liturgical use — stated, not hidden.
Its provenance is documented in geez.md; the table below is transcribed
from geez.org/Numerals/Numerology.html ("Debtera (Halehame) Enumeration").

MECHANISM: (a) DEBTERA — the tradition's own table, values ATTESTED;
word-forms are the scribe's phonetic transliterations (CONSTRUCTED), spelled
naturally in fidel; each character contributes its consonant order's base
value — vowel form ignored, exactly as the tradition's own worked example
does (ክርስቶስ = ከ50+ረ6+ሰ7+ቶ10+ሰ7 = 80, where ቶ counts as ተ).
(b) HEBREW-FALLBACK — the repo doctrine: Latin through
pontifex/tables.py's LATIN_TO_HEBREW (greedy digraphs), values ATTESTED
(mispar hechrechi), map CONSTRUCTED; mergers reported from MERGERS.
(c) FIDEL-ORDINAL — the scribe's transparent construction: ሀ=1 … ፐ=31
in the traditional fidel order; every character worth its order number.
CONSTRUCTED and labeled so — never presented as a discovery.
"""

import csv
import os
import sys

# MECHANISM: the one source of truth for the Hebrew side — never re-key.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import (
    HEBREW, LATIN_TO_HEBREW, LATIN_TO_HEBREW_DIGRAPHS, MERGERS,
)

# -- The shared corpus -------------------------------------------------------
# MECHANISM: raw forms as the parent issued them. Normalization (hyphen
# drop) happens in normalize() and is recorded in the CSV notes.
CORPUS = [
    "AXONEME", "OZ", "TRVVTH", "THELEMA", "AGAPE", "BABALON",
    "HERU-RA-HA", "ABRAHADABRA", "QIRA", "LIBERTY", "CELL",
]

# -- The traditional fidel order (drives ordinal + base resolution) -----------
# DOCTRINE: the traditional order ሀለሐመሠረሰሸቀበተቸኀነኘአከኸወዐዘዠየደገጠጨጰጸፈፐ.
FIDEL_ORDINAL_ORDER = list(
    "ሀለሐመሠረሰሸቀበተቸኀነኘአከኸወዐዘዠየደገጠጨጰጸፈፐ"
)

# -- FIDEL_ORDINAL_VOWEL_BASE (order table lives above) --------------------
FIDEL_ORDINAL_VOWEL_BASE = {
    # MECHANISM: vowel-forms of the same order share the order number.
    'ሁ': 1, 'ሂ': 1, 'ሃ': 1, 'ሄ': 1, 'ህ': 1, 'ሆ': 1,
    'ሉ': 2, 'ሊ': 2, 'ላ': 2, 'ሌ': 2, 'ል': 2, 'ሎ': 2, 'ሏ': 2,
    'ሑ': 3, 'ሒ': 3, 'ሓ': 3, 'ሔ': 3, 'ሕ': 3, 'ሖ': 3, 'ሗ': 3,
    'ሙ': 4, 'ሚ': 4, 'ማ': 4, 'ሜ': 4, 'ም': 4, 'ሞ': 4, 'ሟ': 4,
    'ሡ': 5, 'ሢ': 5, 'ሣ': 5, 'ሤ': 5, 'ሥ': 5, 'ሦ': 5, 'ሧ': 5,
    'ሩ': 6, 'ሪ': 6, 'ራ': 6, 'ሬ': 6, 'ር': 6, 'ሮ': 6, 'ሯ': 6,
    'ሱ': 7, 'ሲ': 7, 'ሳ': 7, 'ሴ': 7, 'ስ': 7, 'ሶ': 7, 'ሷ': 7,
    'ሹ': 8, 'ሺ': 8, 'ሻ': 8, 'ሼ': 8, 'ሽ': 8, 'ሾ': 8,
    'ቁ': 9, 'ቂ': 9, 'ቃ': 9, 'ቄ': 9, 'ቅ': 9, 'ቆ': 9,
    'ቡ': 10, 'ቢ': 10, 'ባ': 10, 'ቤ': 10, 'ብ': 10, 'ቦ': 10, 'ቧ': 10,
    'ቩ': 10, 'ቪ': 10, 'ቫ': 10, 'ቬ': 10, 'ቭ': 10, 'ቮ': 10,  # ቨ-series → በ-order
    'ቨ': 10, 'ኁ': 13,    'ቨ': 10,
    'ቱ': 11, 'ቲ': 11, 'ታ': 11, 'ቴ': 11, 'ት': 11, 'ቶ': 11,
    'ቹ': 12, 'ቺ': 12, 'ቻ': 12, 'ቼ': 12, 'ች': 12, 'ቾ': 12,
    'ኁ': 13, 'ኂ': 13, 'ኃ': 13, 'ኄ': 13, 'ኅ': 13, 'ኆ': 13,
    'ኑ': 14, 'ኒ': 14, 'ና': 14, 'ኔ': 14, 'ን': 14, 'ኖ': 14, 'ኗ': 14,
    'ኑ': 14, 'ኒ': 14, 'ና': 14, 'ኔ': 14, 'ን': 14, 'ኖ': 14, 'ኗ': 14,
    'ኙ': 15, 'ኚ': 15, 'ኛ': 15, 'ኜ': 15, 'ኝ': 15, 'ኞ': 15,
    'ኡ': 16, 'ኢ': 16, 'አ': 16, 'ኤ': 16, 'እ': 16, 'ኦ': 16,
    'ኩ': 17, 'ኪ': 17, 'ካ': 17, 'ኬ': 17, 'ክ': 17, 'ኮ': 17,
    'ኩ': 17, 'ኪ': 17, 'ካ': 17, 'ኬ': 17, 'ክ': 17, 'ኮ': 17,
    'ኹ': 18, 'ኺ': 18, 'ኻ': 18, 'ኼ': 18, 'ኽ': 18, 'ኾ': 18,
    'ዉ': 19, 'ዊ': 19, 'ዋ': 19, 'ዌ': 19, 'ው': 19, 'ዎ': 19,
    'ዑ': 20, 'ዒ': 20, 'ዓ': 20, 'ዔ': 20, 'ዕ': 20, 'ዖ': 20,
    'ዙ': 21, 'ዚ': 21, 'ዛ': 21, 'ዜ': 21, 'ዝ': 21, 'ዞ': 21,
    'ዙ': 21, 'ዚ': 21, 'ዛ': 21, 'ዜ': 21, 'ዝ': 21, 'ዞ': 21,
    'ዡ': 22, 'ዢ': 22, 'ዣ': 22, 'ዤ': 22, 'ዥ': 22, 'ዦ': 22,
    'ዩ': 23, 'ዪ': 23, 'ያ': 23, 'ዬ': 23, 'ይ': 23, 'ዮ': 23,
    'ዱ': 24, 'ዲ': 24, 'ዳ': 24, 'ዴ': 24, 'ድ': 24, 'ዶ': 24,
    'ጉ': 25, 'ጊ': 25, 'ጋ': 25, 'ጌ': 25, 'ግ': 25, 'ጎ': 25,
    'ጁ': 25, 'ጂ': 25, 'ጃ': 25, 'ጄ': 25, 'ጅ': 25, 'ጆ': 25,  # ጀ → ገ-order
    'ጀ': 25,
    'ጡ': 26, 'ጢ': 26, 'ጣ': 26, 'ጤ': 26, 'ጥ': 26, 'ጦ': 26,
    'ጡ': 26, 'ጢ': 26, 'ጣ': 26, 'ጤ': 26, 'ጥ': 26, 'ጦ': 26,
    'ጩ': 27, 'ጪ': 27, 'ጫ': 27, 'ጬ': 27, 'ጭ': 27, 'ጮ': 27,
    'ጱ': 28, 'ጲ': 28, 'ጳ': 28, 'ጴ': 28, 'ጵ': 28, 'ጶ': 28,
    'ጹ': 29, 'ጺ': 29, 'ጻ': 29, 'ጼ': 29, 'ጽ': 29, 'ጾ': 29,
    'ፉ': 30, 'ፊ': 30, 'ፋ': 30, 'ፌ': 30, 'ፍ': 30, 'ፎ': 30,
    'ፑ': 31, 'ፒ': 31, 'ፓ': 31, 'ፔ': 31, 'ፕ': 31, 'ፖ': 31,
}


# -- The Debtera (halehame) enumeration, ATTESTED table ----------------------
# DOCTRINE: transcribed from geez.org ("Debtera (Halehame) Enumeration");
# the tradition's own first-form values. The table covers 26 base orders —
# the labialized and later-added series (ሸ ቸ ኘ ኸ ዠ) have NO value in it;
# the corpus does not need them, and the gap is recorded in geez.md.
# MECHANISM: vowel-form multipliers (hu=×2, hi=×3, …) exist in the table but
# the tradition's own worked examples "invariably use the letters of a word
# in the first form only" — so weigh() sums base values only, always.
DEBTERA = {
    'ሀ': 1, 'ለ': 2, 'ሐ': 3, 'መ': 4, 'ሠ': 5, 'ረ': 6, 'ሰ': 7, 'ቀ': 8,
    'በ': 9, 'ተ': 10, 'ኀ': 20, 'ነ': 30, 'አ': 40, 'ከ': 50, 'ወ': 60,
    'ዐ': 70, 'ዘ': 80, 'የ': 90, 'ደ': 100, 'ገ': 200, 'ጠ': 300, 'ጰ': 400,
    'ጸ': 500, 'ፀ': 600, 'ፈ': 700, 'ፐ': 800,
}
# MECHANISM: vowel-forms of א-order and the modern ቨ all resolve to their
# consonant order's base value — exactly how ቶ counts as ተ=10 in ክርስቶስ.
# (The general resolver ORDER_BASE is built below from the fidel order.)
BASE_OF = {
    'አ': 40, 'ኡ': 40, 'ኢ': 40, 'ኤ': 40, 'እ': 40, 'ኦ': 40,
    'ይ': 90,   # MECHANISM: ይ is የ-order (Yemen), not አ-order — do not merge.
    'ቨ': 9,    # DOCTRINE: modern v-series; consonant order is በ — a judgment,
               # documented here and in the CSV mergers column.
}

# -- order-number resolvers (built, not hand-keyed) ---------------------------
# MECHANISM: one numbering of the traditional fidel order drives both the
# constructed ordinal and the base-resolution for the Debtera table, so the
# two cannot drift apart.
ORDER_NUM = {ch: i + 1 for i, ch in enumerate(FIDEL_ORDINAL_ORDER)}
ORDER_NUM.update(FIDEL_ORDINAL_VOWEL_BASE)  # vowel-forms → their order
BASE_FIRST_FORM = {i + 1: ch for i, ch in enumerate(FIDEL_ORDINAL_ORDER)}


def debtera_value(ch):
    # MECHANISM: resolve any fidel character to its consonant order's base
    # (first-form) character, then take the Debtera value of that order.
    # Returns None for orders outside the 26 the tradition enumerates
    # (ሸ ቸ ኘ ኸ ዠ and the labialized series) — the gap is honest, not patched.
    base = BASE_FIRST_FORM.get(ORDER_NUM.get(ch))
    return DEBTERA.get(base) if base else None


# -- The transliteration convention, CONSTRUCTED -------------------------------
# DOCTRINE: the scribe's uniform phonetic key — recorded here so the red pen
# can re-run or reject it. Choices: vowels on the አ-order (a→አ e→ኤ i→ኢ
# o→ኦ u→ኡ y→ይ); θ (th) → ተ (plain t — Ethiopic has no θ); x → ክስ
# (documented expansion, no single fidel for /ks/); v → ቨ (modern series);
# c is phonetic (/k/→ከ, /s/→ሰ) — the one judgment that reads the English
# aloud first. Hyphens dropped (HERU-RA-HA).
TRANSLIT = {
    'a': 'አ', 'e': 'ኤ', 'i': 'ኢ', 'o': 'ኦ', 'u': 'ኡ', 'y': 'ይ',
    'b': 'በ', 'd': 'ደ', 'f': 'ፈ', 'g': 'ገ', 'h': 'ሀ', 'j': 'ጀ',
    'k': 'ከ', 'l': 'ለ', 'm': 'መ', 'n': 'ነ', 'p': 'ፐ', 'q': 'ቀ',
    'r': 'ረ', 's': 'ሰ', 't': 'ተ', 'v': 'ቨ', 'w': 'ወ', 'z': 'ዘ',
    'c_k': 'ከ', 'c_s': 'ሰ',
    'ch': 'ቸ', 'sh': 'ሸ', 'th': 'ተ', 'x': 'ከሰ',
}
# MECHANISM: which C's are /s/? CELL is "sell". QIRA's q is /k/. Documented
# per-term below; the default is /k/.
C_IS_S = {'CELL'}

CONVENTION_NAME = (
    "scribe phonetic key v1 (vowels on አ-order; θ→ተ; x→ከሰ; c phonetic; "
    "hyphens dropped) — CONSTRUCTED word-forms"
)


def normalize(term):
    # MECHANISM: the only normalization — drop hyphens, lowercase for the key.
    return term.replace("-", "").lower()


def transliterate(term):
    # MECHANISM: greedy digraphs first (ch, sh, th), then single letters;
    # x expands to ከሰ; c is phonetic per C_IS_S.
    t = normalize(term)
    out = []
    i = 0
    while i < len(t):
        two = t[i:i + 2]
        if two in ('ch', 'sh', 'th'):
            out.append(TRANSLIT[two])
            i += 2
            continue
        c = t[i]
        if c == 'x':
            out.append(TRANSLIT['x'])
        elif c == 'c':
            out.append(TRANSLIT['c_s'] if term in C_IS_S else TRANSLIT['c_k'])
        else:
            out.append(TRANSLIT[c])
        i += 1
    return "".join(out)


def weigh_debtera(fidel):
    # MECHANISM: each fidel character → its consonant order's base value
    # (vowel form ignored, per the tradition's own worked example).
    # Returns (total, breakdown list).
    total, parts = 0, []
    for ch in fidel:
        v = debtera_value(ch)
        if v is None:
            raise ValueError(
                f"no debtera value for {ch!r} (order outside the 26)")
        total += v
        parts.append(f"{ch}{v}")
    return total, parts


def weigh_ordinal(fidel):
    # MECHANISM: each character → its traditional-order number (scribe-built).
    total, parts = 0, []
    for ch in fidel:
        v = ORDER_NUM.get(ch)
        if v is None:
            raise ValueError(f"no ordinal value for {ch!r}")
        total += v
        parts.append(f"{ch}{v}")
    return total, parts


def weigh_hebrew_fallback(term):
    # MECHANISM: the repo doctrine — greedy digraphs (ch/sh/th) then
    # LATIN_TO_HEBREW, summed in mispar hechrechi; mergers reported.
    t = normalize(term)
    hebrew, fired, i = [], set(), 0
    while i < len(t):
        two = t[i:i + 2]
        if two in LATIN_TO_HEBREW_DIGRAPHS:
            hebrew.append(LATIN_TO_HEBREW_DIGRAPHS[two])
            i += 2
            continue
        hebrew.append(LATIN_TO_HEBREW[t[i]])
        i += 1
    # MECHANISM: report mergers — which Hebrew letters absorbed >1 Latin.
    latin_used = []
    i = 0
    while i < len(t):
        two = t[i:i + 2]
        if two in LATIN_TO_HEBREW_DIGRAPHS:
            latin_used.append(two)
            i += 2
            continue
        latin_used.append(t[i])
        i += 1
    for h, grp in MERGERS.items():
        hit = [l for l in latin_used if l in grp]
        if len(hit) > 1:
            fired.add(f"{h}<-{','.join(sorted(set(hit)))}")
    total = sum(HEBREW[h] if len(h) == 1 else sum(HEBREW[x] for x in h)
                for h in hebrew)
    parts = [f"{l}→{h}{HEBREW[h] if len(h) == 1 else sum(HEBREW[x] for x in h)}"
             for l, h in zip(latin_used, hebrew)]
    return total, parts, sorted(fired)


def self_check():
    # MECHANISM: the tradition's own calibration — ክርስቶስ must weigh 80.
    # ከ50 + ረ6 + ሰ7 + ቶ(ተ)10 + ሰ7 = 80.
    total, parts = weigh_debtera("ክርስቶስ")
    assert total == 80, f"calibration failed: ክርስቶስ={total}"
    print(f"CALIBRATION OK: ክርስቶስ = {'+'.join(parts)} = {total}")


TARGETS = {418, 666, 777, 93, 77, 11}


def main():
    self_check()
    rows = []
    for term in CORPUS:
        fidel = transliterate(term)
        # -- (a) the native bank: Debtera enumeration ----------------------
        d_total, d_parts = weigh_debtera(fidel)
        d_mergers = ("vowel-forms resolve to consonant order: "
                     "አኤኢኦኡ→አ-order (40/16), ይ→የ-order (90/23); "
                     "ቨ→በ-order (9/10); x→ከሰ expansion"
                     + ("; hyphens dropped" if "-" in term else "")
                     + ("; th→ተ merges with t" if "th" in normalize(term) else ""))
        d_note = ("breakdown " + "+".join(d_parts) + f"={d_total}"
                  + ("; TARGET HIT " + str(d_total) if d_total in TARGETS else ""))
        rows.append([term, "Ge'ez", fidel, CONVENTION_NAME,
                     "DEBTERA halehame enumeration (first-form values; "
                     "transcribed from geez.org Numerology page)",
                     "word-form CONSTRUCTED / table ATTESTED",
                     d_total, d_mergers, d_note])
        # -- (b) the repo Hebrew fallback -----------------------------------
        h_total, h_parts, h_fired = weigh_hebrew_fallback(term)
        if term == "ABRAHADABRA":
            tier = "word-form NATIVE (corpus spelling) / map CONSTRUCTED (repo) / values ATTESTED"
        else:
            tier = "word-form CONSTRUCTED (fidel round-trip of Latin) / map CONSTRUCTED (repo) / values ATTESTED"
        h_mergers = ("repo MERGERS fired: " + ", ".join(h_fired)
                     if h_fired else "none of repo MERGERS fired")
        h_note = ("breakdown " + "+".join(h_parts) + f"={h_total}"
                  + ("; TARGET HIT " + str(h_total) if h_total in TARGETS else ""))
        rows.append([term, "Ge'ez", fidel, CONVENTION_NAME,
                     "HEBREW mispar hechrechi via repo LATIN_TO_HEBREW "
                     "(greedy digraphs)",
                     tier, h_total, h_mergers, h_note])
        # -- (c) the scribe's fidel ordinal (construction, labeled) --------
        o_total, o_parts = weigh_ordinal(fidel)
        o_note = ("breakdown " + "+".join(o_parts) + f"={o_total}"
                  + ("; TARGET HIT " + str(o_total) if o_total in TARGETS else "")
                  + " — scribe construction, not a discovery")
        rows.append([term, "Ge'ez", fidel, CONVENTION_NAME,
                     "FIDEL-ORDINAL ሀ=1..ፐ=31 (scribe-built; CONSTRUCTED)",
                     "word-form CONSTRUCTED / table CONSTRUCTED",
                     o_total, d_mergers, o_note])
        print(f"{term:12s} fidel={fidel:14s} debtera={d_total:5d} "
              f"hebrew={h_total:5d} ordinal={o_total:4d}")

    out = os.path.expanduser(
        "~/workspace/pontifex/research/twelve-tongues/geez-values.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["term", "language", "script_form",
                    "transliteration_convention", "table_used",
                    "provenance_tier", "value", "mergers_or_loss", "notes"])
        w.writerows(rows)
    print(f"\nwrote {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
