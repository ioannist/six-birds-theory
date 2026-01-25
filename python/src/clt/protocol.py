from __future__ import annotations

import numpy as np

from clt.markov import validate_transition_matrix


def pair_mix_kernel(n: int, i: int, j: int, a: float) -> np.ndarray:
    """Kernel that mixes only states i and j with probability a."""
    if not (0.0 <= a <= 1.0):
        raise ValueError("a must be in [0,1]")
    if not (0 <= i < n and 0 <= j < n):
        raise ValueError("indices out of range")
    if i == j:
        raise ValueError("i and j must be distinct")
    K = np.eye(n)
    K[i, i] = 1.0 - a
    K[i, j] = a
    K[j, j] = 1.0 - a
    K[j, i] = a
    return K


def uniform_jump_kernel(pi: np.ndarray) -> np.ndarray:
    """Kernel with all rows equal to pi."""
    if pi.ndim != 1:
        raise ValueError("pi must be 1D")
    if not np.isclose(pi.sum(), 1.0, atol=1e-12):
        raise ValueError("pi must sum to 1")
    return np.tile(pi, (pi.shape[0], 1))


def make_positive_reversible_pair(
    n: int, a: float, b: float, delta: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Construct a positive reversible pair (K0, K1) with uniform pi."""
    if not (0.0 <= delta <= 1.0):
        raise ValueError("delta must be in [0,1]")
    pi = np.ones(n) / n
    A = pair_mix_kernel(n, 0, 1, a)
    B = pair_mix_kernel(n, 1, 2, b)
    J = uniform_jump_kernel(pi)
    K0 = (1.0 - delta) * A + delta * J
    K1 = (1.0 - delta) * B + delta * J
    return pi, K0, K1


def external_stroboscopic(K0: np.ndarray, K1: np.ndarray) -> np.ndarray:
    """External schedule: fixed order K1 @ K0."""
    return K1 @ K0


def autonomous_stroboscopic(K0: np.ndarray, K1: np.ndarray, alpha: float) -> np.ndarray:
    """Autonomous phase mix: R(alpha) = M0 @ M1."""
    if not (0.0 <= alpha <= 1.0):
        raise ValueError("alpha must be in [0,1]")
    M0 = alpha * K0 + (1.0 - alpha) * K1
    M1 = alpha * K1 + (1.0 - alpha) * K0
    return M0 @ M1


def phase_flip_chain(K0: np.ndarray, K1: np.ndarray, alpha: float) -> np.ndarray:
    """Phase-augmented chain on X x {0,1} with flip each step."""
    if K0.shape != K1.shape or K0.ndim != 2:
        raise ValueError("K0 and K1 must be matching square matrices")
    if not (0.0 <= alpha <= 1.0):
        raise ValueError("alpha must be in [0,1]")
    n = K0.shape[0]
    M0 = alpha * K0 + (1.0 - alpha) * K1
    M1 = alpha * K1 + (1.0 - alpha) * K0
    P = np.zeros((2 * n, 2 * n))
    for x in range(n):
        for y in range(n):
            P[2 * x + 0, 2 * y + 1] = M0[x, y]
            P[2 * x + 1, 2 * y + 0] = M1[x, y]
    return P


def phase_flip_stationary(pi_x: np.ndarray) -> np.ndarray:
    """Stationary distribution for the phase-flip chain (unbiased)."""
    if pi_x.ndim != 1:
        raise ValueError("pi_x must be 1D")
    if not np.isclose(pi_x.sum(), 1.0, atol=1e-12):
        raise ValueError("pi_x must sum to 1")
    return np.repeat(pi_x / 2.0, 2)


def kron_stationary(pi_x: np.ndarray, s_phi: np.ndarray) -> np.ndarray:
    """Product stationary distribution on X x Phi (x-major order)."""
    if pi_x.ndim != 1 or s_phi.ndim != 1:
        raise ValueError("pi_x and s_phi must be 1D")
    if not np.isclose(pi_x.sum(), 1.0, atol=1e-12):
        raise ValueError("pi_x must sum to 1")
    if not np.isclose(s_phi.sum(), 1.0, atol=1e-12):
        raise ValueError("s_phi must sum to 1")
    return np.kron(pi_x, s_phi)


def random_scan_protocol_kernel(
    Ks: list[np.ndarray],
    S: np.ndarray,
    *,
    p_phase: float = 0.5,
) -> np.ndarray:
    """Autonomous protocol on X x Phi via random-scan updates."""
    if not (0.0 <= p_phase <= 1.0):
        raise ValueError("p_phase must be in [0,1]")
    if S.ndim != 2 or S.shape[0] != S.shape[1]:
        raise ValueError("S must be square")
    m = S.shape[0]
    if len(Ks) != m:
        raise ValueError("Ks length must match number of phases")
    validate_transition_matrix(S)
    n = Ks[0].shape[0]
    for K in Ks:
        if K.ndim != 2 or K.shape[0] != K.shape[1]:
            raise ValueError("Each K must be square")
        if K.shape[0] != n:
            raise ValueError("All K must have the same size")
        validate_transition_matrix(K)

    PZ = np.zeros((n * m, n * m), dtype=float)
    for x in range(n):
        for phi in range(m):
            row = x * m + phi
            for phi2 in range(m):
                col = x * m + phi2
                PZ[row, col] += p_phase * S[phi, phi2]
            Kphi = Ks[phi]
            for y in range(n):
                col = y * m + phi
                PZ[row, col] += (1.0 - p_phase) * Kphi[x, y]
    return PZ


def is_stationary(P: np.ndarray, mu: np.ndarray, *, tol: float = 1e-10) -> bool:
    """Check whether mu is stationary for P within tolerance."""
    if mu.ndim != 1 or mu.shape[0] != P.shape[0]:
        raise ValueError("mu must be 1D and match P")
    return np.linalg.norm(mu @ P - mu, ord=1) <= tol
