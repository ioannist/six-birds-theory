from __future__ import annotations

import math

import numpy as np


def validate_transition_matrix(P: np.ndarray, tol: float = 1e-12) -> None:
    """Validate that P is row-stochastic with nonnegative entries."""
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("P must be a square 2D array")
    if np.any(P < -tol):
        raise ValueError("P has negative entries")
    row_sums = P.sum(axis=1)
    if not np.allclose(row_sums, 1.0, atol=tol, rtol=0.0):
        raise ValueError("Rows of P must sum to 1")


def normalize_rows(P: np.ndarray) -> np.ndarray:
    """Return a row-normalized copy of P."""
    if P.ndim != 2:
        raise ValueError("P must be 2D")
    row_sums = P.sum(axis=1)
    if np.any(row_sums <= 0.0):
        raise ValueError("All rows must have positive sum to normalize")
    return P / row_sums[:, None]


def _stationary_distribution_power(
    P: np.ndarray,
    *,
    tol: float,
    max_iter: int,
    init: np.ndarray | None,
) -> tuple[np.ndarray, bool]:
    """Power iteration estimate and convergence flag."""
    validate_transition_matrix(P, tol=tol)
    n = P.shape[0]
    if init is None:
        mu = np.full(n, 1.0 / n, dtype=float)
    else:
        mu = np.array(init, dtype=float)
        if mu.shape != (n,):
            raise ValueError("init must be a 1D array matching P")
        if np.any(mu < 0.0):
            raise ValueError("init must be nonnegative")
        if mu.sum() <= 0.0:
            raise ValueError("init must have positive mass")
        mu = mu / mu.sum()
    converged = False
    for _ in range(max_iter):
        mu_next = mu @ P
        if np.linalg.norm(mu_next - mu, ord=1) <= tol:
            mu = mu_next
            converged = True
            break
        mu = mu_next
    mu = np.maximum(mu, 0.0)
    if mu.sum() > 0.0:
        mu = mu / mu.sum()
    else:
        mu = np.full(n, 1.0 / n, dtype=float)
    return mu, converged


def _svd_stationary(P: np.ndarray) -> np.ndarray:
    """Return a stationary distribution via SVD nullspace."""
    n = P.shape[0]
    A = P.T - np.eye(n)
    _, _, Vt = np.linalg.svd(A)
    v = Vt[-1]
    if v.sum() < 0:
        v = -v
    v = np.maximum(v, 0.0)
    if v.sum() <= 0.0:
        raise RuntimeError("SVD nullspace produced nonpositive vector")
    return v / v.sum()


def _scc(n: int, adj: list[list[int]]) -> list[list[int]]:
    index = 0
    indices = [-1] * n
    lowlink = [0] * n
    stack: list[int] = []
    on_stack = [False] * n
    comps: list[list[int]] = []

    def strongconnect(v: int) -> None:
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in adj[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            comp: list[int] = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)
    return comps


def stationary_distribution_solve(
    P: np.ndarray,
    *,
    tol: float = 1e-12,
    threshold: float = 0.0,
    init: np.ndarray | None = None,
) -> np.ndarray:
    """Compute a stationary distribution via SVD with deterministic tie-breaks."""
    validate_transition_matrix(P, tol=tol)
    n = P.shape[0]
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if P[i, j] > threshold:
                adj[i].append(j)
    comps = _scc(n, adj)
    recurrent: list[list[int]] = []
    for comp in comps:
        closed = True
        comp_set = set(comp)
        for i in comp:
            for j in adj[i]:
                if j not in comp_set:
                    closed = False
                    break
            if not closed:
                break
        if closed:
            recurrent.append(comp)
    recurrent.sort(key=lambda c: c[0])

    if init is None:
        init_vec = np.full(n, 1.0 / n, dtype=float)
    else:
        init_vec = np.array(init, dtype=float)
        if init_vec.shape != (n,):
            raise ValueError("init must be a 1D array matching P")
        if np.any(init_vec < 0.0):
            raise ValueError("init must be nonnegative")
        if init_vec.sum() <= 0.0:
            raise ValueError("init must have positive mass")
        init_vec = init_vec / init_vec.sum()

    recurrent_states = [i for comp in recurrent for i in comp]
    transient_states = [i for i in range(n) if i not in set(recurrent_states)]

    weights_state = np.zeros(len(recurrent_states), dtype=float)
    if transient_states:
        Q = P[np.ix_(transient_states, transient_states)]
        Rmat = P[np.ix_(transient_states, recurrent_states)]
        Nmat = np.linalg.inv(np.eye(Q.shape[0]) - Q)
        init_T = init_vec[transient_states]
        init_R = init_vec[recurrent_states]
        weights_state = init_R + init_T @ Nmat @ Rmat
    else:
        weights_state = init_vec[recurrent_states]

    weights_per_class: list[float] = []
    state_to_pos = {s: i for i, s in enumerate(recurrent_states)}
    for comp in recurrent:
        weight = 0.0
        for s in comp:
            weight += weights_state[state_to_pos[s]]
        weights_per_class.append(weight)

    total_weight = sum(weights_per_class)
    if total_weight <= 0.0:
        weights_per_class = [1.0 / len(recurrent) for _ in recurrent]
    else:
        weights_per_class = [w / total_weight for w in weights_per_class]

    pi = np.zeros(n, dtype=float)
    for weight, comp in zip(weights_per_class, recurrent):
        sub = P[np.ix_(comp, comp)]
        pi_comp = _svd_stationary(sub)
        for idx, state in enumerate(comp):
            pi[state] += weight * pi_comp[idx]

    pi = np.maximum(pi, 0.0)
    if pi.sum() <= 0.0:
        raise RuntimeError("Failed to construct stationary distribution")
    pi = pi / pi.sum()
    residual = np.linalg.norm(pi @ P - pi, ord=1)
    if residual > 1e-9:
        raise RuntimeError("Stationary solve failed to meet residual tolerance")
    return pi


def stationary_distribution_cesaro(
    P: np.ndarray,
    *,
    n_steps: int = 50_000,
    init: np.ndarray | None = None,
) -> np.ndarray:
    """Cesaro-averaged stationary estimate for periodic chains."""
    validate_transition_matrix(P)
    if n_steps <= 0:
        raise ValueError("n_steps must be positive")
    n = P.shape[0]
    if init is None:
        mu = np.full(n, 1.0 / n, dtype=float)
    else:
        mu = np.array(init, dtype=float)
        if mu.shape != (n,):
            raise ValueError("init must be a 1D array matching P")
        if np.any(mu < 0.0):
            raise ValueError("init must be nonnegative")
        if mu.sum() <= 0.0:
            raise ValueError("init must have positive mass")
        mu = mu / mu.sum()
    acc = np.zeros(n, dtype=float)
    for _ in range(n_steps):
        acc += mu
        mu = mu @ P
    pi = acc / n_steps
    pi = np.maximum(pi, 0.0)
    if pi.sum() <= 0.0:
        raise RuntimeError("Cesaro averaging produced nonpositive vector")
    return pi / pi.sum()


def stationary_distribution(
    P: np.ndarray,
    *,
    tol: float = 1e-12,
    max_iter: int = 1_000_000,
    init: np.ndarray | None = None,
    on_fail: str = "solve",
) -> np.ndarray:
    """Compute a stationary distribution with a selectable fallback policy."""
    mu, converged = _stationary_distribution_power(
        P, tol=tol, max_iter=max_iter, init=init
    )
    if converged:
        return mu
    if on_fail == "raise":
        raise RuntimeError(
            "power iteration did not converge; chain may be periodic/reducible; "
            "use stationary_distribution_solve or stationary_distribution_cesaro; "
            "consider specifying init"
        )
    if on_fail == "solve":
        return stationary_distribution_solve(P, tol=tol, init=init)
    if on_fail == "cesaro":
        return stationary_distribution_cesaro(P, init=init)
    raise ValueError("on_fail must be one of {'raise','solve','cesaro'}")


def time_reversal(P: np.ndarray, pi: np.ndarray, *, tol: float = 1e-12) -> np.ndarray:
    """Return the time-reversed kernel with respect to pi."""
    validate_transition_matrix(P, tol=tol)
    if pi.ndim != 1 or pi.shape[0] != P.shape[0]:
        raise ValueError("pi must be a 1D array matching P")
    if np.any(pi <= tol):
        raise ValueError("pi must be strictly positive for time reversal")
    numerator = (pi[None, :] * P.T)
    P_rev = numerator / pi[:, None]
    validate_transition_matrix(P_rev, tol=tol)
    return P_rev


def _rev_support_violations(
    P: np.ndarray, pi: np.ndarray, *, tol_flow: float
) -> list[tuple[int, int]]:
    """Return directed edges with forward flow but zero reverse flow."""
    n = P.shape[0]
    violations: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            flow = pi[i] * P[i, j]
            if flow > tol_flow:
                rev_flow = pi[j] * P[j, i]
                if rev_flow <= tol_flow:
                    violations.append((i, j))
    return violations


def entropy_production_rate(
    P: np.ndarray, pi: np.ndarray, *, tol: float = 1e-15
) -> float:
    """Compute discrete-time entropy production rate on REV support."""
    validate_transition_matrix(P, tol=tol)
    if pi.ndim != 1 or pi.shape[0] != P.shape[0]:
        raise ValueError("pi must be a 1D array matching P")
    if np.any(pi <= tol):
        raise ValueError("pi must be strictly positive")
    violations = _rev_support_violations(P, pi, tol_flow=tol)
    if violations:
        return float("inf")
    n = P.shape[0]
    sigma = 0.0
    for i in range(n):
        for j in range(n):
            if P[i, j] > tol:
                num = pi[i] * P[i, j]
                den = pi[j] * P[j, i]
                sigma += num * math.log(num / den)
    return float(sigma)


def compose_kernels(kernels: list[np.ndarray]) -> np.ndarray:
    """Return the composite kernel K = kernels[-1] @ ... @ kernels[0]."""
    if not kernels:
        raise ValueError("kernels must be non-empty")
    K = kernels[0]
    for k in kernels[1:]:
        if k.shape != K.shape:
            raise ValueError("All kernels must have matching shapes")
    K = kernels[-1].copy()
    for k in reversed(kernels[:-1]):
        K = K @ k
    return K
