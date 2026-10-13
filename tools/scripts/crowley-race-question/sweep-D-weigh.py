#!/usr/bin/env python3
# =============================================================================
# sweep-D-weigh.py — Worker D (priority thread) of the PONTIFEX anomaly sweep
# of Aleister Crowley's writings: gematria values for terms meaning
# "Jew"/"Jews" and "black"/"Black".
#
# Epigraph: "The study of the Qabalah is the study of the Universe in
# numbers; the numbers are the servants of the Truth, not its masters."
# — paraphrase of the author's working doctrine; findings here, not doctrine.
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# Scribed by Worker D; findings are drafts for the author's red pen —
# no bridge is decreed here.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the terms "Jew"/"Jews"/"black" in Hebrew and Greek, weighed
#     mechanically in the attested tables, may or may not land on numbers
#     Crowley printed for them or on the loaded numbers (11, 77, 93, 418,
#     666, 777). Any small exact discrepancy between a Crowley-printed
#     value and the mechanical recomputation is the signal being hunted.
#   Method: calibrate the imported ATTESTED tables (Hebrew mispar hechrechi,
#     Greek Milesian) against two anchors — יופיאל=137 and ראהוור=418;
#     fail closed if either misses. Weigh the five assigned terms from
#     their STANDARD spellings (native tongues, no transliteration).
#     Test every result against the loaded set {11, 77, 93, 418, 666, 777}.
#   Observation: recorded per term below with full letter breakdowns.
#   Result: the ledger printed here feeds sweep-D-jew-black.md. Findings,
#     never doctrine. No term is declared "the breadcrumb".
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the D-thread terms in their native tables.

DOCTRINE (the author's, not amended here):
- Each word weighed in its own tongue. Hebrew = mispar hechrechi
  (א=1 ... ת=400, final forms take medial values); Greek = Milesian
  (α=1 ... ϡ=900).
- Every value: ATTESTED tier (native term, attested table, no built
  transliteration) unless stated otherwise.
- Calibration: יופיאל MUST = 137 and ראהוור MUST = 418, or exit 1.

MECHANISM:
- Tables are IMPORTED from pontifex.tables (attested, never re-typed).
- The script weighs STANDARD spellings only: no transliteration variants
  are weighed silently; variant forms are listed in the md ledger with
  their own recomputations where the corpus turns one up.
"""

import os
import sys

# MECHANISM: reuse the repo's attested tables so no value is invented here.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import HEBREW, GREEK  # noqa: E402 (attested tables)

# MECHANISM: the five assigned terms in their standard spellings, with
# glosses. English gloss is research metadata only — the weighing is on
# the script form alone.
TERMS = [
    ("יהודי", "Hebrew", "yehudi — 'Jew' (m. sg.)"),
    ("יהודים", "Hebrew", "yehudim — 'Jews' (m. pl.)"),
    ("Ἰουδαῖος", "Greek", "Ioudaios — 'Jew' (m. sg.)"),
    ("שחור", "Hebrew", "shachor — 'black' (m. sg.)"),
    ("μέλας", "Greek", "melas — 'black' (m. sg.) — standard spelling"),
]

# MECHANISM: loaded numbers of the sweep.
LOADED = (11, 77, 93, 418, 666, 777)


def strip_greek_diacritics(s):
    """Return s with combining diacritical marks removed.

    MECHANISM: Crowley's transliterated Greek and Unicode sources disagree
    on accents/breathings; gematria never weighs them. Both forms are
    weighed to prove the point. Uses NFD decomposition, drops Mn.
    """
    import unicodedata
    return "".join(
        ch for ch in unicodedata.normalize("NFD", s)
        if unicodedata.category(ch) != "Mn"
    )


def weigh(word, lang):
    """Weigh word letter by letter in the named attested table.

    MECHANISM: straight table lookup; no silent skipping — a character not
    in the table raises KeyError so a bad input fails loudly, not softly.
    Returns (total, [(letter, value), ...]).
    """
    table = HEBREW if lang == "Hebrew" else GREEK
    steps = [(ch, table[ch]) for ch in word]
    return sum(v for _, v in steps), steps


def main():
    # -- Calibration: fail closed -------------------------------------------
    # MECHANISM: two independent anchors, one per table. If either misses,
    # the tables are wrong and nothing else may be trusted — exit 1.
    cal = [
        ("יופיאל", "Hebrew", 137),
        ("ראהוור", "Hebrew", 418),
        ("θελημα", "Greek", 93),  # third anchor, greek bank
    ]
    print("CALIBRATION:")
    for word, lang, want in cal:
        total, steps = weigh(word, lang)
        ok = "✓" if total == want else "✗ MISMATCH"
        print(f"  {word} = {'+'.join(str(v) for _, v in steps)} = {total}"
              f" (want {want}) {ok}")
        assert total == want, f"CALIBRATION FAILED: {word} = {total}, want {want}"
    print("  all anchors weigh true — tables trusted.\n")

    # -- The five assigned terms --------------------------------------------
    print("WEIGHINGS (standard spellings):")
    results = []
    for word, lang, gloss in TERMS:
        if lang == "Greek":
            w = strip_greek_diacritics(word.lower())
            note = f" (case-folded + diacritics stripped: {word} → {w})"
        else:
            w = word
            note = ""
        total, steps = weigh(w, lang)
        detail = "+".join(f"{ch}={v}" for ch, v in steps)
        hits = [n for n in LOADED if n == total]
        flag = f"  *** LOADED NUMBER HIT: {hits} ***" if hits else ""
        print(f"  {word} [{gloss}]{note}\n    {detail} = {total}{flag}")
        results.append((word, lang, gloss, total, steps))

    # -- Collision check among the five -------------------------------------
    print("\nCOLLISIONS AMONG D-THREAD TERMS:")
    by_value = {}
    for word, lang, gloss, total, steps in results:
        by_value.setdefault(total, []).append(f"{word} ({gloss.split(' — ')[0]})")
    any_collision = False
    for v, words in sorted(by_value.items()):
        if len(words) > 1:
            any_collision = True
            print(f"  {v}: {', '.join(words)}")
    if not any_collision:
        print("  none — all five weighings are distinct values.")

    # -- Loaded-number summary ----------------------------------------------
    print("\nLOADED-NUMBER SUMMARY:")
    for word, lang, gloss, total, steps in results:
        mark = "LOADED" if total in LOADED else "not loaded"
        print(f"  {word} = {total} — {mark}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
