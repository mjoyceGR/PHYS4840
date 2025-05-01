#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import sys
import subprocess
import matplotlib.pyplot as plt

sys.path.append('/home/mjoyce/MESA/py_mesa_reader/')
import mesa_reader as mr


f = 'history.data' ## the file you copied over from ARCC

md = mr.MesaData(f)

log_Teff = md.log_Teff
log_L = md.log_L

fig, ax = plt.subplots(1, figsize=(8,12))
plt.plot(log_Teff, log_L, "go-")
plt.xlabel('Log Teff (K)')
plt.ylabel('Log L')
plt.gca().invert_xaxis()
plt.show()
plt.close()
