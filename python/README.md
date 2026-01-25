# CLT Python Harness

Finite-state experimental harness for six birds theory sanity checks.

## Run tests

```bash
cd python
python -m pytest -q
```

## Modules

- `clt.markov`: finite Markov chains, stationarity, time reversal, entropy production.
- `clt.paths`: path laws, KL, reversal, coarse-grain pushforward for paths.
- `clt.coarse`: coarse-graining for distributions and stationary kernels.
- `clt.graph`: undirected graph utilities for cycle-rank checks.

## Stationary distribution note

`stationary_distribution` uses power iteration first and falls back based on `on_fail`.
For periodic or reducible chains, prefer `stationary_distribution_solve(...)` or
`stationary_distribution_cesaro(...)` explicitly.

This is a small, deterministic, numpy-only harness intended for theorem stress tests.
