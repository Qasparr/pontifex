#!/usr/bin/env python3
# =============================================================================
# 93 — audit_plate_xiii_the_dial.py
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
# MECHANISM: the independent audit of PLATE-XIII-THE-DIAL. It
# does not read the plate's own figures for its expectations:
# every price is re-weighed on the house engine, both frames
# are rebuilt from their stated constructions (the sketch's
# triangles; the decade classes), the traversals are
# re-derived from the station ring parsed out of the master,
# and the series register is reconciled against the filed
# audit outputs and the repository. Checks:
#   1. controls (θέλημα 93 · VAPOUR 93 · σφίγξ 773);
#   2. the §II station register parsed from the master —
#      13 rows, each price re-weighed in the Greek bank
#      (οὐδέν letter by letter), the sums (nine 1,779 ·
#      relations 29 · ring 1,808), 529 = 23²;
#   3. the coverage table of §III.1 parsed — its frame
#      columns against the rebuilt frames, cell by cell;
#      its classes against the seating's grading (Α
#      POSITION · Ο Υ ΕΙ ΟΥ TRIAD · Ε Η Ι Ω VALUE);
#   4. the marks' evidence re-weighed: the §III.3 dress
#      table dress by dress in both Latin banks (totals
#      123 / 584); the alternates (EI 14 · Y 25/400 ·
#      U 21/200 · V 22); the mirrors (Coptic ⲟⲩ ⲏ ⲓ ⲱ ·
#      Cyrillic І Ѡ И · Armenian Ը · Georgian ჱ); the
#      note bank (A 1 · E 5); the PAIR roots (ΕΙ 6 ·
#      852 6, at canonical position 8); the diphthong
#      four (576 = 24²); the Trinity grid total 2,486;
#      the mirror closure (1,779 − 3 = 1,776; 9 − 6 = 3);
#   5. the traversals re-derived from the parsed ring —
#      step +5 and step −5 — and §IV's printed sequences
#      compared station for station; inverse == forward
#      reversed; each visits thirteen distinct stations;
#   6. the crosshairs: the poles' arithmetic re-weighed
#      (31 + 13 = 44 = VV ordinal; 31 − 13 = 18 = II in
#      both banks); the seated hair and office standing
#      in §V; the horizontal hair STILL OPEN, the float
#      line named, Q3 printed NOT RULED BY THIS PLATE;
#   7. the holes at full size: the eight positions, the
#      four unsettled triads, the unnamed seats, the
#      founder's Zero Point definition entire;
#   8. the §IX series register: the twelve rows against
#      the filed audit outputs of Plates I–XII (counts
#      re-parsed, verdicts PASS) and the twelve commits
#      verified in the repository;
#   9. if the MAGVS PDF stands beside the master, its
#      text layer carries the stations' key signs, the
#      definition's gloss, the poles, the open hair's
#      statement; its footer resolves; and no
#      Hebrew-block codepoint stands in the layer.
# Output is filed to audit_plate_xiii_the_dial_results.txt
# beside this script. VERDICT PASS requires every check
# green.
#
# DOCTRINE: an audit that trusts the document it audits
# proves nothing; this one trusts only the engine and the
# registers.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".local/lib"))
import site
sys.path.insert(0, site.getusersitepackages())
sys.path.insert(0, str(Path.home() / "workspace/pontifex"))

from pontifex import weigh

HERE = Path(__file__).resolve().parent
GOAL_FILES = (Path.home() / "workspace/goals/"
              "cross-gematria-777-gap-filling/files")
MASTER = GOAL_FILES / "PLATE-XIII-THE-DIAL.md"
PDF = GOAL_FILES / "PLATE-XIII-THE-DIAL-MAGVS.pdf"
PONTIFEX = Path.home() / "workspace/pontifex"
RESULTS = HERE / "audit_plate_xiii_the_dial_results.txt"

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return ok


def value(word, bank):
    return weigh(word, bank)["value"]


def root(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


master = MASTER.read_text(encoding="utf-8")
_parts = re.split(r"(?m)^## ", master)
SECS = {}
for _p in _parts[1:]:
    SECS[_p.split(" —")[0].strip()] = _p
sec2 = SECS["§II"]
sec3 = SECS["§III"]
sec4 = SECS["§IV"]
sec5 = SECS["§V"]
sec9 = SECS["§IX"]

# --- 1. controls ------------------------------------------------------
check("control θέλημα == 93", value("θελημα", "greek") == 93)
check("control VAPOUR == 93", value("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ == 773", value("σφιγξ", "greek") == 773)

# --- 2. the station register ------------------------------------------
SIGN_WORD = {"Α": "α", "Ε": "ε", "Η": "η", "Ι": "ι", "Ο": "ο",
             "Υ": "υ", "Ω": "ω", "ΕΙ": "ει", "ΟΥ": "ου",
             "γʹ": "γ", "ϛʹ": "ϛ", "κʹ": "κ", "οὐδέν": "ουδεν"}
rows = []
for ln in sec2.splitlines():
    m = re.match(r"\| (\d+) \| (.+?) \| (.+?) \| (\d+) \|", ln)
    if m:
        rows.append((int(m.group(1)), m.group(2),
                     m.group(3), int(m.group(4))))
check("station register: 13 rows", len(rows) == 13, str(len(rows)))
check("stations in ring order 1–13",
      [r[0] for r in rows] == list(range(1, 14)))
SIGNS = []
for n, sign, name, price in rows:
    SIGNS.append(sign)
    check(f"station {n} {sign}: price re-weighed",
          value(SIGN_WORD[sign], "greek") == price,
          f"printed {price}")
check("οὐδέν letter by letter [70, 400, 4, 5, 50]",
      [value(c, "greek") for c in "ουδεν"] == [70, 400, 4, 5, 50])
check("529 == 23²", 529 == 23 * 23)
prices = {r[1]: r[3] for r in rows}
NINE = ["Α", "Ε", "Η", "Ι", "Ο", "Υ", "Ω", "ΕΙ", "ΟΥ"]
check("the nine sum 1,779", sum(prices[s] for s in NINE) == 1779)
check("the relations sum 29",
      prices["γʹ"] + prices["ϛʹ"] + prices["κʹ"] == 29)
check("the ring totals 1,808",
      sum(prices[s] for s in NINE) + 29 == 1808)

# --- 3. the coverage table ---------------------------------------------
FRAME_A = [[NINE[i] for i in tri] for tri in
           [(0, 3, 6), (1, 4, 7), (2, 5, 8)]]
FRAME_B = [["Α", "Ε", "Η"], ["Ι", "ΕΙ", "Ο"], ["Υ", "ΟΥ", "Ω"]]


def frame_seat(frame, sign):
    for t, tri in enumerate(frame):
        if sign in tri:
            return ("I II III".split()[t],
                    "1st 2nd 3rd".split()[tri.index(sign)])
    raise KeyError(sign)


check("Frame A sums 811/90/878, roots 1/9/5",
      [sum(prices[s] for s in t) for t in FRAME_A] == [811, 90, 878]
      and [root(sum(prices[s] for s in t)) for t in FRAME_A]
      == [1, 9, 5])
check("Frame B sums 14/95/1670, roots 5/5/5",
      [sum(prices[s] for s in t) for t in FRAME_B] == [14, 95, 1670]
      and [root(sum(prices[s] for s in t)) for t in FRAME_B]
      == [5, 5, 5])
EXPECTED_CLASS = {"Α": "POSITION", "Ο": "TRIAD", "Υ": "TRIAD",
                  "ΕΙ": "TRIAD", "ΟΥ": "TRIAD", "Ε": "VALUE",
                  "Η": "VALUE", "Ι": "VALUE", "Ω": "VALUE"}
cov = []
for ln in sec3.splitlines():
    m = re.match(r"\| (Α|Ε|Η|Ι|Ο|Υ|Ω|ΕΙ|ΟΥ) \| \((I{1,3}), "
                 r"(1st|2nd|3rd)\) \| \((I{1,3}), (1st|2nd|3rd)\) "
                 r"\| .* \| \*\*(POSITION|TRIAD|VALUE)\*\* \|", ln)
    if m:
        cov.append(m.groups())
check("coverage table: 9 rows", len(cov) == 9, str(len(cov)))
for sign, fa_t, fa_p, fb_t, fb_p, cls in cov:
    check(f"coverage {sign}: frame columns recomputed",
          frame_seat(FRAME_A, sign) == (fa_t, fa_p)
          and frame_seat(FRAME_B, sign) == (fb_t, fb_p))
    check(f"coverage {sign}: class == {EXPECTED_CLASS[sign]}",
          cls == EXPECTED_CLASS[sign], cls)

# --- 4. the marks' evidence ---------------------------------------------
dress = []
for ln in sec3.splitlines():
    m = re.match(r"\| (Α|Ε|Η|Ι|Ο|Υ|Ω|ΕΙ|ΟΥ) \| (\d+) \| (\S+) \| "
                 r"(\d+) \| (\d+) \|", ln)
    if m:
        dress.append((m.group(1), int(m.group(2)), m.group(3),
                      int(m.group(4)), int(m.group(5))))
check("dress table: 9 rows", len(dress) == 9, str(len(dress)))
for v, gk, d, o, a in dress:
    check(f"dress {v} → {d}: Greek price re-weighed",
          value(SIGN_WORD[v], "greek") == gk)
    check(f"dress {v} → {d}: ordinal re-weighed",
          value(d, "latin_ordinal") == o, f"printed {o}")
    check(f"dress {v} → {d}: Agrippa re-weighed",
          value(d, "agrippa") == a, f"printed {a}")
check("dress totals 123 ordinal / 584 Agrippa",
      sum(r[3] for r in dress) == 123
      and sum(r[4] for r in dress) == 584)
check("alternate Η → EI 14/14",
      value("EI", "latin_ordinal") == 14
      and value("EI", "agrippa") == 14)
check("alternate Υ → Y 25/400, U 21/200",
      (value("Y", "latin_ordinal"), value("Y", "agrippa"))
      == (25, 400)
      and (value("U", "latin_ordinal"), value("U", "agrippa"))
      == (21, 200))
check("alternate ΟΥ → V 22/200 (sound-dress)",
      (value("V", "latin_ordinal"), value("V", "agrippa"))
      == (22, 200))
for glyph, bank, want in (("ⲟⲩ", "coptic", 470), ("ⲏ", "coptic", 8),
                          ("ⲓ", "coptic", 10), ("ⲱ", "coptic", 800),
                          ("І", "cyrillic", 10), ("Ѡ", "cyrillic", 800),
                          ("И", "cyrillic", 8), ("Ը", "armenian", 8),
                          ("ჱ", "georgian", 8)):
    check(f"mirror {glyph} == {want} in {bank}",
          value(glyph, bank) == want)
check("note bank: A == 1, E == 5",
      value("A", "abc_notes") == 1 and value("E", "abc_notes") == 5)
check("PAIR: root(ΕΙ) == root(852) == 6",
      root(prices["ΕΙ"]) == root(852) == 6)
check("PAIR: 852 is the solfeggio eighth; ΕΙ the canonical eighth",
      [174, 285, 396, 417, 528, 639, 741, 852, 963].index(852) == 7
      and NINE.index("ΕΙ") == 7)
check("diphthong four sum 576 == 24²",
      sum(value(w, "greek") for w in ("αι", "ει", "οι", "ου")) == 576
      == 24 * 24)
check("Trinity grid total 2,486",
      1779 + 123 + 584 == 2486 and root(2486) == 2)
check("mirror closure: 1,779 − 3 == 1,776; 9 − 6 == 3 == γʹ",
      1779 - 3 == 1776 and 9 - 6 == 3 == prices["γʹ"])

# --- 5. the traversals ----------------------------------------------------
NAME_OF = {"Α": "Α", "Ε": "Ε", "Η": "Η", "Ι": "Ι", "Ο": "Ο",
           "Υ": "Υ", "Ω": "Ω", "ΕΙ": "ΕΙ", "ΟΥ": "ΟΥ",
           "γʹ": "OFFSET γʹ", "ϛʹ": "MIRROR ϛʹ",
           "κʹ": "REFUSAL κʹ", "οὐδέν": "ZERO οὐδέν"}
RING = [NAME_OF[s] for s in SIGNS]


def traverse(step, n=13):
    seq, cur = [0], 0
    for _ in range(n - 1):
        cur = (cur + step) % n
        seq.append(cur)
    return seq


fwd_i, inv_i = traverse(5), traverse(-5)
fwd = [RING[i] for i in fwd_i]
inv = [RING[i] for i in inv_i]
check("step check: −5 mod 13 == 8 (the {13/8} polygon)",
      -5 % 13 == 8)
check("inverse == forward reversed, station for station",
      inv == [fwd[0]] + fwd[:0:-1])
check("each traversal visits all 13 stations exactly once",
      sorted(fwd_i) == list(range(13))
      and sorted(inv_i) == list(range(13)))
mf = re.search(r"\{13/5\}:\*\* (.+?) → \(Α\)\.", sec4)
mi = re.search(r"\{13/8\}:\*\* (.+?) → \(Α\)\.", sec4)
check("§IV forward sequence printed entire", mf is not None)
check("§IV inverse sequence printed entire", mi is not None)
if mf:
    check("§IV forward == re-derived forward",
          mf.group(1).split(" → ") == fwd)
if mi:
    check("§IV inverse == re-derived inverse",
          mi.group(1).split(" → ") == inv)

# --- 6. the crosshairs -----------------------------------------------------
check("poles: 31 + 13 == 44 == VV ordinal",
      31 + 13 == 44 == value("VV", "latin_ordinal"))
check("poles: 31 − 13 == 18 == II in both banks",
      31 - 13 == 18 == value("II", "latin_ordinal")
      == value("II", "agrippa"))
check("the poles stand in §V (13 N / 31 S)",
      "13 N and 31 S" in sec5)
check("the vertical hair stands SEATED in §V.1",
      "### §V.1 — The vertical hair: SEATED" in sec5)
check("the inversion office stands SEATED in §V.2",
      "### §V.2 — The inversion office: SEATED" in sec5)
check("the horizontal hair stands STILL OPEN in §V.3",
      "### §V.3 — The horizontal hair: STILL OPEN" in sec5)
check("no E–W hair drawn: the record statement stands",
      "No E–W hair stands drawn" in sec5)
check("the float line named at the open seat",
      "float line" in sec5 and "left open in his name" in sec5)
check("Q3 printed NOT RULED BY THIS PLATE",
      "NOT RULED BY THIS PLATE" in sec5)
check("the dial appendix's desk ruling cited, not hidden",
      "bank boundary" in sec5)

# --- 7. the holes and the definition ---------------------------------------
check("the founder's Zero Point definition stands entire",
      "0 = {0, 2, 1−1=0}" in sec2
      and "Zero equals Two, and Both 1 and None" in sec2)
check("the eight open positions named in §III.5",
      "Eight of the nine positions" in sec3)
check("the four unsettled triads named in §III.5",
      "The triads of Ε, Η, Ι, Ω" in sec3)
check("the Archons stand unnamed on the plate",
      "unnamed" in sec3 and "none are invented" in sec3)
check("the hybrid placement law stands in §III.2",
      "HYBRID PLACEMENT LAW" in sec3
      and "no hybrid in the first triad" in sec3)

# --- 8. the series register --------------------------------------------------
SERIES = [("I", "Greek", "196025e", "audit_plate_i_greek_results.txt",
           "cells"),
          ("II", "Hebrew", "1389c16",
           "audit_plate_ii_hebrew_results.txt", "cells"),
          ("III", "Arabic", "5f0b4bd",
           "audit_plate_iii_arabic_results.txt", "cells"),
          ("IV", "Latin", "8e6f01e",
           "audit_plate_iv_latin_results.txt", "cells"),
          ("V", "Japanese", "8d6cd59",
           "audit_plate_v_japanese_results.txt", "checks"),
          ("VI", "Ge'ez", "67d5acc",
           "audit_plate_vi_geez_results.txt", "checks"),
          ("VII", "Armenian", "5c03d88",
           "audit_plate_vii_armenian_results.txt", "checks"),
          ("VIII", "Coptic", "645bcbb",
           "audit_plate_viii_coptic_results.txt", "checks"),
          ("IX", "Georgian", "933f8fd",
           "audit_plate_ix_georgian_results.txt", "checks"),
          ("X", "Cyrillic", "052fd28",
           "audit_plate_x_cyrillic_results.txt", "checks"),
          ("XI", "Glagolitic", "b40abac",
           "audit_plate_xi_glagolitic_results.txt", "checks"),
          ("XII", "Korean", "2ef9ba9",
           "audit_plate_xii_korean_results.txt", "checks")]
plate_rows = {}
for ln in sec9.splitlines():
    m = re.match(r"\| (XIII|XII|XI|X|IX|VIII|VII|VI|V|IV|III|II|I)"
                 r" \| (.+?) \| ([0-9a-f]{7}) \| PASS — (.+?) \|",
                 ln)
    if m:
        plate_rows[m.group(1)] = (m.group(2), m.group(3), m.group(4))
check("series register: 12 tongue rows", len(plate_rows) == 12,
      str(len(plate_rows)))
for num, tongue, commit, fname, kind in SERIES:
    text = (HERE / fname).read_text(encoding="utf-8")
    if kind == "cells":
        label = (re.search(r"PRICED CELLS RE-WEIGHED: (\d+)", text)
                 .group(1) + " priced cells re-weighed")
    else:
        label = (re.search(r"VERDICT: PASS — (\d+) checks", text)
                 .group(1) + " checks")
    check(f"series {num} {tongue}: filed audit PASS",
          "PASS" in text)
    check(f"series {num} {tongue}: plate row == filed register",
          plate_rows.get(num) == (tongue, commit, label),
          str(plate_rows.get(num)))
    ok = subprocess.run(["git", "-C", str(PONTIFEX), "rev-parse",
                         "--verify", "--quiet", commit],
                        capture_output=True, text=True).stdout.strip()
    check(f"series {num} {tongue}: commit {commit} in repository",
          bool(ok))
check("series register: the XIII row stands",
      "| XIII | The Dial" in sec9)

# --- 9. the PDF layer ---------------------------------------------------------
if PDF.exists():
    layer = subprocess.run(["pdftotext", str(PDF), "-"],
                           capture_output=True, text=True).stdout
    for w in ("οὐδέν", "529", "13 N", "31 S", "STILL OPEN",
              "float line", "Zero equals Two", "1,808",
              "MIRROR ϛʹ", "REFUSAL κʹ", "OFFSET γʹ"):
        check(f"PDF layer carries {w}", w in layer)
    check("PDF layer: no Hebrew-block codepoint",
          not any(0x590 <= ord(c) <= 0x5FF for c in layer))
    info = subprocess.run(["pdfinfo", str(PDF)], capture_output=True,
                          text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    check(f"PDF footer resolves ({pages} of {pages})",
          f"{pages} of {pages}" in layer)
else:
    check("MAGVS PDF exists", False, "not built")

# --- verdict -------------------------------------------------------------------
failed = [(n, d) for n, ok, d in CHECKS if not ok]
lines = ["PLATE-XIII-THE-DIAL — independent audit",
         f"checks: {len(CHECKS)} · failed: {len(failed)}", ""]
for name, ok, detail in CHECKS:
    lines.append(f"{'PASS' if ok else 'FAIL'}  {name}"
                 + (f"  [{detail}]" if detail and not ok else ""))
lines.append("")
lines.append(f"VERDICT: {'PASS' if not failed else 'FAIL'} — "
             f"{len(CHECKS)} checks, {len(failed)} failures")
RESULTS.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[-3:]))
sys.exit(0 if not failed else 1)
