import numpy as np

from clt.markov import entropy_production_rate, stationary_distribution_solve, time_reversal


def test_rev_support_infinite_ep_convention():
    P = np.array(
        [
            [0.1, 0.9, 0.0],
            [0.0, 0.1, 0.9],
            [0.9, 0.0, 0.1],
        ]
    )
    pi = stationary_distribution_solve(P)
    ep = entropy_production_rate(P, pi)
    assert np.isinf(ep)

    P_rev = time_reversal(P, pi)
    assert np.allclose(P_rev.sum(axis=1), 1.0, atol=1e-12)


def test_rev_support_finite_ep_control():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    pi = np.array([1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0])
    ep = entropy_production_rate(P, pi)
    assert np.isfinite(ep)
    assert ep >= -1e-12
