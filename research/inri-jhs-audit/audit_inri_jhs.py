#!/usr/bin/env python3
# =============================================================================
# 93 — audit_inri_jhs.py
#
#   "Prove all things; hold fast that which is good."
#   — 1 Thessalonians 5:21
#
# XXIV day of November, Dies Martis, Sol in Sagittarius,
# Anno V:xii e.n. (2026 e.v.)
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# Scientific Illuminism — Method of Science, Aim of Religion.
#
# MECHANISM: the INDEPENDENT audit of THE-INRI-JHS-AUDIT. It trusts
# only the engine and the registers: every figure the essay prints
# is re-weighed here from its source form; every reduction chain
# and root set is re-derived; the TABVLA negatives are re-counted
# from the register; the Frame A/B triad sums are recomputed
# letter by letter; the master's printed figures are matched
# against the recomputed ones; and the PDF text layer is checked
# for the inscriptions, the totals, the hypothesis verdict, a
# resolving footer, and zero Hebrew-block codepoints.
#
# CONTENT TEST: Inputs — the master, the PDF, the engine, the
# TABVLA register. Processes — independent re-weighing and
# matching. Outputs — audit_inri_jhs_results.txt. Tolerances —
# zero failures; a single mismatch fails the audit and the essay
# does not ship.
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

BASE = (Path.home() / "workspace/goals/"
        "cross-gematria-777-gap-filling/files")
MASTER = BASE / "THE-INRI-JHS-AUDIT.md"
PDF = BASE / "THE-INRI-JHS-AUDIT-MAGVS.pdf"
TABVLA = BASE / "THE-777-VERIFICATION-TABVLA.md"
RESULTS = (Path(__file__).parent / "audit_inri_jhs_results.txt")

checks = 0
failures = []


def check(label, cond):
    global checks
    checks += 1
    if not cond:
        failures.append(label)
    return cond


def W(word, bank):
    return weigh(word, bank)["value"]


def root_chain(n):
    chain = [n]
    while chain[-1] >= 10:
        chain.append(sum(int(d) for d in str(chain[-1])))
    return chain


md = MASTER.read_text(encoding="utf-8")

# controls
check("control θέλημα 93", W("θέλημα", "greek") == 93)
check("control VAPOUR 93", W("VAPOUR", "latin_ordinal") == 93)
check("control σφίγξ 773", W("σφίγξ", "greek") == 773)

# §II figures, re-weighed from source forms
FIG = [
    ("INRI", "latin_ordinal", 50), ("INRI", "agrippa", 138),
    ("IESUS NAZARENUS REX IUDAEORUM", "latin_ordinal", 346),
    ("IESUS NAZARENUS REX IUDAEORUM", "agrippa", 2315),
    ("IESVS NAZARENVS REX IVDAEORVM", "latin_ordinal", 350),
    ("IESVS NAZARENVS REX IVDAEORVM", "agrippa", 2315),
    ("Ἰησοῦς ὁ Ναζωραῖος ὁ βασιλεὺς τῶν Ἰουδαίων", "greek", 5610),
    ("ישוע הנצרי ומלך היהודים", "hebrew", 917),
    ("ΙΗΣ", "greek", 218), ("ΙΗΣΟΥΣ", "greek", 888),
    ("ΙΗΣΟΥΣ ΧΡΙΣΤΟΣ", "greek", 1874), ("ΙΝΡΙ", "greek", 170),
    ("IHS", "latin_ordinal", 36), ("IHS", "agrippa", 107),
    ("JHS", "latin_ordinal", 37), ("JHS", "agrippa", 107),
    ("VYX", "latin_ordinal", 71),
    ("RRYYZZ", "latin_ordinal", 138), ("RRYYZZ", "agrippa", 1960),
    ("VVII", "latin_ordinal", 62), ("VVII", "agrippa", 418),
    ("QUANTUM", "latin_ordinal", 107),
    ("ΩΠΗ", "greek", 888), ("Π", "greek", 80),
]
for word, bank, expect in FIG:
    check(f"weigh {word} in {bank} == {expect}", W(word, bank) == expect)

# the classical-dress expansion values, as printed in the master
exp_v_o = W("IESVS NAZARENVS REX IVDAEORVM", "latin_ordinal")
check("master prints the V-dress ordinal", f"| {exp_v_o} |" in md
      or f"ordinal | {exp_v_o}" in md)

# the Nine: values, roots, empty roots re-derived
NINE = {"Α": 1, "Ε": 5, "Η": 8, "Ι": 10, "Ο": 70, "Υ": 400,
        "Ω": 800, "ΕΙ": 15, "ΟΥ": 470}
roots = set()
for g, v in NINE.items():
    check(f"Nine {g} == {v}", W(g, "greek") == v)
    roots.add(root_chain(v)[-1])
check("root set == {1,2,4,5,6,7,8}", roots == {1, 2, 4, 5, 6, 7, 8})
check("empty roots are 3 and 9",
      [r for r in range(1, 10) if r not in roots] == [3, 9])
check("Nine sum 1779", sum(NINE.values()) == 1779)

# reduction chains of the contacts
for n, root in [(138, 3), (36, 9), (218, 2), (888, 6), (50, 5),
                (37, 1), (107, 8), (5610, 3), (917, 8), (488, 2),
                (418, 4)]:
    check(f"root({n}) == {root}", root_chain(n)[-1] == root)
check("ΙΗΣΟΥΣ vowel sum 488",
      sum(W(g, "greek") for g in ["Ι", "Η", "Ο", "Υ"]) == 488)

# hypothesis coordinates
check("2 x 888 == 1776", 2 * W("ΙΗΣΟΥΣ", "greek") == 1776)
fa = [sum(W(g, "greek") for g in t) for t in
      [("Α", "Ι", "Ω"), ("Ε", "Ο", "ΕΙ"), ("Η", "Υ", "ΟΥ")]]
fb = [sum(W(g, "greek") for g in t) for t in
      [("Α", "Ε", "Η"), ("Ι", "ΕΙ", "Ο"), ("Υ", "ΟΥ", "Ω")]]
check("Frame A sums 811/90/878", fa == [811, 90, 878])
check("Frame B sums 14/95/1670", fb == [14, 95, 1670])
check("Frame B all root 5", all(root_chain(s)[-1] == 5 for s in fb))
check("no Frame A/B triad sums to 888", 888 not in fa + fb)
check("nearest Frame A triad Δ10", 888 - max(fa) == 10)

# five-tongue 8
for ch, bank in [("Η", "greek"), ("ⲏ", "coptic"), ("И", "cyrillic"),
                 ("Ը", "armenian"), ("ჱ", "georgian")]:
    check(f"eight {ch} in {bank}", W(ch, bank) == 8)

# TABVLA negatives re-counted
tab = TABVLA.read_text(encoding="utf-8")
for pat in ["INRI", "JHS", "IHS"]:
    check(f"TABVLA register: {pat} occurs 0 times",
          len(re.findall(rf"\b{pat}\b", tab, flags=re.I)) == 0)

# master carries the graded verdicts and fences
for phrase in ["THE EMPTY ROOTS", "THE KEY TOUCH", "NOT SEATINGS",
               "two-thirds Archon", "parted, not landed",
               "witnesses, unseated", "DOOR ONLY",
               "contacts are not seatings"]:
    check(f"master carries: {phrase}",
          phrase.lower() in md.lower() or phrase in md)

# PDF text layer
txt = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                     capture_output=True, text=True).stdout
pages = txt.count("\x0c")
check("PDF has pages", pages >= 8)
for phrase in ["INRI", "888", "138", "5610", "THE EMPTY ROOTS",
               "Flagpole of Claim and Coinage reserved"]:
    check(f"PDF layer carries: {phrase}", phrase in txt)
check("PDF layer: no Hebrew-block codepoints",
      not any(0x590 <= ord(c) <= 0x5FF for c in txt))
m = re.findall(r"— (\d+) of (\d+) —", txt)
check("PDF footer resolves",
      bool(m) and all(int(a) <= int(b) for a, b in m)
      and int(m[-1][1]) == pages)

RESULTS.write_text(
    f"THE-INRI-JHS-AUDIT — independent audit\n"
    f"checks: {checks} · failures: {len(failures)}\n"
    + "".join(f"FAIL: {f}\n" for f in failures)
    + ("PASS\n" if not failures else "FAILED\n"), encoding="utf-8")
print(f"audit: {checks} checks, {len(failures)} failures — "
      f"{'PASS' if not failures else 'FAIL: ' + '; '.join(failures)}")
sys.exit(1 if failures else 0)
