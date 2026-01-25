# Empirical vs Order Closure

## Order-closure (Lean `ClosureOperator`)
- Requires a preorder/poset.
- Axioms: extensive, monotone, idempotent.
- Closed objects are fixed points of `c`.

## Idempotent endomap (no order)
- Just a function `f : α → α` with `f (f x) = f x`.
- Fixed points are still meaningful; no order is required.

## Where E_{tau,Pi} lives
- `E_{tau,Pi} : Δ(Z) → Δ(Z)` is an endomap on the probability simplex.
- We use (approx) idempotence + fixed points + metric defects.
- We do **not** assert extensiveness or monotonicity.

## Why the old stress test was ill-posed
- On the simplex, coordinatewise order is degenerate:
  if `μ, ν ∈ Δ(Z)` and `μ ≤ ν` coordinatewise, then `μ = ν` (both sum to 1).
- Therefore extensiveness `μ ≤ E(μ)` would force `E(μ) = μ` for all `μ`, i.e. `E` is the identity.
- But in general `E_{tau,Pi}(δ_z) ≠ δ_z` (e.g., coarse-grain then uniform-lift spreads mass), so extensiveness fails.

**Conclusion:** `E_{tau,Pi}` is **not** an order-theoretic closure operator on `Δ(Z)` under coordinatewise order. It is an idempotent endomap (approximate) with fixed points, unless we change the ambient order (which we are not doing).
