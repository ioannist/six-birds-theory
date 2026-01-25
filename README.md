# Six Birds: Foundations of Emergence Calculus

This repository is the full research workspace for the math-only preprint
**“Six Birds: Foundations of Emergence Calculus.”** It includes the manuscript,
formal scaffolding, reproducibility checks, and supporting registries/audits.

DOI: [10.5281/zenodo.18365949](https://doi.org/10.5281/zenodo.18365949)

## Quick start

Build the paper PDF (requires `latexmk`, `pdflatex`, or `tectonic`):

```bash
bash scripts/build_paper.sh
```

Run the lightweight consistency checks:

```bash
python3 scripts/check_tex_refs.py manuscript/paper.tex
python3 scripts/check_paper_contract.py
python3 scripts/check_deps_dag.py
python3 scripts/check_kb_pointers.py
```

Build the Lean scaffold:

```bash
bash scripts/check_lean.sh
```

Regenerate knowledge-base indices:

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
