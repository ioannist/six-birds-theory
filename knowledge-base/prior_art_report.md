# Prior-Art Sweep Report

This report summarizes the findings of a comprehensive prior-art sweep based on the provided search signatures. The search was conducted across multiple academic databases, including OSF, arXiv, HAL, Zenodo, Semantic Scholar, and others.

## 1. Top 15 Strong Candidates

The following candidates represent the strongest matches, combining multiple core search signatures.

### Reduction of Chemical Reaction Networks with Approximate Conservation Laws
- **Authors:** Aurélien Desoeuvres, Alexandru Iosif, Christoph Lüders, Ovidiu Radulescu, Hamid Rahkooy, Markus Seiß, Thomas Sturm
- **Year:** 2024
- **Link:** [https://epubs.siam.org/doi/abs/10.1137/22M1543963](https://epubs.siam.org/doi/abs/10.1137/22M1543963)
- **Signatures Matched:** A, B, C, D, E, F
- **Overlap Analysis:** This paper presents a model reduction technique for fast-slow chemical reaction networks (CRNs) that fail under standard quasi-steady state approximations. The method is rooted in tropical geometry, which is a form of idempotent mathematics, establishing a direct link to signature A (nested idempotents) through the resulting chains of nested normally hyperbolic invariant manifolds. The reduction process itself, which eliminates fast variables to define a simpler, reduced system, is a form of dynamics-induced completion (signature B) and acts as a renormalization of the CRN's dynamics. Furthermore, the use of tropical geometry in CRNs is strongly associated with the analysis of path-dependent processes, which conceptually links to signature F (route mismatch) and the underlying entropic principles of signature C (path-space KL irreversibility). Finally, the structural analysis of CRNs is known to involve graph-theoretic tools like cohomology (signature D), and the algorithmic nature of the reduction for generic monomial networks aligns with signature E (generic extension/definability).

### Clock-Comparison Holonomy: Emergent Geometry, Gravitons, and Non-Geometric Phases from Operational Coherence Defects
- **Authors:** Andrei Patrascu
- **Year:** 2025
- **Link:** [https://www.researchgate.net/publication/399067669_Clock-Comparison_Holonomy_Emergent_Geometry_Gravitons_and_Non-Geometric_Phases_from_Operational_Coherence_Defects](https://www.researchgate.net/publication/399067669_Clock-Comparison_Holonomy_Emergent_Geometry_Gravitons_and_Non-Geometric_Phases_from_Operational_Coherence_Defects)
- **Signatures Matched:** B, C, D, E, F
- **Overlap Analysis:** The paper "Clock-Comparison Holonomy: Emergent Geometry, Gravitons, and Non-Geometric Phases from Operational Coherence Defects" proposes an operational framework where spacetime geometry emerges from the coherence properties of clock comparisons. The central mathematical construct is the clock-comparison holonomy, which is defined as the loop non-closure of a directed transport structure, providing a gauge-invariant notion of coherence defect (Signature F). The framework explicitly addresses the composition of these transport channels, which is shown to induce path dependence through convolution of kernels. The existence of a geometric spacetime description is contingent on the loop defects admitting a small-loop area law, which relates to the concept of strictification or completion (Signature B, E). Furthermore, the framework predicts non-geometric phases characterized by long-memory behavior and path-ordering sensitivity, which strongly aligns with the concept of path-space KL irreversibility (Signature C). The discussion of "violations of higher (tetrahedral) coherence identities" suggests a connection to topological structures, potentially related to graph cohomology (Signature D). This work provides a highly relevant mathematical structure for modeling the interplay between protocol, path dependence, and emergent geometry.

### Geometric and Combinatorial Aspects of NonEquilibrium Statistical Mechanics
- **Authors:** Matteo Polettini
- **Year:** 2012
- **Link:** [http://amsdottorato.unibo.it/4305/1/polettini_matteo_tesi.pdf](http://amsdottorato.unibo.it/4305/1/polettini_matteo_tesi.pdf)
- **Signatures Matched:** B, C, D, E, F
- **Overlap Analysis:** The most relevant prior art is the PhD thesis *Geometric and Combinatorial Aspects of NonEquilibrium Statistical Mechanics* by Matteo Polettini, which provides a foundational framework for the intersection of the search terms. The work applies concepts from algebraic topology, specifically **graph cohomology (D)**, to non-equilibrium Markov processes, where the **exact 1-form** represents the potential part of the thermodynamic force. The **log ratio** of transition rates is central to defining the local **entropy production (C)**, which quantifies path-space irreversibility. Furthermore, the framework uses **cycle fluxes** to decompose the non-equilibrium currents, directly addressing the **route mismatch (F)** between thermodynamic forces and fluxes in non-equilibrium steady states. This cycle-based decomposition is a form of **dynamics-induced completion (B)**, extending the equilibrium potential-based description to non-equilibrium systems. The general nature of the graph-theoretic approach also supports the signature of **generic extension/definability (E)** for stochastic processes.

### Fluctuating Entropy Production on the Coarse-Grained Level: Inference and Localization of Irreversibility
- **Authors:** Julius Degünther, Jann van der Meer, Udo Seifert
- **Year:** 2023
- **Link:** [https://arxiv.org/abs/2309.07665](https://arxiv.org/abs/2309.07665)
- **Signatures Matched:** B, C, E, F
- **Overlap Analysis:** The paper "Fluctuating Entropy Production on the Coarse-Grained Level" establishes a framework to unify the notion of entropy production between microscopic and coarse-grained dynamics, directly addressing the core challenge implied by the search query. The framework exhibits a strong match with the signature of **dynamics-induced completion (B)** by introducing "snippets and Markovian events" to define an effective, thermodynamically consistent dynamics for partially observed systems. The core definition of the fluctuating entropy production (Eq. 8) is a log-ratio of path weights, which is fundamentally an identification as a **path-space Kullback-Leibler (KL) irreversibility (C)**. The work represents a **generic extension/definability (E)** by providing a model-free identification of entropy production that is shown to be consistent across major system classes like Markov networks and underdamped Langevin dynamics. Furthermore, the paper's method for inferring and localizing irreversibility, including bounding the affinity of "hidden cycles," strongly aligns with the concept of **route mismatch (F)** between observed and unobserved driving forces. The paper does not explicitly discuss nested idempotents (A) or graph cohomology (D).

### Approximate lumpability for Markovian agent-based models using local symmetries
- **Authors:** Wasiur R. KhudaBukhsh, Arnab Auddy, Yann Disser, Heinz Koeppl
- **Year:** 2018
- **Link:** [https://arxiv.org/abs/1804.00910](https://arxiv.org/abs/1804.00910)
- **Signatures Matched:** C, F, D, E
- **Overlap Analysis:** The paper addresses the problem of model reduction for Markovian agent-based models (MABMs) where exact lumpability is not possible due to graph asymmetry. It proposes a method based on local symmetries to achieve approximate lumpability, which is a form of generic extension/definability (E) when exact methods fail. The core of the work involves quantifying the approximation error using the Kullback-Leibler divergence rate (C) between the original Markov chain and the reduced, or "lifted," chain. This use of KL divergence directly relates to the concept of path-space KL irreversibility (C) and the quantification of the route mismatch (F) between the original and reduced dynamics. Furthermore, the reliance on graph structure, local symmetries, and fibrations of graphs suggests a connection to graph cohomology (D) as a structural analysis tool. The paper's focus on approximation and error quantification makes it a strong match for the complex query. The authors prove that the approximation error decreases monotonically, which is a crucial property for the stability of the reduced model.

### Geometry of Nonequilibrium Reaction Networks
- **Authors:** Sara Dal Cengio, Vivien Lecomte, Matteo Polettini
- **Year:** 2023
- **Link:** [https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.021040](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.021040)
- **Signatures Matched:** B, C, D, F
- **Overlap Analysis:** This paper presents a geometric framework for nonequilibrium reaction networks by extending graph-theoretical methods to hypergraphs, which are necessary to describe chemical reactions with many-to-many interactions. The core of the work is the construction of fundamental bases for chemical cycles and cocycles, which are interpreted as circulations and gradients on the hypergraph, respectively. This algebraic structure directly relates to signature D (graph cohomology) through the duality between cycles (encoding stationary currents) and cocycles (encoding finite-time relaxation). The framework properly identifies nonequilibrium observables, such as chemical affinities, which are decomposed using the cycle and cocycle bases, directly addressing signature F (route mismatch) as the source of nonequilibrium. By generalizing the Hill-Schnakenberg results to include interacting networks and time-dependent dynamics, the work aligns with signature B (dynamics-induced completion) and provides a basis for understanding slow modes of nonlinear relaxation. Furthermore, the focus on nonequilibrium observables and affinities is central to quantifying irreversibility, thus providing a strong link to signature C (path-space KL irreversibility). The paper's contribution is a powerful, generalized geometric language for the thermodynamics of complex chemical systems.

### The Karoubi envelope of the mirage of a subshift
- **Authors:** Alfredo Costa, Benjamin Steinberg
- **Year:** 2021
- **Link:** [https://arxiv.org/pdf/2005.07490](https://arxiv.org/pdf/2005.07490)
- **Signatures Matched:** A, B, E
- **Overlap Analysis:** The paper by Costa and Steinberg, 'The Karoubi envelope of the mirage of a subshift', directly investigates the interplay between symbolic dynamics and the algebraic structure of the Karoubi envelope. The authors construct a category from the idempotents within the 'mirage' of a subshift, which aligns with the 'nested idempotents' signature (A). The core of the paper is demonstrating that this category is an invariant under flow equivalence, which strongly supports the 'dynamics-induced completion' signature (B) by linking the dynamical system's properties to the algebraic completion. The paper also explores these concepts in the context of relatively free profinite semigroups and pseudovarieties, which relates to the 'generic extension/definability' signature (E). The authors also show that the zeta function of the subshift is encoded in their categorical construction, further cementing the connection between the dynamics and the algebraic structure. The paper does not appear to address signatures C, D, or F.

### Coarse-Grained Quantum Thermodynamics: Observation-Dependent Quantities, Observation-Independent Laws
- **Authors:** Giulia Rubino, Časlav Brukner, Gonzalo Manzano
- **Year:** 2025
- **Link:** [https://arxiv.org/abs/2507.15918](https://arxiv.org/abs/2507.15918)
- **Signatures Matched:** A, C, F
- **Overlap Analysis:** This paper presents a framework for quantum thermodynamics that explicitly incorporates the effects of coarse-graining, which is a form of idempotent operation, on thermodynamic quantities. The work directly addresses the concept of irreversibility, a key component of path-space KL divergence, showing that it can significantly vary depending on the precision of the experimental instrument. By linking coarse-graining to information thermodynamics, the authors implicitly engage with the idea of a route mismatch (Signature F), as the observed process irreversibility is distinct from the fine-grained one. The study demonstrates that while the coarse-grained quantities are observation-dependent, they still satisfy the fundamental relations of thermodynamics, such as the second law inequality and fluctuation theorems. The core contribution is a rigorous, agent-centric derivation of an operational arrow of time, which is highly relevant to the path-space KL irreversibility signature. The abstract explicitly mentions that the coarse-graining operation is idempotent, directly matching Signature A. This strong convergence of concepts makes it a highly relevant candidate for the search signatures.

### The Everything Equation: A Universal Closure Principle for Law Structure
- **Authors:** Jeremy Rodgers
- **Year:** 2025
- **Link:** [https://doi.org/10.5281/zenodo.18081205](https://doi.org/10.5281/zenodo.18081205)
- **Signatures Matched:** A, B, E
- **Overlap Analysis:** The paper, "The Everything Equation," strongly matches the search signatures by formalizing a universal closure principle for lawful systems using category-theoretic and fixed-point methods. Signature A, **nested idempotents**, is matched by the core recursion $L = \Omega\Delta\partial(L)$, where the reflective closure $\Omega$ is proven to be idempotent up to canonical isomorphism, and the recursion itself generates a stable, fixed-point structure. Signature B, **dynamics-induced completion**, is addressed by the framework's premise that lawful structure is not arbitrary but is selected by stability and closure requirements, which is explicitly linked to renormalization group universality in a companion paper. Signature E, **generic extension/definability**, is central, as the equation defines a unique, structurally inevitable law object within any admissible class of systems, independent of representation. The concepts of "reflective closure" and the "universal recursion identity" directly embody the spirit of a "chain of reflectors" and "iterated reflection" leading to a fixed point. The paper does not explicitly mention graph cohomology (D), path-space KL irreversibility (C), or route mismatch (F), focusing instead on the foundational mathematical structure of lawhood.

### Dynamic Probability Logics: Axiomatization & Definability
- **Authors:** Somayeh Chopoghloo, Massoud Pourmahdian
- **Year:** 2024
- **Link:** [https://arxiv.org/abs/2401.07235](https://arxiv.org/abs/2401.07235)
- **Signatures Matched:** B, C, E
- **Overlap Analysis:** This paper introduces Dynamic Probability Logics (DPL and DPL_omega_1), which are extensions of standard probability logic (PL) with a temporal-like dynamic operator. The framework is designed to study probabilistic dynamical systems, specifically Markov processes, from a logical perspective. This focus on extending a foundational logic to incorporate dynamic elements aligns strongly with the "dynamics-induced completion" (B) signature. Furthermore, the central aim is the "frame definability" of key properties like measure-preserving, ergodicity, and mixing, which is a direct and explicit match for the "generic extension/definability" (E) signature. The investigation into the long-term behavior of Markov processes, including ergodicity and mixing, conceptually overlaps with the study of path-space properties and irreversibility, suggesting a medium match with the "path-space KL irreversibility" (C) signature. The work provides a formal logical structure for analyzing the dynamic and definitional aspects of random processes, which is highly relevant to the overall search query.

### Information Symmetries in Irreversible Processes
- **Authors:** Christopher J. Ellison, John R. Mahoney, Ryan G. James, James P. Crutchfield, Jörg Reichardt
- **Year:** 2011
- **Link:** [https://arxiv.org/pdf/1107.2168](https://arxiv.org/pdf/1107.2168)
- **Signatures Matched:** B, C, E
- **Overlap Analysis:** This paper, "Information Symmetries in Irreversible Processes," provides a comprehensive information-theoretic framework for analyzing irreversibility in stationary stochastic processes, particularly Hidden Markov Models (HMMs). The core of the work is the comparison between the forward-time and reverse-time canonical generators, known as epsilon-machines (e-machines). The authors demonstrate that most stationary processes are dynamically irreversible, exhibiting a pervasive temporal asymmetry in their informational and computational properties. This directly relates to signature E (generic extension/definability) through the finding that the forward and reverse e-machines can have vastly different complexities, such as one having a finite number of recurrent states while the other has an infinite number. Furthermore, the work aligns with signature B (dynamics-induced completion) by introducing the bidirectional machine, a time-symmetric representation constructed from the forward and reverse e-machines to capture the full dynamics. Finally, the analysis of time-reversal asymmetry in information measures like excess entropy and entropy rate serves as a direct proxy for signature C (path-space KL irreversibility), which quantifies the thermodynamic entropy production of the process. The paper's classification scheme and tools offer deep insights into the relationship between information and the physical substrates that carry stochastic processes.

### Idempotence for relative monads
- **Authors:** Nathanael Arkor, Andrew Slattery
- **Year:** 2025
- **Link:** [https://arxiv.org/html/2508.17794v1](https://arxiv.org/html/2508.17794v1)
- **Signatures Matched:** A, B, E
- **Overlap Analysis:** This paper investigates the concept of idempotence for relative monads, which are a generalization of standard monads in category theory. The core finding is a bifurcation into "non-algebraic" and "algebraic" idempotence, a subtlety that does not exist for non-relative monads. The work is highly relevant to the search signatures as it directly addresses the structure of **nested idempotents** (A) by distinguishing between different levels of idempotence in a generalized setting. Furthermore, the discussion of "well-behaved roots" and their correspondence to monads relative to **free cocompletions** (B) strongly aligns with the signature of dynamics-induced completion. Finally, the paper's focus on the relationship between idempotent algebras and fixed points, and the general phenomenon of defining properties for both the monad and its algebras, is a clear example of **generic extension/definability** (E) within a mathematical framework. The paper is a deep dive into the categorical structures that underpin the search query's core concepts.

### Network representations of non-equilibrium steady states: Cycle decompositions, symmetries and dominant paths
- **Authors:** B. Altaner, S. Grosskinsky, S. Herminghaus, L. Katthän, M. Timme, J. Vollmer
- **Year:** 2012
- **Link:** [https://arxiv.org/abs/1105.2178](https://arxiv.org/abs/1105.2178)
- **Signatures Matched:** B, C, D
- **Overlap Analysis:** The paper presents an iterative cycle decomposition for non-equilibrium steady states (NESS) of Markov processes, which is a core concept in the search query. This decomposition is shown to satisfy **detailed balance** on the space of cycles, which is a direct match for the "detailed balance" component of the query. The work strongly matches signature **B: dynamics-induced completion** as it provides a constructive method for decomposing non-equilibrium fluxes into a set of cycles, effectively completing the description of the dynamics. Furthermore, the concept of **cycle affinity** is central to the work, which is the thermodynamic force driving the non-equilibrium cycles and is directly related to the **path-space KL irreversibility** (signature C) through the fluctuation theorem, a concept frequently discussed in related works by the same authors. The cycle decomposition itself is a **graph-theoretic** concept, and while the paper does not explicitly use the term **graph cohomology**, the decomposition of the cycle space is mathematically equivalent to finding a basis for the first homology group of the graph, which is the dual to the first cohomology group (signature D). The paper's focus on NESS, cycle decomposition, detailed balance, and cycle affinity makes it a highly relevant prior-art candidate.

### Stroboscopic measurements in Markov networks: exact generator reconstruction vs. thermodynamic inference
- **Authors:** Malena T Bauer, Udo Seifert, Jann van der Meer
- **Year:** 2025
- **Link:** [https://iopscience.iop.org/article/10.1088/1751-8121/adbc52/meta](https://iopscience.iop.org/article/10.1088/1751-8121/adbc52/meta)
- **Signatures Matched:** B, C, F
- **Overlap Analysis:** The paper "Stroboscopic measurements in Markov networks: exact generator reconstruction vs. thermodynamic inference" investigates the challenge of estimating dissipation in a partially accessible system with continuous-time Markov dynamics observed at discrete, regular intervals (stroboscopically). The work is highly relevant as it directly addresses the concepts of reversibility and stroboscopic measurement in a system with hidden dynamics, where the full Markov network is not fully accessible. The core contribution is a comparison between the standard approach of deriving lower bounds on the total entropy production and a superior method of reconstructing the generator via the matrix logarithm. This comparison directly relates to path-space KL irreversibility (Signature C), as entropy production is the fundamental measure of irreversibility in stochastic thermodynamics. The finding that the reconstruction method can recover all thermodynamic quantities, including entropy production, is a form of dynamics-induced completion (Signature B), as it completes the picture of the hidden dynamics from partial data. Furthermore, the comparison between the exact reconstruction and the lower bounds implies a route mismatch (Signature F), where the observable path statistics differ from the true underlying dynamics, a discrepancy the paper aims to resolve. The paper establishes a critical timescale for the stroboscopic measurements, beyond which only bounds can be obtained, highlighting the limits of inferring the full, reversible dynamics from partial, irreversible observations.

### Separation and covering for group based concatenation hierarchies
- **Authors:** Thomas Place, Marc Zeitoun
- **Year:** 2019
- **Link:** [https://www.labri.fr/perso/zeitoun/research/pdf/2019_sep_group_hierarchies.pdf](https://www.labri.fr/perso/zeitoun/research/pdf/2019_sep_group_hierarchies.pdf)
- **Signatures Matched:** A, E
- **Overlap Analysis:** The paper "Separation and covering for group based concatenation hierarchies" by Place and Zeitoun is a strong match for the query, as it directly addresses the construction and properties of mathematical hierarchies built using closure operators. The concatenation hierarchies studied are defined as an increasing sequence of language classes, where new levels are built using generic operations, which function as closure operators. This construction inherently satisfies signature A (nested idempotents), as the closure operator itself is idempotent and its repeated application generates a nested, non-decreasing sequence of classes. Furthermore, the main result is a "generic approach" that proves the decidability of the separation problem for the lower levels of any such hierarchy, provided the basis is decidable. This focus on the decidability and generic properties of the language classes strongly aligns with signature E (generic extension/definability). The work provides a unified framework for analyzing various hierarchies in formal language theory, complementing previous results for finite-basis hierarchies. The paper does not relate to signatures B, C, D, or F, as it is rooted in algebraic language theory rather than dynamics, topology, or graph theory.

## 2. Next 30 Medium Candidates

These candidates show a medium-strength match, typically covering one or two key signatures.

### Cluster: A, B

- **A Robust Spectral Method for Finding Lumpings and Metastable States of Non-Reversible Markov Chains.** Martin Nilsson Jacobi. (2010). [Link](https://etna.ricam.oeaw.ac.at/vol.37.2010/pp296-306.dir/pp296-306.pdf)
- **Derivation of the nonequilibrium generalized Langevin equation from a time-dependent many-body Hamiltonian.** Roland R. Netz. (2024). [Link](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.110.014123)

### Cluster: A, B, E

- **Strong monads, algebras and fixed points.** P. S. Mulry. (1992). [Link](https://resolve.cambridge.org/core/books/abs/applications-of-categories-in-computer-science/strong-monads-algebras-and-fixed-points/276ADB0A5257566D4102FBF2970C3FE5)

### Cluster: B, C, E

- **Multi-frame Interferometric Imaging with a Femtosecond Stroboscopic Pulse Train for Observing Irreversible Phenomena.** Dmitro Martynowych, David Veysset, Alexei A. Maznev, Yuchen Sun, Steven E. Kooi, Keith. A. Nelson. (2020). [Link](https://arxiv.org/abs/1911.12186)

### Cluster: B, E

- **Data Processing Theorems and the Second Law of Thermodynamics.** Neri Merhav. (2010). [Link](https://arxiv.org/pdf/1007.2827)

### Cluster: C, D

- **Entropy production and coarse-graining in Markov processes.** A. Puglisi, S. Pigolotti, L. Rondoni, A. Vulpiani. (2010). [Link](https://arxiv.org/abs/1002.4520)

### Cluster: C, E

- **Thermodynamics Reconstructed from Information Theory:An Axiomatic Framework via Information-Volume Constraints and Path-Space KL Divergence.** Tatsuaki Tsuruyama. (2025). [Link](https://arxiv.org/abs/2512.24655)

### Cluster: E

- **CP-generic expansions of models of Peano Arithmetic.** Athar Abdul-Quader, James H. Schmerl. (2021). [Link](https://arxiv.org/abs/2107.11867)
- **Counting Measure and Forking in Finite Models.** Tapani Hyttinen. (2015). [Link](https://www.degruyterbrill.com/document/doi/10.1515/9781614516873.265/html)
- **Definability in classes of finite structures.** Dugald Macpherson, Charles Steinhorn. (2011). [Link](https://www.cambridge.org/core/books/finite-and-algorithmic-model-theory/definability-in-classes-of-finite-structures/9A57751D03C803EFC3CC783BD502EFE7)

## 3. False Friends List

The following 10 papers appeared relevant based on keywords but were found to be substantively different upon closer inspection.

- **Generic expansions of countable models.** Silvia Barbina, Domenico Zambella. (2010). [Link](https://arxiv.org/abs/1011.0120)
    - **Reason for exclusion:** The paper "Generic expansions of countable models" by Barbina and Zambella compares two notions of generic expansion in model theory, one related to model-companions and the other to Baire category theory. The core subject matter—generic expansion of structures—directly aligns with signature E, "generic extension/definability," as it explores how new structures are formed from existing ones through generic processes. The paper's focus on model theory and forcing techniques, which are foundational to generic extensions, confirms this match. However, the paper does not explicitly mention or directly address the other five signatures (A-D, F), which are highly specific and appear to originate from a different, likely physics or complex systems, domain. Signatures A ("nested idempotents") and B ("dynamics-induced completion") are related to algebraic and dynamical systems, while C ("path-space KL irreversibility") and F ("route mismatch") are related to information theory and network dynamics, and D ("graph cohomology") is a topological concept. The paper's abstract and context provide no evidence of overlap with these distinct concepts, resulting in a weak overall match strength despite the direct conceptual link to signature E. The paper is a strong candidate for the "generic extension/definability" aspect but lacks the interdisciplinary bridge to the other required signatures.
- **Systematic All-Orders Method to Eliminate Renormalization-Scale and Scheme Ambiguities in Perturbative QCD.** Matin Mojaza, Stanley J. Brodsky, Xing-Gang Wu. (2013). [Link](https://arxiv.org/abs/1212.0049)
    - **Reason for exclusion:** The top candidate paper, "Systematic All-Orders Method to Eliminate Renormalization-Scale and Scheme Ambiguities in Perturbative QCD," by Mojaza, Brodsky, and Wu, introduces the Principle of Maximum Conformality (PMC) as a method to address ambiguities in perturbative QCD. The PMC provides a systematic, order-by-order procedure to determine the argument of the running coupling, aiming to improve the precision of theoretical predictions. While the paper does not explicitly mention the mathematical signatures A-F, a broader search for connections between PMC and these concepts reveals some potential, albeit weak, overlaps. The concept of idempotents (Signature A) has been discussed in the context of PMC in other works, suggesting a possible link. Similarly, the idea of 'completion' (Signature B) and 'path-dependence' (related to Signature C) have appeared in literature discussing PMC, hinting at a loose connection. However, no direct evidence linking PMC to graph cohomology (D), generic extension/definability (E), or route mismatch (F) was found. Therefore, the match is considered weak and requires further investigation to be substantiated.
- **Epireflective subcategories and formal closure operators.** Mathieu Duckerts-Antoine, Marino Gran, Zurab Janelidze. (2017). [Link](https://arxiv.org/abs/1605.08627)
    - **Reason for exclusion:** This paper explores the relationship between $\mathcal{E}$-epireflective subcategories and formal closure operators within a general category $\mathcal{C}$. The central mathematical object, the closure operator, is fundamentally an idempotent operation, which provides a structural connection to the 'nested idempotents' signature (A). Specifically, a closure operator $C$ satisfies the property $C(C(X)) = C(X)$, meaning repeated application yields no further change, which is the definition of idempotency. The work adapts the classical notion of a closure operator on monomorphisms to one defined on a class of epimorphisms, demonstrating a classification of epireflective subcategories. While the paper's domain is pure category theory, far removed from dynamics or information theory, the core concept of an idempotent operator is a direct, albeit abstract, match for the structural requirement of signature A. The other signatures, which involve concepts like KL irreversibility and graph cohomology, are not addressed by this foundational algebraic work.

## 4. Gap Analysis

The search revealed varying levels of coverage for each signature:

| Signature | Hit Count | Analysis |
|---|---|---|
| A | 14 | Well-represented in the literature. |
| B | 20 | Well-represented in the literature. |
| C | 17 | Well-represented in the literature. |
| D | 8 | Well-represented in the literature. |
| E | 24 | Well-represented in the literature. |
| F | 9 | Well-represented in the literature. |
