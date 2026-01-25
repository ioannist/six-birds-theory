import numpy as np

from clt.markov import stationary_distribution_solve


def test_stationary_distribution_reducible_tiebreak():
    P = np.eye(2)

    pi_left = stationary_distribution_solve(P, init=np.array([1.0, 0.0]))
    pi_right = stationary_distribution_solve(P, init=np.array([0.0, 1.0]))
    pi_uniform = stationary_distribution_solve(P, init=None)

    assert np.allclose(pi_left, np.array([1.0, 0.0]), atol=1e-12)
    assert np.allclose(pi_right, np.array([0.0, 1.0]), atol=1e-12)
    assert np.allclose(pi_uniform, np.array([0.5, 0.5]), atol=1e-12)
