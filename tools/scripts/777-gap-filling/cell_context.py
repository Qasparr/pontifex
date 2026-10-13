#!/usr/bin/env python3
# =============================================================================
# cell_context.py -- print one 777 cell in its full row context.
#
# By the PONTIFEX 777 gap-filling operation, worker-15 (2026-10-13).
# REPO-EXCLUSIVE: hardcoded to ~/workspace/liber777/777-crowley.txt and the
# TABLE OF CORRESPONDENCES layout (Roman-numeral column headers, dot-run
# empties, rows 0-32 plus 31 bis / 32 bis). Useless outside this operation.
#
# METHOD: the worker's share file gives (COLUMN_ROMAN, ROW_LABEL, LINE_REF).
# This prints the column-title header lines above the target plus the target
# line itself, so the worker can verify (a) the cell is really a dot-run
# empty, (b) the column title, and (c) the row's meaning from its neighbours
# -- without re-reading the whole table by hand.
#
# Usage: cell_context.py LINE_REF [CONTEXT_LINES]
# Example: cell_context.py 654
# =============================================================================

import sys

SOURCE = "/home/hatch/workspace/liber777/777-crowley.txt"


def main(argv):
    if len(argv) < 2 or not argv[1].isdigit():
        print("usage: cell_context.py LINE_REF [CONTEXT_LINES]")
        return 2
    target = int(argv[1])
    ctx = int(argv[2]) if len(argv) > 2 else 2
    with open(SOURCE, encoding="utf-8") as f:
        lines = f.readlines()
    # The column-title header for this table block sits ~7-10 lines above
    # the first row; find the nearest "XXXIII." header at or above target.
    header_at = None
    for i in range(target - 1, max(0, target - 40), -1):
        if "XXXIII." in lines[i - 1]:
            header_at = i
            break
    if header_at:
        print(f"--- column header (line {header_at}) ---")
        for i in range(header_at, min(header_at + 8, target - ctx)):
            print(f"{i:5d}: {lines[i-1].rstrip()}")
        print("---")
    lo = max(1, target - ctx)
    hi = min(len(lines), target + ctx)
    for i in range(lo, hi + 1):
        marker = " >>> " if i == target else "     "
        print(f"{marker}{i:5d}: {lines[i-1].rstrip()}")
    line = lines[target - 1]
    if ". . . ." in line:
        print("VERDICT: dot-run empty cell present on this line.")
    else:
        print("VERDICT: no dot-run on this line -- check column alignment by hand.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
