import numpy as np

from clt.markov import (
    entropy_production_rate,
    stationary_distribution,
    time_reversal,
    validate_transition_matrix,
)


def test_stationary_distribution_sanity():
    P = np.array(
        [
            [0.1, 0.6, 0.3],
            [0.2, 0.5, 0.3],
            [0.3, 0.3, 0.4],
        ]
    )
    pi = stationary_distribution(P)
    assert np.allclose(pi @ P, pi, atol=1e-10)


def test_time_reversal_sanity():
    P = np.array(
        [
            [0.1, 0.6, 0.3],
            [0.2, 0.5, 0.3],
            [0.3, 0.3, 0.4],
        ]
    )
    pi = stationary_distribution(P)
    P_rev = time_reversal(P, pi)
    validate_transition_matrix(P_rev)
    for i in range(P.shape[0]):
        for j in range(P.shape[0]):
            left = pi[i] * P[i, j]
            right = pi[j] * P_rev[j, i]
            assert np.isclose(left, right, atol=1e-10)


def test_ep_zero_for_reversible_chain():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    pi = np.ones(3) / 3
    ep = entropy_production_rate(P, pi)
    assert abs(ep) <= 1e-12


def test_ep_positive_for_biased_cycle():
    P = np.array(
        [
            [0.1, 0.8, 0.1],
            [0.1, 0.1, 0.8],
            [0.8, 0.1, 0.1],
        ]
    )
    pi = stationary_distribution(P)
    ep = entropy_production_rate(P, pi)
    assert ep > 1e-6


def test_ep_requires_rev_support():
    P = np.array(
        [
            [0.0, 1.0],
            [0.0, 1.0],
        ]
    )
    pi = np.array([0.5, 0.5])
    assert np.isinf(entropy_production_rate(P, pi))
