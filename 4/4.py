#!/usr/bin/python

# Question : 
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the 
# product of two 3-digit numbers.


import math

def is_palindrome(x):
    digits = []
    while x:
        digits.append(int(x%10))
        x = math.floor(int(x/10))

    for i in range(int(math.floor(len(digits)/2))):
        if digits[i] != digits[len(digits) - i - 1]:
            return False

    return True

def main():
    maxp = 0
    max_i = 999
    max_j = 999

    for i in reversed(range(999)):
        for j in reversed(range(999)):
            if is_palindrome(i*j):
                if i*j > maxp:
                    max_i, max_j, maxp = i, j, i*j

    print max_i, max_j, maxp

main()
