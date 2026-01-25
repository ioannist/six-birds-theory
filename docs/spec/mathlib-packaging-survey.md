# Mathlib packaging survey (reflection / idempotent monad)

## What exists in mathlib
- `Mathlib/CategoryTheory/Adjunction/Reflective`: defines `Reflective`, `reflector`, `reflectorAdjunction`, and unit/counit isomorphism lemmas for reflective inclusions.
- `Mathlib/CategoryTheory/Monad/Adjunction`: relates reflective adjunctions to monads; includes `μ_iso_of_reflective` (monad multiplication iso) and `monadicOfReflective`.
- `Mathlib/CategoryTheory/Monad/Limits`: limits/colimits transfer along reflective/coreflective functors.
- `Mathlib/CategoryTheory/Idempotents/Basic`: `IsIdempotentComplete` and idempotent-splitting lemmas.
- `Mathlib/CategoryTheory/Idempotents/Karoubi`: Karoubi envelope (idempotent completion) and related API.
- `Mathlib/CategoryTheory/Sites/Sheafification`: reflective subcategories as instances in a concrete setting.

## What does not
- No single lightweight theorem in `Order` or `Closure` namespaces stating “closure operator ⇒ reflective subcategory” without category-theory imports.
- The category-theory path is usable but heavier (reflective functor + monad adjunction stack).

## Decision
- **Route B (thin-category / preorder)** using the Galois insertion associated to a closure operator.

## Why this is the smallest robust backbone
- Uses only order-theoretic infrastructure (`ClosureOperator.gi`) and avoids category-theory dependencies.
- Gives a precise reflector universal property and the two expected identities for inclusion/reflection.
- Matches the paper’s “packaging completeness” meaning in a clean, citeable statement.

## Names we can cite (defs/lemmas)
- `ClosureOperator.gi`
- `ClosureOperator.Closeds`
- `ClosureOperator.isClosed_iff`
- `GaloisInsertion.l_u_eq`
- `CategoryTheory.Reflective` (for full category-theory version)
- `μ_iso_of_reflective`
