from __future__ import annotations

import numpy as np

from clt.graph import spectral_gap_lazy_rw


def _complete_graph_edges(n: int) -> set[frozenset[int]]:
    edges = set()
    for i in range(n):
        for j in range(i + 1, n):
            edges.add(frozenset({i, j}))
    return edges


def _clique_edges(nodes: range) -> set[frozenset[int]]:
    edges = set()
    nodes = list(nodes)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edges.add(frozenset({nodes[i], nodes[j]}))
    return edges


def main() -> None:
    n = 12
    block1 = range(6)
    block2 = range(6, 12)

    edges_before = _complete_graph_edges(n)
    edges_after = _clique_edges(block1) | _clique_edges(block2)
    edges_after.add(frozenset({0, 6}))

    gap_before = spectral_gap_lazy_rw(n, edges_before)
    gap_after = spectral_gap_lazy_rw(n, edges_after)

    print(f"n={n}, blocks=6+6, bridges=1 (0-6)")
    print(f"gap_before={gap_before:.6f}")
    print(f"gap_after={gap_after:.6f}")
    print(f"ratio={gap_after / gap_before:.6f}")


if __name__ == "__main__":
    main()
