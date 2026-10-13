#!/usr/bin/env python3
# verify_worker17_cells.py — worker-17 cell-emptiness verifier (PONTIFEX 777 run)
# SCOPE: repo-exclusive — only useful for the 2026-10-13 cross-gematria-777
# gap-filling operation (worker-17's 11 cells).
#
# MECHANISM: for each of worker-17's assigned cells (COLUMN, ROW, LINE_REF),
# the script reads the exact source line from ~/workspace/liber777/777-crowley.txt
# and checks (1) the row label at line start matches the assigned ROW, and
# (2) a blank-cell dot-run ". . . . . . . . . ." is present in the expected
# column region (IX = before the column-X mystic number; XI = after it).
# DOCTRINE: trust, but verify — an assigned "empty cell" is only worked as
# empty after the source itself is shown to hold a blank there.
#
# Usage: python3 verify_worker17_cells.py [--source PATH]
# Exit 0 = all 11 cells verified empty; exit 1 = any mismatch.

import re
import sys

SOURCE = "/home/hatch/workspace/liber777/777-crowley.txt"

# (cell_id, column, row_label, line_no, column_region)
# column_region: "IX" -> dot-run must appear BEFORE the column-X mystic number
#                "XI" -> dot-run must appear AFTER the column-X mystic number
CELLS = [
    ("XI/0",     "XI", "0",      318, "XI"),
    ("XI/12",    "XI", "12",     357, "XI"),
    ("XI/13",    "XI", "13",     364, "XI"),
    ("XI/14",    "XI", "14",     365, "XI"),
    ("XI/21",    "XI", "21",     372, "XI"),
    ("XI/27",    "XI", "27",     378, "XI"),
    ("XI/30",    "XI", "30",     381, "XI"),
    ("XI/32",    "XI", "32",     383, "XI"),
    ("IX/0",     "IX", "0",      318, "IX"),
    ("IX/32 bis","IX", "32 bis", 384, "IX"),
    ("IX/31 bis","IX", "31 bis", 385, "IX"),
]

DOTRUN = ". . . . . . . . . ."


def check(cell_id, column, row_label, line_no, region, lines):
    line = lines[line_no - 1].rstrip("\n")
    # (1) row label at line start (bis rows read "32 bis", "31 bis")
    m = re.match(r"\s*(\d+(?:\s+bis)?)", line)
    if not m or m.group(1) != row_label:
        return False, "row label mismatch: line starts %r" % line[:24]
    # (2) dot-run in the expected column region, split on column X's number
    if region == "IX":
        # IX field sits before the column-X mystic number; for row 0 and the
        # bis rows there is no X number, so check the head of the line.
        head = line[:60]
        ok = DOTRUN in head
    else:
        # XI field sits after the column-X mystic number (rows 11-32 carry
        # one, e.g. row 12 -> 78). Row 0's X value is "0".
        nums = list(re.finditer(r"\d+", line))
        anchor = nums[1].end() if len(nums) > 1 else 0
        ok = DOTRUN in line[anchor:]
    if not ok:
        return False, "no dot-run in %s region" % region
    return True, "empty (dot-run in %s region)" % region


def main():
    src = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else SOURCE
    with open(src, encoding="utf-8") as fh:
        lines = fh.readlines()
    fails = 0
    for args in CELLS:
        ok, msg = check(*args, lines)
        print(("PASS " if ok else "FAIL ") + args[0] + "  line " + str(args[3]) + "  " + msg)
        fails += 0 if ok else 1
    print("---")
    print("%d/%d cells verified empty" % (len(CELLS) - fails, len(CELLS)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
