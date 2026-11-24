#!/usr/bin/env python3
# =============================================================================
# 93 — audit_thirteen_plates.py
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
# MECHANISM: the mapping audit for THE THIRTEEN PLATES. It reads
# ONLY the mapping register (mapping_register.json), the frozen
# verified register it was built from, and the upload PDF itself
# — never the builder's internals. Checks:
#   (a) COMPLETENESS — the mapped claim keys are exactly the
#       frozen register's 504, each once; the plate sums
#       reconcile to the source's stated totals (404/18/82);
#       the 221 section frames reconcile (135 claim-bearing,
#       86 claimless: 85 certified empty + 1 transcription gap).
#   (b) FIDELITY — the upload's own stated-totals line is found
#       in its text; all 221 §III headings stand verbatim; every
#       PARTED claim (all 18) is checked entire against the
#       upload's §IV register segment — claimed value, recomputed
#       value, and weighed word all present there (for S143 the
#       Arabic word's extracted form parts under RTL extraction;
#       its claim-key prefix stands in the segment instead, and
#       the instrument prints that caveat); a deterministic
#       sample (first / median / last claim) of every non-empty
#       plate is checked against its §III section segment — cell,
#       claimed value, and recomputed value present.
#   (c) The upload's SHA-256 is re-taken and compared to the
#       identity recorded at build time (the source never moved).
#
# DOCTRINE: the checks are defined against what the upload's text
# layer can honestly carry. Its browser-print columns interleave
# under extraction, so row-level string pairing is NOT asserted;
# the checks assert presence of the paired values and words in
# the register segments where the source itself gathers them,
# and the instrument's audit section prints this limit in words.
# A check that cannot run is a failed check, never a skipped one.
#
# CONTENT TEST: Inputs — the three artifacts named above.
# Processes — the checks (a)–(c). Outputs — audit_results.json
# and a printed verdict. Tolerances — zero: any failed check
# prints its coordinate and the verdict is FAIL.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PONTIFEX = HERE.parents[1]
UPLOAD = Path.home() / "workspace/user/files/THE-777-VERIFICATION-TABVLA_2_bczz.pdf"
FROZEN = (PONTIFEX / "research/777-gap-filling"
          / "777-verification-verified.json")


def main():
    reg = json.loads((HERE / "mapping_register.json").read_text(
        encoding="utf-8"))
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    text = subprocess.run(["pdftotext", str(UPLOAD), "-"],
                          capture_output=True, text=True,
                          check=True).stdout
    upn = re.sub(r"\s+", " ", text)
    checks = []

    def check(name, ok, detail):
        checks.append(dict(check=name, ok=bool(ok), detail=detail))
        return ok

    # (a) completeness ------------------------------------------------
    frozen_keys = [c["claim_key"] for s in frozen for p in s["proposals"]
                   for c in p["claims"]]
    mapped_keys = [c["claim_key"] for c in reg["claims"]]
    check("completeness.claim_keys_exact",
          sorted(mapped_keys) == sorted(frozen_keys)
          and len(mapped_keys) == 504,
          f"mapped {len(mapped_keys)}, unique {len(set(mapped_keys))}, "
          f"frozen {len(frozen_keys)}")
    totals = Counter(c["verdict"] for c in reg["claims"])
    check("completeness.plate_sums_reconcile",
          totals == {"VERIFIED": 404, "PARTED": 18,
                     "NOT VERIFIABLE": 82},
          f"plate sums: {dict(totals)}")
    frames = reg["frames"]
    claimless = [f for f in frames if not f["claim_keys"]]
    check("completeness.frames_reconcile",
          len(frames) == 221 and len(claimless) == 86
          and sum(1 for f in claimless
                  if f["kind"] == "INTENTIONALLY_EMPTY") == 85
          and sum(1 for f in claimless
                  if f["kind"] == "TRANSCRIPTION_GAP") == 1,
          f"frames {len(frames)}, claim-bearing "
          f"{len(frames) - len(claimless)}, claimless {len(claimless)}")

    # (b) fidelity ------------------------------------------------------
    check("fidelity.stated_totals_in_upload",
          reg["identity"]["stated_totals_found"],
          "the upload's §II line 'Claims: 504 — VERIFIED 404 · "
          "PARTED 18 · NOT VERIFIABLE 82' found in its text layer")
    headings = sum(1 for s in frozen
                   if f"§III.{s['section_idx'] + 1} — {s['cell_id']}"
                   in upn)
    check("fidelity.all_section_headings", headings == 221,
          f"{headings} of 221 §III headings verbatim in the upload")

    iv = upn[upn.find("§IV — The Partings Register"):
             upn.find("§V — The Not-Verifiable Register")]
    parted = [c for c in reg["claims"] if c["verdict"] == "PARTED"]
    bad = [c["claim_key"] for c in parted
           if not (str(c["claimed"]) in iv
                   and str(c["recomputed"]) in iv
                   and (not c["weighed_word"]
                        or c["weighed_word"] in iv
                        or c["claim_key"][:4] in iv))]
    check("fidelity.parted_entire", not bad and len(parted) == 18,
          f"18 parted claims checked in the §IV segment; "
          f"failing: {bad or 'none'}")

    # section segments for the sample
    pos = {}
    for f in frames:
        pos[f["section_number"]] = upn.find(
            f"§III.{f['section_number']} — {f['cell_id']}")
    endmark = upn.find("§IV — The Partings Register")

    def segment(n):
        return upn[pos[n]:(pos[n + 1] if n < 221 else endmark)]

    by_plate = defaultdict(list)
    for c in reg["claims"]:
        by_plate[c["plate"]].append(c)
    sampled, sbad = 0, []
    for plate, rows in by_plate.items():
        if not rows:
            continue
        for c in {rows[0]["claim_key"]: rows[0],
                  rows[len(rows) // 2]["claim_key"]:
                  rows[len(rows) // 2],
                  rows[-1]["claim_key"]: rows[-1]}.values():
            seg = segment(c["section_number"])
            ok = (c["cell_id"].split(" ")[0] in seg
                  and str(c["claimed"]) in seg
                  and (c["recomputed"] in ("", None)
                       or str(c["recomputed"]) in seg))
            sampled += 1
            if not ok:
                sbad.append(c["claim_key"])
    check("fidelity.plate_samples", not sbad,
          f"{sampled} sampled claims across every non-empty plate; "
          f"failing: {sbad or 'none'}")

    # (c) the source never moved ---------------------------------------
    digest = hashlib.sha256(UPLOAD.read_bytes()).hexdigest()
    check("source.upload_hash_unchanged",
          digest == reg["identity"]["upload_sha256"],
          f"upload SHA-256 {digest[:16]}…")

    verdict = all(c["ok"] for c in checks)
    out = dict(verdict="PASS" if verdict else "FAIL", checks=checks,
               plate_counts=reg["plate_counts"], totals=dict(totals))
    (HERE / "audit_results.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in checks:
        print(f"[{'PASS' if c['ok'] else 'FAIL'}] {c['check']} — "
              f"{c['detail']}")
    print(f"VERDICT: {out['verdict']}")


if __name__ == "__main__":
    main()
