#!/usr/bin/env python3
# =============================================================================
# "If it isn't on the page, it didn't happen." — the desk
#
# Thelemic date: Tue 2026-11-24 (Dies Martis), Sol in Sagittario,
# Anno V:xii e.n.
#
# 93.
#
# extract_777_register.py — PHASE 1 of the 777 Verification Tabvla
# (founder's commission, 2026-11-24 13:59 EST: "verify the filled
# 777 gaps in the proven tongues; produce them in the full listing,
# in Tabvla fashion, and MAGVS").
#
# By Johnathan 'Qasparr' Monroe (Greek, -ARR, All Rights Reserved,
# Without Prejudice). Authorship attributed exclusively to
# Johnathan 'Qasparr' Monroe.
#
# METHOD (Scientific Illuminism):
#   Inputs    — the goal-files copy of 777-REVISED.md (154,961
#               bytes; the seat of record for this goal's files).
#               The pontifex research copy PARTS from it: it carries
#               the append-only Orthography-Correction apparatus of
#               2026-10-27 (44 correctio notes + 1 respell note +
#               respelled proposals and reweighed value rows) that
#               the goal copy lacks. The commission directs the
#               goal-files copy; the parting is reported, never
#               silently merged. 777-REVISED.md is NEVER edited by
#               this work — not a character, in either copy.
#   Processes — split the master on its ## column headers and ###
#               section headers; split each section on its
#               **Proposal:** blocks; lift every bank-table row as
#               one claim; normalize each printed bank label to the
#               engine bank it names (the mapping is printed below
#               and fails loudly on an unmapped label); freeze the
#               register as JSON (nested) + CSV (one row per claim,
#               plus one row per claimless section).
#   Outputs   — 777-verification-register.json / .csv beside this
#               script, and the extraction battery's counts on
#               stdout.
#   Tolerances— the battery proves 221 sections in = 221 sections
#               out, 285 proposals out (the count of **Proposal:**
#               lines in the master), 504 claim rows out (the count
#               of bank-table data rows in the master, taken by an
#               independent line count), and the subset relation
#               against the original machine ledger fillings.csv:
#               the ledger's 590 rows are the workers' working
#               record, a SUPERSET of the printed tables (574
#               ledger claim rows against 504 printed; only 16
#               ledger rows for the 86 claimless sections). Every
#               printed claim must appear in the ledger; the
#               deltas print as findings. Any failure of the
#               counts or the subset relation fails the run loudly.
#
# MECHANISM NOTES:
#  * A section with no proposal is still a row: the 85 certified
#    INTENTIONALLY EMPTY sections and the one
#    UNFILLABLE_TRANSCRIPTION_GAP section (CLXXXIV/10) enter the
#    register as claimless sections, claim = NONE STATED.
#  * One claim in the master prints a compound value —
#    "240 (245 incl. ة=5)" — the extractor takes the stated main
#    value (240) as the claim and carries the parenthetical as the
#    claim's variant note, verbatim.
#  * Bank labels are heterogeneous in the master (case, hyphens,
#    parentheticals). The mapping below is the desk's reading of
#    what each label names; it is printed here so the parent can
#    audit every assignment.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import json
import re
import sys
from pathlib import Path

BASE = Path.home() / "workspace/pontifex/research/777-gap-filling"
MASTER = (Path.home() / "workspace/goals/cross-gematria-777-gap-filling"
          / "files" / "777-REVISED.md")
LEDGER = (Path.home() / "workspace/goals/cross-gematria-777-gap-filling"
          / "hidden_files" / "fillings.csv")
OUT_JSON = BASE / "777-verification-register.json"
OUT_CSV = BASE / "777-verification-register.csv"

# DOCTRINE: the label mapping — printed, auditable, and closed.
# An unmapped label fails the run; a silent default would be a lie.
BANK_MAP = {
    "HEBREW": "hebrew",
    "hebrew": "hebrew",
    "HEBREW-gadol": "hebrew_gadol",
    "HEBREW-GADOL": "hebrew_gadol",
    "hebrew_gadol": "hebrew_gadol",
    "HEBREW-fallback": "hebrew_fallback",
    "hebrew_pinyin_fallback": "hebrew_pinyin_fallback",
    "AGRIPPA": "agrippa",
    "agrippa": "agrippa",
    "LATIN-agrippa": "agrippa",
    "LATIN": "latin_ordinal",
    "LATIN-ordinal": "latin_ordinal",
    "LATIN_ORDINAL": "latin_ordinal",
    "LATIN-ORDINAL": "latin_ordinal",
    "latin": "latin_ordinal",
    "latin_ordinal": "latin_ordinal",
    "latin-ordinal": "latin_ordinal",
    "LATIN_ORDINAL (IAST transliteration, macrons stripped)":
        "latin_ordinal",
    "latin(phrase)": "latin_ordinal",
    "GREEK": "greek",
    "greek": "greek",
    "ARABIC": "arabic_abjad",
    "arabic": "arabic_abjad",
    "ARABIC abjad": "arabic_abjad",
    "ARABIC_ABJAD": "arabic_abjad",
    "ARABIC abjad (ptk engine)": "arabic_abjad",
    "ARABIC abjad (conventional; hamza-alif=1)": "arabic_abjad",
    "ENGLISH_ORDINAL": "english_ordinal",
    "ENGLISH": "english_ordinal",
    "stroke_count_prc": "stroke_count_prc",
    "COPTIC": "coptic",
}

ROW_RE = re.compile(r"^\| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")
FLAG_RE = re.compile(r"\s*`\[PONTIFEX-proposed [^\]]*\]`\s*$")


def split_sections(text):
    """MECHANISM: walk the lines once, tracking the current ##
    column header; every ### line opens a section. Returns a list
    of dicts with the header line and the body lines."""
    sections = []
    column = ""
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            column = line[3:].strip()
            current = None
            continue
        if line.startswith("### "):
            current = {"column": column, "header": line[4:].strip(),
                       "body_lines": []}
            sections.append(current)
            continue
        if current is not None:
            current["body_lines"].append(line)
    return sections


def parse_section(idx, sec):
    """MECHANISM: one section -> its register entry. The cell id is
    the header text before the first em dash; the kind is read off
    the body's own markers; proposals split on **Proposal:**."""
    header = sec["header"]
    cell_id = header.split(" — ")[0].strip()
    body = "\n".join(sec["body_lines"])
    entry = {
        "section_idx": idx,
        "cell_id": cell_id,
        "column": sec["column"],
        "header": header,
        "kind": None,
        "proposals": [],
        "section_text": body.strip(),
    }
    parts = body.split("**Proposal:**")
    intro = parts[0]
    if "UNFILLABLE" in intro:
        entry["kind"] = "TRANSCRIPTION_GAP"
    elif len(parts) == 1 and "INTENTIONALLY EMPTY" in intro:
        entry["kind"] = "INTENTIONALLY_EMPTY"
    elif len(parts) > 1:
        entry["kind"] = "FILLED"
    else:
        entry["kind"] = "OTHER"
    for p_idx, block in enumerate(parts[1:]):
        lines = block.splitlines()
        proposal_raw = FLAG_RE.sub("", lines[0]).strip()
        claims = []
        for line in lines:
            m = ROW_RE.match(line.strip())
            if not m:
                continue
            label, value_cell, tier = (c.strip() for c in m.groups())
            if label == "Bank" or set(label) <= set("-: "):
                continue
            vm = re.match(r"^(\d+)\s*(.*)$", value_cell)
            if not vm:
                raise SystemExit(
                    f"unparseable value cell {value_cell!r} in "
                    f"section {cell_id}")
            claims.append({
                "claim_idx": len(claims),
                "bank_label_raw": label,
                "bank_engine": BANK_MAP.get(label),
                "claimed_value": int(vm.group(1)),
                "claim_variant_note": vm.group(2).strip(),
                "tier_printed": tier,
            })
            if BANK_MAP.get(label) is None:
                raise SystemExit(
                    f"unmapped bank label {label!r} in section "
                    f"{cell_id} — extend BANK_MAP openly or fail")
        bridge_m = re.search(r"(?m)^Bridge: (.*)$", block)
        notes_m = re.search(r"(?ms)^Notes: (.*?)(?=^Worker:|\Z)", block)
        worker_m = re.search(r"(?m)^Worker: (\S+)", block)
        entry["proposals"].append({
            "proposal_idx": p_idx,
            "proposal_raw": proposal_raw,
            "claims": claims,
            "bridge": bridge_m.group(1).strip() if bridge_m else "",
            "notes": notes_m.group(1).strip() if notes_m else "",
            "worker": worker_m.group(1) if worker_m else "",
        })
    return entry


def main():
    text = MASTER.read_text(encoding="utf-8")
    raw_sections = split_sections(text)
    entries = [parse_section(i, s) for i, s in enumerate(raw_sections)]

    # MECHANISM: the extraction battery — independent counts taken
    # straight off the master's text, not off the parse.
    n_sections_text = len(re.findall(r"(?m)^### ", text))
    n_proposals_text = text.count("**Proposal:**")
    n_rows_text = 0
    for line in text.splitlines():
        if line.startswith("|") and "Bank" not in line \
                and not set(line) <= set("|-: "):
            n_rows_text += 1
    n_sections = len(entries)
    n_proposals = sum(len(e["proposals"]) for e in entries)
    n_claims = sum(len(p["claims"]) for e in entries
                   for p in e["proposals"])
    print(f"sections: text={n_sections_text} parsed={n_sections}")
    print(f"proposals: text={n_proposals_text} parsed={n_proposals}")
    print(f"claim rows: text={n_rows_text} parsed={n_claims}")
    assert n_sections == n_sections_text == 221, "section count fails"
    assert n_proposals == n_proposals_text, "proposal count fails"
    assert n_claims == n_rows_text, "claim-row count fails"

    # MECHANISM: reconciliation against the original machine
    # ledger. OBSERVED RELATION (reported, not assumed): the
    # ledger is the workers' working record and is a SUPERSET of
    # the printed tables — it carries weighings that never reached
    # the printed MD, and it records only some claimless sections.
    # The hard check is the subset relation: every claim printed
    # in the MD must appear in the ledger (same cell, same value).
    # The count deltas print as findings.
    import collections
    ledger_rows = list(csv.DictReader(LEDGER.open(encoding="utf-8")))
    ledger_claim_rows = [r for r in ledger_rows if r["bank"] != "-"]
    ledger_cell_rows = [r for r in ledger_rows if r["bank"] == "-"]
    claimless = [e for e in entries if not e["proposals"]]
    print(f"ledger: total={len(ledger_rows)} "
          f"claim rows={len(ledger_claim_rows)} "
          f"claimless rows={len(ledger_cell_rows)}")
    print(f"register claimless sections={len(claimless)}")
    assert len(ledger_rows) == 590
    md_counter = collections.Counter()
    for e in entries:
        for p in e["proposals"]:
            for c in p["claims"]:
                md_counter[(e["cell_id"], c["claimed_value"])] += 1
    ledger_counter = collections.Counter()
    for r in ledger_claim_rows:
        # MECHANISM: the ledger prints one compound value verbatim
        # ("240 (245 incl. ة=5)") — the same leading-int parse the
        # extractor applies to the MD side normalizes both.
        vm = re.match(r"^(\d+)", r["value"])
        key = int(vm.group(1)) if vm else r["value"]
        ledger_counter[(r["cell_id"], key)] += 1
    missing = md_counter - ledger_counter
    extra = ledger_counter - md_counter
    print(f"MD claims missing from ledger: {sum(missing.values())}")
    print(f"ledger weighings beyond the printed tables: "
          f"{sum(extra.values())}")
    assert sum(missing.values()) == 0, \
        "printed claims missing from the working ledger — parse fails"
    ledger_cells = sorted(set(r["cell_id"] for r in ledger_rows))
    register_cells = sorted(set(e["cell_id"] for e in entries))
    print("cell sets equal:", ledger_cells == register_cells)

    kinds = {}
    for e in entries:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    print("section kinds:", kinds)

    OUT_JSON.write_text(json.dumps(entries, ensure_ascii=False,
                                   indent=1), encoding="utf-8")
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["section_idx", "cell_id", "column", "section_kind",
                    "proposal_idx", "proposal_raw", "claim_idx",
                    "bank_label_raw", "bank_engine", "claimed_value",
                    "claim_variant_note", "tier_printed", "bridge",
                    "worker"])
        for e in entries:
            if not e["proposals"]:
                w.writerow([e["section_idx"], e["cell_id"], e["column"],
                            e["kind"], "", "", "", "", "", "", "", "",
                            "", ""])
            for p in e["proposals"]:
                for c in p["claims"]:
                    w.writerow([e["section_idx"], e["cell_id"],
                                e["column"], e["kind"],
                                p["proposal_idx"], p["proposal_raw"],
                                c["claim_idx"], c["bank_label_raw"],
                                c["bank_engine"], c["claimed_value"],
                                c["claim_variant_note"],
                                c["tier_printed"], p["bridge"],
                                p["worker"]])
    print(f"wrote {OUT_JSON} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
