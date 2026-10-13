#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weigh_jinn_kings.py — reproduce worker-03's Arabic abjad weighings for the
proposed XLVII ("Kings and Princes of the Jinn") fillings, 777 gap-filling
operation, 2026-10-13.

Epigraph: "Every number is infinite; there is no difference." — Liber AL I:4
Date: 2026-10-13. 93.
Authorship: proposed by the PONTIFEX 777 operation (worker-03); findings,
never doctrine — the red pen rules.
Method (Scientific Illuminism): hypothesis (the seven planetary day-kings
of the Arabic grimoire tradition fill the planetary rows of the Jinn
column) → experiment (weigh each name in its native tongue, Arabic abjad,
via ptk; calibrate() first; unknown() on every weighing) → observation
(values + skipped characters below) → result (recorded in
worker-03-fillings.csv with tiers; bridges assessed per doctrine).
Motto: TRVVTH alone has absolute authority.

MECHANISM: imports ptk.weigh (never retypes a letter table), runs
calibrate() as a gate, then weighs المذهب (Sun king), الأحمر (Mars king),
ميمون (Saturn king) with breakdown() and unknown() so the audit trail is
complete. Prints a tab-separated report.

DOCTRINE: Arabic HAS an attested abjad table, so no Hebrew fallback is
used (each word weighed in its own tongue). The hamza-alif U+0623 in
الأحمر is absent from ptk's table and skipped by the engine (value 279);
conventional abjad counts it as alif=1 (value 280) — both are reported;
a spread, never a single number.
"""
import sys

sys.path.insert(0, "/home/hatch/workspace/pontifex/tools/ptk")
import weigh  # noqa: E402

# MECHANISM: the instrument gate — refuse to weigh if the engine is unwell.
assert weigh.calibrate(), "ptk calibrate() failed; weigh nothing."

# DOCTRINE: candidate, row, and the lore attribution each recorded.
CANDIDATES = [
    ("XLVII/27", "al-Ahmar", "الأحمر", "Mars/Tuesday king"),
    ("XLVII/30", "al-Mudhhib", "المذهب", "Sun/Sunday king"),
    ("XLVII/32", "Maymun", "ميمون", "Saturn/Saturday king"),
]

print("cell\tproposal\tarabic\tvalue_ptk\tskipped_by_engine\tvalue_conventional\tnote")
for cell, latin, arabic, office in CANDIDATES:
    # MECHANISM: engine value; unknown() makes skipped characters visible.
    value = weigh.arabic(arabic)
    skipped = weigh.unknown(arabic, weigh.ARABIC_ABJAD)
    pairs, total = weigh.breakdown(arabic, weigh.ARABIC_ABJAD)
    assert total == value, "breakdown disagrees with arabic()"
    detail = " + ".join("%s=%d" % (c, n) for c, n in pairs)
    # DOCTRINE: skipped hamza-alif conventionally weighs 1 (as alif).
    conventional = value + (1 if "أ" in skipped else 0)
    print("%s\t%s\t%s\t%d\t%s\t%d\t%s | %s = %d"
          % (cell, latin, arabic, value,
             ",".join(skipped) if skipped else "-",
             conventional, office, detail, value))
