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
import matplotlib.animation as animation

# Load the data
data = np.loadtxt("perturbed_pendulum_data.txt", skiprows=1)
t, x1, y1, x2, y2 = data.T

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.0, 1.0)
ax.set_xlabel("X position (m)")
ax.set_ylabel("Y position (m)")
ax.set_title("Double Pendulum Simulation")

# Plot the pivot point (fixed at the origin)
pivot, = ax.plot([], [], 'ko', label="Pivot")

# Create lines for the pendulum arms
line1, = ax.plot([], [], 'b-', label="Mass 1 Path")
line2, = ax.plot([], [], 'r-', label="Mass 2 Path")

# Create markers for the masses
mass1, = ax.plot([], [], 'bo', label="Mass 1", markersize=8)
mass2, = ax.plot([], [], 'ro', label="Mass 2", markersize=8)

# Initial conditions for the animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    mass1.set_data([], [])
    mass2.set_data([], [])
    return line1, line2, mass1, mass2

# Update function for the animation
def update(frame):
    # Get the current positions of the masses
    x1_pos = x1[frame]
    y1_pos = y1[frame]
    x2_pos = x2[frame]
    y2_pos = y2[frame]
    
    # Update the data for the lines
    line1.set_data([0, x1_pos], [0, y1_pos])  # Line from pivot to mass 1
    line2.set_data([x1_pos, x2_pos], [y1_pos, y2_pos])  # Line from mass 1 to mass 2

    # Update the positions of the masses
    mass1.set_data(x1_pos, y1_pos)
    mass2.set_data(x2_pos, y2_pos)
    
    return line1, line2, mass1, mass2

# Set up the animation
# Adjust interval and fps
interval_ms = 10  # 200 ms between frames
fps = 1000 // interval_ms  # Ensure the fps matches the interval

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=interval_ms)

# Save the animation as a video (MP4 file)
ani.save('double_pendulum_simulation.mp4', writer='ffmpeg', fps=fps)

#plt.show()

