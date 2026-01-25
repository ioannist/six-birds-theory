import numpy as np

from clt.markov import entropy_production_rate, stationary_distribution
from clt.protocol import (
    is_stationary,
    kron_stationary,
    pair_mix_kernel,
    random_scan_protocol_kernel,
)


def _symmetric_ring(m: int, stay: float, step: float) -> np.ndarray:
    S = np.zeros((m, m), dtype=float)
    for i in range(m):
        S[i, i] = stay
        S[i, (i + 1) % m] = step
        S[i, (i - 1) % m] = step
    return S


def _biased_ring(m: int, stay: float, forward: float, backward: float) -> np.ndarray:
    S = np.zeros((m, m), dtype=float)
    for i in range(m):
        S[i, i] = stay
        S[i, (i + 1) % m] = forward
        S[i, (i - 1) % m] = backward
    return S


def _reversible_kernel_from_flows(pi: np.ndarray, f01: float, f02: float, f12: float) -> np.ndarray:
    F = np.zeros((3, 3), dtype=float)
    F[0, 1] = F[1, 0] = f01
    F[0, 2] = F[2, 0] = f02
    F[1, 2] = F[2, 1] = f12
    for i in range(3):
        F[i, i] = pi[i] - F[i].sum()
    P = np.zeros((3, 3), dtype=float)
    for i in range(3):
        P[i, :] = F[i, :] / pi[i]
    return P


def test_mphase_unbiased_shared_pi_zero_ep():
    n = 3
    m = 4
    pi = np.ones(n) / n
    Ks = [
        pair_mix_kernel(n, 0, 1, 0.3),
        pair_mix_kernel(n, 1, 2, 0.4),
        pair_mix_kernel(n, 0, 2, 0.2),
        pair_mix_kernel(n, 0, 1, 0.1),
    ]
    S = _symmetric_ring(m, stay=0.5, step=0.25)
    PZ = random_scan_protocol_kernel(Ks, S, p_phase=0.3)

    mu = stationary_distribution(PZ)
    ep = entropy_production_rate(PZ, mu)
    assert ep <= 1e-10

    s = stationary_distribution(S)
    mu_prod = kron_stationary(pi, s)
    assert is_stationary(PZ, mu_prod, tol=1e-8)


def test_mphase_bias_shared_pi_positive_ep():
    n = 3
    m = 4
    pi = np.ones(n) / n
    Ks = [
        pair_mix_kernel(n, 0, 1, 0.3),
        pair_mix_kernel(n, 1, 2, 0.4),
        pair_mix_kernel(n, 0, 2, 0.2),
        pair_mix_kernel(n, 0, 1, 0.1),
    ]
    S = _biased_ring(m, stay=0.2, forward=0.6, backward=0.2)
    PZ = random_scan_protocol_kernel(Ks, S, p_phase=0.3)

    mu = stationary_distribution(PZ)
    ep = entropy_production_rate(PZ, mu)
    assert ep >= 1e-3


def test_mphase_no_shared_pi_product_guess_fails():
    n = 3
    m = 2
    pi0 = np.array([0.6, 0.3, 0.1])
    pi1 = np.array([0.2, 0.5, 0.3])

    K0 = _reversible_kernel_from_flows(pi0, 0.05, 0.03, 0.02)
    K1 = _reversible_kernel_from_flows(pi1, 0.04, 0.02, 0.03)

    S = np.array([[0.6, 0.4], [0.4, 0.6]])
    PZ = random_scan_protocol_kernel([K0, K1], S, p_phase=0.4)

    mu_true = stationary_distribution(PZ)
    s = stationary_distribution(S)
    mu_guess = kron_stationary(pi0, s)

    defect = np.linalg.norm(mu_guess @ PZ - mu_guess, ord=1)
    dist = np.linalg.norm(mu_true - mu_guess, ord=1)
    ep_true = entropy_production_rate(PZ, mu_true)
    ep_guess = entropy_production_rate(PZ, mu_guess)

    assert defect >= 1e-3
    assert dist >= 1e-3
    assert abs(ep_guess - ep_true) >= 1e-3
