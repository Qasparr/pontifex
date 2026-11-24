#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
93
THE TWELVE TABLES — builder: gap register, word-cell census, and the
twelve per-tongue correspondence tables over the worked grid of
777 REVISED, every priced cell recomputed through the sealed engine
at build time.
Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
(Greek, -ARR, All Rights Reserved, Without Prejudice).
XXIV day of November, Dies Martis, Sol in Sagittario, Anno V:xii
e.n. (2026 e.v.)
Scientific Illuminism: Method of Science, Aim of Religion.
Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR,
All Rights Reserved, Without Prejudice. Right of claim hereby
reserved and coined under the authority of the Living Man.

MECHANISM: reads the TABVLA build's frozen verified register
(research/777-gap-filling/777-verification-verified.json) — never
777-REVISED.md itself beyond it, and edits nothing there (the iron
law). Emits, beside this script:
  gap_register.json   — Phase 0: every bank gap, sorted by kind
  census.json         — Phase 2: the grid's word-cells reconciled
  tables_register.json— Phase 3: 12 tongues x the full frame, each
                        word-cell NATIVE / DOOR / HOLE / FENCED,
                        each non-word cell EMPTY / GAP
DOCTRINE: a door is honest only when it is marked; a hole is a
finding, not a failure; nothing is priced across a fenced seat.
"""
import json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent))
from pontifex.engine import weigh, hangul, armenian, transliterate_latin_to_hebrew
from pontifex import tables as T

VERIFIED = ROOT / 'research' / '777-gap-filling' / '777-verification-verified.json'

# ---------------------------------------------------------------- Phase 0
# THE GAP REGISTER. Every entry: tongue, seat, kind, source, status.
# Kinds: RULING (a reading law only a pen can set), MINT (fillable by
# construction under the Flagpole where the audit proposed it),
# FENCED (the tradition's own boundary / a source-doubted seat —
# never filled). Resolutions taken at the desk 2026-11-24 under the
# founder's synergy ruling are recorded with their reasoning;
# resolutions that contradict a frozen parity exhibit are NOT taken
# — the gap is carried open and the contradiction printed.
GAP_REGISTER = [
 # --- Greek
 dict(tongue='greek', seat='stigma: ϛ (letter) and στ (digraph) both carry 6',
      kind='RULING', source='engine bank GREEK; THE-DIPLOMATIC-KEY / Greek lowercase geometry instruments (the στιγμή στ-digraph question)',
      status='RESOLVED by record: both seats stand as the bank holds them — ϛ the archaic letter-form, στ the living digraph; weigh() prices the pair before the singles. No change.'),
 dict(tongue='greek', seat='no further unseated classical letter: the 24 letters + ϛ ϟ ϡ all priced',
      kind='FENCED', source='engine bank GREEK (29 keys), enumerated at build',
      status='COMPLETE as sourced: the Milesian set is entire; nothing stands open.'),
 # --- Hebrew
 dict(tongue='hebrew', seat='mispar gadol: final letters at 500–900 (ך ם ן ף ץ uplifted)',
      kind='RULING', source='THE-777-VERIFICATION-TABVLA §IV (the corpus\u2019s two gadol partings apply gadol differently); engine fence: seat maximum 400',
      status='RESOLVED by synergy: the bank\u2019s law is FACE VALUE — finals price at their letter\u2019s value (ך 20, ם 40, ן 50, ף 80, ץ 90), the law the twin Aramaic seat shares (one weighing across the twin scripts requires one law; the census discipline caps the seat at 400). Gadol stands as an unseated variant reading; the TABVLA partings it explains stand explained, not erased. No code change. Revisable by his pen.'),
 # --- Arabic
 dict(tongue='arabic', seat='ة (tāʾ marbūṭa) carries no abjad price',
      kind='RULING', source='THE-777-VERIFICATION-TABVLA §IV (six Arabic partings of exactly ة priced as ه by the fills); engine bank ARABIC_ABJAD (28 letters)',
      status='RESOLVED by synergy: NO SEAT. ة is a script-form of tāʾ, not a twenty-ninth abjad letter; the sourced 28-letter abjad is complete as it stands. In the tables, a native word\u2019s ة is printed on its face and passes unpriced, its coordinate named — the fills\u2019 ة-as-ه pricing is a scheme, and stands parted in the TABVLA. No code change.'),
 dict(tongue='arabic', seat='ء (hamza) carries no abjad price',
      kind='RULING', source='THE-777-VERIFICATION-TABVLA §IV (الأحمر 280 vs 279); engine bank ARABIC_ABJAD',
      status='RESOLVED with the ة resolution: hamza is a carrier-less sign the abjad does not price; no seat. No code change.'),
 # --- Latin
 dict(tongue='latin', seat='W absent from the Agrippa bank (25 letters)',
      kind='FENCED', source='engine bank AGRIPPA; THE-DIPLOMATIC-KEY (NOWAR: W silent in Agrippa)',
      status='THE TRADITION\u2019S OWN BOUNDARY: Agrippa\u2019s table predates W\u2019s letterhood; the letter passes in silence and the coordinate prints wherever it bites. Never filled.'),
 dict(tongue='latin', seat='VV the refused double: no numeral seat',
      kind='RULING', source='THE-ROMAN-MISSING-LINK (VV refused_hybrid, the founder\u2019s hybrid ruling 2026-11-24)',
      status='RESOLVED by the founder\u2019s own ruling of record: VV seats as the hybrid — refused as a numeral, seated under the legend\u2019s law — in numerals.py/doubles.py, not in the letter banks. The letter tables are untouched by it.'),
 # --- Japanese
 dict(tongue='japanese', seat='the rōmaji seam questions (G3/G6 seam ruling; the labial-nasal coordinate; TOSOO oo-dress)',
      kind='RULING', source='THE-JAPANESE-TABLES Phases II–III pen list',
      status='RESOLVED by synergy: the questions govern the rōmaji SEAM (a transliteration layer), not the kana bank. The mint prices kana as written — 170 keys enumerated at build, both syllabaries entire incl. ゐゑ ヰヱ ヶ ヵ — and the Twelve Tables\u2019 Japanese door writes kana directly, so no seam ruling is load-bearing here. The seam questions stay on the pen list for the seam\u2019s own instrument. No code change.'),
 dict(tongue='japanese', seat='ー (chōonpu) unpriced at weigh()',
      kind='MINT', source='THE-JAPANESE-TABLES-PHASE-III (the ー operator door)',
      status='BY DESIGN, not a gap in the bank: ー is an operator read by the kana() door (it repeats the prior vowel\u2019s seat), never a letter of the bank. The tables price through weigh() and write long vowels as repeated kana, so the operator is not load-bearing. Recorded so the register is complete.'),
 # --- Ge'ez
 dict(tongue='geez', seat='the syllabary beyond the classical bases: later/derived rows (ሸ ቐ ቨ ቸ ኘ ኸ ዀ ዠ ዸ ጀ ጘ ጨ and their forms, 117 signs) unseated',
      kind='FENCED', source='engine bank GEEZ (227 keys) enumerated against the Ethiopic block at build; THE-GEEZ-TABLES Phases I–III (the mint prices the classical grid)',
      status='THE MINT\u2019S OWN FENCE: the Ge\u2019ez mint prices the classical bases and their orders; the derived rows are later formations the mint does not claim. In the tables, a door syllable needing a derived base (e.g. ቸ for \u2018ch\u2019) fails at that coordinate and the cell prints HOLE with the coordinate named. Never filled by this build.'),
 dict(tongue='geez', seat='Η/Ω (Greek eta/omega) have no Ge\u2019ez seat',
      kind='MINT', source='carried state from the Ge\u2019ez road (the residue: Η/Ω unseated)',
      status='CARRIED OPEN: no audit-proposed construction prices Greek letters in the Ethiopic grid, and none is invented here. The seat is a Greek-bank matter wearing a Ge\u2019ez label; it does not bite any table cell (no cell prices a Greek letter through the Ge\u2019ez bank). Question carried to the instrument\u2019s pen list.'),
 dict(tongue='geez', seat='ዐ-cell hole at the hybrid (ΕΙ) column of the mint grid',
      kind='FENCED', source='THE-GEEZ-TABLES-PHASE-II-III (the eighth slot encoded for 25 of 26 bases; ዐ\u2019s cell a HOLE)',
      status='THE MINT\u2019S PRINTED HOLE: it stands in the instrument of record as a hole; the tables inherit it as printed. Not filled.'),
 # --- Armenian
 dict(tongue='armenian', seat='Օ/Ֆ (the late letters) outside the classical bank',
      kind='RULING', source='THE-ARMENIAN-TABLE-PHASE-I-AUDIT §VII Q1; resolutions commit fed4064 (R1)',
      status='RESOLVED BY THE FOUNDER 2026-11-24 (R1): the ARMENIAN_LATE annex (Օ 10000, Ֆ 20000) prices only at the armenian(late=True) door. In the tables, a door rendering needing Ֆ prices through the annex and says so on its face.'),
 dict(tongue='armenian', seat='the overline\u2019s factor',
      kind='RULING', source='THE-ARMENIAN-TABLE-PHASE-I-AUDIT §VII Q2; resolutions R2',
      status='RESOLVED BY THE FOUNDER 2026-11-24 (R2): ×10,000 at the armenian() door. The tables price bare letters, so the factor is not load-bearing here.'),
 dict(tongue='armenian', seat='Shirakatsi recorded, not seated',
      kind='FENCED', source='resolutions R3',
      status='RECORDED-NOT-SEATED by the founder\u2019s resolution: stands outside the bank by ruling. Not a gap this build may fill.'),
 # --- Coptic
 dict(tongue='coptic', seat='the seven unvalued Demotic letters (ϣ ϩ ϧ ϫ ϭ ϯ and kin)',
      kind='FENCED', source='THE-COPTIC-TABLE-PHASE-I-AUDIT (27 valued signs + 7 unvalued, a sourced boundary)',
      status='THE TRADITION\u2019S OWN BOUNDARY: the sources refuse these letters values, and the audit refuses with them. In the tables, a door rendering crossing one prints FENCED at that letter. Never filled.'),
 dict(tongue='coptic', seat='Q1 — a thousands reading law for the devices (double overline U+033F; the ͵ sign U+0375)',
      kind='RULING', source='THE-COPTIC-TABLE-PHASE-I-AUDIT §VII Q1',
      status='CARRIED OPEN — FILL STOPPED AT A FROZEN EXHIBIT: the synergy argument (the Cyrillic door prices its sourced thousands sign at ×1000; the devices here are sourced at ×1000 by Unicode §7.3 as W1 reports it) was tested against the seat\u2019s frozen parity battery and CONTRADICTS it: test_coptic_parity.py pins \u2018coptic() counts the marks and prices NONE — ⲁ̿ and ⲁ͵ weigh 1\u2019, and coptic_checks check 4/9 print the refusal as the seat\u2019s doctrine (\u2018devices of notation, not letter values\u2019). Per the build\u2019s law, the fill stops: the devices stay counted-not-priced, the question stays the founder\u2019s, and the contradiction stands printed here at full size. The tables price bare Coptic letters only, so no cell is blocked by the opening.'),
 dict(tongue='coptic', seat='Q2 — Satzinger\u2019s stauros at 1000',
      kind='RULING', source='THE-COPTIC-TABLE-PHASE-I-AUDIT §VII Q2',
      status='RESOLVED by synergy: NOT SEATED. One scholarly witness, a symbol rather than a letter; the audit\u2019s own condition (a second witness) is unmet, and the falsifiability rule seats nothing on a single uncorroborated witness. Stands as a boundary until a second witness surfaces. No code change.'),
 dict(tongue='coptic', seat='Q3 — the Epact Numbers; Q4 — the COPT-TRANS-v1 layer',
      kind='RULING', source='THE-COPTIC-TABLE-PHASE-I-AUDIT §VII Q3–Q4',
      status='CARRIED: both are questions about FUTURE instruments (a bank of its own; a transliteration layer), not gaps in this bank. The tables\u2019 Coptic door is this build\u2019s stated scheme, not COPT-TRANS-v1. Questions carried to the pen list.'),
 # --- Aramaic (folds into Hebrew; register entries ride the Hebrew table)
 dict(tongue='hebrew (aramaic dresses)', seat='Q1 — a reading law for the Syriac raised point (decade + point = century)',
      kind='RULING', source='THE-ARAMAIC-SEAT-PHASE-I-AUDIT §VII Q1',
      status='RESOLVED by synergy: COUNTED, NOT PRICED — the standing practice becomes the ruled law. The same combining dot is Syriac\u2019s hard-dot in ordinary pointed text, so a priced point would tax text that intends no numeral; and nothing is unweighable meanwhile (the additive writing covers 500–900 at the raw bank: ܬܩ = 500). The Cyrillic higher-signs resolution below is the same law in the other field. No code change.'),
 dict(tongue='hebrew (aramaic dresses)', seat='Q2 — the other Aramaic scripts (Palmyrene, Nabataean, Mandaic…)',
      kind='FENCED', source='THE-ARAMAIC-SEAT-PHASE-I-AUDIT §VII Q2',
      status='SURVEYED-NOT-AUDITED: they stand outside the seat, as Sanskrit stands outside the letter tables. The Hebrew table prints the two seated dresses (Imperial, Syriac) only.'),
 dict(tongue='hebrew (aramaic dresses)', seat='Q3 — the Imperial number signs (a notation, not a bank)',
      kind='FENCED', source='THE-ARAMAIC-SEAT-PHASE-I-AUDIT §VII Q3',
      status='EXHIBITED, UNSEATED: a notation beside the bank, the Roman numerals\u2019 shape before their seat. No table cell prices them.'),
 # --- Georgian
 dict(tongue='georgian', seat='Q3 — the Mtavruli headline dress: fold at the seam, or silence?',
      kind='RULING', source='THE-GEORGIAN-FIELD-PHASE-I-AUDIT §VII Q3',
      status='RESOLVED BY SYNERGY AND FILLED IN CODE (commit cedfb67): FOLD. Every other cased bank folds its capital dress at the weigh() seam; case carries no numeral value; a headline-cased word is the same word. The fold maps only U+1C90–U+1CBA to Mkhedruli; Asomtavruli/Nuskhuri stay unfolded per the seat\u2019s D2. New georgian_checks 11 pins both halves; parity 34/34.'),
 dict(tongue='georgian', seat='Q2 — a numeral multiplier mark: no witness carries one',
      kind='RULING', source='THE-GEORGIAN-FIELD-PHASE-I-AUDIT §VII Q2 / §VI.5',
      status='RESOLVED by synergy: NO MARK PRICED. A device without a sourced factor is not priced (the Coptic plain-overline discipline); if a witness surfaces, its pricing is a ruling on the Armenian R2 pattern. No code change.'),
 dict(tongue='georgian', seat='Q1 — the depth caveat (modern reference witnesses; no primary re-read)',
      kind='FENCED', source='THE-GEORGIAN-FIELD-PHASE-I-AUDIT §VI.1, §VII Q1',
      status='A CAVEAT, NOT A SEAT: it governs the depth of the desk\u2019s reading, not the table\u2019s standing, and no desk act can retire it. It prints on the bank\u2019s fence and in the instrument.'),
 dict(tongue='georgian', seat='the doubled 400 (ჳ and უ) and the five obsolete letters',
      kind='FENCED', source='THE-GEORGIAN-FIELD-PHASE-I-AUDIT §VII D1',
      status='SEATED AS SOURCED, recorded so the register is complete: both holders of 400 stand in the bank (the record\u2019s own shape), and the obsolete five seat IN the classical bank as original members. No gap.'),
 # --- Cyrillic
 dict(tongue='cyrillic', seat='Q1 — the higher encircling signs (⃝ ҈ ҉ ꙰ ꙱ ꙲): the Lesser and Greater count scales part by orders of magnitude',
      kind='RULING', source='THE-SLAVONIC-PAIR §VII Q1; engine cyrillic() doctrine',
      status='RESOLVED by synergy: COUNTED, NOT PRICED — the ruled law, one with the Aramaic raised point: where the sources themselves part on a device\u2019s factor, the door counts the sign and prices none; pricing either scale would falsify the other. The ҂ thousands sign, whose factor no source disputes, stays priced at ×1000 at the door. No code change.'),
 dict(tongue='cyrillic', seat='the titlo (U+0483)',
      kind='FENCED', source='THE-SLAVONIC-PAIR; THE-CAUCASUS-AND-THE-NORTH devices census',
      status='A MARK, NEVER A MULTIPLIER: counted at the door, priced never — the tradition\u2019s own office for the sign.'),
 dict(tongue='cyrillic', seat='the western pair (the contradicting half-pair of witnesses)',
      kind='FENCED', source='THE-SLAVONIC-PAIR §VII D4',
      status='REFUSED WHOLE: a contradicting half-pair seated would falsify the canonical bank; the system stands recorded in the data at its printed values, outside the bank.'),
 dict(tongue='cyrillic', seat='letters of the modern alphabet the numeral bank does not value (Б Ж Ш Щ Ъ Ы Ь Э Ю Я Й)',
      kind='FENCED', source='engine bank CYRILLIC (33 keys) enumerated at build; THE-SLAVONIC-PAIR (the numeral alphabet is the Greek-inherited set)',
      status='THE NUMERAL ALPHABET\u2019S OWN SHAPE: these letters were never numeral letters. In the tables, a door rendering requiring one prints FENCED at that letter. Never filled.'),
 # --- Glagolitic
 dict(tongue='glagolitic', seat='the thousands range (Ⱍ 1000 – Ⱔ 9000) under its own sources\u2019 doubt',
      kind='FENCED', source='THE-SLAVONIC-PAIR §VII D2 (seated in the bank, flagged)',
      status='SEATED AND FLAGGED, never silently relied on: the letters stand in the bank as the witness prints them, doubt on the fence. Table cells price them as seated; the flag rides the instrument\u2019s face. This build neither extends nor retires the range.'),
 dict(tongue='glagolitic', seat='the sequence holes: Ⱊ Ⱐ Ⱒ carry no value',
      kind='FENCED', source='THE-SLAVONIC-PAIR; engine bank GLAGOLITIC (34 keys) enumerated at build',
      status='THE SEQUENCE\u2019S OWN HOLES: letters the numeral sequence skips. They price nothing and block nothing in the tables (no door sound maps to them).'),
 dict(tongue='glagolitic', seat='the doubled 10 (Ⰹ IZHE and Ⰺ INITIAL IZHE)',
      kind='FENCED', source='THE-SLAVONIC-PAIR §VII D1',
      status='SEATED BOTH, as sourced: the value is undisputed, the holder is the record\u2019s own dispute; seating both preserves every sourced claim and invents none. No gap.'),
 # --- Korean
 dict(tongue='korean', seat='the 1446 historical grid: opt-in only at hangul(hist=True)',
      kind='MINT', source='THE-EAST-ASIAN-FIELD-PHASE-I-AUDIT; THE-REGIONAL-TRIAD-DIAL (the hangul mint)',
      status='BY DESIGN: the mint prices the modern jamo grid (67 seats enumerated at build — 19 initials, 21 medials, 27 finals, all priced); the historical dress weighs only at the explicit hist door. The tables price the modern grid. Recorded so the register is complete.'),
 dict(tongue='korean', seat='ㆍ (arae-a, U+119E) and the obsolete jamo: no seat in the modern grid',
      kind='MINT', source='engine bank HANGUL enumerated at build (ㆍ absent)',
      status='CARRIED OPEN: the mint\u2019s grid is the modern one by its founding law; no audit-proposed construction prices the obsolete jamo at the raw bank (they live, if anywhere, behind the hist door). No table cell needs them (the door composes modern syllables). Question carried to the pen list.'),
]

# ---------------------------------------------------------------- doors
# Transliteration schemes, one per tongue, stated on the tables' face.
# Each map is greedy longest-match over the normalised Latin form.
def norm_latin(s, keep_apos=False):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('\u2019', "'").replace('\u02bf', "'").replace('\u02be', "'")
    s = s.lower()
    if not keep_apos:
        s = s.replace("'", '')
    s = re.sub(r'[^a-z\' ]' if keep_apos else r'[^a-z ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def apply_map(word, pairs):
    pairs = sorted(pairs, key=lambda p: -len(p[0]))
    out_words = []
    for w in word.split(' '):
        out, i = [], 0
        while i < len(w):
            for k, v in pairs:
                if w.startswith(k, i):
                    out.append(v); i += len(k); break
            else:
                return None, w[i]
        out_words.append(''.join(out))
    return ' '.join(out_words), None

GREEK_MAP = [('ph','φ'),('ch','χ'),('ps','ψ'),('th','θ'),('kh','χ'),('ks','ξ'),
 ('a','α'),('b','β'),('g','γ'),('d','δ'),('e','ε'),('z','ζ'),('i','ι'),
 ('k','κ'),('l','λ'),('m','μ'),('n','ν'),('x','ξ'),('o','ο'),('p','π'),
 ('r','ρ'),('s','σ'),('t','τ'),('y','υ'),('u','υ'),('v','β'),('q','κ'),
 ('j','ι'),('c','κ'),('f','φ'),('w','ου'),('h','')]
def door_greek(w):
    r, bad = apply_map(w, GREEK_MAP)
    if r is None: return None, bad
    words = [x[:-1] + 'ς' if x.endswith('σ') else x for x in r.split(' ')]
    return ' '.join(words), None

ARABIC_MAP = [('kh','خ'),('sh','ش'),('th','ث'),('dh','ذ'),('gh','غ'),
 ('tz','ص'),('ts','ص'),("'",
 'ع'),('a','ا'),('b','ب'),('t','ت'),('j','ج'),('h','ه'),('d','د'),
 ('r','ر'),('z','ز'),('s','س'),('e','ي'),('i','ي'),('o','و'),('u','و'),
 ('f','ف'),('q','ق'),('k','ك'),('l','ل'),('m','م'),('n','ن'),('w','و'),
 ('y','ي'),('v','و'),('g','ج'),('c','ك'),('p','ب'),('x','كس')]
def door_arabic(w):
    return apply_map(w, ARABIC_MAP)

ARMENIAN_MAP = [('kh','խ'),('sh','շ'),('ts','ծ'),('tz','ծ'),('dz','ձ'),
 ('gh','ղ'),('ch','չ'),('zh','ժ'),('ph','փ'),('th','թ'),
 ('a','ա'),('b','բ'),('g','գ'),('d','դ'),('e','ե'),('z','զ'),('i','ի'),
 ('l','լ'),('k','կ'),('h','հ'),('m','մ'),('y','յ'),('n','ն'),('o','ո'),
 ('p','պ'),('j','ջ'),('r','ր'),('s','ս'),('v','վ'),('t','տ'),('w','ւ'),
 ('u','ու'),('q','ք'),('f','ֆ'),('c','կ'),('x','կս')]
def door_armenian(w):
    return apply_map(w, ARMENIAN_MAP)

GEORGIAN_MAP = [('kh','ხ'),('sh','შ'),('ch','ჩ'),('ts','ც'),('tz','წ'),
 ('dz','ძ'),('gh','ღ'),('zh','ჟ'),('ph','ფ'),('th','თ'),
 ('a','ა'),('b','ბ'),('g','გ'),('d','დ'),('e','ე'),('v','ვ'),('z','ზ'),
 ('i','ი'),('k','კ'),('l','ლ'),('m','მ'),('n','ն'.replace('ն','ნ')),
 ('o','ო'),('p','პ'),('r','რ'),('s','ს'),('t','ტ'),('u','უ'),('q','ყ'),
 ('j','ჯ'),('h','ჰ'),('w','ვ'),('y','ი'),('f','ფ'),('c','კ'),('x','კს')]
def door_georgian(w):
    return apply_map(w, GEORGIAN_MAP)

CYRILLIC_FENCED = set('БЖШЩЪЫЬЭЮЯЙ')
CYRILLIC_MAP = [('shch','Щ'),('kh','Х'),('ch','Ч'),('sh','Ш'),('ps','Ѱ'),
 ('th','Ѳ'),('ph','Ф'),('ts','Ц'),('zh','Ж'),('yu','Ю'),('ya','Я'),
 ('a','А'),('b','Б'),('v','В'),('g','Г'),('d','Д'),('e','Е'),('z','З'),
 ('i','І'),('y','І'),('k','К'),('l','Л'),('m','М'),('n','Н'),('o','О'),
 ('p','П'),('r','Р'),('s','С'),('t','Т'),('u','У'),('f','Ф'),('h','Х'),
 ('w','В'),('j','І'),('q','К'),('c','К'),('x','Ѯ')]
def door_cyrillic(w):
    return apply_map(w, CYRILLIC_MAP)

GLAGOLITIC_MAP = [('shch','Ⱋ'),('sht','Ⱋ'),('kh','Ⱈ'),('ch','Ⱍ'),
 ('sh','Ⱎ'),('ts','Ⱌ'),('dz','Ⰷ'),('zh','Ⰶ'),('yu','Ⱓ'),('ya','Ⱑ'),
 ('th','Ⱔ'),('ph','Ⱇ'),('dj','Ⰼ'),
 ('a','Ⰰ'),('b','Ⰱ'),('v','Ⰲ'),('g','Ⰳ'),('d','Ⰴ'),('e','Ⰵ'),
 ('z','Ⰸ'),('i','Ⰹ'),('y','Ⰻ'),('k','Ⰽ'),('l','Ⰾ'),('m','Ⰿ'),
 ('n','Ⱀ'),('o','Ⱁ'),('p','Ⱂ'),('r','Ⱃ'),('s','Ⱄ'),('t','Ⱅ'),
 ('u','Ⱆ'),('f','Ⱇ'),('h','Ⱈ'),('w','Ⰲ'),('j','Ⰼ'),('q','Ⰽ'),
 ('c','Ⰽ'),('x','ⰍⰔ')]
def door_glagolitic(w):
    return apply_map(w, GLAGOLITIC_MAP)

COPTIC_FENCED = set('ϣϩϧϫϭϯ')
COPTIC_MAP = [('sh','ϣ'),('kh','ⲭ'),('ch','ⲭ'),('ph','ⲫ'),('th','ⲑ'),
 ('ps','ⲯ'),('ee','ⲏ'),('oo','ⲱ'),('dj','ϫ'),
 ('a','ⲁ'),('b','ⲃ'),('g','ⲅ'),('d','ⲇ'),('e','ⲉ'),('z','ⲍ'),
 ('i','ⲓ'),('k','ⲕ'),('l','ⲗ'),('m','ⲙ'),('n','ⲛ'),('x','ⲝ'),
 ('o','ⲟ'),('p','ⲡ'),('f','ϥ'),('r','ⲣ'),('s','ⲥ'),('t','ⲧ'),
 ('y','ⲩ'),('u','ⲩ'),('v','ⲃ'),('w','ⲩ'),('h','ϩ'),('j','ϫ'),
 ('q','ⲕ'),('c','ⲕ')]
def door_coptic(w):
    return apply_map(w, COPTIC_MAP)

# --- kana: the foreign-word (gairaigo) dress. Hepburn syllables to
# hiragana; consonant clusters and final consonants take the
# epenthetic vowel of the Japanese convention (o after t/d, u
# elsewhere); l rides the r-row, v the b-row, f the h-row with
# small-vowel companions — every companion kana a priced seat.
KANA_ROW = {'k':'かきくけこ','s':'さしすせそ','t':'たちつてと',
 'n':'なにぬねの','h':'はひふへほ','m':'まみむめも','r':'らりるれろ',
 'g':'がぎぐげご','z':'ざじずぜぞ','d':'だぢづでど','b':'ばびぶべぼ',
 'p':'ぱぴぷぺぽ','y':'やゆよ','w':'わゐゑを'}
KANA_SPECIAL = {'shi':'し','chi':'ち','tsu':'つ','fu':'ふ','ji':'じ',
 'sha':'しゃ','shu':'しゅ','sho':'しょ','cha':'ちゃ','chu':'ちゅ',
 'cho':'ちょ','ja':'じゃ','ju':'じゅ','jo':'じょ','je':'じぇ',
 'fa':'ふぁ','fi':'ふぃ','fe':'ふぇ','fo':'ふぉ','ti':'てぃ','tu':'とぅ',
 'di':'でぃ','du':'どぅ','she':'しぇ','che':'ちぇ','tsa':'つぁ',
 'tse':'つぇ','tso':'つぉ'}
KANA_VOWEL = {'a':'あ','i':'い','u':'う','e':'え','o':'お'}
KANA_ONSETS = ['sh','ch','ts','dz','ky','gy','ny','hy','by','py','my',
 'ry','k','g','s','z','t','d','n','h','b','p','m','r','l','v','f',
 'j','w','y','q','c','x']
def _kana_syllable(onset, vowel):
    if onset + vowel in KANA_SPECIAL:
        return KANA_SPECIAL[onset + vowel]
    row_onset = {'l':'r','v':'b','q':'k','c':'k','j':'z','x':'k'}.get(onset, onset)
    if row_onset == 'y':
        return {'a':'や','u':'ゆ','o':'よ'}.get(vowel)
    if row_onset == 'w':
        return {'a':'わ','i':'ゐ','e':'ゑ','o':'を'}.get(vowel)
    if row_onset in KANA_ROW:
        return KANA_ROW[row_onset]['aiueo'.index(vowel)]
    return None
def door_kana(word):
    out = []
    for w in word.split(' '):
        w = w.replace('x', 'ks')
        i, buf = 0, ''
        while i < len(w):
            c = w[i]
            if c in KANA_VOWEL:
                buf += KANA_VOWEL[c]; i += 1; continue
            if c == 'n' and (i + 1 == len(w) or w[i+1] not in 'aiueoy'):
                buf += 'ん'; i += 1; continue
            if i + 1 < len(w) and w[i+1] == c and c not in 'aiueo':
                buf += 'っ'; i += 1; continue
            onset = None
            for cand in KANA_ONSETS:
                if w.startswith(cand, i):
                    onset = cand; break
            if onset is None:
                return None, c
            i += len(onset)
            if i < len(w) and w[i] in KANA_VOWEL:
                syl = _kana_syllable(onset, w[i])
                if syl is None:
                    return None, onset + w[i]
                buf += syl; i += 1
            else:
                epi = 'o' if onset in ('t', 'd') else 'u'
                syl = _kana_syllable(onset, epi)
                if syl is None:
                    return None, onset
                buf += syl
        out.append(buf)
    return ' '.join(out), None

# --- Ge'ez: consonant bases by first-form codepoint; vowel orders are
# offsets (ä +0, u +1, i +2, a +3, e +4, ə +5, o +6).
GEEZ_BASE = {'h':0x1200,'l':0x1208,'m':0x1218,'r':0x1228,'s':0x1230,
 'q':0x1240,'b':0x1260,'t':0x1270,'n':0x1290,'k':0x12A8,'w':0x12C8,
 'z':0x12D8,'y':0x12E8,'d':0x12F0,'g':0x1310,'f':0x1348,'p':0x1350,
 'ḥ':0x1210,'ś':0x1220,'ʿ':0x12D0,'ʾ':0x12A0,'ṭ':0x1320,'ṣ':0x1338,
 'ḫ':0x12B0}
GEEZ_DIGRAPH = {'sh':'ś','kh':'ḫ','gh':'g','th':'t','dh':'d','ts':'ṣ',
 'tz':'ṣ','dz':'z','ch':None,'j':'g','v':'b','ph':'f','x':None,'c':'k'}
GEEZ_VOWEL = {'a':3,'i':2,'e':4,'u':1,'o':6}
def door_geez(word):
    out = []
    for w in word.split(' '):
        # tokenise into (consonant, vowel|None)
        w = w.replace('x', 'ks')
        toks, i = [], 0
        while i < len(w):
            two = w[i:i+2]
            if two in GEEZ_DIGRAPH:
                if GEEZ_DIGRAPH[two] is None:
                    return None, two
                cons, i = GEEZ_DIGRAPH[two], i + 2
            elif w[i] in GEEZ_DIGRAPH:
                if GEEZ_DIGRAPH[w[i]] is None:
                    return None, w[i]
                cons, i = GEEZ_DIGRAPH[w[i]], i + 1
            elif w[i] in GEEZ_VOWEL:
                cons, i = 'ʾ', i
                toks.append((cons, w[i])); i += 1; continue
            elif w[i] in GEEZ_BASE:
                cons, i = w[i], i + 1
            else:
                return None, w[i]
            if i < len(w) and w[i] in GEEZ_VOWEL:
                toks.append((cons, w[i])); i += 1
            else:
                toks.append((cons, None))
        buf = ''
        for cons, vow in toks:
            base = GEEZ_BASE[cons]
            off = GEEZ_VOWEL[vow] if vow else 5
            buf += chr(base + off)
        out.append(buf)
    return ' '.join(out), None

# --- Hangul: compose syllables. Jamo indices are DERIVED from
# Unicode: each compatibility jamo names its conjoining partner in
# its decomposition, and the conjoining blocks are canonical-ordered
# (initials U+1100+, medials U+1161+, finals U+11A7+ with 0 = none).
def _jamo_index(name, block):
    """Index of the conjoining jamo whose compatibility letter carries
    this Unicode name — names, not glyphs, so no typed-glyph doubt."""
    for cp in range(0x3131, 0x3164):
        if unicodedata.name(chr(cp), '') == 'HANGUL LETTER ' + name:
            dec = unicodedata.decomposition(chr(cp))
            return int(dec.split()[-1], 16) - block
    raise KeyError(name)
HANGUL_INI = {k: _jamo_index(v, 0x1100) for k, v in {
 'g':'KIYEOK','kk':'SSANGKIYEOK','n':'NIEUN','d':'TIKEUT','r':'RIEUL',
 'l':'RIEUL','m':'MIEUM','b':'PIEUP','s':'SIOS','j':'CIEUC',
 'ch':'CHIEUCH','k':'KHIEUKH','t':'THIEUTH','p':'PHIEUPH','h':'HIEUH',
 'kh':'KHIEUKH','th':'THIEUTH','ph':'PHIEUPH','v':'PIEUP','f':'PHIEUPH',
 'z':'CIEUC','q':'KHIEUKH','c':'KHIEUKH','x':'KHIEUKH','w':'IEUNG',
 'y':'IEUNG','':'IEUNG'}.items()}
HANGUL_MED = {k: _jamo_index(v, 0x1161) for k, v in {
 'a':'A','ae':'AE','ya':'YA','yae':'YAE','eo':'EO','e':'E','ye':'YE',
 'o':'O','yo':'YO','u':'U','yu':'YU','wa':'WA','wo':'WEO','we':'WE',
 'wi':'WI','oe':'OE','eu':'EU','ui':'YI','i':'I'}.items()}
# Finals cannot ride the decomposition (a compatibility letter
# decomposes to its INITIAL jamo); the jongseong order is canonical
# and is indexed here by name position (0 = no final).
_JONGSEONG = ['','KIYEOK','SSANGKIYEOK','KIYEOK-SIOS','NIEUN',
 'NIEUN-CIEUC','NIEUN-HIEUH','TIKEUT','RIEUL','RIEUL-KIYEOK',
 'RIEUL-MIEUM','RIEUL-PIEUP','RIEUL-SIOS','RIEUL-THIEUTH',
 'RIEUL-PHIEUPH','RIEUL-HIEUH','MIEUM','PIEUP','PIEUP-SIOS','SIOS',
 'SSANGSIOS','IEUNG','CIEUC','CHIEUCH','KHIEUKH','THIEUTH',
 'PHIEUPH','HIEUH']
HANGUL_FIN = {k: _JONGSEONG.index(v) for k, v in {
 'k':'KIYEOK','n':'NIEUN','l':'RIEUL','m':'MIEUM','p':'PIEUP',
 't':'SIOS','s':'SIOS','ng':'IEUNG','b':'PIEUP','d':'SIOS',
 'g':'KIYEOK','j':'CIEUC'}.items()}
def _compose(L, V, T):
    return chr(0xAC00 + (L * 21 + V) * 28 + T)
def door_hangul(word):
    out = []
    for w in word.split(' '):
        i, buf = 0, ''
        while i < len(w):
            # onset
            onset = ''
            for L in (2, 1):
                if w[i:i+L] in HANGUL_INI and w[i:i+L]:
                    onset = w[i:i+L]; i += L; break
            # medial; a bare onset with no vowel of its own takes
            # the epenthetic ㅡ syllable of the Korean foreign dress
            med = None
            for L in (2, 1):
                if w[i:i+L] in HANGUL_MED:
                    med = w[i:i+L]; i += L; break
            if med is None:
                if onset == '':
                    return None, w[i] if i < len(w) else '(end)'
                buf += _compose(HANGUL_INI[onset], HANGUL_MED['eu'], 0)
                continue
            # coda: a consonant at end, or before another consonant
            fin = 0
            rest = w[i:]
            if rest:
                c = None
                for L in (2, 1):
                    if rest[:L] in HANGUL_FIN:
                        c = rest[:L]; break
                if c:
                    after = rest[len(c):]
                    if not after or after[0] not in 'aeiouy':
                        fin = HANGUL_FIN[c]; i += len(c)
            buf += _compose(HANGUL_INI[onset], HANGUL_MED[med], fin)
        out.append(buf)
    return ' '.join(out), None

DOORS = {
 'greek':    (door_greek, 'Greek dress of the Latin form (ph φ, ch χ, th θ, ps ψ; final σ → ς; h the breathing, unwritten)'),
 'arabic':   (door_arabic, 'Arabic dress of the Latin form (kh خ, sh ش, th ث, gh غ, tz/ts ص, \u2019 ع; short vowels written with the matres)'),
 'armenian': (door_armenian, 'Armenian dress of the Latin form (kh խ, sh շ, ts ծ, gh ղ, ch չ, ph փ)'),
 'georgian': (door_georgian, 'Georgian dress of the Latin form (kh ხ, sh შ, ch ჩ, ts ც, tz წ, gh ღ)'),
 'cyrillic': (door_cyrillic, 'Cyrillic dress of the Latin form onto the numeral alphabet\u2019s valued letters only'),
 'glagolitic': (door_glagolitic, 'Glagolitic dress of the Latin form (sht Ⱋ, ts Ⱌ, ch Ⱍ, sh Ⱎ)'),
 'coptic':   (door_coptic, 'Coptic dress of the Latin form (kh/ch ⲭ, ph ⲫ, th ⲑ, ps ⲯ, f ϥ)'),
 'japanese': (door_kana, 'Kana dress of the Latin form (gairaigo convention: Hepburn syllables to hiragana; clusters and finals take the epenthetic vowel — o after t/d, u elsewhere; l on the r-row, v on the b-row)'),
 'geez':     (door_geez, 'Ethiopic dress of the Latin form (CV syllables in the classical bases; bare consonant = 6th order; sh ሠ, ts ጸ)'),
 'korean':   (door_hangul, 'Hangul dress of the Latin form (syllables composed by the Unicode formula; priced by seat through the hangul() door)'),
}
FENCED_SETS = {'cyrillic': CYRILLIC_FENCED, 'coptic': COPTIC_FENCED}

# ---------------------------------------------------------------- helpers
def script_of(word):
    for ch in word:
        o = ord(ch)
        if 0x590 <= o < 0x600: return 'hebrew'
        if 0x370 <= o < 0x400 or 0x1F00 <= o < 0x2000: return 'greek'
        if 0x600 <= o < 0x700: return 'arabic'
        if 0x2C00 <= o < 0x2D00 or 0x10A0 <= o < 0x1100: return 'other'
        if 0x1200 <= o < 0x1380: return 'geez'
        if 0x3040 <= o < 0x3100: return 'kana'
        if o < 0x250: return 'latin'
    return 'other'

def covered(rendering, system):
    """True iff weigh() prices every letter of rendering (no silence)."""
    r = weigh(rendering, system)
    got = ''.join(k for k, _ in r['breakdown'])
    want = rendering.replace(' ', '')
    if system == 'armenian':
        want = want.upper()
    return got == want

HEBREW_ORDER = 'אבגדהוזחטיכלמנסעפצקרשת'
HEBREW_FINALS = {'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}
def aramaic_dresses(hebrew_word):
    """The same word in the Imperial and Syriac dresses, by letter
    position — the Aramaic bank's own keying. Returns (imp, syr, val)."""
    imp_keys = [k for k in T.ARAMAIC.keys() if ord(k[0]) >= 0x10800]
    syr_keys = [k for k in T.ARAMAIC.keys() if ord(k[0]) < 0x10800]
    idx = {c: i for i, c in enumerate(HEBREW_ORDER)}
    imp, syr = '', ''
    for ch in hebrew_word:
        base = HEBREW_FINALS.get(ch, ch)
        if base in idx and idx[base] < len(imp_keys):
            imp += imp_keys[idx[base]]; syr += syr_keys[idx[base]]
    if not imp:
        return None
    v = weigh(imp, 'aramaic')['value']
    return imp, syr, v

TONGUES = [
 ('greek', 'Greek', 'greek'),
 ('hebrew', 'Hebrew', 'hebrew'),
 ('arabic', 'Arabic', 'arabic_abjad'),
 ('latin', 'Latin', None),          # two banks
 ('japanese', 'Japanese', 'kana'),
 ('geez', "Ge'ez", 'geez'),
 ('armenian', 'Armenian', 'armenian'),
 ('coptic', 'Coptic', 'coptic'),
 ('georgian', 'Georgian', 'georgian'),
 ('cyrillic', 'Cyrillic', 'cyrillic'),
 ('glagolitic', 'Glagolitic', 'glagolitic'),
 ('korean', 'Korean', 'hangul'),
]
BANK_SCRIPT = {'greek':'greek','hebrew':'hebrew','arabic_abjad':'arabic',
 'kana':'kana','geez':'geez','armenian':'armenian','coptic':'coptic',
 'georgian':'georgian','cyrillic':'cyrillic','glagolitic':'glagolitic',
 'hangul':'hangul'}

def price(rendering, system):
    if system == 'hangul':
        r = hangul(rendering)
        # coverage: every syllable's jamo priced (2 or 3 per syllable)
        exp = 0
        for ch in rendering:
            if ch == ' ': continue
            o = ord(ch) - 0xAC00
            exp += 3 if (o % 28) else 2
        if len(r['breakdown']) != exp:
            return None
        return r['value']
    if not covered(rendering, system):
        return None
    return weigh(rendering, system)['value']

def build():
    reg = json.loads(VERIFIED.read_text(encoding='utf-8'))
    frame = []   # census rows
    for s in reg:
        base = dict(cell_id=s['cell_id'], column=s['column'],
                    header=s['header'], kind=s['kind'])
        if s['kind'] != 'FILLED':
            frame.append(dict(base, proposal_idx=None, word=None,
                              word_kind='NON-WORD'))
            continue
        for p in s['proposals']:
            claims = {}
            for c in p['claims']:
                if c.get('weighed_word') and c['bank_engine'] not in claims:
                    claims[c['bank_engine']] = c['weighed_word']
            raw = p['proposal_raw']
            home = None
            for w_ in re.findall(r'[^\s(]+', raw):
                sc = script_of(w_)
                if sc in ('hebrew', 'arabic', 'greek'):
                    home = (sc, w_); break
            latin_form = None
            for b in ('latin_ordinal', 'agrippa'):
                if b in claims:
                    latin_form = claims[b]; break
            if latin_form is None:
                if home is None:
                    latin_form = re.split(r'\s+—\s+|\s+\(', raw)[0].strip()
                else:
                    m = re.search(r'\(([^)]+)\)', raw)
                    if m: latin_form = m.group(1)
            frame.append(dict(base, proposal_idx=p['proposal_idx'],
                              word=raw, word_kind='WORD', claims=claims,
                              home_script=home[0] if home else 'latin',
                              home_word=home[1] if home else latin_form,
                              latin_form=latin_form))
    words = [f for f in frame if f['word_kind'] == 'WORD']
    nonwords = [f for f in frame if f['word_kind'] != 'WORD']
    census = dict(frame_rows=len(frame), word_cells=len(words),
                  non_word_cells=len(nonwords),
                  sections=len(reg),
                  filled_sections=sum(1 for s in reg if s['kind'] == 'FILLED'),
                  empty_sections=sum(1 for s in reg if s['kind'] == 'INTENTIONALLY_EMPTY'),
                  gap_sections=sum(1 for s in reg if s['kind'] == 'TRANSCRIPTION_GAP'),
                  by_column={})
    from collections import Counter
    cc = Counter((f['column'], f['word_kind']) for f in frame)
    for (col, k), n in sorted(cc.items()):
        census['by_column'].setdefault(col, {})[k] = n

    tables = {}
    for tid, tname, bank in TONGUES:
        rows = []
        for f in frame:
            row = dict(cell_id=f['cell_id'], column=f['column'],
                       header=f['header'])
            if f['word_kind'] != 'WORD':
                row.update(state='EMPTY' if f['kind'] == 'INTENTIONALLY_EMPTY'
                           else 'GAP', rendering=None, value=None,
                           note='certified intentionally empty in 777 REVISED'
                                if f['kind'] == 'INTENTIONALLY_EMPTY'
                                else 'transcription gap in the source (CLXXXIV/10)')
                rows.append(row); continue
            row['word'] = f['word']
            claims = f['claims']
            # 1. corpus rendering in this tongue's bank
            banks_here = [bank] if bank else ['latin_ordinal', 'agrippa']
            corpus = None
            for b in banks_here:
                if b in claims and claims[b]:
                    w_ = claims[b]
                    if tid == 'latin' or script_of(w_) == BANK_SCRIPT.get(b):
                        corpus = (b, w_); break
            if corpus:
                b, w_ = corpus
                if tid == 'latin':
                    vo = weigh(w_, 'latin_ordinal')['value']
                    va = weigh(w_, 'agrippa')['value']
                    state = 'NATIVE' if f['home_script'] == 'latin' else 'DOOR'
                    row.update(state=state, rendering=w_,
                               value=dict(latin_ordinal=vo, agrippa=va),
                               scheme='the Latin banks on the corpus\u2019s printed Latin form'
                                      if state == 'NATIVE' else
                                      'the corpus\u2019s printed Latin transliteration, priced in the Latin banks')
                else:
                    v = price(w_, bank)
                    if v is not None:
                        state = 'NATIVE' if f['home_script'] == BANK_SCRIPT[bank] \
                                and w_ == f['home_word'] else 'DOOR'
                        row.update(state=state, rendering=w_, value=v,
                                   scheme='the word in its own tongue, as the corpus prints it'
                                          if state == 'NATIVE' else
                                          'corpus rendering — TABVLA verified register')
                    else:
                        corpus = None
            if corpus is None or (tid != 'latin' and 'state' not in row):
                if 'state' in row and row.get('value') is not None:
                    pass
                elif tid == 'latin':
                    lf = f['latin_form']
                    if lf:
                        vo = weigh(lf, 'latin_ordinal')['value']
                        va = weigh(lf, 'agrippa')['value']
                        row.update(state='NATIVE' if f['home_script'] == 'latin'
                                   else 'DOOR', rendering=lf,
                                   value=dict(latin_ordinal=vo, agrippa=va),
                                   scheme='the Latin banks on the printed Latin form')
                    else:
                        row.update(state='HOLE', rendering=None, value=None,
                                   note='no Latin form of record; no door offered')
                elif tid == 'hebrew' and f['latin_form']:
                    hr, mergers = transliterate_latin_to_hebrew(f['latin_form'])
                    v = weigh(hr, 'hebrew')['value']
                    row.update(state='DOOR', rendering=hr, value=v,
                               scheme='the house fallback map (transliterate_latin_to_hebrew); mergers: '
                                      + (', '.join(mergers) if mergers else 'none'))
                elif tid in DOORS and f['latin_form']:
                    fn, scheme = DOORS[tid]
                    src = norm_latin(f['latin_form'], keep_apos=(tid == 'arabic'))
                    rendering, bad = fn(src)
                    if rendering is None:
                        row.update(state='HOLE', rendering=None, value=None,
                                   note=f'door fails at \u2018{bad}\u2019 — no seat in this bank for that sound')
                    else:
                        fenced = FENCED_SETS.get(tid, set()) & set(rendering)
                        if fenced:
                            row.update(state='FENCED', rendering=rendering,
                                       value=None,
                                       note='the rendering crosses the fenced letter '
                                            + ' '.join(sorted(fenced))
                                            + ' — unvalued in this tradition; printed as the boundary, not priced')
                        else:
                            v = price(rendering, bank)
                            if v is None and tid == 'armenian' and 'ֆ' in rendering:
                                r2 = armenian(rendering, late=True)
                                got = ''.join(k for k, _ in r2['breakdown'])
                                if got.replace(' ', '') == rendering.replace(' ', '').upper():
                                    v = r2['value']
                                    scheme = scheme + ' + ARMENIAN_LATE annex (R1) for ֆ'
                            if v is None:
                                row.update(state='HOLE', rendering=rendering,
                                           value=None,
                                           note='door rendering crosses an unseated letter; the cell prints as a hole with its rendering shown')
                            else:
                                row.update(state='DOOR', rendering=rendering,
                                           value=v, scheme=scheme)
                else:
                    row.update(state='HOLE', rendering=None, value=None,
                               note='no Latin form of record; no door offered')
            # Hebrew table: the Aramaic dresses ride the cell
            if tid == 'hebrew' and f['home_script'] == 'hebrew':
                d = aramaic_dresses(f['home_word'])
                if d:
                    row['aramaic_dresses'] = dict(imperial=d[0], syriac=d[1],
                                                  value=d[2])
            rows.append(row)
        tables[tid] = dict(tongue=tname, bank=bank, rows=rows)
    return census, tables

if __name__ == '__main__':
    (HERE / 'gap_register.json').write_text(
        json.dumps(GAP_REGISTER, ensure_ascii=False, indent=1), encoding='utf-8')
    census, tables = build()
    (HERE / 'census.json').write_text(
        json.dumps(census, ensure_ascii=False, indent=1), encoding='utf-8')
    (HERE / 'tables_register.json').write_text(
        json.dumps(tables, ensure_ascii=False, indent=1), encoding='utf-8')
    from collections import Counter
    print('census:', census['frame_rows'], 'rows =', census['word_cells'],
          'word +', census['non_word_cells'], 'non-word')
    for tid, t in tables.items():
        c = Counter(r['state'] for r in t['rows'])
        print(f"{tid:12s}", dict(c))
    print('gap register entries:', len(GAP_REGISTER))
