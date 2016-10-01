#coding=utf-8
from problem.Problem import Problem

STOP = 1000
START = -STOP

class Problem27(Problem):
    """
    Quadratic primes
    Problem 27

    Euler discovered the remarkable quadratic formula:

    n^2+n+41

    It turns out that the formula will produce 40 primes for the consecutive
    integer values 0≤n≤39.
    However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41,
    and certainly when n=41,41^2+41+41 is clearly divisible by 41.

    The incredible formula n^2−79n+1601 was discovered, which produces 80 primes
    for the consecutive values 0≤n≤79.
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n^2+an+b, where |a|<1000 and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4

    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n=0.
    """

    def solve(self):
        n, a, b = 0, 0, 0
        for i in range(START, STOP, 1):
            for j in range(START, STOP + 1, 1):
                tmp = self.formula(i, j)
                if n < tmp:
                    n = tmp
                    a = i
                    b = j
        return a * b


    def formula(self, a, b):
        n = 0
        while True:
            tmp = n ** 2 + n * a + b
            if tmp < 0 or not self.is_prime(tmp):
                return n
            n += 1
