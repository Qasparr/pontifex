# PROGRESS — THE BRANCH-OFFSET REGISTER

Commission: founder, 2026-11-26 15:03 EST ("Build the branch-offset register —
chart the 12 tongues' branches"). Method: a branch script weighed against its
parent tongue, letter by letter; offsets printed at coordinates and read in
the branch's own root system where they land signed (exemplar: latin_ordinal
VV−X = 20 = XX, the lawful double).

## Stages
- [x] S0 Sources found (2026-11-26): engine tables (pontifex/tables.py);
  caucasus-north/{cyrillic-table,glagolitic-table,slavonic-parting,
  georgian-table}.csv; twelve-tongues/{aramaic-table,armenian-table,
  coptic-descent}.csv; maps/phoenician-cypher-glyph-map (Greek↔Latin
  22-row line); class-walk fence (Coptic Demotic seven).
- [x] S1 Computation script + frozen data (branch_offsets.csv/json)
- [x] S2 Register MD (Teacher's Edition) in goal files
- [x] S3 Font-coverage audit + MAGVS PDF
- [x] S4 Parity battery + all repo batteries re-run
- [x] S5 Commit + push (this build's files only)
- [x] S6 Announce both houses
- [x] S7 Log (~/memory/2026-11-26.md) + CHECKPOINT → COMPLETED

## Alignment discipline (frozen at S0)
- Greek→Cyrillic: cyrillic-table.csv greek_pair (27 SOURCED seats);
  variants + REFUSED-WESTERN rows in an annex, never in the main count.
- Greek→Glagolitic: CHAINED in-house alignments only — Greek→Cyrillic
  (greek_pair) → Glagolitic (slavonic-parting PAIRS by Cyrillic letter).
  Seat-pairings (Ϛ→dz, Ϟ→ch, Ϡ→ts) flagged as seat-pairings, not sound.
- Greek→Coptic: coptic-descent.csv (27 seats); Demotic seven FENCED,
  printed unvalued, never offset. ϥ fai is valued (90) — printed apart.
- Aramaic→Hebrew: aramaic-table.csv hebrew_equivalent × HEBREW bank,
  both strata (Imperial, Syriac).
- Aramaic→Arabic: shared abjad order — aramaic-table position n ↔
  ARABIC_ABJAD dict order n (the bank's header states the abjadī order).
  Arabic's extra six (500–1000) print as branch-only extension.
- Greek→Latin: the Phoenician map's 22 rows (Greek heir ↔ Latin heir);
  parent Milesian, branch latin_ordinal; Agrippa as second bank.
  TH row unpriced in the map → gap printed. Ϻ san row unvalued → gap.
- Armenian/Georgian: TESTIMONY ONLY — sound alignments vs Greek and vs
  Hebrew printed with per-pair reasoning; pairs beyond a parent's grid
  cap (900 Greek / 400 Hebrew) flagged EXTENSION and excluded from
  agreement counts; no verdict on parentage.
- Limit cases: kana (parent Chinese — no in-house value bank), hangul
  (featural, own root), Ge'ez/halehame (parent South Arabian not
  in-house) — gaps printed, no offsets computed.
