import numpy as np

from clt.empirical_closure import proj_uniform


def test_absorption_refinement_projection():
    f_fine = np.array([0, 0, 1, 1, 2, 2])
    f_coarse = np.array([0, 0, 0, 0, 1, 1])

    mus = []
    for z in range(6):
        mu = np.zeros(6)
        mu[z] = 1.0
        mus.append(mu)
    mus.append(np.ones(6) / 6.0)

    for mu in mus:
        left = proj_uniform(proj_uniform(mu, f_fine), f_coarse)
        right = proj_uniform(mu, f_coarse)
        assert np.allclose(left, right, atol=1e-12)
