# Worker Log — Worker A: Census Regeneration + Reconciliation (final Black's Teacher's Edition build)
Date: 2026-10-25. Worker: A. Constraints honored: no git push; no 5th-edition entry text reproduced in any output (headwords + status metadata only — 5e entries were read transiently during the verification pass and are quoted nowhere, including this log).

---

## 1. Orientation — read the sources first

**Hypothesis:** The task is fully determined by four artifacts: the census engine `5e/analyze.py`, its published `analytics.json` + `worker-log.md`, the base parser `2e/parse_blacks2e.py`, and the shipped base parse `2e/entries.json` (13,145 entries).

**Method:** Read all four before writing any code. Extracted the load-bearing rules:
- Census (`analyze.py`): 5e dual pattern over the study text (John's inline regex verbatim + own-line pattern); 2e dual pattern over the djvu text, body indices from the first `^A\.\s` line to hardcoded 206775; `PAGE_ARTIFACT` guard `^[A-Z] \d{2,}\.?$`; join key `norm()` = lowercase alphanumeric only; dedup longest-kept.
- Census 2e patterns: `HEAD2_INLINE = ^([A-Z][A-Z0-9&'\- ]{1,55})\.\s`, `HEAD2_OWN = ^([A-Z][A-Z0-9&'\- ]{2,50})\.$` — character class admits only A–Z, digits, `&`, straight `'`, `-`, space; total length 2–56 (inline) / 3–51 (own-line); no preceding-blank requirement; no body-content reject.
- Base parser: `HW` requires a preceding blank line (or page-break-block equivalent), period + **two** spaces (`\.\s\s`), admits single-letter dotted prefixes `(?:[A-Z]\.\s{1,2})*`, commas, parentheses, curly quotes `’‘`; `HW_ONLY` for headword-only lines; wrapped-headword joining across lines; guillemet `«` stripping; digit/`;`/`)` body-remainder rejects; a post-pass dropping page-top repeated heads.

**Observation:** The two parsers differ in at least seven independent dimensions (character class, length bounds, blank-line guard, terminator spacing, body rejects, wrapping, artifact guard) — more than enough machinery to explain a 253 gap in both directions. Also noted: `analytics.json` records e2 parse forms as 13,078 inline + **0** own-line, which is suspicious on its face and worth watching in regeneration.

**Result:** Proceed to regeneration with an instrumented copy of the census logic (identical regexes/ranges/dedup; only addition: record each row's line number, needed later for the same-line tests).

## 2. Line-splitting sanity check (a dead end, closed cheaply)

**Hypothesis:** A subtle risk: the census reads the djvu text with `splitlines()` while the base parser uses `split("\n")`. If the djvu file contained `\r`, form feeds, or Unicode line separators, `splitlines()` would split where `split("\n")` does not, silently shifting every line index between the two parses and poisoning any line-based comparison.

**Method:** Counted line totals under both splits and counted every candidate separator character in both source texts.

**Observation:** Djvu: `splitlines()` = 221,768, `split("\n")` = 221,769 (the +1 is the trailing empty after the final newline — same indexing); zero `\r`, `\x0b`, `\x0c`, `\u2028`, `\u2029`, `\x85`. The *study* text does contain 433 form feeds (which is why the census's 5e line indices differ from a naive `\n` count — but the census defines its own 5e parse, so this is its documented behavior, reused exactly).

**Result:** Dead end closed: 2e line indices are directly comparable between the parsers. Base entry `line` fields (1-indexed) map to djvu index `line − 1` with no shift.

## 3. Regeneration

**Hypothesis:** Re-running the census logic reproduces the published aggregates exactly (21,979 / 12,892 / 3,881 / 9,011 / 18,098).

**Method:** Instrumented copy of `analyze.py`'s `parse5`/`parse2`/`uniq`/`norm`, run against the same input files.

**Observation:** Exact reproduction on every figure, including parse forms: 5e 26,420 rows (14,595 inline + 11,825 own-line), 21,979 unique; 2e 13,078 rows (13,078 inline + 0 own-line), 12,892 unique; survived 3,881, lost 9,011, new 18,098. The "0 own-line" oddity from §1 also reproduced — it is a property of the data (djvu headword-only lines evidently carry trailing content/space that routes them through the inline pattern), not a transcription error in `analytics.json`. Regenerated body windows: 5e indices 1221–210281; 2e indices 546–206775 (1-indexed lines 547–206775).

**Result:** Gate passed; proceed. (Had this failed, the task instructed stopping here and reporting the mismatch instead.)

## 4. Top-level gap arithmetic

**Hypothesis:** The 253 is a composite, not a single mechanism: base entries (13,145) vs census keys (12,892) differ by duplicate-key collapses inside the base parse, base-only keys, and census-only keys.

**Method:** Built base norm keys (`norm()` over `entries.json` headwords), intersected with the regenerated census-2e key set.

**Observation:** Distinct base keys = 13,028 (117 entries collapse onto earlier keys; 91 distinct keys carry the extras). |base ∩ census| = 12,506; |base − census| = 522; |census − base| = 386. Check: 117 + 522 − 386 = 253 = 13,145 − 12,892. ✓ Duplicate examples: `L` ×5 (lines 4085, 89928, 116063, 116079, 176641); `A. D` (line 576) + `AD` (line 5329); `A RETRO` / `ARETRO`; `ABATOR` ×2.

**Result:** The 253 is fully accounted at the top level. Remaining work: categorize the 522 (required) and, for the register reconciliation, the 386.

## 5. First pass at the 522 — three quick probes

**Hypothesis:** Most base-only keys will fail the census patterns for visible reasons (characters, length, range, artifact).

**Method:** (i) Range probe: min/max djvu line over base-only entries. (ii) Artifact-shape probe: headwords matching `^[A-Z] \d{2,}$`. (iii) Same-line probe: does any census row sit at a base-only entry's first line (which would mean same row, different key)? (iv) Character inventory of base-only headwords vs the census class; length inventory.

**Observation:** (i) Lines 555–206644 — all strictly inside the census window 547–206775 → range cause (c) is **zero** for base-only keys. (ii) Exactly 1 artifact-shaped headword: I 1180. (iii) Same-line probe: 0 same-key, **0 different-key**, 522 no-row — the census produced *nothing* at those lines; cause (d) in its literal same-row form is zero, which pushed me to look at multi-line headwords (see §6). (iv) Characters outside the census class: `,` in 248 headwords, `’` in 81, `.` in 90, `)` in 12, `(` in 4; lengths: 25 headwords of length 1, 7 longer than 56.

**Result:** Strong signal: character class + something structural for the remainder. The character counts overlap (a headword can carry both `,` and `’`), so a priority-ordered partition is needed, not independent tallies.

## 6. The wrapped-headword discovery (the structural cause)

**Hypothesis:** The unexplained remainder after character/length tests are headwords the base parser assembled from multiple djvu lines — invisible to a line-at-a-time census.

**Method:** Inspected the residue of the first partition attempt (111 keys with clean characters and legal lengths). Their base `head_line` fields showed the base parser's fragment-join notation (`FRAG / TAIL.`), e.g. ACTIO NON ACCREVIT INFRA SEX ANNOS split as "ACTIO NON ACCREVIT INFRA SEX" + "ANNOS." My first detector looked for the two-fragment separator ` // ` and caught only 8; the single-fragment form uses ` / ` — correcting the detector to ` / ` was the fix.

**Observation:** 161 base-only keys are wrapped headwords. Cross-checks: for 156 of 161, the census crowned the *tail fragment* as a headword under a different key (ANNOS, TATIONEM, MENT, …) — this is cause (d) in substance: one physical entry, the census's key for its tail ≠ the base's key for the whole. The 5 exceptions were individually inspected; each tail itself fails the census class (CHARGE D’AFFAIRES and QUEEN’S and KING’S HOUSEHOLD — curly apostrophe; DELIBERANDI) — parenthesis; the EST, SED ITA LEX SCRIPTA EST tail — commas). Also visible in the raw lines: one wrapped entry's first fragment is mixed-case ("CHARGE DES AFFAIRES, or") — the base fragment rule admits lowercase, the census admits none.

**Result:** Wrapped = 161, fully evidenced, no sub-residue.

## 7. Final partition of the 522 — zero residue

**Hypothesis:** Priority order (artifact → wrapped → guillemet → character class → length) partitions the 522 exactly.

**Method:** Implemented in `census_rebuild.py`: for each base-only key, test the representative entry's raw djvu line against the census patterns and the artifact guard; then the wrapped marker; then the raw line's leading `«`; then offending characters in the (uppercased, space-collapsed) base headword; then length against the census bound for the entry's form (own-line if the raw line ends at the headword period).

**Observation:** Partition: comma 182 · wrapped 161 · period 70 · curly `’` 66 · short-inline (single letter) 20 · `)` 7 · comma+`’` 5 · short-own (single letter) 5 · parens+`’` 3 · guillemet 1 · artifact 1 · comma+period 1 = **522. RESIDUE = 0** (asserted in code). Notes:
- The guillemet case is CAVEAT EMPTOR: raw line begins "« CAVEAT EMPTOR.  Let…" — the base strips the ornament, the census `^` anchor fails on it.
- The artifact case, I 1180 (djvu line 122061, raw "I 1180. "), is double-natured: mechanism (b) — the census guard rejects a line its inline pattern otherwise matches; character (e) — it is the one genuine base-parse extra found anywhere in the 522, a page-number/running-head line whose attached body is continuation text of the LIEN entry.
- Maximum-length as primary cause = 0: the 7 headwords over 56 chars are all claimed by wrapped/character first. Stated plainly rather than silently absorbed.

**Result:** The 253 is explained exactly, with the census-only side (§8) closing the arithmetic from the other direction.

## 8. The 386 census-only keys (needed for the register)

**Hypothesis:** Census-only keys are the mirror image: tails of wrapped entries, lines the base's guards refuse, and terminator-spacing cases.

**Method:** For each census-only key, took its census row line; tested (i) membership in the wrapped-tail set, (ii) preceding line blank or not, (iii) whether the line matches the base `HW` pattern with the `.\s\s` terminator relaxed to one space, and whether its body remainder then trips the base digit/`;`/`)` reject.

**Observation:** 127 are wrapped tails (§6). Of the remaining 259: 81 sit in continuation position (no preceding blank — e.g. the citation line "A C. R. Co., 26 Barb…" and the mid-entry fragment AGES); of the 178 after a blank line, 107 match the base headword pattern but their body remainder begins with a digit/`;`/`)` (base rule-3 rejects — citation-led lines), and 71 fail only the base's two-space terminator demand (single-space lines, often with a space before the period: "ABATEMENT . In pleading.…", "ABBRE VIATORS . In ecclesiastical law."). 127 + 81 + 107 + 71 = 386. ✓ No residue on this side either.

**Result:** Both directions of the symmetric difference are fully partitioned; the register reconciliation in §11 is pure set arithmetic on measured quantities.

## 9. Relaxation R-a (plural normalization) — candidate generation

**Hypothesis (to be tested, not assumed):** Some unmatched base keys differ from a 5e key only by final-token plural morphology; the task's own warning example (ACT vs ACTS as different entries) says the class is dangerous.

**Method:** For each of the 9,204 unmatched base keys, generated variants {key+`s`, key+`es`, strip `es`, strip `s`} and intersected with the 5e key set.

**Observation:** 102 candidate pairs over 100 keys, 2 keys ambiguous (two hits). The candidate list visibly mixes true number variants (BLACK ACTS → Black Act) with the trap class (B → Bes, I → Is, RES → Re, CUSTOM → Customs) — formal generation cannot tell them apart, which is precisely what the verification sample is for.

**Result:** Proceed to sample verification (§11 covers both relaxations' verification together).

## 10. Relaxation R-b (Levenshtein ≤ 1) — candidate generation

**Hypothesis:** Some unmatched base keys are one edit from a 5e key (OCR garble in the 2e djvu is the obvious source).

**Method:** Deletion-neighborhood indexing over 5e keys of length ≥ 7 (two keys at Levenshtein ≤ 1 always share a single-deletion variant — substitution pairs share the variant deleting the differing position; insertion/deletion pairs share the shorter key); candidates filtered to both keys ≥ 7 chars, same first letter, verified by an exact Levenshtein-≤1 check.

**Observation:** 263 candidate pairs over 252 keys, 10 ambiguous. Again visibly mixed: genuine OCR pairs (ABRIDGMENT OP DAMAGES → Abridgment of damages; THAVIE8 INN → Thavies inn) sit beside real distinct words (ABROGATION → Arrogation, BROTHEL → Brother, CAPTION → Caution, MARINES → Mariner).

**Result:** Proceed to verification.

## 11. Verification sampling — both relaxations FAIL the 100% gate

**Hypothesis:** If either relaxation is a clean same-lemma class, a 30-pair sample will show it; if the sample shows even one different-lemma pair, the relaxation must be dropped per the task's gate.

**Method:** Deterministic stride sample (30 pairs, evenly spaced over the sorted pair list) per relaxation. Each sampled pair judged by locating both headwords in their texts: the 2e entry body from `entries.json` (public domain) and the 5e entry in the study text (read for judgment only; reproduced nowhere). Judgment standard: same dictionary lemma = same headword word/concept, the formal difference being mere inflection (R-a) or mere OCR/transmission noise (R-b); a pair fails if the two entries carry different concepts, different senses, or the 5e side is itself OCR noise rather than a headword. Full tables with per-pair verdicts are in `reconciliation.md` §7.

**Observation:**
- **R-a: 17/30 same-lemma = 56.7%.** Failures include RES → Re, SCOTS → Scot, TALES → Tale, TESTES → Teste, MARCH → Marches, PARCEL → Parcels, INSTRUCTION → Instructions, REDEMPTIONES → Redemption, SEES → See, MONTES → Mont, B → Bes, I → Is, JES → a noise headword. Several failures are pairs where *both* forms exist as separate entries in the editions' own practice — the ACT/ACTS trap at scale.
- **R-b: 19/30 same-lemma = 63.3%.** Passes are dominated by 2e OCR garble (OP for OF, DAT for DAY, SAXE for SALE, 8 for S, PREFERENTIAX for Preferential). Failures are genuine distinct words one edit apart: CHANCEL → Chancer, COLLEGA → College, CONCESSOR → Confessor, COUNT EZ → Countee, DEFENSA → Defense, DISCOVERT → Discovery, FENERATION → Federation, IMPLEADED → Impleader, INSUPER → Insurer, MARINES → Mariner, PLEAD ED → Pleader.
- Borderline calls, recorded honestly: R-a ABSENTS → Absent judged same (the 2e entry treats the inflected form of *absent* in old reports); R-b FABRICARE → Fabricate and VINDICARE → Vindicate judged same (Latin infinitive forms of the same word); R-b RECOVERED → Recoverer judged same (the 2e body defines the demandant in a common recovery, i.e. the recoverer). Flipping all three borderline calls against the relaxations would only lower precision further; flipping them the other way changes nothing — both relaxations are far from 100% on any reading.

**Result:** Both relaxations REJECTED. Considered and deliberately not adopted: post-hoc tightened variants (e.g. R-b only where an OCR-suspect character is present). They might well pass a fresh sample, but designing the restriction after inspecting the failures is fitting the gate; they are left UNCHARTED in `reconciliation.md` for a future pre-registered pass. **Changed-form = 0 — a verified negative result, not a skipped step.**

## 12. Mapping, register, outputs

**Hypothesis:** With exact join only, coverage and the register follow by set arithmetic and must reconcile against the census's 18,098 with the §§5–8 quantities.

**Method:** `census_rebuild.py` (the shipped mechanism; re-runnable; asserts the regeneration gate, the 522 partition, zero residue, and the coverage sum) writes `census.json` (full `u5` and `u2census` norm-key → display maps), `mapping.json` (per-entry fate for all 13,145 indices), `register.json` (5e-only displays sorted by norm key).

**Observation:** Coverage: carried 3,872 / changed-form 0 / not-carried 9,273 = 13,145 ✓ (carried spans 3,824 distinct keys; the census's 3,881 "survived" counts census-parse keys — the difference is the parse divergence itself). Register: 18,155. Reconciliation vs census "new" 18,098: +57 = 104 − 47, where 104 = 5e keys witnessed in the 2e only by census-only keys, 47 = 5e keys witnessed only by base-only keys. Output sizes verified after the run: census maps 21,979 + 12,892; mapping 13,145 entries; register 18,155. A post-run cross-check confirmed the samples embedded in the script (and their verdict arrays) are byte-identical to the samples actually verified in §11.

**Result:** All six deliverables stand in `final/work-census/`: `census_rebuild.py`, `census.json`, `mapping.json`, `register.json`, `reconciliation.md`, `worker-log.md` (this file). Nothing pushed to git.

## 13. Dead ends and open items, stated plainly

- §2's line-splitting worry: investigated, closed (no divergence in the 2e text).
- Cause (c) body-range for base-only keys: investigated, measured **zero** — reported as zero, not padded.
- Cause (e) genuine extras: exactly one (I 1180), double-flagged under (b)/(e) rather than double-counted.
- The ` // ` vs ` / ` detector miss (§6) initially hid 153 of the 161 wrapped cases; caught because the first partition left an 111-key residue I refused to leave unexplained — the residue was the diagnosis.
- OPEN (UNCHARTED): a pre-registered, OCR-aware tightening of R-b could legitimately recover several hundred OCR-garble changed-form pairs (the R-b passes cluster tightly: OP/OF, DAT/DAY, digit-for-letter). It was not built here because its verification would have to be designed before looking at outcomes. The exact-join mapping ships without it, and every affected entry reads "not-carried" — conservative, and correctable by a future pass without invalidating anything in this folder.
