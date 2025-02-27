#!/usr/bin/python3.8
#####################################
#
# Class 12: Numerical Differentiation II
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# some data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 1, 3, 7, 8])  

# Define fine-grained x-values for interpolation
x_domain = np.linspace(min(x), max(x), 100)

# Linear Interpolation
linear_interp = interp1d(x, y, kind='linear')
y_linear = linear_interp(x_domain)

# Cubic Spline Interpolation
cubic_spline = CubicSpline(x, y)
y_cubic = cubic_spline(x_domain)

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data Points', zorder=3)
plt.plot(x_domain, y_linear, '--', label='Linear Interpolation', linewidth=2)
plt.plot(x_domain, y_cubic, label='Cubic Spline Interpolation', linewidth=2)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear vs. Cubic Spline Interpolation')
plt.grid(True)
plt.show()