#!/usr/bin/python3.8
#####################################
#
# Class 23: PDEs I: Boundary Value
# and Initial Value problems
# Author: Adapted by M Joyce from Mark Newman
#
# https://public.websites.umich.edu/~mejn/cp/programs.html
#
#####################################
from numpy import empty,zeros,max
from pylab import imshow,gray,show

# Constants
M = 100         # Grid squares on a side
h = 1           # length between adjacent nodes

V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy -- tolerance threshold for solution

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float) ## 2D array 


'''
the following statement is setting a Dirichlet boundary condition on the top edge of the 2D grid
phi is a 2D NumPy array of shape (M+1, M+1) representing the potential at each point on a square grid
The notation phi[0,:] means: “all columns in row 0” — in other words, the entire top row of the grid
phi[0,:] = V sets the potential to V = 1.0 on the entire top boundary.
All other boundaries (bottom, left, and right) are implicitly left at zero 
(since phi was initialized with zeros(...)), meaning those edges are held at 0 volts.
'''
phi[0,:] = V    


phinew = empty([M+1,M+1],float)

# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            ## boundary conditions
            if i==0 or i==M or j==0 or j==M:
                phinew[i,j] = phi[i,j]
            else:
                phinew[i,j] = (phi[i+h,j] + phi[i-h,j] \
                                 + phi[i,j+h] + phi[i,j-h])/4.

    # Calculate maximum difference from old values
    delta = max(abs(phi-phinew))

    phi = phinew  # the new value of phi is set to what we just found for phinew
    phinew = phi  # phinew will be immediately overwritten in the next iteration, so 
                  # we assign it a placeholder value of the correct size until then, 
                  # which might as well be phi


    # shorthand way of doing this is to simply swap the two arrays around
    #   phi,phinew = phinew,phi

# Make a plot
imshow(phi)
gray()
show()