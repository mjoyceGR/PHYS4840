#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../')
import my_functions_lib as mfl


filename = 'NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude

blue, green, red = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)

magnitude = blue
color     = blue - red

plt.plot(color, magnitude, "ko")
plt.savefig('terrible_figure.png')
