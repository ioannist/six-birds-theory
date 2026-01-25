import numpy as np

from clt.acc import cycle_affinities, is_exact_one_form, solve_potential_if_exact


def test_reversible_non_symmetric_exact_one_form():
    pi = np.array([0.5, 0.3, 0.2])
    F01 = 0.05
    F02 = 0.03
    F12 = 0.02

    F = np.zeros((3, 3), dtype=float)
    F[0, 1] = F[1, 0] = F01
    F[0, 2] = F[2, 0] = F02
    F[1, 2] = F[2, 1] = F12
    for i in range(3):
        F[i, i] = pi[i] - F[i].sum()

    P = np.zeros((3, 3), dtype=float)
    for i in range(3):
        P[i, :] = F[i, :] / pi[i]

    cycles, A = cycle_affinities(P)
    assert np.allclose(A, 0.0, atol=1e-10)

    phi, ok = solve_potential_if_exact(P)
    assert ok is True
    phi0 = phi - phi[0]
    log_pi = np.log(pi) - np.log(pi[0])
    assert np.max(np.abs(phi0 - log_pi)) <= 1e-8


def test_biased_cycle_non_exact_affinity():
    p = 0.7
    q = 0.2
    s = 0.1
    P = np.array(
        [
            [s, p, q],
            [q, s, p],
            [p, q, s],
        ]
    )
    cycles, A = cycle_affinities(P)
    assert len(cycles) == 1
    expected = 3.0 * np.log(p / q)
    assert abs(abs(A[0]) - expected) <= 1e-10

    _, ok = solve_potential_if_exact(P)
    assert ok is False
    assert is_exact_one_form(P) is False
