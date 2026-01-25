import numpy as np

from clt.empirical_closure import (
    idempotence_defect,
    idempotence_defect_tv,
    induced_empirical_closure,
    max_idempotence_defect,
    three_block_chain,
)


def _make_mus(n: int) -> list[np.ndarray]:
    mus = []
    for z in range(n):
        mu = np.zeros(n)
        mu[z] = 1.0
        mus.append(mu)
    mus.append(np.ones(n) / n)
    return mus


def _empirical_operator_matrix(P: np.ndarray, tau: int, f: np.ndarray) -> np.ndarray:
    n = P.shape[0]
    E = np.zeros((n, n), dtype=float)
    for i in range(n):
        mu = np.zeros(n)
        mu[i] = 1.0
        E[i, :] = induced_empirical_closure(mu, P, tau, f)
    return E


def test_idempotence_defect_tv_matches_diracs():
    tau = 5
    f_coarse = np.array([0, 0, 0, 0, 1, 1])

    P_small = three_block_chain(
        eps_ab=2e-4, eps_toC=2e-3, eps_fromC=1e-3, p_switch=0.35
    )
    P_large = three_block_chain(
        eps_ab=5e-2, eps_toC=1e-1, eps_fromC=5e-2, p_switch=0.35
    )

    mus = _make_mus(6)

    d_old_small = max_idempotence_defect(P_small, tau, f_coarse, mus)
    d_old_large = max_idempotence_defect(P_large, tau, f_coarse, mus)

    E_small = _empirical_operator_matrix(P_small, tau, f_coarse)
    E_large = _empirical_operator_matrix(P_large, tau, f_coarse)

    d_new_small = idempotence_defect_tv(E_small)
    d_new_large = idempotence_defect_tv(E_large)

    assert d_old_small <= d_new_small + 1e-12
    assert d_old_large <= d_new_large + 1e-12
    assert abs(d_old_small - d_new_small) <= 1e-12
    assert abs(d_old_large - d_new_large) <= 1e-12


def test_dirichlet_points_below_extreme_point_max():
    rng = np.random.default_rng(0)
    tau = 5
    f_coarse = np.array([0, 0, 0, 0, 1, 1])
    P_small = three_block_chain(
        eps_ab=2e-4, eps_toC=2e-3, eps_fromC=1e-3, p_switch=0.35
    )

    E_small = _empirical_operator_matrix(P_small, tau, f_coarse)
    d_new = idempotence_defect_tv(E_small)

    max_val = 0.0
    for _ in range(200):
        mu = rng.dirichlet(np.ones(6))
        mu1 = mu @ E_small
        mu2 = mu1 @ E_small
        val = 0.5 * float(np.abs(mu2 - mu1).sum())
        if val > max_val:
            max_val = val

    assert max_val <= d_new + 1e-12
