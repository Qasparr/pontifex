#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Epigraph: "Do what thou wilt shall be the whole of the Law." — Liber AL I:40
# Date: 2026-10-11
# 93
#
# Author: Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure
# Worker: SANSKRIT (worker #9 of 12), PONTIFEX gematria bridge research
#
# SCIENTIFIC ILLUMINISM FRAMING
# -----------------------------
# Method: the aim of religion, the method of science. Every value below is
# computed by explicit, inspectable rule — no table is invented silently, no
# category boundary is crossed without a label. The Katapayadi system is a
# REAL traditional decimal-digit encoding (ATTESTED); applying it as a
# word-sum is a category stretch (CONSTRUCTED), and is tiered accordingly.
# The aim of this script is not a bridge but an honest ledger: what the
# system actually says, where the transliteration choices live, what is
# lost, and what meets no target number at all.
#
# Closing motto: Love is the law, love under will.
# =============================================================================

"""
build_sanskrit.py — PONTIFEX worker #9 (SANSKRIT) computation engine.

Produces two fully labeled columns per corpus term:

  (a) KATAPAYADI READING  — digits in order, as the system would encode
      them; this is a POSITIONAL encoding, not a sum. Provenance:
      the system is ATTESTED, the application as word-sum is CONSTRUCTED
      (category stretch, explained in notes).

  (b) DEVANAGARI CANONICAL-ORDINAL SUM — simple sum of letters in the
      traditional varnamala order (a=1, a=2, ... in the Devanagari
      alphabet sequence). Explicitly labeled CONSTRUCTED throughout.

Both columns are written to sanskrit-values.csv with provenance tiers.
"""

import csv
import os

# ---------------------------------------------------------------------------
# DOCTRINE: The Katapayadi consonant->digit mapping.
# MECHANISM: Per Sankaravarman's Sadratnamala (1819 CE) and the anonymous
#   "kadi nava, tadi nava, padi panca, yady astau" line, the nine digits
#   1..9 repeat across four consonant groups (ka-, ta-, pa-, ya-initial),
#   with na and na (and standalone vowels) standing for zero.
#   ka=1 kha=2 ga=3 gha=4 na=5 ca=6 cha=7 ja=8 jha=9 na=0
#   ta=1 tha=2 da=3 dha=4 na=5 ta=6 tha=7 da=8 dha=9 na=0
#   pa=1 pha=2 ba=3 bha=4 ma=5
#   ya=1 ra=2 la=3 va=4 sa=5 sa=6 sa=7 ha=8
# DOCTRINE: This table is ATTESTED (historical sources cited in
#   sanskrit.md). What is NOT attested is using it as a word-sum; the
#   system encodes numbers positionally in verse. The reading below
#   honors the system's actual rules (conjunct rule, final-halant rule,
#   right-to-left digit reading per "ankanam vamato gatih").
# ---------------------------------------------------------------------------
KATA = {
    "k": 1, "kh": 2, "g": 3, "gh": 4, "ng": 5,      # ka-varga + ca-varga tail
    "c": 6, "ch": 7, "j": 8, "jh": 9, "ny": 0,      # (ny = palatal na)
    "tt": 1, "tth": 2, "dd": 3, "ddh": 4, "nn": 5,  # retroflex ta-varga
    "t": 6, "th": 7, "d": 8, "dh": 9, "n": 0,       # dental ta-varga
    "p": 1, "ph": 2, "b": 3, "bh": 4, "m": 5,       # pa-varga
    "y": 1, "r": 2, "l": 3, "v": 4,                 # semivowels
    "sh": 5, "ss": 6, "s": 7, "h": 8,               # sibilants + ha
}
# MECHANISM: internal key code. "ng" = velar na (Devanagari na); "ny" =
#   palatal na; "nn" = retroflex na; "tt/tth/dd/ddh" = retroflexes;
#   "sh" = palatal sa, "ss" = retroflex sa, "s" = dental sa.
#   Loan letters (z' = za-nuqta, q' = qa-nuqta) are NOT in KATA: they are
#   unmappable in the classical table. This is information loss, recorded,
#   not silently resolved.

# ---------------------------------------------------------------------------
# DOCTRINE: The traditional Devanagari varnamala order used for column (b).
# MECHANISM: 14 vowels (a..ah) then 35 consonants in varga order. This is
#   the canonical Indian alphabetical sequence; using position as a value
#   is a CONSTRUCTED comparison column with no traditional warrant. It is
#   labeled CONSTRUCTED everywhere it appears.
# ---------------------------------------------------------------------------
ORDINAL = {}
_vowels = ["a", "aa", "i", "ii", "u", "uu", "rri", "rrri", "lri", "lrri",
           "e", "ai", "o", "au", "am", "ah"]
_cons = ["k", "kh", "g", "gh", "ng", "c", "ch", "j", "jh", "ny",
         "tt", "tth", "dd", "ddh", "nn", "t", "th", "d", "dh", "n",
         "p", "ph", "b", "bh", "m", "y", "r", "l", "v",
         "sh", "ss", "s", "h", "ksh", "tr", "jny"]
for _i, _v in enumerate(_vowels, start=1):
    ORDINAL[_v] = _i
for _i, _c in enumerate(_cons, start=17):
    ORDINAL[_c] = _i
# MECHANISM: loan letters resolve to their base consonant's ordinal
#   (z' -> j, q' -> k). This is a normalization CHOICE, recorded in the
#   CSV 'mergers_or_loss' field, not a traditional rule.
ORDINAL["z'"] = ORDINAL["j"]
ORDINAL["q'"] = ORDINAL["k"]

# ---------------------------------------------------------------------------
# DOCTRINE: The transliteration record. Each term is stored as a list of
#   aksaras; each aksara is (consonant_list, vowel). The Devanagari
#   string is the display form. ISO 15919 is the romanization standard
#   referenced; the mapping below is the Latin->Devanagari direction,
#   recorded choice by choice. Ambiguities are called out in 'notes'.
# ---------------------------------------------------------------------------
# (consonant codes) k kh g gh ng | c ch j jh ny | tt tth dd ddh nn |
#                   t th d dh n  | p ph b bh m  | y r l v | sh ss s h
TERMS = [
    {
        "term": "AXONEME",
        "devanagari": "अक्षोनेमे",
        # X has no Devanagari native letter; ksa (k + sa conjunct) is the
        # standard Indic convention (as in "kshatriya"-class loans).
        "aksaras": [([], "a"), (["k", "ss"], "o"), (["n"], "e"), (["m"], "e")],
        "notes": "X→क्ष (kṣa conjunct) is a convention choice; in katapayadi only the last conjunct member (ष=6) counts, so the k- is invisible to column (a).",
    },
    {
        "term": "OZ",
        "devanagari": "ओज़",
        # Z is a Perso-Arabic loan letter (za with nuqta); NOT in the
        # classical katapayadi table at all. This term is a stress test.
        "aksaras": [([], "o"), (["z'"], None)],
        "notes": "Z→ज़ (loan letter) is unmappable in katapayadi — pure information loss; recorded, not silently mapped. Variant: ओज (z→j) would read 80.",
    },
    {
        "term": "TRVVTH",
        "devanagari": "त्रव्वथ",
        # TR→त्र conjunct; VV→व्व geminate; TH→थ (aspirate dental).
        "aksaras": [(["t", "r"], "a"), (["v", "v"], "a"), (["th"], "a")],
        "notes": "TH→थ (dental aspirate), T→त, D→द throughout (ISO 15919 dental vs retroflex distinction honored).",
    },
    {
        "term": "THELEMA",
        "devanagari": "थेलेमा",
        "aksaras": [(["th"], "e"), (["l"], "e"), (["m"], "aa")],
        "notes": "TH→थ aspirate dental; mechanical syllabification.",
    },
    {
        "term": "AGAPE",
        "devanagari": "अगापे",
        "aksaras": [([], "a"), (["g"], "aa"), (["p"], "e")],
        "notes": "G→ग unaspirated velar; mechanical.",
    },
    {
        "term": "BABALON",
        "devanagari": "बाबालोन्",
        # Final N is halant (no vowel) — ignored by katapayadi rule
        # "a consonant without a vowel is to be ignored".
        "aksaras": [(["b"], "aa"), (["b"], "aa"), (["l"], "o"), (["n"], None)],
        "notes": "Final न् (halant) is IGNORED in column (a) per the Sadratnamala rule 'na ca cintyo halasvarah'; counted as bare consonant in column (b) — a normalization difference, recorded.",
    },
    {
        "term": "HERU-RA-HA",
        "devanagari": "हेरु-रा-हा",
        # Hyphens are word separators; they carry no value in either column.
        "aksaras": [(["h"], "e"), (["r"], "u"), (["r"], "aa"), (["h"], "aa")],
        "notes": "Hyphens dropped as separators (value-less); R→र, H→ह.",
    },
    {
        "term": "ABRAHADABRA",
        "devanagari": "अब्राहादाब्रा",
        # BR→ब्र conjunct (only r counts in column a).
        "aksaras": [([], "a"), (["b", "r"], "aa"), (["h"], "aa"),
                    (["d"], "aa"), (["b", "r"], "aa")],
        "notes": "BR→ब्र conjuncts: katapayadi reads only the last member (र=2), the ब- is invisible to column (a) — collision/loss recorded.",
    },
    {
        "term": "QIRA",
        "devanagari": "किरा",
        # Q→क is the canonical Sanskritization (as in Arabic 'qamar' ->
        # Sanskrit loans); क़ (nuqta) variant recorded in notes.
        "aksaras": [(["k"], "i"), (["r"], "aa")],
        "notes": "Q→क (canonical Sanskritized); variant क़िरा (q' with nuqta) would be equally defensible — normalization choice, recorded.",
    },
    {
        "term": "LIBERTY",
        "devanagari": "लिबेर्टी",
        # RTY→र्त्य conjunct (r + t + y); only y counts in column (a).
        "aksaras": [(["l"], "i"), (["b"], "e"), (["r", "t", "y"], "ii")],
        "notes": "RTY→र्त्य conjunct: only य=1 counts in (a); the र,त vanish — heavy loss. Variant लिबेरतय (no conjunct) would read 3-3-2-6-1=16233 — normalization moves the number.",
    },
    {
        "term": "CELL",
        "devanagari": "चेल्ल",
        # C→च (palatal affricate) is the letter-by-letter choice; the
        # English /s/ sound would give सेल — variant recorded.
        "aksaras": [(["c"], "e"), (["l", "l"], "a")],
        "notes": "C→च is mechanical (letter-by-letter); phonetic English /s/ would be सेल (s=7) — variant recorded; geminate ल्ल counts once in (a).",
    },
]

# ---------------------------------------------------------------------------
# MECHANISM: katapayadi reading of one term.
#   Per Sadratnamala: vowel-only aksara -> 0; conjunct -> LAST consonant
#   only; consonant without vowel (None) -> ignored (skipped); digits read
#   right-to-left ("ankanam vamato gatih"): the FIRST aksara's digit is the
#   units place. The result is a POSITIONAL NUMBER, not a sum.
# DOCTRINE: This reading is faithful to the attested system. Using it as a
#   "word value" for gematria comparison is the CONSTRUCTED application.
# ---------------------------------------------------------------------------
def katapayadi_reading(term):
    digits = []          # digit sequence in reading order (first = units)
    trace = []           # ultra-verbose audit trail
    for cons, vowel in term["aksaras"]:
        if not cons:
            # MECHANISM: vowel standing alone. Sadratnamala assigns zero;
            # some formulations give vowels NO value. We follow
            # Sadratnamala (0) and record the variant in notes.
            digits.append(0)
            trace.append("vowel-only(%s)->0 [Sadratnamala; no-value variant noted]" % vowel)
        else:
            last = cons[-1]
            if vowel is None and last in ("z'",):
                # MECHANISM: loan letter — absent from the classical table.
                digits.append(None)
                trace.append("z'(loan)->UNMAPPABLE (no classical value)")
            elif vowel is None:
                # MECHANISM: consonant without a vowel (halant) is ignored.
                trace.append("%s(halant, no vowel)->IGNORED [Sadratnamala]" % last)
            else:
                if last not in KATA:
                    digits.append(None)
                    trace.append("%s->UNMAPPABLE" % last)
                else:
                    d = KATA[last]
                    digits.append(d)
                    if len(cons) > 1:
                        trace.append("%s(conjunct %s)->last=%s=%d [loss: %s invisible]"
                                     % (last, "+".join(cons), last, d, "+".join(cons[:-1])))
                    else:
                        trace.append("%s->%d" % (last, d))
    # MECHANISM: drop unmappable slots from the number (they contribute no
    # digit); the number is the digit string REVERSED (right-to-left).
    clean = [d for d in digits if d is not None]
    number = int("".join(str(d) for d in reversed(clean))) if clean else None
    return digits, number, trace


# ---------------------------------------------------------------------------
# MECHANISM: constructed varnamala-ordinal sum of one term.
#   Sum over every aksara of (sum of consonant ordinals + vowel ordinal).
#   Bare consonants (halant) contribute their consonant ordinal, vowel 0.
#   Loan letters take their base consonant's ordinal (documented choice).
# DOCTRINE: CONSTRUCTED. No tradition assigns these values; it exists only
#   as a labeled comparison column for the parent synthesis.
# ---------------------------------------------------------------------------
def ordinal_sum(term):
    total = 0
    trace = []
    for cons, vowel in term["aksaras"]:
        parts = []
        for c in cons:
            v = ORDINAL[c]
            total += v
            parts.append("%s=%d" % (c, v))
        if vowel is not None:
            total += ORDINAL[vowel]
            parts.append("%s=%d" % (vowel, ORDINAL[vowel]))
        trace.append("+".join(parts))
    return total, trace


def main():
    outdir = os.path.expanduser("~/workspace/pontifex/research/twelve-tongues")
    os.makedirs(outdir, exist_ok=True)

    rows = []
    print("=" * 70)
    print("SANSKRIT WORKER — ULTRA-VERBOSE COMPUTATION LOG  (2026-10-11, 93)")
    print("=" * 70)

    for term in TERMS:
        print("\n### TERM: %s  [%s]" % (term["term"], term["devanagari"]))
        # -- column (a): katapayadi reading --
        digits, number, ktrace = katapayadi_reading(term)
        print("  [a] katapayadi digit trace:")
        for t in ktrace:
            print("      " + t)
        print("      digits-in-order(first=units): %s" % digits)
        print("      READING (positional, right-to-left): %s" % number)
        # -- column (b): constructed ordinal sum --
        total, otrace = ordinal_sum(term)
        print("  [b] ordinal-sum trace: %s" % " | ".join(otrace))
        print("      SUM (CONSTRUCTED): %d" % total)

        mergers = []
        if any(d is None for d in digits):
            mergers.append("unmappable slot(s) dropped from reading")
        if any(len(c) > 1 for c, _ in term["aksaras"] if c):
            mergers.append("conjunct member(s) invisible to katapayadi (last-only rule)")
        if any(c and v is None and not any(x in ("z'", "q'") for x in c)
               for c, v in term["aksaras"]):
            mergers.append("halant consonant ignored in (a), counted bare in (b)")
        if term["term"] == "OZ":
            mergers.append("loan letter z' has no classical katapayadi value")

        rows.append({
            "term": term["term"], "language": "Sanskrit",
            "script_form": term["devanagari"],
            "transliteration_convention": "Latin->Devanagari, ISO 15919-informed (dental/aspirate/retroflex distinguished); loan letters with nuqta where applicable",
            "table_used": "katapayadi positional reading (digits, right-to-left)",
            "provenance_tier": "ATTESTED system; CONSTRUCTED application as word-value",
            "value": number if number is not None else "DEGENERATE",
            "mergers_or_loss": "; ".join(mergers) if mergers else "none",
            "notes": term["notes"] + " Digit trace: " + " | ".join(ktrace),
        })
        rows.append({
            "term": term["term"], "language": "Sanskrit",
            "script_form": term["devanagari"],
            "transliteration_convention": "same as above",
            "table_used": "varnamala canonical ordinal (vowels 1-16, consonants 17-49 in alphabet order)",
            "provenance_tier": "CONSTRUCTED (no traditional warrant)",
            "value": total,
            "mergers_or_loss": ("loan letter resolved to base ordinal" if term["term"] == "OZ"
                                else ("bare halant consonant counted without vowel" if term["term"] == "BABALON" else "none")),
            "notes": term["notes"] + " Sum trace: " + " | ".join(otrace),
        })

    csv_path = os.path.join(outdir, "sanskrit-values.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["term", "language", "script_form",
                                         "transliteration_convention", "table_used",
                                         "provenance_tier", "value",
                                         "mergers_or_loss", "notes"])
        w.writeheader()
        w.writerows(rows)
    print("\nWROTE: %s  (%d rows)" % (csv_path, len(rows)))


if __name__ == "__main__":
    main()
