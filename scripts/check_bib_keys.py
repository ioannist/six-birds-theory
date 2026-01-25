#!/usr/bin/env python3
"""Check that all cite keys in manuscript/paper.tex exist in manuscript/refs.bib."""
from __future__ import annotations

import re
import sys
from pathlib import Path

TEX_PATH = Path("manuscript/paper.tex")
BIB_PATH = Path("manuscript/refs.bib")

cite_re = re.compile(r"\\cite[a-zA-Z*]*\{([^}]*)\}")
key_re = re.compile(r"@\w+\s*\{\s*([^,\s]+)")

tex_text = TEX_PATH.read_text(encoding="utf-8")
bib_text = BIB_PATH.read_text(encoding="utf-8")

cited: set[str] = set()
for match in cite_re.finditer(tex_text):
    keys = match.group(1).split(",")
    for key in keys:
        key = key.strip()
        if key:
            cited.add(key)

bib_keys = set(key_re.findall(bib_text))

missing = sorted(cited - bib_keys)
if missing:
    print("Missing citation keys:")
    for key in missing:
        print(f"  - {key}")
    sys.exit(1)

print(f"bib keys OK ({len(cited)} cited, {len(bib_keys)} in refs.bib)")
