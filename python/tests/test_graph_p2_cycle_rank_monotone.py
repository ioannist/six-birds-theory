import numpy as np

from clt.graph import cycle_rank_beta1, erdos_renyi_edges


def test_p2_cycle_rank_monotone_randomized():
    rng = np.random.default_rng(0)
    trials = 300
    for _ in range(trials):
        n = int(rng.integers(3, 21))
        p = float(rng.uniform(0.1, 0.6))
        edges = erdos_renyi_edges(n, p, rng)
        beta0 = cycle_rank_beta1(n, edges)
        q = float(rng.uniform(0.1, 0.9))
        edges_deleted = {e for e in edges if rng.random() > q}
        beta1 = cycle_rank_beta1(n, edges_deleted)
        assert beta1 <= beta0


def test_p2_triangle_deletion_example():
    n = 3
    triangle = {
        frozenset({0, 1}),
        frozenset({1, 2}),
        frozenset({0, 2}),
    }
    beta0 = cycle_rank_beta1(n, triangle)
    edges_deleted = {
        frozenset({0, 1}),
        frozenset({1, 2}),
    }
    beta1 = cycle_rank_beta1(n, edges_deleted)
    assert beta0 == 1
    assert beta1 == 0
