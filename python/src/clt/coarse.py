from __future__ import annotations

import numpy as np


def pushforward_dist(
    mu: np.ndarray, f: list[int] | np.ndarray, n_out: int | None = None
) -> np.ndarray:
    """Push forward a distribution by a state map f."""
    f_arr = np.array(f, dtype=int)
    if mu.ndim != 1 or mu.shape[0] != f_arr.shape[0]:
        raise ValueError("mu and f must have compatible sizes")
    if n_out is None:
        n_out = int(f_arr.max()) + 1
    out = np.zeros(n_out, dtype=float)
    for i, p in enumerate(mu):
        out[f_arr[i]] += float(p)
    return out


def coarse_grain_kernel_stationary(
    P: np.ndarray,
    pi: np.ndarray,
    f: list[int] | np.ndarray,
    n_out: int | None = None,
) -> np.ndarray:
    """Stationary coarse-grained kernel induced by f and pi."""
    f_arr = np.array(f, dtype=int)
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    if pi.ndim != 1 or pi.shape[0] != P.shape[0]:
        raise ValueError("pi must match P")
    if n_out is None:
        n_out = int(f_arr.max()) + 1
    macro = np.zeros((n_out, n_out), dtype=float)
    for x in range(n_out):
        block_x = np.where(f_arr == x)[0]
        if block_x.size == 0:
            raise ValueError("Empty macro block")
        pi_block = pi[block_x].sum()
        if pi_block <= 0.0:
            raise ValueError("Zero stationary mass on a block")
        weights = pi[block_x] / pi_block
        for y in range(n_out):
            block_y = np.where(f_arr == y)[0]
            if block_y.size == 0:
                raise ValueError("Empty macro block")
            total = 0.0
            for i_idx, i in enumerate(block_x):
                total += weights[i_idx] * P[i, block_y].sum()
            macro[x, y] = total
    return macro
