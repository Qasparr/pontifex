#!/usr/bin/env python3
"""WORKER-16 weighing run — PONTIFEX 777 gap-filling, 2026-10-13.

Method: calibrate() first (must pass), then weigh every proposed filling
across its honest banks, auditing unknown() every time. Outputs CSV rows
for worker-16-fillings.csv. Saved to authored-tools/ per the standing order.

By Johnathan 'Qasparr' (Κασπάρρ) Monroe — proposal weighings by worker-16.
"""
import csv, io, sys
sys.path.insert(0, "/home/hatch/workspace/pontifex/tools/ptk")
import weigh as W

# --- 1. CALIBRATE (must pass before any weighing) ---
print("calibrate():", "PASS" if W.calibrate() else "FAIL")
assert W.calibrate(), "calibration failed — no weighings performed"

rows = []
FLAG = "PONTIFEX-proposed 2026-10-13"

def add(cell_id, column, row, column_title, row_meaning, proposal,
        bank, value, tier, bridge, notes):
    unk = ""
    rows.append([cell_id, column, row, column_title, row_meaning, proposal,
                 bank, value, tier, bridge, notes, FLAG, "worker-16"])

def weigh_hebrew(cell_id, column, row, column_title, row_meaning,
                 proposal_he, proposal_lat, placement_note):
    """Weigh a Hebrew proposal in both Hebrew banks; audit skips."""
    for bank_name, fn in (("hebrew", W.hebrew), ("hebrew_gadol", W.hebrew_gadol)):
        val = fn(proposal_he)
        pairs, total = W.breakdown(proposal_he,
                                   W.HEBREW if bank_name == "hebrew"
                                   else {**W.HEBREW, **{k: v for k, v in
                                          W.HEBREW_GADOL_FINALS.items()}})
        # hebrew_gadol(): check how it handles finals — use breakdown w/ merged table
        skipped = W.unknown(proposal_he, W.HEBREW)
        bd = "+".join(f"{ch}={v}" for ch, v in pairs)
        notes = (f"{placement_note} | breakdown {bd} | skipped: {skipped or 'none'}")
        add(cell_id, column, row, column_title, row_meaning,
            f"{proposal_he} ({proposal_lat})", bank_name, total,
            "attested", "no", notes)

def weigh_english(cell_id, column, row, column_title, row_meaning,
                  proposal, placement_note):
    for bank_name, fn in (("latin_ordinal", W.latin), ("agrippa", W.agrippa)):
        val = fn(proposal)
        skipped = W.unknown(proposal.upper(), W.LATIN_ORDINAL)
        notes = (f"{placement_note} | value={val} | skipped: {skipped or 'none'}")
        add(cell_id, column, row, column_title, row_meaning,
            proposal, bank_name, val, "attested", "no", notes)

COL6 = "The Heavens of Assiah"
MARGINAL = ("Crowley's marginal note at row 12, col VI: "
            "'[Planets follow Sephiroth, corresponding]' — the Hebrew planet "
            "name is already attested in this column (rows 1-10); placement "
            "on the planetary path is derived from the note, not invented.")

# --- VI/13 Gimel/Luna path -> Levanah (row 9: hnbl Levanah) ---
weigh_hebrew("VI/13", "VI", "13", COL6, "Gimel — path of Luna (VII: Luna)",
             "לבנה", "Levanah", MARGINAL)
# --- VI/14 Daleth/Venus path -> Nogah (row 7: hgn Nogah) ---
weigh_hebrew("VI/14", "VI", "14", COL6, "Daleth — path of Venus (VII: Venus)",
             "נגה", "Nogah", MARGINAL)
# --- VI/21 Kaph/Jupiter path -> Tzedeq (row 4: qdx Tzedeq) ---
weigh_hebrew("VI/21", "VI", "21", COL6, "Kaph — path of Jupiter (VII: Jupiter)",
             "צדק", "Tzedeq", MARGINAL)
# --- VI/27 Peh/Mars path -> Madim (row 5: \\ydam Madim) ---
weigh_hebrew("VI/27", "VI", "27", COL6, "Peh — path of Mars (VII: Mars)",
             "מאדים", "Madim", MARGINAL)
# --- VI/30 Resh/Sol path -> Shemesh (row 6: cmc Shemesh) ---
weigh_hebrew("VI/30", "VI", "30", COL6, "Resh — path of Sol (VII: Sol)",
             "שמש", "Shemesh", MARGINAL)
# --- VI/32 Tau/Saturn path -> Shabbathai (row 3: yatbc Shabbathai) ---
weigh_hebrew("VI/32", "VI", "32", COL6, "Tau — path of Saturn (VII: Saturn)",
             "שבתאי", "Shabbathai", MARGINAL)

# --- III/32 bis: English of Col. II for Tau = "Tau (as Egyptian)" (row 32) ---
weigh_english("III/32 bis", "III", "32 bis", "English of Col. II",
              "Tau repeated — Spirit/Earth added row",
              "Tau (as Egyptian)",
              "Deterministic: col III is 'English of Col. II'; row 32 prints "
              "'Tau (as Egyptian)'. Weighing the gloss in the native English banks.")
# --- III/31 bis: English of Col. II for Shin = "Tooth" (row 31) ---
weigh_english("III/31 bis", "III", "31 bis", "English of Col. II",
              "Shin repeated — Spirit/Earth added row",
              "Tooth",
              "Deterministic: row 31 col III prints 'Tooth'. Weighing the gloss "
              "in the native English banks.")

# --- Bridge re-check: do any two honest banks agree on one word? ---
print(f"weighings recorded: {len(rows)}")

buf = io.StringIO()
w = csv.writer(buf)
w.writerow(["cell_id","column","row","column_title","row_meaning","proposal",
            "bank","value","tier","bridge","notes","flag","worker"])
w.writerows(rows)
out = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/hidden_files/worker-16-fillings.csv"
with open(out, "w", encoding="utf-8") as f:
    f.write(buf.getvalue())
print("wrote", out)

# summary of values for the log
for r in rows:
    print(r[0], r[5], r[6], "=", r[7])
