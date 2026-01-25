import numpy as np

from clt.forcing import estimate_frequencies


def test_monte_carlo_matches_theory_regime_a():
    f = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
    result = estimate_frequencies(f, n_samples=20_000, seed=0, chunk=10_000)

    p_def_emp = result["p_def_emp"]
    p_def_theory = result["p_def_theory"]
    p_split_emp = result["p_split_emp"]
    p_split_theory = result["p_split_theory"]
    p_split_union_lb = result["p_split_union_lb"]

    assert abs(p_def_emp - p_def_theory) <= 0.01
    assert abs(p_split_emp - p_split_theory) <= 0.03
    assert p_split_emp + 0.02 >= p_split_union_lb


def test_monte_carlo_matches_theory_regime_b():
    f = np.array(
        [
            0, 0, 0, 0,
            1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3, 3,
        ]
    )
    result = estimate_frequencies(f, n_samples=200_000, seed=1, chunk=50_000)

    p_def_emp = result["p_def_emp"]
    p_def_theory = result["p_def_theory"]
    p_split_emp = result["p_split_emp"]
    p_split_theory = result["p_split_theory"]
    p_split_union_lb = result["p_split_union_lb"]

    assert abs(p_def_emp - p_def_theory) <= 3e-4
    assert abs(p_split_emp - p_split_theory) <= 0.01
    assert p_split_emp + 0.02 >= p_split_union_lb
