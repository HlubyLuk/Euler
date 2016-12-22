from problem.Problem import Problem
from functools import reduce

class Problem35(Problem):
    """
    Circular primes
    Problem 35

    The number, 197, is called a circular prime because all rotations of
    the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
    """

    def solve( self ):
        return len([x for x in range(1000000) if all(self.is_prime(int(str(x)[y:] + str(x)[:y])) for y in range(len(str(x))))])
