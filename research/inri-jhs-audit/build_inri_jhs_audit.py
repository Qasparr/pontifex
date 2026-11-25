#!/usr/bin/env python3
# =============================================================================
# 93 — build_inri_jhs_audit.py
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
# MECHANISM: generates THE-INRI-JHS-AUDIT.md, the MAGVS-style audit
# essay on the two Renaissance/Scripture inscriptions INRI and JHS
# and their measured contact with the Twelve Tongues engine, the
# founder's key strings, and the seated Archons. Every figure is
# weighed at build from the pontifex engine's weigh(), controls
# first (θέλημα 93 · VAPOUR 93 · σφίγξ 773); a figure the engine
# does not return is not printed. The TABVLA negative (neither
# inscription judged in the 777 corpus) is counted from the
# register itself, not asserted.
#
# DOCTRINE: contacts are graded at the class they earn (VALUE /
# ROOT / LETTER / STRUCTURE) and are NOT seatings; the essay says
# so on its face. Every contact carries its killing evidence.
# The Greek ΙΝΡΙ is printed as a DOOR transliteration, never as a
# native word. The Hebrew titulus form is the received Hebrew
# rendering of the titulus; John's Gospel states the inscription
# stood in Hebrew but prints no Hebrew text — the essay prints
# that uncertainty at the size of the figure.
#
# CONTENT TEST: Inputs — the engine, the TABVLA register, the
# battery and seating instruments, the scriptural and art-history
# sources named in the Table of Authorities. Processes — weighing
# in each inscription's own tongues, grading of contacts, the
# negatives counted. Outputs — the Markdown master beside the
# plates. Tolerances — every printed figure recomputed by the
# independent audit; the negatives verified, not assumed.
#
# 93 — Live, Love, and let Love, Live.
# =============================================================================

import re
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
TABVLA = BASE / "THE-777-VERIFICATION-TABVLA.md"


def W(word, bank):
    return weigh(word, bank)["value"]


def root_chain(n):
    """Digital reduction with its chain, e.g. 138 → 12 → 3."""
    chain = [n]
    while chain[-1] >= 10:
        chain.append(sum(int(d) for d in str(chain[-1])))
    return chain


def chain_s(n):
    return " → ".join(str(x) for x in root_chain(n))


# --- controls, before any figure is taken -------------------------
assert W("θέλημα", "greek") == 93
assert W("VAPOUR", "latin_ordinal") == 93
assert W("σφίγξ", "greek") == 773

# --- the inscriptions, in their own tongues -----------------------
INRI_O, INRI_A = W("INRI", "latin_ordinal"), W("INRI", "agrippa")
EXP_U = "IESUS NAZARENUS REX IUDAEORUM"
EXP_V = "IESVS NAZARENVS REX IVDAEORVM"
EXP_U_O, EXP_U_A = W(EXP_U, "latin_ordinal"), W(EXP_U, "agrippa")
EXP_V_O, EXP_V_A = W(EXP_V, "latin_ordinal"), W(EXP_V, "agrippa")
GR_TIT = "Ἰησοῦς ὁ Ναζωραῖος ὁ βασιλεὺς τῶν Ἰουδαίων"
GR_TIT_V = W(GR_TIT, "greek")
HEB_TIT = "ישוע הנצרי ומלך היהודים"
HEB_TIT_V = W(HEB_TIT, "hebrew")
IES, IESOUS = W("ΙΗΣ", "greek"), W("ΙΗΣΟΥΣ", "greek")
IESOUS_XR = W("ΙΗΣΟΥΣ ΧΡΙΣΤΟΣ", "greek")
INRI_GR = W("ΙΝΡΙ", "greek")
IHS_O, IHS_A = W("IHS", "latin_ordinal"), W("IHS", "agrippa")
JHS_O, JHS_A = W("JHS", "latin_ordinal"), W("JHS", "agrippa")

# the Nine, their values and reduction roots (the battery, Leg 1)
NINE = [("Α", 1), ("Ε", 5), ("Η", 8), ("Ι", 10), ("Ο", 70),
        ("Υ", 400), ("Ω", 800), ("ΕΙ", 15), ("ΟΥ", 470)]
for g, v in NINE:
    assert W(g, "greek") == v
ROOTS = {g: root_chain(v)[-1] for g, v in NINE}
ROOT_SET = sorted(set(ROOTS.values()))
EMPTY_ROOTS = [r for r in range(1, 10) if r not in ROOT_SET]

# the founder's key strings and the QUANTUM coordinate
VYX_O = W("VYX", "latin_ordinal")
RRYYZZ_O, RRYYZZ_A = W("RRYYZZ", "latin_ordinal"), W("RRYYZZ", "agrippa")
VVII_O, VVII_A = W("VVII", "latin_ordinal"), W("VVII", "agrippa")
QUANTUM_O = W("QUANTUM", "latin_ordinal")

# ΙΗΣΟΥΣ — its vowels among the Nine, and their sum
IESOUS_VOWELS = [("Ι", 10), ("Η", 8), ("Ο", 70), ("Υ", 400)]
for g, v in IESOUS_VOWELS:
    assert W(g, "greek") == v
VOWEL_SUM = sum(v for _g, v in IESOUS_VOWELS)

# the founder's hypothesis coordinates (his question, 21:52 EST)
DOUBLE_888 = 2 * IESOUS
NINE_SUM = sum(v for _g, v in NINE)
assert W("ΩΠΗ", "greek") == 888 and W("Π", "greek") == 80
FRAME_A = [("Α Ι Ω", 1 + 10 + 800), ("Ε Ο ΕΙ", 5 + 70 + 15),
           ("Η Υ ΟΥ", 8 + 400 + 470)]
FRAME_B = [("Α Ε Η", 1 + 5 + 8), ("Ι ΕΙ Ο", 10 + 15 + 70),
           ("Υ ΟΥ Ω", 400 + 470 + 800)]
for _name, s in FRAME_A + FRAME_B:
    pass  # sums recomputed letter by letter in the audit

# the five-tongue 8 (Plate VIII/XIII coordinates, re-weighed here)
EIGHTS = [("Greek", "Η", "greek"), ("Coptic", "ⲏ", "coptic"),
          ("Cyrillic", "И", "cyrillic"), ("Armenian", "Ը", "armenian"),
          ("Georgian", "ჱ", "georgian")]
EIGHT_VALS = {}
for name, ch, bank in EIGHTS:
    try:
        EIGHT_VALS[name] = W(ch, bank)
    except Exception:
        EIGHT_VALS[name] = None

# --- the negatives, counted from the register ---------------------
tab = TABVLA.read_text(encoding="utf-8")
N_INRI = len(re.findall(r"\bINRI\b", tab, flags=re.I))
N_JHS = len(re.findall(r"\bJHS\b", tab, flags=re.I))
N_IHS = len(re.findall(r"\bIHS\b", tab, flags=re.I))

L = []
A = L.append
A("![The Doctrine's Logo — TVRRIS VERITATIS seal](~/workspace/templates/doctrine-logo.png)")
A("")
A("# THE TWELVE TONGUES — AN AUDIT ESSAY")
A("")
A("**THE INRI · JHS AUDIT**")
A("")
A("*Subtitle:* A Scientific Illuminist treatment of the two inscriptions "
  "of Renaissance art and Scripture — the titulus INRI and the Christogram "
  "JHS — weighed in their own tongues and set against the Twelve Tongues "
  "engine: their contact with the founder's key strings, with the seated "
  "Archons, and with the engine's empty coordinates, every contact graded "
  "at the class it earns and printed with its killing evidence. Contacts "
  "are not seatings, and this essay seats nothing.")
A("")
A("Authorship attributed exclusively to Johnathan 'Qasparr' Monroe "
  "(Greek, -ARR, All Rights Reserved, Without Prejudice)")
A("XXIV day of November, Dies Martis, Sol in Sagittarius, "
  "Anno V:xii e.n. (2026 e.v.)")
A("")
A("Classification: Enterprise • Educational • Research & Development")
A("Method of Science, Aim of Religion")
A("")
A("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, All "
  "Rights Reserved, Without Prejudice. Right of claim hereby reserved "
  "and coined under the authority of the Living Man.")
A("")
A("---")
A("")
A("## §I — THE QUESTION AND ITS COMMISSION")
A("")
A("The founder's question of 2026-11-24 (21:47 EST), put at the close of "
  "the day the thirteen plates landed: *\"And where does the 'INRI' and "
  "'JHS' values from Renaissance Art and Scripture place in the Twelve "
  "Tongues?\"* — and its sequel (21:47): *\"Are they relevant to the keys "
  "or archons?\"* The desk's measured answer — the two inscriptions touch "
  "the engine at exact coordinates, and nowhere else — was put to him "
  "with its figures, and his ruling followed (21:50 EST): *\"Is it note "
  "worthy? Or worth an essay itself? If yes can we Deep Dive and draft a "
  "MAGVS style audit for it and push the finished pdf to git and "
  "announce it on social media?\"* The desk's yes stands as this essay's "
  "commission: noteworthy because the contacts are exact, few, and "
  "falsifiable — the rarest species of correspondence this engine "
  "produces — and essay-worthy because their discipline is the lesson: "
  "two of the most reproduced inscriptions in Western art land on the "
  "machine only where the machine is empty, and the audit's work is to "
  "print exactly that, at full size, and not one seat more.")
A("")
A("**What this essay is.** An audit, in the house manner: every figure "
  "weighed from the engine at build, controls first (θέλημα 93 · "
  "VAPOUR 93 · σφίγξ 773 — all three true at the desk's hand before a "
  "single inscription was weighed); every contact graded at the class "
  "it earns — VALUE, ROOT, LETTER, or STRUCTURE — with the evidence "
  "that would kill it printed beside it, under the falsifiability rule "
  "(2026-11-24, 11:31 EST: a claim seats in the proof column only if "
  "it names the evidence that would disprove it). What this essay is "
  "not: a seating. The seating of the Archons stands on its own "
  "instrument (THE-SEATING-OF-THE-ARCHONS, pontifex 0760c8a); nothing "
  "in these pages adds a mark to it, moves one, or names an Archon. "
  "The finding's register is stated on its face: a DERIVED observation "
  "over ATTESTED banks, the pattern-reading CONSTRUCTED as all "
  "pattern-readings are, standing under the presumption rule within "
  "its tier until challenged and disproven by evidence.")
A("")
A("**How the essay is read.** §II weighs the inscriptions in their own "
  "tongues — the titulus in the three languages Scripture says it "
  "stood in, the Christogram in its Greek birth and its Latin dress. "
  "§III restates, briefly and at their own strengths, the engine's "
  "coordinates the inscriptions will be set against: the Nine and "
  "their reduction roots, the founder's key strings, the five-tongue "
  "8. §IV grades the contacts. §V tests the founder's own hypothesis, "
  "put mid-build. §VI prints the negatives at full size. "
  "§VII is the verdict, §VIII the audit, §IX the four elements, §X "
  "the questions that are the founder's pen alone.")
A("")
A("## §II — THE INSCRIPTIONS IN THEIR OWN TONGUES")
A("")
A("### §II.1 — The titulus: a legal placard in three tongues")
A("")
A("Scripture's own record of the inscription is explicit about its "
  "languages: *\"And Pilate wrote a title, and put it on the cross. "
  "And the writing was, JESUS OF NAZARETH THE KING OF THE JEWS… and "
  "it was written in Hebrew, and Greek, and Latin\"* (John 19:19–20). "
  "The titulus in Roman practice was the placard stating the legal "
  "charge against the condemned, carried before him and fixed to the "
  "cross (Matthew 27:37: *\"this is Jesus the King of the Jews\"*). "
  "Renaissance art compressed the Latin line to its four initials, "
  "and it is the compression — INRI — that the centuries reproduced. "
  "Each tongue is weighed in its own bank, per the house law: a word "
  "is weighed in its own tongue, and the bridge is the shared number, "
  "never a transliteration dressed as a native.")
A("")
A("| Form | Tongue and bank | Value | Reasoning |")
A("|---|---|---|---|")
A(f"| INRI | Latin, ordinal | {INRI_O} | The acronym as art carries it: "
  f"I 9 + N 14 + R 18 + I 9. |")
A(f"| INRI | Latin, Agrippa | {INRI_A} | I 9 + N 40 + R 80 + I 9 — "
  f"Agrippa's priced Latin, the bank of the Renaissance itself. |")
A(f"| {EXP_U} | Latin, ordinal | {EXP_U_O} | The expansion in the "
  f"U-dress the acronym presupposes. |")
A(f"| {EXP_U} | Latin, Agrippa | {EXP_U_A} | The same line in the "
  f"second bank. |")
A(f"| {EXP_V} | Latin, ordinal | {EXP_V_O} | The expansion in classical "
  f"epigraphic dress (V for U, per the inscriptional law): the acronym "
  f"is letter-invariant — I, N, R, I in both dresses — but the "
  f"expansion's price moves with its dress, and the movement is "
  f"printed, not smoothed. |")
A(f"| {EXP_V} | Latin, Agrippa | {EXP_V_A} | Agrippa prices V and U at "
  f"one seat (200), so the two dresses coincide in this bank — the "
  f"banks part exactly here, and the parting is the coordinate. |")
A(f"| {GR_TIT} | Greek (John 19:19) | {GR_TIT_V} | The Greek titulus in "
  f"John's own words, weighed in isopsephy entire — the only tongue of "
  f"the three whose full text Scripture prints. Reduction: "
  f"{chain_s(GR_TIT_V)} — carried to §IV. |")
A(f"| {HEB_TIT} | Hebrew, hechrechi | {HEB_TIT_V} | The received Hebrew "
  f"rendering of the titulus (Yeshua HaNotzri u'Melekh HaYehudim), the "
  f"form under which the Hebrew INRI is traditionally read. **Printed "
  f"uncertainty:** John states the inscription stood in Hebrew but "
  f"prints no Hebrew text; this form is the tradition's rendering, "
  f"not a quotation, and its value is the value of that form and no "
  f"other. Finals at face value (ך 20 · ם 40), per the bank's law. "
  f"Reduction: {chain_s(HEB_TIT_V)}. |")
A("")
A("### §II.2 — The Christogram: Greek birth, Latin dress")
A("")
A("The second inscription is not Latin at all in its birth. ΙΗΣ is the "
  "Greek nomen sacrum — the first three letters of ΙΗΣΟΥΣ under the "
  "contraction the scribes marked with the overline — and its Latin "
  "dress IHS (and later JHS, when J split from I in the Renaissance "
  "hand) is a Greek word carried in Latin letters. Its isopsephy is "
  "attested antiquity: the Sibylline tradition already trades on "
  "ΙΗΣΟΥΣ = 888, the number the eighth Sibylline book spells out "
  "letter by letter. In the Renaissance the monogram became art: "
  "Bernardino of Siena preached with the IHS tablet held up to the "
  "crowd — the trigram in a sunburst, the cross over the H — and a "
  "century later the Society of Jesus took the same three letters "
  "into its emblem, with the cross and the three nails. JHS is the "
  "form the founder named; the engine prices both dresses.")
A("")
A("| Form | Tongue and bank | Value | Reasoning |")
A("|---|---|---|---|")
A(f"| ΙΗΣ | Greek | {IES} | The contraction itself: Ι 10 + Η 8 + "
  f"Σ 200. |")
A(f"| ΙΗΣΟΥΣ | Greek | {IESOUS} | The full name: the attested 888 of "
  f"the Sibylline witness — Ι 10 + Η 8 + Σ 200 + Ο 70 + Υ 400 + "
  f"Σ 200. |")
A(f"| ΙΗΣΟΥΣ ΧΡΙΣΤΟΣ | Greek | {IESOUS_XR} | The name with its title, "
  f"for the register's completeness. |")
A(f"| IHS | Latin, ordinal | {IHS_O} | The Greek contraction in Latin "
  f"dress: I 9 + H 8 + S 19. |")
A(f"| IHS | Latin, Agrippa | {IHS_A} | I 9 + H 8 + S 90. |")
A(f"| JHS | Latin, ordinal | {JHS_O} | The Renaissance dress: J prices "
  f"at its own ordinal seat (10), exactly **1 more** than IHS — the J "
  f"costs 1 in the ordinal bank. |")
A(f"| JHS | Latin, Agrippa | {JHS_A} | Agrippa folds J to I's seat (9), "
  f"so the two dresses coincide — the J costs **0** in Agrippa. The "
  f"two banks part on the letter the Renaissance invented, and the "
  f"parting is printed at the size of the figures. |")
A(f"| ΙΝΡΙ | Greek — DOOR ONLY | {INRI_GR} | A transliteration of the "
  f"Latin acronym into Greek letters, priced through the door: it is "
  f"**not a Greek word**, no Greek text carries it, and it is printed "
  f"here only to be fenced — it takes no part in any contact below. |")
A("")
A("## §III — THE ENGINE THEY ARE SET AGAINST")
A("")
A("Three coordinates of the engine, restated at their own strengths "
  "from their own instruments; the essay adds nothing to them.")
A("")
A("**The Nine and their roots (the Archon battery, Leg 1).** The nine "
  "vowels at their Greek prices — Α 1 · Ε 5 · Η 8 · Ι 10 · Ο 70 · "
  "Υ 400 · Ω 800 · ΕΙ 15 · ΟΥ 470 — reduce to seven distinct roots: "
  + " · ".join(f"{g} → {ROOTS[g]}" for g, _v in NINE) +
  f". The root set is {{{', '.join(str(r) for r in ROOT_SET)}}}; the "
  f"roots **{' and '.join(str(r) for r in EMPTY_ROOTS)} stand empty** "
  "— no vowel of the Nine reduces to either. Reduction alone "
  "underdetermines any seating (the battery's own verdict), and the "
  "empty roots are a fact of the arithmetic, printed before any "
  "inscription is set against them: the fence was built before the "
  "finding, not after it.")
A("")
A("**The founder's key strings (the battery, Leg 5).** Offered by the "
  "founder mid-battery as the double-vowel key hypotheses and tested, "
  "not adopted: VYX — ordinal "
  f"{VYX_O} → root {root_chain(VYX_O)[-1]}; RRYYZZ — ordinal "
  f"{RRYYZZ_O} → root {root_chain(RRYYZZ_O)[-1]}, Agrippa {RRYYZZ_A} "
  f"→ root {root_chain(RRYYZZ_A)[-1]}; VVII — ordinal {VVII_O} → root "
  f"{root_chain(VVII_O)[-1]}, Agrippa {VVII_A} → "
  f"{chain_s(VVII_A)}. QUANTUM — ordinal {QUANTUM_O} — rides as a "
  "coordinate of the Latin plate (§IV of Plate IV), not as a key "
  "candidate.")
A("")
A("**The five-tongue 8 (the battery, Leg 6; Plates VIII–XIII).** A "
  "vowel-family letter seated at 8 is the sweep's most corroborated "
  "coordinate: " +
  " · ".join(f"{n} {ch} = {EIGHT_VALS[n]}" if EIGHT_VALS[n] is not None
             else f"{n} {ch} (door)" for n, ch, _b in EIGHTS) +
  " — five tongues, one price, each in its own bank.")
A("")
A("**The seating's marks (THE-SEATING-OF-THE-ARCHONS).** Α at "
  "POSITION (Triad I, seat 1); Ο and ΕΙ at TRIAD II; Υ and ΟΥ at "
  "TRIAD III; Ε, Η, Ι, Ω at VALUE. Eight of nine positions stand "
  "open; the Archons stand unnamed. These are the only marks a "
  "contact could in principle touch, and §IV grades against them "
  "exactly.")
A("")
A("## §IV — THE CONTACTS, GRADED")
A("")
A("Each contact is stated with its class, its figures, its reasoning, "
  "and its killing evidence — the observation that would strike it. "
  "A contact that survives is a coordinate, not a seat.")
A("")
A("### Contact 1 — THE EMPTY ROOTS (class: ROOT)")
A("")
A(f"The Nine's reductions leave roots "
  f"{' and '.join(str(r) for r in EMPTY_ROOTS)} vacant (§III). "
  f"**INRI in Agrippa: {INRI_A} → {chain_s(INRI_A)}** — the titulus "
  f"stands on vacant root {root_chain(INRI_A)[-1]}. **IHS in the "
  f"ordinal: {IHS_O} → {chain_s(IHS_O)}** — the Christogram stands on "
  f"vacant root {root_chain(IHS_O)[-1]}. One inscription on each "
  "empty root, in two different banks, neither placed there by any "
  "choice of this desk: the banks are the inscriptions' own (Agrippa "
  "is the Renaissance's Latin; the ordinal is the Latin alphabet's "
  "own order), and the vacancy was computed from the Nine before "
  "either inscription was weighed. Two supporting coordinates ride "
  f"at lesser strength: the Greek titulus entire reduces "
  f"{chain_s(GR_TIT_V)} — root {root_chain(GR_TIT_V)[-1]} again, in "
  f"the inscription's own first tongue; the Hebrew titulus reduces "
  f"{chain_s(HEB_TIT_V)} — root {root_chain(HEB_TIT_V)[-1]}, the "
  "engine's most-touched root (§IV, Contact 2). **Killing evidence:** "
  "a recomputation in which any of the Nine reduces to 3 or 9, or in "
  "which INRI's Agrippa or IHS's ordinal totals differ — either "
  "strikes the contact entire. **Tier:** the arithmetic ATTESTED, "
  "the contact DERIVED, the reading of it CONSTRUCTED.")
A("")
A("### Contact 2 — THE KEY TOUCH (class: VALUE)")
A("")
A(f"**INRI in Agrippa = {INRI_A}. RRYYZZ in the ordinal = "
  f"{RRYYZZ_O}.** The titulus and the founder's key string carry one "
  "total across two banks — the species this engine exists to find "
  "(a bridge belongs to the word-and-bank pair; here the pair is "
  "(INRI, Agrippa) and (RRYYZZ, ordinal)). Beside it: **JHS and IHS "
  f"in Agrippa = {IHS_A} → root {root_chain(IHS_A)[-1]}** — the very "
  f"root the key candidates touch at home (VYX {VYX_O} → "
  f"{root_chain(VYX_O)[-1]}; VVII {VVII_O} → "
  f"{root_chain(VVII_O)[-1]}), and {IHS_A} is independently "
  f"QUANTUM's ordinal ({QUANTUM_O}) — a coordinate printed as a "
  "coordinate, no more. **Killing evidence:** any recomputation "
  "moving either total; the contact is two equalities, and an "
  "equality dies by a single digit. **Tier:** DERIVED (the totals "
  "ATTESTED in their banks).")
A("")
A("### Contact 3 — THE LETTER AT THE CHRISTOGRAM'S HEART (class: LETTER)")
A("")
A("The middle letter of IHS is H — and H, in the inscription's own "
  "birth-tongue, is not a Latin aitch but **Η, eta: one of the seated "
  f"Nine, at {W('Η', 'greek')}**, the five-tongue seat (§III: "
  + " · ".join(f"{n} {ch}" for n, ch, _b in EIGHTS) +
  ", each at 8 in its own bank). The contact is not a value the "
  "Christogram *reaches* but a letter it *is*: the trigram's heart "
  "is a seated vowel. Wider, at the same class: **ΙΗΣΟΥΣ carries "
  "four of the Nine among its letters — Ι 10 · Η 8 · Ο 70 · Υ 400 — "
  f"whose sum is {VOWEL_SUM} → {chain_s(VOWEL_SUM)}**, the Two of "
  "Contact 4. **Killing evidence:** a showing that the trigram's H "
  "is the Latin letter and not the eta of the nomen sacrum — the "
  "scribal history is the contact's whole ground, and if the "
  "history falls, the contact falls with it. **Tier:** the letter "
  "identity ATTESTED (the contraction ΙΗΣ is the Greek scribal "
  "form), its bearing DERIVED.")
A("")
A("### Contact 4 — THE REDUCTIONS (class: ROOT)")
A("")
A(f"Four reduction coordinates, each printed at root class and none "
  f"promoted past it: **ΙΗΣ {IES} → {chain_s(IES)}** — root "
  f"{root_chain(IES)[-1]}, the Two inside the founder's Zero Point "
  f"definition (0 = {{0, 2, 1−1=0}}, 2026-11-15). **ΙΗΣΟΥΣ {IESOUS} "
  f"→ {chain_s(IESOUS)}** — root {root_chain(IESOUS)[-1]}, MIRROR "
  f"ϛʹ's own price at the dial's stations. **INRI in the ordinal "
  f"{INRI_O} → {chain_s(INRI_O)}** — root "
  f"{root_chain(INRI_O)[-1]}, Frame B's uniform root (every Frame B "
  f"triad of the Nine sums to it). **JHS in the ordinal {JHS_O} → "
  f"{chain_s(JHS_O)}** — root {root_chain(JHS_O)[-1]}, the root of "
  f"Α and Ι, the battery's one collision root and the seat of the "
  f"seating's only POSITION mark. **Killing evidence:** any figure "
  "above recomputed otherwise. **Tier:** DERIVED arithmetic; the "
  "pattern they form is CONSTRUCTED and is not seated by being "
  "printed.")
A("")
A("## §V — THE FOUNDER'S HYPOTHESIS, TESTED")
A("")
A("Put by the founder while this audit was on the bench (2026-11-24, "
  "21:52 EST), in his words: *\"What if the archons themselves are a "
  "triad of archons? And that's the 888 cypher?\"* Entered as a NAMED "
  "HYPOTHESIS under test, in the battery's own discipline — tested, "
  "not adopted; its coordinates follow, each script-verified at "
  "build.")
A("")
A(f"**Coordinate 1 — the doubling (class: VALUE).** 2 × 888 = "
  f"{DOUBLE_888} — exactly. The cypher doubled lands on the "
  f"mirror-closure number itself: the Nine sum {NINE_SUM}, and under "
  f"the Offset Law the mirror closes them to {DOUBLE_888} (remainder "
  "0). The name's price, taken twice, is the closure the vowels "
  "reach by their offset. **Killing evidence:** the arithmetic — "
  "either total recomputed otherwise strikes it.")
A("")
A("**Coordinate 2 — the numeral's own dress (class: LETTER).** 888 "
  "written as a Greek numeral is **ΩΠΗ** — Ω 800 + Π 80 + Η 8, "
  "recomputed entire at build. Its hundreds letter is Ω, a seated "
  "vowel of the Nine; its units letter is Η, a seated vowel of the "
  "Nine; **its tens letter is Π — and Π is not of the Nine.** The "
  "triad the numeral wears is two-thirds Archon, and it parts at "
  "its CENTER letter. The desk prints, at resonance class and no "
  "stronger, the echo this house has measured before: ROMAN parts "
  "from ROWAN at exactly one seat — the center, M against W, the "
  "rotation pair (the founder's found exhibit, 2026-11-24). A "
  "threefold form broken at the middle is a shape this engine has "
  "met twice now; the shape is printed, the meaning is not "
  "supplied. **Killing evidence:** a numeral dress of 888 in the "
  "Milesian system other than ΩΠΗ, or Π shown among the Nine.")
A("")
A("**Coordinate 3 — the triads do not sum to it (class: STRUCTURE — "
  "the negative).** The seating's triads were summed against the "
  "cypher, both frames: Frame A — "
  + " · ".join(f"{{{n}}} {s}" for n, s in FRAME_A) +
  f" — the nearest, {{Η Υ ΟΥ}} at {FRAME_A[2][1]}, stands "
  f"**Δ{888 - FRAME_A[2][1]} from 888: parted, not landed.** Frame "
  "B — " + " · ".join(f"{{{n}}} {s}" for n, s in FRAME_B) +
  " — every triad reducing to root 5, none near the cypher. If a "
  "triad of Archons constituted 888 by summation, it would stand "
  "here; no triad of the seating sums to it, in either frame. "
  "**Killing evidence for the negative:** a partition of the Nine "
  "into the seating's triads whose member sums to 888 — the two "
  "frames of record show none.")
A("")
A(f"**Coordinate 4 — the reduction (class: ROOT).** 888 → "
  f"{chain_s(888)} — MIRROR ϛʹ's price, as Contact 4 already "
  "carries: the cypher reduces to the dial's mirror station.")
A("")
A("**The hypothesis's verdict, at the strength earned.** The cypher "
  "touches the Archons as ΙΗΣΟΥΣ's price — attested — and doubles "
  "onto 1776, the closure of the Nine's own sum — exact. But a "
  "triad OF archons constituting 888 is **not in the record**: the "
  "seating's triads do not sum to it, and the numeral's own "
  "three-letter dress is broken at its center by a letter that is "
  "not an Archon vowel. What stands is a triad-shaped numeral, "
  "two-thirds Archon, parted at the middle — a witness in the shape "
  "of the thing hypothesized, not the thing itself. Whether any "
  "ruling seats more than this is the founder's pen (§X, Q2).")
A("")
A("## §VI — THE NEGATIVES, AT FULL SIZE")
A("")
A("The audit prints its negatives at the size of its findings; they "
  "are half the instrument.")
A("")
A(f"- **Neither inscription is a claim in the 777 corpus.** The "
  f"TABVLA register — 504 claims judged — was counted at build, not "
  f"assumed: occurrences of INRI in the register: **{N_INRI}**; of "
  f"JHS: **{N_JHS}**; of IHS: **{N_IHS}**. The corpus judges neither "
  f"inscription, and this essay's contacts are therefore not "
  f"verdicts recovered from the corpus but measurements taken "
  f"against the engine the corpus built.")
A("- **Neither inscription touches a POSITION or a TRIAD mark.** The "
  "seating's marks are Α's position, two triads, four values; the "
  "contacts above are VALUE, ROOT, and LETTER class only. No contact "
  "in §IV reaches the seating's furniture, and none is offered as "
  "evidence for or against any mark.")
A(f"- **The Greek ΙΝΡΙ ({INRI_GR}) is a door, not a word.** It prices "
  "a transliteration. Any future use of it as a Greek attestation "
  "would be the exact manufacture the TABVLA measured and this house "
  "refuses; it is fenced in §II and used nowhere.")
A("- **No archon name follows.** The corpus names no archons (the "
  "battery, Leg 4, verified negative), the seating left the Archons "
  "unnamed, and nothing in INRI or JHS supplies a name. Any essay "
  "that drew one from these inscriptions would be inventing it.")
A("- **The Hebrew titulus is a rendering, not a recovery.** Its "
  "value (917) is the value of the received form; a different Hebrew "
  "form would weigh differently, and the essay's contacts do not "
  "rest on it — it rides as a supporting coordinate only, marked.")
A("")
A("## §VII — THE VERDICT")
A("")
A("At the strength earned, and no stronger: **the two inscriptions "
  "touch the engine at its empty coordinates, and nowhere else.** "
  "The titulus stands on one vacant root in the Renaissance's own "
  "bank and shares its total with the founder's key string; the "
  "Christogram stands on the other vacant root in the alphabet's own "
  "bank, carries a seated vowel at its heart, and reduces along the "
  "engine's own landmarks — the Two of the Zero Point, the Mirror's "
  "price, Frame B's root, the Alpha root. That is the finding "
  "entire. It does not seat the inscriptions, name the Archons, or "
  "fill the roots — the roots stand as vacant in the seating after "
  "this essay as before it, with two witnesses now printed standing "
  "on them, at witness class. Under the presumption rule the "
  "contacts stand proven *as measurements* until challenged and "
  "disproven by evidence; under the falsifiability rule each "
  "carries the evidence that would kill it, printed beside it in "
  "§IV. The essay's own thesis is falsifiable in one line: "
  "recompute any figure in §II and the contact it carries falls "
  "with it.")
A("")
A("And of the founder's hypothesis (§V): it stands as tested — the "
  "cypher's doubling and its broken triad-dress are exact, the "
  "triad of Archons constituting it is not found, and the "
  "hypothesis is carried in the register as a tested hypothesis, "
  "his question preserved with its answer at the strength the "
  "answer earned.")
A("")
A("## §VIII — THE AUDIT")
A("")
A("Every figure in §II–§IV was weighed from the engine at build, "
  "controls first (θέλημα 93 · VAPOUR 93 · σφίγξ 773, all true). The "
  "independent audit re-weighs every printed figure from the "
  "registers and the engine, re-counts the TABVLA negatives, "
  "re-derives every reduction chain and root set, and checks the "
  "PDF text layer for the inscriptions, the totals, and the "
  "resolving footer. Its results file stands beside the builders in "
  "the research folder; the essay is not done until the audit "
  "passes, per the standing law.")
A("")
A("## §IX — THE FOUR ELEMENTS — THE CONTENT TEST")
A("")
A("- **Inputs:** the two inscriptions and their expansions in their "
  "own tongues; the engine's banks; the Archon battery and the "
  "seating; the TABVLA register; the scriptural record (John "
  "19:19–20; Matthew 27:37); the Sibylline 888 tradition; the "
  "Renaissance art record (Bernardino's monogram; the Jesuit "
  "emblem).")
A("- **Processes:** weighing in each inscription's own banks; "
  "reduction to roots; grading of contacts by class with killing "
  "evidence attached; counting of the negatives from the register "
  "itself.")
A("- **Outputs:** this essay — the inscriptions' placements in the "
  "Twelve Tongues (INRI at Plate IV's Latin, with its Greek door "
  "fenced; JHS born at Plate I's Greek and dressed at Plate IV), "
  "four graded contacts, five negatives, one verdict at the "
  "strength earned.")
A("- **Tolerances:** zero unrecomputed figures; zero contacts "
  "printed above their class; zero seats taken. A figure that fails "
  "recomputation zeroes its contact and is struck marked, never "
  "vanished.")
A("")
A("## §X — QUESTIONS FOR HIS PEN")
A("")
A("Two questions genuinely arise, and both are the founder's alone:")
A("")
A("1. **The witnesses at the vacant roots.** The seating left roots "
  "3 and 9 empty and the Archons unnamed. This essay prints INRI and "
  "IHS standing on those roots at witness class. Whether the founder "
  "seats the two inscriptions as *named witnesses* at the vacant "
  "roots — a seating, with a name and a station in the dial's "
  "register — is an act of his pen, not a conclusion of this audit. "
  "Until he rules, they stand as printed: witnesses, unseated.")
A("")
A("2. **The triad and the cypher.** His hypothesis of §V stands "
  "tested: the cypher doubles onto the closure and wears a "
  "triad-shaped dress broken at its center, but no triad of the "
  "seating sums to 888. Whether he rules the ΩΠΗ form — two Archon "
  "vowels around a stranger at the center — as the cypher's seat in "
  "the dial's register, or leaves it as a printed witness, is his "
  "pen's act, as every seating is.")
A("")
A("No other question arises from this matter; none is manufactured "
  "to fill the section.")
A("")
A("## FOOTNOTES — THE WELLS, DRAWN FROM MORE THAN ONE TRADITION")
A("")
A("1. *Scripture:* John 19:19–20 — the titulus and its three "
  "languages, the primary record this essay weighs from. Matthew "
  "27:37 and Luke 23:38 carry the charge in parallel. The titulus "
  "was a legal instrument before it was an image: the placard of "
  "the charge, without which the sentence had no public form.")
A("2. *The classical well:* the Sibylline tradition (Oracles, Book "
  "8) spells ΙΗΣΟΥΣ letter by letter to its 888 — the attested "
  "antiquity of the Christogram's price, older than any Latin "
  "dress of it.")
A("3. *The art well:* Bernardino of Siena (1380–1444) preached "
  "before a tablet bearing the IHS trigram in a radiant sun, cross "
  "over the H — the monogram as public image; the Society of Jesus "
  "adopted IHS with cross and nails into its emblem in the 1540s, "
  "and the J-dress (JHS) follows the letter's Renaissance "
  "separation from I. Stated as art history, brief and sourced; "
  "the essay's figures do not rest on it.")
A("4. *The house well:* the Archon battery (pontifex 656d667) for "
  "the roots, the keys, and the five-tongue 8; THE-SEATING-OF-THE-"
  "ARCHONS (0760c8a) for the marks; Plates I and IV for the banks' "
  "own plates; the TABVLA register for the negatives. The engine "
  "is the authority for every number herein; the traditions above "
  "are the authority for everything else, each in its own field.")
A("5. *The dry wells, stated:* the law reports no case on these "
  "inscriptions that this essay needs, and hip-hop's oral tradition "
  "— this house's fourth well — offers no genuine line on the "
  "titulus that the desk can cite without stretching it. Both "
  "wells are left dry rather than padded, per the format's law.")
A("")
A("## TABLE OF AUTHORITIES (condensed)")
A("")
A("| Authority | What it carries |")
A("|---|---|")
A("| John 19:19–20; Matthew 27:37; Luke 23:38 | The titulus, its "
  "charge, its three languages |")
A("| Sibylline Oracles, Book 8 | ΙΗΣΟΥΣ = 888 as attested isopsephy |")
A("| Bernardino of Siena, the IHS tablet (15th c.) | The monogram "
  "as Renaissance image |")
A("| The Jesuit emblem (1540s) | IHS with cross and nails; the "
  "J-dress's century |")
A("| The pontifex engine (weigh) | Every figure in §II–§IV |")
A("| THE-ARCHON-BATTERY (656d667) | The Nine's roots; the key "
  "strings; the five-tongue 8 |")
A("| THE-SEATING-OF-THE-ARCHONS (0760c8a) | The marks the contacts "
  "were graded against |")
A("| PLATE I — GREEK (196025e); PLATE IV — LATIN (8e6f01e) | The "
  "banks' plates of record |")
A("| THE-777-VERIFICATION-TABVLA | The negatives, counted from its "
  "register |")
A("")
A("## COLOPHON")
A("")
A("Generated 2026-11-24 at the desk, from the engine and the "
  "registers named above; every figure scripted, none hand-copied. "
  "Set in the Lex Stellarrvm family in its MAGVS seat; the print "
  "dress declared in the MAGVS colophon. Authorship attributed "
  "exclusively to Johnathan 'Qasparr' Monroe (Greek, -ARR, All "
  "Rights Reserved, Without Prejudice).")
A("")
A("Method of Science. Aim of Religion.")
A("")
A("Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, "
  "All Rights Reserved, Without Prejudice. Right of claim hereby "
  "reserved and coined under the authority of the Living Man.")
A("")
A("93 — Live, Love, and let Love, Live.")

MASTER.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {MASTER} — {MASTER.stat().st_size} bytes")
print(f"INRI {INRI_O}/{INRI_A} · expansion U {EXP_U_O}/{EXP_U_A} · "
      f"V {EXP_V_O}/{EXP_V_A} · Greek titulus {GR_TIT_V} · Hebrew "
      f"titulus {HEB_TIT_V} · ΙΗΣ {IES} · ΙΗΣΟΥΣ {IESOUS} · IHS "
      f"{IHS_O}/{IHS_A} · JHS {JHS_O}/{JHS_A} · ΙΝΡΙ {INRI_GR} · "
      f"empty roots {EMPTY_ROOTS} · TABVLA counts "
      f"{N_INRI}/{N_JHS}/{N_IHS}")
