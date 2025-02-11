#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np

## Initialize lists to store the data. Note that these ARE NOT ARRAYS!!
## you cannot 'append' to an array! You must append to a list, then
## cast as an array later
blue, green, red = [], [], []

filename = 'NGC6341.dat'
# Open the file and read line by line
with open(filename, 'r') as file:
    for line in file:
        # Skip lines that start with '#'
        if line.startswith('#'):
            continue
        
        # Split the line into columns based on spaces
        columns = line.split()
        
        blue.append(float(columns[8]))   # Column 9 
        green.append(float(columns[14])) # Column 15 
        red.append(float(columns[26]))   # Column 27 

blue = np.array(blue)
green = np.array(green)
red = np.array(red)
