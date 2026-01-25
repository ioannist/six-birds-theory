import Mathlib

/-!
Minimal packaging micro-anchor: a map induces a congruence; the quotient repackaging
is idempotent and stabilizes on packed elements.
-/

namespace ClosureLadder.MetaPackaging

def kerRel (f : α → β) : Setoid α :=
  ⟨fun x y => f x = f y, ⟨by intro x; rfl, by intro x y h; simpa using h.symm, by
    intro x y z hxy hyz
    exact hxy.trans hyz⟩⟩

def pack (f : α → β) : α → Quotient (kerRel f) :=
  Quotient.mk _

def repack (f : α → β) : Quotient (kerRel f) → Quotient (kerRel f) :=
  fun q => q

theorem repack_idempotent (f : α → β) (q : Quotient (kerRel f)) :
    repack f (repack f q) = repack f q := by
  rfl

theorem repack_pack_eq_pack (f : α → β) (x : α) :
    repack f (pack f x) = pack f x := by
  rfl

end ClosureLadder.MetaPackaging
