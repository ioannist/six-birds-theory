# R3 Theorem Smell Test

Total items: 73

## Inventory

|Label|Type|Section|Lines|Restatement|Hypotheses stated|Hypotheses used|Drop-hypothesis counterexample|Classification|Smell flag|
|---|---|---|---|---|---|---|---|---|---|
|def:tk-theory-package|Definition|sec:tk-theory-package|L238-L257|Finite theory package|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:closure-operator|Definition|sec:closure|L313-L320|Closure operator|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:closed-points|Definition|sec:closure|L325-L331|Closed points / objects|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:closed-antitone|Lemma|sec:closure|L337-L340|Closed points are antitone in closure strength|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:closure-iterate-stabilizes|Lemma|sec:closure|L351-L357|One-step stabilization under iteration|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|cor:closure-saturates|Corollary|sec:closure|L364-L368|Closure saturates|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:strictly-stronger|Definition|sec:closure|L379-L382|Strictly stronger closure|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:closure-ladder|Definition|sec:closure|L384-L391|Closure ladder|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:idempotent-endo|L423-L426|Idempotent endomap|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:idempotent-endo|L428-L434|Fixed points|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Lemma|sec:idempotent-endo|L436-L443|Idempotents split|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:D-IC-01|Definition|sec:empirical-closure|L486-L506|Coarse map and canonical lift; \textbf{D-IC-01}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:D-IC-02|Definition|sec:empirical-closure|L520-L539|TV idempotence defect; \textbf{D-IC-02}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:empirical-closure|L541-L550|Prototype stability at scale $\tau$|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|thm:T-IC-02|Theorem|sec:empirical-closure|L552-L568|Approximate idempotence from retention|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Hard|OK|
|thm:T-IC-01|Theorem|sec:empirical-closure|L608-L627|Refinement can help or hurt|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Hard|OK|
|def:edge-one-form|Definition|sec:acc|L682-L690|Edge log-ratio 1-form|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:cycle-integral|Definition|sec:acc|L706-L713|Cycle integral / affinity along a cycle|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:exact-one-form|Definition|sec:acc|L715-L723|Exact 1-forms|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:exact-zero-cycles|Lemma|sec:acc|L725-L730|Exact forms have zero cycle integrals|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|thm:cycle-criterion-exact|Theorem|sec:acc|L739-L749|Cycle criterion for exactness|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|cor:null-regime|Corollary|sec:acc|L765-L775|Null regime as ``no-drive'' / detailed-balance-like|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Definition|sec:aot|L804-L817|Forward path law and reversal (D-AOT-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:aot|L826-L830|Steady-state entropy production (D-AOT-EP-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|thm:dpi_path|Theorem|sec:aot|L842-L850|Data processing for path reversal asymmetry (T-AOT-01)|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Corollary|sec:aot|L861-L866|No false positives|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Definition|sec:aot|L879-L888|Autonomous $m$-phase protocol|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|thm:protocol_trap|Theorem|sec:aot|L890-L901|Protocol trap / hidden-drive principle (T-AOT-02)|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Corollary|sec:aot|L917-L922|``P3 needs P6\_drive'' under autonomy (C-ACC-01)|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Definition|sec:forcing|L942-L949|Predicates and definability|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:count-definable|Lemma|sec:forcing|L970-L977|Counting definable predicates|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|thm:finite-forcing|Theorem|sec:forcing|L989-L1009|Finite forcing lemma / physical forcing lemma|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|cor:strict-language-extension|Corollary|sec:forcing|L1017-L1022|Generic extension is strict|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:meta-proc|Definition|sec:meta-unavoidable|L1039-L1042|Process soup (D-META-PROC-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:meta-lens|Definition|sec:meta-unavoidable|L1044-L1048|Interface lens (D-META-LENS-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:meta-ref|Definition|sec:meta-unavoidable|L1050-L1056|Refinement family (D-META-REF-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:meta-bnd|Definition|sec:meta-unavoidable|L1058-L1061|Bounded interface (D-META-BND-01)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|thm:meta-prim|Theorem|sec:meta-unavoidable|L1063-L1084|Self-generated primitives|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Hard|OK|
|NO_LABEL|Definition|sec:primitives|L1112-L1116|P1: operator rewrite|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:primitives|L1118-L1122|P2: gating / constraints|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:primitives|L1124-L1129|P3: autonomous protocol holonomy|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:primitives|L1131-L1135|P4: sectors / invariants|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:primitives|L1137-L1141|P5: packaging|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Definition|sec:primitives|L1143-L1153|P6: accounting / audit|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|NO_LABEL|Theorem|sec:six-birds-loop|L1202-L1214|P2 gating shrinks cycle space|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|NO_LABEL|Theorem|sec:six-birds-loop|L1221-L1225|P1 can change cycle rank and spectral gap (T-P1-01)|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:work-quantum|Lemma|app:zeno|L1602-L1609|WORK from storage growth|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:latency-lb|Lemma|app:zeno|L1636-L1641|Latency lower bound from WORK+ICAP+FEAS|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|thm:no-zeno|Theorem|app:zeno|L1656-L1663|No-Zeno from divergent reciprocal capacity|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Hard|OK|
|lem:tk-route-capacity|Lemma|sec:tk-route-capacity|L1816-L1834|Route mismatch controls gain growth|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:tk-bridge-ports|Definition|sec:tk-bridge-toolkit|L1869-L1886|Ports, causal bridge, and accounting|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:tk-passive-storage|Definition|sec:tk-bridge-toolkit|L1888-L1897|Passivity with storage|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:tk-icap|Definition|sec:tk-bridge-toolkit|L1899-L1909|Integrated capacity inequality (ICAP)|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:tk-causal-compose|Lemma|sec:tk-bridge-toolkit|L1916-L1920|Causality is closed under composition|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:tk-parallel-add|Lemma|sec:tk-bridge-toolkit|L1927-L1937|Parallel sum: passivity and ICAP constants add|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|thm:ect-summary|Theorem|sec:ect-summary|L1973-L2002|ECT summary: linear ICAP capacity and DIV from three slots|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Hard|OK|
|def:ect-atom|Definition|sec:ect-summary|L2023-L2033|Atomic/sector decompositions of a packaged bridge {\normalfont\textsf{(ID: D-ECT-ATOM-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:ect-atom-ss|Definition|sec:ect-summary|L2036-L2048|Dissipative atom representation {\normalfont\textsf{(ID: D-ECT-ATOM-SS-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:ect-bal|Definition|sec:ect-summary|L2050-L2058|Balanced coupling {\normalfont\textsf{(ID: D-ECT-BAL-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:ect-cap|Definition|sec:ect-summary|L2060-L2073|ICAP capacity functional {\normalfont\textsf{(ID: D-ECT-CAP-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:ect-bal-kmass|Lemma|sec:ect-summary|L2075-L2082|Balanced decay implies a uniform kernel-mass bound {\normalfont\textsf{(ID: L-ECT-BAL-KMASS-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:ect-fmem|Lemma|sec:ect-summary|L2099-L2112|Finite kernel-mass convolution bridges satisfy ICAP for truncated inputs {\normalfont\textsf{(ID: L-ECT-FMEM-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|cor:ect-bal-icap|Corollary|sec:ect-summary|L2130-L2138|Balanced atoms have uniform ICAP|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:ect-mech|Lemma|sec:ect-summary|L2155-L2172|Mechanical ECT: sector ICAP + mode count $\Rightarrow$ linear capacity {\normalfont\textsf{(ID: L-ECT-MECH-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:ect-gate|Definition|sec:ect-gating|L2207-L2223|Feasibility gate and induced coercive norm {\normalfont\textsf{(ID: D-ECT-GATE-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:ect-coer-feas|Lemma|sec:ect-gating|L2225-L2235|Coercivity on the feasible set {\normalfont\textsf{(ID: L-ECT-COER-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|lem:ect-shrink|Lemma|sec:ect-gating|L2248-L2261|Feasibility shrinkage $\Rightarrow$ depth-scaled coercivity {\normalfont\textsf{(ID: L-ECT-SHRINK-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:ect-sectorization|Definition|sec:ect-sectorization|L2275-L2285|Sectorization of the port space {\normalfont\textsf{(ID: D-ECT-SECT-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|def:ect-p5min|Definition|sec:ect-sectorization|L2287-L2297|Sector-respecting minimal decompositions (P5-min) {\normalfont\textsf{(ID: D-ECT-P5MIN-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:ect-mode-ub|Lemma|sec:ect-sectorization|L2299-L2307|Sectorization bounds the minimal mode count {\normalfont\textsf{(ID: L-ECT-MODE-UB-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|def:ect-p4-idx|Definition|sec:ect-sectorization|L2317-L2325|Quantized index hypothesis {\normalfont\textsf{(ID: D-ECT-P4IDX-01)}}|None explicit|Definition only|N/A (definition)|Toolkit identity|OK|
|lem:ect-qsize|Lemma|sec:ect-sectorization|L2327-L2332|Quantized index implies linear sector count {\normalfont\textsf{(ID: L-ECT-QSIZE-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|
|cor:ect-hl1|Corollary|sec:ect-sectorization|L2337-L2345|Linear mode bound from P4 index {\normalfont\textsf{(ID: C-ECT-HL1-01)}}|None explicit|None explicit; proof sketch uses stated local conditions|No drop-hypothesis issue (algebraic/metric identity).|Elementary|OK|

## High-risk zones

- Path-KL / DPI: checked for support/KL=∞ conventions and no hidden stationarity; OK.
- ACC exactness: checked exactness/potential statements are componentwise with bidirected support; OK.
- Protocol trap / P3: route mismatch framed as non-directional; P6_drive required for directionality; OK.
- Forcing/definability rarity: randomness model explicit (iid Bernoulli(1/2)); OK.
- ECT/ATOM balanced atoms: decay rate λ>0 and uniform constants stated; OK.
