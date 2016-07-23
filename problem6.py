#!/usr/bin/python
# coding=utf-8
"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
start = time.time()
ret = sum( range( 1, 101 ) ) ** 2 - sum( i ** 2 for i in range( 1, 101 ))
print ret
print time.time() - start
