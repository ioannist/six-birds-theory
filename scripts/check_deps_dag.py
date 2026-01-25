#!/usr/bin/env python3
"""Check docs/spec/deps.dot for cycles."""

from __future__ import annotations

from pathlib import Path
import re
import sys


DOT_PATH = Path(__file__).resolve().parents[1] / "docs" / "spec" / "deps.dot"
INVENTORY_PATH = Path(__file__).resolve().parents[1] / "docs" / "spec" / "theorem-inventory.md"
EDGE_RE = re.compile(r"\"([^\"]+)\"\s*->\s*\"([^\"]+)\"")
ID_RE = re.compile(r"^- \*\*ID:\*\* (.+)$")


def load_edges(text: str):
    edges = []
    nodes = set()
    for line in text.splitlines():
        match = EDGE_RE.search(line)
        if match:
            src, dst = match.groups()
            edges.append((src, dst))
            nodes.add(src)
            nodes.add(dst)
    return nodes, edges


def load_inventory_ids(text: str):
    ids = set()
    for line in text.splitlines():
        match = ID_RE.match(line.strip())
        if match:
            ids.add(match.group(1).strip())
    return ids


def find_cycle(nodes, edges):
    graph = {n: [] for n in nodes}
    for src, dst in edges:
        graph.setdefault(src, []).append(dst)
        graph.setdefault(dst, [])

    visiting = set()
    visited = set()
    stack = []

    def dfs(node):
        visiting.add(node)
        stack.append(node)
        for nxt in graph.get(node, []):
            if nxt in visiting:
                idx = stack.index(nxt)
                return stack[idx:] + [nxt]
            if nxt not in visited:
                cycle = dfs(nxt)
                if cycle:
                    return cycle
        visiting.remove(node)
        visited.add(node)
        stack.pop()
        return None

    for n in sorted(graph.keys()):
        if n not in visited:
            cycle = dfs(n)
            if cycle:
                return cycle
    return None


def main() -> int:
    if not DOT_PATH.exists():
        print(f"Missing dot file: {DOT_PATH}")
        return 1
    if not INVENTORY_PATH.exists():
        print(f"Missing inventory file: {INVENTORY_PATH}")
        return 1
    text = DOT_PATH.read_text(encoding="utf-8")
    nodes, edges = load_edges(text)
    if not edges:
        print("No edges found")
        return 1
    inventory_ids = load_inventory_ids(INVENTORY_PATH.read_text(encoding="utf-8"))
    missing = sorted(n for n in nodes if n not in inventory_ids)
    if missing:
        print("Missing IDs in inventory: " + ", ".join(missing))
        return 1
    cycle = find_cycle(nodes, edges)
    if cycle:
        print("Cycle: " + " -> ".join(cycle))
        return 1
    print("DAG OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
