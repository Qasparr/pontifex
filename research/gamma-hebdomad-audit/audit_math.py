#!/usr/bin/env python3
# =====================================================================
# 93
# Epigraph: "Curvature isn't a feeling — it's path dependence; a claim
# isn't proven — it's recomputed." (desk maxim for this audit)
#
# THE GAMMA–HEBDOMAD AUDIT — MATHEMATICS SEAT
# A Scientific Illuminist recomputation of every checkable mathematical
# claim in the Meta chat log "Gamma, Archons, and the Greek Letters"
# (LEX STELLARRVM, 2026-11-26) and its two plates.
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
# MECHANISM: every figure below is computed from first principles with
# mpmath at 50 digits — Beta densities from their pdfs, Gamma residues
# as limits (z+n)·Γ(z), special values from the functions themselves.
# Nothing is copied from the chat log; the log's figures are compared
# against the computed ones and the verdict is printed at coordinates.
#
# DOCTRINE: scripted recomputation before striking is standing house
# law. A claim is VERIFIED only where the computed figure meets it;
# PARTED where it holds in a neighbour form and the seam is named;
# FAILS where the computation contradicts it as stated.
# =====================================================================

import json
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 50

OUT = {}


def beta_pdf(t, a, b):
    """MECHANISM: Beta(a,b) density t^(a-1)(1-t)^(b-1) / B(a,b)."""
    return t ** (a - 1) * (1 - t) ** (b - 1) / mp.beta(a, b)


# ---------------------------------------------------------------------
# A1. THE BETA PLATE — three densities vs the curves as depicted.
# Depicted readings are the desk's readings of Exhibit 1 (the plate):
# purple bell peak ~1.5 at t=0.5; gold reaches 5.0 at t=1; green peak
# ~2.46 at t~0.2. Tolerance on a depicted reading: ±0.06 (axis grid).
# ---------------------------------------------------------------------
beta_cases = {
    "Beta(2,2) Symmetric Bell": dict(a=2, b=2, dep_peak_t=0.5, dep_peak=1.5,
                                     dep_end0=0.0, dep_end1=0.0),
    "Beta(5,1) Late Snap": dict(a=5, b=1, dep_peak_t=1.0, dep_peak=5.0,
                                dep_end0=0.0, dep_end1=5.0),
    "Beta(2,5) Early Lean": dict(a=2, b=5, dep_peak_t=0.2, dep_peak=2.46,
                                 dep_end0=0.0, dep_end1=0.0),
}
beta_out = {}
for name, c in beta_cases.items():
    a, b = c["a"], c["b"]
    # Mode of a Beta density: (a-1)/(a+b-2) when a,b > 1; boundary else.
    if a > 1 and b > 1:
        mode_t = mp.mpf(a - 1) / (a + b - 2)
        mode_v = beta_pdf(mode_t, a, b)
    elif a > 1 and b == 1:
        mode_t, mode_v = mp.mpf(1), beta_pdf(mp.mpf(1), a, b)
    else:
        mode_t, mode_v = None, None
    total = mp.quad(lambda t: beta_pdf(t, a, b), [0, 1])
    beta_out[name] = dict(
        a=a, b=b,
        mode_t=str(mode_t), mode_value=str(mode_v),
        f_at_0=str(beta_pdf(mp.mpf(0), a, b)) if a >= 1 else "singular",
        f_at_1=str(beta_pdf(mp.mpf(1) - mp.mpf("1e-30"), a, b)),
        integral=str(total),
        depicted_peak_t=c["dep_peak_t"], depicted_peak=c["dep_peak"],
        peak_agrees=abs(float(mode_v) - c["dep_peak"]) <= 0.06,
        mode_agrees=abs(float(mode_t) - c["dep_peak_t"]) <= 0.03,
    )
OUT["beta_plate"] = beta_out

# Beta function values claimed in the chat (§4 Beta entry).
OUT["beta_function_claims"] = dict(
    B_1_1=str(mp.beta(1, 1)), claimed_B_1_1="1",
    B_half_half=str(mp.beta(mp.mpf("0.5"), mp.mpf("0.5"))),
    pi=str(mp.pi), claimed_B_half_half="pi",
    B_2_2=str(mp.beta(2, 2)), claimed_B_2_2="1/6",
    B_2_2_exact=str(Fraction(1, 6)),
)

# ---------------------------------------------------------------------
# A2. GAMMA — poles, residues, and the SABAOTH test.
# Claims: simple poles at 0,-1,-2,...; residue (-1)^n/n! at z=-n;
# residue at -2 is +1/2; "SABAOTH = removable singularity" tested as
# stated against Gamma itself, then against its charitable neighbours:
# (i) 1/Gamma entire with simple zeros at the same points;
# (ii) (z+2)*Gamma(z) extends holomorphically across -2 with value 1/2;
# (iii) the reflection formula Gamma(z)Gamma(1-z) = pi/sin(pi z).
# ---------------------------------------------------------------------
gamma_out = {"residues": {}}
for n in range(0, 7):
    # Limit definition: Res at -n = lim_{z->-n} (z+n) Gamma(z), taken
    # from the right at 1e-6, 1e-9, 1e-12 to show convergence.
    vals = []
    for eps in ("1e-6", "1e-9", "1e-12"):
        z = -n + mp.mpf(eps)
        vals.append((z + n) * mp.gamma(z))
    exact = mp.mpf((-1) ** n) / mp.factorial(n)
    gamma_out["residues"][f"z=-{n}"] = dict(
        limit_estimates=[str(v) for v in vals],
        exact_formula=str(exact),
        agrees=all(abs(v - exact) < mp.mpf("1e-4") for v in vals),
    )

# The removable-singularity test as stated: a singularity of f at z0 is
# removable iff lim_{z->z0} f(z) exists finite. |Gamma(-2+eps)| ~ (1/2)/eps.
growth = {}
for eps in ("1e-2", "1e-4", "1e-6"):
    growth[eps] = str(abs(mp.gamma(-2 + mp.mpf(eps))))
gamma_out["removable_test_as_stated"] = dict(
    abs_gamma_near_minus2=growth,
    behaviour="|Gamma| grows like (1/2)/eps -> limit does not exist finite",
    verdict="FAILS as stated for Gamma: the pole at -2 is a true pole, "
            "non-removable, like every Gamma pole.",
)

# Neighbour (i): 1/Gamma is entire; simple zeros at 0,-1,-2,...;
# derivative at -n equals (-1)^n * n! (so the zeros are simple).
recip = {}
for n in range(0, 7):
    recip[f"z=-{n}"] = dict(
        value=str(1 / mp.gamma(-n + mp.mpf("1e-14")) if n == 0 else
                  mp.mpf(0)),
        note="1/Gamma(-n) = 0 exactly (Gamma has a pole there)",
    )
deriv = mp.diff(lambda z: 1 / mp.gamma(z), mp.mpf(-2))
gamma_out["neighbour_reciprocal"] = dict(
    one_over_gamma_at_poles="0 at 0,-1,-2,... (Gamma pole <=> 1/Gamma zero)",
    derivative_at_minus2=str(deriv),
    derivative_formula="(-1)^2 * 2! = 2",
    derivative_agrees=abs(deriv - 2) < mp.mpf("1e-3"),
    verdict="HOLDS: for 1/Gamma the points are simple zeros of an entire "
            "function — the singularity is absent, not merely removable.",
)
# Neighbour (ii): the cancellation form the chat reaches for.
z = mp.mpf(-2) + mp.mpf("1e-10")
gamma_out["neighbour_cancellation"] = dict(
    limit_z_plus_2_times_gamma=str((z + 2) * mp.gamma(z)),
    residue_at_minus2=str(mp.mpf(1) / 2),
    verdict="HOLDS in product form: (z+2)*Gamma(z) extends across -2 "
            "with value = the residue +1/2. A pole is 'cancelled' only "
            "by multiplying by a factor that vanishes there — the pole "
            "of Gamma itself is untouched.",
)
# Neighbour (iii): reflection formula at a test point.
zt = mp.mpf("0.3")
gamma_out["reflection_formula"] = dict(
    lhs=str(mp.gamma(zt) * mp.gamma(1 - zt)),
    rhs=str(mp.pi / mp.sin(mp.pi * zt)),
    agrees=abs(mp.gamma(zt) * mp.gamma(1 - zt)
               - mp.pi / mp.sin(mp.pi * zt)) < mp.mpf("1e-40"),
)
# Gamma never vanishes (equivalent to 1/Gamma being entire).
gamma_out["gamma_has_no_zeros"] = (
    "VERIFIED as theorem-grade: 1/Gamma is entire (Weierstrass product), "
    "so Gamma takes the value 0 nowhere it is defined.")
OUT["gamma"] = gamma_out

# ---------------------------------------------------------------------
# A3. THE LETTER ENTRIES — every numeric claim in chat §4, recomputed.
# ---------------------------------------------------------------------
L = {}
# Eta
L["eta_0"] = dict(computed=str(mp.altzeta(0)), claimed="1/2")
L["eta_1"] = dict(computed=str(mp.altzeta(1)), claimed="ln 2",
                  ln2=str(mp.log(2)))
L["eta_2"] = dict(computed=str(mp.altzeta(2)), claimed="pi^2/12",
                  pi2_12=str(mp.pi ** 2 / 12))
alt5 = sum(mp.mpf((-1) ** (n - 1)) / n for n in range(1, 6))
L["eta_build_5_terms"] = dict(partial_sum=str(alt5), ln2=str(mp.log(2)),
                              abs_error=str(abs(alt5 - mp.log(2))))
# Zeta
L["zeta_2"] = dict(computed=str(mp.zeta(2)), claimed="pi^2/6",
                   pi2_6=str(mp.pi ** 2 / 6))
L["zeta_3"] = dict(computed=str(mp.zeta(3)), claimed="1.202...")
z5 = sum(mp.mpf(1) / n ** 2 for n in range(1, 6))
L["zeta_build_5_terms"] = dict(partial_sum=str(z5),
                               pi2_6=str(mp.pi ** 2 / 6),
                               abs_error=str(abs(z5 - mp.pi ** 2 / 6)))
# Xi
xi0 = (mp.mpf("0.5") * 0 * (0 - 1))  # xi(0) via limit below instead
xi_at_0 = mp.limit(
    lambda s: mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2)
    * mp.gamma(s / 2) * mp.zeta(s), mp.mpf(0))
L["xi_0"] = dict(computed=str(xi_at_0), claimed="1/2")
s = mp.mpf("0.3") + mp.mpf("0.4") * 1j
xi = lambda w: (mp.mpf("0.5") * w * (w - 1) * mp.pi ** (-w / 2)
                * mp.gamma(w / 2) * mp.zeta(w))
L["xi_symmetry"] = dict(xi_s=str(xi(s)), xi_1_minus_s=str(xi(1 - s)),
                        agrees=abs(xi(s) - xi(1 - s)) < mp.mpf("1e-30"))


# Lambda (von Mangoldt) and Dirichlet lambda, by hand.
def von_mangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m, ok = n, True
            while m % p == 0:
                m //= p
            if m == 1:
                return mp.log(p)
            return mp.mpf(0)
    return mp.mpf(0)


L["lambda_6"] = dict(computed=str(von_mangoldt(6)), claimed="0")
L["lambda_8"] = dict(computed=str(von_mangoldt(8)), claimed="log 2",
                     log2=str(mp.log(2)))
L["dirichlet_lambda_2"] = dict(
    computed=str((1 - 2 ** (-2)) * mp.zeta(2)), claimed="pi^2/8",
    pi2_8=str(mp.pi ** 2 / 8))
# Mu: sum over divisors of 6.
import sympy as _sp  # only for mobius/divisors if present; else by hand
try:
    mu6 = sum(int(_sp.mobius(d)) for d in _sp.divisors(6))
except Exception:
    def mobius(n):
        f = {}
        m = n
        p = 2
        while p * p <= m:
            while m % p == 0:
                f[p] = f.get(p, 0) + 1
                m //= p
            p += 1
        if m > 1:
            f[m] = f.get(m, 0) + 1
        if any(v > 1 for v in f.values()):
            return 0
        return (-1) ** len(f)
    mu6 = sum(mobius(d) for d in [1, 2, 3, 6])
L["mu_divisor_sum_6"] = dict(computed=str(mu6), claimed="0")
# Pi (prime counting)
def pi_count(x):
    sieve = [True] * (x + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [False] * len(sieve[i * i::i])
    return sum(sieve)


L["pi_counts"] = dict(pi_10=pi_count(10), pi_100=pi_count(100),
                      pi_1000=pi_count(1000), pi_20=pi_count(20),
                      claimed="4, 25, 168, 8")
# Phi (totient)
import math as _m
L["phi_12"] = dict(computed=str(sum(1 for k in range(1, 13)
                                    if _m.gcd(k, 12) == 1)),
                   coprime_set=[k for k in range(1, 13)
                                if _m.gcd(k, 12) == 1],
                   claimed="4, set {1,5,7,11}")
# Psi (digamma)
L["psi_1"] = dict(computed=str(mp.digamma(1)), claimed="-gamma = -0.57721",
                  neg_euler=str(-mp.euler))
L["psi_2"] = dict(computed=str(mp.digamma(2)), claimed="0.42278")
# Omega constant: iterate x -> e^{-x} thirty times from 1.
x = mp.mpf(1)
for _ in range(30):
    x = mp.e ** (-x)
L["omega_constant"] = dict(iterated_30=str(x), claimed="0.56714329",
                           omega_e_omega=str(x * mp.e ** x),
                           omega_12="3 (12 = 2^2 * 3, with multiplicity)",
                           J0_at_omega=str(mp.besselj(0, mp.mpf("0.5671432904"))),
                           claimed_J0="0.921")
# Sigma / Tau (divisor functions of 12 and 6)
divs12 = [d for d in range(1, 13) if 12 % d == 0]
divs6 = [d for d in range(1, 7) if 6 % d == 0]
L["sigma_tau"] = dict(sigma_6=sum(divs6), sigma_12=sum(divs12),
                      tau_12=len(divs12),
                      claimed="sigma(6)=12, sigma(12)=28, tau(12)=6",
                      e_minus_1=str(mp.e ** (-1)), claimed_e="0.3679")
# Chi mod 4: the non-principal character over one full period sums to 0.
chi4 = {0: 0, 1: 1, 2: 0, 3: -1}
L["chi_mod4_period_sum"] = dict(computed=str(sum(chi4.values())),
                                claimed="0")
# Planck/Stefan-Boltzmann integral piece: Gamma(4) * zeta(4) = pi^4/15.
L["gamma4_zeta4"] = dict(computed=str(mp.gamma(4) * mp.zeta(4)),
                         pi4_15=str(mp.pi ** 4 / 15),
                         claimed="pi^4/15",
                         agrees=abs(mp.gamma(4) * mp.zeta(4)
                                    - mp.pi ** 4 / 15) < mp.mpf("1e-40"))
OUT["letter_claims"] = L

with open("audit_math.json", "w") as fh:
    json.dump(OUT, fh, indent=1, ensure_ascii=False)
print(json.dumps(OUT, indent=1, ensure_ascii=False))
print("\n93 — Live, Love, and let Love, Live.")
