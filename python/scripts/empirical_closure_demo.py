from __future__ import annotations

import numpy as np

from clt.empirical_closure import (
    induced_empirical_closure,
    max_idempotence_defect,
    idempotence_defect_tv,
    prototype_stabilities,
    three_block_chain,
)


def main() -> None:
    tau = 5
    f_fine = np.array([0, 0, 1, 1, 2, 2])
    f_coarse = np.array([0, 0, 0, 0, 1, 1])

    mus = []
    for z in range(6):
        mu = np.zeros(6)
        mu[z] = 1.0
        mus.append(mu)
    mus.append(np.ones(6) / 6.0)

    P_small = three_block_chain(
        eps_ab=2e-4, eps_toC=2e-3, eps_fromC=1e-3, p_switch=0.35
    )
    P_large = three_block_chain(
        eps_ab=5e-2, eps_toC=1e-1, eps_fromC=5e-2, p_switch=0.35
    )

    d_small = max_idempotence_defect(P_small, tau, f_coarse, mus)
    d_large = max_idempotence_defect(P_large, tau, f_coarse, mus)

    def build_E(P: np.ndarray, f: np.ndarray) -> np.ndarray:
        n = P.shape[0]
        E = np.zeros((n, n), dtype=float)
        for i in range(n):
            mu = np.zeros(n)
            mu[i] = 1.0
            E[i, :] = induced_empirical_closure(mu, P, tau, f)
        return E

    E_small_coarse = build_E(P_small, f_coarse)
    E_large_coarse = build_E(P_large, f_coarse)
    E_small_fine = build_E(P_small, f_fine)
    E_large_fine = build_E(P_large, f_fine)

    d_small_tv_coarse = idempotence_defect_tv(E_small_coarse)
    d_large_tv_coarse = idempotence_defect_tv(E_large_coarse)
    d_small_tv_fine = idempotence_defect_tv(E_small_fine)
    d_large_tv_fine = idempotence_defect_tv(E_large_fine)

    stab_coarse = prototype_stabilities(P_small, tau, f_coarse)
    stab_fine = prototype_stabilities(P_small, tau, f_fine)

    thresh = 0.02
    count_coarse = sum(s <= thresh for s in stab_coarse)
    count_fine = sum(s <= thresh for s in stab_fine)

    print(f"d_small: {d_small:.6f}")
    print(f"d_large: {d_large:.6f}")
    print(f"d_small_tv_coarse: {d_small_tv_coarse:.6f}")
    print(f"d_large_tv_coarse: {d_large_tv_coarse:.6f}")
    print(f"d_small_tv_fine: {d_small_tv_fine:.6f}")
    print(f"d_large_tv_fine: {d_large_tv_fine:.6f}")
    print(f"stab_coarse: {[round(x, 6) for x in stab_coarse]}")
    print(f"stab_fine: {[round(x, 6) for x in stab_fine]}")
    print(f"stable_counts (<= {thresh}): coarse={count_coarse}, fine={count_fine}")


if __name__ == "__main__":
    main()
