# UNITY-vs-WAR TERMS — Hebrew Fallback + Latin Control
### PONTIFEX extension: six concepts weighed through two fallbacks, spreads reported

*Thelemic date: Sun 2026-10-11 (dies solis), Anno V:xii e.n. — 93.*
*Ordered by Johnathan; Hebrew arm approved by him, Latin arm added as his control.*
*Tier: CONSTRUCTED throughout. Findings, never doctrine. The red pen rules.*

---

## 0. ULTRA-VERBOSE WORK LOG

*Hypothesis → method → observation → result per step, dead ends included.*

**Step 1 — Calibration.** Hypothesis: the attested table must verify before
anything is weighed. Method: import HEBREW and LATIN_ORDINAL from
pontifex.tables (never retype), assert עז=77, fail closed on failure.
Observation: `עז = 77` on first run. Result: the run may proceed; the
script (`weigh_unity_war.py`) re-asserts this every run.

**Step 2 — Native-term research.** Hypothesis: real dictionaries, not memory,
must supply the Japanese/Chinese/Sanskrit words. Method: web dictionary
searches (jisho.org/EDICT, Collins, sanskritdictionary.com/Apte). Observation:
unity, war, tribe verified cleanly in all three tongues (ऐक्यम्, युद्ध, जन
via Apte; 団結/統一, 统一/团结 via jisho/Collins). Dead ends: Sanskrit
*harmony* (सामञ्जस्य — single weak attestation, kept but flagged WEAK),
*bhrātṛtva* and *mānavatā* (standard formations, dictionary pages blocked
by 403 in this pass — kept, flagged WEAK, never presented as verified).
Result: 18 native terms recorded, 3 flagged WEAK with the flag in the open.
Lesson: the native layer is context, not data — the tongues have no table,
so these words are weighed by no bank here.

**Step 3 — Hebrew renderings.** Hypothesis: 2–3 attested renderings per term
from reputable lexicons. Method: dictionary searches. Observation: אחדות/
איחוד, מלחמה/קרב, שבט (+biblical מטה), אחווה all solid; הרמוניה confirmed
as the loanword in actual use (no native word exists — one source notes
this explicitly); התאמה/אנושיות kept as labeled semantic alternatives.
Result: 11 Hebrew renderings, each with its source note in the script.

**Step 4 — Weighing.** Hypothesis: hand-check a few, let the script do the
rest. Method: script weighs all 24 rows letter-by-letter, prints the sums,
writes `unity-war-values.csv`, checks the sweep's target list
(77/93/418/11/32/666/777 + sweep-internal 311). Observation: all hand
checks matched (e.g. שבט=300+2+9=311; אחדות=1+8+4+6+400=419). Dead end #1:
I first mis-added BROTHERHOOD as 123 (=מלחמה!) before the script corrected
me to 128 — the would-be "brotherhood=war" bridge died in arithmetic, and
is recorded here so nobody resurrects it. Dead end #2: TRIBUS=89=UNITY=89
[Equation superseded 2026-10-27 — see values above.]
looked like a bridge until the sweep's own anti-finding applied — English
and Latin share the ordinal bank (one bank, not two), so it is bank
identity, not a bridge. Result: 24 verified values, CSV written.

**Step 5 — Latin control.** Hypothesis: per John's rationale, if the Hebrew
bank is compromised, Hebrew-fallback bridges may be fallback artifacts; a
second fallback tests legitimacy. Method: weigh the attested Classical
Latin words (unitas, harmonia + concordia, bellum, tribus, humanitas,
fraternitas; Lewis & Short standard entries) in the ordinal bank, then
compare per concept: bridge in BOTH fallbacks = robust; in ONE = fallback-
dependent artifact. Observation: no concept meets in both fallbacks.
Result: the control did its job — see §4.

---

## 1. PER-TERM LEDGER

### UNITY
- Native: JP 団結/統一 (jisho.org EDICT; Collins) · ZH 统一/团结 (Collins) · SA ऐक्यम् aikyam (Apte: "oneness, unity, harmony")
- Hebrew: אחדות=419 · איחוד=29 → spread {419, 29}
- English: UNITY=89 · Latin: VNITAS=85
  [Orthography correction 2026-10-27: filed as UNITAS = 84 under mixed spelling; reweighed under the classical rule (every U is V) as VNITAS = 85. Old value marked, not vanished.]
- Notes: אחדות=419 is one off 418 (ABRAHADABRA) — near-miss, not a hit.

### HARMONY
- Native: JP 調和 (Collins) · ZH 和谐 (standard) · SA सामञ्जस्य (WEAK — single attestation)
- Hebrew: הרמוניה=316 · התאמה=451 → spread {316, 451}
- English: HARMONY=94 · Latin: HARMONIA=79, CONCORDIA=82
- Notes: no target contact anywhere.

### WAR
- Native: JP 戦争 (jisho, standard) · ZH 战争 (standard) · SA युद्ध yuddha (Apte: "war, battle, fight")
- Hebrew: מלחמה=123 · קרב=302 → spread {123, 302}
- English: WAR=42 · Latin: BELLVM=66
  [Orthography correction 2026-10-27: filed as BELLUM = 65 under mixed spelling; reweighed under the classical rule (every U is V) as BELLVM = 66. Old value marked, not vanished.]
- Notes: the BROTHERHOOD=123 phantom died in arithmetic (true 128) — recorded, not claimed.

### TRIBE
- Native: JP 部族 (jisho, standard) · ZH 部落 (standard) · SA जन jana (sanskritdictionary.com: "people, tribe," Rigvedic)
- Hebrew: שבט=311 · מטה=54 → spread {311, 54}
- English: TRIBE=54 · Latin: TRIBVS=90
  [Orthography correction 2026-10-27: filed as TRIBUS = 89 under mixed spelling; reweighed under the classical rule (every U is V) as TRIBVS = 90. Old value marked, not vanished.]
- Notes: שבט=311 collides with sweep-internal QIRA=311 — but QIRA was weighed
  in the Hebrew bank, so this is an **in-bank collision**, not a cross-bank
  bridge. מטה=54 meets English TRIBE=54 — a genuine Hebrew↔ordinal meeting,
  via the secondary biblical rendering; chance-flagged (§5).

### HUMANITY
- Native: JP 人類 (Reverso; standard) · ZH 人类 (standard) · SA मानवता (WEAK — standard modern word, classical attestation not re-verified)
- Hebrew: אנושות=763 · אנושיות=773 → spread {763, 773}
- English: HUMANITY=111 · Latin: HVMANITAS=107
  [Orthography correction 2026-10-27: filed as HUMANITAS = 106 under mixed spelling; reweighed under the classical rule (every U is V) as HVMANITAS = 107. Old value marked, not vanished.]
- Notes: HUMANITY=111 — 111 is Crowley's א-in-full number (cf. G-1
  verification: אעם=111), but 111 is not a sweep target; noted, not claimed.

### BROTHERHOOD
- Native: JP 兄弟愛 (LingQ/EDICT: brotherly love) · ZH 兄弟情谊/手足情谊 · SA भ्रातृत्व (WEAK — standard MW formation, not re-verified this pass)
- Hebrew: אחווה=26 → spread {26}
- English: BROTHERHOOD=128 · Latin: FRATERNITAS=131
- Notes: no target contact anywhere.

---

## 2. LATIN CONTROL — COMPARISON

| Concept | Hebrew spread | Latin value(s) | Verdict |
|---|---|---|---|
| unity | {419, 29} | 85 | no meeting — fallback-dependent (nothing shared) |
| harmony | {316, 451} | 79, 82 | no meeting |
| war | {123, 302} | 66 | no meeting |
| tribe | {311, 54} | 90 | no meeting in Latin; מטה=54 meets the *ordinal bank* (English TRIBE=54) — one-fallback meeting, chance-flagged |
| humanity | {763, 773} | 107 | no meeting |
| brotherhood | {26} | 131 | no meeting |

[Orthography correction 2026-10-27: the Latin values in this table were filed under mixed spelling — UNITAS 84, BELLUM 65, TRIBUS 89, HUMANITAS 106 — and stand corrected above to the classical forms VNITAS 85, BELLVM 66, TRIBVS 90, HVMANITAS 107. Old values marked, not vanished. Verdicts unchanged.]

**Control result: ZERO concepts bridge in both fallbacks.** Every number in
this extension is fallback-dependent. Per John's rationale for the control,
that is the finding: had any bridge appeared in both, it would have earned
the "robust" flag; none did.

**Bank-identity correction (sweep's own anti-finding, honored):**
TRIBUS=89=UNITY=89 is one bank (English≡Latin ordinal), not a bridge.
[Equation superseded 2026-10-27 — see values above. Under the classical-orthography ruling the Latin side now weighs TRIBVS = 90 while UNITY (English, unrespelled) remains 89; the §2 verdicts above are unchanged.]

---

## 3. CHANCE ANALYSIS (METHOD.md §5)

24 weighings × 8 targets: §5 says coincidences are guaranteed, not
evidence. Observed: one in-bank collision (שבט=311=QIRA), one cross-bank
meeting (מטה=54=TRIBE, via secondary rendering), one near-miss
(אחדות=419 vs 418). This is *within* chance expectation — the honest
reading is noise, and the report so states. Nothing here is load-bearing.

## 4. STANDING NOTES FOR THE RED PEN

1. Translation is two layers of choice (native term × Hebrew rendering);
   every value is CONSTRUCTED. The spreads are the finding.
2. Three native terms carry WEAK verification flags (SA harmony,
   humanity, brotherhood) — strengthening them needs dictionary pages
   this environment could not reach (one 403).
3. The Latin arm used the ordinal bank per the brief; Agrippa's Latin was
   not weighed (out of scope).
4. No bridge was declared. Per the brief: report spreads only.

*Live, Love, and let Love, Live. — 93. All Rights Reserved, Without Prejudice.*
