#!/usr/bin/env python3
# =============================================================================
# weigh_hebrew.py — worker #1 (HEBREW) of the PONTIFEX twelve-tongues research
# v1.0 "The First Bank"
#
# Epigraph: "Do what thou wilt shall be the whole of the Law." — Liber AL I:40.
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# Scribed by worker #1 (HEBREW); findings are drafts for the author's red pen —
# no bridge is decreed here.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: the shared corpus, transliterated into Hebrew by an explicit
#     academic-style convention and weighed in mispar hechrechi, will show
#     which terms converge on the target numbers (418, 666, 777, 93, 77, 11).
#   Method: transliterate each Latin-script term with a stated convention,
#     weigh letter-by-letter on the ATTESTED mispar hechrechi table imported
#     from pontifex.tables (never re-typed), report mergers, collisions, hits,
#     and misses with equal weight.
#   Observation: recorded per term below and in hebrew.md.
#   Result: findings, never doctrine — all to the red pen.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Weigh the shared corpus in the Hebrew bank.

DOCTRINE (the author's, not the scribe's to amend):
  - Each word weighed in its own tongue; Hebrew uses mispar hechrechi.
  - Every value carries a provenance tier: ATTESTED / DERIVED / CONSTRUCTED.
  - This research decrees no bridge. Findings go to the red pen.

MECHANISM:
  - The value table is IMPORTED from pontifex.tables (HEBREW) — the attested
    table is never re-typed by hand, so drift is impossible.
  - The transliteration convention is the scribe's own stated proposal
    (CONSTRUCTED tier): academic-style, greedy digraphs (ch→ח, sh→ש, th→ת),
    single-letter map otherwise, x→קס (expansion), vv→וו (no vowel-length
    merger — the doubled letter is inscriptionally load-bearing), j→י
    (non-firing on this corpus), hyphen dropped (value-neutral).
  - Calibration: עז must weigh 77, or the run fails closed (exit 1).
"""

import csv
import os
import sys

# MECHANISM: bootstrap the repo so the attested table is imported, not copied.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import HEBREW  # noqa: E402  (attested mispar hechrechi)

# -- Worker's transliteration convention (CONSTRUCTED, stated explicitly) ----
# DOCTRINE: the convention is a built proposal — a hypothesis for the red pen,
# never doctrine. Every choice below is recorded so the weighing is auditable.

# MECHANISM: greedy digraphs checked left-to-right before single letters.
DIGRAPHS = {"ch": "ח", "sh": "ש", "th": "ת"}
# MECHANISM: single-letter map. NOTE the deliberate choices:
#   - x → קס is an EXPANSION (one Latin letter, two Hebrew letters).
#   - v → ו means VV → וו: no vowel-length merger (oo→ו declined), because
#     the doubled V of TRVVTH is inscriptionally load-bearing in the author's
#     doctrine; a merger would silently erase it.
#   - j → י follows the repo map; no corpus term uses J, so it never fires.
SINGLE = {
    "a": "א", "b": "ב", "c": "ק", "d": "ד", "e": "ה", "f": "פ", "g": "ג",
    "h": "ה", "i": "י", "j": "י", "k": "כ", "l": "ל", "m": "מ", "n": "נ",
    "o": "ו", "p": "פ", "q": "ק", "r": "ר", "s": "ס", "t": "ת", "u": "ו",
    "v": "ו", "w": "ו", "x": "קס", "y": "י", "z": "ז",
}
# MECHANISM: hyphen carries no value; dropped (value-neutral), recorded.
IGNORED = {"-", " ", "־"}


def transliterate(term, use_digraphs=True):
    """Render a Latin-script term in Hebrew letters per the stated convention.

    MECHANISM: lowercase, walk left-to-right; at each position try a digraph
    first (if use_digraphs), else the single-letter map; skip IGNORED chars.
    Returns (hebrew_string, fired_digraphs, absorbed_letters).
    DOCTRINE: absorbed letters (e.g. the H in TH) lose their individual value
    inside the digraph — the loss is reported, never hidden.
    """
    t = term.lower()
    out, fired, absorbed = [], [], []
    i = 0
    while i < len(t):
        ch = t[i]
        if ch in IGNORED:
            i += 1
            continue
        if use_digraphs and t[i : i + 2] in DIGRAPHS:
            dig = t[i : i + 2]
            out.append(DIGRAPHS[dig])
            fired.append(dig)
            absorbed.append(dig[1])  # the second letter is absorbed, valueless
            i += 2
            continue
        out.append(SINGLE[ch])
        i += 1
    return "".join(out), fired, absorbed


def weigh(hebrew):
    """Weigh a Hebrew string in mispar hechrechi, letter by letter.

    MECHANISM: straight table lookup on the ATTESTED table; final forms share
    values by the table itself, so no special-casing is needed or done.
    Returns (total, [(letter, value), ...]).
    """
    steps = [(ch, HEBREW[ch]) for ch in hebrew]
    return sum(v for _, v in steps), steps


# -- The shared corpus -------------------------------------------------------
# MECHANISM: every term the parent assigned, plus the reference term עז.
# DOCTRINE: עז is natively Hebrew — no transliteration, ATTESTED tier outright.
CORPUS = [
    "AXONEME", "OZ", "TRVVTH", "THELEMA", "AGAPE", "BABALON",
    "HERU-RA-HA", "ABRAHADABRA", "QIRA", "LIBERTY", "CELL",
]
REFERENCE = "עז"  # ATTESTED reference term; calibration target = 77.

TARGETS = (418, 666, 777, 93, 77, 11)

# MECHANISM: known merger map (from pontifex.tables.MERGERS, restated so the
# per-term report can name exactly which distinctions each weighing lost).
MERGER_SETS = {
    "ה": {"e", "h"}, "י": {"i", "j", "y"}, "ו": {"o", "u", "v", "w"},
    "ק": {"c", "q"}, "פ": {"f", "p"},
}


def mergers_in_term(term):
    """Name the merger sets with ≥2 distinct source letters present in a term.

    MECHANISM: a merger only *loses* information when the term actually
    contains two letters that land on one Hebrew letter. Presence of one is
    noted as 'map-level only' by the caller.
    """
    letters = set(term.lower())
    fired = []
    for heb, srcs in MERGER_SETS.items():
        present = sorted(srcs & letters)
        if len(present) >= 2:
            fired.append(f"{heb}:[{','.join(present)}]")
    return fired


def main():
    # -- Calibration: fail closed -------------------------------------------
    # MECHANISM: the author's anchor. If עז != 77 the table is wrong and
    # nothing else may be trusted — exit 1, per the fail-closed capstone.
    cal_total, cal_steps = weigh(REFERENCE)
    assert cal_total == 77, f"CALIBRATION FAILED: עז = {cal_total}, want 77"
    print(f"CALIBRATION: עז = {'+'.join(str(v) for _, v in cal_steps)} = 77 ✓")

    rows = []
    seen_values = {}

    def record(term, script_form, convention, tier, total, steps,
              mergers_loss, notes):
        # MECHANISM: one CSV row per weighing, plus collision tracking.
        rows.append({
            "term": term,
            "language": "Hebrew",
            "script_form": script_form,
            "transliteration_convention": convention,
            "table_used": "Hebrew mispar hechrechi (ATTESTED)",
            "provenance_tier": tier,
            "value": total,
            "mergers_or_loss": mergers_loss,
            "notes": notes,
        })
        seen_values.setdefault(total, []).append(term)
        detail = "+".join(f"{ch}={v}" for ch, v in steps)
        print(f"{term:22s} {script_form:14s} {detail} = {total}")

    CONV = "academic-greedy-digraph v1 (worker-1): ch→ח sh→ש th→ת greedy; "\
           "x→קס expansion; vv→וו (no vowel-length merger); j→י; hyphen dropped"
    TIER = "CONSTRUCTED (transliteration is a built proposal; "\
           "weighing table is ATTESTED mispar hechrechi)"

    for term in CORPUS:
        heb, fired, absorbed = transliterate(term)
        total, steps = weigh(heb)
        mg = mergers_in_term(term)
        loss_bits = []
        if mg:
            loss_bits.append("mergers fired with loss: " + "; ".join(mg))
        if absorbed:
            loss_bits.append(
                "digraph absorption: " + ", ".join(absorbed) +
                " absorbed into " + ", ".join(fired) + " (individual value lost)")
        if "x" in term.lower():
            loss_bits.append("x→קס expansion (1 Latin letter → 2 Hebrew letters)")
        if "-" in term:
            loss_bits.append("hyphen dropped (value-neutral)")
        record(term, heb, CONV, TIER, total, steps,
               "; ".join(loss_bits) if loss_bits else "none within term",
               "")

    # -- Labeled variants (kept OUT of the primary series, reported openly) --
    # DOCTRINE: variants are the same tier as the primary — CONSTRUCTED
    # transliterations on the ATTESTED table — but labeled so the parent can
    # separate the mechanical series from the considered alternatives.

    # Variant A: TRVVTH without the digraph (th → ת+ה, nothing absorbed).
    heb, _, _ = transliterate("TRVVTH", use_digraphs=False)
    total, steps = weigh(heb)
    record("TRVVTH [no-digraph variant]", heb,
           "as primary but th→ת+ה (no digraph absorption)", TIER, total, steps,
           "none within term",
           "Considered alternative: TH not merged. Primary stays greedy per "
           "the repo map and the task's TH→ת example.")

    # Variant B: HERU-RA-HA in the author's established spelling הרו־רא־הא.
    # DOCTRINE: this spelling is the author's own hand (his 418 bridge); the
    # scribe records it as a variant because the mechanical convention renders
    # HERU as ההר (h→ה, e→ה) while the established form elides the e.
    heb = "הרוראהא"
    total, steps = weigh(heb)
    record("HERU-RA-HA [established הרו־רא־הא variant]", heb,
           "author's established spelling (e elided after ה: HERU→הרו)",
           "CONSTRUCTED (transliteration variant; table ATTESTED)", total,
           steps, "e elided by convention (HERU→הרו, not ההרו)",
           "The author's own spelling of his 418 bridge; mechanical "
           "convention gives 423 (see primary row). The gap is the finding.")

    # -- Reference term: ATTESTED outright -----------------------------------
    total, steps = weigh(REFERENCE)
    record("עז [reference]", REFERENCE, "n/a — natively Hebrew",
           "ATTESTED (native term, attested table, no transliteration)",
           total, steps, "none — no transliteration",
           "Calibration anchor; author's AXONEME=77=עז bridge lands here.")

    # -- Collisions ----------------------------------------------------------
    print("\nCOLLISIONS (same value, different terms):")
    collisions = {v: ts for v, ts in seen_values.items() if len(ts) > 1}
    if collisions:
        for v, ts in sorted(collisions.items()):
            print(f"  {v}: {', '.join(ts)}")
    else:
        print("  none — all weighings are distinct values.")

    # -- Target-number hits ---------------------------------------------------
    print("\nTARGET-NUMBER HITS:")
    by_value = {}
    for r in rows:
        by_value.setdefault(r["value"], []).append(r["term"])
    for t in TARGETS:
        hits = by_value.get(t, [])
        print(f"  {t}: {', '.join(hits) if hits else '— no hit —'}")

    # -- CSV -----------------------------------------------------------------
    out_dir = os.path.expanduser("~/workspace/pontifex/research/twelve-tongues")
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, "hebrew-values.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "term", "language", "script_form", "transliteration_convention",
            "table_used", "provenance_tier", "value", "mergers_or_loss",
            "notes"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {csv_path} ({len(rows)} rows)")

    return 0


if __name__ == "__main__":
    sys.exit(main())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
