import numpy as np

from clt.markov import entropy_production_rate
from clt.protocol import make_positive_reversible_pair, phase_flip_chain, phase_flip_stationary
from clt.paths import enumerate_path_law, kl_divergence, reverse_path_law


def test_protocol_clock_audit_phi_included():
    pi, K0, K1 = make_positive_reversible_pair(n=3, a=0.4, b=0.4, delta=0.1)
    piZ = phase_flip_stationary(pi)

    P_half = phase_flip_chain(K0, K1, alpha=0.5)
    epZ_half = entropy_production_rate(P_half, piZ)
    assert abs(epZ_half) < 1e-12

    P_bias = phase_flip_chain(K0, K1, alpha=0.7)
    epZ_bias = entropy_production_rate(P_bias, piZ)
    assert epZ_bias > 1e-5

    law_half = enumerate_path_law(P_half, piZ, T=2)
    kl_half = kl_divergence(law_half, reverse_path_law(law_half))
    assert abs(kl_half) < 1e-12

    law_bias = enumerate_path_law(P_bias, piZ, T=2)
    kl_bias = kl_divergence(law_bias, reverse_path_law(law_bias))
    assert kl_bias > 1e-5
