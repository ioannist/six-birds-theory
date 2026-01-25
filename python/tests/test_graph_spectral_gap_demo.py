import numpy as np

from clt.graph import spectral_gap_lazy_rw


def _clique_edges(nodes: list[int]) -> set[frozenset[int]]:
    edges: set[frozenset[int]] = set()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edges.add(frozenset({nodes[i], nodes[j]}))
    return edges


def test_spectral_gap_barbell_rewire():
    m = 5
    n = 2 * m
    left = list(range(m))
    right = list(range(m, 2 * m))
    edges = _clique_edges(left) | _clique_edges(right)
    edges.add(frozenset({m - 1, m}))

    gap_before = spectral_gap_lazy_rw(n, edges)

    edges_after = set(edges)
    for u, v in [(0, m), (1, m + 1), (2, m + 2), (3, m + 3)]:
        edges_after.add(frozenset({u, v}))

    gap_after = spectral_gap_lazy_rw(n, edges_after)

    assert 0.0 <= gap_before <= 1.0 + 1e-12
    assert 0.0 <= gap_after <= 1.0 + 1e-12
    assert gap_after > gap_before + 1e-3
