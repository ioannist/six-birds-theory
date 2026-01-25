import numpy as np

from clt.empirical_closure import prototype_stabilities, three_block_chain


def test_refinement_can_hurt_stable_counts():
    tau = 5
    threshold = 0.02
    f_fine = np.array([0, 0, 1, 1, 2, 2])
    f_coarse = np.array([0, 0, 0, 0, 1, 1])

    # Strong A<->B mixing relative to tau: AB stable as a whole, A/B not stable separately.
    P = three_block_chain(
        eps_ab=0.05, eps_toC=0.001, eps_fromC=0.0005, p_switch=0.35
    )

    stab_coarse = prototype_stabilities(P, tau, f_coarse)
    stab_fine = prototype_stabilities(P, tau, f_fine)

    stable_count_coarse = sum(s <= threshold for s in stab_coarse)
    stable_count_fine = sum(s <= threshold for s in stab_fine)

    assert stable_count_fine < stable_count_coarse
