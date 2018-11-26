#!/usr/bin/env bash
# Adding env var for fiyeli directory
SCRIPT_PATH=$(readlink -f "$0")
FIYELI_DIR=$(dirname "$SCRIPT_PATH")
echo "export FIYELI_DIR=$(dirname "$SCRIPT_PATH")" >> ~/.bashrc