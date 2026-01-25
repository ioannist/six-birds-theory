import numpy as np

from clt.markov import entropy_production_rate, stationary_distribution
from clt.paths import (
    enumerate_path_law,
    kl_divergence,
    pushforward_path_law,
    reverse_path_law,
)


def test_data_processing_for_path_kl():
    P = np.array(
        [
            [0.1, 0.6, 0.2, 0.1],
            [0.2, 0.1, 0.6, 0.1],
            [0.1, 0.2, 0.1, 0.6],
            [0.6, 0.1, 0.2, 0.1],
        ]
    )
    pi = stationary_distribution(P)
    assert entropy_production_rate(P, pi) > 0.0
    T = 3
    law = enumerate_path_law(P, pi, T)
    rev = reverse_path_law(law)
    kl_micro = kl_divergence(law, rev)

    f = [0, 0, 1, 2]
    def coarse(x: int) -> int:
        return f[x]

    law_macro = pushforward_path_law(law, coarse)
    rev_macro = pushforward_path_law(rev, coarse)
    kl_macro = kl_divergence(law_macro, rev_macro)

    assert kl_macro <= kl_micro + 1e-10


def test_path_kl_zero_for_reversible_chain():
    P = np.array(
        [
            [0.5, 0.25, 0.25],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5],
        ]
    )
    pi = np.ones(3) / 3
    law = enumerate_path_law(P, pi, T=3)
    rev = reverse_path_law(law)
    kl = kl_divergence(law, rev)
    assert abs(kl) <= 1e-12
