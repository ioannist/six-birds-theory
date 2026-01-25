import numpy as np

from clt.forcing import (
    is_definable,
    splits_every_block,
    theory_p_definable,
    theory_p_split_every_block,
)


def test_exact_enumeration_counts():
    f = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
    N = f.size
    K = 3
    count_def = 0
    count_split = 0
    for i in range(2**N):
        h = np.array([(i >> k) & 1 for k in range(N)], dtype=int)
        if is_definable(h, f):
            count_def += 1
        if splits_every_block(h, f):
            count_split += 1

    assert count_def == 2**K
    assert count_split == (2**3 - 2) ** 3

    p_def = count_def / (2**N)
    p_split = count_split / (2**N)
    assert p_def == theory_p_definable(N, K)
    assert np.isclose(p_split, theory_p_split_every_block(f))
