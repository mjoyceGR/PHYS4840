#!/usr/bin/python3.8
#####################################
#
# Class 20: Boundary-Value problems;
# coupled ODEs, the double pendulum
# Author: M Joyce
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("double_pendulum_data.txt", skiprows=1)
t, x1, y1, x2, y2 = data.T

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x1, y1, marker='.', label="Mass 1 (Path)")
plt.plot(x2, y2, marker='.', label="Mass 2 (Path)", color="red")
plt.scatter([0], [0], color="black", marker="o", label="Pivot")  # Fixed pivot point

# Mark initial positions
plt.scatter([x1[0]], [y1[0]], color="blue", marker="+", s=100, label="Mass 1 (Start)", zorder=3)
plt.scatter([x2[0]], [y2[0]], color="red", marker="+", s=100, label="Mass 2 (Start)", zorder=3)

# Formatting
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Double Pendulum Motion")
plt.legend()
plt.axis("equal")
plt.grid()

# Save figure
plt.savefig('motions.png')
plt.close()
