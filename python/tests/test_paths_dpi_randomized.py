import numpy as np

from clt.markov import normalize_rows, stationary_distribution
from clt.paths import arrow_path_kl, arrow_path_kl_coarse


def _surjective_map(rng: np.random.Generator, n: int, k: int) -> np.ndarray:
    while True:
        f = rng.integers(0, k, size=n)
        if len(set(f.tolist())) == k:
            return f


def test_dpi_randomized_path_kl():
    rng = np.random.default_rng(0)
    trials = 150
    T_list = [1, 2, 3]
    max_slack = -1e9

    for _ in range(trials):
        n = int(rng.integers(3, 7))
        A = rng.random((n, n)) + 1e-3
        P = normalize_rows(A)
        pi = stationary_distribution(P)

        k = int(rng.integers(2, n))
        f = _surjective_map(rng, n, k)

        inits = [pi]
        if rng.random() < 0.33:
            inits.append(rng.dirichlet(np.ones(n)))

        for init in inits:
            for T in T_list:
                sigma_micro = arrow_path_kl(P, init, T)
                sigma_macro = arrow_path_kl_coarse(P, init, T, f)
                slack = sigma_macro - sigma_micro
                if slack > max_slack:
                    max_slack = slack
                assert sigma_micro >= -1e-12
                assert sigma_macro >= -1e-12
                # Numerical tolerance for coarse-graining DPI (floating-point error).
                assert slack <= 1e-10

    assert max_slack <= 1e-10
