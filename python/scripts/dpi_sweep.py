from __future__ import annotations

import numpy as np

from clt.markov import normalize_rows, stationary_distribution
from clt.paths import arrow_path_kl, arrow_path_kl_coarse


def surjective_map(rng: np.random.Generator, n: int, k: int) -> np.ndarray:
    while True:
        f = rng.integers(0, k, size=n)
        if len(set(f.tolist())) == k:
            return f


def randomized_dpi_sweep() -> None:
    rng = np.random.default_rng(0)
    trials = 200
    T_list = [1, 2, 3]
    n_min, n_max = 3, 6

    max_slack = -1e9
    worst = None

    for _ in range(trials):
        n = int(rng.integers(n_min, n_max + 1))
        A = rng.random((n, n)) + 1e-3
        P = normalize_rows(A)
        pi = stationary_distribution(P)
        k = int(rng.integers(2, n))
        f = surjective_map(rng, n, k)

        for T in T_list:
            sigma_micro = arrow_path_kl(P, pi, T)
            sigma_macro = arrow_path_kl_coarse(P, pi, T, f)
            slack = sigma_macro - sigma_micro
            if slack > max_slack:
                max_slack = slack
                worst = (n, k, T, f.copy())

    print("Randomized DPI sweep")
    print(f"Trials: {trials} (seed=0)")
    print(f"n range: [{n_min},{n_max}], T_list: {T_list}")
    if worst is None:
        print("No cases recorded")
    else:
        n, k, T, f = worst
        print(f"max_slack: {max_slack:.3e}")
        print(f"worst_case: n={n}, k={k}, T={T}, f={f.tolist()}")


def strict_hiding_example() -> None:
    p, q, r = 0.4, 0.1, 0.5
    P = np.array(
        [
            [r, p, q],
            [q, r, p],
            [p, q, r],
        ]
    )
    pi = np.ones(3) / 3
    f = np.array([0, 1, 0])

    print("Strict hiding example")
    print(f"p={p}, q={q}, r={r}, f={f.tolist()}")
    for T in [1, 2, 3, 4]:
        sigma_micro = arrow_path_kl(P, pi, T)
        sigma_macro = arrow_path_kl_coarse(P, pi, T, f)
        print(f"T={T} micro={sigma_micro:.6e} macro={sigma_macro:.6e}")


def main() -> None:
    randomized_dpi_sweep()
    strict_hiding_example()


if __name__ == "__main__":
    main()
