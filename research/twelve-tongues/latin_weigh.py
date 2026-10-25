#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — latin_weigh.py — the Latin bank of the Twelve-Tongues survey
# Worker #3 of 12 (LATIN)
#
# Epigraph: "Every word, every letter, weighed in its own tongue first."
# — the method of this house.
#
# Thelemic date: ☉ in 18° 30′ Libra, ☽ in 25° 10′ Leo, dies solis,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's, open to the
# author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the shared corpus, weighed in Latin's two attested tables
#   (ordinal and Agrippa), will show whether "bridges" survive a change of
#   table — or are properties of (word, table) pairs rather than of words.
#   Method: weigh every term letter-by-letter in both tables, using the
#   tables exactly as pontifex/tables.py records them; verify the two
#   calibrations (AXONEME=77, CELL=32) by hand; flag collisions and
#   target-number hits; diff the tables.
#   Observation: recorded in the log below and in latin.md.
#   Result: delivered as findings, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Weigh the Twelve-Tongues shared corpus in Latin's two attested tables.

DOCTRINE: both tables are ATTESTED — recorded as the traditions hand them
down, never "improved" by the scribe. Latin ordinal (A=1..Z=26) is the
working Latin table; Agrippa's table (De occulta philosophia II.xix) is
the classical table with J=I, U=V per the classical alphabet.

MECHANISM: import the tables from pontifex.tables so there is exactly one
source of truth; weigh letter by letter; print every breakdown so the
audit trail (TRVVTH's demand) is complete.
"""

import csv
import os
import sys

# MECHANISM: the one source of truth — never re-key a table by hand.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import LATIN_ORDINAL, AGRIPPA, HEBREW

# -- The shared corpus -------------------------------------------------------
# MECHANISM: raw forms as the parent issued them. Normalization happens in
# normalize() and every choice is recorded in the CSV's notes column and in
# the provenance note of latin.md.
CORPUS = [
    "AXONEME", "OZ", "TRVVTH", "THELEMA", "AGAPE", "BABALON",
    "HERU-RA-HA", "ABRAHADABRA", "QIRA", "LIBERTY", "CELL",
]

# MECHANISM: target numbers the parent wants checked against in each table.
TARGETS = (418, 666, 777, 93, 77, 11)


def normalize(term):
    """Uppercase; strip hyphen (HERU-RA-HA → HERURAHHA); strip spaces.

    DOCTRINE: the hyphen is a separator, not a letter — it carries no value
    in either Latin table, so stripping loses no weight. The stripped form
    is what both tables weigh; the raw form travels in script_form's
    neighborhood (the term column keeps the raw spelling).
    """
    return term.upper().replace("-", "").replace(" ", "")


def check_table(table, spec):
    """Verify a table matches its doctrinal spec before any weighing.

    DOCTRINE: the instrument is checked before the measurement — a corrupted
    table would poison every number downstream.
    """
    # MECHANISM: spec is {letter: expected} for every letter.
    bad = [k for k, v in spec.items() if table.get(k) != v]
    return bad


def weigh(word, table):
    """Weigh a normalized word letter by letter in the given table.

    MECHANISM: letters only; anything not in the table is silence (not
    false weight), per pontifex/engine.py. Returns (value, breakdown).
    """
    breakdown = []
    total = 0
    for ch in word:
        if ch in table:
            v = table[ch]
            breakdown.append((ch, v))
            total += v
        # else: silence — non-table characters contribute nothing and are
        #       excluded from the total rather than zeroed silently.
    return total, breakdown


# -- The two attested Latin specs (for the instrument check) -----------------
# MECHANISM: the expected full tables, stated once so check_table can audit
# the imported tables byte-for-byte.
ORDINAL_SPEC = {chr(ord('A') + i): i + 1 for i in range(26)}
AGRIPPA_SPEC = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 9, 'K': 10, 'L': 20, 'M': 30, 'N': 40, 'O': 50,
    'P': 60, 'Q': 70, 'R': 80, 'S': 90, 'T': 100, 'U': 200, 'V': 200,
    'X': 300, 'Y': 400, 'Z': 500,
}

# -- Notes per term (the record that travels with each row) ------------------
# DOCTRINE: what the weighing could not say, or what the reader must know
# to read the number honestly, is written here — never hidden.
NOTES = {
    "AXONEME": "Calibrator #1: 1+24+15+14+5+13+5=77, verified letter-by-letter.",
    "CELL": "Calibrator #2: 3+5+12+12=32 in Latin ordinal, verified letter-by-letter.",
    "OZ": ("Also the Latin transliteration of the Hebrew-bank reference term עז "
           "(ע=70, ז=7, total 77 — attested mispar hechrechi; the Hebrew bank's "
           "term, weighed by the Hebrew worker, not here)."),
    "TRVVTH": ("Contains VV. Latin ordinal: V=22 each. Agrippa: U/V=200 each — "
               "the classical U=V merger is in the table as Agrippa published it."),
    "HERU-RA-HA": ("Raw form hyphenated (HERU-RA-HA); hyphen stripped before "
                   "weighing — a separator, not a letter, so no weight is lost."),
    "THELEMA": "",
    "AGAPE": "",
    "BABALON": "",
    "ABRAHADABRA": "",
    "QIRA": "",
    "LIBERTY": "",
}


def main():
    # -- HYPOTHESIS: the instruments are sound --------------------------------
    # METHOD: audit the imported tables against their doctrinal specs.
    print("=== STEP 1: instrument check ===")
    bad_ord = check_table(LATIN_ORDINAL, ORDINAL_SPEC)
    bad_agr = check_table(AGRIPPA, AGRIPPA_SPEC)
    print("Latin ordinal table audit:", "CLEAN" if not bad_ord else bad_ord)
    print("Agrippa table audit:     ", "CLEAN" if not bad_agr else bad_agr)
    assert not bad_ord and not bad_agr, "TABLE AUDIT FAILED — abort weighing."

    # -- METHOD: weigh everything, both tables, letter by letter -------------
    print("\n=== STEP 2: weighings ===")
    rows = []  # (term, raw, normalized, table_name, tier, value, breakdown)
    results = {}  # term -> {table: value}
    for term in CORPUS:
        norm = normalize(term)
        results[term] = {}
        for tname, table in (("latin_ordinal", LATIN_ORDINAL),
                             ("agrippa", AGRIPPA)):
            value, breakdown = weigh(norm, table)
            results[term][tname] = value
            rows.append((term, norm, tname, "ATTESTED", value, breakdown))
        bd_o = " + ".join("%s=%d" % (c, v) for c, v in rows[-2][5])
        bd_a = " + ".join("%s=%d" % (c, v) for c, v in rows[-1][5])
        print("%-12s -> %-10s  ordinal: %4d  [%s]" % (term, norm, rows[-2][4], bd_o))
        print("%-12s -> %-10s  agrippa: %4d  [%s]" % ("", "", rows[-1][4], bd_a))

    # -- OBSERVATION: check the two calibrations by hand ----------------------
    print("\n=== STEP 3: calibrations ===")
    ax = results["AXONEME"]["latin_ordinal"]
    cl = results["CELL"]["latin_ordinal"]
    print("AXONEME ordinal: %d (expected 77) -> %s" % (ax, "PASS" if ax == 77 else "FAIL"))
    print("CELL ordinal:    %d (expected 32) -> %s" % (cl, "PASS" if cl == 32 else "FAIL"))
    assert ax == 77 and cl == 32, "CALIBRATION FAILED"

    # -- METHOD: collisions within each table ---------------------------------
    print("\n=== STEP 4: collisions ===")
    for tname in ("latin_ordinal", "agrippa"):
        buckets = {}
        for term in CORPUS:
            buckets.setdefault(results[term][tname], []).append(term)
        hits = {v: ts for v, ts in buckets.items() if len(ts) > 1}
        print(tname, "collisions:", hits if hits else "NONE")

    # -- METHOD: target-number hits --------------------------------------------
    print("\n=== STEP 5: target hits ===")
    for tname in ("latin_ordinal", "agrippa"):
        found = [(t, results[t][tname]) for t in CORPUS
                 if results[t][tname] in TARGETS]
        print(tname, "target hits:", found if found else "NONE")

    # -- METHOD: ordinal vs Agrippa agreement ----------------------------------
    print("\n=== STEP 6: table comparison ===")
    agree = [t for t in CORPUS if results[t]["latin_ordinal"] == results[t]["agrippa"]]
    print("terms agreeing in both tables:", agree if agree else "NONE")

    # -- METHOD: write the CSV -------------------------------------------------
    # MECHANISM: one row per term per table; the עז reference row rides along
    # as an informational row so the parent's synthesis sees the Hebrew-side
    # anchor of the OZ line. Its table_used is honest about where it belongs.
    out_dir = os.path.expanduser("~/workspace/pontifex/research/twelve-tongues")
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, "latin-values.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["term", "language", "script_form",
                    "transliteration_convention", "table_used",
                    "provenance_tier", "value", "mergers_or_loss", "notes"])
        for term, norm, tname, tier, value, breakdown in rows:
            translit = "hyphen-stripped (HERURAHA)" if term == "HERU-RA-HA" else "none needed (Latin script native)"
            loss = ("none — 26-letter 1:1 weighing; hyphen is a separator with no value"
                    if term != "HERU-RA-HA"
                    else "none — hyphen stripped; separators carry no value in either Latin table")
            w.writerow([term, "Latin", term, translit, tname, tier, value,
                        loss, NOTES.get(term, "")])
        # The Hebrew-bank reference row: עז weighed in mispar hechrechi.
        # DOCTRINE: this row is the Hebrew bank's term — recorded here only so
        # the synthesis can see what the OZ line bridges to; not a Latin weighing.
        hz_val = sum(HEBREW[ch] for ch in "עז")
        w.writerow(["עז", "Hebrew", "עז",
                    "n/a — Hebrew bank's term, reference only",
                    "hebrew_attested (reference; not weighed in this bank)",
                    "ATTESTED", hz_val,
                    "none — reference row",
                    "ע=70 + ז=7 = 77. This is the number the Latin OZ line is checked against."])
    print("\nCSV written:", csv_path)

    # -- RESULT: summary table for the log -------------------------------------
    print("\n=== STEP 7: summary ===")
    print("%-12s %8s %8s" % ("term", "ordinal", "agrippa"))
    for term in CORPUS:
        print("%-12s %8d %8d" % (term, results[term]["latin_ordinal"],
                                 results[term]["agrippa"]))
    print("\n93. Done — findings to the red pen.")


if __name__ == "__main__":
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
