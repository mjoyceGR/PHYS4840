#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import matplotlib.pyplot as plt
import sys

################################
#
# Homework 2 problem 1 help
#
##############################
load_file = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

## I want columns 14 and 18 for the filters
log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)


#############################################
#
# this file actually contains many isochrone models, and we
# only need one. Deciding which is a physics question. 
# We know Globular Clusters are very old, so let's try
# an isochrone with age around 12 or 13 billion years.
# First, we will need to load the age column and make sure
# it is on the correct scale. Log or linear?
#
##############################################
age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9 	## should be the same as 10**9.
age_Gyr_10 = (10.0**log10_isochrone_age_yr)/10.**9 	## should be the same as 10**9.
age_Gyr = age_Gyr_1e9

## we only want to use the model(s) that fall in this age range
age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 
## this should extract only one isochrone

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]
###########################################
#
# Now let's plot the isochrone. Let's do this
# in terms of LogL vs Teff (HRD) AS WELL AS
# in the HST filter system (CMD)
#
# Let's convert log(Teff) to its unlogged form:
# 
###########################################

Teff = 10.0**logTeff

################################
#
# NOTE that we have already changed the size 
# of the color and magnitude arrays above using
# np.where()
#
# Therefore, we must adjust LogL, Teff arrays
# to be the same size as well, otherwise
# the indices selected by np.where() will
# not align correctly 
#
################################
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

############################################
#
# we now have the equal-sized arrays
#	color_selected
#   magnitude_selected
#   Teff_for_desired_ages
#   logL_for_desired_ages
#
# But we want to perform some additional data cleaning. 
# There is a quantity in the iso.cmd file called "phase."
# This indicates the evolutionary phase of the model. 
# We are only interested in the earlier evolution, so we can
# clean our data by removing phase indices above 4.
#
################################################


### First, we have to truncate the "phase" array
# so that it is the same size and has the same
# index coordinates as the other arrays to which
# we have applied age selection:
phases_for_desired_age = phase[age_selection]

desired_phases = np.where(phases_for_desired_age <= 3)


## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

###############################################
#
# Check that all of these arrays are the same length!
# Plotting will fail otherwise
#
################################################
print("lengths of processed arrays: ", len(cleaned_color),\
									   len(cleaned_magnitude),\
									   len(cleaned_Teff),\
									   len(cleaned_logL) )



#########################################
#
# This plotting code should produce a 
# BEAUTFIUL, two-panel figure showing
# the SAME DATA SET, but rendered in two different
# sets of coordinates: The left is a color-magnitude diagram, 
# in observational coordinates (HST filters), and 
# the left is a theoretical Hertzsprung-Russel diagram,
# in raw physical units (temperature, luminosity)
#
###########################################

fig, axes = plt.subplots(1, 2, figsize=(8, 6))  # 2:1 aspect ratio per panel

# First panel: Color-Magnitude Diagram
axes[0].plot(cleaned_color, cleaned_magnitude, 'go', markersize=2, linestyle='-', label='color-mag')
axes[0].invert_yaxis()
axes[0].set_xlabel('Color', fontsize=15)
axes[0].set_ylabel('Magnitude', fontsize=15)
#axes[0].set_xlim(7500, 2800)

# Second panel: Theoretical Isochrone
axes[1].plot(cleaned_Teff, cleaned_logL, 'go', label='isochrone theoretical')
axes[1].invert_xaxis()
axes[1].set_xlabel('Teff (K)', fontsize=15)
axes[1].set_ylabel('logL', fontsize=15)
axes[1].set_xlim(7500, 2800)

fig.tight_layout()
#plt.ylim(-3,4)
plt.savefig('compare_isochrones.png')
plt.close()