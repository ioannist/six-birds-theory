# Assumption tag hygiene audit (Round 3)

## Occurrences of \textbf{A\_...} in manuscript/paper.tex (grouped by label)

- sec:big-picture (L117): A_AUT, A_REV, A_ACC — OK (cross-reference context).
- def:tk-theory-package (L221): A_FIN — OK (finite theory package definition).
- NO_LABEL / assumption bundles (L265–L275): A_FIN, A_AUT, A_REV, A_ACC, A_NULL, A_STAT, A_LENS — OK (bundle definitions).
- sec:empirical-closure (L439–L442): A_FIN, A_LENS — OK (finite state space + lens setup).
- thm:T-IC-02 (L512): A_FIN, A_LENS — OK (finite Markov setting + lens).
- thm:T-IC-01 (L563): A_FIN, A_LENS — OK (finite Markov setting + lens).
- sec:acc (L614–L623, L630): A_AUT, A_REV, A_ACC, A_FIN — OK (ACC regime on finite graphs).
- def:edge-one-form (L635–L646): A_FIN, A_REV — OK (edge log-ratios need bidirected finite support).
- lem:exact-zero-cycles (L675): A_FIN, A_REV — OK.
- thm:cycle-criterion-exact (L688): A_FIN, A_REV — OK.
- cor:null-regime (L714, L735, L737): A_FIN, A_REV, A_NULL, A_ACC — OK (null regime + ACC context).
- sec:aot (L748, L772, L779): A_FIN, A_STAT, A_LENS — OK (finite Markov + lens + stationarity where stated).
- thm:dpi_path (L784, L800): A_FIN, A_LENS — OK (finite Markov + lens).
- thm:protocol_trap (L824, L832, L848): A_FIN, A_AUT, A_REV, A_ACC, A_NULL — OK (autonomous lifted model context).
- sec:forcing (L865–L866): A_FIN, A_LENS — OK (finite definability setting).
- lem:count-definable (L892): A_FIN, A_LENS — OK.
- thm:finite-forcing (L911): A_FIN, A_LENS — OK.
- cor:strict-language-extension (L939): A_FIN, A_LENS — OK.
- sec:primitives (L1023, L1036, L1043, L1066, L1083): A_AUT, A_REV, A_ACC, A_FIN — OK (ACC/REV assumptions scoped).
- subsec:ex:3cycle (L1119): A_FIN, A_REV — OK.
- sec:discussion-claims (L1200): A_AUT — OK (autonomy guardrail).

## Fix summary

- Updated the A_FIN bundle definition to match finite combinatorial/matrix contexts only.
- Removed A_FIN tags from analytic ICAP/No-Zeno statements: lem:work-quantum, lem:latency-lb, thm:no-zeno.
- Removed A_FIN tags from abstract operator/toolkit statements: lem:tk-route-capacity, def:tk-bridge-ports, lem:tk-causal-compose, lem:tk-parallel-add.
- Updated the assumption audit table in manuscript/consistency_checklist.md to reflect these removals.
