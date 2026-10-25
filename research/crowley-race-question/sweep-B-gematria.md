# Worker B — Gematria Recomputation Sweep

**Assignment:** extract Crowley's own "X = N" equations from his texts, recompute mechanically
against the standard tables, report every mismatch with both values.
**Date:** 2026-10-11. **Findings, never doctrine.** Nothing here is declared "the breadcrumb" —
entries are reported and scored only.

---

## PART 1 — Work log (ultra-verbose: hypothesis → method → observation → result, dead ends included)

### Step 1. Reuse check.
- **Hypothesis:** the corpus dir might already hold texts from another worker.
- **Method:** listed `~/workspace/pontifex/research/crowley-race-question/` and `corpus/`.
- **Observation:** only `DEFENSE-BRIEF.md/.pdf` and its builder existed; no `corpus/` dir.
- **Result:** started from scratch; created `corpus/`. Separately found the twelve-tongues
  sweep's attested tables at `~/workspace/pontifex/pontifex/tables.py` (HEBREW mispar hechrechi,
  GREEK Milesian, LATIN_ORDINAL, AGRIPPA, ARABIC_ABJAD) and imported them rather than retyping —
  drift-proof by construction.

### Step 2. Calibration.
- **Hypothesis:** if my tables are right, יופיאל→137 and ראהוור→418 by hand.
- **Method:** weighed both with the imported HEBREW table before touching any text.
- **Observation:** יופיאל = 10+6+80+10+1+30 = **137** ✓; ראהוור = 200+1+5+6+6+200 = **418** ✓.
- **Result:** tables verified; script asserts both on every run (fails closed otherwise).

### Step 3. Source acquisition — Liber 777.
- **Hypothesis:** a PD transcription of the 1909 777 exists and is machine-usable.
- **Method:** web search → cloned `adamblvck/open_777` (transcription "from the now in open-domain
  book 777", 1909). Got a 36-row × 263-col CSV of the correspondence table.
- **Observation:** CSV is real 777 data (key scale, Hebrew names, transliterations, enumerations).
- **Result:** usable. (Dead end: `v.vibdoc.com/aleister-crowley-liber-777.html` fetched fine but is a
  different/redacted edition — "Yophiel (325)" — not the 1909 table; discarded for this check.)

### Step 4. Source acquisition — Sepher Sephiroth (Equinox I:8, 1912, PD).
- **Hypothesis:** Internet Archive OCR of Equinox I:8 yields the Hebrew entries.
- **Method:** downloaded `Equinox Vol 1 No 08_djvu.txt` (512,900 bytes) from
  `oto-equinox-vol-1-no-01-10`.
- **Observation:** **zero Hebrew runs in the entire OCR** — the engine dropped all Hebrew script.
  Dead end for direct extraction.
- **Result:** pivoted to `alanwillms/sepher-sephiroth` (GitHub): a transcription of Crowley's
  Sepher Sephiroth parsed into `output/sepher_sephiroth.json` — 3,321 numbered entries, each with
  `hebrew`, transliteration, and gloss. Cloned into `corpus/`.
- **Later (crucial):** this transcription turned out to contain misreads (see Steps 8–10), so every
  significant mismatch was re-verified against the 1912 page images via the archive.org
  `*_jp2.zip` + `*_djvu.xml` leaf-mapping route (worked: `..._0330.jp2&ext=jpg` etc.).

### Step 5. Source acquisition — Old/New/Djeridensis Commentaries on Liber AL.
- **Hypothesis:** tarrdaniel.com's combined transcription has inline equations.
- **Method:** fetched `Commentaries_to_Liber_AL_vel_Legis.html` (1 MB). It carries Hebrew script,
  `{Letter}` glosses, and the transcriber's `[HB:XXXX]` ASCII tags.
- **Observation:** 59 Hebrew runs, 11 `[HB:]` tags, plus English-initial letter-sum equations
  (`HADIT=5+1+4+10+9=29` etc.).
- **Result:** rich equation source. Provenance note: transcription (WEH/Heidrick) of
  *The Law is for All* (1996); the Old Comment is pre-1930 composition, the New Comment 1919–20.
  Manuscript not consulted — transcription-dependent findings are marked as such.

### Step 6. Source acquisition — "An Essay Upon Number" (Liber 58) + "Gematria" exposition.
- **Hypothesis:** Equinox I:5 (1911, PD) contains checkable equations.
- **Method:** downloaded `Equinox Vol 1 No 05_djvu.txt`; grepped the essay and the Temple of
  Solomon the King Qabalah section.
- **Observation:** the essay is mostly theosophical reductions (all correct; OCR merges digits,
  e.g. "44+34+84+3=18" = intended "4+3+8+3=18", resolved via context). The Temple section's
  word-equations (רוח אלהים=300, אהבה=אחד=13, מטטרון=שדי=314, יבא שילה=358=משיח,
  והנה שלשה=אלו מיכאל גבריאל ורפאל=701) **all recompute correctly**.
- **Result:** covered; no mismatches there.

### Step 7. The mechanical sweep (Sepher Sephiroth).
- **Hypothesis:** most entries recompute clean; mismatches cluster by cause.
- **Method:** `work/sweep_b.py` — weighed every `hebrew` field (stripping `:` separators etc.)
  with finals-as-medials, compared against the printed section number.
- **Observation:** **2,538 weighable words; 23 mismatches** (0.9%). Raw JSON saved to
  `work/sweep_b_raw.json`.
- **Result:** triage below; scan-verification overturned 2 of the 3 small-diff cases.

### Steps 8–10. Scan verification of the three small-diff SS mismatches (the important part).
- **114 "Brains":** transcription said ShVChVN=370. 1912 print (leaf 330, verified on page image)
  actually reads **שחוחין** ≈ 382 (transcriber misread). Either way ≠ 114 → **genuine print
  anomaly**, large diff, true value not independently meaningful. Likely printer's/lexicon error.
- **276 "Angel L.T.N. of Libra":** transcription AChVBRAYN=278. 1912 print (leaf 345) actually
  reads **אחודראון** = 1+8+6+4+200+1+6+50 = **276** ✓ → transcription error, Crowley correct.
- **380 "Difficulty, narrowness":** transcription YHBMTzRYM=397. 1912 print (leaf 354) actually
  reads **מצרים** = 40+90+200+10+40 = **380** ✓ → transcription error, Crowley correct.
- **Result:** transcription drift is real and material — 2 of 3 "mismatches" evaporated on the
  page image. Lesson recorded: no mismatch counts until scan-verified.

### Step 11. 777 tables check.
- **Method:** verified the CSV's enumeration columns against the standard tables; spot-checked
  the 1909 scan (Table III, leaf 27).
- **Observation:** Hebrew letter values all correct incl. finals; Greek/Arabic pairings correct
  except two majuscule glyph misreads in the transcription (Ξ for Ο at value 70; Ρ for ϟ Koppa
  at value 90) and one Arabic dot-misread (د for ذ at 700) — values themselves right.
- **Calibration bombshell:** the 1909 print spells the Intelligence of Jupiter **יופיל (no aleph)
  = 136** — self-consistent. The "136 vs 137" discrepancy exists only if you import the
  aleph-spelling יופיאל (=137) from another source. Crowley's printed equation is correct as
  printed. (Graphiel=325, Nakhiel=111, Agiel=45, Hagiel=49 on the same page all verify too.)

### Step 12. Commentary equations — the two live anomalies.
- **Method:** regex-extracted `[HB:]=N`, letter-sum chains, Hebrew/Greek `=N`; recomputed each.
- **Observation A (Old Comment III:75):** "Aum-Ha, עם = 111, הא = 6, 111 × 6 = 666" — but
  עם = 70+40 = **110** (+1). The +1 recurs: "עם with ם final adds to 671" vs 670 (+1).
  The 671 is independently real (תרעא=671, Adonai-in-full=671 — both verify), so only the עם
  premise is off. The error is load-bearing: 110×6=660 kills the "Seal of the Beast" equation;
  111 (= א in full, cf. his own I:48 Old Comment "111 = א") makes it work. Not self-flagged.
- **Observation B (New Comment, I:56–57 region):** "„Little‟ — 30+10+9+30+5=93" — the chain sums
  to **84**, not 93. Under his English-initial scheme L-I-T-T-L-E needs six terms:
  30+10+9+**9**+30+5 = 93 ✓. One "+9" dropped (haplography of the doubled T) — in the
  manuscript or the transcription, undetermined. Not self-flagged.
- **Everything else verified correct** (see correct sample).

### Step 13. Tertiary sources — not obtained (honest gap).
- *The Book of Thoth* (1944): still in copyright — **deliberately excluded**.
- *Magick in Theory and Practice* (1929, PD): both archive.org scans are lending-restricted
  ("Item not available"); no clean mirror found (sacred-texts 404, hermetic.com 403 to bots).
  **Not covered.**

### Dead ends log (for the record)
1. hermetic.com → 403 bot-block. 2. Equinox OCR → no Hebrew at all. 3. vibdoc 777 → wrong
   edition. 4. Essay Upon Number OCR → digit-merge glitches (resolved via context, no false
   positives emitted). 5. MWT scans → lending-restricted. 6. My first Greek-enumeration script
   mismatched bracketed Revised-edition glyphs — fixed by pairing letter↔value instead of
   trusting row order.

---

## PART 2 — The ledgers

### Ledger A — GENUINE anomalies (print- or text-level, after verification)

**A1. Sepher Sephiroth §114 — "Brains"**
- Word as printed (1912): שחוחין (transcription misread it as שוחונ)
- Crowley's value: 114 | Recomputed: 382 (print spelling) / 370 (transcription spelling)
- Table: Hebrew mispar hechrechi, finals as medials | Location: Equinox I:8 (1912), SS p.17,
  §114 — page image leaf 330 verified
- Self-flagged by Crowley? **No.**
- Yophiel-model score: (a) small exact discrepancy ✗ (diff +268); (b) true value meaningful ✗
  (382 = 2×191; no standing in his system); (c) cover pairing — none visible; (d) motive —
  none visible. **Low.** Most likely a printer's or lexicon-source error.

**A2. Old Comment on Liber AL III:75 — "Aum-Ha"**
- Word as given: עם ([HB:AUM], gloss {Ayin-Mem})
- Crowley's value: **111** ("עם = 111 … 111 × 6 = 666, the Seal of the Beast"); repeated as
  "עם with ם final adds to 671"
- Recomputed: עם = 70+40 = **110**; with final Mem = 670. (Diff: +1, twice, systematic.)
- Table: Hebrew mispar hechrechi | Location: tarrdaniel.com combined commentaries,
  Old Comment III:75 (transcription of *The Law is for All*; manuscript not consulted —
  transcription-dependent)
- Self-flagged by Crowley? **No.**
- Yophiel-model score: (a) ✓ small exact (+1); (b) ~ — the *claimed* value 111 is independently
  meaningful (א spelt in full = 111; his own Old Comment I:48: "111 = א … = the Number of the
  Beast" via 6×111=666); the true 110 is not; (c) the error is load-bearing for the 666
  "Seal of the Beast" equation in that verse (110×6=660 breaks it); (d) motive unknown.
  **Highest-scoring genuine anomaly in the sweep.** Reported, not interpreted.

**A3. New Comment (I:56–57 region) — "Little"**
- Word as given: "Little" (English-initial scheme: L=30,I=10,T=9,T=9,L=30,E=5)
- Crowley's chain: "30+10+9+30+5=93" | Chain as printed sums to: **84**
- Recomputed with the missing term restored: 30+10+9+9+30+5 = **93** ✓
- Table: Crowley's English-initial→Hebrew-value mapping (his stated scheme)
- Location: tarrdaniel.com combined commentaries, New Comment near I:57 (transcription;
  whether the "+9" dropped in manuscript or transcription is undetermined)
- Self-flagged by Crowley? **No.**
- Yophiel-model score: (a) ✓ small exact (one dropped term); (b) ✓ intended 93 maximally
  meaningful (Thelema/Agape); (c) none visible; (d) haplography of the doubled T is the
  economical reading. **Medium-high.** A dropped addend, not a wrong sum.

### Ledger B — RESOLVED on scan verification (transcription errors, Crowley correct)
- **B1.** SS §276 "Angel L.T.N. of Libra": transcription AChVBRAYN=278 vs §276; 1912 print reads
  אחודראון = **276** ✓ (leaf 345).
- **B2.** SS §380 "Difficulty, narrowness": transcription YHBMTzRYM=397 vs §380; 1912 print reads
  מצרים = **380** ✓ (leaf 354).
- **B3.** SS §114 "Brains": transcription misread the Hebrew (שוחונ vs print שחוחין) — print
  still anomalous (see A1).

### Ledger C — SELF-FLAGGED by Crowley (alternative convention stated; not anomalies)
All 20 remaining SS mismatches resolve under the convention Crowley prints inline:
- *Spelt in full (milui):* §628/633/643 אור (AVR: 111+7/12/22+510 with V as VA/VV/VYV),
  §566 סוד (SMK+VV+DLTh = 120+12+434), §936 כתר (K+ThV+RYSh = 20+406+510),
  §963 אחד (Achad "spelt fully"), §671 אדני ("Adonai spelt in full" = 111+434+106+20).
- *Finals counted:* §572 (יהוה אלהיך, K final), §646 (אלהים, M final), §676 (גלגלים, M final),
  §741 (אמן, N=700), §837 (למרבה, M final), §1060 (משכן, N final), §1173 (את יהוה אלהינו, N final),
  §3321 ×2 (Moon phrases, ם=600/ן=700 — both recompute exactly to 3321 with finals).
- *Scales/symbolic:* §666 (הא × אלף "on the Grand Scale"), §3200 (בראשית ברא אלהים placed
  under "32 × 10², The paths of the Whole Tree in excelsis" — symbolic, annotated),
  §1400 (את "Chaos, or = HB:ATh, 401 q.v." — cross-reference given).

### Ledger D — TRANSCRIPTION garbles (cannot attribute to Crowley; manuscript needed)
- **D1.** Old Comment II:16: "(= 418 = חיטשׁ {HB:ChYTh} = ח {Cheth} = 8)" — as transcribed,
  חיטש=327≠418 and the chain is incoherent; likely corruption in transmission.
- **D2.** 777 CSV, Greek column: row 26 majuscule Ξ paired with 70 (should be Ο; minuscule ο
  correct); row 29 Ρ paired with 90 (should be ϟ Koppa; Rho=100). Transcriber glyph misreads;
  enumeration values correct.
- **D3.** 777 CSV, Arabic column: row 6 letter read د (dal) with value 700 (should be ذ dhal);
  row 10 duplicated غ with dropped value. Transcription artifacts; all letter↔value pairings
  otherwise correct.
- **D4.** Transcriber typo "[HB:YHVHH]" for יהוה (extra H) in the AUMThSh passage.

### Ledger E — UNVERIFIABLE from the spelling given / self-flagged doubt
- **E1.** Old Comment III:54: "Bahlasti = 358" — no Hebrew supplied in the transcription; the
  Latin spelling alone doesn't fix a weighing (one reconstruction, B-A-H-L-A-Sh-T-I with
  S→ש/T→ט, gives 358; manuscript needed).
- **E2.** Old Comment III:54: "Ompehda perhaps 210" — Crowley flags his own doubt ("perhaps").
  (Worker C's lane; noted here only.)

### Correct-sample (the check has teeth — all recomputed clean)
- Sepher Sephiroth: 2,515 of 2,538 weighable words match their printed section (99.1%).
- 777 (1909 print, Table III): יופיל=136, גראפיאל=325, נכיאל=111, אגיאל=45, הגיאל=49 —
  **all exact** (page image verified). Hebrew letter enumerations (incl. finals) all exact;
  Greek/Arabic enumerations exact (modulo D2/D3 glyph misreads).
- Commentaries: בולשכין=418 (Boleskine); ראהוור=418; אמתש=741, +ע=70 → 811 = IAO in Greek
  (Ι+Α+Ω=811) ✓; אמן=91; לא=31; HADIT=5+1+4+10+9=29 ✓; BECAUSE=2+5+3+1+6+7+5=29 ✓;
  REASON=200+5+1+7+70+50=333 ✓; AUGHT=1+6+3+5+9=24 ✓; HEATHEN=5+5+1+9+5+5+50=80 ✓;
  OFF=6+6+6=18 ✓; Well=6+6+5+30+30=77 ✓; HELL=H+L+L=65 ✓; HALF=5+1+30+6=42 ✓;
  Hadit=11+410=421, Nuit=56+410=466, 421−3=418, 466+200=666 ✓ (premises flagged in-text);
  Θε=14, λη=38, μα=41 (Greek) ✓; "Joy"=10+70+10=90 ✓; "ye"=YOD+HE=15 ✓; US=6+60=66 ✓.
- Temple of Solomon the King (Eqx I:5): רוח אלהים=300 ✓; אהבה=אחד=13 ✓; מטטרון=שדי=314 ✓;
  יבא שילה=358=משיח ✓; והנה שלשה=אלו מיכאל גבריאל ורפאל=701 ✓ (both phrases).

### Coverage statement
- **Covered:** Liber 777 (1909 1st ed. scan + open_777 transcription, cross-checked); Sepher
  Sephiroth (1912 Equinox I:8; transcription swept, all significant mismatches scan-verified);
  Old + New + Djeridensis Commentaries (tarrdaniel transcription); "An Essay Upon Number"
  (Liber 58, Equinox I:5); the "Gematria" exposition in Temple of Solomon the King (Eqx I:5).
- **Not obtained:** *The Book of Thoth* (1944 — in copyright, deliberately excluded);
  *Magick in Theory and Practice* (1929 — PD, but both archive.org scans lending-restricted,
  no clean mirror found).
- **Corpus on disk:** `corpus/` — equinox-v1n05.txt, equinox-v1n08.txt, n08_djvu.xml,
  777_djvu.xml, commentaries.html, vibdoc777.html (discarded ed.), open_777/, sepher-sephiroth/,
  page images ss_p330/345/354/412/414.jpg, 777_p27.jpg (+ crops). Raw machine output:
  `work/sweep_b.py`, `work/sweep_b_raw.json`.

### Methodological note for the parent
Transcription drift is the dominant noise source in this lane: 2 of 3 small-diff SS
"mismatches" were transcriber misreads, and the Yophiel 136/137 case dissolves against the
1909 printed spelling (יופיל=136 exact). Any candidate anomaly should be held to the
scan-verification standard applied here before being weighed as Crowley's.
