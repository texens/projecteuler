#!/usr/bin/python

# Question :
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# (1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4 
# 1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

import math

def func(x):
    a = pow(x*(x+1)/2, 2)
    b = x*(x+1)*(2*x+1)/6
    return a - b

print func(100)
