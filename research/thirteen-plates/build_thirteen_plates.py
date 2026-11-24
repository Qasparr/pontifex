#!/usr/bin/env python3
# =============================================================================
# 93 — build_thirteen_plates.py
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
# MECHANISM: maps the Founder's uploaded TABVLA (a browser-print
# form of THE 777 VERIFICATION TABVLA, 123 pp, A4) into the twelve
# tongues, forming thirteen plates. The mapping atoms are the 504
# bank claims of the frozen verified register
# (research/777-gap-filling/777-verification-verified.json), which
# Phase 0 of this build proved to be the upload's own matter: all
# 221 of the upload's §III section headings stand verbatim in its
# text layer, and its stated totals (504 claims — VERIFIED 404,
# PARTED 18, NOT VERIFIABLE 82) coincide with the register at
# every point. Each claim is assigned to exactly one plate by its
# stated bank; the two unseated methods (pinyin fallback, PRC
# stroke count) belong to no tongue and map to the Core (Plate
# XIII). Sections are frames: the 135 claim-bearing sections are
# indexed once in the Core with pointers to the plates their
# claims sit on; the 86 claimless frames (85 certified empty, 1
# transcription gap) sit in the Core alone.
#
# DOCTRINE: the upload is a source document — read-only, never
# edited (its SHA-256 is taken before and after the build and
# asserted unchanged). The upload and the house's struck MAGVS
# part in production only (pagination, paper, fonts, footer);
# both readings stand printed in the instrument — no reconciliation
# is forced. Reasoning rides with every assignment: the plate map
# below states, bank by bank, why it lands where it lands.
#
# CONTENT TEST: Inputs — the upload PDF, the frozen verified
# register, the sealed engine's bank tables (for plate vitals).
# Processes — identity extraction, section page-mapping, claim
# assignment, register emission. Outputs —
# mapping_register.json/.csv and source_identity.json beside this
# script. Tolerances — zero: one unmapped or twice-mapped claim,
# one missing section heading, or a changed upload hash fails
# the build.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PONTIFEX = HERE.parents[1]
sys.path.insert(0, str(PONTIFEX))

UPLOAD = Path.home() / "workspace/user/files/THE-777-VERIFICATION-TABVLA_2_bczz.pdf"
HOUSE_PDF = (Path.home() / "workspace/goals/cross-gematria-777-gap-filling"
             / "files/THE-777-VERIFICATION-TABVLA-MAGVS.pdf")
FROZEN = (PONTIFEX / "research/777-gap-filling"
          / "777-verification-verified.json")

# ---------------------------------------------------------------------------
# THE PLATE MAP — bank by bank, with its reasoning.
# Latin's two banks are one tongue (the census fold), and the
# english_ordinal claims ride the Latin plate because the source
# itself verifies them through the engine's latin_ordinal bank —
# "the same 26-seat table" (§I of the source). The Hebrew plate
# carries the seated bank, the mispar-gadol variant label, and
# the Hebrew fallback door — three subseats of one tongue. The
# pinyin fallback and the PRC stroke count state methods no bank
# seats and no tongue owns: they map to the Core as apparatus.
# ---------------------------------------------------------------------------
PLATE_OF_BANK = {
    "greek": "Greek",
    "hebrew": "Hebrew",
    "hebrew_gadol": "Hebrew",
    "hebrew_fallback": "Hebrew",
    "arabic_abjad": "Arabic",
    "latin_ordinal": "Latin",
    "agrippa": "Latin",
    "english_ordinal": "Latin",
    "coptic": "Coptic",
    "hebrew_pinyin_fallback": "Core",
    "stroke_count_prc": "Core",
}

SUBSEAT = {
    "greek": "the seated Greek bank",
    "hebrew": "the seated Hebrew bank (mispar hechrechi)",
    "hebrew_gadol": "the mispar-gadol variant label (no bank seated)",
    "hebrew_fallback": "the Hebrew fallback door",
    "arabic_abjad": "the seated Arabic abjad bank",
    "latin_ordinal": "Latin ordinal bank",
    "agrippa": "Agrippa bank",
    "english_ordinal": "English ordinal dress (verified through latin_ordinal)",
    "coptic": "the seated Coptic bank",
    "hebrew_pinyin_fallback": "unseated method — pinyin-to-Hebrew fallback",
    "stroke_count_prc": "unseated method — PRC stroke count",
}

# The twelve plates in the Twelve Tables' order, then the Core.
PLATES = [
    ("I", "Greek"), ("II", "Hebrew"), ("III", "Arabic"),
    ("IV", "Latin"), ("V", "Japanese"), ("VI", "Ge'ez"),
    ("VII", "Armenian"), ("VIII", "Coptic"), ("IX", "Georgian"),
    ("X", "Cyrillic"), ("XI", "Glagolitic"), ("XII", "Korean"),
    ("XIII", "Core"),
]
PLATE_ROMAN = {name: roman for roman, name in PLATES}

# Plate heads: script display, engine systems, tier of record.
PLATE_HEADS = {
    "Greek": dict(script="Ἑλληνική — the Greek script",
                  systems=["greek"], tier="ATTESTED"),
    "Hebrew": dict(script="עברית — the Hebrew script, with the Aramaic "
                           "dresses (𐡏 Imperial, ܥ Syriac) folded in by "
                           "inheritance",
                   systems=["hebrew", "aramaic"],
                   tier="ATTESTED (the bank); the gadol label and the "
                        "fallback door ride as variant and door"),
    "Arabic": dict(script="العربية — the Arabic script",
                   systems=["arabic_abjad"], tier="ATTESTED"),
    "Latin": dict(script="Latina — the Latin script",
                  systems=["latin_ordinal", "agrippa"],
                  tier="ATTESTED (both banks; one tongue)"),
    "Japanese": dict(script="日本語 — hiragana and katakana",
                     systems=["kana"],
                     tier="CONSTRUCTED — the gojūon mint, stamped by "
                          "the Founder 2026-11-13"),
    "Ge'ez": dict(script="ግእዝ — the Ethiopic syllabary",
                  systems=["geez", "halehame"],
                  tier="CONSTRUCTED — the Ge'ez mint; the halehame "
                       "table stands beside it as folk WITNESS"),
    "Armenian": dict(script="Հայերեն — the Armenian script",
                     systems=["armenian"],
                     tier="ATTESTED (the classical 36; the late annex "
                          "a tier below, at the door's late path)"),
    "Coptic": dict(script="ⲁⲃⲅ — the Coptic script",
                   systems=["coptic"], tier="DERIVED"),
    "Georgian": dict(script="ქართული — the Georgian script",
                     systems=["georgian"], tier="ATTESTED"),
    "Cyrillic": dict(script="Кириллица — the Cyrillic script and its "
                             "archaic numeral seats",
                     systems=["cyrillic"], tier="DERIVED"),
    "Glagolitic": dict(script="ⰳⰾⰰⰳⱁⰾⰻⱌⰰ — the Glagolitic script",
                       systems=["glagolitic"],
                       tier="ATTESTED (the thousands range under its "
                            "own sources' doubt)"),
    "Korean": dict(script="한국어 — the Hangul jamo",
                   systems=["hangul"],
                   tier="CONSTRUCTED — the hangul mint"),
    "Core": dict(script="οὐδέν — the center",
                 systems=[], tier="the map's frame and apparatus"),
}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pdf_text(path):
    """Raw and layout text of a PDF, via pdftotext (the house tool)."""
    out = {}
    for mode, args in (("raw", []), ("layout", ["-layout"])):
        r = subprocess.run(["pdftotext", *args, str(path), "-"],
                           capture_output=True, text=True, check=True)
        out[mode] = r.stdout
    return out


def bank_vitals():
    """Seats / distinct values / maximum for each plate's systems,
    read from the sealed engine — never typed by hand."""
    from pontifex import engine
    vitals = {}
    for name, head in PLATE_HEADS.items():
        rows = []
        for system in head["systems"]:
            bank = engine.SYSTEMS[system]
            table = bank.get("table")
            if table is None:
                rows.append(dict(system=system, seats=None,
                                 distinct=None, maximum=None))
                continue
            rows.append(dict(system=system, seats=len(table),
                             distinct=len(set(table.values())),
                             maximum=max(table.values())))
        vitals[name] = rows
    return vitals


def main():
    upload_hash_before = sha256(UPLOAD)
    reg = json.loads(FROZEN.read_text(encoding="utf-8"))
    up = pdf_text(UPLOAD)
    raw_pages = up["raw"].split("\f")
    norm_pages = [re.sub(r"\s+", " ", p) for p in raw_pages]

    # --- Phase 0: identity -------------------------------------------
    # Every §III heading of the frozen register stands verbatim in
    # the upload's text; its page is the claim's source coordinate.
    section_page = {}
    for idx, s in enumerate(reg, 1):
        marker = f"§III.{idx} — {s['cell_id']}"
        for pno, page in enumerate(norm_pages, 1):
            if marker in page:
                section_page[idx] = pno
                break
    assert len(section_page) == 221, \
        f"section headings found: {len(section_page)} of 221"

    def marker_page(marker):
        for pno, page in enumerate(norm_pages, 1):
            if marker in page:
                return pno
        return None

    iv_page = marker_page("§IV — The Partings Register")
    v_page = marker_page("§V — The Not-Verifiable Register")
    vi_page = marker_page("§VI — The Falsification Appendix")

    totals_line = re.search(
        r"Claims:\s*504\s*—\s*VERIFIED\s*404\s*·\s*PARTED\s*18\s*·\s*"
        r"NOT VERIFIABLE\s*82", re.sub(r"\s+", " ", up["raw"]))
    identity = dict(
        upload_pages=len([p for p in raw_pages if p.strip()]),
        upload_sha256=upload_hash_before,
        upload_bytes=UPLOAD.stat().st_size,
        house_pages=85,
        house_sha256=sha256(HOUSE_PDF),
        house_bytes=HOUSE_PDF.stat().st_size,
        stated_totals_found=bool(totals_line),
        section_headings_found=len(section_page),
        partings_register_page=iv_page,
        notverifiable_register_page=v_page,
        falsification_page=vi_page,
    )

    # --- Phase 1: the mapping ----------------------------------------
    claims = []
    frames = []
    for s in reg:
        n = s["section_idx"] + 1
        start = section_page[n]
        end = section_page[n + 1] if n < 221 else iv_page
        span = f"p. {start}" if start == end else f"pp. {start}–{end}"
        coord = f"Upload §III.{n} ({s['cell_id']}), PDF {span}"
        keys = []
        for p in s["proposals"]:
            for c in p["claims"]:
                plate = PLATE_OF_BANK[c["bank_engine"]]
                cc = coord
                if c["verdict"] == "PARTED":
                    cc += f"; gathered at §IV, pp. {iv_page}–{v_page - 1}"
                elif c["verdict"] == "NOT VERIFIABLE":
                    cc += f"; gathered at §V, pp. {v_page}–{vi_page - 1}"
                claims.append(dict(
                    claim_key=c["claim_key"], plate=plate,
                    plate_roman=PLATE_ROMAN[plate],
                    bank_engine=c["bank_engine"],
                    subseat=SUBSEAT[c["bank_engine"]],
                    section_number=n, cell_id=s["cell_id"],
                    column=s["column"], section_kind=s["kind"],
                    proposal_raw=p["proposal_raw"],
                    weighed_word=c.get("weighed_word", ""),
                    word_source=c.get("word_source", ""),
                    claimed=c["claimed_value"],
                    recomputed=c.get("recomputed", ""),
                    verdict=c["verdict"],
                    tier_printed=c.get("tier_printed", ""),
                    coordinate=c.get("coordinate", ""),
                    bridge=p.get("bridge", ""),
                    source_coordinate=cc))
                keys.append(c["claim_key"])
        frames.append(dict(
            section_number=n, cell_id=s["cell_id"], column=s["column"],
            kind=s["kind"], section_verdict=s["section_verdict"],
            claim_keys=keys,
            plates=sorted({PLATE_OF_BANK[c["bank_engine"]]
                           for p in s["proposals"] for c in p["claims"]},
                          key=lambda x: PLATE_ROMAN[x]),
            source_coordinate=coord))

    # Completeness is asserted, not assumed: 504 atoms, each once.
    keys = [c["claim_key"] for c in claims]
    assert len(keys) == 504 and len(set(keys)) == 504, len(keys)
    assert len(frames) == 221

    plate_counts = {}
    for roman, name in PLATES:
        rows = [c for c in claims if c["plate"] == name]
        plate_counts[name] = dict(
            claims=len(rows),
            verdicts=dict(Counter(c["verdict"] for c in rows)),
            sections=len({c["section_number"] for c in rows}))

    register = dict(
        identity=identity,
        plate_order=[name for _r, name in PLATES],
        plate_roman=PLATE_ROMAN,
        plate_heads=PLATE_HEADS,
        bank_vitals=bank_vitals(),
        plate_counts=plate_counts,
        claims=claims,
        frames=frames)

    (HERE / "mapping_register.json").write_text(
        json.dumps(register, ensure_ascii=False, indent=1),
        encoding="utf-8")
    with open(HERE / "mapping_register.csv", "w", newline="",
              encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(claims[0].keys()))
        w.writeheader()
        w.writerows(claims)
    (HERE / "source_identity.json").write_text(
        json.dumps(identity, ensure_ascii=False, indent=1),
        encoding="utf-8")

    assert sha256(UPLOAD) == upload_hash_before, "upload changed!"
    print(f"claims mapped: {len(claims)}; frames: {len(frames)}")
    for _r, name in PLATES:
        print(f"  Plate {_r} {name}: {plate_counts[name]}")
    print(f"identity: {identity}")


if __name__ == "__main__":
    main()
