from __future__ import annotations

import numpy as np

from clt.forcing import estimate_frequencies


def main() -> None:
    configs = [
        (np.array([0, 0, 0, 1, 1, 1, 2, 2, 2]), 20_000, 0),
        (
            np.array(
                [
                    0, 0, 0, 0,
                    1, 1, 1, 1,
                    2, 2, 2, 2,
                    3, 3, 3, 3,
                ]
            ),
            200_000,
            1,
        ),
    ]

    header = (
        "N K N-K samples p_def_emp p_def_theory "
        "p_split_emp p_split_theory p_split_union_lb"
    )
    print(header)
    for f, n_samples, seed in configs:
        result = estimate_frequencies(f, n_samples=n_samples, seed=seed, chunk=50_000)
        print(
            f"{result['N']} {result['K']} {result['N']-result['K']} {result['n_samples']} "
            f"{result['p_def_emp']:.6f} {result['p_def_theory']:.6f} "
            f"{result['p_split_emp']:.6f} {result['p_split_theory']:.6f} "
            f"{result['p_split_union_lb']:.6f}"
        )


if __name__ == "__main__":
    main()
