# coding=utf-8
from problem.Problem import Problem


class KnapsackSolver():
    """
    A knapsack is a bin-packing problem, in which the goal is to maximize
    the total value of items in (typically) a single bin. In this documentation
    you'll learn how to use or-tools to solve knapsack problems.
    """

    result = 0
    __target = 0
    __values = []

    def __init__(self, target, values):
        """
        Constructor
        """
        self.__target = target
        self.__values = values

    def solve(self):
        """
        Solve knapsack problem.
        """
        ways = [1] + [0] * self.__target
        for value in self.__values:
            for i in range(value, self.__target + 1, 1):
                ways[i] += ways[i - value]
        self.result = ways[self.__target]


class Problem31(Problem):
    """
    Coin sums
    Problem 31

    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?
    """

    def solve(self):
        target = 200
        values = [1, 2, 5, 10, 20, 50, 100, 200]
        knapsack = KnapsackSolver(target, values)
        knapsack.solve()
        return knapsack.result
