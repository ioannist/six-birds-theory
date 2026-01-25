# Theorem Inventory (Step 2)

## Front matter / conventions

### Assumption bundles (explicit contents)
- A_FIN: finite state space Z and finite-dimensional port spaces; all sets/measures are finite; all maps are measurable.
- A_AUT: time-homogeneous Markov kernel or CTMC rates; no external clock (protocol phase is internal).
- A_REV: microreversibility on support (if k(z->z') > 0 then k(z'->z) > 0).
- A_ACC: edge log-ratio 1-form a(z->z') = log(k(z->z')/k(z'->z)) decomposes as a = dPhi + sum_r A_r * omega_r.
- A_NULL: null regime (all affinities A_r = 0).
- A_STAT: stationary distribution pi with full support.
- A_LENS: coarse-graining map f: Z -> X with induced path pushforward.

### Note
- All hypotheses must be explicit or referenced via bundles above. No implicit defaults.

## Closure machinery

### Entry
- **ID:** D-CL-01
- **Name:** Closure operator
- **Type:** Definition
- **Statement (informal):** A closure operator c is extensive, monotone, and idempotent.
- **Statement (formal sketch):** c: L -> L, (forall x, x <= c(x)), (forall x y, x <= y -> c(x) <= c(y)), and c(c(x)) = c(x).
- **Hypotheses:** L is a partially ordered set (poset).
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/intro.md:L51-L61
- **Override / consistency notes:** none
- **Status:** Lean: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-CL-02
- **Name:** Closed points as objects (fixed points)
- **Type:** Definition
- **Statement (informal):** Objects are fixed points of the closure operator.
- **Statement (formal sketch):** Fix(c) := {x | c(x) = x}.
- **Hypotheses:** D-CL-01
- **Dependencies (by ID):** D-CL-01
- **KB pointers:** docs/knowledge-base/intro.md:L63-L71
- **Override / consistency notes:** none
- **Status:** Lean: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-CL-03
- **Name:** Closure ladder
- **Type:** Definition
- **Statement (informal):** A closure ladder is a chain of closure operators c0 < c1 < c2 < ...
- **Statement (formal sketch):** A sequence (c_n) with c_n <= c_{n+1} pointwise and each c_n a closure operator.
- **Hypotheses:** D-CL-01
- **Dependencies (by ID):** D-CL-01
- **KB pointers:** docs/knowledge-base/intro.md:L730-L738
- **Override / consistency notes:** none
- **Status:** Lean: done
- **Risk / needs stress test:** yes; needs a precise order on closure operators and strictness conditions.
- **Candidate test:** Construct small finite lattices and check monotone chain constraints.

### Entry
- **ID:** T-CAT-01
- **Name:** Closure operator yields a reflective subcategory / idempotent monad
- **Type:** Theorem
- **Statement (informal):** Fixed points of a closure operator form a reflective subcategory; closure is a reflector and defines an idempotent monad.
- **Statement (formal sketch):** For a poset (L, <=) and closure c, inclusion i: Fix(c) -> L has left adjoint c, with c(c(x))=c(x).
- **Hypotheses:** D-CL-01 + D-CL-02
- **Dependencies (by ID):** D-CL-01, D-CL-02
- **KB pointers:** docs/knowledge-base/intro.md:L53-L71
- **Override / consistency notes:** none
- **Status:** Lean: done
- **Risk / needs stress test:** yes; category-theoretic conditions need explicit poset-as-category setup.
- **Candidate test:** Formalize in Lean for a finite lattice.

### Entry
- **ID:** T-CL-01
- **Name:** Closure saturates under fixed rule set
- **Type:** Theorem
- **Statement (informal):** Under a fixed closure operator, iterating closure does not create new objects beyond the first application.
- **Statement (formal sketch):** For all x, c(c(x)) = c(x); hence Fix(c) is stable and no new fixed points arise by further iteration.
- **Hypotheses:** D-CL-01
- **Dependencies (by ID):** D-CL-01
- **KB pointers:** docs/knowledge-base/intro.md:L716-L722
- **Override / consistency notes:** none
- **Status:** Lean: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-CL-02
- **Name:** Closure-only saturates; closure + generic extension can be open-ended
- **Type:** Theorem
- **Statement (informal):** Pure closure stabilizes, while repeated generic extensions can create an infinite strict chain of theories.
- **Statement (formal sketch):** If E_k subset T_k eventually, then T_{k+1}=T_k; if E_k not subset T_k infinitely often, then T_{k+1} superset T_k infinitely often (with strictness).
- **Hypotheses:** D-CL-01 + D-FOR-01 + definability/extension schedule assumptions
- **Dependencies (by ID):** D-CL-01, D-FOR-01
- **KB pointers:** docs/knowledge-base/exercises_1.md:L3745-L3756
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: done (randomized DPI suite N=200, seed=0; strict hiding 3-cycle merge 0&2)
- **Risk / needs stress test:** yes; requires explicit formalization of "extension schedule" and monotonicity conditions.
- **Candidate test:** Toy model with finite closure operator plus scripted extension steps.

## Dynamics-induced closure

### Entry
- **ID:** D-IC-01
- **Name:** Induced empirical closure E_{tau,Pi}
- **Type:** Definition
- **Statement (informal):** Run dynamics for tau steps, coarsen by Pi, then re-lift to canonical representatives; this is an endomap on Δ(Z), not an order-closure operator.
- **Statement (formal sketch):** E_{tau,Pi}(mu) := U_Pi(Q_Pi(mu P^tau)).
- **Hypotheses:** A_FIN + A_LENS
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_1.md:L4087-L4094
- **Override / consistency notes:** none
- **Status:** Lean: planned; Python: done (module: clt.empirical_closure; tests: python/tests/test_empirical_closure_absorption_refinement.py)
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-IC-02
- **Name:** Approximate idempotence (epsilon-idempotent)
- **Type:** Definition
- **Statement (informal):** Define the TV defect on the simplex Δ(Z) and note the supremum is attained at extreme points; this is a metric endomap notion, not an order-closure axiom.
- **Statement (formal sketch):** δ_TV(E) := sup_{μ∈Δ(Z)} |μ(E^2−E)|_TV with |v|_TV := 1/2||v||_1 for signed v; by convexity, δ_TV(E)=max_z |δ_z(E^2−E)|_TV = 1/2 max_i Σ_j |(E^2−E)_{ij}|.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-IC-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L2837-L2840
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: stress test (TV norm on {delta states + uniform}; tests: python/tests/test_empirical_closure_idempotence_defect_leakage.py)
- **Risk / needs stress test:** yes; norm choice and domain of mu must be fixed.
- **Candidate test:** Compute L1 error on representative mu in simulations.

### Entry
- **ID:** T-IC-01
- **Name:** Layer-birth criterion via idempotence of induced closure
- **Type:** Theorem
- **Statement (informal):** If refinement aligns with the metastable decomposition at timescale tau (fast mixing within refined cells, small leakage between them), refinement can increase the number of stable prototypes; if refinement splits a fast-mixing region, stable counts can decrease at that tau.
- **Statement (formal sketch):** Under margin-stability assumptions, E_{tau,Pi} is (approximately) idempotent and its fixed points are the cell prototypes; refinement effects depend on within-cell mixing vs leakage at scale tau (non-monotone in general).
- **Hypotheses:** A_FIN + D-IC-01 + margin-stability condition
- **Dependencies (by ID):** D-IC-01, D-CL-02
- **KB pointers:** docs/knowledge-base/exercises_1.md:L4120-L4135
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_empirical_closure_refinement_reveals_objects.py, python/tests/test_empirical_closure_refinement_can_hurt.py; demo: python/scripts/refinement_help_hurt_sweep.py)
- **Risk / needs stress test:** yes; margin-stability must be formalized and tied to dynamics.
- **Candidate test:** Simulate partitions and verify E^2=E within tolerance.

### Entry
- **ID:** T-IC-02
- **Name:** Approximate idempotence implies metastable objects
- **Type:** Theorem
- **Statement (informal):** When within-cell mixing is fast and leakage is small, E_{tau,Pi} is epsilon-idempotent and objects persist.
- **Statement (formal sketch):** If tau >> t_mix and tau * leakage << 1 then E_{tau,Pi} o E_{tau,Pi} approx E_{tau,Pi} with epsilon = O(tau * leakage).
- **Hypotheses:** A_FIN + D-IC-01 + D-IC-02 + mixing/leakage bounds
- **Dependencies (by ID):** D-IC-01, D-IC-02
- **KB pointers:** docs/knowledge-base/exercises_3.md:L2842-L2852
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence (leakage sweep small vs large; tests: python/tests/test_empirical_closure_idempotence_defect_leakage.py)
- **Risk / needs stress test:** yes; constants depend on model-specific mixing assumptions.
- **Candidate test:** Monte Carlo estimate of leakage vs idempotence error.

## AUT + REV + ACC regime

### Entry
- **ID:** D-AUT-01
- **Name:** Autonomy (AUT)
- **Type:** Definition
- **Statement (informal):** The dynamics are time-homogeneous and any protocol phase is internal.
- **Statement (formal sketch):** k(z->z') is time-independent; no external clock.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_2.md:L367-L375
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-REV-01
- **Name:** Microreversibility (REV)
- **Type:** Definition
- **Statement (informal):** Support graph is undirected: if an edge exists forward it exists backward.
- **Statement (formal sketch):** k(z->z') > 0 implies k(z'->z) > 0.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_2.md:L377-L380
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ACC-01
- **Name:** Edge log-ratio 1-form
- **Type:** Definition
- **Statement (informal):** The edge bias is an antisymmetric log-ratio 1-form on the bidirected support graph.
- **Statement (formal sketch):** a_{ij} := log(k_{ij}/k_{ji}) on bidirected edges (DTMC or CTMC interpretation); a_{ji} = -a_{ij}.
- **Hypotheses:** A_FIN + D-REV-01
- **Dependencies (by ID):** D-REV-01
- **KB pointers:** docs/knowledge-base/exercises_2.md:L384-L387
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_acc_graph_one_form.py)
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ACC-02
- **Name:** ACC decomposition (exact + affinities)
- **Type:** Definition
- **Statement (informal):** The edge 1-form decomposes into an exact part plus cycle affinities; exactness is equivalent to zero cycle integrals.
- **Statement (formal sketch):** a = dPhi + sum_r A_r * omega_r; A_r are cycle integrals over a basis of H^1 (DTMC or CTMC).
- **Hypotheses:** A_FIN + D-ACC-01
- **Dependencies (by ID):** D-ACC-01
- **KB pointers:** docs/knowledge-base/exercises_2.md:L388-L397
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_acc_graph_one_form.py)
- **Risk / needs stress test:** yes; requires explicit basis of exchange 1-forms.
- **Candidate test:** Construct small graphs and verify decomposition.

### Entry
- **ID:** T-ACC-01
- **Name:** No teleology under AUT+REV+ACC in null regime
- **Type:** Theorem
- **Statement (informal):** With no cycle affinities (exact 1-form), detailed balance holds and there are no stationary currents.
- **Statement (formal sketch):** Under A_AUT + A_REV + A_ACC + A_NULL + A_STAT, a = dPhi and pi(z)k(z->z') = pi(z')k(z'->z) with J=0.
- **Hypotheses:** A_AUT + A_REV + A_ACC + A_NULL + A_STAT
- **Dependencies (by ID):** D-AUT-01, D-REV-01, D-ACC-01, D-ACC-02
- **KB pointers:** docs/knowledge-base/exercises_2.md:L418-L428
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; depends on full support and regularity assumptions.
- **Candidate test:** Verify on random reversible CTMCs with A_r = 0.

### Entry
- **ID:** C-ACC-01
- **Name:** P3 alone does not yield sustained arrow-of-time under autonomy
- **Type:** Corollary
- **Statement (informal):** If the protocol phase is internal and unbiased, protocol holonomy cancels; sustained arrow requires P6 or an external schedule.
- **Statement (formal sketch):** Under A_AUT + A_ACC + A_NULL and an autonomous protocol model on X×Φ, any unbiased reversible phase kernel yields reversibility; nonzero arrow requires affinity on the phase cycle.
- **Hypotheses:** A_FIN + A_REV + A_AUT + A_ACC + A_NULL
- **Dependencies (by ID):** D-AUT-01, D-ACC-01, D-ACC-02, D-PROT-01, D-PROT-02, T-AOT-02
- **KB pointers:** docs/knowledge-base/exercises_2.md:L721-L722
- **KB pointers:** docs/knowledge-base/exercises_3.md:L950-L954
- **Override / consistency notes:** Override 1 in docs/registries/overrides.md
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_protocol_trap_external_vs_autonomous.py, python/tests/test_protocol_clock_audit_phi_included.py)
- **Risk / needs stress test:** yes; exact autonomy model of protocol phase must be specified.
- **Candidate test:** Simulate two-phase protocols with alpha=1/2 vs alpha != 1/2.

## Arrow-of-time

### Entry
- **ID:** D-AOT-01
- **Name:** Path reversal asymmetry (finite-horizon)
- **Type:** Definition
- **Statement (informal):** Finite-horizon arrow-of-time is the KL divergence between the forward path law from init rho and its time-reversal; defined for any init rho, but can be infinite if reverse support is missing.
- **Statement (formal sketch):** Sigma_T(rho) := D_KL(P_{rho,T} || R_* P_{rho,T}) on Z^{T+1}; if a path has positive mass but its reverse has zero mass, KL is +inf.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_3.md:L560-L586
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** Nonstationary init yields boundary-term KL even for reversible chains.

### Entry
- **ID:** D-AOT-EP-01
- **Name:** Steady-state entropy production (EP)
- **Type:** Definition
- **Statement (informal):** Steady EP is the path-reversal asymmetry evaluated at a stationary init; requires REV-support for finiteness, and a rate can be defined if the long-time limit exists.
- **Statement (formal sketch):** EP_T := Sigma_T(pi) for stationary pi; sigma := lim_{T->inf} Sigma_T(pi)/T when the limit exists.
- **Hypotheses:** A_FIN + STAT + REV-support (and ERG if stating a rate limit)
- **Dependencies (by ID):** D-AOT-01
- **KB pointers:** docs/knowledge-base/exercises_4.md:L393
- **KB pointers:** docs/knowledge-base/exercises_4.md:L1724
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; long-time rate needs ergodicity assumptions.
- **Candidate test:** Compare reversible vs biased chains under stationary init.

### Entry
- **ID:** L-AOT-STAT-01
- **Name:** Stationary init removes boundary term in path KL
- **Type:** Lemma
- **Statement (informal):** If mu = pi is stationary and REV-support holds, finite-horizon path KL agrees with steady irreversibility/EP over horizon; boundary relaxation term vanishes.
- **Statement (formal sketch):** Under mu=pi and bidirectional support, Sigma_T(pi) matches EP_T; for nonstationary mu, Sigma_T(mu) includes boundary terms.
- **Hypotheses:** A_FIN + STAT + REV-support (and ERG when interpreting long-time rates)
- **Dependencies (by ID):** D-AOT-01, D-AOT-EP-01
- **KB pointers:** docs/knowledge-base/exercises_4.md:L393
- **KB pointers:** docs/knowledge-base/exercises_4.md:L1724
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; EP rate interpretation needs ergodicity.
- **Candidate test:** Compare stationary vs nonstationary init in reversible DTMC.

### Entry
- **ID:** D-LENS-01
- **Name:** Coarse-graining map and path pushforward
- **Type:** Definition
- **Statement (informal):** A lens f: Z -> X induces a path map F and pushforward path measures.
- **Statement (formal sketch):** F(z_0..z_T) = (f(z_0)..f(z_T)); Q_T = F_* P_T.
- **Hypotheses:** A_FIN + A_LENS
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_3.md:L597-L608
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-AOT-01
- **Name:** Data processing for path-space KL
- **Type:** Theorem
- **Statement (informal):** Coarse-graining cannot increase finite-horizon path reversal asymmetry for any init; macro asymmetry is bounded by micro asymmetry (when KL is finite).
- **Statement (formal sketch):** For any init mu, D_KL(Q_T^mu || (Q_T^mu)^rev) <= D_KL(P_T^mu || (P_T^mu)^rev).
- **Hypotheses:** A_FIN + A_LENS
- **Dependencies (by ID):** D-AOT-01, D-LENS-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L611-L618
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-PROT-01
- **Name:** Externally scheduled protocol
- **Type:** Definition
- **Statement (informal):** A protocol applies kernels in a fixed external order, e.g., K1 K0.
- **Statement (formal sketch):** R_ext := K1 K0 with K_i reversible w.r.t. pi.
- **Hypotheses:** A_FIN + A_REV
- **Dependencies (by ID):** D-REV-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L940-L946
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-PROT-02
- **Name:** Autonomous m-phase protocol (random-scan)
- **Type:** Definition
- **Statement (informal):** A protocol is an autonomous Markov chain on X×Φ with phase kernel S and phase-conditioned kernels K_φ; updates mix phase and state without external schedule via random-scan interleaving.
- **Statement (formal sketch):** For α∈[0,1], define P((x,φ),(x',φ')) := α 1_{x'=x} S(φ,φ') + (1-α) 1_{φ'=φ} K_φ(x,x'). If S is reversible w.r.t s and all K_φ reversible w.r.t common π, then μ=π×s is stationary and reversible.
- **Hypotheses:** A_FIN + A_AUT + A_REV
- **Dependencies (by ID):** D-AUT-01, D-REV-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L940-L946
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_protocol_mphase_random_scan.py)
- **Risk / needs stress test:** yes; depends on protocol class and shared-π assumptions.
- **Candidate test:** Compare unbiased vs biased phase kernels and shared vs non-shared π.

### Entry
- **ID:** T-AOT-02
- **Name:** Protocol trap (external schedule implies hidden drive)
- **Type:** Theorem
- **Statement (informal):** External scheduling of reversible kernels can produce apparent irreversibility; under autonomous protocol models (e.g., D-PROT-02) this corresponds to a hidden clock affinity (P6).
- **Statement (formal sketch):** For reversible K0, K1, the external product K1 K0 is nonreversible generically; an autonomous protocol (random-scan on X×Φ) yields reversibility unless the phase kernel is biased.
- **Hypotheses:** A_AUT + A_ACC + A_REV
- **Dependencies (by ID):** D-AUT-01, D-ACC-01, D-ACC-02, D-PROT-01, D-PROT-02
- **KB pointers:** docs/knowledge-base/exercises_3.md:L689-L708
- **Override / consistency notes:** Overrides any P3-only arrow claims.
- **Status:** Informal: needs write-up; Python: evidence (tests: python/tests/test_protocol_trap_external_vs_autonomous.py, python/tests/test_protocol_clock_audit_phi_included.py; demo: python/scripts/protocol_trap_demo.py)
- **Risk / needs stress test:** yes; depends on protocol class and autonomy model.
- **Candidate test:** Compare external schedule vs internal phase simulation.

## Graph topology / primitives

### Entry
- **ID:** D-P2-01
- **Name:** P2 gating (feasible-set edge deletion)
- **Type:** Definition
- **Statement (informal):** P2 acts as constraints that delete edges and restrict feasible transitions (interpreted on the undirected support graph under REV-support).
- **Statement (formal sketch):** Replace undirected support graph G by subgraph G' with edge set E' subset E; dynamics restricted to E' (REV-support justifies bidirected support).
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_3.md:L226-L232
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-P2-01
- **Name:** P2 gating reduces cycle space / H1 channels
- **Type:** Theorem
- **Statement (informal):** Edge deletion can reduce cycle rank and suppress possible affinity channels on the undirected support graph (under REV-support).
- **Statement (formal sketch):** If E' subset E then beta_1(G') <= beta_1(G) for undirected support graphs; feasible H^1 channels shrink (REV-support required).
- **Hypotheses:** A_FIN + graph topology assumptions
- **Dependencies (by ID):** D-P2-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L226-L232
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; requires explicit graph-theoretic model.
- **Candidate test:** Compute cycle rank before/after edge deletions in sample graphs.

### Entry
- **ID:** D-P1-01
- **Name:** P1 rewrite (graph surgery)
- **Type:** Definition
- **Statement (informal):** P1 modifies adjacency/couplings, adding or removing edges (on undirected support under REV-support).
- **Statement (formal sketch):** Replace undirected support graph G by G'' with added/removed edges and updated weights; directed notions needed if REV-support fails.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_3.md:L234-L239
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-P1-01
- **Name:** P1 rewrite can create cycles and alter spectral gap
- **Type:** Theorem
- **Statement (informal):** Graph surgery can increase cycle rank (on the undirected support graph under REV-support) and create slow subspaces enabling metastability.
- **Statement (formal sketch):** There exist rewrites that increase beta_1 and either increase or decrease the spectral gap (weight rewrites can create nearly decomposable structure with small gap).
- **Hypotheses:** A_FIN + graph Laplacian / Markov operator assumptions
- **Dependencies (by ID):** D-P1-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L234-L239
- **KB pointers:** docs/knowledge-base/exercises_3.md:L98-L99
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; requires precise spectral definitions and bounds.
- **Candidate test:** Spectral gap comparison before/after graph edits (see python/tests/test_graph_spectral_gap_demo.py and python/tests/test_p1_spectral_gap_decrease.py; demo: python/scripts/p1_gap_decrease_demo.py).

## Generic extension / forcing

### Entry
- **ID:** D-FOR-01
- **Name:** Generic extension (logical)
- **Type:** Definition
- **Statement (informal):** A generic extension adds objects consistent with prior axioms but not definable from them.
- **Statement (formal sketch):** Given a theory T, extend to T' = Cl(T U {generic}) with generic not definable in the old language.
- **Hypotheses:** A_FIN (abstract model)
- **Dependencies (by ID):** none
- **KB pointers:** docs/knowledge-base/exercises_1.md:L3028-L3036
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; formal definition depends on chosen logic framework.
- **Candidate test:** Formalize in a toy first-order model.

### Entry
- **ID:** D-FOR-02
- **Name:** Definability relative to lens/partition (finite)
- **Type:** Definition
- **Statement (informal):** "Definable" means measurable with respect to the current lens/partition; random predicate model is IID Bernoulli(1/2) on Z (uniform over {0,1}^Z).
- **Statement (formal sketch):** A predicate is definable iff it is measurable w.r.t. sigma(f) induced by f.
- **Hypotheses:** A_FIN + A_LENS
- **Dependencies (by ID):** D-LENS-01
- **KB pointers:** docs/knowledge-base/exercises_4.md:L365-L385
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** yes; exact sigma-algebra model must be fixed.
- **Candidate test:** Compare definable predicates vs full predicate set in finite cases.

### Entry
- **ID:** T-FOR-01
- **Name:** Physical forcing lemma (Theorem 18.1)
- **Type:** Theorem
- **Statement (informal):** With high-entropy internal degrees and IID Bernoulli(1/2) predicates, typical stabilized predicates split old equivalence classes and are non-definable from the old language; fixed-weight sampling changes these probabilities and can force zero.
- **Statement (formal sketch):** Under admissible constraints and high internal randomness, probability(new predicate definable) is exponentially small.
- **Hypotheses:** A_FIN + A_LENS + mixing/admissibility assumptions
- **Dependencies (by ID):** D-FOR-02
- **KB pointers:** docs/knowledge-base/exercises_3.md:L445-L452
- **KB pointers:** docs/knowledge-base/exercises_4.md:L369-L380
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence added (tests: python/tests/test_forcing_exact_enumeration.py, python/tests/test_forcing_monte_carlo_matches_theory.py; demo: python/scripts/forcing_sweep.py)
- **Risk / needs stress test:** yes; depends on precise admissibility and randomness assumptions.
- **Candidate test:** Random predicate sampling with fixed coarse partition.

### Entry
- **ID:** T-FOR-02
- **Name:** Definable predicates are exponentially rare
- **Type:** Theorem
- **Statement (informal):** Counting argument (IID Bernoulli(1/2) model) shows definable predicates are rare among all predicates; fixed-weight models give different probabilities (can be zero depending on block sizes).
- **Statement (formal sketch):** |Definable| / |All predicates| <= exp(-c n) under a suitable model.
- **Hypotheses:** A_FIN + A_LENS
- **Dependencies (by ID):** D-FOR-02
- **KB pointers:** docs/knowledge-base/exercises_4.md:L383-L386
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up; Python: evidence added (tests: python/tests/test_forcing_exact_enumeration.py, python/tests/test_forcing_monte_carlo_matches_theory.py; demo: python/scripts/forcing_sweep.py)
- **Risk / needs stress test:** yes; depends on the chosen counting model and parameters.
- **Candidate test:** Count definable predicates in small finite partitions.

## Appendix Zeno decision frontier

### Entry
- **ID:** D-ZENO-01
- **Name:** Frontier, crossing times, and Zeno cascade
- **Type:** Definition
- **Statement (informal):** Define the activity frontier j_*(t), crossing times t_j, step durations Delta t_j, and a Zeno cascade as bounded (t_j) or summable Delta t_j.
- **Statement (formal sketch):** j_*(t)=max{j: E_j(t)>=theta}, t_j=inf{t: j_*(t)>=j}, Delta t_j=t_{j+1}-t_j; Zeno iff sum Delta t_j < infinity.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix definition
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ZENO-02
- **Name:** Port accounting and positive supplied work
- **Type:** Definition
- **Statement (informal):** Port input/output u_j, y_j define instantaneous power p_j and positive supply p_j^+; supplied work W_j^+ integrates p_j^+ over time.
- **Statement (formal sketch):** p_j(t)=<u_j(t),y_j(t)>, p_j^+(t)=max(p_j(t),0), W_j^+[s,t]=int_s^t p_j^+.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix definition
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ZENO-03
- **Name:** Passive storage inequality and storage-based activity (Option B)
- **Type:** Definition
- **Statement (informal):** Passive storage inequality bounds storage growth by supplied work; activity is the supremum storage gain since activation time.
- **Statement (formal sketch):** S_j(x(t))-S_j(x(s)) <= int_s^t p_j <= W_j^+[s,t], E_{j+1}(t)=sup_{s in [t_j,t]}(S_j(x(s))-S_j(x(t_j))).
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-ZENO-02
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix definition
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ZENO-04
- **Name:** Integrated capacity and feasibility (ICAP/FEAS)
- **Type:** Definition
- **Statement (informal):** ICAP bounds supplied work by integrated port energy; FEAS bounds port energy by an average density on each crossing interval.
- **Statement (formal sketch):** W_j^+[s,t] <= Lambda(j) int_s^t ||u_j||^2, and int_{t_j}^{t_{j+1}} ||u_j||^2 <= \bar B(j) Delta t_j.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-ZENO-02
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix definition
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-ZENO-01
- **Name:** WORK quantum from storage growth
- **Type:** Lemma
- **Statement (informal):** If storage grows by at least theta over a crossing interval, supplied positive work is at least theta.
- **Statement (formal sketch):** From passive storage inequality and definition of t_{j+1}, W_j^+[t_j,t_{j+1}] >= theta.
- **Hypotheses:** A_FIN + D-ZENO-03
- **Dependencies (by ID):** D-ZENO-02, D-ZENO-03
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix lemma
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-ZENO-02
- **Name:** Latency lower bound from WORK+ICAP+FEAS
- **Type:** Lemma
- **Statement (informal):** WORK plus ICAP and FEAS imply Delta t_j >= theta / (Lambda(j) \bar B(j)).
- **Statement (formal sketch):** Combine WORK lower bound with ICAP and FEAS upper bounds on W_j^+.
- **Hypotheses:** A_FIN + D-ZENO-04 + T-ZENO-01
- **Dependencies (by ID):** D-ZENO-04, T-ZENO-01
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix lemma
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** T-ZENO-03
- **Name:** No-Zeno from divergent reciprocal capacity
- **Type:** Theorem
- **Statement (informal):** If sum_j 1/Cap(j) diverges and WORK+ICAP+FEAS hold, Zeno cascades are ruled out.
- **Statement (formal sketch):** Delta t_j >= theta / Cap(j) and divergence implies sum Delta t_j = infinity.
- **Hypotheses:** A_FIN + T-ZENO-02
- **Dependencies (by ID):** T-ZENO-02
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Informal: appendix theorem
- **Risk / needs stress test:** no
- **Candidate test:** n/a

## Diagnostics / counterexamples

### Entry
- **ID:** DIAG-PT-01
- **Name:** Protocol trap audit checklist
- **Type:** Diagnostic
- **Statement (informal):** Audit a protocol claim by making the schedule internal and checking whether a phase bias exists.
- **Statement (formal sketch):** Replace external order by internal phase variable; if phase bias alpha = 1/2, stroboscopic kernel is reversible.
- **Hypotheses:** A_AUT + A_ACC
- **Dependencies (by ID):** D-AUT-01, D-ACC-01, D-PROT-01
- **KB pointers:** docs/knowledge-base/exercises_3.md:L936-L954
- **Override / consistency notes:** supports Override 1 in docs/registries/overrides.md
- **Status:** Python: planned
- **Risk / needs stress test:** yes; needs a precise audit procedure for different protocol classes.
- **Candidate test:** Automated check: external vs internal schedule equivalence.

### Entry
- **ID:** CE-P3-01
- **Name:** Two-state protocols cannot produce holonomy
- **Type:** Counterexample
- **Statement (informal):** In a two-state system, reversible kernels commute and protocol holonomy is impossible.
- **Statement (formal sketch):** For |X|=2 and reversible K_phi, all K_phi commute; any protocol product is reversible.
- **Hypotheses:** A_FIN + A_REV
- **Dependencies (by ID):** D-REV-01
- **KB pointers:** docs/knowledge-base/exercises_1.md:L2234-L2249
- **Override / consistency notes:** none
- **Status:** Informal: needs write-up
- **Risk / needs stress test:** no
- **Candidate test:** n/a

## Toolkit additions (planned)

### Entry
- **ID:** D-TK-THY-01
- **Name:** Theory package
- **Type:** Definition
- **Statement (informal):** A theory package bundles a lens/definability layer, a completion endomap, and an audit rule.
- **Statement (formal sketch):** Package := (f: Z -> X, E: Δ(Z) -> Δ(Z), audit: ...), with named components used by the toolkit.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-LENS-01, D-IC-01
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** yes; tuple components and audit interface to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-CERT-01
- **Name:** Toolkit certificates (stability, novelty, directionality)
- **Type:** Definition
- **Statement (informal):** Define stability, novelty, and directionality certificates as named predicates attached to a theory package.
- **Statement (formal sketch):** Certs := (stable: ..., novel: ..., directional: ...), each with an audit predicate.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-THY-01
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** yes; certificate interfaces to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-DEF-01
- **Name:** Defect calculus (generic defect notion)
- **Type:** Definition
- **Statement (informal):** A defect is a nonnegative functional measuring deviation from an idealized property.
- **Statement (formal sketch):** Defect: Obj -> [0, +inf] with optional composition rules (remark-only).
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** yes; admissible classes to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-DEF-02
- **Name:** Idempotence defect (TV/L1)
- **Type:** Definition
- **Statement (informal):** Define idempotence defect as a TV/L1 distance between E^2 and E, attained at extreme points.
- **Statement (formal sketch):** δ(E) := sup_{μ in Δ(Z)} ||μ(E^2 - E)||_TV = max_z ||δ_z(E^2 - E)||_TV.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-DEF-01
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-ROUTE-01
- **Name:** Route mismatch observable
- **Type:** Definition
- **Statement (informal):** Define RM(j) as a mismatch observable tied to boundary j in a bridge chain.
- **Statement (formal sketch):** RM(j) := ... (boundary-level mismatch functional).
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-01
- **Manuscript labels:** def:ect-atom
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** yes; exact functional form to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-BRG-01
- **Name:** Bridge object (ports + causal operator + accounting)
- **Type:** Definition
- **Statement (informal):** A bridge object specifies ports, a causal operator, and an accounting map.
- **Statement (formal sketch):** Bridge := (U, V, T, accounting, storage?) with typed ports and a causal map.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** none
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** yes; port/causal types to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-BRG-02
- **Name:** Passivity with storage
- **Type:** Definition
- **Statement (informal):** A bridge is passive with storage if storage growth bounds extracted work.
- **Statement (formal sketch):** W^+[s,t] <= S(t) - S(s) with nonnegative storage S.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-01
- **Manuscript labels:** def:tk-passive-storage
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-TK-BRG-03
- **Name:** ICAP (integrated capacity inequality)
- **Type:** Definition
- **Statement (informal):** Integrated capacity bounds work by integrated port energy.
- **Statement (formal sketch):** W^+[s,t] <= Lambda * ∫ ||u(τ)||^2 dτ.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-01
- **Manuscript labels:** def:tk-icap
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-TK-ROUTE-01
- **Name:** Route mismatch bound on capacity
- **Type:** Lemma
- **Statement (informal):** Route mismatch controls a capacity/throughput lower bound via a triangle or submultiplicativity inequality.
- **Statement (formal sketch):** RM(j) <= f(capacity terms) or capacity >= g(RM(j)) for a fixed bridge model.
- **Hypotheses:** A_FIN + D-TK-ROUTE-01 + D-TK-BRG-03
- **Dependencies (by ID):** D-TK-ROUTE-01, D-TK-BRG-03
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** Planned
- **Risk / needs stress test:** yes; inequality form to be fixed.
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-ATOM-01
- **Name:** Atomic/sector decomposition and mode count
- **Type:** Definition
- **Statement (informal):** Decompose a packaged bridge into sector atoms with mode count m_j.
- **Statement (formal sketch):** Z_j = sum_{r<=m_j} Z_{j,r} with m_j the number of active atoms.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-01
- **Manuscript labels:** def:ect-atom
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-CAP-01
- **Name:** Capacity / ICAP constant functional
- **Type:** Definition
- **Statement (informal):** Define Cap(Z) as the minimal ICAP constant for a bridge Z.
- **Statement (formal sketch):** Cap(Z) := inf {Lambda : Z satisfies ICAP with constant Lambda}.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-03
- **Manuscript labels:** def:ect-cap
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-GATE-01
- **Name:** Feasibility gate and induced coercive norm
- **Type:** Definition
- **Statement (informal):** A gating operator defines a feasible subspace and an induced norm that is coercive on it.
- **Statement (formal sketch):** Given $G_j\succeq 0$ on $U_j$, define $\mathcal U_j^{\mathrm{feas}}=\{u:u(t)\in\mathrm{Ran}(G_j)\}$ and $|u|_{X_j}^2=\int_0^T\langle u,G_j u\rangle$.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-01
- **Manuscript labels:** def:ect-gate
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-FMEM-01
- **Name:** Finite-memory convolution kernel implies ICAP
- **Type:** Lemma
- **Statement (informal):** A causal convolution bridge with integrable operator-kernel mass has an ICAP constant given by the mass M.
- **Statement (formal sketch):** If y(t)=∫_0^t K(t-s)u(s)ds with k(s)=||K(s)||op and ∫_0^∞ k(s)ds=M<∞, then for truncated inputs u^{[s,t]} the positive work satisfies W^+[s,t]≤M∫_s^t||u(τ)||^2 dτ.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-TK-BRG-03
- **Manuscript labels:** lem:ect-fmem
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-COER-01
- **Name:** Coercivity on the feasible set
- **Type:** Lemma
- **Statement (informal):** On feasible inputs, strict passivity reduces to the gating inner-product inequality.
- **Statement (formal sketch):** If for all feasible $u$, $\int_s^t\langle u, \mathsf Z_j u\rangle \ge \int_s^t\langle u,G_j u\rangle$, then $\int_s^t\langle u,\mathsf Z_j u\rangle \ge \int_s^t |u|_{X_j}^2$.
- **Hypotheses:** A_FIN + D-ECT-GATE-01
- **Dependencies (by ID):** D-ECT-GATE-01, D-TK-BRG-01
- **Manuscript labels:** lem:ect-coer-feas
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-SHRINK-01
- **Name:** Feasibility shrinkage implies depth-scaled coercivity
- **Type:** Lemma
- **Statement (informal):** A shrinkage bound on the gated norm yields a depth-scaled coercivity coefficient in the baseline norm.
- **Statement (formal sketch):** If $\int \langle u,G_j u\rangle \ge a_j^2\int \|u\|^2$ on feasible inputs, then $\int \langle u,\mathsf Z_j u\rangle \ge a_j^2\int \|u\|^2$.
- **Hypotheses:** A_FIN + D-ECT-GATE-01 + L-ECT-COER-01
- **Dependencies (by ID):** D-ECT-GATE-01, L-ECT-COER-01
- **Manuscript labels:** lem:ect-shrink
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-SECT-01
- **Name:** Sectorization of the port space
- **Type:** Definition
- **Statement (informal):** A finite projection partition of the port space defines sectors and sector-respecting bridges.
- **Statement (formal sketch):** Choose $Q_j$ and orthogonal projections $\Pi_{j,q}$ with $\sum_q \Pi_{j,q}=I$; sector-respecting means $\mathsf Z_j=\sum_q \Pi_{j,q}\mathsf Z_j\Pi_{j,q}$.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-ECT-ATOM-01
- **Manuscript labels:** def:ect-sectorization
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-P5MIN-01
- **Name:** Sector-respecting minimal decompositions (P5-min)
- **Type:** Definition
- **Statement (informal):** Define sector-respecting atoms and the minimal sector-respecting mode count $m_j^{\min}$.
- **Statement (formal sketch):** $\mathsf Z_{j,r}=\Pi_{j,\sigma(r)}\mathsf Z_{j,r}\Pi_{j,\sigma(r)}$ and $m_j^{\min}$ is the smallest number of nonzero sector atoms; P5-min returns a decomposition achieving $m_j^{\min}$.
- **Hypotheses:** A_FIN + D-ECT-SECT-01
- **Dependencies (by ID):** D-ECT-ATOM-01, D-ECT-SECT-01
- **Manuscript labels:** def:ect-p5min
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-MODE-UB-01
- **Name:** Sectorization bounds the minimal mode count
- **Type:** Lemma
- **Statement (informal):** Sector-respecting decompositions merge within sectors to give $m_j^{\min}\le |Q_j|$; under P5-min, $m_j\le |Q_j|$.
- **Statement (formal sketch):** Merge atoms with the same sector label to obtain at most one nonzero atom per sector; conclude the bound.
- **Hypotheses:** A_FIN + D-ECT-SECT-01 + D-ECT-P5MIN-01
- **Dependencies (by ID):** D-ECT-ATOM-01, D-ECT-SECT-01, D-ECT-P5MIN-01
- **Manuscript labels:** lem:ect-mode-ub
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-P4IDX-01
- **Name:** Quantized index hypothesis for sectors
- **Type:** Definition
- **Statement (informal):** A quantized index injectively labels sectors by O(j) integers.
- **Statement (formal sketch):** There exists an injection $\iota_j:Q_j\hookrightarrow\{0,\dots,\lceil C_0(j+1)\rceil-1\}$.
- **Hypotheses:** A_FIN + D-ECT-SECT-01
- **Dependencies (by ID):** D-ECT-SECT-01
- **Manuscript labels:** def:ect-p4-idx
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-QSIZE-01
- **Name:** Quantized index implies linear sector count
- **Type:** Lemma
- **Statement (informal):** Under quantized indexing, the number of sectors is at most $\lceil C_0(j+1)\rceil$.
- **Statement (formal sketch):** Injectivity gives $|Q_j|\le \lceil C_0(j+1)\rceil$.
- **Hypotheses:** A_FIN + D-ECT-P4IDX-01
- **Dependencies (by ID):** D-ECT-P4IDX-01
- **Manuscript labels:** lem:ect-qsize
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** C-ECT-HL1-01
- **Name:** Linear mode bound from sectorization + P4 index
- **Type:** Corollary
- **Statement (informal):** Under P5-min packaging and quantized indexing, $m_j\le \lceil C_0(j+1)\rceil$.
- **Statement (formal sketch):** Combine $m_j\le |Q_j|$ with $|Q_j|\le \lceil C_0(j+1)\rceil$.
- **Hypotheses:** A_FIN + D-ECT-P5MIN-01 + L-ECT-MODE-UB-01 + L-ECT-QSIZE-01
- **Dependencies (by ID):** D-ECT-P5MIN-01, L-ECT-MODE-UB-01, L-ECT-QSIZE-01
- **Manuscript labels:** cor:ect-hl1
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-ATOM-SS-01
- **Name:** Dissipative atom state/semigroup representation
- **Type:** Definition
- **Statement (informal):** A per-atom state-space kernel representation with exponential decay.
- **Statement (formal sketch):** $K_r(\\tau)=C_r e^{A_r\\tau} B_r$ with decay rate $\\lambda_r>0$ on a finite horizon atom.
- **Hypotheses:** A_FIN
- **Dependencies (by ID):** D-ECT-ATOM-01
- **Manuscript labels:** def:ect-atom-ss
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), definition: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** D-ECT-BAL-01
- **Name:** Balanced coupling condition
- **Type:** Definition
- **Statement (informal):** Balanced decay/coupling bound for dissipative atoms.
- **Statement (formal sketch):** $\\|C_r\\|\\,\\|B_r\\|\\le \\Lambda_0\\,\\lambda_r$ (or equivalent) for each atom.
- **Hypotheses:** A_FIN + D-ECT-ATOM-SS-01
- **Dependencies (by ID):** D-ECT-ATOM-SS-01
- **Manuscript labels:** def:ect-bal
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), definition: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-BAL-KMASS-01
- **Name:** Balanced decay implies kernel mass bound
- **Type:** Lemma
- **Statement (informal):** Balanced decay bounds the operator-kernel mass by $\\Lambda_0$.
- **Statement (formal sketch):** If $K_r(\\tau)=C_r e^{A_r\\tau} B_r$ with decay rate $\\lambda_r$ and $\\|C_r\\|\\,\\|B_r\\|\\le \\Lambda_0\\,\\lambda_r$, then $\\int_0^\\infty \\|K_r(\\tau)\\|_{op}\\,d\\tau\\le \\Lambda_0$.
- **Hypotheses:** A_FIN + D-ECT-ATOM-SS-01 + D-ECT-BAL-01
- **Dependencies (by ID):** D-ECT-ATOM-SS-01, D-ECT-BAL-01
- **Manuscript labels:** lem:ect-bal-kmass
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** C-ECT-BAL-ICAP-01
- **Name:** Kernel mass implies per-atom ICAP (incremental)
- **Type:** Corollary
- **Statement (informal):** Kernel mass control yields incremental ICAP for the atom.
- **Statement (formal sketch):** Combine $\\int_0^\\infty \\|K_r\\|_{op}\\le \\Lambda_0$ with Lemma L-ECT-FMEM-01 to get ICAP on truncated inputs and $\\mathrm{Cap}(\\mathsf Z_{j,r})\\le \\Lambda_0$.
- **Hypotheses:** A_FIN + L-ECT-BAL-KMASS-01 + L-ECT-FMEM-01
- **Dependencies (by ID):** L-ECT-BAL-KMASS-01, L-ECT-FMEM-01
- **Manuscript labels:** cor:ect-bal-icap
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

### Entry
- **ID:** L-ECT-MECH-01
- **Name:** Mechanical ECT lemma (atomic ICAP ⇒ linear capacity)
- **Type:** Lemma
- **Statement (informal):** Uniform ICAP per atom implies Cap(Z_j) ≤ Lambda_0 m_j and hence linear-in-j capacity under m_j ≤ C(j+1), yielding divergence of sum 1/Cap(j).
- **Statement (formal sketch):** If Z_j = sum_{r<=m_j} Z_{j,r} and each Z_{j,r} has ICAP constant Lambda_0, then Cap(Z_j) ≤ Lambda_0 m_j. If m_j ≤ C(j+1), then Cap(j) ≲ (j+1) and sum_j 1/Cap(j) diverges.
- **Hypotheses:** A_FIN + D-ECT-ATOM-01 + D-ECT-CAP-01
- **Dependencies (by ID):** D-ECT-ATOM-01, D-ECT-CAP-01, D-TK-BRG-03
- **Manuscript labels:** lem:ect-mech
- **KB pointers:** n/a
- **Override / consistency notes:** none
- **Status:** In manuscript (appendix), informal proof: done
- **Risk / needs stress test:** no
- **Candidate test:** n/a

## Open holes / missing lemmas
- T-IC-02: constants and norms in the epsilon-idempotent bound not fixed.
- T-ACC-01: needs explicit conditions for existence/uniqueness of stationary pi.
- T-P2-01: requires a formal link between edge deletion and H1 or beta_1.
- T-P1-01: requires explicit spectral gap definitions and perturbation bounds.
- T-FOR-01: admissibility and randomness assumptions must be formalized.

## META: self-generated primitives (main text; planned)

### Entry
- **ID:** D-META-PROC-01
- **Name:** Process soup (composable happenings)
- **Type:** Definition
- **Statement (informal):** A minimal composability structure (partial semigroup / small category skeleton).
- **Statement (formal sketch):** A set with partially defined associative composition and identities where applicable.
- **Hypotheses:** none
- **Dependencies (by ID):** none
- **Notes:** Provides the pre-measurement ambient for primitives.
- **Manuscript labels:** def:meta-proc
- **Status:** In manuscript (main text), informal proof sketch: done

### Entry
- **ID:** D-META-LENS-01
- **Name:** Interface lens / limited access map
- **Type:** Definition
- **Statement (informal):** A structural observation map specifying accessible distinctions.
- **Statement (formal sketch):** A projection / functor / congruence generator that identifies indistinguishable states.
- **Hypotheses:** D-META-PROC-01
- **Dependencies (by ID):** D-META-PROC-01
- **Notes:** Related to the lens/coarse-graining notion used under A_LENS, but pre-measurement/structural.
- **Manuscript labels:** def:meta-lens
- **Status:** In manuscript (main text), informal proof sketch: done

### Entry
- **ID:** D-META-REF-01
- **Name:** Refinement family of lenses
- **Type:** Definition
- **Statement (informal):** Nested limited-access views indexed by resolution.
- **Statement (formal sketch):** A directed family of lenses inducing a resolution ladder.
- **Hypotheses:** D-META-LENS-01
- **Dependencies (by ID):** D-META-LENS-01
- **Notes:** Intended to induce a closure ladder in the main text.
- **Manuscript labels:** def:meta-ref
- **Status:** In manuscript (main text), informal proof sketch: done

### Entry
- **ID:** D-META-BND-01
- **Name:** Bounded interface / finiteness-locality
- **Type:** Definition
- **Statement (informal):** Each lens exposes only finitely many distinctions compared to the interior.
- **Statement (formal sketch):** Uniform bound on observable signature per lens level.
- **Hypotheses:** D-META-REF-01
- **Dependencies (by ID):** D-META-REF-01
- **Notes:** Encodes interface smaller than interior at each resolution.
  - Clarification: D-META-BND-01 is an explicit hypothesis on the lens hierarchy (bounded observable signature); it is not implied by refinement (D-META-REF-01) alone.
- **Manuscript labels:** def:meta-bnd
- **Status:** In manuscript (main text), informal proof sketch: done

### Entry
- **ID:** T-META-PRIM-01
- **Name:** Self-generated primitives (P1--P6)
- **Type:** Theorem
- **Statement (informal):** Under composability + limited access + bounded interfaces + refinement, primitives P1--P6 are forced as closure mechanics.
- **Statement (formal sketch):** From D-META-PROC-01 + D-META-LENS-01 + D-META-REF-01 + D-META-BND-01 derive the six primitive moves as necessary closure operations.
- **Hypotheses:** D-META-PROC-01 + D-META-LENS-01 + D-META-REF-01 + D-META-BND-01
- **Dependencies (by ID):** D-META-PROC-01, D-META-LENS-01, D-META-REF-01, D-META-BND-01
- **Notes:** Does not claim coarse-graining creates arrow-of-time; directionality remains governed by DPI/path-KL (AOT section).
  - Clarify dependency split: P5/P6/P4/P2 are construction-level; P1 depends on HL-META-1 (stability for induced macro-update); P3 depends on HL-META-3 (route multiplicity), and P4 is nontrivial only under HL-META-2 (strict refinement somewhere).
  - Emphasize “accounting” here is an information/feasibility preorder, not an arrow-of-time claim.
- **Manuscript labels:** sec:meta-unavoidable, thm:meta-prim
- **Status:** In manuscript (main text), informal proof sketch: done
