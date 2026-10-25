#!/usr/bin/env python3
"""
93 — "Do what thou wilt shall be the whole of the Law."

SCAN-LIMITATION MARKER DETECTOR — Black's Law Dictionary, 2nd Edition,
Teacher's Edition (final build), Worker C.

Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
(Greek, -ARR, All Rights Reserved, Without Prejudice).
Scribed 25 October 2026 e.v. — Method of Science, Aim of Religion.

DOCTRINE
--------
This detector MARKS ONLY. It never repairs, completes, corrects, or
invents any text. Its office is honesty of apparatus: every place where
the 2e text is incomplete because of the scan of the original is to be
flagged as a limitation of the scan-to-text process, NOT an editorial
omission — nothing is being hidden (his words, 2026-10-25 14:18 EDT).

Rules (implemented exactly as assigned; any refinement is logged in
worker-log.md with before/after counts — nothing is tuned silently):

  S1 (strong)    Empty cleaned body.
  S2 (strong)    Cleaned body ends with "-" (word broken off at end).
  S3 (strong)    Cleaned body, trailing quotes/brackets stripped, ends ",".
  S4 (strong)    Token "JU8TITIA" in headword/body; OR garbage clusters:
                 artifact token = ^[A-Za-z]*\\d[A-Za-z0-9]*$ on the
                 punctuation-stripped token core, length >= 4, >= 2
                 letters, >= 1 digit; cluster = >= 3 artifact tokens in
                 any 12-token window, OR >= 2 in the final 12 tokens.
                 Scattered single artifact tokens are NOT marked
                 (pervasive OCR garble is a quality matter, already
                 covered by the book's parsed-not-audited label).
  S5 (strong)    Entries carrying any FLAG row in the stratified audit
                 ledger (sample-ledger.csv).
  C1 (candidate) No terminal punctuation after stripping trailing
                 quotes/brackets, not already S1-S3, EXCLUDING the
                 authority-tail pattern (final token a single
                 capitalized word, length <= 14, immediately preceded
                 by ". " or standing alone as a short citation tail) —
                 Black's authorially ends entries with authority names.
  C2 (candidate) The 52 stratified-sample entries not already strong
                 via S5 (whole-entry scan-verification OPEN state).

Short bodies (1-3 tokens) with terminal punctuation and no other
signal are NOT marked: authorial brevity (one-line definitions and
see-references are complete entries).

MECHANISM
---------
Detection runs on the CLEANED body: the Cleaner class of
vol-1/build_vol1_layered.py is replicated verbatim (rules R1-R4:
tabs->space, multi-space collapse, line-break hyphen joins,
trailing-whitespace strip) so loci match the printed text.

Outputs (this folder):
  markers.json     {entry_index: [{strength, rules, anchor, reason}]}
  census-data.json (intermediate counts + per-rule samples for the
                    census and the worker log; kept in /tmp by caller
                    if preferred — here written beside markers.json
                    only when --keep-census-data is passed)

Usage: python3 detect_scan_markers.py
Love is the law, love under will. 93 93/93.
"""

import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent / "2e"  # .../blacks-teachers-editions/2e
ENTRIES = BASE / "entries.json"
LEDGER = BASE / "audit" / "sample-ledger.csv"
SUMMARY = BASE / "audit" / "sample-summary.json"
OUT = HERE / "markers.json"

SAMPLE_SEED = 20261025  # fixed seed: samples reproducible, retraceable

# ---------------------------------------------------------------------------
# Cleaner — replicated EXACTLY from vol-1/build_vol1_layered.py (R1-R4).
# MECHANISM: R1 tabs->space; R2 collapse runs of 2+ spaces; R3 join a
# hyphen broken across a line-break before a lowercase letter; R4 strip
# trailing whitespace per line; final strip of the whole body.
# ---------------------------------------------------------------------------
class Cleaner:
    def __init__(self):
        self.counts = {"R1_tabs": 0, "R2_multispace": 0,
                       "R3_hyphen_join": 0, "R4_trailing_ws": 0}

    def clean(self, text: str) -> str:
        n = text.count("\t")
        if n:
            self.counts["R1_tabs"] += n
            text = text.replace("\t", " ")
        def _squash(m):
            self.counts["R2_multispace"] += 1
            return " "
        text = re.sub(r" {2,}", _squash, text)
        def _join(m):
            self.counts["R3_hyphen_join"] += 1
            return m.group(1)
        text = re.sub(r"-\s*\n\s*([a-z])", _join, text)
        lines = text.split("\n")
        stripped = [ln.rstrip() for ln in lines]
        self.counts["R4_trailing_ws"] += sum(
            1 for a, b in zip(lines, stripped) if a != b)
        return "\n".join(stripped).strip()


# Trailing characters stripped before final-punctuation tests (S3, C1):
# straight/curly quotes, closing brackets/parens, whitespace.
TRAIL_STRIP = " \t\n\"'”’)]}»›"

ARTIFACT_RE = re.compile(r"^[A-Za-z]*\d[A-Za-z0-9]*$")
TOKEN_RE = re.compile(r"\S+")


def strip_trailing(text: str) -> str:
    """Strip trailing quotes/brackets/parens and whitespace."""
    return text.rstrip(TRAIL_STRIP)


def artifact_core(token: str):
    """Return the alphanumeric core of a whitespace token, or None if the
    token is not an artifact token per rule S4.

    REFINEMENT (logged): the S4 regex is applied to the token core
    (leading/trailing non-alphanumerics stripped) rather than the raw
    whitespace token, because OCR tokens routinely carry punctuation
    ('34R,' / '(17'); applying the regex raw would silently undercount
    clusters. Length/letter/digit tests apply to the core.
    """
    core = re.sub(r"^[^A-Za-z0-9]+|[^A-Za-z0-9]+$", "", token)
    if len(core) < 4:
        return None
    # REFINEMENT 2 (logged in worker-log.md with before/after counts):
    # ordinal numbers (10th, 25th, 16th ...) are the same class as the
    # '1st'-class the S4 spec expressly excludes; the length>=4 filter
    # alone lets 2-digit ordinals through, producing false clusters in
    # legitimate date text ("25th May, 1847, and 16th"). Ordinal cores
    # ^\d+(st|nd|rd|th)$ are therefore excluded. Before: S4 = 5 loci
    # (1 false positive, BATH, KNIGHTS OF THE idx 1346). After: S4 = 4.
    if re.fullmatch(r"\d+(st|nd|rd|th)", core, re.IGNORECASE):
        return None
    if not ARTIFACT_RE.match(core):
        return None
    letters = sum(c.isalpha() for c in core)
    digits = sum(c.isdigit() for c in core)
    if letters >= 2 and digits >= 1:
        return core
    return None


def main() -> int:
    entries = json.loads(ENTRIES.read_text(encoding="utf-8"))
    cleaner = Cleaner()
    cleaned = [cleaner.clean(e.get("body", "") or "") for e in entries]
    headwords = [e.get("headword", "") for e in entries]

    hits = []  # every rule hit: dict(idx, rule, strength, anchor, reason)

    def add(idx, rule, strength, anchor, reason):
        hits.append({"idx": idx, "rule": rule, "strength": strength,
                     "anchor": anchor, "reason": reason})

    # ---- S1 / S2 / S3 -------------------------------------------------
    for i, body in enumerate(cleaned):
        if body == "":
            add(i, "S1", "strong", "EMPTY",
                "cleaned body is empty: no definition text survived "
                "the scan-to-text process for this entry")
        elif body.endswith("-"):
            add(i, "S2", "strong", "END",
                "body ends with a hyphen: a word is broken off at the "
                "end of the scanned text")
        elif strip_trailing(body).endswith(","):
            add(i, "S3", "strong", "END",
                "body ends with a comma (after stripping trailing "
                "quotes/brackets): a printed entry cannot authorially "
                "end with a comma; text is cut off in the scan")

    strong_s123 = {h["idx"] for h in hits if h["rule"] in ("S1", "S2", "S3")}

    # ---- S4a: JU8TITIA -------------------------------------------------
    for i, e in enumerate(entries):
        in_hw = "JU8TITIA" in headwords[i]
        in_body = "JU8TITIA" in cleaned[i]
        if in_hw or in_body:
            if in_body:
                # anchor = the exact cleaned-body line segment containing it
                seg = next(s.strip() for s in cleaned[i].split("\n")
                           if "JU8TITIA" in s)
                anchor = seg
            else:
                anchor = "HEADWORD"
            add(i, "S4", "strong", anchor,
                "named OCR artifact 'JU8TITIA' (digit-for-letter "
                "garble of IVSTITIA/JUSTITIA) present in "
                + ("headword" if in_hw and not in_body else
                   "headword and body" if in_hw else "body"))

    # ---- S4b: garbage clusters ----------------------------------------
    for i, body in enumerate(cleaned):
        if not body:
            continue
        toks = [(m.start(), m.end(), m.group(0))
                for m in TOKEN_RE.finditer(body)]
        art = [j for j, (_, _, t) in enumerate(toks)
               if artifact_core(t) is not None]
        if not art:
            continue
        spans = []  # token-index spans [first, last] inclusive
        art_set = set(art)
        # window rule: >=3 artifact tokens within any 12-token window
        for a in art:
            window = [j for j in art if a <= j < a + 12]
            if len(window) >= 3:
                spans.append((window[0], window[-1]))
        # final-12 rule: >=2 artifact tokens within the final 12 tokens
        final = [j for j in art if j >= len(toks) - 12]
        if len(final) >= 2:
            spans.append((final[0], final[-1]))
        if not spans:
            continue
        # merge overlapping/adjacent spans
        spans.sort()
        merged = [list(spans[0])]
        for s, e_ in spans[1:]:
            if s <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], e_)
            else:
                merged.append([s, e_])
        for s, e_ in merged:
            anchor = body[toks[s][0]:toks[e_][1]]
            n_art = sum(1 for j in art if s <= j <= e_)
            add(i, "S4", "strong", anchor,
                f"garbage cluster: {n_art} OCR artifact tokens "
                f"(letter/digit confusions) within a 12-token window; "
                f"this passage is garbled in the scan-to-text process")

    # ---- S5: audit FLAG entries ----------------------------------------
    ledger_rows = list(csv.DictReader(LEDGER.open(encoding="utf-8")))
    flag_rows = [r for r in ledger_rows if r["STATUS"] == "FLAG"]
    hw_index = defaultdict(list)
    for i, h in enumerate(headwords):
        hw_index[h].append(i)
    s5_mapping_log = []
    s5_indices = set()
    for r in flag_rows:
        name = r["ENTRY"]
        idxs = hw_index.get(name, [])
        if len(idxs) != 1:
            s5_mapping_log.append(
                f"FLAG entry {name!r}: exact-match indices {idxs} "
                f"(NOT uniquely mapped — no locus invented)")
            continue
        i = idxs[0]
        s5_indices.add(i)
        field, note = r["FIELD"], r["NOTE"]
        if field == "HEADWORD":
            anchor = "HEADWORD"
        elif field == "XREF-SEE":
            # anchor: the cleaned cross-reference segment itself
            raw_clean = cleaner.clean(r["RAW OCR"] or "")
            if raw_clean and raw_clean in cleaned[i]:
                anchor = raw_clean
            else:
                last_tok = raw_clean.split()[-1] if raw_clean.split() else ""
                anchor = last_tok if last_tok and last_tok in cleaned[i] \
                    else "ENTRY"
        else:  # BODY truncation flags
            anchor = "END"
        add(i, "S5", "strong", anchor,
            f"stratified audit FLAG ({field}): {note}")
        s5_mapping_log.append(
            f"FLAG entry {name!r} ({field}: {note}) -> index {i}, "
            f"anchor {anchor!r}")

    # ---- C1: no terminal punctuation -----------------------------------
    c1_excluded_authority = 0
    c1_subclasses = Counter()
    for i, body in enumerate(cleaned):
        if not body or i in strong_s123:
            continue
        stripped = strip_trailing(body)
        if not stripped or stripped.endswith((".", "!", "?")):
            continue
        # candidate locus — test the authority-tail exclusion
        toks = [(m.start(), m.end(), m.group(0))
                for m in TOKEN_RE.finditer(stripped)]
        last = toks[-1][2]
        core = re.sub(r"^[^A-Za-z0-9]+|[^A-Za-z0-9]+$", "", last)
        is_single_cap = (re.fullmatch(r"[A-Z][A-Za-z'’-]*", core)
                         is not None and len(core) <= 14)
        if is_single_cap:
            before = stripped[:toks[-1][0]].rstrip()
            preceded_by_period = before.endswith(".")
            stands_alone_line = ("\n" in stripped[toks[-2][1]:]) \
                if len(toks) >= 2 else True
            if preceded_by_period or stands_alone_line:
                c1_excluded_authority += 1
                continue
            c1_subclasses["capitalized-final-word-not-excluded"] += 1
        elif core and core[-1].isdigit():
            c1_subclasses["ends-with-digit-citation-tail"] += 1
        elif stripped.endswith((";", ":")):
            c1_subclasses["ends-semicolon-or-colon"] += 1
        elif core and core[0].islower():
            c1_subclasses["ends-lowercase-word"] += 1
        else:
            c1_subclasses["other"] += 1
        add(i, "C1", "candidate", "END",
            "body ends without terminal punctuation (. ! ?) after "
            "stripping trailing quotes/brackets, and is not an "
            "authority-name tail: possible truncation in the scan")

    # ---- C2: OPEN-SCAN sample entries not already strong via S5 --------
    sample = json.loads(SUMMARY.read_text(encoding="utf-8"))[
        "sample_headwords"]
    c2_mapping_log = []
    for name in sample:
        idxs = hw_index.get(name, [])
        if len(idxs) != 1:
            c2_mapping_log.append(
                f"sampled headword {name!r}: exact-match indices {idxs} "
                f"(no locus invented)")
            continue
        i = idxs[0]
        if i in s5_indices:
            c2_mapping_log.append(
                f"sampled headword {name!r} -> index {i}: already strong "
                f"via S5, C2 not added")
            continue
        add(i, "C2", "candidate", "ENTRY",
            "stratified sample audit (2026-10-18): scan verification "
            "OPEN for this entry")
        c2_mapping_log.append(
            f"sampled headword {name!r} -> index {i}: C2 candidate added")

    # ---- Dedupe / merge per entry+anchor -------------------------------
    merged = {}
    for h in hits:
        key = (h["idx"], h["anchor"])
        m = merged.setdefault(key, {"strength": "candidate",
                                     "rules": set(), "reasons": []})
        if h["strength"] == "strong":
            m["strength"] = "strong"
        m["rules"].add(h["rule"])
        if h["reason"] not in m["reasons"]:
            m["reasons"].append(h["reason"])
    markers = defaultdict(list)
    for (idx, anchor), m in sorted(merged.items()):
        markers[idx].append({
            "strength": m["strength"],
            "rules": sorted(m["rules"]),
            "anchor": anchor,
            "reason": " | ".join(m["reasons"]),
        })
    OUT.write_text(json.dumps({str(k): v for k, v in markers.items()},
                              ensure_ascii=False, indent=1),
                   encoding="utf-8")

    # ---- Census data + precision samples -------------------------------
    rng = random.Random(SAMPLE_SEED)
    per_rule_hits = Counter(h["rule"] for h in hits)
    per_rule_entries = {r: len({h["idx"] for h in hits if h["rule"] == r})
                        for r in sorted(per_rule_hits)}

    def excerpt(h):
        body = cleaned[h["idx"]]
        if h["anchor"] == "EMPTY":
            return "(cleaned body is empty)"
        if h["anchor"] == "END":
            return "…" + body[-110:].replace("\n", " / ")
        if h["anchor"] == "ENTRY":
            return body[:110].replace("\n", " / ") + "…"
        if h["anchor"] == "HEADWORD":
            return f"headword={headwords[h['idx']]!r}; body: " + \
                body[:80].replace("\n", " / ") + "…"
        return "anchor-substring: " + h["anchor"][:170].replace("\n", " / ")

    samples = {}
    for rule in sorted(per_rule_hits):
        pool = [h for h in hits if h["rule"] == rule]
        pick = pool if len(pool) <= 10 else rng.sample(pool, 10)
        samples[rule] = [{"idx": h["idx"], "headword": headwords[h["idx"]],
                          "excerpt": excerpt(h)} for h in pick]

    marked_idx = set(markers)
    short_bodies = [i for i, b in enumerate(cleaned)
                    if 1 <= len(b.split()) <= 3]
    short_unmarked = [i for i in short_bodies if i not in marked_idx]
    short_with_term = [i for i in short_unmarked
                       if strip_trailing(cleaned[i]).endswith((".", "!", "?"))]

    census = {
        "total_entries": len(entries),
        "cleaner_counts": cleaner.counts,
        "hits_per_rule": dict(per_rule_hits),
        "entries_per_rule": per_rule_entries,
        "merged_markers_total": sum(len(v) for v in markers.values()),
        "marked_entries_total": len(markers),
        "strong_entries": len({i for i, v in markers.items()
                                if any(m["strength"] == "strong"
                                       for m in v)}),
        "candidate_only_entries": len({i for i, v in markers.items()
                                       if all(m["strength"] == "candidate"
                                              for m in v)}),
        "strong_markers": sum(1 for v in markers.values() for m in v
                              if m["strength"] == "strong"),
        "candidate_markers": sum(1 for v in markers.values() for m in v
                                 if m["strength"] == "candidate"),
        "c1_excluded_authority_tail": c1_excluded_authority,
        "c1_kept_subclasses": dict(c1_subclasses),
        "s5_mapping_log": s5_mapping_log,
        "c2_mapping_log": c2_mapping_log,
        "short_bodies_1_3_tokens": len(short_bodies),
        "short_bodies_unmarked": len(short_unmarked),
        "short_bodies_unmarked_with_terminal_punct": len(short_with_term),
        "samples": samples,
        "loci": [{"idx": h["idx"], "headword": headwords[h["idx"]],
                  "rule": h["rule"], "strength": h["strength"],
                  "anchor": h["anchor"], "reason": h["reason"]}
                 for h in sorted(hits, key=lambda x: (x["idx"], x["rule"]))],
        "merged_loci": [{"idx": idx, "headword": headwords[idx],
                         "strength": m["strength"],
                         "rules": m["rules"], "anchor": m["anchor"],
                         "reason": m["reason"]}
                        for idx in sorted(markers)
                        for m in markers[idx]],
    }
    (HERE / "census-data.json").write_text(
        json.dumps(census, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in census.items()
                      if k not in ("samples", "loci", "merged_loci",
                                   "s5_mapping_log", "c2_mapping_log")},
                     indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
