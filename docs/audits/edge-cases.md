# Edge Cases + Holes Audit

## Executive summary
- Arrow-of-time hygiene now separates finite-horizon path KL from steady-state EP, with explicit STAT/ERG and REV-support assumptions, but the formal boundary-term lemma is still informal.
- REV-support violations are handled explicitly in code (infinite EP) and tests, but finiteness hypotheses are not formalized in Lean.
- ACC is now treated as a graph 1-form on bidirected support (DTMC/CTMC interpretation separated), with Python diagnostics, but no formal proof of the H^1 decomposition.
- Protocol-trap claims are now tied to an explicit autonomous m-phase random-scan model with shared stationary pi; remaining scope risk is model-class dependence.
- Empirical closure is treated as an idempotent endomap (not an order-closure), with exact TV defect computation; refinement is explicitly non-monotone in stable-object counts.

**Top 5 highest-severity issues:**
- EC-001 (Critical, Mitigated) - Path-KL vs steady EP separation and boundary-term dependence.
- EC-006 (Critical, Mitigated) - Order-closure vs empirical endomap distinction and bridge.
- EC-002 (High, Mitigated) - REV-support required for finite EP/KL.
- EC-004 (High, Mitigated) - ACC treated as graph 1-form; CTMC/DTMC interpretation split.
- EC-005 (High, Mitigated) - Protocol-trap claims depend on explicit autonomous model class.

## Counts and coverage
- Total audit items: 12
- Status breakdown: Open=0, Mitigated=10, Closed=2, Deferred=0
- Severity breakdown: Critical=2, High=4, Medium=5, Low=1
- Theme breakdown:
  - Closure/order-theory vs empirical closure: 2
  - AUT+REV+ACC: 3
  - Arrow-of-time + DPI + protocol trap: 4
  - P1/P2 topology claims: 2
  - Forcing / definability rarity: 1

## Audit items

### EC-001
- **ID:** EC-001
- **Title:** Finite-horizon path KL vs steady-state EP requires stationarity split
- **Severity:** Critical
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-AOT-01, D-AOT-EP-01, L-AOT-STAT-01, T-AOT-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (Arrow-of-time section); docs/registries/assumptions.md (STAT/ERG); python/tests/test_paths_nonstationary_boundary_term.py; python/tests/test_paths_dpi_nonstationary_init.py; python/tests/test_paths_dpi_randomized.py
- **What was wrong:** Path reversal asymmetry was implicitly treated as steady-state EP; nonstationary initial laws introduce boundary terms and change Sigma_T.
- **Fix / mitigation:** Split definition (Sigma_T for any init) from steady-state EP interpretation; added STAT/ERG assumptions; added boundary-term and nonstationary DPI tests.
- **Residual risk:** No formal proof of the boundary-term decomposition or EP rate limit; Lean statements still planned.
- **Proposed next step:** Add Lean lemma connecting Sigma_T(pi) to EP and boundary-term correction; formalize rate limit assumptions.

### EC-002
- **ID:** EC-002
- **Title:** REV-support needed for finiteness of EP/KL
- **Severity:** High
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-REV-01, D-AOT-EP-01, T-AOT-02
- **Repo evidence pointers:** docs/registries/assumptions.md (REV-support); python/src/clt/markov.py (entropy_production_rate); python/tests/test_rev_support_convention.py
- **What was wrong:** Missing reverse support causes log-ratio infinities or undefined reversals; EP/KL can be infinite or NaN.
- **Fix / mitigation:** Documented REV-support as a finiteness condition and made entropy_production_rate return +inf on violations; added explicit test.
- **Residual risk:** Path-KL finiteness for long horizons not formalized; Lean side does not enforce support conditions.
- **Proposed next step:** Add Lean hypotheses for REV-support in EP/KL lemmas and define infinite-EP convention.

### EC-003
- **ID:** EC-003
- **Title:** Stationary distribution convergence/uniqueness not guaranteed
- **Severity:** High
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-AOT-EP-01, L-AOT-STAT-01, T-AOT-01
- **Repo evidence pointers:** docs/registries/assumptions.md (ERG); python/src/clt/markov.py (stationary_distribution_solve, stationary_distribution_cesaro); python/tests/test_stationary_distribution_periodic.py; python/tests/test_stationary_distribution_reducible_tiebreak.py
- **What was wrong:** Power iteration silently fails for periodic or reducible chains; stationary distribution may be non-unique or init-dependent.
- **Fix / mitigation:** Added robust SVD-based solver with deterministic tie-break and Cesaro fallback; exposed power-iteration convergence status; tests cover periodic and reducible cases.
- **Residual risk:** Numerical stability for large chains not proven; non-unique stationary distributions still require modeling choices.
- **Proposed next step:** Add formal statement of ergodicity assumptions in Lean and a note on init-dependent mixtures.

### EC-004
- **ID:** EC-004
- **Title:** ACC formulation was CTMC-native but evidence is DTMC
- **Severity:** High
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-ACC-01, D-ACC-02, T-ACC-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (ACC entries); python/src/clt/acc.py; python/tests/test_acc_graph_one_form.py
- **What was wrong:** ACC statements read like CTMC log-rate identities while evidence was DTMC-based; discrete-time interpretation was unclear.
- **Fix / mitigation:** Reframed ACC as a graph antisymmetric 1-form on bidirected support; exactness via cycle integrals; DTMC/CTMC interpretation explicitly separated.
- **Residual risk:** No formal proof of the H^1 decomposition or exchange-form basis; CTMC translation still informal.
- **Proposed next step:** Formalize the cycle-basis decomposition and exactness criterion in Lean or a small mathlib-backed lemma.

### EC-005
- **ID:** EC-005
- **Title:** Protocol-trap claims depend on a specific autonomous phase model
- **Severity:** High
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-PROT-02, T-AOT-02, C-ACC-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (D-PROT-02); python/src/clt/protocol.py; python/tests/test_protocol_mphase_random_scan.py; python/tests/test_protocol_trap_external_vs_autonomous.py
- **What was wrong:** Claims were tied to a two-phase flip model without stating the autonomous protocol class and shared-stationary assumptions.
- **Fix / mitigation:** Added D-PROT-02 (m-phase random-scan model) and tests covering unbiased vs biased phases with shared pi.
- **Residual risk:** Other autonomous protocol schemes may exhibit different cancellations; no formal theorem bounding the class.
- **Proposed next step:** Restrict paper claims to D-PROT-02 class or extend tests to additional protocol update schemes.

### EC-006
- **ID:** EC-006
- **Title:** Order-closure vs empirical closure are conflated
- **Severity:** Critical
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-CL-01, D-CL-02, D-IC-01, D-IC-02
- **Repo evidence pointers:** docs/spec/empirical-vs-order-closure.md; formal/ClosureLadder/IdempotentEndo.lean; docs/spec/theorem-inventory.md (IC/CL sections)
- **What was wrong:** Coordinatewise order on Delta(Z) is degenerate; extensiveness would force E to be identity, so E_{tau,Pi} is not an order-closure.
- **Fix / mitigation:** Added an explicit separation doc; Lean IdempotentEndo structure formalizes fixed points without order; IC entries now state endomap/idempotent framing.
- **Residual risk:** No formal bridge from empirical closure to IdempotentEndo on the simplex; approximate idempotence remains a metric claim.
- **Proposed next step:** Add a Lean-side notion of idempotent endomaps on probability simplices (or a dedicated metric structure) if needed.

### EC-007
- **ID:** EC-007
- **Title:** Idempotence defect was defined only on a test family
- **Severity:** Medium
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-IC-02, T-IC-02
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (D-IC-02 exact TV formula); python/src/clt/empirical_closure.py (idempotence_defect_tv); python/tests/test_empirical_closure_idempotence_defect_tv.py
- **What was wrong:** The defect sup over the simplex was approximated by {delta states + uniform}, which can underestimate the true maximum.
- **Fix / mitigation:** Defined exact TV defect as a max over Diracs (row L1 formula) and implemented it with tests.
- **Residual risk:** Only addresses TV/L1 on finite simplex; alternate norms or continuous-state settings not covered.
- **Proposed next step:** Add optional bounds for other norms or continuous approximations if needed.

### EC-008
- **ID:** EC-008
- **Title:** Refinement can help or hurt stable-object counts
- **Severity:** Medium
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** T-IC-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (T-IC-01 wording); python/tests/test_empirical_closure_refinement_reveals_objects.py; python/tests/test_empirical_closure_refinement_can_hurt.py; python/scripts/refinement_help_hurt_sweep.py
- **What was wrong:** Refinement was implicitly treated as monotone-helpful; counterexamples exist when refined cells mix rapidly at the chosen tau.
- **Fix / mitigation:** Added a deterministic negative example and sweep script; inventory statement now conditional and non-monotone.
- **Residual risk:** No formal characterization of the tau/leakage regime for monotone behavior.
- **Proposed next step:** Develop a quantitative metastability criterion linking mixing time and leakage to stable counts.

### EC-009
- **ID:** EC-009
- **Title:** P1 spectral-gap claim needed a gap-decrease example
- **Severity:** Medium
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** T-P1-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (T-P1-01); python/tests/test_graph_spectral_gap_demo.py; python/tests/test_p1_spectral_gap_decrease.py; python/scripts/p1_gap_decrease_demo.py
- **What was wrong:** Only a gap-increase example existed, so claims about slow subspaces/metastability were unsupported.
- **Fix / mitigation:** Added a two-block weight-rewrite example with clear spectral gap decrease; inventory now mentions both directions.
- **Residual risk:** Spectral gap definition is for reversible/lazy walks; nonreversible gaps not addressed.
- **Proposed next step:** Add a short note on spectral-gap conventions and consider nonreversible mixing proxies if needed.

### EC-010
- **ID:** EC-010
- **Title:** Cycle-rank conventions depend on undirected support
- **Severity:** Medium
- **Status:** Closed
- **Impacted theorem-inventory IDs:** D-P2-01, T-P2-01, D-P1-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (P1/P2 entries with undirected support + REV-support); python/tests/test_graph_p2_cycle_rank_monotone.py
- **What was wrong:** Directed vs undirected cycle notions were conflated; beta_1 is computed on undirected support only under REV-support.
- **Fix / mitigation:** Inventory entries now explicitly use undirected support under REV-support; audit scope fixed.
- **Residual risk:** none
- **Proposed next step:** n/a

### EC-011
- **ID:** EC-011
- **Title:** Forcing lemma randomness model needed to be explicit
- **Severity:** Low
- **Status:** Closed
- **Impacted theorem-inventory IDs:** D-FOR-02, T-FOR-01, T-FOR-02
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (FOR entries); python/tests/test_forcing_fixed_weight_differs.py; python/scripts/forcing_sweep.py
- **What was wrong:** Random-predicate model was implicit; fixed-weight sampling can change definability probabilities.
- **Fix / mitigation:** Inventory entries now state IID Bernoulli(1/2) model and include a fixed-weight caveat; test added.
- **Residual risk:** none
- **Proposed next step:** n/a

### EC-012
- **ID:** EC-012
- **Title:** Phase-augmented stationarity requires shared stationary distribution
- **Severity:** Medium
- **Status:** Mitigated
- **Impacted theorem-inventory IDs:** D-PROT-02, T-AOT-02, C-ACC-01
- **Repo evidence pointers:** docs/spec/theorem-inventory.md (D-PROT-02); python/tests/test_protocol_mphase_random_scan.py; python/src/clt/protocol.py
- **What was wrong:** Product-form stationary distribution fails when phase-conditioned kernels do not share a common pi.
- **Fix / mitigation:** Added explicit no-shared-pi test and updated protocol definition to require shared pi for product stationarity.
- **Residual risk:** General stationary characterization for arbitrary S and K_phi is not formalized.
- **Proposed next step:** Add a short lemma about stationary measures for random-scan protocols with mixed kernels.

## Action backlog
- P1: Formalize boundary-term relation between Sigma_T and EP (EC-001).
- P1: Formalize REV-support/EP finiteness conditions in Lean (EC-002).
- P2: Formalize ACC cycle-basis decomposition (EC-004).
- P2: Formalize protocol model class and stationary-product condition (EC-005, EC-012).
- P2: Quantify metastability regime for refinement effects (EC-008).

## Snapshot (pre-draft consistency)
- **Snapshot timestamp (UTC):** 2026-01-13T18:24:12Z
- **Git commit (short):** 2d682e1
- **Lean version:** Lean 4.26.0 (commit d8204c9fd894f91bbb2cdfec5912ec8196fd8562)
- **Mathlib commit:** 2df2f0150c275ad53cb3c90f7c98ec15a56a1a67 (2025-12-13 10:35:53 +0000)
- **Check suite results:** DAG=DAG OK; KB pointers=KB pointers OK - 553 checked (0 errors); Lean build=Build completed successfully (441 jobs); Pytest=43 passed in 1.08s
- **Counts (Status):** Open=0, Mitigated=10, Closed=2, Deferred=0
- **Counts (Severity):** Critical=2, High=4, Medium=5, Low=1
- **Remaining Open/Deferred:** none
