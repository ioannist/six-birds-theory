# Mathlib PR drafts (ClosureLadder upstream)

Base revision: `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`
Tests: `lake build` in the mathlib worktree after applying patches

## Recommended plan (2 PRs)

### PR A — Closure operator pointwise order

Proposed titles:
- `feat(Order/Closure): add pointwise order on closure operators`

Description:
- Motivation: enable comparing closure operators pointwise; useful for monotonicity results like closed-set antitonicity.
- What’s added:
  - `instance ClosureOperator.instLE : LE (ClosureOperator α)` defined pointwise
  - `ClosureOperator.le_def`
  - `ClosureOperator.isClosed_of_le`
- Safety/notes: introduces a new global `LE` instance; reviewers should consider typeclass search/diamonds. Intentionally only adds `LE` (no `Preorder`/`PartialOrder`).
- Files changed: `Mathlib/Order/Closure.lean`
- Tests: `lake build`
- AI note: “AI assistance was used for drafting; the author reviewed the changes.”
- Patch mapping: `formal/patches/mathlib/0001-Order-Closure-pointwise-order-on-closure-operators.patch`

Zulip draft (stream `#mathlib4`):
> I plan to add a global pointwise `LE (ClosureOperator α)` instance plus `ClosureOperator.isClosed_of_le` in `Mathlib/Order/Closure.lean`. Is it acceptable to add this global `LE` instance? Should we also provide `Preorder`/`PartialOrder`, or keep it minimal? Is the placement/name `ClosureOperator.instLE` OK?

### PR B — Idempotent functions + iterate lemmas

Proposed titles:
- `feat(Logic/Function): add idempotent predicate and iterate simplifications`

Description:
- Motivation: iteration of idempotent functions stabilizes after one step; these lemmas allow rewriting `f^[n] x` to `f x` when `n ≥ 1`.
- What’s added:
  - `Function.Idempotent : (α → α) → Prop` in `Mathlib/Logic/Function/Basic.lean`
  - `Function.Idempotent.iterate_succ_apply`
  - `Function.Idempotent.iterate_apply_eq` (for `1 ≤ n`)
- Notes for reviewers: please confirm preferred predicate name/location (vs existing conventions), and lemma naming/placement in `Logic/Function/Iterate`.
- Files changed: `Mathlib/Logic/Function/Basic.lean`, `Mathlib/Logic/Function/Iterate.lean`
- Tests: `lake build`
- AI note: “AI assistance was used for drafting; the author reviewed the changes.”
- Patch mapping:
  - `formal/patches/mathlib/0002-Logic-Function-define-Function.Idempotent.patch`
  - `formal/patches/mathlib/0003-Logic-Function-Iterate-idempotent-iterate-lemmas.patch`

Zulip draft (stream `#mathlib4`):
> I added `Function.Idempotent` in `Logic/Function/Basic` and two iterate lemmas in `Logic/Function/Iterate` (`iterate_succ_apply`, `iterate_apply_eq` for `1 ≤ n`). Is `Function.Idempotent` the preferred name/location, or should this reuse an existing predicate? Are the lemma names/placement acceptable?

## Alternate plan (3 PRs)

- PR A: patch `0001-Order-Closure-pointwise-order-on-closure-operators.patch`
- PR B: patch `0002-Logic-Function-define-Function.Idempotent.patch`
- PR C: patch `0003-Logic-Function-Iterate-idempotent-iterate-lemmas.patch`

## Questions to ask maintainers

- Is the global instance `LE (ClosureOperator α)` acceptable (typeclass diamonds/search concerns)?
- Should we also provide `Preorder`/`PartialOrder` instances or keep it minimal?
- Is `Function.Idempotent` the preferred name/location, or should we use an existing convention?
- Are lemma names `iterate_succ_apply` / `iterate_apply_eq` acceptable, or should they be phrased differently?
