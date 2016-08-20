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
from problem.Problem16 import Problem16
from problem.Problem18 import Problem18
from problem.Problem19 import Problem19
from problem.Problem2 import Problem2
from problem.Problem20 import Problem20
from problem.Problem21 import Problem21
from problem.Problem22 import Problem22
from problem.Problem3 import Problem3
from problem.Problem4 import Problem4
from problem.Problem5 import Problem5
from problem.Problem6 import Problem6
from problem.Problem7 import Problem7
from problem.Problem8 import Problem8
from problem.Problem9 import Problem9

if __name__ == '__main__':
    start = time()

    print(Problem1().solve())
    print(Problem2().solve())
    print(Problem3().solve())
    print(Problem4().solve())
    print(Problem5().solve())
    print(Problem6().solve())
    print(Problem7().solve())
    print(Problem8().solve())
    print(Problem9().solve())
    print(Problem10().solve())
    print(Problem11().solve())
    print(Problem12().solve())
    print(Problem13().solve())
    print(Problem14().solve())
    print(Problem15().solve())
    print(Problem16().solve())
    print(Problem18().solve())
    print(Problem19().solve())
    print(Problem20().solve())
    print(Problem21().solve())
    print(Problem22().solve())

    print("finish {}".format(time() - start))
