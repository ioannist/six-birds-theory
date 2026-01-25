import numpy as np

from clt.markov import normalize_rows, stationary_distribution
from clt.paths import (
    enumerate_path_law,
    kl_divergence,
    path_kl_forward_reverse,
    pushforward_path_law,
    reverse_path_law,
)


def _surjective_map(rng: np.random.Generator, n: int, k: int) -> np.ndarray:
    while True:
        f = rng.integers(0, k, size=n)
        if len(set(f.tolist())) == k:
            return f


def _path_kl_coarse(P: np.ndarray, init: np.ndarray, T: int, f: np.ndarray) -> float:
    law = enumerate_path_law(P, init, T)
    coarse = pushforward_path_law(law, lambda i: int(f[i]))
    return kl_divergence(coarse, reverse_path_law(coarse))


def test_dpi_nonstationary_randomized():
    rng = np.random.default_rng(2)
    trials = 120
    T_list = [1, 2]
    max_slack = -1e9

    for _ in range(trials):
        n = int(rng.integers(3, 7))
        A = rng.random((n, n)) + 1e-3
        P = normalize_rows(A)
        pi = stationary_distribution(P)

        init = rng.dirichlet(np.ones(n))
        if np.linalg.norm(init - pi, ord=1) < 1e-3:
            init = init.copy()
            init[0] += 0.01
            init = init / init.sum()

        k = int(rng.integers(2, n))
        f = _surjective_map(rng, n, k)

        for T in T_list:
            sigma_micro = path_kl_forward_reverse(P, init, T)
            sigma_macro = _path_kl_coarse(P, init, T, f)
            slack = sigma_macro - sigma_micro
            if slack > max_slack:
                max_slack = slack
            assert sigma_micro >= -1e-12
            assert sigma_macro >= -1e-12
            # Tolerance accounts for floating-point error in enumeration.
            assert slack <= 1e-10

    assert max_slack <= 1e-10


def test_boundary_term_example_nonstationary_init():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    pi = stationary_distribution(P)
    rho = np.array([0.7, 0.2, 0.1])

    sigma_pi = path_kl_forward_reverse(P, pi, T=2)
    sigma_rho = path_kl_forward_reverse(P, rho, T=2)

    assert abs(sigma_pi) <= 1e-12
    assert sigma_rho > 1e-3
