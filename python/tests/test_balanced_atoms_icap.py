import numpy as np

from clt.balanced_atoms import (
    exp_decay_kernel,
    icap_ratio,
    kernel_mass_approx,
    max_icap_ratio_over_windows,
)
from clt.bridge_kernels import convolve_causal, energy, positive_work, truncate_window


def _signal(T: int) -> np.ndarray:
    u = np.ones((T, 1), dtype=float)
    for t in range(T):
        if t % 7 == 0:
            u[t, 0] += 0.1
    return u


def test_balanced_case_icap_bound() -> None:
    Lambda0 = 1.3
    lam = 0.2
    gain = Lambda0 * (1.0 - np.exp(-lam))  # dt=1.0 discrete mass calibration
    dt = 1.0
    L = 250
    T = 400
    K = exp_decay_kernel(dt=dt, L=L, lam=lam, gain=gain, d=1)
    u = _signal(T)
    windows = [(0, 80), (50, 180), (120, 300), (250, 399)]
    M = kernel_mass_approx(K)
    ratio = max_icap_ratio_over_windows(K, u, windows)
    assert M <= Lambda0 + 1e-2
    assert ratio <= Lambda0 + 5e-2
    for s, t in windows:
        u_tr = truncate_window(u, s, t)
        y_tr = convolve_causal(K, u_tr)
        Wpos = positive_work(u_tr, y_tr, s, t)
        E = energy(u_tr, s, t)
        assert Wpos <= (M + 1e-10) * E + 1e-10


def test_high_q_unbalanced_inflates_constant() -> None:
    Lambda0 = 1.3
    lam = 0.03
    gain = 1.0
    dt = 1.0
    L = 400
    T = 400
    K = exp_decay_kernel(dt=dt, L=L, lam=lam, gain=gain, d=1)
    u = _signal(T)
    windows = [(0, 80), (50, 180), (120, 300), (250, 399)]
    M = kernel_mass_approx(K)
    ratio = max_icap_ratio_over_windows(K, u, windows)
    assert M >= 10.0
    assert ratio >= 10.0 * Lambda0
