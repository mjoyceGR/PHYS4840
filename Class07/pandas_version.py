#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################

import pandas as pd

filename = '../Class06/NGC6341.dat'

# Read the file while skipping the first 54 lines of header
# Assumes space-separated values
# "comment='#'" ensures lines starting with '#' are treated as comments and ignored

df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None, skiprows=54)

# Extract the columns corresponding to
# F336W, F438W, and F814W magnitudes
blue = df.iloc[:, 8]   # Column 9 
green = df.iloc[:, 14]  # Column 15 
red = df.iloc[:, 26]   # Column 27 

blue = blue.to_numpy()
green = green.to_numpy()
red = red.to_numpy()

print("len(green):", len(green))
