from __future__ import annotations

from collections import deque

import numpy as np


def support_graph_edges(
    P: np.ndarray, *, threshold: float = 0.0
) -> set[frozenset[int]]:
    """Undirected support graph from a transition matrix."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be square")
    n = P.shape[0]
    edges: set[frozenset[int]] = set()
    for i in range(n):
        for j in range(i + 1, n):
            if P[i, j] > threshold or P[j, i] > threshold:
                edges.add(frozenset({i, j}))
    return edges


def connected_components(n: int, edges: set[frozenset[int]]) -> list[set[int]]:
    """Return connected components as sets of vertices."""
    adj = {i: set() for i in range(n)}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    seen: set[int] = set()
    comps: list[set[int]] = []
    for i in range(n):
        if i in seen:
            continue
        comp: set[int] = set()
        queue = deque([i])
        seen.add(i)
        while queue:
            u = queue.popleft()
            comp.add(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        comps.append(comp)
    return comps


def cycle_rank_beta1(n: int, edges: set[frozenset[int]]) -> int:
    """Cycle rank beta_1 = |E| - |V| + #components."""
    comps = connected_components(n, edges)
    return len(edges) - n + len(comps)


def spanning_forest(n: int, edges: set[frozenset[int]]) -> set[frozenset[int]]:
    """Construct any spanning forest."""
    adj = {i: set() for i in range(n)}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    forest: set[frozenset[int]] = set()
    seen: set[int] = set()
    for start in range(n):
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    forest.add(frozenset({u, v}))
                    queue.append(v)
    return forest


def _path_in_forest(
    n: int, forest: set[frozenset[int]], start: int, goal: int
) -> list[int]:
    adj = {i: set() for i in range(n)}
    for e in forest:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    queue = deque([start])
    parent = {start: None}
    while queue:
        u = queue.popleft()
        if u == goal:
            break
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    if goal not in parent:
        raise ValueError("No path in forest")
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def fundamental_cycle_basis(
    n: int, edges: set[frozenset[int]], forest: set[frozenset[int]]
) -> list[list[int]]:
    """Return a basis of cycles from non-forest edges."""
    cycles: list[list[int]] = []
    for e in edges:
        if e in forest:
            continue
        u, v = tuple(e)
        path = _path_in_forest(n, forest, u, v)
        cycle = path + [u]
        cycles.append(cycle)
    return cycles


def erdos_renyi_edges(
    n: int, p: float, rng: np.random.Generator
) -> set[frozenset[int]]:
    """Sample an undirected Erdos-Renyi G(n,p) edge set (no loops)."""
    if not (0.0 <= p <= 1.0):
        raise ValueError("p must be in [0,1]")
    edges: set[frozenset[int]] = set()
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                edges.add(frozenset({i, j}))
    return edges


def lazy_random_walk_matrix(
    n: int, edges: set[frozenset[int]], lazy: float = 0.5
) -> np.ndarray:
    """Lazy random walk matrix on an undirected graph (row-stochastic)."""
    if not (0.0 <= lazy <= 1.0):
        raise ValueError("lazy must be in [0,1]")
    adj = [set() for _ in range(n)]
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    P = np.zeros((n, n), dtype=float)
    for i in range(n):
        if not adj[i]:
            P[i, i] = 1.0
            continue
        P[i, i] = lazy
        weight = (1.0 - lazy) / len(adj[i])
        for j in adj[i]:
            P[i, j] = weight
    return P


def spectral_gap_lazy_rw(
    n: int, edges: set[frozenset[int]], lazy: float = 0.5
) -> float:
    """Spectral gap proxy via symmetric similarity transform."""
    if n < 2:
        return 0.0
    if not (0.0 <= lazy <= 1.0):
        raise ValueError("lazy must be in [0,1]")
    A = np.zeros((n, n), dtype=float)
    for e in edges:
        u, v = tuple(e)
        A[u, v] = 1.0
        A[v, u] = 1.0
    deg = A.sum(axis=1)
    deg_safe = np.where(deg > 0.0, deg, 1.0)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(deg_safe))
    S = lazy * np.eye(n) + (1.0 - lazy) * D_inv_sqrt @ A @ D_inv_sqrt
    evals = np.linalg.eigvalsh(S)[::-1]
    gap = 1.0 - float(evals[1])
    if gap < 0.0:
        gap = 0.0
    if gap > 1.0:
        gap = 1.0
    return gap
