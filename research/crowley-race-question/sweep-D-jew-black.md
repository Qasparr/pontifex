# SWEEP D — "JEW"/"BLACK" TERMS: Anomaly Sweep Report

**Thread:** Worker D (priority thread, added by Johnathan personally)
**Sweep:** PONTIFEX coordinated anomaly sweep of Aleister Crowley's writings
**Date:** Sun 2026-10-11 (dies solis), Anno V:xii e.n.

**Epigraph:** "Every number is infinite; there is no difference." — Liber AL I:4.

93.

**Authorship:** Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
Scribed by Worker D. Findings, never doctrine. No term is declared "the breadcrumb" herein — report and score only. All rulings to the red pen.

**Scope (self-contained):** gematria values for terms meaning "Jew"/"Jews" and "black"/"Black":
Hebrew יהודי / יהודים, Greek Ἰουδαῖος, Hebrew שחור, Greek μέλας,
plus any related terms Crowley himself prints with values.

---

## PART 1 — ULTRA-VERBOSE WORK LOG

### Step 1. Corpus reconnaissance

**Hypothesis:** the corpus directory `~/workspace/pontifex/research/crowley-race-question/corpus/` would contain pre-downloaded texts to reuse.

**Method:** listed the directory.

**Observation:** the directory is empty (created Oct 11 20:51, zero files).

**Result:** dead end on reuse; all sources had to be obtained fresh. Moved to the twelve-tongues sweep's tooling instead.

---

### Step 2. Table reuse and calibration design

**Hypothesis:** the twelve-tongues sweep's attested tables (`~/workspace/pontifex/pontifex/tables.py`) could be imported rather than re-typed, eliminating table-drift as an error source.

**Method:** read `weigh_hebrew.py` and `greek_weigh.py`; confirmed both import `HEBREW`/`GREEK` from `pontifex.tables` and `weigh` from `pontifex.engine`.

**Observation:** tables are attested, single-source, and already calibrated by two prior workers.

**Result:** wrote `sweep-D-weigh.py` (in this directory, thelemic + educational format per standing order) importing the same tables. Calibration anchors per task: יופיאל=137, ראהוור=418, plus a third anchor θελημα=93 for the Greek bank.

---

### Step 3. Calibration run — first failure (uppercase Greek)

**Hypothesis:** the script would calibrate and weigh cleanly on first run.

**Method:** ran `sweep-D-weigh.py`.

**Observation:** calibration passed on all three anchors (יופיאל=137 ✓, ראהוור=418 ✓, θελημα=93 ✓). Then `KeyError: 'Ι'` — the GREEK table holds lowercase only (29 keys: α…ϡ, including ς).

**Result:** dead end taught the fix: gematria is case-insensitive, so case-fold before weighing. Fixed the script (`.lower()` before diacritic-stripping).

---

### Step 4. Calibration run — second failure (my own typo)

**Hypothesis:** fixed script runs clean.

**Method:** re-ran.

**Observation:** `KeyError: 'מ'` — I had typed a bogus TERMS row ("מֵלַס" labelled Greek; those are Hebrew letters — mem/lamed/samekh — a script-confusion typo of mine, caught by the fail-loud table lookup).

**Result:** deleted the bogus row. The fail-loud design (KeyError, not silent skip) caught my own error — logged here as evidence the mechanism works.

---

### Step 5. Clean mechanical weighings

**Hypothesis:** the five terms weigh to the hand-computed values.

**Method:** ran the fixed script.

**Observation / result — all five weighed, full breakdowns:**

| # | Term | Script form weighed | Breakdown | Value |
|---|------|--------------------|-----------|-------|
| 1 | יהודי (yehudi, "Jew") | יהודי | י=10+ה=5+ו=6+ד=4+י=10 | **35** |
| 2 | יהודים (yehudim, "Jews") | יהודים | י=10+ה=5+ו=6+ד=4+י=10+ם=40 | **75** |
| 3 | Ἰουδαῖος (Ioudaios, "Jew") | ιουδαιος (case-folded, diacritics stripped) | ι=10+ο=70+υ=400+δ=4+α=1+ι=10+ο=70+ς=200 | **765** |
| 4 | שחור (shachor, "black") | שחור | ש=300+ח=8+ו=6+ר=200 | **514** |
| 5 | μέλας (melas, "black") | μελας (case-folded, diacritics stripped) | μ=40+ε=5+λ=30+α=1+ς=200 | **276** |

**Loaded-number check:** none of {35, 75, 765, 514, 276} is in {11, 77, 93, 418, 666, 777}. No direct loaded hit. No collisions among the five.

**Near-miss noted (not a hit):** Ἰουδαῖος=765 sits 12 below 777 and 99 above 666 — recorded as arithmetic trivia, not a finding.

---

### Step 6. Obtaining Sepher Sephiroth (1912, Equinox I(8) — pre-1930, US public domain)

**Hypothesis:** a greppable transcription of Sepher Sephiroth exists on the public web.

**Method:** web search → found the-equinox.org transcription (`eqi08024.html`, from Equinox Vol I No 8, 1912) — 16,865 lines, full dictionary. Opened it.

**Observation:** the transcription renders Hebrew in ASCII transliteration (e.g. `ShChQYM`, `BVLShKYN`, `YHVDH`), with number headings right-aligned. The Preface (L22-45) contains Crowley's own polemical rhetoric about Jews — noted as context for the parent sweep (the defense-brief dossier covers it); not gematria, not my thread's quarry.

**Result:** primary printed source secured. Also secured the 777 Revised transcription (scribd, Celephaïs Press 2019 reprint of 1909/1955 material) and the Old+New Commentaries PDF (thelema.tools, 11,422 lines) in later steps.

---

### Step 7. Hunting יהודי (YHVDY) and יהודים (YHVDYM) in Sepher Sephiroth

**Hypothesis:** if Crowley printed either term, it would appear under entries 35 and 75 as `YHVDY` / `YHVDYM`.

**Method:** `browser.find` for `YHVDY`, `YHVDYM`, then the looser `YHVD` to validate the tool.

**Observation:** `YHVDY` — no match. `YHVDYM` — no match. `YHVD` — two matches only: entry 25 "Jehewid, God of Geburah — YHVD" and entry 30 "Judah — YHVDH". Entry 35 (viewed directly, L3850-3860) holds AGLA, GBL, YHK — no YHVDY. Entry 75 (L4710-4724) holds GVVNY, HYLL, YKDYAL, YLLH, KYMH, LYLH, NVYT — no YHVDYM.

**Result:** neither "Jew" term appears anywhere in Crowley's Sepher Sephiroth. Printed value for both: **none — absent**. (Related root forms YHVD/YHVDH logged below.)

---

### Step 8. Hunting שחור (ShChVR) in Sepher Sephiroth

**Hypothesis:** שחור would appear under entry 514 as `ShChVR`.

**Method:** `browser.find` for `ShChVR` (validated the tool first with known-present `ShChQYM`).

**Observation:** no match. Viewed entry 514 directly (L9812-9816): it holds only `ChQVTh` ("[Vide K.D. L.C.K. p. 213]").

**Result:** שחור is absent from Sepher Sephiroth. Printed value: **none — absent**. Neighbor at 508, however, is `ShChR` ("Daybreak; black") — logged as the near-miss pair (Step 10).

---

### Step 9. Sweeping all "black"-glossed entries in Sepher Sephiroth

**Hypothesis:** the English gloss "black" would surface every Crowley-printed black-term.

**Method:** `browser.find` for `black` across the full Sepher Sephiroth page.

**Observation — five "black" entries plus two darkness-adjacent:**
- Entry 19: "Was black — DYH"
- Entry 20: "Black liquid — DYV"
- Entry 48: "To grow warm; heat, fire; black; Ham, the son of Noah — ChM"
- Entry 367: "Black [scil. of eye-pupil]: …middle: homunculus — AYShVN"
- Entry 508: "Daybreak; black — ShChR"
- Entry 88: "Darkness — ChSK" (spelling ambiguity — Step 11)
- Entry 380: "Thick darkness, fog — a'aRPL"

**Result:** all recomputed mechanically (Step 12) — every printed value verifies exactly. Zero discrepancies.

---

### Step 10. The ShChR/ShChVR near-miss pair

**Hypothesis:** entry 508's `ShChR` might be a variant spelling of שחור.

**Method:** recomputed both; compared letter-by-letter.

**Observation:** שחר (ShChR, "dawn/daybreak") = 300+8+200 = **508** ✓ (printed at 508, correct). שחור (ShChVR, "black") = 300+8+6+200 = **514** (absent from the book). They differ by exactly one letter — the vav (6). Crowley glosses ShChR "Daybreak; black" — the "black" gloss is his (dawn's darkness), not a misvaluation.

**Result:** not a discrepancy — a genuine near-collision (Δ=6, one vav), honestly reported. Yophiel score: (a)✗ no printed-vs-true mismatch; (b) n/a; (c) n/a; (d)✗. Score **zero** — and that is the finding.

---

### Step 11. The ChSK "Darkness" ambiguity at entry 88

**Hypothesis:** "Darkness — ChSK" at 88 might be a misvalued חשך.

**Method:** recomputed both readings: חסך (samekh) = 8+60+20 = **88** ✓; חשך (shin, the actual word for "darkness") = 8+300+20 = **328** ✗.

**Observation:** as printed (samekh), the value is correct but the gloss doesn't fit חסך ("to withhold, restrain"). As the darkness-word (shin), the gloss fits but the value is wrong by 240. Checked the Ian Rons revised transcription (archive.org djvu.txt) — its OCR is too garbled to resolve shin vs samekh.

**Result:** **unresolved.** One-letter S/Sh ambiguity; needs the 1912 Equinox I(8) print to settle whether Crowley (or the transcriber WEH) dropped the 'h'. Yophiel: (a)? conditional, (b) true 328 not loaded / deviant 88 not loaded, (c) transcription uncertainty = cover, (d)✗. Flagged, not scored as anomaly.

---

### Step 12. Mechanical verification of every Crowley-printed related term

**Hypothesis:** any printed value in the sweep's net might deviate.

**Method:** recomputed each via the attested table (script, Step 5 run + direct checks).

**Observation / result:**

| Printed entry | Crowley's value | Recomputed | Discrepancy? |
|---|---|---|---|
| DYH "Was black" | 19 | 19 ✓ | none |
| DYV "Black liquid" | 20 | 20 ✓ | none |
| ChM "…black; Ham" | 48 | 48 ✓ | none |
| AYShVN "Black [of eye-pupil]" | 367 | 367 ✓ | none |
| ShChR "Daybreak; black" | 508 | 508 ✓ | none |
| a'aRPL "Thick darkness, fog" | 380 | 380 ✓ | none |
| YHVD "Jehewid, God of Geburah" | 25 | 25 ✓ | none |
| YHVDH "Judah" | 30 | 30 ✓ | none |

**Result:** eight for eight — every Crowley-printed value in the net recomputes exactly.

---

### Step 13. The Old Comment on AL I,46 — the AVN/AYN discrepancy (the one real flag)

**Hypothesis:** the commentaries might print a value for a Jew-term.

**Method:** searched the Old+New Commentaries PDF for "Jew"; found AL I,46: "Sixty-one the Jews call it; I call it eight, eighty, four hundred & eighteen." Read the Old Comment on I,46-47 in full.

**Observation:** the restored Old Comment prints: "46. 61 = {Aleph-Vau-Nun}." Recomputed: און (Aleph-Vau-Nun) = 1+6+50 = **57**, not 61. The word that actually equals 61 is אין (Aleph-**Yod**-Nun) = 1+10+50 = **61** — "Nothing", which is precisely Crowley's own Sepher Sephiroth entry 61 ("The Negative, non-existent; not — AYN", verified at L4450-4452), and אדון at 61 too.

**The cover:** the edition's own header states curly-bracketed Hebrew is *editorial interpolation* of typescript gaps ("intended to be filled by handwritten symbols… The accuracy of these interpolations is very high, but not certain"). So the deviant letters are the modern editor's guess, not necessarily Crowley's hand. ו/י are the classic confusable pair in handwritten Hebrew.

**Cross-check of the surrounding equations** (all verify): Cheth spelt fully חית = 418 ✓; 8+80+418 = 506 ✓; 506+61 = 567 ✓; 605+61 = 666 ✓; 30+61 = 91 = אמן (Amen) ✓.

**Result:** the single strongest finding of the thread (see scoring below). Attribution: most likely a modern interpolation slip, **not** Crowley's — the brackets say so.

---

### Step 14. 777 columns check ("Jews", "Judah")

**Hypothesis:** 777's correspondence columns might attach a number to "Jew".

**Method:** searched the 777 Revised transcription for "Jew", "Iudaeus", "melas", "Ioudaios".

**Observation:**
- `Iudaeus`/`Ioudaios`/`melas` — no matches anywhere in 777.
- "Jew" — one substantive hit: the added Hells column (Qliphoth row 7, "Dispersing Ravens … Hutamah **Jews** Jannat al-Naim") — an *attribution* (which group a hell punishes), **no value attached**.
- 777 col. CXXXIX ("The Twelve Tribes"): "Judah" at path 19 (Leo) — a correspondence, **no value attached**. (Hebrew יהודה = 30, correctly printed at Sepher Sephiroth 30.)

**Result:** no Crowley-printed gematria value for any Jew/black term in the 777 columns.

---

### Step 15. Greek terms — Crowley-printed values?

**Hypothesis:** Crowley might have printed Ἰουδαῖος or μέλας with values somewhere.

**Method:** searched 777 Revised (no Greek dictionary present — only a "Some Greek Gods" correspondence column) and Sepher Sephiroth (Hebrew-only by design).

**Observation:** no Greek word-value table exists in Crowley's printed works. His "Greek Qabalah" (Liber MCCCLXV) was never published (unpublished papers only).

**Result:** printed values for both Greek terms: **none — no such table exists in print**. Collision notes: μέλας=276 collides cross-language with Sepher Sephiroth 276 entries (KNVR, KRVKL, SYHRA — all verify; AChVBRAYN there is flagged "Wrong value, 278" by the transcriber WEH, outside this thread's scope, noted for completeness). Ἰουδαῖος=765: Sepher Sephiroth slot 765 is **empty** — no collision at all.

---

### Step 16. Loaded-number and collision sweep

**Hypothesis:** some computed or printed value might land loaded or collide suggestively.

**Method:** tested all values against {11, 77, 93, 418, 666, 777}; inspected the Sepher Sephiroth slots at 35, 75, 276, 514, 765.

**Observation:**
- 35 → slot holds AGLA, GBL, YHK. Not loaded.
- 75 → slot holds GVVNY, HYLL, YKDYAL, YLLH, KYMH, LYLH ("Night; by night"), NVYT ("NUIT, THE STAR GODDESS"). Not loaded. (LYLH is darkness-adjacent — neighbor note only.)
- 276 → slot populated, all verify (see Step 15).
- 514 → slot holds only ChQVTh. Not loaded.
- 765 → slot empty. Not loaded.
- The verse's own 61-complex: 61 not in the loaded set; the Old Comment's 605+61=666 equation is Crowley's own arithmetic and verifies.

**Result:** no loaded-number hit, no suggestive collision anywhere in the thread.

---

### Dead ends logged
- Empty corpus dir (Step 1) → built on twelve-tongues tooling instead.
- vcjones.co.uk "PDF" — SEO spam page, not the text (abandoned).
- archive.org "Collected PDFs" Rons revision — OCR too garbled to resolve ChSK shin/samekh (Step 11 unresolved).
- scribd "Greek Sepher Sephiroth" — modern compilation, not Crowley-printed (noted as coverage limit, not used).
- 777 Revised search for melas/Ioudaios/Iudaeus — all absent.

---

## PART 2 — PER-TERM LEDGER

### Term 1 — יהודי (yehudi, "Jew", m. sg.)
- **Mechanical value:** 35 (י=10+ה=5+ו=6+ד=4+י=10). Tier: ATTESTED (native term, attested table).
- **Crowley's printed value:** none found — absent from Sepher Sephiroth (entry 35 holds AGLA, GBL, YHK only); absent from 777 columns; absent from commentaries as a weighed term.
- **Variants across his works:** YHVD ("Jehewid, God of Geburah", Sepher Sephiroth 25, verifies); YHVDH ("Judah", Sepher Sephiroth 30, verifies; also 777 col. CXXXIX tribe at path 19, no value); "Jews" in 777 Revised Hells column (attribution only, no value); AL I,46 "Sixty-one the Jews call it" (61 is the number of *Nothing*, not of "Jew").
- **Loaded/collision:** 35 not loaded; slot 35 has no suggestive neighbor.
- **Yophiel score:** (a)✗ (b)✗ (c)✗ (d)✗ → **0. Clean absence; that is the finding.**

### Term 2 — יהודים (yehudim, "Jews", m. pl.)
- **Mechanical value:** 75 (…+ם=40). Tier: ATTESTED.
- **Crowley's printed value:** none found — absent from Sepher Sephiroth (entry 75 holds GVVNY, HYLL, YKDYAL, YLLH, KYMH, LYLH, NVYT).
- **Variants:** as Term 1.
- **Loaded/collision:** 75 not loaded. Neighbor note: LYLH ("Night; by night") and NVYT ("NUIT, THE STAR GODDESS") share slot 75 — darkness-adjacent, no collision (term absent).
- **Yophiel score:** **0. Clean absence.**

### Term 3 — Ἰουδαῖος (Ioudaios, "Jew", Greek)
- **Mechanical value:** 765 (ι=10+ο=70+υ=400+δ=4+α=1+ι=10+ο=70+ς=200; case-folded, diacritics stripped — gematria never weighs accents). Tier: ATTESTED (authentic Greek word-form, attested Milesian table).
- **Crowley's printed value:** none found — Crowley never published a Greek word-value table (Liber MCCCLXV, "The Greek Qabalah", remains unpublished papers).
- **Variants:** none in his printed works ("Iudaeus"/"Ioudaios"/"Judaios" all absent from 777).
- **Loaded/collision:** 765 not loaded (12 below 777; 99 above 666 — arithmetic trivia only). Sepher Sephiroth slot 765 is empty — zero collision.
- **Yophiel score:** **0. No printed rival exists to disagree with.**

### Term 4 — שחור (shachor, "black", Hebrew)
- **Mechanical value:** 514 (ש=300+ח=8+ו=6+ר=200). Tier: ATTESTED.
- **Crowley's printed value:** none found — absent from Sepher Sephiroth (entry 514 holds only ChQVTh).
- **Variants / related printed terms (all recomputed, all verify):** ShChR ("Daybreak; black", 508 ✓ — one vav away, the near-miss pair); DYH ("Was black", 19 ✓); DYV ("Black liquid", 20 ✓); ChM ("…black; Ham, the son of Noah", 48 ✓); AYShVN ("Black [of eye-pupil]", 367 ✓); a'aRPL ("Thick darkness, fog", 380 ✓); ChSK ("Darkness", 88 — spelling ambiguous, see below).
- **Loaded/collision:** 514 not loaded; slot 514 = ChQVTh only.
- **Yophiel score:** **0 for the term itself.** The ChSK "Darkness" gloss/spelling ambiguity (חסך=88 valued-right/glossed-wrong vs חשך=328 glossed-right/valued-wrong) is flagged **unresolved** — needs the 1912 print; (a)? conditional, (b) neither 88 nor 328 loaded, (c) transcription uncertainty, (d)✗. Not scored as anomaly.

### Term 5 — μέλας (melas, "black", Greek)
- **Mechanical value:** 276 (μ=40+ε=5+λ=30+α=1+ς=200). Tier: ATTESTED.
- **Crowley's printed value:** none found — no Greek value-table in print.
- **Variants:** none ("melas" absent from 777 Revised).
- **Loaded/collision:** 276 not loaded. Cross-language coincidence only: Sepher Sephiroth 276 holds KNVR, KRVKL, SYHRA (all verify) — Crowley never weighed μέλας, so no anomaly. (Transcriber WEH flags AChVBRAYN at 276 as "Wrong value, 278" — outside this thread, noted for the parent.)
- **Yophiel score:** **0. No printed rival exists.**

### Related printed item — AL I,46 "Sixty-one the Jews call it" (Old Comment)
- **Verse:** "Nothing is a secret key of this law. Sixty-one the Jews call it; I call it eight, eighty, four hundred & eighteen." (Liber AL, Class A.)
- **Old Comment (restored text) prints:** "46. 61 = {Aleph-Vau-Nun}."
- **Recomputed:** און = 57 ≠ 61. True reading: אין (Aleph-Yod-Nun) = 61 = "Nothing" — confirmed as Crowley's own Sepher Sephiroth 61 entry ("The Negative, non-existent; not — AYN").
- **Surrounding equations all verify:** חית (Cheth full) = 418 ✓; 8+80+418 = 506 ✓; 506+61 = 567 ✓; 605+61 = 666 ✓; 30+61 = 91 = אמן ✓.
- **Yophiel score:** (a)✓ one-letter V/Y discrepancy, printed 57 vs claimed 61; (b)✓ both sides independently meaningful (AYN=61 his Sepher Sephiroth 61; AVN=57 his Sepher Sephiroth 57 "Wealth, an age, Time; Night"); (c)✓ strong cover — curly brackets mark it as *modern editorial interpolation* of a typescript gap per the edition's own header, and ו/י is the classic handwritten confusable pair; (d)✗ no motive — deviant 57 is not loaded, true 61 is the verse's own number. **Verdict: flagged transcription anomaly, almost certainly the modern interpolator's slip, not Crowley's — NOT a breadcrumb.**

---

## Summary of findings (never doctrine)

1. **All five assigned terms weigh cleanly** (35, 75, 765, 514, 276); none hits a loaded number; none collides suggestively.
2. **Crowley printed no value for any of the five terms.** יהודי and יהודים are absent from Sepher Sephiroth; שחור is absent (nearest neighbor: ShChR "Daybreak; black" at 508, one vav away — honest near-miss, score zero); no Greek value-table exists in his printed works.
3. **Every Crowley-printed related term recomputes exactly** (8/8): DYH=19, DYV=20, ChM=48, AYShVN=367, ShChR=508, a'aRPL=380, YHVD=25, YHVDH=30.
4. **One real flag:** the restored Old Comment's "61 = {Aleph-Vau-Nun}" (AL I,46, "Sixty-one the Jews call it") — AVN = 57, one letter off the true אין = 61, which is Crowley's own Sepher Sephiroth 61. The brackets mark it as modern editorial interpolation, so this is most likely the *interpolator's* ו/י slip, not Crowley's. Reported, scored (a✓b✓c✓d✗), not a breadcrumb.
5. **One unresolved:** "Darkness — ChSK" at Sepher Sephiroth 88 (samekh=88 valued-right/glossed-wrong vs shin חשך=328 glossed-right/valued-wrong) — needs the 1912 print.

**Coverage limits:** (i) 1912 Equinox I(7) print of the Old Comment not consulted — would settle whether the AVN interpolation exists in Crowley's lifetime print; (ii) 1912 Equinox I(8) print not consulted — would settle ChSK shin/samekh; (iii) New Comment (1936) checked via modern restoration text, brief quotes only, no values found; (iv) Liber MCCCLXV Greek Qabalah unpublished — not in scope for "Crowley-printed".

---
*Scribe: Worker D. 93. "Live, Love, and let Love, Live."*
*All Rights Reserved, Without Prejudice.*
