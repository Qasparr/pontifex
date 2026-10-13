#!/usr/bin/env python3
# "Every word must be verified at the Anchorage — including the share file's."
# label_audit.py — 2026-10-13. 93.
#
# Authored for the PONTIFEX 777 gap-filling operation (worker-20).
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): worker-20's share file labeled four cells
# "XLIX" whose LINE_REFs actually land in columns L/LI (the XLIX rows there are
# FILLED). verify_cells.py (worker-08) checks row-label + dot-run but NOT the
# column header, so it passes such mislabels. This script audits ALL workers'
# cells files: for each LINE_REF it finds the nearest Roman-numeral column
# header above the line and flags any file label absent from that header.
# Findings, never doctrine — the red pen rules.
# Live, Love, and let Love, Live. — 93 93/93.
# All Rights Reserved, Without Prejudice.

import glob
import os
import re
import sys

# MECHANISM: fixed operation paths — the source is read-only, the shares dir
# holds the 24 machine-assigned cells files.
# DOCTRINE: read everything, write nothing outside stdout.
SOURCE = "/home/hatch/workspace/liber777/777-crowley.txt"
SHARES = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/hidden_files/shares"

# MECHANISM: column headers carry bare Roman numerals with periods.
HEADER_RE = re.compile(r"\b([IVXLCDM]{1,8})\.")
# MECHANISM: dotted abbreviations like "L.V.X" are body text, not headers —
# skip lines where numerals chain together with periods (worker-16 false-positive guard).
CHAIN_RE = re.compile(r"\b[IVXLCDM]\.[IVXLCDM]\.")


def header_above(lines, lineno, window=90):
    """Nearest line above `lineno` (1-based) holding 2+ Roman numerals."""
    # MECHANISM: walk upward; multi-numeral lines are table headers.
    # DOCTRINE: the header physically above the row governs the cell.
    for i in range(lineno - 2, max(lineno - window - 1, -1), -1):
        if CHAIN_RE.search(lines[i]):
            continue
        nums = HEADER_RE.findall(lines[i])
        if len(nums) >= 2:
            return i + 1, nums
    return None, []


def audit():
    """DOCTRINE: report every mismatch; silence on clean files is fine."""
    # MECHANISM: split("\n") only — form feeds (\x0c) in the source would
    # corrupt str.splitlines() numbering (worker-08's documented gotcha).
    with open(SOURCE, encoding="utf-8") as f:
        src = f.read().split("\n")
    bad = 0
    for path in sorted(glob.glob(os.path.join(SHARES, "worker-*-cells.txt"))):
        who = os.path.basename(path).replace("-cells.txt", "")
        for raw in open(path, encoding="utf-8"):
            raw = raw.strip()
            if not raw:
                continue
            col, row, lineref = raw.split("\t")
            ln = int(lineref.split()[-1])
            hln, hnums = header_above(src, ln)
            if hln and col not in hnums:
                bad += 1
                print(f"MISMATCH {who} {col}/{row} line {ln}: "
                      f"header above (line {hln}) shows {hnums}")
    print(f"\naudited {len(glob.glob(os.path.join(SHARES, 'worker-*-cells.txt')))} "
          f"share files, {bad} label/header mismatch(es)")


if __name__ == "__main__":
    # MECHANISM: no arguments — sweeps the whole shares directory.
    sys.exit(audit())
