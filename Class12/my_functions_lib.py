#!/usr/bin/python3.8
import numpy as np
from math import tanh

###################################
#
# New functions for Class 12 2/27/25
#
###################################
def f(x):
	fx = 1.0 + 0.5*tanh(2.0*x)
	return fx

def f_with_numpy(x):
	## same as the above, but using tanh from numpy
	## rather than from math --- are they the same?
	fx = 1.0 + 0.5*np.tanh(2.0*x)
	return fx

def df_dx_analytical(x):
	dfdx = 1.0/(np.cosh(2.0*x)**2.0)
	return dfdx


###################################
def my_function(vector):
	a = vector[0]
	b = vector[1]
	c = vector[2]

	answer = np.linalg.norm(vector)

	return answer


vector = [10,11,12]
def normalize_vector(vector):
	answer = np.linalg.norm(vector)
	return answer, vector

# print("output of my function: ",\
# 	  normalize_vector(vector) )


# print( type(normalize_vector(vector)) )