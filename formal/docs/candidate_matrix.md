# Candidate matrix (mathlib overlap re-validation)

All evidence collected from local mathlib checkout and Lean probe logs under `formal/logs/`.

## A. Closure operator order / closedness monotonicity

- instLEClosureOp
  - Repo decl + location: `instLEClosureOp` — `formal/ClosureLadder/Basic.lean:6`
  - Exists in mathlib? no
  - Evidence: `logs/candidate_grep.txt` shows no hits for `LE (ClosureOperator` or `inst.*LE.*ClosureOperator` in `Mathlib/Order/Closure.lean`.
  - Proposed location: `Mathlib/Order/Closure.lean`
  - Proposed name: `instLEClosureOperator` (or `instLEClosureOperator` scoped in namespace `ClosureOperator`)
  - Generalize? no; keep specific to `ClosureOperator` since it aligns with order-theoretic API

- ClosureOp.isClosed_of_le (normalized: `ClosureOperator.isClosed_of_le`)
  - Repo decl + location: `ClosureOp.isClosed_of_le` — `formal/ClosureLadder/Basic.lean:21`
  - Exists in mathlib? no
  - Evidence: `logs/candidate_grep.txt` shows no lemma named/containing `isClosed_of_le` in `Mathlib/Order/Closure.lean`.
  - Proposed location: `Mathlib/Order/Closure.lean`
  - Proposed name: `ClosureOperator.isClosed_of_le`
  - Generalize? no; statement is about closure operators and uses their `le_closure`/`isClosed_iff`

## B. Iterate stabilization for idempotent operators

- closure_iterate_succ (normalized: `ClosureOperator.iterate_succ`-style statement for idempotent `c`)
  - Repo decl + location: `closure_iterate_succ` — `formal/ClosureLadder/Basic.lean:68`
  - Exists in mathlib? no
  - Evidence: `logs/candidate_grep.txt` shows no `idempot` hits in `Mathlib/Logic/Function/Iterate.lean`.
  - Proposed location: `Mathlib/Logic/Function/Iterate.lean`
  - Proposed name: `iterate_idempotent_succ` (or similar: `idempotent.iterate_succ`)
  - Generalize? yes; statement only needs `f : α → α` with `∀ x, f (f x) = f x`

- closure_iterate_ge_one (normalized: `Function.iterate` with idempotent `f`)
  - Repo decl + location: `closure_iterate_ge_one` — `formal/ClosureLadder/Basic.lean:81`
  - Exists in mathlib? no
  - Evidence: `logs/candidate_grep.txt` shows no `idempot` hits in `Mathlib/Logic/Function/Iterate.lean`.
  - Proposed location: `Mathlib/Logic/Function/Iterate.lean`
  - Proposed name: `iterate_idempotent_ge_one`
  - Generalize? yes; this is a corollary of the generalized iterate-idempotent lemma

## C. Idempotent endomorphism packaging

- ClosureLadder.IdempotentEndo (and FixedPoints/incl/retract/incl_retract/retract_incl)
  - Repo decl + location: `ClosureLadder.IdempotentEndo` — `formal/ClosureLadder/IdempotentEndo.lean:8`
  - Exists in mathlib? no (as a structure)
  - Evidence: `logs/mathlib_name_probe.txt` shows `Function.IsFixedPt` and `Function.fixedPoints` exist; `logs/candidate_grep.txt` shows fixed point API in `Mathlib/Dynamics/FixedPoints/Basic.lean`.
  - Proposed location: drop; use existing fixed-points API (`Function.IsFixedPt`, `Function.fixedPoints`)
  - Proposed name: drop
  - Generalize? yes; if anything is upstreamed, add lemmas about fixed points of idempotent functions to `Mathlib/Dynamics/FixedPoints/Basic.lean`

- ClosureOperator.toIdempotentEndo
  - Repo decl + location: `ClosureOperator.toIdempotentEndo` — `formal/ClosureLadder/IdempotentEndo.lean:33`
  - Exists in mathlib? no (because `IdempotentEndo` is absent)
  - Evidence: `logs/mathlib_name_probe.txt` shows fixed-point API exists; no structure to map into.
  - Proposed location: drop; consider a lemma `ClosureOperator.isFixedPt_iff` or a map into `fixedPoints` if needed
  - Proposed name: drop
  - Generalize? yes; prefer statements in terms of `Function.IsFixedPt`/`fixedPoints`

