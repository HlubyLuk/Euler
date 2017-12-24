# -*- coding:utf-8 -*-
from problem.Problem import Problem


class Problem38(Problem):
    """
    Pandigital multiples
    Problem 38
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """


    def solve(self):
        return filter(lambda x: x[0], [self.pandigital_multiples(x) for x in
            range(100, 10000)])[-1][1]
        pass


    def pandigital_multiples(self, a):
        tmp = ""
        for x in range(1, 10):
            tmp = tmp + str(a * x)
            if self.pandigital_number(tmp):
                return (x > 1, tmp)
                pass
            pass
        return (False, tmp)
        pass
    pass
