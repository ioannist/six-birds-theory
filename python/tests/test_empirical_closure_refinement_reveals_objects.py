import numpy as np

from clt.empirical_closure import prototype_stabilities, three_block_chain


def test_refinement_reveals_more_stable_objects():
    tau = 5
    f_fine = np.array([0, 0, 1, 1, 2, 2])
    f_coarse = np.array([0, 0, 0, 0, 1, 1])

    P_small = three_block_chain(
        eps_ab=2e-4, eps_toC=2e-3, eps_fromC=1e-3, p_switch=0.35
    )

    stab_coarse = prototype_stabilities(P_small, tau, f_coarse)
    stab_fine = prototype_stabilities(P_small, tau, f_fine)

    thresh = 0.02
    assert sum(s <= thresh for s in stab_coarse) == 2
    assert sum(s <= thresh for s in stab_fine) == 3
    assert len(stab_fine) > len(stab_coarse)
