#!/usr/bin/env python3
"""
https://projecteuler.net/about
"""
from time import time

from problem.Problem1 import Problem1
from problem.Problem2 import Problem2
from problem.Problem3 import Problem3
from problem.Problem4 import Problem4
from problem.Problem5 import Problem5
from problem.Problem6 import Problem6
from problem.Problem7 import Problem7
from problem.Problem8 import Problem8
from problem.Problem9 import Problem9
from problem.Problem10 import Problem10
from problem.Problem11 import Problem11
from problem.Problem12 import Problem12
from problem.Problem13 import Problem13
from problem.Problem14 import Problem14
from problem.Problem15 import Problem15
from problem.Problem16 import Problem16
from problem.Problem17 import Problem17
from problem.Problem18 import Problem18
from problem.Problem19 import Problem19
from problem.Problem20 import Problem20
from problem.Problem21 import Problem21
from problem.Problem22 import Problem22
from problem.Problem23 import Problem23
from problem.Problem24 import Problem24
from problem.Problem25 import Problem25
from problem.Problem26 import Problem26
from problem.Problem27 import Problem27
from problem.Problem28 import Problem28
from problem.Problem29 import Problem29
from problem.Problem30 import Problem30
from problem.Problem31 import Problem31
from problem.Problem32 import Problem32
from problem.Problem33 import Problem33
from problem.Problem34 import Problem34
from problem.Problem35 import Problem35

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
    print(Problem17().solve())
    print(Problem18().solve())
    print(Problem19().solve())
    print(Problem20().solve())
    print(Problem21().solve())
    print(Problem22().solve())
    print(Problem23().solve())
    print(Problem24().solve())
    print(Problem25().solve())
    print(Problem26().solve())
    print(Problem27().solve())
    print(Problem28().solve())
    print(Problem29().solve())
    print(Problem30().solve())
    print(Problem31().solve())
    print(Problem32().solve())
    print(Problem33().solve())
    print(Problem34().solve())
    print(Problem35().solve())
    time_diff = time() - start
    print("finish {}:{} orig ({})".format(
        int(time_diff // 60), int(time_diff % 60), time_diff))
