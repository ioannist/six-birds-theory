import numpy as np

from clt.bridge_kernels import (
    convolve_causal,
    energy,
    kernel_mass,
    positive_work,
    truncate_window,
)


def _example_kernel() -> np.ndarray:
    K = np.zeros((5, 2, 2), dtype=float)
    K[0] = np.array([[0.20, -0.10], [0.05, 0.15]])
    K[1] = np.array([[0.05, 0.02], [-0.01, 0.04]])
    K[2] = np.array([[0.03, -0.02], [0.01, 0.02]])
    K[3] = np.array([[0.01, 0.00], [0.00, 0.01]])
    K[4] = np.array([[0.005, -0.003], [0.002, 0.004]])
    return K


def _example_signal(T: int = 30) -> np.ndarray:
    t = np.arange(T, dtype=float)
    u = np.zeros((T, 2), dtype=float)
    u[:, 0] = np.sin(0.2 * t) + 0.1 * (t % 5 == 0)
    u[:, 1] = np.cos(0.17 * t) - 0.08 * (t % 7 == 0)
    return u


def test_finite_memory_mass_bound_truncated_inputs() -> None:
    K = _example_kernel()
    u = _example_signal()
    M = kernel_mass(K)
    windows = [(0, 4), (3, 9), (5, 14), (10, 20), (18, 29)]
    tol = 1e-10
    max_slack = -1.0
    for s, t in windows:
        u_tr = truncate_window(u, s, t)
        y_tr = convolve_causal(K, u_tr)
        Wpos = positive_work(u_tr, y_tr, s, t)
        E = energy(u_tr, s, t)
        max_slack = max(max_slack, Wpos - M * E)
        assert Wpos <= (M + tol) * E + tol
    assert max_slack <= tol


def test_parallel_sum_additivity_witness() -> None:
    K1 = _example_kernel()
    K2 = 0.7 * _example_kernel()
    K2[0] += np.array([[0.03, 0.00], [-0.02, 0.01]])
    K = K1 + K2

    u = _example_signal()
    windows = [(2, 8), (12, 25)]
    tol = 1e-10
    M1 = kernel_mass(K1)
    M2 = kernel_mass(K2)
    max_slack = -1.0
    for s, t in windows:
        u_tr = truncate_window(u, s, t)
        y1 = convolve_causal(K1, u_tr)
        y2 = convolve_causal(K2, u_tr)
        y = convolve_causal(K, u_tr)
        W1 = positive_work(u_tr, y1, s, t)
        W2 = positive_work(u_tr, y2, s, t)
        W = positive_work(u_tr, y, s, t)
        E = energy(u_tr, s, t)
        max_slack = max(max_slack, W - (M1 + M2) * E)
        assert W <= W1 + W2 + tol
        assert W <= (M1 + M2 + tol) * E + tol
    assert max_slack <= tol
