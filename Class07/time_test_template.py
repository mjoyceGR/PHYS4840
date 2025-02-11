#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import time
import numpy as np
import sys
import pandas as pd

### where is this file located for you?
### be careful with file organization!!
filename = '../Class06/NGC6341.dat'

###################################################
#
# testing np.loadtxt()
#
###################################################
"""
put the action you want to time between the
star and end commands
"""

start_numpy = time.perf_counter()


blue, green, red, probability = np.loadtxt(filename,\
                 usecols=(8, 14, 26, 32), unpack=True)
print("len(green): ", len(green))


end_numpy  = time.perf_counter()

print('Time to run loadtxt version: ', end_numpy-start_numpy, ' seconds')



###################################################
#
# testing custom parser
#
###################################################
start_parser = ...

"""
insert the custom parsing code
"""

end_parser  = ...

print('Time to run custom parser version: ', end_parser-start_parser, ' seconds')


###################################################
#
# testing pandas
#
###################################################
start_pandas = ...

"""
insert the pandas parsing code
"""

end_pandas  = ...

print('Time to run pandas version: ', end_pandas-start_pandas, ' seconds')