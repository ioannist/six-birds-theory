import ClosureLadder

-- Basic
#check ClosureOp
#print ClosureOp

variable {α : Type u} [Preorder α]
#check instLEClosureOp
#check (inferInstance : LE (ClosureOp α))

#check ClosureOp.IsClosed
#print ClosureOp.IsClosed

#check ClosureOp.Closed
#print ClosureOp.Closed

#check ClosureOp.isClosed_iff
#print ClosureOp.isClosed_iff

#check ClosureOp.isClosed_of_le

variable {α : Type u} [CompleteLattice α] (c : ClosureOp α)
#check ClosureOp.instCompleteLatticeClosed
#check (inferInstance : CompleteLattice (ClosureOp.Closed c))

#check StrictlyStronger
#print StrictlyStronger

#check ClosureLadder

#check ladder_mono

#check closed_sets_antitone_in_ladder

#check closure_isClosed
#print closure_isClosed

#check le_closure
#print le_closure

#check closure_idempotent
#print closure_idempotent

#check closure_iterate_succ

#check closure_iterate_ge_one

#check topClosure
#print topClosure

-- Packaging
variable {α : Type u} [PartialOrder α]
#check ClosureOp.incl
#print ClosureOp.incl

#check ClosureOp.reflect
#print ClosureOp.reflect

#check ClosureOp.reflect_le_iff
#print ClosureOp.reflect_le_iff

#check ClosureOp.incl_reflect_eq
#print ClosureOp.incl_reflect_eq

#check ClosureOp.reflect_incl_eq
#print ClosureOp.reflect_incl_eq

-- IdempotentEndo
#check ClosureLadder.IdempotentEndo
#print ClosureLadder.IdempotentEndo

variable {α : Type u} (e : ClosureLadder.IdempotentEndo α)
#check ClosureLadder.IdempotentEndo.FixedPoints
#print ClosureLadder.IdempotentEndo.FixedPoints

#check ClosureLadder.IdempotentEndo.incl
#print ClosureLadder.IdempotentEndo.incl

#check ClosureLadder.IdempotentEndo.retract
#print ClosureLadder.IdempotentEndo.retract

#check ClosureLadder.IdempotentEndo.incl_retract
#print ClosureLadder.IdempotentEndo.incl_retract

#check ClosureLadder.IdempotentEndo.retract_incl
#print ClosureLadder.IdempotentEndo.retract_incl

#check ClosureLadder.ClosureOperator.toIdempotentEndo
#print ClosureLadder.ClosureOperator.toIdempotentEndo

-- MetaPackaging
#check ClosureLadder.MetaPackaging.kerRel
#print ClosureLadder.MetaPackaging.kerRel

#check ClosureLadder.MetaPackaging.pack
#print ClosureLadder.MetaPackaging.pack

#check ClosureLadder.MetaPackaging.repack
#print ClosureLadder.MetaPackaging.repack

#check ClosureLadder.MetaPackaging.repack_idempotent
#print ClosureLadder.MetaPackaging.repack_idempotent

#check ClosureLadder.MetaPackaging.repack_pack_eq_pack
#print ClosureLadder.MetaPackaging.repack_pack_eq_pack
