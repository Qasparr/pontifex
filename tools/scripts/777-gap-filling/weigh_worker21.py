#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# weigh_worker21.py — candidate weighings for PONTIFEX 777 gap-filling, worker-21
# (repo-exclusive helper: only meaningful inside this 777 run)
# =============================================================================
# Epigraph: "Every number is infinite; there is no difference." — Aleister Crowley, Liber 777
# Date: 2026-10-13. 93.
# Author of the operation: Johnathan 'Qasparr' (Κασπάρρ) Monroe.
# Method: Scientific Illuminism — hypothesis (candidate filling), method
# (weigh in each applicable bank via ptk), observation (value + unknown chars),
# result (recorded with tier; spreads reported, never single numbers).
# DOCTRINE: each word weighed in its own tongue; Hebrew fallback only for
# tongues with no table; English ordinal native for English only; three-tier
# provenance (attested/derived/constructed) on every value; a bridge needs TWO
# honest banks on the SAME word; English≡Latin ordinal is ONE bank.
# Closing: Love is the law, love under will.
# =============================================================================

import sys

sys.path.insert(0, "/home/hatch/workspace/pontifex/tools/ptk")
import weigh  # noqa: E402 — MECHANISM: the PONTIFEX weighing engine; never retype a letter table

# DOCTRINE: calibrate() must pass before any weighing is trusted.
assert weigh.calibrate() is True, "calibrate() FAILED — weighings untrustworthy"
print("calibrate: True\n")


# DOCTRINE: map bank-name -> the engine's letter-table dict for unknown()/breakdown().
BANK_TABLES = {
    "hebrew": weigh.HEBREW,
    "greek": weigh.GREEK,
    "latin": weigh.LATIN_ORDINAL,
    "agrippa": weigh.AGRIPPA,
    "arabic": weigh.ARABIC_ABJAD,
}


def report(label, word, bank_fn, bank_name, tier, note=""):
    """MECHANISM: weigh one (word, bank) pair, show breakdown + skipped chars."""
    table = BANK_TABLES[bank_name]
    value = bank_fn(word)
    skipped = weigh.unknown(word, table)
    pairs, total = weigh.breakdown(word, table)
    print(f"{label} | bank={bank_name} | value={value} | tier={tier}")
    print(f"  word: {word}")
    print(f"  breakdown: {'+'.join(f'{ch}={v}' for ch, v in pairs)} = {total}")
    print(f"  unknown/skipped: {skipped if skipped else 'none'}")
    if note:
        print(f"  note: {note}")
    print()
    return value, skipped


print("=" * 70)
print("CVIII/1 — 'Satan and Moloch' (princes of Thaumiel, Qliphoth of Kether)")
print("=" * 70)
# DOCTRINE: Hebrew is the native tongue of both names -> attested spellings.
report("Satan", "שטן", weigh.hebrew, "hebrew", "attested",
       "standard spelling; shin=300,teth=9,nun=50")
report("Moloch", "מלך", weigh.hebrew, "hebrew", "attested",
       "standard spelling (cf. Molekh); mem=40,lamed=30,kaph=20")
# English/Latin ordinal: native for English transliteration, but the WORD is
# Hebrew — so these weighings are constructed transliterations, ONE bank
# (English≡Latin ordinal counts once).
report("Satan", "SATAN", weigh.latin, "latin", "constructed",
       "transliteration of a Hebrew word; English ordinal is not its tongue")
report("Moloch", "MOLOCH", weigh.latin, "latin", "constructed",
       "transliteration of a Hebrew word")
# Greek cross-checks. MECHANISM NOTE: the engine's GREEK table is keyed on
# unaccented lowercase; accented vowels (ό, ύ) are SKIPPED (contribute 0).
# So the accented spellings are weighed accent-stripped and tiered
# constructed, with the skip made visible — the NT accent is real, the
# engine simply cannot take it.
report("Satan", "σαταν", weigh.greek, "greek", "constructed",
       "Hellenized form; no NT attestation in exactly this spelling")
report("Moloch", "μολοχ", weigh.greek, "greek", "constructed",
       "unaccented Hellenized form; engine skips ό so accent stripped openly")

print("=" * 70)
print("CVIII/2 — 'Beelzebub' (prince of Ghogiel, Qliphoth of Chokmah)")
print("=" * 70)
report("Beelzebub", "בעל זבוב", weigh.hebrew, "hebrew", "attested",
       "biblical spelling, 2 Kings 1:2 (Baal-zebub, 'lord of flies')")
report("Beelzebub", "BEELZEBUB", weigh.latin, "latin", "constructed",
       "transliteration of a Hebrew word")
report("Beelzebub", "βεελζεβουλ", weigh.greek, "greek", "constructed",
       "unaccented form of the NT spelling Beelzeboul (e.g. Matt 12:24); "
       "engine skips ύ so the accent is stripped openly, hence constructed")

print("=" * 70)
print("Sanity: Arabic counterparts relevant to the LII bis-row ruling")
print("=" * 70)
# tha (counterpart of Hebrew Tau, already at LII row 4 = 500)
report("tha", "ث", weigh.arabic, "arabic", "attested",
       "abjad value 500 — already placed at LII row 4")
# shin (counterpart of Hebrew Shin, already at LII row 31 = 300)
report("shin", "ش", weigh.arabic, "arabic", "attested",
       "abjad value 300 — already placed at LII row 31")
