#!/usr/bin/python

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
to_resolve = 600851475143
ret = set()
i = 1
while to_resolve != 1:
    i += 1
    if to_resolve % i == 0:
        to_resolve /= i
        ret.add(i)
        i = 1
print sorted(ret)[len(ret) - 1]
