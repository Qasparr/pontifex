#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — build_correspondence.py — the twelve-tongues synthesis engine
# v0.1 "The Twelve Banks"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: ☉ in 19° Libra, ☽ in 2° Scorpio, dies Solis,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: that the twelve banks' weighings of one shared corpus
#     reveal meeting points — numbers reached in two or more tongues for
#     the same concept — and that scoring each meeting for bank
#     independence separates inheritance from evidence.
#   Method: read every worker's *-values.csv; group rows by
#     (concept, number); attach each row to a bank-group; flag
#     bank-identity (English<->Latin ordinal, Hebrew<->Aramaic abjad) and
#     shared-descent (Greek->Coptic, Semitic abjad inheritance) so the
#     table cannot double-count one bank as two; emit correspondence.csv.
#   Observation: the meetings found, with their independence scoring.
#   Result: candidate bridges ranked by independent-bank count and
#     provenance tier — findings for the author's red pen, never doctrine.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Build correspondence.csv from the twelve workers' value files.

DOCTRINE: a meeting point is a number reached in 2+ tongues for the same
concept. A meeting's evidential weight is the count of INDEPENDENT banks,
not the count of rows. Banks sharing one table (English/Latin ordinal,
Hebrew/Aramaic abjad) or one inheritance (Greek->Coptic Milesian, the
Semitic 22-order) are scored once, with the sharing stated, never hidden.

MECHANISM: meetings are hand-curated below from the verified worker CSVs
(the workers' own handoffs were cross-checked against the files on
2026-10-11). Hand curation is deliberate: a mechanical group-by would
double-count bank-identities and mistake transliteration-echoes for
bridges. Each meeting carries its independence accounting in plain text.
"""

import csv
import os

# ---------------------------------------------------------------------------
# MECHANISM: the bank groups. Two rows in the same group are one bank
# weighed twice, not two banks meeting.
# DOCTRINE: the grouping is the load-bearing judgment of this synthesis.
# ---------------------------------------------------------------------------
BANK_GROUPS = {
    "english": "G1 Latin-script ordinal",
    "latin:latin_ordinal": "G1 Latin-script ordinal",
    "latin:agrippa": "G2 Agrippa's Latin",
    "hebrew": "G3 Hebrew/Aramaic abjad",
    "aramaic": "G3 Hebrew/Aramaic abjad",
    "greek": "G4 Greek Milesian",
    "coptic": "G5 Coptic (Greek-descent)",
    "arabic": "G6 Arabic abjad",
    "armenian": "G7 Armenian numerals",
    "geez:debtera": "G8 Ge'ez Debtera",
    "geez:hebrew-fallback": "G9 Hebrew-table fallback",
    "japanese:hebrew-fallback": "G9 Hebrew-table fallback",
    "chinese:pinyin-fallback": "G9 Hebrew-table fallback",
    "japanese:stroke-count": "G10 constructed columns",
    "chinese:stroke-count": "G10 constructed columns",
    "geez:fidel-ordinal": "G10 constructed columns",
    "sanskrit:katapayadi": "G10 constructed columns",
    "sanskrit:varnamala-ordinal": "G10 constructed columns",
}

# ---------------------------------------------------------------------------
# MECHANISM: the meetings, curated from the verified CSVs. Fields:
#   meeting id, concept, number, then rows of
#   (language, script_form, table, tier, bank_key, independence note).
# DOCTRINE: every row's tier is the worker's own tier, copied not laundered.
# ---------------------------------------------------------------------------
MEETINGS = [
    {
        "id": "M1", "concept": "AXONEME / עז (Oz)", "number": 77,
        "verdict": "CANDIDATE BRIDGE — the canonical example reproduces: "
                   "AXONEME=77 (Latin ordinal, native English spelling, "
                   "ATTESTED) meets עז=77 (Hebrew, native, ATTESTED). "
                   "Independent banks: G1, G3, G6. G4/G5 עז=77 rows are "
                   "shared Phoenician inheritance, scored as echoes.",
        "rows": [
            ("english", "AXONEME", "English ordinal A=1..Z=26 (native)",
             "ATTESTED", "english",
             "independent — Latin ordinal is not the abjad order"),
            ("latin", "AXONEME", "latin_ordinal",
             "ATTESTED", "latin:latin_ordinal",
             "BANK IDENTITY with english — same table, counted once"),
            ("hebrew", "עז", "mispar hechrechi",
             "ATTESTED (native term, no transliteration)", "hebrew",
             "independent — Semitic abjad, native spelling"),
            ("aramaic", "ܥܙ", "22-letter abjad",
             "DERIVED (script-invariance demo)", "aramaic",
             "BANK IDENTITY with hebrew — same values, counted once"),
            ("arabic", "عز", "abjad, Eastern order",
             "ATTESTED", "arabic",
             "independent table; cognate spelling — shares the "
             "Phoenician 22-order inheritance with Hebrew"),
            ("greek", "οζ", "Milesian isopsephy",
             "ATTESTED (table); transliterated Hebrew term", "greek",
             "echo — 70=70, 7=7 by shared Phoenician inheritance"),
            ("greek", "OZ→οζ", "Milesian isopsephy",
             "ATTESTED (table); script-form CONSTRUCTED", "greek",
             "echo — same inheritance as above"),
            ("coptic", "ⲟⲍ", "Coptic alphabetic numerals",
             "ATTESTED (table); script-form CONSTRUCTED", "coptic",
             "echo — Greek-descent Milesian, not independent"),
        ],
    },
    {
        "id": "M2", "concept": "THELEMA / AGAPE", "number": 93,
        "verdict": "GREEK-BANK PHENOMENON — THELEMA=θέλημα=93 and "
                   "AGAPE=ἀγάπη=93, both authentic spellings on the "
                   "attested table. Crosses to Coptic only by Greek "
                   "descent. Does not cross to Hebrew (481/90), Arabic "
                   "(591/1014), or Armenian (250/810).",
        "rows": [
            ("greek", "θελημα", "Milesian isopsephy",
             "ATTESTED (table); authentic Greek word-form", "greek",
             "independent — the bank's strongest convergence"),
            ("greek", "αγαπη", "Milesian isopsephy",
             "ATTESTED (table); authentic Greek word-form", "greek",
             "collision with THELEMA — the classic equation"),
            ("coptic", "ⲑⲉⲗⲏⲙⲁ (authentic spelling)",
             "Coptic alphabetic numerals",
             "ATTESTED (table); authentic spelling", "coptic",
             "descent — Greek Milesian by inheritance, not corroboration"),
            ("coptic", "ⲁⲅⲁⲡⲏ (authentic spelling)",
             "Coptic alphabetic numerals",
             "ATTESTED (table); authentic spelling", "coptic",
             "descent — as above"),
        ],
    },
    {
        "id": "M3", "concept": "ABRAHADABRA / HERU-RA-HA", "number": 418,
        "verdict": "CONVENTION-SENSITIVE — ABRAHADABRA=418 lands unforced "
                   "under the mechanical Hebrew transliteration and "
                   "reproduces in Aramaic (identity) and Arabic; the "
                   "Ge'ez Hebrew-fallback reproduces it with zero "
                   "mergers. HERU-RA-HA=418 in Arabic, but Hebrew gives "
                   "423 mechanically — the established 418 needs the "
                   "hand-built הרו־רא־הא (e-elision). Every 418 depends "
                   "on transliteration choices; Semitic abjad inheritance "
                   "carries the Hebrew↔Arabic agreement.",
        "rows": [
            ("hebrew", "אבראהאדאברא", "mispar hechrechi",
             "CONSTRUCTED transliteration × ATTESTED table", "hebrew",
             "unforced under the mechanical convention — hypothesis"),
            ("aramaic", "אבראהאדאברא", "22-letter abjad",
             "CONSTRUCTED transliteration × ATTESTED table", "aramaic",
             "BANK IDENTITY with hebrew — counted once"),
            ("arabic", "أبراهادابرا", "abjad, Eastern order",
             "ATTESTED (table); script-form CONSTRUCTED", "arabic",
             "independent table; H→ه convention-dependent "
             "(H→ح shifts it to 421)"),
            ("geez", "አበረአሀአደአበረአ→Hebrew values",
             "mispar hechrechi via fidel",
             "word-form NATIVE-ish / map CONSTRUCTED",
             "geez:hebrew-fallback",
             "Hebrew-table evidence, zero mergers fired — candidate "
             "for the red pen, not an independent bank"),
            ("arabic", "هرو را ها (HERU-RA-HA)", "abjad, Eastern order",
             "ATTESTED (table); script-form CONSTRUCTED", "arabic",
             "collision with ABRAHADABRA in-bank — the Arabic 418 pair"),
            ("hebrew", "הרו־רא־הא (established spelling)",
             "mispar hechrechi",
             "author's hand-built spelling", "hebrew",
             "418 only by e-elision; mechanical gives 423 — the fork "
             "is the red-pen question"),
        ],
    },
    {
        "id": "M4", "concept": "CELL", "number": 32,
        "verdict": "SINGLE-BANK FACT — CELL=32 lives in the Latin-script "
                   "ordinal only. Greek refuses (85), Coptic refuses (85), "
                   "Armenian refuses (125). Not a bridge; a calibration.",
        "rows": [
            ("english", "CELL", "English ordinal A=1..Z=26 (native)",
             "ATTESTED", "english", "native spelling, native table"),
            ("latin", "CELL", "latin_ordinal",
             "ATTESTED", "latin:latin_ordinal",
             "BANK IDENTITY with english — counted once"),
        ],
    },
    {
        "id": "M5", "concept": "LIBERTY", "number": 11,
        "verdict": "FILED AS CHANCE — LIBERTY=11 in the Chinese "
                   "stroke-count column (CONSTRUCTED, scribe-chosen "
                   "characters). 22 weighings × 6 targets; METHOD.md §5 "
                   "applies. Not a bridge.",
        "rows": [
            ("chinese", "自由 (scribe's choice)", "stroke-count, PRC",
             "CONSTRUCTED", "chinese:stroke-count",
             "chance coincidence — filed, not claimed"),
        ],
    },
]

# ---------------------------------------------------------------------------
# MECHANISM: near-misses are recorded as misses, per the workers' discipline.
# A near-miss table stops future "discoveries".
# ---------------------------------------------------------------------------
NEAR_MISSES = [
    ("N1", "BABALON", 92, "hebrew/aramaic/geez-fallback",
     "one short of 93 — recorded as a miss"),
    ("N2", "LIBERTY", 657, "hebrew/aramaic/geez-fallback",
     "nine short of 666 — recorded as a miss"),
    ("N3", "AXONEME", 771, "greek (X→χ) / coptic (X→ⲭ)",
     "six short of 777 — fenced anti-hit, explicitly not a hit"),
    ("N4", "OZ", 13, "hebrew/aramaic/geez-fallback",
     "two over 11 — recorded as a miss"),
    ("N5", "AGAPE", 90, "hebrew/aramaic/japanese-fallback/coptic-mechanical",
     "three short of 93 — recorded as a miss"),
    ("N6", "CELL", 125, "armenian",
     "arithmetically 5³ — observation only, not a target"),
]

COLLISIONS = [
    ("C1", "arabic", "HERU-RA-HA = ABRAHADABRA = 418",
     "in-bank collision on the Eastern abjad; the 418 pair"),
    ("C2", "greek", "THELEMA = AGAPE = 93 (authentic spellings)",
     "the classic equation reproduced, not discovered"),
    ("C3", "greek", "OZ = οζ = 77 = עז→οζ",
     "structural — shared Phoenician inheritance, not independence"),
    ("C4", "coptic", "THELEMA = AGAPE = 90 (mechanical) / 93 (authentic)",
     "mirrors the Greek collision by descent"),
    ("C5", "greek/coptic", "BABALON = 156, QIRA = 131, CELL = 85, "
     "AXONEME = 231 on both banks",
     "descent agreement — continuity, not corroboration"),
]


def main():
    # MECHANISM: emit the machine-readable correspondence table.
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "correspondence.csv")
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["meeting_id", "concept", "number", "language",
                    "script_form", "table_used", "provenance_tier",
                    "bank_group", "independence_note", "meeting_verdict"])
        for m in MEETINGS:
            for (lang, form, table, tier,
                 bank_key, note) in m["rows"]:
                w.writerow([m["id"], m["concept"], m["number"], lang,
                            form, table, tier, BANK_GROUPS[bank_key],
                            note, m["verdict"]])
    # MECHANISM: count independent banks per meeting for the report.
    print("meetings written:", len(MEETINGS))
    for m in MEETINGS:
        groups = {BANK_GROUPS[r[4]] for r in m["rows"]}
        print(m["id"], m["concept"], m["number"],
              "rows:", len(m["rows"]), "bank-groups:", sorted(groups))
    print("near-misses:", len(NEAR_MISSES),
          "collisions:", len(COLLISIONS))
    print("wrote", out)


if __name__ == "__main__":
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
