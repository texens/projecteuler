#!/usr/bin/python

# Project Euler Problem 3

# Find largest prim factor of 600851475143 

def largest_prime(n):
    p = 2
    while p < n:
        if n % p == 0:
            n = n/p
            print p, n
        else:
            p += 1

largest_prime(600851475143)
