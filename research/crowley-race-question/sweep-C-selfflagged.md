# Sweep C — Self-Flagged Anomalies in Crowley's Writings

Worker C report. Findings, never doctrine. No hit is declared "the breadcrumb" — reported only.

**Corpus dir (shared with Workers A/B):** `~/workspace/pontifex/research/crowley-race-question/corpus/`
**Copyright discipline:** pre-1930 editions preferred (US public domain); every quotation below is one to two lines, to locate the passage, never to reproduce it.

---

## 1. Work log (ultra-verbose)

### Step 1 — Hypothesis
Crowley occasionally flags his own text as doubtful, erroneous, or deliberately veiled (the KHUT/KHUIT model: "doubt arising in the mind of the prophet as to the unusual spelling... the 'I' makes a difference in the qabalistic interpretation of the name"). If such self-flags exist elsewhere, they will cluster around his characteristic vocabulary: unusual spelling, misprint, printer's error, error, doubt, blind, conceal, corrupt, "should read", "evidently", "seems to be", "perhaps a".

### Step 2 — Method: assemble the corpus
**Observation:** the corpus directory did not exist; Workers A/B had not yet populated it at start of my run.
**Method:** download plain-text transcriptions into the shared dir, preferring Internet Archive full-text files of pre-1930 material, plus thelema.org and sacred-texts.com where reachable.
**Results:**
- Downloaded by me: `liber777.txt` (IA, 1973 annotated ed. of 777 — underlying text 1909, PD), `magick-theory-practice.txt` (IA, Magick in Theory and Practice — 1929 text, PD), `book4.txt` (IA, Book 4 — 1969 Sangreal ed. transcription; underlying 1912–13, PD), `holybooks.txt` (IA, Holy Books of Thelema 1983; underlying texts 1907–11, PD), `holybooks-commentaries.txt` (IA, Regardie's *Commentaries on the Holy Books* 1996 — references only, not the New Comment), `liber58-essay.txt` (IA, Liber LVIII essay), `liberAL-thelemaorg.txt` (Liber AL text scraped from thelema.org/aa/bookofthelaw).
- Found already in shared dir (downloaded by co-workers, reused with thanks): `commentaries.html` (thelemagick-library transcription of the **Old, New, and Djeridensis Commentaries to Liber AL** — the single richest source; underlying texts 1912/1920s, PD), `CCXX_djvu.txt` (Liber AL transcription), `CDXVIII_djvu.txt` (Vision and the Voice), `DCCLXXVII_djvu.txt` (777), `D_djvu.txt` (Sepher Sephiroth), `equinox-v1n05.txt` and `equinox-v1n08.txt` (OCR of the **original 1911 and 1912 Equinox** printings — PD), plus worker-A artifacts (`variants_raw.json`, `extract_variants.py`, `sepher-sephiroth/`, `open_777/`) which I read but did not touch.
- **Dead ends (logged):**
  - `LIBERALVELLEGISEBook` (IA) turned out to be a **Portuguese** translation — discarded.
  - `lawisforallexten0000crow` (IA, *The Law is for All* 1975): **401 lending-restricted**, not downloadable. The New Comment was nevertheless covered via `commentaries.html` (Old + New + Djeridensis, ~1 MB, 235 "New Comment" mentions).
  - `hermetic.com/legis/new_comment/`: **403 to both curl and browser fetch** — not retried, per policy.
  - `sacred-texts.com` via curl: connection reset; via `browser.open` the Liber AL page (`engccxx.htm`) fetched fine (used only to confirm verse text).
  - `bibliotecapleyades.net` crowley index: 404 on guessed URL; real index not located.
  - `keepsilence.org/the-equinox/`: JS-only app, no fetchable text.
  - `lib.oto-usa.org/libri/` index: 403; the `liber0220.html` page itself fetched (Liber AL text + intro, OTO edition).
  - **The Book of Thoth (1944): not covered** — copyrighted work, excluded under the PD discipline. Listed as a known gap.
  - Original Tunis 1925/26 printing of *The Law is for All*: no public scan located.
  - Post-sweep probe: IA identifiers `equinox-v1n7`, `equinox-v1n5`, `equinox-v1n8` return HTTP 200 but carry no title/date metadata and no full-text files (consistent with the co-worker's 0-byte downloads) — dead end, not usable sources. The original 1911/1912 Equinox OCR already in the shared corpus (`equinox-v1n05.txt`, `equinox-v1n08.txt`) remains the PD source for those volumes.

### Step 3 — Method: grep battery
**Method:** case-insensitive grep over all corpus texts for: "unusual spelling", "misprint", "mis-print", "printer's error", "doubt arising", "doubt", "blind", "conceal", "corrupt", "seems to be", "perhaps a", "should read", "evidently", "error" — then a second pass with narrow textual-sense regexes (e.g. `corrupt\w*\s+(text|manuscript|copy)`, `(printer's|copyist's|scribal)\s+\w+ error`, `errat\w+`, `a blind for`, `tamper\w*`, `mistake\s+(in|of)\s+the\s+(text|verse|manuscript)`), each hit extracted with ±300–400 chars of context.
**Observation:** hit counts were dominated by doctrinal/incidental uses ("blind faith", "blind obedience", "corruptible", "in doubt" as tarot meanings, "evidently" as filler). The narrow regexes reduced ~600 raw hits to a triageable set.

### Step 4 — Triage (keep / blinds-list / discard)
Applied per-hit: (i) genuine self-flagged textual anomaly → ledger §2; (ii) doctrinal concealment language → blinds list §3; (iii) incidental → discard log below.

**Discards (with reasons):**
- D.1 — `liber777.txt`/`DCCLXXVII_djvu.txt` "misprint"/"corrupt or misprinted"/"should read"/"error for" hits: all **modern editor's footnotes** (cite Zalewski 1994, Regardie ed., "corrected as compositor's errors"). Not Crowley's voice. (One lead for Worker B: the editor notes 777's printed edition had V/F/C table errors corrected as compositor's errors.)
- D.2 — `commentaries.html` "should read Liber DCCCXIII" / "transcription error": **modern site editor's footnote (Frater D.M.T.)**, not Crowley.
- D.3 — `equinox-v1n05.txt`/`v1n08.txt` "misprints... found in a printed table of errata": an **Equinox book review of another author's qabalistic book** (reviewer notes the misprints were all in the author's own errata table). Not Crowley's own text.
- D.4 — `equinox-v1n05.txt` "which all should read" / "every one should read it and shudder": incidental.
- D.5 — All "in doubt" textual-pattern hits: tarot divination meanings ("recovery not in doubt"), doctrinal ("The Will having stopped in doubt, goes on again in error"), incidental.
- D.6 — "corrupt" hits: overwhelmingly doctrinal ("corruptible", "the corrupt", "incorruptible"). One Crowley line in `holybooks-commentaries.txt` about "the deliberate corruption of the text of that Book" refers to **the biblical Apocalypse**, not his own text — logged as observation O.1, not a kept anomaly.
- D.7 — D_djvu.txt (Sepher Sephiroth) "See also errata on 114": Crowley's own internal cross-reference to the work's errata page — noted, but a routine errata pointer, not a flagged anomaly.
- D.8 — WEH (William E. Heidrick) editorial notes in commentaries.html (e.g. Hadit/Bahadit stele spelling): modern editor, not Crowley.
- D.9 — "I did lose the Manuscript more or less purposely": appears in the thelemagick site's modern preface material quoting Crowley's *Confessions*-era voice about manuscript history — not a textual anomaly; noted as manuscript-history color only.
- D.10 — All remaining "blind"/"conceal"/"error"/"evidently"/"doubt" hits sampled: doctrinal or incidental (verse text itself, metaphors, "blind faith", tarot).

---

## 2. Anomaly ledger (kept hits)

Quotations are one to two lines each, to locate the passage. "Resolved" = Crowley settles it himself; "Open" = he leaves it standing.

**C-1 — Khut/Khuit (the KHUT/KHUIT model, verified in-corpus).**
Old Comment to **III:2** ("...Raise the spell of Ra-Hoor-Khuit!"): *"Suggested by a doubt arising in the mind of the prophet as to the unusual spelling. But the 'I' makes a difference in the qabalistic interpretation of the name."* **Resolved** — he keeps the "I" and gives the qabalistic reason. Corroboration: the `CCXX_djvu.txt` transcription shows the manuscript spelling "Khut" (OCR-dropped final t as "Khu") at III:2, III:14, III:35 ("The half of the word of Heru-ra-ha, called Hoor-pa-kraat and Ra-Hoor-Khut"), and III:66.

**C-2 — I:60, phrase inserted by the Scarlet Woman's hand.**
New Comment to **I:60**: *"In the original MSS. the second paragraph begins 'The shape of my star is' — and then breaks off — the Scribe was unable to hear what was being said... An alternate phrase was subsequently dictated to the Scarlet Woman, and inserted in the manuscript by her own hand."* **Resolved** — he explains the break and accepts the dictated alternate phrase (the Five-Pointed-Star passage as printed).

**C-3 — I:15, "Prince-priest" flagged as possible cipher.**
New Comment to **I:15**: *"'Prince-priest' is an unusual word, and not in tone with other references to me. I suspect therefore a secret cipher of some sort."* **Open** — he offers the anagram PRINCEPS ITER as a possibility but settles nothing.

**C-4 — II:76, the cipher deliberately withheld.**
New Comment to **II:76** (the "4 6 3 8 A B K..." riddle verse): the mystery lies *"within the comprehension of the Beast, kept secret by him in order to prove any one who should claim sonship"* (he names Charles Stansfeld Jones/Achad as claimant). **Open by design** — resolution deferred to a successor as a proof-test.

**C-5 — Liber 418 (Vision and the Voice), "Circle" named as a blind.**
Crowley's own note on the Aethyr passage of the old King and the Virgin on the bull: *"'Circle' — a blind for 'the Mark of the Beast' — {Sun} — which at that time it was necessary to keep secret."* **Resolved/explained** — he names the blind and its reason.

**C-6 — I:11, possible careless phrasing vs. hidden puzzle.**
New Comment to **I:11**: *"Can we have 'phrased' it carelessly, or punctuated it incorrectly? Or is there a Qabalistic puzzle or a mystic submeaning concealed?"* **Open** — he leans toward a "Silent selves" reading but leaves the question standing.

**C-7 — I:24, further mystery suspected.**
New Comment to **I:24** ("I am Nuit, and my word is six and fifty"): *"I am inclined to believe that there is a further mystery concealed in this verse; possibly those of 418 and 666 again."* **Open.**

**Total kept: 7** (4 resolved/explained, 3 open, 1 open-by-design).

---

## 3. Blinds-doctrine passages (general concealment doctrine, not specific textual anomalies)

- **Liber AL I:34** (the verse itself): *"the ordeals I write not: the rituals shall be half known and half concealed."* — the charter text of the doctrine.
- **New Comment I:13**: *"It was obviously necessary, from a practical point of view, to phrase this Book in terms of common parlance, concealing the more recondite Arcana in the numerical and literal cipher."* — the doctrine stated as editorial policy.
- **Old Comment I:37** (the stele-paraphrase verse): *"It conceals a certain secret ritual, of the highest rank."*
- **New Comment II:76** (see C-4): the cipher *"kept secret by him in order to prove any one who should claim sonship"* — concealment as initiatory test.
- **Liber AL II:14** (verse) + New Comment: *"let the light devour men and eat them up with blindness!"* — with cross-references to Liber LXV and Liber VII on the devouring light.
- **Observation O.1** (about another text, not his own): in the Holy Books commentaries Crowley attributes obscurity in Revelation to *"the confusion caused by the deliberate corruption of the text of that Book"* — i.e., he does allege deliberate textual corruption, but of the biblical Apocalypse, never of his own received texts.

---

## 4. Coverage statement

**Covered:** Liber AL + Old, New, and Djeridensis Commentaries (via thelemagick-library transcription in shared corpus; underlying texts 1912/1920s, PD); Liber AL text (thelema.org; OTO-USA; CCXX_djvu transcription); 777 (two transcriptions; 1909 text PD, modern editorial notes filtered out); Sepher Sephiroth (D_djvu + original 1912 Equinox OCR); The Vision and the Voice (CDXVIII_djvu + original 1911 Equinox OCR); Book 4 (1912–13 text); Magick in Theory and Practice (1929 text); the Holy Books (1907–11 texts); Regardie's Commentaries on the Holy Books (references only); Liber LVIII essay.
**Not obtained / not covered:** The Book of Thoth (1944, copyrighted — excluded by the PD discipline); standalone *The Law is for All* Weiser editions (IA lending-restricted); the Tunis 1925/26 first printing (no public scan found); hermetic.com (403, not retried); sacred-texts.com via curl (blocked; one page fetched via browser instead).
