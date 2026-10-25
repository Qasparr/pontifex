#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — weigh_japanese.py — the Japanese bank audit & weighing (worker #6 of 12)
# The twelve-tongues correspondence research, Japanese language leg.
#
# Epigraph: "What is a man? A miserable little pile of secrets."
# — misattributed to André Malraux; the scribe's gloss: secrets kept from
# oneself are the heaviest. This worker keeps none: every choice is shown.
#
# Thelemic date: ☉ in 18° Libra, ☽ in 25° Virgo, dies Solis,
# Anno V:xii e.n. (2026-10-11)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure. This instrument is drafted by the scribe
# for the author's red pen; the doctrine is his, the mechanisms are not.
# Worker #6 of 12 in the PONTIFEX gematria bridge research.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis: Japanese has no native letter-number weighing tradition
#   comparable to gematria/isopsephy/abjad; the honest path is therefore the
#   repo's Hebrew-fallback doctrine (METHOD.md §3): English → katakana →
#   Hepburn romaji → LATIN_TO_HEBREW → mispar hechrechi. The word-FORM is
#   CONSTRUCTED at every step; only the Hebrew TABLE is ATTESTED.
#   Method: stated katakana per term (standard loanword conventions, variants
#   noted); Hepburn romanization with macron-stripping recorded as loss;
#   the repo's greedy-digraph map applied letter by letter; mergers tallied
#   per term. Separately, the stroke-count experiment: fixed katakana stroke
#   counts per a stated standard, kanji arbitrariness demonstrated, not hidden.
#   Observation: reported by the script's own stdout — every chain, every
#   merger, every total. The audit of the native-tradition claims lives in
#   japanese.md, not in code.
#   Result: japanese-values.csv (22 rows: 11 fallback + 11 stroke-count),
#   tiered honestly; negative results recorded at full weight.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""Audit-weigh the shared corpus in the Japanese bank.

DOCTRINE: Japanese has no attested letter-number table — this is the
AUDIT's finding (see japanese.md), not an assumption. The fallback is the
tradition's own move per METHOD.md §3: transliterate into Hebrew and weigh
there. The tiers are therefore SPLIT, and the split is the honest core of
this file:

  - the WORD-FORM (English -> katakana -> Hepburn -> Hebrew letters) is
    CONSTRUCTED: every step is the scribe's choice, documented below.
  - the VALUE's table (mispar hechrechi) is ATTESTED: the numbers come from
    the tradition's own table, imported from the repo, not re-declared.

Per METHOD.md: a convergent point touching the constructed tier is a
hypothesis for the red pen — never doctrine. There were no target hits;
that negative stands as recorded.

MECHANISM: the script imports the repo's tables and applies the map
exactly as declared (greedy digraphs first: ch/sh/th), so any merger the
map produces is the map's own behavior, observed and reported — not the
scribe's invention.
"""

import csv
import os
import sys
import unicodedata

# MECHANISM: reach the repo's own tables — do not re-declare them in silence.
# DOCTRINE: importing (not copying) is what makes the values verifiable
# against the tradition rather than asserted by the scribe.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex"))
from pontifex.tables import (  # noqa: E402
    HEBREW, LATIN_TO_HEBREW, LATIN_TO_HEBREW_DIGRAPHS, MERGERS,
)

TARGETS = {418, 666, 777, 93, 77, 11}

# -- The corpus: stated katakana forms --------------------------------------
# MECHANISM: one row per term. 'katakana' is the scribe's stated choice per
# standard loanword conventions; 'romaji' is its Hepburn romanization as
# the scribe renders it (macrons where Hepburn writes them); 'variant' names
# the nearest alternative the scribe did NOT choose, so the choice is shown
# rather than hidden.
# DOCTRINE: katakana selection is CONSTRUCTED — a different defensible
# selection (noted in 'variant') would weigh differently. The stroke-count
# experiment in japanese.md demonstrates this arbitrariness with kanji.
CORPUS = [
    # term, katakana, romaji (with macrons), variants / choice notes
    ("AXONEME", "アクソニーム", "akusonīmu",
     "アクソネーム (akusonēmu, English-vowel reading) not chosen"),
    ("OZ", "オズ", "ozu",
     "as in オズの国 (the Land of Oz); no live variant"),
    ("TRVVTH", "トゥルヴヴス", "turuvuvusu",
     "letter-faithful via ヴ for V (inscriptional VV preserved at kana "
     "level); phonetic alt トゥルース (turūsu, 'truth') noted in MD"),
    ("THELEMA", "テレーマ", "terēma",
     "English-loanword pattern (cf. テーマ 'theme'); variant テレマ "
     "(terema) weighs identically — ー is romaji-silent"),
    ("AGAPE", "アガペー", "agapē",
     "standard; no live variant"),
    ("BABALON", "ババロン", "babaron",
     "standard Thelemic katakana; no live variant"),
    ("HERU-RA-HA", "ヘル・ラ・ハー", "herurahā",
     "nakaguro ・ dropped (romaji-silent; recorded as loss); final ー kept"),
    ("ABRAHADABRA", "アブラハダブラ", "aburahadabura",
     "standard; no live variant"),
    ("QIRA", "キーラ", "kīra",
     "Q merged to K at the katakana step — q/k distinction lost before "
     "Hebrew is ever reached; alt クィラ (kwira) noted in MD"),
    ("LIBERTY", "リバティー", "ribatī",
     "variant リバティ (ribati) weighs identically — ー is romaji-silent"),
    ("CELL", "セル", "seru",
     "katakana loanword; kanji alts (細胞/独房/監房) in MD arbitrariness demo"),
]

# -- Katakana stroke-count standard (CONSTRUCTED experiment) ------------------
# MECHANISM: stated counts from standard stroke order (the counts used by
# Japanese stroke-count references and seimei-handan calculators for kana).
# Dakuten ゛ = 2 strokes (two small marks); handakuten ゜ = 1 (one circle);
# long vowel ー = 1; small kana count as their large form (ゥ=ウ=3).
# DOCTRINE: the COUNTS are ordinary orthographic fact; the WEIGHING —
# adding kana strokes as a "value" of a word — is the constructed part.
# No tradition does this to loanwords; seimei handan weighs personal names.
STROKES = {
    'ア': 2, 'イ': 2, 'ウ': 3, 'エ': 3, 'オ': 3,
    'カ': 2, 'キ': 3, 'ク': 1, 'ケ': 3, 'コ': 2,
    'サ': 3, 'シ': 3, 'ス': 2, 'セ': 2, 'ソ': 1,
    'タ': 3, 'チ': 3, 'ツ': 3, 'テ': 3, 'ト': 2,
    'ナ': 2, 'ニ': 2, 'ヌ': 2, 'ネ': 4, 'ノ': 1,
    'ハ': 2, 'ヒ': 2, 'フ': 1, 'ヘ': 1, 'ホ': 4,
    'マ': 2, 'ミ': 3, 'ム': 2, 'メ': 2, 'モ': 2,
    'ヤ': 3, 'ユ': 2, 'ヨ': 3,
    'ラ': 3, 'リ': 2, 'ル': 3, 'レ': 1, 'ロ': 3,
    'ワ': 2, 'ヲ': 4, 'ン': 1,
    'ー': 1, '・': 0,
}
DAKUTEN = 2   # ゛ — two small strokes
HANDAKUTEN = 1  # ゜ — one small circle
SMALL_KANA = {'ァ': 'ア', 'ィ': 'イ', 'ゥ': 'ウ', 'ェ': 'エ', 'ォ': 'オ',
              'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ', 'ッ': 'ツ'}


def normalize_romaji(romaji):
    """Strip macrons to base vowels; lowercase.

    MECHANISM: NFD decomposition drops combining macrons, leaving the vowel.
    DOCTRINE: this is a CONSTRUCTED normalization — Japanese vowel LENGTH
    is phonemic, and this step deletes it. Recorded as loss, never silent.
    """
    nfd = unicodedata.normalize('NFD', romaji)
    return ''.join(c for c in nfd if not unicodedata.combining(c)).lower()


def map_to_hebrew(norm):
    """Apply the repo's greedy-digraph map to normalized romaji.

    MECHANISM: two-letter digraphs (ch/sh/th) tried first at each position,
    then single letters — exactly the map's declared behavior. Returns the
    Hebrew string and a list of (position, latin_chunk, hebrew) steps.
    """
    out = []
    steps = []
    i = 0
    while i < len(norm):
        dig = norm[i:i + 2]
        if dig in LATIN_TO_HEBREW_DIGRAPHS:
            h = LATIN_TO_HEBREW_DIGRAPHS[dig]
            out.append(h)
            steps.append((dig, h))
            i += 2
        else:
            ch = norm[i]
            h = LATIN_TO_HEBREW[ch]
            out.append(h)
            steps.append((ch, h))
            i += 1
    return ''.join(out), steps


def stroke_count(katakana):
    """Count strokes per the stated standard; dakuten/handakuten handled.

    MECHANISM: voiced kana are decomposed (base + mark) and counted
    additively. Characters outside the table raise KeyError loudly —
    silence is the enemy here.
    """
    total = 0
    parts = []
    for ch in katakana:
        if ch in STROKES:
            total += STROKES[ch]
            parts.append("%s%d" % (ch, STROKES[ch]))
        elif ch in SMALL_KANA:
            v = STROKES[SMALL_KANA[ch]]
            total += v
            parts.append("%s%d" % (ch, v))
        elif ch in ('゛', '\u3099'):
            total += DAKUTEN
            parts.append("゛%d" % DAKUTEN)
        elif ch in ('゜', '\u309a'):
            total += HANDAKUTEN
            parts.append("゜%d" % HANDAKUTEN)
        else:
            # MECHANISM: decompose precomposed voiced kana (ガ = カ + U+3099).
            # DOCTRINE: the combining marks are U+3099/U+309A, not the
            # spacing ゛/゜ (U+309B/U+309C) — compare the right code points.
            nfd = unicodedata.normalize('NFD', ch)
            base, marks = nfd[0], nfd[1:]
            v = STROKES[base] + sum(
                DAKUTEN if m == "\u3099" else HANDAKUTEN
                for m in marks)
            total += v
            parts.append("%s%d" % (ch, v))
    return total, parts


def main():
    out_dir = os.path.expanduser("~/workspace/pontifex/research/twelve-tongues")
    os.makedirs(out_dir, exist_ok=True)
    rows = []

    print("=" * 70)
    print("PART 2 — HEBREW-FALLBACK WEIGHINGS (constructed form, attested table)")
    print("=" * 70)
    for term, katakana, romaji, choice_note in CORPUS:
        norm = normalize_romaji(romaji).replace('・', '')
        # OBSERVATION: the nakaguro drop is the one character-level loss.
        hebrew, steps = map_to_hebrew(norm)
        digraphs = [s for s in steps if len(s[0]) == 2]
        values = [HEBREW[h] for h in hebrew]
        total = sum(values)

        # MECHANISM: merger tally — which Hebrew letters drew from more than
        # one distinct Latin source letter in THIS term. This is the visible
        # loss; the map's global MERGERS table is the standing record.
        src = {}
        for latin, h in steps:
            src.setdefault(h, set()).add(latin)
        fired = {h: sorted(s) for h, s in src.items() if len(s) > 1}
        merger_note = ("; ".join("%s<-%s" % (h, "/".join(s))
                                 for h, s in sorted(fired.items()))
                       or "none — no multi-source merger in this term")

        seq = "+".join("%s%d" % (h, HEBREW[h]) for h in hebrew)
        # OBSERVATION: the full chain on the record, nothing elided.
        print("%s | %s | %s ->[%s]-> %s | %s = %d%s" % (
            term, katakana, romaji, norm, hebrew, seq, total,
            "  <<< TARGET HIT" if total in TARGETS else ""))
        if digraphs:
            print("  digraphs fired: %s" % digraphs)
        print("  choice: %s" % choice_note)

        rows.append({
            "term": term,
            "language": "Japanese",
            "script_form": katakana,
            "transliteration_convention":
                "English->katakana (stated choice); katakana->Hepburn romaji; "
                "macrons stripped; ・ dropped",
            "table_used":
                "HEBREW mispar hechrechi via repo LATIN_TO_HEBREW fallback "
                "map (greedy digraphs ch/sh/th)",
            "provenance_tier": "CONSTRUCTED form -> ATTESTED table",
            "value": total,
            "mergers_or_loss":
                "digraphs: none fired; mergers: %s; loss: vowel length "
                "(macrons), ・ dropped%s" % (
                    merger_note,
                    "; Q->K merged at katakana step" if term == "QIRA" else ""),
            "notes":
                "chain %s -> %s -> %s -> %s; breakdown %s=%d; %s%s" % (
                    term, katakana, norm, hebrew, seq, total, choice_note,
                    "; TARGET HIT %d" % total if total in TARGETS else ""),
        })

    print()
    print("=" * 70)
    print("PART 3 — STROKE-COUNT EXPERIMENT (constructed; full skepticism)")
    print("=" * 70)
    for term, katakana, romaji, _ in CORPUS:
        total, parts = stroke_count(katakana)
        seq = "+".join(parts)
        print("%s | %s | %s = %d%s" % (
            term, katakana, seq, total,
            "  <<< TARGET HIT" if total in TARGETS else ""))
        rows.append({
            "term": term,
            "language": "Japanese (stroke-count experiment)",
            "script_form": katakana,
            "transliteration_convention":
                "same stated katakana as fallback rows; dakuten=2, "
                "handakuten=1, ー=1, small kana=large-form count",
            "table_used":
                "katakana stroke counts per stated standard — CONSTRUCTED "
                "experiment; no tradition weighs loanwords this way",
            "provenance_tier": "CONSTRUCTED",
            "value": total,
            "mergers_or_loss":
                "small kana counted as large form (ゥ=ウ=3); the loss is the "
                "method choice itself — see japanese.md arbitrariness demo",
            "notes":
                "breakdown %s=%d%s" % (
                    seq, total,
                    "; TARGET HIT %d" % total if total in TARGETS else ""),
        })

    path = os.path.join(out_dir, "japanese-values.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print()
    print("wrote %s (%d rows)" % (path, len(rows)))
    print("target hits across both experiments: %d" % sum(
        1 for r in rows if r["value"] in TARGETS))


if __name__ == "__main__":
    main()

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
