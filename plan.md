

review the response and the attached repo, if you need to fix anything, fold the request into the next ticket; now, produce a ticket for:

### Ticket 3 — Extract mathlib-ready versions into isolated Lean files (in your repo)

**Goal:** Create “clean-room” files that import only mathlib and define/prove only the upstream candidates (no project-specific scaffolding, no wrapper abbreviations).

**Pass criteria**

* New folder (e.g. `formal/Upstream/` or `MathlibPrep/`) with one or more `.lean` files, each:

  * has a mathlib-style header + module docstring
  * imports only what is needed
  * contains only candidate definitions/lemmas
* `lake build` succeeds for those files.

**Response schema**

* “New files:” list paths
* “Declarations implemented in each file:” list names
* “Minimal imports justification (1–2 lines per file):”
* “Commands run:” …

---

review the response and the attached repo, if you need to fix anything, fold the request into the next ticket; now, produce a ticket for:

### Ticket 4 — Align names, docstrings, and linter expectations

**Goal:** Rename/restructure to match mathlib naming conventions and documentation requirements; add docstrings to major results; remove avoidable non-mathlib conventions (e.g. `λ` if style linter expects `fun`).

Mathlib naming conventions are strict about casing and spelling. ([leanprover-community.github.io][2])
Documentation expectations (file/module docstring sections, docstrings on major defs/theorems) are also explicit. ([leanprover-community.github.io][3])

**Pass criteria**

* Candidate files pass style checks (either mathlib’s style linter, or best-effort local equivalents).
* All “major” defs/lemmas in the candidate set have `/-- … -/` docstrings.

**Response schema**

* “Renames performed:” old → new (bullets)
* “Docstrings added for:” list decls
* “Style/lint results summary:” …

---

review the response and the attached repo, if you need to fix anything, fold the request into the next ticket; now, produce a ticket for:

### Ticket 5 — Produce patch files against mathlib (using `.lake/packages/mathlib`)

**Goal:** Prepare actual `git format-patch` outputs that can be applied to mathlib, split into small PR-sized chunks.

**Pass criteria**

* Patch files exist in-repo (e.g. `patches/mathlib/0001-…patch`, `0002-…patch`)
* Each patch corresponds to a small cohesive change (ideally: 1–3 lemmas or one instance + supporting lemmas)
* Each patch compiles when applied to the mathlib checkout used to generate it

**Response schema**

* “Patches produced:” list patch filenames + 1-line description each
* “Mathlib base revision used:” (commit hash from `.lake/packages/mathlib`)
* “Build commands run in mathlib checkout:” …

---

review the response and the attached repo, if you need to fix anything, fold the request into the next ticket; now, produce a ticket for:

### Ticket 6 — Draft PR text and Zulip pitch (no posting, just prepared text)

**Goal:** Provide ready-to-use PR descriptions and a Zulip message to ask maintainers about placement/naming, especially if adding new instances (like `LE (ClosureOperator α)`).

Mathlib encourages discussing bigger/structural additions on Zulip early. ([leanprover-community.github.io][4])

**Pass criteria**

* A markdown file with:

  * proposed PR titles
  * PR descriptions
  * a short Zulip message draft per PR

**Response schema**

* “Draft text file:” `<path>`
* “PR list:” titles + what they add
* “Any questions to ask maintainers:” bullets

---
