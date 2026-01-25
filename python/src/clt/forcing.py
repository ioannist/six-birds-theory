from __future__ import annotations

import numpy as np


def block_labels(f: np.ndarray) -> np.ndarray:
    """Return sorted unique block labels."""
    f_arr = np.array(f, dtype=int)
    if f_arr.ndim != 1:
        raise ValueError("f must be 1D")
    if f_arr.size == 0:
        raise ValueError("f must be non-empty")
    return np.unique(f_arr)


def block_indices(f: np.ndarray) -> list[np.ndarray]:
    """Return indices for each block label."""
    f_arr = np.array(f, dtype=int)
    labels = block_labels(f_arr)
    return [np.where(f_arr == lab)[0] for lab in labels]


def block_sizes(f: np.ndarray) -> np.ndarray:
    """Return sizes for each block label."""
    return np.array([len(idx) for idx in block_indices(f)], dtype=int)


def is_definable(h: np.ndarray, f: np.ndarray) -> bool:
    """Predicate is definable if it is constant on each block."""
    h_arr = np.array(h, dtype=int)
    if h_arr.ndim != 1:
        raise ValueError("h must be 1D")
    if h_arr.size != np.array(f).size:
        raise ValueError("h and f must have same length")
    for idx in block_indices(f):
        values = h_arr[idx]
        if values.min() != values.max():
            return False
    return True


def splits_every_block(h: np.ndarray, f: np.ndarray) -> bool:
    """Return True if each block contains both 0 and 1."""
    h_arr = np.array(h, dtype=int)
    if h_arr.ndim != 1:
        raise ValueError("h must be 1D")
    if h_arr.size != np.array(f).size:
        raise ValueError("h and f must have same length")
    for idx in block_indices(f):
        values = h_arr[idx]
        if values.min() == values.max():
            return False
    return True


def theory_p_definable(N: int, K: int) -> float:
    """Probability a random predicate is definable from a K-block partition."""
    return float(2.0 ** (K - N))


def theory_p_split_every_block(f: np.ndarray) -> float:
    """Exact probability that a random predicate splits every block."""
    sizes = block_sizes(f)
    prob = 1.0
    for m in sizes:
        prob *= 1.0 - 2.0 ** (1 - m)
    return float(prob)


def union_bound_lower_split_every_block(f: np.ndarray) -> float:
    """Union-bound lower bound for split-every-block probability."""
    sizes = block_sizes(f)
    bound = 1.0 - float(np.sum(2.0 ** (1 - sizes)))
    return float(max(0.0, bound))


def estimate_frequencies(
    f: np.ndarray,
    n_samples: int,
    seed: int = 0,
    *,
    chunk: int = 50_000,
) -> dict:
    """Monte Carlo estimates for definable and split predicates."""
    f_arr = np.array(f, dtype=int)
    if f_arr.ndim != 1:
        raise ValueError("f must be 1D")
    N = int(f_arr.size)
    labels = block_labels(f_arr)
    K = int(labels.size)
    blocks = block_indices(f_arr)

    rng = np.random.default_rng(seed)
    count_def = 0
    count_split = 0
    remaining = n_samples

    while remaining > 0:
        take = min(chunk, remaining)
        H = rng.integers(0, 2, size=(take, N), dtype=np.int8)
        definable = np.ones(take, dtype=bool)
        split = np.ones(take, dtype=bool)
        for idx in blocks:
            block_vals = H[:, idx]
            mins = block_vals.min(axis=1)
            maxs = block_vals.max(axis=1)
            definable &= mins == maxs
            split &= mins != maxs
        count_def += int(definable.sum())
        count_split += int(split.sum())
        remaining -= take

    p_def_emp = count_def / n_samples
    p_split_emp = count_split / n_samples

    p_def_theory = theory_p_definable(N, K)
    p_split_theory = theory_p_split_every_block(f_arr)
    p_split_union_lb = union_bound_lower_split_every_block(f_arr)

    return {
        "N": N,
        "K": K,
        "n_samples": n_samples,
        "p_def_emp": p_def_emp,
        "p_def_theory": p_def_theory,
        "p_split_emp": p_split_emp,
        "p_split_theory": p_split_theory,
        "p_split_union_lb": p_split_union_lb,
        "counts_def": count_def,
        "counts_split": count_split,
    }
