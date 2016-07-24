#!/usr/bin/python
# coding=utf-8
"""
https://projecteuler.net/about
"""
from time import time

from problem.problem1 import Problem1
from problem.problem10 import Problem10
from problem.problem2 import Problem2
from problem.problem3 import Problem3
from problem.problem4 import Problem4
from problem.problem5 import Problem5
from problem.problem6 import Problem6
from problem.problem7 import Problem7
from problem.problem8 import Problem8
from problem.problem9 import Problem9

if __name__ == '__main__':
    i = 0

    start = time()
    Problem1().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem2().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem3().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem4().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem5().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem6().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem7().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem8().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem9().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)

    start = time()
    Problem10().solve()
    i += 1
    print "problem {} {}".format(i, time() - start)
