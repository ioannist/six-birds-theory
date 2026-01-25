from __future__ import annotations

import numpy as np

from clt.graph import cycle_rank_beta1, spectral_gap_lazy_rw


def _edge_list(edges: set[frozenset[int]]) -> list[tuple[int, int]]:
    pairs = [tuple(sorted(tuple(e))) for e in edges]
    return sorted(pairs)


def _clique_edges(nodes: list[int]) -> set[frozenset[int]]:
    edges: set[frozenset[int]] = set()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edges.add(frozenset({nodes[i], nodes[j]}))
    return edges


def main() -> None:
    # P2 example: triangle -> delete edge.
    n = 3
    triangle = {
        frozenset({0, 1}),
        frozenset({1, 2}),
        frozenset({0, 2}),
    }
    deleted = {
        frozenset({0, 1}),
        frozenset({1, 2}),
    }
    print("P2 example (triangle -> delete one edge)")
    print(f"edges_before: {_edge_list(triangle)} beta1={cycle_rank_beta1(n, triangle)}")
    print(f"edges_after:  {_edge_list(deleted)} beta1={cycle_rank_beta1(n, deleted)}")

    # P1 example: path -> add edge.
    n = 4
    path_edges = {
        frozenset({0, 1}),
        frozenset({1, 2}),
        frozenset({2, 3}),
    }
    cycle_edges = set(path_edges)
    cycle_edges.add(frozenset({0, 3}))
    print("P1 example (path -> add edge)")
    print(f"edges_before: {_edge_list(path_edges)} beta1={cycle_rank_beta1(n, path_edges)}")
    print(f"edges_after:  {_edge_list(cycle_edges)} beta1={cycle_rank_beta1(n, cycle_edges)}")

    # Spectral gap demo.
    m = 5
    n = 2 * m
    left = list(range(m))
    right = list(range(m, 2 * m))
    edges = _clique_edges(left) | _clique_edges(right)
    edges.add(frozenset({m - 1, m}))
    edges_after = set(edges)
    for u, v in [(0, m), (1, m + 1), (2, m + 2), (3, m + 3)]:
        edges_after.add(frozenset({u, v}))

    gap_before = spectral_gap_lazy_rw(n, edges)
    gap_after = spectral_gap_lazy_rw(n, edges_after)

    print("Spectral gap demo (barbell -> add cross edges)")
    print(f"n={n}, m={m}, gap_before={gap_before:.6e}, gap_after={gap_after:.6e}")


if __name__ == "__main__":
    main()
