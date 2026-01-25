import math


def test_forcing_fixed_weight_differs_from_iid():
    N = 12
    K = 3
    block_sizes = [4, 4, 4]
    w = 6

    # Definable predicates under fixed weight correspond to block unions of size w.
    count_def = 0
    for mask in range(1 << K):
        total = 0
        for i in range(K):
            if (mask >> i) & 1:
                total += block_sizes[i]
        if total == w:
            count_def += 1

    total_subsets = math.comb(N, w)
    p_def_fixed_weight = count_def / total_subsets
    p_def_iid = 2 ** (-(N - K))

    assert p_def_fixed_weight == 0.0
    assert p_def_iid == 2 ** -9
