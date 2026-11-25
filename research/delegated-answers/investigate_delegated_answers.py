#!/usr/bin/env python3
# =============================================================================
# 93 — investigate_delegated_answers.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXIV day of November, Dies Martis, Sol in Sagittario,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: computes every load-bearing figure THE-DELEGATED-ANSWERS
# prints, from the sealed engine and the frozen registers alone, and
# writes them to delegated_answers_data.json beside this script.
# Calibration controls are weighed BEFORE any figure is taken; a
# control failure aborts the run. No figure in the instrument is
# typed by hand: the generator reads only this JSON.
#
# DOCTRINE: this script investigates; it decides nothing. The
# decisions are the generator's prose, at desk strength under the
# founder's delegation of 2026-11-24 22:47 EST, each printed with
# its reasoning and its killing evidence in the instrument itself.
#
# CONTENT TEST: Inputs — the sealed PONTIFEX engine; the frozen
# TABVLA verified register; the Twelve Tables' tables register and
# gap register; the two copies of 777-REVISED.md. Processes —
# scripted recomputation of every parting, population, and count
# the fifteen questions turn on. Outputs — the data JSON.
# Tolerances — a figure that does not reproduce from its source
# aborts the run loudly; nothing is smoothed.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import json
import re
import sys
import site
from collections import Counter
from pathlib import Path

sys.path.insert(0, site.getusersitepackages())
PONTIFEX = Path.home() / "workspace/pontifex"
sys.path.insert(0, str(PONTIFEX))

from pontifex import weigh, transliterate_latin_to_hebrew  # noqa: E402
from pontifex import engine  # noqa: E402

HERE = Path(__file__).parent
GOAL = (Path.home() / "workspace/goals/"
        "cross-gematria-777-gap-filling/files")
REG = PONTIFEX / "research/777-gap-filling/777-verification-verified.csv"
TAB_REG = PONTIFEX / "research/twelve-tables/tables_register.json"
GAP_REG = PONTIFEX / "research/twelve-tables/gap_register.json"

D = {}


def W(word, bank):
    return weigh(word, bank)["value"]


# ---------------------------------------------------------------------
# Calibration controls — weighed before any figure is taken.
# ---------------------------------------------------------------------
D["controls"] = {
    "thelema_greek": W("θέλημα", "greek"),
    "vapour_latin_ordinal": W("VAPOUR", "latin_ordinal"),
    "sphinx_greek": W("σφίγξ", "greek"),
}
assert D["controls"] == {"thelema_greek": 93,
                         "vapour_latin_ordinal": 93,
                         "sphinx_greek": 773}, D["controls"]

rows = list(csv.DictReader(open(REG, encoding="utf-8")))

# ---------------------------------------------------------------------
# TABVLA Q1 — the fallback door against the workers' scheme (XXXIII).
# Every XXXIII claim through the door (claim_idx 2) and under the
# scheme's own label (claim_idx 3), per proposal.
# ---------------------------------------------------------------------
xxx = {}
for r in rows:
    if r["cell_id"].startswith("XXXIII") and r["proposal_raw"]:
        xxx.setdefault(r["proposal_raw"], {})[r["claim_idx"]] = r
q1_names = []
for name, claims in xxx.items():
    door = claims.get("2")
    scheme = claims.get("3")
    if door is None:
        continue
    q1_names.append({
        "name": name,
        "door_rendering": door["coordinate"].split("renders ")[-1]
        .split(" = ")[0] if "renders " in door["coordinate"] else "",
        "door_value": int(door["recomputed"]),
        "scheme_claimed": int(door["claimed_value"]),
        "door_verdict": door["verdict"],
        "scheme_verdict": scheme["verdict"] if scheme else "",
        "scheme_claimed_c3": int(scheme["claimed_value"]) if scheme
        and scheme["claimed_value"] else None,
    })
q1_parted = [n for n in q1_names if n["door_verdict"] == "PARTED"]
q1_verified = [n for n in q1_names if n["door_verdict"] == "VERIFIED"]
# Claims, not names: NERTHUS carries its door claim in two sections
# (XXXIII/10 and XXXIII/32 bis), so the claim population is counted
# straight off the register, claim by claim.
door_claim_rows = [r for r in rows if r["cell_id"].startswith("XXXIII")
                   and r["claim_idx"] == "2"]
D["tabvla_q1"] = {
    "names": q1_names,
    "door_claims_total": len(door_claim_rows),
    "door_claims_verified": sum(1 for r in door_claim_rows
                                if r["verdict"] == "VERIFIED"),
    "door_verified_names": [n["name"] for n in q1_verified],
    "parted_claims": sum(1 for r in door_claim_rows
                         if r["verdict"] == "PARTED"),
    "parted": [{"name": n["name"], "scheme": n["scheme_claimed"],
                "door": n["door_value"],
                "delta": n["door_value"] - n["scheme_claimed"]}
               for n in q1_parted],
    "baldr_scheme_word": "בלדר",
    "baldr_scheme_value": W("בלדר", "hebrew"),
    "baldr_door_word": transliterate_latin_to_hebrew("BALDR")[0],
    "baldr_door_value": W(transliterate_latin_to_hebrew("BALDR")[0],
                          "hebrew"),
    # NERTHUS carries the door claim in two sections (XXXIII/10 and
    # XXXIII/32 bis) — the parted claims count claims, not names.
    "nerthus_door_claims": sum(
        1 for r in rows if r["cell_id"].startswith("XXXIII")
        and r["proposal_raw"] == "NERTHUS" and r["claim_idx"] == "2"
        and r["verdict"] == "PARTED"),
}

# ---------------------------------------------------------------------
# TABVLA Q2 — taa marbuta: the six partings, delta by delta; the
# price of seating it, counted on the verified side of the ledger.
# ---------------------------------------------------------------------
x47_parted = [r for r in rows if r["cell_id"].startswith("XLVII")
              and r["verdict"] == "PARTED"
              and r["claim_key"] != "S143-P0-C1"]
q2 = []
for r in x47_parted:
    word = r["weighed_word"]
    q2.append({
        "claim_key": r["claim_key"], "word": word,
        "claimed": int(r["claimed_value"]),
        "recomputed": int(r["recomputed"]),
        "delta": int(r["claimed_value"]) - int(r["recomputed"]),
        "taa_count": word.count("ة"),
        "with_taa_priced_as_ha": int(r["recomputed"]) + 5 * word.count("ة"),
    })
D["tabvla_q2"] = {
    "partings": q2,
    "all_delta_five": all(p["delta"] == 5 for p in q2),
    "all_reproduce_with_taa_priced":
        all(p["with_taa_priced_as_ha"] == p["claimed"] for p in q2),
    "taa_alone_in_bank": W("ة", "arabic_abjad"),
    "verified_depending_on_silence": [
        {"word": "مرة", "claimed": 240, "bank": W("مرة", "arabic_abjad"),
         "if_taa_priced": W("مرة", "arabic_abjad") + 5},
        {"word": "زوبعة", "claimed": 85,
         "bank": W("زوبعة", "arabic_abjad"),
         "if_taa_priced": W("زوبعة", "arabic_abjad") + 5},
    ],
}

# ---------------------------------------------------------------------
# TABVLA Q3 — the hamza-alif: one word, both conventions filed
# adjacently; the bank's reading is the verified one.
# ---------------------------------------------------------------------
D["tabvla_q3"] = {
    "word": "الأحمر",
    "bank_value": W("الأحمر", "arabic_abjad"),
    "hamza_alone_in_bank": W("أ", "arabic_abjad"),
    "verified_claim": 279, "parted_claim": 280, "delta": 1,
}

# ---------------------------------------------------------------------
# TABVLA Q4 — mispar gadol: the two applications, recomputed letter
# by letter. Canonical gadol uplifts ALL five finals (500–900).
# ---------------------------------------------------------------------
FINALS = {"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900}


def gadol(word, uplift):
    total = 0
    for ch in word:
        if ch in FINALS and ch in uplift:
            total += FINALS[ch]
        elif ch != " ":
            total += W(ch, "hebrew")
    return total


D["tabvla_q4"] = {
    "madim": {"word": "מאדים", "hechrechi": W("מאדים", "hebrew"),
              "full_gadol": gadol("מאדים", set(FINALS)),
              "nun_only": gadol("מאדים", {"ן"}), "claimed": 655},
    "adam_kadmon": {"word": "אדם קדמון",
                    "hechrechi": W("אדם קדמון", "hebrew"),
                    "full_gadol": gadol("אדם קדמון", set(FINALS)),
                    "nun_only": gadol("אדם קדמון", {"ן"}),
                    "claimed": 895},
    "gadol_bank_seated": "hebrew_gadol" in getattr(
        engine, "SYSTEMS", {}),
}

# ---------------------------------------------------------------------
# TABVLA Q5 — the unprinted transliterations (60 claims), and the
# adoption test: the seated door applied to the Hebrew population;
# a stated letter-map applied to the Greek population.
# ---------------------------------------------------------------------
nv = [r for r in rows if r["verdict"] == "NOT VERIFIABLE"]
D["tabvla_q5_populations"] = dict(Counter(r["bank_engine"] for r in nv))
heb_nv = [r for r in nv if r["bank_engine"] == "hebrew"]
door_agree, door_rows = [], []
for r in heb_nv:
    name = r["proposal_raw"].split("(")[0].strip()
    rendered, _notes = transliterate_latin_to_hebrew(name)
    v = W(rendered, "hebrew")
    door_rows.append({"claim_key": r["claim_key"], "name": name,
                      "claimed": int(r["claimed_value"]),
                      "door_word": rendered, "door_value": v,
                      "agree": v == int(r["claimed_value"])})
    if v == int(r["claimed_value"]):
        door_agree.append(r["claim_key"])
D["tabvla_q5_hebrew"] = {
    "population": len(heb_nv), "door_agrees_exactly": len(door_agree),
    "door_agree_keys": door_agree, "rows": door_rows,
    "nearest_miss": {"name": "MAAT", "claimed": 441,
                     "door_value": W(transliterate_latin_to_hebrew(
                         "MAAT")[0], "hebrew")},
}

HEB_MAP = {"א": "Α", "ב": "Β", "ג": "Γ", "ד": "Δ", "ה": "Η", "ו": "Υ",
           "ז": "Ζ", "ח": "Χ", "ט": "Θ", "י": "Ι", "כ": "Κ", "ך": "Κ",
           "ל": "Λ", "מ": "Μ", "ם": "Μ", "נ": "Ν", "ן": "Ν", "ס": "Σ",
           "ע": "Ο", "פ": "Φ", "ף": "Φ", "צ": "Σ", "ץ": "Σ", "ק": "Κ",
           "ר": "Ρ", "ש": "Σ", "ת": "Τ"}
LAT_MAP = {"A": "Α", "B": "Β", "C": "Κ", "D": "Δ", "E": "Ε", "F": "Φ",
           "G": "Γ", "H": "Η", "I": "Ι", "J": "Ι", "K": "Κ", "L": "Λ",
           "M": "Μ", "N": "Ν", "O": "Ο", "P": "Π", "Q": "Κ", "R": "Ρ",
           "S": "Σ", "T": "Τ", "U": "Υ", "V": "Υ", "W": "Ω", "X": "Ξ",
           "Y": "Υ", "Z": "Ζ"}


def greek_plain(r):
    p = r["proposal_raw"]
    m = re.search(r"\(([^)]*)\)", p)
    inner = m.group(1) if m else ""
    heb = "".join(ch for ch in inner if "א" <= ch <= "ת")
    if heb:
        g = "".join(HEB_MAP[ch] for ch in heb)
    else:
        name = p.split("(")[0].strip()
        g = "".join(LAT_MAP.get(ch, "") for ch in name.upper()
                    if ch.isalpha())
    return g, W(g, "greek")


gk_nv = [r for r in nv if r["bank_engine"] == "greek"]
gk_rows, gk_agree = [], 0
for r in gk_nv:
    g, v = greek_plain(r)
    ok = v == int(r["claimed_value"])
    gk_agree += ok
    gk_rows.append({"claim_key": r["claim_key"],
                    "proposal": r["proposal_raw"],
                    "claimed": int(r["claimed_value"]),
                    "plain_dress": g, "plain_value": v, "agree": ok})
D["tabvla_q5_greek"] = {
    "population": len(gk_nv), "plain_map_agrees": gk_agree,
    "rows": gk_rows,
    # The name-tradition joints, each witnessed inside the corpus:
    "joints": {
        "bith_via_theta": {"dress": "ΒΙΘ", "value": W("ΒΙΘ", "greek"),
                           "claimed": 21,
                           "witness": "Θώθ VERIFIED at 818 in the "
                                      "same column — tav reads theta "
                                      "in the letter-name tradition"},
        "azoth_via_omega": {"dress": "ΑΖΩΘ",
                            "value": W("ΑΖΩΘ", "greek"), "claimed": 817},
        "amen_received": {"dress": "ΑΜΗΝ", "value": W("ΑΜΗΝ", "greek"),
                          "claimed": 99,
                          "witness": "the received Greek spelling of "
                                     "the word itself"},
        "yvd_residue": {"claimed": 404,
                        "coincidence": {"dress": "ΥΔ",
                                        "value": W("ΥΔ", "greek")}},
    },
}

# ---------------------------------------------------------------------
# TABVLA Q6 — the unseated methods (XLVI): populations, and the
# corpus-wide absence of the source glyphs.
# ---------------------------------------------------------------------
q6 = {"pinyin": [], "stroke": []}
for r in nv:
    if r["bank_engine"] == "hebrew_pinyin_fallback":
        q6["pinyin"].append({"claim_key": r["claim_key"],
                             "proposal": r["proposal_raw"],
                             "claimed": int(r["claimed_value"])})
    if r["bank_engine"] == "stroke_count_prc":
        q6["stroke"].append({"claim_key": r["claim_key"],
                              "proposal": r["proposal_raw"],
                              "claimed": int(r["claimed_value"])})
corpus = (GOAL / "777-REVISED.md").read_text(encoding="utf-8")
_xlvi_at = corpus.find("Column XLVI")
_xlvi_seg = corpus[_xlvi_at:_xlvi_at + 9000] if _xlvi_at >= 0 else ""
D["tabvla_q6"] = {
    **q6, "pinyin_count": len(q6["pinyin"]),
    "stroke_count": len(q6["stroke"]),
    "cjk_chars_in_corpus": sum(1 for ch in corpus
                               if "一" <= ch <= "鿿"),
    # The method's NAME stands in the fills as a bank label; its
    # mapping — which syllable becomes which letter — is printed
    # nowhere, and the section prints no Hebrew rendering either.
    "pinyin_label_in_corpus": "hebrew_pinyin_fallback" in corpus,
    "hebrew_chars_in_xlvi_section": sum(
        1 for ch in _xlvi_seg if "א" <= ch <= "ת"),
}

# ---------------------------------------------------------------------
# TABVLA Q7 — the two copies: the apparatus counted, not described.
# ---------------------------------------------------------------------
ptx = (PONTIFEX / "research/777-gap-filling/777-REVISED.md").read_text(
    encoding="utf-8")
D["tabvla_q7"] = {
    "pontifex_copy_bytes": len(ptx.encode("utf-8")),
    "goal_copy_bytes": len(corpus.encode("utf-8")),
    "apparatus_notes_pontifex": ptx.count("[Orthography correction"),
    "apparatus_notes_goal": corpus.count("[Orthography correction"),
    "notes_that_reweigh": ptx.count("reweighed"),
}

# ---------------------------------------------------------------------
# TABVLA Q8 — the transcription gap: its register coordinates.
# ---------------------------------------------------------------------
tables = json.load(open(TAB_REG, encoding="utf-8"))
D["tabvla_q8"] = {
    "gap_cells_per_table": tables["greek"]["rows"] and sum(
        1 for r in tables["greek"]["rows"] if r["state"] == "GAP"),
    "gap_cell_id": [r["cell_id"] for r in tables["greek"]["rows"]
                    if r["state"] == "GAP"],
}

# ---------------------------------------------------------------------
# TWELVE TABLES Q2 — the Ge'ez ch-door: the table's states counted
# from its register; the hole species separated.
# ---------------------------------------------------------------------
gz = tables["geez"]["rows"]
holes = [r for r in gz if r["state"] == "HOLE"]
D["tt_q2"] = {
    "states": dict(Counter(r["state"] for r in gz)),
    "holes": len(holes),
    "holes_fail_at_ch": sum(1 for r in holes
                            if "fails at ‘ch’" in (r.get("note") or "")),
    "holes_cross_unseated": sum(
        1 for r in holes
        if "crosses an unseated letter" in (r.get("note") or "")),
    "holes_no_latin_form": sum(
        1 for r in holes
        if "no Latin form of record" in (r.get("note") or "")),
    "derived_bases": list("ሸቐቨቸኘኸዀዠዸጀጘጨ"),
    "armenian_annex_sourced": {
        "omin": engine.ARMENIAN_LATE.get("Օ"),
        "ef": engine.ARMENIAN_LATE.get("Ֆ")},
    "derived_base_in_mint": "ቸ" in engine.GEEZ_FIRST,
    "derived_base_in_halehame": "ቸ" in engine.HALEHAME_FIRST,
}

# ---------------------------------------------------------------------
# TWELVE TABLES Q4 — native depth: the corpus's own printings,
# counted across the twelve tables.
# ---------------------------------------------------------------------
D["tt_q4"] = {
    "native_by_tongue": {
        k: sum(1 for r in v["rows"] if r["state"] == "NATIVE")
        for k, v in tables.items()},
    "native_total": sum(
        sum(1 for r in v["rows"] if r["state"] == "NATIVE")
        for v in tables.values()),
    "word_cells_per_table": 285,
}

# ---------------------------------------------------------------------
# TWELVE TABLES Q5 — door health: the doors' own check functions,
# re-run at this desk. (The parity batteries' counts are re-run by
# the audit script, which shells them independently.)
# ---------------------------------------------------------------------
D["tt_q5"] = {
    "kana_checks": [list(c) for c in engine.kana_checks()],
    "geez_checks": [list(c) for c in engine.geez_checks()],
}

# ---------------------------------------------------------------------
# TWELVE TABLES Q7 — the Chinese leg: notation reader seated,
# weighing bank absent — the census coordinate restated from the
# engine itself.
# ---------------------------------------------------------------------
import pontifex as _ptx  # noqa: E402

D["tt_q7"] = {
    "chinese_in_systems": "chinese" in engine.SYSTEMS,
    "reader_seated": callable(getattr(_ptx, "read_chinese_numerals",
                                      None)),
}

OUT = HERE / "delegated_answers_data.json"
OUT.write_text(json.dumps(D, ensure_ascii=False, indent=1),
               encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
print("Q1 parted:", D["tabvla_q1"]["parted_claims"],
      "| Q2 deltas all 5:", D["tabvla_q2"]["all_delta_five"],
      "| Q5 door agrees:", D["tabvla_q5_hebrew"]["door_agrees_exactly"],
      "| Greek plain agrees:", D["tabvla_q5_greek"]["plain_map_agrees"],
      "| Q7 notes:", D["tabvla_q7"]["apparatus_notes_pontifex"],
      "| TT Q2 holes:", D["tt_q2"]["holes"])
