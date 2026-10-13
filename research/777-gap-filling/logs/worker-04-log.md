# WORKER-04 Thought Log — PONTIFEX 777 gap-filling
worker-04, 2026-10-13. Column XLVII: "Kings and Princes of the Jinn."
Cells: XLVII/32 bis, XLVII/31 bis, XLVII/17, XLVII/22, XLVII/25, XLVII/26.

Standing discipline: hypothesis → method → observation → result per step.
Dead ends and discarded lines included. Findings, never doctrine. Red pen rules.

---

## Step 1 — Read assignment, cells file, column titles
Hypothesis: my 6 cells are tab-separated COLUMN_ROMAN, ROW_LABEL, LINE_REF,
all in column XLVII.
Method: read the shares file and COLUMN-TITLES.md.
Observation: file lists XLVII/32 bis (line 1054), XLVII/31 bis (1055),
XLVII/17 (1091), XLVII/22 (1096), XLVII/25 (1099), XLVII/26 (1100).
COLUMN-TITLES.md maps XLV–XLVII to "Magical Powers [Western] / System of Taoism
(line ~952)" — need source verification since XLVII's title may differ.
Result: proceed to source.

## Step 2 — Identify the column in the source
Hypothesis: COLUMN-TITLES.md's XLV–XLVII note is imprecise; read the source
header directly.
Method: read ~/workspace/liber777/777-crowley.txt around lines 940–1060.
Observation: at line ~1008 the header reads: "XLVII. / Kings and Princes of /
the Jinn." — flanked by XLVIII "Figures related to Pure Number." and XLIX
"Lineal Figures of the Planets, &c., and Geomany." So XLVII = "Kings and
Princes of the Jinn." — the COLUMN-TITLES.md line ~952 note covers the
XLIV–XLVI table; XLVII belongs to the next table (line ~1008). The quick
reference was coarse; the source header rules.
Result: column_title = "Kings and Princes of the Jinn."

## Step 3 — Verify each cell is actually empty; pin the real line numbers
Hypothesis: the shares file's LINE_REF values are the ground truth.
Method: grep line numbers for each row's XLVII content; compare against
the shares file.
Observation:
- "32 bis" XLVII dots: line 1054 ✓ matches shares file.
- "31 bis" XLVII dots: line 1055 ✓ matches shares file.
- Row 17 XLVII: line 1038 (shares file said 1091 — STALE/WRONG). Row 17
  line: `      17                     Swastika                                 Albus *`
- Row 22 XLVII: line 1043 (shares said 1096 — wrong). Line:
  `      22                     Greek Cross Solid, the Rose (3 + 7 + 12) Puella`
- Row 25 XLVII: line 1046 (shares said 1099 — wrong). Line:
  `      25                     The Rose (5 x 5)                         Acquisitio *`
- Row 26 XLVII: line 1047 (shares said 1100 — wrong). Line:
  `      26                     Calvary Cross of 10, Solid               Carcer *`
Result: the row labels are correct; four of six LINE_REFs in the shares
file point into the wrong table (the L/LI table starting line ~1062). The
cells are the same cells; line refs corrected to 1038/1043/1046/1047.
Logged the discrepancy honestly — did not trust the refs blindly.

## Step 4 — Resolve the column-alignment ambiguity (CRITICAL)
Hypothesis: rows 17/22/25/26 have content ("Swastika" etc.) — is that
XLVII content or XLVIII content? The shares file claims these XLVII cells
are empty dot-runs.
Method: measure exact start columns with cat -A; compare header start
positions (XLVII "Kings and Princes of" begins col 8; XLVIII "Figures
related to Pure Number." begins col 33; XLIX header begins col 64).
Observation:
- Row 0: `  0    . . . . . . . . . . . . . . . . . . . . . . . . . . . . The Circle`
  — dots run cols 7–~61 (spans XLVII+XLVIII both empty), "The Circle" col ~64 (XLIX).
- Row 2: `. . . . . . . . . . The Cross` — dots cols 7–25 (XLVII empty),
  "The Cross" starts col 26. Row 3: same pattern, "The Triangle" col 26.
- Rows 4–9, 12–13, 17, 22, 25, 26: NO dots; whitespace cols 7–25, then
  content at col 26: "Tetrahedron or  Pyramid, Cross", "The Rose",
  "Calvary Cross...", "Swastika", "Greek Cross Solid, the Rose (3 + 7 + 12)",
  "The Rose (5 x 5)", "Calvary Cross of 10, Solid".
- Row 1: dots cols 7–61, "The Point" col ~64.
Interpretation decision: the col-26 content belongs to XLVIII ("Figures
related to Pure Number") — semantically airtight: Tetrahedron, Rose,
Calvary Cross, Swastika, Greek Cross, Pentagon-type figures are all
geometric/pure-number figures; XLIX holds the geomantic figures
(Circle, Point, Line, Plane, Solid Figure, Tesseract, Albus, Populus,
Via, Fortuna Major/Minor, Conjunctio, Puella, Rubeus, Acquisitio, Carcer,
Pentagram, Tristitia, Laetitia, Hexagram, Triangle, Ey Triplicity...).
"Kings and Princes of the Jinn" with entries like "Swastika" or
"The Rose (5 x 5)" would be nonsense; as XLVIII entries they are perfect.
Also rows 0,1: XLVIII empty (dots) is consistent — above-the-tree rows
have no pure-number figure except row 2's Cross, row 3's Triangle.
Result: XLVII (Kings and Princes of the Jinn) is EMPTY in every row —
0 through 32, 32 bis, 31 bis. The shares file's claim of empty XLVII
cells stands, confirmed by alignment analysis, not just by the dots.
All 6 cells verified empty. NOTABLE: Crowley never filled this column
at all. It is not "row 0 blank by design" — the whole column is blank.

## Step 5 — INTENTIONALLY EMPTY check
Hypothesis: maybe Crowley deliberately left the Jinn column blank
(e.g., as a blind, or because the attribution was genuinely unknown).
Method: reason from the column's nature and Crowley's habits.
Observation: Crowley DOES fill parallel spirit-hierarchy columns
elsewhere (e.g., Goetic orders, archangels, angels of the Sephiroth).
"Kings and Princes of the Jinn" is a coherent magical category (Islamic
jinn lore has named kings/princes), and Crowley cites Arabic magical
sources elsewhere (Picatrix = Ghayat al-Hakim). A full-column blank
across all 36 rows (incl. 0, where a blank IS by design) reads as
"never got to it / source not at hand" rather than a deliberate blind —
he usually marks impossibility ("[[No attribution possible]]" appears
elsewhere in this very file, e.g., line ~941 "31 bis [[No attribution
possible]]"). He did NOT mark this column that way, so it is an open
gap, not a ruled-out one.
Result: NOT intentionally empty. Propose fillings; flag as PONTIFEX-proposed.

## Step 6 — Calibrate the weighing engine
Hypothesis: ptk.weigh.calibrate() must pass before any weighing.
Method: `from weigh import calibrate; calibrate()` → True.
Result: pass. Engine trusted for this run.

## Step 7 — Choose the candidate set (research)
Hypothesis: the strongest attested source for "Kings and Princes of the
Jinn" is the Islamic magical tradition's Seven Kings of the Jinn
(الملوك السبعة), one per day/planet: al-Mudhhib (Sun), Murrah (Moon),
al-Ahmar (Mars), Barqan (Mercury), Shamhurish (Jupiter), al-Abyad (Venus),
Maymun (Saturn). Attested in Shams al-Ma'arif (al-Buni) and the
Ghayat al-Hakim / Picatrix milieu that Crowley demonstrably used.
Method: web-search to verify the seven-kings list and spellings before
weighing anything; verify the planetary/day mapping.
(pending — next step)

## Step 8 — Map candidates to my rows
Hypothesis (to verify against row meanings):
- Row 17 = path of Zain, Gemini, Mercury → jinn king of Mercury: BARQAN برقان
- Row 22 = path of Lamed, Libra, Venus → jinn king of Venus: AL-ABYAD الأبيض
- Row 25 = path of Samekh, Sagittarius, Jupiter → jinn king of Jupiter: SHAMHURISH شمهورش
- Row 26 = path of Ayin, Capricorn, Saturn → jinn king of Saturn: MAYMUN ميمون
- 31 bis = Earth, 32 bis = Spirit: no planetary king applies. Candidates
  needed from the same tradition or marked as derived/constructed.
(pending research)

## Step 9 — Weigh candidates
Method: ptk arabic() on the Arabic spellings (attested spellings =
attested tier for the NAME; the WEIGHING of an attested name is
attested-tier value); breakdown() each; unknown() check every time.
Also record Latin transliteration English-ordinal values (native for
English words = derived tier, honest single-bank values; Latin≡English
is ONE bank, never a bridge).
(pending)

## Step 7 — Research the candidate tradition
Hypothesis: "Kings and Princes of the Jinn" = the Seven Kings of the Jinn
(الملوك السبعة) of the Arabic magical tradition (Shams al-Ma'arif of
al-Buni; Sihr Muluk al-Jinn; Kitab al-Bulhan; the Picatrix's "Seven Kings
of the Air" as the Latin echo) — the tradition Crowley demonstrably drew
on, and the only named king-and-prince hierarchy of the jinn with
planetary attributions.
Method: two web searches; cross-checked three independent summaries.
Observation: the seven kings, one per day/planet, confirmed across sources:
Sun–al-Mudhhib (المذهب), Moon–al-Abyad (الابيض), Mars–al-Ahmar (الاحمر),
Mercury–Barqan (برقان, var. بورقان), Jupiter–Shamhurish (شمهورش),
Venus–Zawba'ah (زوبعة), Saturn–Maymun (ميمون). Kitab al-Bulhan agrees on
Tuesday/Red, Thursday/Shamhurash, Friday/Zawba'a, Saturday/Maymun, but
gives Wednesday as the "Black King" (al-malik al-aswad) instead of Barqan
— a genuine tradition-variant, recorded as an alternate proposal, not
smoothed over. One video source reassigns the White King to Friday; the
Bulhan + fandom agreement (Friday = Zawba'a) outranks it; noted in CSV.
Result: candidate set fixed; variants kept visible.

## Step 8 — Row meanings verified in the source
Hypothesis: rows 17/22/25/26 are the Mercury/Venus/Jupiter/Saturn letter-paths.
Method: read the source's own letter column (lines 230–252) and zodiac
column (lines 284–298).
Observation: 17 = Zain (Sword), Gemini; 22 = Lamed (Ox-goad), Libra;
25 = Samekh (Prop), Sagittarius; 26 = Ayin (Eye), Capricorn;
31 bis = Ath, Spirit; 32 bis = Aretz, Earth (lines 302–303, 625–626, 1177–1178).
Zodiac→planet via the standard GD attributions Crowley uses throughout
(Gemini–Mercury, Libra–Venus, Sagittarius–Jupiter, Capricorn–Saturn).
Result: mapping Mercury→Barqan, Venus→Zawba'ah, Jupiter→Shamhurish,
Saturn→Maymun. For Spirit (31 bis): JANN (جان), the primordial jinn of
Qur'an 15:27 — attested name, derived mapping. For Earth (32 bis): the
seven-kings tradition names no earth-king; AMAIMON proposed instead —
attested king of the earth quarter in the Goetia/Pseudomonarchia
tradition (cf. source line 1212: "32 bis … Nephesh Amaimon"), with the
cross-tradition nature flagged honestly in notes.

## Step 9 — Weigh every candidate
Hypothesis: ptk arabic() for the Arabic names; latin() (ordinal, native for
Latin script) and agrippa() for the transliterations and Amaimon.
Method: weigh.py convenience functions; unknown() audited on every word;
breakdown() recorded. First attempt crashed: weigh(word, "arabic") takes a
bank OBJECT, not a string — read the source, corrected to arabic(word) /
unknown(word, ARABIC_ABJAD). Dead end logged, lesson kept.
Observation:
- BARQAN برقان = 353, clean (ب2 ر200 ق100 ا1 ن50). Variant بورقان = 359, clean.
- ZAWBAAH زوبعة = 85 with ة SKIPPED by the bank (visible in unknown());
  conventional ta-marbuta=5 gives 90 — reported as spread, not silently adjusted.
- SHAMHURISH شمهورش = 851, clean.
- MAYMUN ميمون = 146, clean.
- JANN جان = 54, clean.
- AL-MALIK AL-ASWAD الملك الاسود = 223, clean (first attempt had an
  alif-with-hamza أ skipped; re-weighed with plain alifs, only space skipped).
- Latin ordinals: BARQAN 53, ZAWBAAH 62, SHAMHURISH 124, MAYMUN 87, JANN 39,
  AMAIMON 66. Agrippa: 194, 513, 524, 701, 90, 161.
Result: no two honest banks agree on any single number for any word —
NO BRIDGES claimed. Latin≡English ordinal counted as one bank throughout.
Single-bank values reported as spreads. Nothing forced; nothing chance-flagged
beyond the visible ة adjustment.

## Step 10 — INTENTIONALLY_EMPTY re-check per cell
All six cells proposed with fillings (the column is an open gap, not a
ruled-out one — Crowley never marked it "no attribution possible").
proposal=INTENTIONALLY_EMPTY used nowhere; every proposal carries the
PONTIFEX-proposed flag and its tier.

## Step 11 — Correction received from worker-01 (column identity)
A follow-up confirmed: XLVII = "Kings and Princes of the Jinn", not the
Taoism column; the geometric names in the visual block are XLVIII ("Figures
related to Pure Number"), gutters verified line by line. This matches my
independent Step 2/Step 4 findings exactly (source header at line ~1008;
col-26 content = XLVIII by alignment + semantics). No rework needed;
the correction is corroboration, logged here.
