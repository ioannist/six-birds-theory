import numpy as np

from clt.markov import entropy_production_rate, validate_transition_matrix


def test_protocol_stroboscopic_irreversibility():
    K0 = np.array(
        [
            [0.7, 0.2, 0.1],
            [0.2, 0.65, 0.15],
            [0.1, 0.15, 0.75],
        ]
    )
    K1 = np.array(
        [
            [0.45, 0.3, 0.25],
            [0.3, 0.65, 0.05],
            [0.25, 0.05, 0.7],
        ]
    )
    assert np.allclose(K0, K0.T)
    assert np.allclose(K1, K1.T)
    K = K1 @ K0
    validate_transition_matrix(K)
    assert not np.allclose(K, K.T)

    pi = np.ones(3) / 3
    ep = entropy_production_rate(K, pi)
    assert ep > 0.0
