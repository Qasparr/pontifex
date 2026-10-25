# BUILD LOG — Black's Law Dictionary 2e, FINAL Teacher's Edition (single volume, with 5e mapping)
## Date: XXV day of October, Dies Solis, Sol in Scorpio, Anno V:xii e.n. (2026 e.v.)
## Order: Johnathan, 2026-10-25 14:09 EDT — finish the full Teacher's Edition (2e) with the 5th edition changes mapped into a single full PDF.

---

## Phase 0 — Inventory and reconciliation (coordinator)

### Hypothesis
All source materials named in the order exist on disk: base full-text parse (13,145 entries), Vol. I layered merge (3,342 pp; 4,502 footnotes), four well-phase annotation sets, the 5e census (published aggregates: 5e 21,979 unique headwords; survived 3,881; lost 9,011; new 18,098), the Scales of Ma'at cover (Design IV), and the 2026-10-25 rulings file naming SANS JOUR for strike at this rebuild.

### Method
Listed `~/workspace/your_files/blacks-teachers-editions/` (2e/, 5e/, full-text/, married/, vol-1/, well-phases/), the pontifex mirror (PDFs only — the census DATA lives in your_files), read: vol-1/RULINGS-2026-10-25.md, vol-1/merge-log.md, full-text/build-log.md, 5e/worker-log.md, 5e/analyze.py, 5e/data/analytics.json, vol-1/build_vol1_layered.py (the typesetting pipeline to be extended).

### Observation
- All present. entries.json = list of 13,145 dicts {headword, raw_headword, line, page, head_line, body}; first 'A', last 'ZYTHUM'.
- Census key discovery (5e worker-log §5): the census's OWN 2e parse (djvu dual-pattern parse inside analyze.py) found 13,078 rows / 12,892 UNIQUE headwords — and 3,881 + 9,011 = 12,892 exactly. The published turnover was computed against the census's 2e parse, NOT against the book's shipped base parse (13,145). The 253 gap = 13,145 − 12,892 is therefore a BETWEEN-PARSES gap, to be decomposed from data (Worker A), not assumed.
- analyze.py regenerates deterministically from two verified source texts: 5e STUDY-TEXT (`~/workspace/user/files/Blacks-Law-Dictionary-5thEd-1979_STUDY-TEXT.txt`, 8.6 MB, present) and 2e djvu (`~/workspace/blacks-2e/source/blacks-2e-1910_djvu.txt`, 8.1 MB, present). Join key = lowercase alphanumeric; dedup longest-kept.
- Scripture annotations: 1,607 keys / 1,621 annotations / 538 deity_verbatim — matches the order's figures exactly. Schema {well, note, citation, reasoning}; note carries the quotation.
- SANS JOUR: present in law annotations with exactly 1 annotation — strike target confirmed (Rulings record: strike the annotation at this rebuild; the 2e entry itself stands; source annotation remains in the phase JSON).
- Cover IV: `~/workspace/your_files/blacks-hardcover-designs/cover-iv-scales.png` present (his ruled cover for the main text).
- Internet egress works through the proxy (Project Gutenberg answered HTTP 200) — KJV acquisition is feasible.

### Result
Inventory complete; no missing inputs. Two workers dispatched in parallel: Worker A (census regeneration + 253 reconciliation + per-entry mapping + new-headword register), Worker B (KJV acquisition + mechanical diff of all 1,621 scripture annotations). Coordinator will build the final PDF from the vol-1 pipeline extended with: KJV corrections applied (logged), SANS JOUR struck, per-entry 5e apparatus, cover frontispiece, errata note, new-headword register appendix, honest NOT AUDITED labeling.

### Rules held throughout
- Copyright boundary absolute: no 5e entry text anywhere — headwords and status only.
- Nothing struck beyond the single SANS JOUR annotation his ruling names; anything else doubtful is flagged in this log, never silently dropped.
- Ultra-verbose logging (his standing order); no git push.

---

## Phase 0 addendum — REFINEMENT (Johnathan, 2026-10-25 14:14 EDT): MARK, DON'T REMOVE

### The clarification
The SANS JOUR disposition is superseded: **do not remove the annotation — MARK it as struck.** The annotation stays in the book, visibly marked: rendered struck through AND labeled "STRUCK — per ruling 2026-10-25" with the ruling's reason (thin Law footnote) noted, so the reader sees both the annotation and its struck status — the same preservation pattern as his annotated-history practice. The same mark-don't-remove handling applies to anything else in this build that a ruling or flag touches.

### Application in this build
- The law/SANS JOUR footnote will be typeset in place under its entry, with strikethrough rendering and the STRUCK label + reason in the footnote block. The build log records it as *marked struck per his clarification*, not deleted. Page-2856 removal language in the older rulings record is superseded by this clarification for execution purposes; the ruling itself (the annotation is struck) stands — only its mode of execution changes, from deletion to visible marking.
- KJV text-diff handling is unchanged in substance and already aligned: transcription errors are corrected in the text (per the original Phase 1 order) with EVERY correction printed in the errata note as old reading → corrected reading, so the original reading remains on the record in the book itself; doubtful and wrong-reference items are never altered at all — flagged only. Nothing disappears from the record anywhere in this build.
- Phantom-key exclusions (SELF-DEFENSE / SERVITUDE / SILENCE) are unaffected: those annotations were fabricated data struck at phase merge in 2026-10, preserved in `worker-21-STRUCK-phantom-keys.json`; they were never part of the book and are not "removed" by this build — verification confirms their continued absence from the annotation sets.

---

## Phase 0 addendum 2 — ADDITIONAL ORDER (Johnathan, 2026-10-25 14:18 EDT): SCAN-LIMITATION MARKERS

### The order
Mark every place where the 2e text is incomplete due to the scan of the original, so readers know the gaps are limitations of the scan-to-text process, NOT editorial omission — nothing is being hidden. Mark only — never repair, complete, or invent text. Ambiguous patterns get the weaker candidate form and a logged ambiguity. The build log carries the full marker census (total, per-rule counts, complete locus list).

### Marker system (to be defined in the book's front matter, in his terms)
- `[TEXT INCOMPLETE — scan limitation]` — a definite break: the scan failed at this point; the text ends or degenerates here in the source itself.
- `[TEXT POSSIBLY INCOMPLETE — scan candidate]` — the weaker form: the pattern is consistent with scan loss but may be authorial; marked openly, ambiguity logged.
Both rendered in a muted rust tone at small size — distinct, not garish — placed exactly where the text breaks (end of body, in place of an empty body, or inline at a garbage cluster).

### Detection rules (Worker C; detection on the R1–R4-cleaned body so loci match the printed text)
- S1 strong: empty body (recon: 23).
- S2 strong: body-final hyphen — word broken off (recon: 49).
- S3 strong: body-final comma — cannot be authorial.
- S4 strong: the named artifact "JU8TITIA" (recon: exactly 1 entry, idx 7302); garbage clusters (≥3 mixed letter-digit artifact tokens in any 12-token window, or ≥2 in the final 12 tokens). Scattered single garbles NOT marked (pervasive OCR noise is a quality matter already covered by the parsed-not-audited label).
- S5 strong: entries carrying FLAG rows in the 2026-10-18 stratified audit ledger (8 FLAG checks: 4 body-truncation, 3 xref-target-absent, 1 digit-in-headword).
- C1 candidate: no terminal punctuation after quote/bracket stripping, EXCLUDING the authority-name tail pattern (Black's ends entries with authority names; OCR period-loss there is not truncation evidence) — exclusion logged with its count.
- C2 candidate: the 52 stratified-sample entries not already strong (reason: scan verification OPEN on record for that entry).
- NOT a rule: short bodies (274 at 1–3 tokens) — samples are legitimate one-line definitions and see-references; authorial brevity is complete, not incomplete.

### Coordinator reconnaissance (to be verified by Worker C, not trusted blindly)
Naive no-terminal-punctuation count ~1,042 (includes quote-closed endings and authority tails — hence the C1 refinement). Worker C must print 10 random samples per rule with an honest precision judgment; any rule whose samples read as noise gets reported loudly before the builder consumes markers.json.

---

## Phase 0 addendum 3 — FINISH-LINE ORDER (Johnathan, 2026-10-25 14:19 EDT): PUSH ON COMPLETION

Amends the original brief's "do not push" for this build only. When the build is complete and verified, PUSH the final folder to **Qasparr/pontifex**, `research/blacks-teachers-editions/final/` (branch master; commit identity Qasparr@users.noreply.github.com), including: the final PDF, this build log, the marker census, the KJV diff data, the census/mapping/register data, and the builder script. The report must carry: commit hash, exact repo paths pushed, final PDF page count and byte size. If the push fails for any reason, report the failure plainly and leave the folder ready for the parent to push. Everything else in the brief stands.

---

## Phase 1 — Census regeneration + reconciliation (Worker A) — COMPLETE, coordinator-verified

### Result
- **Regeneration EXACT**: re-running analyze.py's logic reproduced every published figure (5e 21,979 unique; census-2e 12,892 unique; survived 3,881; lost 9,011; new 18,098). Gate passed.
- **The 253 gap, fully decomposed, zero residue**: 253 = 117 duplicate-key collapses inside the base parse (91 keys; e.g. `L` ×5) + 522 base-only keys − 386 census-only keys; |base ∩ census| = 12,506; distinct base keys = 13,028. Base-only causes (partitioned): comma in headword 182 · wrapped multi-line headwords 161 (the census crowns tail fragments under other keys — cause (d) in substance) · dotted-initial periods 70 · curly apostrophe 66 · single-letter inline 20 · `)` 7 · comma+’ 5 · single-letter own-line 5 · parens+’ 3 · guillemet anchor 1 (CAVEAT EMPTOR) · page-artifact guard 1 (I 1180 — also the sole genuine base-parse extra: a stranded page number crowned as an entry). Body-range cause measured **0**. Census-only 386 partitioned: 127 wrapped tails + 81 continuation-position + 107 digit-body rejects + 71 terminator-spacing. Full evidence: `work-census/reconciliation.md`.
- **Changed-form category: DOES NOT SHIP.** Both relaxations were rejected at the pre-set 100% verification gate (30-pair lemma-checked samples): R-a plural normalization precision 56.7%, R-b Levenshtein ≤1 precision 63.3% (the ACT/ACTS trap class). Post-hoc tightenings deliberately not adopted (fitting the gate); recorded as UNCHARTED for a future pre-registered pass. The apparatus therefore carries exactly two data-supported fates.
- **Coverage (sums to 13,145)**: carried **3,872** entries · changed-form **0** · not carried **9,273**. (Census "survived" 3,881 is a census-parse key count; 3,872 is base-book entries carried — the distinction is stated in the book's apparatus key.)
- **Register: 18,155** 5e-only headwords; reconciled vs census-new 18,098 as +57 = 104 witnessed only by census-only keys − 47 witnessed only by base-only keys.
- Coordinator verification: mapping.json = 13,145 entries, fates sum 13,145; census.json maps 21,979 / 12,892; register 18,155 (AAA … Zweck v). ✓

## Phase 2 — KJV mechanical text-diff (Worker B) — COMPLETE, coordinator-verified

### Result
- **Source**: Project Gutenberg #10 KJV (`work-kjv/pg10.txt`, SHA-256 in KJV-PROVENANCE.md), parser validated at exactly **31,102 verses / 66 books**; cross-checked against the thiagobodruk structured KJV on **all 833 distinct cited verses**: 816 word-for-word agreements, 3 hyphenation-only, 8 æ-ligature-only, 4 genuine inter-edition differences. The cross-check guard converted 7 would-be false "corrections" into edition-variant flags.
- **Counts (sum 1,621 ✓)**: exact **1,424** · partial **176** · corrected **8** · flagged **10** · wrong-reference **1** · excluded **2** (the two Qur'an annotations: CONTRACT [Quran 5:1, Pickthall], RIGHT [Qur'an 4:135, Yusuf Ali]). Extraction failures: 0. Verbatim discipline measured: 1,600/1,619 KJV annotations (98.8%) exact or clean partial as written; deity_verbatim subset 452/76/4/4/2.
- **The 8 corrections** (applied by the builder via corrections.json swap; each printed in the book's errata as old → new): BURIAL (Gen 23:4, dropped "a" restored), IM NOMINE DEI AMEN (Col 3:17, "to" restored), MURDER (Num 35:16, "But"→"And"), NOXAL ACTION (Ex 21:30, spurious "But" removed), OBSES (2 Chr 25:24, "the" restored), OPERATIVE (Luke 10:7, transposition restored, span preserved), PEB INFORTUNIUM (Num 35:22–23, "whereby"→"wherewith"), RENDER (Matt 22:21, "which"→"that", span preserved).
- **The 11 flags** (printed in the errata; texts NOT altered): GALLOWS wrong reference (cited Deut 25:22-23 — those verses do not exist; the text is Deut 21:22–23; reference correction is his pen alone); 7 edition-variant flags over 5 verses (Lev 19:15 "honour" ×4 keys, Acts 24:16, 1 Sam 7:16, Gen 27:19, Prov 6:26); DENARIUS overrun into Matt 22:21 (trim-vs-extend is an editor's call); OUVERTURE DES SUCCESSIONS unmarked interior omission.
- Coordinator verification: diff-results.json = {counts, results ×1,621}, classes re-summed to 1,621 ✓; corrections.json 8 items with old/new ✓; flags.json 11 ✓.

## Phase 3 — Scan-limitation marker detection (Worker C) — COMPLETE, coordinator-verified

### Result
- **775 merged markers over 772 distinct entries: 132 strong (132 entries), 643 candidate (640 candidate-only entries).**
- Per rule: S1 empty body 23 · S2 final hyphen 49 · S3 final comma 49 · S4 artifacts/clusters 4 · S5 audit FLAG 8 · C1 no-terminal-punctuation 601 (after excluding 146 authority-name tails) · C2 OPEN-SCAN sample 44. C1 accounting closes exactly: 845 stripped bodies lacking terminal punctuation = 98 (S2/S3) + 601 (C1) + 146 (authority-tail exclusions, sampled genuine: "… Abbott", "… Blount", "… CowelL").
- S4 refinement (worker's own, logged everywhere, reversible in one line): the literal spec produced 1 false positive (idx 1346 BATH, KNIGHTS OF THE — legitimate date text "25th May, 1847, and 16th" clustering as artifact tokens); an ordinal exclusion was added. S4 ships 4 loci, all real dense garble (JU8TITIA idx 7302 headword; "0RDINE8 UAJORES…"; "8ENATTJ8 CON8ULTUM…"; "6TREPITU8 JUD1CIALI8…"). Scattered single garbles (289 bodies carry ≥1 artifact token) deliberately unmarked per doctrine — quality noise, not incompleteness.
- Precision verdicts: S1/S3/S4/S5 ship strong; S2 high; **C1 ships ONLY as candidate** — its dominant mode is probably OCR period-loss on complete entries; the printed candidate wording and the front-matter definition will carry that ambiguity honestly; C2 definitional (whole-entry OPEN verification state).
- Coordinator verification: markers.json re-counted — 772 entries / 775 markers / strong 132 / candidate 643; anchors END 700, ENTRY 44, EMPTY 23, SUBSTRING 6, HEADWORD 2 ✓.

## Phase 4 — The final build (coordinator) — builder design decisions (recorded before typesetting)
- Base: the Vol. I layered pipeline (build_vol1_layered.py) extended. Same corpus, same R1–R4 cleanup, same REHOME table and join, same red-letter footnote rendering.
- KJV corrections applied to the scripture phase data BEFORE the join, by (key, idx) locator, with an assertion that the current note equals the recorded old_note (mismatch = stop, never misapply). Every correction prints in the front-matter errata as old → new.
- SANS JOUR: rendered in place; the footnote's citation and note text are struck through, preceded by a bold STRUCK label carrying the ruling date and reason; the reasoning line stays legible as record. (fpdf2 strikethrough style probed at build start; fallback = label-only, logged loudly if the probe fails.)
- law/LAST: stands excluded from print as since the Vol. I merge — its claimed host text exists nowhere in the 13,145 entries, so there is no honest locus to mark; the exclusion and its reason are DISCLOSED in the front matter (§VII) and the annotation remains preserved in the phase data. Marking requires a locus; disclosure is the honest form here.
- Markers: END/EMPTY/ENTRY/HEADWORD anchors print as rust marker lines at the exact locus (in place of the body for EMPTY; after the headword for HEADWORD; after the body for END/ENTRY). SUBSTRING anchors (6) insert the canonical bracketed marker inline into the body text at the match point. Strong text: `[TEXT INCOMPLETE — scan limitation]`; candidate: `[TEXT POSSIBLY INCOMPLETE — scan candidate]`.
- Apparatus per entry, from mapping.json by entry index: "5e apparatus — Carried into the 5th edition (1979)." (+ `as "Form"` when the 5e display form differs from the headword beyond case/punctuation); "5e apparatus — Not carried into the 5th edition (1979)." No changed-form state exists (Phase 1 negative result).
- Frontispiece: cover-iv-scales.png (1280×1792) as page 1. Register appendix: the 18,155 headwords, letter-grouped, flowing text. Front matter rebuilt for the final single volume (apparatus key + reconciliation summary, marker definitions, errata + flags, updated content test). Honest label unchanged: PARSED AND CLEANED — SCAN-VERIFICATION PENDING. NOT AUDITED.

## Phase 5 — Build execution (coordinator) — COMPLETE

### Hypothesis → method
The builder (build_final.py, written from the Phase 4 design) typesets the whole volume in one pass: frontispiece, directive front matter (title block, §§I–IX), the 13,145 entries in parse order — each with body, scan markers at their loci, the 5e apparatus line, and its well footnotes (KJV corrections pre-applied by asserted swap; SANS JOUR rendered struck in place) — then the register appendix and colophon. A BUILD STATS block is printed at the end of the run; every number in it is an assertion target for Phase 6.

### Observation — run history (dead ends included)
- **Run 1 failed immediately**: `ModuleNotFoundError: fpdf` — the VM cycle had wiped the pip packages again (the standing gotcha). Remedy: `pip install fpdf2 pypdf pillow --break-system-packages` (fpdf2 2.8.9). Nothing else was missing.
- **Run 2 (first full build)** — exit 0 in ~150 s. BUILD STATS: entries 13,145, rendered 13,145; strikethrough probe OK (fpdf2 accepts the "S" font style — the struck rendering is real, not label-only); phantom keys absent ✓; KJV corrections applied 8, flags printed 11; law/LAST dropped 1 (disclosed); per-well law 2,096 · scripture 1,621 · humanity 676 · hiphop 109 = 4,502 ✓ (matches the Vol. I merge exactly); entries with notes 3,500; red-letter 538; SANS JOUR marked 1; rehomes 83; direct joins 4,256 (both identical to the Vol. I merge log — the foundation is deterministic); mapping entries 13,145; markers 775 over 772 entries, printed strong 132 / candidate 643, substring fallbacks 0; apparatus carried 3,872 / not-carried 9,273 (sum 13,145 ✓); register 18,155; **pages 3,736**.

### Observation — verification caught two defects in MY front matter (both fixed before push)
1. **The phantom-key wording was inaccurate.** The verifier counted SELF-DEFENSE mentions outside the front matter, and inspection found the genuine 1910 definition text of SELF-DEFENSE printed inside the body of the entry headed SELECTMEN: the base parse never segmented it. The same holds for SERVITUDE (embedded in the entry headed VM, its own heading scan-garbled "PRJEDIAXi") and SILENCE (embedded in SIONTJM, likewise garbled). My §II/§VII shorthand — "fabricated headwords", "no entry of this book answers to them" — was therefore wrong in a way a reader could catch: the headwords are genuine; what was struck at the Vol. I merge was the worker's ANNOTATIONS, for hostlessness (no parsed entry to attach to). §II and §VII(3) were rewritten to state exactly that, with the three embedding loci named. (LAST was re-checked the same way: no headword, no embedded text — §VII(2)'s account stands as written.) After the fix, SELF-DEFENSE is mentioned 4 times in the book, every one accounted for: §II once, §VII(3) twice, the genuine embedded text once.
2. **Frontispiece caption overflow.** The caption's last line spilled alone onto page 2, leaving a near-blank page before the title page. Fix: cover image width 150 mm → 138 mm; caption now completes on page 1.

### Result — final build (run 4, after both fixes)
- BUILD STATS identical to run 2 on every count (entries/rendered 13,145; corrections 8; flags 11; SANS JOUR marked 1; wells 2,096/1,621/676/109; red-letter 538; markers printed 132 strong + 643 candidate, fallbacks 0; apparatus 3,872 + 9,273; register 18,155).
- **Final artifact: `blacks-2e-final-teachers-edition.pdf` — 3,735 pages, 13,978,686 bytes** (one page fewer than run 2: the orphan page is gone).

## Phase 6 — Verification of the shipped PDF (coordinator) — COMPLETE

### Method
`verify_final.py` streams the shipped PDF with pypdf and counts content strings across all 3,735 pages, locates key pages, and probes a stratified sample of entries (every 438th of the 13,145, plus the last) for body presence in the extracted text. Pages were then rendered with pdftoppm and inspected visually.

### Result — counts (all reconcile)
- Apparatus lines in the printed book: **carried 3,872 · not-carried 9,273 · sum 13,145** ✓ (every entry carries exactly one apparatus line).
- Marker strings: strong 133 = 132 printed + 1 quoted in the §VI definition ✓; candidate 644 = 643 printed + 1 in §VI ✓.
- "STRUCK — per ruling 2026-10-25" occurs **exactly once** (SANS JOUR) ✓. "NOT AUDITED" label present on the title page ✓. Colophon present ✓. Register header present, register opens p. 3659 ✓.
- MURDER: corrected reading ("And if he smite him…") found at the entry and in the errata; the old reading ("But if he smite…") survives **only** in the §VII errata ✓ — applied, not vanished.
- GALLOWS: the wrong citation "Deuteronomy 25:22-23" stands at the entry (unaltered, as flagged) and in the §VII flag ✓.
- Stratified sample: **32/32 entry bodies found, 0 missed** ✓.
- Located pages in the shipped PDF: errata §VII p. 10 · JU8TITIA (strong S4 marker) p. 2034 · SANS JOUR (struck annotation) p. 3126 · register p. 3659 · colophon p. 3735.

### Result — visual inspection (pdftoppm renders, `renders/`)
- **p. 1 frontispiece** — Design IV, the Scales of Ma'at, with the full caption on the same page ✓ (re-rendered on the final build).
- **p. 2 title page** — full directive title block, authorship + Thelemic date, classification, and the label box: "PARSED AND CLEANED — SCAN-VERIFICATION PENDING. NOT AUDITED." with the status paragraph and the Flagpole of Claim and Coinage ✓ (re-rendered on the final build).
- **p. 3126 SANS JOUR** — entry, apparatus line, the bold STRUCK ruling paragraph, and the annotation's citation + note text visibly struck through, reasoning line legible; the same page shows SANS IMPEACHMENT DE WANT carrying the strong marker for its empty body ✓ (re-rendered on the final build).
- Errata (§VII, old → new pairs), the JU8TITIA page (headword marker + all four wells on one page), the register opening (with the 18,155 vs 18,098 reconciliation printed in its headnote), and the colophon were inspected on the run-2 build; their content is unchanged in the final build and their positions shifted by exactly the one removed page, as the locate table confirms.

### Push
This folder (minus the two raw third-party KJV downloads in work-kjv/ — pg10.txt and kjv-structured-thiagobodruk.json, both re-derivable via KJV-PROVENANCE.md with SHA-256) is pushed to Qasparr/pontifex, `research/blacks-teachers-editions/final/`, branch master, identity Qasparr@users.noreply.github.com. The commit hash is carried in the coordinator's report to the Architect.
