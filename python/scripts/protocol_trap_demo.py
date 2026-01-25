from __future__ import annotations

import numpy as np

from clt.markov import entropy_production_rate
from clt.protocol import (
    autonomous_stroboscopic,
    external_stroboscopic,
    make_positive_reversible_pair,
    phase_flip_chain,
    phase_flip_stationary,
)


def main() -> None:
    np.set_printoptions(precision=6, suppress=True)
    pi, K0, K1 = make_positive_reversible_pair(n=3, a=0.4, b=0.4, delta=0.1)
    comm = np.max(np.abs(K0 @ K1 - K1 @ K0))

    R_ext = external_stroboscopic(K0, K1)
    R_half = autonomous_stroboscopic(K0, K1, alpha=0.5)
    R_bias = autonomous_stroboscopic(K0, K1, alpha=0.7)

    piZ = phase_flip_stationary(pi)
    PZ_half = phase_flip_chain(K0, K1, alpha=0.5)
    PZ_bias = phase_flip_chain(K0, K1, alpha=0.7)

    print("K0:")
    print(K0)
    print("K1:")
    print(K1)
    print(f"maxabs_commutator: {comm:.6e}")
    print(f"ep(R_ext): {entropy_production_rate(R_ext, pi):.6e}")
    print(f"ep(R(0.5)): {entropy_production_rate(R_half, pi):.6e}")
    print(f"ep(R(0.7)): {entropy_production_rate(R_bias, pi):.6e}")
    print(f"ep(PZ(0.5)): {entropy_production_rate(PZ_half, piZ):.6e}")
    print(f"ep(PZ(0.7)): {entropy_production_rate(PZ_bias, piZ):.6e}")


if __name__ == "__main__":
    main()
