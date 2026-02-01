import Mathlib
import Lean

open Lean

#eval do
  let env <- importModules #[{ module := `Mathlib }] {}
  let names : Array Name := #[`Subtype.val, `Quotient.mk, `id]
  for n in names do
    match env.getModuleIdxFor? n with
    | none => IO.println s!"{n} -> <not found>"
    | some idx =>
        match env.header.moduleNames[idx]? with
        | none => IO.println s!"{n} -> <unknown module>"
        | some modName => IO.println s!"{n} -> {modName}"
