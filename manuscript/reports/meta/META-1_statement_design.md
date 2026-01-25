# META-1 Statement Design for T-META-PRIM-01

## A. Formalism choice (pick one)

**Option B:** partial semigroup of happenings $(\mathcal P,\circ)$ with a lens-induced congruence $\sim$.
Justification: it is strictly minimal (only partial composition + an observational equivalence) and avoids category-theoretic overhead while still supporting quotienting, refinement chains, and route-mismatch constructions. It cleanly exposes when induced dynamics is ill-defined (congruence stability), which is the P1 rewrite hinge.

## B. Precise “limited access” definition

Limited access means the lens-induced congruence is nontrivial: there exist $x\neq y$ in $\mathcal P$ such that $x\sim y$.
Formally, let $f:\mathcal P\to X$ be the interface lens; define $x\sim y$ iff $f(x)=f(y)$. Limited access means $\exists x\neq y$ with $f(x)=f(y)$.

## C. Precise “bounded interface / finiteness-locality” definition

Bounded interface means each lens has finite index: for each level $j$, the quotient set $\mathcal P/\!\sim_j$ is finite and
$|\mathcal P/\!\sim_j|\le C_0(j+1)$ for some constant $C_0$.
This encodes a finite observable signature per resolution level.

## D. Refinement family definition

A refinement family is a nested sequence of congruences $(\sim_j)_{j\ge 0}$ such that
$\sim_{j+1}$ refines $\sim_j$ (i.e., $x\sim_{j+1} y \Rightarrow x\sim_j y$).
Equivalently, there are lenses $f_j$ with $f_{j+1}=g_j\circ f_j$ for some maps $g_j$, so each level only merges what was already merged.

## E. Derivation map: P1–P6 as constructions

**P5 (Packaging).** Given $\sim_j$, define the packaging map $\Pi_j: \mathcal P\to \mathcal P/\!\sim_j$ (quotient map). This is idempotent
as an endomap on the quotient and provides the completion rule for that level.

**P6 (Accounting).** Limited access induces a preorder on histories by observational refinement: $x\preceq y$ iff $f_j(x)$ factors through
$f_j(y)$ for all $j$ (or equivalently, $x$ is observationally no more informative than $y$). Define the audit currency as any
monotone map with respect to this preorder. This is information/feasibility accounting only, not physical irreversibility.

**P4 (Staging).** The refinement chain $(\sim_j)$ defines a stage index and a resolution ladder. Stage $j$ corresponds to the quotient
$\mathcal P/\!\sim_j$. Counting stages is purely combinatorial and does not assume dynamics.

**P2 (Constraints).** The feasible macrostates at level $j$ are the image of $\Pi_j$ subject to interface compatibility. Abstractly, P2 is the
restriction to the feasible image; in Markov specializations, this becomes edge deletion on a support graph.

**P1 (Operator rewrite).** An induced macro update $p^\sharp([x])=[p(x)]$ exists iff $\sim_j$ is stable under the micro-update $p$;
if not, one must either rewrite the operator (replace $p$ by a coarse-compatible $\tilde p$) or refine the lens.

**P3 (Holonomy / route dependence).** For two reduction routes between levels, define route mismatch using the toolkit observable RM
(see `D-TK-ROUTE-01`, `L-TK-ROUTE-01`). This captures order-dependence of reduction. Guardrail: P3 does not imply arrow-of-time
in the autonomous regime; directionality is governed by DPI/path-KL.

## F. Theorem skeleton for T-META-PRIM-01

Assume D-META-PROC-01 + D-META-LENS-01 + D-META-REF-01 + D-META-BND-01. Then canonical constructions exist for P1–P6:
(1) P5 by quotient packaging $\Pi_j$; (2) P6 by an observational preorder and monotone audit; (3) P4 by the refinement chain;
(4) P2 as the feasible image under $\Pi_j$; (5) P1 as the induced update when congruence stability holds or else a forced rewrite;
(6) P3 as route mismatch between reduction routes, with explicit RM construction.

## G. What this does NOT claim

- Does NOT claim coarse-graining creates physical arrow-of-time; directionality remains governed by DPI/path-KL in the AOT section.
- Does NOT claim uniqueness of constructions unless formalized (e.g., uniqueness of induced macro updates).
- Does NOT claim any probabilistic, metric, or dynamical structure at the base layer; these are add-ons.

## H. Hard lemma slots (if any)

- HL-META-1 (Congruence stability): conditions under which the induced macro update is well-defined without rewriting.
- HL-META-2 (Nontrivial refinement): conditions ensuring strictness of the refinement ladder (not all levels collapse).
