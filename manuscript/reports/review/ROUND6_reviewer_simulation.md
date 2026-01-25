# ROUND6 Reviewer Simulation

## Lens 1: Order theorist (closure ladders)

Questions and answers:
1) Is the strictness relation $\prec$ irreflexive/transitive?  Answered in sec:closure remark (around L364–L369).
2) Does $c\le d$ imply $\mathrm{Fix}(d)\subseteq\mathrm{Fix}(c)$?  Answered by Lemma~\ref{lem:closed-antitone} and reiterated in the same remark (sec:closure, L355–L370).
3) If $L$ is finite, can closure ladders be infinite?  Answered in sec:closure remark: finite lattices give finite chains; unboundedness comes from changing theory/domains (L367–L368).
4) Where is the reflection correspondence (closure ↔ reflection onto fixed points) stated?  Answered in sec:closure remark + Lean note (L364–L373).
5) How does refinement affect closure strength?  Answered in D-META-REF-01 clarification (sec:meta-unavoidable, around L967–L969).

Edits made:
- Added a short remark in sec:closure consolidating strictness, antitone fixed points, finite-lattice limitation, and reflection correspondence.
- Added refinement/closure-direction sentence in Definition~\ref{def:meta-ref}.

## Lens 2: Probability / information theorist (AOT, DPI, protocol)

Questions and answers:
1) After coarse-graining, is the observed process necessarily Markov?  Answered: explicitly “need not be Markov” in sec:aot (L785–L786).
2) Does time reversal commute with coordinatewise coarse maps?  Answered in the DPI proof sketch (L798–L801).
3) Are DPI claims about path measures rather than Markov kernels?  Answered by the added sentence in sec:aot and the path-measure DPI proof (L785–L801).
4) Does the protocol definition match random-scan implementation?  Answered by D-PROT-02 and the AOT protocol proof sketch (L818–L846).
5) What exactly is meant by “P3 needs P6” under autonomy?  Answered by renaming to P6_drive and clarifying affinity specialization (sec:aot corollary + example + Appendix C paragraph, L814–L1190 and L1323).

Edits made:
- Added “observed process need not be Markov” sentence in sec:aot.
- Retained explicit commutation $f^{T+1}\circ\mathcal R=\mathcal R\circ f^{T+1}$ in the DPI proof sketch (already present).
- Replaced “P3 needs P6” with “P3 needs P6_drive” in protocol corollary, example, and evidence map paragraph.

## Lens 3: Logic / model theory (definability/forcing + META semantics)

Questions and answers:
1) Does the forcing story claim set-theoretic independence?  Answered in new forcing remark (sec:forcing, L886–L890).
2) In a fixed finite $Z$, can refinements be unbounded?  Answered in the same forcing remark (L886–L889).
3) Is the META lens kernel actually a congruence?  Clarified: it is an equivalence; congruence stability is an added hinge (D-META-LENS-01 + thm:meta-prim proof, L958–L1021).
4) Is the refinement direction consistent with factorization?  Fixed in D-META-REF-01: coarser lens factors through finer (L964–L969).
5) What is P6 in META vs ACC?  Clarified by broadening P6 to “accounting/audit” and introducing P6_drive as ACC specialization (sec:primitives, L1071–L1083).

Edits made:
- D-META-LENS-01: changed “congruence” → “kernel equivalence.”
- D-META-REF-01: corrected factorization direction and added closure-strength direction sentence.
- thm:meta-prim proof: added HL-META-1 congruence-stability dependency sentence.
- P6 definition broadened; added P6_drive remark; updated P3/P6 wording in AOT and examples.
- Added a forcing remark clarifying finite proxy scope.

## Checks run

- python3 scripts/check_paper_contract.py: PASS
- python3 scripts/check_deps_dag.py: PASS
- python3 scripts/check_tex_refs.py manuscript/paper.tex: PASS
- python3 scripts/check_kb_pointers.py: PASS
- ./check_lean.sh: PASS
- cd python && .venv/bin/python -m pytest -q: PASS
- override-sensitive greps: NO_HITS for "P3 alone implies", "coarse-graining creates irrevers", "E_{\tau,\Pi} is a ClosureOperator".
