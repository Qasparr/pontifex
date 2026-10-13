#!/usr/bin/env python3
"""worker-06 cell weighing harness — column XXIV candidates.

MECHANISM: weighs each Sanskrit/Pali candidate term in two banks:
  1. LATIN_ORDINAL on the plain Latin transliteration (the word's romanized form)
  2. HEBREW on a documented Hebrew transliteration (Hebrew = proper fallback
     for tongues with no ptk table, per settled doctrine)
DOCTRINE: the transliteration scheme is a CONSTRUCTION — every value below is
constructed-tier. unknown() is checked on every weighing; skipped characters
are printed, never hidden.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/pontifex/tools/ptk")
import weigh

assert weigh.calibrate(), "calibrate() FAILED"

# Sanskrit->Hebrew scheme (constructed, documented):
# a/aa->aleph (final -a -> he), i/ii->yod, u/uu->vav, e->aleph, o->vav
# k/kh->kaf, g/gh->gimel, ng->nun, c/ch->tzadi, j/jh->gimel (collapse noted)
# t/th(retroflex)->tet, d/dh(retroflex)->dalet, n(retroflex)->nun
# t/th(dental)->tav, d/dh(dental)->dalet, n->nun
# p/ph->pe, b/bh->bet, m->mem, y->yod, r->resh, l->lamed, v->vav
# s->samekh, sh(palatal)->shin, s(retroflex)->samekh (collapse noted), h->he

CANDS = [
    # (cell, proposal, latin_weighed, hebrew_weighed)
    ("XXIV/15", "Success in Karma-yoga", "KARMAYOGA", "\u05db\u05e8\u05de\u05d4\u05d9\u05d5\u05d2\u05d4"),
    ("XXIV/17", "Success in Jnana-yoga", "JNANAYOGA", "\u05d2\u05e0\u05d0\u05e0\u05d4\u05d9\u05d5\u05d2\u05d4"),
    ("XXIV/17", "Vision of Budha", "BUDHA", "\u05d1\u05d5\u05d3\u05d4"),
    ("XXIV/18", "Soma-bhawana", "SOMABHAWANA", "\u05e1\u05d5\u05de\u05d4\u05d1\u05d4\u05d0\u05d5\u05d0\u05e0\u05d4"),
    ("XXIV/18", "Success in Mantra-yoga", "MANTRAYOGA", "\u05de\u05d0\u05e0\u05ea\u05e8\u05d4\u05d9\u05d5\u05d2\u05d4"),
    ("XXIV/19", "Tejo-bhawana", "TEJOBHAWANA", "\u05ea\u05d0\u05d2\u05d5\u05d1\u05d4\u05d0\u05d5\u05d0\u05e0\u05d4"),
    ("XXIV/19", "Tapas-siddhi", "TAPASSIDDHI", "\u05ea\u05d0\u05e4\u05d0\u05e1\u05e1\u05d9\u05d3\u05d9"),
    ("XXIV/20", "Success in Kriya-yoga", "KRIYAYOGA", "\u05db\u05e8\u05d9\u05d9\u05d4\u05d9\u05d5\u05d2\u05d4"),
    ("XXIV/20", "Viveka-bhawana", "VIVEKABHAWANA", "\u05d5\u05d9\u05d5\u05d0\u05db\u05d4\u05d1\u05d4\u05d0\u05d5\u05d0\u05e0\u05d4"),
    ("XXIV/21", "Guru-darshana", "GURUDARSHANA", "\u05d2\u05d5\u05e8\u05d5\u05d3\u05d0\u05e8\u05e9\u05d0\u05e0\u05d4"),
    ("XXIV/21", "Success in Raja-yoga", "RAJAYOGA", "\u05e8\u05d0\u05d2\u05d4\u05d9\u05d5\u05d2\u05d4"),
    ("XXIV/22", "Tula-bhawana", "TULABHAWANA", "\u05ea\u05d5\u05dc\u05d4\u05d1\u05d4\u05d0\u05d5\u05d0\u05e0\u05d4"),
    ("XXIV/22", "Dharma-darshana", "DHARMADARSHANA", "\u05d3\u05d0\u05e8\u05de\u05d4\u05d3\u05d0\u05e8\u05e9\u05d0\u05e0\u05d4"),
]

for cell, prop, lat, heb in CANDS:
    vl = weigh.weigh(lat, weigh.LATIN_ORDINAL)
    vh = weigh.weigh(heb, weigh.HEBREW)
    ul = weigh.unknown(lat, weigh.LATIN_ORDINAL)
    uh = weigh.unknown(heb, weigh.HEBREW)
    bl = weigh.breakdown(lat, weigh.LATIN_ORDINAL)
    bh = weigh.breakdown(heb, weigh.HEBREW)
    print(f"{cell} | {prop}")
    print(f"  LATIN  '{lat}' = {vl}  unknown={ul}")
    print(f"  HEBREW '{heb}' = {vh}  unknown={uh}")
    assert vl == bl[1], "latin breakdown mismatch"
    assert vh == bh[1], "hebrew breakdown mismatch"
print("ALL BREAKDOWNS VERIFIED")
