#!/usr/bin/python
# coding=utf-8
"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time


def compute(number):
    if number == 2:
        return True

    if number % 2 == 0 or number < 2:
        return False

    for i in range(3, int(number ** .5), 2):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    ret = []
    for number in range(1, 2000000):
        if compute(number):
            ret.append(number)
    print sum(ret)
