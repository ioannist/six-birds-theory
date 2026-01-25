import numpy as np

from clt.graph import connected_components, cycle_rank_beta1, erdos_renyi_edges


def _component_index(n: int, comps: list[set[int]]) -> list[int]:
    index = [-1] * n
    for k, comp in enumerate(comps):
        for v in comp:
            index[v] = k
    return index


def test_p1_edge_add_beta1_delta_randomized():
    rng = np.random.default_rng(1)
    trials = 300
    for _ in range(trials):
        n = int(rng.integers(3, 21))
        p = float(rng.uniform(0.1, 0.6))
        edges = erdos_renyi_edges(n, p, rng)
        all_pairs = [frozenset({i, j}) for i in range(n) for j in range(i + 1, n)]
        non_edges = [e for e in all_pairs if e not in edges]
        if not non_edges:
            edges = erdos_renyi_edges(n, 0.3, rng)
            non_edges = [e for e in all_pairs if e not in edges]
        e = non_edges[int(rng.integers(0, len(non_edges)))]
        i, j = tuple(e)

        beta_before = cycle_rank_beta1(n, edges)
        comps = connected_components(n, edges)
        comp_index = _component_index(n, comps)
        same_comp = comp_index[i] == comp_index[j]

        edges_after = set(edges)
        edges_after.add(e)
        beta_after = cycle_rank_beta1(n, edges_after)

        assert beta_after >= beta_before
        if same_comp:
            assert beta_after == beta_before + 1
        else:
            assert beta_after == beta_before


def test_p1_path_to_cycle_example():
    n = 4
    path_edges = {
        frozenset({0, 1}),
        frozenset({1, 2}),
        frozenset({2, 3}),
    }
    beta0 = cycle_rank_beta1(n, path_edges)
    edges_after = set(path_edges)
    edges_after.add(frozenset({0, 3}))
    beta1 = cycle_rank_beta1(n, edges_after)
    assert beta0 == 0
    assert beta1 == 1
