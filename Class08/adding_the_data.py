#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import matplotlib.pyplot as plt
import sys

################################################
#
# Homework 2 problem 1 help
# Part 2
#
# Now, let's compare this to the HST data 
#
#################################################


'''
This code block loads and cleans the theoretical models from
the iso.cmd file. It is the same code as in isochrone_in-class_demo.py
but with the comments and instructions removed. Consult the commented 
version of this file if you are confused about any of these steps 
'''
load_file = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)

age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9
age_Gyr = age_Gyr_1e9

age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]

Teff = 10.0**logTeff
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

phases_for_desired_age = phase[age_selection]
desired_phases = np.where(phases_for_desired_age <= 3)

## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

####################################################################

'''
Now, recall how we loaded, cleaned, and plotted NGC6341.dat
'''
filename = 'NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude
## # Col. 33: membership probability
## but Python indexes from 0, not 1!

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

magnitude = blue
color     = blue - red

quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))
 
print("quality_cut: ", quality_cut )


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

##################################
#
# Let's put all three data sets on the same Figure!
#
####################################

#####################################################################################

fig, axes = plt.subplots(1, 3, figsize=(14, 6))  # 3 panels side by side

# First panel: Color-Magnitude Diagram
axes[0].plot(cleaned_color, cleaned_magnitude, 'go', markersize=2, linestyle='-', label='color-mag')
axes[0].invert_yaxis()
axes[0].set_xlabel('Color', fontsize=15)
axes[0].set_ylabel('Magnitude', fontsize=15)

# Second panel: Theoretical Isochrone
axes[1].plot(cleaned_Teff, cleaned_logL, 'go', label='isochrone theoretical')
axes[1].invert_xaxis()
axes[1].set_xlabel('Teff (K)', fontsize=15)
axes[1].set_ylabel('logL', fontsize=15)
axes[1].set_xlim(7500, 2800)

# Third panel: Hubble Space Telescope Data
axes[2].plot(color[quality_cut], magnitude[quality_cut], "k.", markersize=4, alpha=0.2)
axes[2].invert_yaxis()
axes[2].set_xlabel("Color: B-R", fontsize=15)
axes[2].set_ylabel("Magnitude: B", fontsize=15)
axes[2].set_title('Hubble Space Telescope Data for\n the Globular Cluster NGC6341', fontsize=16)
axes[2].set_xlim(-2, 5)
axes[2].set_ylim(25, 13.8)

plt.tight_layout()
#plt.show()
plt.savefig("three_panel_CMD_figure.png")
plt.close()