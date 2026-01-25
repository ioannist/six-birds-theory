#!/usr/bin/env python3
# Usage: python3 scripts/check_paper_contract.py

import json
import re
import sys
from pathlib import Path

SCOPE_PATH = Path("docs/spec/paper-scope-map.json")
INV_PATH = Path("docs/spec/theorem-inventory.md")


def load_inventory_ids(text: str):
    ids = []
    hypotheses = {}
    current_id = None
    for line in text.splitlines():
        m = re.search(r"\*\*ID:\*\*\s*([A-Z0-9-]+)", line)
        if m:
            current_id = m.group(1)
            ids.append(current_id)
            hypotheses[current_id] = None
            continue
        if current_id:
            h = re.search(r"\*\*Hypotheses:\*\*\s*(.*)", line)
            if h:
                hypotheses[current_id] = h.group(1).strip()
    return set(ids), hypotheses


def main():
    errors = []

    if not SCOPE_PATH.exists():
        errors.append(f"missing scope map: {SCOPE_PATH}")
    if not INV_PATH.exists():
        errors.append(f"missing inventory: {INV_PATH}")
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    scope = json.loads(SCOPE_PATH.read_text())
    inv_text = INV_PATH.read_text()
    inv_ids, inv_hyp = load_inventory_ids(inv_text)

    for key in ("main", "appendix", "omit"):
        if key not in scope:
            errors.append(f"missing top-level key: {key}")
            continue
        for subkey in ("definitions", "claims"):
            if subkey not in scope[key]:
                errors.append(f"missing key: {key}.{subkey}")
    if "appendix" in scope and "artifacts" not in scope["appendix"]:
        errors.append("missing key: appendix.artifacts")

    def check_ids(label, entries, prefixes):
        for item in entries:
            if not any(item.startswith(p) for p in prefixes):
                errors.append(f"{label}: invalid prefix for {item}")
            if item not in inv_ids:
                errors.append(f"{label}: unknown ID {item}")

    all_ids = {}

    def add_ids(label, entries):
        for item in entries:
            if item in all_ids:
                errors.append(
                    f"ID {item} appears in multiple sections: {all_ids[item]} and {label}"
                )
            else:
                all_ids[item] = label

    main_defs = scope.get("main", {}).get("definitions", [])
    main_claims = scope.get("main", {}).get("claims", [])
    app_defs = scope.get("appendix", {}).get("definitions", [])
    app_claims = scope.get("appendix", {}).get("claims", [])
    omit_defs = scope.get("omit", {}).get("definitions", [])
    omit_claims = scope.get("omit", {}).get("claims", [])

    check_ids("main.definitions", main_defs, ("D-",))
    check_ids("appendix.definitions", app_defs, ("D-",))
    check_ids("omit.definitions", omit_defs, ("D-",))

    check_ids("main.claims", main_claims, ("T-", "C-", "L-"))
    check_ids("appendix.claims", app_claims, ("T-", "C-", "L-"))
    check_ids("omit.claims", omit_claims, ("T-", "C-", "L-"))

    add_ids("main.definitions", main_defs)
    add_ids("main.claims", main_claims)
    add_ids("appendix.definitions", app_defs)
    add_ids("appendix.claims", app_claims)
    add_ids("omit.definitions", omit_defs)
    add_ids("omit.claims", omit_claims)

    for claim_id in main_claims:
        hyp = inv_hyp.get(claim_id)
        if hyp is None or hyp == "":
            errors.append(f"main.claims: missing Hypotheses line for {claim_id}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print("paper contract scope map OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
