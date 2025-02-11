#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import timeit
import numpy as np

setup_code = """
nums = list(range(100000))
"""
list_comp_time = timeit.timeit("[x**2 for x in nums]", setup=setup_code, number=100)
map_time = timeit.timeit("list(map(lambda x: x**2, nums))", setup=setup_code, number=100)

print("List comprehension time: ","%.5f"%list_comp_time ," seconds")
print("Map function time: ",      "%.5f"%map_time       ," seconds")
print("")

#-----------------------------------------

setup_code = "nums_list = list(range(100000)); nums_set = set(nums_list)"
list_time = timeit.timeit("99999 in nums_list", setup=setup_code, number=10000)
set_time = timeit.timeit("99999 in nums_set", setup=setup_code, number=10000)

print(f"List membership test time: ", "%.5f"%list_time ," seconds")
print(f"Set membership test time: ",  "%.5f"%set_time,  " seconds")
print("")

#-----------------------------------------
########################
#
# In-class Exercise!!
#
#########################

setup_code = "import numpy as np; my_array = np.arange(100000)"

#### compare the speed of 
# 		sum([x**2 for x in range(100000)])
#               vs
#       np.sum(my_array**2)
##
## for 100 iterations, then 1000

loop_time = timeit.timeit("", setup=..., number=...)
numpy_time = timeit.timeit("", ...)

print(...)
print(...)