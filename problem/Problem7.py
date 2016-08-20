#!/usr/bin/python
# coding=utf-8
from problem.Problem import Problem


class Problem7(Problem):
    """
    10001st prime
    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """

    def solve(self):
        ret = []
        i = 1
        while len(ret) < 10001:
            if self.is_prime(i):
                ret.append(i)
            i += 1
        return ret[10000]
