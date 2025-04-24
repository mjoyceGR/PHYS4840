#!/usr/bin/python3.8
#####################################
#
# Class 26: Spectral decomp
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt

# Domain setup
N = 10  
x = np.linspace(-np.pi, np.pi, N, endpoint=False)
f = np.cos(x)  # Function to integrate

# Manual computation of Fourier coefficients: f-hat
def manual_fourier_coeffs(f, x):
    N = len(x)
    dx = x[1] - x[0]
    L = N * dx  # Total domain length

    # Manually construct frequency indices k
    # Assume domain is periodic over [0, L)
    k = np.zeros(N)
    for n in range(N):
        if n <= N // 2:
            k[n] = n
        else:
            k[n] = n - N
    k = (2 * np.pi / L) * k  # Convert to angular frequencies

    # Compute Fourier coefficients manually
    fhats = np.zeros(N, dtype=complex)
    for n in range(N):
        exponent = -1j * k[n] * x
        fhats[n] = (1 / N) * np.sum(f * np.exp(exponent))

    return k, fhats


k, fk = manual_fourier_coeffs(f, x)

for i in range(len(k)):
    print("coeff number", i,\
          "    Fourier wave number k:", int(k[i]),\
          "    Fourier coefficient fk:", fk[i])

# Integrate: divide by i*k (except at k=0)
Fk = np.zeros_like(fk) ## populate an object the shape of fk with zeros 
nonzero = k != 0 # the set 'nonzero' is defined as those for which k != 0 (slicker version of np.where() )
Fk[nonzero] = fk[nonzero] / (1j * k[nonzero]) # perform the integration, AKA division in Fourier, for k[nonzero]
Fk[~nonzero] = 0.0  # ~nonzero means "not nonzero," so we are separating the 0-entry of FK out 
                    # and setting it to zero so as not to enounter a divide-by-zero error

# Reconstruct integrated function
f_integrated = np.real(np.sum([Fk[n] * np.exp(1j * k[n] * x) for n in range(N)], axis=0))

# Plot
x_array_for_sin = np.linspace(-np.pi, np.pi, 10000)

plt.plot(x_array_for_sin, np.sin(x_array_for_sin), '-', linewidth=1, color='black', label='True sin(x)')
plt.plot(x, f_integrated, "go-", linewidth=2, markersize=10, alpha=0.6, label='Integrated cos(x)')

plt.legend()
plt.title("Spectral Integration via Manual Fourier Series")
plt.grid(True)
plt.show()
