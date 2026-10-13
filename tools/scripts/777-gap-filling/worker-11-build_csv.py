#!/usr/bin/env python3
# =============================================================================
# build_worker11_csv.py — build worker-11's fillings CSV from the verified
# batch weighings. Repo-exclusive: the 2026-10-13 PONTIFEX 777 gap-filling
# operation (column CLXXXVII, Magical Formulae). All values were produced by
# batch_weigh.py over the attested ptk engine (calibrate() passed first);
# this script only formats them into the required CSV schema.
#
# By worker-11. Findings, never doctrine. The red pen rules.
# =============================================================================
import csv, sys
sys.path.insert(0, '/home/hatch/workspace/pontifex/tools/ptk')
import weigh

weigh.calibrate()

OUT = '/home/hatch/workspace/goals/cross-gematria-777-gap-filling/hidden_files/worker-11-fillings.csv'
FLAG = 'PONTIFEX-proposed 2026-10-13'
WORKER = 'worker-11'
COL = 'CLXXXVII'
TITLE = 'Magical Formulae (see Col. XLI)'

def W(word, bank):
    fn = {'latin': weigh.latin, 'agrippa': weigh.agrippa, 'greek': weigh.greek,
          'hebrew': weigh.hebrew, 'gadol': weigh.hebrew_gadol}[bank]
    return fn(word)

# rows: cell_id, row, row_meaning, proposal, role, banks, notes
CELLS = [
    ('CLXXXVII/23', '23', 'Mem (Water), 23rd path', [
        ('AQUA', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Cup and Cross of Suffering, the Wine [[Water of Lustration]]; stone (col XL): Beryl or Aquamarine. Water-word for the water letter; no skipped chars (unknown()=[]).'),
        ('CALIX', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: cup). unknown()=[].'),
        ('VINUM', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: wine — the weapon names the Wine). unknown()=[].'),
        ('מים', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: water, mayim). unknown()=[].'),
    ]),
    ('CLXXXVII/27', '27', 'Peh (Mouth, Mars), 27th path', [
        ('GLADIUS', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Sword; stone (col XL): Ruby, any red stone. unknown()=[].'),
        ('חרב', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: sword, cherev). unknown()=[].'),
        ('FERRUM', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: iron — the Mars metal; the sword\'s matter). unknown()=[].'),
    ]),
    ('CLXXXVII/28', '28', 'Tzaddi (Fish-hook), 28th path', [
        ('THUS', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Censer or Aspergillus; stone (col XL): Artificial Glass [[Chalcedony]]. The censer burns incense (Latin thus). unknown()=[].'),
        ('קטרת', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: incense, qetoret). gadol identical (709, no final forms) — not duplicated. unknown()=[].'),
        ('θυμιαμα', 'alternate', ['greek'],
         'ALTERNATE (Greek: incense, thymiama). unknown()=[].'),
    ]),
    ('CLXXXVII/29', '29', 'Qoph (Back of head, Moon), 29th path', [
        ('SPECULUM', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Twilight of the Place and Magic Mirror; stone (col XL): Pearl. The mirror is the operative instrument. unknown()=[].'),
        ('LUNA', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: moon — Qoph is the lunar letter). unknown()=[].'),
        ('מראה', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: mirror, mar\'eh). unknown()=[].'),
        ('σεληνη', 'alternate', ['greek'],
         'ALTERNATE (Greek: moon, selene). NOTE: =301, same number as אש (Hebrew fire, /31 proposal) — two different words, two tongues: coincidence, NOT a bridge. Chance-flagged. unknown()=[].'),
    ]),
    ('CLXXXVII/31', '31', 'Shin (Tooth, Fire), 31st path', [
        ('IGNIS', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Wand or Lamp, Pyramid of B [[The Thurible]]; stone (col XL): Fire Opal. Fire-word for the fire letter. unknown()=[].'),
        ('אש', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: fire, esh). NOTE: =301, same number as σεληνη (/29 alternate) — coincidence, NOT a bridge. Chance-flagged. unknown()=[].'),
        ('LUX', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: light — the Lamp). unknown()=[].'),
        ('LAMPAS', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: lamp, torch). unknown()=[].'),
        ('πυρ', 'alternate', ['greek'],
         'ALTERNATE (Greek: fire, pyr). unknown()=[].'),
    ]),
    ('CLXXXVII/32', '32', 'Tau (Cross, Saturn), 32nd path', [
        ('FALX', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): A Sickle; stone (col XL): Onyx. Saturn\'s reaping instrument. unknown()=[].'),
        ('חרמש', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: sickle, chermesh). unknown()=[].'),
        ('MESSIS', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: harvest — the sickle\'s work). unknown()=[].'),
        ('αρπη', 'alternate', ['greek'],
         'ALTERNATE (Greek: sickle, harpe). unknown()=[].'),
    ]),
    ('CLXXXVII/32 bis', '32 bis', 'Earth (added row)', [
        ('SAL', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): The Pantacle or [[Bread and]] Salt; stone (col XL): Salt. NOTE: Latin ordinal SAL=32 echoes the row number (32 bis) — chance-flagged coincidence, NOT a bridge. unknown()=[].'),
        ('מלח', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: salt, melach). NOTE: מלח=78 = לחם (bread) in the Hebrew bank — two different words, one bank: notable convergence, NOT a bridge. Chance-flagged. unknown()=[].'),
        ('לחם', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: bread, lechem) — the weapon names Bread AND Salt; see מלח=לחם=78 note above. unknown()=[].'),
        ('TERRA', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: earth). unknown()=[].'),
        ('PANIS', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: bread). unknown()=[].'),
    ]),
    ('CLXXXVII/31 bis', '31 bis', 'Spirit (added row)', [
        ('OVUM', 'PRIMARY', ['latin', 'agrippa'],
         'PRIMARY. Weapon (col XLI): [[The Winged Egg]]; stone (col XL): Black Diamond. The egg of spirit. unknown()=[].'),
        ('רוח', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: spirit, ruach). unknown()=[].'),
        ('ביצה', 'alternate', ['hebrew'],
         'ALTERNATE (Hebrew: egg, betzah). unknown()=[].'),
        ('SPIRITUS', 'alternate', ['latin', 'agrippa'],
         'ALTERNATE (Latin: spirit). unknown()=[].'),
        ('πνευμα', 'alternate', ['greek'],
         'ALTERNATE (Greek: spirit, pneuma). unknown()=[].'),
    ]),
]

BANK_LABEL = {'latin': 'LATIN-ORDINAL', 'agrippa': 'AGRIPPA', 'greek': 'GREEK',
              'hebrew': 'HEBREW', 'gadol': 'HEBREW-GADOL'}

with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['cell_id', 'column', 'row', 'column_title', 'row_meaning',
                'proposal', 'bank', 'value', 'tier', 'bridge', 'notes',
                'flag', 'worker'])
    n = 0
    for cell_id, row, meaning, props in CELLS:
        for word, role, banks, notes in props:
            for b in banks:
                w.writerow([cell_id, COL, row, TITLE, meaning, word,
                            BANK_LABEL[b], W(word, b), 'constructed', 'no',
                            notes, FLAG, WORKER])
                n += 1
print(f'wrote {OUT}: {n} rows')
