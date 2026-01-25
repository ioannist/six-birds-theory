#!/usr/bin/env python3
"""Validate KB pointers in docs/spec, docs/registries, and docs/indices."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CANON_PREFIX = "docs/knowledge-base/"
ALT_PREFIX = "knowledge-base/"

DOC_DIRS = [
    ROOT / "docs" / "spec",
    ROOT / "docs" / "registries",
    ROOT / "docs" / "indices",
]

CANON_RE = re.compile(r"(docs/knowledge-base/[\w./-]+\.md):(L\d+(?:-L\d+)?)")
ALT_RE = re.compile(r"(?<!docs/)(knowledge-base/[\w./-]+\.md):(L\d+(?:-L\d+)?)")
LINE_RE = re.compile(r"^L(\d+)(?:-L(\d+))?$")


def iter_doc_files() -> list[Path]:
    files: list[Path] = []
    for root in DOC_DIRS:
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    return files


def parse_line_spec(spec: str) -> tuple[int, int] | None:
    match = LINE_RE.match(spec)
    if not match:
        return None
    start = int(match.group(1))
    end = int(match.group(2) or match.group(1))
    return start, end


def main() -> int:
    errors: list[str] = []
    checked = 0

    for doc_path in iter_doc_files():
        text = doc_path.read_text(encoding="utf-8")

        for match in ALT_RE.finditer(text):
            pointer = f"{match.group(1)}:{match.group(2)}"
            errors.append(
                f"{doc_path.relative_to(ROOT)}: {pointer} -> non-canonical prefix (use {CANON_PREFIX})"
            )

        for match in CANON_RE.finditer(text):
            rel_path, line_spec = match.groups()
            pointer = f"{rel_path}:{line_spec}"
            checked += 1
            file_path = ROOT / rel_path
            if not file_path.exists():
                errors.append(
                    f"{doc_path.relative_to(ROOT)}: {pointer} -> missing file"
                )
                continue
            lines = file_path.read_text(encoding="utf-8").splitlines()
            total = len(lines)
            parsed = parse_line_spec(line_spec)
            if not parsed:
                errors.append(
                    f"{doc_path.relative_to(ROOT)}: {pointer} -> malformed line spec"
                )
                continue
            start, end = parsed
            if start < 1 or end < 1:
                errors.append(
                    f"{doc_path.relative_to(ROOT)}: {pointer} -> line numbers must be >= 1"
                )
                continue
            if start > end:
                errors.append(
                    f"{doc_path.relative_to(ROOT)}: {pointer} -> range start > end"
                )
                continue
            if end > total:
                errors.append(
                    f"{doc_path.relative_to(ROOT)}: {pointer} -> line {end} out of range (max {total})"
                )

    if errors:
        for err in errors:
            print(err)
        print(f"KB pointers FAIL — {checked} checked ({len(errors)} errors)")
        return 1

    print(f"KB pointers OK — {checked} checked (0 errors)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
