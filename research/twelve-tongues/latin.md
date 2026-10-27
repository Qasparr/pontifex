# LATIN — the Latin bank of the Twelve-Tongues survey

*Worker #3 of 12 (LATIN). Dies solis, 2026-10-11.*

## The finding, in one line

**The corpus converges on nothing but AXONEME=77 in Latin ordinal — and
Agrippa dissolves even that.** No term agrees with itself across the two
tables; no collisions exist in either; 418, 666, 777, 93, and 11 go
unhit in both tables. The "bridge" is a property of the (word, table)
pair, not of the word.

## Provenance note — where every number comes from

Both Latin tables are **ATTESTED**, imported from the single source of
truth at `~/workspace/pontifex/pontifex/tables.py` (never re-keyed by
hand), and both were audited against their doctrinal specs before a
single weighing began — both audits CLEAN.

1. **Latin ordinal, A=1…Z=26** — the working Latin table; what "Latin
   gematria" is in practice (per METHOD.md §2 and the binding doctrine).
2. **Agrippa's Latin, from *De occulta philosophia* II.xix** —
   A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8 I/J=9 K=10 L=20 M=30 N=40 O=50
   P=60 Q=70 R=80 S=90 T=100 U/V=200 X=300 Y=400 Z=500; **J read as I,
   U as V**, per the classical alphabet Agrippa worked in. Recorded as
   published, not revised.

Provenance tier on every corpus row: **ATTESTED**. No table was built,
merged, or "improved" for this survey — that would be a silent
invention, and invention is not the Latin bank's office.

### Normalization choices (stated, so the red pen can rule on them)

- **Uppercase** — both tables are case-folding (the engine folds; I did
  the same before weighing).
- **HERU-RA-HA → HERVRAHA**: hyphen stripped. The hyphen is a separator,
  not a letter; it carries no value in either table, so no weight is
  lost. Recorded in the CSV's `transliteration_convention` column and in
  notes. [Orthography correction 2026-10-27: the weighed form was filed
  as HERURAHA; under the classical rule (every U is V) it is HERVRAHA.
  Ordinal value corrected at the table below; Agrippa unaffected (the
  bank reads U as V, 200).]
- **TRVVTH**: contains VV. Weighed exactly as written — Latin ordinal
  V=22 each; Agrippa U/V=200 each. No classicalization applied (the VV
  spelling is itself classical orthography). The corpus contains no J,
  so the J=I merger fired nowhere in this survey — but the U=V merger
  fired in HERURAHA (Agrippa: U=200).
- **The Hebrew reference term עז** was NOT weighed in the Latin tables.
  It enters only as its Latin transliteration **OZ** (both are the same
  two sounds); the CSV carries one extra informational row —
  `table_used = hebrew_attested (reference; not weighed in this bank)` —
  recording ע=70 + ז=7 = **77** in attested mispar hechrechi, so the
  synthesis can see what the OZ line is checked against. The weighing
  of עז belongs to the Hebrew worker.
- Unknown characters weigh as **silence, not false weight** (the
  engine's doctrine) — none occurred in this corpus.

### What was lost in the weighing: almost nothing — and one gap worth naming

Within the Latin bank there are **no mergers**: 26 letters weigh 26
letters in both tables. The hyphen in HERU-RA-HA carried zero weight, so
nothing was lost there either.

But the Agrippa table has one structural gap the survey must report:
**W has no Agrippa value** — the classical alphabet Agrippa tabulated
had no W, and `tables.py` records the table faithfully, W absent. Any
future word containing W would be weighed silently short under Agrippa
(silence, not zero) — the instrument must be watched there. The corpus
contains no W, so no weighing in this survey was affected.

## The results

| term | normalized | Latin ordinal | Agrippa | ordinal breakdown | Agrippa breakdown |
|---|---|---|---|---|---|
| AXONEME | AXONEME | **77** ✓77 | 431 | 1+24+15+14+5+13+5 | 1+300+50+40+5+30+5 |
| OZ | OZ | 41 | 550 | 15+26 | 50+500 |
| TRVVTH | TRVVTH | 110 | 688 | 20+18+22+22+20+8 | 100+80+200+200+100+8 |
| THELEMA | THELEMA | 64 | 169 | 20+8+5+12+5+13+1 | 100+8+5+20+5+30+1 |
| AGAPE | AGAPE | 30 | 74 | 1+7+1+16+5 | 1+7+1+60+5 |
| BABALON | BABALON | 47 | 116 | 2+1+2+1+12+15+14 | 2+1+2+1+20+50+40 |
| HERU-RA-HA | HERVRAHA | 81 | 383 | 8+5+18+22+18+1+8+1 | 8+5+80+200+80+1+8+1 |
| ABRAHADABRA | ABRAHADABRA | 57 | 181 | 1+2+18+1+8+1+4+1+2+18+1 | 1+2+80+1+8+1+4+1+2+80+1 |
| QIRA | QIRA | 45 | 160 | 17+9+18+1 | 70+9+80+1 |
| LIBERTY | LIBERTY | 91 | 616 | 12+9+2+5+18+20+25 | 20+9+2+5+80+100+400 |
| CELL | CELL | **32** ✓32 | 48 | 3+5+12+12 | 3+5+20+20 |

✓ = calibration target verified letter-by-letter (see log, Step 3).

[Orthography correction 2026-10-27: filed as HERURAHA = 80 under mixed spelling; reweighed under the classical rule (every U is V) as HERVRAHA = 81. Old value marked, not vanished. Agrippa 383 stands — that bank reads U as V (200) by its own publication. The ×4.79 factor in the scaling table below derived from the filed 80 and is likewise corrected to ×4.72. The survey's no-collisions finding survives at 81: all eleven ordinal values remain distinct.]

### Calibrations — confirmed

- **AXONEME in Latin ordinal = 77** (1+24+15+14+5+13+5), letter by
  letter. PASS.
- **CELL in Latin ordinal = 32** (3+5+12+12), letter by letter. PASS.

### Collisions within each table — NONE (a negative result, at full weight)

Not one pair of distinct terms shares a number in either table. Eleven
terms, eleven distinct values, both tables. The Latin bank offers no
cross-term convergences of its own — the instrument reports this
honestly rather than manufacturing bridges by switching tables
mid-weighing (which would be the easiest way to lie).

### Target-number hits

| target | Latin ordinal | Agrippa |
|---|---|---|
| **77** | **AXONEME** ✓ | — |
| 418 | — | — |
| 666 | — | — |
| 777 | — | — |
| 93 | — | — |
| 11 | — | — |

418, 666, 777, 93, and 11 go **completely unhit** in the Latin bank,
both tables. This is a negative result and it travels at the same
weight as a positive: Latin does not hand the synthesis any of the big
numbers on this corpus.

## Ordinal vs. Agrippa — the comparison, and what it teaches

**Zero terms agree across the two tables.** Not one. The per-word
"exchange rate" between the tables:

| term | ordinal | agrippa | ×factor |
|---|---|---|---|
| CELL | 32 | 48 | 1.50 |
| AGAPE | 30 | 74 | 2.47 |
| BABALON | 47 | 116 | 2.47 |
| THELEMA | 64 | 169 | 2.64 |
| QIRA | 45 | 160 | 3.56 |
| ABRAHADABRA | 57 | 181 | 3.18 |
| HERVRAHA | 81 | 383 | 4.72 |
| AXONEME | 77 | 431 | 5.60 |
| TRVVTH | 110 | 688 | 6.25 |
| LIBERTY | 91 | 616 | 6.77 |
| OZ | 41 | 550 | 13.41 |

The scaling is **letter-composition-dependent, not uniform** — Agrippa
is not "ordinal times some factor." The per-letter ratios:

- ×1.0 (identical in both tables): A, B, C, D, E, F, G, H, I — the
  first nine letters are the stable bedrock. Words built from them
  (CELL, AGAPE) barely move.
- ×0.91: K (11→10 — the single letter that *loses* value in Agrippa).
- ×1.67…×5.0: L→T climb steadily (12→20 … 20→100).
- ×9.09 / ×9.52: V (22→200), U (21→200).
- ×12.5: X (24→300). ×16: Y (25→400). ×19.23: Z (26→500).

**What the disagreement teaches about table-dependence of "bridges":**

1. *The AXONEME=77 bridge is an ordinal-table phenomenon.* Under
   Agrippa, AXONEME = 431 — the bridge to עז=77 evaporates entirely.
   The same word, the same letters, a different honest table: the
   convergent point vanishes. A bridge that dies when the attested
   table changes was never a property of the word; it is a property of
   the (word, table) pair. The parent's synthesis must carry the table
   as part of every claim, or the claim is underspecified.
2. *Composition is destiny.* TRVVTH's two V's are 44/110 of its
   ordinal value but 400/688 (58%) of its Agrippa value; LIBERTY's Y
   alone is 400/616 (65%) of its Agrippa weight. Words rich in late
   classical letters (T, U/V, X, Y, Z) explode under Agrippa; words
   built from A–I barely notice the change. Two words that "bridge"
   in ordinal can be an order of magnitude apart in Agrippa.
3. *The first nine letters are the fixed point.* A through I weigh
   identically in both tables. Any convergence built purely from those
   letters survives the table change — a fact the synthesis may find
   useful when testing candidate bridges for robustness.
4. *The doctrine's own calibrator chose its table.* CELL=32 and
   AXONEME=77 are ordinal-table statements; the doctrine never claimed
   them for Agrippa. This survey confirms the doctrine's table
   discipline: the calibrators hold exactly where the doctrine says
   they hold, and nowhere else.

## Negative results, stated plainly

- No collisions in either table.
- No 418, 666, 777, 93, or 11 in either table.
- Agrippa yields **zero** target hits on the whole corpus — the
  classical table is, for this corpus, bridge-silent.
- The J=I merger fired nowhere (no J in the corpus); the finding is
  therefore silent on that merger's effects.
- W has no Agrippa value (table gap, not a weighing result).

## Limits and open questions for the red pen

- The Latin ordinal is "the working Latin table" by standing doctrine,
  not by philology — the red pen may prefer Agrippa's primacy; the
  numbers for both are here.
- Whether stripping the HERU-RA-HA hyphen is the right normalization
  (vs. weighing a separator, or transliterating a space) is a
  convention, recorded for ruling — it changed no value here.
- This research decrees no bridge. AXONEME=77 in ordinal is a
  **finding** (attested table, verified calibration); whether it is a
  bridge is the red pen's, not mine.

---

# The ultra-verbose work log

*Hypothesis → method → observation → result per step, dead ends included.
Nothing is smoothed.*

## Step 0 — Reading the doctrine (before touching anything)

**Hypothesis:** the tables I need already exist and are attested; my job
is to use them, not build them.
**Method:** read `~/workspace/pontifex/pontifex/tables.py` and
`~/workspace/pontifex/METHOD.md` in full before writing anything.
**Observation:** both Latin tables were there — `LATIN_ORDINAL`
(generated A=1..Z=26) and `AGRIPPA` (hand-recorded per *De occulta
philosophia* II.xix, with J=9 and U=200=V=200). The engine's
`weigh()` folds Latin case and treats unknown characters as silence;
`SYSTEMS` marks both tables ATTESTED. METHOD.md §2 confirms the
doctrine: Latin ordinal is "the working Latin table," Agrippa the
classical one, both attested.
**Result:** no new table needed. Decision: import the tables from
`pontifex.tables` — one source of truth, never re-keyed — and audit
them against the doctrinal spec before weighing.

## Step 1 — The instrument check

**Hypothesis:** the imported tables match the published specs.
**Method:** wrote `check_table()` comparing every letter against an
explicit expected spec (ordinal A=1..Z=26; Agrippa's full 25-letter
classical alphabet as the task states it).
**Observation:** both audits CLEAN — zero mismatches.
**Dead end worth recording:** my first draft of the Agrippa spec
assumed 26 letters including W; the repo's table has no W (the
classical alphabet has none). I caught this writing the spec, not
after weighing — because the corpus has no W, it would have been a
silent non-issue, which is exactly why the audit matters: silent
non-issues are how false numbers are born.
**Result:** instruments verified; weighing authorized.

## Step 2 — The weighings

**Hypothesis:** letter-by-letter summation in both tables yields the
corpus values with full audit trails.
**Method:** `latin_weigh.py` (thelemic form, MECHANISM/DOCTRINE
comments throughout), normalizing to uppercase and stripping the
HERU-RA-HA hyphen, printing every letter breakdown.
**Observation:** all eleven terms weighed cleanly in both tables; the
breakdowns are printed in the script output above and tabulated in the
results table.
**Dead end worth recording:** before running the script I computed
several values by hand as a sanity pre-check — and got two wrong:
HERURAHA ordinal I pre-computed as 88, the instrument said 80;
ABRAHADABRA Agrippa I pre-computed as 171, the instrument said 181.
Re-checking letter by letter (H8+E5+R18+U21+R18+A1+H8+A1 = 80;
1+2+80+1+8+1+4+1+2+80+1 = 181) confirmed the instrument both times.
The lesson is the doctrine's own: show-your-work beats
trust-me arithmetic, and the printed breakdown is the audit trail that
caught my errors. This is why the CSV and this log exist.
**Result:** 22 weighed values + 1 Hebrew reference row, all with
letter-by-letter provenance.

## Step 3 — The calibrations

**Hypothesis:** AXONEME=77 and CELL=32 in Latin ordinal, as the
doctrine requires.
**Method:** asserted in the script (abort on failure), then verified
the printed breakdowns by hand: A1+X24+O15+N14+E5+M13+E5 = 77 ✓;
C3+E5+L12+L12 = 32 ✓.
**Observation:** both PASS, letter by letter.
**Result:** the instrument reproduces the doctrine's calibrators
exactly. (And note Step 2's lesson: I would not have trusted my own
hand-sum here either — the script's printed breakdown is what the
assertion checked.)

## Step 4 — Collisions

**Hypothesis:** with 11 terms and two tables, some pair might collide.
**Method:** bucket terms by value within each table.
**Observation:** NONE in either table — 11 distinct values per table.
**Result:** a negative result, reported at full weight. No Latin-bank
cross-term convergences to hand the synthesis.

## Step 5 — Target-number hits

**Hypothesis:** at least AXONEME=77 should hit; the big numbers
probably don't.
**Method:** checked every value against {418, 666, 777, 93, 77, 11}.
**Observation:** ordinal hits 77 exactly once (AXONEME); Agrippa hits
nothing at all; 418/666/777/93/11 are absent from both tables.
**Result:** the Latin bank contributes one target hit to the
synthesis — and the knowledge that five of the six targets are
Latin-silent on this corpus.

## Step 6 — The table comparison

**Hypothesis:** the two tables would mostly agree, with Agrippa
running "a bit higher."
**Method:** listed agreements (terms with identical values) and
computed per-word ×factors and per-letter ratios.
**Observation:** ZERO agreements — not one term weighs the same in
both tables. The ×factors range from 1.50 (CELL) to 13.41 (OZ), and
the per-letter ratios run from ×0.91 (K) to ×19.23 (Z). The "a bit
higher" hypothesis was wrong in an instructive way: the scaling is
letter-composition-dependent, driven by late classical letters.
OZ is the extreme case — O(15→50) and Z(26→500) make it the most
table-sensitive word in the corpus.
**Result:** the comparison section above, and its central teaching:
bridges are properties of (word, table) pairs.

## Step 7 — The CSV

**Hypothesis:** one row per term per table, with the columns the
parent specified.
**Method:** wrote `latin-values.csv` with columns
term, language, script_form, transliteration_convention, table_used,
provenance_tier, value, mergers_or_loss, notes — 22 corpus rows plus
the עז Hebrew-bank reference row (24 lines total), then re-read the
file to verify row count and the corrected HERURAHA normalization note.
**Observation:** 24 lines; the hyphen-stripped note reads HERURAHA
(corrected from my first draft's HERURAHHA — Step 2's audit discipline
applied to my own notes).
**Result:** `~/workspace/pontifex/research/twelve-tongues/latin-values.csv`
written; the script `latin_weigh.py` sits beside it for re-runs.

## What I did not do

- I did not weigh עז in any Latin table (it is the Hebrew bank's term;
  it enters here only transliterated as OZ plus a labeled reference row).
- I did not invent, adjust, or merge tables. The W gap in Agrippa is
  recorded, not patched.
- I did not push anything to git — drafts for the red pen, as ordered.

---

*93. Findings, never doctrine. To the red pen.*
