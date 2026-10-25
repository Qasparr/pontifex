# WORKER LOG — Worker C: Scan-Limitation Marker Detection
## Black's Law Dictionary 2e, Teacher's Edition (final build) — 2026-10-25

Ultra-verbose per standing order: hypothesis → method → observation → result, dead ends included.
Doctrine of this task (his words, 2026-10-25 14:18 EDT): mark every place where the 2e text is
incomplete due to the scan of the original, so readers know the gaps are limitations of the
scan-to-text process, NOT editorial omission — nothing is being hidden. MARK ONLY: this worker
never repairs, completes, corrects, or invents any text. Ambiguous patterns get the weaker
candidate marker and a logged ambiguity. No git push (coordinator's order).

---

## STEP 0 — Inputs verified before any detection

Hypothesis: the three data sources named in the assignment exist at the stated paths and match
the coordinator's description (13,145 entries; ledger 369 rows with 205 PASS-TEXT / 156
OPEN-SCAN / 8 FLAG; 52 sampled headwords; Cleaner class in the Vol. 1 builder).

Method: listed the directories; loaded entries.json, sample-ledger.csv, sample-summary.json;
extracted the Cleaner class from build_vol1_layered.py (lines 222–244) and read it in full.

Observation: all files present. entries.json is a list of 13,145 dicts
{headword, raw_headword, line, page, head_line, body}; bodies carry raw OCR double-spacing.
Ledger parses to 369 data rows; STATUS counter = PASS-TEXT 205, OPEN-SCAN 156, FLAG 8 — exact
match to the assignment. The 8 FLAG rows: BREAKING (XREF-SEE, target not in headword set),
HOMESOKEN, HOMSOKEN (XREF-SEE), YEAR (XREF-SEE), DECRETAE ORDER / FIGTIO / FORLER-LARD /
ZEMINDAR (BODY, ends without terminal punctuation), IN PR2EMISSOREM FIDEM (HEADWORD, digit in
headword). Cleaner R1–R4 confirmed: R1 tabs→space; R2 collapse 2+ spaces; R3 join
"-\n" + lowercase; R4 per-line rstrip; final whole-body strip.

Result: inputs verified. The detector replicates the Cleaner verbatim (same regexes, same
order) so every locus matches the printed text.

## STEP 1 — Coordinator's scale reconnaissance: verify, don't trust blindly

Method: ran my own counts on cleaned bodies before writing any rule.

Observation (mine vs coordinator's):
- Empty bodies: 23 vs 23 ✓
- Bodies ending in hyphen: 49 vs 49 ✓
- "JU8TITIA": exactly 1 entry, idx 7302, and it occurs in the HEADWORD ONLY (the body carries
  other garbles — "Jnstitia" etc. — but not the token itself) vs "exactly 1 (idx 7302)" ✓
- Bodies of 1–3 tokens: 274 vs 274 ✓
- Bodies lacking terminal punctuation (naive): coordinator ~1,042; my count with trailing
  quote/bracket stripping = 845 (an earlier probe with a slightly larger strip set gave 846).
  The coordinator's figure evidently used a rawer endswith test (no stripping, raw spacing);
  the discrepancy is in the probe, not the data — my rule C1 is defined on the stripped body
  per the assignment text, and the full C1 accounting reconciles exactly (Step 4).

Result: reconnaissance confirmed on every checkable number; the one divergence is explained
above and logged, not silently absorbed.

## STEP 2 — Mapping checks (S5 / C2 prerequisites)

Hypothesis: sampled/FLAG headwords might be absent or duplicated in entries.json, which would
break exact-match mapping.

Method: built headword → [indices] index; looked up all 8 FLAG entries and all 52 sampled
headwords.

Observation: every FLAG entry and every sampled headword matches EXACTLY ONE index. No absent,
no duplicates. Mappings (also in marker-census.md): BREAKING 1581, DECRETAE ORDER 3555,
FIGTIO 5160, FORLER-LARD 5386, HOMESOKEN, HOMSOKEN 6188, IN PR2EMISSOREM FIDEM 6590,
YEAR 13122, ZEMINDAR 13139.

Result: S5 and C2 mapping is unambiguous; no locus invented, none dropped.

Dead end (minor): for S5 XREF-SEE anchors I first tried the ledger's RAW OCR string verbatim —
it carries double spaces and fails against the cleaned body. Route taken: clean the raw string
with the same Cleaner and search for it (found for BREAKING "See Arbebtment." and YEAR
"See Estate foe Years."); if absent (HOMESOKEN — cleaned body reads "See\n\nHaicesokbn."),
fall back to the final token of the cleaned raw string ("Haicesokbn."), which is present;
if even that failed, anchor would be "ENTRY" (did not occur).

## STEP 3 — Rules as implemented (stated exactly; refinements flagged)

- S1 (strong): cleaned body empty → anchor "EMPTY". 
- S2 (strong): cleaned body ends "-" → anchor "END".
- S3 (strong): cleaned body after stripping trailing straight/curly quotes and closing
  brackets/parens ends "," → anchor "END".
- S4 (strong): (a) token "JU8TITIA" in headword/body → anchor = the containing cleaned-body
  line segment, or "HEADWORD" if headword-only (the actual case at idx 7302).
  (b) Garbage clusters: artifact token = regex ^[A-Za-z]*\d[A-Za-z0-9]*$ over the token CORE,
  length ≥ 4, ≥ 2 letters, ≥ 1 digit; cluster = ≥ 3 artifact tokens in any 12-token window,
  OR ≥ 2 within the final 12 tokens; overlapping spans merged; anchor = exact cluster
  substring of the cleaned body.
  REFINEMENT 1 (mine, logged): the regex is applied to the punctuation-stripped token core,
  not the raw whitespace token — OCR tokens routinely carry punctuation ("34R,"), and the
  literal reading would silently undercount clusters. This changes WHICH tokens count, not
  the thresholds.
  REFINEMENT 2 (mine, logged, with before/after): ordinal cores ^\d+(st|nd|rd|th)$ are
  excluded from artifact tokens. The spec's own parenthetical says the filter "excludes
  '1st'-class" — but length ≥ 4 lets 2-digit ordinals (10th, 25th, 16th) through, and idx 1346
  BATH, KNIGHTS OF THE fired a cluster on the legitimate date text "25th May, 1847, and 16th".
  A 25th is the same class as a 1st; the exclusion implements the spec's stated intent.
  BEFORE: S4 = 5 loci. AFTER: S4 = 4 loci. The removed locus is named here so the coordinator
  can reverse this refinement with one line if he rules otherwise.
  Scattered single artifact tokens NOT marked, per assignment reasoning (pervasive OCR garble
  is a quality matter, covered by the book's parsed-not-audited label). Measured prevalence:
  289 bodies carry ≥ 1 artifact token, 334 artifact tokens total; 28 bodies carry exactly 2
  (e.g. idx 458 JEDIFICARE, pair at gap 2) — mid-body pairs do not meet either cluster test
  and stay unmarked BY DESIGN.
- S5 (strong): any FLAG row → locus; reason from the FLAG NOTE; anchor "END" for BODY
  truncation flags, "HEADWORD" for the digit-headword flag, the cross-reference segment
  itself for XREF-SEE flags (Step 2 dead end).
- C1 (candidate): cleaned body, trailing quotes/brackets stripped, does not end in [.!?],
  entry not already S1–S3 → anchor "END"; EXCLUDING the authority-tail pattern (final token a
  single capitalized word, length ≤ 14, immediately preceded by ". " or standing alone on its
  own line as a short citation tail). Uncertain subclasses KEPT as candidates and counted
  (Step 4), per the assignment's instruction not to exclude on uncertainty.
- C2 (candidate): the 52 sampled entries not already strong via S5 → anchor "ENTRY", reason
  "stratified sample audit (2026-10-18): scan verification OPEN for this entry". Interpretation
  logged: the spec excludes C2 only via S5; a sampled entry carrying an unrelated strong marker
  at a different anchor still receives its C2 whole-entry candidate (anchors differ, both kept).
- Short bodies (1–3 tokens) with terminal punctuation and no other signal: NOT marked.

Cleaner counters over the whole corpus (sanity): R1 tabs 0; R2 multi-space collapses 896,289;
R3 hyphen joins 378; R4 trailing-ws lines 0. The OCR text has no tabs and no trailing line
whitespace; R2/R3 do the real work.

## STEP 4 — Results and exact reconciliation

Rule hits (before dedupe) / distinct entries:
- S1: 23 / 23 — S2: 49 / 49 — S3: 49 / 49 — S4: 4 / 4 (after Refinement 2; 5 before)
- S5: 8 / 8 — C1: 601 / 601 — C2: 44 / 44 (52 sampled − 8 already strong via S5)
- Total hits: 778. Merged markers: 775. Distinct marked entries: 772.
- Strong markers 132 (entries with ≥ 1 strong: 132); candidate markers 643
  (candidate-only entries: 640).
- Dedupe merges (3): idx 3555 DECRETAE ORDER, anchor END, S2+S5; idx 5160 FIGTIO, anchor END,
  C1+S5 → strong; idx 5386 FORLER-LARD, anchor END, C1+S5 → strong. (ZEMINDAR's S5 flag does
  NOT merge with a C1: its cleaned body ends "…Wharton." — the trailing "Z" in the ledger's
  raw excerpt is the next entry's first letter caught in the audit window, and the body itself
  carries terminal punctuation. The S5 strong marker stands on the audit's own finding.)
- C1 reconciliation (exact): 845 bodies lack terminal punctuation after stripping
  = 98 already strong via S2 (49) + S3 (49) + 601 C1 candidates + 146 authority-tail exclusions.
  845 − 98 − 146 = 601 ✓. Exclusion examples verified by eye: "…a qua. Abbott" (A QUO),
  "…metals. Blount" (AFFINAGE), "…falconer. Blount", "…matter. CowelL" (OCR-garbled Cowell —
  pattern still applies). One quirk logged: AD HUNC DIEM ends "…1 Leon. 90. / Digitized by /
  Google" — the scan's own digitization tail; it was excluded via the standing-alone-line
  branch ("Google" a single capitalized word on its own line). Outcome is right (the entry is
  complete; the tail is the scanner's watermark, arguably itself a scan artifact worth a
  different marker someday) but the mechanism is the line branch, not the ". " branch — stated
  here so no one over-reads the exclusion rule.
- C1 kept subclasses: ends-lowercase-word 295; capitalized-final-word-NOT-excluded 130;
  other 115; ends-with-digit citation tail 47; ends-semicolon-or-colon 14.
  The "other" 115, inspected: citation tails whose final token is a digit+letter core
  ("…14 Mass. 15L", "…46 Pac. 84L", "…5 Coke, 80l" — page numbers with OCR L/l for 1), stray
  scan glyphs ("•", "►", "/"), and one body ending "(". All ambiguous between period-loss on a
  complete citation tail and true truncation — kept as candidates, as instructed.
- Short bodies: 274 total; 255 unmarked, of which 247 end with terminal punctuation. The
  remaining unmarked-without-punctuation short bodies are covered by other rules or are
  authority tails. The 19 marked short bodies carry a real signal (S/C rule) — shortness
  itself marked nothing.

## STEP 5 — Precision self-check: 10 random loci per rule (seed 20261025) + honest verdicts

### S1 (strong) — 23 loci total; all are empty by construction (sample of the set):
  - idx 10377 — IRQ — (cleaned body is empty)
  - idx 11144 — SANS IMPEACHMENT DE WANT — (cleaned body is empty)
  - idx 876 — PUKTKNANT — (cleaned body is empty)
  - idx 2367 — COMMANDERY — (cleaned body is empty)
  - idx 11621 — BEB — (cleaned body is empty)
  - idx 4436 — CLOSE — (cleaned body is empty)
  - idx 8407 — I 1 — (cleaned body is empty)
  - idx 9910 — SUMPTION — (cleaned body is empty)
  - idx 12918 — WARRANTY — (cleaned body is empty)
  - idx 3556 — DEB — (cleaned body is empty)
VERDICT S1: precision 1.00 by construction — an empty body is an empty body. SHIP.

### S2 (strong) — body-final hyphen:
  - idx 875 — APPERTAIN — …To belong to; to have relation to; to be appurtenant to. See Ap-
  - idx 804 — ANNULUS — …. Per haspum vel annulum hostii exterioris; by the hasp or ring of the outer door. Fleta, lib. 3, e. 15, /  / i 5-
  - idx 10376 — QUICK WITH CHILD — …See Quicker -
  - idx 5005 — FALSE — …ict.(2d Ed.) -31 /  / place and ' business in which they are uAed. ?J01 CS°5003a'' 1903> 5 552 : PeQ' 00116 Idaho-
  - idx 3898 — DIRIMENT IMPEDIMENTS — … Am. St Rep. 565. /  / At the present day, disability is generally used to indicate an incapacity for the full en-
  - idx 7767 — LOCO PARENTIS — …See Is Loco Pa-
  - idx 9807 — FRIED IA — …In the civil law. Lands; es- tates; tenements; properties. See Pa.«ni-
  - idx 9096 — OUTSUCKEN MULTURES — … grinding corn at any mill to which they are not thirl- ed, or bound by tenure. 1 Forb. Inst. pt. 2, p. 140. -
  - idx 4675 — EVB8-DROPPERS — …See Eaves-Dkop-
  - idx 9957 — PRINCIPLE — …application to' a useful purpose, may be patentable. See Barrett v. Hall, 1 Mason, 470, Fed. Cas. No. 1,047. -
VERDICT S2: HIGH precision. 8 of 10 sampled are mid-word or mid-cross-reference breaks
("See Ap-", "the full en-", "thirl- ed … 140. -"). Two sub-cases end with a LONE "-" after
apparently complete text (idx 9096, 9957): the hyphen is the last glyph the scan gives; whether
a word followed on the original page is exactly what the marker exists to say we cannot know.
Still a scan-limit locus. SHIP as strong.

### S3 (strong) — body-final comma:
  - idx 5457 — FR — …Cir vilis of Justinian, the several extracts from juristic writings of which it is composed be- ing so called,
  - idx 3062 — CRAFT — …s. Not a legal term in this sense, though often used in connection with such terms as “fraud" and “artifice.”,
  - idx 1597 — BREVIATE — …statement, epitome, or abstract. A short statement of contents, accompanying a bill in parliament Holthouse. ,
  - idx 8406 — MONTES — …In Spanish law. Forests or woods. White, New Hecop. b. 2, tit 1, c. 6,
  - idx 11912 — SURGEON — …b, 55 Minn. 20, 50 N. /  / W. 256-; Nelson v. State Board of Health, 108 Ky. 769, 57 S. W. 501, 50 L. R. A. 383. ,
  - idx 11395 — SEXTUS DECRETALIUM — … a collection of supplementary de- cretals, and was published A. D. 1298, Butl. Hor. Jur. 172 ; 1 BL Comm. 82,
  - idx 152 — ACCORD AND SATISFACTION — …Mo. App. 55; Rogers v. Spokane, 9 Wash. 168. 37 Pac. 300; Ileavenrich v. Steele, 57 Minn. 221, 58 N. W. 982. ,
  - idx 6627 — INCARCERATION — …m pro non facto babt* tnr. A tiling done unwarily (or unadvised* ly) will be taken as not done. Dig. 28, 4, 1,
  - idx 5118 — FERIA — …ration of some partic- ular event which had been of importance to- them or their ancestors. Smith, Diet Antiq,
  - idx 12358 — TRAVERSER — …ng. One who traverses or denies. A prisoner or party in- dicted; so called from bis traversing the indictment,
VERDICT S3: HIGH precision. Every sampled locus is a genuine cut-off: prose mid-sentence
(FR, FERIA, TRAVERSER) or citation lists ending mid-cite ("Dig. 28, 4, 1," / "1 Bl. Comm. 82,").
A printed Black's entry cannot authorially end with a comma. SHIP as strong.

### S4 (strong) — named/garbage artifacts (only 4 loci exist; all shown):
  - idx 7302 — JU8TITIA — headword='JU8TITIA'; body: Lat. Justice. A jurisdic- tion, or the office of a judge. /  / —Jnstitia piepoudrous…
  - idx 9033 — ORDINES — anchor-substring: 0RDINE8 UAJORES ET MINORE8
  - idx 11309 — SENATUS OONSULTUM — anchor-substring: 8ENATTJ8 CON8ULTUM /  / 8ENTENOE
  - idx 11765 — STREFITTJ8 — anchor-substring: 6TREPITU8 JUD1CIALI8 /  / 6TULTIL0QUIUM
VERDICT S4: after Refinement 2, precision HIGH — all 4 loci are genuine dense garble
(JU8TITIA headword; "0RDINE8 UAJORES ET MINORE8"; "8ENATTJ8 CON8ULTUM / 8ENTENOE";
"6TREPITU8 JUD1CIALI8 / 6TULTIL0QUIUM"). Sensitivity is deliberately LOW: this rule catches
only catastrophic garble clusters, not the 334 scattered artifact tokens corpus-wide — that is
the assignment's design, restated here so no reader mistakes S4 coverage for a garble census.
WITHOUT Refinement 2 the rule ships 1 false positive in 5 (BATH ordinals) — the refinement is
recommended. SHIP (refined).

### S5 (strong) — audit FLAG entries (8 loci; all shown via samples where sampled):
  - idx 1581 — BREAKING — anchor-substring: See Arbebtment.
  - idx 3555 — DECRETAE ORDER — …See Decree; Ob-
  - idx 5160 — FIGTIO — …m laedit. A fiction of law injures no one. 2 Rolle, 602 ; 3 BL Comm. 43 ; Low v. Little, 17 Johns. (N. Y.) 34R
  - idx 5386 — FORLER-LARD — …dings. If the matter of the plea is bad or insufficient, irre- spective of the manner of setting it forth, the
  - idx 6188 — HOMESOKEN, HOMSOKEN — anchor-substring: Haicesokbn.
  - idx 6590 — IN PR2EMISSOREM FIDEM — headword='IN PR2EMISSOREM FIDEM'; body: In con- firmation or attestation of the premises. A notarial phrase. /  / In prsepar…
  - idx 13122 — YEAR — anchor-substring: See Estate foe Years.
  - idx 13139 — ZEMINDAR — …ultivators, and the realization of the government's share of its produce, either in money or kind. Wharton. /  / Z
VERDICT S5: precision rests on the 2026-10-18 stratified audit, not on my re-judgment — I
mapped, I did not re-audit. Mapping verified 8/8 unique. SHIP.

### C1 (candidate) — no terminal punctuation:
  - idx 9929 — PREVIOUS QUESTION — …der of time, for the purpose of asserting the priority of the. -first Lebrecht v. Wilcoxpn, 40 Iowa. 94. . , :
  - idx 8907 — OBXEMPERARE — …Lat To obey. Hence the Scotch “obtemper," to obey or comply with a Judgment of a court
  - idx 5771 — GRACE, DATS OF — …hange or note It was originally a gratuitous favor, (hence the name,) but custom has rendered it a legal right
  - idx 5041 — FASTI — …. See Dies Fasti. /  / Fatetur f acinus qni judicium fugit. /  / 8 Inst. 14. He who flees Judgment confesses his guilt
  - idx 12826 — VIS — …ms, and expulsive force without arm* Bract, fol. 162.— Via extur- ■atlva. In the civil law. Exturbative force;
  - idx 10513 — RECIPROCAL CONTRACT — …A con- tract, the parties to which enter Into mutual engagements. A mutual or bilateral con- tract
  - idx 1895 — OASTELLAIN — …table of a fortified house; a person having the custody of one of the crown mansions; an officer of the forest
  - idx 9455 — PERFORM — … subject-mat- ter; but the term is usually applied to any action in dlsoharge of a contract other than payment
  - idx 8634 — NETHER HOUSE OF PARLIAMENT — …A name given to the English house of com- mons in the time of Henry YIIL
  - idx 3599 — DEFENDER — …(Fr.) To deny; to defend; to conduct a suit for a defendant; to forbtd; to prevent; to protect
VERDICT C1: MIXED — and that is exactly why it is a candidate, not a strong. Reading the 10:
several are apparently COMPLETE text whose final period was likely lost in OCR (FASTI
"…confesses his guilt"; NETHER HOUSE "…Henry YIIL"; RECIPROCAL CONTRACT "…bilateral contract";
PERFORM "…other than payment" — could equally continue on the page). Some look like true
truncation or garble (PREVIOUS QUESTION's punctuation salad; VIS ending "force;"). Without the
scan image, period-loss and truncation are indistinguishable — the candidate marker says
precisely that. LOUD NOTE TO THE COORDINATOR: C1's dominant failure mode across 601 loci is
probably OCR period-loss on complete entries, NOT missing text. Ship ONLY as candidate; do not
promote to strong in the builder, and the printed marker wording should say "possibly
incomplete in the scan" rather than asserting a break. If any rule were to be dropped for
noise, this is the only candidate for that conversation — my recommendation is nevertheless to
SHIP it as candidate, because the alternative (silence) would let genuine truncations hide
among period-losses, which is the opposite of this task's doctrine.

### C2 (candidate) — OPEN-SCAN sample entries (sample of 44):
  - idx 5664 — GELD — In Saxon law. Money or tribute. A mulct, compensation, value, price. Angeld was the single value of a thing; t…
  - idx 2226 — CLAUSUM — Lat. Close, closed up, seal- ed. Inclosed, as a parcel of land.…
  - idx 8750 — NON SEQUITUR — Lat. It does not fol- low. /  / Non solent qn« abundant vitiare scrip tnr as. Superfluities [things, which aboundj…
  - idx 10633 — REFUND — To repay or restore; to re- turn money bad by one party of another SeeRackllff v. Greenbush, 93 Me. 99, 44 Atl…
  - idx 9499 — PERSONNE — Ft. A person. This term la applicable to men and women, or to either. Civ. Code Lat. art. 3522, § 25. /  / Perspic…
  - idx 2717 — CONSUETUDO — Lat A custom; an established usage or practice. Co. Litt. 58. Tolls; duties; taxes. Id. 586. /  / — Consuetudo Ang…
  - idx 8919 — OCCUPATION — L Possession; control;1 tenure; use. /  / In its usual sense "occupation” is where a per- son exercises physical c…
  - idx 3899 — D IS AFFIRM — To repudiate; to revoke a consent once given ; to recall an affirmance. To refuse one's subsequent sanction to…
  - idx 11367 — SER VITUS — Lat In the civil law. Slavery ; bondage ; the state of service. De- fined as “an Institution of the convention…
  - idx 1403 — BETTER EQUITY — See Equity.…
VERDICT C2: precision is definitional — these 44 entries carry the audit's standing
scan-verification OPEN state. The marker is a whole-entry verification state (anchor ENTRY),
not a claimed break point; the excerpts show ordinary entries whose text has simply never been
checked against the scan image. SHIP as candidate with the audit reason verbatim.

## STEP 6 — What was NOT done (bounds kept)

- No text repaired, completed, corrected, or invented anywhere. markers.json contains loci,
  strengths, rules, anchors, reasons — no proposed readings.
- No git push. All outputs are local to this folder.
- No rule tuned silently: the only two refinements (S4 token-core; S4 ordinal exclusion) are
  stated in the detector's comments, this log, and the census, with before/after counts.

## Outputs

- detect_scan_markers.py — the detector (runnable; re-running reproduces markers.json and
  census-data.json byte-for-byte in counts; samples use fixed seed 20261025).
- markers.json — {entry_index: [{strength, rules, anchor, reason}]}; 775 markers, 772 entries.
- marker-census.md — totals, per-rule counts, C1 accounting, S5/C2 mapping logs, and the
  COMPLETE merged locus list (775 rows) for retracing.
- census-data.json — machine-readable intermediate (counts, per-rule samples, full hit list)
  retained so any number in the census or this log can be re-derived without re-running.
- worker-log.md — this file.
