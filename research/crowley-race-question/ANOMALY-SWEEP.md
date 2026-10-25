# ANOMALY SWEEP — Crowley's Corpus
## Systematic hunt for textual anomalies of the blind/breadcrumb class

*Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n.*

*93.*

*Coordinated sweep, four workers (A: spelling variants · B: gematria recomputation ·
C: self-flagged anomalies · D: "Jew"/"black" priority thread), synthesized by the coordinator.
Findings, never doctrine. No anomaly is declared "the breadcrumb" — reported and scored only.
Nothing pushed to git.*

---

## 0. THE TWO MODELS

**YOPHIEL MODEL** — a small exact numerical discrepancy in Crowley's own tables
(the historical case: printed 136 vs יופיאל=137). Markers: (a) small exact discrepancy,
(b) the true/deviant value independently meaningful, (c) cover pairing, (d) motive
("he was forbidden," oath-bound silence).

**KHUT/KHUIT MODEL** (verified 2026-10-11) — Liber AL manuscript reads "Ra-Hoor-Khut"
(III:35); commentaries use "Ra-Hoor-Khuit"; Crowley himself addressed it: "doubt arising
in the mind of the prophet as to the unusual spelling... the 'I' makes a difference in
the qabalistic interpretation of the name." I.e., an author-flagged spelling anomaly
with stated qabalistic significance.

---

## 1. WORK LOGS (per worker, condensed)

Full ultra-verbose logs live in each worker's file; what follows is the condensed
hypothesis → method → observation → result per worker, dead ends included.

### Worker A — spelling-variant hunt → `sweep-A-spellings.md`
- **Hypothesis:** the divine names are orthographically unstable; a regex sweep will surface
  the full Ra-Hoor family, sibling anomalies, and Crowley's own remarks on spellings.
- **Method:** built `corpus/extract_variants.py` (case-insensitive regex per name-family),
  ran it across 16 corpus files in three passes as co-workers added texts; every hit
  hand-verified with context reads to separate OCR artifacts from genuine variants.
- **Observation:** 30+ distinct variants across 11 name-families; the Ra-Hoor anomaly is a
  FIVE-way family inside Liber AL itself; Aiwass/Aiwaz is author-staged with numbers;
  Nuith/Hadith are authorial 1929 spellings later normalized by editors.
- **Result:** variant ledger (Part 2 of worker file) + reproducible `variants_raw.json`.
- **Dead ends:** hermetic.com 403 (proxy and browser); sacred-texts.com timeout;
  bibliotecapleyades.net 404; archive.org `/download/` 500s (worked around via direct
  server); Equinox I(7) scan not found (Old Comment via secondary transcription);
  *The Law is for All* download failed (172 bytes); Liber XXXI facsimile not obtained;
  Hebrew-letter verification blocked everywhere by OCR mangling; *The Book of Thoth*
  (1944) excluded as in-copyright.

### Worker B — gematria recomputation → `sweep-B-gematria.md`
- **Hypothesis:** mechanically recomputing Crowley's "X = N" equations will surface
  Yophiel-class mismatches; most will resolve as transcription noise or stated conventions.
- **Method:** imported the twelve-tongues sweep's attested tables (drift-proof);
  calibrated on יופיאל→137 and ראהוור→418; swept 2,538 weighable Sepher Sephiroth words
  via `work/sweep_b.py`; extracted commentary equations by regex; **scan-verified every
  significant mismatch against 1912 page images** via archive.org JP2 routes.
- **Observation:** 23 raw hits (0.9%); scan-verification overturned 2 of 3 small-diff cases;
  20 resolved under Crowley's own stated conventions (milui, finals, grand scale);
  3 genuine anomalies remain (A1–A3). **Calibration bombshell:** the Yophiel 136/137 case
  dissolves — the 1909 print spells יופיל (no aleph) = 136 exactly (page image verified);
  the "error" exists only if you import the aleph-spelling from another source.
- **Result:** ledgers A (genuine, 3) / B (transcription errors, 3) / C (self-flagged
  conventions, 20) / D (transcription garbles, 4) / E (unverifiable, 2).
- **Dead ends:** Equinox OCR drops all Hebrew (pivoted to transcription, then to page
  images); vibdoc 777 is a redacted edition (discarded); hermetic.com 403; MWT scans
  lending-restricted; *The Book of Thoth* excluded (copyright).

### Worker C — self-flagged anomalies → `sweep-C-selfflagged.md`
- **Hypothesis:** Crowley's doubt-language ("unusual spelling," "misprint," "doubt arising,"
  "blind," "conceal") will cluster around genuine self-flags.
- **Method:** downloaded 7 texts into the shared corpus; ran a two-pass grep battery
  (~600 raw hits → narrow textual-sense regexes → triage: keep / blinds-list / discard).
- **Observation:** 7 kept anomalies (4 resolved/explained, 2 open, 1 open-by-design);
  hit counts dominated by doctrinal/incidental uses; several "finds" turned out to be
  modern editors' footnotes (filtered).
- **Result:** anomaly ledger §2 + blinds-doctrine list §3 + discard log with reasons.
- **Dead ends:** Portuguese Liber AL mistranslation; *Law is for All* IA item
  lending-restricted (401); keepsilence.org JS-only; lib.oto-usa.org 403; IA identifiers
  equinox-v1n7/v1n5/v1n8 return HTTP 200 with no usable files; *The Book of Thoth*
  excluded (copyright); Tunis 1925/26 printing — no public scan found.

### Worker D — "Jew"/"black" priority thread → `sweep-D-jew-black.md`
- **Hypothesis:** terms for "Jew"/"black" might carry Yophiel-class anomalies or
  loaded-number landings in Crowley's tables.
- **Method:** calibrated script (יופיאל=137, ראהוור=418, θελημα=93 all verify);
  recomputed יהודי/יהודים/Ἰουδαῖος/שחור/μέλας; grepped for Crowley-printed rivals;
  checked loaded numbers {11, 77, 93, 418, 666, 777} and table collisions.
- **Observation:** all five recompute clean; **no Crowley-printed values exist** for any
  of them; no loaded-number hits; 8/8 related printed terms verify exactly.
  Strongest find is a modern editor's interpolation slip, not Crowley's.
- **Result:** per-term ledger with Yophiel scores (all zero on the five terms) + two
  flagged items (D-6 interpolation slip; D-7 unresolved shin/samekh ambiguity at SS §88).
- **Dead ends:** 1912 Equinox I(7) print not consulted (would settle D-6's provenance);
  1912 Equinox I(8) print not consulted (would resolve D-7); New Comment via modern
  restoration only; Liber MCCCLXV Greek Qabalah unpublished (out of scope).

---

## 2. CONSOLIDATED ANOMALY LEDGER

Key: **SF** = self-flagged by Crowley (yes/no). Yophiel markers: (a) small exact
discrepancy · (b) true/deviant value independently meaningful · (c) cover pairing ·
(d) motive. ✓ = hit, ~ = partial, ✗ = miss.

### SPELLING ANOMALIES (Worker A)

**S-1 — Ra-Hoor five-way family, inside Liber AL itself.**
Variants: "Ra Hoor Khuit" (II:7) · "Ra Hoor Khut" (III:1) · "Ra-Hoor-Khuit" (III:2, III:49…)
· "Ra-Hoor-Khu" (III:11, III:51) · "Ra-Hoor-Khut" (III:35) · manuscript-style
"Ra-Hoor-Khu-it" (I:36). **SF: YES** — Old Comment III:2 ("the 'I' makes a difference
in the qabalistic interpretation of the name"); New Comment III:1 (Khu-t = human
conception, Khu-it = Godhead via inserted Yod/Iota); New Comment III:11 ("why is the
name without its termination?"). The KHUT/KHUIT model, verified and generalized from
two forms to five, all inside one book.

**S-2 — Hoor-paar-kraat, three spellings inside Liber AL.**
"Hoor-paar-kraat" (I:7) · "Heru-pa-kraath" (II:8) · "Hoor-pa-kraat" (III:35).
**SF: no.** Yophiel-class (within-single-work). 777 perpetuates two of the three.

**S-3 — Aiwass / Aiwaz (author-staged, with numbers).**
"Aiwass" in Liber AL and all Holy Books; "Aiwaz" from 1929 (MTP: "AIWAZ itself adds
to 93… S. Jacobs: 'Why is Aiwaz spelt Aiwass, not Aiwaz, in the Book of the Law?'
In Greek Aiwass = 418"). Later adopted the Aiwaz Hebrew spelling on Jacobs's authority
(Liber 58 essay footnote). **SF: YES** — textbook KHUT/KHUIT model: AIWAZ=93 Hebrew,
AIWASS=418 Greek.

**S-4 — Nuith / Hadith vs Nuit / Hadit.**
Both pairs sit side-by-side inside 777's own 1909 table; Crowley's own 1929 MTP gloss
writes "Nuith! Hadith! Ra Hoor-Khuit!"; later editors standardized to Nuit/Hadit
(1996 Weiser editor's note confirms the -th period). **SF: no** — but authorial, and
the normalization was editorial, not his.

**S-5 — Babalon / Babylon, both the goddess, inside Liber 418.**
Notes: "Babalon"; 12th Aethyr vision: "O Babylon, thou mighty Mother…", "my Mother
Babylon". **SF: no.**

**S-6 — Yophiel (777) vs Iophiel (Vision and the Voice).**
Cross-work variant. **SF: no.** Hebrew-letter check blocked by OCR — the scans are
too rough (old type, poor image, Hebrew lookalike letters) for reliable
letter-level verification, and the sweep does not guess. **STATUS: UNRESOLVED —
flagged, not scored.** Resolves with clean Hebrew text of both passages.

**S-7 — Ankh-f-n-khonsu (Tunis Comment signature) vs Ankh-af-na-khonsu (verses).**
**SF: no.** Abbreviated vs full form.

*(Minor: S-8 Heru-ra-ha vs Heru-Ra-Ha — case-form only. Negatives, checked and stable:
Adonai, Choronzon, Abrahadabra, Scarlet Woman, Hismael.)*

### GEMATRIA ANOMALIES (Worker B)

**G-1 — Old Comment III:75: עם claimed 111, recomputes 110 (+1, twice).**
"עם = 111 … 111 × 6 = 666, the Seal of the Beast"; repeated as "עם with ם final adds
to 671" (true: 670). **SF: no.** Yophiel: (a)✓ small exact, systematic ×2;
(b)~ the *claimed* 111 is independently meaningful (א spelt in full = 111; his own
Old Comment I:48 ties 111 to the Beast via 6×111=666) — the true 110 is not;
(c)✓ load-bearing: 110×6=660 collapses the verse's 666 equation; (d) motive unknown.
**Highest-scoring genuine anomaly in the sweep.** Transcription-dependent (manuscript
not consulted) — reported, not interpreted.

**UPDATE 2026-10-11 — RESOLVED, anomaly dismissed.** Verified against the 1912
first publication (*The Equinox* I:7, "LIBER LEGIS; THE COMMENT," printed p. 400a;
IA item `oto-equinox-vol-1-no-01-10`, PDF p. 439, Hebrew glyphs read visually at
zoom): the printed word is **אעם** (aleph-ayin-mem) = **111**, not עם. Both web
transcriptions dropped the small initial aleph. The 671 also verifies exactly:
א(1)+ע(70)+ם(600, mispar gadol) = 671, the text explicitly flagging the final-mem
valuation; 111×6=666 holds. Every number on the page is arithmetically exact.
Neither error nor breadcrumb — a transcription artifact, like Yophiel. Full work
log: `G1-VERIFICATION.md`.

**G-2 — New Comment (I:56–57): "Little" chain sums 84, not 93.**
Printed "30+10+9+30+5=93"; six-letter word under his English-initial scheme needs
30+10+9+**9**+30+5=93 — one "+9" dropped (haplography of the doubled T); manuscript
vs transcription undetermined. **SF: no.** Yophiel: (a)✓ (b)✓ intended 93 maximally
meaningful (c) none visible (d) haplography the economical reading. **Medium-high.**

**G-3 — Sepher Sephiroth §114 "Brains": print שחוחין ≈ 382 vs printed 114.**
Page-image verified (leaf 330); transcription had misread it. **SF: no.** Yophiel:
(a)✗ (diff +268) (b)✗ (c) none (d) none. **Low** — likely printer's/lexicon error.

*(Resolved on scan-verification — Crowley correct, transcription wrong: §276
אחודראון=276; §380 מצרים=380. Twenty further mismatches resolve under Crowley's own
stated conventions — milui, finals-counted, grand scale (Ledger C, worker file).
Four transcription garbles unattributable (Ledger D). Two unverifiable (Ledger E:
"Bahlasti = 358" no Hebrew given; "Ompehda perhaps 210" — self-doubted).)*

**Calibration note (Worker B):** the historical Yophiel 136/137 case **dissolves**
against the 1909 print — Crowley printed יופיל (no aleph) = 136 exactly (page image
verified; Graphiel=325, Nakhiel=111, Agiel=45, Hagiel=49 on the same page all exact).
The "error" exists only if the aleph-spelling יופיאל is imported from another source.

### SELF-FLAGGED ANOMALIES (Worker C)

**C-1 — Khut/Khuit** (see S-1). **Resolved** — keeps the "I", gives the qabalistic reason.
**C-2 — AL I:60: phrase inserted by the Scarlet Woman's hand.** Break in dictation;
alternate phrase dictated to her and inserted in her hand. **Resolved.**
**C-3 — AL I:15: "Prince-priest" flagged as possible cipher** ("not in tone with other
references to me... I suspect therefore a secret cipher"). **Open** (PRINCEPS ITER
offered, nothing settled).
**C-4 — AL II:76: the cipher deliberately withheld** — kept secret "in order to prove
any one who should claim sonship" (names Achad). **Open by design.**
**C-5 — Liber 418: "Circle" named as a blind** for "the Mark of the Beast," kept secret
at the time. **Resolved/explained.**
**C-6 — AL I:11: careless phrasing vs hidden puzzle** ("or is there a Qabalistic puzzle
or a mystic submeaning concealed?"). **Open.**
**C-7 — AL I:24: further mystery suspected** ("possibly those of 418 and 666 again").
**Open.**

*(Blinds-doctrine passages, general not specific: AL I:34 "half known and half
concealed" — the charter text; New Comment I:13 (concealment as editorial policy);
Old Comment I:37; II:76; II:14. Observation: Crowley alleges "deliberate corruption
of the text" of the biblical Apocalypse — never of his own received texts.)*

### PRIORITY THREAD — "JEW"/"BLACK" TERMS (Worker D)

| Term | Computed | Crowley-printed | Discrepancy | Yophiel score |
|---|---|---|---|---|
| יהודי (Jew) | 35 | none found (SS 35 = AGLA/GBL/YHK) | none | zero |
| יהודים (Jews) | 75 | none found (SS 75 = GVVNY/HYLL/LYLH/NVYT…) | none | zero |
| Ἰουδαῖος (Jew) | 765 | none found (no Greek table in print; SS 765 empty) | none | zero |
| שחור (black) | 514 | none found (SS 514 = ChQVTh only; near-miss ShChR "Daybreak; black" at 508 — honest near-miss, score zero) | none | zero |
| μέλας (black) | 276 | none found (no Greek table; slot-276 entries all verify) | none | zero |

Related printed terms, all 8 verifying exactly: DYH=19 "Was black", DYV=20 "Black liquid",
ChM=48 "…black; Ham", AYShVN=367 "Black [of eye-pupil]", ShChR=508 "Daybreak; black",
a'aRPL=380 "Thick darkness", YHVD=25, YHVDH=30 "Judah".

**D-6 — Old Comment AL I:46: "61 = {Aleph-Vau-Nun}".** און = 57, one letter off the true
אין = 61 ("Nothing" — his own SS 61 entry). Yophiel: (a✓)(b✓)(c✓)(d✗) — **but** the curly
brackets mark modern editorial interpolation of a typescript gap, so this is almost
certainly the interpolator's ו/י confusion, not Crowley's. A flagged transcription slip,
not a breadcrumb.

**D-7 — Sepher Sephiroth §88 "Darkness — ChSK": shin/samekh ambiguity UNRESOLVED.**
חסך = 88 (valued-right, glossed-wrong) vs חשך = 328 (glossed-right, valued-wrong).
Needs the 1912 Equinox I(8) print to settle — flagged, not scored.

---

## 3. COVERAGE STATEMENT

**Covered:** Liber AL (3 transcriptions) · Old, New, Djeridensis Commentaries
(transcription; underlying 1912/1920s, PD) · Liber 777 (1909 scan + transcription,
cross-checked) · Sepher Sephiroth (1912; transcription swept, significant hits
scan-verified) · The Vision and the Voice · Book 4 (1912–13) · Magick in Theory and
Practice (1929; transcription) · the Holy Books (1907–11) · Liber 58 essay ·
Equinox I:5 and I:8 OCR.

**Not obtained / not covered:** *The Book of Thoth* (1944 — in copyright, deliberately
excluded) · *Magick in Theory and Practice* scans (lending-restricted) · *The Law is
for All* standalone (download failed) · Equinox I(7) scan (Old Comment's first printing;
Old Comment via secondary transcription) · Liber XXXI manuscript facsimile ("AiFass",
"TO MEGA ThHRION", manuscript hands unverified) · Djerid Comment primary · Tunis
1925/26 printing (no public scan) · hermetic.com (403 from this environment) ·
Hebrew-letter verification anywhere (OCR destroys Hebrew).

**Methodological standing rule from this sweep:** transcription drift is the dominant
noise source (2 of 3 small-diff SS "mismatches" were transcriber misreads; the Yophiel
136/137 case dissolves on the 1909 page image). **No candidate anomaly counts until
scan-verified.** New Comment findings remain transcription-dependent throughout.

---

## 4. BOTTOM LINE FOR THE RED PEN

1. The KHUT/KHUIT model is **fully verified and generalized**: five forms inside Liber AL
   itself, author-flagged twice, with Crowley's own qabalistic rationale (Khu-t = human
   conception, Khu-it = Godhead via the inserted Yod). Sibling: Aiwass/Aiwaz, author-staged
   with the numbers 93/418.
2. The YOPHIEL model produced **one high-scoring genuine anomaly**: Old Comment III:75,
   עם claimed 111 vs recomputed 110 — small, exact, systematic (twice), load-bearing for
   the verse's 666 equation, unflagged. Transcription-dependent; the manuscript would
   settle it.
3. The historical Yophiel 136/137 "error" **does not survive the 1909 print**: Crowley
   printed יופיל = 136 exactly. Score this one to the printer, not the blind.
4. The "Jew"/"black" priority thread is **clean**: no discrepancies, no Crowley-printed
   rivals, no loaded-number landings. The one slip found (D-6) is a modern editor's.
5. Crowley's self-flagged set is real and bounded: 7 items, 4 resolved, 3 open
   (I:15, I:11, I:24) plus II:76 open-by-design. His blinds doctrine is about occult
   ciphers (charter: I:34 "half known and half concealed"); he alleges deliberate textual
   corruption of Revelation, never of his own received texts.
6. **Nothing in this sweep is declared the breadcrumb.** Every entry above is scored,
   located, and left for the red pen.

*Live, Love, and let Love, Live. — 93.*
*All Rights Reserved, Without Prejudice.*
