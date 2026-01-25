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


def test_p1_spectral_gap_decrease():
    n = 12
    edges_before = _complete_graph_edges(n)

    block1 = range(6)
    block2 = range(6, 12)
    edges_after = _clique_edges(block1) | _clique_edges(block2)
    edges_after.add(frozenset({0, 6}))

    gap_before = spectral_gap_lazy_rw(n, edges_before)
    gap_after = spectral_gap_lazy_rw(n, edges_after)

    assert gap_after < gap_before / 5.0
    assert gap_before > 0.2
    assert gap_after < 0.1
