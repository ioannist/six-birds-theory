from __future__ import annotations

import itertools
import math
from typing import Callable

import numpy as np


def _as_kernel_list(Ps: np.ndarray | list[np.ndarray], T: int) -> list[np.ndarray]:
    if isinstance(Ps, np.ndarray):
        return [Ps] * T
    if len(Ps) != T:
        raise ValueError("Length of kernel list must match T")
    return Ps


def path_probability(
    Ps: np.ndarray | list[np.ndarray], init: np.ndarray, path: tuple[int, ...]
) -> float:
    """Probability of a specific path (x0,...,xT)."""
    if len(path) == 0:
        raise ValueError("Path must have at least one state")
    T = len(path) - 1
    kernels = _as_kernel_list(Ps, T)
    prob = float(init[path[0]])
    for t in range(T):
        prob *= float(kernels[t][path[t], path[t + 1]])
    return prob


def enumerate_path_law(
    Ps: np.ndarray | list[np.ndarray], init: np.ndarray, T: int
) -> dict[tuple[int, ...], float]:
    """Enumerate the path law for small systems."""
    n = init.shape[0]
    kernels = _as_kernel_list(Ps, T)
    law: dict[tuple[int, ...], float] = {}
    for path in itertools.product(range(n), repeat=T + 1):
        law[path] = path_probability(kernels, init, path)
    return law


def kl_divergence(
    p: dict[tuple[int, ...], float],
    q: dict[tuple[int, ...], float],
    *,
    tol: float = 0.0,
) -> float:
    """KL divergence over finite support; requires support(p) subset of support(q)."""
    total = 0.0
    for k, pv in p.items():
        if pv <= 0.0:
            continue
        qv = q.get(k, 0.0)
        if qv <= 0.0:
            raise ValueError("Support mismatch in KL divergence")
        if tol > 0.0:
            qv = max(qv, tol)
        total += pv * math.log(pv / qv)
    return float(total)


def reverse_path_law(
    path_law: dict[tuple[int, ...], float]
) -> dict[tuple[int, ...], float]:
    """Reverse each path, keeping probabilities."""
    rev: dict[tuple[int, ...], float] = {}
    for path, prob in path_law.items():
        rpath = tuple(reversed(path))
        rev[rpath] = rev.get(rpath, 0.0) + prob
    return rev


def pushforward_path_law(
    path_law: dict[tuple[int, ...], float], f: Callable[[int], int]
) -> dict[tuple[int, ...], float]:
    """Push forward each path through a state map f."""
    pushed: dict[tuple[int, ...], float] = {}
    for path, prob in path_law.items():
        mapped = tuple(f(x) for x in path)
        pushed[mapped] = pushed.get(mapped, 0.0) + prob
    return pushed


def arrow_path_kl(P: np.ndarray, init: np.ndarray, T: int) -> float:
    """Path-space KL between forward and reversed path laws."""
    law = enumerate_path_law(P, init, T)
    rev = reverse_path_law(law)
    return kl_divergence(law, rev)


def arrow_path_kl_coarse(
    P: np.ndarray, init: np.ndarray, T: int, f: np.ndarray
) -> float:
    """Path-space KL after coarse-graining the path law by f."""
    law = enumerate_path_law(P, init, T)
    f_arr = np.array(f, dtype=int)
    coarse = pushforward_path_law(law, lambda i: int(f_arr[i]))
    return kl_divergence(coarse, reverse_path_law(coarse))


def path_kl_forward_reverse(
    Ps: np.ndarray | list[np.ndarray], init: np.ndarray, T: int
) -> float:
    """Finite-horizon KL between forward and reversed path laws."""
    law = enumerate_path_law(Ps, init, T)
    return kl_divergence(law, reverse_path_law(law))
