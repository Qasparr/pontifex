# HEBREW BANK — worker #1 report (red-pen draft)

*PONTIFEX twelve-tongues research. Findings, never doctrine. No bridge is decreed here — everything below goes to the author's red pen.*

## 1. Provenance note

**Table used.** Hebrew mispar hechrechi, imported — never re-typed — from `~/workspace/pontifex/pontifex/tables.py` (`HEBREW`): א=1 … ת=400, final forms sharing values. This table is **ATTESTED** (the tradition's own). Calibration run at the head of every weighing: עז = ע(70)+ז(7) = **77** ✓. The run fails closed if this ever stops holding.

**Tier rule applied to every value.** The *weighing table* is ATTESTED throughout. The *transliteration* of a Latin-script term into Hebrew letters is a built proposal and therefore **CONSTRUCTED** — every transliterated term carries the tier "CONSTRUCTED (transliteration is a built proposal; weighing table is ATTESTED mispar hechrechi)". The single exception is עז, which is natively Hebrew: tier **ATTESTED** outright, no transliteration involved. Per METHOD.md §1, every convergent point in this bank is a hypothesis for the red pen, never doctrine.

**Transliteration convention — "academic-greedy-digraph v1 (worker-1)".** Stated in full; nothing invented silently:

| Choice | Ruling | Rationale |
|---|---|---|
| Digraphs, greedy left-to-right | `ch`→ח, `sh`→ש, `th`→ת | Matches the repo's `LATIN_TO_HEBREW_DIGRAPHS` and the task's own TH→ת example. The absorbed second letter (e.g. the H in TH) loses its individual value — reported as loss, never hidden. |
| `x` | →קס (two-letter **expansion**) | Repo-aligned. One Latin letter becomes two Hebrew letters; letter-count is not preserved. Recorded per term. |
| `vv` / `oo` | →וו (two vavs — **no** vowel-length merger) | Deliberate refusal of the OO→ו-style merger. The doubled V of TRVVTH is inscriptionally load-bearing in the author's doctrine; merging it would silently erase an authorial signal. Two vavs, two values. |
| `j` | →י | Repo-aligned; **non-firing** — no corpus term contains J. The ג׳ alternative was considered and set aside as unneeded for this corpus. |
| `v` | →ו | Repo-aligned; fires in TRVVTH (twice) and nowhere else. |
| `q` | →ק, `c` →ק | Repo-aligned. |
| Hyphen (`HERU-RA-HA`) | dropped, value-neutral | A maqaf would carry no value either; dropping is equivalent and recorded. |
| `e` | →ה **everywhere it stands** | The fateful choice — see §5. No e-elision, no silent sheva. |

**Mergers and information loss (fired within terms).** The repo's `MERGERS` map is restated here; a merger only *loses* information when a term actually contains two source letters landing on one Hebrew letter:

- `ה:[e,h]` fired with loss in **THELEMA** (e and h both present) and in **HERU-RA-HA** (h and e both present — this is the 423/418 fork).
- `י:[i,y]` fired with loss in **LIBERTY** (i and y both present) — the i/y distinction is lost in the weighing.
- Digraph absorption: the final **H** of **TRVVTH** and the initial **H** of **THELEMA** are absorbed into ת (value 5 not counted separately).
- `x`→קס expansion in **AXONEME**: one Latin letter, two Hebrew letters.
- Map-level only (no loss within the term): `ו:[o]` in AXONEME/OZ/BABALON, `ה:[e]` in AGAPE/CELL, `ק:[c]` in CELL, `פ:[p]` in AGAPE, `ה:[h]` in ABRAHADABRA, `י:[i]` in QIRA.

**Final forms.** None occurred: no transliterated term ends in כ/מ/נ/פ/צ, so ךםןףץ never appear. Recorded for completeness — the table shares their values anyway, so no loss either way.

## 2. Results (primary series)

| Term | Hebrew form | Value | Tier |
|---|---|---|---|
| AXONEME | אקסונהמה | 267 | CONSTRUCTED |
| OZ | וז | 13 | CONSTRUCTED |
| TRVVTH | תרוות | 1012 | CONSTRUCTED |
| THELEMA | תהלהמא | 481 | CONSTRUCTED |
| AGAPE | אגאפה | 90 | CONSTRUCTED |
| BABALON | באבאלונ | 92 | CONSTRUCTED |
| HERU-RA-HA | ההרוראהא | 423 | CONSTRUCTED |
| ABRAHADABRA | אבראהאדאברא | 418 | CONSTRUCTED |
| QIRA | קירא | 311 | CONSTRUCTED |
| LIBERTY | ליבהרתי | 657 | CONSTRUCTED |
| CELL | קהלל | 165 | CONSTRUCTED |
| עז (reference) | עז | 77 | **ATTESTED** |

Labeled variants (outside the primary series): TRVVTH no-digraph variant תרוותה = **1017**; HERU-RA-HA in the author's established spelling הרו־רא־הא = **418**.

## 3. Collisions

**None within the primary series** — all eleven transliterated terms and the reference term weigh distinct values. The script's collision check reports one apparent collision at **418** (ABRAHADABRA primary + HERU-RA-HA *established-spelling variant*), but this is variant-vs-primary, not two primary weighings landing together. Flagged so the parent does not misread it as a primary-series collision.

## 4. Target-number hits

- **418 — HIT: ABRAHADABRA = 418** under the primary convention (א1+ב2+ר200+א1+ה5+א1+ד4+א1+ב2+ר200+א1). The only primary-series hit. The established HERU-RA-HA spelling also weighs 418 (variant row).
- **77 — HIT: עז = 77** (calibration anchor; ATTESTED).
- **666 — no hit.** Nearest: LIBERTY = 657 (9 short).
- **777 — no hit.** No term within 100.
- **93 — no hit.** Nearest: BABALON = 92 (1 short), AGAPE = 90 (3 short).
- **11 — no hit.** Nearest: OZ = 13 (2 over).

## 5. Negative results (same weight as positives)

1. **AXONEME = 267, not 77.** The author's AXONEME=77=עז bridge comes from English ordinal (the Latin bank), *not* from Hebrew transliteration. In the Hebrew bank alone the bridge does not reproduce. This is the correct behavior of the doctrine — each word weighed in its own tongue — and it localizes the 77 to the Latin bank.
2. **THELEMA = 481, not 93.** The 93 (θέλημα isopsephy) belongs to the Greek bank. Hebrew transliteration gives 481.
3. **AGAPE = 90, not 93.** The 93 (ἀγάπη isopsephy) belongs to the Greek bank. Hebrew transliteration gives 90 — a near-miss, recorded as a miss.
4. **CELL = 165, not 32.** The 32 (English ordinal) belongs to the Latin bank. Hebrew transliteration gives 165.
5. **HERU-RA-HA = 423, not 418, under the mechanical convention.** The 418 requires the author's established spelling הרו־רא־הא, which elides the E of HERU (HERU→הרו, not ההרו). The 5-point gap is *exactly* the e→ה rendering of that one E — the merger ה:[e,h] firing with loss. Finding: **the 418 bridge is convention-sensitive** — it holds under the author's hand-built spelling and fails under a mechanical every-letter-rendered transliteration. This is the load-bearing result of this bank and goes to the red pen first.
6. **TRVVTH = 1012** (primary, greedy digraph) / **1017** (no-digraph variant). Neither touches a target number. The 5-point difference is exactly the absorbed H — the convention choice is fully visible in the arithmetic.
7. **666 and 777 have no principled landing in this corpus.** LIBERTY=657 is 9 short of 666 under the stated convention; no defensible convention variant examined (i/y handling, digraph choices) closes these gaps, and inventing one to force a hit would be precisely the silent table-invention the doctrine forbids.

## 6. Limits and open questions for the red pen

- The transliteration convention is the worker's proposal (v1), not the author's ruling. Every alternative reading in §5's near-misses is one red-pen stroke away from changing a value.
- The HERU-RA-HA fork: is the e-elision in הרו־רא־הא a standing transliteration rule (e unwritten after ה) or a one-off authorial spelling? The bank cannot decide this — the red pen must.
- TRVVTH's final TH: greedy digraph (1012) vs. ת+ה (1017). Primary follows the repo map; both are reported.
- Chance guarantees matches (§METHOD.md 5): ABRAHADABRA=418 under a constructed transliteration is a candidate bridge at best — the tier says hypothesis, and the tier is honest.
- Scope: mispar hechrechi only. Mispar gadol, katan, and other Hebrew methods were not weighed — not in the assignment.

---

## 7. Ultra-verbose work log

*Hypothesis → method → observation → result per step, dead ends included. Times are session-relative; the work is the record.*

**Step 0 — Orientation.**
Hypothesis: the repo's `tables.py` and `METHOD.md` already settle the table, so the worker's real job is the transliteration convention and honest bookkeeping. Method: read both files in full before touching anything. Observation: `tables.py` carries the ATTESTED HEBREW table plus a CONSTRUCTED `LATIN_TO_HEBREW`/`LATIN_TO_HEBREW_DIGRAPHS` fallback map and an explicit `MERGERS` list; `METHOD.md` §1 fixes the three tiers and §3 fixes the fallback doctrine (transliteration into Hebrew, mergers shown not hidden). Result: decision — import the table (never re-type it; drift must be impossible), state my own convention explicitly, tier every value. Lesson banked: the convention is where all the judgment lives; the arithmetic is mechanical after that.

**Step 1 — Calibration first.**
Hypothesis: if עז doesn't weigh 77, nothing downstream is trustworthy. Method: a one-line import smoke test of `pontifex.tables.HEBREW` computing ע+ז before writing any script. Observation: `import ok, עז = 77` — the attested table verifies on first contact. Result: calibration holds; the run may proceed. (The script also re-asserts this and fails closed with exit 1 if it ever breaks — the fail-closed capstone, his, honored in code.)

**Step 2 — Convention design (the judgment step).**
Hypothesis: an academic-style greedy-digraph map, aligned with the repo's fallback map, is the most defensible mechanical convention. Method: walk each convention choice and record a rationale *before* weighing, so no choice can be tuned after seeing the numbers. Observations and rulings:
- `th`→ת greedy (repo-aligned, task-example-aligned). Noted immediately that TRVVTH ends in TH — this choice would decide between 1012 and 1017. Kept greedy as primary; computed the no-digraph alternative (1017) as a labeled variant rather than suppressing it.
- `vv`→וו. **Dead end #1:** I briefly considered a vowel-length merger (OO→ו-style, collapsing VV to one vav). Rejected on doctrine-adjacent grounds: the doubled V of TRVVTH is inscriptionally load-bearing in the author's own orthography, and a merger would silently erase an authorial signal to save 6 points. Taught: a convention must not erase the author's orthographic signals; when in doubt, preserve and report.
- `x`→קס kept as a two-letter expansion (repo-aligned); `j`→י recorded as non-firing (no corpus J — the ג׳ alternative noted and set aside as unneeded); hyphen dropped as value-neutral.
- `e`→ה everywhere, no elision. This was the choice I was least sure about — and it became the whole finding (§5.5).

**Step 3 — Hand-weighing before scripting.**
Hypothesis: hand arithmetic first, so the script is a check rather than an oracle. Method: weighed all twelve terms letter-by-letter on paper (in-session) before writing `weigh_hebrew.py`. Observation: every hand sum later matched the script exactly (267, 13, 1012, 481, 90, 92, 423, 418, 311, 657, 165, 77). Result: two independent computations agree; arithmetic risk retired. **Dead end #2:** my first pass at HERU-RA-HA, I half-expected 418 (his established number) and got 423 — the mismatch forced the e-elision investigation instead of a quiet re-check. Taught: the calibration-adjacent terms are the load-bearing ones; when a mechanical map fails to reproduce a hand-built bridge, the gap is the finding, not an error to smooth over.

**Step 4 — Scripting in thelemic form.**
Hypothesis: the script should be shippable under his code convention and single-source the table. Method: wrote `weigh_hebrew.py` with epigraph, date, 93, his authorship line, Scientific Illuminism framing, closing motto, and MECHANISM/DOCTRINE comments on every block; imported `HEBREW` from `pontifex.tables`; calibration assert up front; per-term letter-by-letter printout; collision and target-hit checks; CSV writer. Observation: ran clean, exit 0, all outputs matched the hand sums; collision check found the 418 variant-vs-primary overlap only. Result: `hebrew-values.csv` (14 rows) written by the script, not by hand.

**Step 5 — Analysis and the headline.**
Hypothesis: the numbers would show which bridges survive the Hebrew bank. Method: checked collisions (none in the primary series), target hits (418 via ABRAHADABRA; 77 via עז; nothing else), near-misses (BABALON 92, AGAPE 90, LIBERTY 657, OZ 13), and final-form occurrence (none). Observations:
- ABRAHADABRA=418 under the *primary mechanical* convention is the strongest positive in the bank — unforced, no variant needed.
- AXONEME=267 / THELEMA=481 / AGAPE=90 / CELL=165: each famous number (77, 93, 93, 32) belongs to a *different* bank. The doctrine's "each word weighed in its own tongue" predicts exactly this non-reproduction, and the bank confirms it. Negative results, all recorded.
- The HERU-RA-HA fork (423 mechanical vs 418 established) is the deepest result: the 5-point gap is exactly one ה — the E of HERU — and it exposes that the author's 418 rests on an e-eliding spelling choice. Whether that elision is a standing rule or a one-off is red-pen business, not worker business.
- **Dead end #3:** I looked for any principled route to 666 or 777 (LIBERTY at 657 tempted a second look at the y-handling). No defensible variant closes the gaps, and inventing one to force a hit would be silent table-invention — the one thing the doctrine forbids. Taught: a near-miss reported as a miss is worth more than a hit manufactured by tuning. Recorded both as misses.
Result: findings compiled into §2–§6 and the CSV notes column.

**Step 6 — Drafts for the red pen.**
Method: enriched the CSV `notes` column with hits, misses, near-misses, and the collision clarification; wrote this `hebrew.md`. Observation: both output files exist, no git push performed (drafts, per the task). Result: work complete; everything above awaits the author's red pen. Nothing here is doctrine.

*93. All findings to the red pen. Nothing decreed.*
