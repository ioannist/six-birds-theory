import Mathlib.Order.Closure
import Mathlib.Order.GaloisConnection.Defs
import ClosureLadder.Basic

namespace ClosureOp

variable {α : Type u} [PartialOrder α]

abbrev incl (c : ClosureOp α) : Closed c → α :=
  fun x => x.1

abbrev reflect (c : ClosureOp α) : α → Closed c :=
  c.toCloseds

theorem reflect_le_iff (c : ClosureOp α) {x : α} {y : Closed c} :
    reflect c x ≤ y ↔ x ≤ incl c y := by
  simpa [reflect, incl] using (c.gi.gc x y)

theorem incl_reflect_eq (c : ClosureOp α) (x : α) :
    incl c (reflect c x) = c x :=
  rfl

theorem reflect_incl_eq (c : ClosureOp α) (y : Closed c) :
    reflect c (incl c y) = y := by
  simpa [reflect, incl] using (GaloisInsertion.l_u_eq (gi := c.gi) y)

section Checks

#check ClosureOperator.gi
#check GaloisInsertion.l_u_eq
#check ClosureOp.reflect_le_iff

end Checks

end ClosureOp
