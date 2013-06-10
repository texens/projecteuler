#!/usr/bin/python

# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime(n):
    p = 2
    while p < n:
        if n % p == 0:
            n = n/p
            print p, n
        else:
            p += 1

largest_prime(600851475143)
