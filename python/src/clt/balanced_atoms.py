"""Balanced-atom kernels and ICAP ratio witnesses."""

from __future__ import annotations

import numpy as np

from clt.bridge_kernels import convolve_causal, energy, kernel_mass, positive_work, truncate_window


def exp_decay_kernel(dt: float, L: int, lam: float, gain: float, d: int = 1) -> np.ndarray:
    """Return K[k] = dt * gain * exp(-lam * k * dt) * I_d, shape (L, d, d)."""
    if dt <= 0 or L <= 0 or lam <= 0 or d <= 0:
        raise ValueError("dt, L, lam, d must be positive")
    K = np.zeros((L, d, d), dtype=float)
    for k in range(L):
        coeff = dt * gain * np.exp(-lam * k * dt)
        K[k] = coeff * np.eye(d)
    return K


def icap_ratio(K: np.ndarray, u: np.ndarray, s: int, t: int) -> float:
    """Return Wpos/E for truncated inputs on window [s, t]."""
    u_tr = truncate_window(u, s, t)
    y_tr = convolve_causal(K, u_tr)
    Wpos = positive_work(u_tr, y_tr, s, t)
    E = energy(u_tr, s, t)
    return float(Wpos / E) if E > 0 else 0.0


def max_icap_ratio_over_windows(K: np.ndarray, u: np.ndarray, windows: list[tuple[int, int]]) -> float:
    """Return max Wpos/E over a list of windows."""
    ratios = [icap_ratio(K, u, s, t) for (s, t) in windows]
    return float(max(ratios)) if ratios else 0.0


def kernel_mass_approx(K: np.ndarray) -> float:
    """Return the discrete kernel mass via operator-norm sum."""
    return float(kernel_mass(K))
