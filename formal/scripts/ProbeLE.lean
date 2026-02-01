import Mathlib

variable {α : Type u} [Preorder α]
#check (inferInstance : LE (ClosureOperator α))
