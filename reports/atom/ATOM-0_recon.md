# ATOM-0 Recon (ECT add-on: balanced dissipation ⇒ per-atom ICAP)

## Route decision
- Route A: reuse existing Lemma `lem:ect-fmem` (finite kernel mass ⇒ ICAP on truncated inputs).
- Reason: `lem:ect-fmem` already matches the incremental ICAP semantics (truncated inputs, positive work), so a new lemma is unnecessary.

## Existing relevant items (Appendix E / ECT block)
- ECT summary: `thm:ect-summary`, `rem:ect-nonimplication`.
- ICAP capacity functional: `def:ect-cap` (incremental ICAP definition).
- Finite-memory kernel mass ⇒ ICAP: `lem:ect-fmem` (truncated input/output, positive work).
- ECT mechanical lemma: `lem:ect-mech`.

## Semantics check
- `lem:ect-fmem` uses truncated inputs `u^{[s,t]}` and output `y^{[s,t]}`.
- It bounds **positive work** `W^+` on `[s,t]`.
- It assumes **integrable kernel mass** (not finite support).

## Proposed add-on IDs and labels (non-colliding)
- Definition: **D-ECT-ATOM-SS-01** — dissipative atom state/semigroup representation.
  - Label: `def:ect-atom-ss`
- Definition: **D-ECT-BAL-01** — balanced coupling condition.
  - Label: `def:ect-bal`
- Lemma: **L-ECT-BAL-KMASS-01** — decay + balance ⇒ kernel mass bound.
  - Label: `lem:ect-bal-kmass`
- Corollary: **C-ECT-BAL-ICAP-01** — kernel mass ⇒ per-atom ICAP (via `lem:ect-fmem`).
  - Label: `cor:ect-bal-icap`

## Proposed insertion location in paper.tex
- Appendix E → `sec:ect-template`
- Insert **after** `def:ect-cap` and **before** `lem:ect-fmem`.

## Existing labels to reference
- `def:ect-cap`
- `lem:ect-fmem`
- `def:tk-icap` (incremental ICAP definition)

## Note on collisions
- Existing ECT labels scanned: `def:ect-*`, `lem:ect-*`, `cor:ect-*`.
- Proposed IDs/labels are new and do not collide.
