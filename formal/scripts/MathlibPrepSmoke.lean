import ClosureLadder.MathlibPrep.ClosureOperatorOrder
import ClosureLadder.MathlibPrep.IterateIdempotent

example {α : Type} [PartialOrder α] (x : α) :
    (ClosureOperator.id α).IsClosed x := by
  simp

example {α : Type} [PartialOrder α] (x : α) :
    (ClosureOperator.id α).IsClosed x → (ClosureOperator.id α).IsClosed x := by
  intro hx
  simpa using ClosureOperator.isClosed_of_le (c := ClosureOperator.id α)
    (d := ClosureOperator.id α) (hcd := fun _ => le_rfl) (x := x) hx

example (n : Nat) (x : Nat) :
    (fun y : Nat => y)^[n + 1] x = x := by
  simpa using (Function.Idempotent.iterate_succ_apply (f := fun y : Nat => y)
    (hf := by intro y; rfl) n x)

example {n : Nat} (hn : 1 ≤ n) (x : Nat) :
    (fun y : Nat => y)^[n] x = x := by
  simpa using (Function.Idempotent.iterate_apply_eq (f := fun y : Nat => y)
    (hf := by intro y; rfl) (hn := hn) x)
