# coding=utf-8
from problem.Problem import Problem

ALL_DIGITS = "123456789"


class Problem32(Problem):
    """
    Pandigital products
    Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.
    """

    def solve(self):
        return sum(
            set(
                [i * j for i in range(
                    1, 10001) for j in range(
                        1, 1001) if self.pandigital_check(i, j)]))

    def pandigital_check(self, i, j):
        tmp = ''.join(sorted('{}{}{}'.format(i, j, i * j)))
        return ALL_DIGITS == tmp
