#!/usr/bin/env python3
# =============================================================================
# worker10_batch_weigher.py — batch weighing for WORKER-10, PONTIFEX 777 run.
# Column CLXXXVII (Magical Formulæ), cells 1, 8, 11, 12, 15, 17, 20, 21, 22.
#
# METHOD (Scientific Illuminism): calibrate() gates everything; every weighing
# goes through ptk.weigh's ATTESTED tables; unknown() is checked on every
# word and its skips printed loudly. NEVER retype a letter table.
#
# DOCTRINE: English≡Latin ordinal = ONE bank. Hebrew≡Aramaic = one bank.
# A bridge = the SAME word, the SAME number, in TWO honest banks.
# Transliteration agreements = constructed-tier bridges (hypotheses, never
# doctrine). Same-number-different-word = coincidence, explicitly NOT a bridge.
#
# Thelemic form: 93. By the scribe for Johnathan 'Qasparr' Monroe's red pen.
# Live, Love, and let Love, Live.
# =============================================================================
import csv, sys
sys.path.insert(0, '/home/hatch/workspace/pontifex/tools')
from ptk import weigh

ok = weigh.calibrate()
print("calibrate:", ok)
assert ok, "CALIBRATE FAILED — weighing forbidden"

BANKS = {
    'HEBREW': (weigh.HEBREW, weigh.hebrew),
    'GREEK':  (weigh.GREEK,  weigh.greek),
    'LATIN':  (weigh.LATIN_ORDINAL, weigh.latin),
}

FLAG = "PONTIFEX-proposed 2026-10-13"
WORKER = "worker-10"
COL = "CLXXXVII"
COLTITLE = "Magical Formulæ (see Col. XLI)"

# (cell_row, row_meaning, weapon, proposal, proposal_native, bank, word,
#  tier, bridge, notes)
C = [
# --- CLXXXVII/1 — Kether; Swastika/Fylfot Cross, Crown [The Lamp]
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AL", "אל", "HEBREW", "אל", "attested", "yes:HEBREW+GREEK(translit)",
 "God-name of the Crown; the formula of Kether as AL. Greek AL=31 agrees via transliteration only (constructed tier)."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AL", "אל", "GREEK", "αλ", "constructed", "yes:HEBREW+GREEK(translit)",
 "Transliteration of Hebrew אל into Greek capitals; agreement with Hebrew 31 is a constructed-tier bridge — hypothesis, never doctrine."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AL", "אל", "LATIN", "AL", "constructed", "no",
 "Latin ordinal 13; single-bank value, no bridge."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AHIH", "אהיה", "HEBREW", "אהיה", "attested", "no",
 "AHIH, God-name of Kether (777 col. V); the formula 'I am'."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AHIH", "אהיה", "LATIN", "AHIH", "constructed", "no",
 "Latin ordinal 26; no bridge."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "AHIH", "אהיה", "GREEK", "αηιη", "constructed", "no",
 "Transliteration; 27, no agreement."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "IA", "יא", "HEBREW", "יא", "attested", "yes:HEBREW+GREEK(translit)",
 "IA, root of IAO; the concealed spark of the Crown."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "IA", "יא", "GREEK", "ια", "constructed", "yes:HEBREW+GREEK(translit)",
 "Transliteration; 11 agrees with Hebrew 11 — constructed-tier bridge, chance-flagged."),
(1, "Kether (Crown)", "Swastika or Fylfot Cross, Crown [The Lamp]",
 "IA", "יא", "LATIN", "IA", "constructed", "no",
 "Latin ordinal 10; no bridge."),

# --- CLXXXVII/8 — Hod; The Names and Versicles and Apron
(8, "Hod (Splendour)", "The Names and Versicles and Apron",
 "AMEN", "אמן", "HEBREW", "אמן", "attested", "no",
 "The Versicles conclude in Amen; the formula of affirmation sealing the Names."),
(8, "Hod (Splendour)", "The Names and Versicles and Apron",
 "AMEN", "אמן", "LATIN", "AMEN", "constructed", "no",
 "Latin ordinal 33; no bridge."),
(8, "Hod (Splendour)", "The Names and Versicles and Apron",
 "AMEN", "אמן", "GREEK", "αμην", "constructed", "no",
 "Transliteration; 99, no agreement."),

# --- CLXXXVII/11 — Aleph; The Dagger or Fan
(11, "Aleph (Ox)", "The Dagger or Fan",
 "ALPH", "אלף", "HEBREW", "אלף", "attested", "no",
 "Aleph spelled in full; the formula OF the path itself. 111."),
(11, "Aleph (Ox)", "The Dagger or Fan",
 "ALPH", "אלף", "LATIN", "ALPH", "constructed", "no",
 "Latin ordinal 37; no bridge."),
(11, "Aleph (Ox)", "The Dagger or Fan",
 "ALPH", "אלף", "GREEK", "αλφ", "constructed", "no",
 "Transliteration; 531, no agreement."),
(11, "Aleph (Ox)", "The Dagger or Fan",
 "AIR", "air", "LATIN", "AIR", "attested", "no",
 "Aleph = the element Air; English word on its native ordinal scale. 28."),
(11, "Aleph (Ox)", "The Dagger or Fan",
 "AIR", "אויר", "HEBREW", "אויר", "attested", "no",
 "Hebrew 'avir', air. 217; no agreement across banks — spread recorded."),
(11, "Aleph (Ox)", "The Dagger or Fan",
 "AIR", "αήρ", "GREEK", "αηρ", "constructed", "no",
 "Transliteration; 109, no agreement."),

# --- CLXXXVII/12 — Beth; The Wand or Caduceus
(12, "Beth (House)", "The Wand or Caduceus",
 "BITH", "בית", "HEBREW", "בית", "attested", "no",
 "Beth spelled in full; the formula OF the path. 412."),
(12, "Beth (House)", "The Wand or Caduceus",
 "BITH", "בית", "LATIN", "BITH", "constructed", "no",
 "Latin ordinal 39; no bridge."),
(12, "Beth (House)", "The Wand or Caduceus",
 "BITH", "בית", "GREEK", "βιθ", "constructed", "no",
 "Transliteration; 21, no agreement."),
(12, "Beth (House)", "The Wand or Caduceus",
 "HERMES", "Ἑρμῆς", "GREEK", "ερμης", "attested", "no",
 "Hermes = Mercury = the Caduceus-bearer; Greek word in its own table. 353."),
(12, "Beth (House)", "The Wand or Caduceus",
 "HERMES", "Ἑρμῆς", "LATIN", "HERMES", "constructed", "no",
 "Latin ordinal 68; no bridge."),
(12, "Beth (House)", "The Wand or Caduceus",
 "HERMES", "Ἑρμῆς", "HEBREW", "הרמס", "constructed", "no",
 "Hebrew transliteration; 305, no agreement."),
(12, "Beth (House)", "The Wand or Caduceus",
 "THOTH", "Θώθ", "GREEK", "θωθ", "attested", "no",
 "Thoth, Egyptian Hermes, lord of the Caduceus. 818."),
(12, "Beth (House)", "The Wand or Caduceus",
 "THOTH", "Θώθ", "LATIN", "THOTH", "constructed", "no",
 "Latin ordinal 94; no bridge."),

# --- CLXXXVII/15 — Hé; The Horns, Energy, the Burin
(15, "He (Window)", "The Horns, Energy, the Burin",
 "HA", "הא", "HEBREW", "הא", "attested", "no",
 "He spelled in full; the formula OF the path. 6."),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "HA", "הא", "LATIN", "HA", "constructed", "yes:LATIN+GREEK(translit)",
 "Latin ordinal 9; agrees with Greek transliteration ΗΑ=9 — constructed-tier bridge."),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "HA", "הא", "GREEK", "ηα", "constructed", "yes:LATIN+GREEK(translit)",
 "Transliteration; 9 agrees with Latin 9 — constructed-tier bridge, chance-flagged. (Hebrew 6 does NOT join.)"),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "ENERGY", "energy", "LATIN", "ENERGY", "attested", "no",
 "The weapon IS Energy; English word on its native scale. 74 — CHANCE: equals Hebrew LMD=74 but DIFFERENT WORD, NOT a bridge."),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "AZOTH", "azoth", "LATIN", "AZOTH", "constructed", "no",
 "The alchemical Life-force word; Latin ordinal 70, no bridge."),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "AZOTH", "azoth", "GREEK", "αζωθ", "constructed", "no",
 "Transliteration; 817, no agreement."),
(15, "He (Window)", "The Horns, Energy, the Burin",
 "AZOTH", "azoth", "HEBREW", "אזות", "constructed", "no",
 "Hebrew transliteration; 414, no agreement."),

# --- CLXXXVII/17 — Zain; The Tripod
(17, "Zain (Sword)", "The Tripod",
 "ZIN", "זין", "HEBREW", "זין", "attested", "yes:HEBREW+GREEK(translit)",
 "Zain spelled in full; the formula OF the path. 67."),
(17, "Zain (Sword)", "The Tripod",
 "ZIN", "זין", "GREEK", "ζιν", "constructed", "yes:HEBREW+GREEK(translit)",
 "Transliteration; 67 agrees with Hebrew 67 — constructed-tier bridge, chance-flagged."),
(17, "Zain (Sword)", "The Tripod",
 "ZIN", "זין", "LATIN", "ZIN", "constructed", "no",
 "Latin ordinal 61; no bridge."),
(17, "Zain (Sword)", "The Tripod",
 "APOLLO", "Ἀπόλλων", "GREEK", "απολλων", "attested", "no",
 "Apollo of the Delphic Tripod; Greek word in its own table. 1061."),
(17, "Zain (Sword)", "The Tripod",
 "APOLLO", "Ἀπόλλων", "LATIN", "APOLLO", "constructed", "no",
 "Latin ordinal 71; no bridge."),
(17, "Zain (Sword)", "The Tripod",
 "DELPHI", "Δελφοί", "GREEK", "δελφοι", "attested", "no",
 "Delphi, seat of the Tripod oracle. 619."),
(17, "Zain (Sword)", "The Tripod",
 "DELPHI", "Δελφοί", "LATIN", "DELPHI", "constructed", "no",
 "Latin ordinal 54; no bridge."),

# --- CLXXXVII/20 — Yod; The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "YVD", "יוד", "HEBREW", "יוד", "attested", "no",
 "Yod spelled in full; the formula OF the path — the secret Fire. 20."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "YVD", "יוד", "LATIN", "YVD", "constructed", "no",
 "Latin ordinal 51; no bridge."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "YVD", "יוד", "GREEK", "υδ", "constructed", "no",
 "Transliteration; 404, no agreement."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "LVX", "lux", "LATIN", "LVX", "attested", "no",
 "LVX, Light — the formula of the Lamp; Latin word on its native scale. 58."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "LVX", "lux", "GREEK", "λυξ", "constructed", "no",
 "Transliteration; 490, no agreement."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "LECHEM", "לחם", "HEBREW", "לחם", "attested", "no",
 "Lechem, bread — the Eucharistic formula of the Bread. 78."),
(20, "Yod (Hand)", "The Lamp and Wand (Virile Force reserved), the Bread [Lotus Wand]",
 "LECHEM", "לחם", "LATIN", "LECHEM", "constructed", "no",
 "Latin ordinal 46; no bridge."),

# --- CLXXXVII/21 — Kaph; The Sceptre
(21, "Kaph (Palm)", "The Sceptre",
 "KPH", "כף", "HEBREW", "כף", "attested", "no",
 "Kaph spelled in full; the formula OF the path. 100."),
(21, "Kaph (Palm)", "The Sceptre",
 "KPH", "כף", "LATIN", "KPH", "constructed", "no",
 "Latin ordinal 35; no bridge."),
(21, "Kaph (Palm)", "The Sceptre",
 "KPH", "כף", "GREEK", "κφ", "constructed", "no",
 "Transliteration; 520, no agreement."),
(21, "Kaph (Palm)", "The Sceptre",
 "JUPITER", "jupiter", "LATIN", "JUPITER", "attested", "no",
 "Jupiter, wielder of the Sceptre; Latin word on its native scale. 99."),
(21, "Kaph (Palm)", "The Sceptre",
 "ZEUS", "Ζεύς", "GREEK", "ζευς", "attested", "no",
 "Zeus, the Sceptre-bearer; Greek word in its own table. 612."),
(21, "Kaph (Palm)", "The Sceptre",
 "ZEUS", "Ζεύς", "LATIN", "ZEUS", "constructed", "no",
 "Latin ordinal 71; no bridge."),
(21, "Kaph (Palm)", "The Sceptre",
 "ZEUS", "Ζεύς", "HEBREW", "זאוס", "constructed", "no",
 "Hebrew transliteration; 74 — CHANCE: equals Hebrew LMD=74 but DIFFERENT WORD, NOT a bridge."),

# --- CLXXXVII/22 — Lamed; The Cross of Equilibrium
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "LMD", "למד", "HEBREW", "למד", "attested", "yes:HEBREW+GREEK(translit)",
 "Lamed spelled in full; the formula OF the path. 74."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "LMD", "למד", "GREEK", "λμδ", "constructed", "yes:HEBREW+GREEK(translit)",
 "Transliteration; 74 agrees with Hebrew 74 — constructed-tier bridge, chance-flagged."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "LMD", "למד", "LATIN", "LMD", "constructed", "no",
 "Latin ordinal 29; no bridge."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "MIZNYM", "מאזנים", "HEBREW", "מאזנים", "attested", "no",
 "Moznayim, the Scales — the instrument of Equilibrium; the weapon's operative word. 148."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "MIZNYM", "מאזנים", "LATIN", "MIZNYM", "constructed", "no",
 "Latin ordinal 100; no bridge."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "MAAT", "maat", "HEBREW", "מאת", "derived", "no",
 "Maat: Egyptian, no Egyptian table on hand → Hebrew fallback per doctrine. 441."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "MAAT", "maat", "GREEK", "μαατ", "constructed", "no",
 "Transliteration; 342, no agreement."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "MAAT", "maat", "LATIN", "MAAT", "constructed", "no",
 "Latin ordinal 35; no agreement — spread recorded, no bridge."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "LIBRA", "libra", "LATIN", "LIBRA", "attested", "no",
 "Libra, the Balance — the zodiacal correspondence of the path; Latin word native. 42."),
(22, "Lamed (Ox Goad)", "The Cross of Equilibrium",
 "CROSS", "cross", "LATIN", "CROSS", "constructed", "no",
 "English word for the weapon on the ordinal scale. 74 — CHANCE: equals Hebrew LMD=74 but DIFFERENT WORD, NOT a bridge."),
]

rows = []
problems = []
for (rnum, rmean, weapon, prop, native, bank, word, tier, bridge, notes) in C:
    table, fn = BANKS[bank]
    val = fn(word)
    skipped = weigh.unknown(word, table)
    if skipped:
        problems.append((prop, bank, word, skipped))
    rows.append({
        'cell_id': f"{COL}/{rnum}", 'column': COL, 'row': rnum,
        'column_title': COLTITLE, 'row_meaning': rmean,
        'proposal': f"{prop} ({native})", 'bank': bank, 'value': val,
        'tier': tier, 'bridge': bridge,
        'notes': f"Weapon: {weapon}. {notes}",
        'flag': FLAG, 'worker': WORKER,
    })

print(f"weighings: {len(rows)}")
if problems:
    print("UNKNOWN-SKIPS (must be empty):")
    for p in problems:
        print("  ", p)
else:
    print("unknown(): all clean — no skipped characters")

with open('/home/hatch/workspace/goals/cross-gematria-777-gap-filling/hidden_files/worker-10-fillings.csv',
          'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['cell_id','column','row','column_title','row_meaning',
        'proposal','bank','value','tier','bridge','notes','flag','worker'])
    w.writeheader()
    w.writerows(rows)
print("CSV written.")
