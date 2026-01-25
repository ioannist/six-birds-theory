# R56 Overclaim Audit + Related Work Coverage

## Overclaim hardening edits

1. DPI non-creation guardrail (sec:aot, after DPI proof):
   - Snippet: "monotonicity rules out false positives... cannot create it"
   - Change: added explicit non-creation sentence immediately after DPI proof.

2. P3 guardrail (sec:primitives, P3 definition):
   - Snippet: "P3 (route mismatch/holonomy) is a protocol-geometry diagnostic..."
   - Change: added explicit sentence that P3 alone does not certify directionality; audits required.

3. Refinement caution (sec:empirical-closure, before T-IC-01):
   - Snippet: "Refinement is not monotone-good in general..."
   - Change: inserted explicit "can help or hurt" sentence near first refinement mention.

4. Self-organization wording:
   - Snippet: "self-organization"
   - Change: no occurrences found; no edits needed.

## Related Work coverage checklist

- Closure operators / reflections / thin-category reflection: covered in Related Work paragraph with \cite{DaveyPriestley2002,MacLane1998,Borceux1994}.
- Markov coarse-graining / lumpability: covered with \cite{KemenySnell1960,Norris1997,KhudaBukhsh2018,NilssonJacobi2010}.
- Path-space KL / DPI / time reversal: covered with \cite{CoverThomas2006,CsiszarKorner2011,Kelly1979,Seifert2012,Merhav2010,Puglisi2010,DeguntherVanderMeerSeifert2023,BauerSeifertVanderMeer2025}.
- Cycle space / affinities / network thermodynamics: covered with \cite{Polettini2012,AltanerPolettiniEsposito2012,DalCengioLecomtePolettini2023}.
- Finite definability / forcing analogy: covered with \cite{Libkin2004,Cohen1963,Kunen2011,MacphersonSteinhorn2011,Hyttinen2015}.
