# Reconciliation — Census Regeneration vs. the Shipped Base Parse
Worker A (census regeneration + reconciliation), final Black's Teacher's Edition build.
All counts below are produced by `census_rebuild.py` in this folder and are re-derivable by running it.
Copyright boundary honored throughout: headwords and status metadata only; no 5th-edition entry text appears anywhere in this folder's outputs.

## 1. Regeneration check — MATCH

The census engine (`5e/analyze.py`) was re-run with its parsing logic copied exactly — same regexes, same line ranges, same `norm()` join key (lowercase alphanumeric), same longest-kept dedup — instrumented only to record each kept row's line number.

| Quantity | Published (`analytics.json`) | Regenerated | Match |
|---|---|---|---|
| 5e entry rows | 26,420 (14,595 inline + 11,825 own-line) | 26,420 (14,595 + 11,825) | ✓ |
| 5e unique headwords | 21,979 | 21,979 | ✓ |
| Census-2e entry rows | 13,078 (13,078 inline + 0 own-line) | 13,078 (13,078 + 0) | ✓ |
| Census-2e unique headwords | 12,892 | 12,892 | ✓ |
| Survived (census-2e ∩ 5e) | 3,881 | 3,881 | ✓ |
| Lost (census-2e − 5e) | 9,011 | 9,011 | ✓ |
| New (5e − census-2e) | 18,098 | 18,098 | ✓ |

Line ranges as regenerated: 5e body at splitlines indices 1221–210281; census-2e body at indices 546–206775 (1-indexed lines 547–206775). The regeneration gate in `census_rebuild.py` asserts every figure above and halts on any mismatch; it passed, so the reconciliation below proceeds on verified data.

## 2. The 253 gap — exact decomposition

Measured sets (join key = `norm()` for both parses):

- |base entries| (`2e/entries.json`) = **13,145**
- Distinct norm keys among base entries = **13,028**
- |census-2e keys| = **12,892**
- |base_keys ∩ census_keys| = **12,506**
- |base_keys − census_keys| = **522**
- |census_keys − base_keys| = **386**

Arithmetic: 13,145 − 12,892 = **253 = 117 + 522 − 386**, where:

1. **117 duplicate-key collapses inside the base parse.** The base parser kept 13,145 entries but only 13,028 distinct norm keys: 91 distinct keys carry the 117 extra entries. These are genuine separate printed entries that normalize identically — spelling variants and repeated letter/unit entries. Examples: `L` crowned 5 times (djvu lines 4085, 89928, 116063, 116079, 176641); `A. D` (line 576) and `AD` (line 5329) → same key `ad`; `A. S` / `AS`; `A RETRO` / `ARETRO`; `ABATOR` twice; `ACTUS` twice.
2. **522 base-only keys** — base headwords the census parser never produced. Fully categorized in §3; residue zero.
3. **386 census-only keys** — census headwords the base parser never produced. Sub-partitioned in §4 (needed for the register reconciliation in §6).

## 3. The 522 base-only keys — why the census parser missed each

Method: for each base-only key, the representative base entry's raw djvu line was tested against the census patterns (`HEAD2_INLINE`, `HEAD2_OWN`, `PAGE_ARTIFACT`) and both parsers' rules. Causes are assigned by the first matching test in the priority order below; a key is counted once. (Overlaps exist — e.g. most wrapped headwords would also fail on characters or length — and are noted where they matter.)

| # | Cause | Count | Mechanism (census rule vs. base rule) |
|---|---|---|---|
| a1 | Comma in headword | 182 | Census class `[A-Z0-9&'\- ]` excludes `,`; the base class admits it (inverted titles). Examples: ACCESSION, DEED OF · ACCRUER, CLAUSE OF · ACTON BURNED, STATUTE OF · AN, JOUR, ET WASTE · AD VIS ARE, ADVI8ARI |
| d | Wrapped (multi-line) headword | 161 | The printed headword wraps across 2–3 djvu lines; the base parser joins the fragments, the census — line-at-a-time — cannot. Examples: ABBROCHMENT, OR ABBROACHMENT · ACCOUNTANT GENERAL, OR ACCOMPTANT GENERAL · ACTIO NON ACCREVIT INFRA SEX ANNOS · AD AUDIENDUM ET TER MIN ANDUM · AD LUCRANDUM VEL PERDENDUM. Cross-check: for 156 of 161, the census crowned the tail fragment as a headword of its own under a different key (e.g. tail ANNOS, TATIONEM); the 5 exceptions' tails themselves carry census-forbidden characters (CHARGE D’AFFAIRES, DELIBERANDI), KING’S HOUSEHOLD, QUEEN’S, and the comma-bearing EST, SED ITA LEX SCRIPTA EST tail) |
| a2 | Period in headword (dotted initialisms) | 70 | Census class excludes `.`; base admits dotted single-letter prefixes whole. Examples: B. B · B. C · B. D · B. E · B. F |
| a3 | Curly apostrophe (U+2019) | 66 | Census admits the straight `'` only; base admits `’` as well. Examples: ARCHBEACON’S COURT · AT ARM’S LENGTH · ATTAINT D’UNE CAUSE · BANKER’S NOTE · BARNARD’S INN |
| a4 | Single-letter headword, inline form | 20 | Census inline group requires ≥2 characters total; a one-letter head followed immediately by `.` cannot match. Examples: A · B · C · D · E (the letter entries, e.g. the line "A.  Lat.…") |
| a5 | Closing parenthesis in headword | 7 | `)` is in the base class, not the census class (OCR paren debris in the headword). Examples: AHTEH) · ANNONA) CIVIXES · AS AGAINST) AS BETWEEN · BOUGHT AND SOU) NOTES · CONSTITUT’D) |
| a6 | Comma + curly apostrophe | 5 | Examples: CHAMBER, WIDOW’S · COMPASS, THE MARINER’S · MESSAGE, PRESIDENT’S · SHELLET’S CASE, RULE IN · WILD’S CASE, RULE IN |
| a7 | Single-letter headword, own-line form | 5 | Census own-line group requires ≥3 characters total. Examples: K · O · R · U · V |
| a8 | Parentheses + curly apostrophe | 3 | Examples: CAMPBELL’S (LORD) ACTS · DENMAN’S (LORD) ACT · LYNDHURST’S (LORD) ACT |
| b | Page-artifact guard | 1 | I 1180 — the raw line "I 1180. " *does* match the census inline pattern, but the census `PAGE_ARTIFACT` guard (`^[A-Z] \d{2,}\.?$`) rejects it. See also (e) below |
| a9 | Guillemet ornament | 1 | CAVEAT EMPTOR — the raw djvu line begins with the stray ornament "« ", which defeats the census `^` anchor; the base parser strips it |
| a10 | Comma + period | 1 | X. E, X |
| | **Total** | **522** | **Residue unexplained: 0** |

Findings on the candidate causes as posed:

- **(a) Regex character class / length limits — CONFIRMED, 361 keys** (a1+a2+a3+a5+a6+a8+a10 = 335 by character class; a4+a7 = 25 by minimum length; a9 = 1 by the anchor/ornament interaction). Maximum-length failures as a *primary* cause: **0** — the 7 base-only headwords longer than the census inline maximum (56 chars) are all claimed earlier by the wrapped or character classes under the priority order.
- **(b) Page-artifact guard — CONFIRMED, exactly 1 key** (I 1180).
- **(c) Different body line ranges — 0 keys.** Every base-only entry sits at djvu lines 555–206644, strictly inside the census range 547–206775. The range asymmetry runs the other way (the census window is wider at both ends than the base parser's) and shows up on the census-only side instead.
- **(d) Dedup / norm divergence — CONFIRMED in substance as the wrapped class (161 keys).** No case exists of the census parsing the *same first line* to a different key (checked directly: 0 census rows sit at any base-only entry's first line). The divergence is structural: one physical entry, two parses — the base joins the wrapped fragments into one key; the census crowns the tail fragment under a different key or nothing at all.
- **(e) Genuine base-parse extras — exactly 1, the same I 1180.** It is counted under (b) by mechanism, but in character it is a base false positive: a printed page number stranded with a running head, crowned as an entry whose body is in fact continuation text of the LIEN entry. No other base-only key is a non-headword.

## 4. The 386 census-only keys — sub-partition (for §6)

| Cause | Count | Mechanism |
|---|---|---|
| Wrapped-headword tail fragments | 127 | Distinct census keys that are the tail lines of base wrapped entries (§3, cause d) |
| Continuation-position lines | 81 | Census crowns headword-shaped lines with no preceding blank line (citation lines and mid-entry fragments); the base parser's paragraph guard (entry starts require a preceding blank) rejects them. Sampled examples: "A C. R. Co., …" citation lines; the fragment AGES |
| Digit-body rejects | 107 | Lines matching the base headword pattern whose body remainder begins with a digit/`;`/`)` — refused by the base parser's rule 3 as citation continuations; the census has no such reject |
| Terminator spacing | 71 | Headword lines the base parser refuses because it demands `.\s\s` (period + two spaces) while these lines carry a single space (frequently with a space before the period, e.g. "ABATEMENT . In pleading.…") |
| **Total** | **386** | |

## 5. The mapping layer and the two relaxations — both REJECTED on verification

Exact join first: a base entry is **carried** iff its norm key ∈ the 5e key set. That carries **3,872 entries** over 3,824 distinct keys (the census's "survived" 3,881 is a census-parse key count, not a base-entry count — the difference is the same parse divergence decomposed in §§3–4).

The remaining 9,273 entries (9,204 distinct keys) were tested against the two stated relaxations, in order. Candidate generation: R-a (trailing plural normalization on the final token: add/strip `s`, `es` at the key's end) produced **102 candidate pairs** over 100 keys (2 ambiguous); R-b (Levenshtein ≤ 1, both keys length ≥ 7, same first letter; found by deletion-neighborhood indexing) produced **263 candidate pairs** over 252 keys (10 ambiguous).

Verification protocol: a deterministic stride sample of 30 pairs per relaxation; each pair judged same-lemma by locating both headwords in their texts and comparing definitional scope (2e bodies from `entries.json`; 5e entries read in the study text and nowhere reproduced). **Gate: a relaxation is applied only at 100% sample precision.**

- **R-a precision: 17/30 = 56.7% — REJECTED.** The failures are exactly the trap class: distinct entries one `s` apart. B → Bes, I → Is, RES → Re, SCOTS → Scot, TALES → Tale, TESTES → Teste, MARCH → Marches, PARCEL → Parcels, INSTRUCTION → Instructions, REDEMPTIONES → Redemption, SEES → See, MONTES → Mont, JES → an OCR-noise 5e headword. (The 17 passes are true number variants: BLACK ACTS → Black Act, FAGGOT VOTES → Faggot vote, IMPOSSIBLE CONTRACTS → Impossible contract, etc.)
- **R-b precision: 19/30 = 63.3% — REJECTED.** Its passes are overwhelmingly 2e OCR garble resolving to the same lemma (OP→OF, DAT→DAY, SAXE→SALE, 8→S, THAVIE8 → Thavies), but its failures are real distinct words at distance 1: CHANCEL → Chancer, COLLEGA → College, CONCESSOR → Confessor, COUNT EZ → Countee, DEFENSA → Defense, DISCOVERT → Discovery, FENERATION → Federation, IMPLEADED → Impleader, INSUPER → Insurer, MARINES → Mariner, PLEAD ED → Pleader. No purely formal relaxation separates the two populations — only reading the definitions does, which is what the 100% gate exists to prevent faking.

Post-hoc tightened variants (e.g. R-b restricted to pairs containing OCR-suspect characters) were considered and **not** adopted: tuning a relaxation after seeing its failures is fitting the gate, not passing it. They are noted here as UNCHARTED — available for a future pass with a fresh, pre-registered verification sample.

**Consequence: changed-form = 0, by verified decision.** `mapping.json` therefore uses only `via: "exact"` or `null`. Full sample tables with per-pair verdicts follow in §7.

## 6. Final coverage and the new-headword register

Coverage over all 13,145 base entries (must sum to 13,145 — it does):

| Fate | Entries |
|---|---|
| carried | 3,872 |
| changed-form | 0 (both relaxations rejected at the verification gate, §5) |
| not carried | 9,273 |
| **Total** | **13,145** |

Register (`register.json`): 5e display headwords whose keys are matched by no base entry, sorted by norm key — **18,155**.

Reconciliation against the census's 18,098 "new": 18,155 − 18,098 = **+57 = 104 − 47**, where

- **104** 5e keys are witnessed in the 2e *only* by census-only keys (§4): the census does not call them new, but the base parse — the book's actual entries — does not witness them, so the register does.
- **47** 5e keys are witnessed in the 2e *only* by base-only keys (§3): the census calls them new, but the base parse does witness them, so the register does not.

## 7. Verification samples (headwords only; ✓ = same lemma, ✗ = different entries)

Tables appended by script from the recorded verdicts — see below.

### R-a sample (30 of 102 pairs) — precision 17/30 = 56.7% → REJECTED

| # | 2e (base) headword | 5e candidate | Verdict |
|---|---|---|---|
| 1 | ABSENTS | Absent | ✓ same lemma |
| 2 | ADVOCATE'S | Advocate | ✓ same lemma |
| 3 | B | Bes | ✗ different entries |
| 4 | BLACK ACTS | Black Act | ✓ same lemma |
| 5 | CHARTS | Chart | ✓ same lemma |
| 6 | COURT OF SESSION | Court of Sessions | ✓ same lemma |
| 7 | DEGRADATIONS | Degradation | ✓ same lemma |
| 8 | EXEMPLIFICATIONS | Exemplification | ✓ same lemma |
| 9 | FAGGOT VOTES | Faggot vote | ✓ same lemma |
| 10 | FORTUNE-TELLERS | Fortune teller | ✓ same lemma |
| 11 | I | Is | ✗ different entries |
| 12 | IMPOSSIBLE CONTRACTS | Impossible contract | ✓ same lemma |
| 13 | INHERENT POWER | Inherent powers | ✓ same lemma |
| 14 | INSTRUCTION | Instructions | ✗ different entries |
| 15 | JES | J -' | ✗ different entries |
| 16 | LEODES | Leod | ✓ same lemma |
| 17 | MAGISTRATE’S COURT | Magistrate's courts | ✓ same lemma |
| 18 | MARCH | Marches | ✗ different entries |
| 19 | MONTES | Mont | ✗ different entries |
| 20 | PARCEL | Parcels | ✗ different entries |
| 21 | PAYMASTER | Paymasters | ✓ same lemma |
| 22 | PREFERENCE SHARES | Preference share | ✓ same lemma |
| 23 | PRETEXTS | Pretext | ✓ same lemma |
| 24 | PROCURATIONS | Procuration | ✓ same lemma |
| 25 | REDEMPTIONES | Redemption | ✗ different entries |
| 26 | RES | Re | ✗ different entries |
| 27 | SCOTS | Scot | ✗ different entries |
| 28 | SEES | See | ✗ different entries |
| 29 | TALES | Tale | ✗ different entries |
| 30 | TESTES | Teste | ✗ different entries |

### R-b sample (30 of 263 pairs) — precision 19/30 = 63.3% → REJECTED

| # | 2e (base) headword | 5e candidate | Verdict |
|---|---|---|---|
| 1 | ABRIDGMENT OP DAMAGES | Abridgment of damages | ✓ same lemma |
| 2 | AFFIRMANCE DAT GENERAL | Affirmance day general | ✓ same lemma |
| 3 | BARGAIN AND SAXE | Bargain and sale | ✓ same lemma |
| 4 | CARD CAT A | Carucata | ✓ same lemma |
| 5 | CHANCEL | Chancer | ✗ different entries |
| 6 | COLLEGA | College | ✗ different entries |
| 7 | CONCESSOR | Confessor | ✗ different entries |
| 8 | COUNT EZ | Countee | ✗ different entries |
| 9 | DEFENSA | Defense | ✗ different entries |
| 10 | DISCOVERT | Discovery | ✗ different entries |
| 11 | ENTENPMENT | Entendment | ✓ same lemma |
| 12 | FABRIC ARE | Fabricate | ✓ same lemma |
| 13 | FENERATION | Federation | ✗ different entries |
| 14 | FORINSIC | Forensic | ✓ same lemma |
| 15 | HEADING ACT | Healing act | ✓ same lemma |
| 16 | IMPLEADED | Impleader | ✗ different entries |
| 17 | INSUPER | Insurer | ✗ different entries |
| 18 | LEAPING A USE | LeadIng a use | ✓ same lemma |
| 19 | MARINES | Mariner | ✗ different entries |
| 20 | NEGATION | Necation | ✓ same lemma |
| 21 | ON ACCOUNT OF WHOM IT MAT CONCERN | On account of whom It may concern | ✓ same lemma |
| 22 | PLEAD ED | Pleader | ✗ different entries |
| 23 | PREFERENTIAX ASSIGNMENT | Preferential assignment | ✓ same lemma |
| 24 | PRODUCTION OP SUIT | Production of suit | ✓ same lemma |
| 25 | RECOVERED | Recoverer | ✓ same lemma |
| 26 | RETREAT TO THE WALL | Retreat to tbe wall | ✓ same lemma |
| 27 | SOLAR DAT | Solar day | ✓ same lemma |
| 28 | THAVIE8 INN | Thavies inn | ✓ same lemma |
| 29 | TROT WEIGHT | Troy weight | ✓ same lemma |
| 30 | VINDICARE | Vindicate | ✓ same lemma |
