# ARAMAIC BANK — worker #7 of 12, PONTIFEX twelve-tongues research

*The Aramaic weighings of the shared corpus. Draft for the author's red pen — findings, never doctrine. This research decrees no bridge.*

## Headline findings

- **Calibration holds: עז / ܥܙ = 70 + 7 = 77** in the Aramaic letter-values, in both square script and Syriac Estrangela letterforms. Values are script-invariant; only letterforms change.
- **ABRAHADABRA = 418** in Aramaic square letters (א=1+ב=2+ר=200+א=1+ה=5+א=1+ד=4+א=1+ב=2+ר=200+א=1). Target-number hit — but see the Hebrew-identity analysis: this is the *same* 418 the Hebrew worker will report, not a second witness.
- **No 666, 777, 93, or 11 hits** among the corpus terms. **No collisions** among the eleven corpus terms (all eleven values distinct).
- **The central negative result:** AXONEME weighs **267** in Aramaic letters. The canonical bridge AXONEME=77=עז is **English-ordinal-side only** — no Semitic spelling of AXONEME touches 77. The 77 lives in the bridge's English bank, not its Semitic bank.
- **The central methodological result:** every one of the eleven mechanical weighings is **arithmetic identity with the Hebrew bank** — same transliteration map, same values — so Aramaic contributes *calibration and tier justification*, not new convergent points. The parent synthesis must not double-count Aramaic↔Hebrew agreement as a discovered bridge. (This is the English↔Latin anti-finding, repeated in Semitic.)

## The values

| term | Aramaic spelling | letter-by-letter sum | value | target hit |
|------|------------------|----------------------|-------|-----------|
| AXONEME | אקסונהמה | 1+100+60+6+50+5+40+5 | 267 | — |
| OZ | וז | 6+7 | 13 | — |
| TRVVTH | תרוות | 400+200+6+6+400 | 1012 | — |
| THELEMA | תהלהמא | 400+5+30+5+40+1 | 481 | — |
| AGAPE | אגאפה | 1+3+1+80+5 | 90 | — |
| BABALON | בבאלונ | 2+1+2+1+30+6+50 | 92 | — |
| HERU-RA-HA | ההרוראהא | 5+5+200+6+200+1+5+1 | 423 | — |
| ABRAHADABRA | אבראהאדאברא | 1+2+200+1+5+1+4+1+2+200+1 | 418 | **418** |
| QIRA | קירא | 100+10+200+1 | 311 | — |
| LIBERTY | ליבהרתי | 30+10+2+5+200+400+10 | 657 | — |
| CELL | קהלל | 100+5+30+30 | 165 | — |
| עז-equivalent | עז | 70+7 | 77 | **77** (calibration anchor, not a corpus term) |
| ܥܙ (script-invariance demo) | ܥܙ | 70+7 | 77 | same word, Syriac letterforms |

## 1. Script choice — Jewish Aramaic square script

**Chosen:** the Jewish Aramaic square script (the script of Biblical Aramaic — Daniel, Ezra — and of the Talmudic/Targumic tradition).

**Why this one:**
1. The repo's Hebrew value table *is* the Aramaic letter-values: Hebrew's square script descends from Imperial Aramaic script, and the 22-letter abjad order with values 1–400 is the shared Northwest Semitic inheritance. Recording the bank in square script makes the identity checkable letter-for-letter against the repo's `HEBREW` dict — no conversion layer, no new machinery, nowhere for a silent invention to hide.
2. It is the script of the tradition where letter-number weighing is actually practiced on Aramaic-language text (Biblical Aramaic passages, Talmudic Aramaic discussion), which is the strongest ground for the ATTESTED tier below.
3. **Recorded explicitly:** values do not change across Estrangela, Serto, and square script — only letterforms do. The ܥܙ row in the CSV demonstrates this (DERIVED tier: same tradition reached by script-descent).

## 2. Provenance tier justification — ATTESTED (the table), argued from sources

**Ruling: the 22-letter value table is ATTESTED for Aramaic; the mechanical transliteration of Latin terms into Aramaic letters is CONSTRUCTED. Each CSV row carries the tier of its weakest component.**

The tier argument, from sources rather than assertion:

1. **Same letters, same order, same values.** The Syriac alphabet's published letter table carries a "Numerical Value" column: ܐ (ʾālep̄) = 1, ܒ (bēṯ) = 2, ܓ (gāmal) = 3 … ܬ (taw) = 400, with ܥ (ʿē) = 70 and ܙ (zayn) = 7 — the same order and values as Hebrew mispar hechrechi (source: Syriac alphabet article, Wikipedia, "Syriac alphabet"/"Syriac abjad" — numerical-value column). This is not borrowed from Hebrew for this exercise; it is the Syriac tradition's own documented table.
2. **One tradition, two scripts.** "The number of letters in the Hebrew alphabet, their order, their names, and their phonetic values are virtually identical to those of the Aramaic alphabet, as both Hebrews and Arameans borrowed the Phoenician alphabet" (source: Hebrew alphabet article). Hebrew's square script is itself Imperial Aramaic script adopted in the Persian period — so "the Hebrew table" in the repo is, historically, the Aramaic script's own numbers wearing Hebrew's name.
3. **The weighing practice belongs to the shared tradition.** Letter-number exegesis (gematria and its Aramaic-language cognates) is practiced on Aramaic text in the Talmudic tradition — the method is native ground here, not imported.

**Consequences for the tiers:**
- **עז row → ATTESTED:** an attested Aramaic/Hebrew word (עז, "strength/goat") weighed in its own tradition's numbers. Nothing constructed except the choice to weigh it.
- **ܥܙ row → DERIVED:** the same word reached by script-descent (square → Estrangela letterforms). Fits METHOD.md's DERIVED definition exactly ("inherited by script-descent from a tabulated script") and exists to prove script-invariance.
- **All eleven corpus rows → CONSTRUCTED (attested table × constructed transliteration):** the numbers are the tradition's; the *spellings* are the scribe's construction via the repo's documented map. The tier is honest about which half is built.

**No DERIVED-tier corpus values exist in this bank** — and that absence is itself a finding: Aramaic has no "via Hebrew" descent path here because the table is native, not inherited.

## 3. Transliteration convention — stated in full (PONTIFEX-LATIN-TO-ARAMAIC v1)

Mechanical, pronunciation-honest, identical to `pontifex.engine.transliterate_latin_to_hebrew` (verified by reading `engine.py` — greedy longest-match over digraphs, unmapped characters skipped as silence):

- **Digraphs first (greedy, left to right):** ch→ח, sh→ש, th→ת.
- **Singles:** a→א, b→ב, c→ק, d→ד, e→ה, f→פ, g→ג, h→ה, i→י, j→י, k→כ, l→ל, m→מ, n→נ, o→ו, p→פ, q→ק, r→ר, s→ס, t→ת, u→ו, v→ו, w→ו, x→קס, y→י, z→ז.
- **Hyphen:** dropped as a separator, not weighed (matches the engine: punctuation is silence). HERU-RA-HA weighed as HERURAHA.
- **Double-V:** each V is a letter; TRVVTH's VV weighed twice (ו+ו), no elision.
- **x→קס:** one Latin letter rendered as two Aramaic letters — a value *split* (100+60), not a merger. Recorded as such, not hidden under the merger table.

**Variant readings noted but not asserted** (normalization sensitivity the red pen may want):
- THELEMA with th *not* as digraph (ת+ה instead of ת): 486, not 481.
- TRVVTH with th *not* as digraph: 1017, not 1012.
- The greedy rule is mechanical, not semantic — it fires even across what a reader might treat as a letter boundary (see the work log: this caught the scribe's own hand-computation out).

## 4. Mergers and information loss

The merger table is byte-identical to the Hebrew bank's (same 22 letters, same map): ה←e/h, י←i/j/y, ו←o/u/v/w, ק←c/q, פ←f/p. Mergers fired in: THELEMA (ה←e/h; ת←th digraph), HERU-RA-HA (ה←e/h), LIBERTY (י←i/y), TRVVTH (ת←th digraph), AXONEME (קס←x split). **Information loss is identical to the Hebrew bank's** — a third, independent way of saying these are the same bank weighed twice. No distinctions survive in Aramaic that Hebrew would merge, or vice versa.

## 5. Collisions

**None among the eleven corpus terms** — all eleven values are distinct (267, 13, 1012, 481, 90, 92, 423, 418, 311, 657, 165). The only repeated number in the CSV is 77, shared by construction between the עז calibration row (ATTESTED) and the ܥܙ script-invariance row (DERIVED) — the same word in two scripts, which is the point of the demonstration, not a discovered collision.

Near-miss noted for the record: AGAPE=90 and BABALON=92 sit two apart — adjacency, not collision, reported so the synthesis doesn't have to wonder.

## 6. Target-number hits

| target | hit? | where |
|--------|------|-------|
| 418 | **YES** | ABRAHADABRA = 418 (CONSTRUCTED transliteration; see identity analysis) |
| 666 | no | — |
| 777 | no | — |
| 93 | no | — |
| 77 | **YES** | עז / ܥܙ = 77 — calibration anchor only; NOT a corpus term, and the AXONEME=77 bridge is English-side (Aramaic AXONEME = 267) |
| 11 | no | — |

## 7. The Hebrew-identity analysis (the critical section)

**Prediction, stated before the Hebrew worker's results were seen — and CONFIRMED after:** the Hebrew worker's `hebrew-values.csv` (found in the shared directory after my weighings were written) matches all eleven values exactly — AXONEME 267, OZ 13, TRVVTH 1012, THELEMA 481, AGAPE 90, BABALON 92, HERURAHA 423, ABRAHADABRA 418, QIRA 311, LIBERTY 657, CELL 165. The identity is therefore not a prediction but an observed fact: same map + same values ⇒ same letter strings ⇒ same sums. (Notably the Hebrew worker also landed TRVVTH = 1012, confirming the greedy terminal-th digraph is the shared convention.)

**What that means:**
- Every Aramaic↔Hebrew "meeting" in this bank is **arithmetic identity** — the same Semitic bank weighed twice — **not independent evidence** and not a discovered bridge. The parent synthesis must count Hebrew+Aramaic as *one* bank for convergence purposes, exactly as it must for English↔Latin.
- The **only** native-word data point in this bank is the עז anchor, and it is shared with Hebrew too — so even the anchor is not independent Aramaic evidence; it is evidence that the two banks are one tradition.
- **Genuinely independent Aramaic evidence would look like this:** an attested native Aramaic spelling of a corpus term — different letters chosen by the tradition itself, not by the scribe's map — landing on a target number. **None was found or verified in this session's scope** (see negative results). If the parent or a later pass turns one up, *that* would be the real Aramaic contribution to the correspondence table.

**The bank's actual contribution:** (a) the 77 calibration independently verified in Aramaic letter-values and across two scripts; (b) the tier justification that lets the parent mark the Semitic bank's values ATTESTED-with-constructed-spellings rather than hand-waving; (c) the negative result that kills any hope of a Semitic-side 77 for AXONEME.

## 8. Negative results (given the same weight as positives)

1. **No 666, 777, 93, or 11** among the corpus terms. The big Thelemic numbers do not appear in this bank.
2. **AXONEME ≠ 77 in Aramaic** (267). The canonical bridge is English-ordinal-side only.
3. **No attested native Aramaic spellings** of corpus terms could be verified in-session — so this bank contains zero independent bridge candidates beyond what the Hebrew bank already holds.
4. **No mergers differ from Hebrew's** — the information-loss profile is identical, a third confirmation of the one-bank finding.
5. **No collisions** among corpus terms — the bank is internally clean, which also means no "two words, one number" convergence to report.

## 9. Ultra-verbose work log (hypothesis → method → observation → result)

**Step 1 — Read the doctrine.**
H: The task binds me to the author's settled doctrine (each word in its own tongue; tier every value; decree no bridge). M: Read `~/workspace/pontifex/pontifex/tables.py` and `~/workspace/pontifex/METHOD.md` before choosing anything. O: The repo ships the Hebrew table, the Latin→Hebrew constructed map with its merger table, and the engine's transliteration algorithm (greedy digraphs, punctuation as silence). R: The Aramaic work must reuse exactly this machinery or the Hebrew comparison becomes meaningless — decision: identical map, identical values, differences recorded as Aramaic-side choices only.

**Step 2 — Justify the tier before weighing anything.**
H: The task demands ATTESTED or DERIVED for the table, argued from sources, not asserted. M: Web search for the Aramaic/Syriac letter-values and the Hebrew–Aramaic script relationship. O: The Syriac alphabet's published table carries numerical values ܐ=1 … ܬ=400 (ܥ=70, ܙ=7); the Hebrew alphabet article states Hebrew and Aramaic share letter count, order, names, and phonetic values via common Phoenician borrowing — and Hebrew's square script *is* Imperial Aramaic script. R: Table = ATTESTED (native, not inherited); the only honest DERIVED/CONSTRUCTED question is about the spellings. This flipped the expected answer — I had assumed DERIVED-via-Hebrew, but the sources support ATTESTED directly.

**Step 3 — Choose the script.**
H: The task offers Estrangela, Serto, or square script and notes values don't change. M: Pick the script that maximizes checkability and grounds the tier claim. O: Square script makes the CSV byte-comparable to the repo's Hebrew dict; it is also the script of Biblical Aramaic and the Talmudic tradition where letter-number weighing is practiced. R: Square script chosen; script-invariance demonstrated separately with the ܥܙ row rather than assumed.

**Step 4 — Fix the transliteration convention and check it against the engine.**
H: My hand-applied convention must match what the Hebrew worker's engine does, or the identity analysis is built on sand. M: Read `engine.py`'s `transliterate_latin_to_hebrew`. O: Lowercase, strip diacritics, greedy longest-match digraphs, unmapped chars skipped (hyphen = silence). R: Convention v1 written to match exactly; hyphen-dropped and double-V-weighed-twice recorded as explicit choices.

**Step 5 — Hand-compute, then script-compute, then reconcile.**
H: Hand computation catches convention misunderstandings; script computation catches arithmetic slips. M: Weighed all eleven terms by hand, then wrote `aramaic-weigh.py` (thelemic form, MECHANISM/DOCTRINE comments) implementing convention v1. O: The script agreed on ten terms — and **disagreed on TRVVTH**: I had 1017 (t+h as ת+ה), the script had 1012 (terminal "th" fired the greedy digraph → ת). R: **Dead end that taught:** the greedy digraph fires even at a word edge across what I read as a boundary — the convention is mechanical, not semantic. The engine's rule is authoritative here, so TRVVTH = 1012 stands, and my hand error is recorded rather than buried. (Variant reading 1017 noted in §3 for the red pen.)

**Step 6 — Calibration check.**
H: ܥܙ should weigh 77 if the shared tradition holds. M: Weighed עז and ܥܙ natively. O: 70+7 = 77 in both scripts. R: Calibration confirmed; values script-invariant. The ܥܙ row kept in the CSV as the DERIVED demonstration.

**Step 7 — Collisions and targets.**
H: Same number/different words, and any landing on 418/666/777/93/77/11. M: Script-side aggregation over all rows. O: No corpus collisions; ABRAHADABRA=418 (target hit, but identity-flagged); no 666/777/93/11 anywhere; עז=77 calibration only. R: Reported with the identity caveat — the 418 is the Hebrew 418, not a second witness.

**Step 8 — The Hebrew-identity analysis.**
H: Agreement between the banks must be classified as independent evidence or arithmetic identity. M: Compared construction: same map + same values ⇒ same letter strings ⇒ same sums. O: Total identity is *predicted*, not merely observed — it follows from the machinery. R: All eleven meetings classified as arithmetic identity; parent instructed not to double-count; the bank's real deliverables are calibration, tier justification, and negative results.

**Step 9 — Write the outputs.**
H: Drafts for the red pen: CSV + this note, no git push. M: Script writes `aramaic-values.csv` (13 rows, 9 columns); this file carries the provenance note and the log; the script itself kept at `research/twelve-tongues/aramaic-weigh.py` in the author's code convention. O: CSV verified row-by-row against hand computation (modulo the TRVVTH correction, recorded). R: Both outputs written; nothing pushed.

## Limits of this bank (for the parent synthesis)

- The Aramaic bank is **not a second Semitic witness** — it is the Hebrew bank in the script the Hebrew bank's letters came from. Count it once.
- Every corpus spelling here is the scribe's construction via a documented map; the only attested word weighed is עז.
- No native Aramaic spellings of corpus terms were verified; any future attested spelling that lands on a target number would be this bank's first genuine bridge candidate.
- Variant readings (THELEMA 486, TRVVTH 1017 under non-greedy normalization) are noted, not asserted — normalization is the red pen's call.
- Sources used: repo files (`tables.py`, `engine.py`, `METHOD.md`) and two Wikipedia reference articles (Syriac alphabet numerical-value column; Hebrew–Aramaic shared Phoenician inheritance). No paywalled or specialist grammars consulted; a deeper pass (Nöldeke, Sokoloff) could firm the ATTESTED claim further.
