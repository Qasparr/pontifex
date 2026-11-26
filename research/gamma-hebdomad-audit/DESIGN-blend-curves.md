# DESIGN NOTE — THE BETA BLEND CURVES (toolkit seat, desk strength)

Founder's delegation 2026-11-26 09:36 EST ("if this is useful for our house
repo toolkit in anyway you know what to do with it"), routine clarified
09:38 EST: design, development, testing, proof, pushing, announcing.
Decision and reasoning printed in the showcase's §XI; this note is the
design record. Revisable by his pen.

## What it is
The Beta plate's three densities (audit Exhibit 1, claims M-01..M-03, all
VERIFIED by recomputation) seated as a small utility for the Resonantia
render chain: three named mix shapes — SYMMETRIC BELL (2,2), LATE SNAP
(5,1), EARLY LEAN (2,5) — each in two forms:
- **density_envelope(t, a, b)**: the density divided by its own peak (tops
  at exactly 1.0) — a gain-envelope shape: swell / late rise / early lean.
- **blend(t, a, b)**: the regularized incomplete beta I_t(a,b) — a
  crossfade weight 0→1 whose shape the (a,b) seat sets.

## Where it seats
`Qasparr/resonantia`: `resonance/studio/blend_curves.py` + tests at
`tests/test_blend_curves.py`, in the host repo's style (thelemic header,
mechanism comments, unittest). Pure Python (`math` only) — no new
dependency; the incomplete beta is a continued fraction (Numerical
Recipes' betacf, modified Lentz, 3e-14 tolerance).

## Inputs / Processes / Outputs / Tolerances (four-element test)
- **Inputs:** t ∈ [0,1] (clamped, never extrapolated); a seat (a, b),
  the three presets or any (a, b) with a, b ≥ 1.
- **Processes:** B(a,b) from math.gamma; density by the pdf; envelope by
  peak normalization (mode (a−1)/(a+b−2) interior, endpoint for the
  (a,1)/(1,b) seats); crossfade by the continued fraction with the
  symmetry I_t(a,b) = 1 − I_(1−t)(b,a) on the fast half.
- **Outputs:** floats in [0,1] for envelope and blend; beta_pdf returns
  the raw density (the plate's figures: peaks 1.5 / 5.0 / 2.4576).
- **Tolerances:** all three presets possess closed-form integrals
  (3t²−2t³ · t⁵ · 1−(1−t)⁵(1+5t)); the tests swear the continued
  fraction against them to 1e-10. The audio proof strike (proof_strike.py)
  renders a three-segment A→B demonstration (216 Hz → 324 Hz, the fifth
  in the 432 field) and measures the midpoint B:A ratios back out of the
  render by FFT: symmetric 0.0001 dB error, late snap 0.18 dB, early
  lean 0.13 dB against the closed forms; the strike masters at
  −13.99 LUFS / −12.08 dBTP / 320k (`proof-strike/figures.json`).

## What it is not
Not a doctrine seat: the plate's framing is not adopted, no house
instrument is amended, and no render-chain seat is obliged to call it.
The other three exhibits take no toolkit seat (Hebdomad names and the
four corners are doctrine-adjacent — witness/candidate only; the chat
PDF is a record, already filed; the Fiat Lux plate's identities are
standard mathematics, already the house's common stock).

93 — Live, Love, and let Love, Live.
