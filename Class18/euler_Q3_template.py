#!/usr/bin/python3.8
#####################################
#
# Class 18: ODEs 1, Euler's method 
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = ...

    for i in range(1, len(t_values)):
        x_values[i] = x_values[i - 1] + dt * f(..., ...)

    return t_values, x_values

def differential_eq(x, t):
    expresison = ...
    return expression

# Initial conditions
x0 = ...
t0 = ...
t_end = 5
dt = 0.01 ## try two other step sizes

# Solve using Euler method
t_values, x_values = euler_method(...)

# Plotting the solution
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="Euler Approximation", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Euler Method Solution for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()
