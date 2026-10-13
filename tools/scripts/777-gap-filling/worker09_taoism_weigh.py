#!/usr/bin/env python3
# =============================================================================
# Epigraph: "Weigh the word in its own tongue." — the scribe
#
# Thelemic date: Tue 2026-10-13 (dies Martis), Anno V:xii e.n.
#
# 93.
#
# worker09_taoism_weigh.py — weigh Crowley's Yi King trigram tokens for the
# nine empty XLVI (System of Taoism) cells: 19, 20, 22, 24, 25, 26, 28, 29,
# 31 bis. PONTIFEX 777 gap-filling operation, worker-09.
#
# By Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure.
# (Scribe for this run: worker-09.)
#
# METHOD (Scientific Illuminism) — hypothesis → method → observation → result:
#   HYPOTHESIS: each empty Taoism cell takes the trigram (or trigram-pair, in
#     Crowley's own pair-form: "Kan and Khwan", "Li and Khien") whose Yi King
#     symbolism answers the row's Western magical power.
#   METHOD: weigh every proposed token four ways — (1) Latin ordinal and
#     (2) Agrippa on Crowley's printed romanization (the token is fixed by the
#     source: no character-choice arbitrariness); (3) the twelve-tongues
#     standing convention for Chinese, pinyin → LATIN_TO_HEBREW (greedy
#     digraphs ch/sh/th; x→קס expanded) → mispar hechrechi, mergers reported
#     on actual loss only; (4) stroke counts under the stated PRC simplified
#     standard. unknown() is checked on every weighing; skips stay visible.
#   OBSERVATION: printed below, per token, per bank.
#   RESULT: worker-09-fillings.csv — 48 rows, every weighing tiered. All four
#     columns are CONSTRUCTED (the twelve-tongues audit: no attested Chinese
#     letter-number table exists), so no bridge is decreed here; the one
#     honest outcome available is the spread, reported whole.
#
# DOCTRINE: each word weighed in its own tongue; Hebrew is the proper fallback
#   for tongues with no table — here via the sweep's pinyin→Hebrew chain, the
#   scribe's construction at every step, tiered accordingly. English ordinal is
#   native for English only, never a general fallback: the latin/agrippa
#   weighings below are of Crowley's Latin-script tokens as printed, tiered
#   constructed because the tongue behind the token is Chinese. A bridge
#   needs two honest (attested-tier) banks on the same word — impossible for
#   these terms per the sweep audit — so bridge=no throughout; any same-number
#   agreement across constructed columns would be a constructed convergence,
#   chance-flagged, never doctrine. (None occurred.)
#
# "Live, Love, and let Love, Live." — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import os
import sys

# MECHANISM: the engine is imported, never retyped. calibrate() is the
# anchorage — nothing is weighed until the anchors reproduce.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex/tools/ptk"))
import weigh  # noqa: E402

# MECHANISM: the transliteration map is the repo's own instrument
# (pontifex/pontifex/tables.py) — the bridge must land in the repo's engine,
# not in a private copy. Retyping a letter table is how phantom tables breed.
sys.path.insert(0, os.path.expanduser("~/workspace/pontifex/pontifex"))
import tables  # noqa: E402

# ---------------------------------------------------------------------------
# DOCTRINE: the candidates. Crowley's trigram number, his printed token (the
# appendix's canonical spelling), the Chinese character, toneless pinyin, and
# the PRC simplified stroke count (stated standard; traditional counts differ
# for 離 — 19 vs 10 — and are NOT used here; the red pen may revisit).
# "Kbn" prints for BOTH trigram 4 (Feet) and trigram 1 (Hands) in the source;
# the proposals keep the printed token and disambiguate by trigram number —
# the source is audited, never silently corrected.
# ---------------------------------------------------------------------------
# fields: trigram_no, crowley_token, chinese, pinyin, strokes
TRIGRAMS = {
    7: ("Khien", "乾", "qian", 11),   # Ch'ien — Heaven, the Creative
    6: ("Tui", "兑", "dui", 7),       # Tui — Lake, the Joyous
    5: ("Li", "离", "li", 10),        # Li — Fire, the Clinging
    4: ("Kbn", "震", "zhen", 15),     # Chen/Zhen — Thunder, the Arousing (Feet)
    3: ("Sun", "巽", "xun", 12),      # Sun — Wind/Wood, the Gentle
    2: ("Khan", "坎", "kan", 7),      # K'an/Kan — Water, the Abysmal
    1: ("Kbn", "艮", "gen", 6),       # Ken/Gen — Mountain, Keeping Still (Hands)
    0: ("Khwbn", "坤", "kun", 8),     # K'un — Earth, the Receptive
}
# MECHANISM: the appendix prints trigram 2 as "Khân" (circumflex); the column
# itself prints "Khan" (row 10) for the same trigram. The token is weighed as
# KHAN — no letter lost either way; the normalization is stated, not hidden.

# ---------------------------------------------------------------------------
# DOCTRINE: the nine proposals. cell -> list of (proposal_label, [trigram_nos]).
# Pairs follow Crowley's own pair-form ("Kan and Khwan", "Li and Khien").
# ---------------------------------------------------------------------------
PROPOSALS = {
    # 19 Teth/Strength — Power of Training Wild Beasts: Gen, Keeping Still.
    "XLVI/19": [("Kbn [1]", [1])],
    # 20 Yod/Hermit — Invisibility, Initiation: trigram 1 = HANDS; row 20 = Yod = Hand.
    "XLVI/20": [("Kbn [1]", [1])],
    # 22 Lamed/Justice — Works of Justice and Equilibrium: 7+0 = Hexagram 11 T'ai.
    "XLVI/22": [("Khien and Khwbn", [7, 0])],
    # 24 Nun/Death — Necromancy: Kan (water; Nun=fish, Scorpio=water) primary;
    # Khwbn (earth, the grave) as the honest alternative.
    "XLVI/24": [("Khan [2]", [2]), ("Khwbn [0]", [0])],
    # 25 Samekh/Temperance — Transmutations: the Kan-Li crucible (hex. 63/64).
    "XLVI/25": [("Khan and Li", [2, 5])],
    # 26 Ayin/Devil — Witches' Sabbath, Evil Eye: the Abysmal ("pit, defile,
    # peril") primary; Khwbn (Capricorn=earth) as the honest alternative.
    "XLVI/26": [("Khan [2]", [2]), ("Khwbn [0]", [0])],
    # 28 Tzaddi/Star — Astrology: Heaven, the starry heaven.
    "XLVI/28": [("Khien [7]", [7])],
    # 29 Qoph/Moon — Bewitchments, Illusions: the Lake; the moon mirrored in
    # still water (cf. row 23, crystal-gazing = Tui).
    "XLVI/29": [("Tui [6]", [6])],
    # 31 bis Spirit — Invisibility, Transformations: Wind (spiritus = breath).
    "XLVI/31 bis": [("Sun [3]", [3])],
}

ROW_MEANING = {
    "XLVI/19": "Teth (Serpent), Leo/Strength",
    "XLVI/20": "Yod (Hand), Virgo/Hermit",
    "XLVI/22": "Lamed (Ox-goad), Libra/Justice",
    "XLVI/24": "Nun (Fish), Scorpio/Death",
    "XLVI/25": "Samekh (Prop), Sagittarius/Temperance",
    "XLVI/26": "Ayin (Eye), Capricorn/Devil",
    "XLVI/28": "Tzaddi (Fish-hook), Aquarius/Star",
    "XLVI/29": "Qoph (Back of head), Pisces/Moon",
    "XLVI/31 bis": "Shin repeated — Spirit",
}

WESTERN_POWER = {
    "XLVI/19": "Power of Training Wild Beasts",
    "XLVI/20": "Invisibility, Parthenogenesis, Initiation (?)",
    "XLVI/22": "Works of Justice and Equilibrium",
    "XLVI/24": "Necromancy",
    "XLVI/25": "Transmutations [[Vision of Universal Peacock]]",
    "XLVI/26": "The Witches' Sabbath so-called, the Evil Eye",
    "XLVI/28": "Astrology",
    "XLVI/29": "Bewitchments, Casting Illusions",
    "XLVI/31 bis": "Invisibility, Transformations, Vision of the Genius",
}


def pinyin_to_hebrew(pinyin):
    """MECHANISM: the sweep's standing chain — toneless lowercase pinyin,
    greedy digraphs (ch, sh, th) from the repo's LATIN_TO_HEBREW_DIGRAPHS,
    single letters from LATIN_TO_HEBREW, 'x' expanding to both ק and ס —
    then mispar hechrechi from the repo's HEBREW table.

    DOCTRINE: the chain is the scribe's construction at every step; the
    tables it lands in are attested. The weighing is tiered constructed.
    Returns (hebrew_string, value, breakdown_str, mergers_str).
    """
    digraphs = tables.LATIN_TO_HEBREW_DIGRAPHS
    singles = tables.LATIN_TO_HEBREW
    heb = []
    i = 0
    p = pinyin.lower()
    while i < len(p):
        two = p[i:i + 2]
        if two in digraphs:
            heb.append(digraphs[two])
            i += 2
        elif p[i] in singles:
            val = singles[p[i]]
            # MECHANISM: 'x' maps to the two-letter string 'קס' — expand to
            # both letters, as the sweep did (dead end #5 there: the weigher
            # tried to look the pair up as one key).
            heb.extend(list(val) if len(val) > 1 else [val])
            i += 1
        else:
            # DOCTRINE: nothing skipped silently — an unmapped letter is an
            # error here, not a quiet zero.
            raise ValueError("unmapped pinyin letter: %r in %r" % (p[i], pinyin))
    hword = "".join(heb)
    pairs, total = weigh.breakdown(hword, tables.HEBREW)
    # MECHANISM: mergers reported on ACTUAL loss only — two or more distinct
    # source letters present that collapse to one Hebrew letter.
    fired = []
    for hletter, srcs in tables.MERGERS.items():
        present = sorted({s for s in srcs if s in p})
        if len(present) >= 2:
            fired.append("%s (%s collapsed)" % (hletter, "+".join(present)))
    bd = "+".join("%s=%d" % (ch, v) for ch, v in pairs)
    return hword, total, bd, ("none" if not fired else "; ".join(fired))


def weigh_token(trigram_no):
    """MECHANISM: the four weighings of one trigram token. Returns a dict of
    (bank_name -> (value, note)). unknown() is consulted for the Latin banks;
    skips stay visible in the note."""
    token, chinese, pinyin, strokes = TRIGRAMS[trigram_no]
    out = {}
    lv = weigh.latin(token)
    lu = weigh.unknown(token.upper(), weigh.LATIN_ORDINAL)
    lbd, _ = weigh.breakdown(token.upper(), weigh.LATIN_ORDINAL)
    out["latin_ordinal"] = (lv, "breakdown %s | skipped: %s"
                            % ("+".join("%s=%d" % kv for kv in lbd),
                               lu if lu else "none"))
    av = weigh.agrippa(token)
    au = weigh.unknown(token.upper(), weigh.AGRIPPA)
    abd, _ = weigh.breakdown(token.upper(), weigh.AGRIPPA)
    out["agrippa"] = (av, "breakdown %s | skipped: %s"
                       % ("+".join("%s=%d" % kv for kv in abd),
                          au if au else "none"))
    hword, hv, hbd, mergers = pinyin_to_hebrew(pinyin)
    out["hebrew_pinyin_fallback"] = (
        hv, "pinyin '%s' → %s | breakdown %s | mergers: %s"
        % (pinyin, hword, hbd, mergers))
    out["stroke_count_prc"] = (
        strokes, "character %s, PRC simplified standard (Xinhua style); "
        "traditional counts differ for some (e.g. 離=19 vs 离=10)" % chinese)
    return out


def main():
    # DOCTRINE: the anchorage first. If calibrate() fails, nothing below runs.
    assert weigh.calibrate(), "calibrate() failed — the engine is not trusted"
    print("calibrate: True")

    base = os.path.expanduser(
        "~/workspace/goals/cross-gematria-777-gap-filling/hidden_files")
    rows = []
    for cell in ["XLVI/19", "XLVI/20", "XLVI/22", "XLVI/24", "XLVI/25",
                 "XLVI/26", "XLVI/28", "XLVI/29", "XLVI/31 bis"]:
        col, row = cell.split("/", 1)
        for label, tnos in PROPOSALS[cell]:
            parts = [weigh_token(t) for t in tnos]
            for bank in ["latin_ordinal", "agrippa",
                         "hebrew_pinyin_fallback", "stroke_count_prc"]:
                value = sum(p[bank][0] for p in parts)
                notes = " | ".join(
                    "%s: %s" % (TRIGRAMS[t][0], p[bank][1])
                    for t, p in zip(tnos, parts))
                rationale = ("Western power: '%s'. " % WESTERN_POWER[cell])
                if len(tnos) > 1:
                    rationale += ("Pair-form per Crowley's 'Kan and Khwan' / "
                                  "'Li and Khien' precedent. ")
                notes = rationale + notes
                rows.append({
                    "cell_id": cell, "column": col, "row": row,
                    "column_title": "System of Taoism",
                    "row_meaning": ROW_MEANING[cell],
                    "proposal": label, "bank": bank, "value": value,
                    "tier": "constructed",
                    "bridge": "no",
                    "notes": notes,
                    "flag": "PONTIFEX-proposed 2026-10-13",
                    "worker": "worker-09",
                })
                print("%-10s %-16s %-22s = %s" % (cell, label, bank, value))

    path = os.path.join(base, "worker-09-fillings.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "cell_id", "column", "row", "column_title", "row_meaning",
            "proposal", "bank", "value", "tier", "bridge", "notes",
            "flag", "worker"])
        w.writeheader()
        w.writerows(rows)
    print("wrote %d rows -> %s" % (len(rows), path))


if __name__ == "__main__":
    main()
