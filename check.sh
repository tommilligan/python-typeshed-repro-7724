#!/bin/bash

set -euo pipefail

rm -rf .mypy_cache && mypy minimal.py
