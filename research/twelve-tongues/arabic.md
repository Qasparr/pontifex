# Arabic bank — Twelve Tongues research (worker #4)

*Findings, never doctrine. Everything below goes to his red pen.*

> "Weigh every word in its own tongue." — the binding doctrine of the research.

## 1. Provenance of the table

The weighing uses `ARABIC_ABJAD` from `pontifex/tables.py` (read in full before
work began): the abjad numerals in **Eastern order**, ا=1 … غ=1000, tier
**ATTESTED** — recorded as the tradition hands it down; the scribe does not
improve it. The Maghrebi (western) order differs in exactly six letters
(ص 90→60, ض 800→90, س 60→300, ظ 900→800, غ 1000→900, ش 300→1000); the Eastern
order is primary per `tables.py`, the Maghrebi values are computed as a
parallel and reported wherever they differ — noted, not hidden.

## 2. Transliteration convention — "scribe MSA-phonetic-v1"

No standard transliteration of this corpus into Arabic exists, so the scribe
built one and states every choice. The convention follows modern standard
Arabic loanword spelling (journalism/dictionary norms) where a norm exists:

- **Vowels:** long vowels get matres — a→ا, i/e→ي, o/u→و. Short vowels become
  harakat (fatḥa/damma/kasra), which score **zero** — information loss,
  reported per term. Word-initial vowels sit on hamza (أ/إ/آ), counted as the
  carrier letter ا=1 (a hamza=0 variant is named in §6).
- **P → ب** (merges p/b — standard; no P occurs in the corpus, so the merger
  fires nowhere, but the loss is on the record).
- **TH (θ) → ث** (standard θ rendering; *not* ت). The ت alternative is weighed
  as a variant wherever TH occurs.
- **V → ف** (standard; *not* و). **W → و** (no W in corpus).
- **O → و** (merges o/u; Arabic itself merges و as consonant w and vowel o/u —
  source-script loss, inherent).
- **E/I/Y → ي** (three-way merger; the heaviest vowel loss in the bank).
- **X → كس** (digraph split — standard, e.g. أكسجين for oxygen).
- **G (English) → ج**; **G (Greek γ, in AGAPE) → غ** (Egyptian convention for
  Greek gamma). This is the single most convention-sensitive choice in the
  bank: it swings AGAPE between 1014 and 17.
- **J → ج** (merges j/g — standard; no J in corpus).
- **C → س** before e/i, **→ ك** elsewhere.
- **VV in TRVVTH → single و** — gemination collapses to one letter (a shadda
  would double it; the shadda-doubled value is weighed as a variant).
- **Hyphen in HERU-RA-HA → space** (value 0).
- **H → ه** (soft ha) in the base forms. Egyptological accuracy would prefer
  ح (heavy ḥ — Egyptian *ḥr.w* "Horus"), so the ح variants are weighed and
  reported; the base form stays ه for consistency with the English-derived
  convention.

## 3. Results (Eastern order, attested table)

| term | Arabic form | value | headline |
|------|-------------|------:|----------|
| AXONEME | اكسونيم | 187 | = 11×17 — arithmetic note; does **not** carry the 77 |
| OZ | أوز | 14 | — |
| TRVVTH | تروث | 1106 | — |
| THELEMA | ثيليما | 591 | (θ→ت variant: 491) |
| AGAPE | أغابي | 1014 | (G→ج variant: 17 — convention swing) |
| BABALON | بابلون | 91 | = 7×13 |
| HERU-RA-HA | هرو را ها | **418** | target hit (ح-variant: 421) |
| ABRAHADABRA | أبراهادابرا | **418** | target hit; collision with HERU-RA-HA (ح-variant: 421) |
| QIRA | قيرا | 311 | prime |
| LIBERTY | ليبرتي | 652 | — |
| CELL | سيل | 100 | Maghrebi 340 |
| عز (reference) | عز | **77** | calibration confirmed |

## 4. Target-number hits

- **418** — hit twice: HERU-RA-HA and ABRAHADABRA. Both also equal their
  Hebrew values (הרורא הא = 418; ABRAHADABRA = 418). This is partly mechanical:
  transliterating into the sister Semitic letter-stock reproduces the Hebrew
  sums almost letter-for-letter. A candidate bridge — but the mechanicality
  is the honest caveat, and the 418 hit depends on the H→ه choice (ح gives
  421 for both terms; the collision survives under either choice).
- **77** — hit only by the native reference عز. The canonical bridge
  AXONEME=77=עז does **not** cross into Arabic: Arabic AXONEME = 187.
- **666, 777, 93, 11** — no direct hits. Negative result, reported at full
  weight. (Arithmetic observations, not hits: 187 = 11×17; 418 = 2×11×19;
  91 = 7×13.)

## 5. Collisions

- **418: HERU-RA-HA = ABRAHADABRA.** Different terms, same number — and the
  collision holds under both H-conventions (418/418 with ه, 421/421 with ح).
  Under ه both equal the Hebrew 418 values; under ح both shift together.
  The collision is robust to the one defensible H-alternative; it is not
  robust to, e.g., the Maghrebi order (neither term contains a differing
  letter, so it is — both stay 418/421 under Maghrebi too).
- **No other collisions** in the corpus.

## 6. Information loss and mergers

1. **E/I/Y → ي** — total merger of three Latin vowels (fires in THELEMA,
   AGAPE, QIRA, LIBERTY, CELL).
2. **O/U → و** — merges o and u, plus Arabic و's own w/vowel ambiguity
   (fires in AXONEME, OZ, BABALON).
3. **TH vs T** — transliteration *choice*, not loss, but the neighboring
   letters ث (500) and ت (400) are 100 apart; THELEMA swings 591↔491.
   A reader who defaults ت ("as in English loanwords often are") loses the
   θ distinction silently.
4. **Gemination lost** — VV→و (TRVVTH), LL→ل (CELL); a shadda would restore
   the doubling (TRVVTH 1106↔1112).
5. **G→γ vs G→ج** — AGAPE 1014↔17, the widest swing in the bank. This is a
   convention fork (Greek-derived word weighed by which tongue's rule?),
   and it is the honest weak point of the AGAPE value.
6. **Hamza carrier = ا** — the convention counts the seat (OZ 14, AGAPE
   1014, ABRAHADABRA 418). Under hamza=0: OZ 13, AGAPE 1013, ABRAHADABRA 417 —
   and the 418 collision would break (417 vs 418). The collision is therefore
   sensitive to the hamza choice; it holds under the stated convention and
   breaks under the zero-hamza alternative. Reported plainly.
7. **Maghrebi order** — fires only where differing letters occur: CELL
   100↔340 (س), AXONEME 187↔427 (س), AGAPE 1014↔914 (غ). The 418 and 77
   results are stable across both orders.
8. **Short vowels → harakat = 0** — unpronounced-letter distinctions vanish;
   unvocalized Arabic is inherently a consonant-skeleton weighing, like
   Hebrew without matres, but with *more* skeleton letters retained (28 vs
   22) — the two Semitic banks lose and keep different things.

## 7. Negative results

- No corpus term reaches 666, 777, 93, or 11 directly.
- The canonical 77 does not survive transliteration: AXONEME=187, OZ=14.
  Only the native Arabic word عز carries 77 in this bank — which is the
  calibration, not a discovery.
- TRVVTH, the highest term (1106), lands on nothing targeted.
- QIRA = 311 — prime, isolated, no bridge.

## 8. Ultra-verbose work log

**Step 1 — read the ground.** HYPOTHESIS: the repo already fixes the table,
so my only degrees of freedom are the transliterations. METHOD: read
`pontifex/tables.py` and `METHOD.md` before any weighing. OBSERVATION: the
table is exactly the binding doctrine's Eastern order; Maghrebi difference
already flagged in a comment; a `LATIN_TO_HEBREW` fallback map exists but no
Latin→Arabic map — Arabic is weighed natively, not via Hebrew. RESULT: the
table is attested and fixed; all construction lives in my transliteration
convention, which I must state completely.

**Step 2 — check the corpus directory.** HYPOTHESIS: sibling workers may have
started, giving me a format to match. METHOD: listed
`research/twelve-tongues/`. OBSERVATION: empty — I am first. RESULT: I set
the format (CSV + .md + weighing script); the parent will normalize across
workers if needed.

**Step 3 — draft transliterations.** HYPOTHESIS: modern standard Arabic
loanword norms cover most letters. METHOD: mapped each Latin letter,
recording P→ب, TH→ث, V→ف, O→و, X→كس, G→ج (γ→غ for AGAPE), J→ج, C→س/ك,
VV→single و, hyphen→space, hamza carrier→ا. OBSERVATION: dead end — no
single authority transliterates Thelemic corpus terms; "THELEMA" as ثيليما
vs تليما is a genuine fork in the literature. RESULT: the convention is
necessarily scribe-constructed; forked choices get weighed as variants
rather than hidden.

**Step 4 — weigh by hand first, then script.** HYPOTHESIS: hand computation
catches convention errors a script would silently encode. METHOD: summed
letter-by-letter by hand, then wrote `weigh_arabic.py` against
`ARABIC_ABJAD` to verify. OBSERVATION: the script caught two hand errors of
mine (I mis-added THELEMA's ت-variant by 10 — 481 not 491 — and my first
Maghrebi order string was hand-typed and unauditable). RESULT: hand values
corrected to the script's; the Maghrebi table was rebuilt as six explicit
overrides with an assertion — auditability improved by the failure.

**Step 5 — the hamza bug.** HYPOTHESIS: the script's first run should match
my hand sums. METHOD: compared output to hand sums. OBSERVATION: OZ=13,
AGAPE=1013, ABRAHADABRA=417 — the hamza (أ) scored zero because 'أ' ≠ 'ا'
in the table; my hand sums had counted it as 1. RESULT: this taught me the
convention needed the hamza rule stated explicitly — added to the script
(أ/إ/آ→ا) and to §2 above, with the hamza=0 alternative's effect on the 418
collision reported in §6.6 instead of buried.

**Step 6 — the 418 double hit.** HYPOTHESIS: a target hit needs stress-testing
before being called a candidate bridge. METHOD: weighed the H→ح variants
(Egyptologically the better reading for "Heru"). OBSERVATION: both terms
shift together — 418/418 → 421/421; the collision survives, the target hit
moves. OBSERVATION 2: the hit is partly mechanical — Semitic cognate
letter-stock reproduces Hebrew sums. RESULT: reported as a *candidate*
bridge with the mechanicality and the convention-dependence named, not as
a discovery.

**Step 7 — AGAPE fork.** HYPOTHESIS: γ→غ might be presumptuous. METHOD:
weighed both forks. OBSERVATION: 1014 vs 17 — the widest swing in the bank.
RESULT: base form kept at γ→غ (Greek-derived word, Egyptian convention) but
the fork is the single weakest number in the deliverable; flagged, not
smoothed.

**Step 8 — negative-result sweep.** HYPOTHESIS: something might hit 93/666/777
among the variants. METHOD: checked all variants against all targets.
OBSERVATION: nothing. RESULT: reported at full weight — a clean negative is
data.

**Step 9 — cross-checks.** Verified: عز=70+7=77 (calibration); Maghrebi
assertion passes (exactly six differing letters); 12 CSV rows match script
output; script exits 0. No git push — drafts for the red pen, per task.

## 9. Files

- `research/twelve-tongues/arabic-values.csv` — the twelve rows.
- `research/twelve-tongues/arabic.md` — this file.
- `research/twelve-tongues/weigh_arabic.py` — the weighing script (his code
  convention: thelemic form, MECHANISM/DOCTRINE comments).

93. "Live, Love, and let Love, Live."
