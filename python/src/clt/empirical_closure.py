from __future__ import annotations

import numpy as np

from clt.markov import validate_transition_matrix
from clt.coarse import pushforward_dist

ArrayLike = np.ndarray | list[int]


def partition_sizes(f: ArrayLike) -> np.ndarray:
    """Return counts per partition cell."""
    f_arr = np.array(f, dtype=int)
    if f_arr.ndim != 1:
        raise ValueError("f must be 1D")
    if f_arr.size == 0:
        raise ValueError("f must be non-empty")
    if np.any(f_arr < 0):
        raise ValueError("f labels must be nonnegative")
    m = int(f_arr.max()) + 1
    return np.bincount(f_arr, minlength=m)


def partition_num_cells(f: ArrayLike) -> int:
    """Return the number of partition cells."""
    f_arr = np.array(f, dtype=int)
    if f_arr.size == 0:
        raise ValueError("f must be non-empty")
    return int(f_arr.max()) + 1


def coarse_grain(mu: np.ndarray, f: ArrayLike, m: int | None = None) -> np.ndarray:
    """Coarse-grain a distribution via a partition map f."""
    f_arr = np.array(f, dtype=int)
    if mu.ndim != 1 or mu.shape[0] != f_arr.shape[0]:
        raise ValueError("mu and f must be compatible")
    if m is None:
        m = int(f_arr.max()) + 1
    return pushforward_dist(mu, f_arr, n_out=m)


def lift_uniform(nu: np.ndarray, f: ArrayLike) -> np.ndarray:
    """Uniform lift from cell distribution to state distribution."""
    f_arr = np.array(f, dtype=int)
    sizes = partition_sizes(f_arr)
    if nu.ndim != 1 or nu.shape[0] != sizes.shape[0]:
        raise ValueError("nu and f must be compatible")
    if np.any(sizes == 0):
        raise ValueError("partition has empty cells")
    lifted = np.zeros_like(f_arr, dtype=float)
    for z, cell in enumerate(f_arr):
        lifted[z] = nu[cell] / sizes[cell]
    return lifted


def proj_uniform(mu: np.ndarray, f: ArrayLike) -> np.ndarray:
    """Project mu onto uniform-within-cells distributions."""
    return lift_uniform(coarse_grain(mu, f), f)


def induced_empirical_closure(
    mu: np.ndarray, P: np.ndarray, tau: int, f: ArrayLike
) -> np.ndarray:
    """Apply E_{tau,Pi}(mu) = U(Q(mu P^tau))."""
    if tau < 0:
        raise ValueError("tau must be nonnegative")
    validate_transition_matrix(P)
    mu_t = mu @ np.linalg.matrix_power(P, tau)
    return lift_uniform(coarse_grain(mu_t, f), f)


def tv(p: np.ndarray, q: np.ndarray) -> float:
    """Total variation distance."""
    if p.shape != q.shape:
        raise ValueError("p and q must have the same shape")
    return 0.5 * float(np.abs(p - q).sum())


def idempotence_defect(
    mu: np.ndarray, P: np.ndarray, tau: int, f: ArrayLike
) -> float:
    """Idempotence defect d(mu) = TV(E(E(mu)), E(mu))."""
    mu1 = induced_empirical_closure(mu, P, tau, f)
    mu2 = induced_empirical_closure(mu1, P, tau, f)
    return tv(mu2, mu1)


def max_idempotence_defect(
    P: np.ndarray, tau: int, f: ArrayLike, mus: list[np.ndarray]
) -> float:
    """Max idempotence defect over a finite family of tests."""
    return max(idempotence_defect(mu, P, tau, f) for mu in mus)


def idempotence_defect_tv(E: np.ndarray) -> float:
    """Exact TV idempotence defect: 0.5 * max_i sum_j |(E^2 - E)_{ij}|."""
    if E.ndim != 2 or E.shape[0] != E.shape[1]:
        raise ValueError("E must be a square matrix")
    M = E @ E - E
    row_sums = np.sum(np.abs(M), axis=1)
    return 0.5 * float(np.max(row_sums))


def prototypes_uniform(f: ArrayLike) -> list[np.ndarray]:
    """Uniform prototypes for each partition cell."""
    f_arr = np.array(f, dtype=int)
    sizes = partition_sizes(f_arr)
    if np.any(sizes == 0):
        raise ValueError("partition has empty cells")
    n = f_arr.shape[0]
    prototypes: list[np.ndarray] = []
    for cell, size in enumerate(sizes):
        u = np.zeros(n, dtype=float)
        u[f_arr == cell] = 1.0 / size
        prototypes.append(u)
    return prototypes


def prototype_stabilities(
    P: np.ndarray, tau: int, f: ArrayLike
) -> list[float]:
    """Return TV(E(u_i), u_i) for each prototype u_i."""
    stabilities = []
    for u in prototypes_uniform(f):
        Eu = induced_empirical_closure(u, P, tau, f)
        stabilities.append(tv(Eu, u))
    return stabilities


def three_block_chain(
    eps_ab: float,
    eps_toC: float,
    eps_fromC: float,
    p_switch: float = 0.35,
) -> np.ndarray:
    """Construct a 3-block chain with controlled leakage."""
    P = np.zeros((6, 6), dtype=float)

    def add_row(i, j_switch, leak_ab, leak_c, stay):
        P[i, i] += stay
        P[i, j_switch] += p_switch
        P[i, leak_ab] += eps_ab
        P[i, leak_c] += eps_toC

    stay_ab = 1.0 - (p_switch + eps_ab + eps_toC)
    if stay_ab < 0.0:
        raise ValueError("Row probabilities for A/B must be nonnegative")

    add_row(0, 1, 2, 4, stay_ab)
    add_row(1, 0, 3, 5, stay_ab)
    add_row(2, 3, 0, 4, stay_ab)
    add_row(3, 2, 1, 5, stay_ab)

    stay_c = 1.0 - (p_switch + 2.0 * eps_fromC)
    if stay_c < 0.0:
        raise ValueError("Row probabilities for C must be nonnegative")

    P[4, 4] += stay_c
    P[4, 5] += p_switch
    P[4, 0] += eps_fromC
    P[4, 2] += eps_fromC

    P[5, 5] += stay_c
    P[5, 4] += p_switch
    P[5, 1] += eps_fromC
    P[5, 3] += eps_fromC

    validate_transition_matrix(P)
    return P
