# Six Birds: Foundations of Emergence Calculus

> **Six Birds: Foundations of Emergence Calculus**
>
> Tsiokos, Ioannis
>
> Zenodo: https://zenodo.org/records/18365949
>
> DOI: [10.5281/zenodo.18365949](https://doi.org/10.5281/zenodo.18365949)

This repository is the full research workspace for the math-only preprint. It includes the manuscript, formal scaffolding, reproducibility checks, and supporting registries/audits.

## What this repository provides

A math-only framework—Six Birds Theory—for reasoning about hierarchical description, emergence, and open-ended theory growth in multiscale systems. The central construct is a **theory package** with three components:

- **Lens / definability structure** — what distinctions are expressible at a given layer
- **Completion (packaging) rule** — modeled as an idempotent (or approximately idempotent) endomap capturing which descriptions stabilize and become objects
- **Audit / certificate** — quantities that remain monotone (or provably well-behaved) under observation and coarse-graining

Within this framework, the project formalizes:

- **Object formation as fixed points of completion**: stable objects arise as the fixed points of the completion map
- **Saturation under repeated closure**: iterating a fixed completion rule does not yield indefinite novelty; it tends to stabilize and saturate
- **Open-endedness via strict extension**: genuine open-ended growth requires strict theory extension—changes in definability/closure—rather than repeated application of a single closure rule

The project also introduces:

- An **induced empirical completion operator** built from a Markov kernel, a lens, and a timescale
- A computable **total-variation idempotence defect** that quantifies packaging stability
- **Arrow-of-time** defined as path-space KL divergence with a data processing inequality proof
- A **finite forcing–style counting lemma** for anti-saturation and novelty
- **Six primitives (P1–P6)** as a minimal vocabulary of closure-changing moves

## Scope and limitations

This is a **math-only foundations paper**. It provides:

- A reusable emergence calculus that cleanly separates stability (idempotence/fixed points), novelty (non-definability/extension), and directionality (audits monotone under lenses)—including explicit non-implications
- A lightweight reproducibility backbone: a small mechanized proof core (Lean) for closure/idempotent structures and a deterministic Python harness for sanity checks
- Appendix-level theorem templates for capacity control and bounded interface complexity

It does **not** provide domain instantiations—this is the foundational math layer only.

## Build

Build the paper PDF (requires `latexmk`, `pdflatex`, or `tectonic`):

```bash
bash scripts/build_paper.sh
```

Build the Lean scaffold:

```bash
bash scripts/check_lean.sh
```

## Test

Run the lightweight consistency checks:

```bash
python3 scripts/check_tex_refs.py manuscript/paper.tex
python3 scripts/check_paper_contract.py
python3 scripts/check_deps_dag.py
python3 scripts/check_kb_pointers.py
```

## Regenerate indices

```bash
python3 scripts/extract_kb_index.py
```

## Repository layout

- `manuscript/paper.tex` — main LaTeX source.
- `manuscript/` — build helpers and manuscript notes.
- `docs/spec/` — scope/claim inventory and spec references.
- `docs/registries/` — generated registries and indices.
- `docs/audits/` — audit notes and edge cases.
- `formal/` — Lean4 + mathlib scaffold (minimal formal map).
- `scripts/` — build/check tooling for reproducibility.
- `reports/` — check logs and review reports.

## Notes

- The LaTeX toolchain is optional unless you want the PDF.
- The checks above are designed to keep references, scopes, and dependency
  claims consistent with the manuscript.
