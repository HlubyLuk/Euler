from problem.Problem import Problem
from math import pow

START, STOP, STEP = 2, 1000000, 1
POW_INDEX = 5


class Problem30(Problem):
    """
    Digit fifth powers
    Problem 30

    Surprisingly there are only three numbers that can be written
    as the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written
    as the sum of fifth powers of their digits.
    """

    def decomposition(self, number):
        return number == sum([pow(int(val), POW_INDEX) for i, val in enumerate(
            str(number))])

    def solve(self):
        return sum(i for i in range(START, STOP, STEP) if self.decomposition(i))
