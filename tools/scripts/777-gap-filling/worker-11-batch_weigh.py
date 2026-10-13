#!/usr/bin/env python3
# =============================================================================
# batch_weigh.py — weigh candidate formula-words across every applicable bank.
# Repo-exclusive: built for the 2026-10-13 PONTIFEX 777 gap-filling operation
# (worker-11's cells, column CLXXXVII, Magical Formulae). Thin driver over the
# attested ptk engine; never retypes a letter table.
#
# By worker-11. Findings, never doctrine. The red pen rules.
# =============================================================================
import sys
sys.path.insert(0, '/home/hatch/workspace/pontifex/tools/ptk')
import weigh

weigh.calibrate()  # anchorage first; raises on failure

BANKS = {
    'latin':   (weigh.latin,   weigh.LATIN_ORDINAL),
    'agrippa': (weigh.agrippa, weigh.AGRIPPA),
    'greek':   (weigh.greek,   weigh.GREEK),
    'hebrew':  (weigh.hebrew,  weigh.HEBREW),
    'gadol':   (weigh.hebrew_gadol, None),
}

# (cell_id, proposal, bank_keys)
CANDIDATES = [
    # -- CLXXXVII/23 : Mem (Water). Weapon: Cup and Cross of Suffering, the Wine
    ('CLXXXVII/23', 'AQUA',   ['latin', 'agrippa']),
    ('CLXXXVII/23', 'CALIX',  ['latin', 'agrippa']),
    ('CLXXXVII/23', 'VINUM',  ['latin', 'agrippa']),
    ('CLXXXVII/23', 'מים',    ['hebrew']),
    ('CLXXXVII/23', 'יין',    ['hebrew']),
    # -- CLXXXVII/27 : Peh (Mouth, Mars). Weapon: The Sword
    ('CLXXXVII/27', 'GLADIUS', ['latin', 'agrippa']),
    ('CLXXXVII/27', 'FERRUM',  ['latin', 'agrippa']),
    ('CLXXXVII/27', 'חרב',     ['hebrew']),
    ('CLXXXVII/27', 'ξιφος',   ['greek']),
    # -- CLXXXVII/28 : Tzaddi (Fish-hook). Weapon: Censer or Aspergillus
    ('CLXXXVII/28', 'THUS',    ['latin', 'agrippa']),
    ('CLXXXVII/28', 'IGNIS',   ['latin', 'agrippa']),
    ('CLXXXVII/28', 'קטרת',    ['hebrew', 'gadol']),
    ('CLXXXVII/28', 'θυμιαμα', ['greek']),
    # -- CLXXXVII/29 : Qoph (Back of head, Moon). Weapon: Twilight of the Place
    # and Magic Mirror
    ('CLXXXVII/29', 'SPECULUM', ['latin', 'agrippa']),
    ('CLXXXVII/29', 'LUNA',     ['latin', 'agrippa']),
    ('CLXXXVII/29', 'UMBRA',    ['latin', 'agrippa']),
    ('CLXXXVII/29', 'מראה',     ['hebrew']),
    ('CLXXXVII/29', 'σεληνη',   ['greek']),
    # -- CLXXXVII/31 : Shin (Tooth, Fire). Weapon: Wand or Lamp [[Thurible]]
    ('CLXXXVII/31', 'IGNIS',  ['latin', 'agrippa']),
    ('CLXXXVII/31', 'LUX',    ['latin', 'agrippa']),
    ('CLXXXVII/31', 'LAMPAS', ['latin', 'agrippa']),
    ('CLXXXVII/31', 'אש',     ['hebrew']),
    ('CLXXXVII/31', 'נר',     ['hebrew']),
    ('CLXXXVII/31', 'πυρ',    ['greek']),
    # -- CLXXXVII/32 : Tau (Cross, Saturn). Weapon: A Sickle
    ('CLXXXVII/32', 'FALX',    ['latin', 'agrippa']),
    ('CLXXXVII/32', 'MESSIS',  ['latin', 'agrippa']),
    ('CLXXXVII/32', 'חרמש',    ['hebrew']),
    ('CLXXXVII/32', 'αρπη',    ['greek']),
    # -- CLXXXVII/32 bis : Earth. Weapon: Pantacle or [[Bread and]] Salt
    ('CLXXXVII/32 bis', 'SAL',   ['latin', 'agrippa']),
    ('CLXXXVII/32 bis', 'TERRA', ['latin', 'agrippa']),
    ('CLXXXVII/32 bis', 'PANIS', ['latin', 'agrippa']),
    ('CLXXXVII/32 bis', 'מלח',   ['hebrew']),
    ('CLXXXVII/32 bis', 'לחם',   ['hebrew']),
    ('CLXXXVII/32 bis', 'אדמה',  ['hebrew']),
    # -- CLXXXVII/31 bis : Spirit. Weapon: [[The Winged Egg]]
    ('CLXXXVII/31 bis', 'OVUM',     ['latin', 'agrippa']),
    ('CLXXXVII/31 bis', 'SPIRITUS', ['latin', 'agrippa']),
    ('CLXXXVII/31 bis', 'רוח',      ['hebrew']),
    ('CLXXXVII/31 bis', 'ביצה',      ['hebrew']),
    ('CLXXXVII/31 bis', 'πνευμα',   ['greek']),
]

print(f"{'cell':<18} {'proposal':<10} {'bank':<8} {'value':>6}  unknown")
for cell, prop, banks in CANDIDATES:
    for b in banks:
        fn, table = BANKS[b]
        val = fn(prop)
        unk = weigh.unknown(prop.upper() if b in ('latin', 'agrippa') else prop,
                            table) if table is not None else []
        print(f"{cell:<18} {prop:<10} {b:<8} {val:>6}  {unk if unk else '-'}")
