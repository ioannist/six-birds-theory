/-
Copyright (c) 2026 ClosureLadder contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: ClosureLadder contributors
-/
import Mathlib.Order.Closure
/-!
# Closure operator order lemmas

Main statements:
* `ClosureOperator.isClosed_of_le`: closedness is preserved under pointwise order.

Tags: closure operator, order, closed
-/

namespace ClosureOperator

instance instLE [Preorder α] : LE (ClosureOperator α) :=
  ⟨fun c d => ∀ x, c x ≤ d x⟩

theorem le_def [Preorder α] {c d : ClosureOperator α} : c ≤ d ↔ ∀ x, c x ≤ d x := Iff.rfl

/-- Closedness is preserved under pointwise order on closure operators. -/
theorem isClosed_of_le {α : Type u} [PartialOrder α] {c d : ClosureOperator α} (hcd : c ≤ d)
    {x : α} : d.IsClosed x → c.IsClosed x := by
  intro hx
  have hx' : d x = x := (d.isClosed_iff).1 hx
  have hcx : c x ≤ x := by
    have hcdx : c x ≤ d x := hcd x
    simpa [hx'] using hcdx
  have hxc : x ≤ c x := c.le_closure x
  exact (c.isClosed_iff).2 (le_antisymm hcx hxc)

end ClosureOperator
