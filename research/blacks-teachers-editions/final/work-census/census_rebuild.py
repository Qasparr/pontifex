#!/usr/bin/env python3
# ============================================================================
# census_rebuild.py -- Census regeneration + base-parse reconciliation for
# the final Black's Teacher's Edition build (Worker A).
#
# WHAT IT DOES
#   1. Regenerates the 5e/2e census by re-running the parsing logic of
#      5e/analyze.py EXACTLY (same regexes, same line ranges, same norm(),
#      same longest-kept dedup), instrumented only to also record the line
#      number of each kept row. Verifies the published aggregates
#      (5e 21,979 / census-2e 12,892 / survived 3,881 / lost 9,011 /
#      new 18,098) and STOPS if they do not reproduce.
#   2. Joins the shipped base parse (2e/entries.json, 13,145 entries) to the
#      census-2e key set on norm() keys and decomposes the 253 gap:
#      253 = 117 duplicate-key collapses inside the base parse
#          + 522 base-only keys - 386 census-only keys.
#   3. Categorizes every base-only key by the mechanism that made the
#      census parser miss it (priority-ordered, evidence-based tests
#      against the raw djvu lines and both parsers' rules).
#   4. Builds the mapping layer: every base entry is "carried" iff its
#      norm key is in the 5e key set. The two candidate relaxations
#      (R-a plural normalization, R-b Levenshtein<=1) were candidate-
#      generated and sample-verified by hand (30 pairs each, verdicts
#      embedded below as data); both failed the required 100% sample
#      precision (R-a 17/30, R-b 19/30), so NEITHER is applied and
#      "changed-form" is empty by verified decision, not by omission.
#   5. Emits census.json, mapping.json, register.json and prints the full
#      statistics block used by reconciliation.md.
#
# COPYRIGHT BOUNDARY: outputs contain headwords and status metadata ONLY.
# No 5th-edition entry text is read into any output; 5e definition text was
# consulted transiently during the manual verification pass and is nowhere
# reproduced.
# ============================================================================
import re, json, os, collections, sys

HOME = os.path.expanduser("~")
STUDY = HOME + "/workspace/user/files/Blacks-Law-Dictionary-5thEd-1979_STUDY-TEXT.txt"
DJVU2 = HOME + "/workspace/blacks-2e/source/blacks-2e-1910_djvu.txt"
BASE  = HOME + "/workspace/your_files/blacks-teachers-editions/2e/entries.json"
OUT   = HOME + "/workspace/your_files/blacks-teachers-editions/final/work-census"
os.makedirs(OUT, exist_ok=True)

# ---- census engine: regexes and logic copied verbatim from 5e/analyze.py --
HEAD5_INLINE = re.compile(r"^([A-Z][A-Za-z\-\' ]{1,60})\.\s")
HEAD5_OWN    = re.compile(r"^([A-Z][A-Za-z\-\' ]{1,55})\.$")
HEAD2_INLINE = re.compile(r"^([A-Z][A-Z0-9&'\- ]{1,55})\.\s")
HEAD2_OWN    = re.compile(r"^([A-Z][A-Z0-9&'\- ]{2,50})\.$")
PAGE_ARTIFACT = re.compile(r"^[A-Z] \d{2,}\.?$")

def norm(h): return re.sub(r"[^a-z0-9]", "", h.lower())   # analyze.py norm()

def parse5():
    lines = open(STUDY, encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "A.")
    end = next(i for i, l in enumerate(lines) if i > start and "TABLE OF ABBREVIATIONS" in l)
    rows, inline_ct, own_ct = [], 0, 0
    cur = None
    def close():
        nonlocal cur
        if cur is not None: rows.append(cur); cur = None
    for i in range(start, end):
        ln = lines[i]
        m = HEAD5_INLINE.match(ln)
        if m:
            close(); cur = [m.group(1).strip(), len(re.findall(r"\S+", ln[m.end():])), i]; inline_ct += 1
            continue
        m = HEAD5_OWN.match(ln)
        if m:
            close(); cur = [m.group(1).strip(), 0, i]; own_ct += 1
            continue
        if cur is not None: cur[1] += len(re.findall(r"\S+", ln))
    close()
    return rows, start, end, inline_ct, own_ct

def parse2():
    lines = open(DJVU2, encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if re.match(r"^A\.\s", l))
    end = 206775
    rows, inline_ct, own_ct = [], 0, 0
    cur = None
    def close():
        nonlocal cur
        if cur is not None: rows.append(cur); cur = None
    for i in range(start, end):
        ln = lines[i]
        m = HEAD2_INLINE.match(ln)
        if m:
            hw = re.sub(r"\s+", " ", m.group(1)).strip()
            if not PAGE_ARTIFACT.match(hw + "."):
                close(); cur = [hw, len(re.findall(r"\S+", ln[m.end():])), i]; inline_ct += 1
                continue
        m = HEAD2_OWN.match(ln)
        if m and not HEAD2_INLINE.match(ln):
            hw = re.sub(r"\s+", " ", m.group(1)).strip()
            if not PAGE_ARTIFACT.match(hw + "."):
                close(); cur = [hw, 0, i]; own_ct += 1
                continue
        if cur is not None: cur[1] += len(re.findall(r"\S+", ln))
    close()
    return rows, start, end, inline_ct, own_ct

def uniq(rows):                       # longest-kept dedup, as analyze.py
    d = {}
    for hw, w, ln in rows:
        k = norm(hw)
        if k not in d or w > d[k][1]: d[k] = (hw, w, ln)
    return d

e5rows, s5, e5end, i5, o5 = parse5()
e2rows, s2, e2end, i2, o2 = parse2()
u5, u2 = uniq(e5rows), uniq(e2rows)
u5map = {k: v[0] for k, v in u5.items()}
u2map = {k: v[0] for k, v in u2.items()}
k5, k2 = set(u5), set(u2)
survived, lost, new = k5 & k2, k2 - k5, k5 - k2

PUBLISHED = {"u5": 21979, "u2": 12892, "survived": 3881, "lost": 9011, "new": 18098}
GOT = {"u5": len(u5), "u2": len(u2), "survived": len(survived), "lost": len(lost), "new": len(new)}
print("REGENERATION:", GOT)
assert GOT == PUBLISHED, f"REGENERATION MISMATCH: got {GOT}, published {PUBLISHED} -- STOP"
assert (len(e5rows), i5, o5) == (26420, 14595, 11825), "5e parse forms mismatch"
assert (len(e2rows), i2, o2) == (13078, 13078, 0), "2e parse forms mismatch"
print("Regeneration reproduces every published aggregate and parse-form count. PROCEED.")

# ---- base join -------------------------------------------------------------
ents = json.load(open(BASE, encoding="utf-8"))
assert len(ents) == 13145
bk = {}
for idx, e in enumerate(ents):
    bk.setdefault(norm(e["headword"]), []).append(idx)
base_keys = set(bk)
inter = base_keys & k2
base_only = sorted(base_keys - k2)
census_only = sorted(k2 - base_keys)
dup_keys = {k: v for k, v in bk.items() if len(v) > 1}
dup_extra = len(ents) - len(base_keys)
print(f"BASE: entries={len(ents)} distinct_keys={len(base_keys)} dup_extra={dup_extra} "
      f"dup_keys={len(dup_keys)} | inter={len(inter)} base_only={len(base_only)} census_only={len(census_only)}")
assert dup_extra + len(base_only) - len(census_only) == 253 == len(ents) - len(k2)

# ---- categorize base-only keys ---------------------------------------------
# Priority order (first matching cause wins; overlaps noted in the report):
#   b_artifact   raw line matches a census pattern but PAGE_ARTIFACT rejects it
#   d_wrapped    base joined a multi-line (wrapped) headword; census sees only
#                fragments on separate lines, the tail at best a different key
#   a_guillemet  raw line begins with the stray ornament '<<' (U+00AB); the
#                census ^ anchor fails; the base parser strips it
#   a_char_*     headword contains a character outside the census class
#                [A-Z0-9&'\- ] that the base class admits: ',' '.' U+2019
#                '(' ')' (one label per offending-character set)
#   a_short_*    headword shorter than the census minimum (inline group needs
#                >=2 chars total, own-line group >=3)
#   a_long_*     headword longer than the census maximum (inline 56, own 51)
#   RESIDUE      none expected; asserted below
djvu_lines = open(DJVU2, encoding="utf-8").read().splitlines()
CENSUS_CLASS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&'- ")
cats = collections.defaultdict(list)
cat_examples = {}
for k in base_only:
    e = ents[bk[k][0]]; H = e["headword"]; L = e["line"]; raw = djvu_lines[L - 1]
    m = HEAD2_INLINE.match(raw) or HEAD2_OWN.match(raw)
    if m and PAGE_ARTIFACT.match(re.sub(r"\s+", " ", m.group(1)).strip() + "."):
        c = "b_artifact"
    elif " / " in e["head_line"]:
        c = "d_wrapped"
    elif raw.lstrip().startswith("«"):
        c = "a_guillemet"
    else:
        bad = sorted(set(ch for ch in H if ch not in CENSUS_CLASS))
        if bad:
            c = "a_char_" + "+".join(bad)
        else:
            own_form = bool(re.match(r"^.*\.\s*$", raw))
            if own_form and len(H) < 3: c = "a_short_own"
            elif not own_form and len(H) < 2: c = "a_short_inline"
            elif own_form and len(H) > 51: c = "a_long_own"
            elif not own_form and len(H) > 56: c = "a_long_inline"
            else: c = "RESIDUE"
    cats[c].append(k)
    cat_examples.setdefault(c, [])
    if len(cat_examples[c]) < 5: cat_examples[c].append(H)
assert sum(len(v) for v in cats.values()) == len(base_only) == 522
assert "RESIDUE" not in cats, f"unexplained residue: {cats.get('RESIDUE')}"
# wrapped-tail cross-check: how many wrapped entries' tail fragments the
# census crowned as keys of their own
tail_in_census = 0
for k in cats["d_wrapped"]:
    e = ents[bk[k][0]]
    tail = e["head_line"].split(" / ")[-1].rstrip(".").strip()
    if norm(tail) in k2: tail_in_census += 1
tail_keys = {norm(ents[bk[k][0]]["head_line"].split(" / ")[-1].rstrip(".").strip())
             for k in cats["d_wrapped"]}
tails_census_only = len([k for k in census_only if k in tail_keys])
print("BASE-ONLY CAUSES:", {c: len(v) for c, v in sorted(cats.items(), key=lambda t: -len(t[1]))})
print(f"wrapped tails crowned by census as own keys: {tail_in_census}/{len(cats['d_wrapped'])}; "
      f"distinct census-only keys that are wrapped tails: {tails_census_only}")

# census-only mechanisms (for the register reconciliation narrative)
row_line_by_key = {}
for hw, w, ln in e2rows: row_line_by_key.setdefault(norm(hw), ln)
co_prevblank = co_other = 0
for k in census_only:
    if k in tail_keys: continue
    ln = row_line_by_key[k]
    if ln - 1 >= 0 and djvu_lines[ln - 1].strip() != "": co_prevblank += 1
    else: co_other += 1
print(f"census-only non-tail keys: {len(census_only) - tails_census_only} "
      f"(continuation-position, no preceding blank: {co_prevblank}; other: {co_other})")

# ---- relaxations: candidate generation + embedded verification verdicts ----
# Verification protocol (executed by hand by Worker A): deterministic
# stride sample of 30 candidate pairs per relaxation; each pair judged
# same-lemma by locating both headwords in their texts and comparing the
# entries' definitional scope (2e body from entries.json; 5e entry read in
# the study text, never reproduced). Verdict lists below are in sample
# order; True = same dictionary lemma. Both relaxations FAILED the 100%
# precision gate and are therefore NOT applied to the mapping.
unmatched_keys = [k for k in base_keys if k not in k5]
def ra_variants(k):
    v = {k + "s", k + "es"}
    if k.endswith("es"): v.add(k[:-2])
    if k.endswith("s"): v.add(k[:-1])
    return v
ra_pairs = sorted((k, h) for k in unmatched_keys for h in ra_variants(k) if h in k5)
def dels(k): return {k[:i] + k[i+1:] for i in range(len(k))}
u5_by_del = collections.defaultdict(set)
for k in k5:
    if len(k) >= 7:
        for d in dels(k): u5_by_del[d].add(k)
def lev1(a, b):
    if abs(len(a) - len(b)) > 1: return False
    if len(a) == len(b): return sum(1 for x, y in zip(a, b) if x != y) <= 1
    if len(a) > len(b): a, b = b, a
    i = j = diff = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]: i += 1; j += 1
        else: j += 1; diff += 1
        if diff > 1: return False
    return True
rb_pairs = set()
for k in unmatched_keys:
    if len(k) < 7: continue
    cand = set()
    for d in dels(k): cand |= u5_by_del.get(d, set())
    for c in cand:
        if c != k and len(c) >= 7 and c[0] == k[0] and lev1(k, c): rb_pairs.add((k, c))
rb_pairs = sorted(rb_pairs)
def stride_sample(pairs, n=30):
    if len(pairs) <= n: return pairs
    step = len(pairs) / n
    return [pairs[int(i * step)] for i in range(n)]
RA_SAMPLE = stride_sample(ra_pairs); RB_SAMPLE = stride_sample(rb_pairs)
RA_VERDICTS = [True, True, False, True, True, True, True, True, True, True,
               False, True, True, False, False, True, True, False, False, False,
               True, True, True, True, False, False, False, False, False, False]
RB_VERDICTS = [True, True, True, True, False, False, False, False, False, False,
               True, True, False, True, True, False, False, True, False, True,
               True, False, True, True, True, True, True, True, True, True]
ra_prec = sum(RA_VERDICTS) / len(RA_VERDICTS)
rb_prec = sum(RB_VERDICTS) / len(RB_VERDICTS)
print(f"R-a: {len(ra_pairs)} candidate pairs; sample 30 precision {sum(RA_VERDICTS)}/30 = {ra_prec:.1%} -> REJECTED")
print(f"R-b: {len(rb_pairs)} candidate pairs; sample 30 precision {sum(RB_VERDICTS)}/30 = {rb_prec:.1%} -> REJECTED")
APPLY_RA = ra_prec == 1.0
APPLY_RB = rb_prec == 1.0

# ---- mapping layer -----------------------------------------------------------
mapping = {}
claimed5 = set()
for idx, e in enumerate(ents):
    k = norm(e["headword"])
    if k in k5:
        mapping[str(idx)] = {"fate": "carried", "e5_form": u5map[k], "via": "exact"}
        claimed5.add(k)
    elif APPLY_RA and any(h in k5 for h in ra_variants(k)):
        h = sorted(h for h in ra_variants(k) if h in k5)[0]
        mapping[str(idx)] = {"fate": "changed-form", "e5_form": u5map[h], "via": "R-a"}
        claimed5.add(h)
    elif APPLY_RB and len(k) >= 7 and any(c != k and len(c) >= 7 and c[0] == k[0] and lev1(k, c)
                                          for d in dels(k) for c in u5_by_del.get(d, set())):
        cand = sorted(c for d in dels(k) for c in u5_by_del.get(d, set())
                      if c != k and len(c) >= 7 and c[0] == k[0] and lev1(k, c))
        mapping[str(idx)] = {"fate": "changed-form", "e5_form": u5map[cand[0]], "via": "R-b"}
        claimed5.add(cand[0])
    else:
        mapping[str(idx)] = {"fate": "not-carried", "e5_form": None, "via": None}
cov = collections.Counter(v["fate"] for v in mapping.values())
assert sum(cov.values()) == 13145
print("COVERAGE:", dict(cov))

# ---- new-headword register ---------------------------------------------------
register_keys = sorted(k5 - claimed5)
register = [u5map[k] for k in register_keys]
a = len(k5 & set(base_only))          # 5e keys witnessed in 2e ONLY by base-only keys
b = len(k5 & set(census_only))        # 5e keys witnessed in 2e ONLY by census-only keys
print(f"REGISTER: {len(register)} keys; census new={len(new)}; delta={len(register) - len(new)} "
      f"(= census-only-witnessed {b} - base-only-witnessed {a} = {b - a})")
assert len(register) - len(new) == b - a

json.dump({"u5": u5map, "u2census": u2map}, open(OUT + "/census.json", "w"), ensure_ascii=False, indent=0)
json.dump(mapping, open(OUT + "/mapping.json", "w"), ensure_ascii=False, indent=0)
json.dump(register, open(OUT + "/register.json", "w"), ensure_ascii=False, indent=1)
stats = {"regen": GOT, "base_entries": len(ents), "base_keys": len(base_keys),
         "dup_extra": dup_extra, "dup_keys": len(dup_keys), "inter": len(inter),
         "base_only": len(base_only), "census_only": len(census_only),
         "causes": {c: len(v) for c, v in cats.items()}, "cat_examples": cat_examples,
         "tail_in_census": tail_in_census, "tails_census_only": tails_census_only,
         "co_prevblank": co_prevblank, "co_other": co_other,
         "ra_pairs": len(ra_pairs), "rb_pairs": len(rb_pairs),
         "ra_sample": RA_SAMPLE, "rb_sample": RB_SAMPLE,
         "ra_verdicts": RA_VERDICTS, "rb_verdicts": RB_VERDICTS,
         "coverage": dict(cov), "register": len(register), "reg_a": a, "reg_b": b,
         "s2_line1": s2 + 1, "e2_line": e2end, "s5_line1": s5 + 1, "e5_line1": e5end}
json.dump(stats, open("/tmp/censuswork/final_stats.json", "w"), ensure_ascii=False, indent=1)
print("WROTE census.json, mapping.json, register.json to", OUT)
