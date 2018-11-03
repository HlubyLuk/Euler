# -*- coding: utf-8 -*-

'''
Created on Nov 2, 2018

@author: HlubyLuk
'''
from problem.Problem import Problem
import math


STOP = 7


class Problem40(Problem):
    """
    Champernowne's constant
    Problem 40 
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following
    expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """


    def solve(self):
        seq = "".join([str(x) for x in xrange(1, int(math.pow(10, 7)))])
        return reduce(lambda x, y: x * y, [int(seq[int(math.pow(10, p) - 1)]) for p in xrange(1, STOP)])
