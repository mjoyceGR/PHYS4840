#!/usr/bin/python3.8
#####################################
#
# Class 23: PDEs I: Boundary Value
# and Initial Value problems
# Author: M Joyce
#
#####################################

import numpy as np

def laplacian_operator(Phi, dx, dy, dz):
    """
    Compute the Laplacian of a scalar field Phi (i.e., apply the Poisson operator)
    using central finite differences on a 3D uniform grid.

    Parameters:
    - Phi : 3D numpy array of shape (nx, ny, nz)
    - dx, dy, dz : grid spacings in x, y, z directions

    Returns:
    - laplacian : 3D numpy array of the same shape as Phi
    """

    laplacian = (
        (np.roll(Phi, -1, axis=0) - 2*Phi + np.roll(Phi, 1, axis=0)) / dx**2 +
        (np.roll(Phi, -1, axis=1) - 2*Phi + np.roll(Phi, 1, axis=1)) / dy**2 +
        (np.roll(Phi, -1, axis=2) - 2*Phi + np.roll(Phi, 1, axis=2)) / dz**2
    )

    return laplacian