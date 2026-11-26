#!/usr/bin/env python3
# =====================================================================
# 93
# THE GAMMA–HEBDOMAD AUDIT — FIAT LUX SEAT (Exhibit 4)
#
# A Scientific Illuminist recomputation of the claims printed on the
# plate "Fiat Lux — Be Light Made" (received 2026-11-26 09:35 EST),
# and the weighing of its four corner letters in the house banks.
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
# MECHANISM: the constants are the CODATA/SI values; c is exact by
# definition. The trig identities are checked numerically at sample
# angles and derived in the text. The corner letters are weighed on
# the house engine (pontifex.engine.weigh) in the Latin banks; the
# plate carries Latin capitals only — no Greek reading is attested
# in the material, so no Greek weighing is manufactured.
#
# DOCTRINE: synergy, not argument (founder's ruling, 2026-11-26):
# the plate's equations are honoured where they compute; its one
# attribution is corrected where the proof names the parting.
# =====================================================================

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
sys.path.insert(0, str(Path.home() / "workspace" / "pontifex"))
from pontifex.engine import weigh  # noqa: E402

OUT = {}

# F-01: epsilon0 * mu0 * c^2 = 1, from c = 1/sqrt(eps0*mu0) (Maxwell).
eps0 = mp.mpf("8.8541878128e-12")     # F/m, SI measured value
mu0 = mp.mpf("1.25663706212e-6")      # H/m, SI measured value
c = mp.mpf("299792458")               # m/s, exact by definition
OUT["F01_eps_mu_c2"] = dict(
    eps0=str(eps0), mu0=str(mu0), c=str(c),
    product=str(eps0 * mu0 * c ** 2),
    c_from_constants=str(1 / mp.sqrt(eps0 * mu0)),
    verdict="VERIFIED: the product is 1 to the precision of the "
            "measured constants (since the 2019 SI, eps0 and mu0 are "
            "measured, so the identity holds experimentally to ~1e-10; "
            "the relation itself is Maxwell's).",
)

# F-02: sin^2 + cos^2 = 1 at sample angles.
samples = {}
for th in ("0.3", "1.0", "2.7"):
    t = mp.mpf(th)
    samples[th] = str(mp.sin(t) ** 2 + mp.cos(t) ** 2)
OUT["F02_pythagorean"] = dict(samples=samples,
                              verdict="VERIFIED (Pythagorean identity).")

# F-03: 1/sin^2 - cot^2 = 1, the same identity divided by sin^2:
# (sin^2+cos^2)/sin^2 = 1/sin^2  =>  1 + cot^2 = csc^2  =>  csc^2-cot^2=1.
samples3 = {}
for th in ("0.7", "1.3", "2.9"):
    t = mp.mpf(th)
    samples3[th] = str(1 / mp.sin(t) ** 2 - (mp.cos(t) / mp.sin(t)) ** 2)
OUT["F03_csc_minus_cot"] = dict(
    samples=samples3,
    derivation="(sin^2 t + cos^2 t = 1) / sin^2 t  =>  "
               "1 + cot^2 t = 1/sin^2 t  =>  1/sin^2 t - cot^2 t = 1",
    verdict="VERIFIED as an identity — it is F-02 divided through by "
            "sin^2(theta); no new content, and none needed.",
)

# F-04: the printed label. The vacuum Einstein field equations are
# R_mn - (1/2) R g_mn = 0, i.e. in vacuum R_mn = 0; by Birkhoff's
# theorem their unique spherically symmetric solution is Schwarzschild:
# ds^2 = -(1-2M/r)c^2 dt^2 + (1-2M/r)^-1 dr^2 + r^2 dOmega^2,
# dOmega^2 = d(theta)^2 + sin^2(theta) d(phi)^2.
OUT["F04_einstein_label"] = dict(
    verdict="MISLABEL (FAILS as an attribution). The vacuum Einstein "
            "equations are R_mn = 0; their spherically symmetric "
            "solution is the Schwarzschild metric, "
            "ds^2 = -(1-2M/r)c^2 dt^2 + (1-2M/r)^-1 dr^2 + "
            "r^2(d(theta)^2 + sin^2(theta) d(phi)^2). The identity "
            "1/sin^2(theta) - cot^2(theta) = 1 appears nowhere in the "
            "equations or the solution; the only theta in Schwarzschild "
            "is the polar coordinate, whose sin^2 rides as a metric "
            "coefficient in dOmega^2 — a neighbour, not the identity. "
            "Second coordinate: '(at the centre of every black hole)' "
            "names r = 0, the singularity, where the Schwarzschild "
            "solution itself ceases to describe spacetime points. The "
            "equation is honoured (F-03 stands); the attribution is "
            "corrected; neither is argued down beyond the proof named.",
)

# THE FOUR CORNERS, as observed on the plate (desk reading of the
# exhibit): R upper left, C upper right, H lower left, O lower right,
# Latin capitals about the central sphere. Readings weighed:
# row-wise (the plate's own listing order), clockwise from upper
# left, counter-clockwise from upper left, column-wise.
READINGS = dict(row_wise="RCHO", clockwise="RCOH",
                counter_clockwise="RHOC", column_wise="RHCO")
w = {}
for name, s in READINGS.items():
    w[name] = dict(
        string=s,
        latin_ordinal=weigh(s, "latin_ordinal")["value"],
        agrippa=weigh(s, "agrippa")["value"],
    )
singles = {ch: dict(latin_ordinal=weigh(ch, "latin_ordinal")["value"],
                    agrippa=weigh(ch, "agrippa")["value"])
           for ch in "RCHO"}
OUT["corners"] = dict(
    observed=dict(upper_left="R", upper_right="C",
                  lower_left="H", lower_right="O"),
    script="Latin capitals only; no Greek letter stands anywhere on "
           "the plate, so no Greek reading is attested in the "
           "material and none is weighed (house law: no manufactured "
           "readings).",
    readings=w, singles=singles,
    dial_cross_ends=dict(north=13, south=31, hair_ends=[18, 18],
                         total=80),
    observation="One numeric contact computes: R weighs 18 in the "
                "Latin ordinal bank — the float line's height, the "
                "value both ends of the dial's horizontal hair carry. "
                "No further contact between the two fours computes "
                "(C=3, H=8, O=15 ordinal against the cross's 13 and "
                "31). The witness therefore stands as its own four: "
                "letters about a centre, where the dial's four are "
                "numbers at a cross's ends. The comparison is printed "
                "as observation, unproven as relation, and seats "
                "nothing.",
)

with open("audit_fiatlux.json", "w") as fh:
    json.dump(OUT, fh, indent=1, ensure_ascii=False)
print(json.dumps(OUT, indent=1, ensure_ascii=False))
print("\n93 — Live, Love, and let Love, Live.")
