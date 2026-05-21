#!/usr/bin/env bash

set -euo pipefail

rm -rf build dist

python3 -m PyInstaller --noconfirm --onefile --name total-score main.py

cp dist/total-score dist/total-score-linux-x64
