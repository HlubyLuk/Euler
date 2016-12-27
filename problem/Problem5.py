from problem.Problem import Problem
from collections import Counter


class Problem5(Problem):
    """
    Smallest multiple
    Problem 5

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """

    def solve(self):
        prime_dividers = [self.prime_dividers(i) for i in range(1, 21)]
        tmp = list([0] * 21)
        for i in prime_dividers:
            d = Counter(i).items()
            for i, val in enumerate(d):
                index = val[0]
                y = index ** val[1]
                if tmp[index] < y:
                    tmp[index] = y
        x = 1
        for i in tmp:
            if i > 0:
                x *= i
        return x
