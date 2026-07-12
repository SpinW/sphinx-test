#!/usr/bin/env bash
# Build (and optionally serve) the Sphinx docs for this project.
#
# Usage:
#   ./build.sh          Clean, build HTML, then serve at http://localhost:8000
#   ./build.sh serve    Build, then serve at http://localhost:8000
#   ./build.sh clean    Remove generated output in docs/_build
set -euo pipefail

# Run from the repo root regardless of where the script is invoked.
cd "$(dirname "$0")"

case "${1:-all}" in
  all)
    uv run sphinx-build -M clean docs docs/_build
    uv run sphinx-build -M html docs docs/_build
    uv run python -m http.server --directory docs/_build/html 8000
    ;;
  serve)
    uv run sphinx-build -M html docs docs/_build
    uv run python -m http.server --directory docs/_build/html 8000
    ;;
  clean)
    uv run sphinx-build -M clean docs docs/_build
    ;;
  *)
    uv run sphinx-build -M "$1" docs docs/_build
    ;;
esac
