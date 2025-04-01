#!/usr/bin/python3.8
#####################################
#
# Class 19: ODEs II, Runge-Kutta, Fortran
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt


def RungeKutta2(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        x = x_values[i - 1]
        k1 = ...
        k2 = ...
        x_values[i] = x + k2

    return t_values, x_values


def differential_eq(x, t):
    my_eqn = ...
    return my_eqn


# Initial conditions
t0 = ...
x0 = ...
t_end = ...
dt = ...

# Solve using RK2 method
t_values, x_values = RungeKutta2(...)

# Plotting the solution
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="RK2 solution", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("RK2 Solution for dx/dt = -x^3 + sin(t)")
plt.grid(True)
plt.legend()
#plt.show()
plt.savefig('RK2_python.png')
plt.close()