from __future__ import annotations

import numpy as np

from clt.empirical_closure import prototype_stabilities, three_block_chain


def stable_count(P: np.ndarray, tau: int, f: np.ndarray, threshold: float) -> int:
    stabs = prototype_stabilities(P, tau, f)
    return sum(s <= threshold for s in stabs)


def main() -> None:
    f_fine = np.array([0, 0, 1, 1, 2, 2])
    f_coarse = np.array([0, 0, 0, 0, 1, 1])
    threshold = 0.02

    eps_toC = 0.001
    eps_fromC = 0.0005
    eps_ab_list = [0.002, 0.01, 0.05, 0.1, 0.2, 0.3]
    tau_list = [1, 2, 3, 5, 8, 10]

    help_point = None
    hurt_point = None

    header = "tau "+" ".join(f"{x:.3f}" for x in eps_ab_list)
    print(header)
    for tau in tau_list:
        deltas = []
        for eps_ab in eps_ab_list:
            P = three_block_chain(
                eps_ab=eps_ab,
                eps_toC=eps_toC,
                eps_fromC=eps_fromC,
                p_switch=0.35,
            )
            c = stable_count(P, tau, f_coarse, threshold)
            f = stable_count(P, tau, f_fine, threshold)
            delta = f - c
            deltas.append(delta)
            if delta > 0 and help_point is None:
                help_point = (tau, eps_ab, delta)
            if delta < 0 and hurt_point is None:
                hurt_point = (tau, eps_ab, delta)
        print(f"{tau:>3d} " + " ".join(f"{d:>3d}" for d in deltas))

    print("help:", help_point)
    print("hurt:", hurt_point)


if __name__ == "__main__":
    main()
