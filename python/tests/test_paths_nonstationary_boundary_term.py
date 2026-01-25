import numpy as np

from clt.markov import stationary_distribution
from clt.paths import path_kl_forward_reverse


def test_stationary_init_reversible_gives_zero_path_kl():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    pi = stationary_distribution(P)
    for T in [1, 2, 3, 4]:
        sigma = path_kl_forward_reverse(P, pi, T)
        assert abs(sigma) <= 1e-12


def test_nonstationary_init_reversible_gives_positive_path_kl():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    init = np.array([0.7, 0.2, 0.1])
    sigma = path_kl_forward_reverse(P, init, T=2)
    assert sigma > 1e-3
