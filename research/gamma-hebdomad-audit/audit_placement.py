#!/usr/bin/env python3
# =====================================================================
# 93
# THE GAMMA–HEBDOMAD AUDIT — PLACEMENT SEAT (desk strength, by order)
#
# A Scientific Illuminist computation for the Placement Attempt: the
# house's nine Archon seats (Frame B triads; addresses I–IX; names
# none, by the Q4 ratification of 2026-11-24) laid against the seven
# gates of the audited Hebdomad plate (Gamma poles 0..-6).
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe
# (Greek, -ARR, All Rights Reserved, Without Prejudice)
# XXVI day of November, Dies Iovis, Sol in Sagittarius, Anno V:xii e.n.
# (2026 e.v.)
#
# Classification: Enterprise • Educational • Research & Development
# Method of Science, Aim of Religion
#
# Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, All
# Rights Reserved, Without Prejudice. Right of claim hereby reserved
# and coined under the authority of the Living Man.
#
# MECHANISM: seat values are the Greek bank's (Milesian) prices, as
# seated in THE-SEATING-OF-THE-ARCHONS and its Q4 ratification; gate
# residues are the recomputed residues of audit_math.py. Two frames
# are laid (Address, Triads), the gateless seats of each are printed,
# and the frames' parting is computed, not smoothed. The founder's
# guess "VRXM" is carried byte-exact and never expanded; the strings
# the construction produces are printed as computed.
#
# DOCTRINE: diplomacy and synergy, not argument (founder's order,
# 2026-11-26 09:34 EST). Contention is printed only where it carries
# proof — a computed figure or an attested text. The attempt seats
# nothing and amends no instrument; it is presented to his pen.
# =====================================================================

import json
from fractions import Fraction

def root(n):
    """Digital root, the battery's reduction."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

# The Nine, canonical address order (Q4 ratification, 2026-11-24):
# (address, seat, Milesian value)
SEATS = [
    ("I", "Α", 1), ("II", "Ε", 5), ("III", "Η", 8), ("IV", "Ι", 10),
    ("V", "Ο", 70), ("VI", "Υ", 400), ("VII", "Ω", 800),
    ("VIII", "ΕΙ", 15), ("IX", "ΟΥ", 470),
]
# Frame B triads (the Delegation's answer to Seating §XI Q1):
TRIADS = [("I", ["Α", "Ε", "Η"]), ("II", ["Ι", "ΕΙ", "Ο"]),
          ("III", ["Υ", "ΟΥ", "Ω"])]
# The seven gates: Gamma pole seats and their residues (audit_math).
GATES = [(0, Fraction(1)), (-1, Fraction(-1)), (-2, Fraction(1, 2)),
         (-3, Fraction(-1, 6)), (-4, Fraction(1, 24)),
         (-5, Fraction(-1, 120)), (-6, Fraction(1, 720))]
GATE_NAMES = ["YALDABAOTH/Saturn", "IAO/Jupiter", "SABAOTH/Mars",
              "ADONAIOS/Sun", "ELOAIOS/Mercury (plate)",
              "ORAIOS/Venus (plate)", "ASTAPHAIOS/Moon (plate)"]

OUT = {}
OUT["seats"] = [dict(address=a, seat=s, value=v, root=root(v))
                 for a, s, v in SEATS]
OUT["nine_sum"] = sum(v for _, _, v in SEATS)
OUT["nine_sum_root"] = root(OUT["nine_sum"])
OUT["triads"] = [dict(triad=t, seats=ss,
                      total=sum(dict((s, v) for _, s, v in SEATS)[s]
                                for s in ss),
                      root=root(sum(dict((s, v) for _, s, v in SEATS)[s]
                                    for s in ss)))
                 for t, ss in TRIADS]
val = {s: v for _, s, v in SEATS}

# FRAME 1 — ADDRESS: seats I..VII (the seven canonical vowels) laid
# in address order over gates 0..-6; VIII and IX stand gateless.
f1 = []
for k in range(7):
    a, s, v = SEATS[k]
    g, res = GATES[k]
    f1.append(dict(seat=s, address=a, value=v, gate=g,
                   gate_name=GATE_NAMES[k], residue=str(res)))
OUT["frame1_address"] = dict(
    pairs=f1,
    gateless=[dict(seat=s, address=a, value=v)
              for a, s, v in SEATS[7:]],
    gateless_total=sum(v for _, _, v in SEATS[7:]),
    gateless_root=root(sum(v for _, _, v in SEATS[7:])),
    gated_string="".join(s for _, s, _ in SEATS[:7]),
    gateless_string="".join(s for _, s, _ in SEATS[7:]),
)

# FRAME 2 — TRIADS: Frame B triads laid in order over gate triads
# {0,-1,-2}, {-3,-4,-5}, {-6}; within a triad, Frame B position order
# (from the Seating instrument: I: Α Ε Η; II: Ι ΕΙ Ο; III: Υ ΟΥ Ω).
gate_order = [g for g, _ in GATES]
f2_pairs, f2_gateless = [], []
gi = 0
for t, ss in TRIADS:
    for s in ss:
        if gi < len(gate_order):
            f2_pairs.append(dict(triad=t, seat=s, value=val[s],
                                 gate=gate_order[gi],
                                 gate_name=GATE_NAMES[gi]))
            gi += 1
        else:
            f2_gateless.append(dict(triad=t, seat=s, value=val[s]))
OUT["frame2_triads"] = dict(
    pairs=f2_pairs, gateless=f2_gateless,
    gateless_total=sum(d["value"] for d in f2_gateless),
    gateless_root=root(sum(d["value"] for d in f2_gateless)),
    gateless_string="".join(d["seat"] for d in f2_gateless),
)
OUT["frames_parting"] = dict(
    frame1_gateless=OUT["frame1_address"]["gateless_string"],
    frame2_gateless=OUT["frame2_triads"]["gateless_string"],
    gateless_in_both="ΟΥ",
    note="ΟΥ (IX, 470) is gateless under both frames; ΕΙ is gated only "
         "in Frame 2 (at -4, inside Triad II); Ω is gated only in "
         "Frame 1 (at -6, the last address).",
)

# THE FOUR CORNERS, first four: the dial cross's four ends (standing
# instrument): N pole 13, S pole 31, the horizontal hair's two ends,
# both at the float line's height 18 (ruling of 2026-11-24: the hair
# IS the bank boundary, one line at height 18 = 31 - 13).
OUT["corners_dial_cross"] = dict(
    ends=dict(north=13, south=31, hair_end_a=18, hair_end_b=18),
    total=13 + 31 + 18 + 18, root=root(13 + 31 + 18 + 18),
    pole_difference=31 - 13,
)
# THE FOUR CORNERS, second four: the triad grid's corners — the 3x3 of
# Frame B (rows Α Ε Η / Ι ΕΙ Ο / Υ ΟΥ Ω): Α, Η, Υ, Ω.
corners = ["Α", "Η", "Υ", "Ω"]
OUT["corners_triad_grid"] = dict(
    seats=corners, values=[val[s] for s in corners],
    roots=[root(val[s]) for s in corners],
    total=sum(val[s] for s in corners),
    root=root(sum(val[s] for s in corners)),
    string="".join(corners),
)

# ROOT FRAME, tested and set aside by its own arithmetic: the Nine's
# distinct roots are seven — the gate count — but two roots collide.
roots = [root(v) for _, _, v in SEATS]
OUT["root_frame_check"] = dict(
    roots_in_address_order=roots,
    distinct_sorted=sorted(set(roots)),
    collisions=dict(root_1=[s for (a, s, v) in SEATS if root(v) == 1],
                    root_8=[s for (a, s, v) in SEATS if root(v) == 8]),
    absent_roots=[r for r in range(1, 10) if r not in set(roots)],
    verdict="A root-to-gate bijection fails by collision: 9 seats, 7 "
            "distinct roots, 7 gates — two gates would have to be "
            "double-seated and none left gateless, against both "
            "frames above. Printed as a measured non-fit.",
)

# The founder's guess, carried byte-exact, never expanded.
OUT["founder_guess"] = dict(
    as_given="VRXM",
    treatment="Recorded byte-exact as a guess-in-formation under his "
              "Flagpole. Not expanded, not decoded, not built on. "
              "Computed strings of this construction: gated core "
              "ΑΕΗΙΟΥΩ (Frame 1); gateless ΕΙΟΥ (Frame 1) and ΟΥΩ "
              "(Frame 2); triad-grid corners ΑΗΥΩ. None spells the "
              "guess; the comparison stands as a printed observation "
              "only.",
)

with open("audit_placement.json", "w") as fh:
    json.dump(OUT, fh, indent=1, ensure_ascii=False)
print(json.dumps(OUT, indent=1, ensure_ascii=False))
print("\n93 — Live, Love, and let Love, Live.")
