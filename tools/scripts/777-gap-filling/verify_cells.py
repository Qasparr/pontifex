#!/usr/bin/env python3
# =============================================================================
# verify_cells.py — check a worker's cells are genuinely empty dot-runs in the
# 777 source before gap-filling work begins.
#
# Thelemic date: Tue 2026-10-13. 93.
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
# PONTIFEX-proposed 2026-10-13 (author: worker-08).
#
# METHOD (Scientific Illuminism): the share file is tab-separated
# COLUMN_ROMAN, ROW_LABEL, LINE_REF. For each cell this script reads the given
# source line, confirms it carries the expected row label, and confirms the
# column region is a dot-run (". . . ."), printing a per-cell verdict.
# Findings, never doctrine — the red pen rules.
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================
import re
import sys

# MECHANISM: the source is the plain-text Liber 777; never edited by workers.
SOURCE = "/home/hatch/workspace/liber777/777-crowley.txt"
DOTRUN = re.compile(r"\.\s\.\s\.")
ROWLAB = re.compile(r"^\s*(\d+|31 bis|32 bis)\b")


def verify(cells_path):
    """DOCTRINE: verify, don't trust. Returns list of (cell_id, ok, detail)."""
    # MECHANISM: split on "\n" ONLY — the file contains form feeds (\x0c) that
    # Python's str.splitlines() would count as extra lines, breaking LINE_REF.
    lines = open(SOURCE, encoding="utf-8").read().split("\n")
    results = []
    for raw in open(cells_path, encoding="utf-8"):
        raw = raw.strip()
        if not raw:
            continue
        # MECHANISM: tab-separated COLUMN_ROMAN, ROW_LABEL, LINE_REF ("line N").
        col, row, lineref = raw.split("\t")
        lineno = int(lineref.split()[-1])
        text = lines[lineno - 1]
        m = ROWLAB.match(text)
        row_ok = bool(m and m.group(1) == row)
        empty_ok = bool(DOTRUN.search(text))
        ok = row_ok and empty_ok
        detail = "row_label=%s dotrun=%s :: %s" % (
            "match" if row_ok else "MISMATCH",
            "empty" if empty_ok else "NOT-EMPTY",
            text.strip()[:80],
        )
        results.append(("%s/%s" % (col, row), ok, detail))
    return results


if __name__ == "__main__":
    # MECHANISM: cells file path from argv; prints verdicts, exits nonzero on failure.
    path = sys.argv[1] if len(sys.argv) > 1 else (
        "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/"
        "hidden_files/shares/worker-08-cells.txt")
    bad = 0
    for cell_id, ok, detail in verify(path):
        print(("PASS " if ok else "FAIL ") + cell_id + " — " + detail)
        bad += not ok
    sys.exit(1 if bad else 0)
