#!/usr/bin/env python3.8
####################################################
#
# This is a bad replacement for py_mesa_reader
# in case py_mesa_reader is not available
#
# Author: M Joyce
#
####################################################

import numpy as np
import shlex            # handles quoted strings cleanly
from pathlib import Path

def _read_block(lines, i0):
    """
    Parse one block that starts at line index `i0`.
    Returns (data_dict, next_line_index).
    """
    # numeric column indices (throw-away, but useful for the width)
    nums = lines[i0].rstrip("\n")
    # names (the line right after the numbers)
    names_line = lines[i0+1].rstrip("\n")

    # split on shell-style tokens so "quoted strings" stay intact
    names = shlex.split(names_line)
    width  = (len(nums) // len(names))  # fixed width of each column

    # grab subsequent data lines until we hit a completely blank line
    i = i0 + 2
    block_lines = []
    while i < len(lines) and lines[i].strip():
        block_lines.append(lines[i])
        i += 1

    # Build a 2-D array of strings, fixed width-slice per column
    raw = np.char.strip(
        np.asarray(
            [[row[j*width:(j+1)*width] for j in range(len(names))]
             for row in block_lines],
            dtype="U48"                # 48 chars matches MESA’s default
        )
    )

    # Convert each column to the best numeric type; leave quoted things as str
    data = {}
    for j, name in enumerate(names):
        col = np.char.strip(raw[:, j])
        if col.size == 1:              # scalar meta-data (first section)
            token = col[0]
            try:
                data[name] = float(token.replace("D","E"))  # handle Fortran exponents
            except ValueError:
                data[name] = token.strip('"')               # strip surrounding quotes
        else:                           # time-series / profile columns
            try:
                data[name] = col.astype(float)
            except ValueError:
                data[name] = np.array([s.strip('"') for s in col])

    return data, i                      # where the *next* block starts


def load_mesa_table(path):
    """
    Parse the whole file and merge the resulting dicts.
    For duplicate keys later blocks overwrite earlier ones.
    """
    lines = Path(path).read_text().splitlines()
    i = 0
    full = {}
    while i < len(lines):
        if not lines[i].strip():       # skip blank lines
            i += 1
            continue
        # A block always starts with digits 1, 2, 3 ...
        if lines[i].lstrip()[0].isdigit():
            block, i = _read_block(lines, i)
            full.update(block)
        else:
            i += 1                     # defensive – shouldn't happen
    return full