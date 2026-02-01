# Zulip pitch drafts (ready to send; insert PR links)

## PR A — Closure operator pointwise order

Link: <PR_A_URL>

Short pitch:
I opened a small PR adding a pointwise `LE (ClosureOperator α)` instance plus `ClosureOperator.le_def` and `ClosureOperator.isClosed_of_le` in `Mathlib/Order/Closure.lean`. This makes it easy to compare closure operators and derive closedness monotonicity. The order is pointwise, adds no new imports, and aligns with the standard pointwise order on `OrderHom` when that module is imported.

Questions:
- Is it acceptable to add a global `LE (ClosureOperator α)` instance? Any typeclass-search/diamond concerns?
- Should I also add `Preorder`/`PartialOrder` instances, or keep it minimal?
- Is the placement/name `ClosureOperator.instLE` OK?

## PR B — Idempotent functions + iterate lemmas

Link: <PR_B_URL>

Short pitch:
This PR adds `Function.Idempotent` in `Logic/Function/Basic` and two iterate lemmas in `Logic/Function/Iterate`: `Function.Idempotent.iterate_succ_apply` and `Function.Idempotent.iterate_apply_eq` (for `1 ≤ n`). These are general (no order assumptions) and let users rewrite `f^[n] x` to `f x` for idempotent functions.

Questions:
- Is `Function.Idempotent` the preferred name/location, or should this reuse an existing predicate?
- Are the lemma names/placement acceptable, or would you prefer a different naming style (e.g., `..._of_pos`)?
