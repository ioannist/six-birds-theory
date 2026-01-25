# Assumptions Registry

## AUT
- docs/knowledge-base/exercises_2.md:L367
- docs/knowledge-base/exercises_3.md:L804

## REV
- docs/knowledge-base/exercises_2.md:L377
- docs/knowledge-base/exercises_3.md:L805
- Note: REV-support is the minimal bidirectional support condition; full reversibility/detailed balance is stronger when used.

## ACC
- docs/knowledge-base/exercises_2.md:L382
- docs/knowledge-base/exercises_3.md:L808
- Note: treat ACC as a graph 1-form on bidirected support; DTMC/CTMC change the interpretation of k (probabilities vs rates), not the cohomology statement.

## STAT (Stationary init)
- docs/knowledge-base/exercises_4.md:L393
- docs/knowledge-base/exercises_4.md:L1724

## ERG (Ergodic / unique stationary)
- paper-side technical condition: irreducible (and aperiodic if DTMC) so stationary distribution is unique and convergence holds
- docs/knowledge-base/exercises_3.md:L2399

## REV-support (bidirectional support)
- docs/knowledge-base/exercises_3.md:L805
- docs/knowledge-base/exercises_4.md:L1724
- Note: ensures EP/path-KL finiteness; without it, reversed paths can have zero probability and KL can be infinite.

## Arrow-of-time definition = path KL
- docs/knowledge-base/exercises_3.md:L580
- docs/knowledge-base/exercises_4.md:L18

## Coarse-graining cannot create irreversibility (data processing)
- docs/knowledge-base/exercises_3.md:L896
- docs/knowledge-base/exercises_4.md:L183
