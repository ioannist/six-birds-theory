import numpy as np
import pytest

from clt.markov import (
    _stationary_distribution_power,
    stationary_distribution,
    stationary_distribution_cesaro,
    stationary_distribution_solve,
)


def test_stationary_distribution_periodic_two_cycle():
    P = np.array([[0.0, 1.0], [1.0, 0.0]])
    init = np.array([0.6, 0.4])

    pi_power, converged = _stationary_distribution_power(
        P, tol=1e-12, max_iter=200, init=init
    )
    assert converged is False

    pi_solve = stationary_distribution_solve(P)
    pi_cesaro = stationary_distribution_cesaro(P, n_steps=20000, init=init)

    assert np.allclose(pi_solve, np.array([0.5, 0.5]), atol=1e-10)
    assert np.allclose(pi_cesaro, np.array([0.5, 0.5]), atol=1e-4)
    assert np.allclose(pi_solve @ P, pi_solve, atol=1e-10)

    pi_default = stationary_distribution(P, on_fail="solve", max_iter=200, init=init)
    assert np.allclose(pi_default, pi_solve, atol=1e-10)

    with pytest.raises(RuntimeError):
        stationary_distribution(P, on_fail="raise", max_iter=200, init=init)
