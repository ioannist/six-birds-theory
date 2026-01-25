from __future__ import annotations

import numpy as np

from clt.graph import fundamental_cycle_basis, spanning_forest


def bidirected_support_edges(
    P: np.ndarray, *, threshold: float = 0.0
) -> set[frozenset[int]]:
    """Undirected edges where both directions have positive weight."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    n = P.shape[0]
    edges: set[frozenset[int]] = set()
    for i in range(n):
        for j in range(i + 1, n):
            if P[i, j] > threshold and P[j, i] > threshold:
                edges.add(frozenset({i, j}))
    return edges


def edge_one_form(P: np.ndarray, *, threshold: float = 0.0) -> np.ndarray:
    """Antisymmetric log-ratio 1-form on bidirected support."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    n = P.shape[0]
    a = np.full((n, n), np.nan, dtype=float)
    edges = bidirected_support_edges(P, threshold=threshold)
    for e in edges:
        i, j = tuple(e)
        val = float(np.log(P[i, j] / P[j, i]))
        a[i, j] = val
        a[j, i] = -val
    return a


def fundamental_cycle_basis_from_P(
    P: np.ndarray, *, threshold: float = 0.0
) -> list[list[int]]:
    """Fundamental cycle basis on the bidirected support graph."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    n = P.shape[0]
    edges = bidirected_support_edges(P, threshold=threshold)
    forest = spanning_forest(n, edges)
    return fundamental_cycle_basis(n, edges, forest)


def cycle_integral(a: np.ndarray, cycle: list[int]) -> float:
    """Sum a[i,j] along a closed cycle list."""
    if len(cycle) < 2:
        return 0.0
    total = 0.0
    if cycle[0] == cycle[-1]:
        end = len(cycle) - 1
    else:
        end = len(cycle) - 1
    for t in range(end):
        i = cycle[t]
        j = cycle[t + 1]
        val = a[i, j]
        if np.isnan(val):
            raise ValueError("cycle uses edge outside bidirected support")
        total += float(val)
    if cycle[0] != cycle[-1]:
        i = cycle[-1]
        j = cycle[0]
        val = a[i, j]
        if np.isnan(val):
            raise ValueError("cycle uses edge outside bidirected support")
        total += float(val)
    return total


def cycle_affinities(
    P: np.ndarray, *, threshold: float = 0.0
) -> tuple[list[list[int]], np.ndarray]:
    """Return basis cycles and their 1-form integrals."""
    cycles = fundamental_cycle_basis_from_P(P, threshold=threshold)
    a = edge_one_form(P, threshold=threshold)
    A = np.array([cycle_integral(a, c) for c in cycles], dtype=float)
    return cycles, A


def solve_potential_if_exact(
    P: np.ndarray, *, threshold: float = 0.0, tol: float = 1e-10
) -> tuple[np.ndarray, bool]:
    """Solve a = dPhi on each component if the 1-form is exact."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    n = P.shape[0]
    edges = bidirected_support_edges(P, threshold=threshold)
    adj: list[list[int]] = [[] for _ in range(n)]
    for e in edges:
        u, v = tuple(e)
        adj[u].append(v)
        adj[v].append(u)

    phi = np.full(n, np.nan, dtype=float)
    for root in range(n):
        if not np.isnan(phi[root]):
            continue
        phi[root] = 0.0
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if np.isnan(phi[v]):
                    phi[v] = phi[u] + float(np.log(P[u, v] / P[v, u]))
                    stack.append(v)

    ok = True
    for e in edges:
        i, j = tuple(e)
        diff = phi[j] - phi[i]
        target = float(np.log(P[i, j] / P[j, i]))
        if abs(diff - target) > tol:
            ok = False
            break
    return phi, ok


def is_exact_one_form(
    P: np.ndarray, *, threshold: float = 0.0, tol: float = 1e-10
) -> bool:
    """Return True if the bidirected 1-form is exact."""
    _, ok = solve_potential_if_exact(P, threshold=threshold, tol=tol)
    return ok
