"""Discrete-time witnesses for finite-memory ICAP bounds.

These utilities implement causal convolution bridges on a finite horizon and
verify the mass-bound ICAP inequality on truncated inputs. They are intended
as deterministic numerical witnesses for the continuous-time lemma.
"""

from __future__ import annotations

import numpy as np


def opnorm(A: np.ndarray) -> float:
    """Return the spectral/operator 2-norm of a matrix."""
    A = np.asarray(A, dtype=float)
    if A.ndim != 2:
        raise ValueError("opnorm expects a 2D array")
    svals = np.linalg.svd(A, compute_uv=False)
    return float(svals[0]) if svals.size else 0.0


def kernel_mass(K: np.ndarray) -> float:
    """Return M = sum_k ||K[k]||_op for a kernel K with shape (L, d, d)."""
    K = np.asarray(K, dtype=float)
    if K.ndim != 3:
        raise ValueError("kernel_mass expects a 3D array of shape (L, d, d)")
    return float(sum(opnorm(K[k]) for k in range(K.shape[0])))


def truncate_window(u: np.ndarray, s: int, t: int) -> np.ndarray:
    """Zero out a signal outside the inclusive window [s, t]."""
    u = np.asarray(u, dtype=float)
    if u.ndim != 2:
        raise ValueError("truncate_window expects a 2D array of shape (T, d)")
    if s < 0 or t < 0 or s > t or t >= u.shape[0]:
        raise ValueError("invalid window [s, t] for input length")
    out = np.zeros_like(u)
    out[s : t + 1] = u[s : t + 1]
    return out


def convolve_causal(K: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Compute y[t] = sum_{k=0}^{min(t, L-1)} K[k] u[t-k]."""
    K = np.asarray(K, dtype=float)
    u = np.asarray(u, dtype=float)
    if K.ndim != 3 or u.ndim != 2:
        raise ValueError("convolve_causal expects K:(L,d,d) and u:(T,d)")
    L, d1, d2 = K.shape
    T, d = u.shape
    if d1 != d2 or d2 != d:
        raise ValueError("kernel and input dimensions are incompatible")
    y = np.zeros((T, d), dtype=float)
    for t in range(T):
        kmax = min(t, L - 1)
        acc = np.zeros(d, dtype=float)
        for k in range(kmax + 1):
            acc += K[k] @ u[t - k]
        y[t] = acc
    return y


def positive_work(u: np.ndarray, y: np.ndarray, s: int, t: int) -> float:
    """Sum max(0, <u[t], y[t]>) over t in the inclusive window [s, t]."""
    u = np.asarray(u, dtype=float)
    y = np.asarray(y, dtype=float)
    if u.shape != y.shape or u.ndim != 2:
        raise ValueError("positive_work expects matching (T, d) arrays")
    if s < 0 or t < 0 or s > t or t >= u.shape[0]:
        raise ValueError("invalid window [s, t] for input length")
    wpos = 0.0
    for i in range(s, t + 1):
        wpos += max(0.0, float(np.dot(u[i], y[i])))
    return float(wpos)


def energy(u: np.ndarray, s: int, t: int) -> float:
    """Sum ||u[t]||^2 over t in the inclusive window [s, t]."""
    u = np.asarray(u, dtype=float)
    if u.ndim != 2:
        raise ValueError("energy expects a 2D array of shape (T, d)")
    if s < 0 or t < 0 or s > t or t >= u.shape[0]:
        raise ValueError("invalid window [s, t] for input length")
    return float(np.sum(u[s : t + 1] ** 2))


def icap_slack_mass_bound(K: np.ndarray, u: np.ndarray, s: int, t: int) -> float:
    """Return M*E - Wpos for truncated inputs, using the kernel mass bound."""
    u_tr = truncate_window(u, s, t)
    y_tr = convolve_causal(K, u_tr)
    M = kernel_mass(K)
    E = energy(u_tr, s, t)
    Wpos = positive_work(u_tr, y_tr, s, t)
    return float(M * E - Wpos)
