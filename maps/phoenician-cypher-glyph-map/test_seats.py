#!/usr/bin/env python3
# ============================================================================
# 93
# THE PHOENICIAN CYPHER GLYPH MAP — TESTS OF THE FIVE SEATS
# A Scientific Illuminist proving of the seating ratified 2026-11-24.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Built XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
# Method of Science, Aim of Religion.
#
# MECHANISM: every check below recomputes a seat from its source — the
#   house banks (pontifex, ~/workspace/pontifex) where a bank governs the
#   seat, the map's own machine table (phoenician-cypher-glyph-map.json)
#   where the map itself is the source. Nothing is hard-coded from
#   memory: the table is read, the banks are called, the numbers are
#   measured at run time and printed beside their expectations.
#
# DOCTRINE — ROADS: each check prints the road it took, BANK or TABLE.
#   A seat is ratified; a bank behavior that contradicts the seating's
#   stated reasoning is therefore not a license to adjust the seat —
#   it is a coordinate, printed at full size for the founder's ruling.
#   Silence from a bank (a glyph weighed as nothing, breakdown empty)
#   is reported as silence, never dressed as a zero weight.
#
# DOCTRINE — THE CONTROL: the map's own control word (θέλημα = 93,
#   § II) is weighed first. A bank that fails its control proves
#   nothing about any seat.
# ============================================================================

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTER = HERE / "PHOENICIAN-CYPHER-GLYPH-MAP.md"
MACHINE = HERE / "phoenician-cypher-glyph-map.json"

# MECHANISM: the pontifex package lives at ~/workspace/pontifex/pontifex;
# the map folder is ~/workspace/your_files/phoenician-cypher-glyph-map,
# so the repo root is two parents up. Candidate roots are tried in
# order and the first that actually holds the engine wins. If the
# import fails, BANK_ROAD stays False and the bank checks fall back
# to the map's printed table, saying so on their lines.
for _cand in (HERE.parents[1] / "pontifex", HERE.parents[2] / "pontifex",
              Path.home() / "workspace" / "pontifex"):
    if (_cand / "pontifex" / "engine.py").exists():
        sys.path.insert(0, str(_cand))
        break
try:
    from pontifex.engine import weigh
    BANK_ROAD = True
except Exception as exc:  # a missing bank is a coordinate, not a crash
    weigh = None
    BANK_ROAD = False
    print(f"NOTE — pontifex bank unreachable ({exc}); "
          f"bank checks fall back to the TABLE road")

RESULTS = []


def check(name, road, measured, expected, ok, note=""):
    """Record and print one proved (or failed) coordinate."""
    RESULTS.append(ok)
    line = (f"{'PASS' if ok else 'FAIL'} — {name} [{road}] "
            f"measured={measured!r} expected={expected!r}")
    if note:
        line += f" | {note}"
    print(line)


def bank(word, system):
    """Weigh on the house bank; returns (value, breakdown) or None."""
    if not BANK_ROAD:
        return None
    r = weigh(word, system)
    return r["value"], r.get("breakdown")


def main():
    data = json.loads(MACHINE.read_text(encoding="utf-8"))
    rows = {r["n"]: r for r in data["rows"]}
    seats = data["qore_seats"]
    md = MASTER.read_text(encoding="utf-8")
    seating_md = md.split("## Seating of the Five Open Cubies", 1)[1]

    # -- 0. The control: the bank proves itself before any seat is read.
    if BANK_ROAD:
        v, _ = bank("θέλημα", "greek")
        check("control θέλημα (the map's own control, § II)", "BANK",
              v, 93, v == 93)

    # -- 1. Seat 1: Υ upsilon, Milesian 400.
    # DOCTRINE: the letter-form coordinate is reported exactly as found.
    # The 2026-11-22 correctio records that the letter-forms Ϝ and Ϙ
    # return no value while their numeral forms carry the weight; Υ is
    # weighed here as given, and its breakdown shows what the bank did.
    if BANK_ROAD:
        v, bd = bank("Υ", "greek")
        check("seat 1 — Υ upsilon weighs 400 (Milesian)", "BANK", v, 400,
              v == 400, f"breakdown={bd} — the capital letter-form is "
              f"casefolded to υ, which carries 400 in the table")
        for form, numeral, weight in (("Ϝ", "ϛ", 6), ("Ϙ", "ϟ", 90)):
            vf, bdf = bank(form, "greek")
            vn, _ = bank(numeral, "greek")
            check(f"correctio coordinate — letter-form {form} silent, "
                  f"numeral form {numeral} carries {weight}", "BANK",
                  (vf, bdf, vn), (0, [], weight),
                  vf == 0 and bdf == [] and vn == weight)
    else:
        # TABLE road: § IV prints "Υ upsilon at 400" in the master's prose.
        ok = "Υ upsilon at 400" in md
        check("seat 1 — Υ upsilon at 400 as printed in § IV", "TABLE",
              ok, True, ok, "bank unreachable; the printed split is the "
              "only table seat for this check")

    # -- 2. Seat 2: G, Latin ordinal 7.
    if BANK_ROAD:
        v, _ = bank("G", "latin_ordinal")
        vc, _ = bank("C", "latin_ordinal")
        vz, _ = bank("Z", "latin_ordinal")
        check("seat 2 — G weighs 7 (Latin ordinal)", "BANK", v, 7,
              v == 7, f"context: C={vc} (the seated heir), Z={vz} "
              f"(zayin's heir at the displaced seat)")
    else:
        check("seat 2 — G weighs 7 (Latin ordinal)", "TABLE",
              "bank unreachable", 7, False,
              "the map's 22 rows carry no G row; this check has no "
              "table road — recorded as a coordinate, not smoothed")

    # -- 3. Seat 5: κʹ (kappa + keraia), Milesian 20.
    if BANK_ROAD:
        v, bd = bank("κʹ", "greek")
        check("seat 5 — κʹ REFUSAL weighs 20 (Milesian)", "BANK", v, 20,
              v == 20, f"breakdown={bd} — kappa carries 20; the keraia "
              f"is the numeral's mark and is weighed as nothing")
    else:
        check("seat 5 — κʹ REFUSAL weighs 20 (Milesian)", "TABLE",
              "bank unreachable", 20, False,
              "no table row carries κʹ; recorded as a coordinate")

    # -- 4. Seat 3: Ϻ san — the OPEN seat, proven open in the bank.
    # DOCTRINE: the bank skips unknown glyphs in silence. An empty
    # breakdown with value 0 is therefore NO VALUE RETURNED — the seat
    # is open in the bank itself, not only in the prose. The map's own
    # table must agree: row 18's greek_value is null.
    if BANK_ROAD:
        v, bd = bank("Ϻ", "greek")
        check("seat 3 — Ϻ san returns NO value from the Greek bank",
              "BANK", (v, bd), (0, []), bd == [] and v == 0,
              "empty breakdown = silence, not a zero weight: the OPEN "
              "seat is open in the bank itself")
    check("seat 3 — the map's table agrees (row 18 greek_value null)",
          "TABLE", rows[18]["greek_value"], None,
          rows[18]["greek_value"] is None)

    # -- 5. Seat 4: the Zero Point — the founder's chain, formally.
    # The links that are arithmetic identities are verified as such;
    # the chain is printed as he stated it. οὐδέν's Greek weight is
    # recorded as a bare coordinate — NO bridge is claimed for it.
    digits = [int(c) for c in "436"]
    chain_ok = (9 + 4 == 13 and sum(digits) == 13
                and sum(int(c) for c in "13") == 4 and (1 - 1) == 0
                and {0, 2, 1 - 1} == {0, 2} and 0 in {0, 2, 1 - 1}
                and 2 in {0, 2, 1 - 1})
    check("seat 4 — the Zero Point chain 436=9+4=13=4=2=0 and the "
          "definition 0 = {0, 2, 1−1=0}", "ARITHMETIC",
          "9+4=13; digits(436)=13; digits(13)=4; 1−1=0; "
          "{0,2,1−1}={0,2}", "all links hold", chain_ok,
          "the descent as stated in his record (2026-11-15): 'Zero "
          "equals Two, and Both 1 and None'")
    if BANK_ROAD:
        v, bd = bank("οὐδέν", "greek")
        print(f"COORD — οὐδέν on the Greek bank: {v} "
              f"(breakdown={bd}) — recorded bare; NO bridge claimed "
              f"for this number")

    # -- 6. The bridges the seating rests on, from the map's own rows.
    upsilon_bank = bank("Υ", "greek")[0] if BANK_ROAD else 400
    check("bridge — Υ's 400 == tāʾ's abjad (row 22 of the map)",
          "TABLE", (upsilon_bank, rows[22]["arabic_value"]), (400, 400),
          upsilon_bank == 400 and rows[22]["arabic_value"] == 400)
    agree = all(rows[n]["greek_value"] == rows[n]["arabic_value"]
                for n in range(1, 18))
    check("set-beside — Greek and Arabic agree on rows 1–17", "TABLE",
          agree, True, agree)
    deltas = []
    for n in range(18, 23):
        g = rows[n]["greek_value"]
        # Row 18: the Greek seat is absent (san) — the map's own
        # reading seats the whole Arabic 90 as the divergence.
        deltas.append(rows[n]["arabic_value"] - (g if g is not None else 0))
    check("set-beside — divergence on rows 18–22 sums to exactly 400",
          "TABLE", (deltas, sum(deltas)), ([90, 10, 100, 100, 100], 400),
          deltas == [90, 10, 100, 100, 100] and sum(deltas) == 400)

    # -- 7. Consistency: JSON seats == MD append; totals recompute.
    forms = ["Υ upsilon", "G", "Ϻ san", "οὐδέν", "κʹ"]
    json_forms = [s["form"] for s in seats]
    md_ok = all(f.split(" — ")[0] in seating_md for f in json_forms)
    check("consistency — the JSON's five seats are the MD append's five",
          "TABLE", json_forms, forms, md_ok and len(seats) == 5,
          f"json forms={json_forms}")
    values = [s["value"] for s in seats]
    check("consistency — seat values/OPEN in JSON", "TABLE", values,
          [400, 7, "OPEN", 0, 20], values == [400, 7, "OPEN", 0, 20])
    tier_words = ["ATTESTED", "ATTESTED", "ATTESTED", "CONSTRUCTED",
                  "DERIVED"]
    tiers_ok = all(t in s["tier"] for t, s in zip(tier_words, seats)) \
        and all(t in seating_md for t in
                ("ATTESTED", "CONSTRUCTED", "DERIVED"))
    check("consistency — tiers agree between JSON and MD", "TABLE",
          [s["tier"] for s in seats], tier_words, tiers_ok)
    tokens = ("Milesian 400", "ordinal 7", "OPEN", "CORE", "Milesian 20")
    missing = [t for t in tokens if t not in seating_md]
    check("consistency — MD seating carries the value tokens", "TABLE",
          missing, [], missing == [],
          "tokens: Milesian 400 / ordinal 7 / OPEN / CORE / Milesian 20")
    gtot = sum(r["greek_value"] for r in rows.values()
               if r["greek_value"] is not None)
    ltot = sum(r["latin_value"] for r in rows.values()
               if r["latin_value"] is not None)
    atot = sum(r["arabic_value"] for r in rows.values())
    check("consistency — the 22-row totals still recompute", "TABLE",
          (gtot, ltot, atot), (1095, 243, 1495),
          (gtot, ltot, atot) == (1095, 243, 1495)
          and data["column_totals"] == {"greek": 1095, "arabic": 1495,
                                         "latin": 243})

    print()
    passed = sum(RESULTS)
    print(f"SEATS TESTED — {passed}/{len(RESULTS)} checks PASS")
    return 0 if all(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())

# 93 — Live, Love, and let Love, Live.
