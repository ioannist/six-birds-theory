import numpy as np

from clt.markov import entropy_production_rate
from clt.protocol import (
    autonomous_stroboscopic,
    external_stroboscopic,
    make_positive_reversible_pair,
)


def test_protocol_trap_external_vs_autonomous():
    pi, K0, K1 = make_positive_reversible_pair(n=3, a=0.4, b=0.4, delta=0.1)

    comm = np.max(np.abs(K0 @ K1 - K1 @ K0))
    assert comm > 1e-8

    R_ext = external_stroboscopic(K0, K1)
    ep_ext = entropy_production_rate(R_ext, pi)
    assert ep_ext > 1e-3

    R_half = autonomous_stroboscopic(K0, K1, alpha=0.5)
    ep_half = entropy_production_rate(R_half, pi)
    assert abs(ep_half) < 1e-12

    R_bias = autonomous_stroboscopic(K0, K1, alpha=0.7)
    ep_bias = entropy_production_rate(R_bias, pi)
    assert ep_bias > 1e-5
