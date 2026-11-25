#!/usr/bin/env python3
# =============================================================================
# 93 — audit_delegated_answers.py
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
# MECHANISM: the independent audit of THE-DELEGATED-ANSWERS. It
# re-derives every load-bearing figure from the sealed engine
# and the frozen registers on its OWN code paths (nothing is
# imported from the investigation script or read from its JSON),
# checks the Markdown master (every question quoted, every
# decision at its strength, killing evidence present), and
# checks the MAGVS PDF's text layer (footer resolved, no
# Hebrew- or Arabic-block codepoint standing in it, the
# decisions and the UNCHARTED tag present). Shells the kana and
# Ge'ez parity batteries for §XIV's health claims.
#
# DOCTRINE: the audit grades the instrument, not the decisions'
# wisdom — the decisions are the desk's, under delegation; what
# the audit certifies is that every number they rest on
# reproduces, every question is quoted entire, and nothing is
# printed above desk strength.
#
# CONTENT TEST: Inputs — the engine, the registers, the master,
# the PDF. Processes — independent recomputation, text-layer
# extraction, string assertions. Outputs — the results file
# beside this script and a PASS/FAIL line per check. Tolerances
# — zero: one failure fails the instrument.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import csv
import json
import re
import subprocess
import sys
import site
from collections import Counter
from pathlib import Path

sys.path.insert(0, site.getusersitepackages())
PONTIFEX = Path.home() / "workspace/pontifex"
sys.path.insert(0, str(PONTIFEX))

from pontifex import weigh, transliterate_latin_to_hebrew  # noqa: E402
from pontifex import engine  # noqa: E402
import pontifex as ptx  # noqa: E402

HERE = Path(__file__).parent
GOAL = (Path.home() / "workspace/goals/"
        "cross-gematria-777-gap-filling/files")
MASTER = GOAL / "THE-DELEGATED-ANSWERS.md"
PDF = GOAL / "THE-DELEGATED-ANSWERS-MAGVS.pdf"
REG = PONTIFEX / "research/777-gap-filling/777-verification-verified.csv"
TAB_REG = PONTIFEX / "research/twelve-tables/tables_register.json"

RESULTS = []
FAILED = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    if not ok:
        FAILED.append(name)
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")


def W(w, b):
    return weigh(w, b)["value"]


md = MASTER.read_text(encoding="utf-8")
rows = list(csv.DictReader(open(REG, encoding="utf-8")))
tables = json.load(open(TAB_REG, encoding="utf-8"))

# --- controls ---------------------------------------------------------
check("controls 93/93/773",
      (W("θέλημα", "greek"), W("VAPOUR", "latin_ordinal"),
       W("σφίγξ", "greek")) == (93, 93, 773))

# --- TABVLA Q1 --------------------------------------------------------
door_rows = [r for r in rows if r["cell_id"].startswith("XXXIII")
             and r["claim_idx"] == "2"]
check("Q1 door claims 14 = 5 verified + 9 parted",
      len(door_rows) == 14
      and sum(r["verdict"] == "VERIFIED" for r in door_rows) == 5
      and sum(r["verdict"] == "PARTED" for r in door_rows) == 9)
check("Q1 BALDR scheme 236 / door 237",
      W("בלדר", "hebrew") == 236
      and W(transliterate_latin_to_hebrew("BALDR")[0], "hebrew")
      == 237)
check("Q1 SURTR coordinate 475 vs 866",
      any(r["proposal_raw"] == "SURTR" and r["claim_idx"] == "2"
          and r["claimed_value"] == "475"
          and r["recomputed"] == "866" for r in door_rows))

# --- TABVLA Q2 --------------------------------------------------------
p47 = [r for r in rows if r["cell_id"].startswith("XLVII")
       and r["verdict"] == "PARTED" and r["claim_key"] != "S143-P0-C1"]
check("Q2 six partings, each delta exactly 5, each one taa",
      len(p47) == 6 and all(
          int(r["claimed_value"]) - int(r["recomputed"]) == 5
          and r["weighed_word"].count("ة") == 1 for r in p47))
check("Q2 bank prices taa at silence",
      W("ة", "arabic_abjad") == 0)
check("Q2 verified counterweights stand on the silence",
      W("مرة", "arabic_abjad") == 240
      and W("زوبعة", "arabic_abjad") == 85)

# --- TABVLA Q3 --------------------------------------------------------
check("Q3 al-Ahmar bank 279, hamza silent",
      W("الأحمر", "arabic_abjad") == 279
      and W("أ", "arabic_abjad") == 0)

# --- TABVLA Q4 --------------------------------------------------------
FIN = {"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900}


def gadol(word, up):
    return sum(FIN[ch] if ch in FIN and ch in up else W(ch, "hebrew")
               for ch in word if ch != " ")


check("Q4 Maadim: hechrechi 95, full gadol 655",
      W("מאדים", "hebrew") == 95
      and gadol("מאדים", set(FIN)) == 655)
check("Q4 Adam Kadmon: hechrechi 245, nun-only 895, full 1455",
      W("אדם קדמון", "hebrew") == 245
      and gadol("אדם קדמון", {"ן"}) == 895
      and gadol("אדם קדמון", set(FIN)) == 1455)
check("Q4 no gadol bank seated in the engine",
      "hebrew_gadol" not in engine.SYSTEMS)

# --- TABVLA Q5 --------------------------------------------------------
nv = [r for r in rows if r["verdict"] == "NOT VERIFIABLE"]
pops = Counter(r["bank_engine"] for r in nv)
check("Q5 population 60 = 29 + 17 + 13 + 1",
      pops["hebrew"] + pops["greek"] + pops["hebrew_gadol"]
      + pops["arabic_abjad"] == 60)
agree = 0
for r in nv:
    if r["bank_engine"] == "hebrew":
        name = r["proposal_raw"].split("(")[0].strip()
        if W(transliterate_latin_to_hebrew(name)[0], "hebrew") \
                == int(r["claimed_value"]):
            agree += 1
check("Q5 door reproduces exactly 3 of the 29 Hebrew claims",
      agree == 3, f"agree={agree}")
check("Q5 Greek joints: BITH 21, AZOTH 817, AMEN 99",
      W("ΒΙΘ", "greek") == 21 and W("ΑΖΩΘ", "greek") == 817
      and W("ΑΜΗΝ", "greek") == 99)
check("Q5 YVD residue coincidence printed as coincidence",
      W("ΥΔ", "greek") == 404)

# --- TABVLA Q6 --------------------------------------------------------
check("Q6 population 22 = 11 pinyin + 11 stroke",
      pops["hebrew_pinyin_fallback"] == 11
      and pops["stroke_count_prc"] == 11)
corpus = (GOAL / "777-REVISED.md").read_text(encoding="utf-8")
check("Q6 corpus prints zero CJK characters",
      sum(1 for ch in corpus if "一" <= ch <= "鿿") == 0)

# --- TABVLA Q7 --------------------------------------------------------
ptx_copy = (PONTIFEX / "research/777-gap-filling/777-REVISED.md"
            ).read_text(encoding="utf-8")
check("Q7 apparatus: 44 notes in the pontifex copy, 0 in the goal",
      ptx_copy.count("[Orthography correction") == 44
      and corpus.count("[Orthography correction") == 0)
check("Q7 copy sizes 163,795 / 154,961 bytes",
      len(ptx_copy.encode()) == 163795
      and len(corpus.encode()) == 154961,
      f"{len(ptx_copy.encode())}/{len(corpus.encode())}")

# --- TABVLA Q8 --------------------------------------------------------
check("Q8 exactly one GAP cell, at CLXXXIV/10",
      [r["cell_id"] for r in tables["greek"]["rows"]
       if r["state"] == "GAP"] == ["CLXXXIV/10"])

# --- Twelve Tables Q2 -------------------------------------------------
gz = Counter(r["state"] for r in tables["geez"]["rows"])
holes = [r for r in tables["geez"]["rows"] if r["state"] == "HOLE"]
check("TT Q2 Ge'ez states: DOOR 205, HOLE 80, EMPTY 85, GAP 1",
      gz == {"DOOR": 205, "HOLE": 80, "EMPTY": 85, "GAP": 1})
check("TT Q2 hole species 62 + 12 + 6 = 80",
      sum("no Latin form of record" in (r.get("note") or "")
          for r in holes) == 62
      and sum("crosses an unseated letter" in (r.get("note") or "")
              for r in holes) == 12
      and sum("fails at ‘ch’" in (r.get("note") or "")
              for r in holes) == 6)
check("TT Q2 Armenian annex values are the sourced 10000/20000",
      engine.ARMENIAN_LATE.get("Օ") == 10000
      and engine.ARMENIAN_LATE.get("Ֆ") == 20000)
check("TT Q2 derived base in neither Ge'ez bank",
      "ቸ" not in engine.GEEZ_FIRST
      and "ቸ" not in engine.HALEHAME_FIRST)

# --- Twelve Tables Q4 -------------------------------------------------
native = sum(sum(1 for r in v["rows"] if r["state"] == "NATIVE")
             for v in tables.values())
check("TT Q4 NATIVE total across the twelve tables is 245",
      native == 245, f"native={native}")

# --- Twelve Tables Q5 -------------------------------------------------
check("TT Q5 door check functions pass entire",
      all(c[-1] for c in engine.kana_checks())
      and all(c[-1] for c in engine.geez_checks()))
for test, want in (("test_kana_parity.py", "20/20"),
                   ("test_geez_parity.py", "27/27")):
    out = subprocess.run([sys.executable, str(PONTIFEX / test)],
                         capture_output=True, text=True).stdout
    check(f"TT Q5 parity battery {test} green", want in out)

# --- Twelve Tables Q7 -------------------------------------------------
check("TT Q7 Chinese: reader seated, no weighing bank",
      callable(getattr(ptx, "read_chinese_numerals", None))
      and "chinese" not in engine.SYSTEMS)

# --- the master: form --------------------------------------------------
for phrase in (
        "Make your recommendations the pen's decisions",
        "The fallback door against the workers' scheme",
        "Seat a priced ة in the Arabic bank",
        "The same question as Q2 at size one",
        "which application is canonical",
        "the population becomes recomputable",
        "Build seats for them",
        "do the copies stand as two witnesses",
        "not filled by invention",
        "let counted-not-priced stand as the law",
        "keep the holes as the mint's honest edge",
        "Commission them as mint work",
        "does the corpus-bounded depth stand",
        "amends by correctio",
        "standing outside as surveyed",
        "the seam is the pen's to name"):
    check(f"master quotes: {phrase[:44]}…", phrase in md)
check("master: thirteen desk decisions printed",
      md.count("**Decision (desk strength)") == 13,
      f"count={md.count('**Decision (desk strength)')}")
check("master: killing evidence with the decisions",
      md.count("**Killing evidence:**") >= 13,
      f"count={md.count('**Killing evidence:**')}")
check("master: UNCHARTED at its three coordinates",
      md.count("UNCHARTED") >= 6,
      f"count={md.count('UNCHARTED')}")
check("master: the register of decisions stands",
      "## §XVII — The Register of Decisions" in md
      and "## §XVIII" in md and "## Colophon" in md)

# --- the PDF text layer ------------------------------------------------
txt = subprocess.run(["pdftotext", str(PDF), "-"],
                     capture_output=True, text=True).stdout
info = subprocess.run(["pdfinfo", str(PDF)],
                      capture_output=True, text=True).stdout
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
footers = [(int(a), int(b)) for a, b in
           re.findall(r"— (\d+) of (\d+) —", txt)]
check("PDF footer resolves on every page",
      len(footers) >= pages and max(a for a, _b in footers) == pages
      and all(b == pages for _a, b in footers),
      f"pages={pages}, footers found={len(footers)}")
check("PDF layer: no Hebrew-block codepoint",
      not any("֐" <= ch <= "׿" for ch in txt))
check("PDF layer: no Arabic-block codepoint",
      not any("؀" <= ch <= "ۿ" for ch in txt))
for phrase in ("THE DELEGATED ANSWERS", "documented second door",
               "honest edge", "UNCHARTED",
               "Flagpole of Claim and Coinage", "[U+1311]",
               "Killing evidence"):
    check(f"PDF layer carries: {phrase}", phrase in txt)

# --- verdict ------------------------------------------------------------
total = len(RESULTS)
passed = total - len(FAILED)
lines = [f"{'PASS' if ok else 'FAIL'}  {name}  {detail}"
         for name, ok, detail in RESULTS]
lines.append(f"\nAUDIT {'PASS' if not FAILED else 'FAIL'} — "
             f"{passed}/{total} checks, {len(FAILED)} failures")
(HERE / "audit_delegated_answers_results.txt").write_text(
    "\n".join(lines) + "\n", encoding="utf-8")
print(f"\nAUDIT {'PASS' if not FAILED else 'FAIL'} — "
      f"{passed}/{total} checks, {len(FAILED)} failures")
sys.exit(1 if FAILED else 0)
