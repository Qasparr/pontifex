# Worker B — KJV Mechanical Text-Diff — Ultra-Verbose Log

Date: 2026-10-25. Task: diff EVERY quoted verse in the Phase 2
Scripture-well annotations against a real KJV text; correct genuine
transcription errors (logging each); flag everything doubtful; no
silent alterations. Do NOT push to git — nothing was pushed.

All outputs in this folder:
`~/workspace/your_files/blacks-teachers-editions/final/work-kjv/`

---

## 1. HYPOTHESIS (going in)

H1. The annotations file matches its stated shape: 1,607 keys,
1,621 annotations, ~538 flagged `deity_verbatim`, citations of the
form "[Book C:V, KJV]", the `note` field carrying the quotation.

H2. Most notes are pure quotations; any commentary admixture will be
rare and structurally visible (quotation marks, dashes, ellipses).

H3. PG #10 will parse at verse level: it prints verses as "C:V text"
blocks, so a marker scan under book headers should reconstruct a
complete index. Expected size: 31,102 verses / 66 books.

H4. Worker verbatim discipline was mostly sound, so exact + partial
should dominate; genuine transcription errors should be a small
tail; anything doubtful goes to flags.

## 2. METHOD — STEP BY STEP, WITH OBSERVATIONS

### Step 1 — Inspect the annotations file

Observation: H1 confirmed exactly. 1,607 keys, 1,621 annotations,
538 with `deity_verbatim: true`, all `well == "scripture"`. Note
lengths 20–393 chars, mean ~129. Distinct citations: 826.

Observation (citation grammar): after stripping the trailing
", KJV", only **9 KJV citations are structurally complex**, plus the
2 non-KJV ones:
- Verse lists: `[Matthew 5:34, 37, KJV]` (SO HELP YOU GOD, S),
  `[Luke 16:10, 12, KJV]` (TRUSTEE), `[Matthew 5:34,37, KJV]` (OATH #1).
- Discontinuous same-book refs: `[Matthew 5:34, 5:37, KJV]`
  (ABAHO, ASSAOH, ASSATH), `[Psalms 139:13, 139:16, KJV]`
  (EN VENTRE SA MERE).
- Multi-reference: `[Proverbs 11:1; Deuteronomy 25:13-15, KJV]`
  (NOTARY PUBLIC).
- Non-KJV (excluded by rule): `[Quran 5:1, Pickthall]` (CONTRACT #0)
  and `[Qur'an 4:135, Yusuf Ali]` (RIGHT #1) — exactly the 2 Qur'an
  annotations on record.
Book names include both "Psalm" (53 citations) and "Psalms" —
alias handled. Books cited span 64 of the 66 (no Song of Solomon,
no Lamentations citations; both still indexed).

Observation (note shapes — answers "inspect the whole set"): the
notes are **pure quotations; NO note appends prose commentary**.
The only admixtures, all catalogued:
- 143 notes are wrapped in straight double quotes; some of those are
  wrapped a second time in straight single quotes by the JSON string
  itself as stored (e.g. NOT GUILTY). Zero curly characters anywhere
  in any note (verified by scan).
- 5 notes are multi-segment: quoted segments joined by ` — `
  (NOTARY PUBLIC, OATH #1) and/or `...` omission marks inside a
  quoted span (NOTARY PUBLIC, SO HELP YOU GOD, S, TRUSTEE) — the
  full multi-chunk set is NOTARY PUBLIC, OATH #1, SO HELP YOU GOD,
  S, TRUSTEE.
- 4 notes contain `...` (the three above-named plus none other;
  count verified by scan: ellipsis in exactly 4 notes — NOTARY
  PUBLIC, SO HELP YOU GOD, S, TRUSTEE).
- An early scare: terminal reprs seemed to show literal
  backslash-apostrophes (`Caesar\'s`) in some notes. Direct byte
  scan of the raw JSON and of every loaded note: **zero backslashes
  in any note**. It was a repr artifact of the tool-output layer.
  The normalizer still repairs `\'` defensively; it never fired.

Extraction method (final): split the note into chunks at `...`
omission marks and at `" — "` segment joins; strip quote marks;
each chunk must match the cited verses as a contiguous word
sequence, in order. **Extraction failures: 0** — every note's chunks
were accounted for by the classifier (no note fell into an
"unparseable note" bucket; the 21 non-matching notes all resolved
to a named class: corrected, flagged, or wrong-reference).

### Step 2 — Obtain KJV sources

Downloaded via the egress proxy (curl):
- PG #10 → `pg10.txt` (see KJV-PROVENANCE.md for URL + SHA-256).
- thiagobodruk/bible `en_kjv.json` → `kjv-structured-thiagobodruk.json`
  (structured cross-check source).
- A third candidate (aruljohn/Bible-kjv) turned out to be only a
  book-name list at the URL tried; discarded, no loss — the
  two-source requirement (primary + ≥20-verse cross-check) was
  already exceeded: the final cross-check covered **all 833
  distinct cited verses**, not 20.

### Step 3 — Build the PG #10 verse index (three dead ends)

DEAD END A — book headers. First parse: 29,591 verses, 64 books;
1 & 2 Samuel missing, Kings counts inflated. Observation: PG #10
prints alternate titles as a second header block ("The First Book
of Samuel / Otherwise Called: / The First Book of the Kings"), so
Samuel's verses were swallowed under Kings. Kings itself survived
by luck (its alternate, "The Third Book of the Kings", is not a
real header). Fix: a header line arriving while the current book
still has zero verses is an alternate title, not a new book.

DEAD END B — wrapped verse markers. Second parse: 30,682 verses.
Observation (Genesis 3:4–5): PG wraps lines mid-verse, and a verse
marker can land at end-of-line ("...surely die: 3:5" / "For God
doth know..."). My marker regex required trailing whitespace
*within the line*, so ~420 markers were missed and verses merged.
Fix: marker pattern `(?:\s+|$)`.

DEAD END C — tokenization. `raw_tokens` produced one more token
than `norm_words` on verses containing curly apostrophes (PG mixes
' and ' by verse; norm folds curly→straight, the span tokenizer
didn't). Fix: fold curly characters in the span tokenizer too
(single-char replacements, spans stay valid).

Result after fixes: **PG index = 31,102 verses, 66 books; key set
identical to the structured source (0 missing, 0 extra).** H3
confirmed. The structured source also parses to 31,102 / 66.

### Step 4 — Cross-check the two KJV sources

Method: compare every distinct cited verse (833) between PG and
structured, normalized identically. Full detail in
`crosscheck-report.json`; summary in KJV-PROVENANCE.md.

Result: 816/833 word-identical; 3 hyphenation/word-division only;
12 text differences, 8 of which are æ-ligature-only (Cæsar vs
Caesar etc.); 4 genuine reading/spelling differences (Acts 24:16
"void to/of offence", Lev 19:15 honor/honour, Prov 6:26
adultress/adulteress, Isa 62:6 mention/remembrancers); 2 of the 833
(Deut 25:22–23) exist in NEITHER source because the chapter has
only 19 verses — the first sign of the GALLOWS wrong reference.

Design consequence: an annotation matching the structured text but
not PG at a point where the sources themselves disagree is an
EDITION VARIANT → flag, never correct. (Full-Bible comparison for
context: the two transcriptions differ at 1,748 of 31,102 verses
before the ligature/hyphen blinds — they are genuinely different
printings' children; a one-source diff without this guard would
have manufactured false "errors".)

### Step 5 — The diff engine (`kjv_diff.py`, runnable)

Pipeline per annotation:
1. Non-KJV citation → **excluded** (the 2 Qur'an annotations).
2. Parse citation (ranges, verse lists, discontinuous refs,
   multi-ref). Parse failures → flagged. **Parse failures in the
   final run: 0.**
3. Missing cited verse → scan all single verses and same-chapter
   verse pairs for where the quotation actually lives; strong match
   → **wrong-reference**; else flagged.
4. Chunk-match (contiguous, in order) against cited verses:
   full coverage → **exact**; clean subsequence → **partial**
   (deliberate partial quotes are not errors; recorded, not fixed).
5. Mismatch path, in strict order:
   a. Edition-variant guard 1: note matches the structured source
      for the same verses while the sources disagree → flagged.
   b. Edition-variant guard 2: identical letter stream, different
      word division/hyphenation → flagged.
   c. Wrong-reference search: rare-word candidate generation over
      the whole index; an alternative verse beating the cited one
      decisively (exact containment, or ≥0.97 and >cited+0.03) →
      **wrong-reference** flag. Citation is NEVER auto-changed.
   d. Spelling-variant-only differences (defined pair list:
      judgment/judgement, throughly/thoroughly, shew/show, etc.)
      → flagged.
   e. Boundary discipline (see Step 6 — this is where the engine
      earned its keep).
   f. Otherwise, similarity within the quoted span ≥ 0.80 →
      **corrected**, with the corrected note rebuilt from the PG
      raw text for exactly the quoted span (original surrounding
      quote marks preserved; PG's stray curly apostrophes folded to
      straight, matching the book's uniform straight-apostrophe
      typography — normalization only, no wording change).
   g. Everything else → **flagged** with the word diffs recorded.

Normalization (both sides, identical): backslash-apostrophe repair
(never fired — see Step 1), curly→straight quotes, case-fold,
punctuation stripped, whitespace collapsed. Spelling is NOT
normalized: a spelling difference is data, classified — never
erased.

### Step 6 — Boundary discipline: two engine bugs found by review

First full run gave: exact 1424, partial 176, corrected 9,
flagged 10, excluded 2. Manual review of EVERY correction and flag
(the whole point of a mechanical diff is that a human reads the
tail) caught the engine mis-handling partial-quote boundaries:

BUG 1 — span expansion. DENARIUS (Matt 22:19–20) quotes vv.19–20
plus the first sentence of v.21 ("They say unto him, Caesar's.");
the draft "correction" silently DELETED the v.21 words.
OPERATIVE (Luke 10:7) is a partial quote with an interior word
transposition; the draft "correction" silently APPENDED the rest
of the verse ("Go not from house to house."), converting a partial
quote into a full one. OUVERTURE (Num 27:8) likewise had the
verse's opening clause silently prepended. Root cause: an
opcode-axis error — in difflib opcodes over (a=note, b=KJV),
'insert' means KJV words the note skipped and 'delete' means
note-only words; the draft span logic and overrun check had the
two reversed (and an empty-word-list comparison made the overrun
check fire spuriously on OPERATIVE's trailing skip).

Fix + rules adopted (all conservative — doubtful goes to flags):
- A correction may restore KJV wording INSIDE the quoted span
  only; it may not move the span's boundaries.
- A note that continues verbatim into the next verse beyond the
  cited range (DENARIUS) → flagged (trim quote or extend citation
  is the editor's choice), not corrected.
- A partial quote whose discrepancy sits AT its boundary
  (OUVERTURE's added "And" at the head of a mid-verse span) →
  flagged, not corrected.
- A pure omission of 3+ KJV words with no omission mark
  (OUVERTURE's skipped opening clause, had it stood alone) →
  flagged as unmarked omission.
- A pure omission of ≤2 words interior to an otherwise complete
  quotation (BURIAL's dropped "a", OBSES's dropped "the") → a
  transcription slip → corrected. Threshold stated here so the
  editor can see the line that was drawn.
- RENDER (Matt 22:21) also taught the gate a lesson: its similarity
  against the FULL verse is 0.727 because the note is a partial
  quote (second half of the verse) — under the draft full-text gate
  it was nearly lost as "low similarity". The gate now measures
  similarity within the quoted span (0.94), and its one interior
  error ("which" for KJV "that" in "the things that are God's")
  is corrected with the span preserved.

Final counts after the fixes (stable across the last two runs):
**exact 1,424 · partial 176 · corrected 8 · flagged 10 ·
wrong-reference 1 · excluded 2 — sum 1,621.** ✓

### Step 7 — Independent re-verification (separate code path)

A throwaway checker (plain regex word streams + string containment,
not the engine's classifier) re-tested every exact and partial
claim: **1,424/1,424 exacts verified; 174/176 partials verified
naively**; the remaining 2 (NOTARY PUBLIC, OATH #1) are the
multi-segment notes — verified segment-by-segment instead (every
segment is a contiguous subsequence of its cited verses, in order).
Every correction's `new_note` was also independently verified: its
normalized word stream is an exact/contiguous match to the PG text
of the cited verses, and every `old_note` is byte-identical to the
annotations file. **Zero discrepancies.**

Breakdowns worth knowing:
- `deity_verbatim` subset (538): exact 452, partial 76,
  corrected 4, flagged 4, excluded 2 — the verbatim discipline held
  at the same rate as the whole set; no special failure mode.
- Multi-chunk notes (5): exact 3, partial 2 — no errors.
- No annotation cited a verse missing from the index except
  GALLOWS (the wrong reference below).

## 3. RESULTS — THE TAIL, IN FULL

### Corrections (8) — also in `corrections.json`; errata text in §4

1. BURIAL #0 [Gen 23:4] — omission: "give me possession" →
   "give me **a** possession".
2. IM NOMINE DEI, AMEN #0 [Col 3:17] — addition: "God and **to**
   the Father" → "God and the Father".
3. MURDER #0 [Num 35:16] — substitution, first word: "**But** if
   he smite" → "**And** if he smite".
4. NOXAL ACTION #0 [Ex 21:30] — addition: "**But** if there be
   laid on him" → "If there be laid on him".
5. OBSES #0 [2 Chr 25:24] — omission: "all the gold and silver" →
   "all the gold and **the** silver".
6. OPERATIVE #0 [Luke 10:7] — transposition: "And **remain in the
   same house**" → "And **in the same house remain**" (partial
   quote; span unchanged).
7. PEB INFORTUNIUM #0 [Num 35:22–23] — substitution: "any stone,
   **whereby** a man may die" → "**wherewith**".
8. RENDER #0 [Matt 22:21] — substitution: "the things **which**
   are God's" → "the things **that** are God's" (partial quote of
   the verse's second half; span unchanged; the first "which" —
   "the things which are Caesar's" — is correct KJV and stands).

### Wrong reference (1) — in `flags.json`; citation NOT changed

- GALLOWS #0, cited [Deuteronomy 25:22-23, KJV]: Deuteronomy 25
  has 19 verses; the cited verses do not exist. The quotation
  matches **Deuteronomy 21:22–23** (clean partial, ending mid-23
  at "accursed of God;"). Almost certainly a chapter transposition
  (25 for 21) at annotation time. Editor's pen.

### Flags (10) — in `flags.json`

Edition variants — note matches the structured KJV transcription;
PG #10 differs at the same point (7 annotations, 5 verses):
- CLEAR #0 [Acts 24:16] — "void **of** offence" (note/structured)
  vs PG "void **to** offence".
- EYRE #0 [1 Sam 7:16] — "**Beth-el**" vs PG "Bethel".
- HADERUNGA, INDIFFERENT, PACK, PREJUDICE (4 keys, one verse)
  [Lev 19:15] — "hon**our**" vs PG "hon**or**".
- PERSONATE #0 [Gen 27:19] — "**firstborn**" vs PG "first born".
- WHORE #0 [Prov 6:26] — "**adulteress**" vs PG "adultress".
Recommendation to the editor (not enacted): the notes as written
follow the more common modern KJV printing at all five points; if
the book standardizes on one KJV printing, these need no change —
but that standardization decision is the editor's, so they are
flagged, not "corrected" toward PG.

Scope/boundary questions (3):
- DENARIUS #0 [Matt 22:19-20] — quote overruns into 22:21
  ("They say unto him, Caesar's."). Trim or extend the citation.
- OUVERTURE DES SUCCESSIONS #0 [Num 27:8] — partial quote
  beginning mid-verse whose first word "And" is not the KJV word
  at that point (KJV: "saying, **If** a man die"); the verse's
  opening clause is omitted without a mark. Re-scope, restore, or
  mark — editor's pen.
- (GALLOWS is counted above as wrong-reference, not in these 3.)

### Excluded (2) — counted, listed, not diffed against KJV

- CONTRACT #0 [Quran 5:1, Pickthall].
- RIGHT #1 [Qur'an 4:135, Yusuf Ali].

## 4. ERRATA TEXT (print-ready, for the book's errata note)

> Errata — Scripture well (KJV text-diff, final build).
> The following eight quotations are corrected against the King
> James Version (Project Gutenberg #10):
> (1) BURIAL, Gen. 23:4 — read "give me a possession of a
> buryingplace", not "give me possession".
> (2) IM NOMINE DEI, AMEN, Col. 3:17 — read "giving thanks to God
> and the Father by him", not "to God and to the Father".
> (3) MURDER, Num. 35:16 — read "And if he smite him", not "But if
> he smite him".
> (4) NOXAL ACTION, Ex. 21:30 — read "If there be laid on him a
> sum of money", not "But if there be laid on him".
> (5) OBSES, 2 Chron. 25:24 — read "all the gold and the silver",
> not "all the gold and silver".
> (6) OPERATIVE, Luke 10:7 — read "And in the same house remain",
> not "And remain in the same house".
> (7) PEB INFORTUNIUM, Num. 35:22–23 — read "with any stone,
> wherewith a man may die", not "whereby".
> (8) RENDER, Matt. 22:21 — read "the things that are God's",
> not "the things which are God's".
> One citation is queried, not altered: GALLOWS is cited to
> Deut. 25:22–23, a passage that does not exist (Deuteronomy 25
> ends at verse 19); the quotation is Deut. 21:22–23.
> Ten further annotations are flagged in the build record as
> edition variants between KJV printings (incl. Lev. 19:15
> "honour", Acts 24:16 "void of offence", Prov. 6:26 "adulteress")
> or as quotation-scope questions (DENARIUS; OUVERTURE DES
> SUCCESSIONS); their text stands as annotated pending the
> editor's ruling. Two annotations quote the Qur'an (Pickthall;
> Yusuf Ali) and were excluded from the KJV diff.

## 5. UNEXPECTED FINDINGS (for the report back)

1. **The two public KJV transcriptions disagree with each other**
   at 4 cited verses in ways that matter (Acts 24:16 "void to
   offence" in PG is the outlier reading; the annotations follow
   the mainstream "void of offence"). A single-source diff would
   have manufactured 7 false corrections; the cross-check guard
   converted them to edition-variant flags.
2. **The only wrong reference is a chapter transposition**
   (Deut. 25 for Deut. 21) pointing at verses that do not exist —
   it surfaced as a parse-level impossibility before any text
   comparison.
3. **No commentary is mixed into any note** — extraction was a
   solved problem once segment joins and omission marks were
   modeled; extraction failures = 0.
4. **The workers' verbatim discipline was strong**: 1,600 of 1,619
   KJV annotations (98.8%) are exact or clean partials as written;
   the genuine error tail is 8 corrections + 1 wrong reference.
5. PG #10's own text is typographically inconsistent (curly vs
   straight apostrophes by verse; "honor" at Lev 19:15 against
   "honour" elsewhere in the tradition) — provenance is recorded
   so any future re-diff can reproduce these exact results
   (SHA-256 in KJV-PROVENANCE.md).

## 6. FILES

- `pg10.txt` — PG #10 as downloaded (primary source).
- `kjv-structured-thiagobodruk.json` — cross-check source.
- `KJV-PROVENANCE.md` — provenance + cross-check summary.
- `kjv_diff.py` — the diff engine (runnable; re-running reproduces
  all outputs deterministically; it never modifies the annotations
  file). SHA-256 at time of log:
  `d447da29cb3f94459f16605705e2e97998c16af79dd6597be0cb435a60b1f1cb`
  (hash of the final, fixed engine).
- `diff-results.json` — per-annotation outcome for all 1,621
  ({counts, results{"KEY#idx": {class, ref, detail, ...}}}).
- `corrections.json` — 8 × {key, idx, ref, old_note, new_note};
  the builder swaps note text wholesale from this.
- `flags.json` — 11 × {key, idx, ref, reason, note}
  (10 flagged + 1 wrong-reference).
- `crosscheck-report.json` — the full 833-verse source comparison.
- `worker-log.md` — this file.

Not pushed to git (per orders). The annotations file was never
modified; corrections exist only as `corrections.json` for the
builder to apply.
