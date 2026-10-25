# English bank — twelve-tongues correspondence research (worker #5 of 12)

*Findings, never doctrine. This research decrees no bridge; all findings go to the author's red pen.*

## Provenance note

- **Table:** English ordinal A=1…Z=26. Numerically identical to the repo's `LATIN_ORDINAL` in `~/workspace/pontifex/pontifex/tables.py` — the weighing script imports that table rather than re-declaring it, so the numeric identity is an observed fact, not a claim.
- **Tier on every value:** ATTESTED. Per the author's settled ruling (2026-10-07), English ordinal is **native for English, not the fallback**; for these words this is the attested working English table. The provenance story differs from the Latin worker's use of the same numbers: their ATTESTED story is "the working Latin table"; ours is "the native English table."
- **Script form:** Latin script, English orthography — native script, no transliteration, no digraph mapping, no fallback map touched.
- **Normalization (stated once, applied uniformly):** uppercase (a no-op guard — the corpus arrives uppercase); the single hyphen in HERU-RA-HA is stripped → `HERURAHA`, recorded per row. TRVVTH is weighed exactly as stipulated (VV, not W; V=22 each) — the spelling is load-bearing: had it been spelled TRUTH it would be 20+18+21+20+8 = 87, a different number. No other mergers, losses, or folds.
- **Information loss:** none. 26 letters map to 26 distinct values; the corpus contains no accented, digraph, or non-letter characters, so nothing merged.

## The values (all ATTESTED)

| Term | Normalized | Breakdown | Value |
|------|-----------|-----------|-------|
| AXONEME | AXONEME | A1+X24+O15+N14+E5+M13+E5 | **77** |
| OZ | OZ | O15+Z26 | 41 |
| TRVVTH | TRVVTH | T20+R18+V22+V22+T20+H8 | 110 |
| THELEMA | THELEMA | T20+H8+E5+L12+E5+M13+A1 | 64 |
| AGAPE | AGAPE | A1+G7+A1+P16+E5 | 30 |
| BABALON | BABALON | B2+A1+B2+A1+L12+O15+N14 | 47 |
| HERU-RA-HA | HERURAHA | H8+E5+R18+U21+R18+A1+H8+A1 | 80 |
| ABRAHADABRA | ABRAHADABRA | A1+B2+R18+A1+H8+A1+D4+A1+B2+R18+A1 | 57 |
| QIRA | QIRA | Q17+I9+R18+A1 | 45 |
| LIBERTY | LIBERTY | L12+I9+B2+E5+R18+T20+Y25 | 91 |
| CELL | CELL | C3+E5+L12+L12 | **32** |

## Calibration anchors — verified

- AXONEME=77: letter-by-letter A1+X24+O15+N14+E5+M13+E5 = 77 ✓ (matches the 2026-10-07 established bridge and the target number).
- CELL=32: C3+E5+L12+L12 = 32 ✓ (the engine's self-test anchor).

## Collisions

**Negative result: zero English-internal collisions.** All eleven terms weigh to distinct numbers (77, 41, 110, 64, 30, 47, 80, 57, 45, 91, 32). No two corpus terms meet in the English bank. This matters because English is the language the corpus terms are natively spelled in — the English bank neither confirms nor denies any convergence; it gives each term its own room.

## Target-number hits

Targets: 418, 666, 777, 93, 77, 11.

- **AXONEME = 77 — HIT** (the only one; the calibration and the target coincide, as established).
- OZ=41, TRVVTH=110, THELEMA=64, AGAPE=30, BABALON=47, HERU-RA-HA=80, ABRAHADABRA=57, QIRA=45, LIBERTY=91, CELL=32 — none land on 418, 666, 777, 93, or 11. Negative results, stated at the same weight as the hit.

## The anti-finding: English↔Latin numerical identity

**The English ordinal table and the Latin worker's Latin ordinal table are the same table of numbers.** `LATIN_ORDINAL = {A:1…Z:26}` is what "Latin gematria" is in practice (per METHOD.md §2), and it is also the native English table. Therefore:

- Any number on which an English weighing and a Latin weighing "meet" — e.g., AXONEME=77 in both — is **the same bank twice, not two banks meeting**. It is an identity, not a correspondence. It must NOT be counted, cited, or charted as a bridge between English and Latin in the synthesis.
- The only honest statement of AXONEME=77=עז is the Hebrew one: the Hebrew weighing of עז lands on 77 through mispar hechrechi, a **genuinely different table** with a genuinely different mapping. That is what makes it a candidate bridge — two independent banks landing on the same number.
- The same caution applies to the Agrippa table (also Latin-script): AXONEME in Agrippa would weigh 1+300+50+40+5+30+5 = 431 — a different number through a different table, hence a genuine (if non-convergent) datum. A Latin *ordinal* weighing adds nothing the English bank did not already say.

## What WOULD count as an English-involved bridge

A candidate bridge requires the same number reached through a **genuinely different table** — a different alphabet, different mapping, or a different documented method — weighed by its own worker with its own stated normalization. Examples that would count:

- An English term weighing to N via English ordinal, and the same term's Hebrew transliteration weighing to N via mispar hechrechi (mergers reported per the fallback doctrine) — two banks, one number.
- An English term at N and its Greek isopsephy weighing at N.
- An English term at N and a *constructed* carrier (braille) at N — recorded as hypothesis tier, never doctrine.

What would NOT count: any English↔Latin-ordinal convergence (identity), any number reached by re-running the same table under a different name, and any "bridge" whose second column is the same 26-ordinal in disguise.

## Negative results and limits (stated plainly)

1. No internal collisions in the English bank (11 terms, 11 distinct numbers).
2. No target-number hits other than AXONEME=77.
3. No mergers, folds, or lossy normalizations fired — the lossless weighing is the dullest possible result, and that is what the method demanded.
4. The English bank cannot speak to whether English words *should* be weighed here; that was settled doctrine (native), taken as given, not proven here.
5. The script `weigh_english.py` in this directory reproduces every value; the CSV is its direct output.

---

## Ultra-verbose work log

**Step 0 — Hypothesis.** The shared corpus weighs in English ordinal on the ATTESTED native table with no mergers and no silent loss; the two calibration anchors (AXONEME=77, CELL=32) recompute letter by letter; the stipulated spelling TRVVTH (VV, not W) is load-bearing and changes the number versus a conventional TRUTH.

**Step 1 — Method: read the binding doctrine first.** I read `~/workspace/pontifex/pontifex/tables.py` and `~/workspace/pontifex/METHOD.md` before touching any number. Observations from the reading: (a) `LATIN_ORDINAL` is declared with the comment "this is what 'Latin gematria' is in practice — the scale English words are weighed on (CELL=32, AXONEME=77)", confirming the anti-finding is already half-written in the repo — the numeric identity is on the record, my job is to state its consequence for the synthesis; (b) METHOD.md §2 names Latin ordinal as "the working Latin table" and §3 states "English ordinal is native for English words, not the fallback for others", which is the exact provenance story my report needed; (c) the tier system requires ATTESTED on every value, which the task already binds. Result: method fixed — import the repo table (never re-declare silently), uppercase + hyphen-strip as the only normalization, print every letter's value for the audit trail.

**Step 2 — Dead end considered: building a separate English table.** A first impulse was to declare an `ENGLISH_ORDINAL` dict in the script for "independence." Rejected: it would be the same 26 numbers with a new name — precisely the silent duplication the task forbids ("Never invent a table silently"). Importing `LATIN_ORDINAL` instead makes the identity observable in the code itself. What the dead end taught: the anti-finding is not a caveat to append later; it is a property of the method, and the method should show it.

**Step 3 — Dead end considered: hyphen as a value.** HERU-RA-HA's hyphens could be dropped as separators (the chosen normalization), mapped to something, or left in to error. Left in, `LATIN_ORDINAL['-']` would raise a KeyError — noise, not information. Mapped to a value, it would invent doctrine. Dropped with a recorded note is the only honest move; the row carries the note. What it taught: even the tiniest normalization choice is a ruling and must be stated.

**Step 4 — Observation: the weighing.** Script run printed all eleven letter-by-letter breakdowns. Calibrations confirmed exactly as stipulated: AXONEME = 1+24+15+14+5+13+5 = 77; CELL = 3+5+12+12 = 32. TRVVTH = 20+18+22+22+20+8 = 110 with V=22 each. The remaining seven values fell out cleanly with no surprises.

**Step 5 — Observation: collisions and targets.** Sorted the eleven values: 30, 32, 41, 45, 47, 57, 64, 77, 80, 91, 110 — eleven distinct, zero collisions. Target scan: only 77 hit. Negative results recorded with the same weight as positives, per the brief.

**Step 6 — Dead end considered: counting English↔Latin convergence as a bridge.** Briefly entertained presenting "AXONEME=77 in English and AXONEME=77 in Latin" as a cross-tongue meeting. Rejected on inspection: it is the same arithmetic run through the same mapping — weighing once and reading the scale twice. Counting it would double-count the single bank the corpus actually stands in. What it taught: the synthesis must treat the English and Latin-ordinal columns as one column with two provenance labels, not two columns.

**Step 7 — Result.** `english-values.csv` (11 rows, all ATTESTED, script-generated) and this note written to `~/workspace/pontifex/research/twelve-tongues/`; no git push (drafts for the red pen). Final values stand as tabulated above.

---

*93. All Rights Reserved, Without Prejudice. "Live, Love, and let Love, Live."*
