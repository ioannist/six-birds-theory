#!/usr/bin/env python3
"""Print a compact balanced vs high-Q witness summary."""

from __future__ import annotations

import numpy as np

from clt.balanced_atoms import exp_decay_kernel, kernel_mass_approx, max_icap_ratio_over_windows


def _signal(T: int) -> np.ndarray:
    u = np.ones((T, 1), dtype=float)
    for t in range(T):
        if t % 7 == 0:
            u[t, 0] += 0.1
    return u


def main() -> None:
    T = 400
    windows = [(0, 80), (50, 180), (120, 300), (250, 399)]
    u = _signal(T)

    Lambda0 = 1.3
    K_bal = exp_decay_kernel(dt=1.0, L=250, lam=0.2, gain=Lambda0 * (1.0 - np.exp(-0.2)), d=1)
    M_bal = kernel_mass_approx(K_bal)
    ratio_bal = max_icap_ratio_over_windows(K_bal, u, windows)
    print(f\"balanced: M={M_bal:.6f}, max_ratio={ratio_bal:.6f}\")

    K_hq = exp_decay_kernel(dt=1.0, L=400, lam=0.03, gain=1.0, d=1)
    M_hq = kernel_mass_approx(K_hq)
    ratio_hq = max_icap_ratio_over_windows(K_hq, u, windows)
    print(f\"high-Q:   M={M_hq:.6f}, max_ratio={ratio_hq:.6f}\")


if __name__ == \"__main__\":  # pragma: no cover
    main()
