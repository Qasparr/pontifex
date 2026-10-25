#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — weigh_english.py — the English bank weighing (worker #5 of 12)
# The twelve-tongues correspondence research, English language leg.
#
# Epigraph: "Measure twice, cut once." — the carpenter's proverb.
#
# Thelemic date: ☉ in 18° Libra, dies Solis, Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure. This instrument is drafted by the scribe
# for the author's red pen; the doctrine is his, the mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the shared corpus weighs in English ordinal (A=1..Z=26) on
#   the ATTESTED native table, with no mergers and no silent loss; the
#   stipulated spelling TRVVTH (VV, not W) is load-bearing.
#   Method: uppercase, strip the hyphen in HERU-RA-HA, weigh letter by
#   letter against pontifex.tables.LATIN_ORDINAL, recompute the two
#   calibration anchors (AXONEME=77, CELL=32) from the letter breakdowns.
#   Observation: reported by the script's own stdout — every letter's value.
#   Result: the CSV in english-values.csv, one row per term, tier ATTESTED.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the shared corpus in the English bank.

DOCTRINE: English ordinal A=1..Z=26 is NATIVE for English words (settled
with the author 2026-10-07) — numerically identical to the repo's
LATIN_ORDINAL table, but its provenance story is the native table,
ATTESTED as the working English table. The scribe does not invent a
parallel table silently; the script imports the repo table so the numeric
identity with the Latin worker's table is on the record.

MECHANISM: one function weighs one term; the letter-by-letter breakdown is
printed so the calibrations are audited in the log, not asserted.
"""

import csv
import os
import sys

# MECHANISM: reach the repo's own table — do not re-declare it in silence.
# DOCTRINE: importing (not copying) the table is what makes the
# English<->Latin numeric identity an observed fact rather than a claim.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import LATIN_ORDINAL  # noqa: E402

# The shared corpus, weighed as spelled; HERU-RA-HA's hyphen is stripped by
# stated normalization (see NORMALIZATION below), TRVVTH keeps its VV.
CORPUS = [
    "AXONEME", "OZ", "TRVVTH", "THELEMA", "AGAPE", "BABALON",
    "HERU-RA-HA", "ABRAHADABRA", "QIRA", "LIBERTY", "CELL",
]

TARGETS = {418, 666, 777, 93, 77, 11}


def weigh(term):
    """Weigh one term; return (normalized, breakdown, total).

    MECHANISM: uppercase is a no-op guard (the corpus is already uppercase);
    the hyphen strip is the single stated normalization, recorded per row.
    """
    normalized = term.upper().replace("-", "")
    breakdown = [(ch, LATIN_ORDINAL[ch]) for ch in normalized]
    total = sum(v for _, v in breakdown)
    return normalized, breakdown, total


def main():
    out_dir = os.path.expanduser("~/workspace/pontifex/research/twelve-tongues")
    os.makedirs(out_dir, exist_ok=True)

    rows = []
    for term in CORPUS:
        normalized, breakdown, total = weigh(term)
        # OBSERVATION: the audit trail — every letter's value on the record.
        seq = "+".join("%s%d" % (ch, v) for ch, v in breakdown)
        print("%s -> %s = %d" % (term, seq, total))
        norm_note = ("hyphen stripped from HERU-RA-HA"
                     if "-" in term else "none")
        rows.append({
            "term": term,
            "language": "English",
            "script_form": term,
            "transliteration_convention": "native script; no transliteration",
            "table_used": "LATIN_ORDINAL — English ordinal A=1..Z=26 (native)",
            "provenance_tier": "ATTESTED",
            "value": total,
            "mergers_or_loss": "none — 26 letters, 26 distinct values",
            "notes": "normalized: %s; breakdown %s=%d%s" % (
                norm_note, seq, total,
                "; TARGET HIT %d" % total if total in TARGETS else ""),
        })

    # RESULT: the CSV, machine-readable, one row per term.
    path = os.path.join(out_dir, "english-values.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote %s (%d rows)" % (path, len(rows)))


if __name__ == "__main__":
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
