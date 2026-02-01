import Mathlib
import Lean

open Lean

elab "#whereis " id:ident : command => do
  let env <- getEnv
  let n := id.getId
  match env.getModuleIdxFor? n with
  | none =>
      logInfo m!"{n} -> <not found>"
  | some idx =>
      let modName? := env.header.moduleNames[idx]?
      match modName? with
      | none => logInfo m!"{n} -> <unknown module>"
      | some modName => logInfo m!"{n} -> {modName}"

#whereis ClosureOperator
#whereis ClosureOperator.IsClosed
#whereis ClosureOperator.Closeds
#whereis ClosureOperator.isClosed_iff
#whereis ClosureOperator.isClosed_closure
#whereis ClosureOperator.le_closure
#whereis ClosureOperator.idempotent
#whereis ClosureOperator.toCloseds
#whereis ClosureOperator.gi
#whereis GaloisInsertion.gc
#whereis GaloisInsertion.liftCompleteLattice
#whereis GaloisInsertion.l_u_eq
#whereis Setoid.ker
