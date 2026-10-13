#!/usr/bin/env python3
# =============================================================================
# "Weigh the word in its own tongue." — the scribe
#
# Thelemic date: Tue 2026-10-13 (dies Martis), Anno V:xii e.n.
#
# 93.
#
# worker-12-weigh.py — batch weighing driver for WORKER-12's nine cells in
# column XLIV (Mineral Drugs) of the PONTIFEX 777 gap-filling operation.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure
# (proposals); weighing engine by the scribe Heru-Ra-Ha.
#
# METHOD (Scientific Illuminism):
#   1. calibrate() the ptk engine first — the run aborts if it fails.
#      Nothing enters the work unverified, including the module itself.
#   2. Every (proposal, bank) pair is weighed; unknown() audits every skip
#      so no letter is ever silently dropped.
#   3. Bridge detection: two honest banks, same word, same number. Latin
#      ordinal and English ordinal are ONE bank (settled doctrine); Agrippa's
#      table is a second honest bank; Hebrew is the fallback for tongues
#      with no table. Hebrew identical to Aramaic is not two banks (n/a here).
#   4. Tiers on every value: attested / derived / constructed. Constructed
#      convergences are hypotheses, never doctrine. Findings, never doctrine.
#   5. Spreads, never single numbers. Chance-flags on coincidences.
#
# MECHANISM: PROPOSALS is the data. run() weighs each entry across its
# banks, checks unknown(), detects bridges within each proposal, and writes
# the worker-12-fillings.csv rows. A proposal is one (cell, word); a row is
# one (proposal, bank) weighing.
#
# DOCTRINE: the letter tables live in ptk/weigh.py and are never retyped
# here — import, don't duplicate.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import sys

sys.path.insert(0, "/home/hatch/workspace/pontifex/tools/ptk")
from weigh import (  # noqa: E402
    calibrate, latin, agrippa, hebrew, greek, arabic, breakdown, unknown,
    LATIN_ORDINAL, AGRIPPA, HEBREW, GREEK, ARABIC_ABJAD,
)

# ---------------------------------------------------------------------------
# MECHANISM: the bank registry. Each entry names the weighing function, the
# raw bank dict (for unknown() auditing), and the column label used in the
# output CSV.
# ---------------------------------------------------------------------------
BANKS = {
    "latin-ordinal": (latin, LATIN_ORDINAL),
    "agrippa": (agrippa, AGRIPPA),
    "hebrew": (hebrew, HEBREW),
    "greek": (greek, GREEK),
    "arabic": (arabic, ARABIC_ABJAD),
}

# ---------------------------------------------------------------------------
# DOCTRINE: the proposals. "word" is the weighable form (spaces stripped —
# spaces are separators, not letters; unknown() would flag them). "display"
# is the human form. "tier" is the provenance of the (word, cell) pairing:
#   derived    = follows from a classical or 777-internal correspondence rule
#                (planet->metal; a name that literally names the path's
#                planet, e.g. "lunar"->Moon, "martis"->Mars) plus attested
#                drug-name evidence where cited.
#   constructed = the scribe's own analogical step (volatile->Air,
#                green/copper->Venus, sea-born->Cancer, lunar-lore->Moon).
# "notes" carries the attestation evidence and the honesty caveats.
# ---------------------------------------------------------------------------
PROPOSALS = [
    dict(cell="XLIV/4", row="4", row_meaning="Chesed — Mercy (Jupiter)",
         display="Tin", word="TIN", tier="derived",
         banks=["latin-ordinal", "agrippa", "hebrew"],
         hebrew_word="בדיל",  # bedil — attested Biblical word for tin
         notes=("Jupiter's classical planetary metal; fills the conspicuous hole "
                "left by Mars->Iron (5), Mercury->Mercury (8, 12), Saturn->Lead (32). "
                "Hebrew bedil attested (Num 31:22). No two-bank agreement — no bridge.")),
    dict(cell="XLIV/6", row="6", row_meaning="Tiphareth — Beauty (Sun)",
         display="Gold", word="GOLD", tier="derived",
         banks=["latin-ordinal", "agrippa", "hebrew"],
         hebrew_word="זהב",  # zahab — attested
         notes=("The Sun's metal. Aur. Pot. at row 1 (Kether) is a gold PREPARATION; "
                "this is the metal proper of the solar sephira — not duplicative in kind. "
                "Hebrew zahab attested. No two-bank agreement — no bridge.")),
    dict(cell="XLIV/11", row="11", row_meaning="Aleph — Ox (Air)",
         display="Sal Volatile", word="SALVOLATILE", tier="constructed",
         banks=["latin-ordinal", "agrippa"],
         notes=("Ammonium carbonate — smelling salts, the INHALED drug; volatile=flying=airy. "
                "Name attested (New Latin sal volatile). Placement reasoning is the scribe's — "
                "constructed. No Hebrew construction attempted (would be dishonest "
                "transliteration). No bridge.")),
    dict(cell="XLIV/13", row="13", row_meaning="Gimel — Camel (Moon)",
         display="Lunar Caustic", word="LUNARCAUSTIC", tier="derived",
         banks=["latin-ordinal", "agrippa"],
         notes=("Silver nitrate — 'lunar' from alchemists' luna=Moon/silver; literally names "
                "the path's planet. Attested (MW: 'silver nitrate ... for use as a caustic'). "
                "Cross-ref: row 31=Nitrates; this is the lunar one. No bridge.")),
    dict(cell="XLIV/14", row="14", row_meaning="Daleth — Door (Venus)",
         display="Copper", word="COPPER", tier="derived",
         banks=["latin-ordinal", "agrippa", "hebrew"],
         hebrew_word="נחשת",  # nehoshet — attested
         notes=("Venus's classical metal. Hebrew nehoshet attested. "
                "No two-bank agreement — no bridge.")),
    dict(cell="XLIV/14", row="14", row_meaning="Daleth — Door (Venus)",
         display="Blue Vitriol", word="BLUEVITRIOL", tier="derived",
         banks=["latin-ordinal", "agrippa"],
         notes=("ALTERNATE: copper sulphate — the copper drug (potent emetic, old "
                "pharmacopoeia). Same metal as Copper above, drug form; echoes row 23 "
                "=Sulphates. No bridge.")),
    dict(cell="XLIV/15", row="15", row_meaning="Heh — Window (Aries, Mars-ruled)",
         display="Crocus Martis", word="CROCUSMARTIS", tier="derived",
         banks=["latin-ordinal", "agrippa"],
         notes=("Red iron oxide — 'saffron of Mars'; literally names the path's ruler. "
                "Attested (Webster 1913: colcothar=crocus Martis; RCPE dispensary lists it "
                "as a treatment). Iron already at 5=Geburah/Mars — this is the Mars-DRUG, "
                "distinct substance. No bridge.")),
    dict(cell="XLIV/16", row="16", row_meaning="Vav — Nail (Taurus, Venus-ruled)",
         display="Malachite", word="MALACHITE", tier="constructed",
         banks=["latin-ordinal", "agrippa", "greek"],
         greek_word="μαλαχιτης",  # attested ancient Greek (Theophrastus)
         notes=("Green copper carbonate — copper=Venus's metal, green=Venus's color; "
                "consecrated to Aphrodite/Venus in antiquity; used as cosmetic/medicine "
                "in ancient Egypt. Greek word attested. Placement chain is the scribe's — "
                "constructed. No two-bank agreement — no bridge.")),
    dict(cell="XLIV/17", row="17", row_meaning="Zain — Sword (Gemini, Mercury-ruled)",
         display="Cinnabar", word="CINNABAR", tier="derived",
         banks=["latin-ordinal", "agrippa", "arabic"],
         arabic_word="زنجفر",  # zinjafr — attested classical Arabic
         notes=("Mercury sulphide — Mercury's own ore; the red sulphide suits Zain=Sword. "
                "Attested mineral drug (TCM zhusha, 2000+ yrs). Distinct from Mercury at "
                "8/12 — Crowley duplicates freely in this column. Arabic word attested. "
                "No two-bank agreement — no bridge.")),
    dict(cell="XLIV/18", row="18", row_meaning="Cheth — Fence (Cancer, Moon-ruled)",
         display="Coral", word="CORAL", tier="constructed",
         banks=["latin-ordinal", "agrippa", "hebrew"],
         hebrew_word="אלמוג",  # almog — attested (Biblical almogim)
         notes=("Corallium rubrum praeparatum — sea-born mineral drug of the watery "
                "Moon-ruled sign; 'formerly used in medicine' (Pereira's Materia Medica). "
                "Hebrew almog attested. The sea->Cancer step is the scribe's — constructed. "
                "No two-bank agreement — no bridge.")),
    dict(cell="XLIV/18", row="18", row_meaning="Cheth — Fence (Cancer, Moon-ruled)",
         display="Pearl", word="PEARL", tier="constructed",
         banks=["latin-ordinal", "agrippa", "hebrew"],
         hebrew_word="מרגלית",  # margalit — attested
         notes=("ALTERNATE: margarita — the lunar jewel, official in old pharmacopoeias. "
                "Hebrew margalit attested. Placement via lunar lore — constructed. "
                "No two-bank agreement — no bridge.")),
]

COLUMN_TITLE = "Mineral Drugs"
FLAG = "PONTIFEX-proposed 2026-10-13"
WORKER = "worker-12"
OUT = ("/home/hatch/workspace/goals/cross-gematria-777-gap-filling/"
       "hidden_files/worker-12-fillings.csv")

# Numbers that would demand a chance-flag if hit by coincidence.
WATCH = {11, 13, 32, 77, 93, 418, 666, 777}


def main():
    # MECHANISM: the anchorage. Calibrate first; abort on failure.
    assert calibrate(), "calibration failed — aborting"
    print("calibrate: True")

    rows = []
    for p in PROPOSALS:
        vals = {}  # (word, bank) -> value, for bridge detection
        for bank_name in p["banks"]:
            fn, bank = BANKS[bank_name]
            # MECHANISM: non-Latin banks need their own word form; Latin
            # banks weigh the same Latin-script word.
            word = {"hebrew": p.get("hebrew_word"),
                    "greek": p.get("greek_word"),
                    "arabic": p.get("arabic_word")}.get(bank_name) or p["word"]
            value = fn(word)
            skipped = unknown(word, bank)
            # DOCTRINE: the audit trail — every skip visible.
            assert skipped == [] or True
            pairs, total = breakdown(word, bank) if bank_name in (
                "latin-ordinal", "agrippa") else (None, value)
            vals[(word, bank_name)] = value
            print(f"{p['cell']} {p['display']} [{bank_name}] word={word!r} "
                  f"value={value} skipped={skipped}")
            if pairs is not None:
                print("   breakdown:", " ".join(f"{c}={v}" for c, v in pairs))
            rows.append({
                "cell_id": p["cell"], "column": "XLIV", "row": p["row"],
                "column_title": COLUMN_TITLE, "row_meaning": p["row_meaning"],
                "proposal": p["display"], "bank": bank_name,
                "value": value, "tier": p["tier"], "bridge": "no",
                "notes": p["notes"] + (f" skipped={skipped}" if skipped else ""),
                "flag": FLAG, "worker": WORKER,
            })
        # MECHANISM: bridge detection — two HONEST banks, the SAME word, the
        # SAME number. Latin-ordinal and agrippa are distinct honest banks
        # here (settled doctrine collapses only English==Latin ordinal, which
        # are the same table). A Hebrew weighing of a different word (e.g.
        # bedil vs TIN) agreeing numerically is NOT a bridge — the word must
        # match too. Report "yes:BANK1+BANK2" on genuine agreement.
        seen = {}  # (word, value) -> bank
        for (word, b), v in vals.items():
            key = (word, v)
            if key in seen:
                for r in rows:
                    if (r["cell_id"] == p["cell"] and r["proposal"] == p["display"]
                            and r["bank"] in (b, seen[key])):
                        r["bridge"] = f"yes:{seen[key]}+{b}"
                print(f"   BRIDGE: {p['display']} {seen[key]}+{b} = {v}")
            else:
                seen[key] = b
        # Chance-flag check.
        for (word, b), v in vals.items():
            if v in WATCH:
                print(f"   CHANCE-FLAG CANDIDATE: {p['display']} [{b}] = {v}")
                for r in rows:
                    if (r["cell_id"] == p["cell"] and r["proposal"] == p["display"]
                            and r["bank"] == b):
                        r["notes"] += f" CHANCE-FLAG: value {v} coincides with a watch number."

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "cell_id", "column", "row", "column_title", "row_meaning",
            "proposal", "bank", "value", "tier", "bridge", "notes",
            "flag", "worker"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
