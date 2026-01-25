import numpy as np

from clt.bridge_kernels import convolve_causal, energy, positive_work, truncate_window
from clt.ect_toy import cap_bound_linear, harmonic_partial_sum, icap_mass_constant, make_atom_kernel, make_sector_kernels


def _example_signal(T: int = 40) -> np.ndarray:
    t = np.arange(T, dtype=float)
    u = np.zeros((T, 2), dtype=float)
    u[:, 0] = np.sin(0.2 * t) + 0.1 * (t % 6 == 0)
    u[:, 1] = np.cos(0.17 * t) - 0.08 * (t % 9 == 0)
    return u


def test_linear_capacity_growth_and_partial_sums() -> None:
    atom = make_atom_kernel()
    Lambda0 = icap_mass_constant(atom)
    for j in range(0, 6):
        cap_j = cap_bound_linear(j, Lambda0)
        cap_next = cap_bound_linear(j + 1, Lambda0)
        assert abs((cap_next - cap_j) - Lambda0) <= 1e-12

    psum_12 = harmonic_partial_sum(12, Lambda0)
    assert psum_12 > 0.5 / Lambda0


def test_parallel_sum_witness_inequality() -> None:
    j = 5
    kernels = make_sector_kernels(j)
    atom = kernels[0]
    Lambda0 = icap_mass_constant(atom)
    u = _example_signal()
    s, t = 10, 30
    u_tr = truncate_window(u, s, t)
    y_total = np.zeros_like(u_tr)
    for K in kernels:
        y_total += convolve_causal(K, u_tr)
    Wpos = positive_work(u_tr, y_total, s, t)
    E = energy(u_tr, s, t)
    tol = 1e-10
    assert Wpos <= (j + 1) * Lambda0 * E + tol
