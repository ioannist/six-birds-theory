# formal

## Build (first time)

```bash
cd formal
lake exe cache get
lake build
```

## Build (subsequent)

```bash
cd formal && lake build
```

## Troubleshooting

- If mathlib seems corrupt: delete `formal/.lake/packages/mathlib` and rerun `lake update`, then `lake exe cache get`, then `lake build`.
