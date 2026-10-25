# SWEEP A — Spelling-Variant Hunt: Divine/Angelic Names in Crowley's Corpus

**Worker A report — 2026-10-11. Findings, never doctrine. No variant is declared "the breadcrumb."**

Scope: collect every spelling variant of the divine/angelic names across Crowley's corpus, distinguishing (i) variants within a single work, (ii) variants across works, (iii) variants Crowley himself flagged.

---

## PART 1 — ULTRA-VERBOSE WORK LOG

### Step 0 — Hypothesis
Crowley's divine names are not orthographically stable. The task supplied two models: (1) YOPHIEL MODEL — a small exact discrepancy inside Crowley's own tables; (2) KHUT/KHUIT MODEL — an author-flagged spelling anomaly with stated qabalistic significance ("doubt arising in the mind of the prophet as to the unusual spelling… the 'I' makes a difference in the qabalistic interpretation of the name"). Hypothesis: a systematic regex sweep across the major works will surface (a) the full variant family for Ra-Hoor-Khuit/Khut, (b) sibling anomalies (Aiwass/Aiwaz, Nuit/Nuith, Hadit/Hadith, Babalon/Babylon, Hoor-paar-kraat and kin), and (c) places where Crowley himself comments on a spelling.

### Step 1 — Method: locate the shared corpus
**Method:** list `~/workspace/pontifex/research/crowley-race-question/corpus/`.
**Observation:** the directory did not exist; nothing had been downloaded yet by anyone. Other workers' files appeared *during* my run (equinox-v1n05.txt, equinox-v1n08.txt, liber777.txt, liberAL.txt, magick-theory-practice.txt, book4.txt, holybooks.txt, holybooks-commentaries.txt, liber58-essay.txt, liberAL-thelemaorg.txt, law-is-for-all.txt). Two zero-byte failed downloads (equinox-v1n5.txt, equinox-v1n8.txt) and one 172-byte failed download (law-is-for-all.txt) were also present. A Portuguese translation (liberAL.txt) appeared and was later removed by another worker.
**Result:** I created the corpus dir and downloaded 4 texts myself; I re-ran extraction after each batch of new files so the final ledger covers everything present.

### Step 2 — Method: obtain Liber AL text
**Method:** tried hermetic.com/legis/ccxx (named in task) via curl and via browser.open.
**Observation:** direct egress is dead on this host (curl without proxy = 000; known quirk). Via the egress proxy, hermetic.com returned **403 Forbidden**; browser.open likewise returned 403 upstream_access_rejected. sacred-texts.com timed out (000). bibliotecapleyades.net returned 404 for the guessed path.
**Result (dead end):** hermetic.com is not reachable from this environment. Fell back to archive.org.

### Step 3 — Method: archive.org "Libers" collection
**Method:** queried `https://archive.org/metadata/Libers`, listed `*_djvu.txt` files.
**Observation:** the collection holds OCR texts of the Holy Books incl. CCXX (Liber AL), DCCLXXVII (777), D (Sepher Sephiroth, Liber 500), CDXVIII (Vision and the Voice, Liber 418). First download attempt via `https://archive.org/download/Libers/CCXX_djvu.txt` returned **500 Internal Server Error** (170-byte error page).
**Result (dead end → workaround):** the `/download/` redirector was failing; the metadata API gave the direct server (`ia801807.us.archive.org`, dir `/13/items/Libers`), and direct-server URLs returned 200. Downloaded: CCXX_djvu.txt (44 KB), DCCLXXVII_djvu.txt (141 KB), D_djvu.txt (129 KB), CDXVIII_djvu.txt (433 KB).

### Step 4 — Method: Equinox full texts on archive.org
**Method:** archive.org advancedsearch API for Equinox I(7), I(5), I(8).
**Observation:** no clean Equinox I(7) full-text item found. Another worker later supplied equinox-v1n05.txt (Equinox I(5), 580 KB) and equinox-v1n08.txt (Equinox I(8), 513 KB). I never obtained Equinox I(7) (first publication of Liber AL + Old Comment, 1912).
**Result (partial):** Old Comment passages verified instead via a secondary web transcription (geocities.ws mirror of the hermetic.com commentaries page, which labels Old vs New Comment per verse). Noted as secondary-source verification, not a primary scan.

### Step 5 — Method: extraction script
**Method:** wrote `corpus/extract_variants.py` — case-insensitive regex per name, emitting variant → [{file, line, one-line context}].
**Observation:** first run covered 9 files; after other workers added files, re-ran twice more (final: 16 files, incl. two zero-byte files that yielded nothing).
**Result:** `corpus/variants_raw.json` — the machine-readable ledger. All findings below were then hand-verified with context reads (OCR artifacts separated from genuine variants).

### Step 6 — Method: verify the KHUT/KHUIT family inside Liber AL
**Method:** grepped all Ra-Hoor forms across the three Liber AL transcriptions (CCXX_djvu, holybooks, liberAL-thelemaorg).
**Observation:** FIVE distinct surface forms inside one short book:
- II:7 — "Ra Hoor Khuit" (spaced, with i): "then expect the direful judgments of Ra Hoor Khuit!"
- III:1 — "Ra Hoor Khut" (spaced, no i): "Abrahadabra; the reward of Ra Hoor Khut."
- III:2 — "Ra-Hoor-Khuit" (hyphenated, with i): "Raise the spell of Ra-Hoor-Khuit!"
- III:11 — "Ra-Hoor-Khu" (hyphenated, no -t at all): "Ra-Hoor-Khu is with thee."
- III:35 — "Ra-Hoor-Khut" (hyphenated, no i): "called Hoor-pa-kraat and Ra-Hoor-Khut."
- III:51 — "Ra-Hoor-Khu" again: "prophet of Ra-Hoor-Khu!"
- I:36 — "Ra-Hoor-Khu-it" in the manuscript-style transcription (holybooks.txt); the thelema.org transcription prints "Ra-Hoor-Khuit" here.
**Result:** the KHUT/KHUIT model is not a two-way variant — it is a five-way family, and the variation sits *inside* Liber AL itself (YOPHIEL-model class), not only between manuscript and commentary.

### Step 7 — Method: check whether Crowley flagged the Khut/Khuit spelling
**Method:** grepped the corpus for "doubt arising" / "unusual spelling" — no hits (Old Comment not in corpus). Used browser.search for the exact phrase.
**Observation:** the phrase is the **Old Comment on AL III:2** (Equinox I(7), 1912 — public domain): "2. Suggested by a doubt arising in the mind of the prophet as to the unusual spelling. But the 'I' makes a difference in the qabalistic interpretation of the name." The **New Comment on AL III:1** expands it: "Why is the name of Him spelt Khut? … Without the Yod or Iota, Khu-t, we get a human conception; the insertion of that letter makes the transmutation to Godhead." The **New Comment on AL III:11** flags the third form: "Ra-Hoor-Khu; why is the name without its termination? Perhaps to indicate the essence of the force."
**Result:** author-flagged (KHUT/KHUIT model) — twice over, in both the 1912 Old Comment (PD) and the New Comment. Quoted minimally below.

### Step 8 — Method: the child-god's other name
**Method:** grepped all Hoor-paar-kraat/Heru-pa-kraath forms.
**Observation:** THREE distinct spellings inside Liber AL:
- I:7 — "Hoor-paar-kraat": "Aiwass the minister of Hoor-paar-kraat."
- II:8 — "Heru-pa-kraath": "Who worshipped Heru-pa-kraath have worshipped me…"
- III:35 — "Hoor-pa-kraat": "called Hoor-pa-kraat and Ra-Hoor-Khut."
Plus 777's tables: "Heru-pa-Kraath" (Egyptian-gods column, line 0) and "Hoor-pa-kraat" (line II, glossed "as ATU 0"). The 777 Revised editorial note normalizes to "Hoor-par-Kraat (Horus the Child)" — an editor's spelling, not Crowley's.
**Result:** a second within-single-work (YOPHIEL-class) anomaly: the child-god's name is spelled three different ways in Liber AL.

### Step 9 — Method: Aiwass/Aiwaz
**Method:** grepped both forms across corpus.
**Observation:** Liber AL (I:7) and all Holy Books print "Aiwass". "Aiwaz" appears only in later works: Magick in Theory and Practice (1929) — "AIWAZ itself adds to 93… S. Jacobs: 'Why is Aiwaz spelt Aiwass, not Aiwaz, in the Book of the Law?' In Greek Aiwass = 418"; the New Comment ("identified with the essence of the life of Aiwaz"; "die at the caress of AIWAZ"); a modern Liber 58 essay footnote ("Crowley later decided this was an error and that the actual Hebrew spelling of Aiwaz was [Hebrew] = 93, after having the latter spelling communicated to him by one Samuel A. Jacobs"). The manuscript title-page form "AiFass" (per secondary sources) was NOT found in the corpus — manuscript facsimile not obtained.
**Result:** author-flagged spelling anomaly with stated qabalistic significance (93 Hebrew / 418 Greek) — textbook KHUT/KHUIT-model.

### Step 10 — Method: Nuit/Nuith, Hadit/Hadith
**Method:** grepped both pairs.
**Observation:** Liber AL proper uses only "Nuit" / "Hadit" — BUT the short forms "Nu" and "Had" also occur in-verse (III:51 "prophet of Nu! prophet of Had!"; III:17 "Nu is your refuge as Hadit your light"; II:1 "Nu! the hiding of Hadit"). "Nuith"/"Hadith" appear in: 777's 1909 Egyptian-gods table (line 0: "Nuith [[Nuit and Hadit]]"; line 1: "Hadith [[Heru-Ra-Ha]]"; line 2: "Nuith [Zodiac]") — i.e., WITHIN the 777 table both -t and -th forms sit side by side; Magick in Theory and Practice (1929), Crowley's own words: 'SA-BA-FT "Nuith! Hadith! Ra Hoor-Khuit! Hail, Great Wild Beast!"' (his Thelemic gloss of a barbarous name); the New Comment typescripts (per the 1996 Weiser editor's note: "This commentary was produced in the period when Crowley frequently used spellings ending in 'th' like 'Nuith'" — editor standardized them to "Nuit").
**Result:** genuine variants, both within 777's own table and across works; the -th forms are authorial (1929 MTP), later normalized by editors. (The 50-word quote cap respected: one line each.)

### Step 11 — Method: Babalon/Babylon
**Method:** grepped both; checked whether "Babylon" ever denotes the goddess vs. the city.
**Observation:** in the Vision and the Voice (Liber 418), BOTH spellings denote the goddess: "Babalon" in the notes ("Minister of Babalon", "the Cup of Babalon") and "Babylon" in the 12th Aethyr vision ("O Babylon, thou mighty Mother, that ridest upon the crown…", "my Mother Babylon", "Babylon the Beautiful"). 777's table prints "BABALON." (single form).
**Result:** within-single-work variant in Liber 418 (YOPHIEL class).

### Step 12 — Method: Yophiel/Iophiel/Jophiel
**Method:** grepped all three.
**Observation:** 777's tables (1909) print "Yophiel" (beside the 136 entry — the number is Worker B's remit). The Vision and the Voice prints "Iophiel" ("Visit Iophiel and Hismael, and report their appearance"). No "Jophiel" in corpus. "Hismael" is spelled consistently (777 + V&V). The Hebrew behind Yophiel is OCR-mangled in both 777 texts ("V'BV", "SB)"), so the Hebrew spelling (יופיאל vs. spaced) could NOT be verified from OCR — needs the scan.
**Result:** cross-work spelling variant (Yophiel vs Iophiel); Hebrew-letter verification blocked by OCR quality — flagged as a gap.

### Step 13 — Method: Ankh-af-na-khonsu, Heru-ra-ha, Therion, V.V.V.V.V., Adonai, Choronzon, Abrahadabra
**Observation:**
- "Ankh-af-na-khonsu": single consistent spelling everywhere it occurs in the verses. BUT the Tunis Comment signature (appended to Liber AL in the thelema.org transcription) reads "Ankh-f-n-khonsu" — a genuine abbreviated variant form.
- "Heru-ra-ha": Liber AL prints "Heru-ra-ha"; 777, V&V, and the commentaries print "Heru-Ra-Ha" — case-form variant only, same letters.
- "Therion"/"To Mega Therion": "Therion" occurs only in prose/intro material ("Master Therion"); Liber AL's verses say "the Beast". "To Mega Therion" occurs NOWHERE in the corpus — the manuscript title ("TO MEGA ThHRION") was not obtained.
- "V.V.V.V.V.": single genuine form; "VVVV.V."/"VVV.V.V" hits are OCR errors of it (holybooks-commentaries.txt:2069 etc.).
- Adonai (146 hits), Choronzon (98), Abrahadabra (38): no variants found.
- Sepher Sephiroth's "Angel of Ra Hoor Khuit AYVAS/OSTS": OCR garbage over Hebrew — not a variant; Hebrew unreadable in OCR.
**Result:** mostly negative — recorded as such.

### Step 14 — Method: The Book of Thoth
**Method:** searched archive.org for a full-text item (bookofthothshort0000crow found — the 1944 Equinox III:5).
**Observation:** did not download/OCR it in the time available; it is also the one major work still in copyright (1944), so only minimal fair-use quoting would be possible anyway.
**Result (not covered):** flagged as a gap for a follow-up with proper copyright discipline.

### Dead ends and honest negatives (kept, per instructions)
- hermetic.com: 403 via proxy AND via browser.open — unusable from this environment.
- sacred-texts.com: connection timeout; bibliotecapleyades.net: 404 on the tried path.
- archive.org `/download/` redirector 500s for the Libers item — worked around via direct server.
- Equinox I(7) (1912, Old Comment's first printing): no usable archive.org full-text item found; Old Comment verified via secondary transcription only.
- "Law is for All" (New Comment on Liber AL): download failed (172 bytes); New Comment passages verified via secondary transcription only.
- Liber XXXI manuscript facsimile: not obtained — so "AiFass", "Ra-Hoor-Khut" manuscript hand, and "TO MEGA ThHRION" title forms are unverified from primary source.
- Hebrew spellings in 777/Sepher Sephiroth: OCR renders Hebrew as garbage; no Hebrew-letter variant claims made.
- Greps returning nothing: "Jophiel", "To Mega Therion", "Megatherion", "ThHRION", "AiFass", "Nuith" inside Liber AL proper, "Hadith" inside Liber AL proper, "Aiwaz" in any pre-1920 text, "Babalon" variant spellings other than Babylon.

---

## PART 2 — VARIANT LEDGER

Format: name → variant → locations (file:line) + one-line context. PD = pre-1930/public-domain work. "Ed." = modern editorial apparatus (quoted minimally).

### 1. RA-HOOR-KHUIT family (5 surface forms — within Liber AL itself)

| Variant | Where | Context (one line) |
|---|---|---|
| Ra Hoor Khuit (spaced, +i) | Liber AL II:7 (CCXX_djvu.txt:507; liberAL-thelemaorg) | "then expect the direful judgments of Ra Hoor Khuit!" |
| Ra Hoor Khut (spaced, no i) | Liber AL III:1 (CCXX_djvu.txt:814; holybooks.txt:4184; liberAL-thelemaorg) | "Abrahadabra; the reward of Ra Hoor Khut." |
| Ra-Hoor-Khuit (hyphenated, +i) | Liber AL III:2, III:49, III:60 etc.; 777; V&V; MTP; commentaries | "Raise the spell of Ra-Hoor-Khuit!" (III:2) |
| Ra-Hoor-Khut (hyphenated, no i) | Liber AL III:35 (holybooks.txt:4347; liberAL-thelemaorg; CCXX_djvu.txt:915 truncated "Ra-Hoor-Khu.") | "called Hoor-pa-kraat and Ra-Hoor-Khut." |
| Ra-Hoor-Khu (no -t) | Liber AL III:11 (CCXX_djvu.txt:841), III:51 (CCXX_djvu.txt:761) | "Ra-Hoor-Khu is with thee." / "prophet of Ra-Hoor-Khu!" |
| Ra-Hoor-Khu-it (split) | Liber AL I:36, manuscript-style transcription (holybooks.txt:3661); thelema.org prints "Ra-Hoor-Khuit" here | "he shall comment thereupon by the wisdom of Ra-Hoor-Khu-it." |
| Ra Hoor Khuit (spaced, +i) | V&V (CDXVIII_djvu.txt:5076 etc.; equinox-v1n05.txt:10516); Sepher Sephiroth (D_djvu.txt:1367; equinox-v1n08.txt:14695) | "the great god Ra Hoor Khuit." |
| Ra Hoor-Khuit (hybrid) | MTP (1929) barbarous-name gloss (magick-theory-practice.txt:10256) | 'SA-BA-FT "Nuith! Hadith! Ra Hoor-Khuit! …"' |

**Author-flagged (KHUT/KHUIT model):**
- Old Comment, AL III:2 (Equinox I(7), 1912, PD): "Suggested by a doubt arising in the mind of the prophet as to the unusual spelling. But the 'I' makes a difference in the qabalistic interpretation of the name." (verified via secondary transcription; primary scan not obtained)
- New Comment, AL III:1: "Why is the name of Him spelt Khut? … Without the Yod or Iota, Khu-t, we get a human conception; the insertion of that letter makes the transmutation to Godhead." (secondary source; New Comment is posthumous)
- New Comment, AL III:11: "Ra-Hoor-Khu; why is the name without its termination? Perhaps to indicate the essence of the force." (secondary source)

### 2. HOOR-PAAR-KRAAT family (3 spellings — within Liber AL itself)

| Variant | Where | Context |
|---|---|---|
| Hoor-paar-kraat | Liber AL I:7; V&V (CDXVIII); MTP ("HOOR-PAAR-KRAAT"); Commentaries on the Holy Books | "Aiwass the minister of Hoor-paar-kraat." (AL I:7) |
| Hoor-pa-kraat | Liber AL III:35; 777 Egyptian-gods table line II ("Nu [[Hoor-pa-kraat as ATU 0]]") | "called Hoor-pa-kraat and Ra-Hoor-Khut." (AL III:35) |
| Heru-pa-kraath | Liber AL II:8; 777 Egyptian-gods table line 0 ("Heru-pa-Kraath") | "Who worshipped Heru-pa-kraath have worshipped me…" (AL II:8) |
| Hoor-par-Kraat | 777 Revised editorial note ONLY (DCCLXXVII_djvu.txt:13831; liber777.txt) — modern editor's normalization: "said to combine Hoor-par-Kraat (Horus the Child)" | — not Crowley's spelling; recorded to prevent confusion |

### 3. AIWASS / AIWAZ (author-flagged; 93/418)

| Variant | Where | Context |
|---|---|---|
| Aiwass | Liber AL I:7 (all transcriptions); V&V; 777; Commentaries on the Holy Books | "it is revealed by Aiwass the minister of Hoor-paar-kraat." |
| Aiwaz | MTP (1929) (magick-theory-practice.txt:9808, 9836, 12565); New Comment ("the essence of the life of Aiwaz"; "die at the caress of AIWAZ"); Liber 58 essay fn. | MTP: 'S. Jacobs: "Why is Aiwaz spelt Aiwass, not Aiwaz, in the Book of the Law?" In Greek Aiwass = 418.' ; Liber 58 essay fn.: "Crowley later decided this was an error and that the actual Hebrew spelling of Aiwaz was [Hebrew] = 93, after having the latter spelling communicated to him by one Samuel A. Jacobs" |
| AiFass | Liber XXXI manuscript title-page ("as delivered by … AiFass …") — per secondary sources only; NOT in corpus | NOT VERIFIED from primary source (manuscript facsimile not obtained) |

### 4. NUIT / NUITH and HADIT / HADITH

| Variant | Where | Context |
|---|---|---|
| Nuit | everywhere, incl. all of Liber AL | "Had! The manifestation of Nuit." (AL I:1) |
| Nuith | 777 table line 0 ("Harpocrates, Amoun, Nuith [[Nuit and Hadit]]") and line 2 ("Amoun, Thoth, Nuith [Zodiac]"); MTP (1929) barbarous-name gloss ('"Nuith! Hadith! Ra Hoor-Khuit!"'); New Comment typescripts (per 1996 Weiser ed. note: "the period when Crowley frequently used spellings ending in 'th' like 'Nuith'") | 777's own table prints Nuith AND Nuit side by side |
| Hadit | everywhere, incl. all of Liber AL | "Be thou Hadit, my secret centre…" (AL I:2) |
| Hadith | 777 table line 1 ("Ptah, Asar un Nefer, Hadith [[Heru-Ra-Ha]]") vs. line 0 "Hadit"; MTP (1929) as above | 777 Revised ed. note: "Hadith in this line (also Hadit in line 0)" |
| Nu / Had (short forms) | Liber AL II:1 ("Nu! the hiding of Hadit"), III:17 ("Nu is your refuge as Hadit your light"), III:51 ("prophet of Nu! prophet of Had!") | noted as in-text short/long forms, not spelling variants per se |

### 5. BABALON / BABYLON (within Liber 418)

| Variant | Where | Context |
|---|---|---|
| Babalon | Liber Cheth (holybooks.txt:3356: "Babalon the Mother of Abominations"); V&V notes ("Minister of Babalon", "the Cup of Babalon"); 777 table ("BABALON.") | goddess |
| Babylon | V&V 12th Aethyr (CDXVIII_djvu.txt:6154–6270; equinox-v1n05.txt:11359ff) | "O Babylon, thou mighty Mother, that ridest upon the crown…"; "my Mother Babylon"; "Babylon the Beautiful" — the goddess, not the city |

### 6. YOPHIEL / IOPHIEL

| Variant | Where | Context |
|---|---|---|
| Yophiel | 777 tables (1909) (DCCLXXVII_djvu.txt:6658; liber777.txt:2433 — beside the 136 entry) | "Yophiel" |
| Iophiel | The Vision and the Voice (holybooks-commentaries.txt:435) | "Visit Iophiel and Hismael, and report their appearance…" |
| (Jophiel) | no hits in corpus | — |
| Hebrew | OCR-mangled in both 777 texts ("V'BV", "SB)") — NOT verifiable from OCR | gap: needs the scan |

### 7. ANKH-AF-NA-KHONSU

| Variant | Where | Context |
|---|---|---|
| Ankh-af-na-khonsu | Liber AL I:36, III:35-song (all transcriptions) — fully consistent | "My scribe Ankh-af-na-khonsu, the priest of the princes…" |
| Ankh-f-n-khonsu | Tunis Comment signature (liberAL-thelemaorg.txt, appended to Liber AL) | "The priest of the princes, Ankh-f-n-khonsu" |

### 8. HERU-RA-HA (case-form only)

| Variant | Where |
|---|---|
| Heru-ra-ha | Liber AL III:35 (all transcriptions) |
| Heru-Ra-Ha | 777 (DCCLXXVII_djvu.txt:2307 etc.); V&V (CDXVIII_djvu.txt ×7); Commentaries on the Holy Books; MTP ("HERU-RA-HA") |

### 9. THERION / TO MEGA THERION / THE BEAST

| Variant | Where |
|---|---|
| the Beast | Liber AL I:15, III:22, III:47 ("the Beast & his Bride"; "in the writing of the Beast") |
| Therion | prose/intro only ("Master Therion") — never in the verses |
| To Mega Therion / TO MEGA ThHRION | ZERO hits in corpus — manuscript title form not obtained (Liber XXXI facsimile not in corpus) |

### 10. V.V.V.V.V. — no genuine variant
Single form "V.V.V.V.V." (21 hits across files). "VVVV.V." / "VVV.V.V" (holybooks-commentaries.txt:2069, 10417) are OCR errors of it.

### 11. Negative results (checked, no variants)
Adonai (146 hits), Choronzon (98), Abrahadabra (38), Scarlet Woman (18) — one spelling each. "Hismael" consistent (777 + V&V). Sepher Sephiroth "Angel of Ra Hoor Khuit AYVAS/OSTS" = OCR garbage over Hebrew, not a variant.

---

## PART 3 — COVERAGE

**Covered (primary texts, PD unless noted):**
- Liber AL — 3 transcriptions: archive.org "Libers" OCR (CCXX_djvu.txt), Holy Books transcription (holybooks.txt), thelema.org page (liberAL-thelemaorg.txt, another worker's download)
- 777 — 1909 OCR (DCCLXXVII_djvu.txt) + 777 Revised transcription (liber777.txt, another worker's)
- Sepher Sephiroth (Liber D) — Equinox I(8) OCR (D_djvu.txt; equinox-v1n08.txt)
- The Vision and the Voice (Liber 418) — "Libers" OCR (CDXVIII_djvu.txt) + Equinox I(5) OCR (equinox-v1n05.txt)
- Magick in Theory and Practice (1929) (magick-theory-practice.txt)
- Book 4 Parts I–II (book4.txt)
- Commentaries on the Holy Books and Other Papers, Weiser 1996 (holybooks-commentaries.txt) — in-copyright; quoted ≤1 line (editorial note)
- Liber 58 essay (liber58-essay.txt) — modern; quoted ≤1 line (footnote)
- Old Comment (1912) and New Comment on Liber AL — via secondary web transcriptions only (geocities.ws mirror labeling Old vs New per verse; thelema.org forum thread). Primary scans NOT obtained.

**NOT obtained:**
- The Book of Thoth (1944) — in copyright; needs a careful fair-use pass
- Equinox I(7) (1912) scan — Old Comment's first printing
- "The Law is for All" / Magical and Philosophical Commentaries (New Comment) — download failed
- Liber XXXI manuscript facsimile — "AiFass", "TO MEGA ThHRION", manuscript "Ra-Hoor-Khut" hand unverified from primary source
- Djerid Comment
- Hebrew-letter spellings anywhere (OCR destroys Hebrew)

**Shared-work note:** other workers added/removed files mid-run (liberAL.txt added then removed; book4.txt, holybooks.txt, holybooks-commentaries.txt, liber58-essay.txt, liberAL-thelemaorg.txt added). Final extraction (16 files) covers everything present at write time. `corpus/extract_variants.py` and `corpus/variants_raw.json` are reproducible artifacts. Nothing pushed to git.

---

## PART 4 — SUMMARY OF FINDINGS (no doctrine declared)

1. Liber AL contains **five** surface forms of Ra-Hoor's name (Ra Hoor Khuit / Ra Hoor Khut / Ra-Hoor-Khuit / Ra-Hoor-Khut / Ra-Hoor-Khu, plus manuscript-style Ra-Hoor-Khu-it at I:36) — the KHUT/KHUIT model generalized from two forms to five, all inside one book.
2. Liber AL contains **three** spellings of the child-god's name (Hoor-paar-kraat I:7 / Heru-pa-kraath II:8 / Hoor-pa-kraat III:35) — a second within-single-work anomaly of the YOPHIEL class.
3. **Aiwass/Aiwaz** is the cleanest KHUT/KHUIT-model match: Crowley himself stages the question (via S. Jacobs) and answers it with two qabalistic numbers (AIWAZ=93 Hebrew, AIWASS=418 Greek) in MTP (1929); later he reportedly adopted the Aiwaz Hebrew spelling on Jacobs's authority.
4. **Nuith/Hadith** are authorial 1929 spellings (MTP's own barbarous-name gloss: "Nuith! Hadith! Ra Hoor-Khuit!") and sit side-by-side with Nuit/Hadit inside 777's own 1909 table; later editors standardized them away.
5. **Babalon/Babylon** both denote the goddess inside Liber 418 (notes vs. 12th Aethyr vision).
6. **Yophiel (777) vs Iophiel (V&V)** — cross-work variant; Hebrew-letter check blocked by OCR.
7. **Ankh-f-n-khonsu** (Tunis Comment signature) vs **Ankh-af-na-khonsu** (verses).
8. Crowley **flagged** the Khut/Khuit spelling himself in the 1912 Old Comment ("the 'I' makes a difference in the qabalistic interpretation of the name") and again in the New Comment (Khu-t human conception vs. Khu-it Godhead via the inserted Yod/Iota; "Ra-Hoor-Khu; why is the name without its termination?").
