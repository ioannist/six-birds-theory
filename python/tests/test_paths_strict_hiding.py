import numpy as np

from clt.paths import arrow_path_kl, arrow_path_kl_coarse


def test_strict_hiding_three_cycle_merge_0_2():
    p = 0.4
    q = 0.1
    r = 0.5
    P = np.array(
        [
            [r, p, q],
            [q, r, p],
            [p, q, r],
        ]
    )
    pi = np.ones(3) / 3
    f = np.array([0, 1, 0])

    micro_positive = False
    for T in [1, 2, 3, 4]:
        sigma_micro = arrow_path_kl(P, pi, T)
        sigma_macro = arrow_path_kl_coarse(P, pi, T, f)
        if sigma_micro > 1e-6:
            micro_positive = True
        assert abs(sigma_macro) <= 1e-12

    assert micro_positive
