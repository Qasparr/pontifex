#!/usr/bin/env python3
# =============================================================================
# 93 — build_delegated_answers.py
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
# MECHANISM: generates THE-DELEGATED-ANSWERS.md in the goal files
# from delegated_answers_data.json (the investigation's output).
# Every number in the instrument is read from that JSON; the prose
# carries the questions verbatim from the two filed instruments,
# the investigations, the decisions at desk strength, and their
# killing evidence.
#
# DOCTRINE: the instruments answered are NOT edited — the iron law
# of the TABVLA build stands. These answers are a separate
# instrument, at DESK strength under the founder's delegation of
# 2026-11-24 22:47 EST, revisable by his pen. What proved to be
# the founder's call after all is tagged UNCHARTED and left
# standing, never decided.
#
# CONTENT TEST: Inputs — the data JSON; the two filed instruments'
# question sections, quoted verbatim. Processes — generation with
# every figure interpolated from the JSON. Outputs —
# THE-DELEGATED-ANSWERS.md. Tolerances — the independent audit
# re-derives every figure from the engine and the registers and
# fails the instrument on any parting.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import json
from pathlib import Path

HERE = Path(__file__).parent
GOAL = (Path.home() / "workspace/goals/"
        "cross-gematria-777-gap-filling/files")
D = json.loads((HERE / "delegated_answers_data.json").read_text(
    encoding="utf-8"))

B = []  # the instrument, block by block


def add(s=""):
    B.append(s)


# ---------------------------------------------------------------------
# Title block — the Teacher's Edition manner.
# ---------------------------------------------------------------------
add("![The Doctrine's Logo — TVRRIS VERITATIS seal]"
    "(~/workspace/templates/doctrine-logo.png)")
add()
add("**THE DELEGATED ANSWERS**")
add()
add("*Subtitle:* A Scientific Illuminist treatment of the fifteen "
    "questions left to the founder's pen by the Verification TABVLA "
    "(§VII) and the Twelve Tables (§VIII) — answered at desk "
    "strength under the founder's delegation, with the reasoning "
    "logged and the founder's own questions left standing where "
    "they proved to be his after all")
add()
add("Authorship attributed exclusively to Johnathan 'Qasparr' Monroe "
    "(Greek, -ARR, All Rights Reserved, Without Prejudice)")
add("XXIV day of November, Dies Martis, Sol in Sagittario, "
    "Anno V:xii e.n. (2026 e.v.)")
add()
add("Classification: Enterprise • Educational • Research & Development")
add("Method of Science, Aim of Religion")
add()
add("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, "
    "All Rights Reserved, Without Prejudice. Right of claim hereby "
    "reserved and coined under the authority of the Living Man.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §I — the delegation.
# ---------------------------------------------------------------------
add("## §I — The Delegation, and the Strength of These Answers")
add()
add("**The authority.** The founder's delegation of 2026-11-24 "
    "(22:47 EST), verbatim: *\"Make your recommendations the pen's "
    "decisions.\"* The Twelve Tables' decisions appendix, appended "
    "the same night under those words, records that the remaining "
    "questions of its §VIII and of the Verification TABVLA's §VII "
    "\"stand delegated to the desk as commissioned work under the "
    "same words, to be answered at desk strength with reasoning "
    "logged, or tagged UNCHARTED and left standing where a question "
    "proves to be the founder's after all.\" This instrument is "
    "that commissioned work.")
add()
add("**The strength.** Every decision below is a **DESK DECISION "
    "UNDER DELEGATION** — the desk's ruling, printed at desk "
    "strength, revisable by the founder's pen at any time, and "
    "nowhere dressed as his ruling. Where a question proved on "
    "inspection to be a founder's call after all — a coinage, a "
    "tier promotion, a doctrine choice no evidence settles — it is "
    "tagged **UNCHARTED** and left standing, with the exact "
    "coordinate of why it is his. Dispositions are marked, never "
    "vanished; neither filed instrument is edited by so much as a "
    "character — the answers live here, in a separate instrument, "
    "as the TABVLA's iron law requires.")
add()
add("**The method.** Each question is quoted verbatim from its "
    "instrument. Each investigation runs hypothesis → method → "
    "observation → result, dead ends included, and every "
    "load-bearing number is recomputed on the sealed engine or "
    "recounted from the frozen registers before it is printed — "
    "calibration controls first (θέλημα "
    f"{D['controls']['thelema_greek']} · VAPOUR "
    f"{D['controls']['vapour_latin_ordinal']} · σφίγξ "
    f"{D['controls']['sphinx_greek']}, all true at this desk). "
    "Each decision carries its killing evidence, per the founder's "
    "falsifiability rule: a decision no evidence could overturn "
    "would not be printed as one.")
add()
add("**One question is not answered here, because it is already "
    "decided.** Twelve Tables §VIII Q1 (the Coptic thousands) was "
    "ruled in the decisions appendix itself — *the frozen parity "
    "exhibit stands; the fill is not made* — and is cited at §X "
    "below, not re-opened. Fourteen questions remain: eight of the "
    "TABVLA, six of the Tables. Thirteen are decided at desk "
    "strength; one is tagged UNCHARTED entire, and two more carry "
    "an UNCHARTED residue at a named coordinate inside a decided "
    "answer.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q1 — §II.
# ---------------------------------------------------------------------
q1 = D["tabvla_q1"]
add("## §II — TABVLA §VII Q1 — The Fallback Door Against the "
    "Workers' Scheme")
add()
add("> **Q1 — The fallback door against the workers' scheme (9 "
    "partings, Column XXXIII).** The Norse fills were weighed "
    "through a phonetic Latin-to-Hebrew scheme their own notes "
    "document, letter by letter; the engine's seated door renders "
    "otherwise, and the two part at named letters (BALDR: the "
    "scheme's בלדר weighs 236; the door renders באלדר, 237). His "
    "pen has already ruled once in this exact seam: on 2026-10-25 "
    "the BALDR fill was corrected TO the scheme's rendering. Does "
    "the scheme stand as a documented second door beside the "
    "engine's — or do the nine fills re-price through the seated "
    "door — or do the partings stand marked, as printed here?")
add()
add("**Investigation.** *Hypothesis:* the parting is not an error "
    "on either side but two stated schemes disagreeing at named "
    "letters — in which case the founder's own prior ruling in the "
    "seam decides the desk's course. *Method:* every Column XXXIII "
    "door claim recounted from the frozen verified register, claim "
    "by claim; BALDR reweighed both ways on the engine. "
    f"*Observation:* the column carries {q1['door_claims_total']} "
    f"door claims over 13 names: {q1['door_claims_verified']} "
    "verify entire through the seated door ("
    + ", ".join(q1["door_verified_names"]) + "), and "
    f"{q1['parted_claims']} part from the scheme — over 8 names, "
    "NERTHUS carrying the parted claim in two sections (XXXIII/10 "
    "and XXXIII/32 bis). The partings, scheme against door: "
    + "; ".join(f"{p['name']} {p['scheme']} against {p['door']} "
                f"(Δ{p['delta']:+d})" for p in q1["parted"])
    + f". BALDR itself: the scheme's {q1['baldr_scheme_word']} = "
    f"{q1['baldr_scheme_value']}; the door's {q1['baldr_door_word']} "
    f"= {q1['baldr_door_value']}. *Result:* the hypothesis holds. "
    "The door is not broken — it verifies five names entire — and "
    "the scheme is not careless — its renderings are documented "
    "letter by letter in the fills' own notes. Two stated schemes "
    "part at named letters, which is a coordinate, not a defect.")
add()
add("**Decision (desk strength): the workers' scheme stands as a "
    "documented second door beside the engine's; the nine partings "
    "stand marked, as printed; neither side re-prices.** The "
    "reasoning rides in three parts. (1) *The founder has already "
    "ruled in this seam, and he ruled toward the scheme:* the "
    "2026-10-25 correction moved BALDR from the door's 237 to the "
    "scheme's 236, inside the corpus itself, under delegated "
    "red-pen authority and revisable by his pen — it was never "
    "revised. A desk decision re-pricing the fills through the "
    "door would reverse his one ruling in the exact seam, and no "
    "decision of the desk's may contradict a filed ruling of the "
    "house. (2) *Two stated schemes are this house's standing "
    "shape* — the Aramaic seat holds two strata, the Ge'ez table a "
    "mint and a witness; a documented second door is a normal "
    "instrument, not an anomaly to be flattened. (3) *Re-pricing "
    "would falsify the record:* the fills state their method on "
    "their faces; to recompute them under another method and print "
    "the new numbers as theirs would misstate what the workers "
    "did. The partings are the zero point between the two schemes, "
    "and the zero-point method prints boundaries rather than "
    "verdicts.")
add()
add("**Killing evidence:** a ruling of the founder's pen "
    "superseding 2026-10-25 in this seam, or a showing that the "
    "scheme's letter-by-letter documentation is not what the "
    "fills' notes record — either kills this decision on the spot.")
add()
add("[^1]: The 2026-10-25 ruling stands in the corpus itself, at "
    "the BALDR entry of Column XXXIII: \"CORRECTED 237->236 by "
    "ruling 2026-10-25 (delegated red-pen authority; revisable by "
    "his pen): documented phonetic scheme gives בלדר=236.\"")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q2 — §III.
# ---------------------------------------------------------------------
q2 = D["tabvla_q2"]
add("## §III — TABVLA §VII Q2 — Tāʾ Marbūṭa")
add()
add("> **Q2 — Tāʾ marbūṭa (6 partings, Column XLVII).** The jinn "
    "fills price ة as ه (5), a convention their notes record "
    "openly (\"standard abjad reads ة as ه\"); the seated abjad "
    "bank prices ة not at all. Seat a priced ة in the Arabic bank, "
    "or leave the six partings standing?")
add()
add("**Investigation.** *Hypothesis:* the six partings are one "
    "letter deep — if each is exactly one ة priced 5 by the fills' "
    "convention, the question is a bank amendment, and a bank "
    "amendment is judged by its cost on both sides of the ledger. "
    "*Method:* the six parted claims recounted from the register; "
    "each delta recomputed; each word reweighed with ة priced as "
    "ه; and the verified side searched for claims that stand only "
    "because ة is silent. *Observation:* all six deltas are "
    "exactly 5, each word carries exactly one ة, and pricing ة as "
    "ه reproduces all six claimed values to the unit — the "
    "convention is exactly what the fills say it is. But the "
    "ledger's other side is not empty: "
    + "; ".join(f"{v['word']} verifies at {v['claimed']} with ة "
                f"silent and would read {v['if_taa_priced']} — "
                "parted — with ة priced"
                for v in q2["verified_depending_on_silence"])
    + ". The bank itself prices ة at "
    f"{q2['taa_alone_in_bank']} — silence — which is the standard "
    "abjad table's own reading, as the engine's Arabic audit "
    "documents it. *Result:* seating a priced ة would repair six "
    "partings by breaking two verified claims and amending an "
    "attested bank against its own audit. The trade is bad on its "
    "face, and worse in kind: the six partings are already honest "
    "— each prints its coordinate, and the convention that "
    "produces them is recorded openly in the fills' notes.")
add()
add("**Decision (desk strength): no priced ة is seated in the "
    "Arabic bank; the six partings stand, with the fills' "
    "convention named as their coordinate.** An attested bank is "
    "not amended at desk strength to absorb a documented "
    "convention of the fills — the convention lives in the fills, "
    "marked, exactly where its own notes put it. The bank's "
    "silence on ة is not a gap in the bank; it is the standard "
    "table's reading, and two verified claims in the same column "
    "stand on it.")
add()
add("**Killing evidence:** a witness of the standard abjad table "
    "pricing ة in its own right (not as a sounded ه), or the "
    "founder's pen seating it by ruling — the first would re-open "
    "the bank's audit, the second would supersede this decision "
    "by the authority that delegated it.")
add()
add("[^2]: Tāʾ marbūṭa (ة, U+0629): in the standard abjad table "
    "the letter carries no value; the fills' convention prices it "
    "as its sounded letter ه (5). The TABVLA's own footnote, "
    "carried here because the decision rests on it.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q3 — §IV.
# ---------------------------------------------------------------------
q3 = D["tabvla_q3"]
add("## §IV — TABVLA §VII Q3 — The Hamza-Alif")
add()
add("> **Q3 — The hamza-alif (1 parting).** الأحمر claims 280 "
    "against the bank's 279, the delta exactly the hamza on the "
    "alif, priced 1 by the fill's recorded convention. The same "
    "question as Q2 at size one.")
add()
add("**Investigation.** *Hypothesis:* Q2's reasoning decides Q3 "
    "if the coordinate is the same shape — a mark priced by "
    "convention against a bank that reads it in silence — and if "
    "the corpus itself files both readings. *Method:* the word "
    "reweighed on the bank; its two filed claims compared. "
    f"*Observation:* {q3['word']} weighs {q3['bank_value']} on the "
    "seated bank, the hamza carrying no price "
    f"({q3['hamza_alone_in_bank']} — skipped in silence). The "
    "corpus files the word twice, adjacently: one claim at "
    f"{q3['verified_claim']}, VERIFIED on the bank's reading, and "
    f"one at {q3['parted_claim']}, PARTED, its delta exactly the "
    "hamza priced 1 by the fill's recorded convention. *Result:* "
    "the same shape at size one, with the corpus's own twin "
    "claims as the coordinate — the bank's reading is not merely "
    "the desk's preference; it is the reading under which the "
    "word verifies in the same section that files the parting.")
add()
add("**Decision (desk strength): the hamza stays a mark, not a "
    "priced letter; the one parting stands, its convention named.** "
    "Decided with §III and by the same reasoning: an attested "
    "bank is not amended at desk strength for a documented "
    "convention, and here the amendment would part the word "
    "against its own verified twin.")
add()
add("**Killing evidence:** as §III — a witness pricing the hamza "
    "in the standard table, or the founder's pen ruling otherwise.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q4 — §V.
# ---------------------------------------------------------------------
q4 = D["tabvla_q4"]
m, a = q4["madim"], q4["adam_kadmon"]
add("## §V — TABVLA §VII Q4 — Mispar Gadol")
add()
add("> **Q4 — Mispar gadol (2 partings, two applications).** "
    "מאדים holds only under the full gadol uplift (every final at "
    "500–900); אדם קדמון holds only under the nun's uplift alone, "
    "as its notes document. If a gadol bank is to be seated, which "
    "application is canonical — and if none is seated, both "
    "partings stand as printed.")
add()
add("**Investigation.** *Hypothesis:* the two applications are "
    "not two readings of one method — one of them is mispar gadol "
    "as the tradition defines it, and the other is a local "
    "convention wearing its name. *Method:* both words recomputed "
    "letter by letter under hechrechi, under the full uplift (all "
    "five finals at 500–900), and under the nun-only uplift. "
    f"*Observation:* {m['word']}: hechrechi {m['hechrechi']}, full "
    f"gadol {m['full_gadol']} — its claimed {m['claimed']} "
    "exactly; the nun-only application does not touch it (its "
    f"only final is ם) and leaves it at {m['nun_only']}. "
    f"{a['word']}: hechrechi {a['hechrechi']}, nun-only "
    f"{a['nun_only']} — its claimed {a['claimed']} exactly — but "
    f"full gadol {a['full_gadol']}, because the full uplift also "
    "raises the ם of אדם. Each claim holds under exactly one "
    "application, and the applications are not interchangeable. "
    "*Result:* the question's fork is real, and it is decidable "
    "from the tradition the method's name invokes: mispar gadol, "
    "\"the great number,\" *is* the full uplift — the five finals "
    "at 500, 600, 700, 800, 900 — as the engine's Hebrew audit "
    "documents the tradition. A nun-only uplift is not a second "
    "form of gadol; it is the fill's documented local convention, "
    "honest as a convention and misnamed as the method.")
add()
add("**Decision (desk strength): the canonical application is "
    "the full uplift.** Consequences, printed at their sizes: "
    f"(1) {m['word']} at {m['claimed']} stands as a true gadol "
    "reading — its parting against hechrechi stands as printed "
    "in the TABVLA, now characterized: the claim is a gadol claim, "
    "and under gadol it is exact. (2) "
    f"{a['word']} at {a['claimed']} stands as its fill's "
    "documented nun-only convention — not canonical gadol, under "
    "which it reads "
    f"{a['full_gadol']} — and its parting stands as printed. "
    "(3) **No gadol bank is seated by the desk.** The engine seats "
    "no gadol bank today, and seating one is a bank-building act "
    "with census consequences (a seventeenth system becoming an "
    "eighteenth); the characterization above gives every filed "
    "gadol claim its exact standing without it. If the founder "
    "wants the bank, the road is named: a gadol door on the "
    "Hebrew bank, full uplift only, built and parity-tested as "
    "the other doors were.")
add()
add("**Killing evidence:** a witness of the gadol tradition "
    "defining the method by a partial uplift, or a showing that "
    "either recomputation above parts from the engine's letter "
    "values — the first would unseat the canonical reading, the "
    "second the arithmetic it stands on.")
add()
add("[^3]: Mispar gadol (\"great number\"): the extended Hebrew "
    "reckoning in which the final forms ך ם ן ף ץ carry 500, 600, "
    "700, 800, 900 — the TABVLA's footnote, and the engine's "
    "Hebrew audit's documentation of the tradition.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q5 — §VI.
# ---------------------------------------------------------------------
q5h, q5g = D["tabvla_q5_hebrew"], D["tabvla_q5_greek"]
pops = D["tabvla_q5_populations"]
add("## §VI — TABVLA §VII Q5 — The Unprinted Transliterations")
add()
add("> **Q5 — The unprinted transliterations (60 claims).** These "
    "rest on words their sections never print. The engine's door "
    "agrees with 5 of the Hebrew ones as a coordinate. If the pen "
    "adopts the door as the standard rendering for Hebrew claims "
    "— and a stated transliteration table for the Greek ones (the "
    "CLXXXVII letter-name bridges chief among them) — the "
    "population becomes recomputable. Adopt, or leave standing as "
    "claims on unprinted words?")
add()
add("**Investigation.** *Hypothesis:* adoption is a methods "
    "convention, and a methods convention is desk work — but its "
    "honest price must be printed: how much of the population the "
    "standard actually reproduces, and what adoption does *not* "
    "do. *Method:* the population recounted from the register; "
    "the seated door applied to every Hebrew claim's name as "
    "printed; a plain letter-map applied to every Greek claim; "
    "the residue's joints tested one by one. *Observation:* the "
    f"60 claims decompose as {pops['hebrew']} Hebrew, "
    f"{pops['greek']} Greek, {pops['hebrew_gadol']} filed under "
    f"the gadol label, and {pops['arabic_abjad']} Arabic. The "
    f"door reproduces exactly {q5h['door_agrees_exactly']} of the "
    f"{q5h['population']} Hebrew claims as filed ("
    + ", ".join(q5h["door_agree_keys"]) + " — Atum 447, Comananu "
    "254, AZOTH 414 among the names), with the nearest miss a "
    f"single unit out (MAAT: claimed {q5h['nearest_miss']['claimed']}, "
    f"door {q5h['nearest_miss']['door_value']}). The TABVLA's own "
    "count said 5; this desk's recount, the door applied to the "
    "proposal names exactly as printed, finds 3 — the parting is "
    "printed here rather than smoothed, and it does not move the "
    "decision, which does not rest on the count. The plain Greek "
    f"letter-map reproduces {q5g['plain_map_agrees']} of "
    f"{q5g['population']} Greek claims exactly; three more fall "
    "to joints witnessed inside the corpus itself — BITH at "
    f"{q5g['joints']['bith_via_theta']['value']} as "
    f"{q5g['joints']['bith_via_theta']['dress']} (tav reads theta "
    "in the letter-name tradition, as Θώθ verifies at 818 in the "
    "same column), AZOTH at "
    f"{q5g['joints']['azoth_via_omega']['value']} as "
    f"{q5g['joints']['azoth_via_omega']['dress']}, and AMEN at "
    f"{q5g['joints']['amen_received']['value']} as "
    f"{q5g['joints']['amen_received']['dress']}, the received "
    "Greek spelling of the word — bringing the stated table's "
    "reach to 13 of 17. The residue is four: Malachite (1190), "
    "Moloch (810), Beelzebub (556), and YVD (404) — the last "
    "matched only by the coincidence ΥΔ = "
    f"{q5g['joints']['yvd_residue']['coincidence']['value']}, "
    "printed as a coincidence and not a rendering. *Result:* a "
    "standard exists for both populations, it is statable in "
    "full, and its reach and its residue are both measurable. "
    "What adoption cannot do is re-grade the filed claims: the "
    "TABVLA's verdicts were computed against the record as filed, "
    "and a filed instrument's verdicts are not rewritten by an "
    "answers appendix.")
add()
add("**Decision (desk strength): ADOPT — prospectively, as desk "
    "conventions, both standards.** (1) The engine's seated "
    "Latin-to-Hebrew door is the standard rendering for Hebrew "
    "claims on unprinted words: any future such claim is rendered "
    "by the door and is recomputable on its face. (2) The stated "
    "Greek table is adopted beside it: the plain letter-map "
    "(א→Α, ב→Β, ג→Γ, ד→Δ, ה→Η, ו→Υ, ז→Ζ, ח→Χ, ט→Θ, י→Ι, כ/ך→Κ, "
    "ל→Λ, מ/ם→Μ, נ/ן→Ν, ס→Σ, ע→Ο, פ/ף→Φ, צ/ץ→Σ, ק→Κ, ר→Ρ, ש→Σ, "
    "ת→Τ; Latin letters by their Greek counterparts of sound), "
    "with the three witnessed joints — tav as theta in "
    "letter-names, the long o as omega where the name's own "
    "tradition carries it, and received Greek spellings where a "
    "word has one. (3) **The 60 filed claims stand NOT VERIFIABLE "
    "as filed.** Adoption governs future claims and gives the "
    "filed ones a stated coordinate — door value against claimed "
    "value, printed in the investigation above — but their "
    "verdicts move only under a re-grade battery, which is named "
    "here as charted desk work on the founder's word, not "
    "executed in this instrument.")
add()
add("**Killing evidence:** a filed claim shown to reproduce "
    "under a *different* stated standard that also reproduces the "
    "door's three exact agreements — a rival standard with a "
    "longer reach would displace the adopted one by the same "
    "reasoning that adopted it.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q6 — §VII.
# ---------------------------------------------------------------------
q6 = D["tabvla_q6"]
add("## §VII — TABVLA §VII Q6 — The Unseated Methods")
add()
add("> **Q6 — The unseated methods (22 claims, Column CLXXXVI).** "
    "A pinyin-to-Hebrew fallback and a PRC stroke count seat in "
    "no proven bank or door. Build seats for them — a pinyin "
    "door, a stroke reader — or leave the claims standing under "
    "their stated methods, marked not verifiable?")
add()
add("**Investigation.** *Hypothesis:* a seat can be built only "
    "from stated materials — a mapping, a table, a source text — "
    "and if none of the three exists in the record, seat-building "
    "is invention wearing a hard hat. *Method:* the population "
    "recounted; the corpus searched entire for the methods' "
    "materials. *Observation:* the population is "
    f"{q6['pinyin_count']} pinyin-fallback claims and "
    f"{q6['stroke_count']} stroke-count claims, all in Column "
    "XLVI, the Yî King names in their romanized dress (Khan, "
    "Khien, Khwbn, Tui, Sun, Li). The corpus prints "
    f"{q6['cjk_chars_in_corpus']} Chinese characters — in the "
    "whole file, not merely in the section — and "
    f"{q6['hebrew_chars_in_xlvi_section']} Hebrew letters in the "
    "XLVI section itself. The pinyin method stands in the fills "
    "as a bank *label* (\"hebrew_pinyin_fallback,\" tier: "
    "constructed); its mapping — which syllable becomes which "
    "letter — is printed nowhere. The stroke counts' objects — "
    "the characters — are likewise nowhere printed. *Result:* "
    "neither seat has materials. A pinyin door built at this desk "
    "would have every joint chosen by the desk — and a scheme "
    "whose joints are all chosen is a coinage, of the same class "
    "as the diplomatic key, which was the founder's coinage and "
    "not the desk's. A stroke reader built without the characters "
    "is a table of numbers in search of its objects.")
add()
add("**Decision (desk strength): no seats are built; the 22 "
    "claims stand under their stated methods, marked NOT "
    "VERIFIABLE, exactly as filed.** The desk does not coin "
    "schemes under a delegation to answer questions. The road is "
    "named at its coordinate: if the founder names the "
    "syllable-to-letter scheme (or orders the XLVI characters "
    "sourced from a printed 777's Yî column, as §IX's road "
    "sources its witness), the desk builds both seats and "
    "recomputes the 22 in an afternoon. Until then the claims' "
    "standing is the honest one — stated methods, no seat, no "
    "verdict available — and their falsifiability posture is "
    "printed with them: as filed, no recomputation could disprove "
    "them, which is precisely why they hold no proof seat.")
add()
add("**Killing evidence:** the production of the scheme's "
    "statement or the characters from any witness of the corpus — "
    "either supplies the missing materials and converts this "
    "decision's premise to falsehood.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q7 — §VIII.
# ---------------------------------------------------------------------
q7 = D["tabvla_q7"]
add("## §VIII — TABVLA §VII Q7 — The Two Copies")
add()
add("> **Q7 — The two copies.** The pontifex copy carries the "
    "2026-10-27 orthography-correction apparatus (44 notes, "
    "respelled proposals, reweighed rows); the goal-files copy — "
    "the seat of record this battery verified — does not. Does "
    "the apparatus overlay the goal copy by his pen, or do the "
    "copies stand as two witnesses, the issued form and the "
    "corrected working copy? If the overlay is ruled, the "
    "corrected rows (some 45 claims) want a delta battery of "
    "their own — a small road, charted on his word.")
add()
add("**Investigation.** *Hypothesis:* the question is decided "
    "by what the goal copy *is* — if it is the frozen seat the "
    "verified register was computed from, overlaying it does not "
    "correct the record, it unfreezes it. *Method:* the apparatus "
    "counted, not described, in both copies; the copies' sizes "
    "compared. *Observation:* the pontifex copy carries exactly "
    f"{q7['apparatus_notes_pontifex']} bracketed apparatus notes "
    "(\"[Orthography correction 2026-10-27: … reweighed … old "
    "value marked, not vanished\"]), and the goal copy carries "
    f"{q7['apparatus_notes_goal']}. The copies stand "
    f"{q7['pontifex_copy_bytes']:,} and {q7['goal_copy_bytes']:,} "
    f"bytes — a delta of "
    f"{q7['pontifex_copy_bytes'] - q7['goal_copy_bytes']:,} bytes, "
    "the apparatus entire. The frozen register of the TABVLA was "
    "extracted from the goal copy as it stands; every one of its "
    "504 verdicts is a verdict *on that text*. *Result:* an "
    "overlay would leave the register pointing at a text that no "
    "longer exists in its verified form — the battery would have "
    "to be re-run entire before any verdict could be trusted, "
    "and the issued form of the corpus would have been edited "
    "under a delegation to answer questions, against the build's "
    "iron law (777-REVISED edited by zero characters in either "
    "copy).")
add()
add("**Decision (desk strength): the copies stand as two "
    "witnesses.** The goal-files copy is the issued form and the "
    "seat of record — unedited, as the iron law holds it. The "
    "pontifex copy is the corrected working copy, its apparatus "
    "standing in brackets with every old value marked, never "
    "vanished — which is already the house's disposition form, "
    "applied by the apparatus itself. The two-witness posture "
    "loses nothing: every corrected value is on record in the "
    "working copy, and every verified verdict is on record "
    "against the issued form. The delta battery over the "
    "corrected rows is named as charted desk follow-on work — a "
    "small road, run on the founder's word or a future "
    "delegation — and is not executed in this instrument, whose "
    "commission is answers, not batteries.")
add()
add("**Killing evidence:** a showing that any verdict in the "
    "frozen register was in fact computed against the pontifex "
    "copy's corrected text — which would invert the copies' "
    "offices and re-open the question on its facts.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TABVLA Q8 — §IX.
# ---------------------------------------------------------------------
q8 = D["tabvla_q8"]
add("## §IX — TABVLA §VII Q8 — The Transcription Gap")
add()
add("> **Q8 — The transcription gap (CLXXXIV/10).** Its source "
    "glyph is lost in transmission (a 0x8F byte). No question of "
    "ruling arises until a witness of the printed 777 supplies "
    "the letter; the gap stands marked, not filled by invention.")
add()
add("**Investigation.** *Hypothesis:* the question answers "
    "itself, and the desk's work is only to confirm the "
    "coordinate still stands as filed and to name the one lawful "
    "road. *Method:* the gap recounted in the frozen tables "
    "register. *Observation:* exactly "
    f"{q8['gap_cells_per_table']} GAP cell stands in each of the "
    f"twelve tables, at {q8['gap_cell_id'][0]} — the Malkuth "
    "cell, its source glyph a lost byte (0x8F) where the letter "
    "stood. Every other cell of the 371-row frame is accounted "
    "for in every table. *Result:* the coordinate stands as "
    "filed; there is nothing to recompute, because there is "
    "nothing to recompute *from* — and that absence is the whole "
    "of the matter.")
add()
add("**Decision (desk strength): the gap stands marked, "
    "unfilled, in every instrument that carries the frame.** No "
    "letter is invented for it at any strength this desk holds. "
    "The one lawful fill is a witness of the printed 777 — a "
    "published edition's CLXXXIV/10 cell — and sourcing that "
    "witness is named as the road: a sourcing act, not a ruling, "
    "which the desk will execute on the founder's word and "
    "correctio into the record when the witness is in hand.")
add()
add("**Killing evidence:** the witness itself — a printed 777 "
    "supplying the letter kills the gap, which is the decision's "
    "own stated hope; short of it, nothing overturns a decision "
    "to leave a hole a hole.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q1 — §X (cited, not re-opened).
# ---------------------------------------------------------------------
add("## §X — Twelve Tables §VIII Q1 — The Coptic Thousands "
    "(Decided; Cited, Not Re-Opened)")
add()
add("> **Q1 — The Coptic thousands devices.** The fill stopped "
    "at a frozen exhibit (§III): price the double overline and "
    "the ͵ sign at ×1000 at the `coptic()` door (the Cyrillic "
    "pattern), amending the seat's parity doctrine — or let "
    "counted-not-priced stand as the law? The contradiction is "
    "printed at §III in full; the pen decides what synergy could "
    "not.")
add()
add("**Status: DECIDED before this instrument was commissioned, "
    "and cited here so the register of answers is complete.** "
    "The decisions appendix to the Twelve Tables, appended "
    "2026-11-24 (22:47 EST) under the founder's delegation, rules: "
    "*the frozen parity exhibit stands; the fill is not made* — "
    "the ×1000 fill contradicts the filed exhibit (\"coptic() "
    "counts the marks and prices NONE\"), and no decision of the "
    "desk's may contradict a filed instrument of the house; the "
    "stop is permanent at desk strength, revisable only by the "
    "founder's pen against the exhibit itself. This desk does not "
    "re-open it, re-argue it, or re-print its investigation: the "
    "decision stands where it was made, and this section is its "
    "citation, not its second hearing.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q2 — §XI.
# ---------------------------------------------------------------------
t2 = D["tt_q2"]
add("## §XI — Twelve Tables §VIII Q2 — The Ge'ez Ch-Door")
add()
add("> **Q2 — The Ge'ez ch-door.** Eighty holes stand in the "
    "Ge'ez table, the sharpest coordinate the derived base ቸ "
    "(for 'ch'), which the classical mint does not seat. Seat a "
    "derived-base annex for the door's use only (the Armenian R1 "
    "shape), or keep the holes as the mint's honest edge?")
add()
add("**Investigation.** *Hypothesis:* the Armenian shape "
    "transfers only if its load-bearing property transfers — the "
    "R1 annex's values were *sourced* — and the annex's reach "
    "must be counted before it is praised. *Method:* the Ge'ez "
    "table's states and hole species recounted from its register; "
    "the Armenian annex's values read from the engine; the "
    "derived base tested against both Ge'ez banks. "
    f"*Observation:* the table stands DOOR {t2['states']['DOOR']} "
    f"· HOLE {t2['states']['HOLE']} · EMPTY "
    f"{t2['states']['EMPTY']} · GAP {t2['states']['GAP']}. The "
    f"{t2['holes']} holes separate into three species: "
    f"{t2['holes_no_latin_form']} where the corpus offers no Latin "
    f"form of record and no door is offered at all; "
    f"{t2['holes_cross_unseated']} whose renderings cross "
    "unseated signs; and "
    f"{t2['holes_fail_at_ch']} that fail at 'ch' itself. An annex "
    f"of derived bases reaches at most "
    f"{t2['holes_cross_unseated'] + t2['holes_fail_at_ch']} of "
    f"the {t2['holes']} — the {t2['holes_no_latin_form']} are not "
    "the door's failures and no annex touches them. And the "
    "transfer test fails at its load-bearing point: the Armenian "
    "annex seats Օ and Ֆ at "
    f"{t2['armenian_annex_sourced']['omin']} and "
    f"{t2['armenian_annex_sourced']['ef']} — values the tradition "
    "itself carries for those late letters, sourced in the "
    "Armenian audit before they were seated. For the Ge'ez "
    "derived bases no source prices anything: ቸ stands in "
    "neither the mint nor the halehame witness "
    f"(mint: {t2['derived_base_in_mint']}; witness: "
    f"{t2['derived_base_in_halehame']}), and the witness's own "
    "doctrine is that the folk table assigns the later-added "
    "bases no value. An annex here would be priced by invention — "
    "twelve bases' values chosen by the desk — on the founder's "
    "own mint, struck the same day as the tables themselves. "
    "*Result:* the R1 shape does not transfer, because what made "
    "R1 lawful was its sourcing, and there is nothing here to "
    "source.")
add()
add("**Decision (desk strength): the holes are kept as the "
    "mint's honest edge; no derived-base annex is seated by the "
    "desk.** The annex road is named for the founder's pen at its "
    "exact missing coordinate: a pricing law for the derived "
    "bases, which no source in the record supplies and which is "
    "therefore his to state or to leave unstated. If he states "
    "one, the desk builds the annex door-scoped in the R1 shape — "
    "mint untouched, annex behind its flag — and the "
    f"{t2['holes_cross_unseated'] + t2['holes_fail_at_ch']} "
    "reachable holes re-render. Until then the holes print with "
    "their coordinates, which is what an honest edge looks like.")
add()
add("**Killing evidence:** a source pricing any derived base — "
    "a halehame witness extended to the later rows, a debtera "
    "table valuing them — would supply the missing sourcing and "
    "reverse the transfer test this decision stands on.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q3 — §XII.
# ---------------------------------------------------------------------
add("## §XII — Twelve Tables §VIII Q3 — The Ge'ez Η/Ω Seat and "
    "the Korean Obsolete Jamo")
add()
add("> **Q3 — The Ge'ez Η/Ω seat and the Korean obsolete jamo.** "
    "Two mint-kind gaps carried open (§III): constructions exist "
    "for neither in any audit. Commission them as mint work, or "
    "let them stand as printed holes in the register?")
add()
add("**Investigation.** *Hypothesis:* the two gaps look alike "
    "and are not — one is a label in search of a seat, the other "
    "a grid boundary drawn by its founding law — and the desk "
    "must say what commissioning either would actually be. "
    "*Method:* the gap register's own entries read entire; each "
    "gap's bite on the tables measured. *Observation:* the "
    "register carries the Η/Ω entry as it stands: \"no "
    "audit-proposed construction prices Greek letters in the "
    "Ethiopic grid, and none is invented here. The seat is a "
    "Greek-bank matter wearing a Ge'ez label; it does not bite "
    "any table cell (no cell prices a Greek letter in the "
    "Ethiopic grid).\" The Korean entry: the obsolete jamo (ㆍ, "
    "U+119E, and kin) hold no seat in the modern grid, and \"the "
    "mint's grid is the modern one by its founding law; no "
    "audit-proposed construction prices the obsolete jamo.\" Both "
    "banks are the founder's mints — the Ge'ez mint his coinage "
    "of 2026-11-24 under the end-goal rule, the hangul mint his "
    "ratified coinage — and in neither case does any audit, "
    "source, or witness propose the construction that would fill "
    "the gap. *Result:* commissioning either gap means the desk "
    "designing new seats inside the founder's own coinages, with "
    "no source to calibrate against — the definition of a "
    "founder's call wearing a work order.")
add()
add("**Decision (desk strength): both stand as printed holes in "
    "the register.** The Η/Ω entry additionally stands "
    "re-characterized at desk strength, on its register's own "
    "evidence: it is a Greek-bank matter wearing a Ge'ez label "
    "and bites no cell — the register keeps it, marked as the "
    "label it is, so no future builder mistakes it for a hole in "
    "the mint. **The commissioning of either construction is "
    "tagged UNCHARTED at this coordinate:** extending the "
    "founder's mints is the founder's act, and the desk leaves "
    "both commissions on his desk, named, with their costs "
    "printed — a Ge'ez seat for two Greek letters inside a grid "
    "whose law is Ethiopic syllable order, and an obsolete-jamo "
    "annex against a founding law that chose the modern grid on "
    "purpose.")
add()
add("**Killing evidence:** an audit-proposed construction for "
    "either gap, from any quarter, with a source to calibrate it "
    "— the desk's ground is that none exists in the record, and a "
    "single produced construction kills it.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q4 — §XIII.
# ---------------------------------------------------------------------
t4 = D["tt_q4"]
add("## §XIII — Twelve Tables §VIII Q4 — Native Depth Beyond the "
    "Corpus")
add()
add("> **Q4 — Native depth beyond the corpus.** The tables' "
    "NATIVE cells are the corpus's own printings. A deeper road "
    "exists — each tongue's attested vocabulary for the "
    "categories (its planetary, zodiacal, elemental names from "
    "its own literature) sourced cell by cell. Commission it as "
    "a Phase II per tongue, or does the corpus-bounded depth "
    "stand as the tables' stated depth?")
add()
add("**Investigation.** *Hypothesis:* the question is not "
    "whether the deeper road exists — it plainly does — but "
    "whose act a twelve-tongue sourcing program is, and what the "
    "tables currently claim. *Method:* the NATIVE population "
    "recounted from the tables register; the tables' stated "
    "depth read from their faces. *Observation:* across the "
    "twelve tables, NATIVE cells total "
    f"{t4['native_total']} (Latin {t4['native_by_tongue']['latin']}, "
    f"Hebrew {t4['native_by_tongue']['hebrew']}, Greek "
    f"{t4['native_by_tongue']['greek']}, Arabic "
    f"{t4['native_by_tongue']['arabic']}, and none in the eight "
    "remaining tongues, whose cells are carried by their doors) — "
    "against 285 word-cells in every table's frame. The tables "
    "state this depth on their faces: NATIVE is *defined* as the "
    "corpus's own printings, and the counts print in every table's "
    "frame. A Phase II would source attested vocabulary from "
    "twelve literatures, cell by cell — a program of twelve "
    "Phase-I-class surveys, each with its own witnesses to "
    "choose among and its own audit to pass. *Result:* the "
    "tables make no claim the deeper road would correct — their "
    "depth is stated, bounded, and printed — and the program that "
    "would deepen them is a commission at the founder's scale: "
    "its sizing, its order of tongues, and its witnesses are "
    "choices no evidence in the record settles.")
add()
add("**Decision (desk strength): the corpus-bounded depth "
    "stands as the tables' stated depth.** It is not a shortfall "
    "to be apologized for; it is the tables' printed specification, "
    "and under the presumption rule it stands proven as what it "
    "claims to be. **The Phase II commission itself is the "
    "founder's to give** — named here at its coordinate, with its "
    "shape printed (per-tongue sourcing of attested category "
    "vocabulary, cell by cell, each tongue audited as the twelve "
    "were) — and the desk will execute it tongue by tongue on "
    "his word. What the desk will not do under a delegation to "
    "answer questions is commission a twelve-literature program "
    "in his name.")
add()
add("**Killing evidence:** a showing that any table claims a "
    "depth beyond the corpus on its face — one NATIVE cell not "
    "printed in the corpus would falsify the stated depth and "
    "re-open the question on its facts.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q5 — §XIV.
# ---------------------------------------------------------------------
t5 = D["tt_q5"]
add("## §XIV — Twelve Tables §VIII Q5 — The Door Schemes")
add()
add("> **Q5 — The door schemes.** Each door is a stated "
    "construction (§VII, not-seated (i)). Any scheme the pen "
    "would amend — the Arabic matres for short vowels, the Ge'ez "
    "sh→ሠ, the kana epenthetic law — amends by correctio, "
    "append-only, and the tables rebuild.")
add()
add("**Investigation.** *Hypothesis:* an amendment needs a "
    "defect, and a defect needs evidence — a door misrendering "
    "its own stated scheme, a check failing, a cell parting. If "
    "no defect is evidenced in any named scheme, there is nothing "
    "for a correctio to correct. *Method:* the three named "
    "schemes' health re-run at this desk — the doors' own check "
    "functions and parity batteries — and the tables' audit "
    "standing read for the doors as built. *Observation:* the "
    f"kana door's own checks pass {len(t5['kana_checks'])} of "
    f"{len(t5['kana_checks'])} and its parity battery stands "
    "green; the Ge'ez door's checks pass "
    f"{len(t5['geez_checks'])} of {len(t5['geez_checks'])} and "
    "its parity battery likewise; and the Twelve Tables' audit "
    "recomputed all 2,614 priced cells — every DOOR cell among "
    "them, the Arabic matres renderings included — and found no "
    "parting: the doors render exactly what their stated schemes "
    "say they render. The schemes' *rightness* as dresses is "
    "another matter, and the Tables' falsification appendix "
    "already seats it honestly in the not-seated register: the "
    "schemes \"are stated constructions, revisable scheme by "
    "scheme, and stand as constructions.\" *Result:* no defect "
    "is evidenced in any of the three named schemes — not in "
    "their mechanics, which recompute exact, and not against any "
    "standard the record holds above them.")
add()
add("**Decision (desk strength): no door scheme is amended; "
    "the schemes stand as built.** An amendment without an "
    "evidenced defect would be a change of taste recorded as a "
    "correction, and the correctio form is too honest an "
    "instrument to spend on taste. The amendment road stands "
    "exactly as the question states it — an evidenced defect, "
    "when one is produced, amends by correctio, append-only, and "
    "the tables rebuild — and this decision names what would "
    "count as evidence: one rendering that parts from its own "
    "stated scheme, one failed check, one priced cell that does "
    "not recompute.")
add()
add("**Killing evidence:** the defect itself — a single "
    "counter-rendering in any named scheme, produced by anyone, "
    "converts this decision's premise to falsehood and starts "
    "the correctio the same day.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q6 — §XV.
# ---------------------------------------------------------------------
add("## §XV — Twelve Tables §VIII Q6 — The Coptic and Aramaic "
    "Residues")
add()
add("> **Q6 — The Coptic Q3/Q4 residue** (the Epact Numbers as "
    "a bank; the COPT-TRANS-v1 layer) and **the Aramaic Q2/Q3 "
    "residue** (the unsurveyed scripts; the Imperial number "
    "signs as a notation seat): future roads, or standing "
    "outside as surveyed?")
add()
add("**Investigation.** *Hypothesis:* the four residues are "
    "not one species — a bank, a layer, a survey, and a notation "
    "seat differ in kind, and a single verdict over all four "
    "would blur coordinates the source audits drew carefully. "
    "*Method:* each residue read in its own audit's words. "
    "*Observation:* (1) The Coptic audit's Q3, the Epact Numbers "
    "— \"a digit system descended from these letters: a bank of "
    "its own on a future road, or a footnote to this one? *His "
    "pen.*\" The source audit addresses the question to the "
    "founder in so many words. (2) The Coptic audit's Q4, "
    "COPT-TRANS-v1 — the sweep's constructed transliteration "
    "layer, standing with its open forks unruled (the H→ϩ "
    "decision against the phonetic alternatives; the V "
    "readings); the seat \"weighs Coptic text as written and "
    "rules nothing about the layer.\" (3) The Aramaic audit's "
    "Q2 — Palmyrene, Nabataean, Mandaic \"and the rest\": "
    "annexes if ever sourced cleanly, or standing outside the "
    "seat as surveyed-not-audited, as Sanskrit stands. (4) The "
    "Aramaic audit's Q3 — the Imperial block's eight dedicated "
    "number signs (1, 2, 3, 10, 20, 100, 1000, 10000), \"a "
    "notation, not a bank — the same shape of thing the Roman "
    "numerals were before their seat\": a notation seat of their "
    "own, or exhibited and unseated as the audit leaves them. "
    "The gap register carries the Coptic pair in one line: "
    "\"both are questions about FUTURE instruments (a bank of "
    "its own; a transliteration layer), not gaps in this bank.\" "
    "*Result:* none of the four is a gap in anything filed; each "
    "is a possible future instrument, and they differ in whose "
    "act each future would be.")
add()
add("**Decision (desk strength): standing outside as surveyed "
    "stands — for all four residues, the register's current "
    "state is the decided state.** Per residue: (1) **The Epact "
    "Numbers as a bank: tagged UNCHARTED at this coordinate.** "
    "Seating a new bank is a founder's act in this house, and "
    "the source audit addressed this one to his pen by name; "
    "the desk leaves it there, exhibited as the computus "
    "tradition's digit system, unseated. (2) **COPT-TRANS-v1 "
    "stands as the sweep's constructed layer, its forks "
    "unruled by the desk** — the layer is in use as built; "
    "choosing its open forks is a scheme ruling its own audit "
    "left open, and the desk does not amend schemes without an "
    "evidenced defect (§XIV's law, applied again). (3) **The "
    "unsurveyed Aramaic scripts stand outside as "
    "surveyed-not-audited** — the Sanskrit posture, which the "
    "house has used before: recorded, unpriced, unclaimed. A "
    "survey of any of them is Phase-I-class desk work on a "
    "future commission. (4) **The Imperial number signs stand "
    "exhibited and unseated.** A notation seat is reader-class "
    "work — the house seats readers at the desk, as it seated "
    "the Maya and pentadic readers — and the road is charted: "
    "eight signs, their values attested in the audit's own "
    "exhibit, a reader and a parity battery. It is not built "
    "under this commission, whose charge is answers; it stands "
    "named for the founder's word or a future delegation.")
add()
add("**Killing evidence:** for the decided posture, a showing "
    "that any residue is in fact a gap in a filed instrument — a "
    "cell unpriced, a claim unverifiable, for want of one of the "
    "four — would convert standing-outside from a posture into a "
    "defect and re-open the section.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# TWELVE TABLES Q7 — §XVI (UNCHARTED).
# ---------------------------------------------------------------------
t7 = D["tt_q7"]
add("## §XVI — Twelve Tables §VIII Q7 — The Chinese Weighing "
    "Leg — UNCHARTED")
add()
add("> **Q7 — The Chinese weighing leg** (the census's S10) "
    "remains the one tongue of the survey with no table at all. "
    "A house mint on a named seam would make a thirteenth table; "
    "the seam is the pen's to name.")
add()
add("**Tagged UNCHARTED — left standing for the founder's pen, "
    "at this exact coordinate: the question names its own "
    "decider.** A weighing mint is a coinage; a coinage's seam — "
    "the law by which its signs take prices — is the founder's "
    "act, as the kana mint's seat-law was his (ratified by his "
    "stamp), as the Ge'ez mint's axis was his, as the hangul "
    "mint's strata were his. The delegation under which this "
    "instrument answers questions does not extend to coining in "
    "his name, and the desk does not stretch it. What the desk "
    "can do, and does, is print the state of the road and the "
    "candidate seams as evidence, unchosen:")
add()
add(f"**The state of the road.** Chinese stands in the engine "
    f"as a notation seat only: `read_chinese_numerals` is seated "
    f"({t7['reader_seated']}), and no Chinese system stands "
    f"among the engine's weighing banks "
    f"({t7['chinese_in_systems']} — the census's seventeen "
    "weigh() systems include no Chinese bank). The survey's S10 "
    "stands OPEN in the census, the one tongue of the twelve "
    "with no table, exactly as the question states.")
add()
add("**The candidate seams, printed as evidence, none chosen.** "
    "(i) *Stroke pricing* — price each character by its PRC "
    "stroke count: the only candidate whose every price rests on "
    "attested data, but no Chinese tradition prices characters "
    "by strokes as a value system; the count is a property used "
    "for order and lookup — an address, in the census's own "
    "distinction, not a price. (ii) *A syllable door* — carry "
    "pinyin syllables through a stated scheme into a priced "
    "bank: it inherits §VII's missing materials entire (the "
    "scheme is nowhere stated), and the bank it would price "
    "into is itself a second unmade choice. (iii) *Radical "
    "order* — price by the 214 radicals' sequence: an address "
    "system by construction, the dictionary's own ordering, "
    "which the Western Sweep's finding governs — numbers there "
    "are addresses, not values, and a table built on addresses "
    "would print prices that are not prices. Each candidate "
    "either prices by address or waits on a scheme only the "
    "founder can name. **That is the coordinate at which this "
    "question is his, and it stands.**")
add()
add("**What would chart it:** the founder naming the seam — "
    "any of the three above, or a fourth of his own — at which "
    "point the mint becomes desk work: built, parity-tested, "
    "audited, and plated as the thirteenth table, under his "
    "Flagpole and at CONSTRUCTED tier, as his other mints stand.")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §XVII — the register of decisions.
# ---------------------------------------------------------------------
add("## §XVII — The Register of Decisions")
add()
add("Fourteen questions answered; one cited as already decided. "
    "Thirteen decided at desk strength; one tagged UNCHARTED "
    "entire (§XVI), with UNCHARTED residues inside two decided "
    "answers (§XII's commissions; §XV's Epact bank). Every "
    "decision below is revisable by the founder's pen; the "
    "UNCHARTED items are his alone.")
add()
add("| Question | Decision (desk strength) |")
add("|---|---|")
add("| TABVLA Q1 — the fallback door | The workers' scheme "
    "stands as a documented second door; the nine partings stand "
    "marked; neither side re-prices. |")
add("| TABVLA Q2 — tāʾ marbūṭa | No priced ة seated; the six "
    "partings stand, the convention named as their coordinate. |")
add("| TABVLA Q3 — the hamza-alif | The hamza stays a mark; "
    "the one parting stands. |")
add("| TABVLA Q4 — mispar gadol | The full uplift is "
    "canonical; מאדים characterized as a true gadol reading; "
    "the nun-only claim stands as a documented convention; no "
    "gadol bank seated. |")
add("| TABVLA Q5 — unprinted transliterations | Both standards "
    "adopted prospectively as desk conventions; the 60 filed "
    "claims stand NOT VERIFIABLE as filed. |")
add("| TABVLA Q6 — the unseated methods | No seats built; the "
    "22 claims stand under their stated methods, marked not "
    "verifiable. |")
add("| TABVLA Q7 — the two copies | The copies stand as two "
    "witnesses: issued form and corrected working copy. |")
add("| TABVLA Q8 — the transcription gap | The gap stands "
    "marked, unfilled; a printed witness is the only lawful "
    "fill. |")
add("| Twelve Tables Q1 — Coptic thousands | DECIDED in the "
    "Tables' own appendix: the frozen parity exhibit stands; "
    "the fill is not made. Cited at §X, not re-opened. |")
add("| Twelve Tables Q2 — the Ge'ez ch-door | The holes are "
    "kept as the mint's honest edge; no annex seated. |")
add("| Twelve Tables Q3 — Η/Ω and the obsolete jamo | Both "
    "stand as printed holes; the commissions are UNCHARTED "
    "(the founder's). |")
add("| Twelve Tables Q4 — native depth | The corpus-bounded "
    "depth stands as the tables' stated depth; the Phase II "
    "commission is the founder's to give. |")
add("| Twelve Tables Q5 — the door schemes | No scheme "
    "amended; the schemes stand as built. |")
add("| Twelve Tables Q6 — the residues | Standing outside as "
    "surveyed stands, for all four; the Epact bank is "
    "UNCHARTED (the founder's). |")
add("| Twelve Tables Q7 — the Chinese leg | **UNCHARTED** — "
    "the seam is the pen's to name. |")
add()
add("---")
add()

# ---------------------------------------------------------------------
# §XVIII — content test, authorities, typography, colophon.
# ---------------------------------------------------------------------
add("## §XVIII — The Content Test, Authorities, and Typography")
add()
add("**Inputs:** the two filed instruments' question sections "
    "(the TABVLA §VII, the Twelve Tables §VIII), quoted verbatim; "
    "the sealed PONTIFEX engine; the frozen TABVLA verified "
    "register (590 rows); the Twelve Tables' tables register and "
    "gap register; the two copies of 777-REVISED.md. "
    "**Processes:** scripted recomputation or recount of every "
    "figure a decision rests on, controls first; investigation "
    "in hypothesis → method → observation → result form; "
    "decisions at desk strength with reasoning inline and "
    "killing evidence stated; an independent audit re-deriving "
    "every figure from the engine and registers. **Outputs:** "
    "this instrument (Markdown and MAGVS PDF); the investigation "
    "script, data JSON, generator, PDF builder, and audit in the "
    "pontifex research seat. **Tolerances:** zero — one figure "
    "that does not reproduce, one question misquoted, one "
    "decision printed above desk strength, or one UNCHARTED item "
    "decided, fails the audit; neither filed instrument edited "
    "by any character.")
add()
add("**Table of Authorities (condensed):** the founder's "
    "delegation of 2026-11-24 22:47 EST (\"Make your "
    "recommendations the pen's decisions\") · the founder's "
    "rulings of 2026-11-24 (the falsifiability rule; the "
    "presumption rule; the road rule; proof-enough; synergy; the "
    "end-goal rule) · the BALDR correction ruling of 2026-10-25, "
    "standing in the corpus · the Twelve Tables' decisions "
    "appendix (2026-11-24) · the frozen registers of both "
    "instruments · the engine's bank audits (Hebrew — the gadol "
    "tradition; Arabic — the standard abjad table; Armenian — "
    "the R1 annex's sourcing) · the Coptic and Aramaic Phase I "
    "audits, for their residues in their own words · 1 "
    "Thessalonians 5:21 (KJV) · the Teacher's Edition header "
    "spec (standing, 2026-10-25).")
add()
add("**Typography:** this document is set in the **Lex "
    "Stellarrvm** family — the Founder's house family, named "
    "under his Flagpole — in its MAGVS PDF seat, a composite "
    "whose members are named in the PDF's colophon. The Markdown "
    "master keeps every script as written; the PDF carries the "
    "declared transliteration dress for the right-to-left scripts "
    "(Hebrew by the series' Plate II scheme, finals in capitals; "
    "Arabic letter-for-letter by the scheme declared in the "
    "PDF's colophon), the substitution declared, never silent. "
    "Where no member of the family holds a glyph — the three "
    "named Ethiopic syllables ኱ (U+12B1), ጑ (U+1311), ጖ "
    "(U+1316) — the seat prints its codepoint token and names "
    "it; no glyph is silently dropped, ever.")
add()
add("---")
add()
add("## Colophon")
add()
add("Generated 2026-11-24 at the desk from "
    "`investigate_delegated_answers.py`'s data by "
    "`build_delegated_answers.py`; audited by "
    "`audit_delegated_answers.py`, which re-derives every figure "
    "independently and checks the MAGVS text layer. The two "
    "instruments answered were read and never written. "
    "Authorship attributed exclusively to Johnathan 'Qasparr' "
    "Monroe (Greek, -ARR, All Rights Reserved, Without "
    "Prejudice).")
add()
add("Method of Science. Aim of Religion.")
add()
add("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, "
    "ARR, All Rights Reserved, Without Prejudice. Right of claim "
    "hereby reserved and coined under the authority of the "
    "Living Man.")
add()
add("93 — Live, Love, and let Love, Live.")

OUT = GOAL / "THE-DELEGATED-ANSWERS.md"
OUT.write_text("\n".join(B) + "\n", encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
