#!/usr/bin/python3.8
#####################################
#
# Class 20: Boundary-Value problems;
# coupled ODEs, the double pendulum
# Author: M Joyce
#
#####################################
import numpy as np
import random

# Constants
g = 9.81  # Gravity (m/s^2)
l = 0.4   # Length of pendulum arms (m)
m = 1.0   # Mass of pendulums (kg)

# Set random seed for reproducibility if needed (remove this for full randomness)
random.seed()  # Seed from system time, removes fixed randomness

# Randomly perturb initial conditions to simulate chaos
theta1 = np.radians(90 + random.uniform(-1, 1))  # Slight random perturbation
theta2 = np.radians(90 + random.uniform(-1, 1))  # Slight random perturbation
omega1 = random.uniform(-0.1, 0.1)  # Small random initial velocity
omega2 = random.uniform(-0.1, 0.1)  # Small random initial velocity

r0 = np.array([theta1, theta2, omega1, omega2])  # State vector r = [theta1, theta2, omega1, omega2]

# Time parameters
dt = 0.001  # Time step
t_max = 10  # Simulation duration
t = np.arange(0, t_max, dt)

# Equations of motion for the double pendulum
def equations(r):
    theta1, theta2, omega1, omega2 = r
    delta_theta = theta2 - theta1

    # Define the four equations for the system
    ftheta1 = omega1
    ftheta2 = omega2
    
    # The derivatives of omega1 and omega2
    denom1 = (2 * m * l ** 2)
    denom2 = (m * l ** 2)

    fomega1 = (-g * (2 * m) * np.sin(theta1) - m * g * np.sin(theta1 - 2 * theta2) - 
                2 * np.sin(delta_theta) * m *\
                (omega2 ** 2 * l + omega1 ** 2 * l * np.cos(delta_theta))) / denom1

    fomega2 = (2 * np.sin(delta_theta) * (omega1 ** 2 * l * m + g * m * np.cos(theta1) + 
                omega2 ** 2 * l * m * np.cos(delta_theta))) / denom2

    return np.array([ftheta1, ftheta2, fomega1, fomega2])

# Runge-Kutta 4th order method
def rk4_step(r, dt):
    k1 = dt * equations(r)
    k2 = dt * equations(r + 0.5 * k1)
    k3 = dt * equations(r + 0.5 * k2)
    k4 = dt * equations(r + k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Integrate equations and save data
R = np.zeros((len(t), 4))
R[0] = r0

for i in range(1, len(t)):
    R[i] = rk4_step(R[i - 1], dt)

# Extract angles and angular velocities
theta1_vals, theta2_vals, omega1_vals, omega2_vals = R.T

# Convert to Cartesian coordinates for visualization
x1 = l * np.sin(theta1_vals)
y1 = -l * np.cos(theta1_vals)
x2 = x1 + l * np.sin(theta2_vals)
y2 = y1 - l * np.cos(theta2_vals)

# Save data
np.savetxt("perturbed_pendulum_data.txt", np.column_stack([t, x1, y1, x2, y2]),
           header="time x1 y1 x2 y2", comments="")
