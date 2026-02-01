/-
Copyright (c) 2026 ClosureLadder contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: ClosureLadder contributors
-/
import Mathlib.Logic.Function.Basic
/-!
# Idempotent functions

Main statements:
* `Function.Idempotent`: predicate for unary idempotent functions.

Tags: function, idempotent
-/

namespace Function

/-- A unary function is idempotent if applying it twice is the same as applying it once. -/
def Idempotent (f : α → α) : Prop := ∀ x, f (f x) = f x

end Function
