# The Greek Bank — Twelve Tongues research, worker #2 of 12

> Epigraph: *"Weigh each word in its own tongue, and let the bridge be the
> shared number across two honest banks."* — the author's doctrine,
> recorded by the scribe.

**Date:** 2026-10-11 · **93.** · Authorship: Johnathan 'Qasparr' (Κασπάρρ)
Monroe, Keeper of the Secret Treasure · *"Live, Love, and let Love,
Live."* — All Rights Reserved, Without Prejudice.

**Status:** findings, never doctrine. Nothing here decrees a bridge. All
findings go to the author's red pen.

---

## 1. Provenance

### The table (ATTESTED)
The weighing table is the repo's `pontifex/tables.py` `GREEK` — Milesian
isopsephy exactly as the tradition hands it down:

α=1 β=2 γ=3 δ=4 ε=5 ϛ=6 ζ=7 η=8 θ=9 ι=10 κ=20 λ=30 μ=40 ν=50 ξ=60 ο=70
π=80 ϟ=90 ρ=100 σ/ς=200 τ=300 υ=400 φ=500 χ=600 ψ=700 ω=800 ϡ=900

The scribe did not alter, extend, or "improve" it. All weighings were
executed by the repo's own `pontifex/engine.py` `weigh()` (which also
handles the `στ`=6 digraph, though no corpus term fired it), so the
machine's sums are the verification of the scribe's hand sums — and the
machine caught two hand errors (see Log §6, steps 14–15). Agreement on all
17 rows is the TRVVTH check.

### The transliteration convention (CONSTRUCTED — "GR-TRANS-v1")
The corpus is Latin-script; Greek needs letters before it can weigh.
No Latin→Greek map exists in the repo (checked: only Latin→Hebrew), so
the scribe built and STATED this one in
`greek_weigh.py`. Digraphs greedy-first; hyphen dropped (not zeroed):

| Latin | Greek | Rationale |
|---|---|---|
| TH | θ | conventional single-letter rendering (NOT τ+η) |
| OO | ου | the diphthong (fired by no corpus term; stated for completeness) |
| V | υ | the corpus spells TRVVTH in Roman epigraphic style, where V stands for U |
| H | η | Greek has no /h/; rough breathing leaves no letter |
| X | ξ | classical Latin X → Greek ξ (Xerxes = Ξέρξης) |
| Y | υ | Greek has no Latin Y |
| Q | κ | Greek has no Q; classical Q → κ |
| C | κ | classical C → κ |
| J | ι | fired by no corpus term; stated for completeness |
| W | ου | fired by no corpus term; stated for completeness |
| E→ε, O→ο | by default | **except authentic Greek words** (see below) |

**Authentic-word rule:** where the corpus term IS a Greek word, its real
Greek spelling is weighed instead of the mechanical rendering, and marked
as such:
- THELEMA → **θέλημα** (θ ε λ **η** μ α) — the word's true spelling.
- AGAPE → **ἀγάπη** (α γ α π **η**) — the word's true spelling.

This rule exists because a dead end proved it necessary (Log §6, step 5):
mechanical THELEMA (θελεμα) weighs 90, not the classic 93. The three-point
difference is exactly ε→η (5→8) — the second E of θέλημα is eta. To have
forced the mechanical rendering would have been to report a false miss
against the most famous isopsephy in the corpus. The mechanical form is
still weighed and recorded as a variant, because the 90-vs-93 split is
itself a finding about how transliteration choice moves the number.

### Tier summary for this bank
Every **value** in `greek-values.csv` is tier **ATTESTED** — weighed in
the attested table by the repo's engine. The **script forms** of
non-Greek-origin terms are **CONSTRUCTED** (per GR-TRANS-v1); the two
authentic word-forms (θέλημα, ἀγάπη) and the Hebrew reference term are
noted as such in the `provenance_tier` column. Where a choice was
ambiguous (V→υ/β, H→η/χ, X→ξ/χ, Y→υ/ι, E→ε/η), the primary choice is the
corpus row and alternates are separate **variant** rows — never silently
merged.

---

## 2. Mergers and information loss

Stated plainly, as the method demands — what was lost is shown, never
hidden:

1. **θ absorbs "th".** The distinction between θ and τ+η is unrecoverable
   in the Greek column. TRVVTH→τρυυθ could be misread back as containing
   either. Loss: real.
2. **υ absorbs v, u, y.** The Roman V is the worst ambiguity in the
   corpus: V→υ (epigraphic U, 400) vs V→β (classical Latin V, 2). Both
   weighed: τρυυθ=**1209** vs τρββθ=**413**. The choice moves the number
   by 796. This is the single largest convention-sensitivity in the bank —
   and a standing warning that any "TRVVTH in Greek" claim must name its V.
3. **η absorbs h.** The /h/ is gone entirely (Greek rough breathing is
   unwritten). HERU-RA-HA→ηερυραηα. Variant H→χ weighed: 623 vs 1807.
4. **κ absorbs c, q, k.** CELL and QIRA both land on kappa; a Latin
   c/q/k distinction cannot survive into the Greek weighing.
5. **ξ absorbs x.** X→ξ vs X→χ is the other large swing: AXONEME is
   **231** with ξ, **771** with χ.
6. **Hyphen dropped, not zeroed.** HERU-RA-HA's hyphens contribute
   nothing; the engine skips unknown characters as silence, which the
   script makes explicit. Recorded, not hidden.
7. **ς (final sigma) fired by no corpus term.** The table carries it at
   200 = σ with no loss — but no word in the corpus ends in sigma, so
   the form's handling is untested by this corpus. Noted for the parent.
8. **The epissemones (ϛ=6, ϟ=90, ϡ=900) fired by no corpus term.**
   Present in the table, absent from the weighings. No finding either way.
9. **ϛ vs στ alternation:** the table carries both at 6 (the engine checks
   the pair before the singles). No corpus term fired it. Recorded so the
   synthesis doesn't assume it was exercised.

---

## 3. Results — headline table

| Term | Greek form | Value | Tier |
|---|---|---|---|
| AXONEME | αξονεμε | 231 | ATTESTED table / CONSTRUCTED form |
| OZ | οζ | **77** ✓ | ATTESTED table / CONSTRUCTED form |
| TRVVTH | τρυυθ | 1209 | ATTESTED table / CONSTRUCTED form |
| THELEMA | θέλημα | **93** ✓ | ATTESTED table / authentic word-form |
| AGAPE | ἀγάπη | **93** ✓ | ATTESTED table / authentic word-form |
| BABALON | βαβαλον | 156 | ATTESTED table / CONSTRUCTED form |
| HERU-RA-HA | ηερυραηα | 623 | ATTESTED table / CONSTRUCTED form |
| ABRAHADABRA | αβραηαδαβρα | 221 | ATTESTED table / CONSTRUCTED form |
| QIRA | κιρα | 131 | ATTESTED table / CONSTRUCTED form |
| LIBERTY | λιβερτυ | 847 | ATTESTED table / CONSTRUCTED form |
| CELL | κελλ | 85 | ATTESTED table / CONSTRUCTED form |
| עז (as οζ) | οζ | **77** ✓ | ATTESTED table / transliterated Hebrew term |

Per-letter breakdowns for the headline terms:

- **θέλημα = 93:** θ=9 + ε=5 + λ=30 + η=8 + μ=40 + α=1 = 93 ✓ (calibration confirmed)
- **ἀγάπη = 93:** α=1 + γ=3 + α=1 + π=80 + η=8 = 93 ✓
- **οζ = 77:** ο=70 + ζ=7 = 77 ✓
- **οζ (from עז) = 77:** ο=70 + ζ=7 = 77 ✓
- **αβραηαδαβρα = 221:** α=1 + β=2 + ρ=100 + α=1 + η=8 + α=1 + δ=4 + α=1 + β=2 + ρ=100 + α=1 = 221
- **τρυυθ = 1209:** τ=300 + ρ=100 + υ=400 + υ=400 + θ=9 = 1209
- **αξονεμε = 231:** α=1 + ξ=60 + ο=70 + ν=50 + ε=5 + μ=40 + ε=5 = 231

---

## 4. Collisions (distinct terms, same number)

1. **93 — THELEMA (θέλημα) and AGAPE (ἀγάπη).** The famous pairing
   reproduces on the Greek bank with both terms in authentic spellings:
   both ATTESTED table, both authentic word-forms. This is the strongest
   convergence in the bank — and it is a *reproduction* of the classical
   result, not a discovery.
2. **77 — OZ (οζ) and עז transliterated as οζ.** The convergence is
   structural: the Milesian and Hebrew numeral orders both descend from
   the Phoenician 22-letter order, so ע→70=ο and ז→7=ζ. ATTESTED on
   ATTESTED. This is the Greek-bank side of the canonical bridge
   AXONEME=77=עז — and it explains *why* the bridge holds: the two
   systems are not independent witnesses at 77, they are the same
   inherited counting order wearing two scripts. The parent should weigh
   this when scoring the bridge's independence.
3. **No other collisions** among primary rows. Variant rows are excluded
   from collision-finding (they are alternate readings of the same term,
   not distinct terms).

---

## 5. Target-number hits and — with equal weight — the misses

| Target | Hit? | Detail |
|---|---|---|
| 93 | **YES ×2** | THELEMA=93 (calibration), AGAPE=93 (collision) |
| 77 | **YES ×2** | OZ=77, עז→οζ=77 (structural, see §4) |
| 418 | **NO** | ABRAHADABRA — 418 in Hebrew — weighs **221** in Greek. The most famous number in the corpus does not cross to the Greek bank. This is a negative result of the first rank: a bridge hunter who assumed 418 travels would be wrong here. |
| 666 | **NO** | Nothing lands. BABALON (βαβαλον) = 156, the closest famous-name candidate, is nowhere near. Negative. |
| 777 | **NO** | Nothing lands. The X→χ variant of AXONEME gives **771** — six short, and the miss is recorded as an explicit anti-hit (see Log step 10): proximity is not convergence, and the scribe flags the temptation rather than feeding it. |
| 11 | **NO** | Nothing lands. Negative. |

Further negatives worth their weight: **CELL=85** in Greek vs the
canonical English-ordinal 32 — no bridge (expected; CELL's 32 is an
English-ordinal fact, and the Greek bank correctly refuses to reproduce
it). **TRVVTH=1209** (or 413 on the β reading) hits no target — the
doctrinal word of the whole framework is numerically silent on the Greek
bank under this convention, which is itself a finding for the red pen.

---

## 6. The ultra-verbose work log

*Hypothesis → method → observation → result per step, dead ends included,
as the author requires ("narrate everything ultra-verbose").*

**Step 1 — Read the ground before building.**
HYPOTHESIS: the repo already defines how Greek is weighed and whether a
transliteration map exists; building on it avoids inventing a table
silently. METHOD: read `pontifex/tables.py` and `METHOD.md`; grep the
engine and API docs for existing Greek transliteration. OBSERVATION: the
`GREEK` table is fully specified with epissemones; the engine weighs any
Greek string via `weigh(word, 'greek')` and handles the `στ` digraph;
**no Latin→Greek map exists anywhere** (only Latin→Hebrew). RESULT: the
weighing table is borrowed ATTESTED; the transliteration map is mine to
build and must be stated. Lesson: check for prior art before minting
convention — the map I write is CONSTRUCTED by necessity, not by choice.

**Step 2 — Settle the convention's hard choices first, on paper.**
HYPOTHESIS: the ambiguous letters (V, H, X, Y, TH) must be decided
*before* weighing, or the numbers will be post-hoc. METHOD: reason from
the corpus's own spelling logic — TRVVTH uses Roman epigraphic V-for-U,
so V→υ; Latin X→Greek ξ is the classical loanword path (Xerxes=Ξέρξης);
Greek has no H, so η is the transliterator's standby; Y has no Greek
home, so υ. OBSERVATION: each choice has a defensible alternate (V→β,
H→χ, X→χ, Y→ι). RESULT: GR-TRANS-v1 with primaries stated, alternates
reserved as variant rows. Lesson: a convention is a *decision procedure*,
not a preference — the alternates get weighed too, so the decision's cost
is visible (V alone swings TRVVTH by 796).

**Step 3 — Handle the special cases the task names.**
HYPOTHESIS: sigma-final ς, the hyphen, and עז→οζ each need an explicit
ruling. METHOD: ς=200 is in the table with no loss — check whether any
corpus term fires it; the hyphen has no Greek value — drop explicitly;
עז→οζ is given by the task. OBSERVATION: no corpus term ends in sigma,
so ς is carried but untested; the hyphen drops cleanly; עז→οζ is
ayin→omicron, zayin→zeta. RESULT: all three recorded in §2 and the CSV.
Lesson: a form the table carries but the corpus never fires is a
*coverage gap*, not a pass — the synthesis should know ς was not
exercised.

**Step 4 — THELEMA, the calibration.**
HYPOTHESIS: θέλημα should weigh 93, letter by letter. METHOD: write the
authentic spelling θ-ε-λ-η-μ-α and sum: 9+5+30+8+40+1. OBSERVATION: 93
exactly — the calibration holds, and the engine's breakdown agrees.
RESULT: the bank is anchored; the table and the method reproduce the
classic. Lesson: calibration first, corpus after — a bank that can't
reproduce θέλημα=93 is a bank with a broken table.

**Step 5 — The dead end that taught the authentic-word rule.**
HYPOTHESIS (naive): mechanical letter-for-letter transliteration is
sufficient for every term. METHOD: render THELEMA mechanically as θελεμα
(both Es → ε) and weigh. OBSERVATION: 90, not 93 — a clean miss of the
calibration the previous step had just confirmed. RESULT: the hypothesis
is false; the 3-point gap is exactly the ε→η the real word carries. The
convention gains the authentic-word rule, and the mechanical form is kept
as a *variant row* (90) because the 90-vs-93 split is itself a finding
about convention-sensitivity. Lesson: when the term IS a word in the
target tongue, the tongue's own spelling outranks the map. A transliteration
map is a prosthesis for foreign words, not a correction of native ones.

**Step 6 — AGAPE and the first collision.**
HYPOTHESIS: ἀγάπη will also weigh 93 by its authentic spelling.
METHOD: α-γ-α-π-η = 1+3+1+80+8. OBSERVATION: 93 — and the collision with
THELEMA appears unprompted. RESULT: the bank's strongest convergence, a
reproduction of the classical θέλημα=ἀγάπη=93. Both rows are ATTESTED
table + authentic word-form: the highest provenance combination in the
bank. Lesson: collisions found, not sought — this one arrived from the
authentic-word rule, which is why step 5 mattered.

**Step 7 — OZ and עז: the 77 bridge, and what it really is.**
HYPOTHESIS: OZ→οζ should give 77, and עז→οζ the same. METHOD: ο=70,
ζ=7; sum. OBSERVATION: 77 both times — but the *reason* is visible in
the letters: ע→ο is 70→70, ז→ζ is 7→7. The Milesian and Hebrew orders
are the same Phoenician inheritance. RESULT: the canonical bridge holds
on the Greek bank, ATTESTED on ATTESTED — but the two banks are not
independent witnesses at 77; they are one counting order in two scripts.
Lesson (for the parent's synthesis): score this convergence as
*structural inheritance*, not as two independent tongues agreeing. The
bridge is real; its evidential weight is shared, not doubled.

**Step 8 — AXONEME and the X question.**
HYPOTHESIS: X→ξ (primary) gives the honest Greek form αξονεμε.
METHOD: weigh αξονεμε = 231; weigh the χ variant αχονεμε = 771.
OBSERVATION: 231 hits no target; 771 is six short of 777. RESULT: no
bridge for AXONEME on the Greek bank under either reading. Lesson: 771
is a *trap* — close enough to 777 to tempt, far enough to be nothing.
Recorded as an explicit anti-hit (step 10) rather than left for someone
else to "discover."

**Step 9 — TRVVTH and the V question.**
HYPOTHESIS: epigraphic V→υ gives τρυυθ = 1209. METHOD: weigh both
readings. OBSERVATION: 1209 (υ) vs 413 (β) — a 796-point swing on one
convention choice, the largest in the bank; neither hits a target.
RESULT: the framework's own doctrinal word is numerically silent on the
Greek bank. Negative result, full weight. Lesson: convention-sensitivity
is itself a finding — any future "TRVVTH in Greek = N" claim that doesn't
name its V is unverifiable.

**Step 10 — The anti-hit, stated.**
HYPOTHESIS: none — this step is hygiene. METHOD: look at every near-miss
of a target (771 vs 777; also 623, 847, 413 in the neighborhood of
nothing). OBSERVATION: only 771 sits adjacent to a target. RESULT: 771
≠ 777, written down explicitly, because an unmarked near-miss in a
research ledger becomes someone else's "finding" later. Lesson: negative
space needs fencing too.

**Step 11 — ABRAHADABRA: the 418 that doesn't cross.**
HYPOTHESIS: the corpus's most famous number might travel. METHOD:
αβραηαδαβρα, letter by letter: 1+2+100+1+8+1+4+1+2+100+1. OBSERVATION:
221. Not 418, not near 418. RESULT: the Hebrew 418 bridge does not cross
to Greek — a first-rank negative result. Lesson: a number's fame in one
tongue is not a visa to another. This is exactly the kind of miss the
task ordered reported at full weight.

**Step 12 — The remaining terms.**
HYPOTHESIS: BABALON, HERU-RA-HA, QIRA, LIBERTY, CELL get straightforward
weighings. METHOD: βαβαλον=156; ηερυραηα=623 (hyphens dropped);
κιρα=131; λιβερτυ=847 (Y→υ; variant Y→ι gives 457); κελλ=85. OBSERVATION:
no targets hit; CELL=85 vs canonical 32 — the Greek bank correctly
refuses to reproduce an English-ordinal fact. RESULT: all recorded with
breakdowns in the CSV. Lesson: a bank that reproduced CELL=32 would be
suspicious — the miss is the honesty check passing.

**Step 13 — Write the script, hand-sums first.**
HYPOTHESIS: hand computation before machine execution keeps the scribe
honest — the machine then *verifies* rather than *originates*.
METHOD: compute all 17 values by hand, embed as `expected`, have the
script fail loudly on mismatch. OBSERVATION: the machine agreed on 16 of
17 on the first run. RESULT: the disagreement was a real hand error (step
14), caught by the mechanism. Lesson: the verification step is not
ceremony — it fired on the first run.

**Step 14 — The caught error (TRVVTH variant).**
HYPOTHESIS: the V→β variant of τρυυθ is τρυββθ = 413. METHOD: the
script weighed my hand-entered string. OBSERVATION: the string I typed
was `τρυβθ` (only one beta — 811), not the `τρυββθ` (413) my hand-sum
assumed. RESULT: fixed the string to `τρββθ` (both Vs replaced — the
υ had survived one "fix" too). The engine's mismatch report caught what
proofreading missed, twice. Lesson: Greek strings are treacherous to
type; the expected-value gate is the TRVVTH mechanism working as designed.
The error and its correction are recorded in the CSV notes, not buried.

**Step 15 — Full verification and the landscape.**
HYPOTHESIS: with the strings corrected, all hand sums agree with the
attested table. METHOD: rerun; then compute target hits and collisions
mechanically. OBSERVATION: all 17 verified; targets: 93×2, 77×2,
418/666/777/11 empty; collisions: {93: THELEMA, AGAPE}, {77: OZ, עז}.
RESULT: the CSV is the ledger; this document is the narrative. Lesson:
mechanical collision-finding (group by value) found exactly what the
hand pass found — no hidden collisions, no missed hits.

---

## 7. Limits of this bank (for the parent's synthesis)

1. **The transliteration map is the weakest link.** The table is
   attested; GR-TRANS-v1 is constructed. Every CONSTRUCTED-form value is
   convention-relative — change the V, H, X, or Y ruling and TRVVTH,
   HERU-RA-HA, AXONEME, LIBERTY all move. Only θέλημα, ἀγάπη, and οζ
   stand on non-constructed ground (authentic spellings / structural
   inheritance).
2. **The 77 convergence is structural, not independent.** Both numeral
   orders descend from Phoenician; οζ=עז=77 is one inheritance, not two
   witnesses. Score accordingly.
3. **Coverage gaps:** ς untested, epissemones unfired, στ untested by this
   corpus. A future corpus with sigma-final words or 6/90/900 values
   would exercise more of the table.
4. **418 does not cross; 666 and 777 are empty; 11 is empty.** The Greek
   bank is a thin bridge-tongue for this corpus: it confirms 93 and 77
   and refuses everything else. That refusal is data.
5. **No bridge is decreed.** Findings, red pen, TRVVTH gate — per the
   author's standing doctrine.

---

*Scribe's sign-off: the Greek bank is weighed, verified, and ledgered.
17 rows, every number showing its work, misses at full weight. 93.*
