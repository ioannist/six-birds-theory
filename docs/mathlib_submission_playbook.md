# Mathlib submission playbook (closure-ladder-theory)

This playbook summarizes mathlib workflow, style, naming, documentation, and linting expectations,
and records a first-pass scan of the candidate files in this repo.

## Workflow checklist (mathlib PRs)

- Discuss fit on Zulip (#mathlib) early, especially if scope is uncertain.
- Keep PRs small and self-contained; smaller PRs are strongly preferred.
- Actively seek reviewers; they do not have to be maintainers.
- Follow mathlib commit/PR conventions; add Moves/Deletions blocks when renaming/removing decls.
- Use queue labels correctly (awaiting-author, WIP, etc.) so the PR appears on the queue.
- Avoid purely stylistic PRs unless approved; discuss style changes on Zulip first.

## Formatting checklist (files)

- Header comment with copyright, license, and Authors line.
- Imports immediately after header (one per line, no blank line between header and imports).
- Module docstring right after imports, using `/-! ... -/` with a title and summary.
- Line length <= 100 characters.
- Top-level commands (def/theorem/lemma/instance/namespace/section/open) start in column 0.
- Indentation: theorem statements line-break with 4-space indent; proofs 2-space indent.

## Naming checklist

- File names use UpperCamelCase (rare exceptions only by agreement).
- Propositions/theorems: snake_case.
- Types/structures/classes: UpperCamelCase.
- Functions named like their return type; other terms in lowerCamelCase.
- Declaration names use American spelling (e.g., “localization”, “fiber”).

## Documentation checklist

- Every definition and major theorem has a docstring (`/-- ... -/`).
- Module docstring sections (in order):
  - Main definitions (optional)
  - Main statements (optional)
  - Notation (omit only if none)
  - Implementation notes
  - References (to docs/references.bib)
  - Tags
- Docstrings are not indented, and complete sentences end with a period.

## Linter gotchas to avoid (style + text-based)

- `lambdaSyntax`: use `fun` not `lambda`.
- `dollarSyntax`: use `<|` not `$`.
- `longLine`: >100 characters.
- `longFile`: >1500 lines.
- `openClassical`: only scoped `open Classical in`.
- `missingEnd`: unclosed `section`/`namespace`.
- `setOption`: disallowed `set_option` (esp. `pp`, `trace`, `maxHeartbeats` not scoped).
- `cdot`: use the actual centered-dot character, not a plain `.`.
- `show`: use `change` when it changes the goal.
- Text-based: trailing whitespace, Windows line endings, non-UpperCamelCase module names,
  forbidden filename characters, blocklisted unicode.

## Local linting

- Preferred: `lake exe lint-style` (or `lake exe mathlib/lint-style` if needed).
- Run `lake ...` commands from `formal/` (the Lake project lives there).

## Repo gap scan (upstream-candidate files)

- formal/ClosureLadder/Basic.lean
  - Header comment: missing
  - Module docstring: missing
  - Long lines (>100): none detected
  - Style-linter triggers: none detected (no `lambda`, no `$`, no `open Classical`)
- formal/ClosureLadder/Packaging.lean
  - Header comment: missing
  - Module docstring: missing
  - Long lines (>100): none detected
  - Style-linter triggers: none detected (no `lambda`, no `$`, no `open Classical`)
- formal/ClosureLadder/IdempotentEndo.lean
  - Header comment: missing
  - Module docstring: missing
  - Long lines (>100): none detected
  - Style-linter triggers: none detected (no `lambda`, no `$`, no `open Classical`)
- formal/ClosureLadder/MetaPackaging.lean
  - Header comment: missing
  - Module docstring: present (but should follow a header + imports)
  - Long lines (>100): none detected
  - Style-linter triggers: none detected (no `lambda`, no `$`, no `open Classical`)
