#!/usr/bin/python

# Question :
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


primes = []
digits = []

def func(x):
    global primes
    global digits

    i = 2

    while len(digits) < x:
        if i in digits:
            while i in digits:
                t = digits.index(i)
                digits[t] = digits[t] + primes[t]
        else:
            primes.append(i)
            digits.append(2*i)

        i += 1

func(10001)
print primes[10000]
