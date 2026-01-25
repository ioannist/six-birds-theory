import numpy as np

from clt.empirical_closure import max_idempotence_defect, three_block_chain


def test_idempotence_defect_leakage_trend():
    tau = 5
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

    assert d_small < 0.02
    assert d_large > 0.05
    assert d_small < d_large
