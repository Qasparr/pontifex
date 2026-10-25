# SANSKRIT — PONTIFEX worker #9 of 12

**Status: research draft for Johnathan's red pen. Findings, never doctrine. This research decrees no bridge.**

---

## 1. The Katapayadi system, documented faithfully

### 1.1 What it is
The Katapayadi (kā-ṭa-pa-yādi) system is an ancient Indian alphabetical numeral notation in which **consonants stand for decimal digits**, so that numbers can be encoded inside pronounceable Sanskrit words and verses. The name itself is the rule: the system begins with the letters **ka, ṭa, pa, ya**, each standing for the digit **1**. It is a **positional digit encoding**, not a letter-sum gematria. This distinction is load-bearing for everything below.

### 1.2 The defining rule, in the tradition's own words
The mechanism is given in verse form in Śaṅkaravarman's *Sadratnamālā* (1819 CE):

> *ñayāvacas ca śūnyāni saṅkhyāḥ kaṭapayādayaḥ / miśre tūpāntyahal saṅkhyā na ca cintyo halasvaraḥ //*

Translation: "**na** (न), **ña** (ञ) and the **a**s, i.e. vowels, represent **zero**. The nine integers are represented by the consonant groups beginning with **ka**, **ṭa**, **pa**, **ya**. In a conjunct consonant, **only the last of the consonants counts**. A consonant without a vowel is to be **ignored**."

A shorter anonymous formulation runs: *"kadi nava, ṭadi nava, padi pañca, yady aṣṭau"* — the nine consonants starting with ka, the nine starting with ṭa, the five starting with pa, and the eight starting with ya [respectively denote the numbers 1 to 9].

### 1.3 The full consonant→digit mapping

| Digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| ka-group | क ka | ख kha | ग ga | घ gha | ङ ṅa | च ca | छ cha | ज ja | झ jha | ञ ña |
| ṭa-group | ट ṭa | ठ ṭha | ड ḍa | ढ ḍha | ण ṇa | त ta | थ tha | द da | ध dha | न na |
| pa-group | प pa | फ pha | ब ba | भ bha | म ma | – | – | – | – | – |
| ya-group | य ya | र ra | ल la | व va | श śa | ष ṣa | स sa | ह ha | – | – |

Digit 0 is given by na, ña, and standalone vowels (per the *Sadratnamālā*).

### 1.4 The operating rules (all attested)
1. **Vowels carry no digit value of their own.** Śaṅkaravarman assigns standalone vowels zero; other scholarly formulations (e.g. Kim Plofker's description, and the *Mahāsiddhānta* variant below) treat vowels as having no numerical significance at all. Both are recorded in this research; the difference matters for initial-vowel words (see §5).
2. **In a conjunct (saṁyoga), only the last consonant — the one bearing the vowel — counts.** Example: *kya* (k + ya + a) = 1 (ya alone).
3. **A consonant not followed by a vowel (halant/final) is ignored** — including visarga and anusvāra.
4. **Digits are read right-to-left**: *"aṅkānāṁ vāmato gatiḥ"* — numbers run leftward, i.e. the first consonant of the string is the units (least significant) digit. The standard worked example: *bhavati* decodes as the digit sequence 4-4-6, implying the number **644**.
5. **No decimal separator** can be represented.

### 1.5 Attested variant: Āryabhaṭa II's reform (ca. 950 CE)
In his astronomical *Mahāsiddhānta*, Āryabhaṭa II defines a modified version with the same consonant values but three changes: (i) **vowels have no numerical significance even standing alone**; (ii) **every member of a conjunct counts**, not just the last; (iii) **digits are read left-to-right** as the text runs. Because his expressions were not required to form meaningful words, they come out as unpronounceable jumbles. This variant is included here because it is the scholarly source of the "vowels have no value" reading — and it demonstrates that even within the tradition, the vowel rule was not unanimous. It is **not** used as the primary reading in this report; it appears only as a sensitivity note (§5).

### 1.6 Actual historical use
- The system underlies the **vākya ("sentence") genre** of Kerala astronomical texts, where planetary positions at regular intervals were encoded in katapayadi sentences. The earliest such work traditionally cited is the **Candra-vākyāni ("Moon-sentences") of Vararuci** (traditionally 4th century CE, though the date is doubted by scholars).
- The famous devotional-mathematical verse beginning *"gopī bhāgya madhuvrāta…"* encodes π to 31 decimal places (31415926535897932384626433832792) — the classic demonstration that the system was built for **embedding large numbers inside meaningful verse**, not for summing letter-values of words.
- Pali chronograms in the system have been found in Burma; degree-markings on a Sanskrit astrolabe in Varanasi use it. The system was a **mnemonic/encoding technology for numbers**, full stop.

### 1.7 Sources consulted
- **Śaṅkaravarman, *Sadratnamālā* (1819)** — the defining verse, via the Wikipedia article "Katapayadi system" (https://en.wikipedia.org/wiki/Katapayadi_system), which quotes and translates it.
- **S. R. Sarma, "The Katapayadi System of Numerical Notation"** (*Revue d'Histoire des Mathématiques* 18.1, 2012, pp. 37–66) — the modern scholarly survey: anonymous rule-verses, the Kerala vākya genre, Āryabhaṭa II's modified version, manuscript evidence in Orissa, the Burma Pali chronograms. Mirrors: https://sup1vyvpyr1prllo.vchorizon.xyz/pdf/articles/2012_Katapayadi_System.pdf and http://www.numdam.org/item/RHM_2012__18_1_37_0.pdf
- **J. F. Fleet, "The Katapayadi System of Expressing Numbers"** (*JRAS*, July 1911, pp. 788–794) — rules including the halant/final-consonant rule and right-to-left reading, via the Scribd-hosted summary document.
- **Kim Plofker (via secondary summary)** — the "consonants mapped to decimal digits; vowels have no numerical significance; only a consonant immediately followed by a vowel has value; numbers read starting with the least significant digit; *bhavati* → 4-4-6 → 644" formulation.
- **HinduFAQs, "Was first discovered by Hindus Ep II: Value of Pi"** (https://www.hindufaqs.com/first-discovered-hindus-ep-ii-value-pi/) — the π-verse demonstration and the "kapa, tapa, papa, yapa all mean 11" observation (relevant: 11 is trivially encodable in the system, but our corpus produces it only by coincidence — see §6).

### 1.8 The category verdict (binding)
The Katapayadi system is **ATTESTED** as a positional digit-encoding scheme for numbers in verse. **Applying it as a word-sum for gematria comparison is a category stretch** — the tradition never used it that way; it used it in the opposite direction (author starts from a *number* and *chooses* a word that encodes it). Every value in column (a) of the table below therefore carries the tier **"ATTESTED system; CONSTRUCTED application as word-value"**. This research neither hides nor softens that.

---

## 2. Transliteration record (ISO 15919-informed)

Every corpus term was carried Latin → Devanagari mechanically, distinguishing dental/aspirate/retroflex per ISO 15919 (TH→थ, T→त, D→द). Ambiguities and loan letters are called out per term; the chosen resolution is recorded, and the rejected variant is named, so the red pen can see exactly where the number could move.

| # | Term | Devanagari | Aksara breakdown (consonants + vowel) | Normalization choices |
|---|---|---|---|---|
| 1 | AXONEME | अक्षोनेमे | a · k+ṣ+o · n+e · m+e | X→क्ष (kṣa conjunct) is the standard Indic convention for X; in katapayadi only the last conjunct member (ष=6) counts, so the क- is invisible to column (a). |
| 2 | OZ | ओज़ | o · z'(loan) | Z→ज़ (nuqta loan letter); NOT in the classical table — unmappable in (a). Variant ओज (z→j) would read 80. |
| 3 | TRVVTH | त्रव्वथ | t+r+a · v+v+a · th+a | TR→त्र conjunct, VV→व्व geminate, TH→थ (dental aspirate), T→त. |
| 4 | THELEMA | थेलेमा | th+e · l+e · m+ā | TH→थ aspirate dental; mechanical syllabification. |
| 5 | AGAPE | अगापे | a · g+ā · p+e | G→ग unaspirated velar; mechanical. |
| 6 | BABALON | बाबालोन् | b+ā · b+ā · l+o · n(halant) | Final न् (no vowel) IGNORED in (a) per *Sadratnamālā*; counted bare in (b) — a recorded normalization fork. |
| 7 | HERU-RA-HA | हेरु-रा-हा | h+e · r+u · r+ā · h+ā | Hyphens dropped as value-less separators. |
| 8 | ABRAHADABRA | अब्राहादाब्रा | a · b+r+ā · h+ā · d+ā · b+r+ā | BR→ब्र conjuncts: only र=2 counts in (a); the ब- vanishes. |
| 9 | QIRA | किरा | k+i · r+ā | Q→क is the canonical Sanskritization; क़िरा (nuqta) would be equally defensible — recorded. |
| 10 | LIBERTY | लिबेर्टी | l+i · b+e · r+t+y+ī | RTY→र्त्य conjunct (only य=1 counts in (a); र,त lost). Variant लिबेरतय (no conjunct) would read 16233 — normalization moves the number hard. |
| 11 | CELL | चेल्ल | c+e · l+l+a | C→च is letter-by-letter; phonetic English /s/ would give सेल (s=7) — variant recorded; geminate ल्ल counts once in (a). |

---

## 3. Column (a) — Katapayadi READINGS (positional, not sums)

Reading rule: digit per aksara (last conjunct member; vowel-only → 0 per *Sadratnamālā*; halant → ignored; loan letters → unmappable, dropped); the digit string is read **right-to-left**, first aksara = units. **Each result is a positional number — the number the word would encode — not a letter-sum.** Provenance tier: **ATTESTED system; CONSTRUCTED application.**

| Term | Devanagari | Digit trace (first = units) | Reading | Loss/mergers in this term |
|---|---|---|---|---|
| AXONEME | अक्षोनेमे | 0·6·0·5 | **5060** | क of क्ष invisible (conjunct last-only rule) |
| OZ | ओज़ | 0·(unmappable) | **0 — DEGENERATE** | ज़ has no classical value; term is a vowel + an unmappable loan letter. Pure information loss. |
| TRVVTH | त्रव्वथ | 2·4·7 | **742** | त of त्र, first व of व्व invisible |
| THELEMA | थेलेमा | 7·3·5 | **537** | none |
| AGAPE | अगापे | 0·3·1 | **130** | initial अ contributes a 0 units digit (see §5) |
| BABALON | बाबालोन् | 3·3·3 | **333** | final न् ignored (halant rule) |
| HERU-RA-HA | हेरु-रा-हा | 8·2·2·8 | **8228** | none |
| ABRAHADABRA | अब्राहादाब्रा | 0·2·8·8·2 | **28820** | both ब of the ब्र conjuncts invisible |
| QIRA | किरा | 1·2 | **21** | none |
| LIBERTY | लिबेर्टी | 3·3·1 | **133** | र,त of र्त्य invisible |
| CELL | चेल्ल | 6·3 | **36** | geminate ल counted once |

Worked example for the headline term (HERU-RA-HA → 8228): हेरु = h(ह=8) + ru(र=2); रा = r(र=2); हा = h(ह=8). Digit sequence in order: 8, 2, 2, 8. Right-to-left: 8228.

---

## 4. Column (b) — Devanagari canonical-ordinal SUMS (CONSTRUCTED)

Each letter takes its position in the traditional varṇamālā order: vowels अ=1 … अः=16; consonants क=17 … ह=49 (14 + 35 = 49 positions; conjunct members counted separately; vowels counted once per aksara; bare halant consonants counted without vowel; loan letters take their base consonant's ordinal). **This column has no traditional warrant — it is an invented comparison instrument, labeled CONSTRUCTED throughout the CSV.**

| Term | Devanagari | Sum trace | Sum (CONSTRUCTED) |
|---|---|---|---|
| AXONEME | अक्षोनेमे | a=1 · k=17+ṣ=47+o=13 · n=36+e=11 · m=41+e=11 | **177** |
| OZ | ओज़ | o=13 · z'→j=24 | **37** |
| TRVVTH | त्रव्वथ | t=32+r=43+a=1 · v=45+v=45+a=1 · th=33+a=1 | **201** |
| THELEMA | थेलेमा | th=33+e=11 · l=44+e=11 · m=41+ā=2 | **142** |
| AGAPE | अगापे | a=1 · g=19+ā=2 · p=37+e=11 | **70** |
| BABALON | बाबालोन् | b=39+ā=2 · b=39+ā=2 · l=44+o=13 · n=36 | **175** |
| HERU-RA-HA | हेरु-रा-हा | h=49+e=11 · r=43+u=5 · r=43+ā=2 · h=49+ā=2 | **204** |
| ABRAHADABRA | अब्राहादाब्रा | a=1 · b=39+r=43+ā=2 · h=49+ā=2 · d=34+ā=2 · b=39+r=43+ā=2 | **256** |
| QIRA | किरा | k=17+i=3 · r=43+ā=2 | **65** |
| LIBERTY | लिबेर्टी | l=44+i=3 · b=39+e=11 · r=43+t=32+y=42+ī=4 | **218** |
| CELL | चेल्ल | c=22+e=11 · l=44+l=44+a=1 | **122** |

---

## 5. Collisions, information loss, and normalization forks

1. **Conjunct invisibility.** Katapayadi's last-member rule erases consonants systematically: AXONEME loses क (reading would be identical for "अषोनेमे"); ABRAHADABRA's ब्र conjuncts make the word read as if spelled "अराहादारा". Any transliteration that introduces or removes a conjunct changes the number — LIBERTY reads **133** with the र्त्य conjunct but **16233** without it (र=2, त=6, य=1 as separate aksaras). The number is a function of the transliteration, not of the word.
2. **The vowel-zero fork.** Per the *Sadratnamālā*, initial अ/ओ contribute a 0 digit: AXONEME = 5060, AGAPE = 130, ABRAHADABRA = 28820. Under the Plofker/Āryabhaṭa-II "vowels have no value" reading, the initial vowel drops out: AXONEME = 506, AGAPE = 13, ABRAHADABRA = 2882. The primary column follows the *Sadratnamālā*; the fork is recorded, not hidden.
3. **OZ is degenerate.** ओज़ = a standalone vowel (0) plus a Perso-Arabic loan letter the classical table never knew. The reading collapses to 0 — not a finding about "Oz" but a demonstration that the system cannot see foreign phonemes. The Sanskritized variant ओज would read 80. Either way: no bridge, and the reason is structural.
4. **CELL's C.** Letter-by-letter C→च gives reading 36; phonetic English /s/ (सेल) would give स=7 as first digit → 76. Noted because 76 sits next to the 77 target without touching it — a near-miss worth one honest line and no more.
5. **QIRA's Q.** क vs क़ is a coin-flip with no effect here (both would resolve to the k-series in any honest treatment), but the choice is recorded because it matters in principle.
6. **Column (b) is order-fiction.** The varṇamālā order is real; treating position as value is not traditional. It exists only so the parent synthesis can see what a naive sum does — and what it does is scatter (65–256, no target contact).

---

## 6. Target-number assessment — the honest negative

Targets: **418, 666, 777, 93, 77, 11.**

- **Column (a) readings:** 5060, 0, 742, 537, 130, 333, 8228, 28820, 21, 133, 36. **No target hit.**
- **Column (b) sums:** 177, 37, 201, 142, 70, 175, 204, 256, 65, 218, 122. **No target hit.**
- Closest brushes, reported at face value and no further: AXONEME sums to **177** in column (b) — the digits of 77 appear, but 177 ≠ 77 and it is a constructed column; CELL would read **76** under the सेल variant — adjacent to 77, not 77. The famous "kapa/tapa/papa/yapa = 11" shows the system *can* encode 11, but no corpus term does.

**Verdict: no meaningful meeting in either column.** The expected finding — "no meaningful meeting" — is what the numbers say, and it is a finding, not a failure: it is consistent with the category analysis in §1.8. Katapayadi encodes numbers into chosen words; it does not reveal numbers hidden in words. Running it backwards as a word-value oracle is the constructed move, and the oracle answers: nothing on this corpus touches 418, 666, 777, 93, 77, or 11. A palindromic curiosity (HERU-RA-HA → 8228) and a triple (BABALON → 333) are pattern-noticings, not bridges — filed as observations for the red pen, weighted at zero doctrinally.

---

## 7. Ultra-verbose work log

**Step 1 — Hypothesis:** Katapayadi might offer an attested Sanskrit-bank numeral system, avoiding an invented letter-sum. **Method:** web search for scholarly documentation of the mapping, vowel rule, reading direction, and historical use. **Observation:** Two independent source families (Wikipedia quoting the *Sadratnamālā* verse; Sarma 2012's survey via the srsarma.in/numdam mirrors; Fleet 1911 via Scribd; Plofker's summary formulation; the π-verse via HinduFAQs) agree on the table, the conjunct rule, the halant rule, and right-to-left reading — with one genuine fork: Śaṅkaravarman gives standalone vowels zero; Plofker/Āryabhaṭa II give them no value. **Result:** documented faithfully with both readings; chose *Sadratnamālā* as primary, fork recorded. **What it taught:** the vowel rule is the one place scholarly formulations diverge, and it moves three of our eleven numbers — so it had to be surfaced, not smoothed.

**Step 2 — Hypothesis:** mechanical ISO 15919-informed transliteration would be unambiguous. **Method:** hand-built the aksara breakdown per term, recording each ambiguous Latin→Devanagari choice (X→क्ष, Z→ज़, TH→थ, Q→क, C→च, RTY→र्त्य). **Observation:** ambiguity is everywhere a Latin word meets Devanagari — loan letters (Q, Z) and English phonetics (CELL's C) have no single right answer. **Result:** every choice recorded with its rejected variant and the number the variant would produce. **What it taught:** for katapayadi, the transliteration IS the number — LIBERTY swings from 133 to 16233 on the conjunct decision alone. A bridge built on this would be a bridge built on sand; saying so is the category-honest move.

**Step 3 — Hypothesis:** a script would compute both columns reproducibly. **Method:** wrote `build_sanskrit.py` in his thelemic/educational code convention, implementing the katapayadi rules (conjunct last-only, halant ignored, vowel→0, right-to-left) and the constructed ordinal sum. **Observation (dead end #1):** first run died with a `NameError` in the mergers-logging comprehension (stale variable name from a rewrite). **Result:** fixed, re-ran. **What it taught:** the verbose trace logging paid for itself immediately — the trace showed the bug's neighborhood before the traceback did.

**Step 4 — Hypothesis:** my hand-computed readings were right. **Method:** compared hand notes against script output. **Observation (dead end #2):** I had hand-computed AXONEME as 506 and ABRAHADABRA as 2882 — the script said 5060 and 28820. I was wrong: I had silently dropped the initial-vowel zero digit, i.e. I had applied the "vowels have no value" rule while claiming the *Sadratnamālā* rule. **Result:** script correct; hand notes corrected; the fork documented explicitly in §5.2. **What it taught:** the exact failure mode the doctrine warns about — an unexamined normalization silently moving the number. Caught by the trace, owned plainly.

**Step 5 — Hypothesis:** the OZ row might need special-casing. **Method:** inspected the CSV's `mergers_or_loss` field for OZ and BABALON. **Observation (dead end #3):** the halant-detection predicate misfired on OZ's z' (vowel=None means "loan letter," not "halant") — OZ was labeled as having a halant consonant it doesn't have. **Result:** predicate refined to exclude loan-letter codes; re-ran; both rows now describe themselves accurately. **What it taught:** loan letters and halants are different kinds of absence (unmappable vs. ignored) and the ledger must not conflate them.

**Step 6 — Hypothesis:** a target might be hit somewhere. **Method:** programmatic check of all 22 values against {418, 666, 777, 93, 77, 11}. **Observation:** zero hits in either column. **Result:** the negative is the finding; the two nearest brushes (177, variant-76) reported at face value with explicit non-bridge framing. **What it taught:** nothing new — the category analysis in §1.8 already predicted that a backwards-run encoding oracle would answer in noise. The discipline is in writing the noise down anyway, at full weight.

---

## Files

- [sanskrit-values.csv](sandbox://workspace/pontifex/research/twelve-tongues/sanskrit-values.csv) — 22 rows (11 terms × 2 columns), schema: term, language, script_form, transliteration_convention, table_used, provenance_tier, value, mergers_or_loss, notes
- [build_sanskrit.py](sandbox://workspace/pontifex/research/twelve-tongues/build_sanskrit.py) — computation engine + ultra-verbose log, written in his thelemic/educational code convention
- No git push performed (drafts for his red pen, per task).

---

*Love is the law, love under will.*
