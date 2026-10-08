#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — __init__.py — the public API
# v0.3.0 "The Third Span"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: ☉ in 14° 54′ Libra, ☽ in 14° 12′ Virgo, dies jovis,
# Anno V:xii e.n. (2026-10-08)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The name PONTIFEX ("bridge-builder") was proposed by the scribe and approved
# by the author's red pen, 2026-10-07. The doctrine is the author's; the
# mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   (The full statement stands in pontifex/engine.py; this module is the
#   public door — everything the API promises is exported here.)
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""PONTIFEX — the Universal Language Gematria Cartographer.

The public API. Everything a script, a CLI, or the HTTP server may use is
exported here:

    import pontifex
    pontifex.weigh('CELL', 'latin_ordinal')          # -> result dict
    pontifex.bridge('AXONEME', 'latin_ordinal', 'עז', 'hebrew')
    pontifex.weigh_melody('C E G')                   # the music bridge
    pontifex.weigh_via_hebrew_fallback('cell')       # mergers shown
    pontifex.self_test()                             # the instrument checks itself

Result dicts carry: word, system, value, provenance, breakdown (audit trail).
DOCTRINE: a result without provenance is a rumor — every weighing here has one.
"""

from .engine import (
    SYSTEMS,
    weigh,
    weigh_via_hebrew_fallback,
    bridge,
    transliterate_latin_to_hebrew,
    to_jsonable,
    self_test,
)
from .music import (
    NOTE_VALUES,
    MUSIC_CONVENTIONS,
    extract_pitches,
    weigh_melody,
)
from .tables import (
    HEBREW,
    GREEK,
    LATIN_ORDINAL,
    AGRIPPA,
    ARABIC_ABJAD,
    BRAILLE,
    LATIN_TO_HEBREW,
    LATIN_TO_HEBREW_DIGRAPHS,
    MERGERS,
)

__version__ = '0.3.0'

__all__ = [
    '__version__',
    'SYSTEMS',
    'weigh',
    'weigh_via_hebrew_fallback',
    'bridge',
    'transliterate_latin_to_hebrew',
    'to_jsonable',
    'self_test',
    'NOTE_VALUES',
    'MUSIC_CONVENTIONS',
    'extract_pitches',
    'weigh_melody',
    'HEBREW',
    'GREEK',
    'LATIN_ORDINAL',
    'AGRIPPA',
    'ARABIC_ABJAD',
    'BRAILLE',
    'LATIN_TO_HEBREW',
    'LATIN_TO_HEBREW_DIGRAPHS',
    'MERGERS',
]

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
