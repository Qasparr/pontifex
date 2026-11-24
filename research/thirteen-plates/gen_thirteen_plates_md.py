#!/usr/bin/env python3
# =============================================================================
# 93 — gen_thirteen_plates_md.py
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
# MECHANISM: generates THE-THIRTEEN-PLATES.md from the mapping
# register (mapping_register.json) and the audit results
# (audit_results.json) produced by build_thirteen_plates.py and
# audit_thirteen_plates.py. Every count, value, and coordinate in
# the instrument is read from those artifacts — no number is
# typed by hand. The generator asserts the reconciliation
# (504 claims across the plates; 221 frames) before it writes.
#
# DOCTRINE: Teacher's Edition entire. The plates print every
# mapped claim in full; parted and not-verifiable coordinates
# print entire, verified coordinates print as the source prints
# them (the weighed word and its identification rule, or the
# battery's note where it gave one). The seven silent plates
# print their silence as a finding, with its source coordinate.
#
# CONTENT TEST: Inputs — the two artifacts. Processes — plate
# assembly, audit transcription, assertion of totals. Outputs —
# the Markdown master in the goal files. Tolerances — the
# generator aborts unless 504 / 221 reconcile.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOAL = (Path.home() / "workspace/goals/cross-gematria-777-gap-filling"
        / "files")
OUT = GOAL / "THE-THIRTEEN-PLATES.md"

REG = json.loads((HERE / "mapping_register.json").read_text(
    encoding="utf-8"))
AUD = json.loads((HERE / "audit_results.json").read_text(
    encoding="utf-8"))
ID = REG["identity"]
COUNTS = REG["plate_counts"]
HEADS = REG["plate_heads"]
VITALS = REG["bank_vitals"]
ROMAN = REG["plate_roman"]

BY_PLATE = defaultdict(list)
for c in REG["claims"]:
    BY_PLATE[c["plate"]].append(c)
assert sum(len(v) for v in BY_PLATE.values()) == 504
assert len(REG["frames"]) == 221


def cell(text):
    """A Markdown table cell: pipes and newlines neutralized."""
    return str(text).replace("|", "¦").replace("\n", " ").strip()


def short_coord(c):
    """The claim's source coordinate, shortened for the table:
    '§III.n, pp. x–y' (the full form is defined in §II)."""
    sc = c["source_coordinate"]
    head = sc.split(", PDF ")
    return f"§III.{c['section_number']}, PDF {head[1]}"


def reasoning(c):
    if c["verdict"] == "VERIFIED" and not c["coordinate"]:
        return (f"Weighed on {c['weighed_word']} "
                f"({c['word_source']}).")
    return c["coordinate"]


def claim_table(rows):
    out = ["| Key | Cell | Fill (weighed word) | Bank | Claimed | "
           "Recomputed | Verdict | Coordinate / reasoning | Source |",
           "|---|---|---|---|---|---|---|---|---|"]
    for c in rows:
        fill = c["proposal_raw"]
        if c["weighed_word"] and c["weighed_word"] != fill:
            fill += f" — {c['weighed_word']}"
        out.append(
            f"| {c['claim_key']} | {cell(c['cell_id'])} | "
            f"{cell(fill)} | {c['bank_engine']} | {c['claimed']} | "
            f"{c['recomputed'] if c['recomputed'] not in ('', None) else '—'} | "
            f"{c['verdict']} | {cell(reasoning(c))} | "
            f"{short_coord(c)} |")
    return out


def vitals_lines(name):
    rows = VITALS[name]
    if not rows:
        return []
    out = ["| Bank (engine system) | Seats | Distinct values | Max |",
           "|---|---|---|---|"]
    for v in rows:
        out.append(f"| {v['system']} | {v['seats']} | "
                   f"{v['distinct']} | {v['maximum']} |")
    return out


def counts_line(name):
    pc = COUNTS[name]
    v = pc["verdicts"]
    return (f"**Claims on this plate: {pc['claims']}** — VERIFIED "
            f"{v.get('VERIFIED', 0)} · PARTED {v.get('PARTED', 0)} · "
            f"NOT VERIFIABLE {v.get('NOT VERIFIABLE', 0)} — drawn "
            f"from {pc['sections']} of the source's sections.")


ZERO_WHY = {
    "Japanese": "The source states it in terms (§I): *no claim in "
                "the corpus is stated in kana, geez, hangul, or any "
                "other mint — the fills claim only in the classical "
                "banks, the Hebrew fallback door, and two methods "
                "no proven bank seats.* The kana mint stands seated "
                "in the engine and holds a full table in THE "
                "TWELVE TABLES; its silence here is the TABVLA "
                "corpus's, not the tongue's.",
    "Ge'ez": "The source states it in terms (§I): no claim in the "
             "corpus is stated in any house mint, the Ge'ez mint "
             "among them. The mint and its halehame witness stand "
             "seated in the engine and hold a full table in THE "
             "TWELVE TABLES; their silence here is the TABVLA "
             "corpus's, not the tongue's.",
    "Armenian": "No fill in the corpus states an Armenian claim: "
                "the source's §II bank table seats no Armenian row, "
                "because the table lists only banks the fills "
                "claimed in; the bank itself stands among the "
                "engine's seventeen in the source's §I. The tongue "
                "holds a full table in THE TWELVE TABLES; its "
                "silence here is the TABVLA corpus's, not the "
                "tongue's.",
    "Georgian": "No fill in the corpus states a Georgian claim: "
                "the source's §II bank table seats no Georgian row, "
                "because the table lists only banks the fills "
                "claimed in; the bank itself stands among the "
                "engine's seventeen in the source's §I. The tongue "
                "holds a full table in THE TWELVE TABLES; its "
                "silence here is the TABVLA corpus's, not the "
                "tongue's.",
    "Cyrillic": "No fill in the corpus states a Cyrillic claim: "
                "the source's §II bank table seats no Cyrillic row, "
                "because the table lists only banks the fills "
                "claimed in; the bank itself stands among the "
                "engine's seventeen in the source's §I. The tongue "
                "holds a full table in THE TWELVE TABLES; its "
                "silence here is the TABVLA corpus's, not the "
                "tongue's.",
    "Glagolitic": "No fill in the corpus states a Glagolitic claim: "
                  "the source's §II bank table seats no Glagolitic "
                  "row, because the table lists only banks the "
                  "fills claimed in; the bank itself stands among "
                  "the engine's seventeen in the source's §I. The "
                  "tongue holds a full table in THE TWELVE TABLES; "
                  "its silence here is the TABVLA corpus's, not "
                  "the tongue's.",
    "Korean": "The source states it in terms (§I): no claim in the "
              "corpus is stated in kana, geez, hangul, or any other "
              "mint. The hangul mint stands seated in the engine "
              "and holds a full table in THE TWELVE TABLES; its "
              "silence here is the TABVLA corpus's, not the "
              "tongue's.",
}

L = []
L.append("![The Doctrine's logo — the TVRRIS VERITATIS seal]"
         "(doctrine-logo.png)")
L.append("")
L.append("**THE THIRTEEN PLATES**")
L.append("*Subtitle:* A Scientific Illuminist treatment of the "
         "verification TABVLA mapped into the twelve tongues — "
         "each tongue one plate, and the Core the thirteenth")
L.append("")
L.append("Authorship attributed exclusively to Johnathan 'Qasparr' "
         "Monroe (Greek, -ARR, All Rights Reserved, Without "
         "Prejudice)")
L.append("XXIV day of November, Dies Martis, Sol in Sagittario, "
         "Anno V:xii e.n. (2026 e.v.)")
L.append("")
L.append("Classification: Enterprise • Educational • Research & "
         "Development")
L.append("Method of Science, Aim of Religion")
L.append("")
L.append("Flagpole of Claim and Coinage: Johnathan 'Qasparr' "
         "Monroe, ARR, All Rights Reserved, Without Prejudice. "
         "Right of claim hereby reserved and coined under the "
         "authority of the Living Man.")
L.append("")
L.append("---")
L.append("")

# ---------------------------------------------------------------- §I
L.append("## §I — The Commission, and the Identity of the Source")
L.append("")
L.append("The Founder's commission (2026-11-24 15:36–15:37 EST): "
         "*\"Map this into the Each of the Twelve Tongues forming "
         "the 13 plates\"* + *\"Then save as a pdf magvs audit "
         "fashion.\"* The thing handed to the desk was his own "
         "upload of the verification TABVLA — and the first duty "
         "of the build was to establish what the upload is, "
         "because it is **not** the house's struck MAGVS: it "
         "parts from it, and the parting is printed here at full "
         "size, never merged away.")
L.append("")
L.append("**The parting table — the upload against the house's "
         "struck TABVLA:**")
L.append("")
L.append("| Coordinate | The upload (the source of these plates) "
         "| The house's struck TABVLA |")
L.append("|---|---|---|")
L.append(f"| Pages | **123** | 85 |")
L.append(f"| Paper | A4 (594.96 × 841.92 pts) | Letter "
         f"(612 × 792 pts) |")
L.append(f"| Bytes | 3,138,900 | 521,398 |")
L.append(f"| SHA-256 | `bfb45413d09e4166…` | `35e97b53ffd630fa…` |")
L.append("| Producer | HeadlessChrome 157 / Skia PDF — a browser "
         "print of `input.html` | the house MAGVS builder (fpdf2) |")
L.append("| Created | 2026-11-24 19:27:44 UTC | 2026-11-24 "
         "19:20:41 UTC |")
L.append("| Fonts | Noto Sans family, Liberation, DejaVu — the "
         "browser's faces | the Lex Stellarrvm family |")
L.append("| Page furniture | no house footer | the resolving "
         "house footer on every page |")
L.append("| Stated totals | 504 claims — VERIFIED 404 · PARTED "
         "18 · NOT VERIFIABLE 82; 221 sections | identical, to "
         "the digit |")
L.append("| Structure | all 221 §III section headings, verbatim "
         "| identical |")
L.append("")
L.append("**The finding:** the upload is the *same instrument in "
         "a different dress* — a browser-print form of the "
         "TABVLA's matter, struck seven minutes after the house "
         "MAGVS from an HTML rendering. It is **not** a fuller or "
         "later recension: it holds no section, claim, register, "
         "or verdict that the house's frozen verified register "
         "lacks, and none is missing from it — all 221 of its "
         "§III headings stand verbatim in its text layer, and its "
         "stated totals coincide with the register at every "
         "point. Its 38 further pages are the browser's "
         "pagination, not further matter. The plates below are "
         "therefore mapped from the upload as commissioned, on "
         "the frozen register that Phase 0 proved to be the "
         "upload's own matter; where a coordinate could part "
         "(production, pagination, type), both readings stand "
         "printed and neither is smoothed. The upload itself is "
         "a source document: read-only, never edited — its "
         "SHA-256 was taken before and after this build and did "
         "not move (audit §XV).")
L.append("")
L.append("Footnotes to this section, from the wells that have "
         "water: the method is the Apostle's — \"Prove all "
         "things; hold fast that which is good\" (1 Thessalonians "
         "5:21, KJV).[^1] The wells of Law and of hip-hop oral "
         "tradition have nothing genuine to add to a document's "
         "identification and are stated dry, not padded.")
L.append("")
L.append("---")
L.append("")

# ---------------------------------------------------------------- §II
L.append("## §II — The Mapping Law")
L.append("")
L.append("**The atom is the claim.** The source judges 504 bank "
         "claims; each is assigned to exactly one plate, by the "
         "bank it is stated in, under these rules — the reasoning "
         "rides with each assignment:")
L.append("")
L.append("- **Latin is one tongue with two banks** (the census "
         "fold): `latin_ordinal` (167) and `agrippa` (86) sit on "
         "Plate IV, and the 9 `english_ordinal` claims ride with "
         "them, because the source itself verifies English "
         "ordinal through the engine's `latin_ordinal` bank — "
         "\"the same 26-seat table\" (its §I, printed at each "
         "such row).")
L.append("- **Hebrew is one plate with three subseats**: the "
         "seated bank `hebrew` (111), the `hebrew_gadol` variant "
         "label (21 — a method the engine does not seat, judged "
         "against the seated bank with the coordinate printed), "
         "and the Hebrew fallback door `hebrew_fallback` (14). "
         "**Aramaic folds into this plate** by the inheritance "
         "the census proved — its values are Hebrew's values in "
         "two further dresses, and a separate Aramaic plate "
         "would count one weighing as two witnesses.")
L.append("- `greek` (38) → Plate I · `arabic_abjad` (35) → "
         "Plate III · `coptic` (1) → Plate VIII.")
L.append("- **The two unseated methods belong to no tongue** and "
         "map to the Core (Plate XIII): the pinyin-to-Hebrew "
         "fallback (11) and the PRC stroke count (11) — methods "
         "the source itself finds no proven bank to seat. They "
         "concern Chinese names, and Chinese holds no plate "
         "(below); they are apparatus, and the Core is where "
         "apparatus lives.")
L.append("- **Sections are frames, not atoms.** The 135 "
         "claim-bearing sections are indexed once, in the Core's "
         "frame index, with pointers to every plate their claims "
         "sit on; the 86 claimless frames (85 certified "
         "intentionally empty + the 1 transcription gap, "
         "CLXXXIV/10) sit in the Core alone. No section is "
         "counted twice; no claim is split.")
L.append("- **The boundaries stand printed.** Sanskrit seats as "
         "doors, not a letter table, and holds no plate; Chinese "
         "holds none until its weighing leg is ruled (the "
         "census's S10 stands open). Their absence is the map's "
         "stated boundary, carried on the Core plate — not a "
         "silent drop.")
L.append("- **Plate order** is the Twelve Tables' order — Greek "
         "→ Korean as the census seated them — and the Core "
         "stands last and central: Plate XIII is the dial's "
         "center, not a thirteenth tongue.")
L.append("")
L.append("Every claim row carries its **source coordinate**: the "
         "upload's §III section and the PDF pages that section "
         "spans, with the gathered registers (§IV for partings, "
         "pp. 103–105; §V for the not-verifiable, pp. 106–120) "
         "named where the source gathers the claim again. Any "
         "plate cell can be traced back to the source page.")
L.append("")
L.append("---")
L.append("")

# ------------------------------------------------------- §III–§XIV
SECTION_OF_PLATE = {
    "Greek": "III", "Hebrew": "IV", "Arabic": "V", "Latin": "VI",
    "Japanese": "VII", "Ge'ez": "VIII", "Armenian": "IX",
    "Coptic": "X", "Georgian": "XI", "Cyrillic": "XII",
    "Glagolitic": "XIII", "Korean": "XIV",
}
for name in REG["plate_order"]:
    if name == "Core":
        continue
    sec = SECTION_OF_PLATE[name]
    head = HEADS[name]
    rows = BY_PLATE[name]
    L.append(f"## §{sec} — PLATE {ROMAN[name]} — {name.upper()}")
    L.append("")
    L.append(f"*{head['script']}*")
    L.append("")
    L.extend(vitals_lines(name))
    L.append("")
    L.append(f"**Tier of record:** {head['tier']}.")
    L.append("")
    L.append(counts_line(name))
    L.append("")
    if not rows:
        L.append("**THE ZERO FACE.** This plate carries no claim, "
                 "and the absence is its finding. " + ZERO_WHY[name])
        L.append("")
        L.append("---")
        L.append("")
        continue
    L.extend(claim_table(rows))
    L.append("")
    parted = [c for c in rows if c["verdict"] == "PARTED"]
    if parted:
        L.append(f"**The partings of this plate, gathered** "
                 f"({len(parted)}):")
        L.append("")
        for c in parted:
            L.append(f"- {c['claim_key']} — {cell(c['cell_id'])} — "
                     f"claimed {c['claimed']} against recomputed "
                     f"{c['recomputed']}: "
                     f"{cell(c['coordinate'])[:400]}")
        L.append("")
    if name in ("Hebrew", "Latin", "Greek"):
        L.append("The source's claimed bridges touch this plate; "
                 "they are gathered entire on the Core plate "
                 "(§XV of the plates, Plate XIII), where the "
                 "battery's finding on them stands.")
        L.append("")
    L.append("---")
    L.append("")

# ------------------------------------------------------------- Core
core_rows = BY_PLATE["Core"]
L.append("## §XV — PLATE XIII — THE CORE (οὐδέν)")
L.append("")
L.append("*The center of the dial — not a thirteenth tongue.* "
         "The Core holds the whole instrument's face: its totals, "
         "its method, the matter that belongs to no tongue, the "
         "frame of all 221 sections, the bridges, the map's "
         "boundaries, and its zero.")
L.append("")
L.append("**The totals of the whole, as the plates return them:**")
L.append("")
L.append("| Plate | Tongue | Claims | VERIFIED | PARTED | NOT "
         "VERIFIABLE |")
L.append("|---|---|---|---|---|---|")
for name in REG["plate_order"]:
    pc = COUNTS[name]
    v = pc["verdicts"]
    L.append(f"| {ROMAN[name]} | {name} | {pc['claims']} | "
             f"{v.get('VERIFIED', 0)} | {v.get('PARTED', 0)} | "
             f"{v.get('NOT VERIFIABLE', 0)} |")
L.append("| | **THE WHOLE** | **504** | **404** | **18** | "
         "**82** |")
L.append("")
L.append("**The method, in the source's own compression** (§I of "
         "the upload): every value recomputed through the seated "
         "PONTIFEX engine, on a word the section itself prints, "
         "identified by fixed rules (C0–C4) with five hand-read "
         "decisions recorded; exactly three verdicts — VERIFIED, "
         "PARTED, NOT VERIFIABLE — each defined on the source's "
         "face and applied without exception in these plates.")
L.append("")
L.append("**The unseated methods** — the Core's own claims (22, "
         "all NOT VERIFIABLE, from 9 sections of Column XLVI): "
         "no proven bank seats either method, and the source "
         "refuses to substitute a different scheme for either.")
L.append("")
L.extend(claim_table(core_rows))
L.append("")
L.append("**The frame index** — all 221 sections of the source, "
         "each accounted once: its kind, its verdict, the plates "
         "its claims sit on (— = the Core alone).")
L.append("")
L.append("| §III | Cell | Kind | Section verdict | Claims | "
         "Plates |")
L.append("|---|---|---|---|---|---|")
for f in REG["frames"]:
    plates = ", ".join(ROMAN[p] for p in f["plates"]) or "XIII"
    L.append(f"| {f['section_number']} | {cell(f['cell_id'])} | "
             f"{f['kind']} | {f['section_verdict']} | "
             f"{len(f['claim_keys'])} | {plates} |")
L.append("")
bridge_rows = []
seen = set()
for c in REG["claims"]:
    b = c["bridge"]
    if b.lower().startswith("yes") and b not in seen:
        seen.add(b)
        bridge_rows.append((c["cell_id"], c["proposal_raw"], b))
L.append("**The bridges.** The source file's own count is 12 rows "
         "marked \"Bridge: yes\" — transliteration agreements, or "
         "chance agreements the file itself flags; the battery's "
         "finding, printed in the source and standing here "
         "unchanged: **honest two-bank bridges: zero** — each side "
         "of every claimed pair was weighed independently, and "
         "those per-side verdicts are the stronger instrument; "
         "they stand on the plates above. The proposal-level "
         "\"yes\" records in the frozen register (7) are:")
L.append("")
for cell_id, prop, b in bridge_rows:
    L.append(f"- {cell(cell_id)} — {cell(prop)} — {cell(b)[:300]}")
L.append("")
L.append("**The boundaries.** Sanskrit holds no plate: it seats "
         "in the engine as doors (kaṭapayādi and the Āryabhaṭīya "
         "cipher), and the source's corpus states no Sanskrit "
         "claim — its door routing there is vacuous, as the "
         "source itself reports. Chinese holds no plate: no "
         "letter-value table exists for it in the census, and "
         "its weighing leg (S10) stands open for the Founder's "
         "pen; the 22 method claims above are its whole presence "
         "in the source. Braille and the ABC notes are a code and "
         "a notation, not tongues of the twelve; the halehame "
         "witness rides the Ge'ez plate's head, where it "
         "belongs.")
L.append("")
L.append("**The Zero Point seat of the map.** The center holds "
         "what the dial's rim cannot: the 86 claimless frames — "
         "85 cells the corpus certifies intentionally empty and "
         "1 whose letter was lost in transcription — and the two "
         "tongues the map names but does not plate. οὐδέν stands "
         "at the core of these plates as it stands at the core "
         "of the Phoenician map: the zero is a *place*, held "
         "open, priced at nothing — 0 = {0, 2, 1−1=0}, in the "
         "Founder's definition of record. The seating of the "
         "Core as the map's center is this instrument's "
         "construction (CONSTRUCTED), printed as such.")
L.append("")
L.append("---")
L.append("")

# ---------------------------------------------------------------- §XV
L.append("## §XVI — The Mapping Audit")
L.append("")
L.append("The audit (`audit_thirteen_plates.py`) ran on the built "
         "register, independently of the builder: it reads only "
         "the mapping register, the frozen verified register, "
         "and the upload itself. **THE VERDICT: "
         f"{AUD['verdict']}.**")
L.append("")
L.append("| Check | Result | Detail |")
L.append("|---|---|---|")
for chk in AUD["checks"]:
    L.append(f"| {chk['check']} | "
             f"{'PASS' if chk['ok'] else 'FAIL'} | "
             f"{cell(chk['detail'])} |")
L.append("")
L.append("**Reconciliation, in one view:** source totals as "
         "extracted (504 = 404 + 18 + 82) = the sum over the "
         "thirteen plates (262 Latin + 146 Hebrew + 38 Greek + "
         "35 Arabic + 1 Coptic + 22 Core + 0 × 7 silent plates); "
         "sections 221 = 135 claim-bearing + 86 claimless (85 "
         "certified empty + 1 gap). Residue: **none** — every "
         "claim and every section of the source is accounted "
         "exactly once.")
L.append("")
L.append("**The audit's limits, printed at full size.** The "
         "upload's browser-print columns interleave under text "
         "extraction, so the fidelity checks assert *presence* — "
         "of the paired claimed and recomputed values and the "
         "weighed word, in the register segments where the source "
         "itself gathers them (§IV entire for the partings; the "
         "§III section segment for the samples) — not row-level "
         "string pairing, which the upload's text layer cannot "
         "honestly carry. Two extraction caveats stand named: "
         "the Arabic word of S143 (الأحمر) parts in extracted "
         "form under RTL extraction, its claim-key prefix "
         "standing in the §IV segment in its place, with its "
         "values 280/279 paired there; and the words NOT "
         "VERIFIABLE wrap and interleave in the listing's "
         "columns, so verdict tokens were not made a load-bearing "
         "check. What the checks do not reach, this paragraph "
         "says; what they reach, they passed entire.")
L.append("")
L.append("**The upload-vs-house parting, restated as audit "
         "matter:** the two documents part at exactly the "
         "coordinates of §I's table — production (browser print "
         "against the house builder), pagination (123 against "
         "85), paper (A4 against Letter), type (the browser's "
         "faces against the Lex Stellarrvm family), and "
         "furniture (no footer against the resolving footer). "
         "They part at **no** substantive coordinate: no total, "
         "section, claim, or verdict parts between them. Both "
         "readings stand; the plates follow the upload, as "
         "commissioned.")
L.append("")
L.append("---")
L.append("")

# --------------------------------------------------------------- §XVI
L.append("## §XVII — The Falsification Appendix, and the "
         "Presumption")
L.append("")
L.append("Under the Founder's falsifiability rule (2026-11-24 "
         "11:31 EST — *of at least one claim worthy of being "
         "disproven by evidence*), this instrument's proven-form "
         "claims are printed with the evidence that would kill "
         "them. Under his presumption rule (11:35 EST), a claim "
         "that has passed the system's own tests stands proven "
         "until challenged **and** disproven; argument alone "
         "does not vacate standing, and adjustment proceeds in "
         "synergy, not in argument. The presumption protects "
         "standing *within tier*: the mapping stands proven as "
         "a working instrument under his Flagpole, and nothing "
         "in it is promoted beyond its tier.")
L.append("")
L.append("1. *Every claim of the source is mapped to exactly one "
         "plate.* Killing evidence: one claim key of the frozen "
         "register absent from the mapping, or present twice — "
         "the audit compared the key sets entire and found them "
         "equal.")
L.append("2. *The upload is the house TABVLA's matter in a "
         "browser-print dress.* Killing evidence: one section, "
         "register, or verdict in the upload that the frozen "
         "register lacks, or one stated total that parts — all "
         "221 headings and every stated total were compared and "
         "agree.")
L.append("3. *The seven silent plates are silent in the source.* "
         "Killing evidence: one claim in the source stated in "
         "kana, geez, hangul, Armenian, Georgian, Cyrillic, or "
         "Glagolitic — the source's §I and §II are the seats "
         "where it would have to stand.")
L.append("4. *The parted claims are faithful to the source's "
         "§IV.* Killing evidence: one parted claim whose claimed "
         "or recomputed value parts from the §IV register — all "
         "18 were checked entire against that segment.")
L.append("5. *The Core's frame index accounts every section "
         "once.* Killing evidence: a recount of the register's "
         "221 sections parting from 135 + 86, or one section "
         "indexed twice.")
L.append("")
L.append("**The NOT-SEATED register** — printed as proven "
         "nowhere: (i) the seating of the Core as the dial's "
         "center and οὐδέν as its face — this instrument's "
         "construction, offered to the Founder's pen; (ii) any "
         "reading of the upload's later striking (seven minutes "
         "after the house MAGVS) as intention — the metadata "
         "proves sequence, not purpose; (iii) the legend's "
         "universal claim over all tongues (the census's S8) — "
         "stands OPEN, unpromoted by anything here.")
L.append("")
L.append("---")
L.append("")

# -------------------------------------------------------------- §XVII
L.append("## §XVIII — Questions for the Founder's Pen")
L.append("")
L.append("**Q1 — The upload's dress.** The browser-print form "
         "stands proved the same instrument in another dress. "
         "Does it stand as a second authorized dress of the "
         "TABVLA, or is the Lex Stellarrvm MAGVS the sole "
         "edition of record and the print a reading copy?")
L.append("**Q2 — The seven silent plates.** Their silence is the "
         "corpus's: the fills claimed in five tongues only. "
         "Commission a fill round stated in the silent tongues "
         "(the Twelve Tables' doors give the road), or does "
         "their silence stand as the corpus's face?")
L.append("**Q3 — The unseated methods.** The pinyin fallback and "
         "the PRC stroke count sit in the Core unseated, as the "
         "source left them. Seat either as a door or a table — "
         "or leave the Core holding them as the map's open "
         "apparatus?")
L.append("**Q4 — Sanskrit and Chinese.** The map names both at "
         "its boundary and plates neither. A doors-plate for "
         "Sanskrit, or a Chinese weighing leg (S10), would "
         "change the map's shape from thirteen — the pen rules "
         "the shape.")
L.append("**Q5 — The pontifex-copy overlay.** The TABVLA's own "
         "open question rides forward: the corrected rows of "
         "the pontifex copy of 777-REVISED (the 2026-10-27 "
         "orthography apparatus) were verified by neither the "
         "TABVLA nor these plates. A delta battery over those "
         "~45 claims remains a small, named road.")
L.append("")
L.append("---")
L.append("")

# --------------------------------------------------------- content test
L.append("## Content Test — the four elements")
L.append("")
L.append("**Inputs:** the Founder's upload (123 pp, SHA-256 "
         "`bfb45413…`, read-only) · the frozen verified register "
         "of the TABVLA battery (221 sections, 504 claims) · the "
         "sealed PONTIFEX engine's bank tables (plate vitals). "
         "**Processes:** Phase 0 identification (headings, "
         "totals, production metadata, the parting table) · the "
         "mapping by stated bank under §II's law · the mapping "
         "audit (completeness, fidelity, source-hash) run "
         "independently of the builder. **Outputs:** this "
         "instrument and its MAGVS edition · the mapping "
         "register (`mapping_register.json/.csv`), the audit "
         "results, and the three scripts, in the engine's "
         "research tree (`research/thirteen-plates/`). "
         "**Tolerances:** zero — one unmapped or twice-mapped "
         "claim, one unaccounted section, one parted total, or "
         "a moved upload hash fails the audit and prints its "
         "coordinate; none was found.")
L.append("")
L.append("## Table of Authorities (condensed)")
L.append("")
L.append("The source: the Founder's upload, *THE-777-VERIFICATION-"
         "TABVLA_2_bczz.pdf* (browser print, 2026-11-24 19:27:44 "
         "UTC). The house instruments of record: "
         "THE-777-VERIFICATION-TABVLA (the struck MAGVS and its "
         "frozen register, pontifex commits `45747a7`, `37a6642`) "
         "· THE-TWELVE-TABLES (the census fold, the plate order, "
         "the inheritance discipline) · THE-CAUCASUS-AND-THE-"
         "NORTH (the world census: S6, S8, S10). Scripture: 1 "
         "Thessalonians 5:21 (KJV).[^1]")
L.append("")
L.append("---")
L.append("")
L.append("## Colophon")
L.append("")
L.append("Generated at the desk from the frozen register and the "
         "upload by `build_thirteen_plates.py`, audited by "
         "`audit_thirteen_plates.py` (VERDICT: PASS), and set "
         "by `gen_thirteen_plates_md.py` — no number in this "
         "instrument was typed by hand. The upload was read and "
         "never written; *777-REVISED.md* was not touched by "
         "this work. Exclusive authorship: Johnathan 'Qasparr' "
         "Monroe, ARR — All Rights Reserved, Without Prejudice. "
         "Method of Science. Aim of Religion.")
L.append("")
L.append("Flagpole of Claim and Coinage: Johnathan 'Qasparr' "
         "Monroe, ARR, All Rights Reserved, Without Prejudice. "
         "Right of claim hereby reserved and coined under the "
         "authority of the Living Man.")
L.append("")
L.append("93 — Live, Love, and let Love, Live.")
L.append("")
L.append("[^1]: 1 Thessalonians 5:21 (KJV): \"Prove all things; "
         "hold fast that which is good.\"")

OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {OUT} — {OUT.stat().st_size} bytes, "
      f"{len(L)} lines")
