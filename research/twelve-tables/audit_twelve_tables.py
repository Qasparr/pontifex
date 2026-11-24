#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
93
THE TWELVE TABLES — THE AUDIT (Phase 4). Independent of the builder:
reads only the frozen tables_register.json + census.json and the
sealed engine, recomputes every priced cell from its frozen
rendering, reconciles every tongue against the census, proves the
twelve frames are one grid, and re-runs the engine's parity
batteries. Prints the verdict: PASS, or the failing coordinates.
Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
(Greek, -ARR, All Rights Reserved, Without Prejudice).
XXIV day of November, Dies Martis, Sol in Sagittario, Anno V:xii
e.n. (2026 e.v.)
Scientific Illuminism: Method of Science, Aim of Religion.
Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR,
All Rights Reserved, Without Prejudice.
"""
import json, subprocess, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent))
from pontifex.engine import weigh, hangul, armenian

tables = json.loads((HERE / 'tables_register.json').read_text(encoding='utf-8'))
census = json.loads((HERE / 'census.json').read_text(encoding='utf-8'))
fails = []
notes = []

def recompute(tid, row):
    r, v = row['rendering'], row['value']
    if tid == 'latin':
        return (weigh(r, 'latin_ordinal')['value'],
                weigh(r, 'agrippa')['value'])
    if tid == 'korean':
        return hangul(r)['value']
    if tid == 'armenian' and 'ARMENIAN_LATE' in (row.get('scheme') or ''):
        return armenian(r, late=True)['value']
    bank = tables[tid]['bank']
    return weigh(r, bank)['value']

frames = {}
for tid, t in tables.items():
    rows = t['rows']
    frames[tid] = [(r['cell_id'], r.get('proposal_idx')) for r in rows]
    # (b) reconciliation against the census
    states = Counter(r['state'] for r in rows)
    if len(rows) != census['frame_rows']:
        fails.append(f'{tid}: {len(rows)} rows != census frame {census["frame_rows"]}')
    priced_states = states['NATIVE'] + states['DOOR']
    accounted = priced_states + states['HOLE'] + states['FENCED']
    if accounted != census['word_cells']:
        fails.append(f'{tid}: native+door+hole+fenced = {accounted} != word cells {census["word_cells"]}')
    if states['EMPTY'] + states['GAP'] != census['non_word_cells']:
        fails.append(f'{tid}: empty+gap != non-word cells')
    # (a) independent recomputation of every priced cell
    checked = 0
    for r in rows:
        if r['state'] in ('NATIVE', 'DOOR'):
            got = recompute(tid, r)
            want = r['value']
            if tid == 'latin':
                ok = got == (want['latin_ordinal'], want['agrippa'])
            else:
                ok = got == want
            checked += 1
            if not ok:
                fails.append(f'{tid} {r["cell_id"]}: frozen {want} != recomputed {got} (rendering {r["rendering"]!r})')
        elif r['state'] in ('HOLE', 'FENCED'):
            if r['value'] is not None:
                fails.append(f'{tid} {r["cell_id"]}: {r["state"]} cell carries a value')
        # Hebrew dresses: the identity, recomputed
        if tid == 'hebrew' and 'aramaic_dresses' in r:
            d = r['aramaic_dresses']
            vi = weigh(d['imperial'], 'aramaic')['value']
            vs = weigh(d['syriac'], 'aramaic')['value']
            if not (vi == vs == d['value'] == r['value']):
                fails.append(f'hebrew {r["cell_id"]}: dress identity fails '
                             f'(imp {vi}, syr {vs}, frozen {d["value"]}, hebrew {r["value"]})')
    notes.append(f'{tid}: {checked} priced cells recomputed, '
                 f'{states["HOLE"]} holes, {states["FENCED"]} fenced')

# (b2) the twelve frames are the SAME grid
ref = frames['greek']
for tid, fr in frames.items():
    if fr != ref:
        fails.append(f'{tid}: frame parts from the Greek frame')

# (c) the bank seals: every parity battery at the repo root
batteries = sorted(ROOT.glob('test_*_parity.py'))
battery_lines = []
for b in batteries:
    p = subprocess.run([sys.executable, str(b)], capture_output=True,
                       text=True, cwd=ROOT,
                       env={'PATH': '/usr/bin:/bin:/usr/local/bin',
                            'PYTHONPATH': f'{ROOT}:{ROOT.parent}'})
    tail = (p.stdout.strip().splitlines() or [''])[-1]
    battery_lines.append(f'{b.name}: rc={p.returncode} — {tail[:90]}')
    if p.returncode != 0:
        fails.append(f'battery {b.name} FAILED: {tail}')

print('=== THE TWELVE TABLES — AUDIT ===')
for n in notes:
    print(' ', n)
print(' batteries:')
for l in battery_lines:
    print(' ', l)
if fails:
    print(f'VERDICT: FAIL — {len(fails)} failing coordinates:')
    for f in fails[:40]:
        print('  ✗', f)
    sys.exit(1)
print('VERDICT: PASS — every priced cell recomputes exact; every '
      'tongue reconciles to the census; the twelve frames are one '
      'grid; all parity batteries green.')
