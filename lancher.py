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
    start = time()

    Problem1().solve()
    Problem2().solve()
    Problem3().solve()
    Problem4().solve()
    Problem5().solve()
    Problem6().solve()
    Problem7().solve()
    Problem8().solve()
    Problem9().solve()
    Problem10().solve()


    print "finis {}".format(time() - start)
