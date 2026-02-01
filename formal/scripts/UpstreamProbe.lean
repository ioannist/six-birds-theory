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

private def logTryCheckTerm (t : Term) : CommandElabM Unit := do
  let ok ← liftTermElabM <| (try
    let e ← elabTerm t none
    let ty ← inferType e
    let tyStr ← ppExpr ty
    logInfo m!"TERM OK: {t} : {tyStr}"
    pure true
  catch err =>
    logInfo m!"TERM FAIL: {t}"
    logInfo m!"  error: {err.toMessageData}"
    pure false)
  if !ok then pure ()

private def logTrySynthTerm (t : Term) : CommandElabM Unit := do
  let _ ← liftTermElabM <| (try
    let ty ← elabType t
    let tyStr ← ppExpr ty
    let inst? ← synthInstance? ty
    match inst? with
    | some _ => logInfo m!"SYNTH OK: {tyStr}"
    | none => logInfo m!"SYNTH FAIL: {tyStr}"
    pure true
  catch err =>
    logInfo m!"SYNTH ERROR: {t}"
    logInfo m!"  error: {err.toMessageData}"
    pure false)

elab "#try_check " id:ident : command => do
  logTryCheck id.getId

elab "#try_check_term " t:term : command => do
  logTryCheckTerm t

elab "#try_synth_term " t:term : command => do
  logTrySynthTerm t

#try_check ClosureOperator
#try_check Function.Idempotent
#try_check Function.fixedPoints
#try_check Function.IsFixedPt
#try_check Function.Idempotent.iterate_succ_apply
#try_check Function.Idempotent.iterate_apply_eq

-- Instance probes (safe term checks)
#try_synth_term (LE (ClosureOperator Nat))
#try_synth_term (Preorder (ClosureOperator Nat))
