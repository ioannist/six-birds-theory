/-
Copyright (c) 2026 ClosureLadder contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: ClosureLadder contributors
-/
import Mathlib.Logic.Function.Iterate
import ClosureLadder.MathlibPrep.FunctionIdempotent
/-!
# Iteration lemmas for idempotent functions

Main statements:
* `Function.Idempotent.iterate_succ_apply`: iterates stabilize after one step.
* `Function.Idempotent.iterate_apply_eq`: all iterates with `1 ≤ n` agree with one step.

Tags: function, idempotent, iterate
-/

namespace Function.Idempotent

/-- If `f` is idempotent, all positive iterates of `f` agree with one application. -/
theorem iterate_succ_apply {α : Type u} {f : α → α} (hf : Idempotent f) (n : Nat) (x : α) :
    f^[n + 1] x = f x := by
  induction n generalizing x with
  | zero =>
      simp
  | succ n ih =>
      calc
        f^[n + 2] x = f^[n + 1] (f x) := by
          simp [Function.iterate_succ_apply]
        _ = f (f x) := by
          simpa using ih (f x)
        _ = f x := hf x

/-- If `f` is idempotent, any iterate with `1 ≤ n` equals a single application. -/
theorem iterate_apply_eq {α : Type u} {f : α → α} (hf : Idempotent f) {n : Nat} (hn : 1 ≤ n)
    (x : α) : f^[n] x = f x := by
  cases n with
  | zero =>
      cases hn
  | succ n =>
      simpa [Nat.succ_eq_add_one] using iterate_succ_apply (f := f) hf n x

end Function.Idempotent
