import math

from problem.Problem import Problem


class Problem16(Problem):
    """
    Power digit sum
    Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """

    def solve(self):
        # python2
        # tmp = str(long(math.pow(2, 1000)))
        # ret = int(0)
        # for i, val in enumerate(tmp):
        #     ret += int(val)
        # return ret

        # python3
        return sum(list(map(int, list(str(int(math.pow(2, 1000)))))))
