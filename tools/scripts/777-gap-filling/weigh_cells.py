#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# weigh_cells.py — PONTIFEX 777 gap-filling weighing harness (worker-19).
#
# 93. "Every number is a shadow; the weighing is the substance." — scribe's gloss.
# Anno 2026 e.v. PONTIFEX operation, by order of Johnathan.
#
# MECHANISM: reads a small TSV of candidate weighings
#   (candidate<TAB>word<TAB>bank) and prints one line per weighing:
#   value, skipped characters via unknown(), and the letter-by-letter
#   breakdown, so the red pen can check every letter.
#   Banks: latin | agrippa | hebrew | hebrew_gadol | greek | arabic.
# DOCTRINE: NEVER retype a letter table — all tables come from ptk.weigh.
#   calibrate() must pass before any weighing is trusted.
# Usage: python3 weigh_cells.py weighings.tsv
#   (no argument: runs the built-in worker-19 candidate set)
# 93 93/93. ABRAHADABRA.

import sys
sys.path.insert(0, "/home/hatch/workspace/pontifex/tools")
from ptk import weigh

BANKS = {
    "latin":        (weigh.latin,        weigh.LATIN_ORDINAL),
    "agrippa":      (weigh.agrippa,      weigh.AGRIPPA),
    "hebrew":       (weigh.hebrew,       weigh.HEBREW),
    "hebrew_gadol": (weigh.hebrew_gadol, weigh.HEBREW_GADOL_FINALS),
    "greek":        (weigh.greek,        weigh.GREEK),
    "arabic":       (weigh.arabic,       weigh.ARABIC_ABJAD),
}

BUILTIN = """\
HEMLOCK\tCONIUM\tlatin
HEMLOCK\tCONIUM\tagrippa
HEMLOCK\tCONIUM MACULATUM\tlatin
HEMLOCK\tCONIUM MACULATUM\tagrippa
HEMLOCK\tκωνειον\tgreek
HEMLOCK\tראש\thebrew
SAGE\tSALVIA\tlatin
SAGE\tSALVIA\tagrippa
SAGE\tSALVIA OFFICINALIS\tlatin
SAGE\tSALVIA OFFICINALIS\tagrippa
SAGE\tמרווה\thebrew
GINGER\tZINGIBER\tlatin
GINGER\tZINGIBER\tagrippa
GINGER\tZINGIBER OFFICINALE\tlatin
GINGER\tZINGIBER OFFICINALE\tagrippa
GINGER\tזנגביל\thebrew
CAPSICUM\tCAPSICUM\tlatin
CAPSICUM\tCAPSICUM\tagrippa
CAPSICUM\tCAPSICUM ANNUUM\tlatin
CAPSICUM\tCAPSICUM ANNUUM\tagrippa
CAPSICUM\tפלפל\thebrew
CAPSICUM\tפלפלת\thebrew
MANDRAKE\tMANDRAGORA\tlatin
MANDRAKE\tMANDRAGORA\tagrippa
MANDRAKE\tMANDRAGORA OFFICINARUM\tlatin
MANDRAKE\tMANDRAGORA OFFICINARUM\tagrippa
MANDRAKE\tדודאים\thebrew
"""


def weigh_line(candidate, word, bank):
    fn, table = BANKS[bank]
    value = fn(word)
    skipped = weigh.unknown(word, table)
    pairs, total = weigh.breakdown(word, table)
    assert total == value
    letters = "+".join("%s=%d" % (ch, n) for ch, n in pairs)
    return "%s\t%s\t%s\t%d\tskipped=%s\t%s" % (
        candidate, word, bank, value,
        "".join(skipped) if skipped else "none", letters)


def main():
    if not weigh.calibrate():
        print("CALIBRATION FAILED — weigh nothing.", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        text = BUILTIN
    print("candidate\tword\tbank\tvalue\tskipped\tbreakdown")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        candidate, word, bank = line.split("\t")
        print(weigh_line(candidate, word, bank))


if __name__ == "__main__":
    main()
