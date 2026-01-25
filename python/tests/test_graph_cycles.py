from clt.graph import cycle_rank_beta1


def test_cycle_rank_basic():
    n = 4
    tree_edges = {frozenset({0, 1}), frozenset({1, 2}), frozenset({2, 3})}
    assert cycle_rank_beta1(n, tree_edges) == 0

    one_cycle = set(tree_edges)
    one_cycle.add(frozenset({0, 2}))
    assert cycle_rank_beta1(n, one_cycle) == 1


def test_cycle_rank_decreases_on_edge_removal():
    n = 4
    cycle_edges = {
        frozenset({0, 1}),
        frozenset({1, 2}),
        frozenset({2, 3}),
        frozenset({3, 0}),
    }
    assert cycle_rank_beta1(n, cycle_edges) == 1

    removed = set(cycle_edges)
    removed.remove(frozenset({3, 0}))
    assert cycle_rank_beta1(n, removed) == 0
