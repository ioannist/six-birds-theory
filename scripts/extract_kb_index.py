#!/usr/bin/env python3
"""Extract headings, statement-like lines, and keyword hits from the KB."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
KB_DIR = ROOT / "docs" / "knowledge-base"
OUT_DIR = ROOT / "docs" / "indices"


HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
STATEMENT_RES = [
    re.compile(r"^\s*(?:[-*]\s*)?Definition\b", re.I),
    re.compile(r"^\s*(?:[-*]\s*)?Lemma\b", re.I),
    re.compile(r"^\s*(?:[-*]\s*)?Theorem\b", re.I),
    re.compile(r"^\s*(?:[-*]\s*)?Corollary\b", re.I),
    re.compile(r"^\s*(?:[-*]\s*)?Proposition\b", re.I),
]
EXERCISE_RE = re.compile(r"^\s*(?:[-*]\s*)?Exercise\b", re.I)
EXERCISE_NAMED_RE = re.compile(
    r"\b(Theorem|Lemma|Proposition|Corollary|Definition|Claim)\b", re.I
)

KEYWORDS = [
    ("closure ladder", re.compile(r"closure ladder", re.I)),
    ("E_{", re.compile(r"E_{")),
    ("AUT", re.compile(r"\bAUT\b")),
    ("REV", re.compile(r"\bREV\b")),
    ("ACC", re.compile(r"\bACC\b")),
    ("path KL", re.compile(r"path KL", re.I)),
    ("path-space KL", re.compile(r"path-space KL", re.I)),
    ("data processing", re.compile(r"data processing", re.I)),
    ("protocol trap", re.compile(r"protocol trap", re.I)),
    ("holonomy", re.compile(r"holonomy", re.I)),
    ("forcing", re.compile(r"forcing", re.I)),
    ("generic extension", re.compile(r"generic extension", re.I)),
    ("Theorem 18.1", re.compile(r"Theorem 18\.1", re.I)),
    ("Physical forcing lemma", re.compile(r"Physical forcing lemma", re.I)),
]


def iter_kb_files() -> list[Path]:
    if not KB_DIR.exists():
        raise SystemExit(f"KB dir not found: {KB_DIR}")
    return sorted(p for p in KB_DIR.rglob("*.md") if p.is_file())


def rel_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def extract() -> tuple[dict[str, list[tuple[int, str, str]]], dict[str, list[tuple[int, str]]], dict[str, list[tuple[int, str, str]]]]:
    headings: dict[str, list[tuple[int, str, str]]] = {}
    statements: dict[str, list[tuple[int, str]]] = {}
    keyword_hits: dict[str, list[tuple[int, str, str]]] = {k[0]: [] for k in KEYWORDS}

    for path in iter_kb_files():
        display_path = rel_path(path)
        headings[display_path] = []
        statements[display_path] = []
        with path.resolve().open("r", encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, 1):
                stripped = line.rstrip("\n")
                heading_match = HEADING_RE.match(stripped)
                if heading_match:
                    level, text = heading_match.groups()
                    headings[display_path].append((lineno, level, text.strip()))

                if any(regex.search(stripped) for regex in STATEMENT_RES):
                    statements[display_path].append((lineno, stripped.strip()))
                elif EXERCISE_RE.search(stripped) and EXERCISE_NAMED_RE.search(stripped):
                    statements[display_path].append((lineno, stripped.strip()))

                for label, pattern in KEYWORDS:
                    if pattern.search(stripped):
                        keyword_hits[label].append((lineno, display_path, stripped.strip()))

    return headings, statements, keyword_hits


def write_headings(out_path: Path, headings: dict[str, list[tuple[int, str, str]]]) -> None:
    lines = ["# Knowledge Base Headings", ""]
    for file_path in sorted(headings.keys()):
        lines.append(f"## {file_path}")
        entries = headings[file_path]
        if not entries:
            lines.append("- (no headings found)")
        else:
            for lineno, level, text in entries:
                lines.append(f"- L{lineno} {level} {text}")
        lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_statements(out_path: Path, statements: dict[str, list[tuple[int, str]]]) -> None:
    lines = ["# Knowledge Base Statement-Like Lines", ""]
    for file_path in sorted(statements.keys()):
        lines.append(f"## {file_path}")
        entries = statements[file_path]
        if not entries:
            lines.append("- (no statement-like lines found)")
        else:
            for lineno, text in entries:
                lines.append(f"- L{lineno}: {text}")
        lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_keyword_hits(out_path: Path, keyword_hits: dict[str, list[tuple[int, str, str]]]) -> None:
    lines = ["# Knowledge Base Keyword Hits", ""]
    for label, _pattern in KEYWORDS:
        lines.append(f"## {label}")
        hits = keyword_hits[label]
        if not hits:
            lines.append("- (no hits found)")
        else:
            for lineno, file_path, text in hits:
                lines.append(f"- {file_path}:L{lineno}: {text}")
        lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    headings, statements, keyword_hits = extract()
    write_headings(OUT_DIR / "kb_headings.md", headings)
    write_statements(OUT_DIR / "kb_statements.md", statements)
    write_keyword_hits(OUT_DIR / "kb_keyword_hits.md", keyword_hits)


if __name__ == "__main__":
    main()
