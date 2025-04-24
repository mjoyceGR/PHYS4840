#!/usr/bin/python3.8
#####################################
#
# Class 26: Spectral decomp
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Set up the domain and function
N = 64                             # Number of grid points
L = 2 * np.pi                      # Domain length [-π, π]
x = np.linspace(-np.pi, np.pi, N, endpoint=False)  # Grid points
f = np.cos(x)                      # Function to integrate

# Step 2: Compute the FFT of the function (go to frequency space)
f_hat = np.fft.fft(f)              # Fourier coefficients (complex)

# Step 3: Build the frequency array
k = np.fft.fftfreq(N, d=L/N)       # Frequencies in cycles per unit length
k = 2 * np.pi * k                  # Convert to angular frequencies (radians)

# Step 4: Integrate in Fourier space by dividing by ik
F_hat = np.zeros(N, dtype=complex) # Initialize integrated coefficients

for i in range(N):
    if k[i] != 0:
        F_hat[i] = f_hat[i] / (1j * k[i])
    else:
        F_hat[i] = 0  # No contribution from the DC component (mean value)

# Step 5: Inverse FFT to return to real space
f_integrated = np.fft.ifft(F_hat).real  # Take the real part

# Plot results
x_array_for_sin = np.linspace(-np.pi, np.pi, 10000)

plt.plot(x_array_for_sin, np.sin(x_array_for_sin), '-', linewidth=1, color='black', label='True sin(x)')
plt.plot(x, f_integrated, "ro-", linewidth=2, markersize=10, alpha=0.6, label='Integrated cos(x)')

plt.legend()
plt.title("Spectral Integration using FFT")
plt.grid(True)
plt.show()