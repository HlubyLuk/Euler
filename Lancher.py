#!/usr/bin/python
# coding=utf-8
"""
https://projecteuler.net/about
"""
from time import time

from problem.Problem1 import Problem1
from problem.Problem10 import Problem10
from problem.Problem11 import Problem11
from problem.Problem12 import Problem12
from problem.Problem13 import Problem13
from problem.Problem14 import Problem14
from problem.Problem15 import Problem15
from problem.Problem2 import Problem2
from problem.Problem3 import Problem3
from problem.Problem4 import Problem4
from problem.Problem5 import Problem5
from problem.Problem6 import Problem6
from problem.Problem7 import Problem7
from problem.Problem8 import Problem8
from problem.Problem9 import Problem9

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
    Problem11().solve()
    Problem12().solve()
    Problem13().solve()
    print (Problem14().solve())
    print (Problem15().solve())

    print "finish {}".format(time() - start)
