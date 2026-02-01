import Mathlib
import Lean

open Lean
open Lean.Elab
open Lean.Elab.Command
open Lean.Elab.Term
open Lean.Meta

private def logTryCheck (n : Name) : CommandElabM Unit := do
  let env <- getEnv
  match env.find? n with
  | none =>
      logInfo m!"NOT FOUND: {n}"
  | some info =>
      let tyStr ← liftTermElabM <| ppExpr info.type
      logInfo m!"FOUND: {n} : {tyStr}"

private def logTryWhereis (n : Name) : CommandElabM Unit := do
  let env <- getEnv
  match env.getModuleIdxFor? n with
  | none => logInfo m!"WHEREIS: {n} -> <not found>"
  | some idx =>
      match env.header.moduleNames[idx]? with
      | none => logInfo m!"WHEREIS: {n} -> <unknown module>"
      | some modName => logInfo m!"WHEREIS: {n} -> {modName}"

elab "#try_check " id:ident : command => do
  logTryCheck id.getId

elab "#try_whereis " id:ident : command => do
  logTryWhereis id.getId

elab "#try_synth " t:term : command => do
  let ty ← liftTermElabM (elabType t)
  let ok ← liftTermElabM <| (try
    let _ ← synthInstance ty
    pure true
  catch _ =>
    pure false)
  let tyStr ← liftTermElabM <| ppExpr ty
  if ok then
    logInfo m!"SYNTH SUCCESS: {tyStr}"
  else
    logInfo m!"SYNTH FAIL: {tyStr}"

-- Candidate name probes
#try_check ClosureOperator
#try_check ClosureOperator.IsClosed
#try_check ClosureOperator.Closeds
#try_check ClosureOperator.toCloseds
#try_check ClosureOperator.isClosed_iff
#try_check ClosureOperator.isClosed_closure
#try_check ClosureOperator.le_closure
#try_check ClosureOperator.idempotent

#try_check GaloisInsertion.gc
#try_check GaloisInsertion.l_u_eq

#try_check Setoid.ker

-- Fixed point APIs to compare with IdempotentEndo
#try_check Function.IsFixedPt
#try_check Function.fixedPoints

-- Instance existence checks
