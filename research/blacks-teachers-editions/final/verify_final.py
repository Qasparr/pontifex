#!/usr/bin/env python3
# verify_final.py — post-build verification for the Final Teacher's Edition.
# Streams the PDF page by page (never holds the whole text), checks counts
# against the three workers' data files, locates key pages for rendering.
import json
import re
import sys
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
PDF = HERE / "blacks-2e-final-teachers-edition.pdf"
BASE = Path.home() / "workspace/your_files/blacks-teachers-editions"

MARK_STRONG = "[TEXT INCOMPLETE — scan limitation]"
MARK_CAND = "[TEXT POSSIBLY INCOMPLETE — scan candidate]"

reader = PdfReader(str(PDF))
pages = len(reader.pages)
size = PDF.stat().st_size
print(f"PAGES: {pages}  SIZE: {size} bytes")

counts = {
    "apparatus_carried": 0, "apparatus_not": 0,
    "mark_strong": 0, "mark_cand": 0,
    "struck_label": 0, "not_audited": 0,
    "murder_new": 0, "murder_old": 0,
    "gallows_flag": 0, "register_header": 0,
    "colophon": 0, "flagpole_pages": 0,
    "self_defense_mentions": 0,
}
locate = {"sans_jour_headword": [], "errata": [], "register_start": [],
          "murder": [], "ju8titia": []}

# stratified sample: every 438th entry + first/last
entries = json.loads((BASE / "2e/entries.json").read_text(encoding="utf-8"))


def clean_body(t):
    t = t.replace("\t", " ")
    t = re.sub(r" {2,}", " ", t)
    t = re.sub(r"-\s*\n\s*([a-z])", r"\1", t)
    return t.strip()


sample = {}
for i in list(range(0, len(entries), 438)) + [len(entries) - 1]:
    b = clean_body(entries[i].get("body", "") or "")
    sample[i] = {
        "headword": entries[i]["headword"],
        "probe": re.sub(r"\s+", " ", b)[:40] if b else "",
        "body_found": False,
    }

for pno in range(pages):
    try:
        text = reader.pages[pno].extract_text() or ""
    except Exception:
        text = ""
    flat = re.sub(r"\s+", " ", text)
    counts["apparatus_carried"] += flat.count("5e apparatus — Carried into")
    counts["apparatus_not"] += flat.count("5e apparatus — Not carried into")
    counts["mark_strong"] += flat.count(MARK_STRONG)
    counts["mark_cand"] += flat.count(MARK_CAND)
    counts["struck_label"] += flat.count("STRUCK — per ruling 2026-10-25")
    counts["not_audited"] += flat.count("NOT AUDITED")
    counts["murder_new"] += flat.count(
        "And if he smite him with an instrument of iron")
    counts["murder_old"] += flat.count(
        "But if he smite him with an instrument of iron")
    counts["gallows_flag"] += flat.count("Deuteronomy 25:22-23")
    counts["register_header"] += flat.count(
        "APPENDIX — HEADWORDS NEW IN THE FIFTH EDITION")
    counts["colophon"] += flat.count("COLOPHON")
    counts["self_defense_mentions"] += flat.count("SELF-DEFENSE")
    if "SANS JOUR" in flat and len(locate["sans_jour_headword"]) < 4:
        locate["sans_jour_headword"].append(pno + 1)
    if "Errata, Flags, and Marked Dispositions" in flat.replace(
            "ERRATA, FLAGS, AND MARKED DISPOSITIONS", "Errata, Flags, and "
            "Marked Dispositions") or "ERRATA, FLAGS" in flat:
        locate["errata"].append(pno + 1)
    if "APPENDIX — HEADWORDS NEW IN THE FIFTH EDITION" in flat:
        locate["register_start"].append(pno + 1)
    if "MURDER" in flat and len(locate["murder"]) < 4:
        locate["murder"].append(pno + 1)
    if "JU8TITIA" in flat and len(locate["ju8titia"]) < 4:
        locate["ju8titia"].append(pno + 1)
    for i, s in sample.items():
        if not s["body_found"] and s["probe"] and s["probe"] in flat:
            s["body_found"] = True

print("COUNTS:", json.dumps(counts, indent=1))
print("LOCATE:", json.dumps(locate))
missed = {i: s for i, s in sample.items() if s["probe"] and not s["body_found"]}
print(f"SAMPLE: {len(sample)} entries probed, "
      f"{len(sample) - len(missed)} bodies found, {len(missed)} missed")
for i, s in missed.items():
    print(f"  MISSED idx {i} {s['headword']!r} probe={s['probe']!r}")
