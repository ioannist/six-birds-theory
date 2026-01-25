#!/usr/bin/env python3
import re
import sys
from pathlib import Path

TEX_PATH = Path('manuscript/paper.tex')

label_re = re.compile(r"\\label\{([^}]+)\}")
ref_re = re.compile(r"\\(?:ref|eqref)\{([^}]+)\}")

text = TEX_PATH.read_text()
labels = set(label_re.findall(text))
refs = ref_re.findall(text)
missing = sorted({r for r in refs if r not in labels})

if missing:
    print("Missing labels:")
    for r in missing:
        print(r)
    sys.exit(1)

print(f"tex refs OK ({len(refs)} refs, {len(labels)} labels)")
