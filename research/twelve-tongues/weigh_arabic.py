#!/usr/bin/env python3
# =============================================================================
# weigh_arabic.py — the Arabic bank of the Twelve Tongues research
#
# Epigraph: "Weigh every word in its own tongue." — the binding doctrine of
# the PONTIFEX research, settled with the author 2026-10-07.
#
# Thelemic date: ☉ in 18° Libra, ☽ in 24° Scorpio, dies dominica,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is his; the mechanisms below are the scribe's, and they decree
# no bridge. Every finding goes to his red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   HYPOTHESIS: Latin-script Thelemic corpus terms can be weighed in the
#     Arabic abjad (Eastern order, ATTESTED table in pontifex/tables.py).
#   METHOD: transliterate per the scribe's recorded convention
#     (MSA-phonetic-v1, constructed — stated fully in arabic.md §2),
#     then sum with ARABIC_ABJAD. Maghrebi-order parallels computed
#     wherever the order differs. Every choice recorded; losses named.
#   OBSERVATION: letter-by-letter sums printed below for the record.
#   RESULT: the numbers — not doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the Twelve Tongues corpus in the Arabic abjad.

DOCTRINE: the abjad table is ATTESTED (recorded as handed down); the
transliterations are CONSTRUCTED by the scribe's stated convention —
every merger and loss is reported, never hidden.
"""

import sys

sys.path.insert(0, "/home/hatch/workspace/pontifex")

from pontifex.tables import ARABIC_ABJAD  # MECHANISM: the attested table.

# MECHANISM: Maghrebi (western) abjadī order. DOCTRINE: the Eastern order is
# primary per tables.py; the Maghrebi order differs in exactly six letters —
# recorded, not hidden. Maghrebi sequence runs ...ن ص ع ف ض ق ر س ت ث خ ذ ظ غ ش
# assigning 60→ص, 90→ض, 300→س, 800→ظ, 900→غ, 1000→ش. Built as explicit
# overrides (not a hand-typed order string) so the difference is auditable.
_MAGHREBI = dict(ARABIC_ABJAD)
_MAGHREBI.update({'ص': 60, 'ض': 90, 'س': 300, 'ظ': 800, 'غ': 900, 'ش': 1000})

# MECHANISM: sanity check — exactly six letters differ; calibration stable.
_diffs = {k for k in _MAGHREBI if _MAGHREBI[k] != ARABIC_ABJAD[k]}
assert _diffs == {'ص', 'ض', 'س', 'ظ', 'غ', 'ش'}, f"unexpected diffs: {_diffs}"
assert _MAGHREBI["ع"] == 70 and _MAGHREBI["ز"] == 7, "calibration drift!"

# DOCTRINE: the corpus — weighed exactly as received from the parent task,
# plus the reference term عز (the Arabic sister-bank cognate of עז).
CORPUS = {
    "AXONEME": "اكسونيم",     # A-xo-ne-me: X→كس digraph split
    "OZ": "أوز",               # O→و; hamza counted as ا
    "TRVVTH": "تروث",         # TH→ث; VV→single و (gemination lost)
    "THELEMA": "ثيليما",      # TH→ث; E→ي
    "AGAPE": "أغابي",         # Greek γ→غ (Egyptian convention)
    "BABALON": "بابلون",      # standard MSA spelling
    "HERU-RA-HA": "هرو را ها",  # hyphens→spaces; H→ه (soft)
    "ABRAHADABRA": "أبراهادابرا",  # H→ه (soft)
    "QIRA": "قيرا",           # Q→ق
    "LIBERTY": "ليبرتي",      # E/I/Y→ي (all merge); T→ت
    "CELL": "سيل",            # C→س before e; LL→single ل
    "عز": "عز",               # NATIVE — no transliteration; calibration
}

# MECHANISM: recorded variants — same term, defensible alternate choices.
# DOCTRINE: variants are hypotheses for the red pen, not doctrine.
VARIANTS = {
    "THELEMA (θ→ت)": "تيليما",
    "AGAPE (G→ج)": "أجابي",
    "HERU-RA-HA (H→ح)": "حرو را ها",
    "ABRAHADABRA (H→ح)": "أبراحادابرا",
    "TRVVTH (VV geminated)": "تروث",  # ش → shadda doubles و: 400+200+12+500
}


def weigh(word, table):
    """MECHANISM: sum letter values; spaces and harakat score zero."""
    # DOCTRINE: hamza seats (أ إ آ) are carriers for the initial vowel —
    # convention counts them as the carrier letter ا (=1). The choice is
    # recorded, not hidden; a hamza=0 variant is named in arabic.md §6.
    word = word.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    letters = []
    total = 0
    for ch in word:
        v = table.get(ch, 0)  # DOCTRINE: unknown marks (harakat, hamza
        if v:                  # alone) score zero — the loss is reported.
            letters.append((ch, v))
            total += v
    return total, letters


def main():
    print("=== ARABIC BANK — letter-by-letter weighings ===\n")
    for term, form in CORPUS.items():
        total, letters = weigh(form, ARABIC_ABJAD)
        mag_total, _ = weigh(form, _MAGHREBI)
        parts = " + ".join(f"{ch}={v}" for ch, v in letters)
        mag_note = "" if mag_total == total else f"  [Maghrebi: {mag_total}]"
        print(f"{term:14s} {form:12s} = {parts} = {total}{mag_note}")
    print("\n=== recorded variants ===\n")
    for name, form in VARIANTS.items():
        total, letters = weigh(form, ARABIC_ABJAD)
        if name.startswith("TRVVTH"):
            total = 400 + 200 + 12 + 500  # DOCTRINE: shadda-doubled و
            parts = "ت=400 + ر=200 + و=6×2(shadda) + ث=500"
        else:
            parts = " + ".join(f"{ch}={v}" for ch, v in letters)
        print(f"{name:24s} {form:12s} = {parts} = {total}")
    print("\n93. Live, Love, and let Love, Live.")


if __name__ == "__main__":
    main()
