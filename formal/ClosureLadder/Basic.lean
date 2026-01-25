import Mathlib.Order.Closure
import Mathlib.Logic.Function.Iterate

abbrev ClosureOp (α : Type u) [Preorder α] := ClosureOperator α

instance {α : Type u} [Preorder α] : LE (ClosureOp α) :=
  ⟨fun c d => forall x, c x <= d x⟩

namespace ClosureOp

def IsClosed {α : Type u} [Preorder α] (c : ClosureOp α) (x : α) : Prop :=
  ClosureOperator.IsClosed c x

abbrev Closed {α : Type u} [PartialOrder α] (c : ClosureOp α) := c.Closeds

theorem isClosed_iff {α : Type u} [Preorder α] {c : ClosureOp α} {x : α} :
    IsClosed c x ↔ c x = x :=
  by
    simpa [IsClosed] using (ClosureOperator.isClosed_iff (self := c) (x := x))

lemma isClosed_of_le {α : Type u} [PartialOrder α] {c d : ClosureOp α} (hcd : c <= d) {x : α} :
    IsClosed d x -> IsClosed c x := by
  intro hx
  have hx' : d x = x := (isClosed_iff (c := d) (x := x)).1 hx
  have hcx : c x <= x := by
    have hcdx : c x <= d x := hcd x
    simpa [hx'] using hcdx
  have hxc : x <= c x := c.le_closure x
  exact (isClosed_iff (c := c) (x := x)).2 (le_antisymm hcx hxc)

instance {α : Type u} [CompleteLattice α] (c : ClosureOp α) :
    CompleteLattice (Closed c) :=
  c.gi.liftCompleteLattice

end ClosureOp

def StrictlyStronger {α : Type u} [Preorder α] (c d : ClosureOp α) : Prop :=
  c <= d ∧ ¬ d <= c

notation:50 c " ≺ " d => StrictlyStronger c d

structure ClosureLadder (α : Type u) [Preorder α] where
  c : Nat -> ClosureOp α
  step_strict : forall n, c n ≺ c (n + 1)

lemma ladder_mono {α : Type u} [Preorder α] (L : ClosureLadder α) (n : Nat) :
    L.c n <= L.c (n + 1) :=
  (L.step_strict n).1

lemma closed_sets_antitone_in_ladder {α : Type u} [PartialOrder α]
    (L : ClosureLadder α) (n : Nat) {x : α} :
    ClosureOp.IsClosed (L.c (n + 1)) x -> ClosureOp.IsClosed (L.c n) x := by
  intro hx
  exact ClosureOp.isClosed_of_le (ladder_mono L n) hx

lemma closure_isClosed {α : Type u} [PartialOrder α] (c : ClosureOp α) (x : α) :
    ClosureOp.IsClosed c (c x) :=
  c.isClosed_closure x

lemma le_closure {α : Type u} [PartialOrder α] (c : ClosureOp α) (x : α) :
    x <= c x :=
  c.le_closure x

lemma closure_idempotent {α : Type u} [PartialOrder α] (c : ClosureOp α) (x : α) :
    c (c x) = c x :=
  c.idempotent x

lemma closure_iterate_succ {α : Type u} [PartialOrder α] (c : ClosureOp α) (n : Nat) (x : α) :
    c^[n + 1] x = c x := by
  induction n generalizing x with
  | zero =>
      simp
  | succ n ih =>
      calc
        c^[n + 2] x = c^[n + 1] (c x) := by
          simp [Function.iterate_succ_apply]
        _ = c (c x) := by
          simpa using ih (c x)
        _ = c x := c.idempotent x

lemma closure_iterate_ge_one {α : Type u} [PartialOrder α] (c : ClosureOp α) {n : Nat}
    (h : 1 <= n) (x : α) :
    c^[n] x = c x := by
  cases n with
  | zero =>
      cases h
  | succ n =>
      simpa using closure_iterate_succ (c := c) n x

section Smoke

open ClosureOp

def topClosure : ClosureOp (Set Nat) :=
  ClosureOperator.mk' (fun _ => (⊤ : Set Nat))
    (by intro a b h; exact le_rfl)
    (by intro a; exact le_top)
    (by intro a; exact le_rfl)

example (s : Set Nat) : IsClosed (ClosureOperator.id (Set Nat)) s := by
  simp [IsClosed]

example (s : Set Nat) : (ClosureOperator.id (Set Nat))^[3] s = s := by
  have h : (1 : Nat) <= 3 := by decide
  simp [closure_iterate_ge_one (c := ClosureOperator.id (Set Nat)) (n := 3) (x := s) h]

example : StrictlyStronger (ClosureOperator.id (Set Nat)) topClosure := by
  refine ⟨?_, ?_⟩
  · intro s
    simp [topClosure]
  · intro h
    have h' : (⊤ : Set Nat) <= (∅ : Set Nat) := by
      simpa [topClosure] using h (∅ : Set Nat)
    have h0 : (0 : Nat) ∈ (∅ : Set Nat) := h' (by simp)
    cases h0

end Smoke
