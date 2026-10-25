#!/usr/bin/env python3
"""Worker B: gematria recomputation sweep over Crowley's printed X=N claims.
Calibration: יופיאל must recompute 137; ראהוור must recompute 418.
Tables imported from pontifex (attested), never retyped.
"""
import json, re, sys, csv, html
sys.path.insert(0, '/home/hatch/workspace/pontifex')
from pontifex.tables import HEBREW, GREEK, LATIN_ORDINAL, AGRIPPA

CORPUS = '/home/hatch/workspace/pontifex/research/crowley-race-question/corpus'

def weigh_hebrew(word):
    letters = re.sub('[^\u0590-\u05EA]', '', word)
    if not letters:
        return None, ''
    return sum(HEBREW[c] for c in letters), letters

def weigh_greek(word):
    letters = re.sub('[^\u0370-\u03FF\u1F00-\u1FFFϛϟϡ]', '', word)
    if not letters:
        return None, ''
    vals = []
    for c in letters:
        if c in GREEK:
            vals.append(GREEK[c])
    if not vals:
        return None, ''
    return sum(vals), letters

def weigh_latin_ordinal(word):
    letters = re.sub('[^A-Za-z]', '', word).upper()
    if not letters:
        return None, ''
    return sum(LATIN_ORDINAL[c] for c in letters), letters

# ---------- calibration ----------
cal = [('יופיאל', 137, weigh_hebrew), ('ראהוור', 418, weigh_hebrew)]
for w, want, fn in cal:
    got, _ = fn(w)
    status = 'OK' if got == want else 'FAIL'
    print(f'CALIBRATION {w}: recomputed={got} expected={want} [{status}]')
    assert got == want, 'calibration failed'

results = {'mismatches': [], 'correct_sample': []}

# ---------- 1. Sepher Sephiroth (alanwillms transcription of 1912) ----------
d = json.load(open(f'{CORPUS}/sepher-sephiroth/output/sepher_sephiroth.json', encoding='utf-8'))
n_words = 0
for e in d:
    num = e['number']
    for w in e.get('words', []):
        h = w.get('hebrew', '')
        got, letters = weigh_hebrew(h)
        if got is None:
            continue
        n_words += 1
        rec = {'word_hebrew': h, 'letters_used': letters, 'printed': num,
               'recomputed': got, 'transliteration': w.get('word', ''),
               'desc': w.get('desc', '')[:120], 'source': 'Sepher Sephiroth (Equinox I:8, 1912; via alanwillms transcription)'}
        if got != num:
            results['mismatches'].append(rec)
        elif len(results['correct_sample']) < 12:
            results['correct_sample'].append(rec)
print(f'Sepher Sephiroth: {n_words} weighable words, {len(results["mismatches"])} mismatches')

json.dump(results, open('/home/hatch/workspace/pontifex/research/crowley-race-question/work/sweep_b_raw.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved raw results')
