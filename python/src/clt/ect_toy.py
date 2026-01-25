"""Toy family witnesses for linear mode count and linear capacity growth."""

from __future__ import annotations

import numpy as np

from clt.bridge_kernels import kernel_mass


def make_atom_kernel(L: int = 3, d: int = 2) -> np.ndarray:
    """Return a fixed finite-memory kernel for one atom, shape (L, d, d)."""
    K = np.zeros((L, d, d), dtype=float)
    K[0] = np.array([[0.20, -0.10], [0.05, 0.15]])
    if L > 1:
        K[1] = np.array([[0.05, 0.02], [-0.01, 0.04]])
    if L > 2:
        K[2] = np.array([[0.03, -0.02], [0.01, 0.02]])
    for k in range(3, L):
        scale = 0.01 / (k + 1)
        K[k] = np.array([[scale, 0.0], [0.0, scale]])
    return K


def make_sector_kernels(j: int, *, L: int = 3, d: int = 2) -> list[np.ndarray]:
    """Return a list of (j+1) identical atom kernels (parallel-sum witness)."""
    if j < 0:
        raise ValueError("j must be nonnegative")
    atom = make_atom_kernel(L=L, d=d)
    return [atom.copy() for _ in range(j + 1)]


def icap_mass_constant(K: np.ndarray) -> float:
    """Return M = sum_k ||K[k]||_op, the ICAP mass bound for a kernel."""
    return float(kernel_mass(K))


def cap_bound_linear(j: int, Lambda0: float) -> float:
    """Return the linear capacity bound Lambda0 * (j+1)."""
    if j < 0:
        raise ValueError("j must be nonnegative")
    return float(Lambda0 * (j + 1))


def harmonic_partial_sum(J: int, Lambda0: float) -> float:
    """Return sum_{j=0..J} 1/(Lambda0*(j+1))."""
    if J < 0:
        raise ValueError("J must be nonnegative")
    return float(sum(1.0 / (Lambda0 * (j + 1)) for j in range(J + 1)))
