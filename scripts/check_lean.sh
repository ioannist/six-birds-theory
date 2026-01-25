#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
cd formal
lake exe cache get
lake build
