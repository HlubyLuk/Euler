# coding=utf-8
from collections import defaultdict
from problem.Problem import Problem

STOP = 1000000


class Problem14(Problem):
    """
    Longest Collatz sequence
    Problem 14

    The following iterative sequence is defined for
    the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13,
    we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    def solve(self):
        ret = defaultdict(int)
        for i in range(2, STOP):
            self.count(i, ret)
        return sorted(ret.items(), key=lambda x: x[1]).pop()[0]

    def count(self, number, ret):
        tmp = number
        count = 0
        while number not in ret and number > 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = 3 * number + 1
            count += 1
        rest = ret.get(number, 1)
        ret.update({tmp: count + rest})
        pass

#         def solve(self):
#             tmp = set()
#             for i in range(1, STOP):
#                 tmp.add(Holder(i, self.collatz(i)))
#             ret = Holder(0, 0)
#             for i in tmp:
#                 if ret.count < i.count:
#                     ret = i
#             print "fin {}".format(ret)
#
#         def collatz(self, number):
#             if number == 1:
#                 return 1
#             if number % 2 == 0:
#                 var = int(number / 2)
#             else:
#                 var = int(3 * number) + 1
#             if var < 1:
#                 print var
#                 raise ValueError("Negative output")
#             return 1 + self.collatz(var)
#
#
# class Holder:
#     count = None
#     i = None
#
#     def __init__(self, i, count):
#         self.i = i
#         self.count = count
#
#     def __str__(self):
#         return "i = {}, count {}".format(self.i, self.count)
