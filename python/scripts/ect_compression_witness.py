#!/usr/bin/env python3
"""Print a small table for the ECT compression witness (j=0..12)."""

from __future__ import annotations

from clt.ect_toy import cap_bound_linear, harmonic_partial_sum, icap_mass_constant, make_atom_kernel


def main() -> None:
    J = 12
    atom = make_atom_kernel()
    Lambda0 = icap_mass_constant(atom)
    print("j\tm_j\tLambda0\tCap_bound\tpartial_sum")
    for j in range(J + 1):
        m_j = j + 1
        cap = cap_bound_linear(j, Lambda0)
        psum = harmonic_partial_sum(j, Lambda0)
        print(f"{j}\t{m_j}\t{Lambda0:.6f}\t{cap:.6f}\t{psum:.6f}")
    print("partial_sum grows ~ log(j), consistent with divergence")


if __name__ == "__main__":
    main()
