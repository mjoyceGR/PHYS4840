#!/usr/bin/python3.8
#####################################
#
# Class 13: Matrices and Linear Algebra
# Author: M Joyce
#
#####################################
import numpy as np
from numpy import array, empty

A = array([[2, 1, 4, 1], 
            [3, 4, -1, -1], 
            [1, -4, 1, 5], 
            [2, -2, 1, 3]], float)

## dimension 
N = len(A)

# Initialize L as the N=4 identity matrix 
L = np.array([[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)])
# this above is just a more explicit way of doing
#L = np.identity(N)

print("L looks like this: ", L) ## should return the N=4 I


# initalize U as a copy of A
U = A.copy()


## this double loop will transform L
## into the lower-diagonal form we need
for m in range(N):
    for i in range(m+1, N):        
        
        # Compute the multiplier for the current row operation
        L[i, m] = U[i, m] / U[m, m]
        
        # Subtract the appropriate multiple of the pivot row from the current row
        U[i, :] -= L[i, m] * U[m, :]

print('The lower triangular matrix L is:\n', L)
print('The upper triangular matrix U is:\n', U)

## Write the next part of this program:
##  How do we solve the system of equations using forward and backward substitution?
##  Use L and U to solve Ax = b for a given vector b.

## HINT: see the end of 6.1.4 in your textbook (equations 6.37 through 6.39 in my version)