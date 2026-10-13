#!/usr/bin/env python3
# =============================================================================
# "Each word weighed in its own tongue; the fallback weighed twice, lest the
#  fallback itself be the scale." — the scribe, on the unity-vs-war extension
#
# Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.
#
# 93.
#
# weigh_unity_war.py — weigh the six unity-vs-war terms through two fallback
# arms: HEBREW (mispar hechrechi, the standing fallback for tongues with no
# table) and LATIN ordinal (the control arm, testing whether bridges survive
# a change of fallback).
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): the ATTESTED tables are imported from
# pontifex.tables — never retyped, so drift is impossible. Calibration
# (עז=77) is asserted up front; the script fails closed if it breaks.
# Every Hebrew rendering carries its lexicon source; every native term its
# dictionary. Two layers of choice (native-term selection × Hebrew-rendering
# selection) make every value CONSTRUCTED — the script reports spreads,
# never single "answers."
#
# MECHANISM: for each term, weigh all Hebrew renderings letter-by-letter,
# all Latin candidates, and the English term; emit a CSV; check collisions
# against the sweep's known numbers (77, 93, 418, 11, 32, 666, 777) and
# sweep-internal values (QIRA=311, AXONEME=77, CELL=32).
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# DOCTRINE: import the tables — the scribe does not retype what is attested.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from pontifex.tables import HEBREW, LATIN_ORDINAL

# -- Calibration: fail closed ----------------------------------------------
# MECHANISM: if the attested anchor does not verify, nothing downstream is
# trustworthy, so the run must not proceed.
assert sum(HEBREW[c] for c in "עז") == 77, "calibration עז=77 FAILED"
print("calibration ok: עז = 77")


def weigh(word, table):
    """MECHANISM: sum letter values; raise on any unmapped character rather
    than silently skipping it (fail closed on unknown glyphs)."""
    total, letters = 0, []
    for ch in word:
        if ch not in table:
            raise KeyError(f"unmapped character {ch!r} in {word!r}")
        total += table[ch]
        letters.append(f"{ch}={table[ch]}")
    return total, letters


# ---------------------------------------------------------------------------
# DATA — every entry carries its source. Tier: CONSTRUCTED throughout
# (translation is a built proposal; native-term selection × rendering
# selection = two layers of choice).
# ---------------------------------------------------------------------------
# Format: (term, language, script_form, source_note)
TERMS = [
    # -- ENGLISH (native bank, ATTESTED table) --
    ("unity", "english", "UNITY", "native spelling"),
    ("harmony", "english", "HARMONY", "native spelling"),
    ("war", "english", "WAR", "native spelling"),
    ("tribe", "english", "TRIBE", "native spelling"),
    ("humanity", "english", "HUMANITY", "native spelling"),
    ("brotherhood", "english", "BROTHERHOOD", "native spelling"),
    # -- HEBREW renderings (CONSTRUCTED translation × ATTESTED table) --
    ("unity", "hebrew", "אחדות", "wordhippo/learnentry: unity=אחדות"),
    ("unity", "hebrew", "איחוד", "wordhippo: unity=איחוד (union/unification)"),
    ("harmony", "hebrew", "הרמוניה", "loanword in use; shoah.org.uk notes no native word, Israelis use harmonia"),
    ("harmony", "hebrew", "התאמה", "semantic alternative: correspondence/suitability"),
    ("war", "hebrew", "מלחמה", "standard; ulpanor usage"),
    ("war", "hebrew", "קרב", "standard: battle/combat"),
    ("tribe", "hebrew", "שבט", "standard"),
    ("tribe", "hebrew", "מטה", "biblical: tribe (e.g. מטה יהודה)"),
    ("humanity", "hebrew", "אנושות", "standard: mankind/humanity"),
    ("humanity", "hebrew", "אנושיות", "semantic alternative: humanness"),
    ("brotherhood", "hebrew", "אחווה", "proz.com KudoZ, peer-agreed: brotherhood/fraternity"),
    # -- LATIN control arm (CONSTRUCTED translation × ATTESTED ordinal) --
    ("unity", "latin", "UNITAS", "Lewis & Short: unity, oneness"),
    ("harmony", "latin", "HARMONIA", "Lewis & Short: harmony, agreement"),
    ("harmony", "latin", "CONCORDIA", "Lewis & Short: harmony, union of hearts (noted alternative)"),
    ("war", "latin", "BELLUM", "Lewis & Short: war"),
    ("tribe", "latin", "TRIBUS", "Lewis & Short: tribe"),
    ("humanity", "latin", "HUMANITAS", "Lewis & Short: humanity, human nature"),
    ("brotherhood", "latin", "FRATERNITAS", "Lewis & Short: brotherhood"),
]

# Native-term record (context layer — not weighed; the tongues have no table).
# Each carries its dictionary citation.
NATIVE = {
    "unity": [("Japanese", "団結/統一", "jisho.org (EDICT); Collins English-Japanese"),
              ("Chinese", "统一/团结", "Collins English-Chinese"),
              ("Sanskrit", "ऐक्यम् (aikyam)", "Apte via sanskritdictionary.com: oneness, unity, harmony")],
    "harmony": [("Japanese", "調和", "Collins English-Japanese; wordhippo"),
                ("Chinese", "和谐", "standard (Collins pattern)"),
                ("Sanskrit", "सामञ्जस्य (sāmañjasya)", "WEAK: single web attestation; treat as provisional")],
    "war": [("Japanese", "戦争", "jisho.org (EDICT), standard"),
            ("Chinese", "战争", "standard (Collins pattern)"),
            ("Sanskrit", "युद्ध (yuddha)", "Apte via sanskritdictionary.com: war, battle, fight")],
    "tribe": [("Japanese", "部族", "jisho.org (EDICT), standard"),
              ("Chinese", "部落", "standard (Collins pattern)"),
              ("Sanskrit", "जन (jana)", "sanskritdictionary.com: people, tribe (Rigvedic)")],
    "humanity": [("Japanese", "人類", "Reverso Context; standard"),
                 ("Chinese", "人类", "standard (Collins pattern)"),
                 ("Sanskrit", "मानवता (mānavatā)", "WEAK: standard modern word; classical attestation not re-verified this pass")],
    "brotherhood": [("Japanese", "兄弟愛", "LingQ (EDICT-based): brotherly love"),
                    ("Chinese", "兄弟情谊/手足情谊", "indifferentlanguages; wordhippo"),
                    ("Sanskrit", "भ्रातृत्व (bhrātṛtva)", "WEAK: standard Monier-Williams formation; not independently re-verified this pass")],
}

TABLE_FOR = {"english": LATIN_ORDINAL, "hebrew": HEBREW, "latin": LATIN_ORDINAL}
TARGETS = {77: "AXONEME/עז", 93: "THELEMA/AGAPE", 418: "ABRAHADABRA",
           11: "LIBERTY(chance)", 32: "CELL", 666: "Beast", 777: "—",
           311: "QIRA(sweep-internal)"}


def main():
    out = Path(__file__).resolve().parent / "unity-war-values.csv"
    rows = []
    for term, lang, form, src in TERMS:
        # DOCTRINE: English and Latin share the ordinal bank (one bank, not
        # two) — the sweep's anti-finding, honored here.
        value, letters = weigh(form, TABLE_FOR[lang])
        hits = [f"{n}({TARGETS[n]})" for n in TARGETS if value == n]
        rows.append({"term": term, "language": lang, "script_form": form,
                     "value": value, "letters": "+".join(letters),
                     "source": src, "target_hits": ";".join(hits)})
        print(f"{term:12s} {lang:8s} {form:10s} = {value:4d}  "
              f"{'+'.join(letters)}" + (f"  <-- {';'.join(hits)}" if hits else ""))
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
