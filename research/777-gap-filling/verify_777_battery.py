#!/usr/bin/env python3
# =============================================================================
# "If it isn't on the page, it didn't happen." — the desk
#
# Thelemic date: Tue 2026-11-24 (Dies Martis), Sol in Sagittario,
# Anno V:xii e.n.
#
# 93.
#
# verify_777_battery.py — PHASE 2 of the 777 Verification Tabvla
# (founder's commission, 2026-11-24 13:59 EST).
#
# By Johnathan 'Qasparr' Monroe (Greek, -ARR, All Rights Reserved,
# Without Prejudice). Authorship attributed exclusively to
# Johnathan 'Qasparr' Monroe.
#
# METHOD (Scientific Illuminism):
#   Inputs    — 777-verification-register.json (Phase 1's frozen
#               extraction), the pontifex engine (the ONLY weighing
#               instrument — no hand arithmetic, no external
#               tables), and handread_decisions.json where the
#               parent desk has ruled a weighed word by reading
#               the section (each decision carries its reason).
#   Processes — CONTROLS FIRST: the engine proves itself before
#               it judges (θέλημα = 93 in the Greek bank; the
#               World Census parity battery run whole as a
#               subprocess). Then every claim is recomputed in
#               the stated tongue's proven bank. The weighed word
#               is identified ONLY from strings the section itself
#               prints, in a fixed priority (the fill's own
#               breakdown first, then its named forms, then the
#               proposal's own forms) — identification, never
#               fitting: if no printed string produces the claimed
#               value, the claim PARTS, and the register prints
#               every candidate tried with its value.
#   Outputs   — 777-verification-verified.json / .csv (the
#               register with verdicts), the hand-read queue, and
#               the summary counts on stdout.
#   Tolerances— exactly three verdicts exist: VERIFIED, PARTED,
#               NOT VERIFIABLE. The battery fails loudly on any
#               claim left unclassified, any claim whose coverage
#               mirror disagrees with the engine's own value, and
#               any section left without a roll-up verdict.
#
# DOCTRINE:
#  * Three refinements were added during the hand-read pass,
#    each on evidence printed in the corpus itself, each
#    recorded here so the instrument's history is whole:
#    (1) the C1b-gloss candidate — a proposal of the form
#    'X — the Y' weighs its gloss (XXI/22's pair proves the
#    pattern: 'Mouth' = 77 as printed, 'Right Ear' = 86);
#    (2) the C4-phrase candidate — a claim may weigh the
#    phrase its sibling proposal in the same section prints
#    (LXIII/31 bis); (3) the single-final gadol
#    characterization — a gadol delta may be exactly one
#    final's uplift, as the fill's own notes document
#    ('final nun = 700'), told apart from the full uplift
#    in the printed coordinate. Five claims the sections
#    document only in letter-name dress (שטן, מלך, ת, ⲧ, ϡ)
#    are supplied by hand-read decision, each with its
#    reason, in handread_decisions.json.
#  * A parting is data, not an accusation — printed neutrally and
#    completely, with its coordinate.
#  * Mispar gadol is NOT a seated bank in this engine. A gadol
#    claim is recomputed in the seated hechrechi bank; where the
#    delta is exactly the gadol finals uplift (the tradition's
#    stated prices 500/600/700/800/900 against the plain
#    20/40/50/80/90 — used ONLY to characterize the delta in the
#    coordinate, never as the recomputation), the coordinate
#    says so in terms.
#  * The Hebrew-fallback claims are recomputed through the
#    engine's own fallback door (weigh_via_hebrew_fallback). The
#    pinyin-fallback and PRC stroke-count claims name methods no
#    proven bank or door seats: NOT VERIFIABLE, the reason in
#    full.
#  * English ordinal and the engine's latin_ordinal bank are the
#    same 26-seat table (A=1 … Z=26); English claims verify
#    through it, the identity printed in the coordinate.
#  * Inheritance discipline: a Hebrew claim and its gadol twin on
#    the same word with no final forms are ONE weighing under two
#    labels — counted once wherever counting matters, the
#    identity printed.
#
# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
# =============================================================================

import csv
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "workspace" / "pontifex"))
from pontifex.engine import SYSTEMS, weigh, weigh_via_hebrew_fallback
from pontifex.engine import _normalize_greek

BASE = Path.home() / "workspace/pontifex/research/777-gap-filling"
REGISTER = BASE / "777-verification-register.json"
DECISIONS = BASE / "handread_decisions.json"
OUT_JSON = BASE / "777-verification-verified.json"
OUT_CSV = BASE / "777-verification-verified.csv"
QUEUE_OUT = BASE / "handread_queue.json"
PONTIFEX = Path.home() / "workspace" / "pontifex"

SCRIPT_RANGES = {
    "hebrew": [(0x0590, 0x05FF)],
    "arabic": [(0x0600, 0x06FF), (0x0750, 0x077F),
               (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)],
    "greek": [(0x0370, 0x03FF), (0x1F00, 0x1FFF)],
    "coptic": [(0x2C80, 0x2CFF), (0x03E2, 0x03EF)],
}
BANK_SCRIPT = {"hebrew": "hebrew", "hebrew_gadol": "hebrew",
               "greek": "greek", "arabic_abjad": "arabic",
               "coptic": "coptic"}
NO_DOOR = {"hebrew_pinyin_fallback", "stroke_count_prc"}
GADOL_FINALS = {"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900}
PLAIN_FINALS = {"ך": 20, "ם": 40, "ן": 50, "ף": 80, "ץ": 90}


def script_runs(text, script):
    """MECHANISM: maximal runs of characters in the script's
    Unicode ranges, in order of appearance."""
    ranges = SCRIPT_RANGES[script]
    runs, cur = [], ""
    for ch in text:
        if any(a <= ord(ch) <= b for a, b in ranges):
            cur += ch
        else:
            if cur:
                runs.append(cur)
            cur = ""
    if cur:
        runs.append(cur)
    return [r for r in runs if r]


def breakdown_words(notes):
    """MECHANISM: the fill's own printed work — segments of the
    notes are split on 'breakdown' and '|'; within a segment, the
    ordered char=value pairs spell the weighed word. A segment
    that prices letter NAMES in prose (shin=300) spells no word
    and is skipped. Returns the candidate words in order."""
    words = []
    for seg in re.split(r"breakdown|\|", notes):
        if re.search(r"[A-Za-z]{2,}\s*=\s*\d+", seg):
            continue
        pairs = re.findall(r"([^\s=+,;])\s*=\s*\d+", seg)
        if len(pairs) >= 2:
            words.append("".join(pairs))
    return words


def named_forms(notes):
    """MECHANISM: forms the notes name with a total — WORD = NNN
    or WORD=NNN — SINGLE TOKENS only, in order of appearance.
    (Prose phrases before an '=' are the notes talking, not a
    weighed form; multi-word weighed forms ride the phrase and
    dash candidates instead.)"""
    out = []
    for m in re.finditer(
            r"([A-Za-z\u0590-\u05FF\u0600-\u06FF\u0370-\u03FF"
            r"\u1F00-\u1FFF\u2C80-\u2CFF][\w\u0590-\u05FF\u0600-"
            r"\u06FF\u0370-\u03FF\u1F00-\u1FFF\u2C80-\u2CFF\-]*)"
            r"\s*=\s*\d+", notes):
        w = m.group(1).strip(" -")
        if w and " " not in w and len(w) <= 30 \
                and not re.match(r"^.\d+$", w):
            out.append(w)
    return out


def dedup(seq):
    seen, out = set(), []
    for s in seq:
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def latin_candidates(proposal, notes):
    """MECHANISM: the printed Latin forms, in fixed priority:
    the fill's breakdown word, its named forms, the segment after
    the '--' dash, the proposal as printed, the parenthetical
    transliterations, the first token, the last token."""
    cands = []
    bd = [w for w in breakdown_words(notes)
          if re.search(r"[A-Za-z]", w)]
    cands += [("C0-breakdown", w) for w in bd]
    if len(bd) >= 2:
        # a proposal naming a PAIR of powers weighs the pair:
        # the two breakdown words together (XLVI/22, XLVI/25).
        cands.append(("C0-phrase", " ".join(bd)))
    cands += [("C0-named", w) for w in named_forms(notes)
              if re.search(r"[A-Za-z]", w)]
    clean = re.sub(r"\[\d+\]", "", proposal).strip()
    if " -- " in clean:
        cands.append(("C1-postdash", clean.split(" -- ")[-1].strip()))
    for sep in (" -- ", " — "):
        if sep in clean:
            # the gloss after the dash is a documented weighed
            # form in this corpus ('Maat — the Right Ear' weighs
            # its gloss; the sibling proposal in XXI/22 weighs
            # 'Mouth' the same way) — with and without its
            # article.
            seg = clean.split(sep)[-1].strip()
            cands.append(("C1b-gloss", seg))
            if seg.lower().startswith("the "):
                cands.append(("C1b-gloss", seg[4:]))
    cands.append(("C2-full", clean))
    for paren in re.findall(r"\(([^)]*)\)", clean):
        if re.search(r"[A-Za-z]", paren):
            cands.append(("C3-paren", paren.strip()))
    toks = clean.split()
    if toks:
        cands.append(("C4-first", toks[0].strip("(),")))
        cands.append(("C5-last", toks[-1].strip("(),")))
    seen, out = set(), []
    for rule, w in cands:
        if w and w not in seen:
            seen.add(w)
            out.append((rule, w))
    return out


def script_candidates(proposal, notes, bridge, script,
                      section_text=""):
    """MECHANISM: the printed forms in the bank's script, in
    fixed priority: breakdown words, named forms, the proposal's
    own runs, the notes' runs, the bridge line's runs, and last
    the whole section's runs (workers cross-referenced within a
    section; a section-wide source is recorded as C4 so the
    parent can audit it)."""
    cands = []
    cands += [("C0-breakdown", w) for w in breakdown_words(notes)
              if script_runs(w, script) == [w] and w]
    cands += [("C0-named", w) for w in named_forms(notes)
              if script_runs(w, script) and len(w) >= 2]
    cands += [("C1-proposal", w) for w in script_runs(proposal, script)]
    cands += [("C2-notes", w) for w in script_runs(notes, script)]
    cands += [("C3-bridge", w) for w in script_runs(bridge, script)]
    # the phrase candidate is built from WORD runs only (length
    # >= 2): single letters in the notes are breakdown debris
    # (ע=70, ة, ه), and appending them would manufacture values
    # the fill never claimed — the battery identified exactly
    # that false match in its first pass and refuses it here.
    word_runs = [w for w in (script_runs(proposal, script)
                             + script_runs(notes, script)
                             + script_runs(bridge, script))
                 if len(w) >= 2]
    if len(word_runs) >= 2:
        # names in these columns are PHRASES (A'arab Zaraq =
        # ערב זרק; Adam Kadmon = אדם קדמון; the jinn kings' names
        # run to three words): the runs together are a candidate.
        cands.append(("C3-phrase", " ".join(word_runs)))
    cands += [("C4-section", w)
              for w in script_runs(section_text, script)]
    sec_runs = [w for w in script_runs(section_text, script)
                if len(w) >= 2]
    if len(sec_runs) >= 2:
        # the section-wide phrase: a claim may weigh a name its
        # sibling proposal in the same section prints (LXIII/31
        # bis, the gadol twin of the phrase claim beside it).
        cands.append(("C4-phrase", " ".join(sec_runs)))
    seen, out = set(), []
    for rule, w in cands:
        key = w if script != "coptic" else w
        if w and key not in seen:
            seen.add(key)
            out.append((rule, w))
    return out


def prepare(word, system):
    """MECHANISM: the engine's own preparation, mirrored so the
    coverage walk sees exactly the letters the engine weighed."""
    if system in ("latin_ordinal", "agrippa", "armenian",
                  "cyrillic", "glagolitic"):
        return word.upper()
    if system == "greek":
        return _normalize_greek(word)
    if system == "coptic":
        return word.casefold()
    return word


def coverage(word, system):
    """MECHANISM: walk the prepared word against the engine's
    table exactly as weigh() does (pair keys first), returning
    (value, skipped_chars). The battery asserts this value equals
    weigh()'s — the mirror may describe the weighing, never
    replace it."""
    table = SYSTEMS[system]["table"]
    w = prepare(word, system)
    total, skipped, i = 0, [], 0
    while i < len(w):
        pair = w[i:i + 2]
        if pair in table:
            total += table[pair]
            i += 2
            continue
        ch = w[i]
        if ch in table:
            total += table[ch]
        else:
            skipped.append(ch)
        i += 1
    return total, skipped


def skipped_letters(skipped):
    """MECHANISM: of the skipped characters, the ones that are
    letters (spaces and punctuation are the fills' own printed
    'skipped:' lists and carry no weight either way)."""
    return [c for c in skipped if c.isalpha()]


def weigh_checked(word, system):
    """MECHANISM: the value comes from the engine; the coverage
    mirror is asserted against it on every call."""
    result = weigh(word, system)
    mirror, skipped = coverage(word, system)
    assert mirror == result["value"], \
        f"coverage mirror diverges: {word!r} {system} " \
        f"{mirror} != {result['value']}"
    return result["value"], skipped


def verify_claim(claim, proposal, notes, bridge, decisions, queue,
                 section, p_idx):
    """MECHANISM: one claim -> verdict, recomputed value, weighed
    word, word source, coordinate. Exactly three verdicts."""
    bank = claim["bank_engine"]
    claimed = claim["claimed_value"]
    key = f"S{section['section_idx']:03d}-P{p_idx}-C{claim['claim_idx']}"
    out = {"claim_key": key, "verdict": None, "recomputed": None,
           "weighed_word": "", "word_source": "", "coordinate": ""}

    if bank in NO_DOOR:
        out["verdict"] = "NOT VERIFIABLE"
        if bank == "hebrew_pinyin_fallback":
            out["coordinate"] = (
                "The stated method is the pinyin fallback (a "
                "Chinese name's pinyin syllables carried into "
                "Hebrew letters by the worker's scheme); no proven "
                "bank or engine door seats that method, so the "
                "claim cannot be recomputed in a proven tongue. "
                "The engine's plain Hebrew fallback door is a "
                "different scheme and is not substituted for it.")
        else:
            out["coordinate"] = (
                "The stated method is PRC stroke-count (the "
                "character's stroke total under the PRC standard); "
                "no proven bank in the engine seats a stroke "
                "table, so the claim cannot be recomputed in a "
                "proven tongue.")
        return out

    decision = decisions.get(key)
    hand_word = decision["weighed_word"] if decision else None

    if bank in BANK_SCRIPT:
        script = BANK_SCRIPT[bank]
        cands = script_candidates(proposal, notes, bridge, script,
                                  section["section_text"])
        if hand_word:
            cands = [("HAND-READ", hand_word)] + cands
        if not cands:
            out["verdict"] = "NOT VERIFIABLE"
            coord = (
                f"No word in the {script} script is printed "
                f"anywhere in this section; the claim rests on "
                f"a transliteration the section does not print, "
                f"so it cannot be recomputed in the stated bank.")
            if bank in ("hebrew", "hebrew_gadol"):
                # the engine's one transliteration door, printed
                # as a coordinate — never substituted for the
                # stated bank's verification. The door's input is
                # the proposal's headword token (a multi-name
                # proposal has no single door input and gets
                # none).
                door_word = None
                # the fill's own documented weighed form
                # outranks every other door input ('Weighed
                # compact KARMAYOGA', the XXIV notes say) — it
                # is the word the claim actually weighs.
                named = re.search(
                    r"[Ww]eighed compact ([A-Za-z]+)"
                    r"|[Ww]eighing ([A-Za-z]+)"
                    r"|[Tt]ransliteration ([A-Za-z][A-Za-z]+)",
                    notes)
                if named:
                    door_word = next(g for g in named.groups()
                                     if g)
                toks = re.sub(r"\[\d+\]", "", proposal).split()
                if door_word is None and len(toks) <= 3:
                    for _, lw in latin_candidates(proposal, notes):
                        if " " not in lw and "(" not in lw:
                            door_word = lw
                            break
                if door_word:
                    door = weigh_via_hebrew_fallback(door_word)
                    lw = door_word
                    coord += (
                        f" Coordinate, not verification: the "
                        f"engine's Latin-to-Hebrew fallback door "
                        f"renders {lw} as {door['rendering']} = "
                        f"{door['value']} in the seated hechrechi "
                        f"bank")
                    if bank == "hebrew_gadol":
                        uplift = sum(
                            GADOL_FINALS[c] - PLAIN_FINALS[c]
                            for c in door["rendering"]
                            if c in GADOL_FINALS)
                        coord += (
                            "; with gadol finals on the door's "
                            f"rendering, "
                            f"{door['value'] + uplift}")
                    coord += "."
            else:
                coord += (
                    f" No engine door seats a Latin-to-{script} "
                    f"transliteration.")
            out["coordinate"] = coord
            queue.append({"claim_key": key,
                          "cell_id": section["cell_id"],
                          "bank": bank, "claimed": claimed,
                          "reason": "no script candidate"})
            return out
        system = "hebrew" if bank == "hebrew_gadol" else bank
        local = [(r, w) for r, w in cands if not r.startswith("C4")]
        sect = [(r, w) for r, w in cands if r.startswith("C4")]
        values = []
        for rule, w in local + sect:
            v, skipped = weigh_checked(w, system)
            values.append((rule, w, v, skipped))
        hit = next(((r, w, v, s) for r, w, v, s in values
                    if v == claimed), None)
        if not hit and bank == "hebrew_gadol":
            # a gadol claim whose word is printed in the section
            # (a sibling proposal's notes) and whose delta is
            # exactly a gadol finals uplift PARTS with that
            # coordinate — it is not unverifiable, it is priced
            # in an unseated bank. Two applications are told
            # apart: the full uplift (every final at gadol) and
            # the single-final uplift (LXIII/31 bis, whose own
            # notes document 'final nun = 700' and nothing
            # more: אדם קדמון parts at the nun alone).
            for r, w, v, s in values:
                uplift = sum(GADOL_FINALS[c] - PLAIN_FINALS[c]
                             for c in w if c in GADOL_FINALS)
                if uplift and v + uplift == claimed:
                    out.update(
                        verdict="PARTED", recomputed=v,
                        weighed_word=w, word_source=r,
                        coordinate=(
                            f"claimed {claimed}; the word {w} "
                            f"is printed in the section and "
                            f"weighs {v} in the seated hechrechi "
                            f"bank; the delta is exactly the "
                            f"mispar gadol finals uplift "
                            f"({v} + {uplift} = {claimed}): the "
                            f"claim holds only under mispar "
                            f"gadol, a bank this engine does "
                            f"not seat"))
                    return out
                for c in dict.fromkeys(
                        ch for ch in w if ch in GADOL_FINALS):
                    one = GADOL_FINALS[c] - PLAIN_FINALS[c]
                    if v + one == claimed:
                        out.update(
                            verdict="PARTED", recomputed=v,
                            weighed_word=w, word_source=r,
                            coordinate=(
                                f"claimed {claimed}; the word "
                                f"{w} is printed in the section "
                                f"and weighs {v} in the seated "
                                f"hechrechi bank; the delta is "
                                f"exactly the gadol uplift of "
                                f"the final {c} alone "
                                f"({v} + {one} = {claimed}), as "
                                f"the fill's own notes document "
                                f"it; full mispar gadol (every "
                                f"final uplifted) would give "
                                f"{v + uplift}. The claim holds "
                                f"under neither the seated bank "
                                f"nor full gadol, but under a "
                                f"single-final gadol application "
                                f"this engine does not seat"))
                        return out
        if not hit and not local:
            # the claim's own proposal prints no word in the
            # script; a section-mate's word cannot part it.
            out["verdict"] = "NOT VERIFIABLE"
            named = "; ".join(f"{w} = {v}" for _, w, v, _ in values)
            out["coordinate"] = (
                f"No word in the {script} script is printed in "
                f"this claim's own proposal; the claim rests on "
                f"a transliteration the proposal does not print. "
                f"Words in the script printed elsewhere in the "
                f"section weigh: {named} — none is this claim's "
                f"word.")
            queue.append({"claim_key": key,
                          "cell_id": section["cell_id"],
                          "bank": bank, "claimed": claimed,
                          "reason": "no script candidate (own "
                                    "proposal)"})
            return out
        if hit:
            rule, w, v, skipped = hit
            out.update(verdict="VERIFIED", recomputed=v,
                       weighed_word=w, word_source=rule)
            coord = []
            letters = skipped_letters(skipped)
            if letters:
                coord.append(
                    "letters carrying no price in the seated "
                    "bank and skipped in silence: "
                    + " ".join(letters))
            if bank == "hebrew_gadol":
                finals = [c for c in w if c in GADOL_FINALS]
                if not finals:
                    coord.append(
                        "mispar gadol is not a seated bank in "
                        "this engine; the word carries no final "
                        "forms, so gadol and the seated hechrechi "
                        "bank coincide on it exactly")
                else:
                    coord.append(
                        "verified in the seated hechrechi bank")
            out["coordinate"] = "; ".join(coord)
            return out
        # no candidate produced the claimed value. The primary
        # form — the one the recomputation is stated on — is the
        # phrase when the proposal itself prints a multi-word
        # name in the script, else the first candidate.
        primary = values[0]
        prop_runs = [w for w in script_runs(proposal, script)
                     if len(w) >= 2]
        if len(prop_runs) >= 2:
            for entry in values:
                if entry[0] == "C3-phrase":
                    primary = entry
                    break
        else:
            # the proposal's own printed word outranks breakdown
            # debris (a segment pricing ة and ه to explain a
            # convention is not the weighed word).
            for entry in values:
                if entry[0] == "C1-proposal":
                    primary = entry
                    break
        rule, w, v, skipped = primary
        out.update(verdict="PARTED", recomputed=v,
                   weighed_word=w, word_source=rule)
        tried = "; ".join(f"{r} {w!r}={vv}" for r, w, vv, _ in values)
        coord = [f"claimed {claimed}; recomputed {v} on the "
                 f"primary printed form; candidates tried: {tried}"]
        if bank == "hebrew_gadol":
            uplift = sum(GADOL_FINALS[c] - PLAIN_FINALS[c]
                         for c in w if c in GADOL_FINALS)
            if uplift and v + uplift == claimed:
                coord.append(
                    "the delta is exactly the mispar gadol "
                    "finals uplift: the claim holds only under "
                    "mispar gadol (finals priced 500-900), a "
                    "bank this engine does not seat; in the "
                    "seated hechrechi bank the word weighs "
                    f"{v}")
            else:
                for c in dict.fromkeys(
                        ch for ch in w if ch in GADOL_FINALS):
                    one = GADOL_FINALS[c] - PLAIN_FINALS[c]
                    if v + one == claimed:
                        coord.append(
                            f"the delta is exactly the gadol "
                            f"uplift of the final {c} alone "
                            f"({v} + {one} = {claimed}); full "
                            f"mispar gadol would give "
                            f"{v + uplift}: a single-final "
                            f"gadol application, which this "
                            f"engine does not seat")
                        break
        if bank == "arabic_abjad":
            # the fills' own recorded conventions, printed in
            # their notes ('standard abjad reads ة as ه';
            # 'hamza-alif=1'): characterize the delta against
            # them — characterization, never the recomputation.
            n_ta = w.count("ة")
            n_hamza = sum(w.count(c) for c in "أإآ")
            if n_ta and claimed - v == 5 * n_ta:
                coord.append(
                    f"the delta is exactly ة priced as ه (5 "
                    f"each, {n_ta} in the word): the fill's "
                    f"recorded convention, printed in its own "
                    f"notes; the seated abjad bank prices ة "
                    f"not at all, and on the priced letters "
                    f"the word weighs {v}")
            elif n_hamza and claimed - v == n_hamza:
                coord.append(
                    f"the delta is exactly the hamza-alif "
                    f"priced as alif (1 each, {n_hamza} in the "
                    f"word): a convention one fill in this "
                    f"corpus states on its face ('hamza-alif"
                    f"=1'); the seated abjad bank does not "
                    f"price the hamza carriers, and on the "
                    f"priced letters the word weighs {v}")
        letters = skipped_letters(skipped)
        if letters:
            coord.append("letters with no price in the seated "
                         "bank: " + " ".join(letters))
        out["coordinate"] = "; ".join(coord)
        queue.append({"claim_key": key, "cell_id": section["cell_id"],
                      "bank": bank, "claimed": claimed,
                      "reason": "PARTED — parent eyeball"})
        return out

    if bank == "hebrew_fallback":
        cands = latin_candidates(proposal, notes)
        if hand_word:
            cands = [("HAND-READ", hand_word)] + cands
        if not cands:
            out["verdict"] = "NOT VERIFIABLE"
            out["coordinate"] = ("No Latin form is printed for "
                                 "the fallback door to carry.")
            return out
        values = []
        for rule, w in cands:
            door = weigh_via_hebrew_fallback(w)
            values.append((rule, w, door["value"], door["rendering"]))
        hit = next(((r, w, v, rend) for r, w, v, rend in values
                    if v == claimed), None)
        if hit:
            rule, w, v, rend = hit
            out.update(verdict="VERIFIED", recomputed=v,
                       weighed_word=w, word_source=rule,
                       coordinate=f"through the engine's Hebrew "
                                  f"fallback door: {w} -> {rend} "
                                  f"= {v}")
            return out
        rule, w, v, rend = values[0]
        out.update(verdict="PARTED", recomputed=v,
                   weighed_word=w, word_source=rule)
        coord = [f"claimed {claimed}; the engine's fallback door "
                 f"renders {w} as {rend} = {v}"]
        # the fill may document its own rendering in the notes;
        # verify that rendering in the Hebrew bank and print it.
        for _, hw in script_candidates(proposal, notes, bridge,
                                       "hebrew"):
            hv, _ = weigh_checked(hw, "hebrew")
            if hv == claimed:
                coord.append(
                    f"the rendering the fill itself documents, "
                    f"{hw}, weighs {hv} in the seated Hebrew "
                    f"bank — the parting is between the fill's "
                    f"documented phonetic scheme and the engine "
                    f"door's rendering, at the letters printed")
                break
        out["coordinate"] = "; ".join(coord)
        queue.append({"claim_key": key, "cell_id": section["cell_id"],
                      "bank": bank, "claimed": claimed,
                      "reason": "PARTED — parent eyeball"})
        return out

    # Latin-family banks: latin_ordinal, agrippa, english_ordinal
    system = "latin_ordinal" if bank == "english_ordinal" else bank
    cands = latin_candidates(proposal, notes)
    if hand_word:
        cands = [("HAND-READ", hand_word)] + cands
    if not cands:
        out["verdict"] = "NOT VERIFIABLE"
        out["coordinate"] = "No Latin form is printed in the section."
        return out
    values = []
    for rule, w in cands:
        v, skipped = weigh_checked(w, system)
        values.append((rule, w, v, skipped))
    hit = next(((r, w, v, s) for r, w, v, s in values
                if v == claimed), None)
    if hit:
        rule, w, v, skipped = hit
        out.update(verdict="VERIFIED", recomputed=v,
                   weighed_word=w, word_source=rule)
        coord = []
        if bank == "english_ordinal":
            coord.append(
                "English ordinal and the engine's latin_ordinal "
                "bank are the same 26-seat table (A=1 … Z=26); "
                "verified through it")
        letters = skipped_letters(skipped)
        if letters:
            coord.append("letters carrying no price in the "
                         "seated bank and skipped in silence: "
                         + " ".join(letters))
        out["coordinate"] = "; ".join(coord)
        return out
    rule, w, v, skipped = values[0]
    out.update(verdict="PARTED", recomputed=v,
               weighed_word=w, word_source=rule)
    tried = "; ".join(f"{r} {w2!r}={vv}" for r, w2, vv, _ in values)
    coord = [f"claimed {claimed}; recomputed {v} on the primary "
             f"printed form; candidates tried: {tried}"]
    letters = skipped_letters(skipped)
    if letters:
        coord.append("letters with no price in the seated bank: "
                     + " ".join(letters))
    out["coordinate"] = "; ".join(coord)
    queue.append({"claim_key": key, "cell_id": section["cell_id"],
                  "bank": bank, "claimed": claimed,
                  "reason": "PARTED — parent eyeball"})
    return out


def main():
    # CONTROLS FIRST — the instrument proves itself before it
    # judges: the house control weighing, then the World Census
    # parity battery whole, as a subprocess.
    control = weigh("θελημα", "greek")["value"]
    print(f"control: θέλημα in the Greek bank = {control}")
    assert control == 93, "control weighing fails — engine unproven"
    proc = subprocess.run(
        [sys.executable, "test_census_parity.py"],
        cwd=str(PONTIFEX), capture_output=True, text=True,
        env={"PATH": "/usr/bin:/bin:/usr/local/bin",
             "PYTHONPATH": str(Path.home() / ".local/lib/"
                               "python3.12/site-packages") + ":" +
             str(PONTIFEX)})
    tail = (proc.stdout.strip().splitlines() or [""])[-1]
    print(f"control: census parity battery — {tail} "
          f"(exit {proc.returncode})")
    assert proc.returncode == 0, "census parity control fails"

    entries = json.loads(REGISTER.read_text(encoding="utf-8"))
    decisions = {}
    if DECISIONS.exists():
        decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
        print(f"hand-read decisions loaded: {len(decisions)}")
    queue = []
    counts = {"VERIFIED": 0, "PARTED": 0, "NOT VERIFIABLE": 0}
    by_bank = {}
    twin_count = 0

    for e in entries:
        verdicts = []
        for p in e["proposals"]:
            # inheritance discipline: hebrew + gadol on one word
            heb = [c for c in p["claims"]
                   if c["bank_engine"] == "hebrew"]
            gad = [c for c in p["claims"]
                   if c["bank_engine"] == "hebrew_gadol"]
            results = []
            for c in p["claims"]:
                r = verify_claim(c, p["proposal_raw"], p["notes"],
                                 p["bridge"], decisions, queue, e,
                                 p["proposal_idx"])
                c.update(r)
                results.append(r)
                counts[r["verdict"]] += 1
                by_bank.setdefault(c["bank_engine"],
                                   {"VERIFIED": 0, "PARTED": 0,
                                    "NOT VERIFIABLE": 0})
                by_bank[c["bank_engine"]][r["verdict"]] += 1
                verdicts.append(r["verdict"])
            if heb and gad:
                hw = next((r["weighed_word"] for r, c in
                           zip(results, p["claims"])
                           if c["bank_engine"] == "hebrew"), "")
                if hw and not any(ch in GADOL_FINALS for ch in hw):
                    twin_count += 1
        if e["kind"] in ("INTENTIONALLY_EMPTY", "TRANSCRIPTION_GAP"):
            e["section_verdict"] = "NOT VERIFIABLE"
            e["section_coordinate"] = (
                "certified intentionally empty — no weighing "
                "claim is stated; the emptiness is the finding"
                if e["kind"] == "INTENTIONALLY_EMPTY" else
                "unfillable transcription gap — the source glyph "
                "did not survive transcription, so no weighing "
                "claim is stated or can be recomputed")
        elif any(v == "PARTED" for v in verdicts):
            e["section_verdict"] = "PARTED"
            e["section_coordinate"] = ""
        elif any(v == "NOT VERIFIABLE" for v in verdicts):
            e["section_verdict"] = "NOT VERIFIABLE"
            e["section_coordinate"] = (
                "verified in part: every stated claim that a "
                "proven bank seats is verified; the remainder "
                "names a method no proven bank seats")
        else:
            e["section_verdict"] = "VERIFIED"
            e["section_coordinate"] = ""

    total = sum(counts.values())
    print(f"claims classified: {total} (must be 504)")
    assert total == 504, "unclassified claims remain"
    print("verdicts:", counts)
    print("by bank:")
    for b in sorted(by_bank):
        print(f"  {b}: {by_bank[b]}")
    print(f"hebrew/gadol one-weighing-two-labels twins: {twin_count}")
    sec_counts = {}
    for e in entries:
        sec_counts[e["section_verdict"]] = \
            sec_counts.get(e["section_verdict"], 0) + 1
    print("section verdicts:", sec_counts)
    assert len(entries) == 221
    assert all(e.get("section_verdict") for e in entries)

    OUT_JSON.write_text(json.dumps(entries, ensure_ascii=False,
                                   indent=1), encoding="utf-8")
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["claim_key", "section_idx", "cell_id", "column",
                    "section_kind", "section_verdict", "proposal_idx",
                    "proposal_raw", "claim_idx", "bank_label_raw",
                    "bank_engine", "claimed_value",
                    "claim_variant_note", "tier_printed",
                    "weighed_word", "word_source", "recomputed",
                    "verdict", "coordinate", "bridge", "worker"])
        for e in entries:
            if not e["proposals"]:
                w.writerow(["", e["section_idx"], e["cell_id"],
                            e["column"], e["kind"],
                            e["section_verdict"], "", "", "", "",
                            "", "", "", "", "", "", "", "",
                            e["section_coordinate"], "", ""])
            for p in e["proposals"]:
                for c in p["claims"]:
                    w.writerow([c["claim_key"], e["section_idx"],
                                e["cell_id"], e["column"], e["kind"],
                                e["section_verdict"],
                                p["proposal_idx"], p["proposal_raw"],
                                c["claim_idx"], c["bank_label_raw"],
                                c["bank_engine"], c["claimed_value"],
                                c["claim_variant_note"],
                                c["tier_printed"], c["weighed_word"],
                                c["word_source"], c["recomputed"],
                                c["verdict"], c["coordinate"],
                                p["bridge"], p["worker"]])
    QUEUE_OUT.write_text(json.dumps(queue, ensure_ascii=False,
                                    indent=1), encoding="utf-8")
    print(f"hand-read queue: {len(queue)} items")
    print(f"wrote {OUT_JSON}, {OUT_CSV}, {QUEUE_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Live, Love, and let Love, Live. — 93.
# All Rights Reserved, Without Prejudice.
