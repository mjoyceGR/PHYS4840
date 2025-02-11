#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################

from math import sqrt

x = 1.0
y = 1.0 + (1e-14)*sqrt(2)

answer_1 = 1e14*(y-x)
answer_2 = sqrt(2)

print("answer1: ", answer_1 )
print("answer2: ", answer_2 ) 