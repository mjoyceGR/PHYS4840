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
## # Col. 33: membership probability

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)


magnitude = blue
color     = blue - red


quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))
 
print("quality_cut: ", quality_cut )

## demonstrate downsampling?

## set dimensions of figure 
fig, ax = plt.subplots(figsize=(8,16))

plt.plot(color[quality_cut], magnitude[quality_cut], "k.", markersize = 4, alpha = 0.2)
plt.gca().invert_yaxis()
plt.xlabel("Color: B-R", fontsize=20)
plt.ylabel("Magnitude: B", fontsize=20)
plt.title('Hubble Space Telescope Data for\nthe Globular Cluster NGC6341', fontsize=22)
plt.xlim(-2, 5)
plt.ylim(25,13.8)
plt.show()
plt.close()

###################################
# Bonus Exercise
###################################

# Set dimensions of figure
fig, ax = plt.subplots(figsize=(8, 16))

# Create a scatter plot with color-coding by probability
scatter = ax.scatter(color[quality_cut], magnitude[quality_cut], c=probability[quality_cut], 
                     cmap='viridis', s=4, alpha=0.8)

# Add a color bar to show the probability scale
cbar = plt.colorbar(scatter)
cbar.set_label('Membership Probability', fontsize=16)

# Invert the y-axis
plt.gca().invert_yaxis()

# Label the axes and title
plt.xlabel("Color: B-R", fontsize=20)
plt.ylabel("Magnitude: B", fontsize=20)
plt.title('Hubble Space Telescope Data for\nthe Globular Cluster NGC6341', fontsize=22)

# Set axis limits
plt.xlim(-2, 5)
plt.ylim(25, 13.8)

# Show the plot
plt.show()
plt.close()