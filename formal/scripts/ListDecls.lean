import ClosureLadder
import Lean

open Lean

-- Print all declarations whose defining module is one of the ClosureLadder modules.
#eval do
  let env <- importModules #[{ module := `ClosureLadder }] {}
  let mods : Array Name := #[`ClosureLadder.Basic, `ClosureLadder.Packaging, `ClosureLadder.IdempotentEndo, `ClosureLadder.MetaPackaging, `ClosureLadder]
  let mut names : Array Name := #[]
  for (n, _) in env.constants.toList do
    if let some idx := env.getModuleIdxFor? n then
      if let some mod := env.header.moduleNames[idx]? then
        if mods.contains mod then
          names := names.push n
  names := names.qsort (fun a b => a.toString < b.toString)
  for n in names do
    IO.println s!"{n}"
