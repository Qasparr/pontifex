# The Chinese Bank — twelve-tongues research, worker #12 (CHINESE)

*DRAFT FOR THE AUTHOR'S RED PEN. Not pushed. Every value CONSTRUCTED —
hypotheses, never doctrine. This research decrees no bridge.*

**Worker:** #12 of 12 (CHINESE) · **Date:** 2026-10-11 · **Corpus:** AXONEME,
OZ, TRVVTH, THELEMA, AGAPE, BABALON, HERU-RA-HA, ABRAHADABRA, QIRA, LIBERTY,
CELL · **Targets:** 418, 666, 777, 93, 77, 11

**Governing doctrine** (his, settled 2026-10-07): each word weighed in its own
tongue, but ONLY where the tongue has an honest letter-number tradition; the
audit flag — stroke-count divination claims (姓名学 / seimei-handan practice)
are UNAUDITED and treated with FULL SKEPTICISM; METHOD.md §5 — "CJK ordering
is arbitrary-in. Stroke count, pinyin, radical — every choice bakes in an
assumption. Any CJK table is CONSTRUCTED with its ordering choice stated."

**Scripts:** `chinese_weigh.py` (thelemic-formatted, MECHANISM/DOCTRINE
comments) generates `chinese-values.csv` (22 rows: 11 terms × 2 methods).

---

## 1. Character selection — the crux, fully documented

There is no established Chinese "spelling" of most corpus terms, so the
selection below IS the weighing. Each entry states what convention was used:
*established* (a rendering with real currency) or *scribe's own* (my phonetic
choice). Pinyin via pypinyin (machine), tones stripped.

| Term | Characters | Pinyin | Convention | Rationale |
|------|-----------|--------|------------|-----------|
| AXONEME | 阿克索尼姆 | a ke suo ni mu | **scribe phonetic** | No established rendering exists. Five syllables for ak-so-ne-me, standard transliteration characters. |
| OZ | 奥兹 | ao zi | **scribe phonetic** | Common phonetic choice for "Oz" in Chinese popular use; no thelemic-standard rendering of Liber Oz found. |
| TRVVTH | 真理 | zhen li | **established semantic** | The standard dictionary translation of "truth". |
| THELEMA | 泰勒玛 | tai le ma | **established phonetic** | The rendering used in Chinese thelemic materials (泰勒瑪 traditional). |
| AGAPE | 阿加佩 | a jia pei | **established phonetic** | The phonetic used in Chinese theological writing for agape-love. |
| BABALON | 巴巴隆 | ba ba long | **scribe phonetic** | Chosen to preserve Crowley's distinct *-lon* ending, set apart from 巴比伦 — the established standard for "Babylon". |
| HERU-RA-HA | 赫鲁拉哈 | he lu la ha | **scribe phonetic** | No established rendering; four syllables he-ru-la-ha. |
| ABRAHADABRA | 阿布拉哈达布拉 | a bu la ha da bu la | **scribe phonetic** | No established rendering; syllable-by-syllable a-bra-ha-dab-ra. |
| QIRA | 奇拉 | qi la | **scribe phonetic** | No established rendering. 契拉 was considered and rejected (see §5). |
| LIBERTY | 自由 | zi you | **established semantic** | The standard translation of "liberty". |
| CELL | 细胞 | xi bao | **established semantic** | The standard translation of "cell". |

**Pinyin correction, recorded:** pypinyin read 勒 in 泰勒玛 as *lēi*
("strangle"); the transliteration intends *lè*. The script logs the raw
machine output and applies the scribe's correction explicitly — the override
is visible in `chinese_weigh.py`, not hidden. This is itself an arbitrariness
data point: even the machine step needs a human adjudication.

---

## 2. Column A — stroke-count weighing (CONSTRUCTED)

**Standard stated:** PRC simplified stroke counts, Xinhua-dictionary style
(the counts used in mainland printed references). Three counts web-verified
against Xinhua-dictionary sources on 2026-10-11: 奥=12 (总笔画十二画),
索=10, 佩=8. The rest are standard reference values; spot-anchors (自由=11,
真理=21) are among the best-known counts in the language.

| Term | Characters | Stroke detail | Sum |
|------|-----------|---------------|-----|
| AXONEME | 阿克索尼姆 | 7+7+10+5+8 | **37** |
| OZ | 奥兹 | 12+9 | **21** |
| TRVVTH | 真理 | 10+11 | **21** |
| THELEMA | 泰勒玛 | 10+11+7 | **28** |
| AGAPE | 阿加佩 | 7+5+8 | **20** |
| BABALON | 巴巴隆 | 4+4+11 | **19** |
| HERU-RA-HA | 赫鲁拉哈 | 14+12+8+9 | **43** |
| ABRAHADABRA | 阿布拉哈达布拉 | 7+5+8+9+6+5+8 | **48** |
| QIRA | 奇拉 | 8+8 | **16** |
| LIBERTY | 自由 | 6+5 | **11** ← target number |
| CELL | 细胞 | 8+9 | **17** |

**The standard alone moves the numbers.** Under Kangxi counts the differing
terms would read: OZ 22 (奧=13), THELEMA 35 (瑪=14), HERU-RA-HA 46 (魯=15),
ABRAHADABRA 58 (達=16), CELL 20 (細=11); the rest unchanged. That is a second
arbitrariness axis, independent of character choice.

**Tier:** CONSTRUCTED. Nothing here is attested (see §4).

---

## 3. Column B — pinyin → Hebrew fallback (CONSTRUCTED)

**Chain, fully stated:** characters → pinyin (pypinyin, toneless, lowercase,
syllables concatenated) → repo `LATIN_TO_HEBREW` map with greedy digraphs
(ch→ח, sh→ש, th→ת; the map's 'x'→'קס' expanded to both letters) → mispar
hechrechi from the repo's `HEBREW` table. Mergers reported only on **actual
loss** (two or more distinct source letters present that collapse to one
Hebrew letter), per the repo's `MERGERS` map.

| Term | Pinyin string | Hebrew | Value | Mergers actually fired |
|------|--------------|--------|-------|------------------------|
| AXONEME | akesuonimu | אכהסוונימו | **204** | ו (u+o collapsed) |
| OZ | aozi | אוזי | **24** | none |
| TRVVTH | zhenli | זההנלי | **107** | ה (e+h collapsed) |
| THELEMA | tailema | תאילהמא | **487** | none |
| AGAPE | ajiapei | אייאפהי | **117** | י (j+i collapsed) |
| BABALON | babalong | באבאלונג | **95** | none |
| HERU-RA-HA | helulaha | ההלולאהא | **83** | ה (h+e collapsed) |
| ABRAHADABRA | abulahadabula | אבולאהאדאבולא | **90** | none |
| QIRA | qila | קילא | **141** | none |
| LIBERTY | ziyou | זייוו | **39** | י (i+y), ו (o+u) — double merger |
| CELL | xibao | קסיבאו | **179** | none |

**Tier:** CONSTRUCTED. The Hebrew weighing is the repo's engine; the path
into it (character choice → pinyin → Latin → Hebrew) is the scribe's
construction at every step.

---

## 4. The audit: 姓名学 / seimei-handan as a "tradition"

**Audit question:** does a Chinese/Japanese stroke-count *tradition* exist that
could serve as an attested letter-number table comparable to gematria?

### What the sources actually say

1. **Wikipedia, "Onomancy"** (https://en.wikipedia.org/wiki/Onomancy):
   "In China and Taiwan, onomancy is known as 姓名學 (xìngmíngxué), and in
   Japan, onomancy is known as 姓名判断 (seimei handan)." The most popular
   form "is based on the character strokes in the subject's written name,
   and the result number will be modulo 81," with a fixed lucky/unlucky list.

2. **japanese-names.info, "Seimei-Handan: Japanese Name Fortune-Telling
   Explained"**
   (https://japanese-names.info/articles/seimei-handan-fortunetelling-based-on-your-name/):
   the dominant school is the **Kumasaki-shiki (熊崎式)**, founded by
   Kumazaki Kennō in the early 20th century — a *modern* system, not an
   ancient one. Its core is the **five counts (五格 gokaku)** — tenkaku,
   jinkaku, chikaku, gaikaku, soukaku — computed from *portions of a personal
   name* (surname strokes, given-name strokes, combinations). "Seimei-handan
   is not a unified system. Multiple schools exist, and they sometimes
   produce different results for the same name" — e.g. differing on whether
   to count 郎 as 9 strokes or as its old form 郞 at 14.

3. **geomancy.net, "About Chinese Name Stroke Analysis"**
   (https://www.geomancy.net/forums/blogs/entry/2-about-chinese-name-stroke-analysis/):
   "based on the Traditional Brush Stroke count, which generally we use the
   Kang Xi Dictionary as a guide" — applied to surname+given-name groups,
   yielding five-elements breakdowns and name-luck assessments, explicitly
   framed as choosing names for newborns.

### Why it is NOT a general word-weighing table

- **It weighs personal names, not words.** Every source describes a
  fortune-telling method applied to a *person's name* (often a baby's), never
  a general instrument for weighing arbitrary terms.
- **There is no letter→number table.** Gematria assigns each letter a value
  and sums them. 姓名学 assigns no value to any character; it sums stroke
  counts of name-portions and looks the total up in an **81-number fortune
  chart** (大吉/大凶). The "table" is a luck lookup, not a correspondence
  table. Nothing in it maps a sign to a number the way א=1 does.
- **The schools cannot agree on the counts.** The same character is counted
  differently by different schools (9 vs 14 strokes for 郎/郞; traditional
  vs simplified forms). An "attested table" that disagrees with itself on
  the input data is not a table — it is a family of competing divination
  recipes.
- **It is modern, not a rooted tradition.** The dominant Japanese school
  dates to Kumazaki in the early 1900s; the Chinese practice rides the same
  modern fortune-telling industry. There is no ancient letter-number lineage
  behind it comparable to the abjad/isopsephy transmission.
- **Yijing number symbolism is a different thing entirely.** The Yijing's
  numbers (64 hexagrams, line counts, the Hetu/Luoshu magic squares) are
  cosmological numerology attached to *divination outcomes*, not a
  character-weighing system. Invoking it as a "Chinese gematria" conflates
  two unrelated instruments.

### Verdict

**The "tradition" claim does not survive.** 姓名学/seimei-handan is a modern
name-fortune industry method: it counts strokes of a *personal name* and
reads the total off an 81-number luck chart. It is not a letter-number table,
it has no per-character values, its schools disagree on the counts, and it
has never been a general word-weighing instrument. The audit flag stands
vindicated: **both Chinese columns in this bank are CONSTRUCTED**, and no
attested Chinese table exists to promote them. Any future claim of a
"Chinese gematria tradition" must produce a per-sign value table with a
lineage — stroke-count fortune-telling is not that table.

---

## 5. Arbitrariness analysis — the primary deliverable

The "value" is a function of the scribe's choices, not of the word. Each
demonstration below is a *valid alternative* selection, with the numbers it
would produce:

1. **BABALON** — mine 巴巴隆 (stroke 19, fallback 95) vs the established
   "Babylon" 巴比伦 (strokes 4+4+7=**15**; pinyin "babilun" → fallback
   **92**). Choosing the standard dictionary rendering moves both columns.
2. **HERU-RA-HA** — mine 赫鲁拉哈 (43) vs the established Horus rendering
   荷鲁斯 (strokes 10+12+12=**34**). Nine strokes of pure choice.
3. **QIRA** — mine 奇拉 (16) vs 契拉 (9+8=**17**). One character, one stroke,
   a different "value". Nothing about the token prefers either.
4. **OZ** — mine 奥兹 (21) vs 欧兹 (8+9=**17**). Both are unobjectionable
   phonetic choices.
5. **TRVVTH** — semantic 真理 (21) vs 真实 (10+8=**18**) vs 真相
   (10+9=**19**). Three standard translations of "truth", three values.
6. **Stroke standard** — Kangxi vs PRC moves OZ 21→22, THELEMA 28→35,
   HERU-RA-HA 43→46, ABRAHADABRA 48→58, CELL 17→20 (§2). The *ruler itself*
   is a choice.
7. **Pinyin adjudication** — the machine read 勒 as *lēi*; the intended
   transliteration needs *lè*. A different adjudication changes the fallback
   column (lei → le shifts one letter, ה vs none).

**Finding:** a Chinese "gematria value" for any corpus term is underdetermined
by at least three independent choices (which characters, which stroke
standard, how the pinyin is read) — each choice stated, each choice moving
the numbers. This is exactly what METHOD.md §5 predicts, and it is the
strongest result of this bank: **the Chinese column cannot be a discovery,
only a construction.**

---

## 6. Negative results

- **No target hits in the fallback column.** Nothing lands on 418, 666, 777,
  93, 77, or 11.
- **One target hit in the stroke column: LIBERTY = 11.** 自由 is 6+5=11 —
  the most standard translation of "liberty" in the language, with the most
  standard count. With 22 weighings against 6 targets, METHOD.md §5 applies
  verbatim: "Chance guarantees matches." This is filed as coincidence until
  TRVVTH says otherwise — it is not a bridge, and this report does not
  present it as one.
- **The audit is negative** (§4): no attested Chinese letter-number table
  exists; both columns stay CONSTRUCTED.
- **No bridge is decreed.** All findings go to the red pen.

---

## 7. Work log — ultra-verbose (hypothesis → method → observation → result)

1. **H — the repo binds the method.** M — read `METHOD.md` and
   `pontifex/tables.py` in full before touching anything. O — the fallback
   doctrine (pinyin→`LATIN_TO_HEBREW`→mispar hechrechi), the merger-reporting
   rule, the CJK arbitrariness clause, the three tiers. R — the task's two
   columns are licensed by the repo itself; the audit flag governs the rest.

2. **H — the machine needs pinyin and stroke libraries.** M — checked the
   environment for pypinyin/cnradical. O — neither installed. R — proceed to
   install.

3. **H — pip install will just work.** M — `pip install pypinyin cnradical`.
   O — refused: externally-managed environment (PEP 668). R — dead end #1;
   lesson: use a venv.

4. **H — a venv in /tmp will hold the tools.** M — created `/tmp/cjk-env`,
   installed pypinyin + cnradical. O — **the service restarted mid-install**;
   the venv vanished. R — dead end #2; rebuilt the venv from scratch and the
   install completed ("imports ok"). Lesson recorded: /tmp is ephemeral
   across restarts — nothing load-bearing lives there.

5. **H — cnradical gives stroke counts.** M — probed its API on candidate
   characters. O — `trans_ch` returns radical + pinyin only; its dictionary
   is an opaque pickle with no stroke data and no stated standard. R — dead
   end #3; cnradical cannot supply the weighing. Decision: hard-code PRC
   standard counts in the script (Xinhua style), web-verify the least-certain
   ones, and state the standard explicitly. This turned out *better* than a
   library: the standard is now on the record instead of buried in a pickle.

6. **H — cjklib (Unihan kTotalStrokes) could supply counts.** M — tried
   `pip install cjklib`. O — build failure: its setup.py uses Python-2
   `except X, Y` syntax, SyntaxError under 3.12. R — dead end #4, documented.
   The hard-code decision stands.

7. **H — hand counts risk silent error.** M — web-verified 奥, 索, 佩 against
   Xinhua-dictionary sources. O — 奥=12 (总笔画十二画), 索=10, 佩=8: all
   confirmed. R — hand counts stand; verification discipline demonstrated,
   not merely claimed.

8. **H — character selection is the crux.** M — chose per-term renderings,
   preferring established ones (真理, 泰勒玛, 阿加佩, 自由, 细胞) and
   marking the rest as the scribe's own phonetic selections, with pinyin via
   pypinyin. O — the selection table (§1); the pypinyin misreading of 勒
   (lēi vs lè) surfaced here. R — every choice documented; the correction is
   explicit in code.

9. **H — the repo's map handles all pinyin.** M — ran the fallback on all
   terms. O — `KeyError: 'קס'`: the map's 'x'→'קס' is a *two-letter* value
   and the weigher tried to look up the pair as one key. R — dead end #5
   (bug, not doctrine): fixed by expanding multi-letter mappings before
   weighing. Lesson: the map is a *transliteration* table, not a 1:1 cipher;
   the expansion is now commented in code.

10. **H — the numbers will compute cleanly.** M — reran; hand-checked every
    fallback sum independently. O — all 11 terms match hand calculation
    (e.g. LIBERTY ziyou → ז7+י10+י10+ו6+ו6 = 39; AXONEME → 204). R — 22 CSV
    rows written and verified.

11. **H — a stray "45" might be wrong.** M — rechecked the HERU-RA-HA Kangxi
    note: 14+15+8+9 = 46, not 45. O — confirmed the error. R — corrected in
    script and CSV, reran. The red pen should not have to catch arithmetic.

12. **H — 姓名学 might survive as a tradition.** M — web-searched its
    mechanics (Wikipedia Onomancy, japanese-names.info, geomancy.net). O —
    name-only fortune method, 81-number luck chart, no per-character values,
    schools disagree on counts, modern origin (Kumazaki, early 20th c.). R —
    the claim does not survive; verdict recorded in §4. The audit flag is
    vindicated.

13. **H — the arbitrariness needs numbers, not adjectives.** M — computed
    alternate valid selections (巴比伦, 荷鲁斯, 契拉, 欧兹, 真实/真相) and
    the Kangxi-standard column. O — every alternative moves the values (§5).
    R — the primary deliverable: the Chinese value is a function of the
    scribe's choices, stated three axes deep.

---

## 8. Limits and follow-ups for the red pen

- Stroke counts for the non-web-verified characters rest on standard
  reference values; a second verifier (or the author's own dictionary check)
  is welcome — the per-character breakdown is in the CSV for exactly this.
- Pinyin is toneless and concatenated; a tone-aware or syllable-delimited
  variant would give different fallback numbers — another stated choice the
  red pen may revisit.
- The LIBERTY=11 coincidence is filed as noise; promoting it would need a
  second, independent construction landing on 11, and even then METHOD.md §5
  counsels suspicion.
- Anything here the author dislikes — a character, a standard, the whole
  stroke-count column — is his to strike. Findings, never doctrine.

*93. All Rights Reserved, Without Prejudice. "Live, Love, and let Love, Live."*
