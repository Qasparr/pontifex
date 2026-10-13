#!/usr/bin/env python3
# =============================================================================
# fillings_emit.py — emit worker fillings CSV rows for the 777 gap-filling op.
# (author: worker-14, PONTIFEX 777 gap-filling, 2026-10-13)
#
# MECHANISM: takes a JSON list of filling dicts (one per proposal x bank
# weighing) and writes the operation's canonical CSV with its fixed header.
# Validates that every row carries the PONTIFEX flag and a worker id; quotes
# fields containing commas so the notes column survives a round trip.
# DOCTRINE: the script emits rows, it does not weigh — weighing belongs to
# pontifex/tools/ptk/weigh.py. Findings, never doctrine; the red pen rules.
#
# Usage: python3 fillings_emit.py fillings.json out.csv
# JSON schema per row: cell_id, column, row, column_title, row_meaning,
#   proposal, bank, value, tier, bridge, notes, flag, worker
# =============================================================================
import csv
import json
import sys

HEADER = ["cell_id", "column", "row", "column_title", "row_meaning",
          "proposal", "bank", "value", "tier", "bridge", "notes",
          "flag", "worker"]

REQUIRED_FLAG = "PONTIFEX-proposed 2026-10-13"


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: fillings_emit.py fillings.json out.csv")
    with open(sys.argv[1], encoding="utf-8") as fh:
        rows = json.load(fh)
    for i, r in enumerate(rows):
        missing = [c for c in HEADER if c not in r]
        if missing:
            sys.exit(f"row {i} missing columns: {missing}")
        if r["flag"] != REQUIRED_FLAG:
            sys.exit(f"row {i} has wrong flag: {r['flag']!r}")
        if not r["worker"]:
            sys.exit(f"row {i} has empty worker id")
    with open(sys.argv[2], "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow({c: r[c] for c in HEADER})
    print(f"wrote {len(rows)} rows to {sys.argv[2]}")


if __name__ == "__main__":
    main()
