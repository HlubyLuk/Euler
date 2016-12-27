from problem.Problem import Problem
from math import factorial


class Problem34(Problem):
    """
    Digit factorials
    Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """

    def solve(self):
        return sum(
            [x for x in range(
                3, 7 * factorial(9), 1) if x == sum(
                    map(
                        lambda y: factorial(
                            int(y)), str(x)))])
