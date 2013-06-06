#!/usr/bin/python

# Project Euler Problem 2

a = 2
b = 8
sum = a + b

while True:
    temp = b
    b = a + 4*b
    a = temp

    if b < 4000000:
        sum = sum + b
    else:
        print sum
        break
