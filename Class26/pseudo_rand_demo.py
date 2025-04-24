#!/usr/bin/python3.8
#####################################
#
# Class 26: pseudo-random algorithms
# Author: M Joyce
#
#####################################

import numpy as np

seed = 15

# Mersenne Twister (default legacy)
rng1 = np.random.default_rng(np.random.MT19937(seed))
print("Mersenne Twister:", rng1.random(1))

# PCG64 (NumPy default)
rng2 = np.random.default_rng(seed)
print("PCG64:", rng2.random(1))

# Philox (counter-based PRNG, parallel-safe)
rng3 = np.random.Generator(np.random.Philox(seed))
print("Philox:", rng3.random(1))

# SFC64 (good for speed and statistical quality)
rng4 = np.random.Generator(np.random.SFC64(seed))
print("SFC64:", rng4.random(1))