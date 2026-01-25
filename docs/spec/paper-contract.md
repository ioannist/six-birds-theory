# Paper contract

## One-paragraph aim
This paper is math-only and discipline-agnostic: we define closure-ladder objects, empirical closures, and arrow-of-time diagnostics in finite settings, and prove a tightly scoped set of claims about them. We explicitly exclude applications, biology, or simulation narratives; any numerical experiments are relegated to appendix evidence and do not constitute empirical claims.

## Audience and prerequisites
- Order theory basics (posets, closure operators, fixed points).
- Finite Markov chains and stationary distributions.
- KL divergence and data processing inequality (DPI).
- Elementary graph cycle space and beta_1 for undirected graphs.

## Canonical objects and definitions
- D-CL-01, D-CL-02, D-CL-03: order-theoretic closure operators, fixed points, and closure ladders (poset setting).
- D-IC-01, D-IC-02: induced empirical closure E_{tau,Pi} as an idempotent endomap on Delta(Z) with TV defect; not an order-closure operator.
- D-AOT-01, D-AOT-EP-01: finite-horizon path reversal asymmetry and steady-state EP; REV-support needed for finiteness.
- D-ACC-01, D-ACC-02: graph antisymmetric 1-form and cycle affinities on bidirected support.
- D-AUT-01, D-REV-01, D-LENS-01: autonomy, REV-support, and coarse-graining lens.
- D-PROT-02: autonomous m-phase random-scan protocol model on X x Phi with shared stationary pi.
- D-P2-01, D-P1-01: gating and rewrite actions on undirected support under REV-support.
- D-FOR-01, D-FOR-02: forcing/definability with IID Bernoulli(1/2) predicates on Z.
- Separation rule: order-closure is D-CL-* (poset axioms); empirical closure is D-IC-* (idempotent endomap on the simplex with metric defect), not a closure operator.

## Main-text claims
- **ID:** T-CL-01  
  **What we claim:** Closure saturates under a fixed closure operator; iterating closure adds no new objects.  
  **Proof status:** Lean: done.  
  **Assumptions:** D-CL-01.
- **ID:** T-IC-01  
  **What we claim:** Refinement can increase or decrease stable prototypes depending on mixing vs leakage at scale tau.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + D-IC-01 + margin-stability condition.
- **ID:** T-IC-02  
  **What we claim:** Under fast within-cell mixing and small leakage, E_{tau,Pi} is approximately idempotent and objects persist.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + D-IC-01 + D-IC-02 + mixing/leakage bounds.
- **ID:** T-AOT-01  
  **What we claim:** DPI for path reversal asymmetry under coarse-graining; macro arrow <= micro arrow for any initial law.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** D-AOT-01 + D-LENS-01.
- **ID:** L-AOT-STAT-01  
  **What we claim:** Stationary initialization removes boundary relaxation terms; reversible chains have zero steady EP though Sigma_T can be positive for nonstationary init.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** D-AOT-01 + D-AOT-EP-01.
- **ID:** T-AOT-02  
  **What we claim:** Protocol trap: external scheduling can create apparent irreversibility; under autonomous protocols, sustained arrow requires phase bias (P6).  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_AUT + A_ACC + D-PROT-02.
- **ID:** C-ACC-01  
  **What we claim:** P3 alone does not yield sustained autonomous arrow; requires P6 or external schedule.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_AUT + A_ACC + A_NULL + D-PROT-02.
- **ID:** T-ACC-01  
  **What we claim:** If cycle affinities vanish (exact 1-form), detailed balance holds and stationary currents vanish.  
  **Proof status:** Proof-sketch.  
  **Assumptions:** A_AUT + A_REV + A_ACC + A_NULL + A_STAT.
- **ID:** T-P2-01  
  **What we claim:** Edge deletions reduce cycle rank on the undirected support graph (REV-support regime).  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + graph topology assumptions.
- **ID:** T-META-PRIM-01  
  **What we claim:** Under minimal process-soup + interface assumptions, the six primitives P1--P6 self-generate as closure mechanics.  
  **Proof status:** Planned (main text; not yet in manuscript).  
  **Assumptions:** D-META-PROC-01 + D-META-LENS-01 + D-META-REF-01 + D-META-BND-01 (structural / limited-access, not physics).
- **ID:** T-P1-01  
  **What we claim:** P1 rewrites can increase cycle rank and can increase or decrease spectral gap; weight rewrites can create near-decomposability.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + graph Laplacian / Markov operator assumptions.
- **ID:** T-FOR-01  
  **What we claim:** Finite forcing lemma: IID Bernoulli predicates are typically non-definable and split coarse classes.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + A_LENS + mixing/admissibility assumptions.
- **ID:** T-FOR-02  
  **What we claim:** Definable predicates are exponentially rare in N-K under IID Bernoulli sampling.  
  **Proof status:** Proof-sketch + repo evidence.  
  **Assumptions:** A_FIN + A_LENS.

## Appendix-only material
- Randomized DPI sweeps and strict-hiding numerical examples.
- Protocol-trap numeric demos and stroboscopic sanity checks.
- Spectral-gap demos (increase/decrease) and graph sweep scripts.
- Forcing Monte Carlo sweeps and fixed-weight contrasts.
- Implementation policies: stationary distribution fallbacks, REV-support convention tests, Cesaro solver notes.
- Diagnostic/counterexample inventory items (e.g., DIAG-PT-01, CE-P3-01).
- Appendix (Zeno decision frontier).
- ECT add-on (appendix-only): D-ECT-ATOM-01, D-ECT-CAP-01, D-ECT-GATE-01, D-ECT-SECT-01, D-ECT-P5MIN-01, D-ECT-P4IDX-01, D-ECT-ATOM-SS-01, D-ECT-BAL-01, L-ECT-MECH-01, L-ECT-FMEM-01, L-ECT-COER-01, L-ECT-SHRINK-01, L-ECT-MODE-UB-01, L-ECT-QSIZE-01, C-ECT-HL1-01, L-ECT-BAL-KMASS-01, C-ECT-BAL-ICAP-01 (mechanical ECT template + finite-memory ICAP + gating + feasibility shrinkage + sectorization/minimality mode compression + quantized index bound + balanced-dissipation atoms to per-atom ICAP).

## Toolkit additions (planned)
- Main text (definitions only; no new claims):
  - D-TK-THY-01: theory package definition (lens/definability + completion endomap + audit).
  - D-TK-CERT-01: certificates definition (stability/defect, novelty/non-definability, directionality/audit monotonicity).
- Appendix (definitions + at most one lemma):
  - D-TK-DEF-01: defect calculus (generic defect notion).
  - D-TK-DEF-02: idempotence defect definition (TV/L1; extreme point attainment).
  - D-TK-ROUTE-01: route mismatch observable RM(j).
  - D-TK-BRG-01: bridge object (ports + causal operator + accounting).
  - D-TK-BRG-02: passivity-with-storage (storage inequality).
  - D-TK-BRG-03: ICAP (integrated capacity inequality).
  - L-TK-ROUTE-01: route mismatch capacity inequality (single appendix lemma).
- Guardrail: no new main-text theorems are introduced by toolkit material; it is definitional/organizational except for at most one appendix lemma.

## Out of scope for this paper
- Continuous-time stochastic thermodynamics interpretation layer (CTMC physical claims); only the graph 1-form algebra is in scope.
- Sample-complexity or statistical estimation theorems for empirical closure.
- Operads/sheaves/copyability/Darwinian regimes or biological applications.
- Empirical/simulation claims beyond toy finite examples in the appendix.

## Consistency constraints and overrides
- Later-overrides-earlier is governed by docs/registries/overrides.md (canonical).
- Coarse-graining cannot create arrow-of-time: DPI applies to path reversal asymmetry (Sigma_T) and bounds the macro arrow.
- P3 alone does not yield sustained autonomous directionality; P6 or an external schedule is required for persistent arrow.
- Closure operators (D-CL-*) are order-theoretic; E_{tau,Pi} (D-IC-*) is an idempotent endomap with a metric defect, not a closure operator.
- REV-support is required for finiteness of EP/KL; violations may yield infinite EP.

## Reproducibility contract
- Run: `python3 scripts/check_paper_contract.py`
- Run: `python3 scripts/check_deps_dag.py`
- Run: `python3 scripts/check_kb_pointers.py`
- Run: `./check_lean.sh`
- Run: `cd python && .venv/bin/python -m pytest -q`
