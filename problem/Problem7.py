#!/usr/bin/python
# coding=utf-8
from Problem import Problem


class Problem7(Problem):
    """
    10001st prime
    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """

    # ToDo optimization
    def solve(self):
        ret = [2]
        a = 1
        b = False
        while len(ret) < 10001:
            a += 1
            for z in ret:
                if a % z == 0:
                    b = False
                    break
                b = True

            if b:
                ret.append(a)
                b = False

        print ret[len(ret) - 1]


