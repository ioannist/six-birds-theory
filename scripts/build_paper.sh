#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
MANUSCRIPT_DIR="$REPO_DIR/manuscript"
cd "$MANUSCRIPT_DIR"

if command -v latexmk >/dev/null 2>&1; then
  echo "Using latexmk"
  latexmk -pdf -interaction=nonstopmode paper.tex
  exit 0
fi

if command -v pdflatex >/dev/null 2>&1; then
  echo "Using pdflatex"
  pdflatex -interaction=nonstopmode paper.tex
  if [ -f paper.aux ] && grep -q "\\citation" paper.aux; then
    if command -v bibtex >/dev/null 2>&1; then
      bibtex paper
    else
      echo "bibtex not found; skipping bibliography"
    fi
  fi
  pdflatex -interaction=nonstopmode paper.tex
  echo "Note: LaTeX references resolve on the second compile; if you see '??', run the build twice (or use latexmk)."
  exit 0
fi

if command -v tectonic >/dev/null 2>&1; then
  echo "Using tectonic"
  tectonic paper.tex
  exit 0
fi

echo "No LaTeX toolchain found (latexmk/pdflatex/tectonic). Skeleton created; install one of these to compile."
exit 0
