#!/usr/bin/env python3
"""Run Ren'Py lint for the current project.

Usage: python lint.py

Setup:
1. Set RENPY env var to the Ren'Py executable path:
   - Windows (CMD): set RENPY=C:/Path/To/renpy-8.x.x-sdk/renpy.exe
   - Windows (PowerShell): $env:RENPY = "C:/Path/To/renpy-8.x.x-sdk/renpy.exe"
   - macOS/Linux: export RENPY=/path/to/renpy-8.x.x-sdk/renpy.sh

2. Or set RENPY_PATH below to the executable path

3. Or add Ren'Py SDK to PATH:
   - Windows (CMD): set PATH=%PATH%;C:/Path/To/renpy-8.x.x-sdk
   - Windows (PowerShell): $env:Path += ";C:/Path/To/renpy-8.x.x-sdk"
   - macOS/Linux: export PATH="/path/to/renpy-8.x.x-sdk:$PATH"
"""

import os
import shutil
import subprocess
import sys
from typing import Optional


# Fallback if RENPY env var not set
# RENPY_PATH = "/path/to/renpy.sh"
RENPY_PATH: Optional[str] = "C:/Users/r.kucherenko/Downloads/renpy-8.3.4-sdk/renpy.exe"


def main() -> int:
    renpy_executable = os.environ.get("RENPY") or RENPY_PATH or "renpy"
    if shutil.which(renpy_executable) is None:
        print(
            f"Ren'Py executable '{renpy_executable}' not found. Set RENPY_PATH "
            "constant or the RENPY environment variable to its location.",
            file=sys.stderr,
        )
        return 1

    project_dir = os.path.dirname(os.path.abspath(__file__))

    process = subprocess.run(
        [renpy_executable, project_dir, "lint"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    print(process.stdout)
    if process.stderr:
        print(process.stderr, file=sys.stderr)

    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
