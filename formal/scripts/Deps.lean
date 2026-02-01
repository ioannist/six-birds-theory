import ClosureLadder
import Lean
import Lean.Util.FoldConsts

open Lean

-- List of repo-authored declarations to audit.
def repoDecls : Array Name :=
  #[ `ClosureOp
   , `instLEClosureOp
   , `ClosureOp.IsClosed
   , `ClosureOp.Closed
   , `ClosureOp.isClosed_iff
   , `ClosureOp.isClosed_of_le
   , `ClosureOp.instCompleteLatticeClosed
   , `StrictlyStronger
   , `ClosureLadder
   , `ladder_mono
   , `closed_sets_antitone_in_ladder
   , `closure_isClosed
   , `le_closure
   , `closure_idempotent
   , `closure_iterate_succ
   , `closure_iterate_ge_one
   , `topClosure
   , `ClosureOp.incl
   , `ClosureOp.reflect
   , `ClosureOp.reflect_le_iff
   , `ClosureOp.incl_reflect_eq
   , `ClosureOp.reflect_incl_eq
   , `ClosureLadder.IdempotentEndo
   , `ClosureLadder.IdempotentEndo.FixedPoints
   , `ClosureLadder.IdempotentEndo.incl
   , `ClosureLadder.IdempotentEndo.retract
   , `ClosureLadder.IdempotentEndo.incl_retract
   , `ClosureLadder.IdempotentEndo.retract_incl
   , `ClosureLadder.ClosureOperator.toIdempotentEndo
   , `ClosureLadder.MetaPackaging.kerRel
   , `ClosureLadder.MetaPackaging.pack
   , `ClosureLadder.MetaPackaging.repack
   , `ClosureLadder.MetaPackaging.repack_idempotent
   , `ClosureLadder.MetaPackaging.repack_pack_eq_pack
   ]

partial def isRepoConst (env : Environment) (n : Name) : Bool :=
  match env.getModuleIdxFor? n with
  | some idx =>
      match env.header.moduleNames[idx]? with
      | some mod =>
          let s := mod.toString
          s.startsWith "ClosureLadder"
      | none => false
  | none => false

#eval do
  let env <- importModules #[{ module := `ClosureLadder }] {}
  for n in repoDecls do
    match env.find? n with
    | none =>
        IO.println s!"{n}: <not found>"
    | some info =>
        let used := info.type.getUsedConstants
        let repoDeps := used.filter (fun m => isRepoConst env m && m != n)
        let repoDepsList : List String := repoDeps.toList.map Name.toString
        let shortDeps := repoDepsList.take 20
        let depends : Bool := decide (repoDepsList.length > 0)
        IO.println s!"decl={n}"
        IO.println s!"depends_on_repo_defs={depends}"
        IO.println s!"repo_deps=[{String.intercalate ", " shortDeps}]"
        IO.println "--"
